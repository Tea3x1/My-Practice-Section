def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError(
            "Please dont use any zero or negative length or lenght higher ")

    return [series[i: i + length] for i in range(len(series) - length + 1)]
