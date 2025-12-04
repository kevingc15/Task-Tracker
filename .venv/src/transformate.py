import json
from task import Task, Status

#TODO: Transformar json a lista de tasks
def json_to_str(json_data):
    return json.loads(json_data)

def str_to_tasks(tasks_str):
    tasks = []
    for task_dict in tasks_str:
        task = Task(
            id=task_dict['id'],
            _description=task_dict['description'],
            _status=Status[task_dict["status"]]
        )
        tasks.append(task)
    return tasks

def tasks_to_json(tasks):
    tasks_list = [task.to_dict() for task in tasks]
    return json.dumps(tasks_list)

def json_to_tasks(json_data):
    tasks_str = json_to_str(json_data)
    return str_to_tasks(tasks_str)
