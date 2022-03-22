from io import TextIOWrapper
import requests
import urllib.request
import os
from dataclasses import dataclass


@dataclass
class TelebotApiFile:
    name: str
    file: TextIOWrapper
    media_type: str


class TelebotApi:
    def __init__(self, token) -> None:
        self.token = token

    def _call(self, method_name, **kwargs):
        url = f"https://api.telegram.org/bot{self.token}/{method_name}"
        params = {}
        files = []
        for name, value in kwargs.items():
            if isinstance(value, TelebotApiFile):
                files.append(
                    (
                        name,
                        (value.name, value.file, value.media_type)
                    )
                )
            else:
                params[name] = value
        response = requests.post(url, params, files=files)
        response_json = response.json()
        if response_json['ok']:
            return response_json['result']

    def __getattr__(self, method_name):
        def wrapper(*args, **kwargs):
            return self._call(method_name, *args, **kwargs)
        return wrapper

    def download_document(self, document, destination):
        file = self.getFile(file_id=document["file_id"])
        file_path = file["file_path"]
        file_name = document["file_name"]
        url = f'https://api.telegram.org/file/bot{self.token}/{file_path}'
        with urllib.request.urlopen(url) as f:
            dest_with_name = os.path.join(destination, file_name)
            with open(dest_with_name, 'wb') as output:
                output.write(f.read())
                return dest_with_name
