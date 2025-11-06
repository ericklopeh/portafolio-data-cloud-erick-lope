import os
import random
import json
import nltk
import numpy as np
from dotenv import load_dotenv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
from dotenv import load_dotenv

# --- Gemini ---
import google.generativeai as genai

# Descarga recursos NLTK si es la primera ejecución
nltk.download('punkt', quiet=True)

BASE_DIR = Path(__file__).resolve().parent
env_ok = load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini = genai.GenerativeModel(GEMINI_MODEL)
else:
    gemini = None  # seguirá funcionando solo con intents

# ====== Carga de intents locales ======
with open("data/intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

patterns, tags, responses = [], [], []
for intent in intents["intents"]:
    for p in intent["patterns"]:
        patterns.append(p)
        tags.append(intent["tag"])
        # respuesta representativa por patrón (para indexar)
        responses.append(random.choice(intent["responses"]))

# ====== Vectorización ======
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(patterns).toarray()

SIM_THRESHOLD = 0.35  # si la similitud es menor, preguntamos a Gemini

def reply_from_intents(user_input: str) -> tuple[str, float]:
    """Devuelve (respuesta, score_similitud) usando intents locales."""
    user_vec = vectorizer.transform([user_input]).toarray()
    sim = cosine_similarity(user_vec, vectors)
    idx = sim.argmax()
    score = float(sim[0, idx])
    # encuentra la respuesta por el tag ganador (más robusto que 'responses[idx]')
    tag = tags[idx]
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"]), score
    return "No tengo una respuesta para eso.", score

def reply_from_gemini(user_input: str) -> str:
    """Llama a Gemini (si hay API key)."""
    if not gemini:
        return "No entendí bien tu pregunta. (Activa GEMINI_API_KEY para respuestas avanzadas)"
    try:
        system_prompt = (
            "Eres un asistente breve y amable. Responde en español con 1–3 oraciones. "
            "Si el usuario pide código, da un snippet corto. Evita información sensible."
        )
        
        response = gemini.generate_content(f"{system_prompt}\n\nUsuario: {user_input}")
        text = response.text.strip() if hasattr(response, "text") else ""
        return text or "No tengo una respuesta en este momento."
    except Exception as e:
        return f"(Gemini no disponible: {e})"

def get_response(user_input: str) -> str:
    # 1) intenta con intents locales
    local_resp, score = reply_from_intents(user_input)
    if score >= SIM_THRESHOLD:
        return local_resp
    # 2) fallback con Gemini
    return reply_from_gemini(user_input)

# ====== CLI ======
print("🤖 Chatbot AI híbrido – Erick Lope")
print("• Intents locales + Gemini como fallback")
print("• Escribe 'salir' para terminar\n")

while True:
    user_input = input("Tú: ").strip().lower()
    if user_input in {"salir", "exit", "adios", "adiós"}:
        print("Bot: ¡Hasta luego! 👋")
        break
    print("Bot:", get_response(user_input))