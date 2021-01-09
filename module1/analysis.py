import math

import numpy
from scipy.signal import argrelmax

import simulation


def experimental_period(data: simulation.SimulationData) -> float:
    max_indices = argrelmax(numpy.array(data.capacitor_charge))[0][2:15]
    max_time_values = list(map(lambda i: data.time[i], max_indices))
    intervals = []
    for i in range(1, len(max_time_values)):
        intervals.append(max_time_values[i] - max_time_values[i - 1])
    return sum(intervals) / len(intervals)


def experimental_lambda(data: simulation.SimulationData) -> float:
    max_indices = argrelmax(numpy.array(data.capacitor_voltage))[0]
    return 1 / 3 * math.log(data.capacitor_voltage[max_indices[3]] /
                    data.capacitor_voltage[max_indices[6]])
