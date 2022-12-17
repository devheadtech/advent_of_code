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

def process(sack):
    cnt = len(sack)
    lower = sack[:cnt//2]
    upper = sack[cnt//2:]
    
    for c in lower:
        if(-1 != upper.find(c)):
            return convert(c);
        #
    #
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
