from dataclasses import dataclass

from nuscenes_types.asserts import assert_types

@dataclass
class Sample:
    token: str
    scene_token: str
    timestamp: int
    next: str
    prev: str

    @staticmethod
    def from_dict(d: dict):
        assert_types(d, [
            "token",
            "scene_token",
            "next",
            "prev",
        ], str)
        assert_types(d, "timestamp", int)

        return Sample(**d)