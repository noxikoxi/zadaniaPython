# Zadanie 5.3 Wielomainy
# Wielomian [a0, a1, a2] = a0 + a1*x + a2 *x*x

def remove_redundant_zero(poly):
    while poly[-1] == 0 and len(poly) > 1:
        poly.pop()

    return poly


def add_poly(poly1, poly2):  # poly1(x) + poly2(x)
    diff = len(poly1) - len(poly2)
    result = [0] * len(poly1) if diff >= 0 else [0] * len(poly2)

    for i in range(len(poly2)):
        result[i] += poly2[i]

    for i in range(len(poly1)):
        result[i] += poly1[i]

    # Usuwanie nadmiarowych zer
    result = remove_redundant_zero(result)

    return result


def sub_poly(poly1, poly2):  # poly1(x) - poly2(x)
    return add_poly(poly1, [-x for x in poly2])


def mul_poly(poly1, poly2):  # poly1(x) * poly2(x)
    result = [0] * (len(poly1) + len(poly2) - 1)

    for id1, x1 in enumerate(poly1):
        for id2, x2 in enumerate(poly2):
            result[id1 + id2] += x1 * x2

    return result


def is_zero(poly):  # bool, [0], [0,0], itp.
    for x in poly[:-1]:
        if x != 0:
            return False

    return True


def eq_poly(poly1, poly2):  # bool, porównywanie poly1(x) == poly2(x)
    poly1 = remove_redundant_zero(poly1)
    poly2 = remove_redundant_zero(poly2)
    if len(poly1) != len(poly2):
        return False

    for i in range(len(poly1)):
        if poly1[i] != poly2[i]:
            return False

    return True


def eval_poly(poly, x0):  # poly(x0), algorytm Hornera
    result = poly[-1]
    for i in range(1, len(poly)):
        result = (result * x0) + poly[-i-1]

    return result


def combine_poly(poly1, poly2):  # poly1(poly2(x))
    poly_power = poly2.copy()

    result = [poly1[0]]

    for i in range(1, len(poly1)):
        # dla każdego x^n obliczam (poly2)^n a potem wymnażam przez współczynnik przy x^n
        result = add_poly(result, mul_poly([poly1[i]], poly_power))
        # aby nie liczyć potęg (poly2)^n co iteracje
        poly_power = mul_poly(poly_power, poly2)

    return result


def pow_poly(poly, n):  # poly(x) ** n
    result = poly.copy()
    for i in range(n - 1):
        result = mul_poly(result, poly)

    return result


def diff_poly(poly):  # pochodna wielomianu
    result = [0] * (len(poly) - 1)
    for i in range(1, len(poly)):
        result[i - 1] = poly[i] * i

    return result
