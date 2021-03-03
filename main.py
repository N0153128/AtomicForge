from math import sqrt
from random import randint
import datetime


class Coin:

    def __init__(self):
        self.unit = 0

    # TODO
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

# decided to go with jump search + random integer
    # TODO
    @staticmethod
    def jump_search(arr, query):
        print(f'Search query: {query}')
        div = int(sqrt(len(arr)))
        print(f'step = {div}, floor: {div//2}')
        i = 0
        found = False
        while not found:
            if i == query:
                print('found')
                found = True
            elif i > query:
                for j in arr[i-div:i]:
                    if j == query:
                        print(f'found {j}')
                        found = True
            i += div

    @staticmethod
    def array_generator(num):
        arr = []
        for i in range(num):
            arr.append(i)
        return arr

# THIS IS MY PLAYGROUND, DO NOT TOUCH please
# Coin.jump_search(Coin.array_generator(10000000), 9999999)
# print(f'Output data: {Coin.bubble(array)}')
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
