import matplotlib.pyplot as plt
from typing import Dict, List

distances: List[int] = [-9, -7, -5, -3, -1, 0, 1, 3, 5, 7, 9]

measurements: Dict[str, Dict[str, List[float]]] = {
    'Prečna': {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': [],
    },
    'Vzdolžna': {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': [],
    },
}

plt.xlabel("Odmik po x [cm]")
plt.ylabel("Jakost magnetnega polja [dBm]")
plt.xticks(distances)

toDraw = 'Prečna'

plt.title(f'{toDraw} komponenta magnetnega polja')

# For charts with same key

for key, measurement in measurements[toDraw].items():
    plt.plot(distances, measurement, label=f'{key}')

plt.legend(loc='best')
# plt.show()
