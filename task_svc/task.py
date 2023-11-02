import os, requests

# API call to get user profile
def gettasks():
    host = os.environ.get("TASK_HOST")  
    response = requests.get(f"http://{host}:8082/tasks")
    return response.text

def addtask(data):
    task = data["task"]
    request={'task': task}
    host = os.environ.get("TASK_HOST")

    response = requests.post(f"http://{host}:8082/task/add", json =request)

    return response.text

def updatetask(id, data):
    task = data["task"]
    request={'task': task}
    host = os.environ.get("TASK_HOST")

    response = requests.put(f"http://{host}:8082/task/{id}", json =request)

    return response.text

def deletetask(id):
    host = os.environ.get("TASK_HOST")
    response = requests.delete(f"http://{host}:8082/task/{id}")

    return response.text

