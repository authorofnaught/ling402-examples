#!/usr/bin/env python3
import sys

def printStack():
    print("========================")
    for i in range(1,4):
        print(stack[i])    

def simpleMove(start, end):
        disc = stack[start].pop()
        stack[end].append(disc)
        printStack()


def recursiveMove(n, start, end, aux):
    if n > 0:
        recursiveMove(n-1, start, 
                           aux, end)
        simpleMove(start, end)
        recursiveMove(n-1, aux, 
                           end, start)

stack = { 1:[], 2:[], 3:[]}

if __name__ == "__main__":
        
    n = int(sys.argv[1])
    stack[1] = list(range(n,0,-1))
    printStack()
    recursiveMove(n, 1, 3, 2)

