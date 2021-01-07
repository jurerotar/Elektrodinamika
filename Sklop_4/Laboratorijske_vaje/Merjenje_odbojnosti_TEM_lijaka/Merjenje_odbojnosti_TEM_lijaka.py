from typing import List, Dict
import math
import matplotlib.pyplot as plt

# convert values to reflection, average them, then convert back to log


def avg(value_1: float, value_2: float) -> float:
    return round(sum((logToWat(value_1), logToWat(value_2)))/2, 2)


def reflectionToLog(value: float) -> float:
    return 20 * math.log10(abs(value))


def logToWat(value: float) -> float:
    return 10**((value) / 10)


def watToLog(value: float) -> float:
    return 10 * math.log10(abs(value))


frequencies: List[int] = [100*x for x in range(1, 21)]

reflections: Dict[str, List[float]] = {
    'Odprte sponke': [],
    'Kratki stik': [],
    '50ohm': []
}

# potrebujemo graf in na podlagi grafa ugotovimo obmocje, kjer antena najboljse dela

p_max: List[float] = [avg(value[0], value[1]) for value in zip(
    reflections['Odprte sponke'], reflections['Kratki stik'])]


p: List[float] = [
    round(reflectionToLog(math.sqrt(logToWat(val[0]) / val[1])), 2) for val in zip(reflections['50ohm'], p_max)]


plt.xlabel("Frekvenca [MHz]")
plt.ylabel("Odbojnost [dB]")
plt.xticks(frequencies)
plt.title('Odbojnost TEM lijaka')


plt.plot(frequencies, p, label="Odbojnost")

plt.legend(loc='best')
plt.show()
