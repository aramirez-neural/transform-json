import json

def translate_keys(data):
    # Diccionario de traducción de claves
    translation_map = {
        "Etapa": "stage",
        "Situación": "situation",
        "Realidad": "reality",
        "Mejora": "improvement",
        "Acciones": "actions",
        "Responsable": "responsible",
        "Fecha": "date"
    }

    transformed_data = {}
    for key, value in data.items():
        new_key = translation_map.get(key, key).lower()
        
        # Crear array cuando la clave es "actions"
        if new_key == "actions" and value:
            transformed_data[new_key] = [value]
        else:
            transformed_data[new_key] = value

    return transformed_data

def process_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if isinstance(data, list):
        transformed_data = [translate_keys(item) for item in data]
    else:
        transformed_data = translate_keys(data)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(transformed_data, f, ensure_ascii=False, indent=4)

# Uso del script
input_json_file = r'C:\Users\adrian.ramirez\Downloads\protocols.json'  # Ruta al archivo JSON de entrada
output_json_file = r'C:\Users\adrian.ramirez\Downloads\protocols-transformed.json'  # Ruta al archivo JSON de salida
process_json(input_json_file, output_json_file)

"""
Uso:
1. Modifica las rutas de entrada y salida de los archivos JSON en las variables 'input_json_file' y 'output_json_file'.
2. Ejecuta el script desde la terminal o símbolo del sistema con el comando:
   python index.py

"""
