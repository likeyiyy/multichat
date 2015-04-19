#!/usr/bin/env python
# coding=utf-8
"""
In this multichat, I want do something like this:

1. It have a GUI, just like QQ, LEFT is big window that view
chat context, RIGTH is a list window view online people.
DOWN is a window can input infomation, and send it to others.
yes, it likes a qq qun.
-------------------------------
| sir_a(1234) 19:00 |         |
|     some_word     | sir_a   |
|                   | sir_b   |
|                   |         |
|                   |         |
|                   |         |
|                   |         |
|                   |         |
|                   |         |
|                   |         |
---------------------         |
|            | Send |         |
-------------------------------

2. More imporant is that I want it is a never offline system.
when only one is online, It while search others.
and give the BIGS ip, so he can register it.
"""
from multiChatGui import *

if __name__ == "__main__":
    a = multiChatGui()
    a.display()
