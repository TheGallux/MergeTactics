from math import floor
from random import randint
import datetime

from meta2 import *

def heuristique(L):

    # get sum of traits of powers
    D = {}
    for carte in L:
        for trait in perso_traits[carte]:
            D[trait] = D.get(trait, 0) + 1
    for k in D:
        D[k] //= 2
    D = dict(filter(lambda x: x[1] != 0, D.items()))
    for k in D:
        D[k] -= 1
    power_traits = sum(force_traits[perso][D[perso]] for perso in D)

    # get sum of troops powers
    power_troops = sum(force_perso[perso] for perso in L)

    return power_traits + power_troops

def get_random_config(lenght: int) -> list[str]:
    L = []
    while len(L) != lenght:
        n = randint(0, len(cartes) - 1)
        if not(cartes[n] in L):
            L.append(cartes[n])

    return L

def mutate(config: list[str]):
    new = config[0]
    for i in range(randint(1, 3)):
        while (new in config):
            new = cartes[randint(0, len(cartes) - 1)]
        config[randint(0, len(config) - 1)] = new

    return config

def evolve(configs):
    n = len(configs)
    configs = sorted(configs, key=heuristique, reverse=True)[n-1:]
    for i in range(n-1):
        configs.append(mutate(list(configs[i])))

    return configs

univers = [get_random_config(6) for _ in range(1000)]
for i in range(100):
    if (i % 1000 == 0):
        print(i)
    univers = evolve(univers)

univers = sorted(univers, key=heuristique, reverse=True)

current_time = datetime.datetime.now().strftime("%H_%M_%S")

filename = f"merge_tactics_{current_time}.txt"

with open(filename, "w", encoding="utf-8") as file:
    for item in univers:
        file.write(", ".join(sorted(item) + [str(heuristique(item))]) + "\n")

print(f"File '{filename}' created successfully with {len(univers)} items.")