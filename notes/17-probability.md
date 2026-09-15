---
title: 概率论与数理统计
description: 排列组合、随机变量及其分布、分布特征数、大数定律与中心极限定理、抽样分布、点估计与假设检验。
---
# 概率论与数理统计

[[toc]]

## 排列组合

### 排列

$$A_{n}^{r} = P_{n}^{r} = n(n - 1)\cdots(n - r + 1) = \frac{n!}{(n - r)!}$$

### 组合

$$C_{n}^{r} = \begin{pmatrix}
n \\
r
\end{pmatrix} = \frac{A_{n}^{r}}{A_{r}^{r}} = \frac{n(n - 1)\cdots(n - r + 1)}{r!} = \frac{n!}{r!(n - r)!}$$

## 排列组合公式

$$\begin{pmatrix}
n \\
r
\end{pmatrix} = \begin{pmatrix}
n \\
n - r
\end{pmatrix}$$

$$\begin{pmatrix}
n \\
r
\end{pmatrix} = \begin{pmatrix}
n - 1 \\
r - 1
\end{pmatrix} + \begin{pmatrix}
n - 1 \\
r
\end{pmatrix}$$

$$\begin{pmatrix}
n \\
r
\end{pmatrix} = \frac{n - r + 1}{r}\begin{pmatrix}
n \\
r - 1
\end{pmatrix} = \frac{n}{n - r}\begin{pmatrix}
n - 1 \\
r
\end{pmatrix} = \frac{r + 1}{n + 1}\begin{pmatrix}
n + 1 \\
r + 1
\end{pmatrix} = \frac{n}{r}\begin{pmatrix}
n - 1 \\
r - 1
\end{pmatrix}$$

$$\begin{pmatrix}
n \\
0
\end{pmatrix} + \begin{pmatrix}
n \\
1
\end{pmatrix} + \cdots + \begin{pmatrix}
n \\
n
\end{pmatrix} = 2^{n}$$

$$\begin{pmatrix}
n \\
1
\end{pmatrix} + 2\begin{pmatrix}
n \\
2
\end{pmatrix} + \cdots + n\begin{pmatrix}
n \\
n
\end{pmatrix} = n2^{n - 1}$$

$$\begin{pmatrix}
a \\
0
\end{pmatrix}\begin{pmatrix}
b \\
n
\end{pmatrix} + \begin{pmatrix}
a \\
1
\end{pmatrix}\begin{pmatrix}
b \\
n - 1
\end{pmatrix} + \cdots + \begin{pmatrix}
a \\
n
\end{pmatrix}\begin{pmatrix}
b \\
0
\end{pmatrix} = \begin{pmatrix}
a + b \\
n
\end{pmatrix}\text{，}n = \min\left\{ a\text{，}b \right\}$$

$$\begin{pmatrix}
r \\
r
\end{pmatrix} + \begin{pmatrix}
r + 1 \\
r
\end{pmatrix} + \cdots + \begin{pmatrix}
r + n \\
r
\end{pmatrix} = \begin{pmatrix}
r + n + 1 \\
r + 1
\end{pmatrix}$$

$$\begin{pmatrix}
n \\
0
\end{pmatrix}^{2} + \begin{pmatrix}
n \\
1
\end{pmatrix}^{2} + \cdots + \begin{pmatrix}
n \\
n
\end{pmatrix}^{2} = \begin{pmatrix}
2n \\
n
\end{pmatrix}$$

<div class="table-scroll">
<table>
<tr>
<th rowspan="16">

分布函数

</th>
<th>

$$F(x) = P(X \leq x)$$

</th>
<th>

$$F(x,y) = P(X \leq x,Y \leq y)$$

</th>
</tr>
<tr>
<td colspan="2">

$F(x)$是$\mathbb{R}$上的单调非减右连续函数

</td>
</tr>
<tr>
<td colspan="2">

$$0 \leq F(x) \leq 1$$

</td>
</tr>
<tr>
<td colspan="2">

$$F( - \infty) = \lim_{x \rightarrow - \infty}{F(x)} = 0,\ \ F( + \infty) = \lim_{x \rightarrow + \infty}{F(x)} = 1$$

</td>
</tr>
<tr>
<td colspan="2">

$$F(x)右连续，即F\left( x_{0} + 0 \right) = F\left( x_{0} \right)/\lim_{x \rightarrow x_{0}^{+}}{F(x)} = F\left( x_{0} \right)$$

</td>
</tr>
<tr>
<td colspan="2">

$P\left( X = x_{0} \right) = F\left( x_{0} - 0 \right) = \lim_{x \rightarrow x_{0}^{-}}{F(x)}$（左极限）

</td>
</tr>
<tr>
<td colspan="2">

$$P(a < X \leq b) = F(b) - F(a)$$

</td>
</tr>
<tr>
<td colspan="2">

$$P(a \leq X < b) = F(b - 0) - F(a - 0)$$

</td>
</tr>
<tr>
<td colspan="2">

$F(x.y)$分别对$x$或$y$单调非减，即

</td>
</tr>
<tr>
<td colspan="2">

$$\forall x_{1} < x_{2},F\left( x_{1},y \right) \leq F\left( x_{2},y \right)，有\forall y_{1} < y_{2},F\left( x,y_{1} \right) \leq F\left( x,y_{2} \right)$$

</td>
</tr>
<tr>
<td colspan="2">

$$0 \leq F(x,y) \leq 1$$

</td>
</tr>
<tr>
<td colspan="2">

$$F( - \infty,y) = \lim_{x \rightarrow - \infty}{F(x,y)} = 0$$

</td>
</tr>
<tr>
<td colspan="2">

$$F(x, - \infty) = \lim_{y \rightarrow - \infty}{F(x,y)} = 0$$

</td>
</tr>
<tr>
<td colspan="2">

$$F( + \infty, + \infty) = \lim_{x,y \rightarrow + \infty}{F(x,y)} = + \infty$$

</td>
</tr>
<tr>
<td colspan="2">

$$F(x + 0,y) = F(x,y),\ \ F(x,y + 0) = F(x,y)$$

</td>
</tr>
<tr>
<td colspan="2">

$$\forall a < b,c < d，有P(a < X \leq b,c < Y \leq d) = F(b,d) - F(a,d) - F(a,c) + F(a,c) \geq 0$$

</td>
</tr>
<tr>
<td rowspan="3">

分布列

</td>
<td>

$$p_{i} = p\left( x_{i} \right) = P\left( X = x_{i} \right)$$

</td>
<td>

$$p_{ij} = P\left( X = x_{i},Y = y_{j} \right)$$

</td>
</tr>
<tr>
<td colspan="2">

$$p\left( x_{i} \right) \geq 0,i = 1,2,\cdots \\ \sum_{i}^{}{p\left( x_{i} \right)} = 1$$

</td>
</tr>
<tr>
<td colspan="2">

$$p_{ij} \geq 0 \\ \sum_{i}^{}{\sum_{j}^{}p_{ij}} = 1$$

</td>
</tr>
<tr>
<td rowspan="4">

概率密度函数

</td>
<td>

$$F(x) = \int_{- \infty}^{x}{p(t)dt}$$

</td>
<td>

$$F(x,y) = \int_{- \infty}^{x}{\int_{- \infty}^{y}{p(u,v)dvdu}}$$

</td>
</tr>
<tr>
<td colspan="2">

$$p(x) \geq 0 \\ p(x,y) \geq 0$$

</td>
</tr>
<tr>
<td colspan="2">

$$\int_{- \infty}^{+ \infty}{p(x)dx} = 1 \\ \int_{- \infty}^{+ \infty}{\int_{- \infty}^{+ \infty}{p(x,y)dydx}} = 1$$

</td>
</tr>
<tr>
<td colspan="2">

$$P(a < X \leq b) = \int_{a}^{b}{p(x)dx} \\ P\left( (X,Y) \in D \right) = \iint_{D}^{}{p(x,y)dxdy}$$

</td>
</tr>
<tr>
<td rowspan="4">

经验分布函数

</td>
<td colspan="2">

$$F_{n}(x) = \left\{ \begin{array}{r} 0,\ \ x < x_{(1)}\ \ \ \ \ \ \ \ \ \  \\ k\text{/}n,\ \ x_{(k)} \leq x < \\ 1,\ \ x > x_{(n)}\ \ \ \ \ \ \ \ \ \ \end{array} \right.\ x_{(k + 1)}$$

</td>
</tr>
<tr>
<td colspan="2">

$F_{n}(x)$是非减右连续函数

</td>
</tr>
<tr>
<td colspan="2">

$$F_{n}( - \infty) = 0,\ \ F_{n}( + \infty) = 1$$

</td>
</tr>
<tr>
<td colspan="2">

Glivenko（格利文科）定理：$P\left( \sup_{- \infty < x < + \infty}\left\vert F_{n}(x) - F(x) \right\vert \rightarrow 0 \right) = 1$

</td>
</tr>
<tr>
<td>

概率函数

</td>
<td colspan="2">

分布列或概率密度函数

</td>
</tr>
</table>
</div>

<div class="table-scroll">
<table>

<thead>
<tr>
<th></th>
<th>

离散

</th>
<th>

连续

</th>
</tr>
<tr>
<th>

分布函数

</th>
<th>

F(x) = P(X ≤ x)

</th>
</tr>
<tr>
<th>

F(x, y) = P(X ≤ x, Y ≤ y)

</th>
</tr>
<tr>
<th>

分布列/概

率密度函数

</th>
<th>

pi = p(xi) = P(X = xi)

</th>
<th>

F(x) = ∫−∞xp(t)dt

</th>
</tr>
<tr>
<th>

pij = P(X = xi, Y = yj)

</th>
<th>

F(x, y) = ∫−∞x∫−∞yp(u, v)dvdu

</th>
</tr>
<tr>
<th>

边际分布

</th>
<th>

FX(x) = F(x, +∞)

FY(y) = F(+∞, y)

</th>
</tr>
<tr>
<th>

$$p_{i \cdot} = \sum_{j}^{\infty}p_{ij}$$

$$p_{\cdot j} = \sum_{i}^{\infty}p_{ij}$$

</th>
<th>

pX = ∫−∞+∞p(x, y)dy

pY = ∫−∞+∞p(x, y)dx

</th>
</tr>
<tr>
<th>

条件分布

</th>
<th>

F(x|yi)=

$$\sum_{x_{i} \leq x}^{}{P\left( X = x_{i}\text{|}Y = y_{j} \right)} = \sum_{x_{i} \leq x}^{}p_{i\text{|}j}$$

F(y|xi)=

$$\sum_{y_{j} \leq y}^{}{P\left( Y = y_{j}\text{|}X = x_{i} \right)} = \sum_{y_{j} \leq y}^{}p_{j\text{|}i}$$

</th>
<th>

$$F\left( x\text{|}y \right) = \int_{- \infty}^{x}{\frac{p(u,y)}{p_{Y}(y)}du}$$

$$F\left( y\text{|}x \right) = \int_{- \infty}^{y}{\frac{p(x,v)}{p_{X}(x)}dv}$$

</th>
</tr>
<tr>
<th>

条件概率

</th>
<th>

P(AB) = P(A)P(B|A)

P(A1A2⋯An) = P(A1)P(A2|A3)⋯P(An|A1A2⋯An − 1)

</th>
</tr>
<tr>
<th>

$${p_{i\text{|}j} = P\left( X = x_{i}\text{|}Y = y_{j} \right)
}{= \frac{P\left( X = x_{i},Y = y_{j} \right)}{P\left( Y = y_{j} \right)} = \frac{p_{ij}}{p_{\cdot j}}}$$

$${p_{j\text{|}i} = P\left( Y = y_{j}\text{|}X = x_{i} \right)
}{= \frac{P\left( X = x_{i},Y = y_{j} \right)}{P\left( X = x_{i} \right)} = \frac{p_{ij}}{p_{i \cdot}}}$$

</th>
<th>

$$p\left( x\text{|}y \right) = \frac{p(x,y)}{p_{Y}(y)}$$

$$p\left( y\text{|}x \right) = \frac{p(x,y)}{p_{X}(x)}$$

</th>
</tr>
<tr>
<th>

全概率公式

</th>
<th>

$$P(B) = \sum_{i}^{}{P\left( A_{i} \right)P\left( B|A_{i} \right)},\ \ \text{其中}\bigcup_{i}^{}A_{i} = \Omega$$

</th>
</tr>
<tr>
<th>

$$p_{i \cdot} = \sum_{j = 1}^{+ \infty}{p_{\cdot j}p_{i\text{|}j}}$$

$$p_{\cdot j} = \sum_{i = 1}^{+ \infty}{p_{i \cdot}p_{j\text{|}i}}$$

</th>
<th>

pX(x) = ∫−∞+∞pY(y)p(x|y)dy

pY(y) = ∫−∞+∞pX(x)p(y|x)dx

</th>
</tr>
<tr>
<th>

贝叶斯公式

</th>
<th>

$$P\left( A_{i} \middle| B \right) = \frac{P\left( A_{i}B \right)}{P(B)} = \frac{P\left( A_{i} \right)P\left( B \middle| A_{i} \right)}{P(B)} = \frac{P\left( A_{i} \right)P\left( B \middle| A_{i} \right)}{\sum_{k = 1}^{n}{P\left( A_{k} \right)P\left( B \middle| A_{k} \right)}}$$

</th>
</tr>
<tr>
<th>

$$p_{i\text{|}j} = \frac{p_{i \cdot}p_{j\text{|}i}}{\sum_{i = 1}^{+ \infty}{p_{i \cdot}p_{j\text{|}i}}}$$

$$p_{j\text{|}i} = \frac{p_{\cdot j}p_{i\text{|}j}}{\sum_{j = 1}^{+ \infty}{p_{\cdot j}p_{i\text{|}j}}}$$

</th>
<th>

$$p\left( x\text{|}y \right) = \frac{p_{X}(x)p\left( y\text{|}x \right)}{\int_{- \infty}^{+ \infty}{p_{X}(x)p\left( y\text{|}x \right)dx}}$$

$$p\left( y\text{|}x \right) = \frac{p_{Y}(y)p\left( x\text{|}y \right)}{\int_{- \infty}^{+ \infty}{p_{Y}(y)p\left( x\text{|}y \right)dy}}$$

</th>
</tr>
<tr>
<th>

两两独立

</th>
<th>

P(AB) = P(A)P(B),  P(AC) = P(A)P(C),  P(BC) = P(B)P(C)

</th>
</tr>
<tr>
<th>

相互独立

</th>
<th>

P(AB) = P(A)P(B),  P(AC) = P(A)P(C),  P(BC) = P(B)P(C)

P(ABC) = P(A)P(B)P(C)

$$F\left( x_{1},x_{2},\cdots,x_{n} \right) = \prod_{i}^{}{F_{i}\left( x_{i} \right)}$$

</th>
</tr>
<tr>
<th>

$$P\left( X_{1} = x_{1},X_{2} = x_{2},\cdots,X_{n} = x_{n} \right) = \prod_{i}^{}{P\left( X_{i} = x_{i} \right)}$$

</th>
<th>

$$p\left( x_{1},x_{2},\cdots,x_{n} \right) = \prod_{i}^{}{p_{i}\left( x_{i} \right)}$$

</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
</div>

<div class="table-scroll">
<table style="width:100%;">

<thead>
<tr>
<th>

分布

</th>
<th>

分布列pk或分布密度函数p(x)

特征函数φ(t) = E(eitX)

</th>
<th>

期望

</th>
<th>

方差

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

单点分布

</td>
<td>

P(X = a) = 1

eita

</td>
<td>

a

</td>
<td>

0

</td>
</tr>
<tr>
<td>

0—1分布

</td>
<td>

pk = pk(1 − p)1 − k,  k = 0, 1

peit + q

</td>
<td>

p

</td>
<td>

p(1 − p)

</td>
</tr>
<tr>
<td>

二项分布

b(n, p)

</td>
<td>

$$p_{k} = \begin{pmatrix}
n \\
k
\end{pmatrix}p^{k}(1 - p)^{n - k}$$

k = 0, 1, ⋯, n

(peit + q)n

</td>
<td>

np

</td>
<td>

np(1 − p)

</td>
</tr>
<tr>
<td>

多/r项分布

M(n, p1, p2, ⋯, pn)

</td>
<td>

P(X1 = n1, X2 = n2⋯Xr = nr)=

$$\frac{n!}{n_{1}!n_{2}!\cdots n_{r}!}p_{1}^{n_{1}}\cdots p_{r}^{n_{r}}$$

</td>
<td></td>
<td></td>
</tr>
<tr>
<td>

泊松分布

P(λ)

</td>
<td>

$$p_{k} = \frac{\lambda^{k}}{k!}e^{- \lambda},\ \ k = 0,1,\cdots$$

exp {λ(eit − 1)}

</td>
<td>

λ

</td>
<td>

λ

</td>
</tr>
<tr>
<td></td>
</tr>
<tr>
<td>

超几何分布

h(n, N, M)

</td>
<td>

$$p_{k} = \frac{\begin{pmatrix}
M \\
k
\end{pmatrix}\begin{pmatrix}
N - M \\
n - k
\end{pmatrix}}{\begin{pmatrix}
N \\
n
\end{pmatrix}},\ \begin{matrix}
k = 0,1,\cdots,r \\
r = \min\left\{ M,n \right\}
\end{matrix}$$

2F1(−k, −n; N − k + 1; eit)

</td>
<td>

$$n\frac{M}{N}$$

</td>
<td>

$$\frac{nM(N - M)(N - n)}{N^{2}(N - 1)}$$

</td>
</tr>
<tr>
<td>

多维

超几何分布

</td>
<td>

P(X1 = n1, X2 = n2⋯Xr = nr)=

$$\frac{\begin{pmatrix}
N_{1} \\
n_{1}
\end{pmatrix}\begin{pmatrix}
N_{2} \\
n_{2}
\end{pmatrix}\cdots\begin{pmatrix}
N_{r} \\
n_{r}
\end{pmatrix}}{\begin{pmatrix}
N \\
n
\end{pmatrix}}$$

</td>
<td></td>
<td></td>
</tr>
<tr>
<td>

几何分布

Ge(p)

</td>
<td>

pk = (1 − p)k − 1p,  k = 1, 2, ⋯

$$\frac{pe^{it}}{1 - (1 - p)e^{it}}$$

</td>
<td>

$$\frac{1}{p}$$

</td>
<td>

$$\frac{1 - p}{p^{2}}$$

</td>
</tr>
<tr>
<td>

X1 + X2 + ⋯ + Xr ∼ Nb(r, p)，其中Xi ∼ Ge(p)

几何分布的无记忆性：设X ∼ Ge(p)，∀m, n ∈ ℤ，有

P(X > m + n|X > m) = P(X > n)

</td>
</tr>
<tr>
<td>

负二项分布

Nb(r, p)

</td>
<td>

$$p_{k} = \begin{pmatrix}
k - 1 \\
r - 1
\end{pmatrix}(1 - p)^{k - r}p^{r}$$

k = r, r + 1, ⋯

$$\left( \frac{pe^{it}}{1 - (1 - p)e^{it}} \right)^{r}$$

</td>
<td>

$$\frac{r}{p}$$

</td>
<td>

$$\frac{r(1 - p)}{p^{2}}$$

</td>
</tr>
<tr>
<td>

X1 + X2 + ⋯ + Xr ∼ Nb(r, p)，其中Xi ∼ Ge(p)

</td>
</tr>
<tr>
<td>

正态分布

N(μ, σ2)

</td>
<td>

$$p(x) = \frac{1}{\sqrt{2\pi}\sigma}\exp\left\{ - \frac{(x - \mu)^{2}}{2\sigma^{2}} \right\}$$

−∞ < x < +∞

$$\exp\left\{ i\mu t - \frac{\sigma^{2}t^{2}}{2} \right\}$$

$$N(0,1)\text{对应}\Phi(u) = \frac{1}{\sqrt{2\pi}}\int_{- \infty}^{u}{e^{- \frac{t^{2}}{2}}dt}$$

$$\varphi(u) = \frac{1}{\sqrt{2\pi}}e^{- \frac{u^{2}}{2}}$$

</td>
<td>

μ

</td>
<td>

σ

</td>
</tr>
<tr>
<td>

$$I = \int_{- \infty}^{+ \infty}{e^{- x^{2}}dx} = \sqrt{\pi},\ \ \int_{0}^{+ \infty}{e^{- x^{2}}dx} = \frac{\sqrt{\pi}}{2}$$

$$\text{证明：}I^{2} = \int_{- \infty}^{+ \infty}{\int_{- \infty}^{+ \infty}{e^{- \left( x^{2} + y^{2} \right)}dxdy}} = \int_{0}^{2\pi}{\int_{0}^{+ \infty}{e^{- r^{2}}rdrd\theta}} = \int_{0}^{2\pi}{\frac{1}{2}d\theta} = \pi$$

P(a < U < b) = Φ(b) − Φ(a),  P(|U| < c) = 2Φ(c) − 1

U = (X − μ)/σ ∼ N(0, 1)

$$P(a < X < b) = \Phi\left( \frac{b - \mu}{\sigma} \right) - \Phi\left( \frac{a - \mu}{\sigma} \right)$$

$$P\left( |X| < c \right) = \Phi\left( \frac{c - \mu}{\sigma} \right) + \Phi\left( \frac{c + \mu}{\sigma} \right)$$

$$\text{过程能力指数：}C_{p} = \frac{\text{上控制限} - \text{下控制限}}{6\sigma} \geq 1.33\text{表示生产过程正常}$$

Y = aX + b ∼ N(aμ + b, a2σ2)

X ∼ N(0, 1) ⇒ X2 ∼ χ2(1)

X ∼ N(μ1, σ12), Y ∼ N(μ2, σ22)，且X, Y独立 ⇒ X ± Y ∼ N(μ1 ± μ2, σ12 + σ22)

$$X_{i}\sim N\left( \mu_{i},\sigma_{i}^{2} \right)\text{且}X_{i}\text{相互独立} \Rightarrow \sum_{i}^{}{c_{i}X_{i}}\sim N\left( \sum_{i}^{}{c_{i}\mu_{i}},\sum_{i}^{}{c_{i}^{2}\sigma_{i}^{2}} \right)$$

$$X,Y\sim N\left( \mu,\sigma^{2} \right) \Rightarrow E\left( \max\left\{ X,Y \right\} \right) = \mu + \frac{\sigma}{\sqrt{\pi}},\ \ E\left( \min\left\{ X,Y \right\} \right) = \mu - \frac{\sigma}{\sqrt{\pi}}$$

</td>
</tr>
<tr>
<td>

二元正态分布

N(μ1, μ2, σ1, σ2, ρ)

</td>
<td>

$$p(x,y) = \frac{1}{2\pi\sigma_{1}\sigma_{2}\sqrt{1 - \rho^{2}}} \cdot$$

$$\exp\left\{ - \frac{\frac{\left( x - \mu_{1} \right)^{2}}{\sigma_{1}^{2}} - 2\rho\frac{\left( x - \mu_{1} \right)\left( y - \mu_{2} \right)}{\sigma_{1}\sigma_{2}} + \frac{\left( y - \mu_{2} \right)^{2}}{\sigma_{2}^{2}}}{2\left( 1 - \rho^{2} \right)} \right\}$$

</td>
<td>

(μ1, μ2)

</td>
<td>

(σ1, σ2)

</td>
</tr>
<tr>
<td></td>
<td>

aX + bY ∼ N(aμ1 + bμ2, a2σ12 + 2abσ1σ2ρ + b2σ22)

(aX + bY, cX + dY)是二维正态分布（$\left| \begin{matrix}
a & b \\
c & d
\end{matrix} \right| \neq 0$）

二维正态分布的相关系数就是ρ。

X, Y独立/无关⇔ ρ = 0。

多元正态变量经线性变换后仍是多元正态变量。

二维正态分布的边际分布和条件分布都是一维正态分布。

</td>
</tr>
<tr>
<td>

n元正态分布

</td>
<td>

p(x1, x2, ⋯, xn) = p(x)=

$$\frac{2}{(2\pi)^{\frac{n}{2}}\left| \mathbf{B} \right|^{\frac{1}{2}}}\exp\left\{ - \frac{\left( \mathbf{x} - \mathbf{a} \right)'\mathbf{B}^{- 1}\left( \mathbf{x} - \mathbf{a} \right)}{2} \right\}$$

</td>
<td>

a

</td>
<td>

B

</td>
</tr>
<tr>
<td>

均匀分布

（平顶分布）

U(a, b)

</td>
<td>

$$p(x) = \frac{1}{b - a},\ \ a < x < b$$

$$\frac{e^{ibt} - e^{iat}}{it(b - a)}$$

</td>
<td>

$$\frac{a + b}{2}$$

</td>
<td>

$$\frac{(b - a)^{12}}{12}$$

</td>
</tr>
<tr>
<td>

FX(X) ∼ U(0, 1)，其中FX(x)是严格单调增函数且反函数存在

</td>
</tr>
<tr>
<td>

多元均匀分布

</td>
<td>

$$p\left( x_{1},x_{2},\cdots,x_{n} \right) = \frac{1}{S_{D}}$$

(x1, x2, ⋯, xn) ∈ D

</td>
<td></td>
<td></td>
</tr>
<tr>
<td>

指数分布

Exp(λ)

</td>
<td>

p(x) = λe−λx,  x ≥ 0

$$\left( 1 - \frac{it}{\lambda} \right)^{- 1}$$

</td>
<td>

$$\frac{1}{\lambda}$$

</td>
<td>

$$\frac{1}{\lambda^{2}}$$

</td>
</tr>
<tr>
<td>

指数分布的无记忆性：设X ∼ Exp(λ)，∀m, n ∈ ℤ，有

P(X > m + n|X > m) = P(X > n)

</td>
</tr>
<tr>
<td>

伽马分布

Ga(α, λ)

</td>
<td>

$$p(x) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)}x^{\alpha - 1}e^{- \lambda x},\ \ x \geq 0$$

$$\left( 1 - \frac{it}{\lambda} \right)^{- \alpha}$$

</td>
<td>

$$\frac{\alpha}{\lambda}$$

</td>
<td>

$$\frac{\alpha}{\lambda^{2}}$$

</td>
</tr>
<tr>
<td>

伽马函数：Γ(α) = ∫0+∞xα − 1e−xdx

$$\Gamma(1) = 1,\ \ \ \Gamma\left( \frac{1}{2} \right) = \sqrt{\pi},\ \ \Gamma(\alpha + 1) = \alpha\Gamma(\alpha),\ \ \Gamma(n + 1) = n\Gamma(n) = n!$$

$$Ga(1,\lambda) = Exp(\lambda),\ \ Ga\left( \frac{n}{2},\frac{1}{2} \right) = \chi^{2}(n)$$

Ga(α, λ) ⇒ Y = kX ∼ Ga(α, λ/k)

伽马函数的可加性：X ∼ Ga(α1, λ), Y ∼ Ga(α2, λ) ⇒ X + Y ∼ Ga(α1 + α2, λ)

X1 + X2 + ⋯ + Xr ∼ Ga(r, λ)，其中Xi ∼ Exp(λ)

</td>
</tr>
<tr>
<td>

卡方分布

χ2(n)

</td>
<td>

$$p(x) = \frac{x^{\frac{n}{2} - 1}e^{- \frac{x}{2}}}{\Gamma\left( n\text{/}2 \right)2^{\frac{n}{2}}},\ \ x \geq 0$$

(1 − 2it)−n/2

</td>
<td>

n

</td>
<td>

2n

</td>
</tr>
<tr>
<td>

χ2 = x12 + x22 + ⋯ + xn2，其中xi是来自标准正态分布的独立样本

$$\chi\sim\chi^{2}(1) \rightarrow p(x) = \frac{x^{- \frac{1}{2}}e^{- \frac{x}{2}}}{\sqrt{2\pi}}$$

X1 + X2 + ⋯ + Xm ∼ χ2(n1 + n2 + ⋯ + nm)，其中Xi ∼ χ2(ni)

P(χ2 ≤ χ1 − α2(n)) = 1 − α

</td>
</tr>
<tr>
<td>

F分布

F(m, n)

</td>
<td>

$$p(x) = \frac{\Gamma\left( \frac{m + n}{2} \right)\left( \frac{m}{n} \right)^{\frac{m}{2}}}{\Gamma\left( \frac{m}{2} \right)\Gamma\left( \frac{n}{2} \right)}x^{\frac{m}{2} - 1}$$

</td>
<td>

$$\frac{n}{n - 2}$$

(n > 2)

</td>
<td>

$$\frac{2n^{2}(m + n - 2)}{m(n - 2)^{2}(n - 4)}$$

(n > 4)

</td>
</tr>
<tr>
<td>

$$F = \frac{(x_{1}^{2} + x_{2}^{2} + \cdots + x_{m}^{2})\text{/}m}{(y_{1}^{2} + y_{2}^{2} + \cdots + y_{n}^{2})\text{/}n}\text{，其中}x_{i},y_{j}\text{是来自标准正态分布的独立样本}$$

P(F ≤ F1 − α(m, n)) = 1 − α

$$F\sim F(m,n) \Rightarrow \frac{1}{F}\sim F(n,m)$$

Fα(n, m) ⋅ F1 − α(m, n) = 1

t ∼ t(n) ⇒ t2 ∼ F(1, n)

</td>
</tr>
<tr>
<td>

t分布

t(n)

</td>
<td>

$$p(x) = \frac{\Gamma\left( \frac{n + 1}{2} \right)}{\sqrt{n\pi}\Gamma\left( \frac{n}{2} \right)}\left( 1 + \frac{y^{2}}{n} \right)^{- \frac{n + 1}{2}}$$

</td>
<td>

0

(n > 1)

</td>
<td>

$$\frac{n}{n - 2}$$

(n > 2)

</td>
</tr>
<tr>
<td>

$$t = \frac{y_{1}}{\sqrt{\left( x_{1}^{2} + x_{2}^{2} + \cdots + x_{n}^{2} \right)\text{/}n}}\text{，其中}x_{i},y_{1}\text{是来自标准正态分布的独立样本}$$

概率密度函数是偶函数。

P(t ≤ t1 − α(n)) = 1 − α

tα(n) + t1 − α(n) = 0

t ∼ t(n) ⇒ t2 ∼ F(1, n)

n ≥ 30时，t分布的分位数可用标准正态分位数代替。

</td>
</tr>
<tr>
<td>

贝塔分布

Be(a, b)

</td>
<td>

$$p(x) = \frac{\Gamma(a + b)}{\Gamma(a)\Gamma(b)}x^{a - 1}(1 - x)^{b - 1},0 < x < 1$$

</td>
<td>

$$\frac{a}{a + b}$$

</td>
<td>

$$\frac{ab}{(a + b)^{2}(a + b + 1)}$$

</td>
</tr>
<tr>
<td>

贝塔函数：B(a, b) = ∫01xa − 1(1 − x)b − 1dx,  a, b > 0

$$B(a,b) = B(b,a),\ \ B(a,b) = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a + b)}$$

</td>
</tr>
<tr>
<td>

对数正态

分布

LN(μ, σ2)

</td>
<td>

$$p(x) = \frac{1}{\sqrt{2\pi}\sigma x}\exp\left\{ - \frac{\left( \ln x - \mu \right)^{2}}{2\sigma^{2}} \right\}$$

x ≥ 0

</td>
<td>

eμ + σ2/2

</td>
<td>

e2μ + σ2(eσ2 − 1)

</td>
</tr>
<tr>
<td>

柯西分布

Cau(μ, λ)

</td>
<td>

$$p(x) = \frac{1}{\pi}\frac{\lambda}{\lambda^{2} + (x - \mu)^{2}}$$

−∞ < x < +∞

</td>
<td>

不存在

</td>
<td>

不存在

</td>
</tr>
<tr>
<td>

韦布尔分布

</td>
<td>

$$p(x) = \frac{m}{\eta}\left( \frac{x}{\eta} \right)^{m}\exp\left\{ - \left( \frac{x}{\eta} \right)^{m} \right\}$$

x ≥ 0

</td>
<td>

$$\eta\Gamma\left( 1 + \frac{1}{m} \right)$$

</td>
<td>

$$\eta^{2}\left\lbrack \Gamma\left( 1 + \frac{2}{m} \right) - \Gamma^{2}\left( 1 + \frac{1}{m} \right) \right\rbrack$$

</td>
</tr>
</tbody>
</table>
</div>

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

一维随机变量

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Y = aX + b

</td>
<td>

$$p_{Y}(y) = p_{X}\left( \frac{y - b}{a} \right) \cdot \frac{1}{|a|}$$

</td>
</tr>
<tr>
<td>

二维随机变量

</td>
</tr>
<tr>
<td>

Z = X + Y

</td>
<td>

pZ(z) = ∫−∞+∞p(x, z − x)dx = ∫−∞+∞p(z − y, y)dy

</td>
</tr>
<tr>
<td>

Z = aX + bY

</td>
<td>

$$p_{Z}(z) = \frac{1}{|b|}\int_{- \infty}^{+ \infty}{p\left( x,\frac{z - ax}{b} \right)dx} = \frac{1}{|a|}\int_{- \infty}^{+ \infty}{p\left( \frac{z - by}{a},y \right)dy}$$

</td>
</tr>
<tr>
<td>

Z = XY

</td>
<td>

$$p_{Z}(z) = \int_{- \infty}^{+ \infty}{p\left( x,\frac{z}{x} \right)\frac{1}{|x|}dx} = \int_{- \infty}^{+ \infty}{p\left( \frac{z}{y},y \right)\frac{1}{|y|}dy}$$

</td>
</tr>
<tr>
<td>

Z = X/Y

</td>
<td>

pZ(z) = ∫−∞+∞p(zy, y)|y|dy

</td>
</tr>
<tr>
<td>

Z = X2 + Y2

</td>
<td>

$$p_{Z}(z) = \frac{1}{2}\int_{0}^{2\pi}{p\left( \sqrt{z}\cos\theta,\sqrt{z}\sin\theta \right)d\theta}$$

</td>
</tr>
<tr>
<td>

最大值分布：max {X1, X2, ⋯, Xn}，其中X1, X2⋯, Xn是相互独立的n个随机变量

</td>
</tr>
<tr>
<td>

Xi ∼ Fi(x)

</td>
<td>

$$F_{Y}(y) = P\left( X_{1} \leq y,X_{2} \leq y,\cdots,X_{n} \leq y \right) = \prod_{i = 1}^{n}{F_{i}(y)}$$

</td>
</tr>
<tr>
<td>

Xi ∼ F(x)

</td>
<td>

FY(y) = [F(y)]n,  pY(y) = n[F(y)]n − 1p(y)

</td>
</tr>
<tr>
<td>

最小值分布：min {X1, X2, ⋯, Xn}，其中X1, X2⋯, Xn是相互独立的n个随机变量

</td>
</tr>
<tr>
<td>

Xi ∼ Fi(x)

</td>
<td>

$$F_{Y}(y) = 1 - P\left( \min\left\{ X_{1} > y,X_{2} > y,\cdots,X_{n} > y \right\} \right) = 1 - \prod_{i = 1}^{n}\left\lbrack 1 - F_{i}(y) \right\rbrack$$

</td>
</tr>
<tr>
<td>

Xi ∼ F(x)

</td>
<td>

FY = 1 − [1 − F(y)]n,  pY(y) = n[1 − F(y)]n − 1p(y)

</td>
</tr>
</tbody>
</table>
</div>

## 分布特征数与性质

<div class="table-scroll">
<table>

<thead>
<tr>
<th></th>
<th>

离散定义

</th>
<th>

连续定义

</th>
<th>

样本定义

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

均值

</td>
<td>

$$E(X) = \mu = \sum_{i}^{}{x_{i}p\left( x_{i} \right)}$$

</td>
<td>

E(X) = μ = ∫−∞+∞xp(x)dx

</td>
<td>

$$\overline{x} = \frac{1}{n}\sum_{i = 1}^{n}x_{i}$$

</td>
</tr>
<tr>
<td>

$$\sum_{i}^{}{\left| x_{i} \right|p_{i}}\text{收敛}$$

∫−∞+∞|x|p(x)dx收敛

$$E\left\lbrack g(X) \right\rbrack = \left\{ \begin{array}{r}
\sum_{i}^{}{g\left( x_{i} \right)p\left( x_{i} \right)} \\
\int_{- \infty}^{+ \infty}{g(x)p(x)dx}
\end{array} \right.\ $$

E(aX + b) = aE(X) + b

E[f(X) + g(X)] = E[f(X)] + E[g(X)]

$$E\left( X^{*} \right) = 0,\ \ X^{*} = \left\lbrack X - E(X) \right\rbrack\text{/}\sqrt{Var(X)}$$

$$E\left( Z = g(X,Y) \right) = \left\{ \begin{array}{r}
\sum_{i}^{}{\sum_{j}^{}{g\left( x_{i},y_{i} \right)P\left( X = x_{i},Y = y_{i} \right)}} \\
\int_{- \infty}^{+ \infty}{\int_{- \infty}^{+ \infty}{g(x,y)p(x,y)dxdy}}\ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

E(X + Y) = E(X) + E(Y)

E(XY) = E(X)E(Y) + Cov(X, Y)

</td>
</tr>
<tr>
<td>

方差

</td>
<td>

Var(X) = D(X) = σ2

E(X − E(X))2

$$\sum_{i}^{}{\left( x_{i} - E(X) \right)^{2}p\left( x_{i} \right)}$$

</td>
<td>

Var(X) = D(X) = σ2

E(X − E(X))2

∫−∞+∞(x − E(X))2p(x)dx

</td>
<td>

$$s_{n}^{2} = \frac{1}{n}\sum_{i = 1}^{n}\left( x_{i} - \overline{x} \right)^{2}$$

$$s^{2} = \frac{1}{n - 1}\sum_{i = 1}^{n}\left( x_{i} - \overline{x} \right)^{2}$$

</td>
</tr>
<tr>
<td>

Var(aX + b) = a2E(X)

$$Var\left( X^{*} \right) = 1,\ \ X^{*} = \left\lbrack X - E(X) \right\rbrack\text{/}\sqrt{Var(X)}$$

Var(X ± Y) = Var(X) + Var(Y) ± 2Cov(X, Y)

$$\text{切比雪夫不等式：}P\left( \left| X - E(X) \right| \geq \varepsilon \right) \leq \frac{Var(X)}{\varepsilon^{2}},\ \ \forall\varepsilon > 0$$

</td>
</tr>
<tr>
<td>

协方差

Cov(X, Y)

</td>
<td>

Cov(X, Y) = E[(X − E(X))(Y − E(Y))]

</td>
<td></td>
</tr>
<tr>
<td>

Cov(X, Y) = E(XY) − E(X)E(Y)

Cov(aX + b, cX + d) = acCov(X, Y)

Cov(X + Y, Z + W)=

Cov(X, Z) + Cov(X, W) + Cov(Y, Z) + Cov(Z, W)

Cov(X*, Y*) = Corr(X, Y)

[Cov(X, Y)]2 ≤ σX2σY2

X, Y独立 ⇒ Cov(X, Y) = 0

</td>
<td></td>
</tr>
<tr>
<td>

相关系数

Corr(X, Y)

</td>
<td>

$$Corr(X,Y) = \frac{Cov(X,Y)}{\sqrt{Var(X)}\sqrt{Var(Y)}} = \frac{Cov(X,Y)}{\sigma_{X}\sigma_{Y}}$$

</td>
<td></td>
</tr>
<tr>
<td>

$$Corr(X,Y) = Cov\left( X^{*},Y^{*} \right) = E\left( \frac{X - \mu_{X}}{\sigma_{X}} \cdot \frac{Y - \mu_{Y}}{\sigma_{Y}} \right)$$

−1 ≤ Corr(X, Y) ≤ 1

</td>
<td></td>
</tr>
<tr>
<td>

众数

</td>
<td>

出现次数最多的数

</td>
</tr>
<tr>
<td>

下侧分位数

xp

上侧分位数

xp′

</td>
<td></td>
<td>

F(xp) = ∫−∞xpp(x)dx = p

1 − F(xp′) = ∫xp+∞p(x)dx = p

</td>
<td>

mp=

$$\left\{ \begin{array}{r}
x_{\left( \left\lfloor np + 1 \right\rfloor \right)},\ \ np\text{非整} \\
\frac{x_{(np)} + x_{(np + 1)}}{2}\ \ \ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

</td>
</tr>
<tr>
<td></td>
<td>

xp′ = x1 − p,  xp = x1 − p′

</td>
<td>

$$m_{p}\dot{\sim}$$

$$N\left( x_{p},\frac{p(1 - p)}{n\left\lbrack p\left( x_{p} \right) \right\rbrack^{2}} \right)$$

</td>
</tr>
<tr>
<td>

中位数

x0.5

</td>
<td></td>
<td>

∫−∞x0.5p(x)dx = ∫x0.5+∞p(x)dx

</td>
<td>

m0.5=

$$\left\{ \begin{array}{r}
x_{\left( \frac{n + 1}{2} \right)},\ \ n\text{为奇数} \\
\frac{x_{\left( \frac{n}{2} \right)} + x_{\left( \frac{n}{2} + 1 \right)}}{2}\ \ \ \ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

</td>
</tr>
<tr>
<td></td>
<td></td>
<td>

$$m_{0.5}\dot{\sim}$$

$$N\left( x_{0.5},\frac{1}{4n\left\lbrack p\left( x_{0.5} \right) \right\rbrack^{2}} \right)$$

</td>
</tr>
<tr>
<td>

k阶矩

k阶原点矩

k阶中心矩

</td>
<td>

Ak = μk = E(Xk)

Bk = νk = E(X − E(X))k

</td>
<td>

$$a_{k} = \frac{1}{n}\sum_{i = 1}^{n}x_{i}^{k}$$

$$b_{k} = \frac{1}{n}\sum_{i = 1}^{n}\left( x_{i} - \overline{x} \right)^{k}$$

</td>
</tr>
<tr>
<td>

$$\nu_{k} = \sum_{i = 0}^{n}{\begin{pmatrix}
k \\
i
\end{pmatrix}\mu_{i}\left( - \mu_{i} \right)^{k - i}}$$

$$\left\{ \begin{array}{r}
\nu_{1} = 0\ \ \ \ \ \ \ \ \ \ \ \  \\
\nu_{2} = \mu_{2} - \mu_{1}^{2}
\end{array} \right.\ $$

</td>
<td></td>
</tr>
<tr>
<td>

变异系数

Cv(X)

</td>
<td>

$$C_{v}(X) = \frac{\sqrt{Var(X)}}{E(X)} = \frac{\sigma(X)}{E(X)}$$

Cv(X)越大说明波动越大

</td>
<td></td>
</tr>
<tr>
<td>

偏度系数

βS

</td>
<td>

$$\beta_{S} = \frac{\nu_{3}}{\nu_{2}^{3\text{/}2}} = \frac{E\left( X - E(X) \right)^{3}}{\left\lbrack Var(X) \right\rbrack^{3\text{/}2}}$$

</td>
<td>

$${\widehat{\beta}}_{S} = \frac{b_{3}}{b_{2}^{3\text{/}2}}$$

</td>
</tr>
<tr>
<td>

峰度系数

βk

</td>
<td>

$$\beta_{k} = \frac{\nu_{4}}{\nu_{2}^{2}} - 3 = \frac{E\left( X - E(X) \right)^{3}}{\left\lbrack Var(X) \right\rbrack^{2}} - 3$$

</td>
<td>

$${\widehat{\beta}}_{k} = \frac{b_{4}}{b_{2}^{2}} - 3$$

</td>
</tr>
<tr>
<td>

条件期望

</td>
<td>

E(X|Y = y)=

$$\sum_{i}^{}{x_{i}P\left( X = x_{i}\text{|}Y = y \right)}$$

E(Y|X = x)=

$$\sum_{j}^{}{y_{i}P(Y = y_{j}\text{|}X = x)}$$

</td>
<td>

E(X|Y = y) = ∫−∞∞xp(x|y)dx

E(Y|X = x) = ∫−∞∞yp(y|x)dy

</td>
<td></td>
</tr>
<tr>
<td>

全期望公式

E(X) = E[E(X|Y)]

E(Y) = E[E(Y|X)]

</td>
<td></td>
</tr>
<tr>
<td>

条件方差

</td>
<td>

Var(X|Y = y)=

E[(X − E(X|Y = y))2|Y = y]

Var(Y|X = x)=

E[(Y − E(Y|X = x))2|X = x]

</td>
<td>

Var(X|Y = y)=

∫−∞+∞(X − E(X|Y = y))2fX|Y(x|y)dx

Var(Y|X = x)=

∫−∞+∞(Y − E(Y|X = x))2fY|X(y|x)dy

</td>
<td></td>
</tr>
<tr>
<td>

全方差公式

Var(X) = E[Var(X|Y)] + Var[E(X|Y)]

Var(Y) = E[Var(Y|X)] + Var[E(Y|X)]

</td>
<td></td>
</tr>
</tbody>
</table>
</div>

## 随机变量函数的分布

### 变量变换法

设二维随机变量$(X,Y)$的联合密度函数为$p(x,y)$，如果函数

$$\left\{ \begin{array}{r}
u = g_{1}(x,y) \\
v = g_{2}(x,y)
\end{array} \right.\ $$

有连续偏导数且存在唯一的反函数

$$\left\{ \begin{array}{r}
x = x(u,v) \\
y = y(u,v)
\end{array} \right.\ $$

使得其变换的雅可比行列式

$$J = \frac{\partial(x,y)}{\partial(u,v)} = \left| \begin{matrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{matrix} \right| = \left( \frac{\partial(u,v)}{\partial(x,y)} \right)^{- 1} = \left| \begin{matrix}
\frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\
\frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
\end{matrix} \right| \neq 0$$

若

$$\left\{ \begin{array}{r}
U = g_{1}(X,Y) \\
V = g_{2}(X,Y)
\end{array} \right.\ $$

则$(U,V)$的联合密度函数为

$$p(u,v) = p\left( x(u,v),y(u,v) \right)|J|$$

严格单调函数且反函数具有连续导数

$$p_{Y}(y) = \left\{ \begin{array}{r}
p_{X}\left\lbrack h(y) \right\rbrack\left| h'(y) \right|,\ \ \min\left\{ g( - \infty),g( + \infty) \right\} < y < \max\left\{ g( - \infty),g( + \infty) \right\} \\
0,\ \ \text{其他}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

## 大数定律与中心极限定律

### 伯努利大数定律

设$S_{n}$为

记

$$X_{i} = \left\{ \begin{array}{r}
1,\ \ \text{第}i\text{次试验中事件}A\text{发生}\ \ \ \ \  \\
0,\ \ \text{第}i\text{次试验中事件}A\text{不发生}
\end{array} \right.\ \ \ i = 1,2,\cdots,$$

### 大数定律的一般形式

设对随机变量序列$\left\{ X_{n} \right\}$，对$\forall\varepsilon > 0$，有

$$\lim_{n \rightarrow \infty}{P\left( \left| \frac{1}{n}\sum_{i = 1}^{n}X_{i} - \frac{1}{n}\sum_{i = 2}^{n}{E\left( X_{i} \right)} \right| < \varepsilon \right)} = 1$$

则称随机变量序列$\left\{ X_{n} \right\}$服从大数定律。

<div class="table-scroll">
<table style="width:83%;">

<thead>
<tr>
<th>

大数定律

</th>
<th>

条件

</th>
<th>

∀ε > 0，有结论

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

### 伯努利大数定律

（Bernoulli）

</td>
<td>

X ∼ b(n, p)

</td>
<td>

$$\lim_{n \rightarrow \infty}{P\left( \left| \frac{X}{n} - p \right| < \varepsilon \right)} = 1$$

</td>
</tr>
<tr>
<td>

切比雪夫大数定律

（Chebyshev）

</td>
<td>

{Xi}两两不相关

Var(Xi) ≤ c

</td>
<td>

通式

</td>
</tr>
<tr>
<td>

马尔可夫大数定律

（）

</td>
<td>

$$\frac{1}{n^{2}}Var\left( \sum_{i = 1}^{n}X_{i} \right) \rightarrow 0$$

（马尔可夫条件）

</td>
<td>

通式

</td>
</tr>
<tr>
<td>

辛钦大数定律

（Khinchin）

</td>
<td>

{Xi}独立同分布

E(Xi)存在

</td>
<td>

若E(Xi) = μ，则

$$\lim_{n \rightarrow \infty}{P\left( \left| \frac{1}{n}\sum_{i = 1}^{n}X_{i} - \mu \right| < \varepsilon \right)} = 1$$

</td>
</tr>
</tbody>
</table>
</div>

### 中心极限定理

<div class="table-scroll">
<table style="width:96%;">

<thead>
<tr>
<th>

### 中心极限定理

</th>
<th>

条件

</th>
<th>

结论

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

林德伯格—莱维

### 中心极限定理

（Lindeberg-Lévy）

</td>
<td>

{Xi}独立同分布

均值和方差存在

</td>
<td>

$$\lim_{n \rightarrow \infty}{P\left( \frac{\left( \sum_{i = 1}^{n}X_{i} - n\mu \right)}{\sigma\sqrt{n3}} \leq x \right)} = \Phi(x)$$

或

$$\frac{\left( \sum_{i = 1}^{n}X_{i} - n\mu \right)}{\sigma\sqrt{n}}\overset{L}{\rightarrow}N(0,1)$$

或

$$\sum_{i = 1}^{n}X_{i}\overset{L}{\rightarrow}N(\mu,\sigma)$$

</td>
</tr>
<tr>
<td>

棣莫弗—拉普拉斯

### 中心极限定理

（de Moivre-Laplace）

</td>
<td>

X ∼ b(n, p)

</td>
<td>

$$\lim_{n \rightarrow \infty}{P\left( \frac{X - np}{\sqrt{np(1 - p)}} \leq x \right)} = \Phi(x)$$

或

$$\frac{X - np}{\sqrt{np(1 - p)}}\overset{L}{\rightarrow}N(0,1)$$

或

$$X\dot{\sim}N\left( np,np(1 - p) \right)$$

</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

## 连续总体的抽样的次序统计量的分布

### 单个次序统计量的分布

设总体$X$的分布函数为$F(x)$，概率密度函数为$p(x)$，则次序统计量$x_{(i)}$的密度函数$p_{k}(x)$为

$$p_{k}(x) = \frac{n!}{(k - 1)!(n - k)!}\left\lbrack F(x) \right\rbrack^{k - 1}\left\lbrack 1 - F(x) \right\rbrack^{n - k}p(x)$$

取$k = 1$和$k = n$，得到最小次序量$x_{(1)}$（即$\min\left\{ x_{1},x_{2},\cdots,x_{n} \right\}$）和最大次序量$x_{(n)}$（即${max}\left\{ x_{1},x_{2},\cdots,x_{n} \right\}$）的概率密度函数

$$p_{1}(x) = n\left\lbrack 1 - F(x) \right\rbrack^{n - 1}p(x),\ \ p_{n}(x) = n\left\lbrack F(x) \right\rbrack^{n - 1}p(x)$$

再取$n = 2$，得到同分布下两随机变量$X,Y$的最小值和最大值的分布

$$p_{\min} = 2\left\lbrack 1 - F(x) \right\rbrack,\ \ p(x)p_{\max} = 2F(x)p(x)$$

### 多个个次序统计量的分布

次序统计量$\left( x_{(i)},x_{(j)} \right),i < j$的联合密度函数（$y \leq z$）

$$p(y,z) = \frac{n!}{(i - 1)!(j - i - 1)!(n - j)!}\left\lbrack F(y) \right\rbrack^{i - 1}\left\lbrack F(z) - F(y) \right\rbrack^{j - i - 1}\left\lbrack 1 - F(z) \right\rbrack^{n - j}p(y)p(z)$$

特别地，样本极差$R_{n} = x_{(n)} - x_{(1)}$的分布为

$$p_{R}(r) = n(n - 1)\int_{- \infty}^{+ \infty}{\left\lbrack F(u + r) - F(u) \right\rbrack^{n - 2}p(u)p(u + r)du}$$

设$x_{i}$是从随机变量$X\sim N(\mu,\sigma^{2})$中抽取的独立样本，

则$\overline{x}\sim N\left( \mu,\sigma^{2}\text{/}n \right)$，$\overline{x}$与$s^{2}$相互独立，且

$$\frac{\overline{x} - \mu}{\sigma\text{/}\sqrt{n}}\sim N(0,1)$$

$$\frac{1}{\sigma^{2}}\sum_{i = 1}^{n}\left( x_{i} - \mu \right)^{2}\sim\chi^{2}(n) \\ \frac{s_{x}^{2}\text{/}\sigma_{x}^{2}}{s_{y}^{2}\text{/}\sigma_{y}^{2}}\sim F(m - 1,n - 1)$$
$$\frac{\overline{x} - \mu}{s\text{/}\sqrt{n}}\sim t(n - 1)$$

$$\frac{1}{\sigma^{2}}(n - 1)s^{2}\sim\chi^{2}(n - 1) \\ \frac{1}{\sigma^{2}}ns_{n}^{2}\sim\chi^{2}(n - 1)$$

设$x_{i}$是从随机变量$X$中抽取的独立样本，则

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

$$\frac{\overline{x} - \mu}{\sigma\text{/}\sqrt{n}}\sim N(0,1)$$

</th>
<th>

$$\frac{1}{\sigma^{2}}\sum_{i = 1}^{n}\left( x_{i} - \mu \right)^{2}\sim\chi^{2}(n)$$

</th>
<th>

$$\frac{s_{x}^{2}\text{/}\sigma_{x}^{2}}{s_{y}^{2}\text{/}\sigma_{y}^{2}}\sim F(m - 1,n - 1)$$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$$\frac{\overline{x} - \mu}{s\text{/}\sqrt{n}}\sim t(n - 1)$$

</td>
<td>

$$\frac{1}{\sigma^{2}}(n - 1)s^{2}\sim\chi^{2}(n - 1)$$

</td>
<td>

$$\frac{1}{\sigma^{2}}ns_{n}^{2}\sim\chi^{2}(n - 1)$$

</td>
</tr>
</tbody>
</table>
</div>

## 点估计的评价标准

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

$$E\left( \overline{x} \right) = \mu$$

</th>
<th>

E(s2) = σ2

</th>
<th>

$$E\left( s_{n}^{2} \right) = \frac{n - 1}{n}\sigma^{2}$$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$$Var\left( \overline{x} \right) = \frac{\sigma^{2}}{n}$$

</td>
<td>

$$Var\left( s^{2} \right) = \frac{2\sigma^{4}}{n - 1}$$

（正态整体）

</td>
<td>

$$Var\left( s_{n}^{2} \right) = \frac{2(n - 1)}{n^{2}}\sigma^{4}$$

（正态整体）

</td>
</tr>
</tbody>
</table>
</div>

### 常见点估计的诸性质

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

无偏性

</th>
<th>

Eθ(θ̂) = θ

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

渐近无偏性

</td>
<td>

$$E_{\theta}\left( \widehat{\theta} \right)\overset{P}{\rightarrow}\theta$$

</td>
</tr>
<tr>
<td>

有效性（无偏估计）

</td>
<td>

Var(θ̂1) ≤ Var(θ̂2)

</td>
</tr>
<tr>
<td>

一致性/相合性

</td>
<td>

$${\widehat{\theta}}_{n}\overset{P}{\rightarrow}\theta$$

</td>
</tr>
<tr>
<td>

均方误差

</td>
<td>

MSE(θ̂) = E(θ̂ − θ) = Var(θ̂) + [E(θ̂) − θ]2

</td>
</tr>
<tr>
<td>

一致最小方差无偏估计

UMVUE（无偏估计）

</td>
<td>

Var(θ̂) ≤ Var(θ̃)

</td>
</tr>
</tbody>
</table>
</div>

## 假设检验的定义与原则

<div class="table-scroll">
<table style="width:96%;">

<thead>
<tr>
<th>

样本

</th>
<th>

θ̂

</th>
<th>

θ

</th>
<th>

无偏性

</th>
<th>

极大似然估计

</th>
<th>

一致性

</th>
<th>

均方误差最小

</th>
<th>

UMVUE

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

一般总体

</td>
<td>

$$\overline{x}$$

</td>
<td>

μ

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

一般总体

</td>
<td>

s2

</td>
<td>

σ2

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

一般总体

</td>
<td>

sn2

</td>
<td>

σ2

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

一般总体

</td>
<td>

μ̂MLE

</td>
<td>

μ

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

一般总体

</td>
<td>

$${\widehat{\sigma^{2}}}_{MLE}$$

</td>
<td>

σ2

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

正态分布

</td>
<td>

$$\overline{x}$$

</td>
<td>

μ

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

正态分布

</td>
<td>

s2

</td>
<td>

σ2

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

正态分布

</td>
<td>

sn2

</td>
<td>

σ2

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

正态分布

</td>
<td>

μ̂MLE

</td>
<td>

μ

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

正态分布

</td>
<td>

$${\widehat{\sigma^{2}}}_{MLE}$$

</td>
<td>

σ2

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

指数分布

</td>
<td>

$$\overline{x}$$

</td>
<td>

μ

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

指数分布

</td>
<td>

s2

</td>
<td>

σ2

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

指数分布

</td>
<td>

sn2

</td>
<td>

σ2

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

均匀分布

</td>
<td>

$$\overline{x}$$

</td>
<td>

μ

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

均匀分布

</td>
<td>

s2

</td>
<td>

σ2

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

均匀分布

</td>
<td>

sn2

</td>
<td>

σ2

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

均匀分布

</td>
<td>

μ̂MLE

</td>
<td>

μ

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

均匀分布

</td>
<td>

$${\widehat{\sigma^{2}}}_{MLE}$$

</td>
<td>

σ2

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

均匀分布

(0, b)

</td>
<td>

b̂MLE

</td>
<td>

b

</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

显著性水平为$\alpha$的显著性检验：检验满足$\forall\theta \in \Theta_{0}$，有

$$P_{\theta}\left( \mathbf{x} \in W \right) \leq \alpha$$

选择原假设和备择假设的依据：

1.  想否定的假设作为原假设$H_{0}$。

2.  有把握的，有经验的判断作为原假设$H_{0}$。

3.  后果严重的错误作为第一类错误（拒真错误）。

4.  保守的倾向作为原假设$H_{0}$。

<div class="table-scroll">
<table>

<thead>
<tr>
<th></th>
<th>

H0为真（原假设）

θ ∈ Θ0

</th>
<th>

H1为真（备择假设）

θ ∈ Θ1 = Θ − Θ0

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

x ∈ W（拒绝域）

</td>
<td>

犯第一类错误

（拒真错误）

犯错概率为α

</td>
<td>

正确

</td>
</tr>
<tr>
<td>

$\mathbf{x} \in \overline{W}$（接受域）

</td>
<td>

正确

</td>
<td>

犯第二类错误

（取伪错误）

犯错概率为β

</td>
</tr>
</tbody>
</table>
</div>

## 区间估计和参数检验

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

实例

</th>
<th>

H0

（必须包含等号）

</th>
<th>

倾向

</th>
<th>

第一类错误（拒真错误）（不希望犯）

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

生产产品检验

</td>
<td>

满足产家宣称的要求或标准

</td>
<td>

希望达标

</td>
<td>

达标了但认为没达标

</td>
</tr>
<tr>
<td>

新药疗效是否优于旧药

</td>
<td>

新药不优于旧药（≤）

</td>
<td>

希望新药劣于旧药

</td>
<td>

新药劣于旧药但认为新药优于旧药

</td>
</tr>
<tr>
<td>

“刷题”能否提分

</td>
<td>

不能

</td>
<td>

希望“刷题”不能

</td>
<td>

刷题不能提分但被认为能

</td>
</tr>
<tr>
<td>

性别和是否吸烟是否有关联

</td>
<td>

无关

</td>
<td>

希望证明无关

</td>
<td>

无关但被认为有关

</td>
</tr>
</tbody>
</table>
</div>
