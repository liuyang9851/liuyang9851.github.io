---
title: 高阶线性微分方程
description: 二阶常系数齐次与非齐次线性方程、n 阶常系数齐次与非齐次线性方程、欧拉方程、线性微分方程解的结构（齐次与非齐次）、常系数线性微分方程组。
---

# 高阶线性微分方程

[[toc]]

可降阶的高阶微分方程

1.

y(n) = f(x)

连续积分即得

2.

y″ = f(x，y′)

令p = y′，得

p′ = f(x，p)

此是关于x和p的一阶微分方程，如果能求得其通解

p = φ(x，C1)

则原方程的通解为

y = ∫φ(x，C1)dx + C2

3.

y″ = f(y，y′)

令p = y′，得

$$y^{''} = \frac{dp}{dx} = \frac{dp}{dy}\frac{dy}{dx} = p\frac{dp}{dy}$$

代入原方程得

$$p\frac{dp}{dy} = f\left( y\text{，}y' \right)$$

此是关于y和p的一阶微分方程，如果能求得其通解

p = φ(y，C1)

则原方程的通解为

$$\int_{}^{}\frac{dy}{\varphi\left( y\text{，}C_{1} \right)} = x + C_{2}$$

二阶常系数齐次线性微分方程

y″ + py′ + qy = 0

考虑特征方程

r2 + pr + q = 0

（1）当Δ > 0时，有两个不等实根

$$r_{1} = \frac{- p + \sqrt{p^{2} - 4q}}{2}\text{，}r_{2} = \frac{- p - \sqrt{p^{2} - 4q}}{2}$$

此时方程的通解为

y = C1er1x + C2er2x

（2）当Δ = 0时，有两个等根

$$r = - \frac{p}{2}$$

此时方程的通解为

y = (C1 + C2x)erx

（3）当Δ < 0时，有两个共轭复根

r1 = α + βi，r2 = α − βi

其中

$$\alpha = - \frac{p}{2}\text{，}\beta = \frac{\sqrt{4q - p^{2}}}{2}$$

此时方程的通解为

t = eαx(C1cos βx + C2 sin βx)

$$eg.\text{解方程} - kx = ma\text{，其中}x\left| \underset{t = 0}{} \right.\  = x_{0}\text{，}v\left| \underset{t = 0}{} \right.\  = v_{0}$$

解：方程可化为

$$\frac{d^{2}x}{dt^{2}} + \frac{k}{m}x = 0$$

其特征方程

$$r^{2} + \frac{k}{m} = 0$$

的根为

$r = \pm \sqrt{\frac{k}{m}}i$

因此方程的通解为

$$
x = C_{1}\cos\left( \sqrt{\frac{k}{m}}t \right) + C_{2}\sin\left( \sqrt{\frac{k}{m}}t \right)
$$

代入初值条件

$$
x\left| \underset{t = 0}{} \right.\  = x_{0}\text{，}v\left| \underset{t = 0}{} \right.\  = v_{0}
$$

，得到$C_{1} = x_{0}\text{，}C_{2} = v_{0}\sqrt{\frac{m}{k}}$，得

$$
x = x_{0}\cos\left( \sqrt{\frac{k}{m}}t \right) + v_{0}\sqrt{\frac{m}{k}}\sin\left( \sqrt{\frac{k}{m}}t \right) = \sqrt{x_{0}^{2} + \frac{m}{k}v_{0}^{2}\ }\sin\left( \sqrt{\frac{k}{m}}t + \varphi \right)
$$

因此，简谐运动的振幅$A = \sqrt{x_{0}^{2} + \frac{m}{k}v_{0}^{2}}$，频率$\omega = \sqrt{\frac{k}{m}}$，周期$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}$。

不难发现，小角度单摆的

$$
T = 2\pi\sqrt{\frac{m}{k'}} = 2\pi\sqrt{\frac{m}{\frac{mg}{l}}} = 2\pi\sqrt{\frac{l}{g}}
$$

二阶常系数非齐次线性微分方程

y″ + py′ + q = f(x)

（1）f(x) = eλxPm(x)，其中

Pm(x) = a0 + a1x + a2x2 + ⋯ + amxm   （即Pm(x)的次数为m）

考虑特征方程

r2 + pr + q = 0

则方程的一个特解为

y* = xkeλxRm(x)

其中Rm(x)是与Pm(x)同次（m次）的多项式（系数全部待定），k按照λ不是特征方程的根、是特征方程的单根$\left( \lambda \neq - \frac{p}{2} \right)$或是特征方程的重根$\left( \lambda = - \frac{p}{2} \right)$依次取0、1或2。换种表述如下：

$$R_{m}(x) = b_{0} + b_{1}x + b_{2}x^{2} + \cdots + b_{m}x^{m}\text{，}k = \left\{ \begin{array}{r}
0\text{，}\lambda \neq r_{1} \neq r_{2}\ \ \ \  \\
1\text{，}\lambda = r_{12} \neq r_{21} \\
2\text{，}\lambda \neq r_{1} \neq r_{2}\ \ \ \ 
\end{array} \right.\ $$

（2）f(x) = eλx[Pl(x)cos ωx + Qn(x)sin ωx]，其中λ，ω是常数，ω ≠ 0，Pl(x)、Qn(x)分别是x的l次、n次多项式，且仅有一个可为零

考虑特征方程

r2 + pr + q = 0

则方程的一个特解为

y* = xkeλx[Rm(1)(x)cos ωx + Rm(2)(x)sin ωx]

其中Rm(1)(x)、Rm(2)(x)是m次多项式，m = max {l，n}，而k按照λ + ωi或(λ − ωi)不是特征方程的根、或是特征方程的单根依次取0或1。

求解时，为了得到Rm(x)各系数的值，可以将其代入原方程求得系数的值（即待定系数法）。

n阶常系数齐次线性微分方程

y(n) + p1y(n − 1) + p2y(n − 2) + ⋯ + pn − 1y′ + pny = 0

$$\text{记}D = \frac{d}{dx}\text{，}Dy = \frac{dy}{dx}\text{，}D^{n}y = \frac{d^{n}y}{dx^{n}}\text{，则}$$

L(D) = Dn + p1Dn − 1 + ⋯ + pn − 1D + pn = 0

考虑特征方程

rn + p1rn − 1 + p2rn − 2 + ⋯ + pn − 1r + pn = 0

对应情况如下

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

特征方程的根

</th>
<th>

微分方程通解中的对应项

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

单实根r

</td>
<td>

给出一项： Cerx

</td>
</tr>
<tr>
<td>

一对单复根r1, 2 = α ± βi

</td>
<td>

给出两项： eαx(C1cos βx + C2sin βx)

</td>
</tr>
<tr>
<td>

k重实根r

</td>
<td>

给出k项： erx(C1 + C2x + ⋯ + Ckxk − 1)

</td>
</tr>
<tr>
<td>

一对k重复根r1, 2 = α ± βi

</td>
<td>

给出2k项：eαx[(C1 + C2x + ⋯ + Ckxk − 1)cos βx + (D1 + D2x + ⋯ + Dkxk − 1)sin βx]

</td>
</tr>
</tbody>
</table>
</div>

n阶常系数非齐次线性微分方程

y(n) + p1y(n − 1) + p2y(n − 2) + ⋯ + pn − 1y′ + pny = f(x)

（1）f(x) = eλxPm(x)，其中

Pm(x) = a0xm + a1xm − 1 + ⋯ + am − 1x + am

考虑特征方程

rn + p1rn − 1 + p2rn − 2 + ⋯ + pn − 1r + pn = 0

则方程的一个特解为

y* = xkeλxRm(x)

其中Rm(x)是与Pm(x)同次（m次）的多项式，k按照λ不是特征方程的根或是特征方程的s重根取0或s

（2）f(x) = eλx[Pl(x)cos ωx + Qn(x)sin ωx]，其中λ，ω是常数，ω ≠ 0，Pl(x)、Qn(x)分别是x的l次、n次多项式，且仅有一个可为零

考虑特征方程

rn + p1rn − 1 + p2rn − 2 + ⋯ + pn − 1r + pn = 0

则方程的一个特解为

y* = xkeλx[Rm(1)(x)cos ωx + Rm(2)(x)sin ωx]

其中Rm(1)(x)、Rm(2)(x)是m次多项式，m = max {l，n}，而k按照λ + ωi或(λ − ωi)不是特征方程的根、或是特征方程的s重根取0或s。

欧拉方程

xny(n) + p1xn − 1y(n − 1) + p2xn − 2y(n − 2) + ⋯ + pn − 1xy′ + pny = f(x)

当x > 0时，令t = ln x，得（当x < 0时，令t = ln (−x)）

$$\frac{dy}{dx} = \frac{dy}{dx} \cdot \frac{dt}{dx} = \frac{1}{x}\frac{dy}{dt}$$

线性微分方程的解的结构

二阶齐次线性微分方程

定理1：二阶齐次线性微分方程的两个解的线性组合也是该二阶齐次线性微分方程的解。

若y1(x)、y2(x)满足y″ + P(x)y′ + Q(x)y = 0，则解C1y1(x) + C2y2(x)亦满足该方程。

定理2：二阶齐次线性微分方程的两个线性无关的解（不一定是“特解”）的线性组合是该二阶齐次线性微分方程的通解。

若两特解y1(x)、y2(x)满足y1(x) ≠ ky2(x)，则y″ + P(x)y′ + Q(x)y = 0的通解为C1y1(x) + C2y2(x)

二阶非齐次线性微分方程

定理3：二阶非齐次线性微分方程的一个解（不一定是“特解”）加上对应的二阶齐次线性微分方程的通解是该二阶非齐次线性微分方程的通解。（即y = Y + y*）

定理4（叠加原理）：把一个二阶非齐次线性微分方程的自由项拆成两个函数，形成的两个新的二阶非齐次线性微分方程的特解的和是原二阶非齐次线性微分方程的一个特解。

若y1*和y2*分别是y″ + P(x)y′ + Q(x)y = f1(x)和y″ + P(x)y′ + Q(x)y = f2(x)的特解，则y1* + y2*是y″ + P(x)y′ + Q(x)y = f1(x) + f2(x)的特解。

n阶线性微分方程

定理1：n阶齐次线性微分方程的n个线性无关的特解的线性组合是该n阶齐次线性微分方程的通解。

定理2：n阶非齐次线性微分方程的一个解（不一定是“特解”）加上对应的n阶齐次线性微分方程的通解是该n阶非齐次线性微分方程的通解。

定理3：把一个n阶非齐次线性微分方程的自由项拆成两个函数，形成的两个新的n阶非齐次线性微分方程的特解的和是原n阶非齐次线性微分方程的一个特解。

解题时常用到如下的一个结论

若y1(x)、y2(x)是n阶非齐次线性微分方程的两个解，则y1(x) − y2(x)是对应的n阶齐次线性微分方程的解。

一般来说，题目通常会给出二阶非齐次线性微分方程的三个解，这就需要合理地对这三个解做差以找出线性无关的二阶齐次线性微分方程的两个解，这样就找到了二阶齐次线性微分方程的通解，进而得到二阶非齐次线性微分方程的通解。

常系数线性微分方程组

（1）从方程组中校消去一些未知函数及其各阶导数，得到只含有一个未知函数的高阶常系数线性微分方程。

（2）解此高阶微分方程，求出满足该方程的未知函数。

（3）把已求得都函数代入原方程组，一般来说，不必经过积分就可求出其余的未知函数

现将这些方程的解总结如下

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

类型

</th>
<th>

表达式

</th>
<th>

特解

</th>
<th>

通解

</th>
</tr>
</thead>
<tbody>
<tr>
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
</tr>
<tr>
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
</tr>
<tr>
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
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

若g(x) ∼ axm，f(x) ∼ bxn，则∫0g(x)f(t)dt ∼ ∫0axmbtndt
