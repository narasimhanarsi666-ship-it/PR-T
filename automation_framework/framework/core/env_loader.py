from dotenv import load_dotenv
import os

def load_env():
    load_dotenv("automation/configs/dev.env")
    return os.environ
