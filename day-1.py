input = open('inputs/' + __file__.split('\\')[-1].split('.')[0] + '.txt', 'r')
input_lines = [int(line.rstrip()) for line in input]

# part 1
for line in input_lines: 
    if (2020-line) in input_lines: 
        print('part 1: ' + str(line * (2020-line)))
        break

# part 2
for line in input_lines:
    for sub_line in input_lines:
        if (2020-line-sub_line) in input_lines:
            print('part 2: ' + str(line * sub_line * (2020-line-sub_line)))
            quit()
