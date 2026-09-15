---
title: "立体几何"
hs_seq: "A6"
description: "立体几何：棱柱：有两个面平行，其余各面都是四边形，相邻两个四边形的公共边都互相平行，由这些面所围成的多面体。"
---

# 立体几何

基本立体图形

棱柱：有两个面平行，其余各面都是四边形，相邻两个四边形的公共边都互相平行，由这些面所围成的多面体。

圆柱：以矩形的一边所在直线为旋转轴，其余三边旋转一周形成的面所围成的旋转体。

> 直棱柱：侧棱垂直于底面的棱柱。
>
> 侧棱柱：侧棱不垂直于底面的棱柱。
>
> 正棱柱：底面是正多边形的直棱柱。
>
> 平行六面体：底面是平行四边形的四棱柱。

棱锥：有一个面是多边形，其余各面都是有一个公共顶点的三角形，由这些面所围成的多面体。

圆锥：以直角三角形的一条直角边所在直线为旋转轴，其余两边旋转一周形成的面所围成的旋转体。

> 正棱锥：底面是正多边形，并且顶点和底面中心的连线垂直于底面的棱锥。

棱台：用一个平行于棱锥底面的平面去截棱锥得到的底面和截面之间那部分多面体。

> 原棱锥的底面和截面分别叫做棱台都下底面和上底面。

球体：半圆以它的直径所在直线为旋转轴，旋转一周形成的曲面所围成的旋转体。

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

立体图形

</th>
<th>

表面积

</th>
<th>

体积

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

棱柱

</td>
<td></td>
<td>

$Sh$

</td>
</tr>
<tr>
<td>

圆柱

</td>
<td>

$2\pi r(r + l)$

</td>
<td>

$\pi r^{2}h$

</td>
</tr>
<tr>
<td>

棱锥

</td>
<td></td>
<td>

$\frac{1}{3}Sh$

</td>
</tr>
<tr>
<td>

圆锥

</td>
<td>

$\pi r(r + l)$

</td>
<td>

$\frac{1}{3}\pi r^{2}h$

</td>
</tr>
<tr>
<td>

棱台

$\left( S'\text{为上底面，}S\text{为下底面} \right)$

</td>
<td></td>
<td>

$\frac{1}{3}h\left( S' + \sqrt{S'S} + S \right)$

</td>
</tr>
<tr>
<td>

圆台

</td>
<td>

$\pi\left( {r'}^{2} + r^{2} + r'l + rl \right)$

</td>
<td>

$\frac{1}{3}\pi h({r'}^{2} + r'r + r^{2})$

</td>
</tr>
<tr>
<td>

球

</td>
<td>

$4\pi R^{2}$

</td>
<td>

$\frac{4}{3}\pi R^{3}$

</td>
</tr>
</tbody>
</table>
</div>

斜棱柱体积公式：$V = S_{\text{直截面}}h_{\text{侧棱长}}$

多面体的欧拉定理：$V - E + F = 2$（V为顶点，E为边，F为面）

点。直线、平面

基本事实1：过不在一条直线上的三个点，有且只有一个平面。

基本事实2：如果一条直线上的两个点在一个平面内，那么这条直线在这个平面内。

$A \in l\text{，}B \in l\text{，}A \in \alpha \text{，}B \in \alpha \Rightarrow l \subset \alpha$

基本事实3：如果两个不重合的平面有一个公共点，那么它们有且只有一条过该点的公共直线。

$P \in \alpha \text{，}P \in \beta \Rightarrow \alpha \cap \beta = l\text{，}P \in l$

基本事实4：平行于同一条直线的两条直线平行。

$m \parallel l\text{，}n \parallel L \Rightarrow m \parallel n$

基本事实5：过一点垂直于已知平面的直线有且只有一条。

推论1：经过一条直线和这条直线外一点，有且只有一个平面。

推论2：经过两条相交直线，有且只有一个平面。

推论3：经过两条平行直线，有且只有一个平面。

异面直线：不同在任何一个平面内的两条直线。

$\text{两条直线的位置关系}\left\{ \begin{array}{r} \text{共面直线}\left\{ \begin{array}{r} \text{相交直线：在同一平面内，有且只有一个公共点} \\ \text{平行直线：在同一平面内，没有公共点}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\  \\ \text{异面直线：不同在任何一个平面内，没有公共点}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

$\text{直线与平面的位置关系}\left\{ \begin{array}{r} \text{直线在平面内：有无数个公共点}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \text{直线在平面外}\left\{ \begin{array}{r} \text{直线与平面相交：有且只有一个公共点} \\ \text{直线与平面平行：没有公共点}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\ \end{array} \right.\$

$\text{平面与平面的位置关系}\left\{ \begin{array}{r} \text{两个平面平行：没有公共点}\ \ \ \  \\ \text{两个平面相交：有一个公共点} \end{array} \right.\$

定理1：如果空间中两个角的两条边分别对应平行，那么这两个角相等或互补。

定理2：如果平面外一条直线与此平面平行，那么该直线与此平面平行。

$a ⊄ \alpha \text{，}b \subset \alpha \text{，}a \parallel b \Rightarrow a \parallel \alpha$

定理3：一条直线与一个平面平行，如果过该直线的平面与此平面相交，那么该直线与交线平行。

$a \parallel \alpha \text{，}a \subset \beta \text{，}\alpha \cap \beta = b \Rightarrow a \parallel b$

定理4：如果一个平面内的两条相交直线与另一个平面平行，那么这两个平面平行。

$a \subset \beta \text{，}b \subset \beta \text{，}a \cap \beta = P\text{，}a \parallel \alpha \text{，}b \parallel \alpha \Rightarrow \beta \parallel \alpha$

定理5：两个平面平行，如果另一个平面与这两个平面相交，那么两条交线平行。

$\alpha \parallel \beta \text{，}\gamma \cap \alpha = a\text{，}\gamma \cap \beta = b \Rightarrow a \parallel b$

定理6：如果一条直线与一个平面内的两条相交直线垂直，那么该直线与此平面垂直。

$m \subset \alpha \text{，}n \subset \beta \text{，}m \cap n = P\text{，}l\bot m\text{，}l\bot n \Rightarrow l\bot\alpha$

定理7：垂直于同一个平面的两条直线平行。

$m\bot\alpha \text{，}n\bot\alpha \Rightarrow m \parallel n$

定理8：如果一个平面过另一个平面的垂线，那么这两个平面垂直。

$a \subset \alpha \text{，}a\bot\beta \Rightarrow \alpha\bot\beta$

定理9：两个平面垂直，如果一个平面内有一直线垂直于这两个平面的交线，那么这条直线与另一个平面垂直。

$\alpha\bot\beta \text{，}\alpha \cap \beta = l\text{，}a \subset \alpha \text{，}a\bot l \Rightarrow a\bot b$

外接球与内切球

$\text{棱柱}\left\{ \begin{array}{r} \text{上下底面外心连线的中点为外接球的球心} \\ \text{正棱柱}\left\{ \begin{array}{r} \text{中心连线}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \text{正、长方体：对角线交点} \end{array} \right.\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

$\text{棱锥}\left\{ \begin{array}{r} \text{正棱锥：}R^{2} = r^{3} + (R - h)^{2}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \text{直角四面体：构造长方体，}R = \frac{\sqrt{a^{2} + b^{2} + c^{2}}}{2}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \text{共斜边直角三角形：公共斜边的中点}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \text{对棱相等：}2R = \frac{\sqrt{a^{2} + b^{2} + c^{2}}}{2}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \text{任意：取} \bigtriangleup ABC\text{的外心}O\text{，过}O\text{作面}ABC\text{的垂线，寻找点}D\text{使}PD = CD \end{array} \right.\$

正多面体常用结论

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

正多边形

</th>
<th>

表面积**S**

</th>
<th>

体积**V**

</th>
<th>

外接球半径**R**

</th>
<th>

内切球半径**r**

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

正四面体

</td>
<td>

$\sqrt{3}a^{2}$

</td>
<td>

$\frac{\sqrt{2}}{12}a^{3}$

</td>
<td>

$\frac{\sqrt{6}}{4}a\ \left( \frac{3}{4}h \right)$

</td>
<td>

$\frac{\sqrt{6}}{12}a\ \left( \frac{1}{4}h \right)$

</td>
</tr>
<tr>
<td>

正六面体

</td>
<td>

$6a^{2}$

</td>
<td>

$a^{3}$

</td>
<td>

$\frac{\sqrt{3}}{2}a$

</td>
<td>

$\frac{1}{2}a$

</td>
</tr>
<tr>
<td>

正八面体

</td>
<td>

$2\sqrt{3}a^{2}$

</td>
<td>

$\frac{\sqrt{2}}{3}a^{3}$

</td>
<td>

$\frac{\sqrt{2}}{2}a$

</td>
<td>

$\frac{\sqrt{6}}{6}a$

</td>
</tr>
</tbody>
</table>
</div>

四面体

> 四面体对棱的夹角
>
> $\left| \cos\theta \right| = \frac{\left| \left( |AB|^{2} + |CD|^{2} \right) - \left( |BC|^{2} + |AD|^{2} \right) \right|}{2|AC||BD|}$
>
> 正四面体
>
> $h = \frac{\sqrt{6}}{3}a\text{，对棱中点的连线长：}\frac{\sqrt{2}}{2}a\text{，线面角的余弦值：}\frac{\sqrt{3}}{3}\text{，二面角的余弦值：}\frac{1}{3}$

正方体

三个向量共面

正方体的体对角线垂直于与它不相交的面对角线。

空间角

> 线线角：平移，三线角公式，向量
>
> $\text{两条异面直线所成的角的余弦值为}\left| \cos{< \overrightarrow{a}\text{，}\overrightarrow{b} >} \right| = \left| \frac{\overrightarrow{a} \cdot \overrightarrow{b}}{\left| \overrightarrow{a} \right|\left| \overrightarrow{b} \right|} \right|$
>
> 线面角：定义，转移顶点求体积，三线角公式，模型，向量
>
> 设直线的方向向量为$\overrightarrow{m}$，面的法向量为$\overrightarrow{n}$
>
> $\text{直线与面所成的角的正弦值为}\left| \cos{< \overrightarrow{m}\text{，}\overrightarrow{n} >} \right| = \left| \frac{\overrightarrow{m} \cdot \overrightarrow{n}}{\left| \overrightarrow{m} \right|\left| \overrightarrow{n} \right|} \right|$
>
> 二面角：定义，三垂线定理，补棱，垂面，面积，向量
>
> 设两个平面的法向量分别为$\overrightarrow{m}$，$\overrightarrow{n}$

$\text{两个面的夹角的余弦值为}\left| \cos{< \overrightarrow{m}\text{，}\overrightarrow{n} >} \right| = \left| \frac{\overrightarrow{m} \cdot \overrightarrow{n}}{\left| \overrightarrow{m} \right|\left| \overrightarrow{n} \right|} \right|$

> 二面角需要观察得到

空间直线

点到点的距离：$d = \sqrt{\left( x_{1} - x_{2} \right)^{2} + \left( y_{1} - y_{2} \right)^{2} + \left( z_{1} - z_{2} \right)^{2}}$

点到线的距离：$d^{2} = {\overrightarrow{PA}}^{2} - \left( \frac{\overrightarrow{PA} \cdot \overrightarrow{AB}}{\left| \overrightarrow{AB} \right|} \right)^{2}$

线到面的距离：$d = \left| \frac{\overrightarrow{PA} \cdot \overrightarrow{n}}{\left| \overrightarrow{n} \right|} \right|$

异面直线距离：$d = \left| \frac{\overrightarrow{PA} \cdot \overrightarrow{n}}{\left| \overrightarrow{n} \right|} \right|$

结论与模型

![](/images/hs/hs-a06/img01.png)![](/images/hs/hs-a06/img02.png)

三垂线定理及其逆定理

$PA\bot\alpha \text{，}AO\bot a \Rightarrow PO\bot\alpha(\text{垂直于投影则垂直于斜线})$

$PA\bot\alpha \text{，}PO\bot a \Rightarrow AO\bot\alpha(\text{垂直于斜线则垂直于投影})$

三余弦定理（最小角定理）

设$A$为面上一点，过$A$的斜线$AO$在面上的射影为$AB$，$AC$为面上的一条直线，则

$\cos{\angle OAC} = \cos{\angle BAC} \cdot \cos{\angle OAB}$

三正弦定理

> $\sin\gamma = \sin\alpha \cdot \sin\beta$

面积射影定理

如图，$PO\bot \text{面}OAB\text{，}PC\bot AB\text{，}OC\bot AB$

$\cos{\angle PCO} = \frac{|OC|}{|PC|} = \frac{S_{\bigtriangleup OAB}}{S_{\bigtriangleup PAB}}$

![](/images/hs/hs-a06/img03.png)![](/images/hs/hs-a06/img04.png)

直角四面体

> 1.线面垂直：$PA\bot \text{面}PBC\text{，}PB\bot \text{面}PAC\text{，}PC\bot \text{面}PAB$
>
> 2.面面垂直：三个侧面两两垂直
>
> $3.\text{特殊体积：}V = \frac{1}{6}abc$
>
> $4.\text{两球半径：}R = \frac{\sqrt{a^{2} + b^{2} + c^{2}}}{2}\text{，}r = \frac{3V}{S_{\text{表}}}$
>
> 5.射影定理：
>
> ${S_{\bigtriangleup PAB}^{2} = S_{\bigtriangleup OAB} \cdot S_{\bigtriangleup ABC} }{S_{\bigtriangleup PBC}^{2} = S_{\bigtriangleup OAB} \cdot S_{\bigtriangleup ABC} }{S_{\bigtriangleup PBC}^{2} = S_{\bigtriangleup OAC} \cdot S_{\bigtriangleup ABC} }{S_{\bigtriangleup ABC}^{2} = S_{\bigtriangleup PAB}^{2} + S_{\bigtriangleup PBC}^{2} + S_{\bigtriangleup PAC}^{2}}$
>
> 6.顶点的投影为垂心

$\left. \ \begin{array}{r} PC\bot \text{面}PAB \Rightarrow PC\bot AB \\ PO\bot \text{面}ABC \Rightarrow PO\bot AB \end{array} \right\} AB\bot \text{面}PCO \Rightarrow AB\bot OC\text{，}AB\bot CD$

鳖臑

> 已知$PA\bot \text{面}ABC\text{，}\angle ABC = 90{^\circ}\text{，}AM\bot PB\text{，}AN\bot PC$
>
> $1.BC\bot PB(PA\bot BC\text{，}BC\bot AB \Rightarrow BC\bot \text{面}PAB)$
>
> $2.AM\bot \text{面}PBC(BC\bot \text{面}ABP \Rightarrow BC\bot AM\text{，}AM\bot PB \Rightarrow AM\bot PBC)$
>
> $3.PC\bot \text{面}AMN(AM\bot \text{面}PBC \Rightarrow AM\bot PC\text{，}AN\bot PC \Rightarrow PC\bot \text{面}AMN)$
>
> $4.\angle AMC = 90{^\circ}(2)\text{，}PC\bot MN(3)\text{，}PC\text{的中点为外接圆的圆心}$

阳马

> $\text{已知}PA\bot \text{面}ABCD\text{，}\angle ABCD\text{是矩形}$
>
> 1.四个侧面的三角形都是直角三角形
>
> $AB\bot AD\text{，}PD\bot \text{面}ABCD \Rightarrow PD\bot AB \Rightarrow AB\bot \text{面}PAD \Rightarrow AB\bot PA$
>
> $2.\text{取}PB\text{中点}E\text{，则}EA = EB = EC = ED = EP$

三棱锥顶点在底面的投影O的位置

$1.PA = PB = PC/\angle PAO = \angle PBO = \angle PCO \Rightarrow O\text{是外心}$

> 证：$\bigtriangleup PAO \cong \bigtriangleup PBO \cong \bigtriangleup PCO(HL)/(AAS)$

$2.\angle P - AB - C = \angle P - AC - B/PD = PE = PF \Rightarrow O\text{是内心}$

> 证：作$PD\bot AB\text{，}PE\bot BC\text{，}PF\bot AC$
>
> 由三垂线定理，$OD\bot AB\text{，}OE\bot BC\text{，}OF\bot AC$
>
> $\bigtriangleup PDO \cong \bigtriangleup PEO \cong \bigtriangleup PFO(AAS)/(HL)$

$3.\text{两组对棱互相垂直} \Rightarrow O\text{是垂心，第三组对棱也垂直}$

> 证：$\text{延长}CO\text{交点}D\text{，连接}PD$
>
> $AB\bot PO\text{，}AB\bot PC \Rightarrow AB\bot \text{面}PDC \Rightarrow AB\bot CD$
>
> 因此$O$是$\bigtriangleup ABC$的三条高线的交点，即垂心
>
> 证：已知$PA\bot BC\text{，}PB\bot AC\text{，则}\overrightarrow{PC} \cdot \overrightarrow{AB}$
>
> $= \left( \overrightarrow{PB} + \overrightarrow{BC} \right) \cdot \left( \overrightarrow{PB} - \overrightarrow{PA} \right) = \overrightarrow{PB} \cdot \overrightarrow{PB} - \overrightarrow{PB} \cdot \overrightarrow{PA} + \overrightarrow{BC} \cdot \overrightarrow{PB} = \overrightarrow{PB} \cdot \left( \overrightarrow{PB} - \overrightarrow{PA} + \overrightarrow{BC} \right) = \overrightarrow{PB} \cdot \overrightarrow{AC} = 0$

4.三条侧棱两两垂直$\Rightarrow O\text{是垂心}$（直角四面体）

常用证明思路

> 1.证明直线与直线平行
>
> 转化为判定共面二直线无交点
>
> 转化为二直线同第三条直线平行
>
> 转化为线面平行
>
> 转化为线面垂直
>
> 转化为面面平行
>
> 2.证明直线与平面平行
>
> 转化为直线与平面无交点
>
> 转化为线线平行
>
> 转化为面面平行
>
> 3.证明平面与平面平行
>
> 转化为判定二平面无交点
>
> 转化为线面平行
>
> 转化为线面垂直
>
> 4.证明直线与直线垂直
>
> 转化为相交垂直
>
> 转化为线面垂直
>
> 转化为线与另一条的射影垂直
>
> 转化为线与形成射影的斜线垂直
>
> 5.证明直线与平面垂直
>
> 转化为该直线与平面内任一直线垂直
>
> 转化为该直线与平面内相交二直线垂直
>
> 转化为该直线与平面的一条垂线平行
>
> 转化为该直线垂直于另一个平行平面
>
> 转化为该直线与两个垂直平面的交线垂直
>
> 6.证明平面与平面垂直
>
> 转化为判断二面角是直二面角
>
> 转化为线面垂直

空间解析几何

平面的点法式方程：$A\left( x - x_{0} \right) + B\left( y - y_{0} \right) + C\left( z - z_{0} \right) = 0$

> 其中$(A\text{，}B\text{，}C)$是平面的法向量，$\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)$是平面上一点，方程表示平面上任意一点与该点连线形成的直线都与法向量所在直线垂直。

平面的一般方程：$Ax + By + Cz + D = 0$

$\text{直线的对称式}/\text{点向式方程：}\frac{x - x_{0}}{m} = \frac{y - y_{0}}{n} = \frac{z - z_{0}}{p}$

> 其中$(m\text{，}n\text{，}p)$是直线的方向向量

直线的参数方程

$\left\{ \begin{array}{r} x = x_{0} + mt \\ y = y_{0} + nt \\ z = z_{0} + pt \end{array} \right.\$

两直线的夹角

若直线A、直线B的方向向量分别为$\overrightarrow{a} = \left( m_{1}\text{，}n_{1}\text{，}p_{1} \right)\text{，}\overrightarrow{b} = \left( m_{2}\text{，}n_{2}\text{，}p_{2} \right)$，则两条直线的夹角$\theta$满足

$\cos\theta = \frac{\left| \overrightarrow{a} \cdot \overrightarrow{b} \right|}{\left| \overrightarrow{a} \right| \cdot \left| \overrightarrow{b} \right|} = \frac{\left| m_{1}m_{2} + n_{1}n_{2} + p_{1}p_{2} \right|}{\sqrt{m_{1}^{2} + n_{1}^{2} + p_{1}^{2}}\sqrt{m_{2}^{2} + n_{2}^{2} + p_{2}^{2}}}$

直线与平面的夹角

平面$Ax + By + Cz = 0$与直线（方向向量为$(m\text{，}n\text{，}p)$）的夹角$\theta$满足

$\sin\theta = \frac{|Am + Bn + Cp|}{\sqrt{A^{2} + B^{2} + C^{2}}\sqrt{m^{2} + n^{2} + p^{2}}}$

平面的夹角

平面$A_{1}x + B_{1}y + C_{1}z = 0$与平面$A_{2}x + B_{2}y + C_{2}z = 0$的夹角$\theta$满足

$\cos\theta = \frac{\left| A_{1}A_{2} + B_{1}B_{2} + C_{1}C_{2} \right|}{\sqrt{A_{1}^{2} + B_{1}^{2} + C_{1}^{2}}\sqrt{A_{2}^{2} + B_{2}^{2} + C_{2}^{2}}}$

外积与混合积

外积(解析几何外积，又叫叉积、向量积)

外积的运算结果是一个向量而不是一个数。并且两个向量的叉积与这两个向量组成的坐标平面垂直。

设有三维向量

$\mathbf{a} = \left( x_{1}\text{，}y_{1}\text{，}z_{1} \right)^{T}\text{，}\mathbf{b} = \left( x_{1}\text{，}y_{2}\text{，}z_{2} \right)^{T}$

定义

$\mathbf{a} \times \mathbf{b =}\left| \begin{matrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ x_{1} & y_{1} & z_{1} \\ x_{1} & y_{2} & z_{1} \end{matrix} \right|\mathbf{=}\left| \begin{matrix} y_{1} & z_{1} \\ y_{2} & z_{2} \end{matrix} \right|\mathbf{i} - \left| \begin{matrix} x_{1} & z_{1} \\ x_{2} & z_{2} \end{matrix} \right|\mathbf{j} + \left| \begin{matrix} x_{1} & y_{1} \\ x_{2} & y_{2} \end{matrix} \right|\mathbf{k}$

其中

$\mathbf{i} = (1\text{，}0\text{，}0)\text{，}\mathbf{j} = (0\text{，}1\text{，}0)\text{，}\mathbf{k} = (0\text{，}0\text{，}1)$

即

$\mathbf{a} \times \mathbf{b =}\left( \left| \begin{matrix} y_{1} & z_{1} \\ y_{2} & z_{2} \end{matrix} \right|\text{，} - \left| \begin{matrix} x_{1} & z_{1} \\ x_{2} & z_{2} \end{matrix} \right|\text{，}\left| \begin{matrix} x_{1} & y_{1} \\ x_{2} & y_{2} \end{matrix} \right| \right)$

其为$\mathbf{a}\text{，}\mathbf{b}$的某一个法向量

大小：$\left| \mathbf{a} \times \mathbf{b} \right| = \left| \mathbf{a} \right|\left| \mathbf{b} \right|\sin\theta$，表示$\mathbf{a}$与$\mathbf{b}$所围成的平行四边形的面积。

方向：伸出右手，用食指指向$\mathbf{a}$所在方向，中指指向$\mathbf{b}$所在方向，则大拇指所指方向就是叉积所在方向。

$\mathbf{a} \times \mathbf{b = - b} \times \mathbf{a}$，满足结合律与分配律，不满足交换律。

混合积

设有3个三维向量

$\mathbf{a} = \left( x_{1}\text{，}y_{1}\text{，}z_{1} \right)^{T}\text{，}\mathbf{b} = \left( x_{1}\text{，}y_{2}\text{，}z_{2} \right)^{T}\text{，}\mathbf{c} = \left( x_{3}\text{，}y_{3}\text{，}z_{3} \right)^{T}$

定义

$\left\lbrack \mathbf{abc} \right\rbrack = \mathbf{a} \times \mathbf{b} \cdot \mathbf{c} = \left| \begin{matrix} x_{1} & x_{2} & x_{3} \\ y_{1} & y_{2} & y_{3} \\ z_{1} & z_{2} & z_{3} \end{matrix} \right|$

称其为向量的混合积。其结果是一个数，表示三个向量夹成的平行六面体的体积

四面体体积公式

设四面体的四点分别为A、B、C、D，则四面体的面积为

$V = \pm \frac{1}{6}\left| \begin{matrix} x_{2} - x_{1} & x_{3} - x_{1} & x_{4} - x_{1} \\ y_{2} - y_{1} & y_{3} - y_{1} & y_{4} - y_{1} \\ z_{2} - z_{1} & z_{3} - z_{1} & z_{4} - z_{1} \end{matrix} \right| = \pm \frac{1}{6}\left| \begin{array}{r} \overrightarrow{AB} \\ \overrightarrow{AC} \\ \overrightarrow{AD} \end{array} \right| = \frac{1}{6}\left| \begin{matrix} x_{1} & x_{2} & x_{3} & x_{4} \\ y_{1} & y_{2} & y_{3} & y_{4} \\ z_{1} & z_{2} & z_{3} & z_{4} \\ 1 & 1 & 1 & 1 \end{matrix} \right|$
