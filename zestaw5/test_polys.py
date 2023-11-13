import unittest
from polys import *


class TestPolynomials(unittest.TestCase):
    def setUp(self):
        self.p1 = [0, 1]  # W(x) = x
        self.p2 = [0, 0, 1]  # W(x) = x^2
        self.p3 = [1, 2, 3, 4]  # W(x) = 1 + 2x + 3x^2 + 4x^3
        self.p4 = [2, 3, 0, 2, 1]  # W(x) = 2 + 3x + 2x^3 + x^4

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
        self.assertEqual(add_poly(self.p1, self.p3), [1, 3, 3, 4])
        self.assertEqual(add_poly(self.p1, self.p4), [2, 4, 0, 2, 1])
        self.assertEqual(add_poly(self.p2, self.p3), [1, 2, 4, 4])
        self.assertEqual(add_poly(self.p3, self.p4), [3, 5, 3, 6, 1])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])
        self.assertEqual(sub_poly(self.p1, self.p3), [-1, -1, -3, -4])
        self.assertEqual(sub_poly(self.p3, self.p2), [1, 2, 2, 4])
        self.assertEqual(sub_poly(self.p3, self.p4), [-1, -1, 3, 2, -1])
        self.assertEqual(sub_poly(self.p4, self.p3), [1, 1, -3, -2, 1])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])
        self.assertEqual(mul_poly(self.p1, self.p3), [0, 1, 2, 3, 4])
        self.assertEqual(mul_poly(self.p2, self.p3), [0, 0, 1, 2, 3, 4])
        self.assertEqual(mul_poly(self.p4, self.p3), [2, 7, 12, 19, 17, 8, 11, 4])
        self.assertEqual(mul_poly(self.p4, [0]), [0] * len(self.p4))

    def test_is_zero(self):
        self.assertIs(is_zero([0]), True)
        self.assertIs(is_zero([0, 0, 0]), True)
        self.assertIs(is_zero([0, 1, 2]), False)
        self.assertIs(is_zero([0, 4, 5, 0, 0]), False)
        self.assertIs(is_zero([0, -1, 0]), False)

    def test_eq_poly(self):
        self.assertIs(eq_poly(self.p1, self.p2), False)
        self.assertIs(eq_poly(self.p1, self.p1), True)
        self.assertIs(eq_poly(self.p1, self.p1.copy()), True)
        self.assertIs(eq_poly(self.p2, self.p3), False)
        self.assertIs(eq_poly(self.p3, self.p4), False)
        self.assertIs(eq_poly([0, 0, 0, 0], [0, 0]), True)
        self.assertIs(eq_poly([0, 0, 0, 0, 0, 0], [0]), True)
        self.assertIs(eq_poly([0, 0, 0, 0, 1, 0], [0]), False)

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1, 2), 2)
        self.assertEqual(eval_poly(self.p2, 2), 4)
        self.assertEqual(eval_poly(self.p3, 2), 49)
        self.assertEqual(eval_poly(self.p4, 2), 40)
        self.assertEqual(eval_poly(self.p3, 0), 1)
        self.assertEqual(eval_poly(self.p4, 0), 2)
        self.assertEqual(eval_poly(self.p4, 1), 8)
        self.assertEqual(eval_poly(self.p4, 10), 12032)

    def test_combine_poly(self):
        self.assertEqual(combine_poly([1, 1, 1], [1, 2, 3]), [3, 6, 13, 12, 9])
        self.assertEqual(combine_poly(self.p1, self.p2), [0, 0, 1])
        self.assertEqual(combine_poly(self.p1, self.p3), self.p3)
        self.assertEqual(combine_poly(self.p3, self.p1), self.p3)
        self.assertEqual(combine_poly(self.p3, self.p2), [1, 0, 2, 0, 3, 0, 4])
        self.assertEqual(combine_poly(self.p4, self.p3), [8, 26, 87, 244, 532, 996, 1562, 2016, 2193, 1968, 1376, 768, 256])

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p1, 2), [0, 0, 1])
        self.assertEqual(pow_poly(self.p1, 4), [0, 0, 0, 0, 1])
        self.assertEqual(pow_poly(self.p2, 3), [0, 0, 0, 0, 0, 0, 1])
        self.assertEqual(pow_poly(self.p3, 2), [1, 4, 10, 20, 25, 24, 16])
        self.assertEqual(pow_poly(self.p3, 3), [1, 6, 21, 56, 111, 174, 219, 204, 144, 64])
        self.assertEqual(pow_poly(self.p4, 2), [4, 12, 9, 8, 16, 6, 4, 4, 1])
        self.assertEqual(pow_poly(self.p4, 3), [8, 36, 54, 51, 84, 90, 51, 60, 42, 17, 12, 6, 1])

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p1), [1])
        self.assertEqual(diff_poly(self.p2), [0, 2])
        self.assertEqual(diff_poly([0, 0, 0, 0, 1]), [0, 0, 0, 4])
        self.assertEqual(diff_poly(self.p3), [2, 6, 12])
        self.assertEqual(diff_poly(self.p4), [3, 0, 6, 4])

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
