#
# @author: DevHeadTech
# 
# Advent of Code - Day 03
#

import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print('Bad Parameters')
#

def convert(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    elif c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27
#

def process(elf):
    global elf_grp

    elf_grp.append(elf)

    if len(elf_grp) != 3:
        return 0
    
    for c in elf_grp[0]:
        if(-1 != elf_grp[1].find(c) and -1 != elf_grp[2].find(c)):
            ret = convert(c);
        #
    #

    elf_grp.clear()
    return ret
#

file = open(sys.argv[1], "r")

elf_grp = []
total = 0 
while ( line := file.readline().strip() ):
    if '' != line:
        total += process(line)
    #
#

print("Priority Sum: ", total)

file.close()
