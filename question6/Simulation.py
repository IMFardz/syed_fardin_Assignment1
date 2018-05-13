"""Simulation of game as defined by question"""
from Ship import Ship
from Speeder import Speeder
from Warship import Warship
import random as rm


if __name__ == "__main__":
    live_ships = []
    names = ['ship1', 'ship2', 'ship3', 'speeder', 'warship']

    Ship1 = Ship(names[0])
    live_ships.append(Ship1)
    Ship2 = Ship(names[1])
    live_ships.append(Ship2)
    Ship3 = Ship(names[2])
    live_ships.append(Ship3)
    Ship4 = Speeder(names[3])
    live_ships.append(Ship4)
    Ship5 = Warship(names[4])
    live_ships.append(Ship5)

    while len(live_ships) != 1:
        print("Current ships are:")
        for i in live_ships:
            print(i)
        i = rm.randint(0, len(live_ships) - 1)
        j = rm.randint(0, len(live_ships) - 1)
        print()
        while j == i:  # Ensures a ship cannot attack itself
            j = rm.randint(0, len(live_ships) - 1)
        live_ships[i].attack(live_ships[j])
        print("{} attacked {}".format(live_ships[i].name, live_ships[j].name))
        print()
        if not live_ships[j].alive:
            print('{} has died'.format(live_ships[j]))
            live_ships.remove(live_ships[j])
            print()

    print("The winner is {}".format(live_ships[0].name))
