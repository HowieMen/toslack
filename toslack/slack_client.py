from io import IOBase
from typing import Any, Union
from dataclasses import dataclass

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

@dataclass
class SlackClient:

    token: str = ''
    channel: str = ''
    channel_id: str = ''

    def _client(self):
        if self.token == '':
            raise TypeError("missing required parameter: slack robot token")
        return WebClient(self.token)

    def post(self, text: str=""):
        if self.channel == '':
            raise TypeError("missing required parameter: slack channel")
        self._client().chat_postMessage(channel=self.channel, text=text)

    def upload(self, file: Union[str, bytes, IOBase, None], filename: Union[str, None]):
        if self.channel_id == '':
            raise TypeError("missing required parameter: slack channel ID")
        return self._client().files_upload_v2(channel=self.channel_id, file=file, filename=filename)