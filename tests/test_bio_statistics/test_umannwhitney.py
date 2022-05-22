import pytest
from bio_statistics.utils import UMannWhitney


@pytest.mark.parametrize("x1, x2, cv, result", [
    (  # test case 1
        [1, 2, 3, 4],
        [2, 3, -1, 5],
        0.05,
        False
    ),
    (  # test case 2
        [1, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4],
        [2, 3, -1, 5, 3, -1, 5, 3, -1, 5, 3, -1, 5, 3, -1, 5, -1, 5, 3, -1, 5, 3, -1, 5, 3, -1, 5, 3, -1, 5],
        0.05,
        True
    )
])
def test_basic(x1, x2, cv, result):
    assert UMannWhitney(x1, x2, cv) == result
