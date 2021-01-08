from functools import reduce
import reader
import analysis
import matplotlib.pyplot as pyplot
from os import path, mkdir


# Find center line of picture (with black circle)
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


# Plot chart and save to file
def plot_results(plot_path: str, visibility: analysis.Visibility):
    pyplot.grid()
    pyplot.title('V(r)')
    pyplot.xlabel('r')
    pyplot.ylabel('V')

    r = range(len(visibility.values))

    pyplot.plot(r, visibility.func(r), r, visibility.values, 'bo')

    pyplot.savefig(plot_path)


def main(debug: bool = False):
    data = reader.read('resources/rings.png')

    # Strip top & bottom parts of picture because they are too dark
    data = data[(len(data) // 5):(len(data) - len(data) // 5)]

    # Find line, containing center of circle
    values = find_center(data)

    # Turn line to receive it from center to the end of rings
    values = values[515:60:-1]

    # Find extremes of this line
    extremes = analysis.extremes(values)
    # Find approximated visibility function
    visibility = analysis.visibility(extremes)

    print(str(visibility.func))

    if not path.exists('results'):
        mkdir('results')
    plot_results('results/plot.png', visibility)


if __name__ == '__main__':
    main(debug=False)
