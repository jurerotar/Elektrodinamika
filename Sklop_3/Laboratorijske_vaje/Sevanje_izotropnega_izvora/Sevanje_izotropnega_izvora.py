import matplotlib.pyplot as plt
import math
from typing import List,  Tuple


def md_table_row(values: Tuple[int, float, float]) -> str:
    return f"| {' | '.join([f'{value}' for value in values])} | \n"


distances: List[float] = [x for x in range(1, 41)]

# Zarnica z nitko
measurements1: List[int] = [
]

# Ledica
measurements2: List[int] = [
]


chartToDraw = 2

fig, ax1 = plt.subplots()

color: str = "tab:red"
ax1.set_xlabel("Razdalja [cm]")
ax1.set_ylabel("Osvetljenost [Lux]", color=color)
ax1.plot(distances, measurements1 if chartToDraw ==
         1 else measurements2, color=color)
ax1.tick_params(axis="y", labelcolor=color)

ax2 = ax1.twinx()

color: str = "tab:blue"
ax2.set_yscale('log')
ax2.set_ylabel("Osvetljenost [Lux]", color=color)
ax2.plot(distances, measurements1 if chartToDraw ==
         1 else measurements2, color=color)
ax2.tick_params(axis="y", labelcolor=color)

fig.tight_layout()
plt.show()
