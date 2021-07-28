import os
import pytest

from src.fetch_scene import _validate_input, fetch_scene

# tests for _validate_input (Using valid input)


@pytest.mark.parametrize(
    "test_input",
    [
        # case 1
        {"bands": [1]},
        # case 2
        {"bands": [1, 2]},
        # case 3
        {"bands": [1, 2, 3]},
        # case 4
        {"bands": [1, 2, 3, 4]},
        # case 5
        {"bands": [1, 2, 3, 4, 5]},
        # case 6
        {"bands": [1, 2, 3, 4, 5, 6]},
        # case 7
        {"bands": [1, 2, 3, 4, 5, 6, 7]},
        # case 8
        {"bands": [1, 2, 3, 4, 5, 6, 7, 8]},
        # case 9
        {"bands": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
        # case 10
        {"bands": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
        # case 11
        {"bands": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]},
        # case 12
        {"bands": [3, 6, 9, 1]},
    ],
)
def test_validate_input_by_valid_input(test_input):
    assert _validate_input(**test_input)


# tests for _validate_input (Using invalid input)
@pytest.mark.parametrize(
    "test_input",
    [
        # case 1
        {"bands": [1, 2, 7, 14, 66, 99]},
        # case 2
        {"bands": ["blue", "green", "swir", 7]},
    ],
)
def test_validate_input_by_invalid_input(test_input):
    with pytest.raises(ValueError):
        _validate_input(**test_input)


# tests for fetch_Scene
@pytest.mark.parametrize(
    "test_input",
    [
        # case 1
        {"s3_endpoint": "s3://usgs-landsat/collection02/level-1/standard/oli-tirs/2021/046/028/LC08_L1TP_046028_20210725_20210725_02_RT/",
         "bands": [5, 6, 7]},
    ],
)
def test_fetch_scene(test_input, tmpdir):
    paths = fetch_scene(
        test_input['s3_endpoint'],
        tmpdir,
        test_input['bands']
    )
    for path in paths:
        assert os.path.exists(path)
