from file_manage import get_tasks, save_tasks
from transformate import json_to_str, str_to_tasks, tasks_to_json, json_to_tasks

def read_tasks():
    data = get_tasks()
    tasks_str = json_to_str(data)
    tasks = str_to_tasks(tasks_str)
    return [task.__str__() for task in tasks]

def write_tasks(task):
    tasks = read_tasks()
    tasks.append(task)
    save_tasks(tasks_to_json(tasks))
    return "Task added successfully"

def read_tasks_TODO():
    data = get_tasks()
    tasks = json_to_tasks(data)
    todo_tasks = [task for task in tasks if task.status.name == "TODO"]
    return [task.__str__() for task in todo_tasks]

def read_tasks_IN_PROGRESS():
    data = get_tasks()
    tasks = json_to_tasks(data)
    in_progress_tasks = [task for task in tasks if task.status.name == "IN_PROGRESS"]
    return [task.__str__() for task in in_progress_tasks]

def read_tasks_DONE():
    data = get_tasks()
    tasks = json_to_tasks(data)
    done_tasks = [task for task in tasks if task.status.name == "DONE"]
    return [task.__str__() for task in done_tasks]

def chanche_task_status(id, new_status):
    tasks = json_to_tasks(get_tasks())
    for task in tasks:
        if task.id == id:
            task.status = new_status
    save_tasks(tasks_to_json(tasks))
    return "Task status updated"