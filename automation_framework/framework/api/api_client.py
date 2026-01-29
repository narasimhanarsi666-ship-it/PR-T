import requests
from framework.core.env_loader import load_env

env = load_env()

def post(path,data):
    return requests.post(env["BASE_URL"]+path,json=data)

def get(path):
    return requests.get(env["BASE_URL"]+path)
