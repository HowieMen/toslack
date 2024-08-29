from typing import Any
from dataclasses import dataclass, field

from .slack_client import Client

@dataclass
class Message:

    client: Client
    blocks: list[dict[str, Any]] = field(default_factory=list)
    text: str = ''

    def post(self, text: str) -> None:
        self.client.post(blocks=self.blocks, text=text)
    
    def upload(self, file_path: str) -> None:
        self.client.upload(file=file_path, filename=file_path)