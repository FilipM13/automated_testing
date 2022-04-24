import pytest
import bio_statistics.utils


@pytest.mark.parametrize("test_input, expected", [
    (
        [float(x) for x in [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1234, 111]],
        [
            [0.0, 0.0], [1.0, 2.5], [1.0, 2.5], [1.0, 2.5], [1.0, 2.5], [2.0, 5.0], [3.0, 6.0], [4.0, 7.0],
            [5.0, 8.0], [6.0, 9.0], [7.0, 10.0], [8.0, 11.0], [9.0, 12.0], [111.0, 13.0], [1234.0, 14.0]]
    )
])
def test_basic(test_input, expected):
    assert bio_statistics.utils.get_rangs(test_input), expected
