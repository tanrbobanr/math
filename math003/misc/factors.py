import typing
import math
import functools



def get_factors(n: int) -> typing.Generator[tuple[int, int], None, None]:
    """Get all integer factors of `num`.
    
    """
    i = 0
    anum = abs(n)
    while True:
        if i == anum:
            return
        i += 1
        factor = n / i
        ifactor = int(factor)
        if ifactor != factor:
            continue
        yield (i, ifactor)


def facsum(n) -> typing.Generator[tuple[int, int, int], None, None]:
    for f1, f2 in get_factors(n):
        yield (f1, f2, f1+f2)


def groupsum(a: int, b: int, c: int, m: int) -> typing.Generator[tuple[tuple[int, int, int, int],
                                                                       tuple[int, int, int, int]],
                                                                 None, None]:
    for i in range(abs(b) + m * 2):
        l = i-m
        r = b-i+m
        l_gcd = math.gcd(a, l)
        r_gcd = math.gcd(r, c)
        yield ((a, l, l_gcd, a // l_gcd), (r, c, r_gcd, c // r_gcd))


def solvequad(a: int, b: int, c: int):
    # try facsum
    for f1, f2, s in facsum(a*c):
        if s == b:
            return (f1, f2)
    
    # try groupsum
    for (_a, l, l_gcd, l_div), (r, _c, r_gcd, r_div) in groupsum(a, b, c, a*c):
        if l_div == r_div:
            return ((_a, l), (r, _c))
    
    raise ValueError("No solution.")


# def fully_factor(n: int) -> list[int]:
#     def factors(n) -> list[int]:
#         return list(sorted(functools.reduce(list.__add__, ([i, n//i] for i
#                                                            in range(1, int(n**0.5) + 1)
#                                                            if n % i == 0))))
#     facs: list[int] = []
#     current: int = n
#     while True:
#         f = factors(current)
#         if len(f) == 0:
#             return facs + [current]
#         facs.append()
    

def fully_factor(n):
    def _factors(n) -> list[int]:
        return list([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)
    factors: list[int] = []
    current: int = n
    while True:
        facs = _factors(current)
        if len(facs) == 0:
            return factors + [current]
        fac, rem = facs[0]
        factors.append(fac)
        current = rem


def lcm(a: int, b:int):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        greater += 1
    return lcm

# print(fully_factor(128))
# print(list(fully_factor(97)))
# print(lcm(25, 36))
# a = 1904
# b = 12
# print(round(b / (a / 10000)))


# print((4-1j)*(5-6j))
print(list(get_factors(54)))

# def distance(a: tuple[int, int], b: tuple[int, int]) -> float:
#     return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
# print(distance((3, 2), (-2, 1)))


# def calc(x):
#     print(6*(x**3)+11*(x**2) > 2*x)

# calc(1)

# print(factors(456))


# print("\n".join(str(x) for x in groupsum(81, 18, -6, 81*-6)))


# def get_all_factors(num: int) -> None:
#     i = 1
#     highest_factor = None
#     factors: list[str] = list()
#     sums: list[str] = list()
#     while True:
#         if i == highest_factor:
#             break
#         factor = num / i
#         if int(factor) != factor:
#             i += 1
#             continue
#         else:
#             factor = int(factor)
#         highest_factor = abs(factor)
#         if num < 0:
#             factors.extend([f"{{{i}, {factor}}}", f"{{{-i}, {-factor}}}"])
#             sums.extend([f"+={i+factor}"] * 2)
#         else:
#             factors.append(f"{{{i}, {factor}}}")
#             sums.append(f"+={i+factor}")
#         i += 1
#     f_max_len = max(len(f) for f in factors)
#     fmt = "{: <{}}  {}"
#     for f, s in zip(factors, sums):
#         print(fmt.format(f, f_max_len, s))

# get_all_factors(81*-6)
