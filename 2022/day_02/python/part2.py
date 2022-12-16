#
# @author: DevHeadTech
# 
# Advent of Code - Day 02
#

import sys

opp_dict = {
    "A":1,
    "B":2,
    "C":3
}

outcome_dict = {
    "X":-1,
    "Y":0,
    "Z":1
}

actions = [3,1,2]

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print('Bad Parameters')
#

def process(round):
    global my_score 

    outcome = outcome_dict[round[1]]
    opp_action = opp_dict[round[0]]
    my_action = actions[(opp_action+outcome)%3]
    my_score += my_action

    if(outcome == 0): #tie
        my_score += 3
    elif(outcome == 1): #win
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
