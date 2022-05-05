import pytest
from bio_statistics.utils import Wilcoxon


@pytest.mark.parametrize("x1, x2, cv, result", [
    (  # test case 1
        [1, 2, 3, 4],
        [2, 3, -1, 5],
        0.5,
        False
    )
])
def test_basic(x1, x2, cv, result):
    assert Wilcoxon(x1, x2, cv) == result
