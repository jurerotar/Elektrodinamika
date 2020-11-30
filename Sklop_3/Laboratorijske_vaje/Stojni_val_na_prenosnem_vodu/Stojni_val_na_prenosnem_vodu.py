from typing import List, Dict, Any
import matplotlib.pyplot as plt


distances: List[float] = [x for x in range(0, 102, 2)]

measurements: Dict[str, List[float]] = {
    'Odprte sponke': [],
    'Kratki stik': [],
    '50 ohm': [],
    '100 ohm': []
}

plt.xticks(distances)
plt.xlabel("Razdalja [mm]")
plt.ylabel("Amplituda [dB]")
for key, value in measurements.items():
    plt.plot(distances, value, label=key)
plt.legend(measurements, bbox_to_anchor=(1.12, 1), loc="upper right", ncol=1)
plt.show()
