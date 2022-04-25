import statistics


# TODO: function: check_variance_normality
# TODO: function: test_tStudent
# TODO: function: test_UMannWhitney
# TODO: function: test_Wilcoxon
# TODO: function: test_KruskallWallis
# TODO: function: test_Friedman
# TODO: function: test_Anova
# TODO: function: test_Anova_multivariate


def get_ranks(series: list[float]) -> list[list[float]]:
    """
    Function calculating ranks for given series of values.
    :param series: List of numeric values values
    :return: List of pair of values where first element in pair is element from given input and second element is it's rang
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
