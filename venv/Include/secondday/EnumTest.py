from enum import IntEnum
import dis
import collections


class TripNum(IntEnum):
    ADD_TYPE = 0x101
    EDIT_TYPE = 0x102


def getName(type):
    if type == TripNum.ADD_TYPE:
        return "shi- %i" % type
    elif type == TripNum.EDIT_TYPE:
        return "qiang- %i" % type


print(getName(TripNum.EDIT_TYPE))

value = ["Python", "Javascript"][2 > 1]
print(value)


def f1(delta_seconds):
    if delta_seconds < 11 * 24 * 3600:
        return


dis.dis(f1)


def getDisPlay(a, b, mutil= 1):
    return a * b + mutil


print(getDisPlay(*(2, 4), **{"mutil": 10}))

user = {**{"name": "piglei"}, **{"movies": ["Fight Club"]}}
print(user)

max_num = float('-inf')
if max_num < 0:
    print(max_num)
