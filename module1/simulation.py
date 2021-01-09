from typing import Optional

import model


class SimulationData:
    def __init__(self):
        self.time = []
        self.capacitor_charge = []
        self.capacitor_voltage = []
        self.capacitor_current = []

    def point(self,
              time: float,
              capacitor_charge: float,
              capacitor_voltage: float,
              capacitor_current: float):
        self.time.append(time)
        self.capacitor_charge.append(capacitor_charge)
        self.capacitor_voltage.append(capacitor_voltage)
        self.capacitor_current.append(capacitor_current)


def simulate(circuit: model.OscillatoryCircuit,
             duration: float,
             time_delta: Optional[float] = 0.001) -> SimulationData:
    time = 0
    data = SimulationData()
    while time <= duration:
        data.point(
            time=time,
            capacitor_charge=circuit.capacitor_charge(time),
            capacitor_voltage=circuit.capacitor_voltage(time),
            capacitor_current=circuit.capacitor_current(time)
        )
        time += time_delta
    return data
