# 1 pac without abilities and types

import sys
import math
from array import *

# Grab the pellets as fast as you can!

# width: size of the grid
# height: top left corner is (x=0, y=0)
width, height = [int(i) for i in input().split()]
for i in range(height):
    row = input()  # one line of the grid: space " " is floor, pound "#" is wall
dest_id = 0

# game loop
while True:
    my_score, opponent_score = [int(i) for i in input().split()]
    visible_pac_count = int(input())  # all your pacs and enemy pacs in sight
    pac_cor = []
    for i in range(visible_pac_count):
        # pac_id: pac number (unique within a team)
        # mine: true if this pac is yours
        # x: position in the grid
        # y: position in the grid
        # type_id: unused in wood leagues
        # speed_turns_left: unused in wood leagues
        # ability_cooldown: unused in wood leagues
        pac_id, mine, x, y, type_id, speed_turns_left, ability_cooldown = input().split()
        pac_id = int(pac_id)
        mine = mine != "0"
        x = int(x)
        y = int(y)
        if mine:
            pac_cor.insert(0, [x, y])
        speed_turns_left = int(speed_turns_left)
        ability_cooldown = int(ability_cooldown)
    visible_pellet_count = int(input())  # all pellets in sight
    dest_len = 0
    destin = []
    sec_dest = []
    closest = 100

    for i in range(visible_pellet_count):
        # value: amount of points this pellet is worth
        x, y, value = [int(j) for j in input().split()]
        if value == 10:
            destin.insert(dest_len, [x, y])
            dest_len += 1
        else:
            dist_from_pallet = abs(pac_cor[0][0] - x) + abs(pac_cor[0][1] - y)
            if dist_from_pallet < closest:
                closest = dist_from_pallet
                sec_dest.insert(0, [x, y])

        

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # MOVE <pacId> <x> <y>
    if dest_len > 0:
        dest_dist = [0]
        dest_dist[0] = abs(pac_cor[0][0] - destin[0][0]) + abs(pac_cor[0][1] - destin[0][1])
        short_loop_x = 1
        dest_count = len(destin)
        print(dest_dist[0], file=sys.stderr)
        while dest_count - 1 > 0:
           dest_dist += [abs(pac_cor[0][0] - destin[short_loop_x][0]) + abs(pac_cor[0][1] - destin[short_loop_x][1])]
           short_loop_x += 1
           dest_count -= 1
        min_dist = dest_dist.index(min(dest_dist))
        print("MOVE 0 " + str(destin[min_dist][0]) + " " + str(destin[min_dist][1]))
    else:
        print("MOVE 0 " + str(sec_dest[0][0]) + " " + str(sec_dest[0][1]))jjjjkkjj
