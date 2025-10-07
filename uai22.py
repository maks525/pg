import os 
where_i_am = os.getcwd()+'/'

file = open(f'{where_i_am}HW02_cypher.txt', 'r').read().split('\n')[:-1]
my_shift = open(f'{where_i_am}HW02_shifts.txt', 'r').read().split('\n')[:-1]

for row_id in range(len(file)):
    for letter in file[row_id]:
        print(chr(ord(letter) - int(my_shift[row_id])), end='')
    print()