---
title: "复数"
hs_seq: "A7"
description: "复数：其中叫做实部，叫做虚部，当时，叫做虚数。当时，叫做纯虚数。"
---

# 复数

虚数单位

$i^{2} = - 1 \Rightarrow i = \pm \sqrt{- 1}$

复数

$z = a + bi\ \ (a\text{，}b\mathbb{\in R)}$

其中$a$叫做实部，$b$叫做虚部，当$b \neq 0$时，叫做虚数。当$a = 0\text{且}b \neq 0$时，叫做纯虚数。

虚数没有绝对值。

虚数不能比较大小。

复数的模

$|z| = \sqrt{a^{2} + b^{2}}$

共轭复数

$\overline{z} = a - bi$

复数的三角形式

$z = r\left( \cos\theta + i\sin\theta \right)$

$\text{其中}r = |z| = \sqrt{a^{2} + b^{2}}\text{，}\theta \text{叫做辐角，}\cos\theta = \frac{a}{r}\text{，}\sin\theta = \frac{b}{r}\text{。}$

$\text{特别地，当}\theta \in \lbrack 0\text{，}2\pi\rbrack \text{时，}\theta \text{叫做辐角主值。}\left( \arg z \right)$

复数的运算

加（减）运算：$(a + bi) \pm (c + di) = (a \pm c) + (b \pm d)i$

一般形式

乘法运算：$(a + bi) \times (c + di) = (ac - bd) + (ad + bc)i$

$\text{除法运算：}\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac + bd) + (bc - ad)i}{c^{2} + d^{2}}$

三角形式

乘法运算：$r_{1}\left( \cos\theta_{1} + i\sin\theta_{1} \right) \cdot r_{2}\left( \cos\theta_{2} + i\sin\theta_{2} \right) = r_{1}r_{2}\left\lbrack \cos\left( \theta_{1} + \theta_{2} \right) + i\sin\left( \theta_{1} + \theta_{2} \right) \right\rbrack$

$\text{除法运算：}\frac{r_{1}\left( \cos\theta_{1} + i\sin\theta_{1} \right)}{r_{2}\left( \cos\theta_{2} + i\sin\theta_{2} \right)} = \frac{r_{1}}{r_{2}}\left\lbrack \cos\left( \theta_{1} - \theta_{2} \right) + i\sin\left( \theta_{1} - \theta_{2} \right) \right\rbrack$

处理加减运算时，多用一般形式；处理乘除运算时，多用三角形式。

复平面（阿尔冈图）

用直角坐标系表示复数的图形叫做复平面（阿尔冈图）。

复数在复平面的运算满足平行四边形法则与三角形法则。

复数的性质

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$z\overline{z} = |z|^{2}$

</th>
<th>

$\overline{z_{1} \pm z_{2}} = \overline{z_{1}} \pm \overline{z_{2}}$

</th>
<th>

$\overline{z_{1}z_{2}} = \overline{z_{1}} \cdot \overline{z_{2}}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\frac{1}{z} = r\left( \cos( - \theta) + i\sin( - \theta) \right)$

</td>
<td>

$\left| \frac{z_{1}}{z_{2}} \right| = \frac{\left| z_{1} \right|}{\left| z_{2} \right|}$

</td>
<td></td>
</tr>
</tbody>
</table>
</div>

一元二次方程的解

$ax^{2} + bx + c = 0\ (a \neq 0)$

$\text{当}\Delta \geq 0\text{时，}\ x = \frac{- b \pm \sqrt{b^{2} - 4ac}}{2a}\text{；当}\Delta < 0\text{时，}x = \frac{- b \pm i\sqrt{- \left( b^{2} - 4ac \right)}}{2a}$

棣莫佛定理

$z^{n} = r^{n}\left\lbrack \cos{n\theta} + i\sin{n\theta} \right\rbrack$

1的n次方根

设$z = \rho\left( \cos\theta + i\sin\theta \right)$是1的n次方根，则

$z^{n} = \rho^{n}\left( \cos{n\theta} + i\sin{n\theta} \right) = 1 = \cos 0 + i\sin 0$

实部与虚部对应，得到方程组

$\left\{ \begin{array}{r} \rho^{n} = 1\ \ \ \ \ \ \ \ \ \ \ \ \  \\ n\theta = 0 + 2k\pi \end{array} \right.\$，解得$\left\{ \begin{array}{r} \rho = 1\ \ \  \\ \theta = \frac{2k\pi}{n} \end{array} \right.\$

$z = \cos\frac{2k\pi}{n} + i\sin\frac{2k\pi}{n}$

由该式注意到，1的n次方根在复平面将单位圆n等分。
