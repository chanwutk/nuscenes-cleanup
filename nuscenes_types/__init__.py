from .attribute import Attribute
from .calibrated_sensor import CalibratedSensor
from .category import Category
from .ego_pose import EgoPose
from .instance import Instance
from .lidarseg import Lidarseg
from .log import Log
from .map import Map
from .sample_annotation import SampleAnnotation
from .sample_data import SampleData
from .sample import Sample
from .scene import Scene
from .sensor import Sensor
from .visibility import Visibility

from_dicts = {
    "attribute": Attribute.from_dict,
    "calibrated_sensor": CalibratedSensor.from_dict,
    "category": Category.from_dict,
    "ego_pose": EgoPose.from_dict,
    "instance": Instance.from_dict,
    "lidarseg": Lidarseg.from_dict,
    "log": Log.from_dict,
    "map": Map.from_dict,
    "sample_annotation": SampleAnnotation.from_dict,
    "sample_data": SampleData.from_dict,
    "sample": Sample.from_dict,
    "scene": Scene.from_dict,
    "sensor": Sensor.from_dict,
    "visibility": Visibility.from_dict,
}

__all__ = [
    "Attribute",
    "CalibratedSensor",
    "Category",
    "EgoPose",
    "Instance",
    "Lidarseg",
    "Log",
    "Map",
    "SampleAnnotation",
    "SampleData",
    "Sample",
    "Scene",
    "Sensor",
    "Visibility",
    "from_dicts",
]