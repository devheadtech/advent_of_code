#!/usr/bin/python3
#
# @author: DevHeadTech
# 
# Advent of Code - Day 05
#

import sys

def process_stack(file, stacks):
    rows = []
    while ( line := file.readline() ):
        if '' != line.strip():
            rows.append(line)
        else:
            break
        #
    #

    # split last line, grab last number, convert
    num_stacks = int(rows.pop().split().pop())

    for i in range(0, num_stacks):
        s = [] 
        for r in rows:
            if len(r) < num_stacks*4:
                print("Bad Row")
            #

            if ' ' != r[(i*4)+1]:
                s.insert(0,r[(i*4)+1])
        #  
        stacks.append(s)
    #
#

def process_moves(file, stacks):
    print(stacks)
    while ( line := file.readline() ):
        actions = line.split()
        move = int(actions[1])
        src = int(actions[3])-1
        dst = int(actions[5])-1
    
        for i in range(0,move):
            stacks[dst].append(stacks[src].pop())
        #
    #
#

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('Bad Parameters')
    #

    file = open(sys.argv[1], "r")

    stacks = []
    process_stack(file, stacks)
    process_moves(file, stacks)
    for s in stacks:
        print(s.pop(), end ='')
    print("")
    file.close()
#

if __name__ == "__main__":
    main()
#