#!/usr/bin/python3
#
# @author: DevHeadTech
# 
# Advent of Code - Day 08
#

from enum import Enum
import sys

LEFT = 0
TOP = 1
RIGHT = 2
BOT = 3

class Tree():
    def __init__(self, h, v=False) -> None:
        self.height = h
        self.visible = v
    #

    def __str__(self) -> str:
        return "("+str(self.height)+","+str(self.visible)+")"
    #

    def __repr__(self) -> str:
        return "("+str(self.height)+","+str(self.visible)+")"
#

class Forest(): 
    def __init__(self) -> None:
        self.trees = []
        self.rows = 0
        self.cols = 0
    #

    def print(self) -> None:
        for r in self.trees:
            print(r)
        #
    #

    def set_border(self) -> None:
        self.cols = len(self.trees[0])
        self.rows = len(self.trees)
        c = self.cols

        # top
        for t in self.trees[0]:
            t.visible = True
        #

        # left/right
        for r in self.trees:
            r[0].visible = True
            r[c-1].visible = True
        #

        # Bottom
        for t in self.trees[c-1]:
            t.visible = True
        #
    #

    def find_visible(self) -> int:
        c = self.cols
        r = self.rows

        # Top/Left
        for i in range(1,c-2):
            for j in range(1,r-2):
                cur = self.trees[i][j]
                top = self.trees[i-1][j]
                left = self.trees[i][j-1]

                if cur.height > top.height and top.visible:
                    self.trees[i][j].visible = True
                elif cur.height > left.height and left.visible:
                    self.trees[i][j].visible = True
                #
            #
        #

        # Bottom/Right
        for i in range(c-2, 0, -1):
            for j in range(r-2, 0, -1):
                cur = self.trees[i][j]
                bot = self.trees[i+1][j]
                right = self.trees[i][j+1]

                if cur.height > bot.height and bot.visible:
                    self.trees[i][j].visible = True
                elif cur.height > right.height and right.visible:
                    self.trees[i][j].visible = True
                #
            #
        #
        return self.count_visible()
    #

    def count_visible(self) -> int:
        cnt = 0
        for row in self.trees:
            for t in row:
                if t.visible:
                    cnt += 1
                #
            #
        #
        return cnt
    #
#

def build_forest(name) -> None:
    file = open(name, "r")
    while (line := file.readline().strip()):
        row = []
        for f in line:
            row.append(Tree(int(f)))
        #
        forest.trees.append(row)
    #
    file.close()
#

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('Bad Parameters')
        return
    #

    build_forest(sys.argv[1])

    forest.set_border()

    cnt = forest.find_visible()

    forest.print()

    print("Visible Count:", cnt)
#

forest = Forest()

if __name__ == "__main__":
    main()
#