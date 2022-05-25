import statistics
from typing import Any
from bio_statistics import critical_value_tables

# TODO: add files with crtical value tables
# TODO: remove critical_value parameter from test functions
# TODO: function: Friedman
# TODO: class: CheckVarianceNormality, methods: Lilliefors, ShapiroWilk, KolmogorovSmirnov
# TODO: function: KruskallWallis
# TODO: function: Anova
# TODO: function: Anova_multivariate


def _get_critical_value(test: str, **kwargs: Any) -> float:
    """
    Get critical value for test from source UMannWhitney_table.
    :param test: name of test
    :param kwargs: parameters to get value from UMannWhitney_table
    :return: critical value
    """

    sources = [
        'UMannWhitney'
    ]

    assert test in sources, 'Unavailable test.'

    if test == 'UMannWhitney':
        alfa = kwargs['alfa']

        n1 = kwargs['n1']
        if n1 <= 3:
            n1 = 3

        n2 = kwargs['n2']
        if n2 <= 3:
            n2 = 3

        rv = critical_value_tables.UMannWhitney_table[alfa][n1][n2]  # noqa: F841
        return 0.5  # temporary, replace with rv

    return 0.5


def _lower_dict_sum(series: dict[float, int], k: float) -> int:
    """
    IMPORTANT: hack for get_ranks function, it serves no utility on its's own.
    Return sum of values corresponding to keys smaller than k.
    :param series: dictionary of key (float or int) and value (int)
    :param k: value for comparing keys
    :return: sum of chosen values
    """
    s = 0
    for key, value in series.items():
        if key < k:
            s += value
    return s


def get_ranks(series: list[float]) -> list[list[float]]:
    """
    Function calculating ranks for given series of values.
    :param series: List of numeric values values
    :return: List of pair of values where first element in pair is element from given input and second element is it's rank
    """

    # input data validation
    assert all([isinstance(v, (float, int)) for v in series]), 'All values must be numeric (int or float).'

    # steps
    sorted_series = sorted(series, key=lambda x: abs(x))  # sort series by absolute value
    absolute_sorted_series = [abs(v) for v in sorted_series]  # get absolut values of sorted values
    values = set(absolute_sorted_series)  # get unique values
    values_count = {v: absolute_sorted_series.count(v) for v in values}  # count unique values
    values_range = {v: range(_lower_dict_sum(values_count, v) + 1, _lower_dict_sum(values_count, v) + values_count[v] + 1) for v in values}  # associate unique values with index ranges # noqa: E501
    rank_assignments = {v: statistics.mean(values_range[v]) for v in values}  # associate unique values with mean of coresponding indices

    # create list of [value, rank] in order of original series
    ranks = []
    for s in series:
        ranks.append([s, rank_assignments[abs(s)]])

    return ranks


# disabled
class CheckVarianceNormality:
    """
    Temporarily disabled.
    """
    @classmethod
    def lilliefors(cls, series: list[float], critical_value: float) -> bool:
        pass

    @classmethod
    def shapiro_wilk(cls, series: list[float], critical_value: float) -> bool:
        pass

    @classmethod
    def kolmogorov_smirnov(cls, series: list[float], critical_value: float) -> bool:
        pass


# add _get_critical_value functionality
def tStudent(series1: list[float], series2: list[float], critical_value: float, independent_samples: bool = True) -> bool:
    """
    Reject H0 hypothesis if return value is True.
    :param series1:
    :param series2:
    :param critical_value:
    :param independent_samples:
    :return:
    """

    # input validation
    assert all([isinstance(v, (float, int)) for v in series1]), 'All values must be numeric (int or float).'
    assert all([isinstance(v, (float, int)) for v in series2]), 'All values must be numeric (int or float).'
    assert isinstance(critical_value, (float, int)), 'Critical value must be numeric (int or float).'
    assert isinstance(independent_samples, bool), 'Independent_samples must be boolean.'
    if not independent_samples:
        assert len(series1) == len(series2), 'For dependent samples series size must be the same.'

    # calcualting basic constans
    v1 = statistics.variance(series1)  # variance
    v2 = statistics.variance(series2)
    m1 = statistics.mean(series1)  # mean
    m2 = statistics.mean(series2)
    n1 = len(series1)  # number of samples
    n2 = len(series2)

    # test steps for equal variance and independent samples
    if v1 == v2 and independent_samples:
        _top = m1 - m2

        _bottom_top = v1 ** 2 * (n1 - 1) + v2 ** 2 * (n2 - 1)
        _bottom_btm = n1 + n2 - 2
        _bottom_multiplier = 1 / n1 + 1 / n2

        _bottom = (_bottom_top / _bottom_btm * _bottom_multiplier) ** 0.5

        t = _top / _bottom

    # test steps for unequal varianc and indepandent samples
    if v1 != v2 and independent_samples:
        _top = m1 - m2
        _bottom = (v1 ** 2 / n1 + v2 ** 2 / n2) ** 0.5

        t = _top / _bottom

    # test steps for dependent samples
    if not independent_samples:
        series_dif = [abs(s[0] - s[1]) for s in zip(series1, series2)]
        m = statistics.mean(series_dif)  # mean
        n = len(series_dif)  # number of samples
        std = statistics.stdev(series_dif)  # standard deviation
        t = m * n ** 0.5 / std

    rv = t < critical_value
    return rv  # type: ignore[no-any-return]


def UMannWhitney(series1: list[float], series2: list[float], alfa: float) -> bool:
    """
    Reject H0 hypothesis if return value is True.
    :param series1:
    :param series2:
    :param critical_value:
    :return:
    """

    # input data validation
    assert (len(series1) <= 20 and len(series2) <= 20) or (len(series1) > 20 and len(series2) > 20), 'Both series must be in the same count group (both <= 20 or both >20).'  # noqa: E501
    assert all([isinstance(v, (float, int)) for v in series1]), 'All values must be numeric (int or float).'
    assert all([isinstance(v, (float, int)) for v in series2]), 'All values must be numeric (int or float).'
    assert isinstance(alfa, (float, int)), 'Critical value must be numeric (int or float).'

    # test steps
    series1_ranks = get_ranks(series1)  # get ranks for both series
    series2_ranks = get_ranks(series2)
    sum_series1_ranks = sum([r[1] for r in series1_ranks])  # sum ranks for both series
    sum_series2_ranks = sum([r[1] for r in series2_ranks])
    n1 = len(series1)  # get length of both series
    n2 = len(series2)

    # calculate statistic if both series are not larger than 20
    if n1 <= 20 and n2 <= 20:
        u1 = n1 * n2 + n1 * (n1 + 1) / 2 - sum_series1_ranks
        u2 = n1 * n2 + n2 * (n2 + 1) / 2 - sum_series2_ranks
        u = min(u1, u2)
        critical_value = _get_critical_value(test='UMannWhitney', alfa=alfa, n1=n1, n2=n2)

    # calculate statistic if both series are larger than 20
    elif n1 > 20 and n2 > 20:
        n = n1 + n2
        _top = sum_series1_ranks - sum_series2_ranks - (n1 - n2) * (n + 1) / 2
        _bottom = (n1 * n2 * (n+1) / 3) ** 0.5
        u = _top / _bottom
        critical_value = 0.5

    rv = u < critical_value  # compare statistic with critical value
    return rv  # return result


# add _get_critical_value functionality
def Wilcoxon(series1: list[float], series2: list[float], critical_value: float = 0.05) -> bool:
    """
    Reject H0 hypothesis if return value is True.
    :param series1: first series of values
    :param series2: second  series of values
    :param critical_value:
    :return:
    """

    # input data validation
    assert len(series1) == len(series2), 'Series must be same length.'
    assert all([isinstance(v, (float, int)) for v in series1]), 'All values must be numeric (int or float).'
    assert all([isinstance(v, (float, int)) for v in series2]), 'All values must be numeric (int or float).'
    assert isinstance(critical_value, (float, int)), 'Critical value must be numeric (int or float).'

    # test steps
    differance = [r[0]-r[1] for r in zip(series1, series2)]  # calculate differance between series
    differance = list(filter(lambda r: r != 0, differance))  # remove 0 values
    differance_ranks = get_ranks(differance)  # get ranks
    positive_ranks = list(v[1] for v in filter(lambda r: r[0] > 0, differance_ranks))  # get positive ranks
    negative_ranks = list(v[1] for v in filter(lambda r: r[0] < 0, differance_ranks))  # get negative ranks
    positive_sum = sum(positive_ranks)  # calculate sum of positive ranks
    negative_sum = sum(negative_ranks)  # calculate sum of negative ranks
    w = min(negative_sum, positive_sum)  # get statistic
    if len(series1) > 25:  # check test series length
        n = len(series1)  # series length
        m = n * (n + 1) / 4  # calculate micro
        s = ((2 * n + 1) * m / 6) ** 0.5  # calculate sigma
        w = (w - m) / s  # calculate new statistic
    rv = w < critical_value  # compare sum with given critical value
    return rv  # return test result


def KruskallWallis():
    pass


def Friedman():
    pass


def Anova():
    pass


def Anova_multivariate():
    pass


def pearson_corelation(series1: list[float], series2: list[float]) -> float:
    """
    Calculates corelation value using Pearson method.
    :param series1: first series of values
    :param series2: second  series of values
    :return: corelation value
    """

    # input data validation
    assert len(series1) == len(series2), 'Series must be same length.'
    assert all([isinstance(v, (float, int)) for v in series1]), 'All values must be numeric (int or float).'
    assert all([isinstance(v, (float, int)) for v in series2]), 'All values must be numeric (int or float).'

    # calculating corelation
    m1 = statistics.mean(series1)
    m2 = statistics.mean(series2)
    difs1 = [abs(m1 - s) for s in series1]
    difs2 = [abs(m2 - s) for s in series2]
    mult = [d[0] * d[1] for d in zip(difs1, difs2)]
    A = float(sum(mult))

    square_difs1 = [d**2 for d in difs1]
    square_difs2 = [d**2 for d in difs2]
    B1 = float(sum(square_difs1)**0.5)
    B2 = float(sum(square_difs2)**0.5)

    rp = A / (B1 * B2)

    return rp


def spearman_corelation(series1: list[float], series2: list[float]) -> float:
    """
    Calculates corelation value using Spearman method.
    :param series1: first series of values
    :param series2: second  series of values
    :return: corelation value
    """

    # input data validation
    assert len(series1) == len(series2), 'Series must be same length.'
    assert all([isinstance(v, (float, int)) for v in series1]), 'All values must be numeric (int or float).'
    assert all([isinstance(v, (float, int)) for v in series2]), 'All values must be numeric (int or float).'

    # calculating corelation
    s1r = [r[1] for r in get_ranks(series1)]
    s2r = [r[1] for r in get_ranks(series2)]
    difs_r = [s[0] - s[1] for s in zip(s1r, s2r)]
    difs_r = [d ** 2 for d in difs_r]
    sdifsr = sum(difs_r)

    n = len(series1)

    repetition_count1 = [s1r.count(r) for r in set(s1r)]
    repetition_count1 = [r ** 3 - r for r in repetition_count1]
    t1 = sum(repetition_count1) / 12

    repetition_count2 = [s2r.count(r) for r in set(s2r)]
    repetition_count2 = [r ** 3 - r for r in repetition_count2]
    t2 = sum(repetition_count2) / 12

    rs = 1 - (6 * sdifsr + t1 + t2) / (n * (n * 2 - 1))

    return rs
