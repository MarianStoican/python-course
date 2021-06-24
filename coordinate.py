

class Coordinate(object):
    """O coordonata este compusa din valorile X si Y"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # return f"({self.__x}, {self.__y})"
        return '(%s, %s)' % (self.x, self.y)

    def __add__(self, other):
        x_add = self.x + other.x
        y_add = self.y + other.y

        return Coordinate(x_add, y_add)

    def distance(self, other):
        x_diff_sqr = (self.x - other.x) ** 2
        y_diff_sqr = (self.y - other.y) ** 2

        return (x_diff_sqr + y_diff_sqr) ** 0.5 # radical de ordinul 2


origin = Coordinate(0, 0)
coord1 = Coordinate(2, 12)
coord2 = Coordinate(2, 8)

coord3 = coord1 + coord2

print(coord3)



