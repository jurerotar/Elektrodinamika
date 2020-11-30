import matplotlib.pyplot as plt
import math
from typing import List, Dict

distances: List[int] = range(25)


measurements: Dict[str, Dict[str, List[float]]] = {
    'distiled_water': {
        '8GHz': [],
        '10GHz': [],
        '12GHz': []
    },
    'water': {
        '8GHz': [],
        '10GHz': [],
        '12GHz': []
    }
}

chartToDraw = 'water'

plt.xlabel("Razdalja [mm]")
plt.ylabel("Moč [dB]")
plt.xticks(distances)
plt.title('Distilirana voda' if chartToDraw ==
          'distiled_water' else 'Navadna voda')

for key, xValues in measurements[chartToDraw].items():
    plt.plot([i for i in range(len(xValues))],
             [-1 * x for x in xValues], label=key)

plt.legend(loc='best')
plt.show()
