from typing import List

import matplotlib.pyplot as plt

odprte_sponke: List[float] = []
kratek_stik: List[float] = []
odprte_sponke: List[float] = [-x for x in odprte_sponke]
kratek_stik: List[float] = [-x for x in kratek_stik]

frequencies: List[int] = range(20, 1320, 20)

plt.xlabel("Frekvenca [MHz]")
plt.ylabel("Moč [dBm]")
plt.xticks([x for index, x in enumerate(frequencies) if index % 5 == 0])
plt.title('Izmerjena moč v odvisnosti od frekvence')

plt.plot(frequencies, odprte_sponke, label='Odprte sponke')
plt.plot(frequencies, kratek_stik, label='Kratek stik')

plt.legend(loc='best')
plt.show()
