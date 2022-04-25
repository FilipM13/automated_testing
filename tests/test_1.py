import pytest
import bio_statistics.utils


@pytest.mark.parametrize("test_input, expected", [
    (
        [float(x) for x in [0, 5, 6, 7, 8, -7, -1, 2, 1, 1]],
        [[0, 1.0], [-1, 3.0], [1, 3.0], [1, 3.0], [2, 5.0], [5, 6.0], [6, 7.0], [7, 8.5], [-7, 8.5], [8, 10.0]]
    ),
    (
        [],
        []
    )
])
def test_basic(test_input, expected):
    assert bio_statistics.utils.get_ranks(test_input) == expected, f'{bio_statistics.utils.get_ranks(test_input)} not equal to {expected}'
