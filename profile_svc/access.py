import os, requests

# API call to get user profile
def getprofile():
    host = os.environ.get("PROFILE_HOST")  
    response = requests.get(f"http://{host}:8080/profile")
    return response.text
