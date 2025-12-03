from file_manage import get_tasks, save_tasks
from transformate import json_to_str, str_to_tasks, tasks_to_json

def read_tasks():
    data = get_tasks()
    tasks_str = json_to_str(data)
    tasks = str_to_tasks(tasks_str)
    return tasks

def write_tasks(task):
    tasks = read_tasks()
    tasks.append(task)
    tasks_json = tasks_to_json(tasks)
    save_tasks(tasks_json)
    return save_tasks

from task import Task, Status
task = Task(1, "Buy groceries", Status.TODO)
print(write_tasks(task))