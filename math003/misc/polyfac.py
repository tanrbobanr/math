import typing
from fractions import Fraction


def get_pos_factors(n: int) -> typing.Generator[tuple[int, int], None, None]:
    """Get all positive integer factors of `num`.
    
    """
    for f in range(1, int(n)+1):
        if not n % f:
            yield f

def polydiv(coefficients: list[int | Fraction], r: int | Fraction) -> list[int | Fraction]:
    new_coefs: list[int] = [coefficients[0]]
    for old_coef in coefficients[1:]:
        new_coefs.append(old_coef + new_coefs[-1] * r)
    return new_coefs

def rzt(numerator: int, denominator: int) -> typing.Generator[Fraction, None, None]:
    for nfac in get_pos_factors(abs(numerator)):
        for dfac in get_pos_factors(abs(denominator)):
            f = Fraction(abs(nfac), abs(dfac))
            yield f
            yield f * -1

def polyfac(coefficients: list[int | Fraction]) -> list[int]:
    zeros: list[int | Fraction] = list()
    for _ in range(len(coefficients) - 1):
        for r in rzt(coefficients[-1], coefficients[0]):
            divided = polydiv(coefficients, r)
            if divided[-1] == 0:
                zeros.append(r)
                coefficients = divided[:-1]
                break
    return zeros

def facfmt(zeros: list[Fraction | int]) -> str:
    factors: list[str] = list()
    for z in zeros:
        if z == 0:
            factors.append("x")
            continue
        if isinstance(z, int):
            if z < 0:
                factors.append(f"(x+{abs(z)})")
                continue
            factors.append(f"(x-{z})")
            continue
        if isinstance(z, Fraction):
            i = int(z)
            if i == z:
                if i < 0:
                    factors.append(f"(x+{abs(i)})")
                    continue
                factors.append(f"(x-{i})")
                continue
            if z < 0:
                factors.append(f"(x+\\frac{{{abs(z.numerator)}}}{{{z.denominator}}})")
                continue
            factors.append(f"(x-\\frac{{{z.numerator}}}{{{z.denominator}}})")
            continue
    return "".join(factors)






print(facfmt(polyfac([1,0,-1,2,2])))

    
    


# print(polydiv([1,-6,-1,34,-12,-40], 2))
# print(list(rzt(2, 2)))
