---
title: "线性代数初步"
hs_seq: "B11"
description: "线性代数初步：从这里开始，行列式的符号与绝对值的符号发生了冲突，在线性代数中，绝对值的符号改为，如。"
---

# 线性代数初步

行列式

一阶行列式

$\left| a_{11} \right| = a_{11}$

从这里开始，行列式的符号与绝对值的符号发生了冲突，在线性代数中，绝对值的符号改为$\left\| \begin{matrix} \end{matrix} \right\|$，如$\left\| \begin{matrix} - 1 \end{matrix} \right\| = 1$。

二阶行列式

$\left| \begin{matrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{matrix} \right| = a_{11}a_{22} - a_{12}a_{21}$ ，$\left| \begin{matrix} \text{爱} & \text{辈} \\ \text{子} & \text{你} \end{matrix} \right| = \text{爱你一辈子}$

二阶行列式的定义在小学的“新定义/新运算”中已经见过。

三阶行列式

$\left| \begin{matrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{matrix} \right| = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33} - a_{13}a_{22}a_{31}$

三阶行列式的计算有一个特有的“对角线法则”：

三阶行列式被三条曲线贯穿，每条曲线贯穿三个数，把这三个数相乘，取正号，得到：$a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32}$

同样被三条曲线贯穿，每条曲线贯穿三个数，把这三个数相乘，取负号，得到：$- a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33} - a_{13}a_{22}a_{31}$

两式相加，得$a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33} - a_{13}a_{22}a_{31}$

n阶行列式

$D = \det\left( a_{ij} \right) = \left| \mathbf{A} \right| = \det\mathbf{A} = \left| \begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix} \right|$

> n阶行列式为$n^{2}$个数组成的数表。每个n阶行列式都有其对应的值，n阶行列式也是一个数。

对于其中任意一个元素$a_{ij}$，$i$指出$a_{ij}$位于第$i$行，$j$指出$a_{ij}$位于第$j$列。

余子式和代数余子式

余子式：

选定行列式中的某个数字，以它为中心画横竖两线，删去线上的所有数字后剩下的数按原相对位置组成的行列式称为余子式。

> n阶行列式$\left| \begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix} \right|$的元素$a_{ij}$对应的余子式$M_{ij}$为

$M_{ij} = \left| \begin{matrix} a_{11} & \cdots & a_{i,j - 1} & a_{i,j + 1} & \cdots & a_{1n} \\ \vdots & & \vdots & \vdots & & \vdots \\ a_{i - 1,i} & \cdots & a_{i - 1,\ j - 1} & a_{i - 1,j + 1} & \cdots & a_{i - 1,n} \\ a_{i + 1,1} & \cdots & a_{i + 1,j - 1} & a_{i + 1,j + 1} & \cdots & a_{i + 1,n} \\ \vdots & & \vdots & \vdots & & \vdots \\ a_{n1} & \cdots & a_{n,j - 1} & a_{n,j + 1} & \cdots & a_{nn} \end{matrix} \right|$

> $eg.\left| \begin{matrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{matrix} \right|$中$a_{11}$的余子式为$\left| \begin{matrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{matrix} \right|$，$a_{22}$的余子式为$\left| \begin{matrix} a_{11} & a_{13} \\ a_{31} & a_{33} \end{matrix} \right|$

代数余子式

对余子式赋正负号后变为代数余子式。确定符号的方法为定义余子式时选定的数的横纵“坐标”之和的奇偶性，奇为负号，偶为正号。

n阶行列式的元素$a_{ij}$对应的代数余子式$A_{ij}$为

$A_{ij} = ( - 1)^{i + j}\left| \begin{matrix} a_{11} & \cdots & a_{i,j - 1} & a_{i,j + 1} & \cdots & a_{1n} \\ \vdots & & \vdots & \vdots & & \vdots \\ a_{i - 1,i} & \cdots & a_{i - 1,\ j - 1} & a_{i - 1,j + 1} & \cdots & a_{i - 1,n} \\ a_{i + 1,1} & \cdots & a_{i + 1,j - 1} & a_{i + 1,j + 1} & \cdots & a_{i + 1,n} \\ \vdots & & \vdots & \vdots & & \vdots \\ a_{n1} & \cdots & a_{n,j - 1} & a_{n,j + 1} & \cdots & a_{nn} \end{matrix} \right|$

> $eg.\left| \begin{matrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{matrix} \right|$中$a_{11}$的代数余子式为$+ \left| \begin{matrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{matrix} \right|$，因为$a_{11}$，$1 + 1 = 2$为偶数，对应正号
>
> $a_{12}$的代数余子式为$- \left| \begin{matrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{matrix} \right|$，因为$a_{12}$，$1 + 2 = 3$为奇数，对应负号

行列式的定义

行列式的定义常见的是用逆序数来将行列式直接表示成可以计算的代数式，这里给出用行列式按第一列列展开的归纳法定义。

n阶行列式可以定义为行列式按第一列分解为第一列的n个元素与其对应代数余子式乘积之和（行列式按第一列展开），即

$\left| \begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix} \right| = a_{11}A_{11} + a_{21}A_{21} + \cdots + a_{n1}A_{n1} = \sum_{i = 1}^{n}{a_{i1}A_{i1}}$

展开写作

$D = a_{11}\left| \begin{matrix} a_{21} & a_{22} & \cdots & a_{2n} \\ a_{31} & a_{32} & \cdots & a_{3n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix} \right| - a_{21}\left| \begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{31} & a_{32} & \cdots & a_{3n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix} \right| + \cdots$

$+ ( - 1)^{i + 1}a_{i1}\left| \begin{matrix} a_{11} & \cdots & a_{i,j - 1} & a_{i,j + 1} & \cdots & a_{1n} \\ \vdots & & \vdots & \vdots & & \vdots \\ a_{i - 1,i} & \cdots & a_{i - 1,\ j - 1} & a_{i - 1,j + 1} & \cdots & a_{i - 1,n} \\ a_{i + 1,1} & \cdots & a_{i + 1,j - 1} & a_{i + 1,j + 1} & \cdots & a_{i + 1,n} \\ \vdots & & \vdots & \vdots & & \vdots \\ a_{n1} & \cdots & a_{n,j - 1} & a_{n,j + 1} & \cdots & a_{nn} \end{matrix} \right| + \cdots + ( - 1)^{n + 1}a_{n1}\left| \begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n - 1,1} & a_{n - 1,2} & \cdots & a_{n - 1,n} \end{matrix} \right|$

一阶行列式和二阶行列式已经在上面定义，三阶行列式也满足上面的行列式按第一列展开。

${\left| \begin{matrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{matrix} \right| = a_{11}\left| \begin{matrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{matrix} \right| - a_{12}\left| \begin{matrix} a_{21} & a_{23} \\ a_{31} & a_{33} \end{matrix} \right| + a_{13}\left| \begin{matrix} a_{21} & a_{22} \\ a_{31} & a_{32} \end{matrix} \right|(\text{按第一行展开}) }{= a_{11}\left| \begin{matrix} a_{22} & a_{23} \\ a_{32} & a_{33} \end{matrix} \right| - a_{21}\left| \begin{matrix} a_{12} & a_{13} \\ a_{32} & a_{33} \end{matrix} \right| + a_{31}\left| \begin{matrix} a_{12} & a_{13} \\ a_{22} & a_{23} \end{matrix} \right|(\text{按第一列展开})}$

$\left| \begin{matrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{matrix} \right| = - a_{12}\left| \begin{matrix} a_{21} & a_{23} & a_{24} \\ a_{31} & a_{33} & a_{34} \\ a_{41} & a_{43} & a_{44} \end{matrix} \right| + a_{22}\left| \begin{matrix} a_{11} & a_{13} & a_{14} \\ a_{31} & a_{33} & a_{34} \\ a_{41} & a_{43} & a_{44} \end{matrix} \right| - a_{32}\left| \begin{matrix} a_{11} & a_{13} & a_{14} \\ a_{21} & a_{23} & a_{24} \\ a_{41} & a_{43} & a_{44} \end{matrix} \right| + a_{42}\left| \begin{matrix} a_{11} & a_{13} & a_{14} \\ a_{21} & a_{23} & a_{24} \\ a_{31} & a_{33} & a_{34} \end{matrix} \right|(\text{按第二行展开})$

全排列与对换

排列与逆序数

把n个不同的元素排成一排，叫做这n个元素的（全）排列

排列的种数为$P_{n} = n!$（也就是$A_{n}^{n}$）

在这些排列中，先选定一个称之为“标准次序”，则剩下的排列中，每有一对元素的先后顺序与标准次序不同时，则它构成1个逆序，一个排列中所有逆序数的总和称为这个排列的逆序数$t$。

逆序数为奇数的排列称为奇排列，逆序数为偶数的排列称为偶排列。在n个元素的全排列中，奇排列和偶排列各占$\frac{n!}{2}$个。

为了计算某个排列的逆序数，可以从左到右依次对元素比较在本在它后面的元素在它前面的数量$t_{i}$，把这些数量累加就得到了排列的逆序数。

$eg.\text{求排列为}32514\text{的逆序数}$（一般规定自然数排列中以从小到大为标准次序）

> $t_{1} = 0\text{，}t_{2} = 1\text{，}t_{3} = 0\text{，}t_{4} = 3\text{，}t_{5} = 1\text{，}t = \sum_{i = 1}^{n}t_{i} = 0 + 1 + 0 + 3 + 1 = 5\text{逆序数为}5$

对换

把一个排列中的任意两个元素交换位置称为对换，把相邻两个元素交换位置称为相邻对换。

一个排列中任意两个元素对换，排列改变奇偶性。

证明：为了考虑任意位置元素的对换，考虑到任意元素的对换可以由若干次相邻对换组成，故先考虑相邻对换。

若在某次相邻对换中把$ab$对换成$ba$，则当$a > b$时（$a$本应在$b$后时），$a$元素的逆序数不变，b元素的逆序数减1；当$a < b$时（$a$本应在$b$前时），$a$元素的逆序数加1，b元素的逆序数不变。综合两种情况，得到经相邻变换后改变奇偶性。

若在某次对换中把$ab$对换成$ba$，且$a$与$b$之间有$n$个数（即由$\cdots a,x_{1},x_{2},\cdots,x_{n},b_{n}\cdots \text{对换为}\cdots b,x_{1}x_{2},\cdots,x_{n},a\cdots$）则可把该对换分解为先把a与靠右的相邻元素对换$n + 1$次使得a在最右边而其余元素相对位置不变（$\cdots x_{1},x_{2},\cdots,x_{n},b_{n},a_{n}\cdots$），再把b与靠左的相邻元素对换$n$次使得b在最左边而其余元素相对位置不变（$\cdots b_{n},x_{1},x_{2},\cdots,x_{n},a_{n}\cdots$），总共进行了$2n + 1$次相邻对换，由前，排列的奇偶性改变。

奇排列对换成标准排列的对换次数为奇数，偶排列对换成标准排列的对换次数为偶数。（根据奇排列与偶排列的定义以及上述定理）

行列式的性质

性质1：上（下）三角行列式的值等于其主对角线上元素之积。

性质2：若行列式的某一行（列）元素全为$0$，则行列式的值等于$0$。

性质3：用某个常数$c$乘以行列式的某一行（列），所得行列式的值等于原行列式值的$c$倍。

性质4：对换行列式的两行（列），行列式的值改变符号。

性质5：若行列式的某两行（列）成比例，则行列式的值等于$0$。

性质6：若行列式的某一行（列）元素$a_{ij} = b_{ij} + c_{ij}$，则该行列式可以分解为两个行列式之和，其中一个行列式的相应行（列）的元素为$b_{ij}$，另一个行列式的相应行（列）的元素为$c_{ij}$。

性质7：将行列式的某一行（列）乘以常数$c$加到另一行（列）上去，行列式的值不变。

性质8：行列式转置后的值不变。

性质1：$\left| \begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ & a_{22} & \cdots & a_{2n} \\ & & \ddots & \vdots \\ 0 & & & a_{nn} \end{matrix} \right| = \left| \begin{matrix} a_{11} & & & 0 \\ a_{21} & a_{22} & & \\ \vdots & \vdots & \ddots & \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix} \right| = a_{11}a_{22}\cdots a_{nn} = \sum_{k = 1}^{n}a_{kk}$

性质2：$\left| \begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & & & \vdots \\ a_{i - 1,1} & a_{i - 1,2} & \cdots & a_{i - 1,n} \\ 0 & 0 & \cdots & 0 \\ a_{i + 1,1} & a_{i + 1,2} & \cdots & a_{i + 1,n} \\ \vdots & & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix} \right| = \left| \begin{matrix} a_{11} & \cdots & a_{1,j - 1} & 0 & a_{1,j + 1} & \cdots & a_{1n} \\ a_{21} & \cdots & a_{2,j - 1} & 0 & a_{2,j + 1} & \cdots & a_{2n} \\ \vdots & & \vdots & \vdots & \vdots & & \vdots \\ a_{n1} & \cdots & a_{n,j - 1} & 0 & a_{n,j + 1} & \cdots & a_{nn} \end{matrix} \right| = 0$

性质3：$\left| \begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & & \vdots \\ b_{i1} + c_{i1} & b_{i2} + c_{i2} & \cdots & b_{in} + c_{in} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix} \right| = \left| \begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & & \vdots \\ b_{i1} & b_{i2} & \cdots & b_{in} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix} \right| + \left| \begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & & \vdots \\ c_{i1} & c_{i2} & \cdots & c_{in} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix} \right|$

性质4：在此处键入公式。

异乘变0定理：行列式某一行（列）的元素与另一行（列）的对应元素的代数余子式乘积之和等于0。

$\left\{ \begin{array}{r} a_{i1} + A_{j1} + a_{i2} + A_{j2} + \cdots + a_{in} + A_{jn} = D\text{，}i = j \\ a_{1i} + A_{1j} + a_{2i} + A_{2j} + \cdots + a_{ni} + A_{nj} = 0\text{，}i \neq j \end{array} \right.\$

$\sum_{k = 1}^{n}{a_{ki}A_{kj}} = \left\{ \begin{array}{r} D\text{，当}i = j \\ 0\text{，当}i \neq j \end{array} \right.\ \ \text{或}\ \sum_{k = 1}^{n}{a_{ik}A_{jk}} = \left\{ \begin{array}{r} D\text{，当}i = j \\ 0\text{，当}i \neq j \end{array} \right.\$

特殊行列式

Laplace（拉普拉斯）定理及其推论

$k$阶子式

设$\mathbf{A}$是$m$行$n$列的矩阵，$k < m$且$k < n$，有两组自然数$i_{1}\text{，}i_{2}\text{，}\cdots \text{，}i_{k}$和$j_{1}\text{，}j_{2}\text{，}\cdots \text{，}j_{n}$满足

$1 \leq i_{1} < i_{2} < \cdots < j_{k} \leq n\text{，}1 \leq j_{1} < j_{2} < \cdots < j_{k} \leq n$

取中第$i_{1}$行，第$i_{2}$行，……，第$j_{k}$行以及第$j_{1}$列，第$j_{2}$列，……，第$j_{k}$列交点上的元素，按原来中的相对位置构成一个行列式，成为矩阵$\mathbf{A}$或行列式$\left| \mathbf{A} \right|$（$\text{若}m = n$）的一个$k$阶子式，记为

$\mathbf{A}\begin{pmatrix} i_{1} & i_{2} & \cdots & i_{n} \\ j_{1} & j_{2} & \cdots & j_{n} \end{pmatrix}$

即

$\left| \begin{matrix} a_{j_{1}j_{1}} & a_{i_{1}j_{2}} & \cdots & a_{i_{1}j_{k}} \\ a_{i_{2}j_{1}} & a_{i_{2}j_{2}} & \cdots & a_{i_{2}j_{k}} \\ \vdots & \vdots & & \vdots \\ a_{i_{k}j_{1}} & a_{i_{k}j_{2}} & \cdots & a_{i_{k}j_{k}} \end{matrix} \right|$

$k$阶子式的余子式和代数余子式

余子式：对行列式$\left| \mathbf{A} \right|$，在$\left| \mathbf{A} \right|$中去掉$i_{1}$行，第$i_{2}$行，……，第$j_{k}$行以及第$j_{1}$列，第$j_{2}$列，……，第$j_{k}$列以后剩下的元素按原来的相对位置构成一个阶行列式，称为子式的余子式，记为

$M\begin{pmatrix} i_{1} & i_{2} & \cdots & i_{n} \\ j_{1} & j_{2} & \cdots & j_{n} \end{pmatrix}$

代数余子式：若令$p = i_{1} + i_{2} + \cdots + i_{k}\text{，}q = j_{1} + j_{2} + \cdots + j_{k}$，则称

$\widehat{\mathbf{A}}\begin{pmatrix} i_{1} & i_{2} & \cdots & i_{n} \\ j_{1} & j_{2} & \cdots & j_{n} \end{pmatrix} = ( - 1)^{p + q}M\begin{pmatrix} i_{1} & i_{2} & \cdots & i_{n} \\ j_{1} & j_{2} & \cdots & j_{n} \end{pmatrix}$

为子式的代数余子式。

Laplace（拉普拉斯）定理

$\left| \mathbf{A} \right| = \sum_{1 \leq i_{1} \leq i_{2} \leq \cdots \leq i_{k} \leq n}^{}{\mathbf{A}\begin{pmatrix} i_{1} & i_{2} & \cdots & i_{n} \\ j_{1} & j_{2} & \cdots & j_{n} \end{pmatrix}\widehat{\mathbf{A}}\begin{pmatrix} i_{1} & i_{2} & \cdots & i_{n} \\ j_{1} & j_{2} & \cdots & j_{n} \end{pmatrix}}$

$\left| \mathbf{A} \right| = \sum_{1 \leq j_{1} \leq j_{2} \leq \cdots \leq j_{k} \leq n}^{}{\mathbf{A}\begin{pmatrix} i_{1} & i_{2} & \cdots & i_{n} \\ j_{1} & j_{2} & \cdots & j_{n} \end{pmatrix}\widehat{\mathbf{A}}\begin{pmatrix} i_{1} & i_{2} & \cdots & i_{n} \\ j_{1} & j_{2} & \cdots & j_{n} \end{pmatrix}}$

推论

$\left| \begin{matrix} a_{11} & \cdots & a_{1k} & 0 & \cdots & 0 \\ \vdots & & \vdots & \vdots & & \vdots \\ a_{k1} & \cdots & a_{kk} & 0 & \cdots & 0 \\ a_{k + 1,1} & \cdots & a_{k + 1,k} & a_{k + 1,k + 1} & \cdots & a_{k + 1,n} \\ \vdots & & \vdots & \vdots & & \vdots \\ a_{n1} & \cdots & a_{nk} & a_{n,k + 1} & \cdots & a_{nn} \end{matrix} \right| = \left| \begin{matrix} a_{11} & \cdots & a_{1k} \\ \vdots & & \vdots \\ a_{k1} & \cdots & a_{kk} \end{matrix} \right|\left| \begin{matrix} a_{k + 1,k + 1} & \cdots & a_{k + 1,n} \\ \vdots & & \vdots \\ a_{n,k + 1} & \cdots & a_{nn} \end{matrix} \right|$

矩阵

零矩阵

元素全为0的矩阵称为零矩阵，记为$\mathbf{O}$（大写字母O）或$\mathbf{O}_{m \times n}$。

方阵

行列数相等的矩阵称为方阵。一般称$n$阶方阵。

对角（矩）阵

除主对角线外所有元素均为0的方阵。

${diag}\left\{ a_{11},a_{22},\cdots,a_{nn} \right\} = \mathbf{\Lambda\ }(\text{大写字母}Lambda) = \begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ 0 & a_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & a_{nn} \end{pmatrix} = \begin{pmatrix} a_{11} & & & \\ & a_{22} & & \\ & & \ddots & \\ & & & a_{nn} \end{pmatrix}$

单位（矩）阵

对角线上元素全为1的对角阵。

$\mathbf{I}_{n} = \mathbf{E}_{n} = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} = \begin{pmatrix} 1 & & & \\ & 1 & & \\ & & \ddots & \\ & & & 1 \end{pmatrix}$

上（下）三角（矩）阵

$\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ 0 & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & a_{nn} \end{pmatrix}$（上三角阵），$\begin{pmatrix} a_{11} & 0 & \cdots & 0 \\ a_{21} & a_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}$（下三角阵）

矩阵的运算

加减法

数乘

乘法

性质1：$\left( \mathbf{AB} \right)\mathbf{C} = \mathbf{A}(\mathbf{BC})$

性质2：$\mathbf{A}\left( \mathbf{B} + \mathbf{C} \right) = \mathbf{AB} + \mathbf{AC}$，$\left( \mathbf{A} + \mathbf{B} \right)\mathbf{C} = \mathbf{AC} + \mathbf{BC}$

性质3：$c\left( \mathbf{AB} \right) = \left( c\mathbf{A} \right)\mathbf{B} = \mathbf{A}\left( c\mathbf{B} \right)$

幂

对于方阵$\mathbf{A}$，定义

$\mathbf{A}^{k} = \mathbf{A} \cdot \mathbf{A} \cdot \cdots \cdot \mathbf{A}$（$k$个$\mathbf{A}$）

性质1：$\mathbf{A}^{r}\mathbf{A}^{s} = \mathbf{A}^{r + s}$

性质2：$\left( \mathbf{A}^{r} \right)^{s} = \mathbf{A}^{rs}$

转置

对矩阵$\mathbf{A}$的转置$\mathbf{A}^{T}$或$\mathbf{A}'$就是把它的行转为列，列转为行，类似于沿主对角线翻转。

$\mathbf{A}_{m \times n} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}\text{，}\mathbf{A}' = \begin{pmatrix} a_{11} & a_{21} & \cdots & a_{m1} \\ a_{12} & a_{22} & \cdots & a_{m2} \\ \vdots & \vdots & & \vdots \\ a_{1n} & a_{2n} & \cdots & a_{mn} \end{pmatrix}$

性质1：$\left( \mathbf{A}' \right)' = \mathbf{A}$

性质2：$\left( \mathbf{A} + \mathbf{B} \right)' = \mathbf{A}' + \mathbf{B}'$

性质3：$\left( c\mathbf{A} \right)' = c\mathbf{A}'$

性质4：$\left( \mathbf{AB} \right)' = \mathbf{B}'\mathbf{A}'$

性质4：

设$C = AB$，$D = B'A'$

方阵的行列式

方阵$\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}$的行列式为：$\left| \mathbf{A} \right| = \left| \begin{matrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{matrix} \right|$

性质1：$\left| \mathbf{A}' \right| = \left| \mathbf{A} \right|$

性质2：$\left| c\mathbf{A} \right| = c^{n}\left| \mathbf{A} \right|$

性质3：$\left| \mathbf{AB} \right| = \left| \mathbf{A} \right|\left| \mathbf{B} \right| = \left| \mathbf{BA} \right|$

性质1：由行列式的性质8可得。

性质2：由矩阵数乘的定义和行列式的性质3可得。

性质3：见下。

伴随（矩）阵

对$n$阶方阵$\mathbf{A}$，定义其伴随（矩）阵

$\mathbf{A}^{*} = \begin{pmatrix} \mathbf{A}_{11} & \mathbf{A}_{21} & \cdots & \mathbf{A}_{n1} \\ \mathbf{A}_{12} & \mathbf{A}_{22} & \cdots & \mathbf{A}_{n2} \\ \vdots & \vdots & & \vdots \\ \mathbf{A}_{1n} & \mathbf{A}_{2n} & \cdots & \mathbf{A}_{nn} \end{pmatrix}$

其中$\mathbf{A}_{ij}$是$\left| \mathbf{A} \right|$的$a_{ij}$对应的代数余子式。

性质1：$\mathbf{A}\mathbf{A}^{*} = \mathbf{A}^{*}\mathbf{A} = \left| \mathbf{A} \right| \cdot \mathbf{I}_{n}$

性质2：$\left| \mathbf{A} \right| = 0$的充要条件为$\left| \mathbf{A}^{*} \right| = 0$

性质3：$\left| \mathbf{A}^{*} \right| = \left| \mathbf{A} \right|^{n - 1}$

性质4：$\left( \mathbf{AB} \right)^{*} = \mathbf{B}^{\mathbf{*}}\mathbf{A}^{\mathbf{*}}$

性质1：

$\mathbf{A}\mathbf{A}^{*} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}\begin{pmatrix} \mathbf{A}_{11} & \mathbf{A}_{21} & \cdots & \mathbf{A}_{n1} \\ \mathbf{A}_{12} & \mathbf{A}_{22} & \cdots & \mathbf{A}_{n2} \\ \vdots & \vdots & & \vdots \\ \mathbf{A}_{1n} & \mathbf{A}_{2n} & \cdots & \mathbf{A}_{nn} \end{pmatrix}$，得到的方阵的第$(i\text{，}j)$元素为

$a_{i1}\mathbf{A}_{j1} + a_{i2}\mathbf{A}_{j2} + \cdots + a_{in}\mathbf{A}_{jn}$

> 由异乘变$0$定理，当$i \neq j$时上式等于$0$，所以只有主对角线上的元素不为$0$，并且恰好为$\left| \mathbf{A} \right|$，得

$\mathbf{A}\mathbf{A}^{*} = \begin{pmatrix} \left| \mathbf{A} \right| & & & \\ & \left| \mathbf{A} \right| & & \\ & & \ddots & \\ & & & \left| \mathbf{A} \right| \end{pmatrix} = \left| \mathbf{A} \right| \cdot \mathbf{I}_{n}$

> 同理$\mathbf{A}^{*}\mathbf{A} = \begin{pmatrix} \mathbf{A}_{11} & \mathbf{A}_{21} & \cdots & \mathbf{A}_{n1} \\ \mathbf{A}_{12} & \mathbf{A}_{22} & \cdots & \mathbf{A}_{n2} \\ \vdots & \vdots & & \vdots \\ \mathbf{A}_{1n} & \mathbf{A}_{2n} & \cdots & \mathbf{A}_{nn} \end{pmatrix}\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}$，得到的方阵的第$(i\text{，}j)$元素为

$\mathbf{A}_{1i}a_{1j} + \mathbf{A}_{2i}a_{2j} + \cdots + \mathbf{A}_{ni}a_{nj}$

> 由异乘变$0$定理同理可得。

性质2：

必要性：假设存在$\mathbf{A}$，使得$\left| \mathbf{A} \right| = 0$时$\left| \mathbf{A}^{*} \right| \neq 0$，则由逆矩阵的性质1，$\mathbf{A}^{*}$是可逆阵，由$\mathbf{A}^{*}\mathbf{A} = \left| \mathbf{A} \right| \cdot \mathbf{I}_{n}$，得$\mathbf{A}^{*}\mathbf{A} = \mathbf{O}$，对该式用$\left( \mathbf{A}^{*} \right)^{- 1}$左乘，得

$\left( \mathbf{A}^{*} \right)^{- 1}\mathbf{A}^{*}\mathbf{A =}\left( \mathbf{A}^{*} \right)^{- 1}\mathbf{O} \Rightarrow \mathbf{A} = \mathbf{O}$

由$\mathbf{A}^{*}$的定义，得$\mathbf{A}^{*} = \mathbf{O}$，则$\left| \mathbf{A}^{*} \right| = 0$，产生了矛盾。

充分性：假设存在$\mathbf{A}$，使得$\left| \mathbf{A}^{*} \right| = 0$时$\left| \mathbf{A} \right| \neq 0$，由$\mathbf{A}\mathbf{A}^{*} = \mathbf{A}^{*}\mathbf{A} = \left| \mathbf{A} \right| \cdot \mathbf{I}_{n}$，对方阵求对应行列式，得

$\left| \mathbf{A}\mathbf{A}^{*} \right| = \left| \mathbf{A}^{*}\mathbf{A} \right| = \left| \left| \mathbf{A} \right| \cdot \mathbf{I}_{n} \right| \Rightarrow \left| \mathbf{A} \right|\left| \mathbf{A}^{*} \right| = \left| \mathbf{A}^{*} \right|\left| \mathbf{A} \right| = \left| \mathbf{A} \right|^{n} \cdot \left| \mathbf{I}_{n} \right| = \left| \mathbf{A} \right|^{n}$

由上式，$\left| \mathbf{A}^{*} \right| = 0$时整个式子为$0$，能得出$\left| \mathbf{A} \right|^{n}\mathbf{=}0$，即$\left| \mathbf{A} \right| = 0$，产生了矛盾。

性质3：

由$\mathbf{A}\mathbf{A}^{*} = \mathbf{A}^{*}\mathbf{A} = \left| \mathbf{A} \right| \cdot \mathbf{I}_{n}$，对方阵求对应行列式，得

$\left| \mathbf{A}\mathbf{A}^{*} \right| = \left| \mathbf{A}^{*}\mathbf{A} \right| = \left| \left| \mathbf{A} \right| \cdot \mathbf{I}_{n} \right| \Rightarrow \left| \mathbf{A} \right|\left| \mathbf{A}^{*} \right| = \left| \mathbf{A}^{*} \right|\left| \mathbf{A} \right| = \left| \mathbf{A} \right|^{n} \cdot \left| \mathbf{I}_{n} \right| = \left| \mathbf{A} \right|^{n}$

当$\left| \mathbf{A} \right| = 0$时，由性质2，$\left| \mathbf{A}^{*} \right| = 0$， $\left| \mathbf{A}^{*} \right| = \left| \mathbf{A} \right|^{n - 1}$成立；当$\left| \mathbf{A} \right| \neq 0$时，对等式两边除以$\left| \mathbf{A} \right|$，也得到$\left| \mathbf{A}^{*} \right| = \left| \mathbf{A} \right|^{n - 1}$。

逆（矩）阵

设有$n$阶方阵$\mathbf{A}$，若存在$n$阶阶方阵$\mathbf{B}$，使得

$\mathbf{AB} = \mathbf{BA} = \mathbf{I}_{n}$

则称$\mathbf{A}$为可逆（矩）阵、非（奇）异（矩）阵、满秩矩阵或非退化矩阵，称$\mathbf{B}$是$\mathbf{A}$的逆（矩）阵，记为$\mathbf{B =}\mathbf{A}^{- 1}$，否则称$\mathbf{A}$为奇异（矩）阵。

性质1：一个矩阵若有逆矩阵，则逆矩阵是唯一的。

性质2：$\text{若方阵}\mathbf{A}\text{可逆}$，则$\mathbf{A}^{- 1}$的逆矩阵（即$\left( \mathbf{A}^{- 1} \right)^{- 1}$）为$\mathbf{A}$（$\left( \mathbf{A}^{- 1} \right)^{- 1} = \mathbf{A}$）。

性质3：若$\text{方阵}\mathbf{A}\mathbf{\text{、}}\mathbf{B}\text{可逆}$，则$\mathbf{AB}$也可逆且$\left( \mathbf{AB} \right)^{- 1} = \mathbf{B}^{- 1}\mathbf{A}^{- 1}$**。**

性质4：$\text{若方阵}\mathbf{A}\text{可逆}$，则$c\mathbf{A}$也可逆且$\left( c\mathbf{A} \right)^{- 1} = c^{- 1}\mathbf{A}^{- 1}$。

性质5：方阵$\mathbf{A}$可逆的充要条件为$\left| \mathbf{A} \right| \neq 0$。

$\text{性质}6\text{：若方阵}\mathbf{A}\text{可逆，则}\mathbf{A}^{- 1} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{*}\text{。}$

性质7：$\left| \mathbf{A}^{*} \right| = \left| \mathbf{A} \right|^{n - 1}$

性质8：若$\mathbf{AB} = \mathbf{I}_{n}$，则$\mathbf{A}\mathbf{\text{、}}\mathbf{B}$为同阶方阵且互为逆矩阵。

性质1：

设可逆方阵$\mathbf{A}$满足$\mathbf{AB} = \mathbf{BA} = \mathbf{I}_{n}$和$\mathbf{AC} = \mathbf{CA} = \mathbf{I}_{n}$，则

$\mathbf{B = B}\mathbf{I}_{n} = \mathbf{B}\left( \mathbf{AC} \right)\mathbf{=}\left( \mathbf{BA} \right)\mathbf{C =}\mathbf{I}_{n}\mathbf{C}$

这说明了逆矩阵的唯一性。

性质2：

因为对于$\mathbf{A}^{- 1}$，存在矩阵$\mathbf{A}$，满足$\mathbf{A}^{- 1}\mathbf{A} = \mathbf{A}\mathbf{A}^{- 1} = \mathbf{I}_{n}$，符合逆矩阵的定义。

性质3：

因为对于$\mathbf{AB}$，存在矩阵$\mathbf{B}^{- 1}\mathbf{A}^{- 1}$，有

$\left( \mathbf{AB} \right)\left( \mathbf{B}^{- 1}\mathbf{A}^{- 1} \right) = \mathbf{A}\left( \mathbf{B}\mathbf{B}^{- 1} \right)\mathbf{A}^{- 1} = \mathbf{A}\mathbf{I}_{n}\mathbf{A}^{- 1} = \mathbf{A}\mathbf{A}^{- 1} = \mathbf{I}_{n}$

且

$\left( \mathbf{B}^{- 1}\mathbf{A}^{- 1} \right)\left( \mathbf{AB} \right) = \mathbf{B}^{- 1}\left( \mathbf{A}^{- 1}\mathbf{A} \right)\mathbf{B} = \mathbf{B}^{- 1}\mathbf{I}_{n}\mathbf{B} = \mathbf{B}^{- 1}\mathbf{B} = \mathbf{I}_{n}$

满足逆矩阵的定义。所以$\mathbf{AB}$可逆且逆矩阵为$\mathbf{B}^{- 1}\mathbf{A}^{- 1}$

性质4：

因为存在矩阵$c^{- 1}\mathbf{A}^{- 1}$，满足$\left( c\mathbf{A} \right)\left( c^{- 1}\mathbf{A}^{- 1} \right) = \left( c \cdot c^{- 1} \right)\left( \mathbf{A}\mathbf{A}^{- 1} \right) = \mathbf{I}_{n}$，$\left( c^{- 1}\mathbf{A}^{- 1} \right)\left( c\mathbf{A} \right) = \left( c \cdot c^{- 1} \right)\left( \mathbf{A}^{- 1}\mathbf{A} \right) = \mathbf{I}_{n}$，符合逆矩阵的定义。

性质5：

必要性：由$\mathbf{A}\text{可逆}$，得$\mathbf{A}\mathbf{A}^{- 1} = \mathbf{I}_{n}$，对等式两边求方阵的行列式，得

$\left| \mathbf{A}\mathbf{A}^{- 1} \right| = \left| \mathbf{A} \right|\left| \mathbf{A}^{- 1} \right| = \left| \mathbf{I}_{n} \right| = 1$

所以$\left| \mathbf{A} \right| \neq 0$且$\left| \mathbf{A}^{- 1} \right| \neq 0$。

充分性：由$\mathbf{A}\mathbf{A}^{*} = \mathbf{A}^{*}\mathbf{A} = \left| \mathbf{A} \right| \cdot \mathbf{I}_{n}$，除以$\left| \mathbf{A} \right|$得

$\mathbf{A} \cdot \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{*} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{*} \cdot \mathbf{A} = \mathbf{I}_{n}$

满足逆矩阵的定义，所以$\mathbf{A}$是可逆的，且逆矩阵为

$\mathbf{A}^{- 1} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{*}$

性质6：

由性质5的证明可得。

性质7：

由$\mathbf{A}\mathbf{A}^{*} = \mathbf{A}^{*}\mathbf{A} = \left| \mathbf{A} \right| \cdot \mathbf{I}_{n}$，对方阵求对应行列式，得

$\left| \mathbf{A}\mathbf{A}^{*} \right| = \left| \mathbf{A}^{*}\mathbf{A} \right| = \left| \left| \mathbf{A} \right| \cdot \mathbf{I}_{n} \right| \Rightarrow \left| \mathbf{A} \right|\left| \mathbf{A}^{*} \right| = \left| \mathbf{A}^{*} \right|\left| \mathbf{A} \right| = \left| \mathbf{A} \right|^{n} \cdot \left| \mathbf{I}_{n} \right| = \left| \mathbf{A} \right|^{n}$

当$\left| \mathbf{A} \right| = 0$时，$\left| \mathbf{A}^{*} \right| = 0$， $\left| \mathbf{A}^{*} \right| = \left| \mathbf{A} \right|^{n - 1}$成立；当$\left| \mathbf{A} \right| \neq 0$时，对等式两边除以$\left| \mathbf{A} \right|$，也得到$\left| \mathbf{A}^{*} \right| = \left| \mathbf{A} \right|^{n - 1}$。

性质8：

对等式求行列式，得

$\left| \mathbf{AB} \right| = \left| \mathbf{I}_{n} \right| \Rightarrow \left| \mathbf{A} \right|\left| \mathbf{B} \right| = \left| I_{n} \right| = 1 \neq 0$

所以$\left| \mathbf{A} \right| \neq 0$且$\left| \mathbf{B} \right| \neq 0$，由性质5，得$\mathbf{A}$，$\mathbf{B}$可逆，且有

$\mathbf{A = A}\mathbf{I}_{n}\mathbf{= A}\left( \mathbf{B}\mathbf{B}^{- 1} \right)\mathbf{=}\left( \mathbf{AB} \right)\mathbf{B}^{- 1}\mathbf{=}\mathbf{I}_{n}\mathbf{B}^{- 1}\mathbf{=}\mathbf{B}^{- 1}$

$\mathbf{B =}\mathbf{I}_{n}\mathbf{B =}\left( \mathbf{A}^{- 1}\mathbf{A} \right)\mathbf{B =}\mathbf{A}^{- 1}\left( \mathbf{AB} \right)\mathbf{=}\mathbf{A}^{- 1}\mathbf{I}_{n}\mathbf{=}\mathbf{A}^{- 1}$

初等变换与初等矩阵

定义矩阵的三类初等行（列）变换如下：

第一类初等变换：对调矩阵中某两行（列）的位置。。

第二类初等变换：用一非0常数$c$乘以矩阵的某一行（列）

第三类初等变换：将矩阵的某一行（列）乘以常数$c$后加到另一行（列）上去。

定义三类初等矩阵如下：

第一类初等矩阵：$\mathbf{P}_{ij}$或$\mathbf{E}(i,j)$：将单位阵$\mathbf{I}_{n}$的第$i$行与第$j$行（第$i$列与第$j$列）对换后得到的矩阵。

第二类初等矩阵：$\mathbf{P}_{i}(c)$或$\mathbf{E}\left( i(c) \right)$：将常数$c$乘以单位阵$\mathbf{I}_{n}$的第$i$行（第$j$列）位置而得到的矩阵。

第三类初等矩阵：$\mathbf{T}_{ij}(c)$或$\mathbf{E}\left( ij(k) \right)$：将单位阵$\mathbf{I}_{n}$的第$i$行（第$j$列）乘以$c$后加到第$j$行（第$i$列）上得到的矩阵。

$\mathbf{P}_{ij} = \mathbf{E}(i,j) = \begin{pmatrix} 1 & & & & & & \\ & \ddots & & & & & \\ & & 0 & \cdots & 1 & & \\ & & \vdots & & \vdots & & \\ & & 1 & \cdots & 0 & & \\ & & & & & \ddots & \\ & & & & & & 1 \end{pmatrix}$

$\mathbf{P}_{i}(c) = \mathbf{E}\left( i(c) \right) = \begin{pmatrix} 1 & & & & & & \\ & \ddots & & & & & \\ & & 1 & & & & \\ & & & c & & & \\ & & & & 1 & & \\ & & & & & \ddots & \\ & & & & & & 1 \end{pmatrix}$

$\mathbf{T}_{ij}(c) = \mathbf{E}\left( ij(k) \right) = \begin{pmatrix} 1 & & & & & & \\ & \ddots & & & & & \\ & & 1 & \cdots & 0 & & \\ & & \vdots & & \vdots & & \\ & & c & \cdots & 1 & & \\ & & & & & \ddots & \\ & & & & & & 1 \end{pmatrix}$

相抵矩阵

如果一个矩阵$\mathbf{A}$经过有限次初等行变换后变成矩阵$\mathbf{B}$，则称$\mathbf{A}$和$\mathbf{B}$是行等价的，记为$\mathbf{A}\overset{r}{\sim}\mathbf{B}$。

如果一个矩阵$\mathbf{A}$经过有限次初等列变换后变成矩阵$\mathbf{B}$，则称$\mathbf{A}$和$\mathbf{B}$是列等价的，记为$\mathbf{A}\overset{c}{\sim}\mathbf{B}$。

如果一个矩阵$\mathbf{A}$经过有限次初等变换后变成矩阵$\mathbf{B}$，则称$\mathbf{A}$和$\mathbf{B}$是等价或相抵的，记为$\mathbf{A}\sim\mathbf{B}$。

矩阵$\mathbf{A}$必然可以通过初等变换变为如下矩阵，该矩阵称为矩阵$\mathbf{A}$的相抵标准型。

$\begin{pmatrix} 1 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & & \vdots & \vdots & & \vdots \\ 0 & \cdots & 1 & 0 & \cdots & 0 \\ 0 & \cdots & 0 & 0 & \cdots & 0 \\ \vdots & & \vdots & \vdots & & \vdots \\ 0 & \cdots & 0 & 0 & \cdots & 0 \end{pmatrix}$（也可以是$\mathbf{O}$）

证明：对于矩阵$\mathbf{A =}\begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$ ，如果$\mathbf{A} \neq \mathbf{O}$，可以通过三种初等变换实现。

（行）阶梯形矩阵

设$\mathbf{A} = \left( a_{ij} \right)_{m \times n}$为$m \times n$矩阵，对任意的$1 \leq i \leq m$，定义$k_{i}$如下：若$\mathbf{A}$的第$i$行元素全为$0$，则$k_{i} = + \infty$；若$\mathbf{A}$的第$i$行元素不全为$0$，则$k_{i}$是第$i$行所有非$0$元素列指标的最小值。即若$k_{i} < + \infty$，则$a_{ik_{i}}$是$\mathbf{A}$的第$i$行中从左到右第一个非元素，$a_{ik_{i}}$称为第$i$行的阶梯点。

若存在$0 \leq r \leq m$，使得$k_{1} < k_{2} < \cdots < k_{r}$，$k_{r + 1} = \cdots = k_{m} = + \infty$，则称这样的矩阵$\mathbf{A}$为（行）阶梯形矩阵。即（行）阶梯形矩阵的矩阵阶梯点的列指标随着行数严格递增，或者从图形上看非$0$元素全体构成一个阶梯。

矩阵$\mathbf{A}$经过若干次初等行变换，可以化为阶梯形矩阵。

证明：类似于高斯消元法。

设$\mathbf{A}$是一个$m \times n$阵，则对$\mathbf{A}$作一次初等行变换后得到的矩阵等于用一个$m$阶相应的初等矩阵左乘后得到的积。对$\mathbf{A}$作一次初等列变换后得到的矩阵等于用一个$n$阶相应的初等矩阵右乘后得到的积。（简称为“行左列右”）

证明：

$\mathbf{P}_{ij}\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & & \vdots \\ a_{j1} & a_{j2} & \cdots & a_{jn} \\ \vdots & \vdots & & \vdots \\ a_{i1} & a_{i2} & & a_{in} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}\text{，}\mathbf{P}_{i}(c)\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & & \vdots \\ ca_{i1} & ca_{i2} & & ca_{in} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}\text{，}\mathbf{T}_{ij}(c)\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & & \vdots \\ a_{i1} & a_{i2} & \cdots & a_{in} \\ \vdots & \vdots & & \vdots \\ ca_{i1} + a_{j1} & ca_{i2} + a_{j2} & & ca_{in} + a_{jn} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}$

分别对应三种初等行变换。

$\mathbf{P}_{ij}\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & & \vdots \\ a_{j1} & a_{j2} & \cdots & a_{jn} \\ \vdots & \vdots & & \vdots \\ a_{i1} & a_{i2} & & a_{in} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}\text{，}\mathbf{P}_{i}(c)\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & & \vdots \\ ca_{i1} & ca_{i2} & & ca_{in} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}\text{，}\mathbf{T}_{ij}(c)\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ \vdots & \vdots & & \vdots \\ a_{i1} & a_{i2} & \cdots & a_{in} \\ \vdots & \vdots & & \vdots \\ ca_{i1} + a_{j1} & ca_{i2} + a_{j2} & & ca_{in} + a_{jn} \\ \vdots & \vdots & & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \end{pmatrix}$

分别对应三种初等列变换。

从这里开始行和列就有了差别，这是由矩阵乘法的定义引起的，而更深层次上这与线性方程组是横着书写方程而非竖着书写方程有关。

定理：初等矩阵都是非异阵且其逆矩阵仍是同类初等矩阵，即

$\mathbf{P}_{ij}^{- 1} = \mathbf{P}_{ij}\text{，}\mathbf{P}_{i}(c)^{- 1} = \mathbf{P}_{i}\left( \frac{1}{c} \right)\text{，}\mathbf{T}_{ij}(c)^{- 1} = \mathbf{T}_{ij}( - c)$

证明：对于$\mathbf{P}_{ij}$，要寻找矩阵$\mathbf{B}$，满足$\mathbf{P}_{ij}\mathbf{B} = \mathbf{B}\mathbf{P}_{ij} = \mathbf{I}_{n}$，由上面的定理，发现若$\mathbf{B} = \mathbf{P}_{ij}$，则$\mathbf{P}_{ij}\mathbf{P}_{ij}$相当于对$\mathbf{P}_{ij}$对换第$i$行与第$j$行（第$i$列与第$j$列），这使得由单位阵$\mathbf{I}_{n}$经过对换第$i$行与第$j$行（第$i$列与第$j$列）而得到的$\mathbf{P}_{ij}$又变回了单位阵$\mathbf{I}_{n}$。

对于$\mathbf{P}_{i}(c)$，发现$\mathbf{P}_{i}(c)\mathbf{P}_{i}\left( \frac{1}{c} \right)$相当于在原单位阵第$i$行（第$j$行）乘以$\frac{1}{c}$得到的$\mathbf{P}_{i}\left( \frac{1}{c} \right)$再乘以$c$还原回单位阵$\mathbf{I}_{n}$。$\mathbf{P}_{i}\left( \frac{1}{c} \right)\mathbf{P}_{i}(c)$也类似。

对于$\mathbf{T}_{ij}(c)$，发现$\mathbf{T}_{ij}(c)\mathbf{T}_{ij}( - c)$相当于在原单位阵施加第三类初等变化得到$\mathbf{T}_{ij}( - c)$的基础上再施加相反的第三类初等变化还原回单位阵$\mathbf{I}_{n}$。$\mathbf{T}_{ij}( - c)\mathbf{T}_{ij}(c)$也类似。

定理：非异阵经初等变换后仍为非异阵，奇异阵经初等变换后仍为奇异阵。

证明：由逆矩阵的性质3，可以得到非异阵经初等变换即与可逆的初等矩阵相乘仍可逆。设矩阵$\mathbf{A}$为奇异阵，$\mathbf{P}$为初等矩阵，假设$\mathbf{PA}$为非异阵，则因为$\mathbf{A} = \mathbf{P}^{- 1}(\mathbf{PA})$，而$\mathbf{P}^{- 1}(\mathbf{PA})$由上面的性质得可逆，产生了矛盾。所以$\mathbf{PA}$为奇异阵。

定理：

$\left| \mathbf{P}_{ij} \right| = - 1\text{，}\left| \mathbf{P}_{i}(c) \right| = c\text{，}\left| \mathbf{T}_{ij}(c) \right| = 1$

证明：这些分别是由行列式的性质1、4，性质1、3，性质1、7得到。

矩阵的相抵满足如下性质：

（1）$\mathbf{A}\sim\mathbf{A}$

（2）若$\mathbf{A}\sim\mathbf{B}$，则$\mathbf{B}\sim\mathbf{A}$

（3）若$\mathbf{A}\sim\mathbf{B}$，$\mathbf{B}\sim\mathbf{C}$，则$\mathbf{A}\sim\mathbf{C}$

证明：用乘以初等矩阵代替初等变换。

（1）因为$\mathbf{I}$也是初等矩阵，而$\mathbf{IA} = \mathbf{A}$，所以$\mathbf{A}\sim\mathbf{A}$。

（2）设$\mathbf{P}_{k}\mathbf{P}_{k - 1}\cdots\mathbf{P}_{2}\mathbf{P}_{1}\mathbf{A}\mathbf{Q}_{1}\mathbf{Q}_{2}\cdots\mathbf{Q}_{t - 1}\mathbf{Q}_{t} = \mathbf{B}$，其中$\mathbf{P}$，$\mathbf{Q}$均为初等矩阵，则对等式左乘$\mathbf{P}_{1}^{- 1}\mathbf{P}_{2}^{- 1}\cdots\mathbf{P}_{k - 1}^{- 1}\mathbf{P}_{k}^{- 1}$，接着对等式右乘$\mathbf{Q}_{t}^{- 1}\mathbf{Q}_{t - 1}^{- 1}\cdots\mathbf{Q}_{2}^{- 1}\mathbf{Q}_{1}^{- 1}$，得

$\mathbf{A} = \mathbf{P}_{1}^{- 1}\mathbf{P}_{2}^{- 1}\cdots\mathbf{P}_{k - 1}^{- 1}\mathbf{P}_{k}^{- 1}\mathbf{B}\mathbf{Q}_{t}^{- 1}\mathbf{Q}_{t - 1}^{- 1}\cdots\mathbf{Q}_{2}^{- 1}\mathbf{Q}_{1}^{- 1} = \mathbf{A}$

（3）设$\mathbf{P}_{k}\mathbf{P}_{k - 1}\cdots\mathbf{P}_{2}\mathbf{P}_{1}\mathbf{A}\mathbf{Q}_{1}\mathbf{Q}_{2}\cdots\mathbf{Q}_{t - 1}\mathbf{Q}_{t} = \mathbf{B}$，$\mathbf{R}_{k'}\mathbf{R}_{k' - 1}\cdots\mathbf{R}_{2}\mathbf{R}_{1}\mathbf{B}\mathbf{S}_{1}\mathbf{S}_{2}\cdots\mathbf{S}_{t' - 1}\mathbf{S}_{t'} = \mathbf{C}$，其中$\mathbf{P}$，$\mathbf{Q}$，$\mathbf{R}$，$\mathbf{S}$均为初等矩阵，把第二个式子中的$\mathbf{B}$用第一个式子代替，得

$\mathbf{R}_{k'}\mathbf{R}_{k' - 1}\cdots\mathbf{R}_{2}\mathbf{R}_{1}\mathbf{P}_{k}\mathbf{P}_{k - 1}\cdots\mathbf{P}_{2}\mathbf{P}_{1}\mathbf{A}\mathbf{Q}_{1}\mathbf{Q}_{2}\cdots\mathbf{Q}_{t - 1}\mathbf{Q}_{t}\mathbf{S}_{1}\mathbf{S}_{2}\cdots\mathbf{S}_{t' - 1}\mathbf{S}_{t'} = \mathbf{C}$

定理：设$\mathbf{A}$是一个$n$阶可逆阵，则仅用初等行变换或仅用初等列变换即可把化为单位阵$\mathbf{I}_{n}$。

证明：类似高斯消元法。

定理：任一$n$阶非异阵均可表示为有限个初等矩阵的积。

证明：由上面的定理，存在有限个初等矩阵$\mathbf{P}_{1}\text{，}\mathbf{P}_{2}\text{，}\cdots \text{，}\mathbf{P}_{k - 1}\text{，}\mathbf{P}_{k}$，使得对任一$n$阶非异阵$\mathbf{A}$，有

$\mathbf{P}_{k}\mathbf{P}_{k - 1}\cdots\mathbf{P}_{2}\mathbf{P}_{1}\mathbf{A} = \mathbf{I}_{n}$

所以

$\mathbf{A} = \mathbf{P}_{1}^{- 1}\mathbf{P}_{2}^{- 1}\cdots\mathbf{P}_{k - 1}^{- 1}\mathbf{P}_{k}^{- 1}$

$\mathbf{P}_{1}^{- 1}\text{，}\mathbf{P}_{2}^{- 1}\text{，}\cdots\mathbf{P}_{k - 1}^{- 1}\text{，}\mathbf{P}_{k}^{- 1}$均为可逆矩阵。

Cauchy-Binet（柯西—毕内）公式

设$\mathbf{A}_{m \times n}$，$\mathbf{B}_{n \times m}$，则有

（1）若$m > n$，则$\left| \mathbf{AB} \right| = 0$

（2）若$m \leq n$，则

$\left| \mathbf{AB} \right| = \sum_{1 \leq j_{1} \leq j_{2} \leq \cdots \leq j_{m} \leq n}^{}{\mathbf{A}\begin{pmatrix} 1 & 2 & \cdots & m \\ j_{1} & j_{2} & \cdots & j_{m} \end{pmatrix}\mathbf{B}\begin{pmatrix} j_{1} & j_{2} & \cdots & j_{m} \\ 1 & 2 & \cdots & m \end{pmatrix}}$

推论

设正整数$r$满足$r \leq m$，则

（1）若$r > n$，则

$\mathbf{AB}\begin{pmatrix} i_{1} & i_{2} & \cdots & i_{r} \\ j_{1} & j_{2} & \cdots & j_{r} \end{pmatrix} = 0$

（2）若$r \leq n$，则

$\mathbf{AB}\begin{pmatrix} i_{1} & i_{2} & \cdots & i_{r} \\ j_{1} & j_{2} & \cdots & j_{r} \end{pmatrix} = \sum_{1 \leq k_{1} \leq k_{2} \leq \cdots \leq k_{r} \leq n}^{}{\mathbf{A}\begin{pmatrix} i_{1} & i_{2} & \cdots & i_{r} \\ k_{1} & k_{2} & \cdots & k_{r} \end{pmatrix}\mathbf{B}\begin{pmatrix} k_{1} & k_{2} & \cdots & k_{r} \\ j_{1} & j_{2} & \cdots & j_{r} \end{pmatrix}}$

向量与线性空间

线性空间

设$\mathbb{K}$是一个数域，$\mathbb{K}$是一个集合，在$V$上定义了一个加法“$+$”，即对$V$为中任意两个元素$\mathbf{\alpha}\text{，}\mathbf{\beta}$，总存在$V$中唯一的元素$\mathbf{\gamma}$与之对应，记为$\mathbf{\gamma} = \mathbf{\alpha} + \mathbf{\beta}$。在数域$\mathbb{K}$与之间定义了一种运算，称为数乘，即对$\mathbb{K}$中任一数$k$及$V$中任一元素$\mathbf{\alpha}$，在$V$中总有唯一的元素$\mathbf{\delta}$与之对应，记为$\mathbf{\delta} = k \cdot \mathbf{\alpha =}k\mathbf{\alpha}$。若上述加法及数乘满足下列运算规则：

> （1）加法交换律：$\mathbf{\alpha} + \mathbf{\beta} = \mathbf{\beta} + \mathbf{\alpha}$
>
> （2）加法结合律：$\left( \mathbf{\alpha} + \mathbf{\beta} \right) + \mathbf{\gamma} = \mathbf{\alpha} + \left( \mathbf{\beta} + \mathbf{\gamma} \right)$
>
> （3）零向量：在中存在一个元素$\mathbf{0}$，对于中任一元素$\mathbf{\alpha}$，都有$\mathbf{\alpha + 0 = \alpha}$，称$\mathbf{0}$为零向量
>
> （4）负向量：对于$V$中每个元素$\mathbf{\alpha}$，存在元素$\mathbf{\beta}$，使$\mathbf{\alpha + \beta = 0}$，并记$\mathbf{\beta = - \alpha}$
>
> （5）：$1 \cdot \mathbf{\alpha} = \mathbf{\alpha}$
>
> （6）左分配律：$k\left( \mathbf{\alpha + \beta} \right) = k\mathbf{\alpha} + k\mathbf{\beta}$
>
> （7）右分配律：$(k + l)\mathbf{\alpha =}k\mathbf{\alpha +}l\mathbf{\beta}$
>
> （8）数乘结合律：$k\left( l\mathbf{\alpha} \right) = (kl)\mathbf{\alpha}$

则称$V$为$\mathbb{K}$上的线性空间/向量空间

上面对“向量”定义事实上与所学的平面向量和空间向量相匹配，从这种意义上看，向量的交换律、结合律、分配律实际上是“无需证明”的。

除了定义中给出的法则，线性空间中的向量满足如下性质，这些性质大多数显而易见，但都是需要证明的：

（1）零向量是唯一的

（2）一个向量的负向量是唯一的

（3）$\mathbf{\alpha + \beta = \alpha + \gamma \Rightarrow \beta = \gamma}$，即加法消去律成立

（4）0与任意向量的数乘为零向量

（5）零向量与任意数的数乘为零向量

（6）$- 1$与任一向量的数乘为该向量的反向量

（7）若$k\mathbf{\alpha} = \mathbf{0}$，则$\mathbf{\alpha} = \mathbf{0}$或$k = 0$

（8）$- \left( - \mathbf{\alpha} \right) = \mathbf{\alpha}$

（9）$- \left( k\mathbf{\alpha} \right) = ( - k)\mathbf{\alpha} = k\left( - \mathbf{\alpha} \right)$

（10）$k\left( \mathbf{\alpha} - \mathbf{\beta} \right) = k\mathbf{\alpha} - k\mathbf{\beta}$

证明：

（1）设$\mathbf{0}_{1}\text{，}\mathbf{0}_{2}$为$V$中两个零向量，则由运算规则（3），得

$\mathbf{0}_{1} = \mathbf{0}_{1} + \mathbf{0}_{2} = \mathbf{0}_{2}$

这就说明任意两个零向量是相等的，即零向量是唯一的。

（2）设$\mathbf{\alpha}\text{，}\mathbf{\beta}_{1}\text{，}\mathbf{\beta}_{2}$为$V$中三个向量，且

$\mathbf{\alpha} + \mathbf{\beta}_{1} = \mathbf{0}\text{，}\mathbf{\alpha +}\mathbf{\beta}_{2} = \mathbf{0}$

则

$\mathbf{\beta}_{1}\overset{3}{\mathbf{=}}\mathbf{\beta}_{1}\mathbf{+ 0}\overset{2}{\mathbf{=}}\mathbf{\beta}_{1}\mathbf{+}\left( \mathbf{\alpha +}\mathbf{\beta}_{2} \right)\overset{2}{\mathbf{=}}\left( \mathbf{\beta}_{1}\mathbf{+ \alpha} \right)\mathbf{+}\mathbf{\beta}_{2}\overset{1}{\mathbf{=}}\left( \mathbf{\alpha +}\mathbf{\beta}_{1} \right)\mathbf{+}\mathbf{\beta}_{2}\overset{1}{\mathbf{=}}\mathbf{0 +}\mathbf{\beta}_{2}\overset{2}{\mathbf{=}}\mathbf{\beta}_{2}$

等号上面的数字代表用到的运算规则。

（3）$\left( \mathbf{- a} \right)\mathbf{+}\left( \mathbf{\alpha + \beta} \right)\mathbf{=}\left( \mathbf{- \alpha} \right)\mathbf{+}\left( \mathbf{\alpha + \gamma} \right)\overset{2}{\Rightarrow}\left( \left( \mathbf{- \alpha} \right)\mathbf{+ \alpha} \right)\mathbf{+ \beta =}\left( \left( \mathbf{- \alpha} \right)\mathbf{+ \alpha} \right)\mathbf{+ \gamma}\overset{4}{\Rightarrow}\mathbf{0 + \beta = 0 + \gamma}\overset{3}{\Rightarrow}\mathbf{\beta = \gamma}$

（4）

向量组的线性关系

线性组合与线性表示

设$V$是数域$\mathbb{K}$上的线性空间，$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$和$\mathbf{\beta}$均是$V$中的向量，若存在$\mathbb{K}$中的$n$个数$k_{1}\text{，}k_{2}\text{，}\cdots \text{，}k_{n}$，使

$\mathbf{\beta} = k_{1}\mathbf{\alpha}_{1} + k_{2}\mathbf{\alpha}_{2} + \cdots k_{n}\mathbf{\alpha}_{n}$

则称$\mathbf{\beta}$是$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$的线性组合，$\mathbf{\beta}$可由$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性表示，$\mathbf{\beta}$处于向量$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$张成的空间。

线性相关与线性无关

若存在$\mathbb{K}$中不全为0的n个数$k_{1}\text{，}k_{2}\text{，}\cdots \text{，}k_{n}$，使

$k_{1}\mathbf{\alpha}_{1} + k_{2}\mathbf{\alpha}_{2} + \cdots k_{n}\mathbf{\alpha}_{n} = \mathbf{0}$

则称$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性相关。反之，则称$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性无关。

对于线性无关的向量$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$，若存在$k_{1}\text{，}k_{2}\text{，}\cdots \text{，}k_{n}\mathbb{\in K}$，使

$k_{1}\mathbf{\alpha}_{1} + k_{2}\mathbf{\alpha}_{2} + \cdots k_{n}\mathbf{\alpha}_{n} = \mathbf{0}$

则必有$k_{1} = k_{2} = \cdots = k_{n} = 0$

定理：只含一个向量$\mathbf{\alpha}$的向量组线性相关的充要条件为$\mathbf{\alpha} = \mathbf{0}$

定理：若向量组$S$含有零向量，则$S$线性相关。

定理：若$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$是一组线性相关的向量，则任一包含这组向量的向量组线性相关。

定理：若$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$是一组线性无关的向量，则从这一组向量中任意取出一组向量线性无关。

定理：向量$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性相关的充要条件是其中至少有一个向量可以表示成其余向量的线性组合。

证明：

> 必要性：由$k_{1}\mathbf{\alpha}_{1} + k_{2}\mathbf{\alpha}_{2} + \cdots k_{n}\mathbf{\alpha}_{n} = \mathbf{0}$中$k_{1}\text{，}k_{2}\text{，}\cdots \text{，}k_{n}$不全为0，可设$k_{i} \neq 0$，则有

$\mathbf{\alpha}_{i} = - \frac{k_{1}\mathbf{\alpha}_{1}}{k_{i}} - \frac{k_{2}\mathbf{\alpha}_{2}}{k_{i}} - \cdots - \frac{k_{i - 1}\mathbf{\alpha}_{i - 1}}{k_{i}} - \frac{k_{i + 1}\mathbf{\alpha}_{i + 1}}{k_{i}} - \cdots - \frac{k_{n}\mathbf{\alpha}_{n}}{k_{i}}$

> 这就说明有一个向量被表示成了其余向量的线性组合，即“至少一个”。
>
> 充分性：设$\mathbf{\alpha}_{i} = k_{1}\mathbf{\alpha}_{1} + k_{2}\mathbf{\alpha}_{2} + \cdots + k_{i - 1}\mathbf{\alpha}_{i - 1} + k_{i + 1}\mathbf{\alpha}_{i + 1} + \cdots + k_{n}\mathbf{\alpha}_{n}$，移项可得

$k_{1}\mathbf{\alpha}_{1} + k_{2}\mathbf{\alpha}_{2} + \cdots + k_{i - 1}\mathbf{\alpha}_{i - 1} - \mathbf{\alpha}_{i} + k_{i + 1}\mathbf{\alpha}_{i + 1} + \cdots + k_{n}\mathbf{\alpha}_{n} = \mathbf{0}$

> 这就说明这组向量线性相关。

定理：设$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}\text{，}\mathbf{\beta}$是线性空间$V$中的向量，且$\mathbf{\beta}$可表示为$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$的线性组合，即$\mathbf{\beta} = k_{1}\mathbf{\alpha}_{1} + k_{2}\mathbf{\alpha}_{2} + \cdots k_{n}\mathbf{\alpha}_{n}$，则这种线性表示唯一的充要条件是$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性无关。

证明：用反证法容易证明。

定理：设向量组$A\text{，}B\text{，}C$满足：$A$中任一向量都是$B$中向量的线性组合，$B$中任一向量都是$C$中向量的线性组合，则$A$中任一向量都是$C$中向量的线性组合。

定理：若$\mathbf{\alpha =}\left( a_{1}\text{，}a_{2}\text{，}\cdots \text{，}a_{n} \right)\text{，}\mathbf{\beta =}\left( b_{1}\text{，}b_{2}\text{，}\cdots \text{，}b_{n} \right)$是两个$n$维行向量，则$\mathbf{\alpha}\text{，}\mathbf{\beta}$线性相关的充要条件是$a_{i}\text{，}b_{i}$成比例。

线性空间的基与坐标向量

线性空间的基和维数：设$V$是数域$\mathbb{K}$上的线性空间，若在$V$中存在线性无关的向量$\mathbf{e}_{1}\text{，}\mathbf{e}_{2}\text{，}\cdots \text{，}\mathbf{e}_{n}$，使得$V$中任一向量均可表示为这组向量的线性组合，则称$\left\{ \mathbf{e}_{1}\text{，}\mathbf{e}_{2}\text{，}\cdots \text{，}\mathbf{e}_{n} \right\}$是$V$的一组基，线性空间$V$称为$n$维线性空间（即该线性空间的维数为$n$）并记$\dim_{\mathbb{K}}V = n$。如果不存在有限个线性无关的向量可以构成$V$的一组基，则称$V$是无限维线性空间。

定理：用基表示线性空间的任一向量的表示是唯一的。

证明：设对于$\alpha$，有

$\mathbf{\alpha} = a_{1}\mathbf{e}_{1} + a_{2}\mathbf{e}_{2} + \cdots + a_{n}\mathbf{e}_{n} = b_{1}\mathbf{e}_{1} + b_{2}\mathbf{e}_{2} + \cdots b_{n}\mathbf{e}_{n}$

则

$\mathbf{\alpha} - \mathbf{\alpha =}\left( a_{1} - b_{1} \right)\mathbf{e}_{1} + \left( a_{2} - b_{2} \right)\mathbf{e}_{2} + \cdots + \left( a_{n} - b_{n} \right)\mathbf{e}_{n} = \mathbf{0}$

因为$\mathbf{e}_{1}\text{，}\mathbf{e}_{2}\text{，}\cdots \text{，}\mathbf{e}_{n}$线性无关，所以$a_{1} = b_{1}\text{，}a_{2} = b_{2}\text{，}\cdots \text{，}a_{n} = b_{n}$，即表示的唯一。

坐标向量：对于$n$维线性空间V和对应的一组基$\left\{ \mathbf{e}_{1}\text{，}\mathbf{e}_{2}\text{，}\cdots \text{，}\mathbf{e}_{n} \right\}$，固定基向量的次序为$\left\{ \mathbf{e}_{1}\text{，}\mathbf{e}_{2}\text{，}\cdots \text{，}\mathbf{e}_{n} \right\}$，则线性表示

$\mathbf{\alpha} = a_{1}\mathbf{e}_{1} + a_{2}\mathbf{e}_{2} + \cdots + a_{n}\mathbf{e}_{n}$

表明$\mathbf{\alpha}$可与唯一的有序数对$\left( a_{1}\text{，}a_{2}\text{，}\cdots \text{，}a_{n} \right)$或$\begin{pmatrix} a_{1} \\ a_{2} \\ \cdots \\ a_{n} \end{pmatrix}$对应，称$\left( a_{1}\text{，}a_{2}\text{，}\cdots \text{，}a_{n} \right)$或$\begin{pmatrix} a_{1} \\ a_{2} \\ \cdots \\ a_{n} \end{pmatrix}$为$\mathbf{\alpha}$在基$\left\{ e_{1}\text{，}e_{2}\text{，}\cdots \text{，}e_{n} \right\}$下的坐标向量。并把V中所有向量在基$\left\{ \mathbf{e}_{1}\text{，}\mathbf{e}_{2}\text{，}\cdots \text{，}\mathbf{e}_{n} \right\}$下对应的坐标向量构成的或$n$维线性空间记为$\mathbb{K}^{n}$（$n$维行向量空间）或$\mathbb{K}_{n}$（维列向量空间）。

从此，对于$n$维线性空间的研究就可以转换到对于$\mathbb{K}^{n}$或$\mathbb{K}_{n}$的研究（通常用$\mathbb{K}_{n}$）。

向量组和矩阵的秩

极/最大（线性）无关组：有两个等价定义

定义1：在线性空间$V$中，若在向量族$S$中存在一组向量$\left\{ \mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n} \right\}$满足

> （1）$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性无关；
>
> （2）$S$中任意一个向量都可以由$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性表示。

则称$\left\{ \mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n} \right\}$是向量族的极/最大线性无关组，简称极/最大无关组。

定义2：在线性空间$V$中，若在向量族$S$中存在一组向量$\left\{ \mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n} \right\}$满足

> （1）$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性无关；
>
> （2）如果$S$中向量个数大于$n$，则任意$n + 1$个向量线性相关。

则称$\left\{ \mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n} \right\}$是向量族的极/最大线性无关组，简称极/最大无关组。

证明：

$1 \rightarrow 2$：设对于$S$中任一向量$\mathbf{\alpha}_{r}$，有

$\mathbf{\alpha}_{r} = a_{1}\mathbf{\alpha}_{1} + a_{2}\mathbf{\alpha}_{2} + \cdots a_{n}\mathbf{\alpha}_{n}$

则由线性相关的定义，容易看出向量$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}\text{，}\mathbf{\alpha}_{r}$是线性线性相关的。

$2 \rightarrow 1$：

向量族的秩：向量族$S$的极大无关组所含的向量个数，记作$R(S)$或$r(S)$或$rank(S)$。

矩阵的行秩和列秩：矩阵$\mathbf{A}_{m \times n}$的$m$个行向量称为$\mathbf{A}_{m \times n}$的行秩，$n$个列向量称为$\mathbf{A}_{m \times n}$的列秩。

矩阵的行秩与列秩相等。

向量组的秩和矩阵的秩的一些性质：

性质：设$A\text{，}B$是$V$中两组向量，$A$含有$r$个向量，$B$含有$s$个向量，且$A$中每个向量都能用$B$中向量线性表示。如果$A$中向量线性无关，则$r \leq s$。

证明：设

$A = \left\{ \mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{r} \right\}$

$B = \left\{ \mathbf{\beta}_{1}\text{，}\mathbf{\beta}_{2}\text{，}\cdots \text{，}\mathbf{\beta}_{r} \right\}$

因为$A$中每个向量都能用$B$中向量线性表示，所以当$r \leq s$时，可以把$B$中$r$个向量替换为$A$中向量的线性组合；而当$r > s$时，假设$B$中$k$个向量被$A$中向量的线性组合替换，则对于$A$中第$k + 1$个向量$\mathbf{\alpha}_{k + 1}$，有

$\mathbf{\alpha}_{k + 1} = \mu_{1}\mathbf{\alpha}_{1} + \cdots + u_{k}\mathbf{\alpha}_{k} + \mu_{k + 1}\mathbf{\beta}_{k + 1} + \cdots + \mu_{s}\mathbf{\beta}_{s}$

由$A$中向量线性无关，得$\mu_{k + 1}\text{，}\cdots \text{，}\mu_{s}$中至少有一个不为$0$，因此可以对$B$中剩下的向量接着做如上替换直到$B$中向量被全部替换，此时$A$中剩余的向量会被表示成$B$中向量即$A$中前$s$个向量的线性组合，产生了矛盾。所以$r \leq s$。

性质：如果两个向量组可以互相线性表示（称这两个向量组等价），则这两个向量组的秩相等。

证明：考虑这两个向量组的极大无关组，则这两个向量组可以互相线性表示等价为这两个极大无关组可以互相线性表示，由上面的性质易得这两个极大无关组的向量数量相等，再由向量组秩的定义得到原向量组的秩相等。

若$\mathbf{P}$可逆，则$r\left( \mathbf{A}\mathbf{P} \right) = r\left( \mathbf{P}\mathbf{A} \right) = r\left( \mathbf{A} \right)$

> $r\left( \mathbf{A} \right) + r\left( \mathbf{I} - \mathbf{A} \right) = r\left( \mathbf{A} - \mathbf{A}^{2} \right) + n$
>
> $r\left( k\mathbf{A} \right) = r\left( \mathbf{A} \right)\ \ \ (k \neq 0)$

$\left. \ \begin{array}{r} r\left( \mathbf{AB} \right) \leq \min\left\{ r\left( \mathbf{A} \right)\text{，}r\left( \mathbf{B} \right) \right\} \leq \max\left\{ r\left( \mathbf{A} \right)\text{，}r\left( \mathbf{B} \right) \right\} \leq \left\{ \begin{array}{r} r\begin{pmatrix} \mathbf{A} & \mathbf{B} \end{pmatrix} \\ r\begin{pmatrix} \mathbf{A} \\ \mathbf{B} \end{pmatrix} \end{array} \right\} \leq r\left( \mathbf{A + B} \right) \\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \left| r\left( \mathbf{A} \right) - r\left( \mathbf{B} \right) \right| \leq r\left( \mathbf{A} - \mathbf{B} \right) \end{array} \right\} \leq r\left( \mathbf{A} \right) + r\left( \mathbf{B} \right) = r\begin{pmatrix} \mathbf{A} & \mathbf{O} \\ \mathbf{O} & \mathbf{B} \end{pmatrix} \leq \left\{ \begin{array}{r} r\left( \mathbf{AB} \right) + n \\ r\begin{pmatrix} \mathbf{A} & \mathbf{C} \\ \mathbf{O} & \mathbf{B} \end{pmatrix} \\ r\begin{pmatrix} \mathbf{A} & \mathbf{O} \\ \mathbf{D} & \mathbf{B} \end{pmatrix} \end{array} \right.\$

线性方程组求解

克拉默法则

含有n个未知数的n个线性方程的方程组

$\left\{ \begin{array}{r} a_{11}x_{1} + a_{12}x_{2} + \cdots + a_{1n}x_{n} = b_{1} \\ a_{21}x_{1} + a_{22}x_{2} + \cdots + a_{2n}x_{n} = b_{2} \\ \cdots\cdots \\ a_{n1}x_{1} + a_{n2}x_{2} + \cdots + a_{nn}x_{n} = b_{n} \end{array} \right.\$

若其系数矩阵$A$的行列式不等于0，即

$\left| \mathbf{A} \right| = \left| \begin{matrix} a_{11} & \cdots & a_{1n} \\ \vdots & & \vdots \\ a_{n1} & \cdots & a_{nn} \end{matrix} \right| \neq 0$

那么，该方程组有唯一解

$x_{i} = \frac{\left| \mathbf{A}_{i} \right|}{\left| \mathbf{A} \right|}$

其中$\mathbf{A}_{i}$是把系数矩阵$\mathbf{A}$中第$i$列的元素用方程组右侧的常数项代替后所得到的n阶矩阵，即

$\begin{pmatrix} a_{11} & \cdots & a_{1,i - 1} & b_{1} & a_{1,i + 1} & \cdots & a_{1n} \\ \vdots & & \vdots & \vdots & \vdots & & \vdots \\ a_{n1} & \cdots & a_{n,i - 1} & b_{n} & a_{n,i + 1} & \cdots & a_{nn} \end{pmatrix}$

特别地，对于二元一次方程组

$\left\{ \begin{array}{r} a_{11}x + a_{12}y = b_{1} \\ a_{21}x + a_{22}y = b_{2} \end{array} \right.\$

有

$x = \frac{\left| \begin{matrix} b_{1} & a_{12} \\ b_{2} & a_{22} \end{matrix} \right|}{\left| \begin{matrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{matrix} \right|}\text{，}y = \frac{\left| \begin{matrix} a_{11} & b_{1} \\ a_{21} & b_{2} \end{matrix} \right|}{\left| \begin{matrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{matrix} \right|}$

证明：方程组的矩阵形式：

$\mathbf{Ax} = \mathbf{\beta}$

由$\left| \mathbf{A} \right| \neq 0$，得$\mathbf{A}^{- 1}$存在，所以

$\mathbf{A}^{- 1}\left( \mathbf{Ax} \right) = \mathbf{A}^{- 1}\mathbf{\beta}$

即

$\mathbf{x} = \mathbf{A}^{- 1}\mathbf{\beta}$

${\text{由}\mathbf{A}}^{- 1} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{*}\text{，得}$

$\begin{pmatrix} x_{1} \\ x_{2} \\ \vdots \\ x_{n} \end{pmatrix} = \frac{1}{\left| \mathbf{A} \right|}\begin{pmatrix} \mathbf{A}_{11} & \mathbf{A}_{21} & \cdots & \mathbf{A}_{n1} \\ \mathbf{A}_{12} & \mathbf{A}_{22} & \cdots & \mathbf{A}_{n2} \\ \vdots & \vdots & & \vdots \\ \mathbf{A}_{1n} & \mathbf{A}_{2n} & \cdots & \mathbf{A}_{nn} \end{pmatrix}\begin{pmatrix} b_{1} \\ b_{2} \\ \vdots \\ b_{n} \end{pmatrix}$

对于$x_{i}$，有

$x_{i} = \frac{1}{\left| \mathbf{A} \right|}\left( b_{1}\mathbf{A}_{1i} + b_{2}\mathbf{A}_{2i} + \cdots + b_{n}\mathbf{A}_{ni} \right)$

由行列式按列展开，$b_{1}\mathbf{A}_{1i} + b_{2}\mathbf{A}_{2i} + \cdots + b_{n}\mathbf{A}_{ni}$相当于$\left| \mathbf{A} \right|$把第$i$列替换为$\mathbf{\beta}$，即$\left| \mathbf{A}_{i} \right|$。故

$x_{i} = \frac{\left| \mathbf{A}_{i} \right|}{\left| \mathbf{A} \right|}$

初等变换

> 实际上是加减消元
>
> 1.对系数矩阵（$\mathbf{A}$）/增广矩阵（$\mathbf{B}$）施行初等行变换变为行最简型矩阵。
>
> 2.判断该行最简型矩阵的秩（它的秩为非$0$行的行数（非$0$子式的最高阶数））。
>
> 3.根据秩的情况得出方程组解的情况。
>
> 记系数矩阵和增广矩阵的秩分别为$R\left( \mathbf{A} \right)\text{，}R\left( \mathbf{B} \right)$，则

$\left\{ \begin{array}{r} R\left( \mathbf{A} \right) < R\left( \mathbf{B} \right)\text{，无解}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ R\left( \mathbf{A} \right) = R\left( \mathbf{B} \right) = n\text{，有唯一解}\ \ \ \ \  \\ R\left( \mathbf{A} \right) = R\left( \mathbf{B} \right) < n\text{，有无限多解} \end{array} \right.\$

> $eg.$求解齐次线性方程组

$\left\{ \begin{array}{r} \ \ x_{1} + 2x_{2} + 2x_{3} + x_{4} = 0 \\ 2x_{1} + x_{2} - 2x_{3} - 2x_{4} = 0 \\ \ \ x_{1} - x_{2} - 4x_{3} - 3x_{4} = 0 \end{array} \right.\$

> 对系数矩阵$\mathbf{A}$施行初等初等行变换变为行最简型矩阵

$\mathbf{A} = \begin{pmatrix} 1 & 2 & 2 & - 3 \\ 2 & 1 & - 2 & - 2 \\ 1 & - 1 & - 4 & 1 \end{pmatrix}\underset{r_{3} - r_{1}}{\overset{r_{2} - 2r_{1}}{\rightarrow}}\begin{pmatrix} 1 & 2 & 2 & 1 \\ 0 & - 3 & - 6 & - 4 \\ 0 & - 3 & - 6 & - 4 \end{pmatrix}\underset{r_{2} \times \left( - \frac{1}{3} \right)}{\overset{r_{3} - r_{2}}{\rightarrow}}\begin{pmatrix} 1 & 2 & 2 & 1 \\ 0 & 1 & 2 & \frac{4}{3} \\ 0 & 0 & 0 & 0 \end{pmatrix}\overset{r_{1} - 2r_{2}}{\rightarrow}\begin{pmatrix} 1 & 0 & - 2 & - \frac{5}{3} \\ 0 & 1 & 2 & \frac{4}{3} \\ 0 & 0 & 0 & 0 \end{pmatrix}$

> $R\left( \mathbf{A} \right) = 2 < 3$，有无数多解。
>
> 得到同解方程组

$\left\{ \begin{array}{r} x_{1} - 2x_{3} - \frac{5}{3}x_{4} = 0 \\ x_{2} + 2x_{3} + \frac{4}{3}x_{4} = 0 \end{array} \right.\$

> 得

$\left\{ \begin{array}{r} x_{1} = \ \ \ 2x_{3} + \frac{5}{3}x_{4} \\ x_{2} = - 2x_{3} - \frac{4}{3}x_{4} \end{array} \right.\ \text{其中}x_{3}\text{，}x_{4}\text{可取任意值。}$

> 或得到对应齐次线性方程组的基础解系
>
> $\mathbf{\xi}_{1} = \begin{pmatrix} 2 \\ - 2 \\ 1 \end{pmatrix}$
>
> 和原方程组的特解
>
> $\mathbf{\gamma} = \begin{pmatrix} - \frac{5}{3} \\ \frac{4}{3} \\ 0 \end{pmatrix}$
>
> 写出通解
>
> $\mathbf{x} = \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \end{pmatrix} = c_{1}\mathbf{\xi}_{1} + \mathbf{\gamma =}c_{1}\begin{pmatrix} 2 \\ - 2 \\ 1 \end{pmatrix} + \begin{pmatrix} - \frac{5}{3} \\ \frac{4}{3} \\ 0 \end{pmatrix}$
>
> $eg.$求解非齐次线性方程组

$\left\{ \begin{array}{r} \ \ \ x_{1} + \ \ x_{2} - 3x_{3} - \ \ x_{4} = 1 \\ 3x_{1} - \ \ x_{2} - 3x_{3} + 4x_{4} = 4 \\ \ \ x_{1} + 5x_{3} - 9x_{3} - 8x_{4} = 0 \end{array} \right.\$

> 对增广矩阵$B$施行初等行变换

$\mathbf{B} = \begin{pmatrix} 1 & 1 & - 3 & - 1 & 1 \\ 3 & - 1 & - 3 & 4 & 4 \\ 1 & 5 & - 9 & - 8 & 0 \end{pmatrix}\underset{r_{3} - r_{1}}{\overset{r_{2} - 3r_{1}}{\rightarrow}}\begin{pmatrix} 1 & 1 & - 3 & - 1 & 1 \\ 0 & - 4 & 6 & 7 & 1 \\ 0 & 4 & - 6 & - 7 & - 1 \end{pmatrix}$

$\underset{r_{2} - 4}{\overset{r_{3} + r_{2}}{\rightarrow}}\begin{pmatrix} 1 & 1 & - 3 & - 1 & 1 \\ 0 & 1 & - \frac{3}{2} & - \frac{7}{4} & - \frac{1}{4} \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}\overset{r_{1} - r_{2}}{\rightarrow}\begin{pmatrix} 1 & 0 & - \frac{3}{2} & 0 & \frac{5}{4} \\ 0 & 1 & - \frac{3}{2} & - \frac{7}{4} & - \frac{1}{4} \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$

> $R\left( \mathbf{A} \right) = R\left( \mathbf{B} \right) = 2 < 3$，有无数多解。
>
> 得
>
> $\left\{ \begin{array}{r} x_{1} = \frac{3}{2}x_{3} - \frac{3}{4}x_{4} + \frac{5}{4} \\ x_{2} = \frac{3}{2}x_{3} + \frac{7}{4}x_{4} - \frac{1}{4} \\ x_{3} = x_{3}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ x_{4} = x_{4}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$
>
> 或有基础解系和特解
>
> $\mathbf{\xi}_{1} = \begin{pmatrix} \frac{3}{2} \\ \frac{3}{2} \\ 1 \\ 0 \end{pmatrix}\text{，}\mathbf{\xi}_{2} = \begin{pmatrix} 0 \\ - \frac{7}{4} \\ 0 \\ 1 \end{pmatrix}\text{，}\mathbf{\gamma} = \begin{pmatrix} \frac{5}{4} \\ - \frac{1}{4} \\ 0 \\ 0 \end{pmatrix}$
>
> 得到通解
>
> $\mathbf{x} = \begin{pmatrix} x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \end{pmatrix} = c_{1}\mathbf{\xi}_{1} + c_{2}\xi_{2} + \mathbf{\gamma =}c_{1}\begin{pmatrix} \frac{3}{2} \\ \frac{3}{2} \\ 1 \\ 0 \end{pmatrix} + c_{2}\begin{pmatrix} 0 \\ - \frac{7}{4} \\ 0 \\ 1 \end{pmatrix} + \begin{pmatrix} - \frac{5}{3} \\ \frac{4}{3} \\ 0 \end{pmatrix}$
>
> $eg.$求解非齐次线性方程组

$\left\{ \begin{array}{r} \ \ x_{1} - 2x_{2} + 3x_{3} - \ \ x_{4} = 1 \\ 3x_{1} - \ \ x_{2} + 5x_{3} - 3x_{4} = 2 \\ 2x_{1} + \ \ x_{2} + 2x_{3} - 2x_{4} = 3 \end{array} \right.\$

> 对增广矩阵$\mathbf{B}$施行初等行变换

$\mathbf{B} = \begin{pmatrix} 1 & - 2 & 3 & - 1 & 1 \\ 3 & - 1 & 5 & - 3 & 2 \\ 2 & 1 & 2 & - 2 & 3 \end{pmatrix}\underset{r_{3} - r_{1}}{\overset{r_{2} - 3r_{1}}{\rightarrow}}\begin{pmatrix} 1 & - 2 & 3 & - 1 & 1 \\ 0 & 5 & - 4 & 0 & - 1 \\ 0 & 5 & - 4 & 0 & 1 \end{pmatrix}\overset{r_{3} - r_{2}}{\rightarrow}\begin{pmatrix} 1 & - 2 & 3 & - 1 & 1 \\ 0 & 5 & - 4 & 0 & - 1 \\ 0 & 0 & 0 & 0 & 2 \end{pmatrix}$

> $R\left( \mathbf{A} \right) = 2 < R\left( \mathbf{B} \right) = 3$，方程组无解。

多项式

多项式

对于多项式

$f(x) = a_{n}x^{n} + a_{n - 1}x^{n - 1} + \cdots + a_{1}x + a_{0}$

$g(x) = b_{m}x^{m} + b_{m - 1}x^{m - 1} + \cdots + b_{1}x + b_{0}$

其中$m \neq n$，补全相差的项使$g(x)$类同于$f(x)$，定义

加法：$f(x) + g(x) = \left( a_{n} + b_{n} \right)x^{n} + \left( a_{n - 1} + b_{n - 1} \right)x^{n - 1} + \cdots + \left( a_{1} + b_{1} \right)x + \left( a_{0} + b_{0} \right)$

数乘：$cf(x) = ca_{n}x^{n} + ca_{n - 1}x^{n - 1} + \cdots + ca_{1}x + ca_{0}$

此时多项式可构成线性空间。

乘积：$h(x) = f(x) \cdot g(x) = f(x)g(x) = c_{n + m}x^{n + m} + c_{n + m - 1}x^{n + m - 1} + \cdots + c_{1}x + c_{0}$

其中

$c_{k} = \sum_{i + j = k}^{}{a_{i}b_{j}} = a_{0}b_{k} + a_{1}b_{k - 1} + \cdots + a_{k - 1}b_{1} + a_{k}b_{0}$

定义$f(x)$的次数为$\deg{f(x)}$，即$\deg{f(x)} = n$，则有

$(1)\deg\left( f(x)g(x) \right) = \deg{f(x)} + \deg{g(x)}$

$(2)\deg\left( cf(x) \right) = \deg{f(x)}$

$(3)\deg\left( f(x) + g(x) \right) \leq \max\left\{ \deg{f(x)}\text{，}\deg{g(x)} \right\}$（最高次项正负抵消）

整除：对于$f(x)$和$g(x)$，若存在$h(x)$，满足

$f(x) = g(x)h(x)$

则称$g(x)$为$f(x)$的因式，$g(x)$可以整除$f(x)$，$f(x)$可以被$g(x)$整除，记作

$g(x)\ \text{|}\ f(x)$

否则，记作

$g(x) \nmid f(x)$

整除的性质

$(4)\text{若}f(x)\ \text{|}\ \ g(x)\text{，则}\ cf(x)\ \text{|}\ g(x)$，因此非零常数多项式c是任一非零多项式的因式。

证：设$g(x) = f(x)p(x)$，则$g(x) = \left( cf(x) \right)\left( c^{- 1}p(x) \right)$，所以$cf(x)\ \text{|}\ g(x)$

$(5)f(x)\ \text{|}\ f(x)$

$(6)\text{（传递性）若}f(x)\ \text{|}\ \ g(x)\text{，}g(x)\ \text{|}\ h(x)\text{，则}f(x)\ \text{|}\ \ h(x)$

证：设$g(x) = f(x)p(x)\text{，}h(x) = g(x)q(x)\text{，}$则

$h(x) = \left( f(x)p(x) \right)q(x) = f(x)\left( p(x)q(x) \right)$

$(7)\text{（线性组合）若}f(x)\ \text{|}\ \ g(x)\text{，}f(x)\ \text{|}\ h(x)\text{，则对于任意的多项式}u(x)\text{，}v(x)\text{，有}$

$f(x)\ \text{|}\ \ g(x)u(x) + h(x)v(x)$

证：设$g(x) = f(x)p(x)\text{，}h(x) = g(x)q(x)\text{，}$则

$g(x)u(x) + h(x)v(x) = f(x)\left( p(x)u(x) + q(x)v(x) \right)$

$(8)$设$f(x)\ \text{|}\ \ g(x)\text{，}g(x)\ \text{|}\ f(x)\$且$f(x)\text{，}g(x)$都是非零多项式，则存在非零元$c$，使

$f(x) = cg(x)$

称$f(x)\text{，}g(x)$为相伴多项式，记为$f(x)\sim g(x)$

证：设$g(x) = f(x)p(x)\text{，}f(x) = g(x)q(x)\text{，}$则

$f(x) = f(x)\left( p(x)q(x) \right)$

所以

$\deg{f(x)} = \deg{f(x)} + \deg\left( p(x)q(x) \right)$

所以

$\deg\left( p(x)q(x) \right) = 0$

所以

$\deg{p(x)} = \deg{q(x)} = 0$

因此$p(x)$和$q(x)$均为非零常数多项式，即$f(x)$和$g(x)$相差一个非零常数。

$(9)$（多项式带余除法唯一性）设$g(x) \neq 0$，则一定存在唯一的$q(x)\text{，}r(x)$，使得

$f(x) = g(x)q(x) + r(x)$

且$\deg{r(x)} < \deg{g(x)}$

证：若$\deg{f(x)} < \deg{g(x)}$，只需令$q(x) = 0$，$r(x) = f(x)$即可。

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

$\left( \mathbf{AB} \right)' = \mathbf{B}'\mathbf{A}'$

转置

</th>
<th>

$\left( \mathbf{AB} \right)^{k}$

$k$次幂

</th>
<th>

$\left( \mathbf{AB} \right)^{*} = \mathbf{B}^{*}\mathbf{A}^{*}$

伴随矩阵

</th>
<th>

$\left( \mathbf{AB} \right)^{- 1} = \mathbf{B}^{- 1}\mathbf{A}^{- 1}$

逆矩阵

</th>
<th>

$\left| \mathbf{AB} \right| = \left| \mathbf{A} \right|\left| \mathbf{B} \right|$

行列式

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\left( \mathbf{AB} \right)' = \mathbf{B}'\mathbf{A}'$

转置

</td>
<td>

$\mathbf{A}^{''} = \mathbf{A}$

</td>
<td>

$\left( \mathbf{A}' \right)^{k} = \left( \mathbf{A}^{k} \right)'$

</td>
<td>

$\left( \mathbf{A}' \right)^{*} = \left( \mathbf{A}^{*} \right)'$

</td>
<td>

$\left( \mathbf{A}' \right)^{- 1} = \left( \mathbf{A}^{- 1} \right)'$

</td>
<td>

$\left| \mathbf{A}' \right| = \left| \mathbf{A} \right|$

</td>
</tr>
<tr>
<td>

$\left( \mathbf{AB} \right)^{k}$

$k$次幂

</td>
<td>

$\left( \mathbf{A}^{k} \right)' = \left( \mathbf{A}' \right)^{k}$

</td>
<td>

$\left( \mathbf{A}^{k} \right)^{t} = \mathbf{A}^{kt}$

</td>
<td>

$\left( \mathbf{A}^{k} \right)^{*} = \left( \mathbf{A}^{*} \right)^{k}$

</td>
<td>

$\left( \mathbf{A}^{k} \right)^{- 1} = \left( \mathbf{A}^{- 1} \right)^{k}$

</td>
<td>

$\left| \mathbf{A}^{k} \right| = \left| \mathbf{A} \right|^{k}$

</td>
</tr>
<tr>
<td>

$\left( \mathbf{AB} \right)^{*} = \mathbf{B}^{*}\mathbf{A}^{*}$

伴随矩阵

</td>
<td>

$\left( \mathbf{A}^{*} \right)' = \left( \mathbf{A}' \right)^{*}$

</td>
<td>

$\left( \mathbf{A}^{*} \right)^{k} = \left( \mathbf{A}^{k} \right)^{*}$

</td>
<td>

$\mathbf{A}\mathbf{A}^{*} = \mathbf{A}^{*}\mathbf{A =}\left| \mathbf{A} \right|\mathbf{E}$

$\left( \mathbf{A}^{*} \right)^{*} = \left| \mathbf{A} \right|^{n - 2}\mathbf{A}$

</td>
<td>

$\mathbf{A}^{\mathbf{*}} = \left| \mathbf{A} \right|\mathbf{A}^{- 1}$

$\left( \mathbf{A}^{*} \right)^{- 1} = \left( \mathbf{A}^{- 1} \right)^{*}$

$= \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}$

</td>
<td>

$\left| \mathbf{A}^{*} \right| = \left| \mathbf{A} \right|^{n - 1}$

</td>
</tr>
<tr>
<td>

$\left( \mathbf{AB} \right)^{- 1} = \mathbf{B}^{- 1}\mathbf{A}^{- 1}$

逆矩阵

</td>
<td>

$\left( \mathbf{A}^{- 1} \right)' = \left( \mathbf{A}' \right)^{- 1}$

</td>
<td>

$\left( \mathbf{A}^{- 1} \right)^{k} = \left( \mathbf{A}^{k} \right)^{- 1}$

</td>
<td>

$\mathbf{A}^{- 1} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{\mathbf{*}}$

$\left( \mathbf{A}^{- 1} \right)^{*} = \left( \mathbf{A}^{*} \right)^{- 1}$

$= \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}$

</td>
<td>

$\left( \mathbf{A}^{- 1} \right)^{- 1} = \mathbf{A}$

</td>
<td>

$\left| \mathbf{A}^{- 1} \right| = \left| \mathbf{A} \right|^{- 1}$

</td>
</tr>
<tr>
<td>

$\left| \mathbf{AB} \right| = \left| \mathbf{A} \right|\left| \mathbf{B} \right|$

行列式

</td>
<td>

$\left| \mathbf{A} \right| = \left| \mathbf{A}' \right|$

</td>
<td>

$\left| \mathbf{A} \right|^{k} = \left| \mathbf{A}^{k} \right|$

</td>
<td>

$\left| \mathbf{A} \right|^{n - 1} = \left| \mathbf{A}^{*} \right|$

</td>
<td>

$\left| \mathbf{A} \right|^{- 1} = \left| \mathbf{A}^{- 1} \right|$

</td>
<td>

$\left| \mathbf{AB} \right| = \left| \mathbf{BA} \right|$

</td>
</tr>
</tbody>
</table>
</div>
