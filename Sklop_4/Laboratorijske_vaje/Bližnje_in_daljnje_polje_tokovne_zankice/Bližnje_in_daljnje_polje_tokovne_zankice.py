from typing import List, Dict, Tuple
import matplotlib.pyplot as plt

distances: List[int] = [10*x for x in range(1, 12)]

measurements: Dict[str, Dict[int, List[float]]] = {
    'Ista ravnina': {
        300: [],
        100: [],
        30: []
    },
    'Ista os': {
        300: [],
        100: [],
        30: []
    }
}

plt.xlabel("Razdalja [cm]")
plt.ylabel("Pspr [dBm]")
plt.xticks(distances)
plt.title('Slabljenje med zankicama v isti osi')

# For charts with same key

for key, measurement in measurements['Ista os'].items():
    plt.plot(distances, measurement,
             label=f'Slabljenje pri frekvenci {key} MHz')

# For chart with same frequency
'''
for measurement_type in ['Ista ravnina', 'Ista os']:
    plt.plot(distances, measurements[measurement_type][100],
             label='Slabljenje na isti ravnini' if measurement_type == 'Ista ravnina' else 'Slabljenje na isti osi')
'''

plt.legend(loc='best')
plt.show()
