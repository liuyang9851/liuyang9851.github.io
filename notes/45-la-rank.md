---
title: 向量组与矩阵的秩
description: 极大线性无关组的两个等价定义、向量组的秩与矩阵的秩。
---

# 向量组与矩阵的秩

[[toc]]

向量组和矩阵的秩

极/最大（线性）无关组：有两个等价定义

定义1：在线性空间V中，若在向量族S中存在一组向量\{α1，α2，⋯，αn\}满足

（1）α1，α2，⋯，αn线性无关；

（2）S中任意一个向量都可以由α1，α2，⋯，αn线性表示。

则称\{α1，α2，⋯，αn\}是向量族的极/最大线性无关组，简称极/最大无关组。

定义2：在线性空间V中，若在向量族S中存在一组向量\{α1，α2，⋯，αn\}满足

（1）α1，α2，⋯，αn线性无关；

（2）如果S中向量个数大于n，则任意n + 1个向量线性相关。

则称\{α1，α2，⋯，αn\}是向量族的极/最大线性无关组，简称极/最大无关组。

证明：

1 → 2：设对于S中任一向量αr，有

αr = a1α1 + a2α2 + ⋯anαn

则由线性相关的定义，容易看出向量α1，α2，⋯，αn，αr是线性线性相关的。

2 → 1：

向量族的秩：向量族S的极大无关组所含的向量个数，记作R(S)或r(S)或rank(S)。

矩阵的行秩和列秩：矩阵Am × n的m个行向量称为Am × n的行秩，n个列向量称为Am × n的列秩。

矩阵的行秩与列秩相等。

向量组的秩和矩阵的秩的一些性质：

性质：设A，B是V中两组向量，A含有r个向量，B含有s个向量，且A中每个向量都能用B中向量线性表示。如果A中向量线性无关，则r ≤ s。

证明：设

A = \{α1，α2，⋯，αr\}

B = \{β1，β2，⋯，βr\}

因为A中每个向量都能用B中向量线性表示，所以当r ≤ s时，可以把B中r个向量替换为A中向量的线性组合；而当r > s时，假设B中k个向量被A中向量的线性组合替换，则对于A中第k + 1个向量αk + 1，有

αk + 1 = μ1α1 + ⋯ + ukαk + μk + 1βk + 1 + ⋯ + μsβs

由A中向量线性无关，得μk + 1，⋯，μs中至少有一个不为0，因此可以对B中剩下的向量接着做如上替换直到B中向量被全部替换，此时A中剩余的向量会被表示成B中向量即A中前s个向量的线性组合，产生了矛盾。所以r ≤ s。

性质：如果两个向量组可以互相线性表示（称这两个向量组等价），则这两个向量组的秩相等。

证明：考虑这两个向量组的极大无关组，则这两个向量组可以互相线性表示等价为这两个极大无关组可以互相线性表示，由上面的性质易得这两个极大无关组的向量数量相等，再由向量组秩的定义得到原向量组的秩相等。

若P可逆，则r(AP) = r(PA) = r(A)

r(A) + r(I − A) = r(A − A2) + n

r(kA) = r(A)   (k ≠ 0)

$$\left. \ \begin{array}{r}
r\left( \mathbf{AB} \right) \leq \min\left\{ r\left( \mathbf{A} \right)\text{，}r\left( \mathbf{B} \right) \right\} \leq \max\left\{ r\left( \mathbf{A} \right)\text{，}r\left( \mathbf{B} \right) \right\} \leq \left\{ \begin{array}{r}
r\begin{pmatrix}
\mathbf{A} & \mathbf{B}
\end{pmatrix} \\
r\begin{pmatrix}
\mathbf{A} \\
\mathbf{B}
\end{pmatrix}
\end{array} \right\} \leq r\left( \mathbf{A + B} \right) \\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \left| r\left( \mathbf{A} \right) - r\left( \mathbf{B} \right) \right| \leq r\left( \mathbf{A} - \mathbf{B} \right)
\end{array} \right\} \leq r\left( \mathbf{A} \right) + r\left( \mathbf{B} \right) = r\begin{pmatrix}
\mathbf{A} & \mathbf{O} \\
\mathbf{O} & \mathbf{B}
\end{pmatrix} \leq \left\{ \begin{array}{r}
r\left( \mathbf{AB} \right) + n \\
r\begin{pmatrix}
\mathbf{A} & \mathbf{C} \\
\mathbf{O} & \mathbf{B}
\end{pmatrix} \\
r\begin{pmatrix}
\mathbf{A} & \mathbf{O} \\
\mathbf{D} & \mathbf{B}
\end{pmatrix}
\end{array} \right.\ $$
