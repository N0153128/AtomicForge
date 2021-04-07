from math import sqrt, ceil, floor
from random import randint
import datetime
from peewee import *
import time


# This class describes Atom's property and mining process
class Atom:

    def __init__(self):
        self.unit = 0

    # This thing here is just for fun
    @staticmethod
    def linear_search(arr, query):
        print(f'Search query: {query}')
        cou = 0
        for i in arr:
            if query == arr[cou]:
                print(f'Result found at: {cou}')
                break
            else:
                pass
            cou += 1

    # decided to go with jump search + random array length, varying from 10 to 50 million elements
    @staticmethod
    def jump_search(arr, query):
        # print(f'Search query: {query}')
        div = int(sqrt(len(arr)))
        i = 0
        found = False
        while not found:
            if i == query:
                # print('found')
                found = True
            elif i > query:
                for j in arr[i-div:i]:
                    if j == query:
                        # print(f'found {j}')
                        found = True
                if not found:
                    # print('Couln\'t Find')
                    break
            i += div
        return found

    # this is how i'm generating arrays
    @staticmethod
    def array_generator(num):
        arr = []
        for i in range(num):
            arr.append(i)
        return arr

    def seek_loop(self):
        atom = 0
        while True:
            if self.jump_search(self.array_generator(5000), randint(10, 500000)):
                atom += 1
                print(f'Total amount of atoms: {atom}')

    def seek_rate(self):
        atom = 0
        timeout = time.time()+60
        result = None
        while True:
            if self.jump_search(self.array_generator(5000), randint(10, 500000)):
                atom += 1
            if time.time() >= timeout:
                break
        if atom > 1000:
            result = round(atom, -3)
        elif atom < 1000:
            result = round(atom, -2)
        print(f'Avg. {result}/pM')

# THIS IS MY PLAYGROUND, DO NOT TOUCH please


atom = Atom()
atom.seek_rate()

# print('Jump search: ')
# start = datetime.datetime.now()
# print(f'Started at: {start}')
# Coin.jump_search(Coin.array_generator(50000000), 49999999)
# elapsed = datetime.datetime.now() - start
# print(f'ended at: {elapsed}')
# print('==========')
# print('Linear search:')
# start = datetime.datetime.now()
# print(f'Started at: {start}')
# Coin.linear_search(Coin.array_generator(50000000), 49999999)
# elapsed = datetime.datetime.now() - start
# print(f'elapsed: {elapsed}')
