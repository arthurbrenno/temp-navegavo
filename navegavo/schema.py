"""
Module documentation
"""


import msgspec
import typing


class ScreenInfo(msgspec.Struct):
    description: typing.Annotated[
        str,
        msgspec.Meta(title="Description", description="The contents of the screen."),
    ]
