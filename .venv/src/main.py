#Esta clase maneja el flujo de la aplicación

import json

obj = '{"name": "Task Tracker","version": "1.0.0","description": "Aplicación para gestionar tareas"}'

with open('data.json', 'w') as file:
    json_d = json.dump(obj, file)

with open('data.json', 'r') as file:
    python_obj = json.load(file)
print(python_obj)