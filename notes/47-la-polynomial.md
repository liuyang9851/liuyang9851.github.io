---
title: 多项式
description: 多项式的加法、数乘与乘积、次数的性质、整除与因式、相伴多项式、带余除法的唯一性，以及矩阵运算性质的汇总表。
---

# 多项式

[[toc]]

多项式

多项式

对于多项式

f(x) = anxn + an − 1xn − 1 + ⋯ + a1x + a0

g(x) = bmxm + bm − 1xm − 1 + ⋯ + b1x + b0

其中m ≠ n，补全相差的项使g(x)类同于f(x)，定义

加法：f(x) + g(x) = (an + bn)xn + (an − 1 + bn − 1)xn − 1 + ⋯ + (a1 + b1)x + (a0 + b0)

数乘：cf(x) = canxn + can − 1xn − 1 + ⋯ + ca1x + ca0

此时多项式可构成线性空间。

乘积：h(x) = f(x) ⋅ g(x) = f(x)g(x) = cn + mxn + m + cn + m − 1xn + m − 1 + ⋯ + c1x + c0

其中

$$c_{k} = \sum_{i + j = k}^{}{a_{i}b_{j}} = a_{0}b_{k} + a_{1}b_{k - 1} + \cdots + a_{k - 1}b_{1} + a_{k}b_{0}$$

定义f(x)的次数为deg f(x)，即deg f(x) = n，则有

(1)deg (f(x)g(x)) = deg f(x) + deg g(x)

(2)deg (cf(x)) = deg f(x)

(3)deg (f(x) + g(x)) ≤ max {deg f(x)，deg g(x)}（最高次项正负抵消）

整除：对于f(x)和g(x)，若存在h(x)，满足

f(x) = g(x)h(x)

则称g(x)为f(x)的因式，g(x)可以整除f(x)，f(x)可以被g(x)整除，记作

g(x) | f(x)

否则，记作

g(x) ∤ f(x)

整除的性质

(4)若f(x) |  g(x)，则 cf(x) | g(x)，因此非零常数多项式c是任一非零多项式的因式。

证：设g(x) = f(x)p(x)，则g(x) = (cf(x))(c−1p(x))，所以cf(x) | g(x)

(5)f(x) | f(x)

(6)（传递性）若f(x) |  g(x)，g(x) | h(x)，则f(x) |  h(x)

证：设g(x) = f(x)p(x)，h(x) = g(x)q(x)，则

h(x) = (f(x)p(x))q(x) = f(x)(p(x)q(x))

(7)（线性组合）若f(x) |  g(x)，f(x) | h(x)，则对于任意的多项式u(x)，v(x)，有

f(x) |  g(x)u(x) + h(x)v(x)

证：设g(x) = f(x)p(x)，h(x) = g(x)q(x)，则

g(x)u(x) + h(x)v(x) = f(x)(p(x)u(x) + q(x)v(x))

(8)设f(x) |  g(x)，g(x) | f(x)且f(x)，g(x)都是非零多项式，则存在非零元c，使

f(x) = cg(x)

称f(x)，g(x)为相伴多项式，记为f(x) ∼ g(x)

证：设g(x) = f(x)p(x)，f(x) = g(x)q(x)，则

f(x) = f(x)(p(x)q(x))

所以

deg f(x) = deg f(x) + deg (p(x)q(x))

所以

deg (p(x)q(x)) = 0

所以

deg p(x) = deg q(x) = 0

因此p(x)和q(x)均为非零常数多项式，即f(x)和g(x)相差一个非零常数。

(9)（多项式带余除法唯一性）设g(x) ≠ 0，则一定存在唯一的q(x)，r(x)，使得

f(x) = g(x)q(x) + r(x)

且deg r(x) < deg g(x)

证：若deg f(x) < deg g(x)，只需令q(x) = 0，r(x) = f(x)即可。

<div class="table-scroll">
<table>

<thead>
<tr>
<th></th>
<th>

(AB)′ = B′A′

转置

</th>
<th>

(AB)k

k次幂

</th>
<th>

(AB)* = B*A*

伴随矩阵

</th>
<th>

(AB)−1 = B−1A−1

逆矩阵

</th>
<th>

|AB| = |A||B|

行列式

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

(AB)′ = B′A′

转置

</td>
<td>

A″ = A

</td>
<td>

(A′)k = (Ak)′

</td>
<td>

(A′)* = (A*)′

</td>
<td>

(A′)−1 = (A−1)′

</td>
<td>

|A′| = |A|

</td>
</tr>
<tr>
<td>

(AB)k

k次幂

</td>
<td>

(Ak)′ = (A′)k

</td>
<td>

(Ak)t = Akt

</td>
<td>

(Ak)* = (A*)k

</td>
<td>

(Ak)−1 = (A−1)k

</td>
<td>

|Ak| = |A|k

</td>
</tr>
<tr>
<td>

(AB)* = B*A*

伴随矩阵

</td>
<td>

(A*)′ = (A′)*

</td>
<td>

(A*)k = (Ak)*

</td>
<td>

AA* = A*A=|A|E

(A*)* = |A|n − 2A

</td>
<td>

A* = |A|A−1

(A*)−1 = (A−1)*

$$= \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}$$

</td>
<td>

|A*| = |A|n − 1

</td>
</tr>
<tr>
<td>

(AB)−1 = B−1A−1

逆矩阵

</td>
<td>

(A−1)′ = (A′)−1

</td>
<td>

(A−1)k = (Ak)−1

</td>
<td>

$$\mathbf{A}^{- 1} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{\mathbf{*}}$$

(A−1)* = (A*)−1

$$= \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}$$

</td>
<td>

(A−1)−1 = A

</td>
<td>

|A−1| = |A|−1

</td>
</tr>
<tr>
<td>

|AB| = |A||B|

行列式

</td>
<td>

|A| = |A′|

</td>
<td>

|A|k = |Ak|

</td>
<td>

|A|n − 1 = |A*|

</td>
<td>

|A|−1 = |A−1|

</td>
<td>

|AB| = |BA|

</td>
</tr>
</tbody>
</table>
</div>
