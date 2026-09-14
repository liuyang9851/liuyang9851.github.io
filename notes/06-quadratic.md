---
title: 二次型理论
description: 二次型的矩阵表示、标准型与规范型、惯性定理、正定性判定、施密特正交化。
---

# 06 · 二次型理论

[[toc]]

二次型：n个变量的一个二次齐次多项式（函数）

$$f\left( x_{1}x_{2}\cdots x_{n} \right) = a_{11}x_{1}^{2} + 2a_{12}x_{1}x_{2} + 2a_{13}x_{1}x_{3} + \cdots + 2a_{1n}x_{1}x_{n}$$

$$\ \ \  + a_{22}x_{2}^{2} + 2a_{23}x_{2}x_{3} + \cdots + 2a_{2n}x_{2}x_{n}$$

$$+ \cdots\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$

$$+ a_{nn}x_{n}^{2}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ $$

标准型：$a_{ij} = 0\ \ (i \neq j)$

规范型：$a_{ii} = \pm 1$的标准型

二次型可表示为形如$\mathbf{x}^{\mathbf{'}}\mathbf{Ax}$的形式（$\mathbf{A}$不一定为对称阵），称$\mathbf{A}$为相伴矩阵或系数矩阵。特别地，若$\mathbf{A}$为对称阵，则称$\mathbf{A}$为二次型$f$的矩阵。（二次型矩阵为对称阵）

$$\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{12} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & \ddots & \vdots \\
a_{1n} & a_{2n} & \cdots & a_{nn}
\end{pmatrix}$$

定理：当$\mathbf{A}$为对称阵时，$\mathbf{A}$唯一。

定理：同一个二次型经不同的坐标变换后得到的不同的二次型矩阵合同。

由二次型矩阵是对称阵，还有

定理：二次型矩阵必相似且合同于某对角阵（规范型）。

惯性定理：二次型的规范型中的正数数量（正惯性指数）与负数数量（负惯性指数）是确定的。

定理：正定二次型$\Leftrightarrow$正惯性指数为$n$（$\Leftrightarrow$负惯性指数为0）。

（负定二次型$\Leftrightarrow$负惯性指数为$n$，半正定二次型$\Leftrightarrow$正惯性指数等于二次型的秩，半负定二次型$\Leftrightarrow$负惯性指数等于二次型的秩）

$$二次型f正定 \Leftrightarrow \left\{ \begin{array}{r}
\forall\mathbf{x} \neq \mathbf{0}\text{，}\mathbf{x}^{\mathbf{'}}\mathbf{Ax} > 0\ \ (定义) \\
\mathbf{A}是正定矩阵\ \ (定义)\ \ \ \ \ \ \ \ \ \ \  \\
标准型的系数全正\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
f的正惯性指数为n\ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\mathbf{A}合同于\mathbf{I}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\mathbf{A}\mathbf{=}\mathbf{D}^{\mathbf{'}}\mathbf{D}\text{，}其中\mathbf{D}是可逆阵 \\
\mathbf{A}的特征值全正\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\mathbf{A}的顺序主子式全正\ \ \ \ \ \ \ \ \ \ \ \ \
\end{array} \right.\ $$

$$二次型f正定 \Rightarrow \left\{ \begin{array}{r}
\mathbf{A}的主对角线元素全正 \\
\left| \mathbf{A} \right| > 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\mathbf{A}'正定\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\mathbf{A}^{k}正定\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\mathbf{A}^{*}正定\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\mathbf{A}^{- 1}正定\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
\end{array} \right.\ $$

二次型还有如下结论：

对称阵$\mathbf{A}$负定$\Leftrightarrow$奇数阶主子式为负，偶数阶主子式为正。

若$\mathbf{A}$，$\mathbf{B}$为正定矩阵，则$\mathbf{A} + \mathbf{B}$也是正定矩阵。（若$\mathbf{A}$，$\mathbf{B}$为半正定矩阵，则$\mathbf{A} + \mathbf{B}$也是半正定矩阵）

### 施密特正交化

$$b_{r} = a_{r} - \sum_{i = 1}^{r - 1}{\frac{\left\lbrack b_{i}\text{，}a_{r} \right\rbrack}{\left\lbrack b_{i}\text{，}b_{i} \right\rbrack}b_{i}}$$

$$你_{r} = 我_{r} - \sum_{i = 1}^{r - 1}{\frac{\left\lbrack 你_{i}\text{，}我_{r} \right\rbrack}{\left\lbrack 你_{i}\text{，}你_{i} \right\rbrack}你_{i}}$$

### 向量

$$\mathbf{x} = \begin{pmatrix}
x_{1} \\
x_{2} \\
 \vdots \\
x_{n}
\end{pmatrix} = x_{1}\mathbf{e}_{1} + x_{2}\mathbf{e}_{2} + \cdots + x_{n}\mathbf{e}_{n}$$

其中$x_{i}$表示第$i$个分量的大小，也可以看成对对应基向量的缩放。

### 向量加法与数乘

$$\mathbf{x} + \mathbf{y} = \begin{pmatrix}
x_{1} + y_{1} \\
x_{2} + y_{2} \\
 \vdots \\
x_{n} + y_{n}
\end{pmatrix},\ \ k\mathbf{x} = \begin{pmatrix}
kx_{1} \\
kx_{2} \\
 \vdots \\
kx_{n}
\end{pmatrix}$$

### 矩阵

$$\mathbf{A}_{m \times n} = \begin{pmatrix}
\mathbf{a}_{1} & \mathbf{a}_{2} & \cdots & \mathbf{a}_{n}
\end{pmatrix} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}$$

在线性变换中，矩阵的每一列对应第$j$个基向量被变换后在原坐标系中的位置。

### 矩阵与向量相乘

$$\mathbf{A}_{m \times n}\mathbf{x} = x_{1}\mathbf{a}_{\mathbf{1}} + x_{2}\mathbf{a}_{\mathbf{2}} + \cdots + x_{n}\mathbf{a}_{\mathbf{n}} = \begin{pmatrix}
a_{11}x_{1} \\
a_{21}x_{2} \\
 \vdots \\
a_{m1}x_{n}
\end{pmatrix} + \begin{pmatrix}
a_{12}x_{1} \\
a_{22}x_{2} \\
 \vdots \\
a_{m2}x_{n}
\end{pmatrix} + \cdots + \begin{pmatrix}
a_{1n}x_{1} \\
a_{2n}x_{2} \\
 \vdots \\
a_{mn}x_{n}
\end{pmatrix} = \begin{pmatrix}
a_{11}x_{1} + a_{12}x_{1} + \cdots + a_{1n}x_{1} \\
a_{21}x_{2} + a_{22}x_{2} + \cdots + a_{2n}x_{2} \\
 \vdots \\
a_{m1}x_{n} + a_{m2}x_{n} + \cdots a_{mn}x_{n}
\end{pmatrix}$$

矩阵与向量相乘得到的结果是对向量做线性变换后在原坐标系中的位置。

### 矩阵乘法

$$\mathbf{A}_{m \times p}\mathbf{B}_{p \times n} = \begin{pmatrix}
\mathbf{A}\mathbf{b}_{1} & \mathbf{A}\mathbf{b}_{2} & \cdots & \mathbf{A}\mathbf{b}_{n}
\end{pmatrix} =$$

$$\begin{pmatrix}
\begin{pmatrix}
a_{11}b_{11} + a_{12}b_{21} + \cdots + a_{1p}b_{p1} \\
a_{21}b_{11} + a_{22}b_{21} + \cdots + a_{2p}b_{p1} \\
 \vdots \\
a_{m1}b_{11} + a_{m2}b_{21} + \cdots a_{mp}b_{p1}
\end{pmatrix} & \begin{pmatrix}
a_{11}b_{12} + a_{12}b_{22} + \cdots + a_{1p}b_{p2} \\
a_{21}b_{12} + a_{22}b_{22} + \cdots + a_{2p}b_{p2} \\
 \vdots \\
a_{m1}b_{12} + a_{m2}b_{22} + \cdots a_{mp}b_{p2}
\end{pmatrix} & \cdots & \begin{pmatrix}
a_{11}b_{1n} + a_{12}x_{1} + \cdots + a_{1p}x_{1} \\
a_{21}b_{1n} + a_{22}x_{2} + \cdots + a_{2p}x_{2} \\
 \vdots \\
a_{m1}b_{1n} + a_{m2}b\_ + \cdots a_{mp}b_{pn}
\end{pmatrix}
\end{pmatrix}$$

矩阵乘法是对把右边的变换与左边的变换复合，先做右边的变换，再做左边的变换。得到的一次性变换为对右边变换的的每个分量做左边变化后拼成的矩阵。

### 矩阵的秩

矩阵的秩描述矩阵对应的线性变换得到的空间的维数。标准基向量经线性变换后能张成的空间的维数。矩阵既可以看成行向量的组合又可以看成列向量的组合，因此矩阵的秩小于m或n，
