---
title: "解析几何初步"
hs_seq: "B8"
description: "解析几何初步：由点的旋转可得出方程的旋转："
---

# 解析几何初步

解析几何

变换

点的旋转

> $\text{点}P(x\text{，}y)\text{绕原点逆时针旋转}\theta \text{角的坐标}\left( x'\text{，}y' \right)\text{为}\left( x\cos\theta - y\sin\theta \text{，}x\sin\theta + y\cos\theta \right)$
>
> $\text{点}\left( \begin{array}{r} x \\ y \end{array} \right)\text{绕点}\left( \begin{array}{r} m \\ n \end{array} \right)\text{逆时针旋转}\theta \text{角的坐标为}\begin{pmatrix} \cos\theta & - \sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\left\lbrack \left( \begin{array}{r} x \\ y \end{array} \right) - \left( \begin{array}{r} m \\ n \end{array} \right) \right\rbrack + \left( \begin{array}{r} m \\ n \end{array} \right)\text{，即}$

$\left( \begin{array}{r} x' \\ y' \end{array} \right) = \left( \begin{array}{r} \cos\theta(x - m) - \sin\theta(y - n) + m \\ \sin\theta(x - m) + \cos\theta(y - n) + n \end{array} \right)$

> 相当于坐标轴平移
>
> $\text{其中}\begin{pmatrix} \cos\theta & - \sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\text{叫做旋转矩阵}$
>
> 旋转矩阵的证明
>
> 假设旋转矩阵成立，不妨设$x = r\cos\alpha \text{，}y = r\sin\alpha$，则
>
> $x' = r\cos\alpha\cos\theta - r\sin\alpha\sin\theta = r\cos(\alpha + \theta)$
>
> $y' = r\cos\alpha\sin\theta + r\sin\alpha\cos\theta = r\sin(\alpha + \theta)$
>
> 符合旋转的条件，得证。

由点的旋转可得出方程的旋转：

方程

$f(x\text{，}y) = 0$

绕原点逆时针旋转$\theta$后的方程为

$f(x\cos\theta + y\sin\theta \text{，} - x\sin\theta + y\cos\theta)$

变换

> $\text{旋转变换：}\left( \begin{array}{r} x' \\ y' \end{array} \right) = \begin{pmatrix} \cos\theta & - \sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\left( \begin{array}{r} x \\ y \end{array} \right)$
>
> $\text{反射变换：}\left( \begin{array}{r} x' \\ y' \end{array} \right) = - \frac{1}{A^{2} + B^{2}}\left\lbrack \begin{pmatrix} A^{2} - B^{2} & 2AB \\ 2AB & B^{2} - A^{2} \end{pmatrix}\left( \begin{array}{r} x \\ y \end{array} \right) + \left( \begin{array}{r} 2AC \\ 2BC \end{array} \right) \right\rbrack$
>
> $\text{伸缩变换：}\left( \begin{array}{r} x' \\ y' \end{array} \right) = \begin{pmatrix} k_{1} & 0 \\ 0 & k_{2} \end{pmatrix}\left( \begin{array}{r} x \\ y \end{array} \right)\ \ \left. \text{（把横坐标、纵坐标分别变为原来的}k_{1}\text{、}k_{2}\text{倍} \right.\text{）}\ \ \left. \text{（仿射变换} \right.\text{）}$
>
> $\text{投影变换：}\left( \begin{array}{r} x' \\ y' \end{array} \right) = \frac{1}{A^{2} + B^{2}}\left\lbrack \begin{pmatrix} B^{2} & - AB \\ - AB & A^{2} \end{pmatrix}\left( \begin{array}{r} x \\ y \end{array} \right) - \left( \begin{array}{r} AC \\ BC \end{array} \right) \right\rbrack\ \ (\text{点到直线的垂足坐标})$
>
> $\text{切变变换：}\left( \begin{array}{r} x' \\ y' \end{array} \right) = \left( \begin{array}{r} x + a \\ y + b \end{array} \right)\ \ \left. \text{（同平移，不是线性变换} \right.\text{）}$
>
> 特别地，由旋转变换和切变变换，可得到坐标轴（图像）平移的一般方法如下

坐标轴（图像）平移

> 一般的，对于点$P\left( x_{0}\text{，}y_{0} \right)$方程$f(x\text{，}y) = 0$，如果把坐标系原点移到原坐标轴对应点$\left( x_{C}\text{，}y_{c} \right)$，则新坐标系下的
>
> 点$P\left( x_{0}\text{，}y_{0} \right)$的坐标：$\left( x_{0} - x_{c}\text{，}y_{0} - y_{c} \right)$
>
> 方程$f(x\text{，}y) = 0$的方程$f\left( x + x_{c}\text{，}y + y_{c} \right) = 0$
>
> 坐标轴的旋转：
>
> $\text{如果坐标轴绕原点逆时针旋转}\theta \text{角}$，有如下规律
>
> $\left\{ \begin{array}{r} x' = \ \ \ x\cos\theta + y\sin\theta \\ y' = - x\sin\theta + y\cos\theta \end{array} \right.\$
>
> $\left\{ \begin{array}{r} x = x'\cos\theta - y'\sin\theta \\ y = x'\sin\theta + y'\cos\theta \end{array} \right.\$

参数方程

常见参数方程

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

曲线

</th>
<th>

参数方程

</th>
<th>

直线

</th>
<th>

参数方程

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

直线

</td>
<td>

$\left\{ \begin{array}{r} x = x_{0} + mt \\ y = y_{0} + nt \end{array} \right.\$

</td>
<td>

螺线

</td>
<td>

$\left\{ \begin{array}{r} x = t\cos{lt} \\ y = t\sin{lt} \end{array} \right.\$

</td>
</tr>
<tr>
<td>

椭圆

</td>
<td>

$\left\{ \begin{array}{r} x = a\cos t \\ y = a\sin t \end{array} \right.\$

</td>
<td>

摆线

</td>
<td>

$\left\{ \begin{array}{r} x = r\left( t - \sin t \right) \\ y = r\left( 1 - \cos t \right) \end{array} \right.\$

</td>
</tr>
<tr>
<td>

双曲线

</td>
<td>

$\left\{ \begin{array}{r} x = a\sec t \\ y = a\tan t \end{array} \right.\$

</td>
<td>

笛卡尔叶形线

</td>
<td>

$\left\{ \begin{array}{r} x = \frac{3at}{1 + t^{3}} \\ y = \frac{3at^{2}}{1 + t^{3}} \end{array} \right.\$

</td>
</tr>
<tr>
<td>

抛物线

</td>
<td>

$\left\{ \begin{array}{r} x = 2ct \\ y = t^{2}\ \ \end{array} \right.\$

</td>
<td>

星形线

</td>
<td>

$\left\{ \begin{array}{r} x = a\cos^{3}t \\ y = a\sin^{3}t \end{array} \right.\$

</td>
</tr>
</tbody>
</table>
</div>

极坐标

极坐标的一般形式

$(r,\theta)\ \ \ \rho = \rho(\theta)$

以原点O为起点的射线作为参考系，称O为极点，这条射线为极轴

点P到原点的距离记为r，称为极径

从参考系射线出发逆时针旋转到OP所经过的角度记为$\theta \in \lbrack 0\text{，}2\pi)$，称为极角

极坐标系与平面直角坐标系互换

$x = r\cos\theta$

$y = r\sin\theta$

$r^{2} = x^{2} + y^{2}\text{，}\theta = \arcsin\frac{y}{r} = \arccos\frac{x}{r} = \arctan\frac{y}{x}$

$r' = \frac{dy}{dx} = \frac{dy}{d\theta}\frac{d\theta}{dx} = \frac{y'}{x'}$

常见曲线的极坐标形式（假设极点与原点重合）

圆心在原点的圆：$r = a(a > 0)$，a为半径

圆心不在原点的圆：$\left( r\cos\theta - x_{0} \right)^{2} + \left( r\sin\theta - y_{0} \right)^{2} = a^{2}$，其中

$r \in \left\lbrack \sqrt{x_{0}^{2} + y_{0}^{2}} - a\text{，}\sqrt{x_{0}^{2} + y_{0}^{2}} + a \right\rbrack$

$\text{对称中心在原点的椭圆：}r = \frac{ab}{\sqrt{\left( a\cos\theta \right)^{2} + \left( b\sin\theta \right)^{2}}}$

> 对标准方程变形得$(bx)^{2} + (ay)^{2} = (ab)^{2}$，代入$x = r\cos\theta$，$y = r\sin\theta$得

$\left( br\cos\theta \right)^{2} + \left( ar\sin\theta \right)^{2} = (ab)^{2}$

> $\text{提出}r\text{整理即得。又有}r = \frac{ab}{\sqrt{\left( a\cos\theta \right)^{2} + \left( b\sin\theta \right)^{2}}} = \frac{b}{\sqrt{1 - \left( e\cos\theta \right)^{2}}}$

过原点的直线：$\theta = \theta_{0}$，$\theta_{0}$为倾斜角

$\text{不过原点的直线：}r = - \frac{C}{A\cos\theta + B\sin\theta}$

> 由直线的方程$Ax + By + C = 0$，代入$x = r\cos\theta$，$y = r\sin\theta$得

$Ar\cos\theta + Br\sin\theta + C = 0\text{，即}$

$r = - \frac{C}{A\cos\theta + B\sin\theta}$

$\text{圆锥曲线统一方程的极坐标形式：}r = \frac{ep}{1 - e\cos\theta}$

其中$p$为焦点到准线的距离（焦准距），圆锥曲线的焦点在极点（极坐标下的“原点”）上。

证：由

$e = \frac{r}{p + r\cos\theta}$

即得

蝴蝶定理

在圆锥曲线中，过弦$PQ$的中点$M$作两条弦$AB$、$CD$，过$A$、$B$、$C$、$D$的二次曲线（包括退化情形）交$PQ$与点$E$、$F$，则$ME = MF$

证明：以$M$为原点，$MP$所在直线为$x$轴，设$P(m\text{，}0)$，$Q( - m\text{，}0)$，且过这六点的圆锥曲线方程为

$Ax^{2} + Bxy + Cy^{2} + Dx + Ey + F = 0$

把$P(m\text{，}0)$和$Q( - m\text{，}0)$代入，得，$F = - Am^{2}$，$D = 0$不妨设$A = 1$，则所设圆锥曲线方程化为

$x^{2} + Bxy + Cy^{2} + Ey - m^{2} = 0$

设直线$AB:x = k_{1}y$，$CD:x = k_{2}y$，那么经过$A$、$B$、$C$、$D$的二次曲线系方程为

$x^{2} + Bxy + Cy^{2} + Ey - m^{2} + \lambda\left( x_{1} - ky_{1} \right)\left( x - k_{2}y \right) = 0$

由两条直线是退化的二次曲线，当$y = 0$时，方程$(1 + \lambda)x^{2} = m^{2}$的两根为$x_{E}\text{，}x_{F}$，由根与系数的关系，得$x_{E} + x_{F} = 0$，所以$ME = MF$。

幂

圆幂与根轴

> ![](/images/hs/hs-b08/img01.png)点对圆的幂
>
> 若圆C外有一点P，CP交圆与点M，定义

$PM^{2} = CP^{2} - r^{2}$

> 为点P对圆C的幂
>
> 圆幂定理
>
> 对平面内任意一点P作C的割线交C与A、B两点，则

$PA \cdot PB = CP^{2} - r^{2} = PM^{2}$

> 根轴
>
> 定义：到两圆等幂的点集是一条直线，该直线叫根轴
>
> 根心定理（蒙日定理）
>
> 三个圆两两的根轴或交于一点，或互相平行，或全部重合。

圆幂与圆幂定理在圆锥曲线的推广

> 椭圆的幂定理
>
> 过平面内任意一点P作椭圆$C_{1}$的割线交与A、B两点，OQ为平行于AB的半径，则定义

$\frac{PA \cdot PB}{OQ^{2}} = \frac{x_{0}^{2}}{a^{2}} + \frac{y_{0}^{2}}{b^{2}} - 1\$

> 为点P对椭圆$C_{1}$的幂。
>
> 双曲线的幂定理
>
> 过平面内任意一点P作双曲线$C_{1}$的割线交与A、B两点，OQ为平行于AB的半径，则定义

$\frac{PA \cdot PB}{OQ^{2}} = \frac{x_{0}^{2}}{a^{2}} - \frac{y_{0}^{2}}{b^{2}} - 1\$

> 为点P对双曲线$C_{1}$的幂。
>
> 抛物线的幂定理
>
> 过平面内任意一点P作抛物线$C_{1}$的割线交与A、B两点，$l$为平行于AB的焦点弦CD的长，则定义

$\frac{PA \cdot PB}{l^{2}} = \frac{y_{0}^{2}}{2p} - x_{0}$

> ![图片包含 游戏机 描述已自动生成](/images/hs/hs-b08/img02.png)为点P对抛物线的幂。

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

圆锥曲线

</th>
<th>

$\frac{x^{2}}{m} + \frac{y^{2}}{n} = 1$

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

幂

</td>
<td>

$\frac{x_{0}^{2}}{m} + \frac{y_{0}^{2}}{n} - 1$

</td>
<td>

$\frac{y_{0}^{2}}{2p} - x_{0}$

</td>
<td>

$\frac{x_{0}^{2}}{2p} - y_{0}$

</td>
</tr>
</tbody>
</table>
</div>

> 某点对于某圆锥曲线的圆锥曲线幂为定值。

圆锥曲线有如下性质

1.圆锥曲线的内接三角形，每个顶点的切线与其对边的交点共线。

2.圆锥曲线的外切三角形，每条边的切点与其对顶点的连线共点。

极线与极点

定义

> 代数定义
>
> 设有圆锥曲线$\Gamma(x\text{，}y) = Ax^{2} + Bxy + Cy^{2} + Dx + Ey + F = 0$，点$P(x_{0}\text{，}y_{0})$，则称

$Ax_{0}x + B\frac{\left( x_{0}y + y_{0}x \right)}{2} + Cy_{0}y + D\frac{x_{0} + x}{2} + E\frac{y_{0} + y}{2} + F = 0$

> 为极点P对应的极线，同时称点P是该线对应的极点。
>
> 在平常研究的范围内，椭圆和双曲线的方程可写为$Ax^{2} + Cy^{2} + F = 0$，其对应的极线为

$Ax_{0}x + Cy_{0}y + F = 0$

> 几何定义
>
> 如图，设$P$是不在圆锥曲线上的点，过$P$点引两条割线依次交圆锥曲线于四点$E$、$F$、$G$、$H$，连接$EH$、$FG$交于$N$，连接$EH\text{，}FG$交于$N$，连接$EG\text{，}FH$交于$M$，则直线$MN$为点$P$对应的极线．若$P$为圆锥曲线上的点，则过$P$点的切线即为极线。
>
> 同理$PM$为点$N$对应的极线，$PN$为点$M$对应的极线，$\Delta MNP$称为自极三点形。若连接$MN$交圆锥曲线于点$A$、$B$，则$PA,PB$恰为圆锥曲线的切线。
>
> 圆锥曲线内接四边形对角线的交点、相对两边的延长线的两个交点，三点连线得到的图形是自极三点形。
>
> 圆锥曲线关于某点的极线与该点为切点的切线相同
>
> 特殊的极点与极线

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

圆锥曲线($C_{1}$)

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

点$M(m\text{，}0)$对应的极线

</td>
<td colspan="2">

$x = \frac{a^{2}}{m}$

</td>
<td>

$x = - m$

</td>
</tr>
</tbody>
</table>
</div>

极点与极线的性质

1.设有圆锥曲线$\Gamma(x\text{，}y) = Ax^{2} + Bxy + Cy^{2} + Dx + Ey + F = 0$，点$P(x_{0}\text{，}y_{0})$

> （1）当$P$在圆锥曲线$\Gamma$上时，其极线是曲线$\Gamma$在$P$点处的切线。

（2）当$P$在$\Gamma$外时，其极线是曲线$\Gamma$从点$P$所引两条切线的切点所确定的直线（即切点弦所在直线）。

（3）当$P$在$\Gamma$内时，其极线是曲线$\Gamma$过点$P$的割线两端点处的切线交点的轨迹。

> 下面给出证明：
>
> （1）对二次曲线$Ax^{2} + Bxy + Cy^{2} + Dx + Ey + F = 0$两边关于$x$求导，得

$2Ax + B\left( y + xy' \right) + 2Cyy' + D + Ey' = 0$

> 取点$P(x_{0}\text{，}y_{0})$，得

$2Ax_{0} + B\left( y_{0} + x_{0}y' \right) + 2Cy_{0}y' + D + Ey' = 0$

> 可得点$P$处切线的斜率

$y'\left| \underset{x = x_{0},y = y_{0}}{} \right.\  = - \frac{2Ax_{0} + By_{0} + D}{Bx_{0} + 2Cy_{0} + E}$

> 可得点$P$处的切线方程为

$y - y_{0} = y'\left| \underset{x = x_{0},y = y_{0}}{} \right.\ \left( x - x_{0} \right)$

> 整理，得

$2Ax_{0}x + B\left( x_{0}y + y_{0}x \right) + 2Cy_{0}y - 2Ax_{0}^{2} - 2Bx_{0}y_{0} - 2Cy_{0}^{2} + Dx + Ey - Dx_{0} - Dx_{0} - Ey_{0} = 0$

> 即

$Ax_{0}x + B\frac{\left( x_{0}y + y_{0}x \right)}{2} + Cy_{0}y - Ax_{0}^{2} - Bx_{0}y_{0} - Cy_{0}^{2} + D\frac{x}{2} + E\frac{y}{2} - D\frac{x_{0}}{2} - E\frac{y_{0}}{2} = 0$

> 因为点P在二次曲线$Ax^{2} + Bxy + Cy^{2} + Dx + Ey + F = 0$上，所以

$Dx_{0} + Ey_{0} + F = - Ax_{0}^{2} - Bx_{0}y_{0} - Cy_{0}^{2}$

> 代入上式，得

$Ax_{0}x + B\frac{\left( x_{0}y + y_{0}x \right)}{2} + Cy_{0}y + Dx_{0} + Ey_{0} + F + D\frac{x}{2} + E\frac{y}{2} - D\frac{x_{0}}{2} - E\frac{y_{0}}{2} = 0$

> 整理，得

$Ax_{0}x + B\frac{\left( x_{0}y + y_{0}x \right)}{2} + Cy_{0}y + D\frac{x_{0} + x}{2} + E\frac{y_{0} + y}{2} + F = 0$

> （2）设切点$M(x_{1}\text{，}y_{1})\text{，}N(x_{2}\text{，}y_{2})$，由切线公式，得

$\left\{ \begin{array}{r} Ax_{1}x + B\frac{\left( x_{1}y + y_{1}x \right)}{2} + Cy_{1}y + D\frac{x_{1} + x}{2} + E\frac{y_{1} + y}{2} + F = 0 \\ Ax_{2}x + B\frac{\left( x_{2}y + y_{2}x \right)}{2} + Cy_{2}y + D\frac{x_{2} + x}{2} + E\frac{y_{2} + y}{2} + F = 0 \end{array} \right.\$

> 因为点$P$在这两条切线上，代入得

$\left\{ \begin{array}{r} Ax_{1}x_{0} + B\frac{\left( x_{1}y_{0} + y_{1}x_{0} \right)}{2} + Cy_{1}y_{0} + D\frac{x_{1} + x_{0}}{2} + E\frac{y_{1} + y_{0}}{2} + F = 0 \\ Ax_{2}x_{0} + B\frac{\left( x_{2}y_{0} + y_{2}x_{0} \right)}{2} + Cy_{2}y_{0} + D\frac{x_{2} + x_{0}}{2} + E\frac{y_{2} + y_{0}}{2} + F = 0 \end{array} \right.\$

> 考虑直线

$Ax_{0}x + B\frac{\left( x_{0}y + y_{0}x \right)}{2} + Cy_{0}y + D\frac{x_{0} + x}{2} + E\frac{y_{0} + y}{2} + F = 0$

> 根据上式能够发现，点$M$，$N$在该直线上，由两点确定一条直线，可得该直线（极线）即切点弦所在直线。
>
> （3）设过P的割线交圆锥曲线于点$M(x_{1}\text{，}y_{1})\text{，}N(x_{2}\text{，}y_{2})$，由切线公式，可得

$\left\{ \begin{array}{r} Ax_{1}x + B\frac{\left( x_{1}y + y_{1}x \right)}{2} + Cy_{1}y + D\frac{x_{1} + x}{2} + E\frac{y_{1} + y}{2} + F = 0 \\ Ax_{2}x + B\frac{\left( x_{2}y + y_{2}x \right)}{2} + Cy_{2}y + D\frac{x_{2} + x}{2} + E\frac{y_{2} + y}{2} + F = 0 \end{array} \right.\$

> 设这两条切线的交点为$Q(m,n)$，则

$\left\{ \begin{array}{r} Ax_{1}m + B\frac{\left( x_{1}n + y_{1}m \right)}{2} + Cy_{1}n + D\frac{x_{1} + m}{2} + E\frac{y_{1} + n}{2} + F = 0 \\ Ax_{2}m + B\frac{\left( x_{2}n + y_{2}m \right)}{2} + Cy_{2}n + D\frac{x_{2} + m}{2} + E\frac{y_{2} + n}{2} + F = 0 \end{array} \right.\$

> 考虑直线

$Axm + B\frac{(xn + ym)}{2} + Cyn + D\frac{x + m}{2} + E\frac{y + n}{2} + F = 0$

> 发现点M，N在该直线上，故该直线也过点P，代入坐标得

$Ax_{0}m + B\frac{\left( x_{0}n + y_{0}m \right)}{2} + Cy_{0}n + D\frac{x_{0} + m}{2} + E\frac{y_{0} + n}{2} + F = 0$

> 因此，点Q在直线

$Ax_{0}x + B\frac{\left( x_{0}y + y_{0}x \right)}{2} + Cy_{0}y + D\frac{x_{0} + x}{2} + E\frac{y_{0} + y}{2} + F = 0$

> 上，即点Q恒在极线上，得证
>
> 2.配极原理：若点P在点Q的极线上，则点Q在点P的极线上，且称点P与点Q调和共轭
>
> 共线点的极线必共点，且所共线为所共点的极线；共点线的极点必共线，且所共点为所共线的极点。
>
> 证明：设$P(x_{1}\text{，}y_{1})\text{，}Q(x_{2}\text{，}y_{2})$，则点P的极线为

$Ax_{1}x + B\frac{\left( x_{1}y + y_{1}x \right)}{2} + Cy_{1}y + D\frac{x_{1} + x}{2} + E\frac{y_{1} + y}{2} + F = 0$

> 点Q的极线为

$Ax_{2}x + B\frac{\left( x_{2}y + y_{2}x \right)}{2} + Cy_{2}y + D\frac{x_{2} + x}{2} + E\frac{y_{2} + y}{2} + F = 0$

> 因为点P在点Q的极线上，所以

$Ax_{1}x_{2} + B\frac{\left( x_{1}y_{2} + y_{1}x_{2} \right)}{2} + Cy_{1}y_{2} + D\frac{x_{1} + x_{2}}{2} + E\frac{y_{1} + y_{2}}{2} + F = 0$

> 与点P的极线方程式对比，发现点Q在点P的极线上。
>
> 3.设点$P$关于圆锥曲线$\Gamma$的极线为$l$，过点$P$任作一割线交$\Gamma$于$A$、$B$，交$l$于$Q$，则$\frac{PA}{PB} = \frac{QA}{QB}$，这时称$P,Q$调和分割线段$AB$，或称$P\text{与}Q$关于$\Gamma$调和共轭。
>
> 4.设点$P$关于圆锥曲线$\Gamma$的调和共轭点为$Q$，则有$\frac{2}{PQ} = \frac{1}{PA} + \frac{1}{PB}$，反之也成立．即$\frac{PA}{PB} = \frac{QA}{QB} \Leftrightarrow \frac{2}{PQ} = \frac{1}{PA} + \frac{1}{PB}$
>
> 证明：$\frac{PA}{PB} = \frac{QA}{QB} \Leftrightarrow \frac{PA}{PB} = \frac{PQ - PA}{PB - PQ} \Leftrightarrow PA \bullet PB - PA \bullet PQ = PQ \bullet PB - PA \bullet PB \Leftrightarrow 2PA \bullet PB = PQ \bullet (PA + PB) \Leftrightarrow \frac{2}{PQ} = \frac{1}{PA} + \frac{1}{PB}$
>
> 5.设点$P$关于有心圆锥曲线$\Gamma$（设其中心为$O$）的调和共轭点为$Q$，直线$PQ$经过圆锥曲线的中心，则有$OR^{2} = OP \cdot OQ$，反之，若有$OR^{2} = OP \cdot OQ$成立，则点$P$与$Q$关于$\Gamma$调和共轭。
>
> 证明：设直线$PQ$与$\Gamma$的另一交点为$R'$，若$\frac{PR}{PR'} = \frac{QR}{QR'} \Rightarrow \frac{OP - OR}{OP + OR'} = \frac{OR - OQ}{OR' + OQ}(\because OR = OR')$，化简即得$OR^{2} = OP \bullet OQ$；反之也成立。
>
> 6.$A,B$是圆锥曲线$\Gamma$的一条对称轴$l$上的两点（不在$\Gamma$上），若$A,B$关于$\Gamma$调和共轭，过$B$任作$\Gamma$的一条割线，交$\Gamma$于$P,Q$两点，则$\angle PAB = \angle QAB$。
>
> 证明：因$\Gamma$关于直线$l$对称，故在$\Gamma$上存在$P,Q$的对称点$P',Q'$。若$P'$与$Q$重合，则$Q'\text{与}P$也重合，此时$P,Q$关于$l$对称，有$\angle PAB = \angle QAB$；若$P'\text{与}Q$不重合，则$Q'$与$P$也不重合，由于$A,B$关于$\Gamma$调和共轭，故$A,B$为$\Gamma$上完全四点形$PQ'QP'$的对边交点，即$Q'$在$PA$上，故$AP,AQ$关于直线$l$对称，也有$\angle PAB = \angle QAB$。

![](/images/hs/hs-b08/img03.png)

> 7.设圆锥曲线$\Gamma$的一个焦点为$F$，与$F$相应的准线为$l$。
>
> （1）若过点$F$的直线与圆锥曲线$\Gamma$相交于$M$、$N$两点，则$\Gamma$在$M$、$N$两点处的切线的交点$Q$在准线$l$上，且$FQ\bot MN$；
>
> （2）若过准线$l$上一点$Q$作圆锥曲线$\Gamma$的两条切线，切点分别为$M$、$N$，则直线$MN$过焦点$F$，且$FQ\bot MN$；
>
> （3）若过焦点的直线与圆锥曲线$\Gamma$相交于$M$、$N$两点，过$F$作$FQ\bot MN$交准线$l$于$Q$，则连线$QM$、$QN$是$\Gamma$的两条切线。
>
> 证明：$\text{对于}\left. \text{（}1 \right.\text{）中椭圆的情形，设}\Gamma:\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1(a > b > 0),F(c,0),l:x = \frac{a^{2}}{c}\text{，由于焦点}F\text{的极线为}l\text{，故切线}MQ,NQ\text{的交点}Q\text{一定在直线}l\text{上，设}Q\left( \frac{a^{2}}{c},y_{Q} \right)\text{，则点}Q\text{的极线为}\frac{\frac{a^{2}}{c}x}{a^{2}} + \frac{y_{Q}y}{b^{2}} = 1\text{，即}y = - \frac{b^{2}}{cy_{Q}}(x - c)\therefore k_{MN} = - \frac{b^{2}}{cy_{Q}}\text{，又}\ k_{FQ} = \frac{y_{Q} - 0}{\frac{a^{2}}{c} - c} = \frac{cy_{Q}}{a^{2} - c^{2}} = \frac{cy_{Q}}{b^{2}}\therefore k_{MN} \bullet k_{FQ} = - 1\text{，}\therefore MN\bot FQ$

二次曲线

一般地，方程

$\Gamma(x\text{，}y) = Ax^{2} + Bxy + Cy^{2} + Dx + Ey + F = 0$

表示圆锥曲线（（椭）圆、双曲线和抛物线）或两条直线（叫做退化的二次曲线）。（实际上还可以表示一条直线或点）

二次曲线有齐次化设法，其方程为

$Ax^{2} + 2Bxy + Cy^{2} + 2Dx + 2Ey + F = 0$

通过坐标轴平移或旋转，可以得到二次曲线的几种类型

> $1.\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1(\text{椭圆（和圆）})$
>
> $2.\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = - 1(\text{虚椭圆（没有任何点满足该方程）})$
>
> $3.\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} = 1(\text{双曲线})$
>
> $4.\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 0(\text{点或相交于实点的共轭虚直线（即一个点）})$
>
> $5.\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} = 0(\text{两相交直线（不重合）})$
>
> $6.y^{2} = 2px(\text{抛物线})$
>
> $7.y^{2} = a^{2}(\text{两平行直线（不重合）})$
>
> $8.y^{2} = - a^{2}(\text{两平行共轭虚直线（没有任何点满足该方程）})$
>
> $9.y^{2} = 0(\text{两重和直线（即一条直线）})$

也可以通过对二次曲线一般式（$Ax^{2} + 2Bxy + Cy^{2} + 2Dx + 2Ey + F = 0$）的讨论，得到二次曲线的几种类型

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$\delta > 0$

</th>
<th>

$\Delta = 0$

</th>
<th></th>
<th>

有一实点的相交虚[直线](https://baike.baidu.com/item/%E7%9B%B4%E7%BA%BF/4876?fromModule=lemma_inlink)

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\delta > 0$

</td>
<td>

$\Delta \neq 0$

</td>
<td>

$\Delta S$

</td>
<td>

椭圆

</td>
</tr>
<tr>
<td>

$\delta > 0$

</td>
<td>

$\Delta \neq 0$

</td>
<td>

$\Delta S > 0$

</td>
<td>

虚椭圆

</td>
</tr>
<tr>
<td>

$\delta$

</td>
<td>

$\Delta = 0$

</td>
<td></td>
<td>

相交直线

</td>
</tr>
<tr>
<td>

$\delta$

</td>
<td>

$\Delta \neq 0$

</td>
<td></td>
<td>

双曲线

</td>
</tr>
<tr>
<td>

$\delta = 0$

</td>
<td>

$\Delta \neq 0$

</td>
<td></td>
<td>

抛物线

</td>
</tr>
<tr>
<td>

$\delta = 0$

</td>
<td>

$\Delta = 0$

</td>
<td>

$D² + E² - AF - CF$

</td>
<td>

平行直线

</td>
</tr>
<tr>
<td>

$\delta = 0$

</td>
<td>

$\Delta = 0$

</td>
<td>

$D² + E² - AF - CF = 0$

</td>
<td>

重合直线

</td>
</tr>
<tr>
<td>

$\delta = 0$

</td>
<td>

$\Delta = 0$

</td>
<td>

$D² + E² - AF - CF > 0$

</td>
<td>

平行虚直线

</td>
</tr>
</tbody>
</table>
</div>

$\text{其中}\Delta = \left| \begin{matrix} A & B & D \\ B & C & E \\ D & E & F \end{matrix} \right|\text{，}\delta = \left| \begin{matrix} A & B \\ B & C \end{matrix} \right|\text{，}S = A + C$

二次曲线的中心由方程

$\left\{ \begin{array}{r} \\ \end{array} \right.\$

圆锥曲线的统一方程（不包含圆）

1.

$e\left| (x - g)\cos\alpha + (y - h)\sin\alpha + p \right| - \sqrt{(x - g)^{2} + (y - h)^{2}} = 0$

$\text{其中}\alpha \in \lbrack 0,2\pi)\text{，}p > 0\text{，}e \geq 0\text{。}$

$1.0 < e < 1$

> $\text{表示以}F(g\text{，}h)\text{为一个焦点，}p\text{为焦点到准线距离，}e\text{为离心率的椭圆。其中}\overrightarrow{AF}\text{与极轴夹角}\alpha \text{。}$

$2.e > 1$

> $\text{表示以}F(g\text{，}h)\text{为一个焦点，}p\text{为焦点到准线距离，}e\text{为离心率的双曲线。其中}\overrightarrow{AF}\text{与极轴夹角}\alpha \text{。}$

$3.e = 1$

> $\text{表示以}F(g\text{，}h)\text{为焦点，}p\text{为焦点到准线距离的抛物线。其中}\overrightarrow{AF}\text{与极轴夹角}\alpha\left. \text{（}A\text{为抛物线顶点} \right.\text{）。}$

$4.e = 0$

> $\text{表示点}F(g\text{，}h)\text{。}$

当$e \neq 0$时，$F(g\text{，}h)$对应准线方程

$\frac{x}{\tan\alpha} + y + p\sqrt{1 + \frac{1}{\tan\alpha}} - \frac{g}{\tan\alpha} - h = 0$

2.

$\left( 1 - e^{2} \right)x^{2} + y^{2} - 2pe^{2}x - p^{2}e^{2} = 0$

其中焦点位于原点，p为焦准距，准线与x轴垂直。

证明：设$P(x\text{，}y)$为圆锥曲线上一点，由焦点在原点上，得到准线方程$x = - p$，则由第二定义，有

$e = \frac{\sqrt{x^{2} + y^{2}}}{|x + p|}$

两边平方整理即得。

二次曲线系

定理1：

给定五点，其中三点在直线l上，另外两点不在l上，则经过这五点的二次曲线是唯一的，并且是退化的二次曲线（即两条直线）

定理2：

给定五点，其中任何三点都不共线，则过此五点有且仅有一条二次曲线。

结论1：

过两个二次曲线$F_{1}(x\text{，}y)\text{、}F_{2}(x\text{，}y)$的四个不同交点的曲线系为

$F_{1}(x\text{，}y) + \lambda F_{2}(x\text{，}y) = 0$

结论2：

过两条直线l<sub>1</sub>、l<sub>2</sub>与二次曲线$F(x\text{，}y)$的四个不同交点的曲线系为

$F(x\text{，}y) + \lambda\left( A_{1}x + B_{1}y + C_{1} \right)\left( A_{2}x + B_{2}y + C_{2} \right) = 0$

结论3：

若有三条直线$f_{1}(x\text{，}y)\text{，}f_{2}(x\text{，}y)\text{，}f_{3}(x\text{，}y)$，则它们围成的三角形的三个定点所在曲线系为

$\lambda_{1}f_{1}(x\text{，}y) + \lambda_{2}f_{2}(x\text{，}y) + \lambda_{3}f_{3}(x\text{，}y) = 0$

结论4：

若有四条直线$f_{1}(x\text{，}y)\text{，}f_{2}(x\text{，}y)\text{，}f_{3}(x\text{，}y)\text{，}f_{4}(x\text{，}y)$，则它们围成的四边形的四个定点所在曲线系为

$f_{1}(x\text{，}y)f_{2}(x\text{，}y) + \lambda f_{3}(x\text{，}y)f_{4}(x\text{，}y) = 0$

其中$f_{1}\text{、}f_{2}$是对边，$f_{3}\text{、}f_{4}$是对边

两条直线l<sub>1</sub>、l<sub>2</sub>可表示为$\left( A_{1}x + B_{1}y + C_{1} \right)\left( A_{2}x + B_{2}y + C_{2} \right) = 0$

> 应用：定点定值问题点在圆锥曲线的情形

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

圆锥曲线（$C_{1}$）

</th>
<th>

直线AB的方程

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

椭圆

</td>
<td>

$k_{1}k_{2}\left( \frac{a^{2}}{b^{2}}y_{0}y - x_{0}x + a^{2} \right) + \left( k_{1} + k_{2} \right)\left( x_{0}y + y_{0}x \right) + \left( \frac{b^{2}}{a^{2}}x_{0}x - y_{0}y + b^{2} \right) = 0$

</td>
</tr>
<tr>
<td>

双曲线

</td>
<td>

$k_{1}k_{2}\left( - \frac{a^{2}}{b^{2}}y_{0}y - x_{0}x + a^{2} \right) + \left( k_{1} + k_{2} \right)\left( x_{0}y + y_{0}x \right) - \left( \frac{b^{2}}{a^{2}}x_{0}x + y_{0}y + b^{2} \right) = 0$

</td>
</tr>
<tr>
<td>

$\frac{x^{2}}{m} + \frac{y^{2}}{n} = 1$

</td>
<td>

$k_{1}k_{2}\left( \frac{m}{n}y_{0}y - x_{0}x + m \right) + \left( k_{1} + k_{2} \right)\left( x_{0}y + y_{0}x \right) + \left( \frac{n}{m}x_{0}x - y_{0}y + n \right) = 0$

</td>
</tr>
<tr>
<td>

$\frac{x^{2}}{m} + \frac{y^{2}}{n} = 1$

</td>
<td>

$mk_{1}k_{2}\left( my_{0}y - nx_{0}x + mn \right) + mn\left( k_{1} + k_{2} \right)\left( x_{0}y + y_{0}x \right) + m\left( nx_{0}x - my_{0}y + nn \right) = 0$

</td>
</tr>
<tr>
<td>

抛物线

</td>
<td>

$\frac{k_{1}k_{2}}{2p^{2}}\left( y_{0}y + px + x_{0}x \right) - \frac{k_{1} + k_{2}}{2p}\left( y + y_{0} \right) + 1 = 0$

</td>
</tr>
</tbody>
</table>
</div>

> 已知$k_{1} + k_{2}$或$k_{1}k_{2}$时，代入其中，得到一个含参（$k_{1}k_{2}$或$k_{1} + k_{2}$）一元二次方程，使含参项和不含参项分别等于0，得到定点坐标。
>
> 特别地，当$k_{1} + k_{2} = 0$时，设$\alpha = \frac{\pi - \angle APB}{2}$，有

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

$S_{\bigtriangleup APB}$

</td>
<td colspan="2">

$\frac{4\left| y_{0}^{2}a^{4}\tan^{3}\alpha - x_{0}^{2}b^{4}\tan\alpha \right|}{\left( a^{2}\tan^{2}\alpha + b^{2} \right)^{2}}$

</td>
<td>

$\frac{4\left| p^{2} - y_{0}^{2}\tan^{2}\alpha \right|}{\tan^{3}\alpha}$

</td>
</tr>
</tbody>
</table>
</div>

二次曲线的其它性质

> 二次曲线的焦点弦两端的切线交点与该焦点的连线垂直于该焦点弦。

阿基米德三角形

设AB是圆锥曲线上的两点，则这两点与过两点的切线围成则两点切线交点与这两点连线围成的图形叫阿基米德三角形，特别地，如果两点连线过焦点，则叫阿基米德焦点三角形。

阿基米德三角形的性质

![](/images/hs/hs-b08/img04.png)当阿基米德三角形的弦边对应角为直角，则该角顶点的轨迹为蒙日圆

阿基米德焦点三角形的特有性质

阿基米德焦点三角形弦边对应点在准线上

$\text{阿基米德焦点三角形面积的最小值为：椭圆}/\text{双曲线：}\frac{b^{4}}{ac}\text{；抛物线：}p^{2}$

其它

1.已知双曲线$C:\frac{x^{2}}{a} - \frac{y^{2}}{b} = 1$的右焦点为F，点A为双曲线在第一象限上的一点，且$AF\bot x$轴，过A作双曲线的两条渐近线的平行线与双曲线的渐近线交于M、N两点，则四边形$OMAN$的面积为$\frac{ab}{2}$

2.己知双曲线$C:\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} = 1(a > 0,b > 0)$的左、右焦点分别为$F_{1}$、$F_{2}$，过$F_{1}$的直线与双曲线的一条渐近线交于点P，且$PF_{1}\bot PF_{2}$，直线$PF_{1}$与双曲线的另一渐近线交于点Q，若$\overrightarrow{F_{1}Q} = 2\overrightarrow{QP}$，则双曲线的离心率为$4$

3.已知双曲线$C:\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} = 1(a > 0,b > 0)$的左、右焦点分别为$F_{1}$、$F_{2}$，过$F_{1}$且斜率为$m$的直线与双曲线*C*的渐近线在第一象限交于点P，若$PF_{1}\bot PF_{2}$，则双曲线的离心率为$\frac{1 - m^{2}}{m^{2} + 1}$

4. 已知双曲线$C:\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} = 1$的右焦点为F，过F且与x轴垂直的直线与双曲线交于A、B两点，则A、B两点到双曲线的一条渐近线的距离之和为$2b$

5.过椭圆C外一点作两条切线，切点分别为A，B，则$PF_{1}$平分$\angle AF_{1}B$，$PF_{2}$平分$\angle AF_{2}B$（图在上面）

调和点列

$\text{调和点列：若直线}l\text{上四个点}A\text{，}B\text{，}C\text{，}D\ \text{满足}\frac{AB}{BC} = \frac{AD}{DC}\text{，则称}A\text{，}C\text{；}B\text{，}D\text{是一组调和点列}$

$\text{调和线束：四条直线}l_{1}\text{到}l_{4}\text{交于一点，若}\frac{\sin\alpha_{12}}{\sin\alpha_{23}} = \frac{\sin\alpha_{14}}{\sin\alpha_{43}}\text{，则称}l_{1}\text{，}l_{3}\text{；}l_{2}\text{，}l_{4}\text{是一簇调和线束}$

$\text{调和点列与调和线束的转换：若直线上有四个点}A\text{，}B\text{，}C\text{，}D\text{，直线外有一点}P\text{，则}A\text{，}C\text{；}B\text{，}D\text{调和} \Leftrightarrow PA\text{，}PC\text{；}PB\text{，}PD\text{调和}\left( \frac{AB}{BC} = \frac{AD}{DC} \Leftrightarrow \frac{\sin{\angle APB}}{\sin{\angle BPC}} = \frac{\sin{\angle APD}}{\sin{\angle DPC}} \right)$

> 证明：
>
> 由正弦定理，得

$\frac{AB}{\sin{\angle APB}} = \frac{AP}{\sin{\angle ABP}}\text{，}\frac{BC}{\sin{\angle BPC}} = \frac{CP}{\sin{\angle CBP}}$

> 两式相除，化简得

$\frac{AB \cdot CP}{BC \cdot AP} = \frac{\sin{\angle CBP}\sin{\angle APB}}{\sin{\angle ABP}\sin{\angle BPC}}$

> 因为$\angle CBP + \angle ABP = \pi$，所以$\sin{\angle CBP} = \sin{\angle ABP}$，所以

$\frac{AB}{BC} = \frac{\sin{\angle APB} \cdot AP}{\sin{\angle BPC} \cdot CP}\text{，同理}\frac{AD}{DC} = \frac{\sin{\angle APD} \cdot AP}{\sin{\angle DPC} \cdot CP}$

$\frac{AB}{BC} = \frac{AD}{DC} \Rightarrow \frac{\sin{\angle APB} \cdot AP}{\sin{\angle BPC} \cdot CP} = \frac{\sin{\angle APD} \cdot AP}{\sin{\angle DPC} \cdot CP} \Rightarrow \frac{\sin{\angle APB}}{\sin{\angle BPC}} = \frac{\sin{\angle APD}}{\sin{\angle DPC}}$

$\text{圆锥曲线上有}A\text{，}B\text{两点，若}P\text{，}Q\text{；}A\text{，}B\text{是调和点列}\left( \frac{PQ}{QA} = \frac{PB}{BA} \right)\text{，则}P\text{，}Q\text{关于圆锥曲线调和共轭}$

$\text{若}A_{1}A_{2}B_{1}B_{2}\text{在圆锥曲线上，}A_{1}B_{1} \cap A_{2}B_{2} = P\text{，}A_{1}B_{2} \cap A_{2}B_{1} = Q\text{，则}P\text{和}Q\text{调和共轭}$

无穷远点：每条直线上有且只有一个无穷远点，并被无穷远点连接成为封闭曲线；所有相互平行的直线相交于一个无穷远点，无穷远点代表直线的方向。

图象平移与齐次化

$\text{令}x' = x - x_{0}\text{，}y' = y - y_{0}\text{，则圆锥曲线方程为}$

$\ \frac{\left( x' + x_{0} \right)^{2}}{m} + \frac{\left( y' + y_{0} \right)^{2}}{n} = 1$

$\text{因为点}P\text{满足}\frac{x_{0}^{2}}{m} + \frac{y_{0}^{2}}{n} = 1\text{，代入，将上述圆锥曲线方程化简得}$

$\frac{{x'}^{2}}{m} + \frac{2x_{0}x'}{m} + \frac{{y'}^{2}}{n} + \frac{2y_{0}y'}{n} = 0$

设$AB$方程为$px' + qy' = 1$，则有（齐次化，使第二项和第四项的次数变为2）

$\frac{{x'}^{2}}{m} + \frac{2x_{0}x'}{m}\left( px' + qy' \right) + \frac{{y'}^{2}}{n} + \frac{2y_{0}y'}{n}\left( px' + qy' \right) = 0$

整理，得

$\frac{1 + 2px_{0}}{m}{x'}^{2} + \left( \frac{2qx_{0}}{m} + \frac{2py_{0}}{n} \right)x'y' + \frac{1 + 2qy_{0}}{n}{y'}^{2} = 0$

两边同时除以${x'}^{2}$，得

$\frac{1 + 2qy_{0}}{n}\left( \frac{y'}{x'} \right)^{2} + \frac{2qnx_{0} + 2pmy_{0}}{mn}\left( \frac{y'}{x'} \right) + \frac{1 + 2px_{0}}{m} = 0$

由韦达定理得

$\left\{ \begin{array}{r} \lambda = k_{1} + k_{2} = \frac{y_{1}'}{x_{1}} + \frac{y_{2}'}{x_{2}} = - \frac{2my_{0}p + 2nx_{0}q}{m + 2my_{0}q} \\ \mu = \ k_{1} \cdot k_{2}\  = \frac{y_{1}'}{x_{1}'}\  \cdot \ \frac{y_{2}'}{x_{2}'} = \frac{n + 2nx_{0}p}{m + 2my_{0}q}\ \ \ \ \ \ \ \ \ \ \ \ \  \\ \nu = \frac{1}{k_{1}} + \frac{1}{k_{2}} = \frac{k_{1} + k_{2}}{k_{1} \cdot k_{2}} = \frac{2qnx_{0} + 2pmy_{0}}{n + 2pny_{0}}\ \ \ \ \end{array} \right.\$

下面证明$k_{1} + k_{2} = \lambda$的情况，其余类似可证

由上式，得

$p = - \frac{\lambda m + 2my_{0}q\lambda + 2nx_{0}q}{2my_{0}}$

代入$px' + qy' = 1$，提出$q$，得

> $- q\left( 2my_{0}\lambda x' + 2nx_{0}x' - 2my_{0}y' \right) - \lambda mx' - 2my_{0} = 0$

由此得到两个方程

$\left\{ \begin{array}{r} 2my_{0}\lambda x' + 2nx_{0}x' - 2my_{0}y' = 0 \\ \lambda mx' + 2my_{0} = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

解得

$\left\{ \begin{array}{r} x' = - \frac{2y_{0}}{\lambda}\ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ y' = - 2y_{0} - \frac{2x_{0}n}{\lambda m} \end{array} \right.\ \text{，故}\left\{ \begin{array}{r} x = x_{0} - \frac{2y_{0}}{\lambda}\ \ \ \ \ \ \ \  \\ y = - y_{0} - \frac{2x_{0}}{\lambda}\frac{n}{m} \end{array} \right.\$

此模型解题步骤：

1.设直线AB的方程为$y = kx + m\text{或}x = ty + n$，与圆锥曲线方程联立得到根与系数关系，$\Delta$求出参数范围；

2.由AP与BP关系（如$k_{AP} \cdot k_{BP} = - 1$），得到$x_{1}\text{，}x_{2}\text{，}y_{1}\text{，}y_{2}$四个参量的关系，代入之前得到的韦达定理，得到关于$k\text{和}m\text{（}t\text{和}n\text{）}$的方程

3.如果为一次方程，直接分离参量代入AB方程得出定点坐标；如果为二次方程，利用结论得出定点坐标，将定点坐标代入AB方程得到$k\text{和}m\text{（}t\text{和}n\text{）}$的关系，将该关系作为一个已知因式对上述方程进行因式分解，根据因式分解的结果，去掉另一种情况，得出$k\text{和}m\text{（}t\text{和}n\text{）}$的关系，得出定点坐标

另：在第二步中，如果$x_{1}\text{，}x_{2}\text{，}y_{1}\text{，}y_{2}$四个参量的关系不能用韦达定理表示，则使用图像平移和齐次化方法。

圆锥曲线新硬解定理

设圆锥曲线方程为$nA^{2}x^{2} + mB^{2}x^{2} - 2pxm - 2pny - mn = 0$，与直线方程联立，得

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$x$

</th>
<th>

$\left( mA^{2} + nB^{2} \right)x^{2} + \left\lbrack 2mAC - 2pB(nA - mB) \right\rbrack x + m\left( C^{2} - nB^{2} \right) + 2pnBC = 0$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$y$

</td>
<td>

$\left( mA^{2} + nB^{2} \right)y^{2} + \left\lbrack 2nBC - 2pA(mB - nA) \right\rbrack y + n\left( C^{2} - mA^{2} \right) + 2pmAC = 0$

</td>
</tr>
</tbody>
</table>
</div>

令$\varepsilon = mA^{2} + nB^{2}$，$\tau_{x} = 2mAC\text{，}\tau_{y} = 2nBC\text{，}\lambda_{x} = m\left( C^{2} - nB^{2} \right)\text{，}\lambda_{y} = n\left( C^{2} - mA^{2} \right)$

$\varepsilon' = mA + nB\text{，}\nu_{x} = nA - mB\text{，}\nu_{y} = mB - nA$

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$x_{1} + x_{2}$

</th>
<th>

$y_{1} + y_{2}$

</th>
<th>

$x_{1} \cdot x_{2}$

</th>
<th>

$y_{1} \cdot y_{2}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\frac{- \tau - 2pB\nu}{\varepsilon}$

</td>
<td>

$\frac{- \tau - 2pA\nu}{\varepsilon}$

</td>
<td>

$\frac{\lambda + 2pnBC}{\varepsilon}$

</td>
<td>

$\frac{\lambda + 2pmAC}{\varepsilon}$

</td>
</tr>
</tbody>
</table>
</div>

$x_{1}y_{2} + x_{2}y_{1} = \frac{2mnAB - (2pmAC + 2pnBC)}{\varepsilon}$
