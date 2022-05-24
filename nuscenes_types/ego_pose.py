from dataclasses import dataclass
from typing import Tuple

from nuscenes_types.asserts import assert_array_types, assert_types


@dataclass
class EgoPose:
    token: str
    translation: Tuple[float, float, float]
    rotation: Tuple[float, float, float, float]
    timestamp: int
    
    @staticmethod
    def from_dict(d: dict):
        assert_types(d, "token", str)
        assert_array_types(d, "translation", 3, (float, int))
        assert_array_types(d, "rotation", 4, (float, int))
        assert_types(d, "timestamp", int)

        return EgoPose(**{
            **d,
            "translation": tuple(d["translation"]),
            "rotation": tuple(d["rotation"]),
        })