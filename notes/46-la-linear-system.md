---
title: 线性方程组求解
description: 克拉默法则、齐次与非齐次方程组的解的结构、初等变换法解方程组。
---

# 线性方程组求解

[[toc]]

线性方程组求解

克拉默法则

含有n个未知数的n个线性方程的方程组

$$\left\{ \begin{array}{r}
a_{11}x_{1} + a_{12}x_{2} + \cdots + a_{1n}x_{n} = b_{1} \\
a_{21}x_{1} + a_{22}x_{2} + \cdots + a_{2n}x_{n} = b_{2} \\
\cdots\cdots \\
a_{n1}x_{1} + a_{n2}x_{2} + \cdots + a_{nn}x_{n} = b_{n}
\end{array} \right.\ $$

若其系数矩阵A的行列式不等于0，即

$$\left| \mathbf{A} \right| = \left| \begin{matrix}
a_{11} & \cdots & a_{1n} \\
 \vdots & & \vdots \\
a_{n1} & \cdots & a_{nn}
\end{matrix} \right| \neq 0$$

那么，该方程组有唯一解

$$x_{i} = \frac{\left| \mathbf{A}_{i} \right|}{\left| \mathbf{A} \right|}$$

其中Ai是把系数矩阵A中第i列的元素用方程组右侧的常数项代替后所得到的n阶矩阵，即

$$\begin{pmatrix}
a_{11} & \cdots & a_{1,i - 1} & b_{1} & a_{1,i + 1} & \cdots & a_{1n} \\
 \vdots & & \vdots & \vdots & \vdots & & \vdots \\
a_{n1} & \cdots & a_{n,i - 1} & b_{n} & a_{n,i + 1} & \cdots & a_{nn}
\end{pmatrix}$$

特别地，对于二元一次方程组

$$\left\{ \begin{array}{r}
a_{11}x + a_{12}y = b_{1} \\
a_{21}x + a_{22}y = b_{2}
\end{array} \right.\ $$

有

$$x = \frac{\left| \begin{matrix}
b_{1} & a_{12} \\
b_{2} & a_{22}
\end{matrix} \right|}{\left| \begin{matrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{matrix} \right|}\text{，}y = \frac{\left| \begin{matrix}
a_{11} & b_{1} \\
a_{21} & b_{2}
\end{matrix} \right|}{\left| \begin{matrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{matrix} \right|}$$

证明：方程组的矩阵形式：

Ax = β

由|A| ≠ 0，得A−1存在，所以

A−1(Ax) = A−1β

即

x = A−1β

$${\text{由}\mathbf{A}}^{- 1} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{*}\text{，得}$$

$$\begin{pmatrix}
x_{1} \\
x_{2} \\
 \vdots \\
x_{n}
\end{pmatrix} = \frac{1}{\left| \mathbf{A} \right|}\begin{pmatrix}
\mathbf{A}_{11} & \mathbf{A}_{21} & \cdots & \mathbf{A}_{n1} \\
\mathbf{A}_{12} & \mathbf{A}_{22} & \cdots & \mathbf{A}_{n2} \\
 \vdots & \vdots & & \vdots \\
\mathbf{A}_{1n} & \mathbf{A}_{2n} & \cdots & \mathbf{A}_{nn}
\end{pmatrix}\begin{pmatrix}
b_{1} \\
b_{2} \\
 \vdots \\
b_{n}
\end{pmatrix}$$

对于xi，有

$$x_{i} = \frac{1}{\left| \mathbf{A} \right|}\left( b_{1}\mathbf{A}_{1i} + b_{2}\mathbf{A}_{2i} + \cdots + b_{n}\mathbf{A}_{ni} \right)$$

由行列式按列展开，b1A1i + b2A2i + ⋯ + bnAni相当于|A|把第i列替换为β，即|Ai|。故

$$x_{i} = \frac{\left| \mathbf{A}_{i} \right|}{\left| \mathbf{A} \right|}$$

初等变换

实际上是加减消元

1.对系数矩阵（A）/增广矩阵（B）施行初等行变换变为行最简型矩阵。

2.判断该行最简型矩阵的秩（它的秩为非0行的行数（非0子式的最高阶数））。

3.根据秩的情况得出方程组解的情况。

记系数矩阵和增广矩阵的秩分别为R(A)，R(B)，则

$$\left\{ \begin{array}{r}
R\left( \mathbf{A} \right) < R\left( \mathbf{B} \right)\text\{，无解\}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
R\left( \mathbf{A} \right) = R\left( \mathbf{B} \right) = n\text\{，有唯一解\}\ \ \ \ \  \\
R\left( \mathbf{A} \right) = R\left( \mathbf{B} \right) < n\text\{，有无限多解\}
\end{array} \right.\ $$

eg.求解齐次线性方程组

$$\left\{ \begin{array}{r}
\ \ x_{1} + 2x_{2} + 2x_{3} + x_{4} = 0 \\
2x_{1} + x_{2} - 2x_{3} - 2x_{4} = 0 \\
\ \ x_{1} - x_{2} - 4x_{3} - 3x_{4} = 0
\end{array} \right.\ $$

对系数矩阵A施行初等初等行变换变为行最简型矩阵

$$\mathbf{A} = \begin{pmatrix}
1 & 2 & 2 & - 3 \\
2 & 1 & - 2 & - 2 \\
1 & - 1 & - 4 & 1
\end{pmatrix}\underset{r_{3} - r_{1}}{\overset{r_{2} - 2r_{1}}{\rightarrow}}\begin{pmatrix}
1 & 2 & 2 & 1 \\
0 & - 3 & - 6 & - 4 \\
0 & - 3 & - 6 & - 4
\end{pmatrix}\underset{r_{2} \times \left( - \frac{1}{3} \right)}{\overset{r_{3} - r_{2}}{\rightarrow}}\begin{pmatrix}
1 & 2 & 2 & 1 \\
0 & 1 & 2 & \frac{4}{3} \\
0 & 0 & 0 & 0
\end{pmatrix}\overset{r_{1} - 2r_{2}}{\rightarrow}\begin{pmatrix}
1 & 0 & - 2 & - \frac{5}{3} \\
0 & 1 & 2 & \frac{4}{3} \\
0 & 0 & 0 & 0
\end{pmatrix}$$

R(A) = 2 < 3，有无数多解。

得到同解方程组

$$\left\{ \begin{array}{r}
x_{1} - 2x_{3} - \frac{5}{3}x_{4} = 0 \\
x_{2} + 2x_{3} + \frac{4}{3}x_{4} = 0
\end{array} \right.\ $$

得

$$\left\{ \begin{array}{r}
x_{1} = \ \ \ 2x_{3} + \frac{5}{3}x_{4} \\
x_{2} = - 2x_{3} - \frac{4}{3}x_{4}
\end{array} \right.\ \text{其中}x_{3}\text{，}x_{4}\text{可取任意值。}$$

或得到对应齐次线性方程组的基础解系

$$\mathbf{\xi}_{1} = \begin{pmatrix}
2 \\
 - 2 \\
1
\end{pmatrix}$$

和原方程组的特解

$$\mathbf{\gamma} = \begin{pmatrix}
 - \frac{5}{3} \\
\frac{4}{3} \\
0
\end{pmatrix}$$

写出通解

$$\mathbf{x} = \begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3}
\end{pmatrix} = c_{1}\mathbf{\xi}_{1} + \mathbf{\gamma =}c_{1}\begin{pmatrix}
2 \\
 - 2 \\
1
\end{pmatrix} + \begin{pmatrix}
 - \frac{5}{3} \\
\frac{4}{3} \\
0
\end{pmatrix}$$

eg.求解非齐次线性方程组

$$\left\{ \begin{array}{r}
\ \ \ x_{1} + \ \ x_{2} - 3x_{3} - \ \ x_{4} = 1 \\
3x_{1} - \ \ x_{2} - 3x_{3} + 4x_{4} = 4 \\
\ \ x_{1} + 5x_{3} - 9x_{3} - 8x_{4} = 0
\end{array} \right.\ $$

对增广矩阵B施行初等行变换

$$\mathbf{B} = \begin{pmatrix}
1 & 1 & - 3 & - 1 & 1 \\
3 & - 1 & - 3 & 4 & 4 \\
1 & 5 & - 9 & - 8 & 0
\end{pmatrix}\underset{r_{3} - r_{1}}{\overset{r_{2} - 3r_{1}}{\rightarrow}}\begin{pmatrix}
1 & 1 & - 3 & - 1 & 1 \\
0 & - 4 & 6 & 7 & 1 \\
0 & 4 & - 6 & - 7 & - 1
\end{pmatrix}$$

$$\underset{r_{2} - 4}{\overset{r_{3} + r_{2}}{\rightarrow}}\begin{pmatrix}
1 & 1 & - 3 & - 1 & 1 \\
0 & 1 & - \frac{3}{2} & - \frac{7}{4} & - \frac{1}{4} \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}\overset{r_{1} - r_{2}}{\rightarrow}\begin{pmatrix}
1 & 0 & - \frac{3}{2} & 0 & \frac{5}{4} \\
0 & 1 & - \frac{3}{2} & - \frac{7}{4} & - \frac{1}{4} \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}$$

R(A) = R(B) = 2 < 3，有无数多解。

得

$$\left\{ \begin{array}{r}
x_{1} = \frac{3}{2}x_{3} - \frac{3}{4}x_{4} + \frac{5}{4} \\
x_{2} = \frac{3}{2}x_{3} + \frac{7}{4}x_{4} - \frac{1}{4} \\
x_{3} = x_{3}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
x_{4} = x_{4}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

或有基础解系和特解

$$\mathbf{\xi}_{1} = \begin{pmatrix}
\frac{3}{2} \\
\frac{3}{2} \\
1 \\
0
\end{pmatrix}\text{，}\mathbf{\xi}_{2} = \begin{pmatrix}
0 \\
 - \frac{7}{4} \\
0 \\
1
\end{pmatrix}\text{，}\mathbf{\gamma} = \begin{pmatrix}
\frac{5}{4} \\
 - \frac{1}{4} \\
0 \\
0
\end{pmatrix}$$

得到通解

$$\mathbf{x} = \begin{pmatrix}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{pmatrix} = c_{1}\mathbf{\xi}_{1} + c_{2}\xi_{2} + \mathbf{\gamma =}c_{1}\begin{pmatrix}
\frac{3}{2} \\
\frac{3}{2} \\
1 \\
0
\end{pmatrix} + c_{2}\begin{pmatrix}
0 \\
 - \frac{7}{4} \\
0 \\
1
\end{pmatrix} + \begin{pmatrix}
 - \frac{5}{3} \\
\frac{4}{3} \\
0
\end{pmatrix}$$

eg.求解非齐次线性方程组

$$\left\{ \begin{array}{r}
\ \ x_{1} - 2x_{2} + 3x_{3} - \ \ x_{4} = 1 \\
3x_{1} - \ \ x_{2} + 5x_{3} - 3x_{4} = 2 \\
2x_{1} + \ \ x_{2} + 2x_{3} - 2x_{4} = 3
\end{array} \right.\ $$

对增广矩阵B施行初等行变换

$$\mathbf{B} = \begin{pmatrix}
1 & - 2 & 3 & - 1 & 1 \\
3 & - 1 & 5 & - 3 & 2 \\
2 & 1 & 2 & - 2 & 3
\end{pmatrix}\underset{r_{3} - r_{1}}{\overset{r_{2} - 3r_{1}}{\rightarrow}}\begin{pmatrix}
1 & - 2 & 3 & - 1 & 1 \\
0 & 5 & - 4 & 0 & - 1 \\
0 & 5 & - 4 & 0 & 1
\end{pmatrix}\overset{r_{3} - r_{2}}{\rightarrow}\begin{pmatrix}
1 & - 2 & 3 & - 1 & 1 \\
0 & 5 & - 4 & 0 & - 1 \\
0 & 0 & 0 & 0 & 2
\end{pmatrix}$$

R(A) = 2 < R(B) = 3，方程组无解。
