import os

import yaml


class YAMLParser:
    @staticmethod
    def parse(filepath):
        with open(os.path.join(os.path.dirname(__file__), filepath), 'r') as stream:
            try:
                print(yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                print(exc)
