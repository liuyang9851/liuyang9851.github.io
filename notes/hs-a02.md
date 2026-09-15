---
title: "一元二次函数、方程和不等式"
hs_seq: "A2"
description: "一元二次函数、方程和不等式：一元二次函数、方程和不等式"
---

# 一元二次函数、方程和不等式

常见不等式的求解

> 1.一元一次不等式：去分母、去括号、移项、合并同类项、系数化为1
>
> 2.一元二次不等式：因式分解/求$\mathrm{\Delta}$/图像
>
> 3.分式不等式：移项、通分、化分为整
>
> $eg.\frac{x + 1}{x - 2} \leq - 1 \Rightarrow \frac{2x - 1}{x - 2} \leq 0 \Rightarrow (2x - 1)(x - 2) \leq 0 \Rightarrow x \in \left\lbrack \frac{1}{2}\text{，}2 \right)$
>
> 4.高次不等式：因式分解、数轴穿根法（从右上角开始、奇穿偶回）
>
> $eg.\left( x^{2} - 4 \right)( - x + 5)(x - 1)^{3}(x - 6)^{2} < 0 \Rightarrow (x + 2)(x - 1)^{3}(x - 2)(x - 5)(x - 6)^{2} > 0$
>
> $\Rightarrow x \in ( - \infty \text{，} - 2) \cup (1\text{，}2) \cup (5\text{，}6) \cup (6\text{，}\infty)$
>
> 5.绝对值不等式：两边平方、绝对值的定义、分类讨论
>
> 6.无理不等式：两边平方

不等式

不等式的基本性质

> 基本事实：$a > b \Leftrightarrow a - b > 0$
>
> $a = 0 \Leftrightarrow a - b = 0$
>
> $a < b \Leftrightarrow a - b < 0$
>
> 对称性：$a > b \Leftrightarrow b < a\text{，}a < b \Leftrightarrow b > a$
>
> 传递性：$a > b\text{，}b > c \Rightarrow a > c$
>
> $a < b\text{，}b < c \Rightarrow a < c$
>
> 可加性：$a + b > c \Leftrightarrow a + c > b + c$
>
> 移项法则：$a + b > c \Leftrightarrow a > c - b$
>
> 可乘性：$a > b\text{，}c > 0 \Rightarrow ac > bc$
>
> $a > b\text{，}c < 0 \Rightarrow ac < bd$
>
> 同向可加性：$a > b\text{，}c > d \Rightarrow a + c > b + d$
>
> 同向同正可乘性：$a > b > 0\text{，}c > d > 0 \Rightarrow ac > bd$
>
> 正可乘方性：$a > b > 0 \Rightarrow a^{n} > b^{n}\ \ \left( n\mathbb{\in N}\text{，}n \geq 2 \right)$

不等式的基本性质的推论

> $ab > 0\text{，}a > b \Rightarrow \frac{1}{a} < \frac{1}{b}\text{；}ab < 0\text{，}a > b \Rightarrow \frac{1}{a} > \frac{1}{b}$
>
> $a > b > 0\text{，}m > 0 \Rightarrow \frac{b}{a} < \frac{b + m}{a + m}\text{；}b > a > 0\text{，}m > 0 \Rightarrow \frac{b}{a} > \frac{b + m}{a + m}\ \ (\text{糖水不等式})$
>
> $a > b > 0 \Rightarrow \sqrt[n]{a} > \sqrt[n]{a}\ \ \left( n\mathbb{\in N}\text{，}n \geq 2 \right)$
>
> $a > b > 0 \Rightarrow a^{n} > b^{n}\ \ \left( n \in \mathbb{R}_{+} \right)$

重要不等式

> $a^{2} + b^{2} \geq 2ab\ \ (a\text{，}b\mathbb{\in R}\text{，当且仅当}a = b\text{时等号成立})$

基本不等式

> $\sqrt{ab} \leq \frac{a + b}{2}\ \ (a\text{，}b \in \mathbb{R}_{+}\text{，当且仅当}a = b\text{时等号成立})$

推论（略去等号成立的条件）

> 基本不等式的一般推论

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$a + b \geq 2\sqrt{ab}(a\text{，}b \in \mathbb{R}_{+})$

</th>
<th>

$ab \leq \left( \frac{a + b}{2} \right)^{2}\left( a\text{，}b\mathbb{\in R} \right)$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$2(a + b)^{2} \geq (a + b)^{2} \geq 4ab(a\text{，}b\mathbb{\in R)}$

</td>
<td>

$a^{2} + b^{2} \geq \frac{(a + b)^{2}}{2}$

</td>
</tr>
</tbody>
</table>
</div>

> 基本不等式在三维时的结论$(a\text{，}b\text{，}c \in \mathbb{R}_{+})$

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$a + b + c \geq 3\sqrt[3]{abc}$

</th>
<th>

$abc \leq \left( \frac{a + b + c}{3} \right)^{3}$

</th>
</tr>
</thead>
<tbody>

</tbody>
</table>
</div>

> （二维）均值不等式（调和均值≤几何均值≤对数均值≤算术均值≤平方均值）

$\frac{2}{\frac{1}{a} + \frac{1}{b}} \leq \sqrt{ab} \leq L(a\text{，}b) = \left\{ \begin{array}{r} \frac{a - b}{\ln a - \ln b}\ \ \ (a \neq b) \\ \ \ \ \ \ \ \ \ \ a\ \ \ \ \ \ \ \ \ \ \ \ (a = b) \end{array} \right.\  \leq \frac{a + b}{2} \leq \sqrt{\frac{a^{2} + b^{2}}{2}}(a,b \in \mathbb{R}_{+})$

> 柯西不等式

$\left( a^{2} + b^{2} \right)\left( c^{2} + d^{2} \right) \geq (ac + bd)^{2}\ \ \left( a\text{，}b \in \mathbb{R}\text{，当}\frac{a}{b} = \frac{c}{d}\text{时，等号成立} \right)$

> 可以简记为“方和积$\geq$积和方”
>
> 权方和不等式

$\frac{a^{2}}{x} + \frac{b^{2}}{y} \geq \frac{(a + b)^{2}}{x + y}\ \ \left( x\text{，}y \in \mathbb{R}_{+}\text{，当}\frac{a}{x} = \frac{b}{y}\text{时，等号成立} \right)$

> 其它

$\text{若}x,y \in \mathbb{R}_{+}\text{，则}\frac{x^{2} + y^{2} + m + n}{\sqrt{m}x + \sqrt{n}y} \geq 2$

三角不等式与向量三角不等式

绝对值不等式

$\left| |a| - |b| \right| \leq |a \pm b| \leq |a| + |b|\ \ \left( a\text{，}b\mathbb{\in C}\text{，}||\text{代表绝对值或模} \right)$

向量形式的绝对值不等式

$\left| \left| \mathbf{a} \right| - \left| \mathbf{b} \right| \right| \leq \left| \mathbf{a} \pm \mathbf{b} \right| \leq \left| \mathbf{a} \right| + \left| \mathbf{b} \right|$

与不等式有关的题型方法$\ \$(其中所有变量均为正数)

> 一、乘几除几
>
> $\text{对于}px + qy\text{与}\frac{m}{ax + by + e} + \frac{n}{cx + dy + f}\text{，已知其中一个值为}i\text{，求另一个的最小值}$
>
> $1.\text{若}px + qy = i\text{，求}\frac{m}{ax + by + e} + \frac{n}{cx + dy + f}\text{的最小值}$
>
> $\text{用配凑法，设}\alpha(ax + by) + \beta(cx + dy) = px + qy\text{，解得}\alpha \text{和}\beta \text{的值，得到相应的恒等式。}$
>
> $2.\text{若}\frac{m}{ax + by + e} + \frac{n}{cx + dy + f} = i\text{，求}px + qy\text{的最小值}$
>
> 与上种情况做法类似。
>
> $\text{特殊地，若有}ax + by = i\text{或}\frac{a}{x} + \frac{b}{y} = i(bx + ay = ixy)$
>
> $\text{则}\frac{c}{x} + \frac{d}{y}\text{或}cx + dy\text{的最小值为}\frac{ac + bd + 2\sqrt{abcd}}{i}$
>
> 二、桥梁法
>
> （对于$ax + by + cxy = i$，求$k(ax + by)\text{、}kxy\text{的最值}$）
>
> $1.\text{求}k(ax + by)\text{的最值}$
>
> $\text{由}ab\left\lbrack i - (ax + by) \right\rbrack = abcxy \leq c \cdot \left( \frac{ax + by}{2} \right)^{2}\text{，得}k(ax + by)\text{只有最小值}2k \cdot \frac{- ab + \sqrt{ab + abci}}{c}$
>
> $2.\text{求}kxy\text{的最值}$
>
> $i - cxy = ax + by \geq 2\sqrt{abxy}\text{，得}kxy\text{只有最大值}k \cdot \frac{ci + 2ab - 2\sqrt{a^{2}b^{2} + abci}}{c^{2}}$
>
> 不要谁谁当桥梁
>
> 三、地位等价
>
> 令未知量相等解方程或不等式，代入要求的式子，需要检验其为最大值还是最小值。
>
> 四、双变单
>
> 对于$ax + by + kxy = 0$，求$mx + ny\text{、}xy$的最值，以及其它便于消参的情况。
>
> 五、万能k法（万能$\mathrm{\Delta}$法）
>
> 令待求式为k，得到一个未知量的表达式，带入约束条件，得到关于未知量的一元二次方程，令$\mathrm{\Delta} \geq 0$解关于k的不等式，根据已知条件确定最大/小值
>
> 六、换元法
>
> 适用于分母较复杂的情况

函数分式型求最值（已知x范围，求含x分式的范围：换成$y = ax + \frac{1}{bx} + c$的形式）

> $1.\frac{1}{x}\text{：图像法}$
>
> $2.\frac{1}{x + a}\text{：换元，令}\ x + a = t\text{，}\ \text{得到}t\text{的范围，图像法}$
>
> $3.\frac{ax + b}{cx + d}$
>
> 1.换元：
>
> $\text{令}cx + d = t\text{，则原式} = \frac{\frac{a}{c}(t - d) + b}{t} = \frac{a}{c} + \frac{\frac{a}{c}d + b}{t}\text{，求}t\text{的范围，图像法}$
>
> 2.配凑：
>
> $\frac{ax + b}{cx + d} = \frac{\frac{a}{c}(cx + d) + \frac{bc - ad}{c}}{cx + d} = \frac{a}{c} + \frac{\frac{bc - ad}{c}}{cx + d} = \frac{a}{c} + \left( \frac{bc - ad}{c} \right)\frac{1}{cx + d}$
>
> $4.\frac{ax^{2} + bx + c}{d}$
>
> $\frac{ax^{2} + bx + c}{d} = \frac{a}{d}x^{2} + \frac{b}{d}x + \frac{c}{d}$
>
> $5.\frac{ax^{2} + bx + c}{dx + e}$
>
> 1.换元
>
> $\text{令}dx + e = t\text{，则原式} = \frac{1}{t}\left( a\left( \frac{t - e}{d} \right)^{2} + b\left( \frac{t - e}{d} \right) + c \right) = \frac{1}{d^{2}}\left( at + \frac{ae^{2} - bde + cd^{2}}{t} + bd - 2ae \right)$
>
> 2.配凑
>
> $\frac{ax^{2} + bx + c}{dx + e} = \frac{m(dx + e)^{2} + n(dx + e) + p}{dx + e} = m(dx + e) + \frac{p}{dx + e} + n$
>
> $6.\frac{dx + e}{ax^{2} + bx + c}$
>
> $\text{原式} = \frac{1}{5}$
>
> $7.\frac{ax^{2} + bx + c}{dx^{2} + ex + f}$
>
> $\text{配凑：原式} = \frac{\frac{a}{d}\left( dx^{2} + ex + f \right) + \left( b - \frac{ae}{d} \right)x + \left( c - \frac{af}{d} \right)}{dx^{2} + ex + f} = \frac{a}{d} + \frac{1}{\frac{dx^{2} + ex + f}{\left( b - \frac{ae}{d} \right)x + \left( c - \frac{af}{d} \right)}}$
>
> 令$m = b - \frac{ae}{d}$，$n = c - \frac{af}{d}$，则有
>
> $\text{原式} = \frac{a}{d} + 1 \div \left\{ \frac{d}{m^{2}}(mx + n) + \frac{1}{mx + n}\left\lbrack c - d\frac{n^{2}}{m^{2}} - \frac{n\left( e - \frac{2dn}{m} \right)}{m} \right\rbrack \right\}$

$\text{也可以求导解决，如}\left( \frac{ax^{2} + bx + c}{dx^{2} + ex + f} \right)' = \frac{(ae - bd)x^{2} + 2(af - cd)x + bf - ce}{\left( dx^{2} + ex + f \right)^{2}}$

二次函数

解析式

<div class="table-scroll">
<table>
<thead>
<tr>
<th rowspan="4">

解析式

</th>
<th colspan="2">

$\text{一般式：}y = ax^{2} + bx + c\ \ (a \neq 0)$

</th>
</tr>
<tr>
<th colspan="2">

$\text{顶点式：}y = a(x - h)^{2} + k\text{，其中}h = - \frac{b}{2a}\text{，}k = \frac{4ac - b^{2}}{4a}$

</th>
</tr>
<tr>
<th colspan="2">

$\text{交点式：}y = a\left( x - x_{1} \right)\left( x - x_{2} \right)$

</th>
</tr>
<tr>
<th colspan="2">

$\text{三点式：}y = \frac{\left( x - x_{2} \right)\left( x - x_{3} \right)}{\left( x_{1} - x_{2} \right)\left( x_{1} - x_{3} \right)} \cdot y_{1} + \frac{\left( x - x_{1} \right)\left( x - x_{3} \right)}{\left( x_{2} - x_{1} \right)\left( x_{2} - x_{3} \right)} \cdot y_{2} + \frac{\left( x - x_{1} \right)\left( x - x_{2} \right)}{\left( x_{3} - x_{1} \right)\left( x_{3} - x_{2} \right)} \cdot y_{3}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

定义域

</td>
<td colspan="2">

$\mathbb{R}$

</td>
</tr>
<tr>
<td>

值域

</td>
<td>

$\left\lbrack \frac{4ac - b^{2}}{4a}\text{，} + \infty \right)\ \ (a > 0)$

</td>
<td>

$\left( - \infty \text{，}\frac{4ac - b^{2}}{4a} \right\rbrack\ \ (a < 0)$

</td>
</tr>
<tr>
<td>

对称轴

</td>
<td colspan="2">

$x = - \frac{b}{2a}$

</td>
</tr>
<tr>
<td>

极值

</td>
<td colspan="2">

$\frac{4ac - b^{2}}{4a}$

</td>
</tr>
<tr>
<td>

图像

</td>
<td>

$a > 0$

</td>
<td>

$a < 0$

</td>
</tr>
</tbody>
</table>
</div>

$a$、$b$、$c$对图像的影响

$a$：$a > 0$，开口向上；$a < 0$，开口向下。$|a|$越大，开口越大；$|a|$越小，开口越小。

$b$：与$a$一起决定对称轴的位置，$ab > 0$，对称轴在y轴左侧；$ab < 0$，对称轴在y轴右侧。

$c$：决定图像与y轴交点的纵坐标。

二次函数的切线

过二次函数凹侧一点不能做切线，过二次函数凸侧一点能做两条切线。

含参一元二次方程

含参一元二次方程/不等式求解

参变分离，因式分解，分类讨论，未知数与变量互换

一元二次方程根的分布

1.两个正根：$\Delta \geq 0\text{，}x_{1} + x_{2} > 0\text{，}x_{1}x_{2} > 0$

2.两个负根：$\Delta \geq 0\text{，}x_{1} + x_{2} < 0\text{，}x_{1}x_{2} > 0$

3.一正一负：$x_{1}x_{2} < 0\text{，}(\Delta > 0)$

4.已知抛物线开口向上

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$x_{1} < x_{2} < m$

</th>
<th>

$m < x_{1} < x_{2}$

</th>
<th>

$x_{1} < m < x_{2}$

</th>
<th>

$m < x_{1} < x_{2} < n$

</th>
<th>

$x_{1} < m < n < x_{2}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$f(m) > 0$

</td>
<td>

$f(m) > 0$

</td>
<td>

$f(m) < 0$

</td>
<td>

$f(m) > 0\ f(n) > 0$

</td>
<td>

$f(m) < 0\ f(n) < 0$

</td>
</tr>
<tr>
<td>

$\Delta > 0$

</td>
<td>

$\Delta > 0$

</td>
<td></td>
<td>

$\Delta > 0$

</td>
<td></td>
</tr>
<tr>
<td>

$- \frac{b}{2a} < m$

</td>
<td>

$- \frac{b}{2a} > m$

</td>
<td></td>
<td>

$m < - \frac{b}{2a} < n$

</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>
