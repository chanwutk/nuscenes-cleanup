from dataclasses import dataclass

from nuscenes_types.asserts import assert_types

@dataclass
class Scene:
    token: str
    name: str
    description: str
    log_token: str
    nbr_samples: int
    first_sample_token: str
    last_sample_token: str

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

        return Scene(**d)