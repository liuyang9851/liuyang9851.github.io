---
title: "解析几何"
hs_seq: "A9"
description: "解析几何：弦长公式（已知直线斜率及直线上两点横坐标/纵坐标，求两点距离）"
---

# 解析几何

$\text{（在椭圆中，记}C_{1}:\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1\text{，}C_{2}:\frac{y^{2}}{a^{2}} + \frac{x^{2}}{b^{2}} = 1\text{，}M(x_{1}\text{，}y_{1})\text{，}N(x_{2}\text{，}y_{2})\text{，}P(x_{0}\text{，}y_{0})\text{）}$

$\text{（在双曲线中，记}C_{1}:\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} = 1\text{，}C_{2}:\frac{y^{2}}{a^{2}} - \frac{x^{2}}{b^{2}} = 1\text{，}M(x_{1}\text{，}y_{1})\text{，}N(x_{2}\text{，}y_{2})\text{，}P(x_{0}\text{，}y_{0})\text{）}$

$\text{（在抛物线中，记}C_{1}:y^{2} = 2px\text{，}C_{2}:y^{2} = - 2px\text{，}C_{3}:x^{2} = 2py\text{，}C_{4}:x^{2} = - 2px\text{）}$

$\text{（椭圆与双曲线的共同方程为}C_{0}:\frac{x^{2}}{m} + \frac{y^{2}}{n} = 1\text{，}|PQ|\text{是过焦点的弦）}$

直线

（$\text{记}l\text{：}Ax + By + C = 0\text{，}l_{1}\text{：}A_{1}x + B_{1}y + C_{1} = 0\text{，}l_{2}\text{：}A_{2}x + B_{2}y + C_{2} = 0$）

直线的方程

> 点斜式：$y - y_{0} = k\left( x - x_{0} \right)(k\text{存在})$
>
> 斜截式：$y = kx + b(k\text{存在})$
>
> $\text{两点式：}\frac{y - y_{1}}{y_{2} - y_{1}} = \frac{x - x_{1}}{x_{2} - x_{1}}(k\text{存在且}k \neq 0)$
>
> 变形：$\left( y_{2} - y_{1} \right)\left( x - x_{1} \right) = \left( x_{2} - x_{1} \right)\left( y - y_{1} \right)$
>
> $\text{截距式：}\frac{x}{a} + \frac{y}{b} = 1(k\text{存在、}k \neq 0\text{且直线不过原点})$
>
> 一般式：$Ax + By + C = 0(A\text{、}B\text{不同时为}0)$
>
> 参数方程：已知向量$\mathbf{v} = (m\text{，}n)\text{，则直线可表示为}\left\{ \begin{array}{r} x = x_{0} + mt \\ y = y_{0} + nt \end{array} \right.\$
>
> 特别地，当$\mathbf{v}$是单位向量时，参数方程也可写为$\left\{ \begin{array}{r} x = x_{0} + t\cos\theta \\ y = y_{0} + t\sin\theta \end{array} \right.\$

直线的平行与对称判定

> $l_{1}//l_{2} \Leftrightarrow A_{1}B_{2} = A_{2}B_{1}\text{，且}A_{1}C_{2} \neq A_{2}C_{1}\ /\ B_{1}C_{2} \neq B_{2}C_{1}$
>
> $l_{1}\bot l_{2} \Leftrightarrow A_{1}A_{2} + B_{1}B_{2} = 0$

线系

> 相交线系（共点线系）：$A_{1}x + B_{1}y + C_{1} + \lambda\left( A_{2}x + B_{2}y + C_{2} \right) = 0$

距离公式

> $\text{点}\ P\left( x_{0}\text{，}y_{0} \right)\text{到直线}l\text{的距离：}d = \frac{\left| Ax_{0} + By_{0} + C \right|}{\sqrt{A^{2} + B^{2}}}$
>
> $\text{两条平行直线}l_{1}\text{，}l_{2}\text{间的距离：}d = \frac{\left| C_{1} - C_{2} \right|}{\sqrt{A^{2} + B^{2}}}$

$\text{直线}l_{1}\text{，}l_{2}\text{的交点：}\left| \begin{matrix} A_{1} & B_{1} \\ A_{2} & B_{2} \end{matrix} \right|\left( - \left| \begin{matrix} C_{1} & B_{1} \\ C_{2} & B_{2} \end{matrix} \right|\text{，}\left| \begin{matrix} C_{1} & A_{1} \\ C_{2} & A_{2} \end{matrix} \right| \right)\ \ (\text{即线性方程组的解})$

直线的平移与等效平移

> 一般平移 ($m\text{，}n \in \mathbb{R}_{+}$)
>
> 上移m：$A(x + m) + By + C = 0$
>
> 下移m：$A(x - m) + By + C = 0$
>
> 左移n：$\ Ax + B(y - n) + C = 0$
>
> 右移n：$\ Ax + B(y + n) + C = 0$
>
> 法向平移
>
> $\text{直线平移的最短距离（法向平移距离）}d = \frac{mn}{\sqrt{m^{2} + n^{2}}} = \left| C_{1} - C_{2} \right|$

直线分割平面

> 不等式$Ax + By + C > 0$表示法向量$(A\text{，}B)$所在区域。
>
> 对直线$l$变形得$y = - \frac{A}{B}x - \frac{C}{B}$，代入$P(x_{0}\text{，}y_{0})$，若$- \frac{A}{B}x_{0} - \frac{C}{B} > y_{0}$，则点在直线上方，反之在下方。直线左右的讨论同理。
>
> （$F(x\text{，}y) = Ax + By + C$代入$P(x_{0}\text{，}y_{0})$）

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

点P在直线的…边

</th>
<th>

$A > 0$

</th>
<th>

$A < 0$

</th>
<th>

$B > 0$

</th>
<th>

$B < 0$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$F > 0$

</td>
<td>

右

</td>
<td>

左

</td>
<td>

上

</td>
<td>

下

</td>
</tr>
<tr>
<td>

$F < 0$

</td>
<td>

左

</td>
<td>

右

</td>
<td>

下

</td>
<td>

上

</td>
</tr>
</tbody>
</table>
</div>

> $AB > 0$，平面被分为左下和右上
>
> $AB < 0$，平面被分为左上和右下

直线与向量

> 直线的方向向量：$(B\text{，} - A)\text{和}( - B\text{，}A)$
>
> 直线的法向量：$(A\text{，}B)$

直线的夹角

> 若有两条直线$l_{1}\text{，}l_{2}$相交，则其夹角$\theta$（较小角）满足：

${\sin\theta = \frac{\left| A_{1}B_{2} - A_{2}B_{1} \right|}{\sqrt{\left( A_{1}^{2} + B_{1}^{2} \right)\left( A_{2}^{2} + B_{2}^{2} \right)}} = \frac{\left| k_{1} - k_{2} \right|}{\sqrt{\left( 1 + k_{1}^{2} \right)\left( 1 + k_{2}^{2} \right)}} }{\cos\theta = \frac{\left| A_{1}B_{2} + A_{2}B_{1} \right|}{\sqrt{\left( A_{1}^{2} + B_{1}^{2} \right)\left( A_{2}^{2} + B_{2}^{2} \right)}} = \frac{\left| 1 + k_{1}k_{2} \right|}{\sqrt{\left( 1 + k_{1}^{2} \right)\left( 1 + k_{2}^{2} \right)}} }{\tan\theta = \left| \frac{A_{1}B_{2} - A_{2}B_{1}}{A_{1}B_{2} + A_{2}B_{1}} \right| = \left| \frac{k_{1} - k_{2}}{1 + k_{1}k_{2}} \right|}$

> 证明：由向量的点乘，得$\left( B_{1}\text{，} - A_{1} \right)\text{和}(B_{2}\text{，} - A_{2})$对应直线的夹角的余弦

$\cos\theta = \frac{\left| A_{1}B_{2} + A_{2}B_{1} \right|}{\sqrt{\left( A_{1}^{2} + B_{1}^{2} \right)\left( A_{2}^{2} + B_{2}^{2} \right)}}\text{，}\sin\theta = \sqrt{1 - \cos^{2}\theta} = \frac{\sqrt{\left( A_{1}B_{2} - A_{2}B_{1} \right)^{2}}}{\sqrt{\left( A_{1}^{2} + B_{1}^{2} \right)\left( A_{2}^{2} + B_{2}^{2} \right)}} = \frac{\left| A_{1}B_{2} - A_{2}B_{1} \right|}{\sqrt{\left( A_{1}^{2} + B_{1}^{2} \right)\left( A_{2}^{2} + B_{2}^{2} \right)}}$

直线的对称

1. 点与点

> $\text{中点坐标公式}\left( \frac{x_{1} + x_{2}}{2}\text{，}\frac{y_{1} + y_{2}}{2} \right)$
>
> $\text{关于点的对称点}(2x_{0} - x_{1}\text{，}2y_{0} - y_{1})$

2. 点与线

> $\text{点}P\left( x_{0}\text{，}y_{0} \right)\text{关于直线}l\text{的对称点：}(x_{0} - 2Am\text{，}y_{0} - 2Bm)\text{，其中}m = \frac{Ax_{0} + By_{0} + C}{A^{2} + B^{2}}$
>
> $\text{特别地，若}k = \pm 1\text{，则对称点为}\left( - \frac{By_{0} + C}{A}\text{，} - \frac{Ax_{0} + C}{B} \right)$
>
> 套路：两直线斜率乘积=-1 和 两点中点在对称轴上
>
> $\text{直线}l\text{关于点}P\left( x_{0},y_{0} \right)\text{的对称直线的方程：}A\left( x - 2x_{0} \right) + B\left( y - 2y_{0} \right) - C = 0$
>
> $\text{点}\left( x_{1},y_{1} \right)\text{和点}\left( x_{2},y_{2} \right)\text{的对称轴的方程：}2\left( x_{1} - x_{2} \right)x + 2\left( y_{1} - y_{2} \right)y - \left( x_{1}^{2} - x_{2}^{2} \right) - \left( y_{1}^{2} - y_{2}^{2} \right) = 0$

3. 线与线

> 两条直线的方向向量的单位向量的和为其对称直线的方向向量。
>
> 若有两条直线$l_{1}\text{，}l_{2}$，则它们的两条对称轴为

$\sqrt{A_{1}^{2} + B_{1}^{2}}\left( A_{1}x + B_{1}y + C_{1} \right) \pm \sqrt{A_{2}^{2} + B_{2}^{2}}\left( A_{2}x + B_{2}y + C_{2} \right) = 0$

> 记$(x_{0}\text{，}y_{0})$为其交点，则其对称直线的方程为

$\frac{A_{1} + A_{2}}{\mu}\left( x - x_{0} \right) + \frac{B_{1} + B_{2}}{\lambda}\left( y - y_{0} \right) = 0$

$\frac{B_{1} + B_{2}}{\mu}\left( x - x_{0} \right) - \frac{A_{1} + A_{2}}{\lambda}\left( y - y_{0} \right) = 0$

> $\text{直线}l_{1}\text{关于直线}l\text{的对称直线的方程：}\frac{A_{1}x + B_{1}y + C_{1}}{Ax + By + C} = \frac{2(AA_{1} + BB_{1})}{A^{2} + B^{2}}$
>
> $\text{设直线的斜率为}k\text{，两条对称直线的斜率为}a\text{、}b\text{，则有：}\frac{k - a}{1 + ka} = \frac{k - b}{1 + kb}$

圆

（记圆$C\text{：}(x - a)^{2} + (y - b)^{2} = r^{2}\text{或}x^{2} + y^{2} + Dx + Ey + F = 0\text{，}A(x_{1}\text{，}y_{2})\text{，}B(x_{2}\text{，}y_{2})\text{，}P(x_{0}\text{，}y_{0})$）

圆的方程

> 标准方程：$(x - a)^{2} + (y - b)^{2} = r^{2}$
>
> 一般方程：$x^{2} + y^{2} + Dx + Ey + F = 0(D^{2} + E^{2} - 4F > 0)$
>
> $\text{变形：}\left( x + \frac{D}{2} \right)^{2} + \left( y + \frac{E}{2} \right)^{2} = \frac{D^{2} + E^{2} - 4F}{4}$
>
> 参数方程：$\left\{ \begin{array}{r} x = a + r\cos\theta \\ y = b + r\sin\theta \end{array} \right.\$
>
> ![](/images/hs/hs-a09/img03.png)以$AB$为直径的圆的方程：$\left( x - x_{1} \right)\left( x - x_{2} \right) + \left( y - y_{1} \right)\left( y - y_{2} \right) = 0$

弦长公式（已知直线斜率及直线上两点横坐标/纵坐标，求两点距离）

$d = \sqrt{1 + k^{2}}\left| x_{1} - x_{2} \right| = \sqrt{1 + \frac{1}{k_{2}}}\left| y_{1} - y_{2} \right|$a

阿氏圆（$A(x_{1}\text{，}y_{2})\text{，}B(x_{2}\text{，}y_{2})\text{，}PA = \lambda PB$）

> 到两定点的距离之商为定值且不为1的点集

$\left( x + \frac{x_{1} - \lambda^{2}x_{2}}{\lambda^{2} - 1} \right)^{2} + \left( y + \frac{y_{1} - \lambda^{2}y_{2}}{\lambda^{2} - 1} \right)^{2} = \left\lbrack \left| \frac{\lambda}{\lambda^{2} - 1} \right|\sqrt{\left( x_{1} - x_{2} \right)^{2} + \left( y_{1} - y_{2} \right)^{2}} \right\rbrack^{2}$

$\text{其中}r = \left| \frac{\lambda}{\lambda^{2} - 1} \right||AB|\text{，圆心坐标} - \frac{1}{\lambda^{2} - 1}(x_{1} - \lambda^{2}x_{2}\text{，}y_{1} - \lambda^{2}y_{2})$

> 特别地，当AB在x轴上且关于原点对称（$A(a\text{，}0)$）时，阿氏圆方程为

$\left( x + a\frac{1 + \lambda^{2}}{1 - \lambda^{2}} \right)^{2} + y^{2} = \left| \frac{2a\lambda}{\lambda^{2} - 1} \right|^{2}$

> 如图，$EC\text{，}ED$分别是$\bigtriangleup AEB$的内角平分线和外角平分线，它们互相垂直。

圆的切线公式

> 圆C上有点P，则过P的切线为

$\left( x_{0} - a \right)(x - a) + \left( y_{0} - b \right)(y - b) = \left( x_{0} - a \right)^{2} + \left( y_{0} - b \right)^{2} = r^{2}$

$x_{0}x + y_{0}y + D\frac{x_{0} + x}{2} + E\frac{y_{0} + y}{2} + F = 0$

切线长公式

$d = \sqrt{\left( x_{0} - a \right)^{2} + \left( y_{0} - b \right)^{2} - r^{2}} = \sqrt{x_{0}^{2} + y_{0}^{2} + Dx_{0} + Ey_{0} + F}$

圆的极线

$l\text{：}x_{0}x + y_{0}y = r^{2}$

> 当P在C外时，$l$为切点弦所在直线
>
> 当P在C上时，$l$为切线
>
> 当P在C内时，在$l$上任取一点M，过M作圆的切点弦，则切点弦恒过点P

圆系

过圆与直线的交点的圆

$(x - a)^{2} + (y - b)^{2} - r^{2} + \lambda(Ax + By + c) = 0$

过圆与圆的交点的圆

$\left( x - a_{1} \right)^{2} + \left( y - b_{1} \right)^{2} - r_{1}^{2} + \lambda\left( \left( x - a_{2} \right)^{2} + \left( y - b_{2} \right)^{2} - r_{2}^{2} \right) = 0$

圆的切线系

$(x - a)\cos\theta + (y - b)\sin\theta = r$

> 证明：

$d = \frac{\left| (a - a)\cos\theta + (b - b)\sin\theta - r \right|}{\sqrt{\cos^{2}\theta + \sin^{2}\theta}} = r$

两圆的位置关系

相离（4 条公切线)：$d > r_{1} + r_{2}$

外切（3 条公切线）：$d = r_{1} + r_{2}$

相交（2 条公切线）：$\left| r_{1} - r_{2} \right| < d < r_{1} + r_{2}$

内切（1 条公切线）：$d = \left| r_{1} - r_{2} \right|$

内含（没有公切线）：$d < \left| r_{1} - r_{2} \right|$

圆方程相减的几何意义

若有圆$C_{1}$和$C_{2}$，设直线

$\left( D_{1} - D_{2} \right)x + \left( E_{1} - E_{2} \right)y + \left( F_{1} - F_{2} \right) = 0$

> 两圆外离：该线为根轴
>
> 两圆外切：该线为公切线
>
> 两圆相交：该线为交点弦

圆锥曲线

> $\text{（在椭圆中，记}C_{1}:\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1\text{，}C_{2}:\frac{y^{2}}{a^{2}} + \frac{x^{2}}{b^{2}} = 1\text{，}M(x_{1}\text{，}y_{1})\text{，}N(x_{2}\text{，}y_{2})\text{，}P\left( x_{0}\text{，}y_{0} \right)\text{，}F_{1}\text{在左边或下边）}$
>
> $\text{（在双曲线中，记}C_{1}:\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} = 1\text{，}C_{2}:\frac{y^{2}}{a^{2}} - \frac{x^{2}}{b^{2}} = 1\text{，}M\left( x_{1}\text{，}y_{1} \right)\text{，}N\left( x_{2}\text{，}y_{2} \right)\text{，}P\left( x_{0}\text{，}y_{0} \right)\text{，}F_{2}\text{在右边或上边）}$
>
> $\text{（在抛物线中，记}C_{1}:y^{2} = 2px\text{，}C_{2}:y^{2} = - 2px\text{，}C_{3}:x^{2} = 2py\text{，}C_{4}:x^{2} = - 2px\text{）}$
>
> $\text{（椭圆与双曲线的共同方程为}C_{0}:\frac{x^{2}}{m} + \frac{y^{2}}{n} = 1\text{。}|PQ|\text{是过焦点的弦）}$

圆锥曲线的定义

椭圆

> 1.到两定点的距离和为定值且大于两定点距离的点的集合。
>
> 2.到定点与定直线的距离之比为大于0小于1的定值的点的集合。
>
> 3.与两定点斜率之积为负定值（且不等于-1）的点的集合。

双曲线

> 1.到两定点的距离差的绝对值为定值且小于两定点距离的点的集合。
>
> 2.到定点与定直线的距离之比大于1的定值的点的集合。
>
> 3.与两定点斜率之积为正定值的点的集合。

抛物线

> 1.到定点与定直线的距离之比为1的点的集合。

对于三类圆锥曲线的共同定义，有

Pappus定理：圆锥曲线上一点的焦半径长度等于该点到相应准线的距离乘以离心率。

圆锥曲线的定义对应性质

椭圆

> 1.椭圆上任意一点到焦点的距离和为长轴长。
>
> 2.椭圆上任意一点到焦点的距离与它到对应准线的距离之比为离心率。
>
> $\text{如图，}x = \frac{a^{2}}{c}\text{，}\frac{PF_{2}}{PE} = e\text{，}\left| F_{2}E \right|_{x} = \frac{b^{2}}{c}$
>
> 3.椭圆上两对称点到椭圆上某点的直线的斜率之积为负定值，且不等于-1。
>
> $\text{如图，}k_{PE} \cdot k_{PF} = - \frac{b^{2}}{a^{2}} = e^{2} - 1\text{，}k_{PE} \cdot k_{PF} = - \frac{a^{2}}{b^{2}} = \frac{1}{e^{2} - 1}$

双曲线

> 1.双曲线上任意一点到焦点的距离差为长轴长。
>
> 2.双曲线上任意一点到焦点的距离与它到对应准线的距离之比为离心率。
>
> $\text{如图，}x = \frac{a^{2}}{c}\text{，}\frac{PF_{2}}{PE} = e\text{，}\left| F_{2}E \right|_{x} = \frac{b^{2}}{c}$
>
> 3.双曲线上两对称点到双曲线上某点的直线的斜率之积为正定值。
>
> $\text{如图，}k_{PE} \cdot k_{PF} = \frac{b^{2}}{a^{2}} = e^{2} - 1\text{（左图）}k_{PE} \cdot k_{PF} = \frac{a^{2}}{b^{2}} = \frac{1}{e^{2} - 1}\text{（右图）}$

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

准线方程

</th>
<th>

焦点到准线的距离（焦准距）

</th>
<th>

第三定义斜率之积

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$x = \pm \frac{a^{2}}{c}/y = \pm \frac{a^{2}}{c}$

</td>
<td>

$\frac{b^{2}}{c}$

</td>
<td>

$- \frac{n}{m}$

</td>
</tr>
</tbody>
</table>
</div>

抛物线

抛物线上任意一点到焦点的距离与它到对应准线的距离之比为离心率，且为1。

> $x = - \frac{p}{2}\text{，}F\left( \frac{p}{2}\text{，}0 \right)$

椭圆的特有性质

$e \geq \sin\frac{\theta}{2}\text{，}\cos\theta \geq 1 - 2e^{2}$

椭圆（$C_{1}$）上任意一点P越靠近y轴，$\theta$越大。

椭圆（$C_{1}$）上任意一点P越靠近y轴，$\angle APB$越大。

$\angle APB$恒为钝角，且随$\theta$的增大而增大。

设椭圆某焦点为F，过F的直线与椭圆交于点A，B。直线的倾斜角为$\theta$，且$\overset{\rightarrow}{AF} = \lambda\overset{\rightarrow}{BF}$，则

$\left| e\cos\theta \right| = \left| \frac{\lambda - 1}{\lambda + 1} \right|$

双曲线的特有性质

1.双曲线准线与渐近线的交点、原点、对应的焦点构成以a,b,c为三边长的直角三角形

> 如图，$OC\bot CF_{1}$，$OC = a$，$CF_{1} = b$

2.A，B分别在$C_{1}$的两条渐近线上,D为$AB$的中点,则$k_{AB} \cdot k_{OD} = \frac{b^{2}}{a^{2}}$

> $\text{证：设}A\left( x_{1}\text{，}\frac{b}{a}x_{1} \right)\text{，}B\left( x_{2}\text{，} - \frac{b}{a}x_{2} \right)\text{，则}\ D\left( \frac{x_{1} + x_{2}}{2},\frac{y_{1} + y_{2}}{2} \right)\text{，此时}$

$k_{AB} = \frac{b}{a}\frac{x_{1} + x_{2}}{x_{1} - x_{2}}\text{，}k_{OD} = \frac{b}{a}\frac{x_{1} + x_{2}}{x_{1} - x_{2}}\text{，有}k_{AB} \cdot k_{OD} = \frac{b^{2}}{a^{2}}$

3. 过双曲线$\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} = 1(a > 0,b > 0)$上任意一点P做

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

线

</th>
<th>

两渐近线的垂线

</th>
<th>

两渐近线的平行线

</th>
<th>

双曲线的切线

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$|PM| \cdot |PN|(|OM| \cdot |ON|)$

</td>
<td>

$\frac{a^{2}b^{2}}{c^{2}}$

</td>
<td>

$\frac{c^{2}}{4}$

</td>
<td>

$c^{2}$

</td>
</tr>
<tr>
<td>

$\overset{\rightarrow}{PM} \cdot \overset{\rightarrow}{PN}\ \ \left( \overset{\rightarrow}{OM} \cdot \overset{\rightarrow}{ON} \right)$

</td>
<td>

$\frac{a^{2}b^{2}}{c^{4}}\left( b^{2} - a^{2} \right)$

</td>
<td>

$\frac{a^{2} - b^{2}}{4}$

</td>
<td>

$a^{2} - b^{2}$

</td>
</tr>
<tr>
<td>

$S_{\bigtriangleup PMN}\ \ \left( S_{\bigtriangleup OMN} \right)$

</td>
<td>

$\frac{a^{3}b^{3}}{c^{4}}$

</td>
<td>

$\frac{ab}{4}$

</td>
<td>

$ab$

</td>
</tr>
</tbody>
</table>
</div>

![](/images/hs/hs-a09/img01.png)

抛物线的特有性质

1.交坐标轴的弦

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

抛物线$C_{1}$

</th>
<th>

$x_{1} \cdot x_{2}$

</th>
<th>

$y_{1} \cdot y_{2}$

</th>
<th>

$k_{OA} \cdot k_{OB}$

</th>
<th>

$\overset{\rightarrow}{OA} \cdot \overset{\rightarrow}{OB}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\mathbf{(a}\mathbf{\text{，}}\mathbf{0)}$

</td>
<td>

$\mathbf{a}^{\mathbf{2}}$

</td>
<td>

$\mathbf{- 2pa}$

</td>
<td>

$\mathbf{-}\frac{\mathbf{2p}}{\mathbf{a}}$

</td>
<td>

$\mathbf{a}^{\mathbf{2}}\mathbf{- 2pa}$

</td>
</tr>
<tr>
<td>

$\mathbf{(p/2}\mathbf{\text{，}}\mathbf{0)}$

</td>
<td>

$\frac{\mathbf{p}^{\mathbf{2}}}{\mathbf{4}}$

</td>
<td>

$\mathbf{-}\mathbf{p}^{\mathbf{2}}$

</td>
<td>

$\mathbf{- 4}$

</td>
<td>

$\mathbf{-}\frac{\mathbf{3}}{\mathbf{4}}\mathbf{p}^{\mathbf{2}}$

</td>
</tr>
<tr>
<td>

$(p\text{，}0)$

</td>
<td>

$p^{2}$

</td>
<td>

$- 2p^{2}$

</td>
<td>

$- 2$

</td>
<td>

$- p^{2}$

</td>
</tr>
<tr>
<td>

$(2p\text{，}0)$

</td>
<td>

$4p^{2}$

</td>
<td>

$- 4p^{2}$

</td>
<td>

$- 1$

</td>
<td>

$0$

</td>
</tr>
</tbody>
</table>
</div>

![](/images/hs/hs-a09/img02.png)2.过焦点弦的结论

> $\angle AC'B = \angle A'FB' = 90{^\circ}$
>
> $S_{\Delta AOB} = \frac{p^{2}}{2\sin\alpha}$
>
> 以焦半径为直径的圆与y轴相切
>
> 以焦点弦为半径的圆与准线相切
>
> $A\text{、}O\text{、}B'\text{，}A'\text{、}O\text{、}B$三点共线
>
> $k_{AB} = \frac{p}{y_{3}} = \frac{2p}{y_{1} + y_{2}}$
>
> $|AB| = x_{1} + x_{2} + p = \frac{2p}{\sin^{2}\alpha}$
>
> $\left| C'F \right| = \frac{1}{2}\left| A'B' \right|$
>
> $\left| A'B' \right|^{2} = 4|AF||BF|$
>
> $\angle AMF = \angle BMF$
>
> $\frac{1}{|AF|} + \frac{1}{|BF|} = \frac{2}{p}$
>
> $AC'BC'$与抛物线相切
>
> $CC'$垂直与y轴垂直
>
> $S_{\bigtriangleup ABC'} \geq p^{2} = \frac{a^{3}}{8p}\ \ \left( |AB| = a \right)$
>
> $CC'$的中点在抛物线上，且过该点的抛物线的切线与焦点弦平行。
>
> ~~若焦点弦恒过点~~$P\left( x_{0}\text{，}y_{0} \right)$

3.抛物线的阿基米德焦点三角形

> 如图，在抛物线上任取两点，则两点切线交点与这两点连线围成的图形叫阿基米德三角形，特别地，如果两点连线过焦点，则叫阿基米德焦点三角形。
>
> 抛物线的阿基米德焦点三角形有如下结论
>
> 1.切线交点在准线上
>
> 2.弦中点与切线交点连线（弦边上的中线）垂直于坐标轴
>
> 3.阿基米德三角形面积的最小值为$p^{2}$，如果已知$AB = a$，则面积最小值为$\frac{a^{3}}{8p}$
>
> ~~4.若阿基米德三角形的弦边恒过点~~$P\left( x_{0}y_{0} \right)$~~，则弦对应的点的轨迹方程与抛物线的切线方程相同~~
>
> 5.弦边上的中线的中点在抛物线上，且该点的切线平行于弦

弦中点

$\text{椭圆和双曲线的弦中点与原点所在直线的斜率与弦所在直线的斜率之积为定值} - \frac{n}{m}$

$\text{当椭圆焦点在}x\text{轴上时，这个定值为} - \frac{b^{2}}{a^{2}}(e^{2} - 1)\text{，当椭圆焦点在}y\text{轴上时，这个定值为}\  - \frac{a^{2}}{b^{2}}(\frac{1}{e^{2} - 1})$

$\text{如图所示，}k_{OC} \cdot k_{MN} = - \frac{b^{2}}{a^{2}}\text{（左图）}k_{OC} \cdot k_{MN} = - \frac{a^{2}}{b^{2}}\text{（右图）}$双曲线同理

焦点三角形

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

圆锥曲线

</th>
<th>

椭圆

</th>
<th>

双曲线

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\left| PF_{1} \right|\left| PF_{2} \right|$

</td>
<td>

$\frac{2b^{2}}{1 + \cos\theta}$

</td>
<td>

$\frac{2b^{2}}{1 - \cos\theta}$

</td>
</tr>
<tr>
<td>

$\overrightarrow{PF_{1}} \cdot \overrightarrow{PF_{2}}$

</td>
<td>

$\frac{2b^{2}}{1 + \cos\theta}\cos\theta$

</td>
<td>

$\frac{2b^{2}}{1 - \cos\theta}\cos\theta$

</td>
</tr>
<tr>
<td>

$S_{\bigtriangleup PF_{1}F_{2}}$

</td>
<td>

$b^{2} \cdot \tan\frac{\theta}{2}$

</td>
<td>

$b^{2}/\tan\frac{\theta}{2}$

</td>
</tr>
<tr>
<td>

$e$

</td>
<td>

$\frac{\sin\theta}{\sin{\angle PF_{1}F_{2}} + \sin{\angle PF_{2}F_{1}}}$

</td>
<td>

$\frac{\sin\theta}{\left| \sin{\angle PF_{1}F_{2}} - \sin{\angle PF_{2}F_{1}} \right|}$

</td>
</tr>
</tbody>
</table>
</div>

圆锥曲线中的圆

蒙日圆

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

圆锥曲线

</th>
<th>

椭圆

</th>
<th>

双曲线（$C_{1}$）

</th>
<th>

双曲线（$C_{2}$）

</th>
<th>

抛物线（$C_{1}$）

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

蒙日圆的半径

</td>
<td>

$a^{2} + b^{2}$

</td>
<td>

$a^{2} - b^{2}(a > b)$

</td>
<td>

$b^{2} - a^{2}(b > a)$

</td>
<td>

$x = - \frac{p}{2}$

</td>
</tr>
</tbody>
</table>
</div>

过蒙日圆上一点作圆锥曲线的两条切线，则这两条切线互相垂直。

其它圆

椭圆/双曲线中以焦半径为直径的圆必于以长轴为直径的圆相切。

双曲线中焦点三角形的内切圆的圆心在直线$x/y = \pm a$上

抛物线中以焦半径为直径的圆于y轴相切

在双曲线$C_{1}$中，圆（即以$F_{1}F_{2}$为直径的圆）

$x^{2} + y^{2} = c^{2}$

与双曲线在第一象限的交点为$\left( \frac{a}{c}\left( c^{2} + b^{2} \right)\text{，}\frac{b^{2}}{c} \right)$与双曲线的渐近线在第一象限的交点为$(a\text{，}b)$

双曲线的焦点三角形的内切圆的圆心在直线$x = \pm a$或$y = \pm a$上

常用范围

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

圆锥曲线

</th>
<th>

椭圆

</th>
<th>

双曲线($C_{1}$)

</th>
<th>

抛物线

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$|PF|$

</td>
<td>

$\lbrack a - c\text{，}a + c\rbrack$

</td>
<td>

$\lbrack c \pm a\text{，} + \infty)$

</td>
<td>

$\left\lbrack \frac{p}{2}\text{，} + \infty \right)$

</td>
</tr>
<tr>
<td>

$\left| PF_{1} \right|\left| PF_{2} \right|$

</td>
<td>

$\left\lbrack b^{2}\text{，}a^{2} \right\rbrack$

</td>
<td>

$\left\lbrack b^{2}\text{，} + \infty \right)$

</td>
<td></td>
</tr>
<tr>
<td>

$|PO|$

</td>
<td>

$\lbrack b\text{，}a\rbrack$

</td>
<td>

$\lbrack a\text{，} + \infty)$

</td>
<td>

$\lbrack 0\text{，} + \infty)$

</td>
</tr>
<tr>
<td>

$\overrightarrow{PF_{1}} \cdot \overrightarrow{PF_{2}}$

</td>
<td>

$\left\lbrack b^{2} - c^{2}\text{，}b^{2} \right\rbrack$

</td>
<td>

$\left\lbrack a^{2} - c^{2}\text{，} + \infty \right)$

</td>
<td></td>
</tr>
<tr>
<td>

$|PQ|$

</td>
<td>

$\left\lbrack \frac{2b^{2}}{a}\text{，}2a \right\rbrack$

</td>
<td>

$\left\{ \begin{array}{r} \ \lbrack 2a\text{，} + \infty)\ \ \ (a > b) \\ \left\lbrack \frac{2b^{2}}{a}\text{，} + \infty \right)(a < b) \end{array} \right.\$

</td>
<td>

$\lbrack 2p\text{，} + \infty)$

</td>
</tr>
<tr>
<td colspan="4">

$\text{注：}2b^{2}/a\text{和}\ 2p\text{称为通径}$

</td>
</tr>
<tr>
<td>

$DP$

</td>
<td>

$\left\{ \begin{array}{r} \lbrack 0\text{，}2b\rbrack\ \ (b > c\ ) \\ \left\lbrack 0\text{，}\frac{a^{2}}{c} \right\rbrack\ (b < c\ ) \end{array} \right.\$

</td>
<td>

$\left\{ \begin{array}{r} \min{DP} = \frac{\sqrt{5a^{2} + b^{2}}}{2}\left( b > \sqrt{3}a \right) \\ \min{DP} = \sqrt{2}a\ \ \ \ \ \ \ \ \ \ \ \ \ \left( b < \sqrt{3}a \right) \end{array} \right.\$

</td>
<td></td>
</tr>
<tr>
<td colspan="4">

注：双曲线中上式中DP所在直线与x轴和双曲线另一交点构成线段被D平分，下式中DP平行于x轴

</td>
</tr>
<tr>
<td>

$e$

</td>
<td>

$\left\{ \begin{array}{r} \left( 0\text{，}\frac{\sqrt{2}}{2} \right)(b < c) \\ \left( \frac{\sqrt{2}}{2}\text{，}1 \right)(b > c) \end{array} \right.\$

</td>
<td>

$\left\{ \begin{array}{r} \left( 1\text{，}\sqrt{2} \right)\ \ \ \ \ \ \ \ \ (a > b) \\ \left( \sqrt{2}\text{，} + \infty \right)\ \ (a < b) \end{array} \right.\$

</td>
<td>

$1$

</td>
</tr>
<tr>
<td>

$\theta$

</td>
<td>

$\left\lbrack 0\text{，}\frac{b^{2} - c^{2}}{a^{2}} \right\rbrack\ \ \left\{ \begin{array}{r} \max\theta > \frac{\pi}{2}(b > c) \\ \max\theta = \frac{\pi}{2}(b = c) \\ \max\theta < \frac{\pi}{2}(b < c) \end{array} \right.\$

</td>
<td colspan="2"></td>
</tr>
<tr>
<td>

内接长方形的周长

</td>
<td>

$\left\lbrack 4b\text{，}4\sqrt{a^{2} + b^{2}} \right\rbrack$

</td>
<td colspan="2"></td>
</tr>
</tbody>
</table>
</div>

焦半径

坐标形式

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$\left| PF_{1} \right|\text{，}\left| PF_{2} \right|$

</th>
<th>

椭圆/双曲线

</th>
<th>

抛物线

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

焦点在x轴

</td>
<td>

$\left| a + ex_{0} \right|$ $\left| a - ex_{0} \right|$

</td>
<td>

$\left| x_{0} \right| + \frac{p}{2}$

</td>
</tr>
<tr>
<td>

焦点在y轴

</td>
<td>

$\left| a + ey_{0} \right|$ $\left| a - ey_{0} \right|$

</td>
<td>

$\left| y_{0} \right| + \frac{p}{2}$

</td>
</tr>
</tbody>
</table>
</div>

特别地，双曲线的焦半径

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$\left| PF_{1} \right|\text{，}\left| PF_{2} \right|$

</th>
<th>

左支/上支

</th>
<th>

右支/下支

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

焦点在x轴

</td>
<td>

$ex + a$ $ex - a$

</td>
<td>

$- (ex + a)$ $- (ex - a)$

</td>
</tr>
<tr>
<td>

焦点在y轴

</td>
<td>

$ey + a$ $ey - a$

</td>
<td>

$- (ey + a)$ $- (ey - a)$

</td>
</tr>
</tbody>
</table>
</div>

倾斜角形式（$\alpha$表示焦半径所在直线的倾斜角）

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

焦半径

</th>
<th>

椭圆

</th>
<th>

双曲线

</th>
<th>

抛物线

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

焦点在x轴

</td>
<td>

$\frac{b^{2}}{a \pm c\cos\alpha}$

</td>
<td>

$\left| \frac{b^{2}}{c\cos\alpha \pm a} \right|$

</td>
<td>

$\frac{p}{1 \pm \cos\alpha}$

</td>
</tr>
<tr>
<td>

焦点在y轴

</td>
<td>

$\frac{b^{2}}{a \pm c\sin\alpha}$

</td>
<td>

$\left| \frac{b^{2}}{c\sin\alpha \pm a} \right|$

</td>
<td>

$\frac{p}{1 \pm \sin\alpha}$

</td>
</tr>
</tbody>
</table>
</div>

其中，椭圆和抛物线的正负号要根据倾斜角和焦半径长短综合判断，双曲线的正负号由P和焦点是否位于y轴同侧决定，同正异负（短边正长边负），也可分类讨论为

$\text{交于同一支：}\frac{b^{2}}{a \pm c\cos\alpha}\text{，交于两支：}\frac{b^{2}}{c\cos\alpha \pm a}$

由此可得，当与椭圆相交或与双曲线一支相交时，有

$\frac{1}{|PF|} + \frac{1}{|QF|} = \frac{2a}{b^{2}}$

对于抛物线有

$\frac{1}{|PF|} + \frac{1}{|QF|} = \frac{2}{p}$

焦点弦

$|PQ| = \sqrt{1 + k^{2}}\left| x_{1} - x_{2} \right| = \sqrt{1 + k^{- 2}}\left| y_{1} - y_{2} \right|$

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

圆锥曲线

</th>
<th>

焦点在x轴

</th>
<th>

焦点在y轴

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

椭圆/双曲线

</td>
<td>

$|PQ| = \left| \frac{2ab^{2}}{a^{2} - c^{2}\cos^{2}\alpha} \right|$

</td>
<td>

$|PQ| = \left| \frac{2ab^{2}}{a^{2} - c^{2}\sin^{2}\alpha} \right|$

</td>
</tr>
<tr>
<td>

抛物线

</td>
<td>

$|PQ| = \left| x_{1} \right| + \left| x_{2} \right| + p = \frac{2p}{\sin^{2}\alpha}$

</td>
<td>

$|PQ| = \left| y_{1} \right| + \left| y_{2} \right| + p = \frac{2p}{\cos^{2}\alpha}$

</td>
</tr>
</tbody>
</table>
</div>

$\text{过焦点弦}AB\text{的中点}M\text{的垂线交焦点所在轴于一点}R\text{，则}\frac{|FR|}{|AB|} = \frac{e}{2}$

特殊的离心率的几何意义

椭圆

$e = \frac{\sqrt{2}}{2}\ \ \ \ \ \ \ \  \Leftrightarrow \bigtriangleup PF_{1}F_{2}\text{是以}P\text{为直角顶点的直角三角形}$

$e = \frac{\sqrt{3}}{3}\ \ \ \ \ \ \ \  \Leftrightarrow \bigtriangleup ABF\text{是等边三角形}$

$e = \sqrt{2} - 1 \Leftrightarrow \bigtriangleup ABF\text{是以}F\text{为直角顶点的直角三角形}$

$e = \frac{\sqrt{5} - 1}{2} \Leftrightarrow b^{2} = ac$

双曲线

$e = \frac{\sqrt{5} + 1}{2} \Leftrightarrow b^{2} = ac$

参数方程（$C_{1}$）

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

椭圆

</th>
<th>

双曲线

</th>
<th>

抛物线

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\left\{ \begin{array}{r} x = a\cos t \\ y = a\sin t \end{array} \right.\$

</td>
<td>

$\left\{ \begin{array}{r} x = a\sec t \\ y = a\tan t \end{array} \right.\$

</td>
<td>

$\left\{ \begin{array}{r} x = t\ \ \ \ \ \ \ \ \ \ \ \  \\ y = \pm \sqrt{2pt} \end{array} \right.\$

</td>
</tr>
</tbody>
</table>
</div>

圆锥曲线硬解定理

> 理念：通过设出点的坐标和直线方程与圆锥曲线方程联立，利用韦达定理得出有关点的坐标的相关表达式，分析推理得出相应结论。

一般地，联立方程

$\left\{ \begin{array}{r} \frac{x^{2}}{m} + \frac{y^{2}}{n} = 1\ \ \ \ \ \ \ \ \ \ \  \\ Ax + By + C = 0 \end{array} \right.\$

$\text{其中记}$

$m = x^{2}\text{系数下的分母，}n = y^{2}\text{系数下的分母}$

$\varepsilon = mA^{2} + nB^{2}$

$\tau_{x} = 2mAC\text{，}\tau_{y} = 2nBC$

$\lambda_{x} = m\left( C^{2} - nB^{2} \right)\text{，}\lambda_{y}n\left( C^{2} - mA^{2} \right)(\text{对于}y)$

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$x$

</th>
<th>

$y$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\left( mA^{2} + nB^{2} \right)x^{2} + 2mACx + m\left( C^{2} - nB^{2} \right) = 0$

$\varepsilon x^{2} + \tau_{x}x + \lambda_{x} = 0$

</td>
<td>

$\left( mA^{2} + nB^{2} \right)y^{2} + 2nBCy + n\left( C^{2} - mA^{2} \right) = 0$

$\varepsilon x^{2} + \tau_{y}x + \lambda_{y} = 0$

</td>
</tr>
<tr>
<td>

$x_{1} + x_{2} = \frac{- 2mAC}{\varepsilon}$

</td>
<td>

$y_{1} + y_{2} = \frac{- 2nBC}{\varepsilon}$

</td>
</tr>
<tr>
<td>

$x_{1} \cdot x_{2} = \frac{m\left( C^{2} - nB^{2} \right)}{\varepsilon}$

</td>
<td>

$y_{1} \cdot y_{2} = \frac{n\left( C^{2} - mA^{2} \right)}{\varepsilon}$

</td>
</tr>
<tr>
<td>

${\Delta_{x} = 4B^{2}mn\left( \varepsilon - C^{2} \right) }{= \varepsilon^{2}\left\lbrack \left( x_{1} + x_{2} \right)^{2} + 4x_{1} \cdot x_{2} \right\rbrack}$

</td>
<td>

${\Delta_{y} = 4A^{2}mn\left( \varepsilon - C^{2} \right) }{= \varepsilon^{2}\left\lbrack \left( y_{1} + y_{2} \right)^{2} + 4y_{1} \cdot y_{2} \right\rbrack}$

</td>
</tr>
<tr>
<td>

$x_{1} = \frac{- \tau + 2B\sqrt{mn\left( \varepsilon - C^{2} \right)}}{2\varepsilon}$

$x_{2} = \frac{- \tau - 2B\sqrt{mn\left( \varepsilon - C^{2} \right)}}{2\varepsilon}$

</td>
<td>

$y_{1} = \frac{- \tau - 2A\sqrt{mn\left( \varepsilon - C^{2} \right)}}{2\varepsilon}$

$y_{2} = \frac{- \tau + 2A\sqrt{mn\left( \varepsilon - C^{2} \right)}}{2\varepsilon}$

</td>
</tr>
<tr>
<td colspan="2">

$x_{1}y_{2} + x_{2}y_{1} = \frac{2mnAB}{\varepsilon}$

</td>
</tr>
<tr>
<td>

$\left( x_{1} - t \right)\left( x_{2} - t \right) = \frac{\varepsilon t^{2} + \tau_{x}t + \lambda_{x}}{A}$

</td>
<td>

$\left( y_{1} - t \right)\left( y_{2} - t \right) = \frac{\varepsilon t^{2} + \tau_{x}t + \lambda_{x}}{A}$

</td>
</tr>
<tr>
<td colspan="2">

$\left| x_{1}y_{2} - x_{2}y_{1} \right| = \left| \frac{2C}{\varepsilon} \right|\sqrt{mn\left( \varepsilon - C^{2} \right)}$

</td>
</tr>
<tr>
<td>

$\left| x_{1} - x_{2} \right| = \sqrt{\left( x_{1} + x_{2} \right)^{2} - 4x_{1}x_{2}} = \frac{\sqrt{4B^{2}mn\left( \varepsilon - C^{2} \right)}}{\varepsilon}$

</td>
<td>

$\left| y_{1} - y_{2} \right| = \sqrt{\left( y_{1} + y_{2} \right)^{2} - 4y_{1}y_{2}} = \frac{\sqrt{4A^{2}mn\left( \varepsilon - C^{2} \right)}}{\varepsilon}$

</td>
</tr>
<tr>
<td>

$\sqrt{1 + k^{2}}\frac{\sqrt{\Delta_{x}}}{|\varepsilon|} = \sqrt{1 + \left( - \frac{A}{B} \right)^{2}}\frac{\sqrt{\Delta_{x}}}{|\varepsilon|}$

</td>
<td>

$\sqrt{1 + k^{- 2}}\frac{\sqrt{\Delta_{y}}}{|\varepsilon|} = \sqrt{1 + \left( - \frac{B}{A} \right)^{2}}\frac{\sqrt{\Delta_{y}}}{|\varepsilon|}$

</td>
</tr>
<tr>
<td>

$\sqrt{A^{2} + B^{2}}\frac{\sqrt{\Delta_{x}/B^{2}}}{|\varepsilon|}$

</td>
<td>

$\sqrt{A^{2} + B^{2}}\frac{\sqrt{\Delta_{y}/A^{2}}}{|\varepsilon|}$

</td>
</tr>
</tbody>
</table>
</div>

可得

可得

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

方程

</th>
<th>

$\varepsilon z^{2} + \tau z + \lambda = 0$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$z_{1} + z_{2}$

</td>
<td>

$- \frac{\tau}{\varepsilon}$

</td>
</tr>
<tr>
<td>

$z_{1} \cdot z_{2}$

</td>
<td>

$\frac{\lambda}{\varepsilon}$

</td>
</tr>
<tr>
<td>

$x_{1}y_{2} + x_{2}y_{1}$

</td>
<td>

$\frac{2mnAB}{\varepsilon}$

</td>
</tr>
<tr>
<td>

$\left( z_{1} - t \right)\left( z_{2} - t \right)$

</td>
<td>

$\frac{\varepsilon t^{2} + \tau t + \lambda}{A}$

</td>
</tr>
<tr>
<td>

$\left| z_{1}z_{2} - z_{2}z_{1} \right|$

</td>
<td>

$\left| \frac{2C}{\varepsilon} \right|\sqrt{mn\left( \varepsilon - C^{2} \right)}$

</td>
</tr>
<tr>
<td>

$\Delta_{z}$

</td>
<td>

$\varepsilon^{2}\left\lbrack \left( z_{1} + z_{2} \right)^{2} + 4z_{1} \cdot z_{2} \right\rbrack$

</td>
</tr>
<tr>
<td>

$\Delta'$

</td>
<td>

$mn\left( \varepsilon - C^{2} \right)$

</td>
</tr>
<tr>
<td>

$z_{1} - z_{2}$

</td>
<td>

$\sqrt{\left( z_{1} + z_{2} \right)^{2} - 4z_{1}z_{2}} = \frac{\sqrt{\Delta_{z}}}{|\varepsilon|}$

</td>
</tr>
<tr>
<td>

弦长

</td>
<td>

$\frac{2\sqrt{\left( A^{2} + B^{2} \right)\Delta'}}{|\varepsilon|}$

</td>
</tr>
</tbody>
</table>
</div>

非对称式韦达定理的应用

倒数法

$x_{2} = \lambda x_{1}\text{，求}\lambda \text{的范围：}\lambda + \frac{1}{\lambda} = \frac{x_{1}^{2} + x_{2}^{2}}{x_{1}x_{2}}$

$y_{2} = - 7y_{1} + 8 \Rightarrow y_{2} - 1 = - 7\left( y_{1} - 1 \right) \Rightarrow \frac{y_{2} - 1}{y_{1} - 1} = - 7 \Rightarrow - 7 - \frac{1}{7} = \frac{y_{2} - 1}{y_{1} - 1} + \frac{y_{1} - 1}{y_{2} - 1} = \frac{\left( y_{1} - 1 \right)^{2} + \left( y_{2} - 1 \right)^{2}}{\left( y_{1} - 1 \right)\left( y_{2} - 1 \right)} = \frac{\left\lbrack \left( y_{1} - 1 \right) + \left( y_{2} - 1 \right) \right\rbrack^{2} - 2\left( y_{1} - 1 \right)\left( y_{2} - 1 \right)}{\left( y_{1} - 1 \right)\left( y_{2} - 1 \right)} = \frac{\left( y_{1} + y_{2} - 2 \right)^{2}}{\left( y_{1} - 1 \right)\left( y_{2} - 1 \right)} - 2$

韦达定理带入消去法与配凑半代换法

$eg.\text{已知}x_{1} + x_{2} = - \frac{12k}{6k^{2} + 4}\text{，}x_{1}x_{2} = - \frac{18}{6k^{2} + 4}\text{，求}\frac{kx_{1}x_{2} + 3x_{1}}{kx_{1}x_{2} - x_{2}}$

$\text{解：由韦达定理得，}\frac{x_{1} + x_{2}}{x_{1}x_{2}} = \frac{- 12k}{- 18} \Rightarrow kx_{1}x_{2} = \frac{3}{2}\left( x_{1} + x_{2} \right)\text{，所以}$

$\frac{kx_{1}x_{2} + 3x_{1}}{kx_{1}x_{2} - x_{2}} = \frac{\frac{3}{2}\left( x_{1} + x_{2} \right) + 3x_{1}}{\frac{3}{2}\left( x_{1} + x_{2} \right) - x_{2}} = \frac{\frac{9}{2}x_{1} + \frac{3}{2}x_{2}}{\frac{3}{2}x_{1} + \frac{1}{2}x_{2}} = \frac{3\left( \frac{3}{2}x_{1} + \frac{1}{2}x_{2} \right)}{\frac{3}{2}x_{1} + \frac{1}{2}x_{2}} = 3$

$\frac{kx_{1}x_{2} + 3x_{1}}{kx_{1}x_{2} - x_{2}} = \frac{kx_{1}x_{2} + 3\left( x_{1} + x_{2} \right) - 3x_{2}}{kx_{1}x_{2} - x_{2}} = \frac{- \frac{18k}{6k^{2} + 4} - \frac{36k}{6k^{2} + 4} - 3x_{2}}{- \frac{18k}{6k^{2} + 4} - x_{2}} = \frac{\frac{54k}{6k^{2} + 4} + 3x_{2}}{\frac{18k}{6k^{2} + 4} + x_{2}} = 3$

$\frac{kx_{1}x_{2} + 3x_{1}}{kx_{1}x_{2} - x_{2}} = \frac{kx_{1}x_{2} + 3\left( x_{1} + x_{2} \right) - x_{2}}{kx_{1}x_{2} - x_{2}} = \frac{kx_{!}x_{2} + 3\left( \frac{2}{3}kx_{1}x_{2} - x_{2} \right)}{kx_{1}x_{2} - x_{2}} = \frac{3kx_{1}x_{2} - 3x_{2}}{kx_{1}x_{2} - x_{2}} = 3$

$eg.\text{已知}x_{1} + x_{2} = \frac{8k^{2}}{4k^{2} + 3}\text{，}x_{1}x_{2} = \frac{4\left( k^{2} - 3 \right)}{4k^{2} + 3}\text{，求证：}\frac{\left( x_{1} - 2 \right)\left( x_{2} + 2 \right)}{\left( x_{2} - 1 \right)\left( x_{1} + 2 \right)} = \frac{x_{1}x_{2} - 2x_{1} - x_{2} + 2}{x_{1}x_{2} - x_{1} + 2x_{2} - 2} = \frac{1}{3}$

系数法

$\frac{x_{1}x_{2} - 2x_{1} - x_{2} + 2}{x_{1}x_{2} - x_{1} + 2x_{2} - 2} = \frac{1}{3} \Leftrightarrow 3x_{1}x_{2} - 6x_{1} - 3x_{2} + 6 = x_{1}x_{2} - x_{1} + 2x_{2} - 2 \Leftrightarrow 2x_{1}x_{2} - 5x_{1} - 5x_{2} + 8 = 0$

$\Leftrightarrow 2x_{1}x_{2} - 5\left( x_{1} + x_{2} \right) + 8 = 0 \Leftrightarrow x_{1}x_{1} = \frac{5}{2}\left( x_{1} + x_{2} \right) - 4$

$\frac{x_{1}x_{2} - 2x_{1} - x_{2} + 2}{x_{1}x_{2} - x_{1} + 2x_{2} - 2} = \frac{\frac{5}{2}\left( x_{1} + x_{2} \right) - 4 - 2x_{1} - x_{2} + 2}{\frac{5}{2}\left( x_{1} + x_{2} \right) - 4 - x_{1} + 2x_{2} - 2} = \frac{\frac{1}{2}x_{1} + \frac{3}{2}x_{2} - 2}{\frac{3}{2}x_{1} + \frac{9}{2}x_{2} - 6} = \frac{1}{3}$

韦达定理带入消去法

$\frac{x_{1}x_{2} - 2x_{1} - x_{2} + 2}{x_{1}x_{2} - x_{1} + 2x_{2} - 2} = \frac{x_{1}x_{2} - 2\left( x_{1} + x_{2} \right) + x_{2} + 2}{x_{1}x_{2} - \left( x_{1} + x_{2} \right) + 3x_{2} - 2} = \frac{\frac{8k^{2}}{4k^{2} + 3} - 2 \cdot \frac{4\left( k^{2} - 3 \right)}{4k^{2} + 3} + x_{2} + 2}{\frac{8k^{2}}{4k^{2} + 3} - \frac{4\left( k^{2} - 3 \right)}{4k^{2} + 3} + 3x_{2} + 2} = \frac{1}{3}$

待定系数法

设$mx_{1}x_{2} + n\left( x_{1} + x_{2} \right) = C$，则

$\frac{8mk^{2}}{4k^{2} + 3} + \frac{4n\left( k^{2} - 3 \right)}{4k^{2} + 3} = \frac{(8m + 4n)k^{2} - 12n}{4k^{2} + 3} = C \Rightarrow \left\{ \begin{array}{r} 8m + 4n = 4C \\ - 12n = 3C\ \ \ \ \ \ \end{array} \right.\  \Rightarrow \left\{ \begin{array}{r} m = \frac{5}{8}C \\ n = - \frac{C}{4} \end{array} \right.\$

$\text{得}\frac{5C}{8}x_{1}x_{2} - \frac{C}{4}\left( x_{1} + x_{2} \right) = C \Rightarrow \frac{5}{8}x_{1}x_{2} - \frac{1}{4}\left( x_{1} + x_{2} \right) = 1 \Rightarrow 5x_{1}x_{2} - 2\left( x_{1} + x_{2} \right) = 8$

椭圆与双曲线$\left( C_{1} \right)$的三角函数设点法

$\text{由}\sin^{2}\theta + \cos^{2}\theta = 1\text{，}\frac{1}{\cos^{2}\theta} - \tan^{2}\theta = 1\text{，有}$

> $\cos\theta = \frac{\cos^{2}\frac{\theta}{2} - \sin^{2}\frac{\theta}{2}}{\sin^{2}\frac{\theta}{2} + \cos^{2}\frac{\theta}{2}} = \frac{1 - \tan^{2}\frac{\theta}{2}}{1 + \tan^{2}\frac{\theta}{2}}\text{，}\sin\theta = \frac{2\sin\frac{\theta}{2}\cos\frac{\theta}{2}}{\sin^{2}\frac{\theta}{2} + \cos^{2}\frac{\theta}{2}} = \frac{2\tan\frac{\theta}{2}}{1 + \tan^{2}\frac{\theta}{2}}$
>
> $\frac{1}{\cos\theta} = \frac{1 + \tan^{2}\frac{\theta}{2}}{1 - \tan^{2}\frac{\theta}{2}}\text{，}\tan\theta = \frac{2\tan\frac{\theta}{2}}{1 - \tan^{2}\frac{\theta}{2}}$

$\text{令}t = \tan\frac{\theta}{2}\text{，得}$

> $\cos\theta = \frac{1 - t^{2}}{1 + t^{2}}\text{，}\sin\theta = \frac{2t}{1 + t^{2}}\text{，}\frac{1}{\cos\theta} = \frac{1 + t^{2}}{1 - t^{2}}\text{，}\tan\theta = \frac{2t}{1 - t^{2}}$

所以可以分别设椭圆和双曲线上的点的坐标为

$\text{椭圆：}\left( a\frac{1 - t^{2}}{1 + t^{2}}\text{，}b\frac{2t}{1 + t^{2}} \right)\text{，双曲线：}\left( a\frac{1 + t^{2}}{1 - t^{2}}\text{，}b\frac{2t}{1 - t^{2}} \right)$

设直线$l$与椭圆/双曲线交于两点A（1），B（2），则

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

椭圆

</th>
<th>

双曲线

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

横截距

</td>
<td>

$a\frac{1 + t_{1}t_{2}}{1 - t_{1}t_{2}}\left( \text{或} - \frac{1}{t_{1} + t_{2}} - a \right)$

</td>
<td>

$a\frac{1 - t_{1}t_{2}}{1 + t_{1}t_{2}}$

</td>
</tr>
<tr>
<td>

纵截距

</td>
<td>

$b\frac{1 + t_{1}t_{2}}{t_{1} + t_{2}}$

</td>
<td>

$b\frac{t_{1}t_{2} - 1}{t_{1} + t_{2}}$

</td>
</tr>
<tr>
<td>

直线斜率

</td>
<td>

$\frac{b\left( t_{1}t_{2} - 1 \right)}{a\left( t_{1} + t_{2} \right)}$

</td>
<td>

$\frac{b(t_{1}t_{2} + 1)}{a\left( t_{1} + t_{2} \right)}$

</td>
</tr>
<tr>
<td>

直线方程

</td>
<td>

$bx\left( 1 - t_{1}t_{2} \right) + ay\left( t_{1} + t_{2} \right) = ab\left( 1 + t_{1}t_{2} \right)$

</td>
<td>

$bx\left( 1 + t_{1}t_{2} \right) - ay\left( t_{1} + t_{2} \right) = ab(1 - t_{1}t_{2})$

</td>
</tr>
</tbody>
</table>
</div>

定点定值问题

1.点在圆锥曲线上（手电筒模型）

> $\text{设椭圆}/\text{双曲线方程}\frac{x^{2}}{m} + \frac{y^{2}}{n} = 1\text{，抛物线方程}C_{1}\text{，过圆锥曲线上一点点}P\left( x_{0}\text{，}y_{0} \right)\text{做圆锥曲线的两条}$
>
> $\text{割线，交点分别为}A\left( x_{1}\text{，}y_{1} \right)\text{，}B(x_{2}\text{，}y_{2})\text{，记}k_{PA} = k_{1}\text{，}k_{PB} = k_{2}\text{，则有}$

<div class="table-scroll">
<table>
<thead>
<tr>
<th colspan="2">

椭圆/双曲线

</th>
<th>

$C_{0}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">

$k_{1} + k_{2} = \lambda$

</td>
<td>

$\lambda \neq 0\text{，过定点}$

</td>
<td>

$\left( x_{0} - \frac{2y_{0}}{\lambda}\text{，} - y_{0} - \frac{2x_{0}}{\lambda}\frac{n}{m} \right)$

</td>
</tr>
<tr>
<td>

$\lambda = 0\text{，}k_{AB} =$

</td>
<td>

$\frac{nx_{0}}{my_{0}}\text{，}\left( k_{AB} \cdot k_{OP} = \frac{n}{m} \right)$

</td>
</tr>
<tr>
<td rowspan="2">

$k_{1} \cdot k_{2} = \mu$

</td>
<td>

$\mu \neq \frac{n}{m}\text{，过定点}$

</td>
<td>

$\frac{\mu m + n}{\mu m - n}\left( x_{0}\text{，} - y_{0} \right)$

</td>
</tr>
<tr>
<td>

$\mu = \frac{n}{m}\text{，}k_{AB} =$

</td>
<td>

$- \frac{y_{0}}{x_{0}}$

</td>
</tr>
<tr>
<td rowspan="2">

$\frac{1}{k_{1}} + \frac{1}{k_{2}} = \nu$

</td>
<td>

$\nu \neq 0\text{，过定点}$

</td>
<td>

$\left( - x_{0} - \frac{2y_{0}}{\nu}\frac{m}{n}\text{，}y_{0} - \frac{2x_{0}}{\nu} \right)$

</td>
</tr>
<tr>
<td>

$\nu = 0\text{，}k_{AB} =$

</td>
<td>

$\frac{nx_{0}}{my_{0}}\ \ \left( k_{AB} \cdot k_{OP} = \frac{n}{m} \right)$

</td>
</tr>
</tbody>
</table>
</div>

<div class="table-scroll">
<table>
<thead>
<tr>
<th colspan="2">

抛物线

</th>
<th>

$C_{1}\left( y^{2} = 2px \right)$

</th>
<th>

$C_{3}\left( x^{2} = 2py \right)$

</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">

$k_{1} + k_{2} = \lambda$

</td>
<td>

$\lambda \neq 0\text{，过定点}$

</td>
<td>

$\left( x_{0} - \frac{2y_{0}}{\lambda}\text{，} - y_{0} + \frac{2p}{\lambda} \right)$

</td>
<td>

$\left( - x_{0} + \frac{2p}{\lambda}\text{，}y_{0} - \frac{2x_{0}}{\lambda} \right)$

</td>
</tr>
<tr>
<td>

$\lambda = 0\text{，}k_{AB} =$

</td>
<td>

$- \frac{p}{y_{0}}\ \ \left( k_{OP} = - 2k_{AB} \right)$

</td>
<td>

$- \frac{p}{x_{0}}\ \ \left( k_{OP} = - 2k_{AB} \right)$

</td>
</tr>
<tr>
<td>

$k_{1} \cdot k_{2} = \mu$

</td>
<td>

过定点

</td>
<td>

$\left( x_{0} - \frac{2p}{\mu}\text{，} - y_{0} \right)$

</td>
<td>

$\left( - x_{0}\text{，} - 2p\mu + y_{0} \right)$

</td>
</tr>
<tr>
<td rowspan="2">

$\frac{1}{k_{1}} + \frac{1}{k_{2}} = \nu$

</td>
<td>

$\nu \neq \frac{y_{0}}{p}\text{，过定点}$

</td>
<td>

$\frac{1}{\nu - \frac{y_{0}}{p}}$

</td>
<td>

$\frac{1}{\frac{p}{x_{0}} - \nu}$

</td>
</tr>
<tr>
<td>

$\nu = \frac{y_{0}}{p}\text{，}k_{AB}$

</td>
<td colspan="2">

$\text{不存在}$

</td>
</tr>
</tbody>
</table>
</div>

> 特别地，当$\mu = - 1$时，有

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$\mu = - 1$

</th>
<th>

$C_{0}$

</th>
<th>

$y^{2} = 2px$

</th>
<th>

$x^{2} = 2py$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

过定点

</td>
<td>

$\frac{m - n}{m + n}\left( x_{0}\text{，} - y_{0} \right)$

</td>
<td>

$\left( x_{0} + 2p\text{，} - y_{0} \right)$

</td>
<td>

$\left( - x_{0}\text{，}y_{0} + 2p \right)$

</td>
</tr>
</tbody>
</table>
</div>

> 证明：图像平移与齐次化（见“B8 解析几何”）

2.点在圆锥曲线外

3.点在圆锥曲线内

> 过圆锥曲线内任意点$P\left( x_{0}\text{，}y_{0} \right)$，作两条相互垂直的弦AB、CD，若弦的中点分别为M、N，则直线MN恒过定点：

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

圆锥曲线（$C_{1}$）

</th>
<th>

椭圆

</th>
<th>

双曲线

</th>
<th>

抛物线

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

MN过定点

</td>
<td>

$\left( \frac{a^{2}x_{0}}{a^{2} + b^{2}}\text{，}\frac{b^{2}y_{0}}{a^{2} + b^{2}} \right)$

</td>
<td>

$\left( \frac{a^{2}x_{0}}{a^{2} - b^{2}}\text{，}\frac{b^{2}y_{0}}{a^{2} - b^{2}} \right)$

</td>
<td>

$\left( p + x_{0}\text{，}0 \right)$

</td>
</tr>
</tbody>
</table>
</div>

> ![](/images/hs/hs-a09/img04.png)特别地，A、B是椭圆$C_{1}$上关于x轴对称的任意两个不同的点，点$P(m\text{，}0)$是x轴上的定点，直线PB交椭圆与一点E，直线PA交椭圆与一点F，则直线AE、BF恒过x轴上的定点，设该定点为$Q(n\text{，}0)$，则

$mn = a^{2}$

4.点在原点上

> 1.椭圆或双曲线上有两个动点P、Q，若$OP\bot OQ$，过原点0作直线PQ的垂线，垂足为D，用d表示O到PQ的距离。则有

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

圆锥曲线

</th>
<th>

$C_{0}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\frac{1}{|OP|^{2}} + \frac{1}{|OQ|^{2}}\ \ \left( \frac{1}{d^{2}} \right)$

</td>
<td>

$\left| \frac{1}{m} + \frac{1}{n} \right|$

</td>
</tr>
<tr>
<td>

$\max|PQ|^{2}\left( \max\left( |OP|^{2} + |OQ|^{2} \right) \right)$

</td>
<td>

$\left| \frac{4mn}{m + n} \right|$

</td>
</tr>
<tr>
<td>

$\min\left( S_{\bigtriangleup OPQ} \right)\ \ \left( d^{2} \right)$

</td>
<td>

$\left| \frac{mn}{m + n} \right|$

</td>
</tr>
<tr>
<td>

$d$

</td>
<td>

$\sqrt{\left| \frac{mn}{m + n} \right|}$

</td>
</tr>
<tr>
<td>

$\text{点}D\text{的轨迹方程}$

</td>
<td>

$x^{2} + y^{2} = \left| \frac{mn}{m + n} \right|$

</td>
</tr>
</tbody>
</table>
</div>

> 2.抛物线上有两个动点P、Q，若$OP\bot OQ$，则

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

抛物线

</th>
<th>

$C_{1}$

</th>
<th>

$C_{2}$

</th>
<th>

$C_{3}$

</th>
<th>

$C_{4}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$PQ\text{恒过点}$

</td>
<td>

$(2p\text{，}0)$

</td>
<td>

$( - 2p\text{，}0)$

</td>
<td>

$(0\text{，}2p)$

</td>
<td>

$(0\text{，} - 2p)$

</td>
</tr>
</tbody>
</table>
</div>

> 点D的轨迹方程是$x^{2} + y^{2} = 2px(x \neq 0)$

5.极点与极线![](/images/hs/hs-a09/img05.png)![](/images/hs/hs-a09/img06.png)

如图，点$P(m\text{，}0)$是x轴上任意一点，过点p作圆锥曲线的割线交与G、H。作射线AG，HB交于一点I，过G、H作圆锥曲线的切线交于一点J，作直线AH，GB交于一点K，则I、J、K三点共线，且垂直于x轴。若设该直线的方程为$x = n$，则有

$mn = a^{2}$

相关口诀

曲线上点作垂直，两点连线过定点，下加上减纵加负；

曲线内点作垂直，中点连线过定点，椭正双负各对各；

曲线过O作垂直，垂足轨迹为定圆，椭正双负有不同。

定直线上取动点，无论相切与相交；

两点连线过定点，坐标乘积为定值。

$\ \ k_{1}\text{、}\ k_{2}\ \ \$和为0，坐标乘积也定值。

曲线定点作两线，$\ \ k_{1}\text{、}\ k_{2}\ \ \$和为0；

平行线系已出现，斜率乘积为定值；

椭正双负有不同，抛物系数$- 2\ \$倍。

切线公式

一般地，二次曲线

$Ax^{2} + Bxy + Cy^{2} + Dx + Ey + F = 0$

在点$P(x_{0}\text{，}y_{0})$上的切线$l$为

$Ax_{0}x + B\frac{\left( x_{0}y + y_{0}x \right)}{2} + Cy_{0}y + D\frac{x_{0} + x}{2} + E\frac{y_{0} + y}{2} + F = 0$

特别地

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

圆锥曲线

</th>
<th>

$C_{0}$

</th>
<th>

$y^{2} = 2px$

</th>
<th>

$x^{2} = 2py$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

切线方程

</td>
<td>

$\frac{x_{0}x}{m} + \frac{y_{0}y}{n} = 1$

</td>
<td>

$y_{0}y = p(x + x_{0})$

</td>
<td>

$x_{0}x = p(y + y_{0})$

</td>
</tr>
</tbody>
</table>
</div>

$\text{在非标准方程中，把}x^{2}\text{换成}x_{0}x\text{，}x\text{换成}\frac{x_{0} + x}{2}\text{，}y\text{同理，}xy\text{换成}\frac{x_{0}y + y_{0}x}{2}$

设切点为$P(x_{0},y_{0})$，可得

> $k_{OP} \cdot k_{l} = - \frac{n}{m}$
