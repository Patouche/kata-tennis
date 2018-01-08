# -*- coding: utf-8 -*-


class Tennis(object):
    def __init__(self):
        self.game = (0, 0)

    def score(self):
        return ':'.join(tuple(map(str, self.game)))
