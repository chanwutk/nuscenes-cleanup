from dataclasses import dataclass
from typing import List

from nuscenes_types.asserts import assert_types
from nuscenes_types import Scene
from cleanup_types import SampleDataWithAnnotations

@dataclass
class SceneWithFrames:
    token: str
    name: str
    description: str
    log_token: str
    nbr_samples: int
    first_sample_token: str
    last_sample_token: str
    frames: List["SampleDataWithAnnotations"]

    @staticmethod
    def from_dict(d: dict):
        assert_types(d, [
            "token",
            "name",
            "description",
            "log_token",
            "first_sample_token",
            "last_sample_token",
        ], str)
        assert_types(d, "nbr_samples", int)

        return SceneWithFrames(**d)

    @staticmethod
    def from_scene(s: "Scene"):
        return SceneWithFrames(
            token=s.token,
            name=s.name,
            description=s.description,
            log_token=s.log_token,
            nbr_samples=s.nbr_samples,
            first_sample_token=s.first_sample_token,
            last_sample_token=s.last_sample_token,
            frames=[]
        )