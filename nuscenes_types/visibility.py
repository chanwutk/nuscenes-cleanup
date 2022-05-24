from dataclasses import dataclass
from typing import Literal, Union

from nuscenes_types.asserts import assert_types

@dataclass
class Visibility:
    token: str
    level: str
    description: str

    @staticmethod
    def from_dict(d: dict):
        assert_types(d, [
            "token",
            "level",
            "description",
        ], str)

        return Visibility(**d)