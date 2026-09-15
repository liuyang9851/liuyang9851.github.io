---
title: "函数与方程"
hs_seq: "A3"
description: "函数与方程：一般地，给定两个非空实数集与以及对应关系，如果对于集合中的每一个实数，在集合中都有唯一确定的实数与对应，则称为定义在集合上的一个函数，记作"
---

# 函数与方程

函数与映射的定义

函数

一般地，给定两个非空实数集$A$与$B$以及对应关系$f$，如果对于集合$A$中的每一个实数$x$，在集合$B$中都有唯一确定的实数$y$与$x$对应，则称$f$为定义在集合$A$上的一个函数，记作

$y = f(x)\text{，}x \in A$

其中$x$称为自变量，$y$称为因变量，自变量取值的范围（即数集$A$）称为这个函数的定义域，所有函数组成的集合

$\left\{ y \in B|y = f(x)\text{，}x \in A \right\}$

称为函数的值域。

映射

设$X\text{、}Y$是两个非空集合，如果存在一个法则$f$，使得对$X$中每一个元素，按法则$f$，在$Y$中有唯一确定的元素$y$与之对应，那么称$f$为从$X$到$Y$的映射，记作

$f:X \rightarrow Y$

其中$y$称为元素$x$（在映射$f$下）的像，并记作$f(x)$，即

$y = f(x)$

而元素$x$称为元素$y$（在映射$f$下）的一个原像；集合$X$称为映射的定义域；记作$D_{f}$，即$D_{f} = X$；$X$中的所有元素的像所组成的集合称为映射$f$的值域，记作$R_{f}$或$f(X)$，即

$R_{f} = f(X) = \left\{ f(x)|x \in X \right\}$

由此得到函数的定义：

设数集$D\mathbb{\subset R}$，则称映射$f:D\mathbb{\rightarrow R}$为定义在$D$上的函数，通常简记为

$y = f(x)\text{，}x \in D$

其中$x$称为自变量，$y$称为因变量，$D$称为定义域，记作$D_{f}$，即$D_{f} = D$

函数的定义中，对每个$x \in D$，按对应法则$d$，总有唯一确定的值$y$与之对应，这个值称为函数$f$在$x$处的函数值，记作$f(x)$，即$y = f(x)$。因变量$y$与自变量$x$之间的这种依赖关系，通常称为函数关系。函数值$f(x)$的全体所构成的集合称为函数的值域，记作$D_{f}$或$f(D)$，即

$R_{f} = f(D) = \left\{ y|y = f(x)\text{，}x \in D \right\}$

方程

二元方程可用二元函数$f(x\text{，}y)$表示为

$f(x\text{，}y) = 0$

$\text{例如，定义函数}f(x\text{，}y) = \frac{x^{2}}{m} + \frac{y^{2}}{n} - 1\text{，则}f(x\text{，}y) = 0\text{就表示方程}\frac{x^{2}}{m} + \frac{y^{2}}{n} = 1$

常见方程对应不等式的几何意义

$Ax + By + C > 0$表示其分割区域中法向量指向区域

$(x - a)^{2} + (y - b)^{2} - r^{2} > 0$表示圆外的区域

$\frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} > 0\text{表示椭圆外的区域}$

$\frac{x^{2}}{a^{2}} - \frac{y^{2}}{b^{2}} > 0\text{表示双曲线}``\text{腰}"\text{两侧部分}$

$y^{2} > 2px$表示抛物线“钟形”外的部分

$Ax^{2} + Bxy + Cy^{2} + Dx + Ey + F > 0$表示二次曲线外侧的部分

存在与任意对应的条件

设函数$f(x)\text{，}g(x)$均有最大值和最小值，则

${1.\forall x_{1}\text{，}\forall x_{2}\text{，}f\left( x_{1} \right) > g\left( x_{2} \right) \Longleftrightarrow \min\left\lbrack f\left( x_{1} \right) \right\rbrack > \max\left\lbrack g\left( x_{2} \right) \right\rbrack }{2.\forall x_{1}\text{，}\exists x_{2}\text{，}f\left( x_{1} \right) > g\left( x_{2} \right) \Longleftrightarrow \min\left\lbrack f\left( x_{1} \right) \right\rbrack > \min\left\lbrack g\left( x_{2} \right) \right\rbrack }{3.\exists x_{1}\text{，}\forall x_{2}\text{，}f\left( x_{1} \right) > g\left( x_{2} \right) \Longleftrightarrow \max\left\lbrack f\left( x_{1} \right) \right\rbrack > \max\left\lbrack g\left( x_{2} \right) \right\rbrack }{4.\exists x_{1}\text{，}\exists x_{2}\text{，}f\left( x_{1} \right) > g\left( x_{2} \right) \Longleftrightarrow \max\left\lbrack f\left( x_{1} \right) \right\rbrack > \min\left\lbrack g\left( x_{2} \right) \right\rbrack }{5.\forall x_{1}\text{，}\forall x_{2}\text{，}f\left( x_{1} \right) = g\left( x_{2} \right) \Longleftrightarrow f(x) = g(x) = c }{6.\forall x_{1}\text{，}\exists x_{2}\text{，}f\left( x_{1} \right) = g\left( x_{2} \right) \Longleftrightarrow R_{f} \subseteq R_{g} }{7.\exists x_{1}\text{，}\forall x_{2}\text{，}f\left( x_{1} \right) = g\left( x_{2} \right) \Longleftrightarrow R_{f} \supseteq R_{g} }{8.\exists x_{1}\text{，}\exists x_{2}\text{，}f\left( x_{1} \right) = g\left( x_{2} \right) \Longleftrightarrow R_{f} \cap R_{g} \neq \varnothing}$

函数与方程的变换

此处函数表示为$y = f(x)$，方程表示为$f(x\text{，}y) = 0$，对变量的变化相当于把改变后的值代入对应法则。

1.平移（$a > 0$）

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

上

</th>
<th>

下

</th>
<th>

左

</th>
<th>

右

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$y = f(x)$

</td>
<td>

$y = f(x) + a$

</td>
<td>

$y = f(x) - a$

</td>
<td>

$y = f(x + a)$

</td>
<td>

$y = f(x - a)$

</td>
</tr>
<tr>
<td>

$f(x\text{，}y) = 0$

</td>
<td>

$f(x\text{，}y - a) = 0$

</td>
<td>

$f(x\text{，}y + a) = 0$

</td>
<td>

$f(x + a\text{，}y) = 0$

</td>
<td>

$f(x\text{，}y - a) = 0$

</td>
</tr>
</tbody>
</table>
</div>

2.伸缩

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

横

</th>
<th>

纵

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$y = f(x)$

</td>
<td>

$y = f(ax)$

$\text{横变为原来的}a^{- 1}$

</td>
<td>

$y = af(x)$

$\text{纵变为原来的}a$

</td>
</tr>
<tr>
<td>

$f(x\text{，}y) = 0$

</td>
<td>

$f(ax\text{，}y) = 0$

$\text{横变为原来的}a^{- 1}$

</td>
<td>

$f(x\text{，}ay) = 0$

$\text{纵变为原来的}a^{- 1}$

</td>
</tr>
</tbody>
</table>
</div>

$af(x\text{，}y) = 0$无变化。

3.取负

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

关于$x$轴对称

</th>
<th>

关于$y$轴对称

</th>
<th>

关于原点对称

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$y = f(x)$

</td>
<td>

$y = f( - x)$

</td>
<td>

$y = - f(x)$

</td>
<td>

$y = - f( - x)$

</td>
</tr>
<tr>
<td>

$f(x\text{，}y) = 0$

</td>
<td>

$f( - x\text{，}y) = 0$

</td>
<td>

$f(x\text{，} - y) = 0$

</td>
<td>

$f( - x\text{，} - y) = 0$

</td>
</tr>
</tbody>
</table>
</div>

$- f(x\text{，}y) = 0$无变化。

4.绝对值

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

横

</th>
<th>

纵

</th>
<th>

横纵

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$y = f(x)$

</td>
<td>

$y = f\left( |x| \right)$

去掉y轴左边的图像，

把y轴右边的图像翻折到左边

</td>
<td>

$y = \left| f(x) \right|$

保留x轴上边的图像，

把x轴下边的图像翻折到上边

</td>
<td>

$y = \left| f\left( |x| \right) \right|$

前两者合并

</td>
</tr>
<tr>
<td>

$f(x\text{，}y) = 0$

</td>
<td>

$f\left( |x|\text{，}y \right) = 0$

去掉y轴左边的图像，

把y轴右边的图像翻折到左边

</td>
<td>

$f\left( x\text{，}|y| \right) = 0$

去掉x轴下边的图像，

把x轴上边的图像翻折到下边

</td>
<td>

$f\left( |x|\text{，}|y| \right) = 0$

保留第一象限的图像，

变换后的图像

关于x轴、y轴对称，

关于中心对称

</td>
</tr>
</tbody>
</table>
</div>

$\left| f(x\text{，}y) \right| = 0$无变化。

5.$y = \pm x$

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

关于$y = x$对称（反函数）

</th>
<th>

关于$y = - x$对称

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$y = f(x)$

</td>
<td>

$x = f(y)$

</td>
<td>

$- x = f( - y)$

</td>
</tr>
<tr>
<td>

$f(x\text{，}y) = 0$

</td>
<td>

$f(y\text{，}x) = 0$

</td>
<td>

$f( - y\text{，} - x) = 0$

</td>
</tr>
</tbody>
</table>
</div>

函数的性质

一、有界性

课本中关于最大值和最小值的定义

> 一般地，设函数$y = f(x)$的定义域为$I$，如果存在实数$M$满足：

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

最大值

</th>
<th>

最小值

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\forall x \in I\text{，都有}f(x) \leq M$

$\exists x_{0} \in I\text{，使得}f\left( x_{0} \right) = M$

</td>
<td>

$\forall x \in I\text{，都有}f(x) \geq M$

$\exists x_{0} \in I\text{，使得}f\left( x_{0} \right) = M$

</td>
</tr>
</tbody>
</table>
</div>

> 那么称$M$是函数$y = f(x)$的最大/小值。
>
> 最小值同理
>
> 由最大值与最小值的定义，能得到
>
> 1.连续函数在闭区间上一定有最大值和最小值。
>
> 2.单调连续函数在开区间上无最大值和最小值。

有界性的定义

> 设函数$f(x)$的定义域为$D$，数集$X \subset D$。
>
> 1.如果存在数$K_{1}$，使得$f(x) \leq K_{1}$对任一$x \in X$都成立，那么称函数$f(x)$在$X$上有上界，而$K_{1}$称为函数$f(x)$在$X$上的一个上界。
>
> 2.如果存在数$K_{2}$，使得$f(x) \leq K_{2}$对任一$x \in X$都成立，那么称函数$f(x)$在$X$上有下界，而$K_{2}$称为函数$f(x)$在$X$上的一个下界。
>
> 3.如果存在正数$M$，使得$\left| f(x) \right| \leq M$对任一$x \in X$都成立，那么称函数$f(x)$在$X$上有界。否则称函数$f(x)$在$X$上无界。

二、单调性

定义

> 一般地，设函数$f(x)$的定义域为$I$，区间$D \subseteq I$：
>
> 1.如果$\forall x_{1}$，$x_{2} \in D$，当$x_{1} < x_{2}$时，都有$f\left( x_{1} \right) < f\left( x_{2} \right)$，那么就称函数$f(x)$在区间$D$上单调递增。特别地，当函数$f(x)$在它的定义域上单调递增时，我们就称它是增函数。
>
> 2.如果$\forall x_{1}$，$x_{2} \in D$，当$x_{1} < x_{2}$时，都有$f\left( x_{1} \right) > f\left( x_{2} \right)$，那么就称函数$f(x)$在区间$D$上单调递减。特别地，当函数$f(x)$在它的定义域上单调递减时，我们就称它是减函数。
>
> 3.如果函数$y = f(x)$在区间$D$上单调递增或单调递减，那么就说函数$y = f(x)$在这一区间具有（严格的）单调性，区间叫做$y = f(x)$的单调区间。

实际上，对于含有一阶导数为零的点的区间，如果满足$f\left( x_{1} \right) \leq f\left( x_{2} \right)$或$f\left( x_{1} \right) \geq f\left( x_{2} \right)$，也可以称其是单调区间。如$y = x^{3}$为增函数。

函数的单调区间可能有无数个，但讨论函数的单调时必须说出其全部单调增区间和单调减区间，且能合并的区间要合并（$\cap$），不能合并的区间用逗号（，）隔开。如反比例函数的单调区间为$( - \infty \text{，}0)\text{，}(0\text{，} + \infty)$。

由函数单调性的定义，得出两个具有单调性的函数加减运算后新函数的单调性：

$\text{增} + \text{增} = \text{增，减} + \text{减} = \text{减，增} - \text{减} = \text{增，减} - \text{增} = \text{减}\ \ (\text{任取，做差，判号，定论})$

三、奇偶性

定义

> 一般地，设函数$f(x)$的定义域为$I$，$\forall x \in I$，都有$- x \in I$：
>
> $1.f( - x) = f(x)$，$f(x)$为偶函数。
>
> $2.f( - x) + f(x) = 0$，$f(x)$为奇函数。

由奇偶性的定义，判断奇偶性要先判断定义域是否对称。

任意初等函数可分为四类：奇函数，偶函数，非奇非偶函数，既奇又偶函数，其中既奇又偶函数是对应法则为$y = 0$的函数。

性质

> $\text{若}g(x)\text{为奇函数，则}k_{1}f\left( k_{2}x \right)\text{为奇函数}$
>
> $\text{若}f(x)\text{为偶函数，则}k_{1}f\left( k_{2}x \right) + C\text{为偶函数}$
>
> $\text{奇} + \text{奇} = \text{奇，奇} \times \text{奇} = \text{奇，偶} + \text{偶} = \text{偶，偶} \times \text{偶} = \text{偶，奇} \times \text{偶} = \text{奇}$
>
> $\text{已知}h(x) = f\left( g(x) \right)$
>
> 1.$\text{若}g(x)\text{为偶函数，则}h(x)\text{为偶函数；}$
>
> 2.$\text{若}g(x)\text{为奇函数}$
>
> $\text{当}f(x)\text{为奇函数时，}h(x)\text{为奇函数；}$
>
> $\text{当}f(x)\text{为偶函数时，}h(x)\text{为偶函数；}$
>
> 3.$\text{若}g(x)\text{为非奇非偶函数}$，$\text{则}h(x)\text{既不是奇函数也不是偶函数。}$
>
> $f(x) = g(x) - g( - x)\text{是奇函数，}f(x) = g(x) + g( - x)\text{是偶函数。}$
>
> $\text{若}f(x)\text{是奇函数，则}f'(x)\text{是偶函数；若}f(x)\text{是偶函数，则}f'(x)\text{是奇函数}$。反过来不一定成立。
>
> $g(x) = f(x) - f( - x)$是奇函数，$g(x) = f(x) + f( - x)$是偶函数。
>
> 由此可得，任意一个函数都能写成一个奇函数和一个偶函数的和，即

$f(x) = \frac{f(x) - f( - x)}{2} + \frac{f(x) + f( - x)}{2}$

> 也就是说，若已知$g(x)$为奇函数，$h(x)$为偶函数，且有$g(x) + h(x) = f(x)$，则

$g(x) = \frac{f(x) - f( - x)}{2}\text{，}h(x) = \frac{f(x) + f( - x)}{2}$

常见奇函数，偶函数模型

> 奇函数
>
> $1.f(x) = \frac{a^{x} \mp 1}{a^{x} \pm 1}\text{或}f(x) = \frac{1 \mp a^{x}}{1 \pm a^{x}}$
>
> $2.f(x) = \frac{a^{x} \mp a^{- x}}{a^{x} \pm a^{- x}} = \frac{a^{2x} \mp 1}{a^{2x} \pm 1}$
>
> $3.f(x) = a^{x} - a^{- x}$
>
> $4.f(x) = \log_{c}\frac{ax \mp b}{ax \pm b}\text{或}f(x) = \log_{c}\frac{b \mp ax}{b \pm ax}$
>
> $5.f(x) = \log_{a}\left( \sqrt{{(mx)}^{2} + 1} \pm mx \right)$
>
> 偶函数
>
> $6.f(x) = a^{x} + a^{- x}$
>
> $7.f(x) = \log_{a}{(1 + a^{mx})} - \frac{m}{2}x$

四、对称性

基本原理：$\text{若}F\left( f(x) \right) = F\left( g(x) \right)$，则$F\left( f\left( h(x) \right) \right) = F\left( g\left( h(x) \right) \right)$

1.函数自己满足一定条件，则其有一定对称性

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

函数

</th>
<th>

对称轴$/$对称中心

</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">

轴对称

</td>
<td>

$f(\omega x) = f( - \omega x + a + b)$

</td>
<td rowspan="3">

$x = \frac{a + b}{2}$

</td>
</tr>
<tr>
<td>

$f(\omega x + a + b) = f( - \omega x)$

</td>
</tr>
<tr>
<td>

$\mathbf{f}\left( \mathbf{\omega x} + \mathbf{a} \right)\mathbf{= f}\left( \mathbf{-}\mathbf{\omega x} + \mathbf{b} \right)$

</td>
</tr>
<tr>
<td rowspan="3">

中心对称

</td>
<td>

$f(\omega x) + f( - \omega x + a + b) = c + d$

</td>
<td rowspan="3">

$\left( \frac{a + b}{2}\text{，}\frac{c + d}{2} \right)$

</td>
</tr>
<tr>
<td>

$f(\omega x + a + b) + f( - \omega x) = c + d$

</td>
</tr>
<tr>
<td>

$\mathbf{f}\left( \mathbf{\omega x} + \mathbf{a} \right)\mathbf{+ f}\left( \mathbf{-}\mathbf{\omega x} + \mathbf{b} \right)\mathbf{= c + d}$

</td>
</tr>
</tbody>
</table>
</div>

2.任意函数按照一定方式变换出的两个新函数具有一定对称性

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

函数

</th>
<th>

对称轴$/$对称中心

</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">

轴对称

</td>
<td>

$y = f(\omega x)\mathbf{\text{与}}y = f( - \omega x + a + b)$

</td>
<td rowspan="3">

$x = \frac{a + b}{2}$

</td>
</tr>
<tr>
<td>

$y = f(\omega x - a - b)\mathbf{\text{与}}y = f( - \omega x)$

</td>
</tr>
<tr>
<td>

$\mathbf{y = f}\left( \mathbf{\omega x - a} \right)\mathbf{\text{与}}\mathbf{y}\mathbf{=}\mathbf{f( - \omega x + b)}$

</td>
</tr>
<tr>
<td rowspan="3">

中心对称

</td>
<td>

$y\mathbf{=}f(\omega x)\mathbf{\text{与}}y = - f( - \omega x + a + b) + c + d$

</td>
<td rowspan="3">

$\left( \frac{a + b}{2}\text{，}\frac{c + d}{2} \right)$

</td>
</tr>
<tr>
<td>

$y = f(\omega x - a - b) - c - d\mathbf{\text{与}}y\mathbf{=}f( - \omega x)$

</td>
</tr>
<tr>
<td>

$\mathbf{y = f}\left( \mathbf{\omega x - a} \right)\mathbf{- d}\mathbf{\text{与}}\mathbf{y = - f}\left( \mathbf{- \omega x + b} \right)\mathbf{+ c}$

</td>
</tr>
</tbody>
</table>
</div>

3. 任意函数按照一定方式构造出的新函数具有一定对称性

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

函数

</th>
<th>

对称轴$/$对称中心

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

轴对称

</td>
<td>

$\mathbf{g}\left( \mathbf{x} \right)\mathbf{=}\frac{\mathbf{1}}{\mathbf{2}}\left\lbrack \mathbf{f}\left( \mathbf{\omega x + a} \right)\mathbf{+ f}\left( \mathbf{- \omega x + b} \right) \right\rbrack$

</td>
<td>

$x = \frac{a + b}{2}$

</td>
</tr>
<tr>
<td>

中心对称

</td>
<td>

$\mathbf{g}\left( \mathbf{x} \right)\mathbf{=}\frac{\mathbf{1}}{\mathbf{2}}\left\lbrack \mathbf{f}\left( \mathbf{\omega x + a} \right)\mathbf{- f}\left( \mathbf{- \omega x + b} \right)\mathbf{+ c + d} \right\rbrack$

</td>
<td>

$\left( \frac{a + b}{2}\text{，}\frac{c + d}{2} \right)$

</td>
</tr>
</tbody>
</table>
</div>

导函数的对称性

已知原函数连续可导，则

$1.\text{原函数关于}x = x_{0}\text{对称} \Leftrightarrow \text{导函数关于}\left( x_{0}\text{，}0 \right)\text{对称}$

$2.\text{原函数关于}\left( x_{0}\text{，}f\left( x_{0} \right) \right)\text{对称} \Leftrightarrow \text{导函数关于}x = x_{0}\text{对称}$

常见对称函数

> $\mathbf{1.f}\left( \mathbf{x} \right)\mathbf{=}\frac{\mathbf{n}}{\mathbf{a}^{\mathbf{x}}\mathbf{+ m}}\mathbf{\text{关于}}\left( \mathbf{\log}_{\mathbf{a}}\left| \mathbf{m} \right|\mathbf{\text{，}}\mathbf{-}\frac{\mathbf{n}}{\mathbf{2m}} \right)\mathbf{\text{对称。}}$
>
> $\mathbf{2.f}\left( \mathbf{x} \right)\mathbf{=}\frac{\mathbf{cx + d}}{\mathbf{ax + b}}\mathbf{\ \ }\left( \mathbf{ad}\mathbf{\neq}\mathbf{bc} \right)\mathbf{\text{关于}}\left( \mathbf{-}\frac{\mathbf{d}}{\mathbf{c}}\mathbf{\text{，}}\frac{\mathbf{a}}{\mathbf{c}} \right)\mathbf{\text{对称。}}$
>
> $3.f(x) = \frac{1}{a^{x} + 1}\text{关于}\left( 0\text{，}\frac{1}{2} \right)\text{对称，且}f(x) = \frac{1}{a^{x} + 1} - \frac{1}{2}\text{是奇函数。}$
>
> $4.f(x) = \frac{1}{a^{x} - 1}\text{关于}\left( 0\text{，} - \frac{1}{2} \right)\text{对称，且}f(x) = \frac{1}{a^{x} - 1} + \frac{1}{2}\text{是奇函数。}$
>
> $5.f(x) = \frac{a^{x}}{a^{x} + \sqrt{a}}\text{关于}\left( \frac{1}{2}\text{，}\frac{1}{2\sqrt{a}} \right)\text{对称，且}f(x) + f(1 - x) = \frac{1}{\sqrt{a}}\text{。}$
>
> $6.f(x) = \frac{1}{a^{x} + \sqrt{a}}\text{关于}\left( \frac{1}{2}\text{，}\frac{1}{2} \right)\text{对称，且}f(x) + f(1 - x) = 1\text{。}$

函数的构造

奇函数：$g(x) = f(x) - f( - x)$

偶函数：$g(x) = f(x) + f( - x)$

轴对称：$g(x) = f(a + x) + f(b - x)\ \ x = \frac{b - a}{2}$

中心对称：$g(x) = f(a + x) + f(b - x)$

五、周期性

周期函数有无穷多个周期，一般说某个函数的周期，指的是它的最小正周期。

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

函数

</th>
<th>

周期

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$f(x + m) = f(x)$

</td>
<td>

$T = m$

</td>
</tr>
<tr>
<td>

$f(x + m) + f(x) = c$

</td>
<td rowspan="6">

$T = 2m$

</td>
</tr>
<tr>
<td>

$f(x + m) = \frac{c}{f(x)}\ (k \neq 0)$

</td>
</tr>
<tr>
<td>

$f(x + m) = f(x - m)$

</td>
</tr>
<tr>
<td>

$f(x + m) = \frac{1 - f(x)}{1 + f(x)}$

</td>
</tr>
<tr>
<td>

$f(x + m) = \frac{f(x) + 1}{f(x) - 1}$

</td>
</tr>
<tr>
<td>

$f(x + m) = \frac{1}{2} + \sqrt{f(x) - f^{2}(x)}\ \ \left( f(x) \in (0\text{，}1) \right)$

</td>
</tr>
<tr>
<td>

$f(x + m) = \frac{1}{1 - f(x)}$

</td>
<td rowspan="3">

$T = 3m$

</td>
</tr>
<tr>
<td>

$f(x + m) = 1 - \frac{1}{f(x)}$

</td>
</tr>
<tr>
<td>

$f(x + m) = \frac{\sqrt{3}f(x)}{1 - \sqrt{3}f(x)}$

</td>
</tr>
<tr>
<td>

$f(x + m) = \frac{1 + f(x)}{1 - f(x)}$

</td>
<td rowspan="2">

$T = 4m$

</td>
</tr>
<tr>
<td>

$f(x + m) = \frac{f(x) - 1}{f(x) + 1}$

</td>
</tr>
<tr>
<td></td>
<td>

$T = 5m$

</td>
</tr>
<tr>
<td>

$f(x + m) + f(x - m) = f(x)$

</td>
<td>

$T = 6m$

</td>
</tr>
<tr>
<td>

$f(x) + f(x + m) + f(x + 2m) + \cdots + f(x + nm) = f(x)f(x + m)f(x + 2m)\cdots f(x + nm)$

</td>
<td>

$T = (n + 1)m$

</td>
</tr>
<tr>
<td>

$f(x + a) = f(x + b)$

</td>
<td>

$T = |a - b|$

</td>
</tr>
<tr>
<td>

$f(x + a) = - f(x + b)$

</td>
<td rowspan="3">

$T = 2|a - b|$

</td>
</tr>
<tr>
<td>

$f(a + x) = f(a - x)\text{，}f(b + x) = f(b - x)$

</td>
</tr>
<tr>
<td>

$f(a + x) = - f(a - x)\text{，}f(b + x) = - f(b - x)$

</td>
</tr>
<tr>
<td>

$f(a + x) = f(a - x)\text{，}f(b + x) = - f(b - x)$

</td>
<td>

$T = 4|a - b|$

</td>
</tr>
</tbody>
</table>
</div>

$f(x) = f(x + T) = c - f\left( x + \frac{T}{2} \right) = \frac{c}{f\left( x + \frac{T}{2} \right)} = \frac{1 - f\left( x + \frac{T}{2} \right)}{f\left( x + \frac{T}{2} \right) + 1} = \frac{1}{2} \pm \sqrt{- f^{2}\left( x + \frac{T}{2} \right) + f\left( x + \frac{T}{2} \right)} = 1 - \frac{1}{f\left( x + \frac{T}{3} \right)} = \frac{1}{1 - f\left( x + \frac{T}{3} \right)} = \frac{f\left( x + \frac{T}{3} \right)}{\sqrt{3}\left( f\left( x + \frac{T}{3} \right) + 1 \right)} = \frac{f\left( x + \frac{T}{4} \right) - 1}{f\left( x + \frac{T}{4} \right) + 1} = \frac{f\left( x + \frac{T}{4} \right) + 1}{1 - f\left( x + \frac{T}{4} \right)} = f\left( x + \frac{T}{6} \right) + f\left( x - \frac{T}{6} \right)$

周期函数的导函数仍为周期函数，且周期相同。

对称轴和对称中心的周期出现

> $1.\text{两相邻对称轴或两相邻对称中心之间的水平距离为}\frac{T}{2}$
>
> $2.\text{对称轴与对称中心之间的最小距离为}\frac{T}{4}$

由两个对称性可推出周期性，由$\frac{T}{2}$的周期性和一个对称性可推出另一个对称性，由$T$的周期性和一个对称性不能推出另一个对称性。

六、凹凸性

一般称左边的函数是凹函数，右边的函数是凸函数

$\text{设}f(x)\text{在区间}I\text{上定义，若对}I\text{中的}\forall x_{1}\text{，}x_{2}\text{，和}\forall\lambda \in (0\text{，}1)\text{，都有}$

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

凹函数

（左图）

</th>
<th>

$f\left( \lambda x_{1} + (1 - \lambda)x_{2} \right) \leq \lambda f\left( x_{1} \right) + (1 - \lambda)f\left( x_{2} \right)$

</th>
<th>

$f\left( \frac{x_{1} + x_{2}}{2} \right) \leq \frac{f\left( x_{1} \right) + f\left( x_{2} \right)}{2}$

</th>
<th>

$f^{''}(x) > 0$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

凸函数

（右图）

</td>
<td>

$f\left( \lambda x_{1} + (1 - \lambda)x_{2} \right) \geq \lambda f\left( x_{1} \right) + (1 - \lambda)f\left( x_{2} \right)$

</td>
<td>

$f\left( \frac{x_{1} + x_{2}}{2} \right) \geq \frac{f\left( x_{1} \right) + f\left( x_{2} \right)}{2}$

</td>
<td>

$f^{''}(x) < 0$

</td>
</tr>
</tbody>
</table>
</div>

由于各种原因，对于凹凸性的定义与图像对应在不同地方有区别，一般情况下，可以对两图图描述为

左图：V型/凸向原点/上凹/下凸

右图：A型/凹向原点/上凸/下凹

反函数

设$y = f(x)$的定义域为$D$，值域为$R_{y}$，若对于任意$y \in R$，有唯一确定的$x \in D$，使得$y = f(x)$，则记为$x = f^{- 1}(y)$，称其为直接函数$y = f(x)$的反函数。

$y = f(x)\underset{\text{图形重合}}{\overset{\text{不同的函数}}{\Leftrightarrow}}x = f^{- 1}(y)\underset{\text{图象关于}y = x\text{对称}}{\overset{\ \ \ \ \ \ \ \ \text{同一个函数}\ \ \ \ \ \ \ \ }{\Leftrightarrow}}y = f^{- 1}(x)$

由上述定义，可得$f^{- 1}\left\lbrack f(x) \right\rbrack = f\left\lbrack f^{- 1}(x) \right\rbrack = x$

严格单调函数必定有严格单调的反函数，并且二者单调性相同。

单调函数一定有反函数，反之则不一定。

函数的各种点

$\text{间断点}\left\{ \begin{array}{r} \text{第一类间断点}\left. \text{（左右极限都存在} \right.\text{）}\left\{ \begin{array}{r} \text{可去间断点：}\lim_{x \rightarrow x_{0}^{-}}{f(x)} = \lim_{x \rightarrow x_{0}^{+}}{f(x)}\left\{ \begin{array}{r} \neq f\left( x_{0} \right)\ \ \ \ \ \ \ \ \  \\ f\left( x_{0} \right)\text{无定义} \end{array} \right.\ \ \ \  \\ \text{不可去间断点}\left. \text{（跳跃间断点} \right.\text{）：}\lim_{x \rightarrow x_{0}^{-}}{f(x)} \neq \lim_{x \rightarrow x_{0}^{+}}{f(x)} \end{array} \right.\ \ \ \ \ \ \ \  \\ \text{第二类间断点}\left. \text{（左右极限至少有一个不存在} \right.\text{）}\left\{ \begin{array}{r} \text{无穷间断点：}\lim_{x \rightarrow x_{0}^{-}}{f(x)} = \infty\lim_{x \rightarrow x_{0}^{+}}{f(x)} = \infty \\ \text{振荡间断点：}\lim_{x \rightarrow x_{0}}{f(x)}\text{振荡}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\ \ \ \end{array} \right.\$

零点：$x = x_{0}$（其中$f\left( x_{0} \right) = 0$）

极值点：$x = x_{0}$（其中$f'\left( x_{0} \right) = 0$，且$f^{''}\left( x_{0} \right) \neq 0$）

驻点（可移点）：$x = x_{0}$（其中$f'\left( x_{0} \right) = 0$，且$f^{''}\left( x_{0} \right) = 0$）

拐点：$\left( x_{0}\text{，}f\left( x_{0} \right) \right)$（其中$f'\left( x_{0} \right) \neq 0$，且$f^{''}\left( x_{0} \right) = 0$）

三种基本初等函数

幂函数

指数函数

对数函数

其它函数

> 1.对勾函数$y = x + \frac{1}{x}$
>
> $2.\text{平移反比例函数}y = \frac{ax + b}{cx + d}\left. \text{（}ad \neq bc\text{，对称点为}\left( - \frac{d}{c}\text{，}\frac{a}{c} \right) \right.\text{）}$
>
> 3.含绝对值的函数

函数的构造与函数方程

抽象函数模型

（成立条件：连续、且不为常函数/有（严格的）单调性/当x……时，y……）

常会代自变量值为$0,1, - x$等

$1.f(x + y) = f(x) + f(y) - b\text{，令}f(x) = kx + b(k \neq 0)$

> $a.f(0) = b$
>
> $b.f(x) + f( - x) = 2b$
>
> $c.\text{若}\forall x > 0\text{，}y > b\text{，则}f(x)\text{单调递增；若}\forall x > 0\text{，}y < b\text{，则}f(x)\text{单调递减}$

$2.f(x + y) = f(x) \cdot f(y)\text{，令}f(x) = a^{x}(a > 0\text{且}a \neq 1)$

> $a.f(0) = 1$
>
> $b.f(x)f( - x) = 1$
>
> $c.\forall x \in D,f(x) > 0$
>
> $d.\text{若}\forall x > 0\text{，}y > 1\text{，则}f(x)\text{单调递增；若}\forall x > 0\text{，}0 < y < 1\text{，则}f(x)\text{单调递减}$

$3.f(x \cdot y) = f(x) + f(y)\text{，令}f(x) = \log_{a}x(a > 0\text{且}a \neq 1)$

> $a.f(1) = 0$
>
> $b.f(x) + f\left( \frac{1}{x} \right) = 0$a
>
> $c.D \subseteq (0\text{，} + \infty)\text{，}\forall x > 1\text{，若}y > 0\text{，则}f(x)\text{单调递增；若}y < 0\text{，则}f(x)\text{单调递减}$

$4.f(x \cdot y) = f(x) \cdot f(y)\text{，令}f(x) = x^{a}(a \neq 0)$

> $a.f(0) = 0\text{，}f(1) = 1$
>
> $b.f(x) \cdot f\left( \frac{1}{x} \right) = 1$
>
> $c.\forall x \geq 0,f(x) \geq 0$
>
> $d.\text{若}\forall x \in (0\text{，}1)\text{，}f(x) < 1\text{或}\forall x \in (1, + \infty)\text{，}f(x) > 1\text{，则}f(x)\text{单调递增；}$
>
> $\ \ \ \ \text{若}\forall x \in (0\text{，}1)\text{，}f(x) > 1\text{或}\forall x \in (1, + \infty)\text{，}f(x) < 1\text{，则}f(x)\text{单调递增}$

$5.f(x + y) = f(x) + f(y) + 2axy - c\text{，令}f(x) = ax^{2} + bx + c$

$5.f(x + y) + f(x - y) = 2f(x)f(y)\text{，令}f(x) = \cos{\omega x}$

$6.f(x) + f(y) = 2f\left( \frac{x + y}{2} \right)f\left( \frac{x - y}{2} \right)\text{，令}f(x) = \cos{\omega x}$

$7.f(x) + f(y) = \frac{f(x) \pm f(y)}{1 \mp f(x)f(y)}\text{，令}f(x) = \tan{\omega x}$

函数方程（$f(x)$连续）

1.$f(x + y) = f(x) + f(y) \Rightarrow f(x) = xf(1)$

2.$f(x + y) = f(x)f(y) \Rightarrow f(x) = \left( f(1) \right)^{x}$

3.$f(x + y) = f(x) + f(y) + kxy \Rightarrow f(x) = ax^{2} + bx$

4.$f(x + y) + f(x - y) = 2f(x) \Rightarrow f(x) = ax + b$

5.$f^{2}(x + y) = f^{2}(x) + f^{2}(y) \Rightarrow f(x) = 0$

6.$f(x + y) - f(y - x) = f(x)f(y) \Rightarrow f(x) = 0$

其它结论

> 若$f(x + a) = \left| f(x) \right|$，则$f(x) \geq 0$

导数

导数的定义

设函数$y = f(x)$在点$x_{0}$的某个邻域内有定义，当自变量$x$在$x_{0}$处取得增量$\mathrm{\Delta}x$（点$x_{0} + \mathrm{\Delta}x$仍在该邻域内）时，相应地，因变量取得增量$\mathrm{\Delta}y = f\left( x_{0} + \mathrm{\Delta}x \right) - f\left( x_{0} \right)$；如果$\mathrm{\Delta}y$与$\mathrm{\Delta}x$之比当$\mathrm{\Delta}x \rightarrow 0$时的极限存在，那么称函数$y = f(x)$在点$x_{0}$处可导，并称这个极限为函数$y = f(x)$在点$x_{0}$处的导数，记为$f'(x)$，即

$f'\left( x_{0} \right) = \lim_{\mathrm{\Delta}x \rightarrow 0}\frac{\mathrm{\Delta}y}{\mathrm{\Delta}x} = \lim_{\mathrm{\Delta}x \rightarrow 0}\frac{f\left( x_{0} + \mathrm{\Delta}x \right) - f\left( x_{0} \right)}{\mathrm{\Delta}x}$

$\text{也可记作}y'\left. \  \right|_{x = x_{0}}\text{，}\frac{dy}{dx}\left| \begin{array}{r} \\ \underset{x = x_{0}}{} \end{array} \right.\ \text{或}\frac{df(x)}{dx}\left| \begin{array}{r} \\ \underset{x = x_{0}}{} \end{array} \right.\$

于是得到导函数的定义式

$y' = f'(x) = \frac{dy}{dx} = \frac{df(x)}{dx} = \lim_{\mathrm{\Delta}x \rightarrow 0}\frac{f(x + \mathrm{\Delta}x) - f(x)}{\mathrm{\Delta}x}$

且有

$f'\left( x_{0} \right) = f'(x)\left. \  \right|_{x = x_{0}}$

一些基本函数的导数及证明

$1.y = f(x) = c$

$\frac{\Delta y}{\Delta x} = \frac{f(x + \Delta x) - f(x)}{\Delta x} = \frac{c - c}{\Delta x} = 0 \Rightarrow y' = \lim_{\Delta x \rightarrow 0}\frac{\Delta y}{\Delta x} = \lim_{\Delta x \rightarrow 0}0 = 0$

$2.y = f(x) = x$

$\frac{\Delta y}{\Delta x} = \frac{f(x + \Delta x) - f(x)}{\Delta x} = \frac{(x + \Delta x) - x}{\Delta x} = 1 \Rightarrow y' = \lim_{\Delta x \rightarrow 0}\frac{\Delta y}{\Delta x} = \lim_{\Delta x \rightarrow 0}1 = 1$

$3.y = f(x) = x^{2}$

$\frac{\Delta y}{\Delta x} = \frac{f(x + \Delta x) - f(x)}{\Delta x} = \frac{(x + \Delta x)^{2} - x^{2}}{\Delta x} = \frac{x^{2} + 2x \cdot \Delta x + (\Delta x)^{2} - x^{2}}{\Delta x} = 2x + \Delta x \Rightarrow y' = \lim_{\Delta x \rightarrow 0}\frac{\Delta y}{\Delta x} = \lim_{\Delta x \rightarrow 0}(2x + \Delta x) = 2x$

$4.y = f(x) = x^{3}$

$\frac{\Delta y}{\Delta x} = \frac{f(x + \Delta x) - f(x)}{\Delta x} = \frac{(x + \Delta x)^{3} - x^{3}}{\Delta x} = \frac{x^{3} + 3x^{2} \cdot \Delta x + 3x \cdot (\Delta x)^{2} + (\Delta x)^{3} - x^{3}}{\Delta x} = 3x^{2} + 3x \cdot \Delta x + (\Delta x)^{2} \Rightarrow y' = \lim_{\Delta x \rightarrow 0}\frac{\Delta y}{\Delta x} = \lim_{\Delta x \rightarrow 0}\left\lbrack 3x^{2} + 3x \cdot \Delta x + (\Delta x)^{2} \right\rbrack = 3x^{2}$

$5.y = f(x) = \frac{1}{x}$

$\frac{\Delta y}{\Delta x} = \frac{f(x + \Delta x) - f(x)}{\Delta x} = \frac{\frac{1}{x + \Delta x} - \frac{1}{x}}{\Delta x} = \frac{x - (x + \Delta x)}{x(x + \Delta x)\Delta x} = - \frac{1}{x^{2} + x \cdot \Delta x} \Rightarrow y' = \lim_{\Delta x \rightarrow 0}\frac{\Delta y}{\Delta x} = \lim_{\Delta x \rightarrow 0}\left( - \frac{1}{x^{2} + x \cdot \Delta x} \right) = - \frac{1}{x^{2}}$

$6.y = f(x) = \sqrt{x}$

$\frac{\Delta y}{\Delta x} = \frac{f(x + \Delta x) - f(x)}{\Delta x} = \frac{\sqrt{x + \Delta x} - \sqrt{x}}{\Delta x} = \frac{\left( \sqrt{x + \Delta x} - \sqrt{x} \right)\left( \sqrt{x + \Delta x} + \sqrt{\Delta x} \right)}{\Delta x\left( \sqrt{x + \Delta x} + \sqrt{x} \right)} = \frac{1}{\sqrt{x + \Delta x} + \sqrt{x}} \Rightarrow y' = \lim_{\Delta x \rightarrow 0}\frac{\Delta y}{\Delta x} = \lim_{\Delta x \rightarrow 0}\frac{1}{\sqrt{x + \Delta x} + \sqrt{x}} = \frac{1}{2\sqrt{x}}$

高阶导数

二阶导数、三阶导数、四阶导数、n阶导数可用如下符号表示

$y^{''}\ \ \frac{d^{2}y}{dx^{2}}\text{，}y^{'''}\ \ \frac{d^{3}y}{dx^{3}}\text{，}y^{(4)}\ \ \frac{d^{4}y}{dx^{4}}\text{，}y^{(n)}\ \ \frac{d^{n}y}{dx^{n}}$

所谓的零阶导数$f^{(0)}$可视作原函数$f(x)$。

常设新的函数来避免出现高阶导数的符号。

导数的求导法则

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

加减

</th>
<th>

$\left\lbrack f(x) \pm g(x) \right\rbrack' = f'(x) \pm g'(x)$

</th>
<th>

$(u \pm v)' = u' \pm v'$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

乘法

</td>
<td>

$\left\lbrack f(x)g(x) \right\rbrack' = f'(x)g(x) + f(x)g'(x)$

</td>
<td>

$(uv)' = u'v + uv'$

</td>
</tr>
<tr>
<td>

除法

</td>
<td>

$\left\lbrack \frac{f(x)}{g(x)} \right\rbrack' = \frac{f'(x)g(x) - f(x)g'(x)}{g^{2}(x)}$

</td>
<td>

$\left( \frac{u}{v} \right)' = \frac{u'v - uv'}{v^{2}}$

</td>
</tr>
<tr>
<td>

复合

</td>
<td>

$f\left\lbrack g(x) \right\rbrack' = f'\left\lbrack g(x) \right\rbrack g'(x)$

</td>
<td>

$y_{x}' = y_{u}' + u_{x}'$

</td>
</tr>
<tr>
<td>

反函数

</td>
<td>

$\left\lbrack f^{- 1}(x) \right\rbrack' = \frac{1}{f'(x)}$

</td>
<td></td>
</tr>
</tbody>
</table>
</div>

常见函数的导数

> $\left( a^{x} \right)' = a^{x}\ln a$
>
> $\left( \log_{a}x \right)' = \frac{1}{x\ln a}$
>
> $\left\lbrack f(x + a) \right\rbrack' = f'(x + a)$
>
> $\left\lbrack af(x) \right\rbrack' = af'(x)$
>
> $\left\lbrack f(ax) \right\rbrack' = af'(ax)$
>
> $\left\lbrack e^{x}f(x) \right\rbrack' = e^{x}\left\lbrack f(x) + f'(x) \right\rbrack$
>
> $\left\lbrack \frac{f(x)}{e^{x}} \right\rbrack' = \frac{f'(x) - f(x)}{e^{x}}$
>
> $\left( \tan x \right)' = = \frac{1}{\cos^{2}x}$
>
> $\left( x\ln x \right)' = \ln x + 1$
>
> $\left( x^{x} \right)' = \left( e^{x\ln x} \right)' = e^{x\ln x}\left( x\ln x \right)' = x^{x}\left( \ln x + 1 \right)$
>
> $\left( c^{f(x)} \right)' = \left( e^{f(x)\ln c} \right)' = c^{f(x)}\ln c \cdot f'(x)$
>
> $\left\lbrack f^{g(x)}(x) \right\rbrack' = \left( e^{g(x)\ln{f(x)}} \right)' = f^{g(x)}(x)\left( f'(x) \cdot \frac{g(x)}{f(x)} + g'(x)\ln{f(x)} \right)$

导数与函数的性质

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$f(x)$

</th>
<th>

$f'(x)$

</th>
<th>

$f^{''}(x)$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$x_{0}$是$f(x)$的极小值点

</td>
<td>

$f'\left( x_{0} \right) = 0$

</td>
<td>

$f^{''}\left( x_{0} \right) > 0$

</td>
</tr>
<tr>
<td>

$x_{0}$是$f(x)$的极大值点

</td>
<td>

$f'\left( x_{0} \right) = 0$

</td>
<td>

$f^{''}\left( x_{0} \right) < 0$

</td>
</tr>
<tr>
<td>

$x_{0}$是$f(x)$的驻点/可移点

</td>
<td>

$f'\left( x_{0} \right) = 0$

</td>
<td>

$f^{''}\left( x_{0} \right) = 0$

</td>
</tr>
</tbody>
</table>
</div>

隐函数求导

方法一：

设该隐函数能写成$f(y) = g(x)$的形式，则

$f'(y)y' = g'(x)$

$eg.$

> $e^{y} + xy - e = 0 \Rightarrow e^{y}y' + y + xy' = 0 \Rightarrow y' = - \frac{y}{x + e^{y}}$
>
> $\frac{x^{2}}{m} + \frac{y^{2}}{n} = 1 \Rightarrow \frac{2}{m}x + \frac{2}{n}yy' = 0 \Rightarrow y' = - \frac{ny}{mx}$
>
> $y = x^{\sin x} \Rightarrow \ln y = \sin x\ln x \Rightarrow \frac{1}{y}y' = \cos x \cdot \ln x + \sin x \cdot \frac{1}{x} \Rightarrow y' = x^{\sin x}\left( \cos x \cdot \ln x + \frac{\sin x}{x} \right)$

方法二：

设该隐函数能写成二元函数$f(x\text{，}y) = 0$的形式，则

$\frac{dy}{dx} = \frac{\frac{\partial F}{\partial x}}{\frac{\partial F}{\partial y}} = - \frac{F_{x}}{F_{y}}$

$\frac{d^{2}y}{dx^{2}} = \frac{\partial}{\partial x}\left( - \frac{F_{x}}{F_{y}} \right) + \frac{\partial}{\partial y}\left( - \frac{F_{x}}{F_{y}} \right)\frac{dy}{dx} = - \frac{F_{xx}F_{y}^{2} - 2F_{xy}F_{x}F_{y} + F_{yy}F_{x}^{2}}{F_{y}^{3}}$

$eg.$

$x^{2} + y^{2} - 1 = 0 \Rightarrow \frac{dy}{dx} = - \frac{F_{x}}{F_{y}} = - \frac{2x}{2y} = - \frac{x}{y}$

补充：偏导数举例

$F(x\text{，}y) = x^{2}\sin{2y} \Rightarrow F_{x} = \frac{\partial z}{\partial x} = 2x\sin{2y}(\text{把}y\text{看作常数})\text{，}F_{y} = \frac{\partial z}{\partial y} = 2x^{2}\cos{2y}(\text{把}x\text{看作常数})$

函数的稳定点与不动点

已知$x_{0} \in D_{f}$，则有

不动点：$f\left( x_{0} \right) = x_{0}$

稳定点：$f\left( f\left( x_{0} \right) \right) = x_{0}$

由定义，若一个函数有不动点，则该点也是稳定点，反之不一定成立。

性质

1.若$f(x)$具有全局单调性，则$f(x)$的所有稳定点均为不动点。

2.$f(x)$的稳定点是$f(x)$与$f^{- 1}(x)$的交点，$f(x)$的不动点是横、纵坐标相同的稳定点。

比较大小

> 1. 作差/商
>
> 根本大法。
>
> 2. 换同底
>
> 3. 幂同乘
>
> 4. 桥梁法
>
> 5. 有理化
>
> 6. 取对数
>
> 7. 单调性
>
> 基本方法
>
> 8. 放缩
>
> 基本方法
>
> 9. 构造函数（同构）
>
> 7的加强版
>
> 10.记数字与泰勒展开

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$\sqrt{2} = 1.4142$

</th>
<th>

$\sqrt{3} = 1.7321$

</th>
<th>

$\sqrt{5} = 2.2361$

</th>
<th>

$\sqrt{7} = 2.6458$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\ln 2 = 0.6931$

</td>
<td>

$\ln 3 = 1.0986$

</td>
<td>

$\ln 5 = 1.6094$

</td>
<td>

$\ln 7 = 1.9459$

</td>
</tr>
<tr>
<td>

$\lg 2 = 0.3010$

</td>
<td>

$\lg 3 = 0.4771$

</td>
<td>

$\lg 5 = 0.6990$

</td>
<td>

$\lg 7 = 0.8451$

</td>
</tr>
<tr>
<td>

$e^{2} = 7.3891$

</td>
<td>

$e^{3} = 20.0855$

</td>
<td>

$\sqrt{e} = 1.6487$

</td>
<td>

$\sqrt[3]{e} = 1.3956$

</td>
</tr>
<tr>
<td>

$\pi^{2} = 9.8696$

</td>
<td>

$\sqrt{\pi} = 1.7725$

</td>
<td>

$\ln\pi = 1.1447$

</td>
<td>

$\lg\pi = 0.4971$

</td>
</tr>
<tr>
<td>

$\sin 1 = 0.8415$

</td>
<td>

$\cos 1 = 0.5403$

</td>
<td>

$\tan 1 = 1.5574$

</td>
<td>

$\lg e = 0.4343$

</td>
</tr>
</tbody>
</table>
</div>

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$\sin{\text{高考年份}{^\circ}}$

</th>
<th>

$\cos{\text{高考年份}{^\circ}}$

</th>
<th>

$\tan{\text{高考年份}{^\circ}}$

</th>
<th>

$\sin{\text{高考年份}}$

</th>
<th>

$\cos{\text{高考年份}}$

</th>
<th>

$\tan{\text{高考年份}}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

> 按照从小到大排列有：
>
> $(0\text{，}1)\text{：}\lg 2 < \lg e < \lg 3 < \lg\pi < \cos 1 < \ln 2 < \lg 5 < \sin 1 < \lg 7$
>
> $(1\text{，}2)\text{：}\ln 3 < \ln\pi < \sqrt[3]{e} < \sqrt{2} < \tan 1 < \ln 5 < \sqrt{e} < \sqrt{3} < \sqrt{\pi} < \ln 7$
>
> $(2\text{，} + \infty)\text{：}\sqrt{5} < \sqrt{7} < e^{2} < e^{3}$
>
> 11.泰勒展开
>
> 泰勒公式

$f(x) = \sum_{k = 1}^{\infty}{\frac{f^{(k)}\left( x_{0} \right)}{k!}\left( x - x_{0} \right)^{k}} = \frac{f\left( x_{0} \right)}{0!} + \frac{f'\left( x_{0} \right)}{1!}\left( x - x_{0} \right) + \frac{f^{''}\left( x_{0} \right)}{2!}\left( x - x_{0} \right)^{2} + \ldots + \frac{f^{(n)}\left( x_{0} \right)}{n!}\left( x - x_{0} \right)^{n}$

> 常用结论
>
> $1.e^{x} = 1 + \frac{x}{1} + \frac{x^{2}}{2} + \frac{x^{3}}{6} + \ldots = \sum_{n = 0}^{\infty}\frac{x^{n}}{n!}\ \  \Rightarrow \ \ a^{x} = e^{x\ln a} = \sum_{n = 0}^{\infty}\frac{\left( \ln a \right)^{n}x^{n}}{n!}$
>
> $2.\sin x = \frac{x}{1!} - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + \ldots = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{(2n + 1)!}x^{2n + 1}}$
>
> $3.\cos x = 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} - \frac{x^{6}}{6!} + \ldots = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{(2n)!}x^{2n}}$
>
> $4.\ln(1 + x) = x - \frac{x^{2}}{2!} + \frac{x^{3}}{3!} - \frac{x^{4}}{4!} + \ldots = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n - 1}}{n!}x^{n}}\ \ ( - 1 < x \leq 1)\ \  \Rightarrow$
>
> $5.\ln(1 - x) = - x - \frac{x^{2}}{2!} - \frac{x^{3}}{3!} - \frac{x^{4}}{4!} + \ldots = \sum_{n = 0}^{\infty}{\frac{- 1}{n!}x^{n}}\ \ ( - 1 < x \leq 1)\ \  \Rightarrow$
>
> $6.\ln\frac{1 + x}{1 - x} = 2\left( x + \frac{1}{3}x^{3} + \frac{1}{5}x^{5} + \cdots \right) = 2\sum_{n = 0}^{\infty}\frac{x^{2n + 1}}{2n + 1}\ \ ( - 1 < x \leq 1)$
>
> $7.\sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^{2}}{8} + \frac{x^{3}}{16} - \frac{5x^{4}}{128} + \ldots$
>
> $8.\frac{1}{1 - x} = 1 + x + x^{2} + x^{3} + \cdots = \sum_{n = 0}^{\infty}x^{n}\ \ \left( |x| < 1 \right)$
>
> $9.\frac{1}{1 + x} = 1 - x + x^{2} - x^{3} + \cdots = \sum_{n = 0}^{\infty}{( - 1)^{n}x^{n}}\ \ \left( |x| < 1 \right)\ \  \Rightarrow \ \ \frac{1}{1 + x^{2}} = \sum_{n = 0}^{\infty}{( - 1)^{n}x^{2n}}\ \ \left( |x| < 1 \right)$
>
> $10.(1 + x)^{m} = 1 + mx + \frac{m(m - 1)}{2!}x^{2} + \cdots + \frac{m(m - 1)\cdots(m - n + 1)}{m!}x^{n} + \cdots\ \ \left( |x| < 1 \right)$
>
> $eg.\ln 2 = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots$（第4个结论）的误差
>
> $\left| r_{n} \right| \leq \frac{1}{n + 1}$
>
> 而用第6个结论，能得到更好的近似：
>
> $\ln 2 = 2\left( \frac{1}{3} + \frac{1}{3} \cdot \frac{1}{3^{3}} + \frac{1}{5} \cdot \frac{1}{3^{5}} + \frac{1}{7} \cdot \frac{1}{3^{7}} + \cdots \right)$
>
> 其误差小于$\frac{1}{70000}$
>
> $eg.\sqrt[5]{240} = \sqrt[5]{243 - 3} = 3\left( 1 - \frac{1}{3^{4}} \right)^{1/5} \approx 3\left( 1 - \frac{1}{5} \cdot \frac{1}{3^{4}} \right)$

指数放缩

对数放缩

对数均值不等式

对于任意$a\text{，}b \in \mathbb{R}_{+}$，令

$L(a\text{，}b) = \left\{ \begin{array}{r} \frac{a - b}{\ln a - \ln b}\ \ \ (a \neq b) \\ \ \ \ \ \ \ \ \ \ a\ \ \ \ \ \ \ \ \ \ \ \ (a = b) \end{array} \right.\$

则

$\sqrt{ab} \leq L(ab) \leq \frac{a + b}{2}$

指数均值不等式

对于任意$x\text{，}y\mathbb{\in R}$，有

$e^{\frac{x + y}{2}} \leq \frac{e^{x} - e^{y}}{x - y} \leq \frac{e^{x} + e^{y}}{2}$

由对数均值不等式把a和b分别替换为![图示 描述已自动生成](/images/hs/hs-a03/img01.png)$e^{x}$和$e^{y}$得到。

几个常见函数及其导数

$y = \frac{\ln x}{x}\ \ \ \ \ \ \ y' = \frac{- \ln x + 1}{x^{2}}$

$y = \frac{x}{e^{x}}\ \ \ \ \ \ \ \ \ y' = \frac{- x + 1}{e^{x}}$

$y = x\ln x\ \ \ y' = \ln x + 1$

$y = xe^{x}\ \ \ \ \ \ \ y' = e^{x} + xe^{x}$

![图示, 形状 描述已自动生成](/images/hs/hs-a03/img04.png)

![图示 中度可信度描述已自动生成](/images/hs/hs-a03/img05.png)

$y = \frac{x}{\ln x}\text{，}y' = \frac{\ln x - 1}{\ln^{2}x}$

$y = \frac{e^{x}}{x}\text{，}y' = \frac{- e^{x} + xe^{x}}{x^{2}}$

同构

可把复杂的部分设为t，再做整理。

地位等同同构（取$x_{1} < x_{2}$）

$\frac{f\left( x_{1} \right) - f\left( x_{2} \right)}{x_{1} - x_{2}} > k \Leftrightarrow f\left( x_{1} \right) - f\left( x_{2} \right) < kx_{1} - kx_{2} \Leftrightarrow f\left( x_{1} \right) - kx_{1} < f\left( x_{2} \right) - kx_{2}\overset{g(x) = f(x) - kx}{\Leftrightarrow}g\left( x_{1} \right) < g\left( x_{2} \right)$

$\frac{f\left( x_{1} \right) - f\left( x_{2} \right)}{x_{1} - x_{2}} < \frac{k}{x_{1}x_{2}} \Leftrightarrow f\left( x_{1} \right) - f\left( x_{2} \right) > \frac{k\left( x_{1} - x_{2} \right)}{x_{1}x_{2}} \Leftrightarrow f\left( x_{1} \right) + \frac{k}{x_{1}} > f\left( x_{2} \right) + \frac{k}{x_{2}}\overset{g(x) = f(x) + \frac{k}{x}}{\Leftrightarrow}g\left( x_{1} \right) > g\left( x_{2} \right)$

指对同构理论

$x = a^{\log_{a}x} = \log_{a}a^{x} = e^{\ln x} = \ln e^{x}$

$f(x)e^{x} = e^{\ln{f(x)} + x}\text{，}\frac{e^{x}}{f(x)} = e^{x - \ln{f(x)}}\text{，}ae^{x} = e^{\ln a + x}\text{，}\frac{e^{x}}{a} = e^{x - \ln a}\text{，}x^{m}e^{x} = e^{m\ln x + x}\text{，}\frac{e^{x}}{x^{m}} = e^{x - m\ln x}$

以下的a和b可指代关于x的函数或常数

$\text{积型：}ae^{a} = b\ln b \Rightarrow \left\{ \begin{array}{r} \text{同左：}ae^{x} = e^{\ln b}\ln b\overset{f(x) = xe^{x}}{\Rightarrow}f(a) = f\left( \ln b \right)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \text{同右：}\ln e^{a}e^{a} = b\ln b\overset{f(x) = x\ln x}{\Rightarrow}f\left( e^{a} \right) = f(b)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \text{取对：}a + \ln a = \ln b + \ln{\ln b}\overset{f(x) = x + \ln x}{\Rightarrow}f(a) = f\left( \ln b \right) \end{array} \right.\$

$\text{商型：}\frac{e^{a}}{a} = \frac{b}{\ln b} \Rightarrow \left\{ \begin{array}{r} \text{同左：}\frac{e^{a}}{a} = \frac{e^{\ln b}}{\ln b}\overset{f(x) = \frac{e^{x}}{x}}{\Rightarrow}f(a) = f\left( \ln b \right)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \text{同右：}\frac{e^{a}}{\ln e^{a}} = \frac{b}{\ln b}\overset{f(x) = \frac{x}{\ln x}}{\Rightarrow}f\left( e^{a} \right) = f(b)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \text{取对：}a - \ln a = \ln b - \ln{\ln b}\overset{f(x) = x - \ln x}{\Rightarrow}f(a) = f\left( \ln b \right) \end{array} \right.\$

和型：$e^{a} \pm a = b \pm \ln b\left\{ \begin{array}{r} \text{同左：}e^{a} \pm a = e^{\ln b} \pm \ln b\overset{f(x) = e^{x} \pm x}{\Rightarrow}f(a) = f\left( \ln b \right) \\ \text{同右：}e^{a} \pm \ln e^{a} = b \pm \ln b\overset{f(x) = x \pm \ln x}{\Rightarrow}f\left( e^{a} \right) = f(b) \end{array} \right.\$

指对同构实践

$1.ae^{ax} > \ln x \Rightarrow axe^{ax} > x\ln x \Rightarrow ax + \ln{ax} > \ln x + \ln{\ln x}$

$2.a^{x} > \log_{a}x \Rightarrow e^{x\ln a} > \frac{\ln x}{\ln a} \Rightarrow x\ln ae^{x\ln a} > x\ln x \Rightarrow \ln\left( x\ln a \right) + e\ln a > \ln x + \ln{\ln x}$

$3.e^{x - 1} \geq \ln x + 1 \Rightarrow e^{x - 1} + x - 1 \geq \ln x + 1 + x - 1 = x + \ln x$

$4.ae^{x - 1} - \ln x + \ln a > 1 \Rightarrow e^{\ln a + x - 1} + \ln a + x - 1 > x + \ln x$

$5.\left( e^{x} - 1 \right)\ln(x + 1) > x^{2} \Rightarrow \frac{\ln(x + 1)}{x} > \frac{x}{e^{x} - 1} = \frac{\ln\left\lbrack \left( e^{x} - 1 \right) + 1 \right\rbrack}{e^{x} - 1} \Rightarrow f(x) = \frac{\ln(x + 1)}{x}$

$6.a\left( e^{ax} + 1 \right) \geq 2\left( x + \frac{1}{x} \right)\ln x \Rightarrow ax\left( e^{ax} + 1 \right) \geq 2\left( x^{2} + 1 \right)\ln x \Rightarrow axe^{ax} + ax \geq \left( x^{2} + 1 \right)\ln x^{2} = x^{2}\ln x^{2} + \ln x^{2} = e^{\ln x^{2}}\ln x^{2} + \ln x^{2} \Rightarrow f(x) = xe^{x} + x$

$7.ae^{x} + \ln\frac{a}{x + 2} - 2 > 0 \Rightarrow e^{\ln a + x} + \ln a - \ln(x + 2) - 2 > 0 \Rightarrow e^{\ln a + x} + \ln a + x > x + 2 + \ln(x + 2)$

$8.x^{2}\ln x - me^{\frac{m}{x}} \geq 0 \Rightarrow x\ln x \geq \frac{m}{x}e^{\frac{m}{x}} \Rightarrow \ln x + \ln{\ln x} \geq \ln\frac{m}{x} + \frac{m}{x} \Rightarrow f(x) = x + \ln x$

$9.x^{2}e^{x} + \ln x = 0 \Rightarrow e^{x + 2\ln x} + x + 2\ln x = x + \ln x \Rightarrow e^{x + 2\ln x} + x + 2\ln x = e^{\ln x} + \ln x$

原函数与导函数混合还原模型

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$f'(x) \pm g'(x) = 0$

</th>
<th>

$h(x) = f(x) \pm g(x)$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$f'(x)g(x) + f(x)g'(x)$

</td>
<td>

$h(x) = f(x) \cdot g(x)$

</td>
</tr>
<tr>
<td>

$f'\left\lbrack g(x) \right\rbrack \cdot g'(x) = 0$

</td>
<td>

$h(x) = f\left\lbrack g(x) \right\rbrack$

</td>
</tr>
<tr>
<td>

$(x + a)f'(x) + kf(x) = 0$

</td>
<td>

$g(x) = (x + a)^{k} \cdot f(x)$

</td>
</tr>
<tr>
<td>

$f'(x) + kf(x) + a = 0$

</td>
<td>

$g(x) = e^{kx}\left\lbrack f(x) + \frac{a}{k} \right\rbrack$

</td>
</tr>
<tr>
<td>

$\sin x \cdot f'(x) + \cos x \cdot f(x) = 0$

</td>
<td>

$g(x) = f(x) \cdot \sin x$

</td>
</tr>
<tr>
<td>

$\sin x \cdot f'(x) - \cos x \cdot f(x) = 0$

</td>
<td>

$g(x) = \frac{f(x)}{\sin x}$

</td>
</tr>
<tr>
<td>

$\cos x \cdot f'(x) - \sin x \cdot f(x) = 0$

</td>
<td>

$g(x) = f(x) \cdot \cos x$

</td>
</tr>
<tr>
<td>

$\cos x \cdot f'(x) + \sin x \cdot f(x) = 0$

</td>
<td>

$g(x) = \frac{f(x)}{\cos x}$

</td>
</tr>
<tr>
<td>

$\frac{f'(x)}{f(x)} = 0\ /\ f'(x)f(x) = 0$

</td>
<td>

$g(x) = \ln{f(x)}$

</td>
</tr>
<tr>
<td>

$f'(x)\ln x + \frac{f(x)}{x} = 0$

</td>
<td>

$g(x) = \ln x \cdot f(x)$

</td>
</tr>
</tbody>
</table>
</div>

这种构造函数的方法本质上是求解一个微分方程，需要求积分的经验。下面是用分离变量法解这种题的步骤：

$1.\text{把题设中的不等号转换为等号，把}f(x)\text{写成}y\text{，把}f'(x)\text{写成}\frac{dy}{dx}\text{。}$

2.把含x项和含$dx$放在等号左边，含y项和含$dy$放在等号右边。

3.解这个“可分离变量的微分方程”，把积分得到的常数写成$\pm \ln C$的形式，放在等号右侧，其中$\pm \ln C$的符号与$\ln y$前的符号相反。

4.写出$C$的表达式

5.把$C$改写成新函数$g(x)$，并把$y$换回$f(x)\text{，}$则$g(x)$即为要构造的函数

6.求$g'(x)$

$eg.\text{已知}\left( x^{2} - 5x + 6 \right)f'(x) + \left( x^{2} - 2x - 2 \right)f(x) > 0\text{对于}\forall x \in ( - \infty \text{，}2\rbrack \text{恒成立}$

> $1.\left( x^{2} - 5x + 6 \right)\frac{dy}{dx} + \left( x^{2} - 2x - 2 \right)y = 0$
>
> $2. - \frac{x^{2} - 2x - 2}{x^{2} - 5x + 6}dx = \frac{1}{y}dy$
>
> $3.x + \ln(x - 3) + 2\ln(x - 2) = \ln y - \ln C$
>
> $4.C = (x - 3)(x - 2)^{2}e^{x}y$
>
> $5.g(x) = (x - 2)(x - 2)^{2}e^{x}f(x)$
>
> $6.g'(x) = \left\lbrack \left( x^{2} - 5x + 6 \right)f'(x) + \left( x^{2} - 2x - 2 \right)f(x) \right\rbrack e^{x} \cdot 2(x - 2)$

极值点偏移

$\text{已知}f\left( x_{1} \right) = f\left( x_{2} \right)\text{，}x_{1} < x_{2}\text{，求证：}x_{0} < \frac{x_{1} + x_{2}}{2}$

核心，把$x_{1}$和$x_{2}$转化到$f(x)$的一个单调区间，利用函数的单调性套上$f$并实现双变单，在构造新函数求导证明。

证明：

（1）综合法

> $f'(x) = \cdots \text{，}f(x)\text{在}\left( - \infty \text{，}x_{0} \right)\text{单调递增，在}\left( x_{0}\text{，} + \infty \right)\text{单调递减}$，得$x_{1} < x_{0} < x_{2}$
>
> 由$x_{2} > x_{0}$，得$2x_{0} - x_{2} < x_{0}$
>
> 令$g(x) = f(x) - f\left( 2x_{0} - x \right)$，则$g\left( x_{0} \right) = 0$
>
> $g'(x) = f'(x) + f'\left( 2x_{0} - x \right)$，对于任意$x \in \left( x_{0} + \infty \right)$，$g'(x) > 0$
>
> 又$g\left( x_{0} \right) = 0$，所以对于任意$x \in \left( x_{0} + \infty \right)$，$g(x) > 0$
>
> $\text{由}x_{2} > x_{0}$得，$f\left( x_{2} \right) - f\left( 2x_{0} - x_{2} \right) > 0$，即$f\left( x_{2} \right) > f\left( 2x_{0} - x_{2} \right)$
>
> 因为$f\left( x_{1} \right) = f\left( x_{2} \right)\text{，}$所以$f\left( x_{1} \right) > f\left( 2x_{0} - x_{2} \right)$
>
> 由$x_{1} < x_{0}$，$2x_{0} - x_{2} < x_{0}$，$f(x)\text{在}\left( - \infty \text{，}x_{0} \right)\text{单调递增}$，得

$x_{1} > 2x_{0} - x_{2}\text{，即}x_{0} < \frac{x_{1} + x_{2}}{2}$

（2）分析法

> $f'(x) = \cdots \text{，}f(x)\text{在}\left( - \infty \text{，}x_{0} \right)\text{单调递增，在}\left( x_{0}\text{，} + \infty \right)\text{单调递减}$，得$x_{1} < x_{0} < x_{2}$
>
> 由$x_{2} > x_{0}$，得$2x_{0} - x_{2} < x_{0}$（把$x_{1}$和$x_{2}\left( \text{即}2x_{0} - x_{2} \right)$放到同一个单调区间）
>
> 要证$x_{0} < \frac{x_{1} + x_{2}}{2}$，即证$x_{1} > 2x_{0} - x_{2}$
>
> 由$f(x)\text{在}\left( - \infty \text{，}x_{0} \right)\text{单调递增，}$即证$f\left( x_{1} \right) > f\left( 2x_{0} - x_{2} \right)$
>
> 由$f\left( x_{1} \right) = f\left( x_{2} \right)$，即证$f\left( x_{2} \right) > f\left( 2x_{0} - x_{2} \right)$
>
> 令$g(x) = f(x) - f\left( 2x_{0} - x \right)$，则$g\left( x_{0} \right) = 0$
>
> $g'(x) = f'(x) + f'\left( 2x_{0} - x \right)$，对于任意$x \in \left( x_{0} + \infty \right)$，$g'(x) > 0$
>
> 又$g\left( x_{0} \right) = 0$，所以对于任意$x \in \left( x_{0} + \infty \right)$，$g(x) > 0$
>
> $\text{由}x_{2} > x_{0}$得，$f\left( x_{2} \right) - f\left( 2x_{0} - x_{2} \right) > 0$
>
> 即$f\left( x_{2} \right) > f\left( 2x_{0} - x_{2} \right)$，得证。

三次函数

$y = ax^{3} + bx^{2} + cx + d$

判别式：$\Delta = 4\left( b^{2} - 3ac \right)$

设$x_{1} < x_{2}$

单调性：

$a > 0\left\{ \begin{array}{r} \Delta \leq 0\text{：在}\mathbb{R}\text{上} \nearrow \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \Delta > 0\text{：在}\left( - \infty \text{，}x_{1} \right) \nearrow \text{，}\left( x_{1}\text{，}x_{2} \right) \searrow \text{，}\left( x_{2}\text{，} + \infty \right) \nearrow \end{array} \right.\$

$a < 0\left\{ \begin{array}{r} \Delta \leq 0\text{：在}\mathbb{R}\text{上} \searrow \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \Delta > 0\text{：在}\left( - \infty \text{，}x_{1} \right) \searrow \text{，}\left( x_{1}\text{，}x_{2} \right) \nearrow \text{，}\left( x_{2}\text{，} + \infty \right) \searrow \end{array} \right.\$

极值点

$\Delta \leq 0\text{，没有极值点；}\Delta > 0\text{，有}2\text{个极值点}$

奇偶性

$b = d = 0\text{，奇函数；否则为非奇非偶函数}$

对称性

$\text{中心对称函数，对称中心为}\left( - \frac{2b}{3a}\text{，}f\left( - \frac{2b}{3a} \right) \right)$

与x轴交点个数

$\begin{matrix} 1\text{个交点：极大值} < 0\text{或极小值} > 0 \\ 2\text{个交点：极大值} = 0\text{或极小值} = 0 \\ 3\text{个交点：极大值} \times \text{极小值} < 0\ \ \ \ \ \ \ \ \ \end{matrix}$

函数图像

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th colspan="2">

$a > 0$

</th>
<th colspan="2">

$a < 0$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

导函数

</td>
<td>

$\Delta \leq 0$

</td>
<td>

$\Delta > 0$

</td>
<td>

$\Delta \leq 0$

</td>
<td>

$\Delta > 0$

</td>
</tr>
<tr>
<td>

图像

</td>
<td>

![](/images/hs/hs-a03/img06.png)

</td>
<td>

![](/images/hs/hs-a03/img07.png)

</td>
<td>

![](/images/hs/hs-a03/img08.png)

</td>
<td>

![](/images/hs/hs-a03/img09.png)

</td>
</tr>
</tbody>
</table>
</div>

![](/images/hs/hs-a03/img10.png)切线与割线

如图，过$(I)(III)$上的点可以做3条切线，过$(II)(IV)$上的点可以做1条切线，过直线或曲线上的点可以做2条切线

对于与曲线交于另一点的切线，有

$\text{切点横坐标的二倍} + \text{交点横坐标} = - \frac{b}{a}$

![](/images/hs/hs-a03/img02.png)常见函数在$(0\text{，}1)$的增长速率

$a:y = \frac{1}{1 - x} - 1$

$b:y = e^{x} - 1$

$c:y = \tan x$

$d:y = \sqrt{x}$

$e:y = x$

$f:y = x^{2}$

$g:y = \sin x$

$h:y = \ln(x + 1)$

$i:y = \frac{2x}{x + 2}$

![](/images/hs/hs-a03/img03.png)
