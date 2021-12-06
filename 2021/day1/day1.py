import sys

def calculateIncreases(previous, current):
    increases = 0
    for (prev, cur) in zip(previous, current):
        if prev < cur:
            increases +=1

    return increases


def part1(measurements):
    current = measurements[1:]
    previous = measurements[:-1]
    
    return calculateIncreases(previous, current)


def part2(measurements):
    three_measurements = [sum(measurements[i:i+3]) for i in range(len(measurements) - 2)]

    previous = three_measurements[:-1]
    current = three_measurements[1:]

    return calculateIncreases(previous, current)


def main():
    with open(sys.argv[1]) as file:
        measurements = [int(line) for line in file]

    print(part1(measurements))
    print(part2(measurements))

main()