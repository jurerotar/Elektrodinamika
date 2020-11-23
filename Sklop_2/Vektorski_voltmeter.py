import matplotlib.pyplot as plt
import math
from typing import List, Dict


def arraySubtraction(array1: List[float], array2: List[float]) -> List[float]:
    return [array1[i] - array2[i] for i in range(len(array1))]


frequency: List[float] = [
    1,
    5,
    10,
    15,
    20,
    31,
    34,
    36,
    39,
    40,
    42.5,
    44,
    45.5,
    46.1,
    46.9,
    48,
    50,
    51,
    60,
    70,
    80,
    90,
    100,
    150,
    200,
]

canalA: List[float] = [
    6,
    6.1,
    6.2,
    6.1,
    6,
    6,
    6,
    5.8,
    5.6,
    5.5,
    5.3,
    4.9,
    3.5,
    2.6,
    1,
    0.9,
    4.9,
    5.3,
    5.8,
    5.6,
    5.5,
    5.4,
    5.4,
    4.2,
    2.5,
]

canalB: List[float] = [
    -55,
    -50.5,
    -34,
    -30.1,
    -28.8,
    -20.5,
    -18.4,
    -17,
    -14,
    -13,
    -9.8,
    -7.4,
    -4.5,
    -3.2,
    -1.9,
    -1.3,
    -4.5,
    -6.2,
    -17,
    -21.5,
    -25,
    -27.8,
    -30,
    -46,
    -38,
]

phase: List[float] = [
    90,
    89,
    85,
    85,
    84,
    80,
    78,
    76,
    75,
    68,
    67,
    64,
    52,
    42,
    20,
    -32,
    -75,
    -82,
    -98,
    -100,
    -102,
    -104,
    -105,
    -75,
    28,
]

fig, ax1 = plt.subplots()

print(arraySubtraction(canalB, canalA))

color: str = "tab:red"
ax1.set_xlabel("Frekvenca [MHz]")
ax1.set_ylabel("Amplitudni odziv [dB]", color=color)
ax1.plot(frequency, arraySubtraction(canalB, canalA), color=color)
ax1.tick_params(axis="y", labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color: str = "tab:blue"
ax2.set_ylabel("Fazni odziv []", color=color)  # we already handled the x-label with ax1
ax2.plot(frequency, phase, color=color)
ax2.tick_params(axis="y", labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
