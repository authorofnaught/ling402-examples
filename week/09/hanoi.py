#!/usr/bin/python3

class Towers:
    """ Towers class with three towers for solving 
    Towers of Hanoi
    """
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.start = []
        self.middle = []
        self.goal = []
        for i in range(num_disks):
            self.start.append(num_disks - i)

    def show(self):
        print('{}\n{}\n{}\n'.format(self.start, self.middle, self.goal))


def move(n, source, aux, target):
    """ Recursive method for solving Towers of Hanoi 
    """ 
    if n > 0:
        # switch target depending on odd or even # of disks
        move(n-1, source, target, aux)
        # source and target established, make a move
        if len(source) > 0:
            target.append(source.pop())
            towers.show() #--> possible because of global scope of variable
        # switch source depending on odd or even # of disks
        move(n-1, aux, source, target)


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

    global towers # 'global' make variable visible outside of this method
    towers = Towers(num_disks)
    towers.show()
    move(len(towers.start), towers.start, towers.middle, towers.goal) 


if __name__ == '__main__':
    play_towers_of_hanoi()
