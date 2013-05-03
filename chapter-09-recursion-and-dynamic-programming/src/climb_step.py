# coding: utf-8
"""階段を登りつめる方法を考えるプログラム
"""

CACHE = {}

def climbup(nsteps):
    """再帰でやるその1
    """
    if CACHE.get(nsteps) is not None:
        return CACHE[nsteps]

    if nsteps == 0:
        return 1
    if nsteps < 0:
        return 0
    CACHE[nsteps] = climbup(nsteps-1) + climbup(nsteps-2) + climbup(nsteps-3)
    return CACHE[nsteps]

print climbup(70)
