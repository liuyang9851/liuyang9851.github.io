---
title: 行列式
description: 行列式的八条基本性质、异乘变 0 定理、Laplace 展开推论，以及 Vandermonde 与爪型行列式的计算套路。
---

# 01 · 行列式

[[toc]]

## 八条基本性质

设 $D=\det(\A)$，以下性质对**行**成立，对**列**同样成立。

| # | 性质 | 效果 |
| --- | --- | --- |
| 1 | 上（下）三角行列式的值等于主对角线元素之积 | — |
| 2 | 某行（列）元素全为 $0$ | $D=0$ |
| 3 | 用常数 $c$ 乘某行（列） | $D$ 变为 $cD$ |
| 4 | 对换两行（列） | $D$ 改变符号 |
| 5 | 某两行（列）成比例 | $D=0$ |
| 6 | 某行（列）元素可拆成两项之和 | $D$ 拆成两个行列式之和 |
| 7 | 某行（列）乘 $c$ 加到另一行（列） | $D$ 不变 |
| 8 | 转置 | $D$ 不变 |

性质 6 值得单独写清楚：若第 $i$ 行每个元素都满足 $a_{ij}=b_{ij}+c_{ij}$，则

$$
\det(\A)=\begin{vmatrix}
b_{i1}+c_{i1} & \cdots & b_{in}+c_{in}\\
\vdots & & \vdots
\end{vmatrix}
=\begin{vmatrix}
b_{i1} & \cdots & b_{in}\\
\vdots & & \vdots
\end{vmatrix}
+\begin{vmatrix}
c_{i1} & \cdots & c_{in}\\
\vdots & & \vdots
\end{vmatrix}
$$

::: tip 记忆方式
性质 2、4、5 说的是「什么时候行列式为 0 或变号」，性质 3、6、7 说的是「行变换如何影响行列式」。性质 7 是**唯一不改变行列式值**的行变换，因此它是计算行列式的主力——所有「化三角」的套路都建立在它上面。
:::

## 异乘变 0 定理

> 行列式某一行（列）的元素，与**另一行（列）**对应元素的代数余子式乘积之和等于 $0$。

记 $\A=(a_{ij})_{n\times n}$，$A_{ij}$ 为 $a_{ij}$ 的代数余子式，则

$$
\sum_{k=1}^{n}a_{ki}A_{kj}=
\begin{cases}
D, & i=j\\[4pt]
0, & i\neq j
\end{cases}
\qquad\text{或}\qquad
\sum_{k=1}^{n}a_{ik}A_{jk}=
\begin{cases}
D, & i=j\\[4pt]
0, & i\neq j
\end{cases}
$$

$i=j$ 时这就是按行（列）展开公式；$i\neq j$ 时就是「异乘变 0」——用别人的余子式搭配自己的元素，结果必为 $0$。

**为什么 $i\neq j$ 时是 0？** 把 $\A$ 的第 $j$ 行替换成第 $i$ 行，得到矩阵 $\B$。$\B$ 有两行相同，故 $\det(\B)=0$；而对 $\B$ 按第 $j$ 行展开，恰好就是 $\sum_k a_{ki}A_{kj}$。

## Laplace（拉普拉斯）定理的推论

**分块三角形式。** 若 $\A$ 为 $k$ 阶方阵、$\B$ 为 $n-k$ 阶方阵，则

$$
\begin{vmatrix}
\A & \C\\
\O & \B
\end{vmatrix}
=
\begin{vmatrix}
\A & \O\\
\D & \B
\end{vmatrix}
=\det(\A)\det(\B)
$$

即：**对角块之一为零矩阵时，整体行列式等于两个对角块行列式之积**，与另一侧的块 $\C$ 或 $\D$ 无关。

这个结论把 $n$ 阶行列式的计算降成了两个小块的计算，是分块法的基础。

## 特殊行列式

### Vandermonde（范德蒙德）行列式

$$
V_n=\begin{vmatrix}
1 & x_1 & x_1^2 & \cdots & x_1^{n-1}\\
1 & x_2 & x_2^2 & \cdots & x_2^{n-1}\\
\vdots & \vdots & \vdots & & \vdots\\
1 & x_n & x_n^2 & \cdots & x_n^{n-1}
\end{vmatrix}
=\prod_{1\le i<j\le n}\left(x_j-x_i\right)
$$

**规律**：结果是所有「下标大的减下标小的」之差连乘，共 $\binom{n}{2}$ 个因子。

**例题。**

$$
\begin{vmatrix}
1 & 1 & 1 & 1\\
1 & 2 & 3 & 4\\
1 & 4 & 9 & 16\\
1 & 8 & 27 & 64
\end{vmatrix}
=(2-1)(3-1)(3-2)(4-1)(4-2)(4-3)=12
$$

这里 $x_1=1,\;x_2=2,\;x_3=3,\;x_4=4$。若某一列不是 $1,x,x^2,\dots$ 的形式，通常先提取公因子化为标准型。

### 爪型行列式

形如

$$
\begin{vmatrix}
a_1 & b_2 & b_3 & \cdots & b_n\\
c_2 & a_2 & 0 & \cdots & 0\\
c_3 & 0 & a_3 & \cdots & 0\\
\vdots & \vdots & \vdots & & \vdots\\
c_n & 0 & 0 & \cdots & a_n
\end{vmatrix}
=\left(a_1-\sum_{i=2}^{n}\frac{b_ic_i}{a_i}\right)\prod_{i=2}^{n}a_i
\qquad (a_i\neq0)
$$

**证明思路。** 利用性质 7（某行乘常数加到另一行，值不变），把第一行以外的行逐一消去第一行上的 $b_i$：

$$
r_1-\frac{b_i}{a_i}r_i \quad (2\le i\le n)
$$

于是第一行变成

$$
\left(a_1-\sum_{i=2}^{n}\frac{b_ic_i}{a_i},\;0,\;0,\;\cdots,\;0\right)
$$

其余行不变。此时行列式已是**下三角**，由性质 1 直接得到上面的结果。

### 主对角线为 $a$、其余为 $b$ 的行列式

$$
D_n=\begin{vmatrix}
a & b & b & \cdots & b\\
b & a & b & \cdots & b\\
b & b & a & \cdots & b\\
\vdots & \vdots & \vdots & & \vdots\\
b & b & b & \cdots & a
\end{vmatrix}
=\bigl[a+(n-1)b\bigr](a-b)^{n-1}
$$

**证法：把各列加到第一列。**

先把第 $2,3,\dots,n$ 列全部加到第 $1$ 列。第一列每个元素都变成

$$
b+b+\cdots+b+a=b(n-1)+a
$$

提出公因子 $a+(n-1)b$ 后，第一列全为 $1$：

$$
D_n=\bigl[a+(n-1)b\bigr]
\begin{vmatrix}
1 & b & b & \cdots & b\\
1 & a & b & \cdots & b\\
1 & b & a & \cdots & b\\
\vdots & \vdots & \vdots & & \vdots\\
1 & b & b & \cdots & a
\end{vmatrix}
$$

**再把第 1 行乘以 $-1$ 加到其余各行**（$r_i-r_1$，$i=2,\dots,n$）。此时第一行之外都变成对角阵：

$$
D_n=\bigl[a+(n-1)b\bigr]
\begin{vmatrix}
1 & b & b & \cdots & b\\
0 & a-b & 0 & \cdots & 0\\
0 & 0 & a-b & \cdots & 0\\
\vdots & \vdots & \vdots & & \vdots\\
0 & 0 & 0 & \cdots & a-b
\end{vmatrix}
$$

这是上三角，由性质 1 得

$$
D_n=\bigl[a+(n-1)b\bigr](a-b)^{n-1}
$$

::: tip 这类题的通法
「每行（列）元素之和相同」→ 把各列加到第一列 → 提公因子 → 用第一行消去其余行。这个套路适用于所有行和相等的行列式。
:::

## 勘误

迁移过程中发现原始 Word 笔记有三处需要修正，均已在上文改正：

1. **异乘变 0 定理的公式把乘号写成了加号。** 原文作
   $a_{i1}+A_{j1}+a_{i2}+A_{j2}+\cdots$，
   但定理名是「异**乘**变 0」，且 $i=j$ 时应等于 $D$。改为
   $\sum_{k=1}^{n}a_{ki}A_{kj}$（元素与余子式**相乘**）。

2. **性质 6 的原文缺少右侧表达式。** 原文只写到「若行列式的某一行（列）元素」，后面的 $a_{ij}=b_{ij}+c_{ij}$ 与分解式被 Word 公式编辑器吞掉，已补全。

3. **Vandermonde 例题未给出结果。** 原文止于连乘式，已补上 $=12$。

此外，原文有 33 处中文标点（如「，则行列式的值等于」）被误置于公式环境内，已移回正文，否则渲染时会被当作数学符号排版。
