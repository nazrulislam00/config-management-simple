import json

def load_config(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

if __name__ == "__main__":
    config = load_config("config.json")

    print("App Name:", config["app_name"])
    print("Version:", config["version"])
    print("Debug Mode:", config["debug"])
    print("Port:", config["port"])
