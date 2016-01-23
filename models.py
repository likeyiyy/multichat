#!/usr/bin/env python
# encoding: utf-8

from peewee import *

import datetime

db = MySQLDatabase('talker', user='root', password='password', charset='utf8')


class RawTalk(Model):
    context = TextField()
    user = IntegerField(default=1)
    dateAdded = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Nodes(Model):
    seg = CharField()
    dateAdded = DateTimeField(default=datetime.datetime.now)
    lastUpdateDate = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        indexes = (
            # Specify a unique multi-column index on from/to-user.
            (('seg',), True),
        )


class Edges(Model):
    from_ = ForeignKeyField(Nodes, related_name='from_')
    to_ = ForeignKeyField(Nodes, related_name='to_')
    weight = IntegerField(default=0)
    dateAdded = DateTimeField(default=datetime.datetime.now)
    lastUpdateDate = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        indexes = (
            # Specify a unique multi-column index on from/to-user.
            (('from_', 'to_'), True),
        )

db.connect()
try:
    db.create_tables([RawTalk, Nodes, Edges])
except:
    pass


def add_node(seg):
    try:
        node = Nodes.get(seg=seg)
        node.lastUpdateDate = datetime.datetime.now()
        node.save()
    except Nodes.DoesNotExist:
        node = Nodes.insert(seg=seg).execute()

    return node


def get_node(seg):
    try:
        return Nodes.get(seg=seg)
    except Nodes.DoesNotExist:
        return None


def add_nodes_from(seg_list):
    for seg in seg_list:
        add_node(seg)


def add_weighted_edges_from(seg, next_seg):
    from_id = Nodes.get(seg=seg).id
    to_id = Nodes.get(seg=next_seg).id
    try:
        edge = Edges.get(from_=from_id,
                         to_=to_id)
        edge.weight += 1
        edge.lastUpdateDate = datetime.datetime.now()
        edge.save()
    except Edges.DoesNotExist:
        Edges.insert(from_=from_id,
                     to_=to_id,
                     weight=1).execute()


def add_raw_data(context):
    try:
        talker = RawTalk.get(context=context)
        talker.lastUpdateDate = datetime.datetime.now()
        talker.save()
    except RawTalk.DoesNotExist:
            talker = RawTalk.insert(context=context).execute()

    return talker

