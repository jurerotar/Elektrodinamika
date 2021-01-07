from typing import List, Dict, Tuple
import matplotlib.pyplot as plt
import math

# na podlagi grafa ugotovi kaksno sito imamo:
# nizkofrekvenco, visokofrekvenco, band stop, band pass

frequencies: List[int] = [x for x in range(400, 1250, 50)]

measurements: Dict[str, Tuple[float, int]] = {
    's_11': [],
    'p_11': [],

    's_12': [],
    'p_12': [],

    's_21': [],
    'p_21': [],

    's_22': [],
    'p_22': [],
}

plt.xlabel("Frekvenca [MHz]")
plt.ylabel("Odziv [dB]")
plt.xticks(frequencies)
plt.title('Odziv')

for key, measurement in measurements.items():
    if(key.startswith(('s'))):
        plt.plot(frequencies, [20 * math.log10(abs(x)) if x != 0 else 20 * math.log10(abs(0.001))
                               for x in measurement], label=key.replace('_', '').upper())

plt.legend(loc='best')
plt.show()
