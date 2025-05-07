import json

def translate_keys(data):
    # Diccionario de traducción de claves al inglés en formato camelCase
    translation_map = {
        "Nombre": "name",
        "Cuando": "when",
        "Acción": "action",
        "El niño/a": "theChild",
        "En": "in",
        "Edad": "age",
        "Etapa": "stage",
        "Destinatario": "recipient",
        "Categoría": "category",
        "Título": "title",
        "Descripción": "description",
        "Indicador": "indicator",
        "Adaptación": "adaptation",
        "Para familia": "forFamily",
        "Para colegio": "forSchool",
        "Material": "material"
    }

    transformed_data = {}
    for key, value in data.items():
        new_key = translation_map.get(key, key)
        transformed_data[new_key] = value

    return transformed_data

def process_json(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error al leer el archivo JSON: {e}")
        return

    if isinstance(data, list):
        transformed_data = [translate_keys(item) for item in data]
    else:
        transformed_data = translate_keys(data)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(transformed_data, f, ensure_ascii=False, indent=4)
        print(f"Archivo transformado guardado en: {output_file}")
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

# Uso del script
input_json_file = r'C:\Users\adrian.ramirez\Downloads\sessions.json'  # Ruta al archivo JSON de entrada
output_json_file = r'C:\Users\adrian.ramirez\Downloads\sessions-transformed.json'  # Ruta al archivo JSON de salida

process_json(input_json_file, output_json_file)

"""
Uso:
1. Modifica las rutas de entrada y salida de los archivos JSON en las variables 'input_json_file' y 'output_json_file'.
2. Ejecuta el script desde la terminal o símbolo del sistema con el comando:
   python sessions.py
"""
