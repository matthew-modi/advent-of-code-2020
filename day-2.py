import time
start = time.time()


input = open('inputs/' + __file__.split('\\')[-1].split('.')[0] + '.txt', 'r')
input_lines = [{'freq_min': int(line.rstrip().split(' ')[0].split('-')[0]), 
                'freq_max': int(line.rstrip().split(' ')[0].split('-')[1]), 
                'letter': line.rstrip().split(' ')[1].split(':')[0], 
                'password': line.rstrip().split(' ')[2]} for line in input]

# part 1
valid = 0
for line in input_lines:
    if line['freq_min']<=line['password'].count(line['letter'])<=line['freq_max']:
        valid += 1
print('part 1: ' + str(valid))

# part 2
valid = 0
for line in input_lines:
    if (line['password'][line['freq_min']-1] == line['letter']) != (line['password'][line['freq_max']-1] == line['letter']):
        valid += 1
print('part 2: ' + str(valid))


end = time.time()
print('complete in ' + str(end-start) + ' seconds')