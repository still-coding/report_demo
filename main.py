#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


convergence_sequence = []

def wallis_multiplier(i):
    return (4 * i * i) / (4 * i * i - 1)


def calculate_wallis_product(eps):
    i = 1
    p = 1
    while True:
        m = wallis_multiplier(i)
        if abs(p - m * p) < eps:
            break
        p *= m
        convergence_sequence.append(p*2)
        i += 1
    return p * 2


def visualize_convergence():
    fig, ax = plt.subplots()
    ax.scatter(
        range(len(convergence_sequence)),
        convergence_sequence,
        s = 1
    )
    ax.set(
        ylim=(3.1, 3.15),
        xlabel = 'Iterations',
        ylabel = 'Wallis Product value',
        title = 'Pi Convergence plot',

    )
    plt.show()


if __name__ == '__main__':
    print(calculate_wallis_product(1e-7))
    visualize_convergence()

# https://matplotlib.org/cheatsheets/