---
title: 解析几何
description: 线性空间与向量代数、向量积与混合积、空间平面与直线的各种方程、点线面的位置关系与投影。
---
# 解析几何

[[toc]]

解析几何初步

## 线性空间

设$\mathbb{K}$是一个数域，$\mathbb{K}$是一个集合，在$V$上定义了一个加法"$+$"，即对$V$为中任意两个元素$\mathbf{\alpha}\text{，}\mathbf{\beta}$，总存在$V$中唯一的元素$\mathbf{\gamma}$与之对应，记为$\mathbf{\gamma} = \mathbf{\alpha} + \mathbf{\beta}$。在数域$\mathbb{K}$与之间定义了一种运算，称为数乘，即对$\mathbb{K}$中任一数$k$及$V$中任一元素$\mathbf{\alpha}$，在$V$中总有唯一的元素$\mathbf{\delta}$与之对应，记为$\mathbf{\delta} = k \cdot \mathbf{\alpha =}k\mathbf{\alpha}$。若上述加法及数乘满足下列运算法则：

> （1）加法交换律：

$$
\mathbf{\alpha} + \mathbf{\beta} = \mathbf{\beta} + \mathbf{\alpha}
$$

>
> （2）加法结合律：

$$
\left( \mathbf{\alpha} + \mathbf{\beta} \right) + \mathbf{\gamma} = \mathbf{\alpha} + \left( \mathbf{\beta} + \mathbf{\gamma} \right)
$$

>
> （3）0向量：在中存在一个元素$\mathbf{0}$，对于中任一元素$\mathbf{\alpha}$，都有$\mathbf{\alpha + 0 = \alpha}$，称$\mathbf{0}$为零向量
>
> （4）负向量：对于$V$中每个元素$\mathbf{\alpha}$，存在元素$\mathbf{\beta}$，使$\mathbf{\alpha + \beta = 0}$，并记$\mathbf{\beta = - \alpha}$
>
> （5）：$1 \cdot \mathbf{\alpha} = \mathbf{\alpha}$
>
> （6）左分配律：

$$
k\left( \mathbf{\alpha + \beta} \right) = k\mathbf{\alpha} + k\mathbf{\beta}
$$

>
> （7）右分配律：$(k + l)\mathbf{\alpha =}k\mathbf{\alpha +}l\mathbf{\beta}$
>
> （8）数乘结合律：$k\left( l\mathbf{\alpha} \right) = (kl)\mathbf{\alpha}$

则称$V$为$\mathbb{K}$上的线性空间/向量空间

上面对"向量"定义事实上与所学的平面向量和空间向量相匹配，从这种意义上看，向量的交换律、结合律、分配律实际上是"无需证明"的。

除了定义中给出的法则，线性空间中的向量满足如下性质，这些性质大多数显而易见，但都是需要证明的：

（1）零向量是唯一的

（2）一个向量的负向量是唯一的

（3）加法消去律成立

（4）0与任意向量的数乘为零向量

（5）零向量与任意数的数乘为零向量

（6）$- 1$与任一向量的数乘为该向量的反向量

（7）若$k\mathbf{\alpha} = \mathbf{0}$，则$\mathbf{\alpha} = \mathbf{0}$或$k = 0$

## 向量

通常而言的向量定义为"有序数对"，即

$$\mathbf{x =}\overrightarrow{x} = (x_{1}\text{，}x_{2}\text{，}x_{3}\text{，}\cdots \text{，}x_{n})$$

向量的模：

$$||\ \mathbf{x\ ||} = \left| \mathbf{x} \right| = \sqrt{x_{1}^{2} + x_{2}^{2} + \cdots + x_{n}^{2}}$$

单位向量：

$$\mathbf{x}^{0}\mathbf{=}\mathbf{e}_{\mathbf{x}}\mathbf{=}\frac{\mathbf{x}}{\left| \mathbf{x} \right|}$$

零向量：

$$\mathbf{0} = (0\text{，}0\text{，}0\text{，}\cdots \text{，}0)$$

负向量：

$$- \mathbf{x} = \left( - x_{1}\text{，} - x_{2}\text{，} - x_{3}\text{，}\cdots \text{，} - x_{n} \right)$$

向量的数乘：

$$\lambda\mathbf{x} = \left( \lambda x_{1}\text{，}\lambda x_{2}\text{，}\lambda x_{3}\text{，}\cdots \text{，}\lambda x_{n} \right)$$

共线向量：

对向量$\mathbf{x}$和非零向量$\mathbf{y}$，有且仅有唯一的数$k$，对任意$i \in \mathbb{N}^{+}$且$i \leq n$，满足

$$x_{i} = ky_{i}$$

则称$\mathbf{x}$和$\mathbf{y}$为共线向量。特别地，定义$\mathbf{0}$与任意向量均为共线向量。

数量积（内积）：

$$\mathbf{x \cdot y =}\sum_{i = 1}^{n}{x_{i}y_{i}}$$

由此定义向量的"夹角"$\theta$

$$\cos\theta = \frac{\mathbf{x \cdot y}}{\left| \mathbf{x} \right|\left| \mathbf{y} \right|}$$

对于二维向量（$n = 2$）和三维向量（$n = 3$），$\theta$的几何含义较为明显。

数量积满足如下运算律：

（1）交换律：$\mathbf{x \cdot y = y \cdot x}$

（2）关于数因子的结合律：

$$
\left( \lambda\mathbf{x} \right) \cdot \mathbf{y =}\lambda\left( \mathbf{x \cdot y} \right) = \mathbf{x \cdot}\left( \lambda\mathbf{b} \right)
$$

（3）分配律：

$$
\left( \mathbf{x + y} \right)\mathbf{\cdot z = x \cdot z + y \cdot z}\mathbf{\text{，}}\mathbf{z \cdot}\left( \mathbf{x + y} \right)\mathbf{= z \cdot x + z \cdot y}
$$

对于三维向量，还有如下定义：

向量积（外积）：

$$\mathbf{a \times b =}\left| \begin{matrix}
a_{y} & a_{z} \\
b_{y} & b_{z}
\end{matrix} \right|\mathbf{i -}\left| \begin{matrix}
a_{x} & a_{z} \\
b_{x} & b_{z}
\end{matrix} \right|\mathbf{j +}\left| \begin{matrix}
a_{y} & a_{z} \\
b_{y} & b_{z}
\end{matrix} \right|\mathbf{k =}\left| \begin{matrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
a_{x} & a_{y} & a_{z} \\
b_{x} & b_{y} & b_{z}
\end{matrix} \right|$$

其中

$$
\mathbf{i =}(1\text{，}0\text{，}0)\text{，}\mathbf{j} = (0\text{，}1\text{，}0)\text{，}\mathbf{k} = (0\text{，}0\text{，}1)
$$

向量积的模满足

$$\left| \mathbf{a \times b} \right| = \left| \mathbf{a} \right|\left| \mathbf{b} \right|\sin\theta \text{，其中}\theta \text{是}\mathbf{a}\text{和}\mathbf{b}\text{的夹角}$$

向量积满足如下运算律：

（1）反交换律：$\mathbf{a \times b = - b \times a}$

（2）关于数因子的结合律：

$$
\lambda\left( \mathbf{a \times b} \right) = \left( \lambda\mathbf{a} \right) \times \mathbf{b} = \mathbf{a \times}\left( \lambda\mathbf{b} \right)
$$

（3）分配律：

$$
\left( \mathbf{a + b} \right) \times \mathbf{c = a \times c + b \times c}\mathbf{\text{，}}\mathbf{a \times}\left( \mathbf{b + c} \right)\mathbf{= a \times b + a \times c}
$$

向量积有如下性质：

（1）Lagrange（拉格朗日）恒等式：

$$
\left( \mathbf{a \times b} \right)\mathbf{\cdot}\left( \mathbf{c \times d} \right)\mathbf{=}\left| \begin{matrix}
\mathbf{a \cdot c} & \mathbf{a \cdot d} \\
\mathbf{b \cdot c} & \mathbf{b \cdot d}
\end{matrix} \right|
$$

（2）Jacobi（雅可比）恒等式：

$$
\left( \mathbf{a \times b} \right)\mathbf{\times c +}\left( \mathbf{b \times c} \right)\mathbf{\times a +}\left( \mathbf{c \times a} \right)\mathbf{\times b = 0}
$$

混合积：

$$\left\lbrack \mathbf{abc} \right\rbrack = \left( \mathbf{abc} \right) = \left| \begin{matrix}
a_{x} & a_{y} & a_{z} \\
b_{x} & b_{y} & b_{z} \\
c_{x} & c_{y} & c_{z}
\end{matrix} \right|$$

混合积满足如下性质：

（1）

$$
\left\lbrack \mathbf{abc} \right\rbrack = \left\lbrack \mathbf{bca} \right\rbrack\mathbf{=}\left\lbrack \mathbf{cab} \right\rbrack\mathbf{= -}\left\lbrack \mathbf{bac} \right\rbrack\mathbf{= -}\left\lbrack \mathbf{cba} \right\rbrack\mathbf{= -}\left\lbrack \mathbf{acb} \right\rbrack
$$

（2）

$$
\left\lbrack \mathbf{abc} \right\rbrack\mathbf{=}\left( \mathbf{a \times b} \right)\mathbf{\cdot c = a \cdot}\left( \mathbf{b \times c} \right)
$$

### 双重向量积

$$\left( \mathbf{a} \times \mathbf{b} \right) \times \mathbf{c} = \left| \begin{matrix}
i & j & k \\
\left| \begin{matrix}
y_{a} & z_{a} \\
y_{b} & z_{b}
\end{matrix} \right| & \left| \begin{matrix}
x_{a} & z_{a} \\
x_{b} & z_{b}
\end{matrix} \right| & \left| \begin{matrix}
x_{a} & y_{a} \\
x_{b} & y_{b}
\end{matrix} \right| \\
x_{c} & y_{c} & z_{c}
\end{matrix} \right|$$

双重向量积有如下性质：

（1）

$$
\left( \mathbf{a} \times \mathbf{b} \right) \times \mathbf{c =}\left( \mathbf{a \cdot c} \right)\mathbf{b - (b \cdot c)a}
$$

### 第一类三重外积

$$\mathbf{a \times}\left\lbrack \mathbf{b \times}\left( \mathbf{c \times d} \right) \right\rbrack\mathbf{=}\left( \mathbf{b \cdot d} \right)\left( \mathbf{a \times c} \right)\mathbf{-}\left( \mathbf{b \cdot c} \right)\left( \mathbf{a \times d} \right)$$

### 第二类三重外积

$$\left( \mathbf{a \times b} \right)\mathbf{\times}\left( \mathbf{c \times d} \right)\mathbf{=}\left\lbrack \mathbf{abd} \right\rbrack\mathbf{c -}\left\lbrack \mathbf{abc} \right\rbrack\mathbf{d =}\left\lbrack \mathbf{acd} \right\rbrack\mathbf{b -}\left\lbrack \mathbf{bcd} \right\rbrack\mathbf{a}$$

## 空间直角坐标系下的平面与直线

### 平面方程

#### 平面的点法式方程

设平面的法向量为$\mathbf{n =}(A\text{，}B\text{，}C)$（$A\text{、}B\text{、}C$不全为$0$），平面上有一点$P(x_{0}\text{，}y_{0}\text{，}z_{0})$，则平面上任意一点$(x\text{，}y\text{，}z)$与$P$相连形成的向量$\left( x - x_{0}\text{，}y - y_{0}\text{，}z - z_{0} \right)$与法向量$\mathbf{n}$垂直，即内积为0：

$$A\left( x - x_{0} \right) + B\left( y - y_{0} \right) + C\left( z - z_{0} \right) = 0$$

#### 平面的一般式方程

把平面的点法式方程整理，得

$$Ax + By + Cz - \left( Ax_{0} + By_{0} + Cz_{0} \right) = 0$$

令$D = - \left( Ax_{0} + By_{0} + Cz_{0} \right)$，即得

$$Ax + By + Cz + D = 0$$

$|A|$越大，平面与$yOz$平面的夹角越小，$B$、$C$同理。$D$增大，平面向其法向量方向的反方向移动，$D$减小则相反，移动的距离与$D$的变化量成正比。

#### 平面的截距式方程

设$A\text{，}B\text{，}C\text{，}D \neq 0$，对一般式方程整理得

$$\frac{x}{- \frac{D}{A}} + \frac{y}{- \frac{D}{B}} + \frac{z}{- \frac{D}{C}} = 1$$

表明平面与三个坐标轴的交点坐标分别为

$$
\left( - \frac{D}{A},0,0 \right),\ \left( 0, - \frac{D}{B},0 \right),\ \left( 0,0, - \frac{D}{C} \right)
$$

，所以截距式方程为

$$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$$

#### 平面的法线式方程

对一般式乘$\frac{1}{\sqrt{A^{2} + B^{2} + C^{2}}}$（法式化因子），得

$$\frac{A}{\sqrt{A^{2} + B^{2} + C^{2}}}x + \frac{B}{\sqrt{A^{2} + B^{2} + C^{2}}}y + \frac{C}{\sqrt{A^{2} + B^{2} + C^{2}}}z = - \frac{D}{\sqrt{A^{2} + B^{2} + C^{2}}}$$

因为法向量$\mathbf{n}$的方向余弦与方程的系数对应，平面到原点的距离为自由量的绝对值，所以有

$$\cos\alpha x + \cos\beta y + \cos\gamma z = p$$

其中$|p|$为平面到原点的距离。对于截距式方程，有

$$
\frac{1}{a^{2}} + \frac{1}{b^{2}} + \frac{1}{c^{2}} = \frac{1}{p^{2}}
$$

#### 平面的三点式方程

对平面上任意三点$A\text{、}B\text{、}C$，选择向量$\overrightarrow{BA}\text{和}\overrightarrow{CA}$获取法向量，由点法式方程得

$$\left| \begin{matrix}
y_{b} - y_{a} & z_{b} - z_{a} \\
y_{c} - y_{a} & z_{c} - z_{a}
\end{matrix} \right|\left( x - x_{a} \right) - \left| \begin{matrix}
x_{b} - x_{a} & z_{b} - z_{a} \\
x_{c} - x_{a} & z_{c} - z_{a}
\end{matrix} \right|\left( y - y_{a} \right) + \left| \begin{matrix}
x_{b} - x_{a} & y_{b} - y_{a} \\
x_{c} - x_{a} & y_{c} - y_{a}
\end{matrix} \right|\left( z - z_{a} \right) = 0$$

逆用行列式展开和行列式的性质，得

$$\left| \begin{matrix}
x - x_{a} & y - y_{a} & z - z_{a} \\
x_{b} - x_{a} & y_{b} - y_{a} & z_{b} - z_{a} \\
x_{c} - x_{a} & y_{c} - y_{a} & z_{c} - z_{a}
\end{matrix} \right| = 0$$

利用行列式的性质和逆用行列式展开，得

$$
\left| \begin{matrix}
x & y & z \\
x_{b} & y_{b} & z_{b} \\
x_{c} & y_{c} & z_{c}
\end{matrix} \right| - \left| \begin{matrix}
x & y & z \\
x_{b} & y_{b} & z_{b} \\
x_{a} & y_{a} & z_{a}
\end{matrix} \right| - \left| \begin{matrix}
x & y & z \\
x_{a} & y_{a} & z_{a} \\
x_{c} & y_{c} & z_{c}
\end{matrix} \right| - \left| \begin{matrix}
x_{a} & y_{a} & z_{a} \\
x_{b} & y_{b} & z_{b} \\
x_{c} & y_{c} & z_{c}
\end{matrix} \right| = 0
$$

或

$$\left| \begin{matrix}
1 & x & y & z \\
1 & x_{a} & y_{a} & z_{a} \\
1 & x_{b} & y_{b} & z_{b} \\
1 & x_{c} & y_{c} & z_{c}
\end{matrix} \right| = 0$$

平面的参数方程（点位式方程）

已知平面内一点$P$和两个线性无关的向量$\mathbf{\alpha}\text{，}\mathbf{\beta}$，则平面内任意一点$M(x\text{，}y\text{，}z)$与P相连形成的

向量可以由$\mathbf{\alpha}\text{，}\mathbf{\beta}$线性表示，即

$$
\overrightarrow{PM} = \lambda\mathbf{\alpha} + \mu\mathbf{\beta}
$$

（向量式参数方程）

对应分量相等，得

$$
\left\{ \begin{array}{r}
x = x_{0} + \lambda x_{a} + \mu x_{a} \\
y = y_{0} + \lambda y_{a} + \mu y_{b} \\
z = z_{0} + \lambda z_{a} + \mu y_{b}
\end{array} \right.\
$$

（坐标式参数方程）

对向量式参数方程两边同点乘$(\mathbf{\alpha} \times \mathbf{\beta})$，因为垂直的两向量的内积为0，所以得

$$\left\lbrack \overrightarrow{PM}\text{，}\mathbf{\alpha}\text{，}\mathbf{\beta} \right\rbrack = 0$$

由坐标式参数方程和行列式的性质，容易验证：

$$\left| \begin{matrix}
x - x_{0} & y - y_{0} & z - z_{0} \\
x_{a} & y_{a} & z_{a} \\
x_{b} & y_{b} & z_{b}
\end{matrix} \right| = 0$$

若把它展开为一般式方程，则有

$$
A = \left| \begin{matrix}
y_{a} & z_{a} \\
y_{b} & z_{b}
\end{matrix} \right|，B = - \left| \begin{matrix}
x_{a} & z_{a} \\
x_{b} & z_{b}
\end{matrix} \right|，C = \left| \begin{matrix}
x_{a} & y_{a} \\
x_{b} & y_{b}
\end{matrix} \right|，D = - \left| \begin{matrix}
x_{0} & y_{0} & z_{0} \\
x_{a} & y_{a} & z_{a} \\
x_{b} & y_{b} & z_{b}
\end{matrix} \right|
$$

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

平面方程类型

</th>
<th>

方程

</th>
<th>

与一般式转化

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

点法式

</td>
<td>

A(x − x0) + B(y − y0) + C(z − z0) = 0

</td>
<td>

D = −Ax0 − By0 − Cz0

</td>
</tr>
<tr>
<td>

一般式

</td>
<td>

Ax + By + Cz + D = 0

</td>
<td></td>
</tr>
<tr>
<td>

截距式

</td>
<td>

$$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$$

</td>
<td>

$$A = \frac{1}{a}\text{，}B = \frac{1}{b}\text{，}C = \frac{1}{c}\text{，}D - 1$$

</td>
</tr>
<tr>
<td>

法线式

</td>
<td>

cos αx + cos βy + cos γz = p

</td>
<td>

A = cos α，B = cos β，C = cos γ，D = −p

</td>
</tr>
<tr>
<td>

三点式

</td>
<td>

$$\left| \begin{matrix}
1 & x & y & z \\
1 & x_{a} & y_{a} & z_{a} \\
1 & x_{b} & y_{b} & z_{b} \\
1 & x_{c} & y_{c} & z_{c}
\end{matrix} \right| = 0$$

</td>
<td>

$$A = - \left| \begin{matrix}
1 & y_{a} & z_{a} \\
1 & y_{b} & z_{b} \\
1 & y_{c} & z_{c}
\end{matrix} \right|\text{，}B = \left| \begin{matrix}
1 & x_{a} & z_{a} \\
1 & x_{b} & z_{b} \\
1 & x_{c} & z_{c}
\end{matrix} \right|\text{，}$$

$$C = \left| \begin{matrix}
1 & x_{a} & y_{a} \\
1 & x_{b} & y_{b} \\
1 & x_{c} & y_{c}
\end{matrix} \right|\text{，}D = \left| \begin{matrix}
x_{a} & y_{a} & z_{a} \\
x_{b} & y_{b} & z_{b} \\
x_{c} & y_{c} & z_{c}
\end{matrix} \right|$$

</td>
</tr>
<tr>
<td>

参数方程

</td>
<td>

$$\left\{ \begin{array}{r}
x = x_{0} + \lambda x_{a} + \mu x_{a} \\
y = y_{0} + \lambda y_{a} + \mu y_{b} \\
z = z_{0} + \lambda z_{a} + \mu y_{b}
\end{array} \right.\ $$

</td>
<td>

$$A = \left| \begin{matrix}
y_{a} & z_{a} \\
y_{b} & z_{b}
\end{matrix} \right|\text{，}B = - \left| \begin{matrix}
x_{a} & z_{a} \\
x_{b} & z_{b}
\end{matrix} \right|\text{，}$$

$$C = \left| \begin{matrix}
x_{a} & y_{a} \\
x_{b} & y_{b}
\end{matrix} \right|\text{，}D = - \left| \begin{matrix}
x_{0} & y_{0} & z_{0} \\
x_{a} & y_{a} & z_{a} \\
x_{b} & y_{b} & z_{b}
\end{matrix} \right|$$

</td>
</tr>
</tbody>
</table>
</div>

### 直线方程

直线的对称式方程（点向式方程，标准式方程）

设过点$\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)$直线$l$的方向向量为$(m\text{，}n\text{，}p)$，则对于直线上的任意一点$(x\text{，}y\text{，}z)$，满足

$$\frac{x - x_{0}}{m} = \frac{y - y_{0}}{n} = \frac{z - z_{0}}{p}\ \ (m\text{，}n\text{，}p \neq 0)$$

#### 直线的参数方程

>

$$\text{令}\frac{x - x_{0}}{m} = \frac{y - y_{0}}{n} = \frac{z - z_{0}}{p} = t\text{，得}$$

$$\left\{ \begin{array}{r}
x = x_{0} + mt \\
y = y_{0} + nt \\
z = z_{0} + pt
\end{array} \right.\ $$

上面的$m\text{，}n\text{，}p$可以用方向余弦$\cos\alpha \text{，}\cos\beta \text{，}\cos\gamma$代替，且有$\cos^{2}\alpha + \cos^{2}\beta + \cos^{2}\gamma = 1$。

#### 直线的两点式方程

把对称式中的方向向量$(m\text{，}n\text{，}p)$替换为直线上两点形成的向量$(x_{2} - x_{1}\text{，}y_{2} - y_{1}\text{，}z_{2} - z_{1})$，得

$$\frac{x - x_{1}}{x_{2} - x_{1}} = \frac{y - y_{1}}{y_{2} - y_{1}} = \frac{z - z_{1}}{z_{2} - z_{1}}$$

#### 直线的一般方程

直线可以看作由两个平面

$$\left\{ \begin{array}{r}
A_{1}x + B_{1}y + C_{1}z + D_{1} = 0 \\
A_{2}x + B_{2}y + C_{2}z + D_{2} = 0
\end{array} \right.\ $$

相交形成，这两平面有且仅有一条交线的充要条件为$\mathbf{n}_{\mathbf{1}}$和$\mathbf{n}_{\mathbf{2}}$线性无关。

>

$$\text{直线的方向向量为}\left| \begin{matrix}
> \mathbf{i} & \mathbf{j} & \mathbf{k} \\
> A_{1} & B_{1} & C_{1} \\
> A_{2} & B_{2} & C_{2}
> \end{matrix} \right|\text{，对应的对称式为}\frac{x - x_{0}}{\left| \begin{matrix}
> B_{1} & C_{1} \\
> B_{2} & C_{2}
> \end{matrix} \right|} = \frac{y - y_{0}}{\left| \begin{matrix}
> C_{1} & A_{1} \\
> C_{2} & A_{2}
> \end{matrix} \right|} = \frac{z - z_{0}}{\left| \begin{matrix}
> A_{1} & B_{1} \\
> A_{2} & B_{2}
> \end{matrix} \right|}$$

直线方程类型                                                                                               方程
对称式

$$\frac{x - x_{0}}{m} = \frac{y - y_{0}}{n} = \frac{z - z_{0}}{p}$$

参数方程

$$\left\{ \begin{array}{r}
x = x_{0} + mt \\
y = y_{0} + nt \\
z = z_{0} + pt
\end{array} \right.\ $$

两点式

$$\frac{x - x_{1}}{x_{2} - x_{1}} = \frac{y - y_{1}}{y_{2} - y_{1}} = \frac{z - z_{1}}{z_{2} - z_{1}}$$

一般式

$$\left\{ \begin{array}{r}
A_{1}x + B_{1}y + C_{1}z + D_{1} = 0 \\
A_{2}x + B_{2}y + C_{2}z + D_{2} = 0
\end{array} \right.\ $$

### 平面束

>

$$\text{以直线}\left\{ \begin{array}{r}
> A_{1}x + B_{1}y + C_{1}z + D_{1} = 0 \\
> A_{2}x + B_{2}y + C_{2}z + D_{2} = 0
> \end{array} \right.\ \text{为轴的有轴平面束的方程为}$$

$$\lambda\left( A_{1}x + B_{1}y + C_{1}z + D_{1} \right) + \mu\left( A_{2}x + B_{2}y + C_{2}z + D_{2} \right) = 0$$

其中$\lambda \text{，}\mu$不全为0。

与平面$Ax + By + Cz + D = 0$平行的平面束为

$$Ax + By + Cz + \lambda = 0$$

## 点、直线和平面的一些性质

### 点到平面的距离

设平面$Ax + By + Cz + D = 0$外一点$P\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)$与平面上一点$M(a\text{，}b\text{，}c)$构成向量$\overrightarrow{MP}$，由向量的数量积，得

$$\left| \frac{\overrightarrow{MP} \cdot \mathbf{n}}{\left| \mathbf{n} \right|} \right| = \left| \overrightarrow{MP} \right|\left| \cos\theta \right| = d$$

$$d = \frac{\left| \left( x_{0} - a \right)A + \left( y_{0} - b \right)B + \left( z_{0} - c \right)C \right|}{\sqrt{A^{2} + B^{2} + C^{2}}} = \frac{\left| Ax_{0} + By_{0} + Cz_{0} - (Aa + Bb + Cc) \right|}{\sqrt{A^{2} + B^{2} + C^{2}}}$$

因为点$M$在平面$Ax + By + Cz + D = 0$上，所以$Aa + Bb + Cc + D = 0$，替换得

$$d = \frac{\left| Ax_{0} + By_{0} + Cz_{0} + D \right|}{\sqrt{A^{2} + B^{2} + C^{2}}}$$

### 平面分割空间

类似于直线$Ax + By + C = 0$分割平面，不等式$Ax + By + Cz + D > 0$表示法向量指向的空间区域，不等式$Ax + By + Cz + D < 0$则相反。

### 两平面的位置关系

平行：$\mathbf{n}_{1} \times \mathbf{n}_{2} = 0$（法向量成比例（共线/线性相关））且$D_{1} \neq D_{1}$（不重合）

重合：$\mathbf{n}_{1} \times \mathbf{n}_{2} = 0$且$D_{1} = D_{1}$

垂直：$\mathbf{n}_{1} \cdot \mathbf{n}_{2} = 0$（法向量垂直）

>

$$\text{两平面的夹角}\theta \text{满足}\cos\theta = \frac{\left| \mathbf{n}_{1} \cdot \mathbf{n}_{2} \right|}{\left| \mathbf{n}_{1} \right|\left| \mathbf{n}_{2} \right|} = \frac{\left| A_{1}A_{2} + B_{1}B_{2} + C_{1}C_{2} \right|}{\sqrt{A_{1}^{2} + B_{1}^{2} + C_{1}^{2}} \cdot \sqrt{A_{2}^{2} + B_{2}^{2} + C_{2}^{2}}}$$

### 直线与平面的位置关系

相交：$Am + Bn + Cp \neq 0$（法向量与方向向量不垂直）

平行且直线不在面内：$Am + Bn + Cp \neq 0$且$Ax_{0} + By_{0} + Cz_{0} + D \neq 0$

直线在平面内：$Am + Bn + Cp \neq 0$且$Ax_{0} + By_{0} + Cz_{0} + D = 0$

垂直：$\mathbf{n}$与$\mathbf{l}$线性相关

>

$$\text{直线与平面的夹角}\varphi \text{满足}\sin\varphi = \frac{\left| \mathbf{n \cdot l} \right|}{\left| \mathbf{n} \right|\left| \mathbf{l} \right|} = \frac{|Am + Bn + Cp|}{\sqrt{A^{2} + B^{2} + C^{2}} \cdot \sqrt{m^{2} + n^{2} + p^{2}}}$$

### 直线与点的位置关系

类似于点到平面的距离，设直线$l$，直线外点$P$，直线上点$M$，则有

$$
\left| \mathbf{l} \times \overrightarrow{MP} \right| = d\left| \mathbf{l} \right|
$$

，得

$$d = \frac{\left| \mathbf{l} \times \overrightarrow{MP} \right|}{\left| \mathbf{l} \right|} = \frac{\left| (m\text{，}n\text{，}p) \times \left( x_{0} - a\text{，}y_{0} - b\text{，}z_{0} - c \right) \right|}{\sqrt{m^{2} + n^{2} + p^{2}}}$$

### 两直线的位置关系

异面：

$$
\Delta = \left| \begin{matrix}
x_{1} - x_{2} & y_{1} - y_{2} & z_{1} - z_{2} \\
m_{1} & n_{1} & p_{1} \\
m_{2} & n_{2} & p_{2}
\end{matrix} \right| \neq 0
$$

相交：$\Delta = 0$且$m_{1}\ :n_{1}\ :p_{1}\  \neq m_{2}\ :n_{2}\ :p_{2}$（$\mathbf{l}_{1}$和$\mathbf{l}_{2}$线性无关）

平行：

$$
m_{1}\ :n_{1}\ :p_{1} = m_{2}\ :n_{2}\ :p_{2} \neq \left( x_{1} - x_{2} \right)\ :\left( y_{1} - y_{2} \right)\ :\left( z_{1} - z_{2} \right)
$$

重合：

$$
m_{1}\ :n_{1}\ :p_{1} = m_{2}\ :n_{2}\ :p_{2} = \left( x_{1} - x_{2} \right)\ :\left( y_{1} - y_{2} \right)\ :\left( z_{1} - z_{2} \right)
$$

垂直：$m_{1}m_{2} + n_{1}n_{2} + p_{1}p_{2} = 0$

>

$$\text{两直线的夹角}\theta \text{满足}\cos\theta = \frac{\left| m_{1}m_{2} + n_{1}n_{2} + p_{1}p_{2} \right|}{\sqrt{m_{1}^{2} + n_{1}^{2} + p_{1}^{2}}\sqrt{m_{2}^{2} + n_{2}^{2} + p_{2}^{2}}}$$

异面直线的距离：设点$M_{1}\text{，}M_{2}$分别在直线$l_{1}$，$l_{2}$上，则有

$$d = \frac{\left| \overrightarrow{M_{1}M_{2}} \cdot \left( \mathbf{l}_{1} \times \mathbf{l}_{2} \right) \right|}{\left| \mathbf{l}_{1}\mathbf{l}_{2} \right|} = \frac{\left| \left\lbrack \overrightarrow{M_{1}M_{2}}\mathbf{l}_{1}\mathbf{l}_{2} \right\rbrack \right|}{\left| \mathbf{l}_{1}\mathbf{l}_{2} \right|} = \frac{\left| \left| \begin{matrix}
x_{1} - x_{2} & y_{1} - y_{2} & z_{1} - z_{2} \\
m_{1} & n_{1} & p_{1} \\
m_{2} & n_{2} & p_{2}
\end{matrix} \right| \right|}{\sqrt{\left| \begin{matrix}
n_{1} & p_{1} \\
n_{2} & p_{2}
\end{matrix} \right|^{2} + \left| \begin{matrix}
m_{1} & p_{1} \\
m_{2} & p_{2}
\end{matrix} \right|^{2} + \left| \begin{matrix}
m_{1} & n_{1} \\
m_{2} & n_{2}
\end{matrix} \right|^{2}}}$$

>

$$\text{其中}\mathbf{l}_{1} \times \mathbf{l}_{2}\text{为这两条直线的公垂线的方向向量，}\frac{\left| \overrightarrow{M_{1}M_{2}} \cdot \left( \mathbf{l}_{1} \times \mathbf{l}_{2} \right) \right|}{\left| \mathbf{l}_{1}\mathbf{l}_{2} \right|}\text{为}\overrightarrow{M_{1}M_{2}}\text{在该公垂线上的投影。}$$

共面：

$$
\left| \begin{matrix}
A_{1} & B_{1} & C_{1} & D_{1} \\
A_{2} & B_{2} & C_{2} & D_{2} \\
A_{3} & B_{3} & C_{3} & D_{3} \\
A_{4} & B_{4} & C_{4} & D_{4}
\end{matrix} \right| = 0
$$

### 点到直线的投影

### 点到平面的投影

### 直线到平面的投影

直线

$$\left\{ \begin{array}{r}
A_{1}x + B_{1}y + C_{1}z + D_{1} = 0 \\
A_{2}x + B_{2}y + C_{2}z + D_{2} = 0
\end{array} \right.\ $$

到平面

$$A_{0}x + B_{0}y + C_{0}z + D_{0} = 0$$

的投影直线为

$$\left\{ \begin{array}{r}
A_{0}x + B_{0}y + C_{0}z + D_{0} = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\lambda\left( A_{1}x + B_{1}y + C_{1}z + D_{1} \right) + \mu\left( A_{2}x + B_{2}y + C_{2}z + D_{2} \right) = 0
\end{array} \right.\ $$

其中

$$\lambda\mathbf{n}_{0}\mathbf{n}_{1} + \mu\mathbf{n}_{0}\mathbf{n}_{2} = 0$$

空间曲线的切线和法平面

空间曲线

$$\left\{ \begin{array}{r}
x = \varphi(t) \\
y = \psi(t) \\
z = \omega(t)
\end{array} \right.\ $$

在点$\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)$的切线为

的切线为

$$\frac{x - x_{0}}{\varphi'\left( t_{0} \right)} = \frac{y - y_{0}}{\psi'\left( t_{0} \right)} = \frac{z - z_{0}}{\omega'\left( t_{0} \right)}$$

法平面为

$$\varphi'\left( t_{0} \right)\left( x - x_{0} \right) + \psi'\left( t_{0} \right)\left( y - y_{0} \right) + \omega'\left( t_{0} \right)\left( z - z_{0} \right) = 0$$

曲面的切平面和法线

曲面

$$F(x\text{，}y\text{，}z) = 0$$

在点$\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)$的切平面为

$$F_{x}'\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)\left( x - x_{0} \right) + F_{y}'\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)\left( y - y_{0} \right) + F_{z}'\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)\left( z - z_{0} \right) = 0$$

法线为

$$\frac{x - x_{0}}{F_{x}'\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)} = \frac{y - y_{0}}{F_{y}'\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)} = \frac{z - z_{0}}{F_{z}'\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)}$$

二次曲线

$$Ax^{2} + 2Bxy + Cy^{2} + 2Dx + 2Ey + F = 0$$

$$a_{11}x^{2} + 2a_{12}xy + a_{22}y^{2} + 2a_{13}x + 2a_{23}y + a_{33} = 0$$

定义

$$F(x\text{，}y) \equiv a_{11}x^{2} + 2a_{12}xy + a_{22}y^{2} + 2a_{13}x + 2a_{23}y + a_{33} = 0$$

$$F_{1}(x\text{，}y) \equiv a_{11}x + a_{12}y + a_{13}$$

$$F_{2}(x\text{，}y) \equiv a_{12}x + a_{22}y + a_{23}$$

$$F_{3}(x\text{，}y) \equiv a_{13}x + a_{23}y + a_{33}$$

$$\Phi(x\text{，}y) \equiv a_{11}x^{2} + 2a_{12}xy + a_{22}y^{2}$$

$$\begin{pmatrix}
F_{1}(x\text{，}y) & F_{2}(x\text{，}y) & F_{3}(x\text{，}y)
\end{pmatrix} \equiv \begin{pmatrix}
x & y & 1
\end{pmatrix}\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{12} & a_{22} & a_{23} \\
a_{13} & a_{23} & a_{33}
\end{pmatrix}$$

$$F(x\text{，}y) \equiv \begin{pmatrix}
F_{1}(x\text{，}y) & F_{2}(x\text{，}y) & F_{3}(x\text{，}y)
\end{pmatrix}\begin{pmatrix}
x \\
y \\
1
\end{pmatrix}$$

$$\Phi(x\text{，}y) \equiv \begin{pmatrix}
x & y
\end{pmatrix}\begin{pmatrix}
a_{11} & a_{12} \\
a_{12} & a_{22}
\end{pmatrix}\begin{pmatrix}
x \\
y
\end{pmatrix}$$

$$I_{1} = a_{11} + a_{22}\text{，}I_{2} = \left| \begin{matrix}
a_{11} & a_{12} \\
a_{12} & a_{22}
\end{matrix} \right|\text{，}I_{3} = \left| \begin{matrix}
a_{11} & a_{12} & a_{13} \\
a_{12} & a_{22} & a_{23} \\
a_{13} & a_{23} & a_{33}
\end{matrix} \right|\text{，}K = M_{22} + M_{11}$$
