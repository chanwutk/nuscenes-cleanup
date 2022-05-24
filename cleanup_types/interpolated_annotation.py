from dataclasses import dataclass
from typing import List, Tuple


Float3 = Tuple[float, float, float]

@dataclass
class InterpolatedAnnotation:
    interpolated_weight: float
    token2: Tuple[str, str]
    sample_token2: Tuple[str, str]
    instance_token: str
    attribute_tokens: List[str]
    visibility_token2: Tuple[str, str]
    translation: Float3
    size: Float3
    rotation: Tuple[float, float, float, float]
    num_lidar_pts2: Tuple[int, int]
    num_radar_pts2: Tuple[int, int]
    