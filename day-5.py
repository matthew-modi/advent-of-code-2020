input = open('inputs/' + __file__.split('\\')[-1].split('.')[0] + '.txt', 'r')
passes = [list(boarding_pass) for boarding_pass in input.read().split('\n')]

# part 1
def iterate(steps, right, dist): return int(right-1) if len(steps) == 0 else iterate(steps[1:], right-dist if steps[0] == '0' else right, dist/2)
print('part 1: ' + str(max([iterate([item.translate(str.maketrans('FB', '01')) for item in boarding_pass[:7]], 128, 64)*8+iterate([item.translate(str.maketrans('LR', '01')) for item in boarding_pass[-3:]], 8, 4) for boarding_pass in passes])))

# part 2
ids = [iterate([item.translate(str.maketrans('FB', '01')) for item in boarding_pass[:7]], 128, 64)*8+iterate([item.translate(str.maketrans('LR', '01')) for item in boarding_pass[-3:]], 8, 4) for boarding_pass in passes]
print('part 2: ' + str([id for id in range(min(ids), max(ids)) if id not in ids][0]))