#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.67
        self.width = 0.75
        self.exp_name = 'yolox_m_jersey'
        self.name = 'player_crops'
        self.random_size = None
        self.test_size = (160, 160)
        self.input_size = (160, 160)
        self.data_num_workers = 4
        self.conf = 0.1
        self.nms = 0.45
        self.fp16 = True