#
# @author: DevHeadTech
# 
# Advent of Code - Day 02
#

import sys

opp_points = {
    "A":1,
    "B":2,
    "C":3
}

my_points = {
    "X":1,
    "Y":2,
    "Z":3
}

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print('Bad Parameters')
#

def process(round):
    global my_score 
    my_score += my_points[round[1]]
    
    diff = my_points[round[1]] - opp_points[round[0]]

    if(diff == 0): #tie
        my_score += 3
    elif(diff == 1 or diff == -2): #win
        my_score += 6
#

file = open(sys.argv[1], "r")

my_score = 0 
while ( line := file.readline() ):
    if '' != line.strip():
        round = line.split()
        process(round)
    #
#

print("My Score: ", my_score)

file.close()
