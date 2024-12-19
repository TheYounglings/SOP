import math
import numpy as np

def getInternalAngel(p2, p1):
    return ( math.pi + math.atan2(np.cross(p1, p2), np.dot(p1, p2)) ) * (180/math.pi)
    