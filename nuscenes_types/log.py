from dataclasses import dataclass

from nuscenes_types.asserts import assert_types

@dataclass
class Log:
    token: str
    logfile: str
    vehicle: str
    date_captured: str
    location: str

    @staticmethod
    def from_dict(d: dict):
        assert_types(d, ["token", "logfile", "vehicle", "date_captured", "location"], str)
        return Log(**d)