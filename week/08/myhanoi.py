#!/usr/bin/python3


class Towers:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.poles = [[],[],[]]
        for i in range(num_disks):
            self.poles[0].append(num_disks - i)

    def __str__(self):
        return "{}\n{}\n{}\n".format(each pole)            

    def move_disk(self, from, to):

def play_towers_of_hanoi():
    num_disks = input("Enter number of disks: ")






if __name__ == '__main__':
    play_towers_of_hanoi()
