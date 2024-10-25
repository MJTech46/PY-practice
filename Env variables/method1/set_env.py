# set_env.py
import os

# only last for end of execution of this code!
def set_env_variable(key: str, value: str) -> None:
    os.environ[key] = value
    print(f"The environment variable {key} is set.")

if __name__ == "__main__":
    set_env_variable("API_KEY", "MY-API-KEY-IS-THIS")
    os.system("python3 get_env.py")
