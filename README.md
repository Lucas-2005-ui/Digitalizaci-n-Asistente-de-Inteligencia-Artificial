# 🚀 Asistente de Inteligencia Artificial

## 👥 Integrantes del Grupo
* **Alberto 1** (@usuario_github)
* **Alex 2** (@usuario_github)
* **Mariano 3** (@usuario_github)
* **Max 4** (@usuario_github)
* **Lucas 5** (@usuario_github)

## 📝 Descripción del Proyecto
Este es un asistente de inteligencia artificial diseñado para ayudar a las empresas pequeñas (Pymes) a digitalizar sus procesos y resolver dudas técnicas.

## 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python 3.10+
* **IA Local:** Ollama
* **Herramientas:** GitHub Desktop, Visual Studio Code

## 📋 Requisitos del Sistema
Para que el proyecto funcione en tu máquina (especialmente en la de pruebas de Mariano), necesitas:
1. **Ollama instalado:** Es el motor que corre los modelos de lenguaje localmente.
2. **Python 3.10 o superior:** Asegúrate de tenerlo en el PATH de tu sistema.
3. **Librería de Ollama para Python:** Se instala mediante el gestor de paquetes pip.
4. **Espacio en disco:** Suficiente para descargar el modelo (unos 4GB-8GB dependiendo del modelo elegido).

## 📂 Estructura del Repositorio
* `/documentacion`: Contiene el informe final, diagramas e investigación teórica.
* `/src`: Carpeta con todos los archivos fuente y lógica del agente.
* `/data`: (Nueva) Espacio para los documentos (PDF, DOC) que el asistente deberá procesar.
* `/assets`: Imágenes y recursos utilizados.

## ⚠️ Límites y Alcance (Tarea de Max)
Para evitar que la IA se desvíe de su función, hemos definido estos límites:
* El asistente **solo** responderá preguntas relacionadas con la digitalización de Pymes.
* No se utilizará para generar código externo o tareas que no sean de asistencia empresarial.
* Si una petición se sale de estos límites, el sistema mostrará un mensaje de cancelación.

## ⚙️ Cómo ejecutar el proyecto
1. **Instalar Ollama** desde su página oficial.
2. **Descargar el modelo** (por ejemplo: `ollama run llama3`).
3. **Instalar dependencias:** Ejecuta `pip install ollama` en tu terminal.
4. **Lanzar el script:** Ejecuta `python src/principal.py` (o el nombre del archivo principal).
