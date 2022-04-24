import statistics


def get_rangs(series: list[float]) -> list[list[float]]:

    sorted_series = sorted(series, key=lambda x: abs(x))
    absolute_sorted_series = [abs(v) for v in sorted_series]

    values = set(absolute_sorted_series)

    values_count = [absolute_sorted_series.count(v) for v in values]

    values_range = [range(sum(values_count[:i]), sum(values_count[:i+1])) for i in range(len(values_count))]

    rangs = [[statistics.mean(_l) for _ in _l] for _l in values_range]
    _tmp = []
    for r in rangs:
        r = [float(_r) for _r in r]
        _tmp.extend(r)

    rangs = [[s, t] for s, t in zip(sorted_series, _tmp)]

    return rangs
