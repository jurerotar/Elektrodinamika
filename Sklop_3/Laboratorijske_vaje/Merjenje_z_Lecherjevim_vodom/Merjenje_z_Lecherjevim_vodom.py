from typing import List, Tuple, Any
import math
from scipy.constants import speed_of_light
from numpy import diff, mean
import itertools


def frequency(wave_length: float) -> float:
    return speed_of_light / wave_length


def average_difference(dataset: List[float], amount_of_missing_values: int = 0) -> float:
    return mean(diff(dataset)) if len(dataset) > 1 else dataset[0] / (amount_of_missing_values + 1)


dataset: List[List[Tuple[float, int]]] = [
    [
        [], 0
    ],
    [
        [], 0
    ],
    [
        [], 0
    ],
    [
        [], 0
    ],
    [
        [], 0
    ],
    [
        [], 0
    ],
    [
        [], 0
    ],
    [
        [], 0
    ],
    [
        [], 0
    ],
    [
        [], 0
    ],
]

frequencies: List[float] = []
wave_lengths: List[float] = []


for arr in dataset:
    arr[0]: List[float] = [(20 + x) / 100 for x in arr[0]]
    wave_length: float = average_difference(arr[0], arr[1]) * 2
    wave_lengths.append(math.floor(wave_length))
    # print(wave_length)
    freq: float = round(frequency(wave_length), 2)
    frequencies.append(math.floor(freq))
    print(f"{freq:.3}")

print(f"{mean(diff(frequencies)):.3}")

'''
md_array = []


def create_table_head(header: List[Any]) -> str:
    return f"| {' | '.join([f'{value}' for value in header])} | \n |{':---:|'*len(header)} \n"


def create_table_row(values: List[Any]) -> str:
    return f"| {' | '.join([f'{value}' for value in values])} | \n"


md_array.append([x for x in range(9)])
md_array.append([])
md_array.append(wave_lengths)
md_array.append(frequencies)

table = create_table_head(['Odmik', 'Izmerjene vrednosti [cm]',
                           'Izračunane valovne dolžine [m]', 'Izračunane frekvence [Hz]'])
transposed_array = itertools.zip_longest(*md_array)
for i in transposed_array:
    table += create_table_row(i)


print(table)
'''
