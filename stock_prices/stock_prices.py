#!/usr/bin/python

import argparse


def find_max_profit(prices):
    if type(prices) == list:
        if len(prices) != 1 and len(prices) != 0:
            max_profit = prices[1] - prices[0]
            for i in range(len(prices) - 1, 1, -1):
                cur_index = i - 1
                while cur_index >= 0:
                    if prices[i] - prices[cur_index] > max_profit:
                        max_profit = prices[i] - prices[cur_index]
                    cur_index -= 1
            return max_profit
        else:
            return 'At least two items must be in the list.'
    else:
        return 'Only accepts a list as a parameter'


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
