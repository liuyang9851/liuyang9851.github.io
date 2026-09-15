---
title: "代数与函数方法"
hs_seq: "B4"
description: "代数与函数方法：一元三次方程与一元四次方程"
---

# 代数与函数方法

一元三次方程与一元四次方程

一元三次方程

$ax^{3} + bx^{2} + cx + d = 0$

现介绍卡尔达诺（Cardano）公式，令最高次项系数为1，得

$x^{3} + ax^{2} + bx + c = 0$

$\text{令}x = y - \frac{1}{3}a\text{，代入得}$

$y^{3} + py + q = 0$

考虑方程

$x^{3} + px + q = 0$

令$x = u + v$，则$x^{3} = u^{3} + v^{3} + 3uv(u + v) = u^{3} + v^{3} + 3uvx$，即$x^{3} - 3uvx - \left( u^{3} + v^{3} \right) = 0$

$\text{对比}\left\{ \begin{array}{r} x^{3} + px + q = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ x^{3} - 3uvx - \left( u^{3} + v^{3} \right) = 0 \end{array} \right.\ \text{，得}$

$\left\{ \begin{array}{r} uv = - \frac{1}{3}p\ \ \ \ \  \\ u^{3} + v^{3} = - q \end{array} \right.\ \text{，即}\left\{ \begin{array}{r} u^{3}v^{3} = - \frac{1}{27}p^{3} \\ u^{3} + v^{3} = - q \end{array} \right.\$

由韦达定理，$u^{3}\text{和}v^{3}$是方程

$y^{2} + qy - \frac{p^{3}}{27} = 0$

的根，得

$u^{3} = - \frac{q}{2} + \sqrt{\frac{a^{2}}{4} + \frac{p^{3}}{27}}\text{，}v^{3} = - \frac{q}{2} - \sqrt{\frac{q^{2}}{2} + \frac{p^{3}}{27}}$

令

$\Delta = \frac{q^{2}}{4} + \frac{p^{3}}{27}$

得方程$x^{3} + px + q = 0$的根为

$\left\{ \begin{array}{r} x_{1} = \sqrt[3]{- \frac{q}{2} + \sqrt{\Delta}} + \sqrt[3]{- \frac{q}{2} - \sqrt{\Delta}}\ \ \ \ \ \ \ \ \  \\ x_{2} = \omega\sqrt[3]{- \frac{q}{2} + \sqrt{\Delta}} + \omega^{2}\sqrt[3]{- \frac{q}{2} - \sqrt{\Delta}} \\ x_{3} = \omega^{2}\sqrt[3]{- \frac{q}{2} + \sqrt{\Delta}} + \omega\sqrt[3]{- \frac{q}{2} - \sqrt{\Delta}} \end{array} \right.\$

$\text{其中}\omega = - \frac{1}{2} + \frac{\sqrt{3}}{2}i$

一元四次方程

$ax^{4} + bx^{3} + cx^{2} + dx + e = 0$

$\text{令}x = y - \frac{1}{4}a\text{可消去三次项，转化为类似如下方程}$

$x^{4} + ax^{2} + bx + c = 0$

现介绍费拉里（Ferrari）解法，方程等号左边加减$ux^{2} + \frac{u^{2}}{4}$，得

$x^{4} + ux^{2} + \frac{u^{2}}{4} - \left\lbrack (u - a)x^{2} - bx + \frac{u^{2}}{4} - c \right\rbrack = 0$

其中$u$是新设的未知数，为了是中括号中的部分形成一个完全平方，需解一元三次方程

$b^{2} - 4(u - a)\left( \frac{u^{2}}{4} - c \right) = 0$

解出$u$的任意一个根后，中括号为完全平方，得

$\left( x^{2} + \frac{u}{2} \right)^{2} - \left( \sqrt{u - a} \cdot x - \frac{b}{2\sqrt{u - a}} \right)^{2} = 0$

得到两个一元二次方程

$\left\{ \begin{array}{r} x^{2} + \sqrt{u - a} \cdot x + \frac{u}{2} - \frac{b}{2\sqrt{u - a}} = 0 \\ x^{2} - \sqrt{u - a} \cdot x + \frac{u}{2} + \frac{b}{2\sqrt{u - a}} = 0 \end{array} \right.\$

解出方程即可得到原方程的所有根

任何复系数一元n次多项式方程（$n \in \mathbb{N}^{*}$）在复数域上至少有一根。

推论：n次复系数多项式方程在复数域内有且只有n个根（重根按重数计算）

线性空间与抽象定义

函数与方程的关系
