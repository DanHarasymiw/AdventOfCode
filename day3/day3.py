def check(sides):
    half_sum = sum(sides) / 2.0
    triangle = True
    for side in sides:
        if side >= half_sum:
            triangle = False
            break

    return triangle


def part_a(input):
    count = 0
    for sides in input:
        if check(sides):
            count += 1

    print count


def part_b(input):
        row = 0
        column = 0
        count = 0

        for i in range(len(input)):

            sides = [input[row][column], input[row+1][column], input[row+2][column]]
            row += 3

            if (row >= len(input_list)):
                row = 0
                column += 1

            if check(sides):
                count += 1

        print count


with open('day3.txt') as f:
    input_list = []
    for line in f.readlines():
        input_list.append([int(side) for side in line.split()])

part_a(input_list)
part_b(input_list)