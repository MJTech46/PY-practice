# load_env.py

# required a file named '.env' with data given below
# API_USER=MY-API-USER-IS-THIS
# API_PASSWORD=MY-API-KEY-IS-THIS

from dotenv import load_dotenv
import os

def load_env_variables():
    load_dotenv()  # Load environment variables from .env file
    api_user = os.getenv('API_USER')
    api_password = os.getenv('API_PASSWORD')
    return api_user, api_password

if __name__ == "__main__":
    user, password = load_env_variables()
    print(f"API_USER: {user}")
    print(f"API_PASSWORD: {password}")
