from points import Point


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie"""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        # Punkty A, B, C są współliniowe kiedy |AB| = |AC| + |CB| lub |AB| = ||AC| - |BC||

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

        ab = (self.pt1 - self.pt2).length()
        ac = (self.pt1 - self.pt3).length()
        bc = (self.pt2 - self.pt3).length()

        if ab == ac + bc or ab == abs(ac - bc):
            raise ValueError("Podane punkty nie mogą być współliniowe")

        # Atrybuty wirtualne
        self._top = max(self.pt1.y, self.pt2.y, self.pt3.y)
        self._right = max(self.pt1.x, self.pt2.x, self.pt3.x)
        self._left = min(self.pt1.x, self.pt2.x, self.pt3.x)
        self._bottom = min(self.pt1.y, self.pt2.y, self.pt3.y)
        self._width = self._right - self._left
        self._height = self._top - self._bottom

        self._topleft = Point(self._left, self._top)
        self._topright = Point(self._right, self._top)
        self._bottomleft = Point(self.left, self._bottom)
        self._bottomright = Point(self._right, self._bottom)

        self._center = Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    @classmethod
    def from_points(cls,points):
        if len(points) != 3:
            raise ValueError("Podane nieprawidłową ilość punktów. Wymagane są 3")

        return cls(points[0].x, points[0].y, points[1].x, points[1].y, points[2].x, points[2].y)

    # Atrybutu wirtualne prostokąta ograniczającego trójkąt
    # Zwracają współrzędna
    @property
    def top(self):
        """ Najwiekszy y punktów trójkąta """
        return self._top

    @property
    def right(self):
        """ Największy x punktów trójkąta"""
        return self._right

    @property
    def left(self):
        """ Najmniejszy x punktów trójkąta"""
        return self._left

    @property
    def bottom(self):
        """ Najmniejszy y punktów trójkąta"""
        return self._bottom

    @property
    def width(self):
        """ Szerokość prostokąta ograniczającego trójkąt"""
        return self._width

    @property
    def height(self):
        """ Wysokość prostokąta ograniczającego trójkąt"""
        return self._height

    # Atrybutu wirtualne prostokąta ograniczającego trójkąt
    # Zwracają Point

    @property
    def topleft(self):
        """ Górny lewy punkt prostokąta ograniczającego trójkąt"""
        return self._topleft

    @property
    def topright(self):
        """ Górny prawy punkt prostokąta ograniczającego trójkąt"""
        return self._topright

    @property
    def bottomleft(self):
        """ Dolny lewy punkt prostokąta ograniczającego trójkąt"""
        return self._bottomleft

    @property
    def bottomright(self):
        """ Dolny prawy prostokąta ograniczającego trójkąt"""
        return self._bottomright

    # Center
    @property
    def center(self):
        """ Środek masy trójkąta"""
        return self._center

    def __str__(self):  # "[(x1, y1), (x2, y2), (x3, y3)]"
        return f'[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]'

    def __repr__(self):  # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f'Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})'

    def __eq__(self, other):  # obsługa tr1 == tr2
        # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
        # niezależnie od kolejności pt1, pt2, pt3.
        return {self.pt1, self.pt2, self.pt3} == {other.pt1, other.pt2, other.pt3}

    def __ne__(self, other):  # obsługa tr1 != tr2
        return not self == other

    def area(self):  # pole powierzchni
        return abs(self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (
                    self.pt1.y - self.pt2.y)) / 2

    def move(self, x, y):  # przesunięcie o (x, y)
        for point in (self.pt1, self.pt2, self.pt3):
            point.x += x
            point.y += y

    def make4(self):
        #     A       po podziale    A
        #    / \                    / \
        #   /   \                  +---+
        #  /     \                / \ / \
        # C-------B              C---+---B
        def segmentCenter(pointA, pointB):
            return Point((pointA.x + pointB.x)/2, (pointA.y + pointB.y)/2)

        # pt1 -> A; pt2 -> B; pt3 -> C;
        ac = segmentCenter(self.pt1, self.pt3)
        ab = segmentCenter(self.pt1, self.pt2)
        bc = segmentCenter(self.pt2, self.pt3)

        return (Triangle(ac.x, ac.y, self.pt1.x, self.pt1.y, ab.x, ab.y),  # Trójkąt z A
                Triangle(bc.x, bc.y, ab.x, ab.y, self.pt2.x, self.pt2.y),  # Trójkąt z B
                Triangle(ac.x, ac.y, bc.x, bc.y, self.pt3.x, self.pt3.y),  # Trójkąt z C
                Triangle(bc.x, bc.y, ac.x, ac.y, ab.x, ab.y)  # Trójkąt ze środków
                )
