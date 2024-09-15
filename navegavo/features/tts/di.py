import typing

from openai import OpenAI

from .services import TextToSpeechService


async def client_factory() -> OpenAI:
    return OpenAI()


async def service_cls_factory() -> typing.Type[TextToSpeechService]:
    return TextToSpeechService
