import ollama
import os

# 1. Configuración
MODELO = 'llama3.2'
ROL_SISTEMA = "Eres un consultor experto en digitalización para Pymes."
CARPETA_DATOS = "src/data" # Aquí es donde Python buscará tus archivos

def leer_archivos_locales():
    contenido_total = ""
    # Python revisa qué hay en la carpeta 'src/data'
    for archivo in os.listdir(CARPETA_DATOS):
        if archivo.endswith(".txt"): # Solo leemos archivos de texto
            ruta = os.path.join(CARPETA_DATOS, archivo)
            with open(ruta, "r", encoding="utf-8") as f:
                contenido_total += f"\n--- Contenido de {archivo} ---\n"
                contenido_total += f.read()
    return contenido_total

def chat_con_ia(pregunta_usuario, contexto_archivos):
    # Aquí creamos la "cápsula" de información que se envía a Ollama
    prompt_final = f"""
    Usa la siguiente información de mis archivos locales para responder:
    {contexto_archivos}
    
    Pregunta del usuario: {pregunta_usuario}
    """
    
    respuesta = ollama.chat(model=MODELO, messages=[
        {'role': 'system', 'content': ROL_SISTEMA},
        {'role': 'user', 'content': prompt_final},
    ])
    return respuesta['message']['content']

# 3. Ejecución de la prueba
if __name__ == "__main__":
    print("Buscando información en tus archivos...")
    contexto = leer_archivos_locales()
    
    pregunta = input("Haz tu pregunta a la IA: ") # Esto permite que escribas en la terminal
    
    resultado = chat_con_ia(pregunta, contexto)
    print("\nRESPUESTA DE LA IA:")
    print(resultado)