from dataclasses import dataclass

from nuscenes_types.asserts import assert_types

@dataclass
class Attribute:
    token: str
    name: str
    description: str

    @staticmethod
    def from_dict(d: dict):
        assert_types(d, ["token", "name", "description"], str)
        return Attribute(**d)