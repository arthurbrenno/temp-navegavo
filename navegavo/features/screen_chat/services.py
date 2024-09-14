import os
import typing

import msgspec
import requests


class ScreenChatService(msgspec.Struct, kw_only=True):
    messages: typing.Annotated[
        typing.List[typing.Dict[str, typing.Any]],
        msgspec.Meta(title="Messages", description="A list of messages to chat with"),
    ]

    async def execute(self) -> typing.Dict[str, typing.Any]:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": self.messages,
            "max_tokens": 300,
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
        )

        return response.json()
