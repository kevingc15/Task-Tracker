#Esta clase maneja las operaciones de archivos

#Metodo para leer datos de archivo
def get_tasks():
    with open("data.json", "r") as file:
        data = file.read()
    file.close()
    return data

#Metodo para guardar datos en archivo
def save_tasks(data):
    with open("data.json", "w") as file:
        file.write(data)
    file.close()
    return "Data saved successfully"
