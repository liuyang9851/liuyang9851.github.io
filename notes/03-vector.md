---
title: 向量与线性空间
description: 线性相关与线性无关的判定、极大无关组、向量组和矩阵的秩。
---

# 03 · 向量与线性空间

[[toc]]

定理：只含一个向量$\mathbf{\alpha}$的向量组线性相关的充要条件为$\mathbf{\alpha} = \mathbf{0}$

定理：若向量组$S$含有零向量，则$S$线性相关。

定理：若$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$是一组线性相关的向量，则任一包含这组向量的向量组线性相关。

定理：若$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$是一组线性无关的向量，则从这一组向量中任意取出一组向量线性无关。

定理：向量$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性相关的充要条件是其中至少有一个向量可以表示成其余向量的线性组合。

定理：设$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}\text{，}\mathbf{\beta}$是线性空间$V$中的向量，且$\mathbf{\beta}$可表示为$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$的线性组合，即$\mathbf{\beta} = k_{1}\mathbf{\alpha}_{1} + k_{2}\mathbf{\alpha}_{2} + \cdots k_{n}\mathbf{\alpha}_{n}$，则这种线性表示唯一的充要条件是$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性无关。

定理：设向量组$A\text{，}B\text{，}C$满足：$A$中任一向量都是$B$中向量的线性组合，$B$中任一向量都是$C$中向量的线性组合，则$A$中任一向量都是$C$中向量的线性组合。

定理：若

$$\mathbf{\alpha =}\left( a_{1}\text{，}a_{2}\text{，}\cdots \text{，}a_{n} \right)\text{，}\mathbf{\beta =}\left( b_{1}\text{，}b_{2}\text{，}\cdots \text{，}b_{n} \right)$$

是两个$n$维行向量，则$\mathbf{\alpha}\text{，}\mathbf{\beta}$线性相关的充要条件是$a_{i}\text{，}b_{i}$成比例。

性质：设$\mathbf{\alpha\beta}$为相同维数的列向量，则$\mathbf{\alpha}^{\mathbf{'}}\mathbf{\beta =}\mathbf{\beta}^{\mathbf{'}}\mathbf{\alpha}$，特别地，$\mathbf{\alpha}'\mathbf{\alpha} = \sum_{}^{}a_{i}$

## 向量组和矩阵的秩

极/最大（线性）无关组：有两个等价定义

定义1：在线性空间$V$中，若在向量族$S$中存在一组向量$\left\{ \mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n} \right\}$满足

（1）$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性无关；

（2）$S$中任意一个向量都可以由$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性表示。

定义2：在线性空间$V$中，若在向量族$S$中存在一组向量$\left\{ \mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n} \right\}$满足

（1）$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n}$线性无关；

（2）如果$S$中向量个数大于$n$，则任意$n + 1$个向量线性相关。

则称$\left\{ \mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{n} \right\}$是向量族的极/最大线性无关组，简称极/最大无关组。

定理：矩阵的行秩与列秩相等。

定理：设$A\text{，}B$是$V$中两组向量，$A$含有$r$个向量，$B$含有$s$个向量，且$A$中每个向量都能用$B$中向量线性表示。如果$A$中向量线性无关，则$r \leq s$。

定理：如果两个向量组可以互相线性表示（称这两个向量组等价），则这两个向量组的秩相等。

矩阵的秩有以下结论：

$$r\left( k\mathbf{A} \right) = r\left( \mathbf{A} \right)\ \ \ (k \neq 0)$$

$$r\left( \mathbf{A}^{\mathbf{'}}\mathbf{A} \right) = r\left( \mathbf{A} \right)$$

若$\mathbf{P}$可逆，则$r\left( \mathbf{AP} \right) = r\left( \mathbf{PA} \right) = r\left( \mathbf{A} \right)$

$$r\left( \mathbf{A} \right) + r\left( \mathbf{I} - \mathbf{A} \right) = r\left( \mathbf{A} - \mathbf{A}^{2} \right) + n$$

$$r\begin{pmatrix}
\mathbf{A}_{n \times n} & \mathbf{A}\mathbf{B}_{n \times n}
\end{pmatrix} = r\left( \mathbf{A} \right)$$

$$\left. \ \begin{array}{r}
r\left( \mathbf{AB} \right) \leq \min\left\{ r\left( \mathbf{A} \right)\text{，}r\left( \mathbf{B} \right) \right\} \leq \left\{ \begin{array}{r}
r\left( \mathbf{A} \right) \\
r\left( \mathbf{B} \right)
\end{array} \right\} \leq \max\left\{ r\left( \mathbf{A} \right)\text{，}r\left( \mathbf{B} \right) \right\} \leq \left\{ \begin{array}{r}
r\begin{pmatrix}
\mathbf{A} & \mathbf{B}
\end{pmatrix} \\
r\begin{pmatrix}
\mathbf{A} \\
\mathbf{B}
\end{pmatrix}
\end{array} \right\} \\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ r\left( \mathbf{A + B} \right) \\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \left| r\left( \mathbf{A} \right) - r\left( \mathbf{B} \right) \right| \leq r\left( \mathbf{A} - \mathbf{B} \right)
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

上式的等号成立的条件不完全相同且复杂。

$$若方阵r\left( \mathbf{A} \right) = 1\text{，}则\mathbf{A}^{n} = \sum_{}^{}a_{ii}\mathbf{A}$$
