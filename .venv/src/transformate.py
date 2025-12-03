import json
from task import Task

#TODO: Transformar json a lista de tasks
def json_to_str(json_data):
    tasks = json.loads(json_data)
    return tasks

def str_to_tasks(tasks_str):
    tasks = []
    for task_dict in tasks_str:
        task = Task(
            id=task_dict['id'],
            _description=task_dict['description'],
            _status=task_dict['status']
        )
        tasks.append(task)
    return tasks
