from typing import Optional
import math


class OscillatoryCircuit:
    def __init__(self, C: float, L: float, Rm: float, R0: Optional[float] = 0):
        self.C = C
        self.L = L
        self.Rm = Rm
        self.R0 = R0

    @property
    def __initial_capacitor_charge__(self) -> float:
        return 1 ** -9

    @property
    def __natural_frequency__(self) -> float:
        return 1 / math.sqrt(self.L * self.C)

    @property
    def frequency(self) -> float:
        return math.sqrt(self.__natural_frequency__ ** 2 - self.__betta__ ** 2)

    @property
    def __betta__(self) -> float:
        return self.resistance / self.L

    @property
    def __lambda__(self) -> float:
        period = math.pi / math.sqrt(1 / (self.L * self.C) - (self.resistance ** 2) / (4 * (self.L ** 2)))
        return self.__betta__ * period

    @property
    def resistance(self) -> float:
        return self.Rm + self.R0

    def capacitor_charge(self, time: float) -> float:
        q0 = self.__initial_capacitor_charge__
        omega = self.frequency
        return q0 * math.e ** (- self.__betta__ * time) * math.cos(omega * time)

    def capacitor_voltage(self, time: float) -> float:
        u0 = self.__initial_capacitor_charge__ / self.C
        omega = self.frequency
        return u0 * math.e ** (- self.__betta__ * time) * math.cos(omega * time)

    def capacitor_current(self, time: float) -> float:
        q0 = self.__initial_capacitor_charge__
        omega = self.frequency
        return -q0 * math.e ** (- self.__betta__ * time) * \
               (self.__betta__ * math.cos(omega * time) + omega * math.sin(omega * time))
