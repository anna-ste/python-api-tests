import json
import os

from py.path import local

project_path = local(os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))))
configs_path = project_path.join("config")


class SettingsParser:
    def __init__(self):
        local_file = configs_path.join("settings_local.json").strpath
        self.path = local_file if os.path.isfile(local_file) else configs_path.join("settings.json").strpath

        with open(self.path) as file:
            self.data = json.load(file) or {}
        for key, value in self.data.items():
            if os.environ.get(key.upper()):
                setattr(self, key, os.environ[key.upper()])
            else:
                setattr(self, key, value)


settings = SettingsParser()