import json
import os

file_path = "tasks.json"

def greet():
    import time
    print(f"Hi! I am your task tracker\n")

def data_id(file_path):
    if not os.path.exists(file_path):
        return 1

    with open(file_path, "r") as f:
        try:
            data = json.load(f)
            if isinstance(data, dict):
                data = [data]  # convert to list if needed
        except json.JSONDecodeError:
            data = []

    return max((task["id"] for task in data), default=0) + 1

def data_status():
    if("add" in task):
        return "to-do"
    elif("in-progress" in task or "update" in task):
        return "in-progress"
    elif("done" in task):
        return "done"

def add(data_task):
    if not os.path.exists(file_path):
        data_task["id"] = 1
        with open(file_path, "w") as f:
            json.dump([data_task], f, indent=4)
    else:
        with open(file_path, "r") as f:
            try:
                tasks = json.load(f)
                if isinstance(tasks, dict):
                    tasks = [tasks]
            except json.JSONDecodeError:
                tasks = []

        data_task["id"] = data_id(file_path)

        tasks.append(data_task)

        with open(file_path, "w") as f:
            json.dump(tasks, f, indent=4)

def delete(name):
    if(os.path.exists(file_path)):
        with open(file_path, "r") as f:
            try:
                tasks = json.load(f)
                if isinstance(tasks, dict):
                    tasks = [tasks]
            except json.JSONDecodeError:
                tasks = []
        updated_tasks = [task for task in tasks if task["name"] != name]
        with open(file_path, "w") as f:
            json.dump(updated_tasks, f, indent=4)
        print(f'Task Deleted "{name}"\n')
    else:
        print("There is nothing to delete\n")

def update_task(status_task):
    with open(file_path, "r") as f:
        try:
            tasks = json.load(f)
            if isinstance(tasks, dict):
                tasks = [tasks]
        except json.JSONDecodeError:
            tasks = []
    status_task = task_list[2]
    index = next((i for i, task in enumerate(tasks) if task["name"] == name), None)
    tasks[index]["status"] = status_task
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent = 4)
    print(f'Task {name} marked {status_task}\n')

def list_done(file_path):
    with open(file_path , "r") as f:
        try:
            tasks = json.load(f)
            if isinstance(tasks, dict):
                tasks = [tasks]
        except json.JSONDecodeError:
            tasks = []
    done_tasks = [task for task in tasks if task["status"] == "done"]
    print(f'\nHere is the list of completed tasks:\n')
    for task in done_tasks:
        print(task)   
        print()    

def list_ongoing(file_path):
    with open(file_path , "r") as f:
        try:
            tasks = json.load(f)
            if isinstance(tasks, dict):
                tasks = [tasks]
        except json.JSONDecodeError:
            tasks = []
    done_tasks = [task for task in tasks if task["status"] == "in-progress"]
    print(f'\nHere is the list of ongoing tasks:\n')
    for task in done_tasks:
        print(task)   
        print()    

def list_incomplete(file_path):
    with open(file_path , "r") as f:
        try:
            tasks = json.load(f)
            if isinstance(tasks, dict):
                tasks = [tasks]
        except json.JSONDecodeError:
            tasks = []
    done_tasks = [task for task in tasks if task["status"] == "to-do"]
    print(f'\nHere is the list of incomplete tasks:\n')
    for task in done_tasks:
        print(task)   
        print()

def list_all(file_path):
    with open(file_path , "r") as f:
        try:
            tasks = json.load(f)
            if isinstance(tasks, dict):
                tasks = [tasks]
        except json.JSONDecodeError:
            tasks = []
    print(f'\nHere is the list of all tasks:\n')
    for task in tasks:
        print(task)   
        print()

greet()

while True:

    task = input('Enter you request: \n')
    task_list = task.split()
    name = task_list[1]

    id_task = data_id(file_path)
    status_task = data_status()
    data_task = {"name":name,
                "id":id_task,
                "status":status_task,}    

    if("add" in task):
        add(data_task)
        print(f'\nTask Added "{name}"\n')
    elif("delete" in task):
        delete(name)
    elif("mark" in task):
        update_task(status_task)
    elif("list completed" in task):
        list_done(file_path)
    elif("list ongoing" in task):
        list_ongoing(file_path)
    elif("list incomplete" in task):
        list_incomplete(file_path)
    elif("list all" in task):
        list_all(file_path)
    elif ("exit" in task):
        print("\nExiting Task Tracker...")
        break

