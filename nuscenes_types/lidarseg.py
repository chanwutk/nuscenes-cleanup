from dataclasses import dataclass

from nuscenes_types.asserts import assert_types

@dataclass
class Lidarseg:
    token: str
    filename: str
    sample_data_token: str

    @staticmethod
    def from_dict(d: dict):
        assert_types(d, ["token", "filename", "sample_data_token"], str)
        return Lidarseg(**d)