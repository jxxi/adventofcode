import sys
from collections import Counter

def main():
    with open(sys.argv[1]) as file:
        data = file.read().split("\n")

    data = [
        [tuple(int(n) for n in pair.split(",")) for pair in segment]
        for segment in [line.split(" -> ") for line in data]
    ]

    # Find all coordinates
    points = []
    for i, segment in enumerate(data):
        x_positions = (segment[0][0], segment[1][0])
        y_positions = (segment[0][1], segment[1][1])

        x_difference = x_positions[1] - x_positions[0]
        y_difference = y_positions[1] - y_positions[0]

        x_sign = -1 if x_difference < 0 else 1
        y_sign = -1 if y_difference < 0 else 1

        x_range = range(x_positions[0], x_positions[1] + x_sign, x_sign)
        y_range = range(y_positions[0], y_positions[1] + y_sign, y_sign)

        #horizontal
        if x_positions[0] == x_positions[1]:
            points += [(x_positions[0], y) for y in y_range]

        #vertical
        elif y_positions[0] == y_positions[1]:
            points += [(x, y_positions[0]) for x in x_range]

        #diagonal
        else:
            points += [(x, y) for x,y in zip(x_range, y_range)]

    # Find repeated coordinates/intersections
    counts = Counter(points)
    intersections = [point for point in counts if counts[point] > 1]

    print(len(intersections))


if __name__ == "__main__":
    main()
