input = open('inputs/' + __file__.split('\\')[-1].split('.')[0] + '.txt', 'r').read()
input_groups_1 = [group.replace('\n', '') for group in input.split('\n\n')]
input_groups_2 = [[list(person) for person in group.split('\n')] for group in input.split('\n\n')]
print(input_groups_2)

# part 1
total = 0
for group in input_groups_1: total += len(set(group))
print('part 1: ' + str(total))


# part 2
total = 0
for group in input_groups_2:
    final = set(group[0])
    for person in group[1:]: final.intersection_update(person)
    total += len(final)
print('part 2: ' + str(total))