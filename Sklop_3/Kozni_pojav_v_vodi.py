import matplotlib.pyplot as plt
import math
from typing import List, Dict

distances: List[int] = range(25)


measurements: Dict[str, Dict[str, List[float]]] = {
    'distiled_water': {
        '8GHz': [26.33, 29.83, 31.83, 34.67, 37.17, 39.67, 42.83, 45.17, 47.82, 51.33, 52, 53, 54.33, 56.83, 59.83, 62.42, 64.17, 65.82, 67.42, 68.00, 70.17, 70.33, 72.83, 73.83, 74.84],
        '10GHz': [24.5, 30, 33.33, 37.83, 42.0, 45.16, 48.83, 52.33, 56.00, 59.33, 63.17, 67.33, 69.67, 69.67, 72.50, 73.83],
        '12GHz': [38.67, 43.5, 46.33, 52.33, 56.5, 61.83, 62.67, 71.67, 72.00, 72.19, 73.83]
    },
    'water': {
        '8GHz': [26.50, 28.83, 31.17, 34.33, 36.67, 39.00, 40.82, 43.50, 45.50, 47.83, 49.67, 51.67, 54.83, 57.33, 58.50, 60.17, 62.17, 67.67, 68.67, 68.83, 69.83, 71.67, 76.67],
        '10GHz': [23.50, 27.33, 30.5, 34.33, 37.17, 40.82, 46.00, 49.83, 52.67, 54.83, 57.67, 62.83, 65.50, 66.33, 67.83, 70.83, 74.33, 76.00],
        '12GHz': [35.17, 40.17, 45.33, 49.33, 53.17, 56.83, 63.17, 66.33, 69.67, 71.50, 76.82]
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
