def isInsideTriangle(triangle, vertex):
    A, B, C = triangle
    v = vertex
    Ax, Ay = A
    Bx, By = B
    Cx, Cy = C
    Vx, Vy = v
    area1 = area(Ax, Ay, Bx, By, Cx, Cy)
    area2 = area(Vx, Vy, Bx, By, Cx, Cy)
    area3 = area(Ax, Ay, Vx, Vy, Cx, Cy)
    area4 = area(Ax, Ay, Bx, By, Vx, Vy)

    return area1 == area2 + area3 + area4
def area(x1, y1, x2, y2, x3, y3):
  return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)