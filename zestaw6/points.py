import math
import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return f'({self.x}, {self.y})'

    def __repr__(self):  # zwraca string "Point(x, y)"
        return f'Point{self.__str__()}'

    def __eq__(self, other):  # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.y + self.y * other.x

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(-1, 4)
        self.p3 = Point(2, 5)
        self.p4 = Point(6, 9)

    def test_str(self):
        self.assertEqual(str(self.p1), '(1, 2)')
        self.assertEqual(str(self.p2), '(-1, 4)')
        self.assertEqual(str(self.p3), '(2, 5)')
        self.assertEqual(str(self.p4), '(6, 9)')

    def test_repr(self):
        self.assertEqual(repr(self.p1), 'Point(1, 2)')
        self.assertEqual(repr(self.p2), 'Point(-1, 4)')
        self.assertEqual(repr(self.p3), 'Point(2, 5)')
        self.assertEqual(repr(self.p4), 'Point(6, 9)')

    def test_eq(self):
        self.assertIs(self.p1 == Point(self.p1.x, self.p1.y), True)
        self.assertIs(self.p1 == Point(self.p1.x + 4, self.p1.y), False)
        self.assertIs(self.p1 == Point(self.p1.x, self.p1.y + 2), False)
        self.assertIs(self.p2 == Point(self.p2.x, self.p2.y), True)
        self.assertIs(self.p2 == Point(self.p2.x, self.p2.y + 1), False)
        self.assertIs(self.p2 == Point(self.p2.x + 4, self.p2.y), False)
        self.assertIs(self.p3 == self.p4, False)
        self.assertIs(Point(1, -1) == Point(-1, 1), False)

    def test_ne(self):
        self.assertIs(self.p1 != self.p2, True)
        self.assertIs(self.p1 != self.p3, True)
        self.assertIs(self.p2 != self.p3, True)
        self.assertIs(self.p4 != self.p2, True)
        self.assertIs(self.p2 != Point(self.p2.x, self.p2.y), False)
        self.assertIs(self.p4 != Point(self.p4.x, self.p4.y), False)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(0, 6))
        self.assertEqual(self.p2 + self.p1, Point(0, 6))
        self.assertEqual(self.p1 + self.p4, Point(7, 11))
        self.assertEqual(self.p2 + self.p3, Point(1, 9))
        self.assertEqual(self.p4 + self.p2, Point(5, 13))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(2, -2))
        self.assertEqual(self.p1 - self.p3, Point(-1, -3))
        self.assertEqual(self.p1 - self.p4, Point(-5, -7))
        self.assertEqual(self.p1 - self.p1, Point(0, 0))
        self.assertEqual(self.p2 - self.p3, Point(-3, -1))
        self.assertEqual(self.p4 - self.p3, Point(4, 4))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 2)
        self.assertEqual(self.p2 * self.p3, 3)
        self.assertEqual(self.p3 * self.p4, 48)
        self.assertEqual(self.p4 * self.p4, 108)
        self.assertEqual(self.p4 * Point(0, 0), 0)
        self.assertEqual(self.p4 * Point(1, 1), self.p4.x + self.p4.y)
        self.assertEqual(self.p2 * Point(2, 2), 6)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), 6)
        self.assertEqual(self.p1.cross(self.p3), 1)
        self.assertEqual(self.p2.cross(self.p3), -13)
        self.assertEqual(self.p3.cross(self.p4), -12)
        self.assertEqual(self.p3.cross(Point(0, 0)), 0)
        self.assertEqual(self.p3.cross(Point(1, 1)), -3)

    def test_length(self):
        self.assertEqual(self.p1.length(), math.sqrt(5))
        self.assertEqual(self.p2.length(), math.sqrt(17))
        self.assertEqual(self.p3.length(), math.sqrt(29))
        self.assertEqual(self.p4.length(), math.sqrt(117))
        self.assertEqual(Point(0, 0).length(), 0)
        self.assertEqual(Point(2, 2).length(), math.sqrt(8))
        self.assertEqual(Point(-3, -4).length(), 5)
        self.assertEqual(Point(-3, 4).length(), 5)
        self.assertEqual(Point(3, -4).length(), 5)


if __name__ == '__main__':
    unittest.main()
