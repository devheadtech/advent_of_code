#
# @author: DevHeadTech
# 
# Advent of Code - Day 01
#

import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print('Bad Parameters')
#

file = open(sys.argv[1], "r")

temp = 0
top = []
while ( line := file.readline() ):
    if '' != line.strip():
        temp += int(line.strip())
    else:
        #print("New Elf: ", temp)
        top.append(temp)
        top.sort(reverse=True)
        if( len(top) > 3):
            top.pop()
        #
        temp = 0
    #
#

print("Top Three Sum: ", top[0] + top[1] + top[2])

file.close()
