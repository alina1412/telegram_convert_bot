
from dataclasses import dataclass
from io import TextIOWrapper
from os import path
import aiofiles
import aiohttp

import requests


@dataclass
class TelebotApiFile:
    name: str
    file: TextIOWrapper
    media_type: str


class TelebotApi:
    def __init__(self, token) -> None:
        self.token = token

    async def _call(self, method_name, **kwargs):
        url = f"https://api.telegram.org/bot{self.token}/{method_name}"
        params = {}
        files = []
        for name, value in kwargs.items():
            if isinstance(value, TelebotApiFile):
                files.append((name, (value.name, value.file, value.media_type)))
            else:
                params[name] = value

        response = requests.post(url, params, files=files)
        response_json = response.json()
        if response_json["ok"]:
            return response_json["result"]

    def __getattr__(self, method_name):
        def wrapper(**kwargs):
            return self._call(method_name, **kwargs)
        return wrapper

    async def get_chunks_of_download(self, url, chunk_size=65536):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                async for chunk in resp.content.iter_chunked(chunk_size):
                    yield chunk

    async def get_file_path(self, document):
        file = await self.getFile(file_id=document["file_id"])
        return file["file_path"]

    def get_file_download_url(self, file_path):
        return f"https://api.telegram.org/file/bot{self.token}/{file_path}"

    async def download_document(self, document, destination):
        file_path = await self.get_file_path(document)
        url = self.get_file_download_url(file_path)
        dest_with_name = path.join(destination, document["file_name"])

        async with aiofiles.open(dest_with_name, 'wb') as download_file:
            async for chunk in self.get_chunks_of_download(url):
                await download_file.write(chunk)
        return dest_with_name
