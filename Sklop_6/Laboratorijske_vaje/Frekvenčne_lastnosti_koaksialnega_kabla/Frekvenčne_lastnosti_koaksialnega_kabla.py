import math
from typing import List

import matplotlib.pyplot as plt


def phase_shift(phase: int, frequency: int) -> float:
    return phase + 360 * math.floor(frequency / 1.952)


frequencies: List[int] = []

canal_A_amplitudes: List[float] = []

canal_B_amplitudes: List[float] = []

phases: List[int] = []

shifted_phases: List[float] = [phase_shift(
    x[0], x[1]) for x in zip(phases, frequencies)]

weakening: List[float] = [
    round(x - y, 2) for x, y in zip(canal_A_amplitudes, canal_B_amplitudes)
]


fig, ax1 = plt.subplots()

ax1.set_xlabel("Frekvenca [MHz]")
ax1.set_ylabel("Slabljenje kabla [dB]")
wkn, = ax1.plot(
    frequencies, weakening, "tab:red", label='Slabljenje kabla'
)
ax1.tick_params(axis="y")

ax2 = ax1.twinx()

ax2.set_ylabel("Fazni zasuk [°]")
ph, = ax2.plot(frequencies, shifted_phases, "tab:blue", label="Fazni zasuk")
ax2.tick_params(axis="y")

plt.legend([wkn, ph], ['Slabljenje kabla', 'Fazni zasuk'])
fig.tight_layout()
plt.show()
