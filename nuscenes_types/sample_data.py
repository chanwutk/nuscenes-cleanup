from dataclasses import dataclass

from nuscenes_types.asserts import assert_types

@dataclass
class SampleData:
    token: str
    sample_token: str
    ego_pose_token: str
    calibrated_sensor_token: str
    filename: str
    fileformat: str
    width: int
    height: int
    timestamp: int
    is_key_frame: bool
    next: str
    prev: str

    @staticmethod
    def from_dict(d: dict):
        assert_types(d, [
            "token",
            "sample_token",
            "ego_pose_token",
            "calibrated_sensor_token",
            "filename",
            "fileformat",
            "next",
            "prev",
        ], str)
        assert_types(d, ["width", "height", "timestamp"], int)
        assert_types(d, "is_key_frame", bool)

        return SampleData(**d)