---
title: 行列式
description: 行列式的性质、Laplace 定理的推论、Vandermonde 行列式与爪型行列式。
---

# 01 · 行列式

[[toc]]

## 行列式的性质

性质1：上（下）三角行列式的值等于其主对角线上元素之积。

性质2：若行列式的某一行（列）元素全为$0$，则行列式的值等于$0$。

性质3：用某个常数$c$乘以行列式的某一行（列），所得行列式的值等于原行列式值的$c$倍。

性质4：对换行列式的两行（列），行列式的值改变符号。

性质5：若行列式的某两行（列）成比例，则行列式的值等于$0$。

性质6：若行列式的某一行（列）元素$a_{ij} = b_{ij} + c_{ij}$，则该行列式可以分解为两个行列式之和，其中一个行列式的相应行（列）的元素为$b_{ij}$，另一个行列式的相应行（列）的元素为$c_{ij}$。

性质7：将行列式的某一行（列）乘以常数$c$加到另一行（列）上去，行列式的值不变。

性质8：行列式转置后的值不变。

异乘变0定理：行列式某一行（列）的元素与另一行（列）的对应元素的代数余子式乘积之和等于0。

$$
\sum_{k = 1}^{n}{a_{ki}A_{kj}} = \left\{ \begin{array}{r}
D\text{，当}i = j \\
0\text{，当}i \neq j
\end{array} \right.\ \ 或\ \sum_{k = 1}^{n}{a_{ik}A_{jk}} = \left\{ \begin{array}{r}
D\text{，当}i = j \\
0\text{，当}i \neq j
\end{array} \right.\ 
$$

## Laplace（拉普拉斯）定理的推论

$$
\left| \begin{matrix}
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
\end{matrix} \right|
$$

$$
\left| \begin{matrix}
\mathbf{A} & \mathbf{C} \\
\mathbf{O} & \mathbf{B}
\end{matrix} \right|\mathbf{=}\left| \begin{matrix}
\mathbf{A} & \mathbf{O} \\
\mathbf{D} & \mathbf{B}
\end{matrix} \right|\mathbf{=}\left| \mathbf{A} \right|\left| \mathbf{B} \right|
$$

## 特殊行列式

### Vandermonde（范德蒙德）行列式

$$
\left| \begin{matrix}
1 & x_{1} & x_{1}^{2} & \cdots & x_{1}^{n - 1} \\
1 & x_{2} & x_{2}^{2} & \cdots & x_{2}^{n - 1} \\
 \vdots & \vdots & \vdots & & \vdots \\
1 & x_{n - 1} & x_{n - 1}^{2} & \cdots & x_{n - 1}^{n - 1} \\
1 & x_{n} & x_{n}^{2} & \cdots & x_{n}^{n - 1}
\end{matrix} \right| = \prod_{1 \leq i < j \leq n}^{}\left( x_{j} - x_{i} \right)
$$

$$
eg.\left| \begin{matrix}
1 & 1 & 1 & 1 \\
1 & 2 & 3 & 4 \\
1 & 4 & 9 & 16 \\
1 & 8 & 27 & 64
\end{matrix} \right| = (2 - 1)(3 - 1)(3 - 2)(4 - 1)(4 - 2)(4 - 3)
$$

### 爪型行列式

$$
\left| \begin{matrix}
a_{1} & b_{2} & b_{3} & \cdots & b_{n} \\
c_{2} & a_{2} & 0 & \cdots & 0 \\
c_{3} & 0 & a_{3} & \cdots & 0 \\
 \vdots & \vdots & \vdots & & \vdots \\
c_{n} & 0 & 0 & 0 & a_{n}
\end{matrix} \right| = \left( a_{1} - \sum_{i = 2}^{n}\frac{b_{i}c_{i}}{a_{i}} \right)\prod_{i = 2}^{n}a_{i}
$$

$$
\text{证明：第}i\text{行乘以} - \frac{b_{i}}{a_{i}}\text{加到第一行上}(2 \leq i \leq n)\text{，得}\left| \begin{matrix}
a_{1} - \sum_{i = 2}^{n}\frac{b_{i}c_{i}}{a_{i}} & 0 & 0 & \cdots & 0 \\
c_{2} & a_{2} & 0 & \cdots & 0 \\
c_{3} & 0 & a_{3} & \cdots & 0 \\
 \vdots & \vdots & \vdots & & \vdots \\
c_{n} & 0 & 0 & 0 & a_{n}
\end{matrix} \right|
$$

$$
\left| \begin{matrix}
a & b & b & \cdots & b \\
b & a & b & \cdots & b \\
b & b & a & \cdots & b \\
 \vdots & \vdots & \vdots & & \vdots \\
b & b & b & \cdots & a
\end{matrix} \right| = \left\lbrack a + (n - 1)b \right\rbrack(a - b)^{n - 1}
$$

$$
\text{证明：}\left| \begin{matrix}
a & b & b & \cdots & b \\
b & a & b & \cdots & b \\
b & b & a & \cdots & b \\
 \vdots & \vdots & \vdots & & \vdots \\
b & b & b & \cdots & a
\end{matrix} \right|\underset{r_{1} + r_{n}}{\overset{\begin{array}{r}
r_{1} + r_{2} \\
r_{1} + r_{3} \\
\cdots
\end{array}}{=}}\left| \begin{matrix}
a + (n - 1)b & a + (n - 1)b & a + (n - 1)b & \cdots & a + (n - 1)b \\
b & a & b & \cdots & b \\
b & b & a & \cdots & b \\
 \vdots & \vdots & \vdots & & \vdots \\
b & b & b & \cdots & a
\end{matrix} \right| = \left\lbrack a + (n - 1)b \right\rbrack\left| \begin{matrix}
1 & 1 & 1 & \cdots & 1 \\
b & a & b & \cdots & b \\
b & b & a & \cdots & b \\
 \vdots & \vdots & \vdots & & \vdots \\
b & b & b & \cdots & a
\end{matrix} \right|\underset{r_{n} - r_{1}}{\overset{\begin{array}{r}
r_{2} - r_{1} \\
r_{3} - r_{1} \\
\cdots
\end{array}}{=}}\left| \begin{matrix}
1 & 1 & 1 & \cdots & 1 \\
0 & a - b & 0 & \cdots & 0 \\
0 & 0 & a - b & \cdots & 0 \\
 \vdots & \vdots & \vdots & & \vdots \\
0 & 0 & 0 & \cdots & a - b
\end{matrix} \right|
$$
