# I'm currently trying to find what a miner could do to give Coins for

from math import sqrt


class Coin:

    def __init__(self):
        self.unit = 0

    @staticmethod
    def primes():
        result = []
        ii = 0
        while True:
            prime = True
            for i in range(2, ii):
                if ii % i == 0:
                    prime = False
                    break
            if prime:
                result.append(ii)
                print(ii)
            ii += 1

    @staticmethod
    def square():
        i = 10000
        while True:
            print(int(sqrt(i)))
            i += 1

    @staticmethod
    def bubble(arr):
        print(f'Original input data: {arr}')
        for i in range(len(arr)):
            for j in range(len(arr)):
                try:
                    if arr[j] > arr[j+1]:
                        reserve = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = reserve
                except IndexError:
                    pass
        return arr

    # TODO
    # @staticmethod
    # def merge_sort(arr):

    # TODO
    # @staticmethod
    # def quick_sort(arr):

    # TODO
    # @staticmethod
    # def binary_search(arr):

    # TODO
    # @staticmethod
    # def insertion_sort(arr):

    # TODO
    # @staticmethod
    # def selection_sort(arr):

    # TODO
    # @staticmethod
    # def shell_sort(arr):

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
                print('Not found')
            cou += 1

    # TODO
    @staticmethod
    def jump_search(arr, query):
        cou = 0
        div = 2

        if len(arr) % 2 == 0:
            if len(arr) > 10:
                div = 8
            elif len(arr) > 100:
                div = 16
            elif len(arr) > 1000:
                div = 32
        else:
            if len(arr) > 10:
                div = 10
            elif len(arr) > 100:
                div = 20
            elif len(arr) > 1000:
                div = 30

        print(f'step = {div}, floor: {div//2}')
        for i in arr[::div]:
            print(i, cou)
            if i == query:
                print(f'Found at {cou}, {i}')
            elif i > query:
                print('almost there')
                for j in arr[cou-3:i:div//2]:
                    print(j, arr.index(j))
                    if j == query:
                        print(f'Found {j} at {cou}')
                        break
                break
            cou += 3

    @staticmethod
    def array_generator(num):
        arr = []
        for i in range(num):
            arr.append(i)
        return arr


# print(f'Output data: {Coin.bubble(array)}')
print(f'{Coin.jump_search(Coin.array_generator(100), 92)}')
