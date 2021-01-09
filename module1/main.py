from typing import Optional
import matplotlib.pyplot as pyplot
from os import path, mkdir
import model
import simulation
import analysis


def plot(num, time: [float], data: [float], title: str, ylabel: str, plot_path: str):
    pyplot.figure(num)
    pyplot.grid()
    pyplot.title(title)
    pyplot.xlabel('t')
    pyplot.ylabel(ylabel)
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
        R0 = 1
        simulation_time = 0.007
        interval = 0.000_000_5
    circuit = model.OscillatoryCircuit(C, L, Rm, R0)
    data = simulation.simulate(circuit, simulation_time, interval)

    print("T (theor.) = {:.7f}".format(circuit.period))
    print("T (exp.) = {:.7f}".format(analysis.experimental_period(data)))
    print("Lambda (theor.) = {:.5f}".format(circuit.lambda_coefficient))
    print("Lambda (exp.) = {:.5f}".format(analysis.experimental_lambda(data)))
    print("Q-factor = {:.5f}".format(circuit.q_factor))

    if not path.exists('results'):
        mkdir('results')
    plot(1, data.time, data.capacitor_charge, 'Capacitor charge', 'q (Кл)', 'results/charge.png')
    plot(2, data.time, data.capacitor_voltage, 'Capacitor voltage', 'U (V)', 'results/voltage.png')
    plot(3, data.time, data.capacitor_current, 'Capacitor current', 'I (A)', 'results/current.png')
    if not debug:
        pyplot.show()


if __name__ == '__main__':
    main(True)
