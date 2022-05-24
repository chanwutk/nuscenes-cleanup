from dataclasses import dataclass

from nuscenes_types.asserts import assert_types

@dataclass
class Instance:
    token: str
    category_token: str
    nbr_annotations: int
    first_annotation_token: str
    last_annotation_token: str

    @staticmethod
    def from_dict(d: dict):
        assert_types(d, ["token", "category_token", "first_annotation_token", "last_annotation_token"], str)
        assert_types(d, "nbr_annotations", int)
        return Instance(**d)