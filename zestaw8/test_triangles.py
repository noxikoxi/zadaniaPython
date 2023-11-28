from triangles import Triangle
from points import Point
import pytest


# Kod testujący moduł

# Działa jak setUp w unittest
@pytest.fixture
def t1():
    return Triangle(0, 0, 5, 0, 0, 5)


@pytest.fixture
def t2():
    return Triangle(2, 2, 4, 2, 2, 4)


@pytest.fixture
def t3():
    return Triangle(-2, -3, 4, 2, 5, 4)


def test_change_attributes(t1):
    with pytest.raises(AttributeError):
        t1.top = 0

    with pytest.raises(AttributeError):
        t1.bottom = 0

    with pytest.raises(AttributeError):
        t1.left = 0

    with pytest.raises(AttributeError):
        t1.right = 0

    with pytest.raises(AttributeError):
        t1.width = 0

    with pytest.raises(AttributeError):
        t1.height = 0

    with pytest.raises(AttributeError):
        t1.topleft = Point(1, 1)

    with pytest.raises(AttributeError):
        t1.topright = Point(2, 2)

    with pytest.raises(AttributeError):
        t1.bottomleft = Point(2, 4)

    with pytest.raises(AttributeError):
        t1.bottomright = Point(2, 5)


def test_from_points():
    temp = Triangle.from_points((Point(1, 2), Point(2, 3), Point(5, 6)))
    temp2 = Triangle.from_points((Point(5, 6), Point(2, 2), Point(-3, 6)))
    temp3 = Triangle.from_points((Point(0, 0), Point(1, 2), Point(-3, -4)))

    assert temp == Triangle(1, 2, 2, 3, 5, 6)
    assert temp2 == Triangle(2, 2, -3, 6, 5, 6)
    assert temp3 == Triangle(-3, -4, 0, 0, 1, 2)


def test_from_points_errors():
    # za mało punktów
    with pytest.raises(ValueError):
        temp = Triangle.from_points((Point(1, 2), Point(2, 3)))

    # za dużo punktów
    with pytest.raises(ValueError):
        temp = Triangle.from_points((Point(1, 2), Point(2, 3), Point(5, 6), Point(1, 0)))


def test_top(t1, t2, t3):
    assert t1.top == 5
    assert t2.top == 4
    assert t3.top == 4


def test_right(t1, t2, t3):
    assert t1.right == 5
    assert t2.right == 4
    assert t3.right == 5


def test_left(t1, t2, t3):
    assert t1.left == 0
    assert t2.left == 2
    assert t3.left == -2


def test_bottom(t1, t2, t3):
    assert t1.bottom == 0
    assert t2.bottom == 2
    assert t3.bottom == -3


def test_width(t1, t2, t3):
    assert t1.width == 5
    assert t2.width == 2
    assert t3.width == 7


def test_height(t1, t2, t3):
    assert t1.height == 5
    assert t2.height == 2
    assert t3.height == 7


def test_topleft(t1, t2, t3):
    assert t1.topleft == Point(0, 5)
    assert t2.topleft == Point(2, 4)
    assert t3.topleft == Point(-2, 4)


def test_topright(t1, t2, t3):
    assert t1.topright == Point(5, 5)
    assert t2.topright == Point(4, 4)
    assert t3.topright == Point(5, 4)


def test_bottomleft(t1, t2, t3):
    assert t1.bottomleft == Point(0, 0)
    assert t2.bottomleft == Point(2, 2)
    assert t3.bottomleft == Point(-2, -3)


def test_bottomright(t1, t2, t3):
    assert t1.bottomright == Point(5, 0)
    assert t2.bottomright == Point(4, 2)
    assert t3.bottomright == Point(5, -3)


def test_init_errors(t1, t2, t3):
    with pytest.raises(ValueError) as message:
        Triangle(0, 0, 1, 1, 2, 2)

    # Sprawdzam, czy komunikat jest poprawny
    assert str(message.value) == "Podane punkty nie mogą być współliniowe";

    with pytest.raises(ValueError) as message:
        Triangle(0, 5, 1, 4, 2, 3)

    assert str(message.value) == "Podane punkty nie mogą być współliniowe"

    with pytest.raises(ValueError) as message:
        Triangle(5, 5, 2, 5, 6, 5)

    assert str(message.value) == "Podane punkty nie mogą być współliniowe"


def test_make4(t1, t2, t3):
    t4 = Triangle(0, 0, 6, 6, 12, 0)
    (a, b, c, d) = t4.make4()
    # Funkcja zwraca trójkąty w kolejności: (z pierwszego wierzchołka, z drugiego, z trzeciego, ze środków);
    # w takiej kolejności będą sprawdzane
    # Triangle(A.x, A.y, B.x, B.y, C.x, C.y)

    assert (a == Triangle(0, 0, 3, 3, 6, 0)) is True  # A
    assert (b == Triangle(6, 6, 3, 3, 9, 3)) is True  # B
    assert (c == Triangle(12, 0, 6, 0, 9, 3)) is True  # C
    assert (d == Triangle(9, 3, 3, 3, 6, 0)) is True  # Środki

    t5 = Triangle(-12, -12, -8, -16, -4, -14)
    (a, b, c, d) = t5.make4()
    assert (a == Triangle(-12, -12, -10, -14, -8, -13)) is True  # A
    assert (b == Triangle(-8, -16, -10, -14, -6, -15)) is True  # B
    assert (c == Triangle(-4, -14, -8, -13, -6, -15)) is True  # C
    assert (d == Triangle(-6, -15, -10, -14, -8, -13)) is True  # Środki

    t6 = Triangle(-9, 6, 6, 4, 2, 0)
    (a, b, c, d) = t6.make4()
    assert (a == Triangle(-9, 6, -1.5, 5, -3.5, 3)) is True  # A
    assert (b == Triangle(6, 4, -1.5, 5, 4, 2)) is True  # B
    assert (c == Triangle(2, 0, 4, 2, -3.5, 3)) is True  # C
    assert (d == Triangle(-3.5, 3, 4, 2, -1.5, 5)) is True  # Środki


def test_str(t1, t2, t3):
    assert str(t1) == "[(0, 0), (5, 0), (0, 5)]"
    assert str(t2) == "[(2, 2), (4, 2), (2, 4)]"
    assert str(t3) == "[(-2, -3), (4, 2), (5, 4)]"


def test_rpr(t1, t2, t3):
    assert repr(t1) == "Triangle(0, 0, 5, 0, 0, 5)"
    assert repr(t2) == "Triangle(2, 2, 4, 2, 2, 4)"
    assert repr(t3) == "Triangle(-2, -3, 4, 2, 5, 4)"


def test_eq(t1, t2, t3):
    assert (t1 == t2) is False
    assert (t1 == t3) is False
    assert (t3 == t2) is False
    assert (t1 == t1) is True
    assert (t1 == Triangle(0, 0, 5, 0, 0, 5)) is True
    assert (t1 == Triangle(1, 0, 5, 0, 0, 5)) is False
    assert (t1 == Triangle(0, 0, -5, 0, 0, -5)) is False

    # Różna kolejność
    assert (t1 == Triangle(5, 0, 0, 5, 0, 0)) is True
    assert (t3 == Triangle(5, 4, 4, 2, -2, -3)) is True


def test_ne(t1, t2, t3):
    assert (t1 != t2) is True
    assert (t1 != t3) is True
    assert (t3 != t2) is True
    assert (t1 != t1) is False
    assert (t1 != Triangle(0, 0, 5, 0, 0, 5)) is False
    assert (t1 != Triangle(1, 0, 5, 0, 0, 5)) is True
    assert (t1 != Triangle(0, 0, -5, 0, 0, -5)) is True
    assert (t3 != Triangle(-2, -3, 4, 2, 5, 4)) is False

    # Różna kolejność
    assert (t1 != Triangle(5, 0, 0, 5, 0, 0)) is False
    assert (t2 != Triangle(4, 2, 2, 2, 2, 4)) is False


def test_center(t1, t2, t3):
    assert t1.center == Point(5 / 3, 5 / 3)
    assert t2.center == Point(8 / 3, 8 / 3)
    assert t3.center == Point(7 / 3, 1)
    assert Triangle(-2, -2, 2, 2, 0, 2).center == Point(0, 2 / 3)


def test_move(t1, t2, t3):
    temp = Triangle(0, 0, 5, 0, 0, 5)
    temp.move(1, 1)
    assert temp == Triangle(1, 1, 6, 1, 1, 6)

    temp.move(0, 0)
    assert temp == Triangle(1, 1, 6, 1, 1, 6)

    temp.move(-10, -10)
    assert temp == Triangle(-9, -9, -4, -9, -9, -4)

    temp.move(0, 4)
    assert temp == Triangle(-9, -5, -4, -5, -9, 0)

    temp.move(8, 0)
    assert temp == Triangle(-1, -5, 4, -5, -1, 0)


def test_area(t1, t2, t3):
    assert t1.area() == 12.5
    assert t2.area() == 2
    assert Triangle(-10, 0, 10, 0, 0, 10).area() == 100
    assert Triangle(-4, 2, 4, 5, 2, 5).area() == 3
