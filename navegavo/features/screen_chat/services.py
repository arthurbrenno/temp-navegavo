import typing

import msgspec
from llama_index.core.base.llms.types import ChatMessage, ChatResponse
from llama_index.core.multi_modal_llms.base import MultiModalLLM
from llama_index.core.multi_modal_llms.generic_utils import load_image_urls
from llama_index.core.schema import ImageDocument


class ScreenChatService(msgspec.Struct, kw_only=True):
    llm: typing.Annotated[
        MultiModalLLM, msgspec.Meta(title="The Multimodal LLM to use to analise images")
    ]

    messages: typing.Annotated[
        typing.List[ChatMessage],
        msgspec.Meta(title="Messages", description="A list of messages to chat with"),
    ]

    b64_image: typing.Annotated[
        typing.Optional[str],
        msgspec.Meta(
            title="Base 64 Encoded Image",
            description="The base 64 encoded image to send to the LLM",
        ),
    ] = msgspec.field(default=None)

    async def execute(self) -> ChatResponse:
        # Criar image documents aqui
        response: ChatResponse = await self.llm.achat(messages=self.messages)
        return response
