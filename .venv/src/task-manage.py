#Esta clase maneja las operaciones de la clase task
from task import Task


#TODO: Metodo para crear tarea
def create_task(id, description, status):
    new_task = Task(id=id, _description=description, _status=status)
    return new_task

#TODO: Metodo para eliminar tarea
def delete_task(tasks, task_id):
    tasks = [task for task in tasks if task.id != task_id]
    return tasks

#TODO: Metodo para actualizar description
def update_task_description(task, new_description):
    task.description = new_description
    return task

#TODO: Metodo para actualizar status
def update_task_status(task, new_status):
    task.status = new_status
    return task

#TODO: Metodo para listar tareas por status
def list_tasks_by_status(tasks, status):
    filtered_tasks = [task for task in tasks if task.status == status]
    return filtered_tasks