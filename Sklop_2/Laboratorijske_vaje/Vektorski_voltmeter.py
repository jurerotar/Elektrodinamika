import matplotlib.pyplot as plt
import math
from typing import List, Dict


def arraySubtraction(array1: List[float], array2: List[float]) -> List[float]:
    return [array1[i] - array2[i] for i in range(len(array1))]


frequency: List[float] = [

]

canalA: List[float] = [

]

canalB: List[float] = [

]

phase: List[float] = [

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
# we already handled the x-label with ax1
ax2.set_ylabel("Fazni odziv []", color=color)
ax2.plot(frequency, phase, color=color)
ax2.tick_params(axis="y", labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
