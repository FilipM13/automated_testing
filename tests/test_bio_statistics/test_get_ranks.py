import pytest
from bio_statistics.utils import get_ranks


# test basic behaviour of function with regular cases and edge cases
@pytest.mark.parametrize("test_input, expected", [
    (  # test case 1
        [float(x) for x in [0, 5, 6, 7, 8, -7, -1, 2, 1, 1]],
        [[0, 1.0], [-1, 3.0], [1, 3.0], [1, 3.0], [2, 5.0], [5, 6.0], [6, 7.0], [7, 8.5], [-7, 8.5], [8, 10.0]]
    ),
    (
        [],
        []
    )
])
def test_basic(test_input, expected):
    assert get_ranks(test_input) == expected
