import statistics

# TODO: function: test_tStudent
# TODO: function: test_UMannWhitney
# TODO: function: test_Wilcoxon
# TODO: class: CheckVarianceNormality, methods: fix Lilliefors, ShapiroWilk, KolmogorovSmirnov
# TODO: function: test_KruskallWallis
# TODO: function: test_Friedman
# TODO: function: test_Anova
# TODO: function: test_Anova_multivariate


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
def test_tStudent():
    pass


def test_UMannWhitney():
    pass


def test_Wilcoxon():
    pass


def test_KruskallWallis():
    pass


def test_Friedman():
    pass


def test_Anova():
    pass


def test_Anova_multivariate():
    pass
