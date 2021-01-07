from typing import Dict, List

import matplotlib.pyplot as plt

distances: List[int] = range(25)

# Vse meritve so z minuso
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
plt.ylabel("Moč [dBm]")
plt.xticks(distances)
plt.title('Primerjava slabljenja pri 8 GHz v navadni in destilirani vodi')

'''
for key, xValues in measurements[chartToDraw].items():
    plt.plot([i for i in range(len(xValues))], xValues, label=key)
'''

for key, value in measurements.items():
    val = value['8GHz']
    plt.plot([i for i in range(len(val))], val, label=key.replace(
        'distiled_', 'Distilirana ').replace('water', 'voda'))


plt.legend(loc='best')
plt.show()
