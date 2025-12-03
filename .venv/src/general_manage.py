from file_manage import get_tasks, save_tasks
from transformate import json_to_str, str_to_tasks

def read_tasks():
    data = get_tasks()
    tasks_str = json_to_str(data)
    tasks = str_to_tasks(tasks_str)
    return tasks

def write_tasks(task):
    tasks = read_tasks()
    tasks.append(task)
    data = json.dumps(tasks)
    save_tasks(data)
    return "Task saved successfully"

from task import Task
print(read_tasks())