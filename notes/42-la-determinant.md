---
title: 行列式
description: 一阶到 n 阶行列式的定义、余子式与代数余子式、全排列与逆序数、对换、行列式的性质、Laplace 定理及其推论、特殊行列式。
---

# 行列式

[[toc]]

行列式

一阶行列式

|a11| = a11

从这里开始，行列式的符号与绝对值的符号发生了冲突，在线性代数中，绝对值的符号改为$\left\| \begin{matrix}

\end{matrix} \right\|$\text{，如}$\left\| \begin{matrix}
 - 1
\end{matrix} \right\| = 1$。

二阶行列式

$\left| \begin{matrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{matrix} \right| = a_{11}a_{22} - a_{12}a_{21}$ \text{，}$\left| \begin{matrix}
爱 & 辈 \\
子 & 你
\end{matrix} \right| = 爱你一辈子$

二阶行列式的定义在小学的“新定义/新运算”中已经见过。

三阶行列式

$$\left| \begin{matrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{matrix} \right| = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33} - a_{13}a_{22}a_{31}$$

三阶行列式的计算有一个特有的“对角线法则”：

三阶行列式被三条曲线贯穿，每条曲线贯穿三个数，把这三个数相乘，取正号，得到：a11a22a33 + a12a23a31 + a13a21a32

同样被三条曲线贯穿，每条曲线贯穿三个数，把这三个数相乘，取负号，得到：−a11a23a32 − a12a21a33 − a13a22a31

两式相加，得a11a22a33 + a12a23a31 + a13a21a32 − a11a23a32 − a12a21a33 − a13a22a31

n阶行列式

$$D = \det\left( a_{ij} \right) = \left| \mathbf{A} \right| = \det\mathbf{A} = \left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right|$$

n阶行列式为n2个数组成的数表。每个n阶行列式都有其对应的值，n阶行列式也是一个数。

对于其中任意一个元素aij，i指出aij位于第i行，j指出aij位于第j列。

余子式和代数余子式

余子式：

选定行列式中的某个数字，以它为中心画横竖两线，删去线上的所有数字后剩下的数按原相对位置组成的行列式称为余子式。

n阶行列式$\left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right|$的元素aij对应的余子式Mij为

$$M_{ij} = \left| \begin{matrix}
a_{11} & \cdots & a_{i,j - 1} & a_{i,j + 1} & \cdots & a_{1n} \\
 \vdots & & \vdots & \vdots & & \vdots \\
a_{i - 1,i} & \cdots & a_{i - 1,\ j - 1} & a_{i - 1,j + 1} & \cdots & a_{i - 1,n} \\
a_{i + 1,1} & \cdots & a_{i + 1,j - 1} & a_{i + 1,j + 1} & \cdots & a_{i + 1,n} \\
 \vdots & & \vdots & \vdots & & \vdots \\
a_{n1} & \cdots & a_{n,j - 1} & a_{n,j + 1} & \cdots & a_{nn}
\end{matrix} \right|$$

$eg.\left| \begin{matrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{matrix} \right|$\text{中}a11\text{的余子式为}$\left| \begin{matrix}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{matrix} \right|$\text{，}a22\text{的余子式为}$\left| \begin{matrix}
a_{11} & a_{13} \\
a_{31} & a_{33}
\end{matrix} \right|$

代数余子式

对余子式赋正负号后变为代数余子式。确定符号的方法为定义余子式时选定的数的横纵“坐标”之和的奇偶性，奇为负号，偶为正号。

n阶行列式的元素aij对应的代数余子式Aij为

$$A_{ij} = ( - 1)^{i + j}\left| \begin{matrix}
a_{11} & \cdots & a_{i,j - 1} & a_{i,j + 1} & \cdots & a_{1n} \\
 \vdots & & \vdots & \vdots & & \vdots \\
a_{i - 1,i} & \cdots & a_{i - 1,\ j - 1} & a_{i - 1,j + 1} & \cdots & a_{i - 1,n} \\
a_{i + 1,1} & \cdots & a_{i + 1,j - 1} & a_{i + 1,j + 1} & \cdots & a_{i + 1,n} \\
 \vdots & & \vdots & \vdots & & \vdots \\
a_{n1} & \cdots & a_{n,j - 1} & a_{n,j + 1} & \cdots & a_{nn}
\end{matrix} \right|$$

$eg.\left| \begin{matrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{matrix} \right|$\text{中}a11\text{的代数余子式为}$+ \left| \begin{matrix}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{matrix} \right|$，因为a11，1 + 1 = 2为偶数，对应正号

a12的代数余子式为$- \left| \begin{matrix}
a_{21} & a_{23} \\
a_{31} & a_{33}
\end{matrix} \right|$，因为a12，1 + 2 = 3为奇数，对应负号

行列式的定义

行列式的定义常见的是用逆序数来将行列式直接表示成可以计算的代数式，这里给出用行列式按第一列列展开的归纳法定义。

n阶行列式可以定义为行列式按第一列分解为第一列的n个元素与其对应代数余子式乘积之和（行列式按第一列展开），即

$$\left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right| = a_{11}A_{11} + a_{21}A_{21} + \cdots + a_{n1}A_{n1} = \sum_{i = 1}^{n}{a_{i1}A_{i1}}$$

展开写作

$$D = a_{11}\left| \begin{matrix}
a_{21} & a_{22} & \cdots & a_{2n} \\
a_{31} & a_{32} & \cdots & a_{3n} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right| - a_{21}\left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{31} & a_{32} & \cdots & a_{3n} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right| + \cdots$$

$$+ ( - 1)^{i + 1}a_{i1}\left| \begin{matrix}
a_{11} & \cdots & a_{i,j - 1} & a_{i,j + 1} & \cdots & a_{1n} \\
 \vdots & & \vdots & \vdots & & \vdots \\
a_{i - 1,i} & \cdots & a_{i - 1,\ j - 1} & a_{i - 1,j + 1} & \cdots & a_{i - 1,n} \\
a_{i + 1,1} & \cdots & a_{i + 1,j - 1} & a_{i + 1,j + 1} & \cdots & a_{i + 1,n} \\
 \vdots & & \vdots & \vdots & & \vdots \\
a_{n1} & \cdots & a_{n,j - 1} & a_{n,j + 1} & \cdots & a_{nn}
\end{matrix} \right| + \cdots + ( - 1)^{n + 1}a_{n1}\left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{n - 1,1} & a_{n - 1,2} & \cdots & a_{n - 1,n}
\end{matrix} \right|$$

一阶行列式和二阶行列式已经在上面定义，三阶行列式也满足上面的行列式按第一列展开。

$${\left| \begin{matrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{matrix} \right| = a_{11}\left| \begin{matrix}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{matrix} \right| - a_{12}\left| \begin{matrix}
a_{21} & a_{23} \\
a_{31} & a_{33}
\end{matrix} \right| + a_{13}\left| \begin{matrix}
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{matrix} \right|(\text\{按第一行展开\})
}{= a_{11}\left| \begin{matrix}
a_{22} & a_{23} \\
a_{32} & a_{33}
\end{matrix} \right| - a_{21}\left| \begin{matrix}
a_{12} & a_{13} \\
a_{32} & a_{33}
\end{matrix} \right| + a_{31}\left| \begin{matrix}
a_{12} & a_{13} \\
a_{22} & a_{23}
\end{matrix} \right|(\text{按第一列展开})}$$

$$\left| \begin{matrix}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34} \\
a_{41} & a_{42} & a_{43} & a_{44}
\end{matrix} \right| = - a_{12}\left| \begin{matrix}
a_{21} & a_{23} & a_{24} \\
a_{31} & a_{33} & a_{34} \\
a_{41} & a_{43} & a_{44}
\end{matrix} \right| + a_{22}\left| \begin{matrix}
a_{11} & a_{13} & a_{14} \\
a_{31} & a_{33} & a_{34} \\
a_{41} & a_{43} & a_{44}
\end{matrix} \right| - a_{32}\left| \begin{matrix}
a_{11} & a_{13} & a_{14} \\
a_{21} & a_{23} & a_{24} \\
a_{41} & a_{43} & a_{44}
\end{matrix} \right| + a_{42}\left| \begin{matrix}
a_{11} & a_{13} & a_{14} \\
a_{21} & a_{23} & a_{24} \\
a_{31} & a_{33} & a_{34}
\end{matrix} \right|(\text{按第二行展开})$$

全排列与对换

排列与逆序数

把n个不同的元素排成一排，叫做这n个元素的（全）排列

排列的种数为Pn = n!（也就是Ann）

在这些排列中，先选定一个称之为“标准次序”，则剩下的排列中，每有一对元素的先后顺序与标准次序不同时，则它构成1个逆序，一个排列中所有逆序数的总和称为这个排列的逆序数t。

逆序数为奇数的排列称为奇排列，逆序数为偶数的排列称为偶排列。在n个元素的全排列中，奇排列和偶排列各占$\frac{n!}{2}$个。

为了计算某个排列的逆序数，可以从左到右依次对元素比较在本在它后面的元素在它前面的数量ti，把这些数量累加就得到了排列的逆序数。

eg.求排列为32514的逆序数（一般规定自然数排列中以从小到大为标准次序）

$$t_{1} = 0\text{，}t_{2} = 1\text{，}t_{3} = 0\text{，}t_{4} = 3\text{，}t_{5} = 1\text{，}t = \sum_{i = 1}^{n}t_{i} = 0 + 1 + 0 + 3 + 1 = 5\text{逆序数为}5$$

对换

把一个排列中的任意两个元素交换位置称为对换，把相邻两个元素交换位置称为相邻对换。

一个排列中任意两个元素对换，排列改变奇偶性。

证明：为了考虑任意位置元素的对换，考虑到任意元素的对换可以由若干次相邻对换组成，故先考虑相邻对换。

若在某次相邻对换中把ab对换成ba，则当a > b时（a本应在b后时），a元素的逆序数不变，b元素的逆序数减1；当a < b时（a本应在b前时），a元素的逆序数加1，b元素的逆序数不变。综合两种情况，得到经相邻变换后改变奇偶性。

若在某次对换中把ab对换成ba，且a与b之间有n个数（即由⋯a, x1, x2, ⋯, xn, bn⋯对换为⋯b, x1x2, ⋯, xn, a⋯）则可把该对换分解为先把a与靠右的相邻元素对换n + 1次使得a在最右边而其余元素相对位置不变（⋯x1, x2, ⋯, xn, bn, an⋯），再把b与靠左的相邻元素对换n次使得b在最左边而其余元素相对位置不变（⋯bn, x1, x2, ⋯, xn, an⋯），总共进行了2n + 1次相邻对换，由前，排列的奇偶性改变。

奇排列对换成标准排列的对换次数为奇数，偶排列对换成标准排列的对换次数为偶数。（根据奇排列与偶排列的定义以及上述定理）

行列式的性质

性质1：上（下）三角行列式的值等于其主对角线上元素之积。

性质2：若行列式的某一行（列）元素全为0，则行列式的值等于0。

性质3：用某个常数c乘以行列式的某一行（列），所得行列式的值等于原行列式值的c倍。

性质4：对换行列式的两行（列），行列式的值改变符号。

性质5：若行列式的某两行（列）成比例，则行列式的值等于0。

性质6：若行列式的某一行（列）元素aij = bij + cij，则该行列式可以分解为两个行列式之和，其中一个行列式的相应行（列）的元素为bij，另一个行列式的相应行（列）的元素为cij。

性质7：将行列式的某一行（列）乘以常数c加到另一行（列）上去，行列式的值不变。

性质8：行列式转置后的值不变。

性质1：$\left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
 & a_{22} & \cdots & a_{2n} \\
 & & \ddots & \vdots \\
0 & & & a_{nn}
\end{matrix} \right| = \left| \begin{matrix}
a_{11} & & & 0 \\
a_{21} & a_{22} & & \\
 \vdots & \vdots & \ddots & \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right| = a_{11}a_{22}\cdots a_{nn} = \sum_{k = 1}^{n}a_{kk}$

性质2：$\left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
 \vdots & & & \vdots \\
a_{i - 1,1} & a_{i - 1,2} & \cdots & a_{i - 1,n} \\
0 & 0 & \cdots & 0 \\
a_{i + 1,1} & a_{i + 1,2} & \cdots & a_{i + 1,n} \\
 \vdots & & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right| = \left| \begin{matrix}
a_{11} & \cdots & a_{1,j - 1} & 0 & a_{1,j + 1} & \cdots & a_{1n} \\
a_{21} & \cdots & a_{2,j - 1} & 0 & a_{2,j + 1} & \cdots & a_{2n} \\
 \vdots & & \vdots & \vdots & \vdots & & \vdots \\
a_{n1} & \cdots & a_{n,j - 1} & 0 & a_{n,j + 1} & \cdots & a_{nn}
\end{matrix} \right| = 0$

性质3：$\left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
 \vdots & \vdots & & \vdots \\
b_{i1} + c_{i1} & b_{i2} + c_{i2} & \cdots & b_{in} + c_{in} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right| = \left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
 \vdots & \vdots & & \vdots \\
b_{i1} & b_{i2} & \cdots & b_{in} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right| + \left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
 \vdots & \vdots & & \vdots \\
c_{i1} & c_{i2} & \cdots & c_{in} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right|$

性质4：在此处键入公式。

异乘变0定理：行列式某一行（列）的元素与另一行（列）的对应元素的代数余子式乘积之和等于0。

$$\left\{ \begin{array}{r}
a_{i1} + A_{j1} + a_{i2} + A_{j2} + \cdots + a_{in} + A_{jn} = D\text{，}i = j \\
a_{1i} + A_{1j} + a_{2i} + A_{2j} + \cdots + a_{ni} + A_{nj} = 0\text{，}i \neq j
\end{array} \right.\ $$

$$\sum_{k = 1}^{n}{a_{ki}A_{kj}} = \left\{ \begin{array}{r}
D\text\{，当\}i = j \\
0\text\{，当\}i \neq j
\end{array} \right.\ \ \text\{或\}\ \sum_{k = 1}^{n}{a_{ik}A_{jk}} = \left\{ \begin{array}{r}
D\text\{，当\}i = j \\
0\text\{，当\}i \neq j
\end{array} \right.\ $$

特殊行列式

Laplace（拉普拉斯）定理及其推论

k阶子式

设A是m行n列的矩阵，k < m且k < n，有两组自然数i1，i2，⋯，ik和j1，j2，⋯，jn满足

1 ≤ i1 < i2 < ⋯ < jk ≤ n，1 ≤ j1 < j2 < ⋯ < jk ≤ n

取中第i1行，第i2行，……，第jk行以及第j1列，第j2列，……，第jk列交点上的元素，按原来中的相对位置构成一个行列式，成为矩阵A或行列式|A|（若m = n）的一个k阶子式，记为

$$\mathbf{A}\begin{pmatrix}
i_{1} & i_{2} & \cdots & i_{n} \\
j_{1} & j_{2} & \cdots & j_{n}
\end{pmatrix}$$

即

$$\left| \begin{matrix}
a_{j_{1}j_{1}} & a_{i_{1}j_{2}} & \cdots & a_{i_{1}j_{k}} \\
a_{i_{2}j_{1}} & a_{i_{2}j_{2}} & \cdots & a_{i_{2}j_{k}} \\
 \vdots & \vdots & & \vdots \\
a_{i_{k}j_{1}} & a_{i_{k}j_{2}} & \cdots & a_{i_{k}j_{k}}
\end{matrix} \right|$$

k阶子式的余子式和代数余子式

余子式：对行列式|A|，在|A|中去掉i1行，第i2行，……，第jk行以及第j1列，第j2列，……，第jk列以后剩下的元素按原来的相对位置构成一个阶行列式，称为子式的余子式，记为

$$M\begin{pmatrix}
i_{1} & i_{2} & \cdots & i_{n} \\
j_{1} & j_{2} & \cdots & j_{n}
\end{pmatrix}$$

代数余子式：若令p = i1 + i2 + ⋯ + ik，q = j1 + j2 + ⋯ + jk，则称

$$\widehat{\mathbf{A}}\begin{pmatrix}
i_{1} & i_{2} & \cdots & i_{n} \\
j_{1} & j_{2} & \cdots & j_{n}
\end{pmatrix} = ( - 1)^{p + q}M\begin{pmatrix}
i_{1} & i_{2} & \cdots & i_{n} \\
j_{1} & j_{2} & \cdots & j_{n}
\end{pmatrix}$$

为子式的代数余子式。

Laplace（拉普拉斯）定理

$$\left| \mathbf{A} \right| = \sum_{1 \leq i_{1} \leq i_{2} \leq \cdots \leq i_{k} \leq n}^{}{\mathbf{A}\begin{pmatrix}
i_{1} & i_{2} & \cdots & i_{n} \\
j_{1} & j_{2} & \cdots & j_{n}
\end{pmatrix}\widehat{\mathbf{A}}\begin{pmatrix}
i_{1} & i_{2} & \cdots & i_{n} \\
j_{1} & j_{2} & \cdots & j_{n}
\end{pmatrix}}$$

$$\left| \mathbf{A} \right| = \sum_{1 \leq j_{1} \leq j_{2} \leq \cdots \leq j_{k} \leq n}^{}{\mathbf{A}\begin{pmatrix}
i_{1} & i_{2} & \cdots & i_{n} \\
j_{1} & j_{2} & \cdots & j_{n}
\end{pmatrix}\widehat{\mathbf{A}}\begin{pmatrix}
i_{1} & i_{2} & \cdots & i_{n} \\
j_{1} & j_{2} & \cdots & j_{n}
\end{pmatrix}}$$

推论

$$\left| \begin{matrix}
a_{11} & \cdots & a_{1k} & 0 & \cdots & 0 \\
 \vdots & & \vdots & \vdots & & \vdots \\
a_{k1} & \cdots & a_{kk} & 0 & \cdots & 0 \\
a_{k + 1,1} & \cdots & a_{k + 1,k} & a_{k + 1,k + 1} & \cdots & a_{k + 1,n} \\
 \vdots & & \vdots & \vdots & & \vdots \\
a_{n1} & \cdots & a_{nk} & a_{n,k + 1} & \cdots & a_{nn}
\end{matrix} \right| = \left| \begin{matrix}
a_{11} & \cdots & a_{1k} \\
 \vdots & & \vdots \\
a_{k1} & \cdots & a_{kk}
\end{matrix} \right|\left| \begin{matrix}
a_{k + 1,k + 1} & \cdots & a_{k + 1,n} \\
 \vdots & & \vdots \\
a_{n,k + 1} & \cdots & a_{nn}
\end{matrix} \right|$$
