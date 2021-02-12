#!/usr/bin/env python3
# -*- config: utf-8 -*-

import timeit


def factorial(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == '__main__':
    r_fib = fib(30)
    r_factorial = factorial(30)

print(f'Результат работы итерактивной функции чисел Фибоначчи(30) = {r_fib}.')
print(f'Время выполнения: {timeit.timeit("r_fib", setup="from __main__ import r_fib")} секунд.')
print(f'Результат работы итерактивной функции факториала(30) = {r_factorial}. ')
print(f'Время выполнения: {timeit.timeit("r_factorial", setup="from __main__ import r_factorial")} секунд.')