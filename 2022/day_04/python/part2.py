#
# @author: DevHeadTech
# 
# Advent of Code - Day 04
#

import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print('Bad Parameters')
#

def process(assignment):
    elf1 = assignment.split(',')[0].split('-')
    elf2 = assignment.split(',')[1].split('-')

    #string conversion
    elf1[0] = int(elf1[0])
    elf1[1] = int(elf1[1])
    elf2[0] = int(elf2[0])
    elf2[1] = int(elf2[1])

    if elf1[0] >= elf2[0] and elf1[0] <= elf2[1]:
        return 1
        
    if elf1[1] >= elf2[0] and elf1[1] <= elf2[1]:
        return 1

    if elf2[0] >= elf1[0] and elf2[0] <= elf1[1]:
        return 1
        
    if elf2[1] >= elf1[0] and elf2[1] <= elf1[1]:
        return 1
    
    return 0
#

file = open(sys.argv[1], "r")

total = 0 
while ( line := file.readline().strip() ):
    if '' != line:
        total += process(line)
    #
#

print("Priority Sum: ", total)

file.close()
