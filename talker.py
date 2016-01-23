#!/usr/bin/env python
# encoding: utf-8
import re
import json
import time
import traceback
import jieba
import datetime
from models import *
from core import *


def process_row(context):
    add_raw_data(context=context)
    seg_list = jieba.cut(context)
    seg_list = [seg for seg in seg_list if seg not in (' ', '', '\n', '\t')]
    add_nodes_from(seg_list)
    for index, seg in enumerate(seg_list):
        if index == len(seg_list) - 1:
            break
        next_seg = seg_list[index + 1]
        # print index, seg, next_seg
        add_weighted_edges_from(seg, next_seg)

    return seg_list


def read_from_input():
    while True:
        input_ = raw_input('你想说啥：')
        process_row(context=input_)


def read_from_file(file):
    with open(file, 'r') as fp:
        lines = fp.readlines()

    for line in lines:
        process_row(line)


if __name__ == '__main__':
    while True:
        context = raw_input('你想说啥：')
        seg_list = process_row(context)
        print get_query_answer(seg_list)
