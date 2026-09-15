---
title: 矩阵
description: 对角阵、单位阵、三角阵、转置、方阵的行列式、伴随矩阵、逆矩阵、初等变换与相抵矩阵。
---

# 02 · 矩阵

[[toc]]

## 对角（矩）阵

除主对角线外所有元素均为0的方阵。

$${diag}\left\{ a_{11},a_{22},\cdots,a_{nn} \right\} = \mathbf{\Lambda\ }(大写字母Lambda) = \begin{pmatrix}
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

对角阵加、减、乘、求逆、伴随仍是对角阵，且有

$$diag\left\{ a_{1}，a_{2}，\cdots ，a_{n} \right\} \cdot diag\left\{ b_{1}，b_{2}，\cdots ，b_{n} \right\} = diag\left\{ a_{1}b_{1}，a_{2}b_{2}，\cdots ，a_{n}b_{n} \right\}$$

$$\left( diag\left\{ a_{1}，a_{2}，\cdots ，a_{n} \right\} \right)^{- 1} = diag\left\{ a_{1}^{- 1}，a_{2}^{- 1}，\cdots ，a_{n}^{- 1} \right\}$$

$$\mathbf{\Lambda}^{*} = \mathbf{\Lambda}$$

## 单位（矩）阵

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

## 上（下）三角（矩）阵

$\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
0 & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & a_{nn}
\end{pmatrix}$（上三角阵），$\begin{pmatrix}
a_{11} & 0 & \cdots & 0 \\
a_{21} & a_{22} & \cdots & 0 \\
 \vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}$（下三角阵）

上（下）三角阵加、减、乘、求逆、伴随仍是对角阵，且对角线上的元素分别为原三角阵的对角阵对应变化而来的对应元素。

## 转置

对矩阵$\mathbf{A}$的转置$\mathbf{A}^{T}$或$\mathbf{A}'$就是把它的行转为列，列转为行，类似于沿主对角线翻转。

$$\mathbf{A}_{m \times n} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}，\mathbf{A}' = \begin{pmatrix}
a_{11} & a_{21} & \cdots & a_{m1} \\
a_{12} & a_{22} & \cdots & a_{m2} \\
 \vdots & \vdots & & \vdots \\
a_{1n} & a_{2n} & \cdots & a_{mn}
\end{pmatrix}$$

## 方阵的行列式

方阵$\mathbf{A} = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{pmatrix}$的行列式为：$\left| \mathbf{A} \right| = \left| \begin{matrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
 \vdots & \vdots & & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{matrix} \right|$

## 伴随（矩）阵

对$n$阶方阵$\mathbf{A}$，定义其伴随（矩）阵

$$\mathbf{A}^{*} = \begin{pmatrix}
\mathbf{A}_{11} & \mathbf{A}_{21} & \cdots & \mathbf{A}_{n1} \\
\mathbf{A}_{12} & \mathbf{A}_{22} & \cdots & \mathbf{A}_{n2} \\
 \vdots & \vdots & & \vdots \\
\mathbf{A}_{1n} & \mathbf{A}_{2n} & \cdots & \mathbf{A}_{nn}
\end{pmatrix}$$

其中$\mathbf{A}_{ij}$是$\left| \mathbf{A} \right|$的$a_{ij}$对应的代数余子式。

## 逆（矩）阵

设有$n$阶方阵$\mathbf{A}$，若存在$n$阶方阵$\mathbf{B}$，使得

$$\mathbf{AB} = \mathbf{BA} = \mathbf{I}_{n}$$

则称$\mathbf{A}$为可逆（矩）阵、非（奇）异（矩）阵、满秩矩阵或非退化矩阵，称$\mathbf{B}$是$\mathbf{A}$的逆（矩）阵，记为$\mathbf{B =}\mathbf{A}^{- 1}$，否则称$\mathbf{A}$为奇异（矩）阵。

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

$$\left( \mathbf{AB} \right)' = \mathbf{B}'\mathbf{A}'$$

转置

</th>
<th>

$$\left( \mathbf{AB} \right)^{k}$$

$$k$$

次幂

</th>
<th>

$$\left( \mathbf{AB} \right)^{*} = \mathbf{B}^{*}\mathbf{A}^{*}$$

伴随矩阵

</th>
<th>

$$\left( \mathbf{AB} \right)^{- 1} = \mathbf{B}^{- 1}\mathbf{A}^{- 1}$$

逆矩阵

</th>
<th>

$$\left| \mathbf{AB} \right| = \left| \mathbf{A} \right|\left| \mathbf{B} \right|$$

行列式

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$$\left( \mathbf{AB} \right)' = \mathbf{B}'\mathbf{A}'$$

转置

</td>
<td>

$$\mathbf{A}^{''} = \mathbf{A}$$

</td>
<td>

$$\left( \mathbf{A}' \right)^{k} = \left( \mathbf{A}^{k} \right)'$$

</td>
<td>

$$\left( \mathbf{A}' \right)^{*} = \left( \mathbf{A}^{*} \right)'$$

</td>
<td>

$$\left( \mathbf{A}' \right)^{- 1} = \left( \mathbf{A}^{- 1} \right)'$$

</td>
<td>

$$\left| \mathbf{A}' \right| = \left| \mathbf{A} \right|$$

</td>
</tr>
<tr>
<td>

$$\left( \mathbf{AB} \right)^{k}$$

$$k$$

次幂

</td>
<td>

$$\left( \mathbf{A}^{k} \right)' = \left( \mathbf{A}' \right)^{k}$$

</td>
<td>

$$\left( \mathbf{A}^{k} \right)^{t} = \mathbf{A}^{kt}$$

</td>
<td>

$$\left( \mathbf{A}^{k} \right)^{*} = \left( \mathbf{A}^{*} \right)^{k}$$

</td>
<td>

$$\left( \mathbf{A}^{k} \right)^{- 1} = \left( \mathbf{A}^{- 1} \right)^{k}$$

</td>
<td>

$$\left| \mathbf{A}^{k} \right| = \left| \mathbf{A} \right|^{k}$$

</td>
</tr>
<tr>
<td>

$$\left( \mathbf{AB} \right)^{*} = \mathbf{B}^{*}\mathbf{A}^{*}$$

伴随矩阵

</td>
<td>

$$\left( \mathbf{A}^{*} \right)' = \left( \mathbf{A}' \right)^{*}$$

</td>
<td>

$$\left( \mathbf{A}^{*} \right)^{k} = \left( \mathbf{A}^{k} \right)^{*}$$

</td>
<td>

$$\mathbf{A}\mathbf{A}^{*} = \mathbf{A}^{*}\mathbf{A =}\left| \mathbf{A} \right|\mathbf{E}$$

$$\left( \mathbf{A}^{*} \right)^{*} = \left| \mathbf{A} \right|^{n - 2}\mathbf{A}$$

</td>
<td>

$$\mathbf{A}^{\mathbf{*}} = \left| \mathbf{A} \right|\mathbf{A}^{- 1}$$

$$\left( \mathbf{A}^{*} \right)^{- 1} = \left( \mathbf{A}^{- 1} \right)^{*}$$

$$= \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}$$

</td>
<td>

$$\left| \mathbf{A}^{*} \right| = \left| \mathbf{A} \right|^{n - 1}$$

</td>
</tr>
<tr>
<td>

$$\left( \mathbf{AB} \right)^{- 1} = \mathbf{B}^{- 1}\mathbf{A}^{- 1}$$

逆矩阵

</td>
<td>

$$\left( \mathbf{A}^{- 1} \right)' = \left( \mathbf{A}' \right)^{- 1}$$

</td>
<td>

$$\left( \mathbf{A}^{- 1} \right)^{k} = \left( \mathbf{A}^{k} \right)^{- 1}$$

</td>
<td>

$$\mathbf{A}^{- 1} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{\mathbf{*}}$$

$$\left( \mathbf{A}^{- 1} \right)^{*} = \left( \mathbf{A}^{*} \right)^{- 1}$$

$$= \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}$$

</td>
<td>

$$\left( \mathbf{A}^{- 1} \right)^{- 1} = \mathbf{A}$$

</td>
<td>

$$\left| \mathbf{A}^{- 1} \right| = \left| \mathbf{A} \right|^{- 1}$$

</td>
</tr>
<tr>
<td>

$$\left| \mathbf{AB} \right| = \left| \mathbf{A} \right|\left| \mathbf{B} \right|$$

行列式

</td>
<td>

$$\left| \mathbf{A} \right| = \left| \mathbf{A}' \right|$$

</td>
<td>

$$\left| \mathbf{A} \right|^{k} = \left| \mathbf{A}^{k} \right|$$

</td>
<td>

$$\left| \mathbf{A} \right|^{n - 1} = \left| \mathbf{A}^{*} \right|$$

</td>
<td>

$$\left| \mathbf{A} \right|^{- 1} = \left| \mathbf{A}^{- 1} \right|$$

</td>
<td>

$$\left| \mathbf{AB} \right| = \left| \mathbf{BA} \right|$$

</td>
</tr>
</tbody>
</table>
</div>

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

转置

</th>
<th>

行列式

</th>
<th>

k次幂

</th>
<th>

伴随矩阵

</th>
<th>

逆矩阵

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

性质

</td>
<td>

$$\left( \mathbf{AB} \right)' = \mathbf{B}'\mathbf{A}'$$

</td>
<td>

$$\left| \mathbf{A}' \right| = \left| \mathbf{A} \right|$$

$$\left| c\mathbf{A} \right| = c^{n}\left| \mathbf{A} \right|$$

$$\left| \mathbf{AB} \right| = \left| \mathbf{A} \right|\left| \mathbf{B} \right| = \left| \mathbf{BA} \right|$$

</td>
<td>

$$\mathbf{A}^{\mathbf{r}}\mathbf{A}^{\mathbf{s}}\mathbf{=}\mathbf{A}^{\mathbf{r + s}}$$

若

$$\mathbf{A =}\mathbf{P}^{\mathbf{- 1}}\mathbf{BP}$$

，则

$$\mathbf{A}^{k} = \mathbf{P}^{- 1}\mathbf{B}^{k}\mathbf{P}$$

</td>
<td>

$$\left( c\mathbf{A} \right)^{\mathbf{*}}\mathbf{=}c^{n - 1}\mathbf{A}^{\mathbf{*}}$$

$$\mathbf{A}\mathbf{A}^{*} = \mathbf{A}^{*}\mathbf{A} = \left| \mathbf{A} \right| \cdot \mathbf{I}_{n}$$

$$\left| \mathbf{A} \right| = 0 \Leftrightarrow \left| \mathbf{A}^{*} \right| = 0$$

$$\left| \mathbf{A}^{*} \right| = \left| \mathbf{A} \right|^{n - 1}$$

$$\left( \mathbf{AB} \right)^{*} = \mathbf{B}^{\mathbf{*}}\mathbf{A}^{\mathbf{*}}$$

$$\mathbf{A}$$

与

$$\mathbf{A}^{\mathbf{*}}$$

同时可逆或同时不可逆

$$r\left( \mathbf{A}^{*} \right) = \left\{ \begin{array}{r} n\text{，}r\left( \mathbf{A} \right) = n\ \ \ \ \ \ \ \  \\ 1\text{，}r\left( \mathbf{A} \right) = n - 1 \\ 0\text{，}r\left( \mathbf{A} \right) < n\ \ \ \ \ \ \ \ \end{array} \right.\$$

$$\mathbf{A}^{*} \neq 0 \Rightarrow r(A) \geq n - 1$$

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{*} = \begin{pmatrix} d & - b \\ - c & a \end{pmatrix}$$

</td>
<td>

$$\left( \mathbf{AB} \right)^{- 1} = \mathbf{B}^{- 1}\mathbf{A}^{- 1}$$

$$\left( c\mathbf{A} \right)^{- 1} = c^{- 1}\mathbf{A}^{- 1}$$

$$\mathbf{A}\text{可逆} \Leftrightarrow \left| \mathbf{A} \right| \neq 0$$

$$\mathbf{A}^{- 1} = \frac{1}{\left| \mathbf{A} \right|}\mathbf{A}^{*}$$

$$\mathbf{A} = \left| \mathbf{A} \right|\left( \mathbf{A}^{*} \right)^{- 1}$$

$$\mathbf{AB} = \mathbf{I}_{n}\mathbf{\Rightarrow A}\text{，}\mathbf{B}$$

互逆

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{- 1} = \frac{\begin{pmatrix} d & - b \\ - c & a \end{pmatrix}}{\left| \begin{matrix} a & b \\ c & d \end{matrix} \right|}$$

</td>
</tr>
<tr>
<td>

$$\mathbf{I}$$

</td>
<td>

$$\mathbf{I}$$

</td>
<td>

$$1$$

</td>
<td>

$$\mathbf{I}$$

</td>
<td>

$$\mathbf{I}$$

</td>
<td>

$$\mathbf{I}$$

</td>
</tr>
<tr>
<td>

$$\mathbf{P}_{ij}$$

</td>
<td>

$$\mathbf{P}_{ij}$$

</td>
<td>

$$- 1$$

</td>
<td></td>
<td>

$$\mathbf{P}_{ij}$$

</td>
<td>

$$\mathbf{P}_{ij}$$

</td>
</tr>
<tr>
<td>

$$\mathbf{P}_{i}(c)$$

</td>
<td>

$$\mathbf{P}_{i}(c)$$

</td>
<td>

$$c$$

</td>
<td></td>
<td>

$$\mathbf{P}_{i}\left( \frac{1}{c} \right)$$

</td>
<td>

$$\mathbf{P}_{i}\left( \frac{1}{c} \right)$$

</td>
</tr>
<tr>
<td>

$$\mathbf{T}_{ij}(c)$$

</td>
<td>

$$\mathbf{T}_{ji}(c)$$

</td>
<td>

$$1$$

</td>
<td></td>
<td>

$$\mathbf{T}_{ij}( - c)$$

</td>
<td>

$$\mathbf{T}_{ij}( - c)$$

</td>
</tr>
<tr>
<td>

$$\mathbf{\Lambda}$$

</td>
<td>

$$\mathbf{\Lambda}$$

</td>
<td>

$$\prod_{i = 1}^{n}a_{ii}$$

</td>
<td></td>
<td>

$$diag\left\{ \frac{\left| \mathbf{A} \right|}{a_{11}},\frac{\left| \mathbf{A} \right|}{a_{22}},\cdots,\frac{\left| \mathbf{A} \right|}{a_{nn}} \right\}$$

</td>
<td>

$$diag\left\{ - a_{11}, - a_{22},\cdots,\  - a_{nn} \right\}$$

</td>
</tr>
<tr>
<td>

分块对角阵

$$\begin{pmatrix} \mathbf{A} & \mathbf{O} \\ \mathbf{O} & \mathbf{B} \end{pmatrix}$$

</td>
<td>

$$\begin{pmatrix} \mathbf{A}^{\mathbf{'}} & \mathbf{O} \\ \mathbf{O} & \mathbf{B}^{\mathbf{'}} \end{pmatrix}$$

</td>
<td>

$$\left| \mathbf{AB} \right|$$

</td>
<td>

$$\begin{pmatrix} \mathbf{A}^{n} & \mathbf{O} \\ \mathbf{O} & \mathbf{B}^{n} \end{pmatrix}$$

</td>
<td>

$$\begin{pmatrix} \mathbf{A}^{\mathbf{*}} & \mathbf{O} \\ \mathbf{O} & \mathbf{B}^{\mathbf{*}} \end{pmatrix}$$

</td>
<td>

$$\begin{pmatrix} \mathbf{A}^{- 1} & \mathbf{O} \\ \mathbf{O} & \mathbf{B}^{- 1} \end{pmatrix}$$

</td>
</tr>
<tr>
<td>

反对角阵

</td>
<td>

不变

</td>
<td>

$$( - 1)^{\frac{n(n - 1)}{2}}\prod_{}^{}a_{i}$$

</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

分块反对角阵

$$\begin{pmatrix} \mathbf{O} & \mathbf{A} \\ \mathbf{B} & \mathbf{O} \end{pmatrix}$$

</td>
<td>

$$\begin{pmatrix} \mathbf{O} & \mathbf{B}^{\mathbf{'}} \\ \mathbf{A}^{\mathbf{'}} & \mathbf{O} \end{pmatrix}$$

</td>
<td></td>
<td></td>
<td></td>
<td>

$$\begin{pmatrix} \mathbf{O} & \mathbf{B}^{- 1} \\ \mathbf{A}^{- 1} & \mathbf{O} \end{pmatrix}$$

</td>
</tr>
<tr>
<td>

上/下三角阵

</td>
<td colspan="5">

仍为三角阵，且对角线上的元素分别为原三角阵的对角阵对应变化而来的对应元素。

</td>
</tr>
<tr>
<td>

可逆阵

</td>
<td>

可逆

</td>
<td>

$$\neq 0$$

</td>
<td>

可逆

</td>
<td>

可逆

</td>
<td></td>
</tr>
<tr>
<td>

对称矩阵

$$\mathbf{A}^{\mathbf{'}}\mathbf{= A}$$

</td>
<td>

$$\mathbf{A}$$

</td>
<td></td>
<td></td>
<td>

对称

</td>
<td>

若可逆则逆阵仍对称

</td>
</tr>
<tr>
<td>

反对称矩阵

$$\mathbf{A}^{\mathbf{'}}\mathbf{= - A}$$

</td>
<td>

$$\mathbf{- A}$$

</td>
<td>

奇数阶为

$$0$$

，偶数阶

$$\geq 0$$

</td>
<td></td>
<td>

奇数阶为零矩阵

偶数阶为对称阵

</td>
<td>

若可逆则逆阵偶数阶反对称

</td>
</tr>
<tr>
<td rowspan="2">

正交矩阵

（是实矩阵）

$$\mathbf{A}\mathbf{A}^{\mathbf{'}}\mathbf{=}\mathbf{A}^{\mathbf{'}}\mathbf{A = I}$$

$$\mathbf{A}^{\mathbf{'}}\mathbf{=}\mathbf{A}^{- 1}$$

</td>
<td>

$$\mathbf{A}^{- 1}$$

（正交）

</td>
<td>

$$\pm 1$$

</td>
<td>

正交

</td>
<td>

$$\mathbf{\pm}\mathbf{A}^{\mathbf{'}}$$

（正交）

</td>
<td>

$$\mathbf{A}^{\mathbf{'}}$$

（正交）

</td>
</tr>
<tr>
<td colspan="5">

正交矩阵

$$\Leftrightarrow$$

方阵的列向量为单位向量，且两两正交。

若

$$\mathbf{A}$$

，

$$\mathbf{B}$$

是正交矩阵，则

$$\mathbf{AB}$$

也是正交矩阵。

</td>
</tr>
<tr>
<td>

正定矩阵

$$\forall\mathbf{x \neq 0},\mathbf{\ }\mathbf{x}^{\mathbf{'}}\mathbf{Ax > 0}$$

</td>
<td>

正定

</td>
<td>

$$\geq 0$$

</td>
<td>

正定

</td>
<td>

正定

</td>
<td>

正定

</td>
</tr>
<tr>
<td>

正规矩阵

$$\mathbf{A}\mathbf{A}^{\mathbf{'}}\mathbf{=}\mathbf{A}^{\mathbf{'}}\mathbf{A}$$

</td>
<td>

正规

</td>
<td></td>
<td></td>
<td>

正规

</td>
<td>

若可逆则逆阵仍正规

</td>
</tr>
</tbody>
</table>
</div>

## 初等变换与初等矩阵

定义矩阵的三类初等行（列）变换如下：

第一类初等变换：对调矩阵中某两行（列）的位置。

第二类初等变换：用一非0常数$c$乘以矩阵的某一行（列）

第三类初等变换：将矩阵的某一行（列）乘以常数$c$后加到另一行（列）上去。

定义三类初等矩阵如下：

第一类初等矩阵：$\mathbf{P}_{ij}$或$\mathbf{E}(i,j)$：将单位阵$\mathbf{I}_{n}$的第$i$行与第$j$行（第$i$列与第$j$列）对换后得到的矩阵。

第二类初等矩阵：$\mathbf{P}_{i}(c)$或$\mathbf{E}\left( i(c) \right)$：将常数$c$乘以单位阵$\mathbf{I}_{n}$的第$i$行（第$j$列）位置而得到的矩阵。

第三类初等矩阵：$\mathbf{T}_{ij}(c)$或$\mathbf{E}\left( ij(k) \right)$：将单位阵$\mathbf{I}_{n}$的第$i$行（第$j$列）乘以$c$后加到第$j$行（第$i$列）上得到的矩阵。

## 相抵矩阵

如果一个矩阵$\mathbf{A}$经过有限次初等行变换后变成矩阵$\mathbf{B}$，则称$\mathbf{A}$和$\mathbf{B}$是行等价的。

如果一个矩阵$\mathbf{A}$经过有限次初等列变换后变成矩阵$\mathbf{B}$，则称$\mathbf{A}$和$\mathbf{B}$是列等价的。

如果一个矩阵$\mathbf{A}$经过有限次初等变换后变成矩阵$\mathbf{B}$，则称$\mathbf{A}$和$\mathbf{B}$是等价或相抵的。

矩阵$\mathbf{A}$必然可以通过初等变换变为如下矩阵，该矩阵称为矩阵$\mathbf{A}$的相抵标准型。

$\begin{pmatrix}
1 & \cdots & 0 & 0 & \cdots & 0 \\
 \vdots & & \vdots & \vdots & & \vdots \\
0 & \cdots & 1 & 0 & \cdots & 0 \\
0 & \cdots & 0 & 0 & \cdots & 0 \\
 \vdots & & \vdots & \vdots & & \vdots \\
0 & \cdots & 0 & 0 & \cdots & 0
\end{pmatrix}\begin{pmatrix}
\mathbf{I} & \mathbf{O} \\
\mathbf{O} & \mathbf{O}
\end{pmatrix}$（也可以是$\mathbf{O}$）

定理：矩阵$\mathbf{A}$经过有限次初等行变换，可以化为阶梯形矩阵。

定理：设$\mathbf{A}$是一个$m \times n$阵，则对$\mathbf{A}$作一次初等行变换后得到的矩阵等于用一个$m$阶相应的初等矩阵左乘后得到的积。对$\mathbf{A}$作一次初等列变换后得到的矩阵等于用一个$n$阶相应的初等矩阵右乘后得到的积。（简称为"行左列右"）

定理：初等矩阵都是非异阵且其逆矩阵仍是同类初等矩阵，即

$$\mathbf{P}_{ij}^{- 1} = \mathbf{P}_{ij}，\mathbf{P}_{i}(c)^{- 1} = \mathbf{P}_{i}\left( \frac{1}{c} \right)，\mathbf{T}_{ij}(c)^{- 1} = \mathbf{T}_{ij}( - c)$$

定理：非异阵经初等变换后仍为非异阵，奇异阵经初等变换后仍为奇异阵。

定理：$\left| \mathbf{P}_{ij} \right| = - 1，\left| \mathbf{P}_{i}(c) \right| = c，\left| \mathbf{T}_{ij}(c) \right| = 1$

定理：设$\mathbf{A}$是一个$n$阶可逆阵，则仅用初等行变换或仅用初等列变换即可把化为单位阵$\mathbf{I}_{n}$。

定理：任一$n$阶可逆阵均可表示为有限个初等矩阵的积。
