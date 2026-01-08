import ollama

# 1. Definimos el "Cerebro" (Modelo)
MODELO = 'llama3.2'

# 2. Definimos el "Rol" (Esto ayuda a Max con los límites)
ROL_SISTEMA = "Eres un consultor experto en digitalización para Pymes."

def chat_con_ia(pregunta_usuario):
    # Esta función envía la pregunta a Ollama
    respuesta = ollama.chat(model=MODELO, messages=[
        {'role': 'system', 'content': ROL_SISTEMA},
        {'role': 'user', 'content': pregunta_usuario},
    ])
    return respuesta['message']['content']

# 3. Prueba de ejecución
if __name__ == "__main__":
    resultado = chat_con_ia("¿Cómo puede una tienda pequeña usar redes sociales?")
    print("RESPUESTA DE LA IA:")
    print(resultado)