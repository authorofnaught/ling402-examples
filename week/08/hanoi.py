#!/usr/bin/python3

START = 0
MID = 1
GOAL = 2

class Towers:
    """ Towers class with three towers for solving 
    Towers of Hanoi
    """
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.poles = [[],[],[]]
        for i in range(num_disks):
            self.poles[START].append(num_disks - i)

#    def show(self):
    def __str__(self):
        return '{}\n{}\n{}\n'.format(self.poles[START], self.poles[MID], self.poles[GOAL])

    def move_disk(self, from_pole, to_pole):
        moved_disk = self.poles[from_pole].pop()
        self.poles[to_pole].append(moved_disk)


def make_move(towers, num_disks, source, aux, target):
    """ Recursive method for solving Towers of Hanoi 
    """ 
    if num_disks > 0:
        
        # Recursively move all but the bottom-most of the requested disks to the auxiliary pole
        make_move(towers, num_disks-1, source, target, aux)
        
        # Move the bottom-most requested disk from the source pole to the target pole
        towers.move_disk(source, target)
        print("Moved from pole {} to pole {}".format(source, target))
        print(towers)
            
        # Recursively move the other requested disks back from the auxiliary pole to the target pole
        make_move(towers, num_disks-1, aux, source, target)


def solve(towers):
    num_disks = towers.num_disks
    make_move(towers, num_disks, START, MID, GOAL)


def play_towers_of_hanoi():
    """ Instantiates and solves Towers of Hanoi 
    """
    while True:
        num_disks = input("Enter the number of disks: ")
        if num_disks.isdigit():
            num_disks = int(num_disks)
            break
        else:
            print("Try again. Please enter an integer value.")

    towers = Towers(num_disks)
    print(towers)
    solve(towers)


if __name__ == '__main__':
    play_towers_of_hanoi()
