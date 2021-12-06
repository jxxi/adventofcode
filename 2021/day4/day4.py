import sys

def main():
    with open(sys.argv[1]) as file:
        data = [line.strip() for line in file if line.strip()]

    drawings = data[0]
    boards = [][]
    lines = 0
    for count,line in data[1:]:
        if lines

    print(draw)
    print(boards)

main()