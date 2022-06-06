import json
import os

from py.path import local


def get_json_schema(schema=""):
    project_path = local(os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))))
    configs_path = project_path.join("data")
    path = configs_path.join(f"{schema}_schema.json").strpath
    with open(path) as file:
        data = json.load(file) or {}
    return data
