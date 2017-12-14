#!/usr/bin/env python


import sys

from pprint import pprint

from vindinium.bots import MosfredRumble
from vindinium.learner import LogReader

from vindinium.observations import ObservationMap

def train_savegame(ann, savegame):
    print("Working on {}. ".format(savegame), end='')
    moves = [s for s in LogReader(open(savegame, 'r'))]
    winner = max(moves[-1].heroes, key=lambda x : x.gold)
    print("Winner after moves {} is bot {}.".format(len(moves), winner.id))

    for move in zip(moves[winner.id-1::4], moves[winner.id::4]):
        hstate_pre = next(x for x in move[0].heroes if x.id == winner.id)
        hstate_post = next(x for x in move[0].heroes if x.id == winner.id)



def main(savegame_files):
    ann = MosfredRumble().create_ann()

    for savegame in savegame_files:
        train_savegame(ann, savegame)

if __name__ == '__main__':
    main(sys.argv[1:])
