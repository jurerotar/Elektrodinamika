from math import sqrt, pi
from typing import List


def resistance(current_power_dbm: float) -> float:
    power = sqrt(10**(current_power_dbm/10))
    return (50 / 2) * sqrt(power) / (1 - sqrt(power))


def quality(res: float,
            frequency: float,
            inductance: float = 0.9 * 10 ** (-6)) -> float:
    return (2 * pi * frequency * 10**6 * inductance) / res


frequencies: List[float] = []

loss: List[float] = []

resistances: List[float] = [
    round(resistance(x), 2) for x in loss
]


real_loss: List[float] = [

]

ideal_loss: List[float] = [

]
