# 📚 Guía Técnica para el Equipo (Fase 2)

Este es el resumen de herramientas que hemos validado y que debéis usar para vuestras tareas:

### 🛠️ Para Alex (Gestión de Datos y Memoria)
* **PyPDF2**: Úsala para extraer texto de los PDF de las Pymes.
* **ChromaDB**: Investiga esta librería para la "Memoria" de la IA (para que recuerde nombres).

### 🛡️ Para Max (Filtros y Límites)
* **System Prompt**: Ya he configurado la base en `src/asistente_pyme.py`. Debes mejorar el texto para que la IA no se salga de su rol.
* **Pydantic**: Investiga cómo usar esto para que el programa dé error si el usuario escribe algo que no sea texto.

### ⚙️ Estado del Motor (Validado por Lucas)
* **Modelo:** Llama 3.2 (Ollama).
* **Lenguaje:** Python 3.10+.