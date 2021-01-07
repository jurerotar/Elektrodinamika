from typing import List
import math
import matplotlib.pyplot as plt

reference_value = 15

frequencies: List[int] = [100*x for x in range(1, 31)]


counter_directional_assembly: List[float] = []
counter_directional_assembly = [
    x - reference_value for x in counter_directional_assembly]

isolation: List[float] = []
isolation = [reference_value - x for x in isolation]


directivity: List[float] = [round(y + x, 2) for x,
                            y in zip(counter_directional_assembly, isolation)]

fig, ax1 = plt.subplots()

plt.title('Smerni sklopnik')
ax1.set_xlabel("Frekvenca [MHz]")
ax1.set_ylabel("Protismerni sklop, Izolacija [dB], Smernost [dB]")
ax1.tick_params(axis="y")
cda, = ax1.plot(frequencies, counter_directional_assembly,
                "tab:red", label='Protismerni sklop')
iso, = ax1.plot(frequencies, isolation, "tab:green", label='Izolacija')
dire, = ax1.plot(frequencies, directivity, "tab:blue", label="Smernost")
plt.legend([cda, iso, dire], ['Protismerni sklop', 'Izolacija', "Smernost"])
fig.tight_layout()
plt.show()
