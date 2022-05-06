import pytest
from bio_statistics.utils import tStudent


@pytest.mark.parametrize("x1, x2, cv, result", [
    (  # test case 1
        [1, 2, 3, 4],
        [2, 3, -1, 5],
        0.5,
        True
    ),
    (  # test case 2
        [1, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4],
        [2, 3, -1, 5, 3, -1, 5, 3, -1, 5, 3, -1, 5, 3, -1, 5, -1, 5, 3, -1, 5, 3, -1, 5, 3, -1, 5, 3, -1, 5],
        0.5,
        False
    )
])
def test_basic(x1, x2, cv, result):
    assert tStudent(x1, x2, cv) == result
