from dataclasses import dataclass
from typing import Tuple

from nuscenes_types.asserts import assert_array_types, assert_types

Float3 = Tuple[float, float, float]

@dataclass
class CalibratedSensor:
    token: str
    sensor_token: str
    translation: Float3
    rotation: Tuple[float, float, float, float]
    camera_intrinsic: Tuple[Float3, Float3, Float3]
    
    @staticmethod
    def from_dict(d: dict):
        assert_types(d, ["token", "sensor_token"], str)
        assert_array_types(d, "translation", 3, (float, int))
        assert_array_types(d, "rotation", 4, (float, int))
        assert [len(i) for i in d["camera_intrinsic"]] == [3, 3, 3] or len(d["camera_intrinsic"]) == 0, f"received: {[len(i) for i in d['camera_intrinsic']]}"
        for i1 in d["camera_intrinsic"]:
            for i2 in i1:
                assert isinstance(i2, (float, int))

        return CalibratedSensor(**{
            **d,
            "translation": tuple(d["translation"]),
            "rotation": tuple(d["rotation"]),
            "camera_intrinsic": tuple([tuple(i) for i in d["camera_intrinsic"]])
        })