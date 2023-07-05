#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def wallis_multiplier(i):
    i_squared_times_4 = 4 * i * i
    return i_squared_times_4 / (i_squared_times_4 - 1)


def calculate_wallis_product(eps):
    convergence_sequence = []
    i, p, p_old = 1, 1.0, 0
    while abs(p - p_old) >= eps:
        p_old = p
        p *= wallis_multiplier(i)
        convergence_sequence.append(p * 2.0)
        i += 1
    return p * 2.0, convergence_sequence


def visualize_convergence(sequence):
    fig, ax = plt.subplots()
    ax.scatter(
        range(len(sequence)),
        sequence,
        s = 1,
    )
    ax.set(
        ylim=(3.1, 3.15),
        xlabel = 'Iterations',
        ylabel = 'Wallis Product value',
        title = 'Pi Convergence plot',
    )
    plt.grid(alpha=0.7)
    plt.savefig('./img/convergence_plot.png')
    plt.show()


if __name__ == '__main__':
    pi_value, conv_seq = calculate_wallis_product(1e-7)
    print('Pi calculated with Wallis product:', pi_value)
    visualize_convergence(conv_seq)
