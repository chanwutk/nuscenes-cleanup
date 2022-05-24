from dataclasses import dataclass
from typing import Optional

from nuscenes_types.asserts import assert_types

@dataclass
class Category:
    token: str
    name: str
    description: str
    index: Optional[int] = None

    @staticmethod
    def from_dict(d: dict):
        assert_types(d, ["token", "name", "description"], str)
        if "index" in d:
            assert_types(d, "index", int)
        return Category(**d)