from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Union

from nuscenes_types.asserts import assert_types

from nuscenes_types import SampleData

if TYPE_CHECKING:
    from nuscenes_types import SampleAnnotation
    from cleanup_types import InterpolatedAnnotation

@dataclass
class SampleDataWithAnnotations(SampleData):
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
    annotations: List[Union["SampleAnnotation", "InterpolatedAnnotation"]]

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

        return SampleDataWithAnnotations(**d)
    
    def from_sample_data(s: "SampleData"):
        return SampleDataWithAnnotations(
            token=s.token,
            sample_token=s.sample_token,
            ego_pose_token=s.ego_pose_token,
            calibrated_sensor_token=s.calibrated_sensor_token,
            filename=s.filename,
            fileformat=s.fileformat,
            width=s.width,
            height=s.height,
            timestamp=s.timestamp,
            is_key_frame=s.is_key_frame,
            next=s.next,
            prev=s.prev,
            annotations=[]
        )