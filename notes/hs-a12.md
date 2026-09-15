---
title: "部分结论证明"
hs_seq: "A12"
description: "部分结论证明：一元二次函数、方程和不等式"
---

# 部分结论证明

集合与常用逻辑术语

一元二次函数、方程和不等式

基本不等式

$\sqrt{ab} \leq \frac{a + b}{2} = \frac{\left( \sqrt{a} \right)^{2} + \left( \sqrt{b} \right)^{2}}{2} \Leftarrow \left( \sqrt{a} \right)^{2} + \left( \sqrt{b} \right)^{2} \geq 2\sqrt{ab}$

二元均值不等式

$a + b \geq 2\sqrt{ab} = \frac{2ab}{\sqrt{ab}} \Rightarrow \sqrt{ab} \geq \frac{2ab}{a + b} = \frac{2}{\frac{1}{a} + \frac{1}{b}}$

$\frac{a + b}{2} \leq \sqrt{\frac{a^{2} + b^{2}}{2}} \Leftarrow a + b \leq \sqrt{2\left( a^{2} + b^{2} \right)} \Leftarrow (a + b)^{2} \leq 2\left( a^{2} + b^{2} \right) \Leftarrow 2ab \leq a^{2} + b^{2}$

对数均值不等式证明部分参见“函数”

柯西不等式

$\left( a^{2} + b^{2} \right)\left( c^{2} + d^{2} \right) \geq (ac + bd)^{2} \Rightarrow a^{2}c^{2} + a^{2}d^{2} + b^{2}c^{2} + b^{2}d^{2} \geq a^{2}c^{2} + b^{2}d^{2} + 2abcd$

> $\Rightarrow (ad)^{2} + (bc)^{2} \geq 2abcd$

权方和不等式

由柯西不等式，得

$\left( \left( \frac{a}{\sqrt{x}} \right)^{2} + \left( \frac{b}{\sqrt{y}} \right)^{2} \right)\left( \left( \sqrt{x} \right)^{2} + \left( \sqrt{y} \right)^{2} \right) \geq (a + b)^{2} \Rightarrow \frac{a^{2}}{x} + \frac{b^{2}}{y} \geq \frac{(a + b)^{2}}{x + y}$

乘几除几

1.

$\text{联立}\left\{ \begin{array}{r} a\alpha + c\beta = p \\ b\alpha + d\beta = q \end{array} \right.\ \text{，解得}\left\{ \begin{array}{r} \alpha = - \frac{dp - cq}{bc - ad} \\ \beta = \ \ \ \ \frac{bp - aq}{bc - ad} \end{array} \right.\$

由$px + qy = i$，得

$- \frac{dp - cq}{bc - ad}(ax + by + e) + \frac{bp - aq}{bc - ad}(cx + dy + f) = - e \cdot \frac{dp - cq}{bc - ad} + f \cdot \frac{bp - aq}{bc - ad} + i$

于是得

$\frac{m}{ax + by + e} + \frac{n}{cx + dy + f}$

$\geq \left( - e \cdot \frac{dp - cq}{bc - ad} + f \cdot \frac{bp - aq}{bc - ad} + i \right)^{- 1}\left( - m \cdot \frac{dp - cq}{bc - ad} + n \cdot \frac{bp - aq}{bc - ad} + 2\sqrt{- mn \cdot \frac{dp - cq}{bc - ad} \cdot \frac{bp - aq}{bc - ad}} \right)$

$= \left( - e \cdot \frac{dp - cq}{bc - ad} + f \cdot \frac{bp - aq}{bc - ad} + i \right)^{- 1}\left( \sqrt{- m \cdot \frac{dp - cq}{bc - ad}} + \sqrt{n \cdot \frac{bp - aq}{bc - ad}} \right)^{2}$

2.

$\text{联立}\left\{ \begin{array}{r} a\alpha + c\beta = p \\ b\alpha + d\beta = q \end{array} \right.\ \text{，解得}\left\{ \begin{array}{r} \alpha = - \frac{dp - cq}{bc - ad} \\ \beta = \ \ \ \ \frac{bp - aq}{bc - ad} \end{array} \right.\$

$\text{则}px + qy = - \frac{dp - cq}{bc - ad}(ax + by + e) + \frac{bp - aq}{bc - ad}(cx + dy + f) + e \cdot \frac{dp - cq}{bc - ad} - f \cdot \frac{bp - aq}{bc - ad}$

于是得

$px + qy \geq i^{- 1}\left( - m \cdot \frac{dp - cq}{bc - ad} + n \cdot \frac{bp - aq}{bc - ad} + 2\sqrt{- mn \cdot \frac{dp - cq}{bc - ad} \cdot \frac{bp - aq}{bc - ad}} \right) + e \cdot \frac{dp - cq}{bc - ad} - f \cdot \frac{bp - aq}{bc - ad}$

$= i^{- 1}\left( \sqrt{- m \cdot \frac{dp - cq}{bc - ad}} + \sqrt{n \cdot \frac{bp - aq}{bc - ad}} \right)^{2} + e \cdot \frac{dp - cq}{bc - ad} - f \cdot \frac{bp - aq}{bc - ad}$

桥梁法

1.

$ab\left\lbrack i - (ax + by) \right\rbrack = abcxy \leq c \cdot \left( \frac{ax + by}{2} \right)^{2}\overset{t = ax + by}{\Rightarrow}ab(i - t) = \frac{ct^{2}}{4}$

$\Rightarrow t \in \left( - \infty \text{，}2\frac{- ab - \sqrt{ab + abci}}{c} \right) \cup \left( 2\frac{- ab + \sqrt{ab + abci}}{c}\text{，} + \infty \right)$

$\text{由}a\text{，}b\text{均为正数，得}2\frac{- ab - \sqrt{ab + abci}}{c} < 0\text{，所以}k(ax + by)\text{只存在最小值}2\frac{- ab + \sqrt{ab + abci}}{c}$

2.

$i - cxy = ax + by \geq 2\sqrt{abxy}\overset{t = xy}{\Rightarrow}i - ct \geq 2\sqrt{abt}$

$\Rightarrow t \in \left( - \infty \text{，}\frac{ci + 2ab - 2\sqrt{a^{2}b^{2} + abci}}{c^{2}} \right) \cup \left( \frac{ci + 2ab + 2\sqrt{a^{2}b^{2} + abci}}{c^{2}}\text{，} + \infty \right)$

$\text{由}a\text{，}b\text{均为正数，得}\frac{ci + 2ab - 2\sqrt{a^{2}b^{2} + abci}}{c^{2}} > 0$

$\frac{ci + 2ab + 2\sqrt{a^{2}b^{2} + abci}}{c^{2}} > i\text{，所以}kxy\text{只存在最大值}\frac{ci + 2ab - 2\sqrt{a^{2}b^{2} + abci}}{c^{2}}$

二次函数顶点式的推导

$y = ax^{2} + bx + c = a\left( x^{2} + \frac{b}{a}x + \frac{c}{a} \right) = a\left( x^{2} + \frac{b}{a}x + \frac{b^{2}}{4a^{2}} - \frac{b^{2}}{4a^{2}} + \frac{c}{a} \right) = a\left\lbrack \left( x + \frac{b}{2a} \right)^{2} + \frac{4ac - b^{2}}{4a^{2}} \right\rbrack = a\left( x + \frac{b}{2a} \right)^{2} + \frac{4ac - b^{2}}{4a}$

二次函数的切线

设过点$\left( x_{0}\text{，}y_{0} \right)$的直线与二次函数$y = ax^{2} + bx + c$相切于点$\left( t\text{，}at^{2} + bt + c \right)$，得到切线方程

$y - \left( at^{2} + bt + c \right) = (2at + b)(x - t)$

由点$\left( x_{0}\text{，}y_{0} \right)$也在该切线上，得

$y_{0} - \left( at^{2} + bt + c \right) = (2at + b)\left( x_{0} - t \right)$

关于t整理，得到

$at^{2} - 2ax_{0}t - bx_{0} - c + y_{0} = 0$

这个关于t方程的解的个数即为可作切线条数。因此

$\Delta = 4a^{2}x_{0}^{2} - 4a\left( - bx_{0} - c + y_{0} \right) = 4a\left( ax_{0}^{2} + bx_{0} + c - y_{0} \right)$

$1.\Delta > 0$，即可作两条切线，此时对$a$分类讨论可得到点在图像的凸侧。

$2.\Delta = 0$，即可作一条切线，此时$y_{0} = ax_{0}^{2} + bx_{0} + c$，即点在图像上。

$3.\Delta < 0$，即不能作出切线，此时对$a$分类讨论可得到点在图像的凹侧。

常见奇函数、偶函数模型

$1.f(x) = \frac{a^{x} \mp 1}{a^{x} \pm 1}\text{或}f(x) = \frac{1 \mp a^{x}}{1 \pm a^{x}}\ \ \left. \text{（只以}\frac{a^{x} - 1}{a^{x} + 1}\text{为例} \right.\text{）}$

$f(x) + f( - x) = \frac{a^{x} - 1}{a^{x} + 1} + \frac{a^{- x} - 1}{a^{- x} + 1} = \frac{a^{x} - 1}{a^{x} + 1} + \frac{1 - a^{x}}{1 + a^{x}} = 0\ \ \left( \text{分子分母同乘}a^{x} \right)$

$2.f(x) = \frac{a^{x} \mp a^{- x}}{a^{x} \pm a^{- x}} = \frac{a^{2x} \mp 1}{a^{2x} \pm 1}\ \ \left. \text{（只以}\frac{a^{x} - a^{- x}}{a^{x} + a^{- x}}\text{为例} \right.\text{）}$

$f(x) + f( - x) = \frac{a^{x} - a^{- x}}{a^{x} + a^{- x}} + \frac{a^{- x} - a^{x}}{a^{- x} + a^{x}} = \frac{a^{x} - a^{- x} + a^{- x} - a^{x}}{a^{x} + a^{- x}} = 0$

$3.f(x) = a^{x} - a^{- x}$（略）

$4.f(x) = \log_{c}\frac{ax \mp b}{ax \pm b}\text{或}f(x) = \log_{c}\frac{b \mp ax}{b \pm ax}\ \ \left. \text{（只以}\log_{c}\frac{ax - b}{ax + b}\text{为例} \right.\text{）}$

$f(x) + f( - x) = \log_{c}\frac{ax - b}{ax + b} + \log_{c}\frac{- ax - b}{- ax + b} = \log_{c}\left( \frac{ax - b}{ax + b} \cdot \frac{ax + b}{ax - b} \right) = 0\ \ (\text{分子分母同乘} - 1)$

$5.f(x) = \log_{a}\left( \sqrt{{(mx)}^{2} + 1} \pm mx \right)$

> ${f(x) + f( - x) = \log_{a}\left( \sqrt{(mx)^{2} + 1} \pm mx \right) + \log_{a}\left( \sqrt{(mx)^{2} + 1} \mp mx \right) }{= \log_{a}\left\lbrack \left( \sqrt{(mx)^{2} + 1} \pm mx \right)\left( \sqrt{(mx)^{2} + 1} \mp mx \right) \right\rbrack }{= \log_{a}\left\lbrack \left( \sqrt{(mx)^{2} + 1} \right)^{2} - m^{2}x^{2} \right\rbrack = 0}$

$6.f(x) = a^{x} + a^{- x}$（略）

$7.f(x) = \log_{a}{(1 + a^{mx})} - \frac{m}{2}x$

$f(x) = \log_{a}{(1 + a^{mx})} - \log_{a}a^{\frac{m}{2}x} = \log_{a}\frac{1 + a^{mx}}{a^{\frac{m}{2}x}} = \log_{a}\frac{a^{- mx} + 1}{a^{- \frac{m}{2}x}} = \log_{a}\left( 1 + a^{- mx} \right) + \frac{m}{2}x = f( - x)$

常见对称函数

$1.f(x) = \frac{n}{a^{x} + m}$

$\text{引理：}y = \frac{a^{x} - m}{a^{x} + m}\text{关于}\left( \log_{a}|m|\text{，}0 \right)\text{对称。}$

证明：

$f(x) = \frac{a^{x} - m}{a^{x} + m} = \frac{\frac{a^{x}}{m} - 1}{\frac{a^{x}}{m} + 1} = \frac{a^{x - \log_{a}|m|} - 1}{a^{x - \log_{a}|m|} + 1}\overset{g(x) = \frac{a^{x} - 1}{a^{x} + 1}}{\Rightarrow}f(x) = g\left( x - \log_{a}|m| \right)$

由$g(x)$是奇函数，可得到$f(x)\text{关于}\left( \log_{a}|m|\text{，}0 \right)\text{对称}$

$f(x) = \frac{n}{a^{x} + m} = \frac{n}{2m} \cdot \frac{\left( a^{x} + m \right) - \left( a^{x} - m \right)}{a^{x} + m} = \frac{n}{2m}\left( 1 - \frac{a^{x} - m}{a^{x} + m} \right) = - \frac{n}{2m} \cdot \frac{a^{x} - m}{a^{x} + m} + \frac{n}{2m}$

可得到$f(x)\text{关于}\left( \log_{a}|m|\text{，}\frac{n}{2m} \right)$对称

导函数的对称性与周期性

对称性

周期性

假如函数满足

$f(x) = f(x + T)$

则有

$f'(x) = \left\lbrack f(x + T) \right\rbrack' = f'(x + T)$

轴对称、中心对称、周期性知二得一

1.轴对称和中心对称得周期性：

2.轴对称和周期性得中心对称：

3.中心对称和周期性得轴对称：

抽象函数

$1.f(x + y) = f(x) + f(y) - b$

$a.f(0 + 0) = f(0) + f(0) - b \Rightarrow f(0) = b$

$b.b = f(0) = f\left( x + ( - x) \right) = f(x) + f( - x) - b \Rightarrow f(x) + f( - x) = 2b$

$c.y > b\text{，}\forall x_{1}\text{，}x_{2} \in \mathbb{R}_{+}\text{，}x_{1} < x_{2}\text{，}f\left( x_{1} \right) - f\left( x_{2} \right) = f\left( x_{1} - x_{2} + x_{2} \right) - f\left( x_{2} \right) = f\left( x_{1} - x_{2} \right) + f\left( x_{2} \right) - f\left( x_{2} \right) - b = f\left( x_{1} - x_{2} \right) - b = \left( 2b - f\left( x_{2} - x_{1} \right) \right) - b = - f\left( x_{2} - x_{1} \right) + b < 0 \Rightarrow f\left( x_{1} \right) - f\left( x_{2} \right) < 0\text{，}y < b\text{同理}$

$2.f(x + y) = f(x) \cdot f(y)$

$a.f(0) = f(0) \cdot f(0) \Rightarrow f(0) = 0\text{或}1f(x + 0) = f(0) \cdot f(0)\text{当}f(0) = 0\text{时，}f(x)\text{恒为}0\text{，故}f(0) = 1$

$b.f( - x) = f(x - 2x) = f(x)f( - x)f( - x) \Rightarrow f(x) \cdot f( - x) = 1$

$c.$

对数均值不等式

证明中用到了齐次化的方法。

不妨设$a > b > 0$

$1.\sqrt{ab} < \frac{a - b}{\ln a - \ln b} \Leftarrow \ln a - \ln b < \frac{a - b}{\sqrt{ab}} \Leftarrow \ln\frac{a}{b} < \sqrt{\frac{a}{b}} - \sqrt{\frac{b}{a}}\overset{x = \sqrt{\frac{a}{b}} > 1}{\Leftarrow}2\ln x < x - \frac{1}{x}$

$f(x) = 2\ln x - x + \frac{1}{x} \Rightarrow f'(x) = \frac{2}{x} - 1 - \frac{1}{x^{2}} = - \left( 1 - \frac{1}{x} \right)^{2}\overset{x > 1}{\Rightarrow}f'(x) < 0 \Rightarrow f(x) < f(1) = 0\text{，得证}$

$2.\frac{a - b}{\ln a - \ln b} < \frac{a + b}{2} \Leftarrow \ln a - \ln b > \frac{2(a - b)}{a + b} \Leftarrow \ln\frac{a}{b} > \frac{2\left( \frac{a}{b} - 1 \right)}{\frac{a}{b} + 1}\overset{x = \frac{a}{b} > 1}{\Leftarrow}\ln x > \frac{2(x - 1)}{x + 1}$

$g(x) = \ln x - \frac{2(x - 1)}{x + 1} \Rightarrow g'(x) = \frac{1}{x} - \frac{4}{(x + 1)^{2}} = \frac{(x - 1)^{2}}{x(x + 1)^{2}}\overset{x > 1}{\Rightarrow}g'(x) > 0 \Rightarrow g(x) > g(1) = 0\text{，得证}$

$0 < a < b$时同理可得。

泰勒公式理解助记

用多项式函数

$p_{n}(x) = a_{0} + a_{1}\left( x - x_{0} \right) + a_{2}\left( x - x_{0} \right)^{2} + \cdots + a_{n}\left( x - x_{0} \right)^{n}$

去近似已知函数$f(x)$，即自变量任取一值$x_{0}$，都有$p_{n}\left( x_{0} \right) = f\left( x_{0} \right)$，且在该点处的各阶导数均相等。为此，求出$p_{n}(x)$的各阶导函数。

> $p_{n}^{(0)}(x) = a_{0} + a_{1}\left( x - x_{0} \right) + a_{2}\left( x - x_{0} \right)^{2} + \cdots + a_{n}\left( x - x_{0} \right)^{n}$
>
> $p_{n}^{(1)}(x) = a_{1} + 2a_{2}\left( x - x_{0} \right) + 3a_{3}\left( x - x_{0} \right)^{2} + \cdots + na_{n}\left( x - x_{0} \right)^{n - 1}$
>
> $p_{n}^{(2)}(x) = 2a_{2} + 2 \times 3a_{3}\left( x - x_{0} \right) + 2 \times 3 \times 4a_{4}\left( x - x_{0} \right)^{2} + \cdots + n(n - 1)a_{n}\left( x - x_{0} \right)^{n - 2}$
>
> $\cdots\cdots\cdots$
>
> $p_{n}^{(n - 1)}(x) = (n - 1)!a_{n - 1} + n!a_{n}\left( x - x_{0} \right)$
>
> $p_{n}^{(n)}(x) = n!a_{n}$

$\text{由}\left\{ \begin{array}{r} p_{n}\left( x_{0} \right) = f\left( x_{0} \right)\ \ \ \ \ \ \ \  \\ p_{n}'\left( x_{0} \right) = f'\left( x_{0} \right)\ \ \ \ \ \ \  \\ p_{n}^{''}\left( x_{0} \right) = f^{''}\left( x_{0} \right)\ \ \ \ \  \\ \cdots \\ p_{n}^{(n)}\left( x_{0} \right) = f^{(n)}\left( x_{0} \right) \end{array} \right.\ \text{，得}\left\{ \begin{array}{r} a_{0} = f\left( x_{0} \right)\ \ \ \ \ \ \ \ \ \  \\ a_{1} = f'\left( x_{0} \right)\ \ \ \ \ \ \ \ \  \\ a_{2} = \frac{1}{2!}f^{''}\left( x_{0} \right)\ \ \  \\ \cdots \\ a_{n} = \frac{1}{n!}f^{(n)}\left( x_{0} \right) \end{array} \right.\$

得到多形式近似

$f(x) \approx p_{n}(x) = f\left( x_{0} \right) + f'\left( x_{0} \right)\left( x - x_{0} \right) + \frac{f^{''}\left( x_{0} \right)}{2!}\left( x - x_{0} \right)^{2} + \cdots + \frac{f^{(n)}\left( x_{0} \right)}{n!}\left( x - x_{0} \right)^{n}$

这样就得到了泰勒公式。

三次函数的切割线

为了得到三次函数的切线与三次函数$f(x) = ax^{3} + bx^{2} + cx + d$的交点情况，设切点$(x_{0}f\left( x_{0} \right))$，得到切线方程$y - \left( ax_{0}^{3} + bx_{0}^{2} + cx_{0} + d \right) = \left( 3ax_{0}^{2} + 2bx_{0} + c \right)\left( x - x_{0} \right)$，把它与三次函数联立得

$ax^{3} + bx^{2} + cx + d = \left( ax_{0}^{3} + bx_{0}^{2} + cx_{0} + d \right) + \left( 3ax_{0}^{2} + 2bx_{0} + c \right)\left( x - x_{0} \right)$

把$\left( ax_{0}^{3} + bx_{0}^{2} + cx_{0} + d \right)$移到等号左边，利用立方差公式和平方差公式，得

$a\left( x - x_{0} \right)\left( x^{2} + x_{0}x + x_{0}^{2} \right) + b\left( x - x_{0} \right)\left( x + x_{0} \right) + c\left( x - x_{0} \right) = \left( 3ax_{0}^{2} + 2bx_{0} + c \right)(x - x_{0})$

提出公因式$\left( x - x_{0} \right)$，以$x$整理，得

$\left( x - x_{0} \right)\left\lbrack ax^{2} + \left( ax_{0} + b \right)x - \left( 2ax_{0}^{2} + b \right)x \right\rbrack = 0$

运用十字相乘法，得

$\left( ax + 2ax_{0} + b \right)\left( x - x_{0} \right)^{2} = 0$

解得

$x_{1} = - \left( 2x_{0} + \frac{b}{a} \right)\text{，}x_{2} = x_{3} = x_{0}$

由此得到切线与三次函数的交点坐标

$\left( x_{0}\text{，}f\left( x_{0} \right) \right)\text{和}\left( - 2x_{0} - \frac{b}{a}\text{，}f\left( - 2x_{0} - \frac{b}{a} \right) \right)$

由此得到切点横坐标的二倍$+$交点横坐标$= - \frac{b}{a}$

和/差角公式$C_{(\alpha - \beta)}$

$\text{在单位圆上，设}A(1\text{，}0)\text{，}P_{1}\left( \cos\alpha \text{，}\sin\alpha \right)\text{，}A_{1}\left( \cos\beta \text{，}\sin\beta \right)\text{，}P\left( \cos(\alpha - \beta)\text{，}\sin(\alpha - \beta) \right)$

$|AP| = \left| A_{1}P_{1} \right| \Rightarrow \left\lbrack \cos(\alpha - \beta) - 1 \right\rbrack^{2} + \sin^{2}(\alpha - \beta) = \left( \cos\alpha - \cos\beta \right)^{2} + \left( \sin\alpha - \sin\beta \right)^{2}$

$\Rightarrow \cos^{2}(\alpha - \beta) - 2\cos(\alpha - \beta) + 1 + \sin^{2}(\alpha - \beta) = \cos^{2}\alpha - 2\cos\alpha\cos\beta + \cos^{2}\beta + \sin^{2}\alpha - 2\sin\beta\sin\beta + \sin^{2}\beta$

$\Rightarrow 2 - 2\cos(\alpha - \beta) = 2 - 2\cos\alpha\cos\beta - 2\sin\beta\sin\beta \Rightarrow \cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\beta\sin\beta$

设两个单位向量$\mathbf{a} = \left( \cos x\text{，}\sin x \right)\text{，}\mathbf{b} = \left( \cos y\text{，}\sin y \right)\text{，则}\mathbf{a \cdot b} = \cos x\cos y + \sin x\sin y$

又由点积定义，$\mathbf{a \cdot b} = 1 \times 1\cos(x - y)\text{，得到}\cos(x - y) = \cos x\cos y + \sin x\sin y$

三倍角公式：

${\sin{3\alpha} = \sin(2\alpha + \alpha) = \sin{2\alpha}\cos\alpha + \cos{2\alpha}\sin\alpha = 2\sin\alpha\cos^{2}\alpha + \left( 1 - 2\sin^{2}\alpha \right)\sin\alpha }{= 2\sin\alpha\left( 1 - \sin^{2}\alpha \right) + \sin\alpha - 2\sin^{3}\alpha = 2\sin\alpha - 2\sin^{3}\alpha + \sin\alpha - 2\sin^{3}\alpha }{= 3\sin\alpha - 4\sin^{3}\alpha }{= 4\sin\alpha\left( \frac{3}{4} - \sin^{2}\alpha \right) = 4\sin\alpha\left( \sin^{2}\frac{\pi}{3} - \sin^{2}\alpha \right) = 4\sin\alpha\sin\left( \frac{\pi}{3} + \alpha \right)\sin\left( \frac{\pi}{3} - \alpha \right)}$

${\cos{3\alpha} = \cos(2\alpha + \alpha) = \cos{2\alpha}\cos\alpha - \sin{2\alpha}\sin\alpha = \left( 2\cos^{2}\alpha - 1 \right)\cos\alpha - 2\sin^{2}\alpha\cos\alpha }{= 2\cos^{3}\alpha - \cos\alpha - 2\left( 1 - \cos^{2}\alpha \right)\cos\alpha = 2\cos^{3}\alpha - \cos\alpha - 2\cos\alpha + 2\cos^{3}\alpha }{= - 3\cos\alpha + 4\cos^{3}\alpha }{= - 4\cos\alpha\left( \frac{3}{4} - \cos^{2}\alpha \right) = - 4\cos\alpha\left( - \frac{1}{4} + \sin^{2}\alpha \right) = 4\cos\alpha\left( \sin^{2}\frac{\pi}{6} - \sin^{2}\alpha \right) }{= 4\cos\alpha\sin\left( \frac{\pi}{6} - \alpha \right)\sin\left( \frac{\pi}{6} + \alpha \right) = 4\cos\alpha\cos\left( \frac{\pi}{3} + \alpha \right)\cos\left( \frac{\pi}{3} - \alpha \right)}$

${\tan{3\alpha} = \tan{(2\alpha + \alpha)} = \frac{\tan{2\alpha} + \tan\alpha}{1 - \tan{2\alpha}\tan\alpha} = \frac{\frac{2\tan\alpha}{1 - \tan^{2}\alpha} + \tan\alpha}{1 - \frac{2\tan^{2}\alpha}{1 - \tan^{2}\alpha}} = \frac{2\tan\alpha + \tan\alpha - \tan^{3}\alpha}{1 - \tan^{2}\alpha - 2\tan^{2}\alpha} = \frac{3\tan\alpha - \tan^{3}\alpha}{1 - 3\tan^{2}\alpha} }{= \frac{\sin{3\alpha}}{\cos{3\alpha}} = \frac{4\sin\alpha\sin\left( \frac{\pi}{3} + \alpha \right)\sin\left( \frac{\pi}{3} - \alpha \right)}{4\cos\alpha\cos\left( \frac{\pi}{3} + \alpha \right)\cos\left( \frac{\pi}{3} - \alpha \right)} = \tan\alpha\tan\left( \frac{\pi}{3} + \alpha \right)\tan\left( \frac{\pi}{3} - \alpha \right)}$

和差化积公式:

> $\sin{(\alpha + \beta)} = \sin\alpha\cos\beta + \cos\alpha\sin\beta\cdots\cdots 1$
>
> $\sin{(\alpha - \beta)} = \sin\alpha\cos\beta - \cos\alpha\sin\beta\cdots\cdots 2$
>
> 1+2，得$\sin{(\alpha + \beta)} + \sin{(\alpha - \beta)} = 2\sin\alpha\cos\beta$
>
> $\text{令}m = \alpha + \beta \text{，}n = \alpha - \beta \text{，则}\alpha = \frac{m + n}{2}\text{，}\beta = \frac{m - n}{2}$
>
> $\text{带入得}\sin m + \sin n = 2\sin\frac{m + n}{2}\cos\frac{m - n}{2}\text{，即}\sin\alpha + \sin\beta = 2\sin\left( \frac{\alpha + \beta}{2} \right)\cos\left( \frac{\alpha - \beta}{2} \right)$

积化和差公式:

> $1 + 2\text{，得}2\sin\alpha\cos\beta = \sin{(\alpha + \beta)} + \sin{(\alpha - \beta)}\text{，即}$ $\sin\alpha\sin\beta = - \frac{1}{2}\lbrack\cos(\alpha + \beta) - \cos{(\alpha - \beta)}\rbrack$
>
> 其余同上

正弦平方差公式

由和差化积公式得

$\sin^{2}\alpha - \sin^{2}\beta = \frac{1 - \cos{2\alpha}}{2} - \frac{1 - \cos{2\beta}}{2} = - \sin\left( \frac{2\beta + 2\alpha}{2} \right)\sin\left( \frac{2\beta - 2\alpha}{2} \right) = \sin(\alpha + \beta)\sin(\alpha - \beta)$

万能公式之一

$\tan\frac{\alpha}{2} = \frac{\sin\frac{\alpha}{2}}{\cos\frac{\alpha}{2}} = \frac{2\sin\frac{\alpha}{2}\sin\frac{\alpha}{2}}{2\sin\frac{\alpha}{2}\cos\frac{\alpha}{2}} = \frac{1 - \cos\alpha}{\sin\alpha} = \frac{(1 - \cos\alpha)(1 + \cos\alpha)}{\sin\alpha(1 + \cos\alpha)} = \frac{\sin\alpha}{1 + \cos\alpha}$

${\sin A + \sin B + \sin C = 2\sin\frac{A + B}{2}\cos\frac{A - B}{2} + \sin(A + B) }{= 2\sin\frac{A + B}{2}\cos\frac{A - B}{2} + 2\sin\frac{A + B}{2}\cos\frac{A + B}{2} }{= 2\sin\frac{A + B}{2}\left( \cos\frac{A - B}{2} + \cos\frac{A + B}{2} \right) }{= 2\sin\frac{A + B}{2} \cdot 2\cos\frac{\frac{A - B}{2} + \frac{A + B}{2}}{2}\cos\frac{\frac{A - B}{2} - \frac{A + B}{2}}{2} }{= 4\cos\frac{C}{2}\cos\frac{A}{2}\cos\frac{B}{2}}$

$\cos A + \cos B + \cos C = 2\cos\frac{A + B}{2}\cos\frac{A - B}{2} - \cos(A + B)$

> $= 2\cos\frac{A + B}{2}\cos\frac{A - B}{2} - \left( 2\cos^{2}\frac{A + B}{2} - 1 \right)$ $= 1 + 2\cos\frac{A + B}{2}\left( \cos\frac{A - B}{2} - \cos\frac{A + B}{2} \right)$ $= 1 + 2\sin\frac{C}{2}\left( - 2\sin\frac{\frac{A - B}{2} + \frac{A + B}{2}}{2}\sin\frac{\frac{A - B}{2} - \frac{A + B}{2}}{2} \right)$
>
> $= 1 + 4\sin\frac{C}{2}\sin\frac{A}{2}\sin\frac{B}{2}$

${\tan A + \tan B + \tan C = \tan(A + B)\left( 1 - \tan A\tan B \right) - \tan C }{= - \tan C\left( 1 - \tan A\tan B \right) - \tan C }{= \tan A\tan B\tan C}$

$\tan\frac{A}{2}\tan\frac{B}{2} + \tan\frac{A}{2}\tan\frac{C}{2} + \tan\frac{B}{2}\tan\frac{C}{2}$

$= \tan\frac{A}{2}\tan\frac{B}{2} + \tan\frac{A}{2}\tan\left( \frac{\pi}{2} - \frac{A + B}{2} \right) + \tan\frac{B}{2}\tan\left( \frac{\pi}{2} - \frac{A + B}{2} \right)$ $= 1 - \frac{\tan\frac{A}{2} + \tan\frac{B}{2}}{\tan\frac{A + B}{2}} + \tan\frac{A}{2}\tan\left( \frac{\pi}{2} - \frac{A + B}{2} \right) + \tan\frac{B}{2}\tan\left( \frac{\pi}{2} - \frac{A + B}{2} \right)$ $= 1 - \frac{\tan\frac{A}{2} + \tan\frac{B}{2}}{\tan\frac{A + B}{2}} + \frac{\tan\frac{A}{2}}{\tan\frac{A + B}{2}} + \frac{\tan\frac{B}{2}}{\tan\frac{A + B}{2}} = 1$

${\sin{2A} + \sin{2B} + \sin{2C} = 2\sin(A + B)\cos(A - B) - \sin{2(A + B)} }{= 2\sin(A + B)\left\lbrack \cos(A - B) - \cos(A + B) \right\rbrack }{= 2\sin(A + B)\left( - 2\sin A\sin B \right) }{= 4\sin A\sin B\sin C}$

$\frac{a + b}{a - b} = \frac{\sin A + \sin B}{\sin A - \sin B} = \frac{2\sin\frac{A + B}{2}\cos\frac{A - B}{2}}{2\cos\frac{A + B}{2}\sin\frac{A - B}{2}} = \frac{\tan\frac{A + B}{2}}{\tan\frac{A - B}{2}}$

余弦定理

$\left| \mathbf{c} \right|^{2} = \mathbf{c} \cdot \mathbf{c} = \left( \mathbf{a} - \mathbf{b} \right)\left( \mathbf{a + b} \right) = \mathbf{a} \cdot \mathbf{a} + \mathbf{b} \cdot \mathbf{b} - 2\mathbf{ab} = \mathbf{a}^{2} + \mathbf{b}^{2} - 2\left| \mathbf{a} \right|\left| \mathbf{b} \right|\cos C$

其余同理

正弦定理

现假定为锐角三角形，钝角三角形同理。

过点A作于$\overrightarrow{AC}$垂直的单位向量$\mathbf{j}$，则$\mathbf{j}$于$\overrightarrow{AB}$的夹角为$\frac{\pi}{2} - A$，$\mathbf{j}$于$\overrightarrow{CB}$的夹角为$\frac{\pi}{2} - C$，由$\overrightarrow{AC} + \overrightarrow{CB} = \overrightarrow{AB}$，得

$\mathbf{j} \cdot \left( \overrightarrow{AC} + \overrightarrow{CB} \right) = \mathbf{j} \cdot \overrightarrow{AB} \Rightarrow \mathbf{j} \cdot \overrightarrow{AC} + \mathbf{j} \cdot \overrightarrow{CB} = \mathbf{j} \cdot \overrightarrow{AB}$

即

$\left| \mathbf{j} \right|\left| \overrightarrow{AC} \right|\cos\frac{\pi}{2} + \left| \mathbf{j} \right|\left| \overrightarrow{CB} \right|\cos\left( \frac{\pi}{2} - C \right) = \left| \mathbf{j} \right|\left| \overrightarrow{AB} \right|\cos\left( \frac{\pi}{2} - A \right)$

也即

$a\sin C = c\sin A$

钝角三角形同理可得

在$\bigtriangleup OBC$中，$\angle BOC = 2\angle A = 2A$，由余弦定理得

$a^{2} = R^{2} + R^{2} - 2R^{2}\cos{2A} = 2R^{2}\left( 1 - \cos{2A} \right) = 2R^{2} \cdot 2\sin^{2}A$

两边开方，得

$a = 2R\sin A$

$\text{即}\frac{a}{\sin A} = 2R$

同理$b = 2R\sin B$，$c = 2R\sin C$。

$S_{\bigtriangleup ABC} = \frac{1}{2}\sqrt{\overrightarrow{AB} \cdot \overrightarrow{AC} - \left( \overrightarrow{AB} \cdot \overrightarrow{AC} \right)^{2}} = \frac{1}{2}\sqrt{b^{2}c^{2} - \left( bc\cos\theta \right)^{2}} = \frac{1}{2}\sqrt{b^{2}c^{2}\left( 1 - \cos^{2}\theta \right)} = \frac{1}{2}bc\sin\theta$

其余同理

三角形中线重心相关结论

已知$BD\text{，}CE$为$\bigtriangleup ABC$的中线且交于点$G$，求证$AG$与第三条中线重合。

证明：设

$\overrightarrow{AG} = x\overrightarrow{AB} + (1 - x)\overrightarrow{AD} = x\overrightarrow{AB} + \frac{1 - x}{2}\overrightarrow{AD}$

$\overrightarrow{AG} = y\overrightarrow{AC} + (1 - y)\overrightarrow{AE} = \frac{1 - y}{2}\overrightarrow{AB} + y\overrightarrow{AC}$

则

$\left\{ \begin{array}{r} x = \frac{1 - y}{2} \\ y = \frac{1 - x}{2} \end{array} \right.\$，解得$\left\{ \begin{array}{r} x = \frac{1}{3} \\ y = \frac{1}{3} \end{array} \right.\$，即$\begin{matrix} \overrightarrow{AG} = \frac{1}{3}\overrightarrow{AB} + \frac{2}{3}\overrightarrow{AD} \\ \overrightarrow{AG} = \frac{1}{3}\overrightarrow{AC} + \frac{2}{3}\overrightarrow{AE} \end{matrix}$

得到

$\overrightarrow{AG} = \frac{1}{3}\overrightarrow{AB} + \frac{1}{3}\overrightarrow{AC}$

$\text{由平面向量基本定理，它与过点}A\text{的中线的方向向量}\left( \frac{1}{2}\overrightarrow{AB} + \frac{1}{2}\overrightarrow{AC} \right)\text{平行。这样就同时证明了三角形三条}$

中线交于一点和重心是中线的一个三等分点两个结论。

课本证明：（重心为$O$）

取$\overrightarrow{OB}\text{，}\overrightarrow{OC}$为基底，并设$\overrightarrow{EO} = t_{1}\overrightarrow{OB}\text{，}\overrightarrow{FO} = t_{2}\overrightarrow{OC}$，则

$\overrightarrow{EC} = \overrightarrow{EO} + \overrightarrow{OC} = t_{1}\overrightarrow{OB} + \overrightarrow{OC}$

$\overrightarrow{FB} = \overrightarrow{FO} + \overrightarrow{OB} = t_{2}\overrightarrow{OC} + \overrightarrow{OB}$

所以

$\overrightarrow{BC} = \overrightarrow{AC} - \overrightarrow{AB} = 2\overrightarrow{EC} - 2\overrightarrow{FB} = 2\left( t_{1}\overrightarrow{OB} + \overrightarrow{OC} \right) - 2\left( t_{2}\overrightarrow{OC} + \overrightarrow{OB} \right) = 2\left( t_{1} - 1 \right)\overrightarrow{OB} - 2\left( t_{2} - 1 \right)\overrightarrow{OC}$

又因为$\overrightarrow{BC} = \overrightarrow{AC} - \overrightarrow{AB}$，所以由平面向量基本定理，得

$\left\{ \begin{array}{r} 2\left( t_{1} - 1 \right) = - 1 \\ 2\left( t_{2} - 1 \right) = - 1 \end{array} \right.\$

解得

$t_{1} = \frac{1}{2}\text{，}t_{2} = \frac{1}{2}$

所以

$\overrightarrow{EO} = \frac{1}{2}\overrightarrow{OB}\text{，}\overrightarrow{FO} = \frac{1}{2}\overrightarrow{OC}$

因此

$\overrightarrow{AO} = \overrightarrow{FO} - \overrightarrow{FA} = \overrightarrow{FO} + \overrightarrow{FB} = \overrightarrow{FO} + \overrightarrow{FO} + \overrightarrow{OB} = \overrightarrow{OC} + \overrightarrow{OB}$

$\overrightarrow{OD} = \overrightarrow{BD} - \overrightarrow{BO} = \frac{1}{2}\overrightarrow{BC} + \overrightarrow{OB} = \frac{1}{2}\left( \overrightarrow{OC} - \overrightarrow{OB} \right) + \overrightarrow{OB} = \frac{1}{2}\left( \overrightarrow{OC} + \overrightarrow{OB} \right)$

于是

$\overrightarrow{AO} = 2\overrightarrow{OD}$

这样，$\overrightarrow{AO}$与$\overrightarrow{OD}$共线，即$AD$是$\bigtriangleup ABC$的$BC$边上的中线，且过$BE\text{，}CF$的交点$O$，所以结论成立。

${\overrightarrow{GA} + \overrightarrow{GB} + \overrightarrow{GC} = \frac{2}{3}\left( \overrightarrow{DA} + \overrightarrow{EB} + \overrightarrow{FC} \right) }{= - \frac{2}{3}\left( \overrightarrow{AD} + \overrightarrow{BE} + \overrightarrow{CF} \right) }{= - \frac{2}{3}\left\lbrack \frac{1}{2}\left( \overrightarrow{AB} + \overrightarrow{AC} \right) + \frac{1}{2}\left( \overrightarrow{BA} + \overrightarrow{BC} \right) + \frac{1}{2}\left( \overrightarrow{CA} + \overrightarrow{CB} \right) \right\rbrack = \mathbf{0}}$

$S_{\bigtriangleup GAB} = \frac{2}{3}S_{\bigtriangleup ABD} = \frac{1}{3}S_{\bigtriangleup ANC}\text{，其余同理}$

$\overrightarrow{PG} = \overrightarrow{PA} + \overrightarrow{AG} = \overrightarrow{PB} + \overrightarrow{BG} = \overrightarrow{PC} + \overrightarrow{CG}$

$\Rightarrow 3\overrightarrow{PG} = \overrightarrow{PA} + \overrightarrow{AG} + \overrightarrow{PB} + \overrightarrow{BG} + \overrightarrow{PC} + \overrightarrow{CG} = \overrightarrow{PA} + \overrightarrow{PB} + \overrightarrow{PC} + \mathbf{0}$

$\Rightarrow \overrightarrow{PG} = \frac{1}{3}\left( \overrightarrow{PA} + \overrightarrow{PB} + \overrightarrow{PC} \right)$

$\text{当}P\text{为坐标原点}O\text{时，得到}\overrightarrow{OG} = \frac{1}{3}\left( \overrightarrow{OA} + \overrightarrow{OB} + \overrightarrow{OC} \right)\text{，即}G\left( \frac{x_{1} + x_{2} + x_{3}}{3}\text{，}\frac{y_{1} + y_{2} + y_{3}}{3} \right)$

奔驰定理

设$\overrightarrow{PA'} = x\overrightarrow{PA}\text{，}\overrightarrow{PB'} = y\overrightarrow{PB}\text{，}\overrightarrow{PC'} = z\overrightarrow{PC}\text{，则}P\text{是} \bigtriangleup A'B'C'\text{的重心，得}$

$S_{\bigtriangleup PBC}\ :S_{\bigtriangleup PAC}\ :S_{\bigtriangleup PAB} = \frac{1}{yz}S_{\bigtriangleup PB'C'}\ :\frac{1}{xz}S_{\bigtriangleup PA'C'}\ :\frac{1}{xy}S_{\bigtriangleup PA'B'} = x\ :y\ :z$

三角形高线垂心相关结论

三条高线交于一点

${\overrightarrow{AH} \cdot \overrightarrow{BC} = \overrightarrow{AH} \cdot \left( \overrightarrow{BA} + \overrightarrow{AC} \right) }{= \overrightarrow{AH} \cdot \overrightarrow{BA} + \overrightarrow{AH} \cdot \overrightarrow{AC} }{= \left( \overrightarrow{AC} + \overrightarrow{CH} \right) \cdot \overrightarrow{BA} + \left( \overrightarrow{AB} + \overrightarrow{BH} \right) \cdot \overrightarrow{AC} }{= \overrightarrow{AC} \cdot \overrightarrow{BA} + 0 + \overrightarrow{AB} \cdot \overrightarrow{AC} + 0 = 0}$

结论左

$\overrightarrow{HA} \cdot \overrightarrow{HB} - \overrightarrow{HA} \cdot \overrightarrow{HC} = \overrightarrow{HA} \cdot \left( \overrightarrow{HB} - \overrightarrow{HC} \right) = \overrightarrow{HA} \cdot \overrightarrow{CB} = 0 \Rightarrow \overrightarrow{HA} \cdot \overrightarrow{HB} = \overrightarrow{HA} \cdot \overrightarrow{HC}\text{，其余同理}$

结论右

由奔驰定理，要证

$\tan A \cdot \overrightarrow{HA} + \tan B \cdot \overrightarrow{HB} + \tan C \cdot \overrightarrow{HC} = \mathbf{0}$

即证

$S_{\bigtriangleup HBC}:S_{\bigtriangleup HAC}:S_{\bigtriangleup HAB} = \tan A:\tan B:\tan C$

$S_{\bigtriangleup HAC}:S_{\bigtriangleup HAB} = |BD|:|CD| = \frac{|BD|}{|AD|}:\frac{|CD|}{|AD|} = \frac{1}{\tan B}:\frac{1}{\tan C} = \tan C:\tan B\text{，其余同理}$

三角形垂直平分线外心相关结论

左结论

由三点共圆，易得。

右结论

由奔驰定理，即证

$S_{\bigtriangleup OBC}:S_{\bigtriangleup OAC}:S_{\bigtriangleup OAB} = \sin{2A}:\sin{2B}:\sin{2C}$

由“同弧所对圆周角是圆心角的一半”，得

${S_{\bigtriangleup OBC}:S_{\bigtriangleup OAC}:S_{\bigtriangleup OAB} = \frac{1}{2}|OB||OC|\sin{\angle BOC}:\frac{1}{2}|OA||OC|\sin{\angle AOC}:\frac{1}{2}|OA||OB|\sin{\angle AOB} }{= \sin{2A}:\sin{2B}:\sin{2C}}$

三角形角平分线内心相关结论

左结论

由奔驰定理，即证

$S_{\bigtriangleup MBC}:S_{\bigtriangleup MAC}:S_{\bigtriangleup MAB} = a:b:c$

由内切圆，易得。

右结论

$\text{由三线合一，}\left( \frac{\overrightarrow{AB}}{|AB|} - \frac{\overrightarrow{AC}}{|AC|} \right)\text{表示与}A\text{的角平分线垂直的向量，其余同理。}$

其它

左结论

复数

三角乘法与除法

${z_{1}z_{2} = r_{1}\left( \cos\theta_{1} + i\sin\theta_{1} \right) \cdot r_{2}\left( \cos\theta_{2} + i\sin\theta_{2} \right) }{= r_{1}r_{2}\left( \cos\theta_{1} + i\sin\theta_{2} \right)\left( \cos\theta_{2} + i\sin\theta_{2} \right) }{= r_{1}r_{2}\left\lbrack \left( \cos\theta_{1}\cos\theta_{2} - \sin\theta_{1}\sin\theta_{2} \right) + i\left( \sin\theta_{1}\cos\theta_{2} + \cos\theta_{1}\sin\theta_{2} \right) \right\rbrack }{= r_{1}r_{2}\left\lbrack \cos\left( \theta_{1} + \theta_{2} \right) + i\sin\left( \theta_{1} + \theta_{2} \right) \right\rbrack}$

${\frac{z_{1}}{z_{2}} = \frac{r_{1}\left( \cos\theta_{1} + i\sin\theta_{1} \right)}{r_{2}\left( \cos\theta_{2} + i\sin\theta_{2} \right)} }{= \frac{r_{1}}{r_{2}} \cdot \frac{\left( \cos\theta_{1}\cos\theta_{2} + \sin\theta_{1}\sin\theta_{2} \right) + (\sin\theta_{1}\cos\theta_{2} - \cos\theta_{1}\sin\theta_{2})i}{\cos^{2}\theta_{2} + \sin^{2}\theta_{2}} }{= \frac{r_{1}}{r_{2}}\left\lbrack \cos\left( \theta_{1} - \theta_{2} \right) + i\sin\left( \theta_{1} - \theta_{2} \right) \right\rbrack}$

棱台的体积公式

设截得棱台的棱锥的体积为$V$，去掉的棱锥的体积为$V'$、高为$h'$，则$PO' = h'$，于是

$V' = \frac{1}{3}S'h'\text{，}V = \frac{1}{3}S\left( h' + h \right)$

所以棱台的体积

$V_{\text{棱台}} = V - V' = \frac{1}{3}S\left( h' + h \right) - \frac{1}{3}S'h' = \frac{1}{3}\left\lbrack Sh + \left( S - S' \right)h' \right\rbrack$

由棱台的上、下底面平行，可以证明棱台的上、下底面相似，并且

$\frac{S'}{S} = \frac{h^{'2}}{\left( h' + h \right)^{2}}$

所以

$h' = \frac{\sqrt{S'}\ h}{\sqrt{S} - \sqrt{S'}}$

代入得

$V_{\text{棱台}} = \frac{1}{3}\left\lbrack Sh + \left( S - S' \right)h' \right\rbrack = \frac{1}{3}h\left\lbrack S + \left( S - S' \right)\frac{\sqrt{S'}}{\sqrt{S} - \sqrt{S'}} \right\rbrack = \frac{1}{3}h\left( S' + \sqrt{S'S} + S \right)$

数列

等差数列与等比数列的基本公式

等差数列

通项：由等差数列的定义归纳得到。

求和：由

$S_{n} = a_{1} + a_{2} + \cdots + a_{n - 1} + a_{n}$

$S_{n} = a_{n} + a_{n - 1} + \cdots + a_{2} + a_{1}$

两式相加，得

${2S_{n} = \left( a_{1} + a_{n} \right) + \left( a_{2} + a_{n - 1} \right) + \cdots + \left( a_{n - 1} + a_{2} \right) + \left( a_{n} + a_{1} \right) }{= \left( a_{1} + a_{n} \right) + \left( a_{1} + a_{n} \right) + \cdots + \left( a_{1} + a_{n} \right) + \left( a_{1} + a_{n} \right) }{= n\left( a_{1} + a_{n} \right)}$

所以

$S_{n} = \frac{a_{1} + a_{n}}{2} = \frac{1}{2}n\left\lbrack a_{1} + a_{1} + (n - 1)d \right\rbrack = na_{1} + \frac{n(n - 1)}{2}d = \frac{d}{2}n^{2} + \left( a_{1} - \frac{d}{2} \right)n$

等比数列

通项：由等比数列的定义归纳得到。

求和：由

> ${S_{n} = a_{1} + a_{2} + \cdots + a_{n} = a_{1} + qa_{1} + q^{2}a_{1} + \cdots + q^{n - 2}a_{1} + q^{n - 1}a_{1} }{qS_{n} = qa_{1} + q^{2}a_{1} + q^{3}a_{1} + \cdots + q^{n - 1}a_{1} + q^{n}a_{1}}$

两式相减，得

$S_{n} - qS_{n} = a_{1} - q^{n}a_{1} \Rightarrow S_{n} = \frac{a_{1} - qa_{n}}{1 - q} = \frac{a_{1}\left( 1 - q^{n} \right)}{1 - q} = \frac{a_{1}}{1 - q} - \frac{a_{1}}{1 - q}q^{n}$

$a_{n} = (an + b)q^{n - 1}$型数列

$a_{n} = (an + b)q^{n - 1}$

$S_{n} = (a + b)q^{0} + (2a + b)q^{1} + (3a + b)q^{2} + \cdots + \left( a(n - 1) + b \right)q^{n - 2} + (an + b)q^{n - 1}$

$qS_{n} = (a + b)q^{1} + (2a + b)q^{2} + (3a + b)q^{3} + \cdots + \left( a(n - 1) + b \right)q^{n - 1} + (an + b)q^{n}$

两式相减，得

> $(q - 1)S_{n}$

$= - aq^{1} - aq^{2} - \cdots - aq^{n - 1} - aq^{n} + (an + b)q^{n} - (a + b)$

$= - a\frac{q\left( 1 - q^{n - 1} \right)}{1 - q} + anq^{n} + bq^{n} - (a + b)$ $= anq^{n} + bq^{n} + \frac{aq}{q - 1} - \frac{aq^{n}}{q - 1} - (a + b)$ $= (q - 1)\frac{q^{n}}{q - 1}(an + b) - (q - 1)\frac{aq^{n}}{(q - 1)^{2}} + \frac{aq}{q - 1} - a - b$ $= (q - 1)\left\lbrack \frac{q^{n}}{q - 1}\left( an + b - \frac{a}{q - 1} \right) \right\rbrack + \frac{aq - a(q - 1) - b(q - 1)}{q - 1}$ $= (q - 1)\left\lbrack \frac{q^{n}}{q - 1}\left( an + b - \frac{a}{q - 1} \right) \right\rbrack - \frac{b(q - 1) - a}{q - 1}$

所以

$S_{n} = \frac{q^{n}}{q - 1}\left( an + b - \frac{a}{q - 1} \right) - \frac{b(q - 1) - a}{(q - 1)^{2}} = q^{n}\left( \frac{a}{q - 1}n + \frac{b - \frac{a}{q - 1}}{q - 1} \right) - \frac{b - \frac{a}{q - 1}}{q - 1} = (An + B)q^{n} - B$

斐波那契数列的通项公式

待定系数法构造等比数列

设常数$\alpha$，$\beta$满足

$a_{n} - \alpha a_{n - 1} = \beta\left( a_{n - 1} - \alpha a_{n - 2} \right)$

由递推式，得

$\left\{ \begin{array}{r} \alpha + \beta = 1\  \\ \alpha \cdot \beta = - 1 \end{array} \right.\$

解方程，得

$\alpha \text{，}\beta = \frac{1 \pm \sqrt{5}}{2}$

代入，得

$a_{n} - \frac{1 + \sqrt{5}}{2}a_{n - 1} = \frac{1 - \sqrt{5}}{2}\left( a_{n - 1} - \frac{1 + \sqrt{5}}{2}a_{n - 2} \right)$

$a_{n} - \frac{1 - \sqrt{5}}{2}a_{n - 1} = \frac{1 + \sqrt{5}}{2}\left( a_{n - 1} - \frac{1 - \sqrt{5}}{2}a_{n - 2} \right)$

$\text{发现数列}\left\{ a_{n} - \frac{1 + \sqrt{5}}{2}a_{n - 1} \right\} \text{和}\left\{ a_{n} - \frac{1 - \sqrt{5}}{2}a_{n - 1} \right\} \text{均为等比数列，其通项为}$

$a_{n} - \frac{1 - \sqrt{5}}{2}a_{n - 1} = \left( \frac{1 + \sqrt{5}}{2} \right)^{n - 2}\left( a_{2} - \frac{1 - \sqrt{5}}{2}a_{1} \right) = \frac{1 + \sqrt{5}}{2}\left( \frac{1 + \sqrt{5}}{2} \right)^{n - 2}$

$a_{n} - \frac{1 + \sqrt{5}}{2}a_{n - 1} = \left( \frac{1 - \sqrt{5}}{2} \right)^{n - 2}\left( a_{2} - \frac{1 + \sqrt{5}}{2}a_{1} \right) = \frac{1 - \sqrt{5}}{2}\left( \frac{1 - \sqrt{5}}{2} \right)^{n - 2}$

把这两个数列看作关于$a_{n}$和$a_{n - 1}$的两个二元一次方程，消去$a_{n - 1}$，即得$\left\{ a_{n} \right\}$的通项公式。

~~第一步中是否存在常数~~$\alpha$~~，~~$\beta$~~满足~~$a_{n} - \alpha a_{n - 1} = \beta\left( a_{n - 1} - \alpha a_{n - 2} \right)$~~是不确定的。~~

运用泰勒公式

两条直线的一条对称轴

设$l_{1}\text{，}l_{2}$的法向量分别为$\left( A_{1}\text{，}B_{1} \right)\text{，}\left( A_{2}\text{，}B_{2} \right)$，则两者的单位向量为

$\left( \frac{A_{1}}{\sqrt{A_{1}^{2} + B_{1}^{2}}}\text{，}\frac{B_{1}}{\sqrt{A_{1}^{2} + B_{1}^{2}}} \right)\text{，}\left( \frac{A_{2}}{\sqrt{A_{2}^{2} + B_{2}^{2}}}\text{，}\frac{B_{2}}{\sqrt{A_{2}^{2} + B_{2}^{2}}} \right)$

得到对称直线的法向量（$\pm$同时取正或同时取负）

$\left( \frac{A_{1}}{\sqrt{A_{1}^{2} + B_{1}^{2}}} \pm \frac{A_{2}}{\sqrt{A_{2}^{2} + B_{2}^{2}}}\text{，}\frac{B_{1}}{\sqrt{A_{1}^{2} + B_{1}^{2}}} \pm \frac{B_{2}}{\sqrt{A_{2}^{2} + B_{2}^{2}}} \right)$

分母有理化，得

$\left( \sqrt{A_{2}^{2} + B_{2}^{2}}A_{1} \pm \sqrt{A_{1}^{2} + B_{1}^{2}}A_{2}\text{，}\sqrt{A_{2}^{2} + B_{2}^{2}}B_{1} \pm \sqrt{A_{1}^{2} + B_{1}^{2}}B_{2} \right)$

得到对称直线的方程

$\left( \sqrt{A_{2}^{2} + B_{2}^{2}}A_{1} \pm \sqrt{A_{1}^{2} + B_{1}^{2}}A_{2} \right)x + \left( \sqrt{A_{2}^{2} + B_{2}^{2}}B_{1} \pm \sqrt{A_{1}^{2} + B_{1}^{2}}B_{2} \right)y + C' = 0$

整理，得

$\sqrt{A_{2}^{2} + B_{2}^{2}}\left( A_{1}x + B_{1}y \right) \pm \sqrt{A_{1}^{2} + B_{1}^{2}}\left( A_{2}x + B_{2}y \right) + C' = 0$

对于相交直线的对称轴，其与这两条直线共点，满足共点线系的要求，于是对称直线还可表示为

$\lambda\left( A_{1}x + B_{1}y + C_{1} \right) \pm \mu\left( A_{2}x + B_{2}y + C_{2} \right) = 0$

发现两式有相同点，所以有

$C' = \sqrt{A_{2}^{2} + B_{2}^{2}}C_{1} \pm \sqrt{A_{1}^{2} + B_{1}^{2}}C_{2}$

得到方程

$\sqrt{A_{2}^{2} + B_{2}^{2}}\left( A_{1}x + B_{1}y + C_{2} \right) \pm \sqrt{A_{1}^{2} + B_{1}^{2}}\left( A_{2}x + B_{2}y + C_{2} \right) = 0$

阿氏圆

$\sqrt{\left( x - x_{1} \right)^{2} + \left( y - y_{1} \right)^{2}} = \lambda\sqrt{\left( x - x_{2} \right)^{2} + \left( y - y_{2} \right)^{2}}$

$\Rightarrow \left( x - x_{1} \right)^{2} + \left( y - y_{1} \right)^{2} = \lambda^{2}\left\lbrack \left( x - x_{2} \right)^{2} + \left( y - y_{2} \right)^{2} \right\rbrack$（平方）

$\Rightarrow x^{2} - 2x_{1}x + x_{1}^{2} + y^{2} + 2y_{1}y + y_{1}^{2} = \lambda^{2}\left( x^{2} - 2x_{2}x + x_{2}^{2} + y^{2} + 2y_{2}y + y_{2}^{2} \right)$（展开）

$\Rightarrow \left( 1 - \lambda^{2} \right)x^{2} + \left( 1 - \lambda^{2} \right)y^{2} + 2\left( \lambda^{2}x_{2} - x_{1} \right)x + 2\left( \lambda^{2}y_{2} - y_{1} \right)y = \lambda^{2}x_{2}^{2} + \lambda^{2}y_{2}^{2} - x_{1}^{2} - y_{1}^{2}$（按次数整理）

$\Rightarrow \left( 1 - \lambda^{2} \right)\left( x^{2} + \frac{2\left( \lambda^{2}x_{2} - x_{1} \right)}{2\left( 1 - \lambda^{2} \right)} \right)^{2} + \left( 1 - \lambda^{2} \right)\left( y^{2} + \frac{2\left( \lambda^{2}y_{2} - y_{1} \right)}{2\left( 1 - \lambda^{2} \right)} \right)^{2}\text{（对}x\text{和}y\text{配方）}$

$= \lambda^{2}x_{2}^{2} + \lambda^{2}y_{2}^{2} - x_{1}^{2} - y_{1}^{2} + \frac{\left\lbrack 2\left( \lambda^{2}x_{2} - x_{1} \right) \right\rbrack^{2} + \left\lbrack 2\left( \lambda^{2}y_{2} - y_{1} \right) \right\rbrack^{2}}{4\left( 1 - \lambda^{2} \right)}\text{（这项是因配方而产生的）}$

$\Rightarrow \left( 1 - \lambda^{2} \right)\left\lbrack \left( x^{2} + \frac{\lambda^{2}x_{2} - x_{1}}{1 - \lambda^{2}} \right)^{2} + \left( y^{2} + \frac{\lambda^{2}y_{2} - y_{1}}{1 - \lambda^{2}} \right)^{2} \right\rbrack$（提取公因式$\left( 1 - \lambda^{2} \right)$）

$= \frac{\left( \lambda^{2}x_{2}^{2} + \lambda^{2}y_{2}^{2} - x_{1}^{2} - y_{1}^{2} \right)\left( 1 - \lambda^{2} \right) + \left( \lambda^{2}x_{2} - x_{1} \right)^{2} + \left( \lambda^{2}y_{2} - y_{1} \right)^{2}}{1 - \lambda^{2}}\text{（准备对等号右边通分整理）}$

$\Rightarrow \left( x^{2} + \frac{\lambda^{2}x_{2} - x_{1}}{1 - \lambda^{2}} \right)^{2} + \left( y^{2} + \frac{\lambda^{2}y_{2} - y_{1}}{1 - \lambda^{2}} \right)^{2}$（等号右边全部展开，消去加黑标框的项）

$= \frac{\lambda^{2}x_{2}^{2} + \lambda^{2}y_{2}^{2}\mathbf{-}\mathbf{x}_{\mathbf{1}}^{\mathbf{2}}\mathbf{-}\mathbf{y}_{\mathbf{1}}^{\mathbf{2}}\mathbf{-}\mathbf{\lambda}^{\mathbf{4}}\mathbf{x}_{\mathbf{2}}^{\mathbf{2}}\mathbf{-}\mathbf{\lambda}^{\mathbf{4}}\mathbf{y}_{\mathbf{2}}^{\mathbf{2}} + \lambda^{2}x_{1}^{2} + \lambda^{2}y_{1}^{2}\mathbf{+}\mathbf{\lambda}^{\mathbf{4}}\mathbf{x}_{\mathbf{2}}^{\mathbf{2}} - 2\lambda^{2}x_{1}x_{2}\mathbf{+}\mathbf{x}_{\mathbf{1}}^{\mathbf{2}}\mathbf{+}\mathbf{\lambda}^{\mathbf{4}}\mathbf{y}_{\mathbf{2}}^{\mathbf{2}} - 2\lambda^{2}y_{1}y_{2}\mathbf{+}\mathbf{y}_{\mathbf{1}}^{\mathbf{2}}}{\left( 1 - \lambda^{2} \right)^{2}}$

$= \frac{\lambda^{2}}{\left( 1 - \lambda^{2} \right)^{2}}\left( x_{2}^{2} + y_{2}^{2} + x_{1}^{2} + y_{1}^{2} - 2x_{1}x_{2} - 2y_{1}y_{2} \right)$（提出$\lambda^{2}$后发现可以配方）

$= \left( \frac{\lambda}{1 - \lambda^{2}} \right)^{2}\left\lbrack \left( x_{1} - x_{2} \right)^{2} + \left( y_{1} - y_{2} \right)^{2} \right\rbrack = \left( \frac{\lambda}{1 - \lambda^{2}}\sqrt{\left( x_{1} - x_{2} \right)^{2} + \left( y_{1} - y_{2} \right)^{2}} \right)^{2}$（最终结果）

弦中点

如图，设$C(x_{0}\text{，}y_{0})M(x_{1}\text{，}y_{1})N(x_{2}\text{，}y_{2})$，联立

$\left\{ \begin{array}{r} \frac{x_{1}^{2}}{m} + \frac{y_{1}^{2}}{n} = 1 \\ \frac{x_{2}^{2}}{m} + \frac{y_{2}^{2}}{n} = 1 \end{array} \right.\ \text{，得}$

$\frac{x_{1}^{2}}{m} + \frac{y_{1}^{2}}{n} = \frac{x_{2}^{2}}{m} + \frac{y_{2}^{2}}{n} \Rightarrow \frac{x_{1}^{2} - x_{2}^{2}}{m} = \frac{y_{2}^{2} - y_{1}^{2}}{n} \Rightarrow \frac{2x_{0}\left( x_{1} - x_{2} \right)}{m} = - \frac{2y_{0}\left( y_{1} - y_{2} \right)}{n} \Rightarrow \frac{y_{0}\left( y_{1} - y_{2} \right)}{x_{0}\left( x_{1} - x_{2} \right)} = - \frac{n}{m}$

其余同理

椭圆/双曲线的第三定义

取PE的中点M，连接OM，根据中位线平行和弦中点，即得。

圆锥曲线的第二定义（欲证明点P的轨迹为相应的圆锥曲线）

$\frac{|PF|}{|PE|} = \frac{\sqrt{(x - c)^{2} + y^{2}}}{\left| x - \frac{a^{2}}{c} \right|} = \frac{c}{a} \Rightarrow \sqrt{(x - c)^{2} + y^{2}} = \left| \frac{cx}{a} - a \right| \Rightarrow (x - c)^{2} + y^{2} = \frac{c^{2}}{a^{2}}x^{2} + a^{2} - 2cx \Rightarrow \left( a^{2} - c^{2} \right)x^{2} + a^{2}y^{2} = a^{2}\left( a^{2} - c^{2} \right)$

当$a^{2} > c^{2}$时，得到椭圆方程（$C_{1}$）；当$a^{2} < c^{2}$时，得到双曲线方程（$C_{1}$）；当$a^{2} = c^{2}$时，得到抛物线方程

对于抛物线方程（$C_{1}$），可以

$\frac{|PF|}{|PE|} = \frac{\sqrt{\left( x - \frac{p}{2} \right)^{2} + y^{2}}}{\left| x + \frac{p}{2} \right|} = 1 \Rightarrow x^{2} - px + \frac{p^{2}}{4} + y^{2} = x^{2} + px + \frac{p^{2}}{4} \Rightarrow y^{2} = 2px$

椭圆的特有性质

设$\angle P$在$P$为上顶点时为$\alpha$，其余为$\theta$，则有

$\alpha > \theta \Rightarrow \frac{\alpha}{2} > \frac{\theta}{2} \Rightarrow \sin\frac{\alpha}{2} > \sin\frac{\theta}{2} \Rightarrow \sin\frac{\alpha}{2} = \frac{c}{a} > \sin\frac{\theta}{2} \Rightarrow e > \sin\frac{\theta}{2}$

$\text{由}S_{\bigtriangleup PF_{1}F_{2}} = b^{2} \cdot \tan\frac{\theta}{2}\text{，当}\theta \text{越来越大时，} \bigtriangleup PF_{1}F_{2}\text{的底} \times \text{高越来越大，即点}P\text{越来越靠近}y\text{轴}$

$\text{由第三定义，得}k_{PA} \cdot k_{PB} = - \frac{b^{2}}{a^{2}} \Rightarrow \tan{\angle PAB} \cdot \tan{\angle PBA} = \frac{b^{2}}{a^{2}}$

$\tan{\angle APB} = - \tan(\angle PAB + \angle PBA) = - \frac{\tan{\angle PAB} + \tan{\angle PBA}}{1 - \tan{\angle PAB} \cdot \tan{\angle PBA}} = - \frac{\tan{\angle PAB} + \tan{\angle PBA}}{1 - \frac{b^{2}}{a^{2}}} = - \frac{a^{2}}{c^{2}}\left( \tan{\angle PAB} + \tan{\angle PBA} \right)$

双曲线的特有性质

由渐近线定义，易得

$\text{设}A\left( x_{1}\text{，}\frac{b}{a}x_{1} \right)\text{，}B\left( x_{2}\text{，} - \frac{b}{a}x_{2} \right) \Rightarrow D\left( \frac{x_{1} + x_{2}}{2},\frac{y_{1} + y_{2}}{2} \right) \Rightarrow k_{AB} = \frac{b}{a}\frac{x_{1} + x_{2}}{x_{1} - x_{2}}\text{，}k_{OD} = \frac{b}{a}\frac{x_{1} + x_{2}}{x_{1} - x_{2}} \Rightarrow k_{AB} \cdot k_{OD} = \frac{b^{2}}{a^{2}}$

点$P(x_{0}\text{，}y_{0})$在双曲线$C_{1}$上，有$\frac{x_{0}^{2}}{a^{2}} - \frac{y_{0}^{2}}{b^{2}} = 1$，即$b^{2}x_{0}^{2} - a^{2}y_{0}^{2} = a^{2}b^{2}$

渐近线方程为$y = \pm \frac{b}{a}x$，即$bx - ay = 0$和$bx + ay = 0$

设斜率大于0的渐近线倾斜角为$\theta$，则$\cos{\angle MPN} = \cos(\pi - 2\theta) = - \cos{2\theta}\text{，}\sin{\angle MPN} = \sin{2\theta}$

$\cos{2\theta} = \frac{1 - \tan^{2}\theta}{1 + \tan^{2}\theta} = \frac{1 - \frac{b^{2}}{a^{2}}}{1 + \frac{b^{2}}{a^{2}}} = \frac{a^{2} - b^{2}}{a^{2} + b^{2}} = \frac{a^{2} - b^{2}}{c^{2}}\text{，}\sin{2\theta} = \frac{2\tan\theta}{1 + \tan^{2}\theta} = \frac{2\frac{b}{a}}{1 + \frac{b^{2}}{a^{2}}} = \frac{2ab}{a^{2} + b^{2}} = \frac{2ab}{c^{2}}$

1.垂线

$|PM| \cdot |PN| = \frac{bx_{0} - ay_{0}}{\sqrt{a^{2} + b^{2}}} \cdot \frac{bx_{0} + ay_{0}}{\sqrt{a^{2} + b^{2}}} = \frac{b^{2}x_{0}^{2} - a^{2}y_{0}^{2}}{a^{2} + b^{2}} = \frac{a^{2}b^{2}}{c^{2}}$

$\overset{\rightarrow}{PM} \cdot \overset{\rightarrow}{PN} = |PM||PN|\cos{\angle MPN} = - \frac{a^{2}b^{2}}{c^{2}} \cdot \frac{a^{2} - b^{2}}{c^{2}} = \frac{a^{2}b^{2}}{c^{4}}(b^{2} - a^{2})$

$S_{\bigtriangleup PMN} = \frac{1}{2}|PM||PN|\sin{\angle MPN} = \frac{1}{2} \cdot \frac{a^{2}b^{2}}{c^{2}} \cdot \frac{2ab}{c^{2}} = \frac{a^{3}b^{3}}{c^{4}}$

2.平行线

$\left\{ \begin{array}{r} y - y_{0} = \pm \frac{b}{a}\left( x - x_{0} \right) \\ y = \pm \frac{b}{a}x\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$联立，得$M\left( \frac{a}{2b}\left( \frac{b}{a}x_{0} + y_{0} \right)\text{，}\frac{\frac{b}{a}x_{0} + y_{0}}{2} \right)\text{，}N\left( \frac{a}{2b}\left( \frac{b}{a}x_{0} - y_{0} \right)\text{，} - \frac{\frac{b}{a}x_{0} - y_{0}}{2} \right)$

$|MN| = \sqrt{\left( \frac{a}{b}y_{0} \right)^{2} + \left( \frac{b}{a}x_{0} \right)^{2}} = \sqrt{\frac{\left( a^{2} + b^{2} \right)y_{0}^{2} + b^{4}}{b^{2}}}$

$\overset{\rightarrow}{PM} \cdot \overset{\rightarrow}{PN} = \left( \frac{|PO|}{2} \right)^{2} - \left( \frac{|MN|}{2} \right)^{2} = \frac{1}{4}\left( x_{0}^{2} + y_{0}^{2} - \frac{\left( a^{2} + b^{2} \right)y_{0}^{2} + b^{4}}{b^{2}} \right) = \frac{b^{2}\left( a^{2} - b^{2} \right)}{4b^{2}} = \frac{a^{2} - b^{2}}{4}$

$|PM| \cdot |PN| = \frac{\overset{\rightarrow}{PM} \cdot \overset{\rightarrow}{PN}}{\cos{\angle MPN}} = \frac{\frac{a^{2} - b^{2}}{4}}{- \frac{b^{2} - a^{2}}{c^{2}}} = \frac{c^{2}}{4}$

$S_{\bigtriangleup PMN} = \frac{1}{2}|PM||PN|\sin{\angle MPN} = \frac{1}{2} \cdot \frac{c^{2}}{4} \cdot \frac{2ab}{c^{2}} = \frac{ab}{4}$

![](/images/hs/hs-a12/img01.png)3.切线

$\left\{ \begin{array}{r} \frac{x_{0}x}{a^{2}} - \frac{y_{0}y}{b^{2}} = 1 \\ y = \pm \frac{b}{a}x\ \ \ \ \ \ \ \end{array} \right.\ \text{联立，得}M\left( \frac{ba^{2}}{bx_{0} - ay_{0}}\text{，}\frac{ab^{2}}{bx_{0} - ay_{0}} \right)\text{，}N\left( \frac{ba^{2}}{bx_{0} + ay_{0}}\text{，}\frac{ab^{2}}{bx_{0} + ay_{0}} \right)$

$|OM| \cdot |ON| = \sqrt{\left( \frac{ba^{2}}{bx_{0} - ay_{0}} \right)^{2} + \left( \frac{ab^{2}}{bx_{0} - ay_{0}} \right)^{2}} \cdot \sqrt{\left( \frac{ba^{2}}{bx_{0} + ay_{0}} \right)^{2} + \left( \frac{ab^{2}}{bx_{0} + ay_{0}} \right)^{2}} = \frac{ab\sqrt{a^{2} + b^{2}}}{bx_{0} - ay_{0}} \cdot \frac{ab\sqrt{a^{2} + b^{2}}}{bx_{0} + ay_{0}} = \frac{a^{2}b^{2}\left( a^{2} + b^{2} \right)}{a^{2}b^{2}} = c^{2}$

$\overset{\rightarrow}{OM} \cdot \overset{\rightarrow}{ON} = |OM||ON|\cos{2\theta} = c^{2} \cdot \frac{a^{2} - b^{2}}{c^{2}} = a^{2} - b^{2}$

$S_{\bigtriangleup OMN} = \frac{1}{2}|OM||ON|\sin{2\theta} = \frac{1}{2}c^{2} \cdot \frac{2ab}{c^{2}} = ab$

抛物线的特有性质

1.交坐标轴的弦

把抛物线与直线联立，易得

$2.\text{设}A\left( x_{1}y_{1} \right)\text{，}B\left( x_{2}y_{2} \right)\text{，}l_{AB}:x = ty + \frac{p}{2}$

$A'\left( - \frac{p}{2}\text{，}y_{1} \right)\text{，}B'\left( - \frac{p}{2}\text{，}y_{2} \right)$

直线方程与抛物线方程联立，得

$x_{1} + x_{2} = 2pt^{2} + p\text{，}x_{1} \cdot x_{2} = \frac{p^{2}}{4}$

$y_{1} + y_{2} = 2pt\text{，}y_{1} \cdot y_{2} = - p^{2}$

$\left| y_{1} - y_{2} \right| = 2p\sqrt{t^{2} + 1}\text{，}|AB| = 2p\left( t^{2} + 1 \right)$

所以

$C\left( pt^{2} + \frac{p}{2}\text{，}pt \right)\text{，}C'\left( - \frac{p}{2}\text{，}pt \right)$

$\left| CC' \right| = pt^{2} + p = p\left( t^{2} + 1 \right) = \frac{1}{2}|AB|$

即得到$\angle AC'B = 90{^\circ}$，同时也得到以焦点弦为半径的圆与准线相切。

此结论也可以由抛物线定义和梯形中位线得到。

$\left| C'F \right| = \sqrt{p^{2} + (pt)^{2}} = p\sqrt{t^{2} + 1} = \frac{1}{2}\left| y_{1} - y_{2} \right|\text{，即得到}\angle AFB = 90{^\circ}$

$\text{对于}AF\text{，其中点坐标为}\left( \frac{1}{2}\left( x_{1} + \frac{p}{2} \right)\text{，}\frac{y_{1}}{2} \right)\text{，对应}y\text{轴上的点设为}D\left( 0\text{，}\frac{y_{1}}{2} \right)\text{，则}$

$\overrightarrow{DF} \cdot \overrightarrow{DA} = \frac{1}{2}px_{1} - \frac{y_{1}^{2}}{4} = - 4\left( y^{2} - 2px_{1} \right) = 0\text{，即以焦半径为直径的圆与}y\text{轴相切，对}FB\text{同理}$

由抛物线倾斜角式的焦半径公式，得到

$|AB| = \frac{p}{1 - \cos\alpha} + \frac{p}{1 + \cos\alpha} = p\frac{1 - \cos\alpha + 1 + \cos\alpha}{\left( 1 - \cos\alpha \right)\left( 1 + \cos\alpha \right)} = \frac{2p}{1 - \cos^{2}\alpha} = \frac{2p}{\sin^{2}\alpha}$

$\text{由}\left| y_{1} - y_{2} \right| = |AB|\sin\alpha = \frac{2p}{\sin\alpha}\text{，得}$

$S_{\bigtriangleup OAB} = \frac{1}{2}|OF|\left| y_{1} - y_{2} \right| = \frac{1}{2} \cdot \frac{p}{2} \cdot \frac{2p}{\sin\alpha} = \frac{p^{2}}{2\sin\alpha}$

同时有

$\left| A'B' \right|^{2} = \left| y_{1} - y_{2} \right|^{2} = \left( \frac{2p}{\sin\alpha} \right)^{2} = 4\frac{p}{1 - \cos\alpha}\frac{p}{1 + \cos\alpha} = 4|AF||BF|$

$k_{AB} = \frac{y_{1} - y_{2}}{x_{1} - x_{2}} = \frac{y_{1} - y_{2}}{\frac{y_{1}^{2}}{2p} - \frac{y_{2}^{2}}{2p}} = 2p\frac{y_{1} - y_{2}}{\left( y_{1} + y_{2} \right)\left( y_{1} - y_{2} \right)} = \frac{2p}{y_{1} + y_{2}} = \frac{p}{y_{3}}$

对于$\angle AMF = \angle BMF$，由斜率相等得到

$\frac{y_{1}}{x_{1} + \frac{p}{2}} + \frac{y_{2}}{x_{2} + \frac{p}{2}} = 0 \Rightarrow \frac{y_{1}}{\frac{y_{1}^{2}}{2p} + \frac{p}{2}} + \frac{y_{2}}{\frac{y_{2}^{2}}{2p} + \frac{p}{2}} = \frac{2py_{1}}{y_{1}^{2} + p^{2}} + \frac{2py_{2}}{y_{2}^{2} + p^{2}} = \frac{1}{y_{1} + \frac{p^{2}}{y_{1}}} + \frac{1}{y_{2} + \frac{p^{2}}{y_{2}}} = y_{1} + y_{2} + \frac{p^{2}}{y_{1}} + \frac{p^{2}}{y_{2}} = 0$

$\text{即证}y_{1} + y_{2} + p^{2}\frac{y_{1} + y_{2}}{y_{1}y_{2}} = 0\text{，带入联立得到的结果即证}$

焦半径

椭圆与双曲线

坐标形式

> 由椭圆/双曲线的准线方程，即得。

倾斜角形式

> 对于$C_{1}$，由椭圆/双曲线的第二定义，有
>
> $\left| PF_{1} \right| = e\left| PP' \right| = e\left\{ \left\lbrack - c - \left( - \frac{a^{2}}{c} \right) \right\rbrack + \left| AF_{1} \right|\cos\alpha \right\} = e \cdot \frac{b^{2}}{c} + e\left| AF_{1} \right|\cos\alpha \Rightarrow \left| AF_{1} \right| = \frac{b^{2}}{a - c\cos\alpha}$
>
> 其余同理
>
> 也可以做出焦点三角形，由余弦定理得到，更为简单。

焦点弦

$|PQ| = \left| PF_{1} \right| + \left| PF_{2} \right| = \frac{b^{2}}{a - c\cos\alpha} + \frac{b^{2}}{a + c\cos\alpha} = \frac{2ab^{2}}{a^{2} - c^{2}\cos^{2}\alpha}$

> 其余同理

抛物线

设抛物线的焦半径为$AF\ \ \left( y_{A} > 0 \right)$，焦半径所在直线的倾斜角为$\alpha$，点A到x轴的垂线的垂足为D，则

$|AF| = x_{A} + \frac{p}{2}\text{，}|FD| = x_{A} - \frac{p}{2}\text{，}|AD| = \sqrt{2px_{A}}\text{，}$

$\text{由}\cos\alpha = \frac{x_{A} - \frac{p}{2}}{x_{A} + \frac{p}{2}}\text{，得到}x_{A} = \frac{p}{2} \cdot \frac{1 + \cos\alpha}{1 - \cos\alpha}$

所以

$|AF| = \frac{p}{2} \cdot \frac{1 + \cos\alpha}{1 - \cos\alpha} + \frac{p}{2} = \frac{p}{2}\left( 1 + \frac{1 + \cos\alpha}{1 - \cos\alpha} \right) = \frac{p}{1 - \cos\alpha}$

> $y_{A} < 0$同理

焦点三角形

$\left| F_{1}F_{2} \right|^{2} = \left| PF_{1} \right|^{2} + \left| PF_{2} \right|^{2} - 2\left| PF_{1} \right|\left| PF_{2} \right|\cos\theta$

> $\Rightarrow 4c^{2} = \left( \left| PF_{1} \right| + \left| PF_{2} \right| \right)^{2} - 2\left| PF_{1} \right|\left| PF_{2} \right|\left( 1 + \cos\theta \right) = (2a)^{2} - 2\left| PF_{1} \right|\left| PF_{2} \right|\left( 1 + \cos\theta \right)$
>
> $\Rightarrow \left| PF_{1} \right|\left| PF_{2} \right| = \frac{4c^{2} - 4a^{2}}{2\left( 1 + \cos\theta \right)} = \frac{2b^{2}}{1 + \cos\theta}$

$\overrightarrow{PF_{1}} \cdot \overrightarrow{PF_{2}} = \left| PF_{1} \right|\left| PF_{2} \right|\cos\theta = \frac{2b^{2}}{1 + \cos\theta} \cdot \cos\theta$

$S_{\bigtriangleup PF_{1}F_{2}} = \frac{1}{2}\left| PF_{1} \right|\left| PF_{2} \right|\sin\theta = \frac{1}{2} \cdot \frac{2b^{2}}{1 + \cos\theta}\sin\theta = b^{2} \cdot \tan\frac{\theta}{2}(\text{半角公式})$

$\frac{\left| PF_{1} \right|}{\sin{\angle PF_{2}F_{1}}} = \frac{\left| PF_{2} \right|}{\sin{\angle PF_{1}F_{2}}} = \frac{\left| F_{1}F_{2} \right|}{\sin\theta}$

> $\Rightarrow \frac{\left| PF_{1} \right| + \left| PF_{2} \right|}{\sin{\angle PF_{2}F_{1}} + \sin{\angle PF_{1}F_{2}}} = \frac{2a}{\sin{\angle PF_{2}F_{1}} + \sin{\angle PF_{1}F_{2}}} = \frac{\left| F_{1}F_{2} \right|}{\sin\theta} = \frac{2c}{\sin\theta}$
>
> $\Rightarrow e = \frac{\sin\theta}{\sin{\angle PF_{2}F_{1}} + \sin{\angle PF_{1}F_{2}}}$

常用范围

$\left| PF_{1} \right| = a + ex_{0}\text{，}x \in \lbrack - a\text{，}a\rbrack$

$\left| PF_{1} \right|\left| PF_{2} \right| = \left( a + ex_{0} \right)\left( a - ex_{0} \right) = a^{2} - e^{2}x_{0}^{2}$

$\text{设}P\left( a\cos\theta \text{，}b\sin\theta \right)\text{，}|PO| = \sqrt{a^{2}\cos^{2}\theta + b^{2}\sin^{2}\theta} \Rightarrow |PO|^{2} = a^{2}\left( 1 - \sin^{2}\theta \right) + b^{2}\sin^{2}\theta = a^{2} + \left( b^{2} - a^{2} \right)\sin^{2}\theta = a^{2} - c^{2}\sin^{2}\theta\overset{\sin\theta \in \lbrack - 1\text{，}1\rbrack}{\Rightarrow}|PO|^{2} \in \left\lbrack a^{2} - c^{2}\text{，}a^{2} \right\rbrack$

$\overrightarrow{PF_{1}} \cdot \overrightarrow{PF_{2}} = |PO|^{2} - c^{2} \in \left\lbrack b^{2} - c^{2}\text{，}a^{2} - c^{2} \right\rbrack$

定点定值

3.证明见“其它”

4.。

5.

6.

$7.$概率

概率的其它关系

$P\left( (B + C) \middle| A \right) = \frac{P\left( (B + C)A \right)}{P(A)} = \frac{n\left( (B + C)A \right)}{n(A)} = \frac{n(AB) + n(AC)}{n(A)} = P\left( B \middle| A \right) + P\left( C \middle| A \right)$

$P\left( A|B \right) + P\left( \overline{A} \middle| B \right) = \frac{P(AB)}{P(B)} + \frac{P\left( \overline{A}B \right)}{P(B)} = \frac{n(AB) + n\left( \overline{A}B \right)}{n(B)}\left( = \frac{(A \cap B) \cup \left( \overline{A} \cap B \right)}{B} = \frac{B \cap (A \cup \overline{A})}{B} \right) = \frac{n(B)}{n(B)} = 1$

全概率公式

${P(B) = P(\Omega B) }{= P\left( \left( A_{1} + A_{2} + \cdots + A_{n} \right)B \right) }{= P\left( A_{1}B + A_{2}B + \cdots + A_{n}B \right) }{= P\left( A_{1} \right)P\left( B \middle| A_{1} \right) + P\left( A_{2} \right)P\left( B \middle| A_{2} \right) + \cdots + P\left( A_{n} \right)P\left( B \middle| A_{n} \right) }{= \sum_{i = 1}^{n}{P\left( A_{i} \right)P\left( B|A_{i} \right)}}$

离散型随机变量

$E(aX + b) = \sum_{i = 1}^{n}{\left( ax_{i} + b \right)p_{i}} = a\sum_{i = 1}^{n}{x_{i}p_{i}} + b\sum_{i = 1}^{n}p_{i} = aE(X) + b$

${D(X) = \sum_{i = 1}^{n}{\left( x_{i} - E(X) \right)^{2}p_{i}} = \sum_{i = 1}^{n}{\left( x_{i}^{2} - 2E(X)x_{i} + \left( E(X) \right)^{2} \right)p_{i}} }{= \sum_{i = 1}^{n}{x_{i}^{2}p_{i}} - 2E(X)\sum_{i = 1}^{n}{x_{i}p_{i}} + \left( E(X) \right)^{2}\sum_{i = 1}^{n}p_{i} }{= \sum_{i = 1}^{n}{x_{i}^{2}p_{i}} - 2\left( E(X) \right)^{2} + \left( E(X) \right)^{2} \times 1 }{= \sum_{i = 1}^{n}{x_{i}^{2}p_{i}} - \left( E(X) \right)^{2} = E\left( X^{2} \right) - \left( E(X) \right)^{2}}$

${D(aX + b) = \sum_{i = 1}^{n}{\left( ax_{i} + b - E(aX + b) \right)^{2}p_{i}} }{= \sum_{i = 1}^{n}{\left( ax_{i} + b - aE(X) + b \right)^{2}p_{i}} }{= a^{2}\sum_{i = 1}^{n}{\left( x_{i} - E(X) \right)^{2}p_{i}} = a^{2}D(X)}$

$E\left( X_{1} + X_{2} + \cdots + X_{m} \right) = \sum_{i = 1}^{n}{x_{1i}p_{1i} + x_{2i}p_{2i} + \cdots + x_{mi}p_{mi}}$

$= \sum_{i = 1}^{n}{x_{1i}p_{1i}} + \sum_{i = 1}^{n}{x_{2i}p_{2i}} + \cdots + \sum_{i = 1}^{n}{x_{mi}p_{mi}}$

$= E\left( X_{1} \right) + E\left( X_{2} \right) + \cdots + E\left( X_{m} \right)$

二项分布

均值

$E(X) = \sum_{k = 0}^{n}{kC_{n}^{k}p^{k}(1 - p)^{n - k}}$

> $= \sum_{k = 1}^{n}{kC_{n}^{k}p^{k}(1 - p)^{n - k}}$
>
> $\overset{kC_{n}^{k} = nC_{n - 1}^{k - 1}}{=}\sum_{k = 1}^{n}{nC_{n - 1}^{k - 1}p^{k}(1 - p)^{n - k}}$
>
> $= np\sum_{k = 1}^{n}{C_{n - 1}^{k - 1}p^{k - 1}(1 - p)^{n - 1 - (k - 1)}}$
>
> $= np(1 - p + p)^{n - 1} = np$

方差

$D(X) = E\left( X^{2} \right) - \left( E(X) \right)^{2}$

由

${E\left( X^{2} \right) = \sum_{k = 0}^{n}{k^{2}C_{n}^{k}p^{k}(1 - p)^{n - k}} }{= \sum_{k = 0}^{n}{k(k - 1)C_{n}^{k}p^{k}(1 - p)^{n - k}} + \sum_{k = 0}^{n}{kC_{n}^{k}p^{k}(1 - p)^{n - k}} }{= \sum_{k = 1}^{n}{(k - 1)\left( kC_{n}^{k} \right)p^{k}(1 - p)^{n - k}} + np }{= \sum_{k = 1}^{n}{(k - 1)\left( nC_{n - 1}^{k - 1} \right)p^{k}(1 - p)^{n - k}} + np }{= n\sum_{k = 1}^{n}{(k - 1)C_{n - 1}^{k - 1}p^{k}(1 - p)^{n - k}} + np }{= n\sum_{k = 2}^{n}{(n - 1)C_{n - 2}^{k - 2}p^{k}(1 - p)^{n - k}} + np }{= n(n - 1)p^{2}\sum_{k = 2}^{n}{C_{n - 2}^{k - 2}p^{k - 2}(1 - p)^{n - 2 - (k - 2)}} + np }{= n(n - 1)p^{2}(p + 1 - p)^{n - 2} + np }{= n(n - 1)p^{2} + np}$

所以

$D(X) = n(n - 1)p^{2} + np - (np)^{2} = np(1 - p)$

由

$\left\{ \begin{array}{r} P(X = k) \geq P(X = k - 1) \Rightarrow k \leq (n + 1)p\ \ \ \ \ \ \ \  \\ P(X = k) \geq P(X = k + 1) \Rightarrow k \geq (n + 1)p - 1 \end{array} \right.\$

得

$(n + 1)p - 1 \leq k \leq (n + 1)p$

超几何分布

均值

$E(X) = \sum_{k = m}^{r}\frac{C_{M}^{k}C_{N - M}^{n - k}}{C_{N}^{n}} = M\sum_{k = m}^{r}\frac{C_{M - 1}^{k - 1}C_{N - M}^{n - k}}{C_{N}^{n}} = \frac{M}{C_{N}^{n}}\sum_{k = m}^{r}{C_{M - 1}^{k - 1}C_{N - M}^{n - k}}\overset{\sum_{k = m}^{r}{C_{M - 1}^{k - 1}C_{N - M}^{n - k}} = C_{N - 1}^{n - 1}}{= =}M\frac{C_{N - 1}^{n - 1}}{C_{N}^{n}} = n\frac{M}{N} = np$

方差

统计

两层分层抽样的方差

${S_{z}^{2} = \frac{1}{m + n}\left\lbrack \sum_{i = 1}^{m}\left( \overline{z} - x_{i} \right)^{2} + \sum_{i = 1}^{n}\left( \overline{z} - y_{i} \right)^{2} \right\rbrack }{= \frac{1}{m + n}\left\lbrack \sum_{i = 1}^{m}\left( x_{i}^{2} - 2x_{i}\overline{z} + {\overline{z}}^{2} \right) + \sum_{i = 1}^{n}\left( y_{i}^{2} - 2y_{i}\overline{z} + {\overline{z}}^{2} \right) \right\rbrack }{= \frac{1}{m + n}\left\lbrack \left( \sum_{i = 1}^{m}x_{i}^{2} - 2m\overline{x}\overline{z} + m{\overline{z}}^{2} \right) + \left( \sum_{i = 1}^{n}y_{i}^{2} - 2n\overline{y}\overline{z} + n{\overline{z}}^{2} \right) \right\rbrack }{= \frac{1}{m + n}\left\lbrack m\left( \frac{1}{m}\sum_{i = 1}^{m}x_{i}^{2} - 2\overline{xz} + {\overline{z}}^{2} \right) + n\left( \frac{1}{n}\sum_{i = 1}^{n}y_{i}^{2} - 2\overline{y}\overline{z} + {\overline{z}}^{2} \right) \right\rbrack }{= \frac{1}{m + n}\left\lbrack m\left( s_{x}^{2} + {\overline{x}}^{2} - 2\overline{x}\overline{z} + {\overline{z}}^{2} \right) + n\left( s_{y}^{2} + {\overline{y}}^{2} - 2\overline{y}\overline{z} + {\overline{z}}^{2} \right) \right\rbrack }{= \frac{1}{m + n}\left\{ m\left\lbrack S_{x}^{2} + \left( \overline{x} - \overline{z} \right)^{2} \right\rbrack + n\left\lbrack S_{y}^{2} + \left( \overline{y} - \overline{z} \right)^{2} \right\rbrack \right\}}$

一元线性回归模型

$\text{定义二元函数}Q(a\text{，}b) = \sum_{i = 1}^{n}\left( y_{i} - bx_{i} - a \right)^{2}\text{，则}$

${Q(a\text{，}b) = \sum_{i = 1}^{n}\left\lbrack y_{i} - bx_{i} - \left( \overline{y} - b\overline{x} \right) + \left( \overline{y} - b\overline{x} \right) - a \right\rbrack^{2} }{= \sum_{i = 1}^{n}\left\lbrack \left( y_{i} - \overline{y} \right) - b\left( x_{i} - \overline{x} \right) + \left( \overline{y} - b\overline{x} - a \right) \right\rbrack^{2} }{= \sum_{i = 1}^{n}\left\lbrack \left( y_{i} - \overline{y} \right) - b\left( x_{i} - \overline{x} \right) \right\rbrack^{2} + 2\left( \overline{y} - b\overline{x} - a \right)\sum_{i = 1}^{n}\left\lbrack \left( y_{i} - \overline{y} \right) - b\left( x_{i} - \overline{x} \right) \right\rbrack + n\left( \overline{y} - b\overline{x} - a \right)^{2} }{= \sum_{i = 1}^{n}\left\lbrack \left( y_{i} - \overline{y} \right) - b\left( x_{i} - \overline{x} \right) \right\rbrack^{2} + n\left( \overline{y} - b\overline{x} - a \right)^{2} + 2\left( \overline{y} - b\overline{x} - a \right)\left( \sum_{i = 1}^{n}\left( y_{i} + x_{i} \right) - n\overline{y} - n\overline{x} \right) }{= \sum_{i = 1}^{n}\left\lbrack \left( y_{i} - \overline{y} \right) - b\left( x_{i} - \overline{x} \right) \right\rbrack^{2} + n\left( \overline{y} - b\overline{x} - a \right)^{2} + 2\left( \overline{y} - b\overline{x} - a \right) \cdot 0 }{= \sum_{i = 1}^{n}\left\lbrack \left( y_{i} - \overline{y} \right) - b\left( x_{i} - \overline{x} \right) \right\rbrack^{2} + n\left( \overline{y} - b\overline{x} - a \right)^{2}}$

$Q(a\text{，}b)$是关于b的二次函数，则当

$\left\{ \begin{array}{r} \widehat{a} = \overline{y} - \widehat{b}x\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \widehat{b} = \frac{\sum_{i = 1}^{n}{\left( x_{i} - \overline{x} \right)\left( y_{i} - \overline{y} \right)}}{\sum_{i = 1}^{n}\left( x_{i} - \overline{x} \right)^{2}} \end{array} \right.\$

时，Q达到最小。
