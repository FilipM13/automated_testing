import statistics

# TODO: function: tStudent
# TODO: function: UMannWhitney
# TODO: function: Wilcoxon
# TODO: class: CheckVarianceNormality, methods: fix Lilliefors, ShapiroWilk, KolmogorovSmirnov
# TODO: function: KruskallWallis
# TODO: function: Friedman
# TODO: function: Anova
# TODO: function: Anova_multivariate


def get_ranks(series: list[float]) -> list[list[float]]:
    """
    Function calculating ranks for given series of values.
    :param series: List of numeric values values
    :return: List of pair of values where first element in pair is element from given input and second element is it's rank
    """
    sorted_series = sorted(series, key=lambda x: abs(x))
    absolute_sorted_series = [abs(v) for v in sorted_series]
    values = set(absolute_sorted_series)
    values_count = [absolute_sorted_series.count(v) for v in values]
    values_range = [range(sum(values_count[:i])+1, sum(values_count[:i+1])+1) for i in range(len(values_count))]
    ranks = [[statistics.mean(_l) for _ in _l] for _l in values_range]
    _tmp = []
    for r in ranks:
        r = [float(_r) for _r in r]
        _tmp.extend(r)

    ranks = [[s, t] for s, t in zip(sorted_series, _tmp)]

    return ranks


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


# TODO: adding paired samples and independent samples version of t student
def tStudent():
    pass


def UMannWhitney(series1: list[float], series2: list[float], critical_value: float) -> bool:
    pass


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
    rv = bool(w < critical_value)  # compare sum with given critical value
    return rv  # return test result


def KruskallWallis():
    pass


def Friedman():
    pass


def Anova():
    pass


def Anova_multivariate():
    pass
