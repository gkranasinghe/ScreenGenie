import yaml
import os

def load_config(path="configs/config.yml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
