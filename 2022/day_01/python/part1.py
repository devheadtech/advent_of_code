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
water_mark = 0 
while ( line := file.readline() ):
    if '' != line.strip():
        temp += int(line.strip())
    else:
        #print("New Elf: ", temp)
        if water_mark < temp:
            water_mark = temp
        #
        temp = 0
    #
#

print("Largest Value: ", water_mark)

file.close()
