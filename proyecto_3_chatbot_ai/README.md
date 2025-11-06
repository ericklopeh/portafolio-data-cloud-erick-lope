# 🤖 Proyecto 3 – Chatbot IA Híbrido con Gemini

### 🧠 Descripción
Este proyecto implementa un **chatbot inteligente híbrido** desarrollado en **Python**, que combina:
- **Respuestas locales** basadas en similitud semántica (TF-IDF + cosine similarity).
- **Integración con la API de Gemini (IA de Google)** para respuestas avanzadas.

El sistema selecciona automáticamente la mejor opción: primero intenta responder con conocimiento local y, si no encuentra coincidencias relevantes, consulta a Gemini.

---

### 🎯 Objetivos
- Desarrollar un chatbot funcional que procese entradas de texto en lenguaje natural.  
- Incorporar una **IA externa (Gemini 1.5 Flash)** como respaldo de respuestas.  
- Implementar un flujo **local → IA** para reducir consumo de API.  
- Preparar la estructura para futuras mejoras (memoria contextual, interfaz web, etc.).

---

### 🧰 Tecnologías utilizadas
- Python 3.11  
- scikit-learn (TF-IDF vectorizer, cosine_similarity)  
- Google Generative AI SDK  
- python-dotenv  
- Matplotlib (opcional para visualizar patrones de intentos)  
- Visual Studio Code  

---

### 🗂️ Estructura del proyecto
proyecto_3_chatbot_ai/
│
├── chatbot.py
├── .env
├── requirements.txt
└── README.md

yaml
Copiar código

---

### ⚙️ Ejecución

1️⃣ **Crear entorno virtual**
```bash
python -m venv venv
venv\Scripts\activate
2️⃣ Instalar dependencias

bash
Copiar código
pip install -r requirements.txt
3️⃣ Configurar la clave Gemini
En el archivo .env coloca tu clave de Google AI Studio:

env
Copiar código
GEMINI_API_KEY=tu_clave_aqui
GEMINI_MODEL=gemini-1.5-flash
4️⃣ Ejecutar el chatbot

bash
Copiar código
python chatbot.py
5️⃣ Conversar

makefile
Copiar código
Tú: Hola
Bot: ¡Hola! ¿Cómo estás?
Tú: ¿Qué es Oracle Cloud?
Bot: (Respuesta generada por Gemini)
🧩 Resultados
Respuestas híbridas → inteligencia local + IA avanzada.

Modo de fall-back inteligente con detección de baja confianza.

Integración lista para despliegue en entornos cloud (OCI, Render, Railway o PythonAnywhere).

👨‍💻 Autor
Erick Lope
📧 ericklopeh@icloud.com
