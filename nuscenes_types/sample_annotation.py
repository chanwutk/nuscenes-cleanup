from dataclasses import dataclass
from typing import List, Tuple

from nuscenes_types.asserts import assert_array_types, assert_types

Float3 = Tuple[float, float, float]

@dataclass
class SampleAnnotation:
    token: str
    sample_token: str
    instance_token: str
    attribute_tokens: List[str]
    visibility_token: str
    translation: Float3
    size: Float3
    rotation: Tuple[float, float, float, float]
    num_lidar_pts: int
    num_radar_pts: int
    next: str
    prev: str
    
    @staticmethod
    def from_dict(d: dict):
        assert_types(d, [
            "token",
            "sample_token",
            "instance_token",
            "visibility_token",
            "next",
            "prev",
        ], str)
        assert_array_types(d, "attribute_tokens", None, str)
        assert_array_types(d, "translation", 3, (float, int))
        assert_array_types(d, "size", 3, (float, int))
        assert_array_types(d, "rotation", 4, (float, int))
        assert_types(d, ["num_lidar_pts", "num_radar_pts"], int)

        return SampleAnnotation(**{
            **d,
            "translation": tuple(d["translation"]),
            "size": tuple(d["size"]),
            "rotation": tuple(d["rotation"]),
        })