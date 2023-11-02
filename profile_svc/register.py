import os, requests

# API call to add new user property
def addproperty(data):
    name = data['name']
    value = data["value"]

    data={'name': name, 'value': value}
    
    host = os.environ.get("PROFILE_HOST")
    response = requests.post(f"http://{host}:8080/profile/add", json =data)

    return response.text

