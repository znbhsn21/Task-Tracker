import json
def greet():
    print("Hi! I am your task tracker")
if (__name__ =="__main__"):
    greet()


task = input('tracker-cli ')
task_list = task.split()
name = task_list[1]
status = ["done","in-progress","to-do"]
if("add" in task):
    print(f'Task Added "{name}"')


data = {"name":name,
        "id":"1",
        "status":"to-do",
        "created_at":"Now"}

json_str = json.dumps(data, indent=4)
with open("sample.json", "w") as f:
    f.write(json_str)