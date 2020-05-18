# 3 pacs without abilities and types

import sys
import math
from array import *

# Grab the pellets as fast as you can!

# width: size of the grid
# height: top left corner is (x=0, y=0)
width, height = [int(i) for i in input().split()]
for i in range(height):
    row = input()  # one line of the grid: space " " is floor, pound "#" is wall

# functions


def destination_print(pac_id, destination_cor):
    print("MOVE " + str(pac_id) + " " +
          str(destination_cor[0]) + " " + str(destination_cor[1]))
    return

# find closest pallet for a given pac


def pac_destin(pac, destin, used):
    temp_short_dist_ind = 0
    shortest_dist = 100
    pal_ind = 0
    i = len(destin)
    while i:
        if pal_ind in used:
            pal_ind += 1
            i -= 1
            continue
        new_dis = abs(pac[0] - destin[pal_ind][0]) + \
            abs(pac[1] - destin[pal_ind][1])
        if shortest_dist > new_dis:
            shortest_dist = new_dis
            temp_short_dist_ind = pal_ind
        pal_ind += 1
        i -= 1
    return temp_short_dist_ind


def dist_between_cor(point1, point2):
    dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return dist

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
        pac_ind = 0
        if mine:
            pac_cor.insert(pac_ind, [x, y])
            pac_ind += 1
        speed_turns_left = int(speed_turns_left)
        ability_cooldown = int(ability_cooldown)
    visible_pellet_count = int(input())  # all pellets in sight

    # my variables
    dest_len = 0
    destin = []
    # arrays id represents dest for that pacs id: 0 for the first pac etc.
    pacs_sec_dest = [[100, 100], [100, 100], [100, 100]]
    pacs_curr_dist = [100, 100, 100]

    for i in range(visible_pellet_count):
        # value: amount of points this pellet is worth
        x, y, value = [int(j) for j in input().split()]
        if value == 10:
            destin.insert(dest_len, [x, y])
            dest_len += 1
        else:
            # find which pac has the shortest dist for this pallet
            pac_id = 0
            pacs_temp_dist = [0, 0, 0]
            while pac_id < 3:
                this_pac_dist = dist_between_cor(pac_cor[pac_id], [x, y])
                if pacs_temp_dist[pac_id] > this_pac_dist:
                    pacs_temp_dist[pac_id] = this_pac_dist
                pac_id += 1

            # find if the newfound dist is shorter than the previous saved for that pac
            closest_pac_ind = pacs_temp_dist.index(min(pacs_temp_dist))
            closest_temp_dist = dist_between_cor(
                pac_cor[closest_pac_ind], [x, y])
            if closest_temp_dist < pacs_curr_dist[closest_pac_ind]:
                pacs_curr_dist[closest_pac_ind] = closest_temp_dist
                pacs_sec_dest[closest_pac_ind] = [x, y]

            # dist_from_pallet =
            # if dist_from_pallet < closest:
            # closest = dist_from_pallet
            # sec_dest.insert(0, [x, y])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # MOVE <pacId> <x> <y>

    free_pacs = 3
    used_dest = []
    while dest_len > 0 or free_pacs > 0:
        pac_id = 0
        dest_print_ind = pac_destin(pac_cor[pac_id], destin, used_dest)
        destination_print(pac_id, destin[dest_print_ind])
        used_dest = used_dest + [dest_print_ind]
        free_pacs -= 1

    while free_pacs > 0:
        destination_print(3 - free_pacs, pacs_sec_dest[3 - free_pacs])
        free_pacs -= 1
