from math import sqrt


class Location:
    def __init__(self, pos_x=0, pos_y=0):
        self.point = Point(pos_x, pos_y)
        pass

    def set_location(self, x, y):
        self.point.x = x
        self.point.y = y

    def get_location(self):
        return self.point

    def equals(self, loc):
        return self.point.x == loc.point.x and self.point.x == loc.point.x

    @staticmethod
    def distance(p1, p2):
        return sqrt((p2.y-p1.y)*(p2.y-p1.y)+(p2.x-p1.x)*(p2.x-p1.x))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass