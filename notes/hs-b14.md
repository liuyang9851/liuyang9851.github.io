---
title: "其它"
hs_seq: "B14"
description: "其它：求方程的近似解，首先要确定根的大致范围，称为根的隔离，确定根所在的大致区间（隔离区间）后，运用以下方法提高根的精确度。"
---

# 其它

进制

琴生不等式

> 若$f(x)$是区间$\lbrack a,b\rbrack$上的下凸函数，则对任意的$x \in \lbrack a\text{，}b\rbrack$，在权$a$下有:

$\frac{1}{n}\sum_{i = 1}^{n}{f\left( a_{i}x_{i} \right)} \geq f\left( \frac{a_{i}}{n}\sum_{i = 1}^{n}x_{i} \right)\left( \text{当}x_{1} = x_{2} = \ldots x_{n}\text{时，等号成立} \right)$

Hadamard不等式

若$f(x)$是$\lbrack a\text{，}b\rbrack$上的可导函数，则

$\left\{ \begin{array}{r} f\left( \frac{a + b}{2} \right) \leq \frac{1}{b - a}\int_{a}^{b}{f(x)dx} \leq \frac{f(a) + f(b)}{2}\text{，}f^{''}(x) > 0 \\ f\left( \frac{a + b}{2} \right) \geq \frac{1}{b - a}\int_{a}^{b}{f(x)dx} \geq \frac{f(a) + f(b)}{2}\text{，}f^{''}(x) < 0 \end{array} \right.\$

切比雪夫（总和）不等式

伯努利不等式

对于任意$x \geq - 1$，有

$\left\{ \begin{array}{r} (1 + x)^{n} \geq 1 + nx\text{，}n \geq 1\ \ \ \ \ \ \ \  \\ (1 + x)^{n} < 1 + nx\text{，}0 < n < 1 \end{array} \right.\$

下面给出$n \geq 1$情况的证明

由均值不等式，得

$1 + nx = (1 + nx) \cdot \underset{n - 1\text{个}1}{\overset{1 \cdot 1 \cdot \cdots \cdot 1}{︸}} \leq \left( \frac{1 + nx + \overset{n - 1\text{个}1}{\overbrace{1 + 1 + \cdots + 1}}}{n} \right)^{n} = \left( \frac{nx + n}{n} \right)^{n} = (x + 1)^{n}$

n次方差公式

$a^{n} - b^{n} = (a - b)\sum_{i = 1}^{n}\left( a^{n - i}b^{i - 1} \right) = (a - b)\left( a^{n - 1} + a^{n - 2}b + \ldots + ab^{n - 2} + b^{n - 1} \right)$

n次方和公式

$a^{n} + b^{n} = (a + b)\sum_{i = 1}^{n}{( - 1)^{i + 1}\left( a^{n - i}b^{i - 1} \right)(n\text{是奇数})}$

求方程的近似解

求方程的近似解，首先要确定根的大致范围，称为根的隔离，确定根所在的大致区间（隔离区间）$\lbrack a\text{，}b\rbrack$后，运用以下方法提高根的精确度。

在下述三种方法中要求$f(x)$连续，$f(a) \cdot f(b) < 0$，且方程$f(x) = 0$在$(a\text{，}b)$内仅有一个实根$\xi$。对于切线法和割线法还要求$f'(x)$和$f^{''}(x)$在$\lbrack a\text{，}b\rbrack$保持定号。

手算开平方

![](/images/hs/hs-b14/img01.png)

$\text{原理：}(10a + b)^{2} = 100a^{2} + (20a + b) \times b$

鞋带公式

对于任意多边形，若其顶点坐标以逆时针方向数分别为$\left( x_{1}\text{，}y_{1} \right)\left( x_{2}\text{，}y_{2} \right)\cdots\left( x_{n}\text{，}y_{n} \right)$，则该多边形的面积为

$S = \frac{1}{2}\left( \sum_{i = 1}^{n - 1}\left( x_{i}y_{i + 1} - y_{i}x_{i + 1} \right) + x_{n}y_{1} - y_{n}x_{1} \right) = \frac{1}{2}\left( \sum_{i = 1}^{n - 1}\left| \begin{matrix} x_{i} & x_{i + 1} \\ y_{i} & y_{i + 1} \end{matrix} \right| + \left| \begin{matrix} x_{n} & x_{1} \\ y_{n} & y_{1} \end{matrix} \right| \right)$

考虑如下数表

$\begin{matrix} y_{1} & y_{2} & y_{3} & \cdots & y_{n} & y_{1} \\ x_{1} & x_{2} & x_{3} & \cdots & x_{n} & x_{1} \end{matrix}$

$S = \frac{1}{2}\left\lbrack \left( x_{1}y_{2} + x_{2}y_{3} + \cdots + x_{n}y_{1} \right) - \left( y_{1}x_{2} + y_{2}x_{3} + \cdots + y_{n}x_{1} \right) \right\rbrack$

皮克公式

在正方形格点网上若有一简单凸多边形，其各个顶点都在格点上，那么该多边形的面积为

$S = a + \frac{b}{2} - 1$

其中a表示多边形内部格点的点数，b表示多边形边界上的点数。（教室内全价，窗户边半价，老师不收）

四面体体积公式

设四面体的四点分别为A、B、C、D，则四面体的面积为

$V = \pm \frac{1}{6}\left| \begin{matrix} x_{2} - x_{1} & x_{3} - x_{1} & x_{4} - x_{1} \\ y_{2} - y_{1} & y_{3} - y_{1} & y_{4} - y_{1} \\ z_{2} - z_{1} & z_{3} - z_{1} & z_{4} - z_{1} \end{matrix} \right| = \pm \frac{1}{6}\left| \begin{array}{r} \overrightarrow{AB} \\ \overrightarrow{AC} \\ \overrightarrow{AD} \end{array} \right| = \frac{1}{6}\left| \begin{matrix} x_{1} & x_{2} & x_{3} & x_{4} \\ y_{1} & y_{2} & y_{3} & y_{4} \\ z_{1} & z_{2} & z_{3} & z_{4} \\ 1 & 1 & 1 & 1 \end{matrix} \right|$

$f(n) = \log_{n}(n + 1)$

${f(n + 1) - f(n) = \log_{n + 1}(n + 2) - \log_{n}(n + 1) }{= 1 + \log_{n + 1}\frac{n + 2}{n + 1} - \left( 1 + \log_{n}\frac{n + 1}{n} \right) }{= \log_{n + 1}\frac{n + 2}{n + 1} - \log_{n}\frac{n + 1}{n} }{< \log_{n}\frac{n + 2}{n + 1} - \log_{n}\frac{n + 1}{n} }{< \log_{n}\frac{n + 1}{n} - \log_{n}\frac{n + 1}{n} }{= 0}$

故$\log_{2}3 > \log_{3}4 > \cdots > \log_{n}(n + 1)$

符号函数

$sgn(x) = \left\{ \begin{array}{r} - 1\text{，}x < 0 \\ 0\text{，}\ \ \ x = 0 \\ 1\text{，}\ \ \ x > 0 \end{array} \right.\$

由此得到

$x = sgn(x) \cdot |x|$

$sgn\left( x^{n} \right) = sgn^{n}(x)$

$\frac{d|x|}{dx} = sgn(x)\ (x \neq 0)$

多项式定理与广义二项式定理

多项式定理

${\left( x_{1} + x_{2} + \cdots + x_{m} \right)^{n} = \sum_{n_{i} \geq 0,n_{1} + n_{2} + \cdots + n_{m} = n}^{}{\frac{n!}{n_{1}!n_{2}!\cdots n_{3}!}\prod_{1 < i < m}^{}x_{i}^{n_{i}}} }{= \sum_{n_{i} \geq 0,n_{1} + n_{2} + \cdots + n_{m} = n}^{}{\frac{n!}{n_{1}!n_{2}!\cdots n_{3}!}x_{1}^{n_{1}}x_{2}^{n_{2}}}\cdots x_{n}^{n_{m}}}$

$\text{展开式一共有}C_{n + m - 1}^{m - 1}\text{项。}$

广义二项式定理

$(x + y)^{\alpha} = \sum_{k = 0}^{\infty}{\left( \begin{array}{r} \alpha \\ k \end{array} \right)x^{\alpha - k}y^{k}}$

$\text{其中}\left( \begin{array}{r} \alpha \\ k \end{array} \right) = \frac{\alpha(\alpha - 1)\cdots(\alpha - k + 1)}{k!} = \frac{(\alpha)_{k}}{k!}$

$\text{特别地，}\left( \begin{array}{r} \alpha \\ 0 \end{array} \right) = 1$

$eg.\sqrt{2} = (1 + 1)^{0.5} = \frac{1}{0!}1^{0.5 - 0}1^{0} + \frac{0.5}{1!}1^{0.5 - 1}1^{1} + \frac{0.5 \cdot ( - 0.5)}{2!}1^{0.5 - 2}1^{2} + \cdots = 1 + \frac{0.5}{1} - \frac{0.5 \cdot 0.5}{2} + \cdots$

二分法

描述1

$1.\text{取}\lbrack a\text{，}b\rbrack \text{的中点}\xi_{1} = \frac{a + b}{2}\text{，计算}f\left( \xi_{1} \right)$

> 1.若$f\left( \xi_{1} \right) = 0$，则$\xi = \xi_{1}$
>
> 2.若$f\left( \xi_{1} \right)$与$f(a)$同号，则取$a_{1} = \xi_{1}\text{，}b_{1} = b$
>
> 3.否则$f\left( \xi_{1} \right)$与$f(b)$同号，取$a_{1} = a\text{，}b_{1} = \xi_{1}$
>
> $\text{这样能得到}a_{1} < \xi < b_{1}\text{，且}\ b_{1} - a_{1} = \frac{1}{2}(b - a)$

$2.\text{取}\left\lbrack a_{1}\text{，}b_{1} \right\rbrack \text{的中点}\xi_{2} = \frac{a_{1} + b_{2}}{2}\text{，计算}f\left( \xi_{2} \right)\text{，重复上述操作。}$

$\text{若取}a_{n}\text{或}b_{n}\text{为}\xi \text{的近似值，则误差小于}\frac{1}{2^{n}}(b - a)$

描述2

$1.\text{确定区间}\lbrack a\text{，}b\rbrack \text{，验证}f(a) \cdot f(b) < 0$

$2.\text{求区间}(a\text{，}b)\text{的中点}c$

$3.\text{计算}f(c)$

$(1)\ \text{若}f(c) = 0\text{，则}c\text{就是函数的零点；}$

$(2)\ \text{若}f(a) \cdot f(c) < 0\text{，则令}b = c;$

$(3)\ \text{若}f(c) \cdot f(b) < 0\text{，则令}a = c.$

$(4)\ \text{判断是否达到精确度：即若}|a - b| < \text{精确度，则得到零点近似值}a(\text{或}b)\text{，否则重复}2 - 4$

切线法（牛顿逼近法）

令$x_{0} = a$或$x_{0} = b$得到点$\left( x_{0}\text{，}f\left( x_{0} \right) \right)$处的切线方程

$y - f\left( x_{0} \right) = f'\left( x_{0} \right)(x - x_{0})$

令$y = 0$，得到

$x_{1} = x_{0} - \frac{f\left( x_{0} \right)}{f'\left( x_{0} \right)}$

再在$\left( x_{1}\text{，}f\left( x_{1} \right) \right)$处做切线，重复上述操作，得到根的近似值。

$x_{n + 1} = x_{n} - \frac{f\left( x_{n} \right)}{f'\left( x_{n} \right)}$

割线法（弦截法）

用$\frac{f\left( x_{n} \right) - f\left( x_{n - 1} \right)}{x_{n} - x_{n - 1}}$代替$f'(x)$，得

$x_{n + 1} = x_{n} - \frac{x_{n} - x_{n - 1}}{f\left( x_{n} \right) - f\left( x_{n - 1} \right)} \cdot f\left( x_{n} \right)$

插值

利用已知成对数据预测其它数据的方法。

线性插值

即待求数两侧数据的平均值

多项式插值

类似于待定系数法，设出多项式函数

$f(x) = a + bx + cx^{2} + dx^{3} + \cdots$

代入已知数据，解出由系数组成的一次方程组。

牛顿插值法

用于解决求解线性方程组计算大的问题，随着已知数据的增多，估计会越来越精准。

$f(x) = f\left( x_{0} \right)$

$+ f\left\lbrack x_{0}\text{，}x_{1} \right\rbrack\left( x - x_{0} \right)$

$+ f\left\lbrack x_{0}\text{，}x_{1}\text{，}x_{2} \right\rbrack\left( x - x_{0} \right)\left( x - x_{1} \right) + \cdots$

$+ f\left\lbrack x_{0}\text{，}x_{1}\cdots \text{，}x_{n} \right\rbrack\left( x - x_{0} \right)\left( x - x_{1} \right)\left( x - x_{n} \right)$

其中

$f\left\lbrack x_{i}\text{，}x_{j} \right\rbrack = \frac{f\left( x_{i} \right) - f\left( x_{j} \right)}{x_{i} - x_{j}}$

$f\left\lbrack x_{i}\text{，}x_{j}\text{，}x_{k} \right\rbrack = \frac{f\left\lbrack x_{i}\text{，}x_{j} \right\rbrack - f\left\lbrack x_{j}\text{，}x_{k} \right\rbrack}{x_{i} - x_{k}}$

$f\left\lbrack x_{i}\text{，}x_{j}\text{，}x_{k}\text{，}x_{l} \right\rbrack = \frac{f\left\lbrack x_{i}\text{，}x_{j}\text{，}x_{k} \right\rbrack - f\left\lbrack x_{j}\text{，}x_{k}\text{，}x_{l} \right\rbrack}{x_{i} - x_{l}}$

以此类推

拉格朗日插值

帕德逼近

$2 \cdot \frac{x - 1}{x + 1} < \frac{3\left( x^{2} - 1 \right)}{x^{2} + 4x + 1} < \ln x\ \ (x > 1)$

$\ln x < \frac{3\left( x^{2} - 1 \right)}{x^{2} + 4x + 1} < 2 \cdot \frac{x - 1}{x + 1} < x - 1\ \ (0 < x < 1)$

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$f(x) = e^{x}$

</th>
<th>

$0$

</th>
<th>

$1$

</th>
<th>

$2$

</th>
<th>

$f(x) = \ln x$

</th>
<th>

0

</th>
<th>

$1$

</th>
<th>

$2$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$0$

</td>
<td>

$1$

先小后大

</td>
<td>

$x + 1$

恒大于

</td>
<td>

$1 + x + \frac{1}{2}x^{2}$

先小后大

</td>
<td>

$0$

</td>
<td rowspan="3"></td>
<td>

$x - 1$

恒小于

</td>
<td>

$\frac{- x^{2} + 4x - 3}{2}$

先小后大

</td>
</tr>
<tr>
<td>

$1$

</td>
<td>

$\frac{1}{1 - x}$

先小后大

</td>
<td>

$\frac{2 + x}{2 - x}$

先小后大

</td>
<td>

$\frac{x^{2} + 4x + 6}{- 2x + 6}$

恒小于

</td>
<td>

$1$

</td>
<td>

$\frac{2x - 2}{x + 1}$

先大后小

</td>
<td>

$\frac{x^{2} + 4x - 5}{4x + 2}$

恒小于

</td>
</tr>
<tr>
<td>

$2$

</td>
<td>

$\frac{2}{x^{2} - 2x + 2}$

先大后小

</td>
<td>

$\frac{2x + 6}{x^{2} - 4x + 6}$

恒大于

</td>
<td>

$\frac{x^{2} + 6x + 12}{x^{2} - 6x + 12}$

先小后大

</td>
<td>

$2$

</td>
<td>

$\frac{12x - 12}{- x^{2} + 8x + 5}$

恒小于

</td>
<td>

$\frac{3x^{2} - 3}{6x^{2} - 11x + 11}$

先小后大

</td>
</tr>
</tbody>
</table>
</div>

洛朗级数

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$e^{x} \leq - \frac{x^{2} + 4x + 6}{2(x - 3)}(x < 3)$

</th>
<th>

$e^{x} \geq \frac{2 - x}{2 + x}(x \leq 0)$

</th>
<th>

$\sin x \geq \frac{60x - 7x^{3}}{60 + 3x^{2}}(x \geq 0)$

</th>
<th>

$\cos x \leq 1 + \frac{3x^{4} - 60x^{2}}{4x^{2} + 120}$

</th>
</tr>
</thead>
<tbody>

</tbody>
</table>
</div>
