#!/usr/bin/python

import argparse


def find_max_profit(prices):
    if len(prices) > 1:
        # Step 1: Set cur_index and max_profit variables
        cur_index = 0
        max_profit = prices[1] - prices[0]

    # Step 2: Loop through the array, subtracting cur_value from later values and saving max profit to max_profit variable
        while cur_index < len(prices) - 1:
            cur_value = prices[cur_index]
            for i in range(cur_index + 1, len(prices)):
                if prices[i] - cur_value > max_profit:
                    max_profit = prices[i] - cur_value
            cur_index += 1

    # Step 3: Return max_profit
        return max_profit
    else:
        return -1


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
