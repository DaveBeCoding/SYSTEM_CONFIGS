Syntax
Headers

# This is an <h1> tag
## This is an <h2> tag
###### This is an <h6> tag

Emphasis

*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_

Lists
Unordered

- Item 1
- Item 2
  - Item 2a
  - Item 2b

Ordered

1. Item 1
2. Item 2
3. Item 3
   1. Item 3a
   2. Item 3b

Images

![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)

Links

http://github.com - automatic!
[GitHub](http://github.com)

Blockquotes

As Kanye West said:

> We're living the future so
> the present is our past.

Inline code

To print some text with python, you should use the `print()` function.
```
print("Hello world!")
```

Writing Math

Math formulas are easy to write using Markdown, either using the inline mode or the displayed formulas mode. With the inline mode, formulas are inlined in the current paragraph whereas with the displayed mode, they appear as centered and emphasized.

The formatting generally slightly differs in both cases since, to display nicely on a single line, it is generally required to pack them a bit more than when they are emphasized.

To write formulas using the inline mode, they should be surrounded by a single $ (as a consequence, whenever you need to use the original dollar symbol, you should prefix it with a backslash: \$). To write formulas using the displayed mode, they should be surrounded by a $$. Here are a few examples:

This expression $\sum_{i=1}^n X_i$ is inlined.

This expression ∑ni=1Xi

is inlined.

This expression is emphasized:

$$\sum_{i=1}^n X_i$$

This expression is emphasized:

n∑i=1Xi

In the rest of this section we present a brief selection of common symbols and commands. Actually, almost any classical LaTeX command can used as such in Markdown, provided it is surrounded by a $. For more complete examples, please have a look at these ces examples by James H. Steiger.
Greek Letters
Symbol 	Command
α
	$\alpha$
β
	$\beta$
γ
	$\gamma$
Γ
	$\Gamma$
π
	$\pi$
Usual functions and operators
Symbol 	Command
cos
	$\cos$
sin
	$\sin$
lim
	$\lim$
exp
	$\exp$
→
	$\to$
∈
	$\in$
∀
	$\forall$
∃
	$\exists$
≡
	$\equiv$
∼
	$\sim$
≈
	$\approx$
×
	$\times$
≤
	$\le$
≥
	$\ge$
Exponents and indices
Symbol 	Command
kn+1
	$k_{n+1}$
n2
	$n^2$
k2n
	$k_n^2$
Fractions, binomial coefficients, square roots, …
Symbol 	Command
4z316
	$\frac{4z^3}{16}$
n!k!(n−k)!
	$\frac{n!}{k!(n-k)!}$
(nk)
	$\binom{n}{k}$
x1x−y
	$\frac{\frac{x}{1}}{x - y}$
3/7
	$^3/_7$
√k
	$\sqrt{k}$
n√k
	$\sqrt[n]{k}$
Summations and integrals
Symbol 	Command
∑10i=1ti
	$\sum_{i=1}^{10} t_i$
∫∞0e−xdx
	$\int_0^\infty \mathrm{e}^{-x}\,\mathrm{d}x$
Outfits
Symbol 	Command
^a
	$\hat{a}$
¯a
	$\bar{a}$
˙a
	$\dot{a}$
¨a
	$\ddot{a}$
−−→AB
	$\overrightarrow{AB}$
