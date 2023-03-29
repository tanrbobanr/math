# 1.2 Exponents and Radicals

`Properties of Exponents`
> - **Product Rule**: $a^ma^n = a^{m + n}$
> - **Power of a Power**: $(a^m)^n = a^{mn}$
> - **Power of a Product**: $(ab)^n = a^nb^n$
> - **Quotient Rule**: $\frac{a^m}{a^n} = a^{m-n}$
> - **Power of a Quotient**: $(\frac{a}{b})^n = \frac{a^n}{b^n}$
> - **Negative Power**: $a^{-n} = \frac{1}{a^n}, a \ne 0$
> - **Zero Exponent Rule**: $a^0 = 1, a \ne 0$

`Properties of Radicals`
> - **Fractional Exponents**: $\sqrt[n]{a} = a^{\frac{1}{n}}$
> - **Power of a Radical**: $(\sqrt[n]{a})^m = \sqrt[n]{a^m} = a^{\frac{m}{n}}$
> - **Product Rule**: $\sqrt[n]{ab} = \sqrt[n]{a}\sqrt[n]{b}$
> - **Quotient Rule**: $\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$

# 1.3 Algebraic Expressions

`Algebraic Expressions and Polynomials`
> - **Variable**: A letter that can represent any number from a given set of numbers.
> - **Algebraic Expression**: A conglomerate of variables and real numbers.
> - **Polynomial**: An algrebraic expression in the form $a_nx^n + a_{n-1}x^{n-1} + ... + a_1x_1 + a_0$, where $a_0, a_1, ..., a_n$ are real numbers, and$n$is a non-negative integer.
> - **Monomial**: A polynomial with a single term$a_kx^k$.
> - **Term / Monomial**: Each monomial$a_kx^k$in a polynomial is a term.
> - **Degree**: Highest power of the polynomial.
> - **Binomial**: A polynomial with 2 terms.
> - **Trinomial**: A polynomial with 3 terms.

`Product / Factoring Formulas`
> - **Difference of Squares**: $a^2 - b^2 = (a + b)(a - b)$
> - **Difference of Cubes**: $a^3 - b^3 = (a - b)(a^2 - ab + b^2)$
> - **Sum of Cubes**: $a^3 - b^3 = (a + b)(a^2 - ab + b^2)$
> - **Square of a Sum**: $(a + b)^2 = a^2 + 2ab + b^2$
> - **Square of a Difference**: $(a + b)^2 = a^2 + 2ab + b^2$
> - **Cube of a Sum**: $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$
> - **Cube of a Difference**: $(a + b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$

# 3.1 Quadratic Functions and Models

`Quadratic Functions`
> - **Form**: $f(x) = ax^2 + bx + c$
> - **Standard Form**: $f(x) = a(x - h)^2 + k$
>     - Forms a parabola.
>     - **Vertex**: $(h, k)$
>     - **Symmetry**: About $x = h$
>     - **Y-Intercept**: At $a \cdot c$
>     - **Opens**: `UP` if $a \gt 0$, `DOWN` if $a \lt 0$
>     - **X-Intercepts**: Solutions of $ax^2 + bx + c = 0$
>     - **Maximum / Minimum Value**: Maximum (if $a \lt 0$) or minimum (if $a \gt 0$) is $k$

# 3.2 Polynomial Functions and Their Graphs

`End Behavior`
> If the degree of the polynomial is `ODD`:
> - If $a_n \gt 0$($\downarrow \uparrow$):
>     - As $x \rightarrow -\infty, y \rightarrow -\infty$
>     - As $x \rightarrow \infty, y \rightarrow \infty$
> - If $a_n \lt 0$($\uparrow \downarrow$):
>     - As $x \rightarrow -\infty, y \rightarrow \infty$
>     - As $x \rightarrow \infty, y \rightarrow -\infty$
> If the degree of the polynomial is `EVEN`:
> - If $a_n \gt 0$($\uparrow \uparrow$):
>     - As $x \rightarrow -\infty, y \rightarrow \infty$
>     - As $x \rightarrow \infty, y \rightarrow \infty$
> - If $a_n \lt 0$($\downarrow \downarrow$):
>     - As $x \rightarrow -\infty, y \rightarrow -\infty$
>     - As $x \rightarrow \infty, y \rightarrow -\infty$

`Real Zeros of Polynomials`
> Given a polynomial $P(x)$, if $P(c) = 0$, then $(x - c)$ is a factor of $P(x)$

`Intermediate Value Theorem for Polynomials`
> Suppose $P(x)$ is a polynomial function and $P(a)$ and $P(b)$ have opposite signs, then there exists at least one value $c$ between $a$ and $b$ where $P(c) = 0$.

# 3.6 Rational Functions

> Given a rational function $f(x) = \frac{P(x)}{Q(x)}$, where $P$ and $Q$ are polynomials and we assume that $P$ and $Q$ have no common factors:
> - The domain is all numbers where $Q \ne 0$

`Graphing Rational Functions`
> 1. **Factor**: Factor the numerator and denominator.
> 2. **Intercepts**:
>     1. **X-Intercept(s)**: Find the X-intercept(s) by finding the zeros of the numerator.
>     2. **Y-Intercept**: Find the Y-intercept by setting $x = 0$.
> 3. **Holes**: Any factor $(x - r)$ that is cancelled from the numerator and denominator will have a hole at $x = r$.
> 4. **Vertical Asymptotes**: Set the denominator equal to$0$and solve. Each solution $s$ will have a vertical asymptote at $x = s$. Test values on each side of the asymptote to determine the graph's behavior.
> 5. **Horizontal or Slant Asmyptotes**
>     1. If the degree of the numerator is less than the degree of the denominator, there is a horizontal asymptote at $y = 0$.
>     2. If the degree of the numerator is equal to the degree of the denominator, there is a horizontal asymptote at $y = \frac{a}{b}$ where $a$ is the leading coefficient of the highest term in the numerator, and $b$ is the leading coefficient of the highest term in the denominator.
>     3. If the degree of the numerator is exactly one more than the degree of the denominator, there is a slant asymptote $ax + b$ where $ax + b$ is the quotient (remainder is dropped) of the numerator divided by the denominator.

# 3.7 Polynomial and Rational Inequalities

`Solving Polynomial Inequalities`
> Move all variables to one side of the inequality, then find the zeros of the polynomial side. Test values between/around each zero and determine whether or not they satisfy the inequality.

`Rational Inequalities`
> Move all variables to one side of the inequality, then find the zeros and all values that make the rational polynomial undefined (i.e. when denominator = 0), and finally test values between/around each of the aforementioned and determine whether or not they satisfy the inequality.

# 4.1 Exponential Functions

> An exponential function is a function of the form $f(x)=a^x, a \gt 0, a \ne 1$ where $a$ is called the **base** of the function.

`Properties of The Exponential Parent Function`
> The parent function for exponential functions is$f(x)=a^x$, which has the following properties:
> - **Domain**: All real numbers.
> - **Range**: $(0, \infty)$
> - **Y-Intercept**: $(0, 1)$
> - **X-Intercept**: None.
> - $y=0$ is a **Horizontal Asymptote**.
> - If $a \gt 1$, then the function is increasing.
> - If $0 \lt a \lt 1$, then the function is decreasing.
> - $f(x)$ is a one-to-one function.

`Graphing the Parent Function`
> To graph the parent function, plot the points $(-1, \frac{1}{a})$, $(0, 1)$, and $(1, a)$.

`Intermittent Compound Interest Function`
> $A(t) = P(1+ \frac{r}{n})^{nt}$ where $A(t)$ is the ending value, $P$ is the principle, $r$ is the annual rate, $n$ is the interest period, and $t$ is the time in years.

# 4.2 The Natural Exponential Function

> $e$, or Euler's number, is approximately $2.718281828$.

`Continuous Compound Interest Function`
> $A(t)=Pe^{rt}$ where $A(t)$ is the ending value, $P$ is the principal, $r$ is the annual rate, and $t$ is the time in years.

`Exponential Growth Function`
> $Q(t)=q_0e^{kt}$ where $Q(t)$ is the ending population, $q_0$ is the initial population, $k$ is the growth rate (per period), and $t$ is the time (in periods).

`Exponential Decay Function`
> $Q(t)=q_0e^{-kt}$ where $Q(t)$ is the ending population, $q_0$ is the initial population, $k$ is the decay rate (per period), and $t$ is the time (in periods).

# 4.3 Logarithmic Functions

> The inverse of the exponential function $f(x)=a^x$ is $f^-1(x)=log_a(x)$.

> $f(x)=log_a(x), a \gt 0, a \ne 1$ is the parent function for logarithms.

`Properties of The Exponential Parent Function`
> The parent function for exponential functions is$f(x)=log_a(x)$, which has the following properties:
> - **Domain**: $(0, \infty)$
> - **Range**: All real numbers.
> - **Y-Intercept**: None.
> - **X-Intercept**: $(1, 0)$
> - $x=0$ is a **Vertical Asymptote**.
> - If $a \gt 1$, then the function is increasing.
> - If $0 \lt a \lt 1$, then the function is decreasing.
> - $f(x)$ is a one-to-one function.

`Graphing the Parent Function`
> To graph the parent function, plot the points $(\frac{1}{a}, -1)$, $(1, 0)$, and $(a, 1)$.

`Exponential Form to Logarithmic Form`
> The equation $a^n = b$ can be rewritten as $log_a(b) = n$. That is, $log_a(b)$ is the exponent of $a$ that produces $b$.

# 4.4 Laws of Largarithms

`Properties of Logarithms`
> - **Product Rule**: $log_a(xy)=log_a(x)+log_a(y)$
> - **Quotient Rule**: $log_a(\frac{x}{y})=log_a(x)-log_a(y)$
> - **Power Rule**: $log_a(x^n)=n \cdot log_a(x)$
> - **Change of Base**: $log_a(x) = \frac{log_n(x)}{log_n(a)}$
> - **Other Properties**:
>     - $log_a(a^x) = x$
>     - $log_a(\frac{1}{a^n}) = -n$
>     - $log_a(\frac{1}{a}) = -1$
>     - $log_a(1) = 0$
>     - $log_a(a) = 1$
>     - $a^{log_a(x)} = x$

# 4.5 Exponential and Logarithmic Equations

`Solving Exponential Equations`
> 1. If the equation is in the form of $a^x=a^y$, it can be transformed into $x=y$, then solve.
> 2. If the equation is in the form of $a^x=c$, then change the form to $log_a(c) = x$, the solve.
> 3. If the equation is in the form of $a^{2x} \pm b^x + c$, then transform it into the quadratic form $A(u)^2+B(u)+C$ where $u$ is some common term, then solve for $u$. For example:
>    1. Solve for $x$, $e^{2x}-5e^x-14 = 0$
>    2. $(e^x)^2 - 5(e^x) - 14 = 0$
>    3. Solve the quadratic: $((e^x) - 7)((e^x) + 2) = 0$, thus $(e^x) = \{-2, 7\}$
>    4. Solve for $x$: $x = \{log_e(-2), log_e(7)\}$
>    5. Filter out complex or undefined answers (in this case, $log_e(-2)$).
