# @author DevHeadTech
# 
# Advent of Code - Day 01

CC=gcc
CFLAGS=
OUT=build


all: part1 part2
	
	
part1: part1.c
	[ -d $(OUT) ] || mkdir -p $(OUT)
	$(CC) -o $(OUT)/part1 part1.c 

part2: part2.c
	[ -d $(OUT) ] || mkdir -p $(OUT)
	$(CC) -o $(OUT)/part2 part2.c 

clean:
	rm -r build/
