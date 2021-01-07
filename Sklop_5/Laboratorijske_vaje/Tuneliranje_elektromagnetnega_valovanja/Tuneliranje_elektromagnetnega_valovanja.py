from typing import List, Dict, Tuple
import matplotlib.pyplot as plt

distances: List[float] = [round(x/10, 2) for x in range(0, 55, 5)]

measurements: Dict[str, Dict[int, List[float]]] = {
    'Odbiti': {
        # Magnetno polje vzporedno z mejno ploskvijo
        'TM': [],
        # Električno polje vzporedno z mejno ploskvijo
        'TE': [],
    },
    'Tuneliran': {
        # Magnetno polje vzporedno z mejno ploskvijo
        'TM': [],
        # Električno polje vzporedno z mejno ploskvijo
        'TE': [],
    }
}

plt.xlabel("Razmik med prizmama [cm]")
plt.ylabel("Moč vala [dBm]")
plt.xticks(distances)
plt.title('Primerjava tuneliranega TE in odbitega TE vala')

plt.plot(distances, measurements['Odbiti']['TE'], label='Odbiti TE')
plt.plot(distances, measurements['Tuneliran']['TE'], label='Tuneliran TE')

plt.legend(loc='best')
plt.show()
