import decimal
import fractions
import math
from typing import (
    Union,
    List,
    Set,
    Tuple,
    Optional,
    Generator,
    SupportsComplex
)
import string, io
import collections


def format_complex(value: complex, force_complex: bool, floats_as_integer_ratios: bool) -> str:
    # format real part
    if value.real.is_integer():
        left = str(int(value.real))
    elif floats_as_integer_ratios:
        _sign = "-" if value.real < 0 else ""
        num, denom = abs(value.real).as_integer_ratio()
        left = f"{_sign}({num} / {denom})"
    else:
        left = str(value.real)

    # format imaginary part
    sign = "-" if value.imag < 0 else "+"
    if value.imag == 0:
        if force_complex:
            right = "0i"
        else:
            right = ""
            sign = ""
    elif value.imag == 1:
        right = "i"
    elif value.imag.is_integer():
        right = f"{int(abs(value.imag))}i"
    elif floats_as_integer_ratios:
        num, denom = abs(value.imag).as_integer_ratio()
        right = f"({num} / {denom})i"
    else:
        right = f"{abs(value.imag)}i"
    
    return f"{left}{sign}{right}"


class QuadraticSolutions:
    def __init__(self, solution_1: complex, solution_2: complex) -> None:
        self.solution_1 = solution_1
        self.solution_2 = solution_2

    def to_string(self, *, force_complex: bool = False,
                  floats_as_integer_ratios: bool = False) -> str:
        s1 = format_complex(self.solution_1, force_complex, floats_as_integer_ratios)
        s2 = format_complex(self.solution_2, force_complex, floats_as_integer_ratios)
        return f"{{ {s1}, {s2}}}"
    
    def __str__(self) -> str:
        return self.to_string()


def _quadratic_formula(a: Union[int, float], b: Union[int, float],
                       c: Union[int, float]) -> Tuple[complex, complex]:
    # -b/{2a}
    left: int = -1 * b / (2 * a)

    # \sqrt{b^2-4*a*c}/2*a
    right: Union[int, complex] = (b**2 - 4 * a * c)**(1/2) / (2 * a)

    return (complex(left + right), complex(left - right))


def quadratic_formula(a: Union[int, float], b: Union[int, float],
                      c: Union[int, float]) -> QuadraticSolutions:
    return QuadraticSolutions(*_quadratic_formula(a, b, c))


# print(quadratic_formula(1, -5, 7).to_string(floats_as_integer_ratios=True))



def get_single_factors(n: int) -> List[int]:
    factors: List[int] = list()
    for i in range(1, abs(n) + 1):
        q, r = divmod(n, i)
        if not r:
            factors.append(i)
    return factors

class MathIO(io.StringIO):
    def read_int(self, accept_sign_only: bool = False) -> int:
        cursor = self.tell()
        data: str = ""
        while True:
            char = self.read(1)
            if not char:
                if not data:
                    raise OSError("No more characters to read")
                return int(data)
            
            if char == "+":
                continue

            if char == "-" and not data or char in "0123456789":
                data += char
                continue

            if not data:
                self.seek(cursor)
                raise ValueError(f"Unexpected character {char!r}")
            
            if data == "-":
                if accept_sign_only:
                    data = -1
                else:
                    self.seek(cursor)
                    raise ValueError(f"No digits found after '-'")

            self.seek(self.tell() - 1)
            return int(data)

    def read_uint(self) -> int:
        cursor = self.tell()
        data: str = ""
        while True:
            char = self.read(1)
            if not char:
                if not data:
                    raise OSError("No more characters to read")
                return int(data)

            if char in "0123456789":
                data += char
                continue

            if not data:
                self.seek(cursor)
                raise ValueError(f"Unexpected character {char!r}")
            
            self.seek(self.tell() - 1)
            return int(data)


class Zeros(List[fractions.Fraction]):
    def to_copyable(self) -> str:
        s: List[str] = list()
        for f in self:
            num = f.numerator
            den = f.denominator
            neg = "-" if num * den < 0 else ""
            s.append(f"{neg}\\frac{{{abs(num)}}}{{{abs(den)}}}")
        return ",".join(s)




class PolynomialEndBehavior:
    __slots__ = ("end_behavior",)
    def __init__(self, left: int, right: int) -> None:
        self.end_behavior = (left, right)
    
    def __str__(self) -> str:
        def s(v: int) -> str:
            return "-∞" if v < 0 else "∞"
        L, R = [s(v) for v in self.end_behavior]
        return f"Y -> {L} as X -> -∞ || Y -> {R} as X -> ∞"

    __repr__ = __str__



class PolynomialTerm:
    __slots__ = ("coefficient", "degree")
    def __init__(self, coefficient: int, degree: int) -> None:
        self.coefficient = coefficient
        self.degree = degree
    
    def __str__(self) -> str:
        return f"{self.coefficient}x^{self.degree}"
    
    __repr__ = __str__

    def copy(self) -> "PolynomialTerm":
        return PolynomialTerm(self.coefficient, self.degree)


class Polynomial:
    def __init__(self, *args) -> None:
        terms: List[PolynomialTerm] = list()
        for term in args:
            if isinstance(term, PolynomialTerm):
                terms.append(term)
            else:
                terms.extend(self.parse(str(term)))
        self.terms = terms
        self.sort()
    
    def __str__(self) -> str:
        return self.unparse(self.terms)
    
    __repr__ = __str__
    
    def end_behavior(self) -> PolynomialEndBehavior:
        highest_term = self.terms[0]
        if highest_term.degree % 2:
            if highest_term.coefficient < 0:
                return PolynomialEndBehavior(1, -1)
            return PolynomialEndBehavior(-1, 1)
        if highest_term.coefficient < 0:
            return PolynomialEndBehavior(-1, -1)
        return PolynomialEndBehavior(1, 1)
    
    def sort(self) -> None:
        self.terms.sort(key=lambda t: t.degree, reverse=True)

    def get_rzt(self) -> Zeros:
        potential_zeros: List[fractions.Fraction] = list()
        lowest_term = self.terms[-1]
        if lowest_term.degree != 0:
            const = 0
        else:
            const = lowest_term.coefficient
        for q in get_single_factors(self.terms[0].coefficient):
            for p in get_single_factors(const):
                potential_zeros.append(fractions.Fraction(p, q))
                potential_zeros.append(fractions.Fraction(-p, q))
        return Zeros(dict.fromkeys(potential_zeros))
        

    def is_synthetic_divisor(self) -> bool:
        return len(self.terms) == 2 and self.terms[0].degree == 1 and self.terms[1].degree == 0
    
    def copy(self) -> "Polynomial":
        return Polynomial(*[t.copy() for t in self.terms])

    def get_term_by_degree(self, degree: int) -> Optional[PolynomialTerm]:
        for term in self.terms:
            if term.degree == degree:
                return term

    def __truediv__(self, other: "Polynomial") -> Tuple["Polynomial", "Polynomial", "Polynomial"]:
        other.sort()
        if len(other.terms) != 2 or other.terms[0].degree != 1 or other.terms[1].degree != 0:
            raise ValueError("The divisor must be a binomial with one term being of degree 1 and "
                             "the other being of degree 0")
        
        quotient: List[PolynomialTerm] = list()
        L, R = other.terms
        copy = self.copy()
        copy.sort()
        i = -1
        # for i, term in enumerate(copy.terms):
        while True:
            i += 1
            term = copy.terms[i]
            if term.degree == 0:
                return Polynomial(*quotient), Polynomial(*copy.terms[i:])
            
            recipiant_degree = term.degree - L.degree
            quo_term = PolynomialTerm(term.coefficient // L.coefficient, recipiant_degree)
            quotient.append(quo_term)
            
            # copy.get_term_by_degree(recipiant_degree).coefficient -= R.coefficient * quo_term.coefficient
            recipiant = copy.get_term_by_degree(recipiant_degree)
            if recipiant:
                recipiant.coefficient -= R.coefficient * quo_term.coefficient
            else:
                copy.terms.append(PolynomialTerm(-R.coefficient * quo_term.coefficient,
                                                 recipiant_degree))
                copy.sort()
        
    def quadratic_solve(self) -> List[Union[int, complex]]:
        # ensure we have the correct number of terms
        if len(self.terms) != 3:
            raise ValueError("number of terms must be exactly 3")
        if self.terms[0].degree !=2 or self.terms[1].degree != 1 or self.terms[2].degree != 0:
            raise ValueError("not in quadratic form")
        
        a, b, c = [t.coefficient for t in self.terms]

        # -b/{2*a}
        left: int = -1 * b / (2 * a)
        
        # \sqrt{b^2-4*a*c}/2*a
        right: Union[int, complex] = (b**2 - 4 * a * c)**(1/2) / (2 * a)

        return [left+right, left-right]

            


    @staticmethod
    def parse(form: str) -> List[PolynomialTerm]:
        variables: Set[str] = set(filter(lambda c: c not in "0123456789+-^ ", form))
        if len(variables) > 1:
            raise ValueError(f"Expected a maximum of one variable, found two: "
                             f"{', '.join(f'{v!r}' for v in variables)}")
        
        form: MathIO = MathIO(form.replace(" ", ""))
        flen = len(form.getvalue())
        var = list(variables)[0]
        terms: List[PolynomialTerm] = list()

        while True:
            try:
                try:
                    coefficient = form.read_int(True)
                except ValueError as exc:
                    coefficient = 1

                if form.read(1) == var:
                    if form.read(1) == "^":
                        degree = form.read_uint()
                    else:
                        cursor = form.tell()
                        if cursor != flen:
                            form.seek(cursor - 1)
                        degree = 1
                else:
                    degree = 0
                
                terms.append(PolynomialTerm(coefficient, degree))
            except OSError:
                return terms
    
    @staticmethod
    def unparse(terms: List[PolynomialTerm]) -> str:
        def format_term(term: PolynomialTerm, is_first: bool = False) -> str:
            if is_first:
                op = "-" if term.coefficient < 0 else ""
            else:
                op = " - " if term.coefficient < 0 else " + "
            coef = "" if term.coefficient in {1, -1} else str(abs(term.coefficient))
            var = "" if term.degree == 0 else "x" if term.degree == 1 else f"x^{term.degree}"
            return op + coef + var
        
        if len(terms) == 1:
            return format_term(terms[0], True)
        
        return format_term(terms[0], True) + "".join(format_term(t) for t in terms[1:])


def addfrac(numerator_a: int, denominator_a: int, numerator_b: int,
            denominator_b: int) -> tuple[int, int]:
    numerator = (numerator_a * denominator_b) + (numerator_b * denominator_a)
    denominator = denominator_a * denominator_b
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd

print(addfrac(1,6,1,42))


# print(Polynomial("x^2+12x+37").quadratic_solve())
# print(quadratic_formula(1, -5, 7))

# dividend = Polynomial("x^3+2x^2-x+4")
# divisor = Polynomial("x - 2")
# print(dividend / divisor)

