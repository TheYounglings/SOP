from heapq import merge
from unittest import skip
from xml.etree.ElementTree import QName
from angles import getInternalAngel
from points import isInsideTriangle
import pygame
def signedArea(polygon):
    area = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        area += (x1 * y2 - x2 * y1)
    return area / 2

def ensureWindingOrder(polygon):
    if signedArea(polygon) < 0:
        print("reverse")
        polygon.reverse()
    else:
        print("don't reverse")
    return polygon




def triangulate(polygon):
    finalTriangles = []
    vertices = list(polygon)
    originalVertices = list(polygon)
    traingulated = False
    vertices = ensureWindingOrder(vertices)

    while traingulated == False:         
        for index, _ in enumerate(vertices):
            prevVertex = vertices[index - 1]
            nextVertex = vertices[(index + 1)]  
            vertex = vertices[index]
            vector1 = (vertex[0] - prevVertex[0], vertex[1] - prevVertex[1])
            vector2 = (nextVertex[0] - vertex[0], nextVertex[1] - vertex[1])
            angle = getInternalAngel(vector1, vector2)

            if len(vertices) == 3:
                    triangle = (prevVertex, vertex, nextVertex)
                    finalTriangles.append(triangle)
                    traingulated = True
                    break

            if angle >= 180:
                continue
            else:
                triangle = (prevVertex, vertex, nextVertex)
                points = [p for p in originalVertices if p not in triangle]
                inside_evaluation = [isInsideTriangle(triangle, point) for point in points]
                if True in inside_evaluation:
                    continue
                else:
                    finalTriangles.append(triangle)
                    vertices.pop(index)
                    break

    return finalTriangles