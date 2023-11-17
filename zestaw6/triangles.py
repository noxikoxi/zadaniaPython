import math

from points import Point
import unittest


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

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

    def center(self):  # zwraca środek (masy) trójkąta
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self):  # pole powierzchni
        return math.fabs(self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (self.pt1.y - self.pt2.y)) / 2

    def move(self, x, y):  # przesunięcie o (x, y)
        for point in (self.pt1, self.pt2, self.pt3):
            point.x += x
            point.y += y


# Kod testujący moduł.


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.t1 = Triangle(0, 0, 5, 0, 0, 5)
        self.t2 = Triangle(2, 2, 4, 2, 2, 4)
        self.t3 = Triangle(-2, -3, 4, 2, 5, 4)

    def test_str(self):
        self.assertEqual(str(self.t1), "[(0, 0), (5, 0), (0, 5)]")
        self.assertEqual(str(self.t2), "[(2, 2), (4, 2), (2, 4)]")
        self.assertEqual(str(self.t3), "[(-2, -3), (4, 2), (5, 4)]")

    def test_rpr(self):
        self.assertEqual(repr(self.t1), "Triangle(0, 0, 5, 0, 0, 5)")
        self.assertEqual(repr(self.t2), "Triangle(2, 2, 4, 2, 2, 4)")
        self.assertEqual(repr(self.t3), "Triangle(-2, -3, 4, 2, 5, 4)")

    def test_eq(self):
        self.assertIs(self.t1 == self.t2, False)
        self.assertIs(self.t1 == self.t3, False)
        self.assertIs(self.t3 == self.t2, False)
        self.assertIs(self.t1 == self.t1, True)
        self.assertIs(self.t1 == Triangle(0, 0, 5, 0, 0, 5), True)
        self.assertIs(self.t1 == Triangle(1, 0, 5, 0, 0, 5), False)
        self.assertIs(self.t1 == Triangle(0, 0, -5, 0, 0, -5), False)

        # Różna kolejność
        self.assertIs(self.t1 == Triangle(5, 0, 0, 5, 0, 0), True)
        self.assertIs(self.t3 == Triangle(5, 4, 4, 2, -2, -3), True)

    def test_ne(self):
        self.assertIs(self.t1 != self.t2, True)
        self.assertIs(self.t1 != self.t3, True)
        self.assertIs(self.t3 != self.t2, True)
        self.assertIs(self.t1 != self.t1, False)
        self.assertIs(self.t1 != Triangle(0, 0, 5, 0, 0, 5), False)
        self.assertIs(self.t1 != Triangle(1, 0, 5, 0, 0, 5), True)
        self.assertIs(self.t1 != Triangle(0, 0, -5, 0, 0, -5), True)
        self.assertIs(self.t3 != Triangle(-2, -3, 4, 2, 5, 4), False)

        # Różna kolejność
        self.assertIs(self.t1 != Triangle(5, 0, 0, 5, 0, 0), False)
        self.assertIs(self.t2 != Triangle(4, 2, 2, 2, 2, 4), False)

    def test_center(self):
        self.assertEqual(self.t1.center(), Point(5 / 3, 5 / 3))
        self.assertEqual(self.t2.center(), Point(8 / 3, 8 / 3))
        self.assertEqual(self.t3.center(), Point(7 / 3, 1))
        self.assertEqual(Triangle(-2, -2, 2, 2, 0, 2).center(), Point(0, 2 / 3))

    def test_move(self):
        temp = Triangle(0, 0, 5, 0, 0, 5)
        temp.move(1, 1)
        self.assertEqual(temp, Triangle(1, 1, 6, 1, 1, 6))

        temp.move(0, 0)
        self.assertEqual(temp, Triangle(1, 1, 6, 1, 1, 6))

        temp.move(-10, -10)
        self.assertEqual(temp, Triangle(-9, -9, -4, -9, -9, -4))

        temp.move(0, 4)
        self.assertEqual(temp, Triangle(-9, -5, -4, -5, -9, 0))

        temp.move(8, 0)
        self.assertEqual(temp, Triangle(-1, -5, 4, -5, -1, 0))

    def test_area(self):
        self.assertEqual(self.t1.area(), 12.5)
        self.assertEqual(self.t2.area(), 2)
        self.assertEqual(Triangle(-10, 0, 10, 0, 0, 10).area(), 100)
        self.assertEqual(Triangle(-4, 2, 4, 5, 2, 5).area(), 3)


if __name__ == '__main__':
    unittest.main()
