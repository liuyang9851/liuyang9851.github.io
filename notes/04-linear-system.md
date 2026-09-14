---
title: 线性方程组
description: 克拉默法则、解的结构与判定、基础解系。
---

# 04 · 线性方程组

[[toc]]

### 克拉默法则

含有$n$个未知数的$n$个线性方程的方程组

$$\left\{ \begin{array}{r}
a_{11}x_{1} + a_{12}x_{2} + \cdots + a_{1n}x_{n} = b_{1} \\
a_{21}x_{1} + a_{22}x_{2} + \cdots + a_{2n}x_{n} = b_{2} \\
\cdots\cdots \\
a_{n1}x_{1} + a_{n2}x_{2} + \cdots + a_{nn}x_{n} = b_{n}
\end{array} \right.\ $$

若其系数矩阵$A$的行列式不等于0，即

$$\left| \mathbf{A} \right| = \left| \begin{matrix}
a_{11} & \cdots & a_{1n} \\
 \vdots & & \vdots \\
a_{n1} & \cdots & a_{nn}
\end{matrix} \right| \neq 0$$

那么，该方程组有唯一解（否则方程组无解或有无穷多解）

$$x_{i} = \frac{\left| \mathbf{A}_{i} \right|}{\left| \mathbf{A} \right|}$$

其中$\mathbf{A}_{i}$是把系数矩阵$\mathbf{A}$中第$i$列的元素用方程组右侧的常数项代替后所得到的n阶矩阵，即

$$\begin{pmatrix}
a_{11} & \cdots & a_{1,i - 1} & b_{1} & a_{1,i + 1} & \cdots & a_{1n} \\
 \vdots & & \vdots & \vdots & \vdots & & \vdots \\
a_{n1} & \cdots & a_{n,i - 1} & b_{n} & a_{n,i + 1} & \cdots & a_{nn}
\end{pmatrix}$$

## 秩

记系数矩阵和增广矩阵的秩分别为$r\left( \mathbf{A} \right)\text{，}r\left( \mathbf{B} \right)$，则

$$\left\{ \begin{array}{r}
r\left( \mathbf{A} \right) < r\left( \mathbf{B} \right)\text{，}无解\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
r\left( \mathbf{A} \right) = r\left( \mathbf{B} \right) = n\text{，}有唯一解\ \ \ \ \  \\
r\left( \mathbf{A} \right) = r\left( \mathbf{B} \right) < n\text{，}有无限多解
\end{array} \right.\ $$

## 基础解系

定理：齐次线性方程组$\mathbf{A}_{m \times n}\mathbf{x} = \mathbf{0}$若有$r\left( \mathbf{A} \right) = r < n$，则其基础解系为$n - r$个解向量的线性组合

定理：线性方程组$\mathbf{A}_{m \times n}\mathbf{x} = \mathbf{\beta}$的通解为其特解与导出组$\mathbf{Ax = 0}$的通解的和。

推论：设$\mathbf{\alpha}_{1}\text{，}\mathbf{\alpha}_{2}\text{，}\cdots \text{，}\mathbf{\alpha}_{t}$是$\mathbf{Ax = \beta}$的解，则

$$k_{1}\mathbf{\alpha}_{1} + k_{2}\mathbf{\alpha}_{2} + \cdots + k_{t}\mathbf{\alpha}_{t}\ \ \left( k_{1} + k_{2} + \cdots + k_{t} = 1 \right)$$

仍是$\mathbf{Ax = \beta}$的解，

$$k_{1}\mathbf{\alpha}_{1} + k_{2}\mathbf{\alpha}_{2} + \cdots + k_{t}\mathbf{\alpha}_{t}\ \ \left( k_{1} + k_{2} + \cdots + k_{n} = 0 \right)$$

是$导出组\mathbf{Ax = 0}$的解

<div class="table-scroll">
<table>
<thead>
<tr>
<th>等价关系</th>
<th>相抵（等价）</th>
<th>相似</th>
<th>合同</th>
</tr>
</thead>
<tbody>

<tr>
<td>定义</td>
<td>

相抵：$\mathbf{A}$能经过有限次初等变换变成$\mathbf{B}$（不需要是方阵）

</td>
<td>

相似：存在可逆阵$\mathbf{P}$，使得$\mathbf{B} = \mathbf{P}^{- 1}\mathbf{AP}$（必须是方阵）

</td>
<td>

合同：存在可逆阵$\mathbf{C}$，使得$\mathbf{B} = \mathbf{C}'\mathbf{AC}$（必须是方阵，且一般只讨论$\mathbf{A}$为实对称阵的情况）

</td>
</tr>

<tr>
<td>判定</td>
<td>

同型$+$等秩

</td>
<td>

可对角化$+$特征值相等

<br>

相似两矩阵必同时可对角化或同时不可对角化。对于可对角化的矩阵，特征多项式（特征值）相同则相似；只凭特征值相等无法判定一般的方阵是否相似。

<br>

实对称阵一定既相似又合同于某对角阵。

</td>
<td>

对称$+$正负惯性指数相等

</td>
</tr>

<tr>
<td>等价性质</td>
<td>

自反性：$\mathbf{A}$等价于$\mathbf{A}$。

<br>

对称性：若$\mathbf{A}$等价于$\mathbf{B}$，则$\mathbf{B}$等价于$\mathbf{A}$。

<br>

传递性：若$\mathbf{A}$等价于$\mathbf{B}$，$\mathbf{B}$等价于$\mathbf{C}$，则$\mathbf{A}$等价于$\mathbf{C}$。

</td>
<td></td>
<td></td>
</tr>

<tr>
<td>不变量与全系不变量</td>
<td>

秩

</td>
<td>

特征多项式，特征值，迹，行列式，秩

<br>

行列式因子和不变因子

</td>
<td>

实对称矩阵：秩和符号差（正负惯性指数）

</td>
</tr>

<tr>
<td>性质</td>
<td>

秩相等（不变）

<br>

任意矩阵可以通过初等行变换和初等列变换化为相抵标准型。

<br>

行左列右。

<br>

任一可逆阵与任一不可逆阵均不相抵。

<br>

任意矩阵经过有限次初等行变换可以化为行阶梯矩阵。

<br>

任意可逆阵可仅通过初等行变换或仅通过初等列变换变为单位阵。

<br>

任意可逆阵可以表示为有限个初等矩阵的积。

<br>

$$\mathbf{P}_{ij}^{- 1} = \mathbf{P}_{ij}$$

$$\mathbf{P}_{i}(c)^{- 1} = \mathbf{P}_{i}\left( \frac{1}{c} \right)$$

$$\mathbf{T}_{ij}(c)^{- 1} = \mathbf{T}_{ij}( - c)$$

$$\left| \mathbf{P}_{ij} \right| = - 1$$

$$\left| \mathbf{P}_{i}(c) \right| = c$$

$$\left| \mathbf{T}_{ij}(c) \right| = 1$$

</td>
<td>

特征多项式，特征值，迹，行列式，秩相等（不变）

<br>

$$\left| \mathbf{A} \right| = \left| \mathbf{B} \right| = \prod_{i = 1}^{n}\lambda_{i}$$

$$tr\left( \mathbf{A} \right) = tr\left( \mathbf{B} \right) = \sum_{i = 1}^{n}\lambda_{ii}$$

<br>

仅纯量阵$c\mathbf{I}$没有除本身外的相似矩阵

<br>

$$\mathbf{A}'相似于\mathbf{B}'$$

$$\mathbf{A}^{*}相似于\mathbf{B}^{*}$$

$$\mathbf{A}^{- 1}相似于\mathbf{B}^{- 1}$$

<br>

$\mathbf{A}^{n}$相似于$\mathbf{B}^{n}$

<br>

$\mathbf{A} + k\mathbf{I}$相似于$\mathbf{B} + k\mathbf{I}$

</td>
<td>

秩，符号差，正惯性指数，负惯性指数相等（不变）

</td>
</tr>

<tr>
<td>关系</td>
<td colspan="3">

任意方阵相似必相抵，合同必相抵。

<br>

两实对称阵相似一定合同，合同不一定相似。

<br>

实对称阵即可相似对角化，又可合同对角化。

<br>

实对称阵既相似又合同于对角阵，且变换为对角阵的变换矩阵为正交矩阵。

</td>
</tr>

</tbody>
</table>
</div>
