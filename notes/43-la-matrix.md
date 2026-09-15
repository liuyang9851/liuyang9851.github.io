---
title: 矩阵
description: 零矩阵与方阵、对角阵、单位阵、三角阵、矩阵的加减法/数乘/乘法/幂/转置、方阵的行列式、伴随矩阵、逆矩阵、初等变换与初等矩阵、相抵矩阵、行阶梯形矩阵、Cauchy-Binet 公式。
---

# 矩阵

[[toc]]

矩阵

零矩阵

元素全为0的矩阵称为零矩阵，记为O（大写字母O）或Om × n。

方阵

行列数相等的矩阵称为方阵。一般称n阶方阵。

对角（矩）阵

除主对角线外所有元素均为0的方阵。

$${diag}\left\{ a_{11},a_{22},\cdots,a_{nn} \right\} = \mathbf{\Lambda\ }(\text{大写字母}Lambda) = \begin{pmatrix}
a_{11} & 0 & \cdots & 0 \\
0 & a_{22} & \cdots & 0 \\
 \vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & a_{nn}
\end{pmatrix} = \begin{pmatrix}
a_{11} & & & \\
 & a_{22} & & \\
 & & \ddots & \\
 & & & a_{nn}
\end{pmatrix}$$

单位（矩）阵

对角线上元素全为1的对角阵。

$$\mathbf{I}_{n} = \mathbf{E}_{n} = \begin{pmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
 \vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{pmatrix} = \begin{pmatrix}
1 & & & \\
 & 1 & & \\
 & & \ddots & \\
 & & & 1
\end{pmatrix}$$

上（下）三角（矩）阵

$\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
0 & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & a_{nn}
\end{pmatrix}$\text{（上三角阵），}$\begin{pmatrix}
a_{11} & 0 & \cdots & 0 \\
a_{21} & a_{22} & \cdots & 0 \\
 \vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}$（下三角阵）

矩阵的运算

加减法

数乘

乘法

性质1：(AB)C = A(BC)

性质2：A(B + C) = AB + AC，(A + B)C = AC + BC

性质3：c(AB) = (cA)B = A(cB)

幂

对于方阵A，定义

Ak = A ⋅ A ⋅ ⋯ ⋅ A（k个A）

性质1：ArAs = Ar + s

性质2：(Ar)s = Ars

转置

对矩阵A的转置AT或A′就是把它的行转为列，列转为行，类似于沿主对角线翻转。

$$\mathbf{A}_{m \times n} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}\text{，}\mathbf{A}' = \begin{pmatrix}
a_{11} & a_{21} & \cdots & a_{m1} \\
a_{12} & a_{22} & \cdots & a_{m2} \\
 \vdots & \vdots & & \vdots \\
a_{1n} & a_{2n} & \cdots & a_{mn}
\end{pmatrix}$$

性质1：(A′)′ = A

性质2：(A + B)′ = A′ + B′

性质3：(cA)′ = cA′

性质4：(AB)′ = B′A′

性质4：

设C = AB，D = B′A′

方阵的行列式

方阵$\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}$\text{的行列式为：}$\left| \mathbf{A} \right| = \left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right|$

性质1：|A′| = |A|

性质2：|cA| = cn|A|

性质3：|AB| = |A||B| = |BA|

性质1：由行列式的性质8可得。

性质2：由矩阵数乘的定义和行列式的性质3可得。

性质3：见下。

伴随（矩）阵

对n阶方阵A，定义其伴随（矩）阵

$$\mathbf{A}^{*} = \begin{pmatrix}
\mathbf{A}_{11} & \mathbf{A}_{21} & \cdots & \mathbf{A}_{n1} \\
\mathbf{A}_{12} & \mathbf{A}_{22} & \cdots & \mathbf{A}_{n2} \\
 \vdots & \vdots & & \vdots \\
\mathbf{A}_{1n} & \mathbf{A}_{2n} & \cdots & \mathbf{A}_{nn}
\end{pmatrix}$$

其中Aij是|A|的aij对应的代数余子式。

性质1：AA* = A*A = |A| ⋅ In

性质2：|A| = 0的充要条件为|A*| = 0

性质3：|A*| = |A|n − 1

性质4：(AB)* = B*A*

性质1：

$\mathbf{A}\mathbf{A}^{*} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}\begin{pmatrix}
\mathbf{A}_{11} & \mathbf{A}_{21} & \cdots & \mathbf{A}_{n1} \\
\mathbf{A}_{12} & \mathbf{A}_{22} & \cdots & \mathbf{A}_{n2} \\
 \vdots & \vdots & & \vdots \\
\mathbf{A}_{1n} & \mathbf{A}_{2n} & \cdots & \mathbf{A}_{nn}
\end{pmatrix}$，得到的方阵的第(i，j)元素为

ai1Aj1 + ai2Aj2 + ⋯ + ainAjn

由异乘变0定理，当i ≠ j时上式等于0，所以只有主对角线上的元素不为0，并且恰好为|A|，得

$$\mathbf{A}\mathbf{A}^{*} = \begin{pmatrix}
\left| \mathbf{A} \right| & & & \\
 & \left| \mathbf{A} \right| & & \\
 & & \ddots & \\
 & & & \left| \mathbf{A} \right|
\end{pmatrix} = \left| \mathbf{A} \right| \cdot \mathbf{I}_{n}$$

同理$\mathbf{A}^{*}\mathbf{A} = \begin{pmatrix}
\mathbf{A}_{11} & \mathbf{A}_{21} & \cdots & \mathbf{A}_{n1} \\
\mathbf{A}_{12} & \mathbf{A}_{22} & \cdots & \mathbf{A}_{n2} \\
 \vdots & \vdots & & \vdots \\
\mathbf{A}_{1n} & \mathbf{A}_{2n} & \cdots & \mathbf{A}_{nn}
\end{pmatrix}\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}$，得到的方阵的第(i，j)元素为

A1ia1j + A2ia2j + ⋯ + Anianj

由异乘变0定理同理可得。

性质2：

必要性：假设存在A，使得|A| = 0时|A*| ≠ 0，则由逆矩阵的性质1，A*是可逆阵，由A*A = |A| ⋅ In，得A*A = O，对该式用(A*)−1左乘，得

(A*)−1A*A=(A*)−1O ⇒ A = O

由A*的定义，得A* = O，则|A*| = 0，产生了矛盾。

充分性：假设存在A，使得|A*| = 0时|A| ≠ 0，由AA* = A*A = |A| ⋅ In，对方阵求对应行列式，得

|AA*| = |A*A| = ||A| ⋅ In| ⇒ |A||A*| = |A*||A| = |A|n ⋅ |In| = |A|n

由上式，|A*| = 0时整个式子为0，能得出|A|n=0，即|A| = 0，产生了矛盾。

性质3：

由AA* = A*A = |A| ⋅ In，对方阵求对应行列式，得

|AA*| = |A*A| = ||A| ⋅ In| ⇒ |A||A*| = |A*||A| = |A|n ⋅ |In| = |A|n

当|A| = 0时，由性质2，|A*| = 0， |A*| = |A|n − 1成立；当|A| ≠ 0时，对等式两边除以|A|，也得到|A*| = |A|n − 1。

逆（矩）阵

设有n阶方阵A，若存在n阶阶方阵B，使得

AB = BA = In

则称A为可逆（矩）阵、非（奇）异（矩）阵、满秩矩阵或非退化矩阵，称B是A的逆（矩）阵，记为B=A−1，否则称A为奇异（矩）阵。

性质1：一个矩阵若有逆矩阵，则逆矩阵是唯一的。

性质2：若方阵A可逆，则A−1的逆矩阵（即(A−1)−1）为A（(A−1)−1 = A）。

性质3：若方阵A、B可逆，则AB也可逆且(AB)−1 = B−1A−1。

性质4：若方阵A可逆，则cA也可逆且(cA)−1 = c−1A−1。

性质5：方阵A可逆的充要条件为|A| ≠ 0。

$$\text{性质}6\text{：若方阵}\mathbf{A}\text{可逆，则}\mathbf{A}^{- 1} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{*}\text{。}$$

性质7：|A*| = |A|n − 1

性质8：若AB = In，则A、B为同阶方阵且互为逆矩阵。

性质1：

设可逆方阵A满足AB = BA = In和AC = CA = In，则

B = BIn = B(AC)=(BA)C=InC

这说明了逆矩阵的唯一性。

性质2：

因为对于A−1，存在矩阵A，满足A−1A = AA−1 = In，符合逆矩阵的定义。

性质3：

因为对于AB，存在矩阵B−1A−1，有

(AB)(B−1A−1) = A(BB−1)A−1 = AInA−1 = AA−1 = In

且

(B−1A−1)(AB) = B−1(A−1A)B = B−1InB = B−1B = In

满足逆矩阵的定义。所以AB可逆且逆矩阵为B−1A−1

性质4：

因为存在矩阵c−1A−1，满足(cA)(c−1A−1) = (c ⋅ c−1)(AA−1) = In，(c−1A−1)(cA) = (c ⋅ c−1)(A−1A) = In，符合逆矩阵的定义。

性质5：

必要性：由A可逆，得AA−1 = In，对等式两边求方阵的行列式，得

|AA−1| = |A||A−1| = |In| = 1

所以|A| ≠ 0且|A−1| ≠ 0。

充分性：由AA* = A*A = |A| ⋅ In，除以|A|得

$$\mathbf{A} \cdot \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{*} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{*} \cdot \mathbf{A} = \mathbf{I}_{n}$$

满足逆矩阵的定义，所以A是可逆的，且逆矩阵为

$$\mathbf{A}^{- 1} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{*}$$

性质6：

由性质5的证明可得。

性质7：

由AA* = A*A = |A| ⋅ In，对方阵求对应行列式，得

|AA*| = |A*A| = ||A| ⋅ In| ⇒ |A||A*| = |A*||A| = |A|n ⋅ |In| = |A|n

当|A| = 0时，|A*| = 0， |A*| = |A|n − 1成立；当|A| ≠ 0时，对等式两边除以|A|，也得到|A*| = |A|n − 1。

性质8：

对等式求行列式，得

|AB| = |In| ⇒ |A||B| = |In| = 1 ≠ 0

所以|A| ≠ 0且|B| ≠ 0，由性质5，得A，B可逆，且有

A = AIn = A(BB−1)=(AB)B−1=InB−1=B−1

B=InB=(A−1A)B=A−1(AB)=A−1In=A−1

初等变换与初等矩阵

定义矩阵的三类初等行（列）变换如下：

第一类初等变换：对调矩阵中某两行（列）的位置。。

第二类初等变换：用一非0常数c乘以矩阵的某一行（列）

第三类初等变换：将矩阵的某一行（列）乘以常数c后加到另一行（列）上去。

定义三类初等矩阵如下：

第一类初等矩阵：Pij或E(i, j)：将单位阵In的第i行与第j行（第i列与第j列）对换后得到的矩阵。

第二类初等矩阵：Pi(c)或E(i(c))：将常数c乘以单位阵In的第i行（第j列）位置而得到的矩阵。

第三类初等矩阵：Tij(c)或E(ij(k))：将单位阵In的第i行（第j列）乘以c后加到第j行（第i列）上得到的矩阵。

$$\mathbf{P}_{ij} = \mathbf{E}(i,j) = \begin{pmatrix}
1 & & & & & & \\
 & \ddots & & & & & \\
 & & 0 & \cdots & 1 & & \\
 & & \vdots & & \vdots & & \\
 & & 1 & \cdots & 0 & & \\
 & & & & & \ddots & \\
 & & & & & & 1
\end{pmatrix}$$

$$\mathbf{P}_{i}(c) = \mathbf{E}\left( i(c) \right) = \begin{pmatrix}
1 & & & & & & \\
 & \ddots & & & & & \\
 & & 1 & & & & \\
 & & & c & & & \\
 & & & & 1 & & \\
 & & & & & \ddots & \\
 & & & & & & 1
\end{pmatrix}$$

$$\mathbf{T}_{ij}(c) = \mathbf{E}\left( ij(k) \right) = \begin{pmatrix}
1 & & & & & & \\
 & \ddots & & & & & \\
 & & 1 & \cdots & 0 & & \\
 & & \vdots & & \vdots & & \\
 & & c & \cdots & 1 & & \\
 & & & & & \ddots & \\
 & & & & & & 1
\end{pmatrix}$$

相抵矩阵

如果一个矩阵A经过有限次初等行变换后变成矩阵B，则称A和B是行等价的，记为$\mathbf{A}\overset{r}{\sim}\mathbf{B}$。

如果一个矩阵A经过有限次初等列变换后变成矩阵B，则称A和B是列等价的，记为$\mathbf{A}\overset{c}{\sim}\mathbf{B}$。

如果一个矩阵A经过有限次初等变换后变成矩阵B，则称A和B是等价或相抵的，记为A ∼ B。

矩阵A必然可以通过初等变换变为如下矩阵，该矩阵称为矩阵A的相抵标准型。

$\begin{pmatrix}
1 & \cdots & 0 & 0 & \cdots & 0 \\
 \vdots & & \vdots & \vdots & & \vdots \\
0 & \cdots & 1 & 0 & \cdots & 0 \\
0 & \cdots & 0 & 0 & \cdots & 0 \\
 \vdots & & \vdots & \vdots & & \vdots \\
0 & \cdots & 0 & 0 & \cdots & 0
\end{pmatrix}$（也可以是O）

证明：对于矩阵$\mathbf{A =}\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}$ ，如果A ≠ O，可以通过三种初等变换实现。

（行）阶梯形矩阵

设A = (aij)m × n为m × n矩阵，对任意的1 ≤ i ≤ m，定义ki如下：若A的第i行元素全为0，则ki = +∞；若A的第i行元素不全为0，则ki是第i行所有非0元素列指标的最小值。即若ki < +∞，则aiki是A的第i行中从左到右第一个非元素，aiki称为第i行的阶梯点。

若存在0 ≤ r ≤ m，使得k1 < k2 < ⋯ < kr，kr + 1 = ⋯ = km = +∞，则称这样的矩阵A为（行）阶梯形矩阵。即（行）阶梯形矩阵的矩阵阶梯点的列指标随着行数严格递增，或者从图形上看非0元素全体构成一个阶梯。

矩阵A经过若干次初等行变换，可以化为阶梯形矩阵。

证明：类似于高斯消元法。

设A是一个m × n阵，则对A作一次初等行变换后得到的矩阵等于用一个m阶相应的初等矩阵左乘后得到的积。对A作一次初等列变换后得到的矩阵等于用一个n阶相应的初等矩阵右乘后得到的积。（简称为“行左列右”）

证明：

$$\mathbf{P}_{ij}\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
 \vdots & \vdots & & \vdots \\
a_{j1} & a_{j2} & \cdots & a_{jn} \\
 \vdots & \vdots & & \vdots \\
a_{i1} & a_{i2} & & a_{in} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}\text{，}\mathbf{P}_{i}(c)\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
 \vdots & \vdots & & \vdots \\
ca_{i1} & ca_{i2} & & ca_{in} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}\text{，}\mathbf{T}_{ij}(c)\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
 \vdots & \vdots & & \vdots \\
a_{i1} & a_{i2} & \cdots & a_{in} \\
 \vdots & \vdots & & \vdots \\
ca_{i1} + a_{j1} & ca_{i2} + a_{j2} & & ca_{in} + a_{jn} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}$$

分别对应三种初等行变换。

$$\mathbf{P}_{ij}\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
 \vdots & \vdots & & \vdots \\
a_{j1} & a_{j2} & \cdots & a_{jn} \\
 \vdots & \vdots & & \vdots \\
a_{i1} & a_{i2} & & a_{in} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}\text{，}\mathbf{P}_{i}(c)\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
 \vdots & \vdots & & \vdots \\
ca_{i1} & ca_{i2} & & ca_{in} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}\text{，}\mathbf{T}_{ij}(c)\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
 \vdots & \vdots & & \vdots \\
a_{i1} & a_{i2} & \cdots & a_{in} \\
 \vdots & \vdots & & \vdots \\
ca_{i1} + a_{j1} & ca_{i2} + a_{j2} & & ca_{in} + a_{jn} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}$$

分别对应三种初等列变换。

从这里开始行和列就有了差别，这是由矩阵乘法的定义引起的，而更深层次上这与线性方程组是横着书写方程而非竖着书写方程有关。

定理：初等矩阵都是非异阵且其逆矩阵仍是同类初等矩阵，即

$$\mathbf{P}_{ij}^{- 1} = \mathbf{P}_{ij}\text{，}\mathbf{P}_{i}(c)^{- 1} = \mathbf{P}_{i}\left( \frac{1}{c} \right)\text{，}\mathbf{T}_{ij}(c)^{- 1} = \mathbf{T}_{ij}( - c)$$

证明：对于Pij，要寻找矩阵B，满足PijB = BPij = In，由上面的定理，发现若B = Pij，则PijPij相当于对Pij对换第i行与第j行（第i列与第j列），这使得由单位阵In经过对换第i行与第j行（第i列与第j列）而得到的Pij又变回了单位阵In。

对于Pi(c)，发现$\mathbf{P}_{i}(c)\mathbf{P}_{i}\left( \frac{1}{c} \right)$相当于在原单位阵第i行（第j行）乘以$\frac{1}{c}$得到的$\mathbf{P}_{i}\left( \frac{1}{c} \right)$再乘以c还原回单位阵In。$\mathbf{P}_{i}\left( \frac{1}{c} \right)\mathbf{P}_{i}(c)$也类似。

对于Tij(c)，发现Tij(c)Tij(−c)相当于在原单位阵施加第三类初等变化得到Tij(−c)的基础上再施加相反的第三类初等变化还原回单位阵In。Tij(−c)Tij(c)也类似。

定理：非异阵经初等变换后仍为非异阵，奇异阵经初等变换后仍为奇异阵。

证明：由逆矩阵的性质3，可以得到非异阵经初等变换即与可逆的初等矩阵相乘仍可逆。设矩阵A为奇异阵，P为初等矩阵，假设PA为非异阵，则因为A = P−1(PA)，而P−1(PA)由上面的性质得可逆，产生了矛盾。所以PA为奇异阵。

定理：

|Pij| = −1，|Pi(c)| = c，|Tij(c)| = 1

证明：这些分别是由行列式的性质1、4，性质1、3，性质1、7得到。

矩阵的相抵满足如下性质：

（1）A ∼ A

（2）若A ∼ B，则B ∼ A

（3）若A ∼ B，B ∼ C，则A ∼ C

证明：用乘以初等矩阵代替初等变换。

（1）因为I也是初等矩阵，而IA = A，所以A ∼ A。

（2）设PkPk − 1⋯P2P1AQ1Q2⋯Qt − 1Qt = B，其中P，Q均为初等矩阵，则对等式左乘P1−1P2−1⋯Pk − 1−1Pk−1，接着对等式右乘Qt−1Qt − 1−1⋯Q2−1Q1−1，得

A = P1−1P2−1⋯Pk − 1−1Pk−1BQt−1Qt − 1−1⋯Q2−1Q1−1 = A

（3）设PkPk − 1⋯P2P1AQ1Q2⋯Qt − 1Qt = B，Rk′Rk′ − 1⋯R2R1BS1S2⋯St′ − 1St′ = C，其中P，Q，R，S均为初等矩阵，把第二个式子中的B用第一个式子代替，得

Rk′Rk′ − 1⋯R2R1PkPk − 1⋯P2P1AQ1Q2⋯Qt − 1QtS1S2⋯St′ − 1St′ = C

定理：设A是一个n阶可逆阵，则仅用初等行变换或仅用初等列变换即可把化为单位阵In。

证明：类似高斯消元法。

定理：任一n阶非异阵均可表示为有限个初等矩阵的积。

证明：由上面的定理，存在有限个初等矩阵P1，P2，⋯，Pk − 1，Pk，使得对任一n阶非异阵A，有

PkPk − 1⋯P2P1A = In

所以

A = P1−1P2−1⋯Pk − 1−1Pk−1

P1−1，P2−1，⋯Pk − 1−1，Pk−1均为可逆矩阵。

Cauchy-Binet（柯西—毕内）公式

设Am × n，Bn × m，则有

（1）若m > n，则|AB| = 0

（2）若m ≤ n，则

$$\left| \mathbf{AB} \right| = \sum_{1 \leq j_{1} \leq j_{2} \leq \cdots \leq j_{m} \leq n}^{}{\mathbf{A}\begin{pmatrix}
1 & 2 & \cdots & m \\
j_{1} & j_{2} & \cdots & j_{m}
\end{pmatrix}\mathbf{B}\begin{pmatrix}
j_{1} & j_{2} & \cdots & j_{m} \\
1 & 2 & \cdots & m
\end{pmatrix}}$$

推论

设正整数r满足r ≤ m，则

（1）若r > n，则

$$\mathbf{AB}\begin{pmatrix}
i_{1} & i_{2} & \cdots & i_{r} \\
j_{1} & j_{2} & \cdots & j_{r}
\end{pmatrix} = 0$$

（2）若r ≤ n，则

$$\mathbf{AB}\begin{pmatrix}
i_{1} & i_{2} & \cdots & i_{r} \\
j_{1} & j_{2} & \cdots & j_{r}
\end{pmatrix} = \sum_{1 \leq k_{1} \leq k_{2} \leq \cdots \leq k_{r} \leq n}^{}{\mathbf{A}\begin{pmatrix}
i_{1} & i_{2} & \cdots & i_{r} \\
k_{1} & k_{2} & \cdots & k_{r}
\end{pmatrix}\mathbf{B}\begin{pmatrix}
k_{1} & k_{2} & \cdots & k_{r} \\
j_{1} & j_{2} & \cdots & j_{r}
\end{pmatrix}}$$
