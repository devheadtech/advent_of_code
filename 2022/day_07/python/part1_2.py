#!/usr/bin/python3
#
# @author: DevHeadTech
# 
# Advent of Code - Day 07
#

import sys

DISK_SZ = 70000000
UPDATE_SZ = 30000000

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

    def list(self, recurse=False, dir_only=False) -> None:
        print("---")
        print(self.name, ":")
        for c in self.children:
            if(type(c).__name__ == "File" and dir_only != True) or (type(c).__name__ == "Dir"):
                print(c)
        #

        if (recurse):
            for c in self.children:
                if(getattr(c, "list", False)):
                    c.list(recurse, dir_only)
                #
            #
        #
    #

    def calc_size(self) -> int:
        self.size = 0
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

    def find(self,min,max) -> int:
        if (self.size < min):
            return max

        if(self.size < max):
            max = self.size

        for c in self.children:
            if(getattr(c, "find", False)):
                ret = c.find(min,max)
                if(ret < max):
                    max = ret
                #
            #
        #      
        return max
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

    def ls(self, recurse = False, dir_only=False) -> None:
        self.pos.list(recurse, dir_only)
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

    def du(self, dir, max=100000) -> None:
        cnt = 0
        if(dir.size <= max):
            cnt += dir.size
            #print(dir)
        #

        for c in dir.children:
            if(type(c).__name__ == "Dir"):
                cnt += self.du(c, max)
            #
        #
        return cnt
    #

    def delete(self, min) -> int:
        return self.root.find(min,self.root.size)
    #
# 

def make_fs(name) -> None:
    file = open(name, "r")
    while (line := file.readline().strip().split()):
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
    file.close()
#

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('Bad Parameters')
        return
    #

    make_fs(sys.argv[1])

    fs.root.calc_size()

    free = DISK_SZ - fs.root.size
    need = UPDATE_SZ - free

    print("Free Space: ", free)
    print("Root Size: ", fs.root.size)
    print("Needed Space: ", need)
    
    print("Found to delete (part2): ", int(fs.delete(need)))
    print("Total Under 100000 (part1): ", fs.du(fs.root))
#

fs = FileSystem()
delete_dir = Dir("", None)

if __name__ == "__main__":
    main()
#