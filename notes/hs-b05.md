---
title: "复数"
hs_seq: "B5"
description: "复数：由以及，可以注意到一个问题。"
---

# 复数

关于$i = \pm \sqrt{- 1}$的讨论

由$\sqrt{- 1} \cdot \sqrt{- 1} = i \cdot i = - 1$以及$\sqrt{- 1} \cdot \sqrt{- 1} = \sqrt{( - 1) \cdot ( - 1)} = 1$，可以注意到一个问题。

由欧拉恒等式$e^{i\theta} = \cos\theta + i\sin\theta$，代$\theta = \pi + 2k\pi$，得$- 1 = e^{i\pi + 2k\pi}$，则有

$\sqrt{- 1} = ( - 1)^{\frac{1}{2}} = e^{i\left( \frac{\pi}{2} + k\pi \right)} = \cos\left( \frac{\pi}{2} + k\pi \right) + i\sin\left( \frac{\pi}{2} + k\pi \right)$

当k取不同的值时，$\sqrt{- 1}$既可为$+ i$也可为$- i$，为了方便，要约定k的取值，这样就得到确定的值。

欧拉恒等式

$e^{i\theta} = \cos\theta + i\sin\theta$

特别地，当$\theta = \pi$时，有

$e^{i\pi} + 1 = 0$

证明：由泰勒公式，有以下展开

$e^{x} = 1 + x + \frac{x^{2}}{2} + \frac{x^{3}}{6} + \cdots \text{，}\cos x = 1 - \frac{x^{2}}{2} + \frac{x^{4}}{4!} - \frac{x^{6}}{6!} + \cdots \text{，}\sin x = x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + \cdots$

把$x$换成$i\theta$，得

> ${e^{i\theta} = 1 + \frac{i\theta}{1!} + \frac{i\theta}{2!} + \frac{i\theta}{3!} + \frac{i\theta}{4!} + \frac{i\theta}{5!} + \frac{i\theta}{6!} + \frac{i\theta}{7!}\cdots }{= 1 + i\theta - \frac{\theta^{2}}{2!} - \frac{i\theta^{3}}{3!} + \frac{\theta^{4}}{4!} + \frac{i\theta^{5}}{5!} - \frac{\theta^{6}}{6!} - \frac{i\theta^{7}}{7!} + \cdots }{= \left( 1 - \frac{\theta^{2}}{2!} + \frac{\theta^{4}}{4!} - \frac{\theta^{6}}{6!} + \cdots \right) + i\left( \theta - \frac{a^{3}}{3!} + \frac{\theta^{5}}{5!} - \frac{\theta^{7}}{7!} + \cdots \right) }{= \cos\theta + i\sin\theta}$

由欧拉恒等式，可得到复数的乘方运算，开方运算，指数运算，对数运算等。

$x^{a + bi} = x^{a} + e^{i\ln x^{b}} = x^{a} + \cos{\ln x^{b}} + i\sin{\ln x^{b}}$

三角函数的复指数形式

因为

$\left\{ \begin{array}{r} \ e^{i\theta}\  = \cos\theta + i\sin\theta \\ e^{- i\theta} = \cos\theta - i\sin\theta \end{array} \right.\$

两式相加，相减，得

$\cos\theta = \frac{1}{2}\left( e^{i\theta} + e^{- i\theta} \right)\text{，}\sin\theta = \frac{1}{2i}\left( e^{i\theta} - e^{- i\theta} \right)$

由此能得到全部三角函数的复指数形式，运用它可以方便地得到一些三角函数公式。

$\cos(\alpha - \beta) = \frac{1}{2}\left( e^{i(\alpha - \beta)} + e^{- i(\alpha - \beta)} \right) = \frac{1}{2}\left( \frac{e^{i\alpha}}{e^{i\beta}} + \frac{e^{i\beta}}{e^{i\alpha}} \right) = \cos\alpha\cos\beta + \sin\alpha + \sin\beta$

由双曲函数的定义

${sinh}x = \frac{e^{x} - e^{- x}}{2}\text{，}\cosh x = \frac{e^{x} + e^{- x}}{2}$

得

$\cos x = \cosh{ix}$

$\sin x = - i\sinh{ix}$

n倍角公式

由

$\cos{n\theta} + i\sin{n\theta} = e^{ni\theta} = \left( e^{i\theta} \right)^{n} = \left( \cos\theta + i\sin\theta \right)^{n} = \sum_{k = 0}^{n}{C_{n}^{k}\cos^{n - k}\theta\left( i\sin\theta \right)^{k}}$

用与上面相似的做法，得

$\cos{n\theta} = Re\left( \left( \cos\theta + i\sin\theta \right)^{n} \right)\text{，}\sin{n\theta} = Im\left( \left( \cos\theta + i\sin\theta \right)^{n} \right)$

其中$Re$表示取实数部分，$Im$表示取虚数部分。

棣莫佛定理

$z^{n} = r^{n}\left\lbrack \cos{n\theta} + i\sin{n\theta} \right\rbrack$

证明：可利用复数的三角形式，n个复数依次相乘得到。

也可以由欧拉恒等式，得$z^{n} = r^{n}\left( \cos\theta + i\sin\theta \right)^{n} = r^{n}\left( e^{i\theta} \right)^{n} = r^{n}e^{i(n\theta)} = r^{n}\left\lbrack \cos{n\theta} + i\sin{n\theta} \right\rbrack$

1的n次方根

设$z = \rho\left( \cos\theta + i\sin\theta \right)$是1的n次方根，则

$z^{n} = \rho^{n}\left( \cos{n\theta} + i\sin{n\theta} \right) = 1 = \cos 0 + i\sin 0$

实部与虚部对应，得到方程组

$\left\{ \begin{array}{r} \rho^{n} = 1\ \ \ \ \ \ \ \ \ \ \ \ \  \\ n\theta = 0 + 2k\pi \end{array} \right.\$，解得$\left\{ \begin{array}{r} \rho = 1\ \ \  \\ \theta = \frac{2k\pi}{n} \end{array} \right.\$

$z = \cos\frac{2k\pi}{n} + i\sin\frac{2k\pi}{n}$

由该式注意到，1的n次方根在复平面将单位圆n等分。

把n次单位根分别记作$z_{1}\text{，}z_{2}\text{，}\cdots \text{，}z_{n}$

1的n次方根有如下性质

$1.|z| = 1$

$2.z_{a} \cdot z_{b} = z_{a + b}$

推论：$z_{a}^{- 1} = z_{- a}\text{，}z_{a}^{b} = z_{ab}\text{，}z_{k} = z_{1}^{k}\text{，}z_{k} = z_{n - k}\text{，}z_{k}^{h} = z_{h}^{k}$

由第三个推论，$z_{1}$被称为本原根，且所有的单位根可写作$z_{1}\text{，}z_{1}^{2}\text{，}z_{1}^{3}\text{，}\cdots \text{，}z_{1}^{n}$

$3.$

1的n次方根也被称为单位根，在因式分解中有所应用。

特别地，1的三次方根中虚数根$\omega_{1}\text{，}\omega_{2}$有如下性质：

$\omega_{1}^{2} = \overline{\omega_{2}}\text{，}\omega_{2}^{2} = \overline{\omega_{1}}\text{，}{\overline{\omega_{1}}}^{2} = \omega_{2}\text{，}{\overline{\omega_{2}}}^{2} = \omega_{1}\text{，}\frac{1}{\omega_{1}} = \overline{\omega_{2}}\text{，}\frac{1}{\omega_{2}} = \overline{\omega_{1}}\text{，}\frac{1}{\overline{\omega_{2}}} = \omega_{1}\text{，}\frac{1}{\overline{\omega_{1}}} = \omega_{2}$

韦达定理（根与系数的关系）

三次方程

$a_{3}x^{3} + a_{2}x^{2} + a_{1}x + a_{0} = 0$

有三个复数根，可表示为

$a_{3}\left( x - x_{1} \right)\left( x - x_{2} \right)\left( x - x_{3} \right) = 0$

展开，得

$a_{3}x^{3} - a_{3}\left( x_{1} + x_{2} + x_{3} \right)x^{2} + a_{3}\left( x_{1}x_{2} + x_{1}x_{3} + x_{2}x_{3} \right)x - a_{3}x_{1}x_{2}x_{3} = 0$

得到方程组

$\left\{ \begin{array}{r} x_{1} + x_{2} + x_{3} = - \frac{a_{2}}{a_{1}}\ \ \ \ \ \ \ \ \  \\ x_{1}x_{2} + x_{1}x_{3} + x_{2}x_{3} = \frac{a_{1}}{a_{3}} \\ x_{1}x_{2}x_{3} = - \frac{a_{0}}{a_{3}}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

四次方程

$a_{4}x^{4} + a_{3}x^{3} + a_{2}x^{2} + a_{1}x + a_{0} = 0$

有四个复数根，用类似的方法可以得到

$\left\{ \begin{array}{r} x_{1} + x_{2} + x_{3} + x_{4} = - \frac{a_{1}}{a_{4}}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ x_{1}x_{2} + x_{1}x_{3} + x_{1}x_{4} + x_{2}x_{3} + x_{2}x_{4} + x_{3}x_{4} = \frac{a_{2}}{a_{4}} \\ x_{1}x_{2}x_{3} + x_{1}x_{2}x_{4} + x_{1}x_{3}x_{4} + x_{2}x_{3}x_{4} = - \frac{a_{1}}{a_{4}}\ \ \ \ \ \  \\ x_{1}x_{2}x_{3}x_{4} = \frac{a_{0}}{a_{4}}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$ 一般地，有$\left\{ \begin{array}{r} \sum_{i = 1}^{n}x_{i} = - \frac{a_{n - 1}}{a_{n}} \\ \prod_{i = 1}^{n}x_{i} = ( - 1)^{n}\frac{a_{0}}{a_{n}} \end{array} \right.\$

$\text{从上到下，第}i\text{行等号左边为}C_{n}^{i}\text{个}i\text{次式之和，等号右边为}( - 1)^{i}\frac{a_{i}}{a_{n}}\text{。}$

四元数

四元数在形式上满足

$z = a + bi + cj + dk$

其中

$a\text{，}b\text{，}c\text{，}d\mathbb{\in R}$

$i^{2} + j^{2} + k^{2} = - 1$

$ij = k\text{，}ji = - k\text{，}jk = i\text{，}kj = - i\text{，}ki = j\text{，}ik = - j$

由此看出，四元数乘积不满足交换律。
