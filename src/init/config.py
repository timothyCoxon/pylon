# name: config
# purpose: Initial Configurations required by many files
# complete: No
# task: 
# idea: 
# test: Need Tests
import json
import os

class Config:
    def __init__(self, config_path=os.path.join(os.path.dirname(__file__), 'config.json')):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as file:
            return json.load(file)

    def get_constant(self, key):
        return self.config['constants'].get(key)

    def get_global(self, key):
        return self.config['globals'].get(key)

    def set_global(self, key, value):
        self.config['globals'][key] = value
        self.save_config()

    def save_config(self):
        with open(self.config_path, 'w') as file:
            json.dump(self.config, file, indent=4)

    def update_seen_names(self, name):
        seen_names = self.config['globals'].get('seen_names', [])
        if name not in seen_names:
            seen_names.append(name)
            self.config['globals']['seen_names'] = seen_names
            self.save_config()

config = Config()