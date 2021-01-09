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
        return self.resistance / (2 * self.L)

    @property
    def lambda_coefficient(self) -> float:
        return self.__betta__ * self.period

    @property
    def resistance(self) -> float:
        return self.Rm + self.R0

    @property
    def period(self) -> float:
        return 2 * math.pi / self.frequency

    @property
    def q_factor(self) -> float:
        return 1 / self.resistance * math.sqrt(self.L / self.C)

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
