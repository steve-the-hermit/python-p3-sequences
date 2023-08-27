#!/usr/bin/env python3



def print_fibonacci(length):
    fib_sequence = [0, 1] if length > 1 else [0] if length == 1 else []
    while len(fib_sequence) < length:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    print(fib_sequence)

    pass