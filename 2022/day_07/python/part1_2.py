#!/usr/bin/python3
#
# @author: DevHeadTech
# 
# Advent of Code - Day 07
#

import sys

class Node:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
    #

    def __str__(self) -> str:
        str_name = self.name + " (" + str(type(self).__name__)
        str_size = ", size=" + str(self.size) + ")"
        return str_name + str_size
    #

    def __repr__(self) -> str:
        return self.name
    #
#

class Dir(Node):
    def __init__(self, name, parent, size=0) -> None:
        Node.__init__(self,name, size)
        self.children = []
        self.parent = parent
    #

    def add(self, n) -> None:
        self.children.append(n)
    #

    def list(self, recurse=False) -> None:
        print("---")
        print(self, ":")
        for c in self.children:
            print(c)
        #

        if (recurse):
            for c in self.children:
                if(getattr(c, "list", False)):
                    c.list(recurse)
                #
            #
        #
    #

    def calc_size(self) -> int:
        for c in self.children:
            if(getattr(c, "calc_size", False)):
                sz = c.calc_size()
            else:    
                sz = c.size
            #
            self.size += sz
        #
        return self.size
    #
#

class File(Node):
    pass
#

class FileSystem:
    def __init__(self) -> None:
        self.root = Dir("/", None)
        self.pos = self.root
    #

    def mkdir(self, name) -> None:
        self.pos.add(Dir(name, self.pos))
    #

    def ls(self, recurse = False) -> None:
        self.pos.list(recurse)
    #

    def cd(self, dir) -> None:
        if(dir == ".." and self.pos.parent != None):
            self.pos = self.pos.parent
            return
        elif (dir == "/"):
            self.pos = self.root
        #

        for c in self.pos.children:
            if (c.name == dir and isinstance(c, Dir)):
                self.pos = c
            #
        #
    #

    def touch(self,file,size) -> None:
        self.pos.add(File(file,size))
    #

    def du(self, dir, min=100000) -> None:
        cnt = 0
        if(dir.size <= min):
            cnt += dir.size
            print(dir)
        #

        for c in dir.children:
            if(type(c).__name__ == "Dir"):
                cnt += self.du(c)
            #
        #
        return cnt
    #
# 

def make_fs(line) -> None:
    if (line[0] == "$"):
        if (line[1] == "cd"):
            fs.cd(line[2])
        # ignore ls
    elif (line[0] == "dir"):
        fs.mkdir(line[1])
    else:
        fs.touch(line[1], int(line[0]))
    #
#

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('Bad Parameters')
        return
    #

    file = open(sys.argv[1], "r")
    while (line := file.readline().strip().split()):
        make_fs(line)
    #

    fs.root.calc_size()
    print("Total: ", fs.du(fs.root))
    
    file.close()
#

fs = FileSystem()

if __name__ == "__main__":
    main()
#