---
title: "数列"
hs_seq: "A8"
description: "数列：应用上述两式可实现与的相互转化。"
---

# 数列

数列的相关概念

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

名称

</th>
<th>

定义

</th>
<th>

符号

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

数列

</td>
<td>

按照一定次序排列的一列数

</td>
<td>

$\left\{ a_{n} \right\}$

</td>
</tr>
<tr>
<td>

项

</td>
<td>

数列中的每个项分别被称为第$1$项、第$2$项、……

</td>
<td>

$a_{n}$

</td>
</tr>
<tr>
<td>

项数

</td>
<td>

组成数列的数的个数

</td>
<td>

$n$

</td>
</tr>
<tr>
<td>

有穷数列与无穷数列

</td>
<td>

项数有限的数列称为有穷数列，项数无限的数列称为无穷数列

</td>
<td></td>
</tr>
<tr>
<td>

首项与末项

</td>
<td>

数列的第一项称为首项，有穷数列的最后一项称为末项

</td>
<td>

$a_{1}$和$a_{n}$

</td>
</tr>
<tr>
<td>

递增数列

</td>
<td>

从第$2$项起，每一项都大于它的前一项的数列

</td>
<td></td>
</tr>
<tr>
<td>

递减数列

</td>
<td>

从第$2$项起，每一项都小于它的前一项的数列

</td>
<td></td>
</tr>
<tr>
<td>

常（数）数列

</td>
<td>

各项都相等的数列

</td>
<td></td>
</tr>
<tr>
<td>

摆动（摇摆）数列

</td>
<td>

从第2项起，有些项大于它的前一项，有些项小于它的前一项的数列

</td>
<td></td>
</tr>
<tr>
<td>

周期数列

</td>
<td>

各项呈周期性变化的数列

</td>
<td></td>
</tr>
</tbody>
</table>
</div>

等差数列与等比数列

基本公式

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

等差数列

</th>
<th>

等比数列

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

递推

</td>
<td>

$a_{n} = a_{n - 1} + d\ \ (n \geq 2)$

</td>
<td>

$a_{n} = qa_{n - 1}\ \ (n \geq 2)$

</td>
</tr>
<tr>
<td>

通项

</td>
<td>

$a_{n} = a_{1} + (n - 1)d$

</td>
<td>

$a_{n} = a_{1} \cdot q^{n - 1}$

</td>
</tr>
<tr>
<td>

中项

</td>
<td>

$a_{n} = \frac{1}{2}\left( a_{n + 1} + a_{n - 1} \right)\ \ (n \geq 2)$

</td>
<td>

$a_{n} = \sqrt{a_{n + 1}a_{n - 1}}\ \ (n \geq 2)$

</td>
</tr>
<tr>
<td rowspan="3">

求和

</td>
<td>

$S_{n} = \frac{n\left( a_{1} + a_{n} \right)}{2}$

</td>
<td>

$S_{n} = \frac{a_{1} - qa_{n}}{1 - q}$

</td>
</tr>
<tr>
<td>

$S_{n} = na_{1} + \frac{n(n - 1)}{2}d$

</td>
<td>

$S_{n} = \frac{a_{1}\left( 1 - q^{n} \right)}{1 - q} = \frac{a_{1}(a^{n} - 1)}{q - 1}$

</td>
</tr>
<tr>
<td>

$S_{n} = \frac{d}{2}n^{2} + \left( a_{1} - \frac{d}{2} \right)n$

</td>
<td>

$a_{n} = \frac{a_{1}}{1 - q} - \frac{a_{1}}{1 - q}q^{n}$

</td>
</tr>
</tbody>
</table>
</div>

导出公式

等差数列

其它公式结论

$\text{等差中项：}a_{n} = \frac{a_{n - x} + a_{n + x}}{2}$

$\text{等差中项的推广：}a_{n} = \frac{\sum_{i = 1}^{x}a_{n - i} + \sum_{j = 1}^{x}a_{n + j}}{2x}$

$a_{x} + a_{y} = 2a_{\frac{x + y}{2}}$

$\text{公差：}d = \frac{a_{m} - a_{n}}{m - n}$

$\text{已知}a_{x} = a_{y}(x \neq y)\text{，则}d = 0$

$\text{已知}a_{x} = y\text{，}a_{y} = x\text{，则}\ d = - 1\text{且}a_{1} = x + y - 1\text{，}a_{x + y} = 0$

> $\text{证：}d = \frac{a_{y} - a_{x}}{y - x} = \frac{x - y}{y - x} = - 1\text{，}a_{1} = a_{x} - (x - 1)d = x + y - 1\text{，}a_{x + y} = a_{x} + yd = 0$

$\text{已知}S_{x} = S_{y}(x > y)\text{，则}a_{\frac{x + y + 1}{2}} = 0\text{，}S_{x + y} = 0$

> $\text{证：}S_{x} - S_{y} = a_{y + 1} + a_{y + 2} + \ldots + a_{x} = ka_{\frac{x + y + 1}{2}} = 0 \Rightarrow a_{\frac{x + y + 1}{2}} = 0$
>
> $\text{因为}a_{n} = \frac{S_{2n - 1}}{2n - 1}\text{，所以}a_{\frac{x + y + 1}{2}} = \frac{S_{x + y}}{x + y} = 0 \Rightarrow S_{x + y} = 0$

$\text{已知}S_{x} = y\text{，}S_{y} = x\text{，则}a_{\frac{x + y + 1}{2}} = - 1\text{，}S_{x + y} = - (x + y)$

> $\text{证：设}S_{x} = Ax^{2} + Bx = y\text{，}S_{y} = Ay^{2} + By = x\text{，两式相减，得}$
>
> $A\left( x^{2} - y^{2} \right) + B(x - y) = y - x \Rightarrow A(x + y) + B = - 1$
>
> $\therefore S_{x + y} = A(x + y)^{2} + B(x + y) = (x + y)\left\lbrack A(x + y) + B \right\rbrack = - (x + y)$
>
> $S_{x + y} = (x + y)a_{\frac{x + y + 1}{2}} = - (x + y) \Rightarrow a_{\frac{x + y + 1}{2}} = - 1$

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

命题

</th>
<th>

$a_{x} = a_{y}(x \neq y)$

</th>
<th>

$a_{x} = y\text{，}a_{y} = x$

</th>
<th>

$S_{x} = S_{y}(x \neq y)$

</th>
<th>

$S_{x} = y\text{，}S_{y} = x$

</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">

结论

</td>
<td rowspan="2">

$d = 0$

</td>
<td>

$d = - 1$

</td>
<td>

$a_{\frac{x + y + 1}{2}} = 0$

</td>
<td>

$a_{\frac{x + y + 1}{2}} = - 1$

</td>
</tr>
<tr>
<td>

$a_{x + y} = 0$

</td>
<td>

$S_{x + y} = 0$

</td>
<td>

$S_{x + y} = - (x + y)$

</td>
</tr>
</tbody>
</table>
</div>

通项公式推导和推论

$\text{由该式可知}S_{n}\text{是关于}n\text{的不含常数项的二次式，其中二次项系数为公差的一半。}$

$S_{n} = na_{1} + \frac{n(n - 1)}{2}d = n\left( a_{1} + \frac{n - 1}{2}d \right) = na_{1 + \frac{n - 1}{2}} = na_{\frac{n + 1}{2}}$

$S_{n} = na_{\frac{n + 1}{2}}$

$\text{把上式中}\frac{n + 1}{2}\text{换成}n\text{可得}$

$S_{2n - 1} = (2n - 1)a_{n}\text{，}a_{n} = \frac{S_{2n - 1}}{2n - 1}$

应用上述两式可实现$a_{n}$与$S_{n}$的相互转化。

$\text{将}S_{n} = na_{\frac{n + 1}{2}}\text{两边同除}n\text{，得}$

$\frac{S_{n}}{n} = a_{\frac{n + 1}{2}} = a_{1} + (n - 1)\frac{d}{2}$

$\text{故}\left\{ \frac{S_{n}}{n} \right\} \text{是以}a_{1}\text{为首项，以}\frac{d}{2}\text{为公差的等差数列。}$

由上式得

$\frac{S_{x}}{x} - \frac{S_{y}}{y} = (x - y)\frac{d}{2}$

设$S_{n} = An^{2} + Bn + C$

当$C = 0\text{时，}\left\{ a_{n} \right\} \text{是以}A + B\text{为首项，公差为}2A\text{的等差数列}$

$\text{当}C \neq 0\text{时，}a_{n} = S_{n} - S_{n - 1} = 2An + B - A = A + B + 2A(n - 1)$

$\left\{ a_{n} \right\} \text{不是等差数列，}\left\{ a_{n + 1} \right\} \text{是以}A + B\text{为首项，公差为}2A\text{的等差数列}$

奇偶项问题

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

n

</th>
<th>

奇数项数

</th>
<th>

偶数项数

</th>
<th>

$a_{\text{中}}$

</th>
<th>

$a_{\text{奇中}}$

</th>
<th>

$a_{\text{偶中}}$

</th>
<th>

$S_{\text{全}}$

</th>
<th>

$S_{\text{奇}}$

</th>
<th>

$S_{\text{偶}}$

</th>
<th>

$S_{\text{奇}} - S_{\text{偶}}$

</th>
<th>

$\frac{S_{\text{奇}}}{S_{\text{偶}}}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

奇数

</td>
<td>

$\frac{n + 1}{2}$

</td>
<td>

$\frac{n - 1}{2}$

</td>
<td>

$a_{\frac{n + 1}{2}}$

</td>
<td>

$a_{\frac{n + 1}{2}}$

</td>
<td>

$a_{\frac{n + 1}{2}}$

</td>
<td>

$na_{\frac{n + 1}{2}}$

</td>
<td>

$\frac{n + 1}{2}a_{\frac{n + 1}{2}}$

</td>
<td>

$\frac{n - 1}{2}a_{\frac{n + 1}{2}}$

</td>
<td>

$a_{\frac{n + 1}{2}}$

</td>
<td>

$\frac{n + 1}{n - 1}$

</td>
</tr>
<tr>
<td>

偶数

</td>
<td>

$\frac{n}{2}$

</td>
<td>

$\frac{n}{2}$

</td>
<td>

$a_{\frac{n + 1}{2}}$

</td>
<td>

$a_{\frac{n}{2}}$

</td>
<td>

$a_{\frac{n}{2} + 1}$

</td>
<td>

$na_{\frac{n + 1}{2}}$

</td>
<td>

$\frac{n}{2}a_{\frac{n + 1}{2}}$

</td>
<td>

$\frac{n}{2}a_{\frac{n + 1}{2}}$

</td>
<td>

$- \frac{n}{2}d$

</td>
<td>

$\frac{a_{\frac{n}{2}}}{a_{\frac{n}{2}} + d}$

</td>
</tr>
</tbody>
</table>
</div>

等比数列

$\text{通项公式：}a_{n} = a_{1} \cdot q^{x} = a_{1 + x}$

$\text{递推公式：}\frac{a_{n + 1}}{a_{n}} = q$

$\text{前}n\text{项和公式：}S_{n} = \frac{a_{1} - qa_{n}}{1 - q} = \frac{a_{1}\left( 1 - q^{n} \right)}{1 - q} = \frac{a_{1}}{1 - q} - \frac{a_{1}}{1 - q}q^{n}$

常用裂项相消

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

原式

</th>
<th>

裂项

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\frac{b - a}{ab}$

</td>
<td>

$\frac{1}{a} - \frac{1}{b}$

</td>
</tr>
<tr>
<td>

$\frac{1}{x(x + k)}$

</td>
<td>

$\frac{1}{k}\left( \frac{1}{x} - \frac{1}{x + k} \right)$

</td>
</tr>
<tr>
<td>

$\frac{1}{(ax + b)(ax + c)}$

</td>
<td>

$\frac{1}{c - b}\left( \frac{1}{ax + b} - \frac{1}{ax + c} \right)$

</td>
</tr>
<tr>
<td>

$\frac{1}{\sqrt{ax + k} + \sqrt{ax}}$

</td>
<td>

$\frac{1}{k}\left( \sqrt{ax + k} - \sqrt{ax} \right)$

</td>
</tr>
<tr>
<td>

$\frac{1}{(x - k)x(x + k)}$

</td>
<td>

$\frac{1}{2k^{2}}\left\lbrack \left( \frac{1}{x - k} - \frac{1}{x} \right) - \left( \frac{1}{x} - \frac{1}{x + k} \right) \right\rbrack$

</td>
</tr>
<tr>
<td>

$\frac{q^{n}}{\left( q^{n} + k \right)\left( q^{n + 1} + k \right)}$

</td>
<td>

$\frac{1}{q - 1}\left( \frac{1}{q^{n} + k} - \frac{1}{q^{n + 1} + k} \right)$

</td>
</tr>
<tr>
<td>

$\frac{(a - 1)(dn + c) + ad}{(dn + c)(dn + c + d)a^{n}}$

</td>
<td>

$\frac{1}{(dn + c)a^{n - 1}} - \frac{1}{(dn + c + d)a^{n}}$

</td>
</tr>
<tr>
<td>

$x$

</td>
<td>

$\frac{x(x + 1)}{2} - \frac{(x - 1)x}{2}$

</td>
</tr>
<tr>
<td>

$x^{2}$

</td>
<td>

$\frac{x(x + 1)(2x + 1)}{6} - \frac{(x - 1)x(2x - 1)}{6}$

</td>
</tr>
<tr>
<td>

$x^{3}$

</td>
<td>

$\left( \frac{x(x + 1)}{2} \right)^{2} - \left( \frac{(x - 1)x}{2} \right)^{2}$

</td>
</tr>
<tr>
<td>

$m^{x}$

</td>
<td>

$\frac{m^{x + 1}}{m - 1} - \frac{m^{x}}{m - 1}$

</td>
</tr>
<tr>
<td>

$\frac{n + 1}{n(n - 1) \cdot 2^{n}}$

</td>
<td>

$\frac{1}{(n - 1) \cdot 2^{n - 1}} - \frac{1}{n \cdot 2^{n}}$

</td>
</tr>
<tr>
<td>

$\frac{1}{k^{2^{n}} - 1}$

</td>
<td>

$\frac{1}{2}\left( \frac{1}{k^{2^{n - 1}}} - \frac{1}{k^{2^{n - 1}}} \right)$

</td>
</tr>
<tr>
<td>

$\frac{1}{(n + 1)(n + 2)\cdots(n + k)}$

</td>
<td>

$\frac{1}{k - 1} \cdot \left( \frac{1}{(n + 1)(n + 2)\cdots(n + k - 1)} - \frac{1}{(n + 2)(n + 3)\cdots(n + k)} \right)$

</td>
</tr>
<tr>
<td>

$\tan(n - 1)\tan(n + 1)$

</td>
<td>

$\frac{1}{\tan 2}\left( \tan(n + 1) - \tan(n - 1) \right) - 1$

</td>
</tr>
<tr>
<td>

$\sin(nx)$

</td>
<td>

$\frac{1}{2\sin x}\left\{ \cos\left\lbrack (n - 1)x \right\rbrack - \cos\left\lbrack (n + 1)x \right\rbrack \right\}$

</td>
</tr>
</tbody>
</table>
</div>

差比数列求和公式

差比数列

$a_{n} = (an + b)q^{n - 1}$

的求和公式为

$S_{n} = (An + B)q^{n} - B$

$\text{其中}A = \frac{a}{q - 1}\text{，}B = \frac{b - A}{q - 1}$

证明可以使用错位相减法，答题时也使用这种方法。

已知递推求通项

线性递推数列求数列通项

1阶线性递推数列

$a_{n + 1} = pa_{n} + q$

发现

$a_{n + 1} + \frac{q}{p - 1} = p\left( a_{n} + \frac{q}{p - 1} \right)$

故

$a_{n} = \left( a_{1} + \frac{q}{p - 1} \right)p^{n - 1} - \frac{q}{p - 1}$

$\text{当}a_{n} = \frac{q}{p - 1}\text{时，发现}\frac{q}{p - 1} = p\frac{q}{p - 1} + q\text{，因此称}\frac{q}{p - 1}\text{是方程}x = px + q\text{的特征根，}a_{n} = \frac{q}{p - 1}\text{是数列}$

的一个不动点

2阶线性递推数列

$a_{n + 1} = pa_{n} + qa_{n - 1} + r$

令

$a_{n + 1} + xa_{n} + y = z\left( a_{n} + xa_{n - 1} + y \right)$

可得到

$a_{n + 1} + xa_{n} + y = \left( a_{2} + xa_{1} + y \right)z^{n - 1}$

特殊形式

$a_{n + 1} = \frac{An + B}{Cn + D}$

考虑特征方程

$x = \frac{Ax + B}{Cx + D}$

设其根为$x_{1}\text{，}x_{2}$

$1.x_{1} \neq x_{2}\mathbb{\in R}\text{，}\frac{a_{n} - x_{1}}{a_{n} - x_{2}}\text{是首项为}\frac{a_{1} - x_{1}}{a_{1} - x_{2}}\text{，公比为}\frac{A - Cx_{1}}{A - Cx_{2}}\text{的等比数列}$

$2.x_{1} = x_{2}\mathbb{\in R}\text{，}\frac{1}{a_{n} - x_{1}}\text{是首项为}\frac{1}{a_{1} - x_{1}}\text{，公差为}\frac{C}{A - Cx_{1}}\text{等比数列}$

$3.x_{1} \neq x_{2}\mathbb{\in C|R}\text{，}a_{n}\text{是周期数列}$

不动点

当递推公式中仅存在$a_{n + 1}$和$a_{n}$时，把他们替换为未知数$x$，求得的解称为该数列的不动点，在递推公式两边加上/减去不动点并做适当整理，能得到类似等差数列或等比数列的形式。

eg考虑递推公式

$a_{n + 1} = pa_{n} + q$

若令

$x = px + q$

$\text{解得}x = - \frac{q}{p - 1}\text{，在递推公式两端同减} - \frac{q}{p - 1}\text{，即得}$

$a_{n + 1} + \frac{q}{p - 1} = pa_{n} + q + \frac{q}{p - 1} = p\left( a_{n} + \frac{q}{p - 1} \right)$

周期数列与反周期数列

$a_{n} = a_{n + T}$

> $a_{n + 1} = - \frac{1}{1 + a_{n}}\text{，}T = 3$
>
> $a_{n + 1} = 1 - \frac{1}{a_{n}}\text{，}T = 3$
>
> $a_{n + 2} = a_{n + 1} - a_{n}\text{，}T = - 3$
>
> $a_{n + 1} = \frac{1 + a_{n}}{1 - a_{n}}\ /\ a_{n + 1} = \frac{1 - a_{n}}{1 + a_{n}}\text{，}T = 4$
>
> $a_{n + 1} = m - a_{n}\text{，}T = 2$
>
> $a_{n + 1} = m - a_{n} - a_{n - 1}\text{，}T = 3$

求和

累加法，累乘法，裂项相消法，加减消元法

多阶等差数列

斐波那契数列的通项公式

若数列$\left\{ a_{n} \right\}$满足

$a_{n} = a_{n - 1} + a_{n - 2}\text{，}a_{1} = a_{2} = 1$

则

$a_{n} = \frac{1}{\sqrt{5}}\left\lbrack \left( \frac{1 + \sqrt{5}}{2} \right)^{n} - \left( \frac{1 - \sqrt{5}}{2} \right)^{n} \right\rbrack$
