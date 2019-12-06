

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def modulo(self):
        return abs(self.x) + abs(self.y)
    
    # Manhattan distance
    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def contains(self, p):
        return self.p1.distance(p) + self.p2.distance(p) == self.p1.distance(self.p2)

    def __str__(self):
        return f"{self.p1} -> {self.p2}"

    @staticmethod
    def intersection(v, u):
        if v.p1 == u.p1 or v.p1 == u.p2 or v.p2 == u.p1 or v.p2 == u.p2:
            return None
        x1 = v.p1.x
        y1 = v.p1.y
        x2 = v.p2.x
        y2 = v.p2.y
        x3 = u.p1.x
        y3 = u.p1.y
        x4 = u.p2.x
        y4 = u.p2.y
        try:
            x = (x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)
            x = x // ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))

            y = (x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)
            y = y // ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
        except ZeroDivisionError:
            return None
        
        inter = Point(x, y)

        if not u.contains(inter) or not v.contains(inter):
            return None
        
        return inter

class CrossedWires:

    def __init__(self):

        with open("input.txt", "r") as f:
            first_wire, second_wire = f.readlines()
            self.first_inputs = first_wire.split(',')
            self.second_inputs = second_wire.split(',')

        self.first_lines = []
        self.second_lines = []


    def parse_inputs(self):
        current = Point(0, 0)
        for move in self.first_inputs:
            new_line = self.construct(current, move)
            current = Point(new_line.p2.x, new_line.p2.y)
            self.first_lines.append(new_line)

        current = Point(0, 0)
        for move in self.second_inputs:
            new_line = self.construct(current, move)
            current = Point(new_line.p2.x, new_line.p2.y)
            self.second_lines.append(new_line)
        
    def main(self):
        self.parse_inputs()
        intersections = []
        for v in self.first_lines:
            for u in self.second_lines:
                inter = Line.intersection(u, v)
                if inter is not None:
                    intersections.append(inter)

        minDistance = intersections[0].modulo()
        for point in intersections:
            modulo = point.modulo()
            if modulo < minDistance:
                minDistance = modulo

        return minDistance


    @staticmethod
    def construct(current, move):
        new_point = Point(current.x, current.y)
        if(move[0] == 'U'):
            new_point.y += int(move[1:])
        elif(move[0] == 'D'):
            new_point.y += -1 * int(move[1:])
        elif(move[0] == 'R'):
            new_point.x += int(move[1:])
        elif(move[0] == 'L'):
            new_point.x += -1 * int(move[1:])
        else:
            raise Exception("unvalid direction")

        return Line(current, new_point)


if __name__ == "__main__":
    print(CrossedWires().main()) # 2050