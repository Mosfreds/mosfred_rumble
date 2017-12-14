#!/usr/bin/env python


import sys
import numpy as np

from pprint import pprint

from vindinium.bots import MosfredRumble
from vindinium.learner import LogReader
from vindinium.observations import ObservationMap


def train_savegame(ann, savegame):
    print("Working on {}. ".format(savegame), end='')
    moves = [s for s in LogReader(open(savegame, 'r'))]
    winner = max(moves[-1].heroes, key=lambda x : x.gold)
    print("Winner after moves {} is bot {}.".format(len(moves), winner.id))

    inputs = []
    expected_outputs = []
    for move in zip(moves[winner.id-1::4], moves[winner.id::4]):
        inputs.append(ObservationMap(move[0]).translate_map())
        hstate_pre = next(x for x in move[0].heroes if x.id == winner.id)
        hstate_post = next(x for x in move[0].heroes if x.id == winner.id)
        # ['North', 'East', 'South', 'West', 'Stay']

        expected_output = [0, 0, 0, 0, 0]
        if hstate_pre.y - hstate_post.y == 1:
            expected_output[0] = 1
        elif hstate_pre.x - hostate_post.x == -1:
            expected_output[1] = 1
        elif hstate_pre.y - hstate_post.y == -1:
            expected_output[2] = 1
        elif hstate_pre.x - hstate_post.x == 1:
            expected_output[3] = 1
        else:
            expected_output[-1] = 1  # Stay
        expected_outputs.append(np.array(expected_output))
    ann.fit(inputs, expected_outputs, epochs=200, batch_size=10)



def main(savegame_files):
    mosfred_rumble = MosfredRumble()
    mosfred_rumble.ann = mosfred_rumble.create_ann()

    for savegame in savegame_files:
        train_savegame(mosfred_rumble.ann, savegame)

    mosfred_rumble.serialize_ann()

if __name__ == '__main__':
    main(sys.argv[1:])
