import matplotlib.pyplot as plt
import math
from typing import List


def reflectionToDbm(reflection: float) -> float:
    return round(20 * math.log10(abs(reflection)), 2)


def dbmToWat(num: float) -> float:
    return round(10 ** (-1 * num / 10), 6)


def watToReflection(currentPower: float, maximumPower: float) -> float:
    return 4 * math.sqrt(currentPower / maximumPower)


def convertPower(array: list) -> list:
    returnArray: List[List[float]] = []
    for arr in array:
        returnArray.append([dbmToWat(value) for value in arr])
    return returnArray


def convertAveragePower(array: list) -> float:
    returnArray = []
    for dataset in array:
        dataset = dataset[:2]
        returnArray.append(sum(dataset) / 2)
    return returnArray


def convertPowerToReflection(
    powerAverages: List[float], powerValues: List[List[float]]
) -> List[List[float]]:
    returnArray: List[List[float]] = []
    for index, arr in enumerate(powerValues):
        returnArray.append(
            [
                reflectionToDbm(watToReflection(value, powerAverages[index]))
                for value in arr
            ]
        )
    return returnArray


frequencies: List[int] = [100, 500, 1000, 1500, 2000]
labels: List[str] = [
    "Kratek stik",
    "Odp. sponke",
    "Prilag. breme",
    "Slabilnik #1",
    "Slabilnik #2",
    "Slabilnik #3",
    "Slabilnik #4",
    "Slabilnik #5",
]

powerInDBm: List[List[float]] = [

]

powerInWats: List[List[float]] = convertPower(powerInDBm)

averages: List[float] = convertAveragePower(powerInWats)
averages = [16 * x for x in averages]

reflections: List[List[float]] = convertPowerToReflection(
    averages, powerInWats)

print("Moč [W]")
print(powerInWats)
print("")
print("Povprečna moč [W]")
print(averages)
print("")
print("Odbojnost [dB]")
print(reflections)

plt.xticks(frequencies)
plt.xlabel("Frekvenca [MHz]")
plt.ylabel("Odbojnost [dB]")
for xe, ye in zip(frequencies, reflections):
    plt.scatter([xe] * len(ye), ye, c="gray", s=1)
plt.plot(frequencies, reflections)
plt.legend(labels, bbox_to_anchor=(1.12, 1), loc="upper right", ncol=1)
plt.show()
