import re


input = open('inputs/' + __file__.split('\\')[-1].split('.')[0] + '.txt', 'r')
input_passports = [[field.split(':') for field in re.split(' |\n', passport)] for passport in input.read().split('\n\n')]


# part 1
fields = [
    'byr', 
    'iyr', 
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]

valid = 0
for passport in input_passports:
    if all(field in [item[0] for item in passport] for field in fields):
        valid += 1

print('part 1: ' + str(valid))


# part 2
present_list = []
for passport in input_passports:
    if all(field in [item[0] for item in passport] for field in fields):
        if [''] in passport: 
            new = passport
            new.remove([''])
            present_list.append({field[0]: field[1] for field in new})
        else:
            present_list.append({field[0]: field[1] for field in passport})

ecl = [
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
]

valid = 0
for passport in present_list:
    if not 1920<=int(passport['byr'])<=2002:
        continue
    if not 2010<=int(passport['iyr'])<=2020:
        continue
    if not 2020<=int(passport['eyr'])<=2030:
        continue
    if not ((passport['hgt'][-2:] == 'cm' and 150<=int(passport['hgt'][0:-2])<=193)
        or (passport['hgt'][-2:] == 'in' and 59<=int(passport['hgt'][0:-2])<=76)):
        continue
    if not (re.match('#[a-f|0-9]{6}', passport['hcl']) is not None and len(passport['hcl']) == 7):
        continue
    if not (passport['ecl'] in ecl):
        continue
    if not (re.match('[0-9]{9}', passport['pid']) is not None and len(passport['pid']) == 9):
        continue
    valid += 1

print('part 2: ' + str(valid))
