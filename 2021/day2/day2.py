import sys

def part1(instructions):
    horizontal = 0
    depth = 0
    for current in instructions:
        direction = current[0]
        move = current[1]
        
        if direction == 'forward':
            horizontal += move
        elif direction == 'down':
            depth += move
        elif direction == 'up':
            depth -= move

    answer = horizontal * depth
    return answer


def part2(instructions):
    horizontal = 0
    depth = 0
    aim = 0

    for current in instructions:
        direction = current[0]
        move = current[1]
        
        if direction == 'forward':
            horizontal += move
            depth += aim*move
        elif direction == 'down':
            aim += move
        elif direction == 'up':
            aim -= move

    answer = horizontal * depth
    return answer


def main():
    instructions = []
    directions = []
    amounts = []
    with open(sys.argv[1]) as file:
        for line in file:
            direction,amount = line.split()
            directions.append(direction)
            amounts.append(int(amount))

    instructions = list(zip(directions, amounts))

    print(part1(instructions))
    print(part2(instructions))

main()