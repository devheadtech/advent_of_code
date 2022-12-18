#!/usr/bin/python3
#
# @author: DevHeadTech
# 
# Advent of Code - Day 06
#

import sys

sop_seq = ""
sop_count = 0

som_seq = ""
som_count = 0

def process_pkt_start(s) -> int:
    global sop_seq
    global sop_count 
    sop_seq = sop_seq + s
    sop_count += 1
    if(len(sop_seq) < 4):
        return 0
    #
    
    ret = sop_count
    for i in range(1,4):
        tmp = sop_seq[i:4]
        c = sop_seq[i-1]
        if -1 != tmp.find(c):
            ret = 0
            break
        #
    #

    sop_seq = sop_seq[1:4]
    return ret
#
def process_data_start(s) -> int:
    global som_seq
    global som_count 
    som_seq = som_seq + s
    som_count += 1
    if(len(som_seq) < 14):
        return 0
    #
    
    ret = som_count
    for i in range(1,14):
        tmp = som_seq[i:14]
        c = som_seq[i-1]
        if -1 != tmp.find(c):
            ret = 0
            break
        #
    #

    som_seq = som_seq[1:14]
    return ret
#

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('Bad Parameters')
    #

    file = open(sys.argv[1], "r")
    som_loc = 0
    sop_loc = 0
    while (s := file.read(1)):
        if( sop_loc < 4): 
            sop_loc = process_pkt_start(s)
        #
        if( som_loc < 14):
            som_loc = process_data_start(s)
        #
    #
    print("SOP: ", sop_loc)
    print("SOM: ", som_loc)
    file.close()
#

if __name__ == "__main__":
    main()
#