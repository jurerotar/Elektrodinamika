import matplotlib.pyplot as plt
from typing import Dict, List
import numpy
from scipy.constants import speed_of_light

width = 2.3
length = 1

# prek dimenzij izracunas kriticno frekvenco, pod to frekvenco
# se valovanje ne more siriti


distances: Dict[float, List[float]] = {
    12.5: [],
    12.0: [],
    11.5: [],
    11.0: [],
    10.5: [],
    10.0: [],
    9.5: [],
    9.0: [],
    8.5: [],
    7.5: [],
    7.0: [],
    6.5: [],
}

frequencies: List[float] = [x for x in reversed(distances.keys())]
average_differences: List[float] = [
    round(2 * numpy.mean(abs(numpy.diff(x))), 2) for x in reversed(distances.values())]

plt.xlabel("Frekvenca [GHz]")
plt.ylabel("λg [cm]")
plt.xticks(frequencies)
plt.title('Odvisnost λg od frekvence')

plt.plot(frequencies, [x for x in average_differences], label='λg')

plt.legend(loc='best')
plt.show()
