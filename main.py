from functools import reduce
import reader
import analysis
import matplotlib.pyplot as pyplot
from os import path, mkdir


def print_data(data: [[int]]):
    i = 0
    for row in data:
        print(f"{i}: ", " ".join(map(lambda value: '{:0>3d}'.format(value), row)))
        i += 1


def find_center(data: [[int]]) -> [int]:
    if len(data) == 0:
        return []
    min_i = 0
    min_value = 255 * len(data[0])
    for i in range(len(data)):
        cur_value = reduce(lambda v1, v2: v1 + v2, data[i])
        if cur_value < min_value:
            min_value = cur_value
            min_i = i
    return data[min_i]


def plot_results(plot_path: str, visibility: analysis.Visibility):
    pyplot.grid()
    pyplot.title('V(r)')
    pyplot.xlabel('r')
    pyplot.ylabel('V')

    r = range(len(visibility.values))

    pyplot.plot(r, visibility.func(r), visibility.values, 'bo')

    pyplot.savefig(plot_path)


def main(debug: bool = False):
    data = reader.read('resources/rings.png')

    # Strip top & bottom parts of picture because they are too dark
    data = data[(len(data) // 5):(len(data) - len(data) // 5)]
    # Find line, containing center of circle
    values = find_center(data)

    values = values[(len(values) // 5):(len(values) - len(values) // 4)]
    # Find extremes of this line
    extremes = analysis.extremes(values)
    # Find approximated visibility function
    visibility = analysis.visibility(extremes)

    print(str(visibility.func))
    if debug:
        print(len(visibility.values))
    if not path.exists('results'):
        mkdir('results')
    plot_results('results/plot.png', visibility)


if __name__ == '__main__':
    main(debug=True)
