---
title: 极限与泰勒公式
description: 数列与函数极限的定义、无穷小与无穷大的阶、运算法则、泰勒公式与麦克劳林展开、误差估计、二元函数的泰勒公式、洛必达法则、等价无穷小代换、夹逼与 Stolz 定理、常见极限。
---

# 极限与泰勒公式

[[toc]]

一元函数的极限

其它极限结论

数列极限的定义

设{xn}为一数列，如果存在任意给定的正数ε（不论它多么小），总存在正整数N，使得当n > N时，不等式

|xn − a| < ε

（对任意n）都成立，那么就称常数a使数列{xn}的极限，或者称数列{xn}收敛于a，记为

limn → ∞xn = a 或 xn → a(n → ∞)

如果不曾在这样的常数a，就说数列{xn}没有极限，或者说数列{xn}是发散的，习惯上也说limn → ∞xn不存在。

任意的ε实现了实现了“由大到小”的过程，并且保证了是“任意小”的。而N则说明了极限的存在只与数列最后的变化趋势有关，改变某一收敛数列的有限项，无法改变数列的趋势，可以把N取在所有改变项的后面，改变项后面的数列每一项仍保留收敛性质，因此对与n > N的任意n都满足。xn − a的绝对值则体现了收敛不一定单调，可以在极限上下震荡中靠近极限值。<体现与极限的接近性，在ε越来越小的过程中（实际没有“越来越小”的过程，只是由“任意给定”可以想象在若干次“任意”中ε越来越小），始终<，这就避开了xxx= a必须用等号写明的尴尬。

函数极限的定义

类比数列极限的定义，推广可得。这种定义方法被成为ε − δ语言。

<div class="table-scroll">
<table style="width:100%;">

<thead>
<tr>
<th></th>
<th>

f(x) → A

</th>
<th>

f(x) → +∞

</th>
<th>

f(x) → +∞

</th>
<th>

f(x) → −∞

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

x → x0

</td>
<td>

∀ε > 0，∃δ > 0，

∀x(0 < |x − x0| < δ)

: |f(x) − A|< ε

</td>
<td>

∀M > 0，∃δ > 0，

∀x(0 < |x − x0| < δ)

: |f(x)| > M

</td>
<td>

∀M > 0，∃δ > 0，

∀x(0 < |x − x0| < δ)

: f(x) > M

</td>
<td>

∀M > 0，∃δ > 0，

∀x(0 < |x − x0| < δ)

: f(x) < −M

</td>
</tr>
<tr>
<td>

x → x0+

</td>
<td>

∀ε > 0, ∃δ > 0,

∀x(0 < x − x0 < δ)

: |f(x) − A|< ε

</td>
<td>

∀M > 0，∃δ > 0，

∀x(0 < x − x0 < δ)

: |f(x)| > M

</td>
<td>

∀M > 0，∃δ > 0，

∀x(0 < x − x0 < δ)

: f(x) > M

</td>
<td>

∀M > 0，∃δ > 0，

∀x(0 < x − x0 < δ)

: f(x) < −M

</td>
</tr>
<tr>
<td>

x → x0−

</td>
<td>

∀ε > 0, ∃δ > 0，

∀x(0 > x − x0 > −δ)

: |f(x) − A|< ε

</td>
<td>

∀M > 0，∃δ > 0，

∀x(0 > x − x0 > −δ)

: |f(x)| > M

</td>
<td>

∀M > 0，∃δ > 0，

∀x(0 > x − x0 > −δ)

: f(x) > M

</td>
<td>

∀M > 0，∃δ > 0，

∀x(0 > x − x0 > −δ)

: f(x) < −M

</td>
</tr>
<tr>
<td>

x → ∞

</td>
<td>

∀ε > 0，∃X > 0，

∀x(|x| > X)

: |f(x) − A|< ε

</td>
<td>

∀M > 0，∃X > 0，

∀x(|x| > X)

: |f(x)| > M

</td>
<td>

∀M > 0，∃X > 0，

∀x(|x| > X)

: f(x) > M

</td>
<td>

∀M > 0，∃X > 0，

∀x(|x| > X)

: f(x) < −M

</td>
</tr>
<tr>
<td>

x → +∞

</td>
<td>

∀ε > 0，∃X > 0，

∀x(x > X)

: |f(x) − A|< ε

</td>
<td>

∀M > 0，∃X > 0，

∀x(x > X)

: |f(x)| > M

</td>
<td>

∀M > 0，∃X > 0，

∀x(x > X)

: f(x) > M

</td>
<td>

∀M > 0，∃X > 0，

∀x(x > X)

: f(x) < −M

</td>
</tr>
<tr>
<td>

x → −∞

</td>
<td>

∀ε > 0，∃X > 0，

∀x(x < −X)

: |f(x) − A|< ε

</td>
<td>

∀M > 0，∃X > 0，

∀x(x < −X)

: |f(x)| > M

</td>
<td>

∀M > 0，∃X > 0，

∀x(x < −X)

: f(x) > M

</td>
<td>

∀M > 0，∃X > 0，

∀x(x < −X)

: f(x) < −M

</td>
</tr>
</tbody>
</table>
</div>

无穷小、无穷大与阶

定义

无穷小：在某个变化过程中，若lim f(x) = 0，则称此时f(x)是无穷小（量），记作f(x) = o(1)  (x → xxx)

无特殊说明，一般默认是当x → 0时。

无穷大：在某个变化过程中，若lim f(x) = 0，则称此时f(x)是无穷大（量）。

运算法则

无穷小：o(1) ± o(1) = o(1)

o(1) ⋅ o(1) = o(1)

o(1) ⋅ O(1) = o(1)

$$\frac{\infty}{o(1)} = \infty$$

无穷大：(+∞) + (+∞) = +∞，(−∞) + (−∞) = −∞

(+∞) − (−∞) = +∞，(−∞) − (+∞) = −∞

(+∞) ± O(1) = +∞，(−∞) ± O(1) = −∞

(+∞) ⋅ (+∞) = +∞，(−∞) ⋅ (−∞) = +∞，(+∞) ⋅ (−∞) = −∞

∞ ⋅ O(1) = ∞

无穷小的倒数为无穷大，无穷大的倒数为无穷小，这使得无穷大和无穷小可以相互转换，在实际中更多地用到无穷小。

阶

阶类似于整式的次数概念，是衡量极限逼近速度快慢的指标。代数式的阶在一些情况下为代数式所有项的最大指数或最小指数。

无穷小量阶的比较

设f(x)，g(x)为两个无穷小，则

$$\lim\frac{f(x)}{g(x)} = \left\{ \begin{array}{r}
0\ \ \ \ \ \ \ \  \Rightarrow f(x)\text{是}g(x)\text{的高阶无穷小，记作}f(x) = o\left( g(x) \right) \\
\infty\ \ \ \ \ \ \  \Rightarrow f(x)\text{是}g(x)\text{的低阶无穷小，记作}g(x) = o\left( f(x) \right) \\
c \neq 0 \Rightarrow f(x)\text{是}g(x)\text{的同阶无穷小}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
1\ \ \ \ \ \ \ \  \Rightarrow f(x)\text{是}g(x)\text{的等价无穷小，记作}f(x)\sim g(x)\ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

$$\lim\frac{f(x)}{g^{k}(x)} = c \neq 0\  \Rightarrow f(x)\text{是}g(x)\text{的}k\text{阶无穷小}$$

对于f(x) = o(g(x))的情形（x → 0），若是多项式，则可以称f(x)的阶为g(x)的最高项的次数，如f(x) = o(x3 + 2x) = o(x3)，则f(x)的阶为3。

o()与O（）

o()表示无穷小（一般是对→ 0的），括号内常放入一个幂函数，如o(x3)表示比x3高阶的无穷小，如x4 = o(x3)，x5 = o(x3)，表示x4，x5比x3高阶，但反过来o(x3)不能替换为x4或x5。所以o()表示的不是某个确定的函数而是一系列更高阶的函数。

O()表示有界，

$$
0 \leq \left| \frac{u(x)}{v(x)} \right| \leq A \Leftrightarrow u(x) = O\left( v(x) \right)
$$

，其中u(x)和v(x)均为无穷小量。如$x\sin\frac{1}{x} = O(x)$表示当x → 0时，$x\sin\frac{1}{x}$为有界量。

泰勒公式

泰勒公式的一般形式

$${f(x) = \sum_{n = 1}^{N}{\frac{f^{(n)}\left( x_{0} \right)}{n!}\left( x - x_{0} \right)^{n}} + R_{n}(x)
}{= \frac{f\left( x_{0} \right)}{0!} + \frac{f'\left( x_{0} \right)}{1!}\left( x - x_{0} \right) + \frac{f^{''}\left( x_{0} \right)}{2!}\left( x - x_{0} \right)^{2} + \ldots + \frac{f^{(n)}\left( x_{0} \right)}{n!}\left( x - x_{0} \right)^{n} + R_{n}(x)}$$

其中Rn(x)称为余项，其具体有如下几种形式

佩亚诺余项：o((x − x0)n)

$$\text{施勒米希尔} - \text{罗什余项：}f^{(n + 1)}\left\lbrack x_{0} + \theta\left( x - x_{0} \right) \right\rbrack\frac{(1 - \theta)^{n + 1 - p}\left( x - x_{0} \right)^{n + 1}}{n!p}\ \ \left( \theta \in (0\text{，}1)\text{，}p \in \mathbb{R}_{+} \right)$$

$$\text{拉格朗日余项：}\frac{f^{(n + 1)}(\xi)}{(n + 1)!}\left( x - x_{0} \right)^{n + 1}\ \ \left( \xi \text{是}x_{0}\text{与}x\text{之间的某个值} \right)$$

$$\text{柯西余项：}f^{(n + 1)}\left\lbrack x_{0} + \theta\left( x - x_{0} \right) \right\rbrack\frac{(1 - \theta)^{n}\left( x - x_{0} \right)^{n + 1}}{n!}$$

$$\text{积分余项：}\frac{( - 1)^{n}}{n!}\int_{n}^{- x}{(t - x)^{n}f^{(n + 1)}(t)dt}$$

x的次数为几就称其为第几阶。

麦克劳林公式

令一般式中的x0 = 0，得

$$f(x) = \sum_{n = 1}^{N}{\frac{f^{(n)}(0)}{n!}x^{n}} + R_{n}(x) = \frac{f(0)}{0!} + \frac{f'(0)}{1!}x + \frac{f^{''}(0)}{2!}x^{2} + \ldots + \frac{f^{(n)}(0)}{n!}x^{n} + R_{n}(x)$$

常用函数的泰勒展开

$$1.e^{x} = 1 + \frac{x}{1} + \frac{x^{2}}{2} + \frac{x^{3}}{6} + \ldots + x^{n} + o\left( x^{n} \right) = \sum_{n = 0}^{\infty}\frac{x^{n}}{n!}\ \ $$

$$\Rightarrow \ \ a^{x} = e^{x\ln a} = \sum_{n = 0}^{\infty}\frac{\left( \ln a \right)^{n}x^{n}}{n!}$$

$$2.\sin x = \frac{x}{1!} - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + \ldots + \frac{( - 1)^{n}}{(2n + 1)!}x^{2n + 1} + o\left( x^{2n + 2} \right) = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{(2n + 1)!}x^{2n + 1}}$$

$$3.\cos x = 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} - \frac{x^{6}}{6!} + \ldots + \frac{( - 1)^{n}}{(2n)!}x^{2n} + o\left( x^{2n} \right) = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{(2n)!}x^{2n}}$$

$$4.\ln(1 + x) = x - \frac{x^{2}}{2!} + \frac{x^{3}}{3!} - \frac{x^{4}}{4!} + \ldots + \frac{( - 1)^{n - 1}}{n!}x^{n} + o\left( x^{n} \right) = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n - 1}}{n!}x^{n}}\ \ $$

$$\  \Rightarrow \ln(1 - x) = - x - \frac{x^{2}}{2!} - \frac{x^{3}}{3!} - \frac{x^{4}}{4!} + \ldots = \sum_{n = 0}^{\infty}{\frac{- 1}{n!}x^{n}}\ \ \left( |x| < 1 \right)\ \ $$

$$\Rightarrow \ln\frac{1 + x}{1 - x} = 2\left( x + \frac{1}{3}x^{3} + \frac{1}{5}x^{5} + \cdots \right) = 2\sum_{n = 0}^{\infty}\frac{x^{2n + 1}}{2n + 1}\ \ \left( |x| < 1 \right)$$

$$5.(1 + x)^{m} = 1 + mx + \frac{m(m - 1)}{2!}x^{2} + \cdots + \begin{pmatrix}
m \\
n
\end{pmatrix}x^{n} + o\left( x^{n} \right) = \sum_{n = 0}^{\infty}{\begin{pmatrix}
m \\
n
\end{pmatrix}x^{n}}\ \ \left( m\mathbb{\in N} \right)$$

$$6.(1 + x)^{a} = 1 + ax + \frac{a(a - 1)}{2!}x^{2} + \cdots + \frac{a(a - 1)\cdots(a - n + 1)}{a!}x^{n} + o(1)\ \ \left( a\mathbb{\in R} \right)$$

$$\Rightarrow \sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^{2}}{8} + \frac{x^{3}}{16} - \frac{5x^{4}}{128} + \ldots$$

$$\Rightarrow \frac{1}{1 + x} = 1 - x + x^{2} - x^{3} + \cdots = \sum_{n = 0}^{\infty}{( - 1)^{n}x^{n}}\ \ \left( |x| < 1 \right)\ \ $$

$$\Rightarrow \ \ \frac{1}{1 + x^{2}} = \sum_{n = 0}^{\infty}{( - 1)^{n}x^{2n}}\ \ \left( |x| < 1 \right)$$

$$\Rightarrow \frac{1}{1 - x} = 1 + x + x^{2} + x^{3} + \cdots = \sum_{n = 0}^{\infty}x^{n}\ \ \left( |x| < 1 \right)$$

$$7.\tan x = x + \frac{1}{3}x^{3} + \frac{2}{15}x^{5} + \cdots$$

泰勒公式的误差

由拉格朗日余项，误差不超过

$$\left| \frac{f^{(n + 1)}(\xi)}{(n + 1)!}\left( x - x_{0} \right)^{n + 1} \right|$$

因此，考虑ξ的值，使上式取最大值，所得到的范围即为误差范围

泰勒公式求极限

二元函数的泰勒公式

设z = f(x，y)上有两点(x0，y0)和(x0 + h，y0 + k)，则

f(x0 + h，y0 + k)

$$= f\left( x_{0}\text{，}y_{0} \right) + \left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)f\left( x_{0}\text{，}y_{0} \right) + \frac{1}{2!}\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)^{2}f\left( x_{0}\text{，}y_{0} \right) + \cdots + \frac{1}{n!}\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)^{n}f\left( x_{0}\text{，}y_{0} \right) + \frac{1}{(n + 1)!}\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)^{n + 1}f\left( x_{0} + \theta h\text{，}y_{0} + \theta k \right)$$

其中

$$\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)\ \ f\left( x_{0}\text{，}y_{0} \right)\text{表示}\ \ hf_{x}\left( x_{0}\text{，}y_{0} \right) + kf_{y}\left( x_{0}\text{，}y_{0} \right)$$

$$\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)^{2}f\left( x_{0}\text{，}y_{0} \right)\text{表示}\ \ h^{2}f_{xx}\left( x_{0}\text{，}y_{0} \right) + 2hkf_{xy}\left( x_{0}\text{，}y_{0} \right) + k^{2}f_{yy}\left( x_{0}\text{，}y_{0} \right)$$

⋯⋯⋯

$$\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)^{n}f\left( x_{0}\text{，}y_{0} \right)\text{表示}\sum_{p = 0}^{m}{C_{m}^{p}h^{p}k^{m - p}\frac{\partial^{m}f}{\partial x^{p}\partial y^{m - p}}}\left| \underset{\left( x_{0}\text{，}y_{0} \right)}{} \right.\ $$

0 < θ < 1

也就是说，对于二元函数f(x，y)，有

f(x + x0，y + y0)

$$= f\left( x_{0}\text{，}y_{0} \right) + \left( x\frac{\partial}{\partial x} + y\frac{\partial}{\partial y} \right)f\left( x_{0}\text{，}y_{0} \right) + \frac{1}{2!}\left( x\frac{\partial}{\partial x} + y\frac{\partial}{\partial y} \right)^{2}f\left( x_{0}\text{，}y_{0} \right) + \cdots + \frac{1}{n!}\left( x\frac{\partial}{\partial x} + y\frac{\partial}{\partial y} \right)^{n}f\left( x_{0}\text{，}y_{0} \right) = \sum_{i = 1}^{n}{\left( x\frac{\partial}{\partial x} + y\frac{\partial}{\partial y} \right)^{i}f\left( x_{0}\text{，}y_{0} \right)}$$

$$eg.x^{y} = 1 + (x - 1) + (x - 1)(y - 1) + \frac{1}{2}(x - 1)^{2}(y - 1) + R_{3}\ \left( (1\text{，}1)\text{处展开} \right)$$

L’Hospital（洛必达）法则

$$\text{设}f(x)\text{，}g(x)\text{可导，}\ g'(x) \neq 0\text{，}\lim\frac{f'(x)}{g'(x)}\text{存在，当满足以下两个条件}$$

1.lim f(x) = lim g(x) = 0

2.lim g(x) = ∞

中的一个时，即有

$$\lim\frac{f(x)}{g(x)} = \lim\frac{f'(x)}{g'(x)}$$

特殊极限定义式及推论

$$1.\lim_{x \rightarrow 0}\frac{\sin x}{x} = 1$$

$$2.\lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n} = \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n + 1} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{1}{x} \right)^{x} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{k}{x} \right)^{x} = \lim_{\frac{x}{k} \rightarrow \infty}\left( 1 + \frac{1}{\frac{x}{k}} \right)^{\frac{x}{k} \cdot k} = e^{k} \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{a}{x} \right)^{bx + c} = e^{ab}$$

$$\text{特别地，}e^{x} = \lim_{n \rightarrow \infty}\left( 1 + \frac{x}{n} \right)^{n} = \exp(x)$$

lim u(x)v(x) = elim [(u(x) − 1)v(x)]，其中在同一过程中lim u(x) = 1，lim v(x) = ∞

$$3.\lim_{n \rightarrow \infty}\left( 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} - \ln n \right) = \gamma = 0.557\ 215\ 664\ 90\cdots$$

等价无穷小代换

常见的等价无穷小可以用洛必达法则轻易地得出，等价无穷小替换可以视为泰勒公式的简易应用。

一阶：

$$
x\ \ \sim\ \ \sin x\ \ \sim\ \ \tan x\ \ \sim\ \ \arcsin{x\ \ }\sim\ \ \arctan x\ \ \sim\ \ e^{x} - 1\ \ \sim\ \ \ln(1 + x)\ \  \sim \ \ \sqrt{1 + x} - \sqrt{1 - x}
$$

$$\text{二阶：}\frac{1}{2}x^{2}\ \  \sim \ \ 1 - \cos x\ \ \sim\ \ x - \ln(1 + x)\ \  \sim \ \ e^{x} - x - 1\sim - \ln{\cos x}$$

三阶：

$$\frac{1}{2}x^{3}\ \  \sim \ \tan x - \sin x\ \  \sim \ \ \arcsin x - \arctan x$$

$$\frac{1}{3}x^{3}\ \  \sim \ \ \tan x - x\ \  \sim \ \ x - \arctan x\ \  \sim \ \ \arcsin x - \sin x$$

$$\frac{2}{3}x^{3}\ \  \sim \ \ \tan x - \arctan x$$

$$- \frac{1}{3}x^{3}\ \  \sim \ \ x - \ln(1 + x) - \frac{x^{2}}{2}$$

$$\frac{1}{6}x^{3}\  \sim \ \ x - \sin x\  \sim \ \tan x - \arcsin x\  \sim \ \arcsin x - x\  \sim \ \sin x - \arctan x$$

其它：

(1 + x)m − 1 ∼ mx

$$\log_{a}(1 + x)\sim\frac{x}{\ln a}$$

ax − 1 ∼ xln a

1 − x ∼ −ln x  (x → 1)

一些等价无穷小代换的证明

$$\lim_{x \rightarrow 0}\frac{\sin x}{x} = 1$$

$$\lim_{x \rightarrow 0}\frac{\tan x}{x} = \lim_{x \rightarrow 0}\left( \frac{x}{\sin x} \cdot \cos x \right) = \lim_{x \rightarrow 0}\frac{x}{\sin x} \cdot \lim_{x \rightarrow 0}{\cos x} = 1$$

$$\lim_{x \rightarrow 0}\frac{\arcsin x}{x} = \lim_{t \rightarrow 0}\frac{t}{\sin t} = 1$$

$$\lim_{x \rightarrow 0}\frac{\arctan x}{x} = \lim_{t \rightarrow 0}\frac{t}{\tan t} = 1$$

$$\lim_{x \rightarrow 0}\frac{\ln(1 + x)}{x} = \lim_{x \rightarrow 0}{\ln(1 + x)^{\frac{1}{x}}} = \ln{\lim_{x \rightarrow 0}(1 + x)^{\frac{1}{x}}} = \ln e = 1$$

$$\lim_{x \rightarrow 0}\frac{e^{x} - 1}{x} = \lim_{t \rightarrow 0}\frac{t}{\ln(1 + t)} = 1$$

$$\lim_{x \rightarrow 0}\frac{(1 + x)^{\alpha} - 1}{\alpha x} = \lim_{x \rightarrow 0}\left( \frac{(1 + x)^{\alpha} - 1}{\ln(1 + x)^{\alpha}} \cdot \frac{\alpha\ln(1 + x)}{\alpha x} \right)\overset{(1 + x)^{\alpha} - 1 = t}{\Leftrightarrow}\lim_{t \rightarrow 0}\frac{t}{\ln(1 + t)} \cdot \lim_{x \rightarrow 0}\frac{\alpha\left( 1 + \ln x \right)}{\alpha x} = 1$$

$$- \ln{\cos x} = - \ln\left\lbrack 1 + \left( \cos x - 1 \right) \right\rbrack\sim - \left( \cos x - 1 \right)\sim\frac{1}{2}x^{2}$$

$$\ln(x + 1)\sim x\ \ (x \rightarrow 0)\overset{t = x + 1}{\Leftrightarrow}\ln t\sim t - 1\ \ (t \rightarrow 1) \Leftrightarrow - \ln x\sim 1 - x\ \ (x \rightarrow 1)$$

与极限有关的定理和结论

1.夹逼定理

数列{xn}，{yn}，{zn}从某项起开始满足

xn ≤ yn ≤ zn，limn → ∞xn = limn → ∞zn = a

则

limn → ∞yn = a

证明：对{xn}和{zn}由定义，有a − ε < xn < a + ε，a − ε < zn < a + ε，由xn ≤ yn ≤ zn，有

a − ε < xn ≤ yn ≤ zn < a + ε

满足极限的定义，得证。

2.Stolz定理

对数列{xn}，{yn}

$$\left. \text{（}1 \right.\text{）若}\left\{ y_{n} \right\} \text{严格单调递增趋于}\  + \infty \text{，且}\lim_{n \rightarrow \infty}\frac{x_{n} - x_{n - 1}}{y_{n} - y_{n - 1}} = a\text{，则}\ \lim_{n \rightarrow \infty}\frac{x_{n}}{y_{n}} = a\ \ (a\text{可以为某数或} \pm \infty)$$

$$(2)\text{若}\left\{ y_{n} \right\} \text{严格单调递减趋于}\ 0\text{，}\left\{ x_{n} \right\} \text{趋于}0\text{，且}\lim_{n \rightarrow \infty}\frac{x_{n} - x_{n - 1}}{y_{n} - y_{n - 1}} = a\text{，则}\ \lim_{n \rightarrow \infty}\frac{x_{n}}{y_{n}} = a\ \ (a\text{可以为某数或} \pm \infty)$$

3.单调有界收敛定理：单调有界数列必定收敛。

4. 闭区间套定理：如果{[an，bn]}构成一个闭区间套，则存在唯一的实数ξ属于所有的闭区间[an，bn]，且ξ = limn → ∞an = limn → ∞bn。

5.若数列{xn}收敛于a，则其任何子数列也收敛于a。

6.Cauchy（柯西）收敛原理：数列{xn}收敛的充要条件是{xn}是基本数列。基本数列{xn}满足：对于任意的ε > 0，存在正整数N，使得当n, m > N时|xn − xm| < ε恒成立。

常见极限

$$\cdot \lim_{x \rightarrow 0}\frac{a_{0}x^{m} + a_{1}x^{m - 1} + \cdots + a_{m}}{b_{0}x^{n} + b_{1}x^{n - 1} + \cdots + b_{n}} = \left\{ \begin{array}{r}
0\text{，当}a_{m} = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\frac{a_{m}}{b_{n}}\text{，当}a_{m} \neq 0\text{且}b_{n} \neq 0 \\
\infty \text{，当}b_{n} = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ \ \ \ \left( a_{m}\text{，}b_{n}\text{不同时为}0 \right)$$

$$\cdot \lim_{x \rightarrow \infty}\frac{a_{0}x^{m} + a_{1}x^{m - 1} + \cdots + a_{m}}{b_{0}x^{n} + b_{1}x^{n - 1} + \cdots + b_{n}} = \left\{ \begin{array}{r}
0\text{，当}n > m \\
\frac{a_{0}}{b_{0}}\text{，当}n = m \\
\infty \text{，当}n < m
\end{array} \right.\ $$

$$\cdot \lim_{n \rightarrow \infty}{n\sin\frac{180{^\circ}}{n}} = \pi \Rightarrow \lim_{n \rightarrow + \infty}\frac{\sin\frac{\pi}{n}}{\frac{\pi}{n}} = 1 \Rightarrow \lim_{x \rightarrow 0}\frac{\sin x}{x} = 1$$

$$\cdot \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n} = \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n + 1} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{1}{x} \right)^{x} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{k}{x} \right)^{x} = \lim_{\frac{x}{k} \rightarrow \infty}\left( 1 + \frac{1}{\frac{x}{k}} \right)^{\frac{x}{k} \cdot k} = e^{k} \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{a}{x} \right)^{bx + c} = e^{ab}$$

$$\text{特别地，}e^{x} = \lim_{n \rightarrow \infty}\left( 1 + \frac{x}{n} \right)^{n} = \exp(x)$$

$$\cdot \lim_{x \rightarrow \infty}\frac{x^{n}}{e^{\lambda x}} = 0$$

$$\cdot \lim_{x \rightarrow \infty}\frac{a^{x}}{x!} = 0$$

⋅limx → 0xln x = 0

对ln x关于1泰勒展开，得

$$\ln x = 0 + (x - 1) - \frac{1}{2}(x - 1)^{2} + \frac{1}{3}(x - 1)^{3} - \frac{1}{4}(x - 1)^{4} + \cdots$$

故

$$x\ln x = x(x - 1) - \frac{1}{2}x(x - 1)^{2} + \frac{1}{3}x(x - 1)^{3} - \frac{1}{4}x(x - 1)^{4} + \cdots$$

当x → 0时，由于(x − 1)n = ±1有界，故x(x − 1)n趋于0，式子各项趋于0，得证

也可以用洛必达法则

$$\lim_{x \rightarrow 0}{x\ln x} = \lim_{x \rightarrow 0}\frac{\ln x}{\frac{1}{x}} = \lim_{x \rightarrow 0}\frac{\frac{1}{x}}{- \frac{1}{x^{2}}} = \lim_{x \rightarrow 0}\frac{- x}{1} = 0$$

⋅limx → ∞(x − ln x) = +∞

$$\lim_{x \rightarrow \infty}\left( x - \ln x \right) = \lim_{x \rightarrow 0}\left( \frac{1}{x} - \ln\frac{1}{x} \right) = \lim_{x \rightarrow 0}\left( \frac{1}{x} + \ln x \right) = \lim_{x \rightarrow 0}\left( \frac{1}{x} + \ln x \right) = \lim_{x \rightarrow 0}\left( \frac{1 + x\ln x}{x} \right) = \lim_{x \rightarrow 0}\frac{1}{x} = + \infty$$

$$\cdot \lim_{n \rightarrow \infty}\sqrt[n]{n} = 1$$

$$\cdot \lim_{n \rightarrow \infty}\sqrt[n]{n^{k}} = 1$$

$$\cdot \text{若}\ \lim_{n \rightarrow \infty}a_{n} = a\text{，则}\ \lim_{n \rightarrow \infty}\frac{a_{1} + a_{2} + \cdots + a_{n}}{n} = a$$

$$\cdot \lim_{n \rightarrow \infty}\left( a_{1}^{n} + a_{2}^{n} + \cdots + a_{p}^{n} \right)^{\frac{1}{n}} = \max_{1 \leq i \leq p}\left\{ a_{i} \right\}$$

$$\cdot \lim_{n \rightarrow \infty}{n\left( \sqrt{n^{2} + 1} - \sqrt{n^{2} - 1} \right)} = 1$$

$$\text{若}\ \lim_{n \rightarrow \infty}a_{n} = a\text{，则}\ \lim_{n \rightarrow \infty}\sqrt[n]{a_{1}a_{2}\cdots a_{n}} = a$$

$$\cdot \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} - \ln n \right) = \gamma = 0.557\ 215\ 664\ 90\cdots$$
