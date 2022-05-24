from dataclasses import dataclass
from typing import Literal, Union

from nuscenes_types.asserts import assert_types

@dataclass
class Sensor:
    token: str
    channel: str
    modality: Union[Literal["camera"], Literal["lidar"], Literal["radar"]]

    @staticmethod
    def from_dict(d: dict):
        assert_types(d, [
            "token",
            "channel",
            "modality",
        ], str)

        modality = d["modality"]
        assert modality in ("camera", "lidar", "radar")

        return Sensor(**d)