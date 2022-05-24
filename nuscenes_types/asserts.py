from typing import List, Optional, Union


def assert_types(
    d: dict,
    fields: Union[str, List[str]],
    types: Union[type, List[type]],
):
    if not isinstance(fields, list):
        fields = [fields]
    if not isinstance(types, list):
        types = [types]
    for field in fields:
        assert isinstance(d[field], tuple(types)), f"received: {d[field]}"


def assert_array_types(
    d: dict,
    fields: Union[str, List[str]],
    length: Optional[int],
    types: Union[type, List[type]],
):
    if not isinstance(fields, list):
        fields = [fields]
    if not isinstance(types, list):
        types = [types]
    for field in fields:
        if length is not None:
            assert len(d[field]) == length, f"received: {len(d[field])}"
        for dd in d[field]:
            assert isinstance(dd, tuple(types)), f"received: {dd}"