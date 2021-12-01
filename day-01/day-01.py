#!/usr/local/bin/python3
from collections import defaultdict

# Read in the input into a list.
def read_input():
    lines = []
    with open('./input.txt') as f:
        lines = [int(line.strip()) for line in f.readlines()]

    return lines

# Loops through the list of depths, keeping a running tally of how many
# depths are greater than the previous.
def get_greater_than_previous_count(input):
    previous = None
    count = 0

    for current in input:
        if previous and current > previous:
            count += 1
        previous = current

    return count

def get_greater_than_previous_sliding_window_count(input):
    count = 0
    windows = defaultdict(list)
    current_window = 1

    for current in input:
        # Add this depth to the current window, and the two previous ones.
        windows[current_window].append(current)
        windows[current_window - 1].append(current)
        windows[current_window - 2].append(current)

        # If this is the third depth added to a window, perform the comparison
        if (
            current_window - 3
            and len(windows[current_window - 2]) == 3
            and sum(windows[current_window - 2]) > sum(windows[current_window - 3])
        ):
            count += 1

        current_window += 1

    return count


if __name__ == "__main__":
    input = read_input()

    greater_than_previous = get_greater_than_previous_count(input)

    print(f"{greater_than_previous} depths are greater than the previous depth.")

    greater_than_previous_window = get_greater_than_previous_sliding_window_count(input)

    print(f"{greater_than_previous_window} windows are greater than the previous windows")