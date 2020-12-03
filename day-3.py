import time
start = time.time()


input = open('inputs/' + __file__.split('\\')[-1].split('.')[0] + '.txt', 'r')
tree_rows = [list(line.rstrip()) for line in input]
width = len(tree_rows[0])

# part 1
trees = 0
x = 0
for y in range(len(tree_rows)):
    if tree_rows[y][x%width] == '#':
        trees += 1
    x+=3

print('part 1: ' + str(trees))


# part 2
slope_set = [
    [1, 1], 
    [3, 1], 
    [5, 1], 
    [7, 1],
    [1, 2]
]
results = []

for slopes in slope_set: 
    trees = 0
    x = 0
    for y in range(len(tree_rows)):
        if slopes[1]*y > len(tree_rows):
            break
        if tree_rows[slopes[1]*y][x%width] == '#':
            trees += 1
        x += slopes[0]
    results.append(trees)

total = 1
for num in results:
    total = num * total
print('part 2: ' + str(total))


end = time.time()
print('complete in ' + str(end-start) + ' seconds')