import math
import numpy as np

def truncate(number, digits):
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

with open("input.txt", "r") as f:
    d = f.read().split("\n")

## Part one

astroids = [(i , j) for j in range(len(d)) for i in range(len(d[j])) if d[i][j] == "#"]
accuracy = 10

def normalized_vector(center, point):
    x = point[0] - center[0]
    y = point[1] - center[1]
    magnitude = math.sqrt(x**2 + y**2)

    return (truncate(x/magnitude, accuracy), truncate(y/magnitude, accuracy)) if magnitude != 0 else None

max_visible = 0
c = None # our base of operations
for center in astroids:
    detected = len({normalized_vector(center, astroid) for astroid in astroids if normalized_vector(center, astroid) != None})
    if detected > max_visible:
        max_visible = detected
        c = center

print(max_visible) # 227
