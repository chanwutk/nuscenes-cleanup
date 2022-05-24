from dataclasses import dataclass
from typing import List

from nuscenes_types.asserts import assert_array_types, assert_types

@dataclass
class Map:
    token: str
    log_tokens: List[str]
    category: str
    filename: str

    @staticmethod
    def from_dict(d: dict):
        assert_types(d, ["token", "category", "filename"], str)
        assert_array_types(d, "log_tokens", None, str)
        return Map(**d)