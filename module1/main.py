from typing import Optional
import matplotlib.pyplot as pyplot
from os import path, mkdir
import model
import simulation


def plot(num, time: [float], data: [float], title: str, plot_path: str):
    pyplot.figure(num)
    pyplot.grid()
    pyplot.title(title)
    pyplot.xlabel('t')
    pyplot.plot(time, data)
    pyplot.savefig(plot_path)


def main(debug: Optional[bool] = False):
    if not debug:
        C = float(input("C (нФ) = ")) * 10 ** -9
        L = float(input("L (мГн) = ")) * 10 ** -3
        Rm = float(input("Rm (Ом) = "))
        R0 = float(input("R0 (Ом) = "))
        simulation_time = float(input("Simulation time: "))
        interval = float(input("Data interval: "))
    else:
        C = 50 * 10 ** -9
        L = 10 * 10 ** -3
        Rm = 10
        R0 = 0
        simulation_time = 0.006
        interval = 0.000_000_5
    circuit = model.OscillatoryCircuit(C, L, Rm, R0)
    data = simulation.simulate(circuit, simulation_time, interval)

    if not path.exists('results'):
        mkdir('results')
    plot(1, data.time, data.capacitor_charge, 'Capacitor charge', 'results/charge.png')
    plot(2, data.time, data.capacitor_voltage, 'Capacitor voltage', 'results/voltage.png')
    plot(3, data.time, data.capacitor_current, 'Capacitor current', 'results/current.png')
    if not debug:
        pyplot.show()


if __name__ == '__main__':
    main(True)
