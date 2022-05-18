import pytest
from bio_statistics.utils import get_ranks


# test basic behaviour of function with regular cases and edge cases
@pytest.mark.parametrize("test_input, expected", [
    (  # test case 1
        [0, 5, 6, 7, 8, -7, -1, 2, 1, 1],
        [[0, 1], [5, 6], [6, 7], [7, 8.5], [8, 10], [-7, 8.5], [-1, 3], [2, 5], [1, 3], [1, 3]]
    ),
    (  # test case 2
        [],
        []
    ),
    (  # test case 3
        [1, 2, 3, 4, 3],
        [[1, 1], [2, 2], [3, 3.5], [4, 5], [3, 3.5]]
    ),
    (  # test case 3
        [18, 22, 23, 26, 23],
        [[18, 1], [22, 2], [23, 3.5], [26, 5], [23, 3.5]]
    )
])
def test_basic(test_input, expected):
    assert get_ranks(test_input) == expected
