import os

class EnvMissingError(Exception):
    pass

class SDK:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        if self.api_key is None:
            raise EnvMissingError("API_KEY es requerida")