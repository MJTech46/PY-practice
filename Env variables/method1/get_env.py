# get_env.py
import os

def get_env_variable(key: str) -> None:
    value: str = os.getenv(key)
    print(f"{key}: {value}")

if __name__ == "__main__":
    get_env_variable("API_KEY")
