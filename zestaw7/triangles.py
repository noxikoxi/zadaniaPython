from points import Point
import unittest


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


# Kod testujący moduł.


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.t1 = Triangle(0, 0, 5, 0, 0, 5)
        self.t2 = Triangle(2, 2, 4, 2, 2, 4)
        self.t3 = Triangle(-2, -3, 4, 2, 5, 4)

    def test_init_errors(self):
        with self.assertRaises(ValueError) as message:
            Triangle(0, 0, 1, 1, 2, 2)

        # Sprawdzam, czy komunikat jest poprawny
        self.assertEqual(str(message.exception), "Podane punkty nie mogą być współliniowe")

        with self.assertRaises(ValueError) as message:
            Triangle(0, 5, 1, 4, 2, 3)

        self.assertEqual(str(message.exception), "Podane punkty nie mogą być współliniowe")

        with self.assertRaises(ValueError) as message:
            Triangle(5, 5, 2, 5, 6, 5)

        self.assertEqual(str(message.exception), "Podane punkty nie mogą być współliniowe")

    def test_make4(self):
        t4 = Triangle(0, 0, 6, 6, 12, 0)
        (a, b, c, d) = t4.make4()
        # Funkcja zwraca trójkąty w kolejności: (z pierwszego wierzchołka, z drugiego, z trzeciego, ze środków);
        # w takiej kolejności będą sprawdzane
        # Triangle(A.x, A.y, B.x, B.y, C.x, C.y)

        self.assertIs(a == Triangle(0, 0, 3, 3, 6, 0), True)  # A
        self.assertIs(b == Triangle(6, 6, 3, 3, 9, 3), True)  # B
        self.assertIs(c == Triangle(12, 0, 6, 0, 9, 3), True)  # C
        self.assertIs(d == Triangle(9, 3, 3, 3, 6, 0), True)  # Środki

        t5 = Triangle(-12, -12, -8, -16, -4, -14)
        (a, b, c, d) = t5.make4()
        self.assertIs(a == Triangle(-12, -12, -10, -14, -8, -13), True)  # A
        self.assertIs(b == Triangle(-8, -16, -10, -14, -6, -15), True)  # B
        self.assertIs(c == Triangle(-4, -14, -8, -13, -6, -15), True)  # C
        self.assertIs(d == Triangle(-6, -15, -10, -14, -8, -13), True)  # Środki

        t6 = Triangle(-9, 6, 6, 4, 2, 0)
        (a, b, c, d) = t6.make4()
        self.assertIs(a == Triangle(-9, 6, -1.5, 5, -3.5, 3), True)  # A
        self.assertIs(b == Triangle(6, 4, -1.5, 5, 4, 2), True)  # B
        self.assertIs(c == Triangle(2, 0, 4, 2, -3.5, 3), True)  # C
        self.assertIs(d == Triangle(-3.5, 3, 4, 2, -1.5, 5), True)  # Środki

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
