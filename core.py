#!/usr/bin/env python
# encoding: utf-8
import copy
from random import choice
from models import *
from scipy.stats import gamma
COUNTER_MAX = 5
GAMMA = 4
TIMES = 3
B_TIMES = 81


def more_or_rare(weight):
    return TIMES * weight + B_TIMES / weight


def get_next_seg_similarity(seg, query):
    count = 0
    for item in query:
        if item == seg:
            count += 1
    return count


def calc_weight(weight, period, similarity):
    """
    :descption
    Before answer we add this five content.
    1. more is different.
    2. rare is beautiful.
    3. new is good.
    4. refractory period
    5. key word
    """
    return gamma.pdf(period, GAMMA) + similarity + more_or_rare(weight)


def get_edge_weight(edge, query):
    period = (datetime.datetime.now() - edge.lastUpdateDate).total_seconds()
    weight = edge.weight
    similarity = get_next_seg_similarity(edge.to_.seg, query)
    result = calc_weight(weight, period, similarity)
    return {edge: result}


def get_a_answer(query=[], item=''):
    counter = 0
    answer = [item]
    seg = item
    while counter < COUNTER_MAX and Edges.select().join(Nodes, on=Edges.from_).where(Nodes.seg == seg).exists():
        result = []
        for edge in Edges.select().join(Nodes, on=Edges.from_).where(Nodes.seg == seg):
            result.append(get_edge_weight(edge, query))

        result = sorted(result, key=lambda x: x.values(), reverse=True)
        if not result:
            break
        # at here, we can choice first or first of K, at here, we choice first one.
        next_node = result[0].keys()[0].to_
        next_node.lastUpdateDate = datetime.datetime.now()
        seg = next_node.seg
        next_node.save()
        answer.append(seg)
        counter += 1
    return ''.join(answer)


def get_best_answer(result):
    return choice(result)


def get_query_answer(query=[]):
    result = []
    for item in query:
        result.append(get_a_answer(query, item))
    return get_best_answer(result)
