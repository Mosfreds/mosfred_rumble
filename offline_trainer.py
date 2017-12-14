#!/usr/bin/env python


import sys

from pprint import pprint

from vindinium.bots import MosfredRumble
from vindinium.learner import LogReader


def train_savegame(ann, savegame):
    print("Working on {}. ".format(savegame))
    for s in LogReader(open(savegame, 'r')):
        pprint(s)


def main(savegame_files):
    ann = MosfredRumble().create_ann()

    for savegame in savegame_files:
        train_savegame(ann, savegame)

if __name__ == '__main__':
    main(sys.argv[1:])