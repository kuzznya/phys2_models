from typing import TypeVar
import numpy
from scipy.signal import argrelmax, argrelmin


class Visibility:
    def __init__(self, values: [float], func: numpy.poly1d):
        self.values = values
        self.func = func


T = TypeVar('T')


def extremes(values: [T]) -> [T]:
    max_indices = argrelmax(numpy.array(values))[0]
    min_indices = argrelmin(numpy.array(values))[0]

    max_i = 0
    min_i = 0
    result = []
    while max_i < len(max_indices) and min_i < len(min_indices):
        if max_indices[max_i] < min_indices[min_i] and values[max_indices[max_i]] > values[min_indices[min_i]]:
            result.append(values[max_indices[max_i]])
            max_i += 1
        else:
            result.append(values[min_indices[min_i]])
            min_i += 1
    result.extend(map(lambda i: values[i], max_indices[max_i:]))
    result.extend(map(lambda i: values[i], min_indices[min_i:]))
    return result


def visibility(i_extremes: [float]) -> Visibility:
    visibility_values = []
    for i in range(len(i_extremes) - 1):
        i_max = max(i_extremes[i], i_extremes[i + 1])
        i_min = min(i_extremes[i], i_extremes[i + 1])
        vis = (i_max - i_min) / (i_max + i_min)
        visibility_values.append(vis)

    coefficients = numpy.polyfit(x=range(len(visibility_values)), y=visibility_values, deg=5)
    func = numpy.poly1d(coefficients)
    return Visibility(visibility_values, func)
