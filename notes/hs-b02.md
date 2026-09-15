---
title: "不等式"
hs_seq: "B2"
description: "不等式：证明：因为，当且仅当时等号成立，所以"
---

# 不等式

不等式的基本性质

> 基本事实：$a > b \Leftrightarrow a - b > 0\text{，}a = 0 \Leftrightarrow a - b = 0\text{，}a < b \Leftrightarrow a - b < 0$
>
> 对称性：$a > b \Leftrightarrow b < a\text{，}a < b \Leftrightarrow b > a$
>
> 传递性：$a > b\text{，}b > c \Rightarrow a > c\ \ \ \ \ \ \ \ \ \ a < b\text{，}b < c \Rightarrow a < c$
>
> 可加性：$a + b > c \Leftrightarrow a + c > b + c$
>
> 移项法则：$a + b > c \Leftrightarrow a > c - b$
>
> 可乘性：$a > b\text{，}c > 0 \Rightarrow ac > bc\ \ \ \ \ \ \ \ \ \ a > b\text{，}c < 0 \Rightarrow ac < bd$
>
> 同向可加性：$a > b\text{，}c > d \Rightarrow a + c > b + d$
>
> 同向同正可乘性：$a > b > 0\text{，}c > d > 0 \Rightarrow ac > bd$
>
> 正可乘方性：$a > b > 0 \Rightarrow a^{n} > b^{n}\ \ \left( n\mathbb{\in N}\text{，}n \geq 2 \right)$
>
> 正可开方性：$a > b > 0 \Rightarrow \sqrt[n]{a} > \sqrt[n]{b}\ \ \left( n\mathbb{\in N}\text{，}n \geq 2 \right)$

重要不等式

$(a + b)^{2} \geq 2ab\ \ \left( a\text{，}b\mathbb{\in R} \right)$

证明：因为$a^{2} + b^{2} - 2ab = (a - b)^{2} \geq 0$，当且仅当$a = b$时等号成立，所以

$(a + b)^{2} \geq 2ab$

当且仅当$a = b$时，等号成立。

![](/images/hs/hs-b02/img01.png)

基本不等式

$\sqrt{ab} \leq \frac{a + b}{2}\ \ \left( a\text{，}b \in \mathbb{R}_{+} \right)$

当且仅当$a = b$时，等号成立。

两个正数的算术平均数不小于它们的几何平均数。

证明：因为$a + b = \left( \sqrt{a} \right)^{2} + \left( \sqrt{b} \right)^{2} \geq 2\sqrt{a} \cdot \sqrt{b} = 2\sqrt{ab}$，所以

$\sqrt{ab} \leq \frac{a + b}{2}$

当且仅当$\sqrt{a} = \sqrt{b}$，即$a = b$时，等号成立。

三个正数的算数——几何平均不等式

如果$a\text{，}b\text{，}c \in \mathbb{R}_{+}$，那么

$\frac{a + b + c}{3} \geq \sqrt[3]{abc}$

当且仅当$a = b = c$时，等号成立。

三个正数的算术平均数不小于它们的几何平均数。

证明：因为

> $a^{3} + b^{3} + c^{3} - 3abc$

$= (a + b)^{3} - 3a^{2}b - 3ab^{2} + c^{3} - 3abc$

$= (a + b)^{3} + c^{3} - 3a^{2}b - 3ab^{2} - 3abc$

$= (a + b + c)\left\lbrack (a + b)^{2} - (a + b)c + c^{2} \right\rbrack - 3ab(a + b + c)$（前两项使用立方和公式）

$= (a + b + c)\left( a^{2} + 2ab + b^{2} - ac - bc + c^{2} - 3ab \right)$

$= (a + b + c)\left( a^{2} + b^{2} + c^{2} - ab - bc - ca \right)$

$= \frac{1}{2}(a + b + c)\left\lbrack (a - b)^{2} + (b - c)^{2} + (c - a)^{2} \right\rbrack \geq 0\text{，得证}$

均值不等式的一般形式

$n\left( \sum_{i = 1}^{n}\frac{1}{a_{i}} \right)^{- 1} \leq \sqrt[n]{\prod_{i = 1}^{n}a_{i}} \leq \frac{1}{n}\sum_{i = 1}^{n}a_{i} \leq \sqrt{\frac{1}{n}\sum_{i = 1}^{n}a_{i}^{2}}\ \ \left( a_{i} \in \mathbb{R}_{+}\text{，}n \in \mathbb{N}_{+} \right)\ \ \left( H_{n} \leq G_{n} \leq A_{n} \leq Q_{n} \right)$

调和均值$\left( H_{n} \right) \leq$几何均值$\left( G_{n} \right) \leq$算术均值$\leq \left( A_{n} \right)$平方均值$\left( Q_{n} \right)$，在$a_{1} = a_{2} = \cdots = a_{n}$取等号

证明：数学归纳法

几何均值$\leq$算术均值

下面给出不用数学归纳法的证明

$\text{由}A_{n} = \frac{a_{1} + a_{2} + \cdots + a_{n}}{n}\text{，}G_{n} = a_{1} \cdot a_{2} \cdot \cdots \cdot a_{n}\text{则}$

$e^{\frac{a_{1}}{n} - 1} \geq \frac{a_{1}}{A} > 0\text{，}e^{\frac{a_{2}}{n} - 1} \geq \frac{a_{2}}{A} > 0\text{，}\cdots \text{，}e^{\frac{a_{n}}{n} - 1} \geq \frac{a_{n}}{A} > 0$

各不等式相乘，得

$e^{\frac{a_{1} + a_{2} + \cdots + a_{n}}{A} - n} \geq \frac{a_{1} \cdot a_{2} \cdot \cdots \cdot a_{n}}{A_{n}}$

$\text{由}A_{n} = \frac{a_{1} + a_{2} + \cdots + a_{n}}{n}\text{，得}$

$e^{n - n} \geq \frac{a_{1} \cdot a_{2} \cdot \cdots \cdot a_{n}}{A^{n}}\text{，即}A_{n} \geq a_{1} \cdot a_{2} \cdot \cdots \cdot a_{n} = G_{n}$

$\text{对}G_{n} \leq A_{n}\text{，用}\frac{1}{x_{i}}\text{替换}x_{i}\text{，稍作整理，就得到}H_{n} \leq G_{n}\text{。}$

对于$A_{n} \leq Q_{n}$，要用到柯西不等式。

$A_{n} = \frac{1}{n^{2}}\left( a_{1}^{2} + a_{2}^{2} + \cdots + a_{n}^{2} \right)(\underset{n\text{个}1}{\overset{1 + 1 + \cdots + 1}{︸}}) \geq \frac{1}{n}\left( a_{1} \cdot 1 + a_{2} \cdot 1 + \cdots + a_{n} \cdot 1 \right) = G_{n}$

绝对值三角不等式

对于$a\text{，}b\mathbb{\in R}$，有

$\left| |a| - |b| \right| \leq |a + b| \leq |a| + |b|$

当且仅当$ab \geq 0$时，等号成立。

$\left| |a| - |b| \right| \leq |a - b| \leq |a| + |b|$

当且仅当$ab \leq 0$时，等号成立。

证明：当$ab \geq 0$时，$ab = |ab|$，所以

$|a + b| = \sqrt{(a + b)^{2}} = \sqrt{a^{2} + 2ab + b^{2}} = \sqrt{|a|^{2} + 2|ab| + |b|^{2}} = \sqrt{\left( |a| + |b| \right)^{2}} = |a| + |b|$

当$ab < 0$时，$ab = - |ab|$，所以

$|a + b| = \sqrt{a^{2} + 2ab + b^{2}} = \sqrt{|a|^{2} - 2|ab| + |b|^{2}} < \sqrt{|a|^{2} + 2|ab| + |b|^{2}} = \sqrt{\left( |a| + |b| \right)^{2}} = |a| + |b|$

二维形式的柯西不等式

$\left( a^{2} + b^{2} \right)\left( c^{2} + d^{2} \right) \geq (ac + bd)^{2}$

当且仅当$ad = bc$时取等号。

证明：$\left( a^{2} + b^{2} \right)\left( c^{2} + d^{2} \right) = a^{2}c^{2} + b^{2}d^{2} + a^{2}d^{2} + b^{2}c^{2} = (ac + bd)^{2} + (ad - bc)^{2} \geq (ac + bd)^{2}$

柯西不等式的一般形式

设$a_{1}\text{，}a_{2}\text{，}a_{3}\text{，}\cdots \text{，}a_{n}\text{，}b_{1}\text{，}b_{2}\text{，}b_{3}\text{，}\cdots \text{，}b_{n}$是实数，则

$\sum_{i = 1}^{n}a_{i}^{2}\sum_{i = 1}^{n}b_{i}^{2} \geq \left( \sum_{i = 1}^{n}{a_{i}b_{i}} \right)^{2}\left( \text{当}\frac{a_{1}}{b_{1}} = \frac{a_{2}}{b_{2}} = \cdots = \frac{a_{n}}{b_{n}}\text{时，等号成立} \right)$

当且仅当$b_{i} = 0\ \ (i = 1\text{，}2\text{，}\cdots \text{，}n)$或$a_{i}x + b_{i} = 0\ \ (i = 1\text{，}2\text{，}\cdots \text{，}n)$时，等号成立。

其用内积的形式可写为（向量形式）：

$\left\lbrack \mathbf{a}\text{，}\mathbf{b} \right\rbrack^{2} \leq \left\lbrack \mathbf{a}\text{，}\mathbf{a} \right\rbrack\left\lbrack \mathbf{b}\text{，}\mathbf{b} \right\rbrack$

证明：当$a_{1} = a_{2} = \cdots = a_{n}$或$b_{1} = b_{2} = \cdots = b_{n}$时，显然成立。

设$a_{1}\text{，}a_{2}\text{，}\cdots \text{，}a_{n}$中至少有一个不为0，则

$a_{1}^{2} + a_{2}^{2} + \cdots + a_{n}^{2} > 0$

考虑二次函数

$f(x) = \left( a_{1}^{2} + a_{2}^{2} + \cdots + a_{n}^{2} \right)x^{2} + 2\left( a_{1}b_{1} + a_{2}b_{2} + \cdots + a_{n}b_{n} \right) + (b_{1}^{2} + b_{2}^{2} + \cdots + b_{n}^{2})$

因为对于任意实数$x$，

$f(x) = \left( ax_{1} + b_{1} \right)^{2} + \left( ax_{2} + b_{n} \right)^{2} + \cdots + \left( ax_{n} + b_{n} \right)^{2} \geq 0$

所以二次函数$f(x)$的判别式$\Delta \leq 0$，即

$4\left( a_{1}b_{1} + a_{2}b_{2} + \cdots + a_{n}b_{n} \right)^{2} - 4\left( a_{1}^{2} + a_{2}^{2} + \cdots + a_{n}^{2} \right)\left( b_{1}^{2} + b_{1}^{2} + \cdots + b_{n}^{2} \right) \leq 0$

于是

$\left( a_{1}^{2} + a_{2}^{2} + \cdots + a_{n}^{2} \right)\left( b_{1}^{2} + b_{1}^{2} + \cdots + b_{n}^{2} \right) \geq \left( a_{1}b_{1} + a_{2}b_{2} + \cdots + a_{n}b_{n} \right)^{2}$

当且仅当$f(x)$有唯一零点时，判别式$\Delta = 0$，以上不等式取等号。此时，有唯一实数$x$，使

$a_{i}x + b_{i} = 0\ \ (i = 1\text{，}2\text{，}\cdots \text{，}n)$

若$x = 0$，则$b_{1} = b_{2} = \cdots = b_{n} = 0$，不等式成立；若$x \neq 0$，则有$x_{i} = - \frac{1}{x}b_{i}$。总之，当且仅当$b_{i} = 0\ \ (i = 1\text{，}2\text{，}\cdots \text{，}n)$或$a_{i}x + b_{i} = 0\ \ (i = 1\text{，}2\text{，}\cdots \text{，}n)$时，等号成立。

三角不等式

设$\mathbf{a} = \left( a_{1}\text{，}a_{2}\text{，}\cdots \text{，}a_{n} \right)\text{，}\mathbf{b} = \left( b_{1}\text{，}b_{2}\text{，}\cdots \text{，}b_{n} \right)\mathbb{\in R}$，则

$\left| \left| \mathbf{a} \right| - \left| \mathbf{b} \right| \right| \leq \left| \mathbf{a} \pm \mathbf{b} \right| \leq \left| \mathbf{a} \right| + \left| \mathbf{b} \right|$

写成代数形式也就是

$\left| \sqrt{a_{1}^{2} + a_{2}^{2} + \cdots + a_{n}^{2}} - \sqrt{b_{1}^{2} + b_{2}^{2} + \cdots + b_{n}^{2}} \right| \leq \left| \sqrt{\left( a_{1} \pm b_{1} \right)^{2} + \left( a_{2} \pm b_{2} \right)^{2} + \cdots + \left( a_{n} \pm b_{n} \right)^{2}} \right| \leq \sqrt{a_{1}^{2} + a_{2}^{2} + \cdots + a_{n}^{2}} + \sqrt{b_{1}^{2} + b_{2}^{2} + \cdots + b_{n}^{2}}$

三角不等式与柯西不等式等价。

将不等式的每一部分都平方，由柯西不等式可证。

由上述两种形式可以看出，绝对值三角不等式是三角不等式的一位正数情况，同时也能看出实数不等式与向量不等式的某种联系，因此可以尝试把常见不等式中的实数换为向量。

权方和不等式的一般形式

$\sum_{i = 1}^{n}\frac{a_{i}^{m + 1}}{b_{i}^{m}} \geq \frac{\left( \sum_{i = 1}^{n}a_{i} \right)^{m + 1}}{\left( \sum_{i = 1}^{n}b_{i} \right)^{m}}\left( \text{当}\frac{a_{1}}{b_{1}} = \frac{a_{2}}{b_{2}} = \cdots = \frac{a_{n}}{b_{n}}\text{时，等号成立} \right)$

权方和不等式是柯西不等式的推论。

排序不等式

设$a_{1} \leq a_{2} \leq \cdots \leq a_{n}\text{，}b_{1} \leq b_{2} \leq \cdots \leq b_{n}$为两组实数，$c_{1}\text{，}c_{2}\text{，}\cdots \text{，}c_{n}$是$b_{1}\text{，}b_{2}\text{，}\cdots \text{，}b_{n}$的任一序列，则

$a_{1}b_{n} + a_{2}b_{n - 1} + \cdots + a_{n}b_{1} \leq a_{1}c_{1} + a_{2}c_{2} + \cdots + a_{n}c_{n} \leq a_{1}b_{1} + a_{2}b_{2} + \cdots + a_{n}b_{n}$

当且仅当$a_{1} = a_{2} = \cdots + a_{n}$或$b_{1} = b_{2} = \cdots = b_{n}$时，反序和等于正序和。

其中$S_{1} = a_{1}b_{n} + a_{2}b_{n - 1} + \cdots + a_{n}b_{1}$，称为反序和；$S_{2} = a_{1}b_{1} + a_{2}b_{2} + \cdots + a_{n}b_{n}$，称为正序和；$S = a_{1}c_{1} + a_{2}c_{2} + \cdots + a_{n}c_{n}$，称为乱序和。故排序不等式也可表示为$S_{1} \leq S \leq S_{2}$（反序和$\leq$乱序和$\leq$正序和）。

证明：$S = a_{1}c_{1} + a_{2}c_{2} + \cdots + a_{n}c_{n}$的不同的值只有有限个（个数$\leq n!$），其中必有最大值和最小值。

若$c_{1} \neq b_{1}$，则有某$c_{k} = b_{1}\ \ (k > 1)\text{，}c_{1} > c_{k}$。将$S$中$c_{1}\text{，}c_{k}$对换，得

$S' = a_{1}c_{k} + \cdots + a_{k}c_{1} + \cdots + a_{n}c_{n}$

所以

$S' - S = a_{1}c_{k} + a_{k}c_{1} - a_{1}c_{1} - a_{k}c_{k} = \left( a_{k} - a_{1} \right)\left( c_{1} - c_{k} \right) \geq 0$

做类似有限部调整，可得$S \leq S_{2}$，类似的可证$S_{1} \leq S$，经讨论得到去等条件。

卡尔松不等式（矩阵长方形不等式）

$m \times n$的非负实数矩阵中，$n$列每列元素之和的几何平均值不小于矩阵中$m$行每行元素的几何平均值之和。

对于矩阵

$\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$

其中$a_{ij} \geq 0$，有

$\sqrt[n]{\prod_{j = 1}^{n}{\sum_{i = 1}^{m}a_{ij}}} \geq \sum_{i = 1}^{m}\sqrt[n]{\prod_{j = 1}^{n}a_{ij}}$

> 当$n = 2$时，其退化为柯西不等式。

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

证明不等式的基本方法

1、比较法：做差或做商

$eg.``\text{糖水不等式}"\text{：}a\text{，}b\text{，}m \in \mathbb{R}_{+}\text{，}a < b$，则

$\frac{a + m}{b + m} > \frac{a}{b}$

证明：两边做差，得

$\frac{a + m}{b + m} - \frac{a}{b} = \frac{m(b - a)}{b(b + m)}$

由$a < b$，得$m(b - a) > 0$，故该不等式大于0，得证。

$eg.a\text{，}b \in \mathbb{R}_{+}$，$a^{a}b^{b} \geq a^{b}b^{a}$，当且仅当$a = b$时，等号成立。

证明：两边相除，得

$\frac{a^{a}b^{b}}{a^{b}b^{a}} = a^{a - b} \cdot b^{b - a} = \left( \frac{a}{b} \right)^{a - b}$

$\text{不妨设}a \geq b > 0\text{，则}\frac{a}{b} > 1\text{，}a - b \geq 0\text{，}\left( \frac{a}{b} \right)^{a - b} \geq 1\text{当且仅当}a = b\text{时，等号成立。得证。}$

2、综合法与分析法：执果索因与有因导果。

3、反证法

4、放缩法

5、数学归纳法

不等式的全导数定理

$\text{对于}n\text{元函数}f\left( x_{1}\text{，}x_{2}\text{，}\cdots{\text{，}x}_{n} \right)$，已知$x_{1}x_{2}\cdots x_{n} \geq 0$

如果

> $1.\text{当}x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} = 0\text{时，}f \geq 0$
>
> $2.D(f) \geq 0$

则

$f\left( x_{1}\text{，}x_{2}\text{，}\cdots{\text{，}x}_{n} \right) \geq 0\text{恒成立}$

$eg.a^{2} + b^{2} \geq 2ab$

$D\left( a^{2} + b^{2} \right) \geq D(2ab) \Leftrightarrow 2a + 2b \geq 2a + 2b$

二元不等式链

$\frac{ab}{a + b - \sqrt{ab}} \leq \frac{\sqrt{2}ab}{\sqrt{a^{2} + b^{2}}} \leq \frac{2}{\frac{1}{a} + \frac{1}{b}} \leq \frac{ab\left( \ln a - \ln b \right)}{a - b} \leq \sqrt[3]{\frac{2a^{2}b^{2}}{a + b}} \leq \sqrt{ab} \leq \sqrt[3]{\frac{ab(a + b)}{2}} \leq L(a\text{，}b) = \left\{ \begin{array}{r} \frac{a - b}{\ln a - \ln b}\ \ \ (a \neq b) \\ a\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ (a = b) \end{array} \right.\  \leq \left( \frac{\sqrt[3]{a} + \sqrt[3]{b}}{2} \right)^{3} \leq \left( \frac{\sqrt{a} + \sqrt{b}}{2} \right)^{2} \leq \frac{a + \sqrt{ab} + b}{3} \leq \sqrt{\frac{a + b}{2}} \leq \frac{\sqrt{a} + \sqrt{b}}{2} \leq \frac{a + b}{2} \leq \sqrt{\frac{a^{2} + ab + b^{2}}{3}} \leq \left( \frac{a^{\frac{3}{2}} + b^{\frac{3}{2}}}{2} \right)^{\frac{2}{3}} \leq \sqrt[3]{\frac{(a + b)\left( a^{2} + b^{2} \right)}{4}} \leq \frac{2\left( a^{2} + ab + b^{2} \right)}{3(a + b)} \leq \sqrt{\frac{a^{2} + b^{2}}{2}} \leq \sqrt[3]{\frac{a^{3} + b^{3}}{2}} \leq \frac{a^{2} + b^{2}}{ab} \leq \sqrt{a^{2} - ab + b^{2}} \leq \frac{a^{\frac{5}{2}} + b^{\frac{5}{2}}}{a^{\frac{3}{2}} + b^{\frac{3}{2}}} \leq \left( a^{\frac{a}{b}}b^{\frac{b}{a}} \right)^{\frac{1}{\frac{a}{b} + \frac{b}{a}}} \leq \frac{a^{2} + b^{2}}{2\sqrt{ab}} \leq \frac{a^{3} + b^{3}}{2ab} \leq \frac{a^{4} + b^{4}}{2a^{\frac{3}{2}}b^{\frac{3}{2}}}$

课本例题习题节选

（$a\text{，}b\text{，}c\text{，}d \in \mathbb{R}_{+}\text{，}x\text{，}y\text{，}z\text{，}w\mathbb{\in R}\text{，}n \in \mathbb{N}_{+}$）

$(a + b + c)^{3} \geq 27abc$

$(a + b)(b + c)(a + c) \geq 8abc$

$a + b + c \geq \sqrt{ab} + \sqrt{bc} + \sqrt{ca}$

$x^{2} + y^{2} + z^{2} + w^{2} \geq xy + yz + zw + wx$

$\left( \frac{a}{b} + \frac{b}{c} + \frac{c}{a} \right)\left( \frac{b}{a} + \frac{c}{b} + \frac{a}{c} \right) \geq 9$

$(a + b + c)\left( a^{2} + b^{2} + c^{2} \right) \geq 9abc$

$a\left( b^{2} + c^{2} \right) + b\left( c^{2} + a^{2} \right) + c\left( a^{2} + b^{2} \right) > 6abc$

$1 + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{3}} + \cdots + \frac{1}{\sqrt{n}} < 2\sqrt{n}$

$\left( a_{1} + a_{2} + \cdots + a_{n} \right)\left( \frac{1}{a_{1}} + \frac{1}{a_{2}} + \cdots + \frac{1}{a_{n}} \right) \geq n^{2}$

$\frac{2}{a + b} + \frac{2}{b + c} + \frac{2}{c + a} \geq \frac{9}{a + b + c}$

$2\left( a^{3} + b^{3} + c^{3} \right) \geq a^{2}(b + c) + b^{2}(a + c) + c^{2}(a + b)$

$\frac{ab}{c} + \frac{bc}{a} + \frac{ca}{b} \geq a + b + c$

$\frac{a_{1}^{2}}{a_{2}} + \frac{a_{2}^{2}}{a_{3}} + \cdots + \frac{a_{n - 1}^{2}}{a_{n}} + \frac{a_{n}^{2}}{a_{1}} \geq a_{1} + a_{2} + \cdots + a_{n}$

$(1 + 2 + 3 + \cdots + n)\left( 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} \right) \geq n^{2} + n - 1\ \ (n \geq 2)$

$\frac{1}{2^{2}} + \frac{1}{3^{2}} + \cdots + \frac{1}{n^{2}} < \frac{n - 1}{n}$

$\frac{n(n + 1)}{2} < \sqrt{1 \cdot 2} + \sqrt{2 \cdot 3} + \cdots + \sqrt{n(n + 1)} < \frac{(n + 1)^{2}}{2}$

$\left| \sin\left( \alpha_{1} + \alpha_{2} + \cdots + \alpha_{n} \right) \right| < \sin\alpha_{1} + \sin\alpha_{2} + \cdots + \sin\alpha_{n}\ \ \left( \alpha_{i} \in (0\text{，}\pi) \right)$

$\left( a_{1} + a_{2} + \cdots + a_{n} \right)\left( \frac{1}{a_{1}} + \frac{1}{a_{2}} + \cdots + \frac{1}{a_{n}} \right) \geq n^{2}$
