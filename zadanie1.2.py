#!/usr/bin/env python3
# -*- config: utf-8 -*-

from functools import lru_cache
import timeit


@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


@lru_cache
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    r_fib = fib(30)
    r_factorial = factorial(30)

print(f'Результат работы рекурсивной функции чисел Фибоначчи(30) = {r_fib}.')
print(f'Время выполнения: {timeit.timeit("r_fib", setup="from __main__ import r_fib")} секунд.')
print(f'Результат работы рекурсивной функции факториала(30) = {r_factorial}. ')
print(f'Время выполнения: {timeit.timeit("r_factorial", setup="from __main__ import r_factorial")} секунд.')
