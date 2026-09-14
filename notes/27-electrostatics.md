---
title: 静电场
description: 库仑定律、电场强度、电通量与高斯定理、环路定理、电势能与电势、场强与电势的关系、电容与电场能量、有电介质时的高斯定理。
---

# 静电场

[[toc]]

## 库伦定律

$$\mathbf{F} = \frac{1}{4\pi\varepsilon_{0}}\frac{q_{1}q_{2}}{r^{2}}\mathbf{r}^{0}$$

$$d\mathbf{B} = \frac{\mu_{0}}{4\pi}\frac{Id\mathbf{l} \times \mathbf{r}^{0}}{r^{2}} = \frac{\mu_{0}I}{4\pi r^{2}}d\mathbf{l} \times \mathbf{r}^{0}$$

### 电场强度

$$\mathbf{E} = \frac{\mathbf{F}}{q_{0}}$$

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

点电荷

</th>
<th>

连续分布线

</th>
<th>

连续分布面

</th>
<th>

连续分布体

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$$\mathbf{E} = \frac{1}{4\pi\varepsilon_{0}}\frac{q_{0}}{r^{2}}\mathbf{r}^{0}$$

</td>
<td>

$$\mathbf{E} = \frac{1}{4\pi\varepsilon_{0}}\int_{L}^{}\frac{\lambda dl}{r^{2}}\mathbf{r}^{0}$$

</td>
<td>

$$\mathbf{E} = \frac{1}{4\pi\varepsilon_{0}}\int_{S}^{}\frac{\sigma dS}{r^{2}}\mathbf{r}^{0}$$

</td>
<td>

$$\mathbf{E} = \frac{1}{4\pi\varepsilon_{0}}\int_{V}^{}\frac{\rho dV}{r^{2}}\mathbf{r}^{0}$$

</td>
</tr>
</tbody>
</table>
</div>

求场强

$$\left\{ \begin{array}{r}
dq = \lambda dl = \sigma dS = \rho dV \\
dE = \frac{dq}{4\pi\varepsilon_{0}r^{2}} \\
E = \int_{}^{}{dE}
\end{array} \right.\ $$

### 电通量

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

小面元dS⊥

</th>
<th>

任意小面元

</th>
<th>

任意曲面

</th>
<th>

闭合曲面

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

dϕe = EdS⊥

</td>
<td>

dϕe = E ⋅ dS

</td>
<td>

ϕe = ∫SE ⋅ dS

</td>
<td>

ϕe = ∮SE ⋅ dS

</td>
</tr>
</tbody>
</table>
</div>

### 高斯定理

$$\phi_{e} = \oint_{S}^{}{\mathbf{E} \cdot d\mathbf{S}} = \frac{\sum_{}^{}q_{i}}{\varepsilon_{0}}$$

静电力做功

$$A_{ab} = \frac{q_{0}q}{4\pi\varepsilon_{0}}\int_{r_{a}}^{r_{b}}{\frac{1}{r^{2}}dr} = \frac{q_{0}q}{4\pi\varepsilon_{0}}\left( \frac{1}{r_{a}} - \frac{1}{r_{b}} \right)$$

### 静电场的环路定理

∮E ⋅ dl = 0

### 电势能

Wa = q0∫a电势能零点E ⋅ dl

Wa = q0∫a∞E ⋅ dl

### 电势

$$V_{a} = \frac{W_{a}}{q_{0}} = \int_{a}^{\text{电势零点}}{\mathbf{E} \cdot d\mathbf{l}}$$

Va = ∫a∞E ⋅ dl

### 电势差

Uab = Va − Vb = ∫abE ⋅ dl

Aab = q0Uab

### 点电荷电场中的电势

$$V_{P} = \frac{q}{4\pi\varepsilon_{0}r_{P}}$$

### 连续分布带电体电场中的电势

$$V = \frac{1}{4\pi\varepsilon_{0}}\int_{}^{}\frac{dp}{r}$$

### 场强与电势的关系

$$E = - \nabla V = - gradV = - \left( \frac{dV}{dx}\mathbf{i} + \frac{dV}{dx}\mathbf{j} + \frac{dV}{dx}\mathbf{k} \right)$$

<div class="table-scroll">
<table>

<thead>
<tr>
<th></th>
<th>

点电荷

</th>
<th>

连续分布线

</th>
<th>

连续分布面

</th>
<th>

连续分布体

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$$\mathbf{E} = \frac{\mathbf{F}}{q_{0}} = \frac{1}{4\pi\varepsilon_{0}}\int_{}^{}\frac{dq}{r^{2}}\mathbf{r}^{0}$$

</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

$$V_{a} = \frac{W_{a}}{q_{0}} = \int_{a}^{\text{电势零点}}{\mathbf{E} \cdot d\mathbf{l}}$$

Va = ∫a∞E ⋅ dl

</td>
<td>

$$V_{P} = \frac{q}{4\pi\varepsilon_{0}r_{P}}$$

</td>
<td></td>
<td></td>
<td>

$$V = \frac{1}{4\pi\varepsilon_{0}}\int_{}^{}\frac{dp}{r}$$

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

圆环

</th>
<th>

直导线

</th>
<th>

圆盘

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

场强

</td>
<td>

$$\frac{q}{4\pi\varepsilon_{0}}\frac{x}{\left( R^{2} + x^{2} \right)^{3\text{/}2}}\mathbf{i}$$

$$x = \pm \frac{\sqrt{2}}{2}R\text{处取极大值}$$

</td>
<td>

$$\frac{\lambda}{4\pi\varepsilon_{0}d}\left( \begin{array}{r}
\sin\theta_{2} - \sin\theta_{1}\text{，} - \cos\theta_{2} + \cos\theta_{1}
\end{array} \right)$$

$$\frac{\lambda}{2\pi\varepsilon_{0}d}\mathbf{j}$$

</td>
<td>

$$\frac{\sigma}{2\varepsilon_{0}}\left( 1 - \frac{x}{\sqrt{R^{2} + x^{2}}} \right)\mathbf{i}$$

</td>
</tr>
<tr>
<td>

电势

</td>
<td>

$$\frac{q}{4\pi\varepsilon_{0}}\frac{1}{\sqrt{R^{2} + x^{2}}}$$

</td>
<td>

$$V_{p} - V_{p_{1}} = - \frac{\lambda}{2\pi\varepsilon_{0}}\ln d + C$$

</td>
<td></td>
</tr>
<tr>
<td>

无限平面

</td>
<td>

无限圆柱面

</td>
<td>

球壳

</td>
<td>

均匀带电球体

</td>
</tr>
<tr>
<td>

$$\frac{\sigma}{2\varepsilon_{0}}\mathbf{i}$$

</td>
<td>

$$\left\{ \begin{array}{r}
\ \ \ \ \ \ 0\ \ \ \ \ \ \ \ \ \ (r < R) \\
\frac{\lambda}{2\pi\varepsilon_{0}r}\mathbf{r}^{0}(r > R)
\end{array} \right.\ $$

</td>
<td>

$$\left\{ \begin{array}{r}
\ \ \ \ \ \ \ 0\ \ \ \ \ \ \ \ \ (r < R) \\
\frac{q}{4\pi\varepsilon_{0}r^{2}}\mathbf{r}^{0}(r > R)
\end{array} \right.\ $$

</td>
<td>

$$\left\{ \begin{array}{r}
\frac{qr}{4\pi\varepsilon_{0}R^{3}}\mathbf{r}^{0}(r < R) \\
\frac{q}{4\pi\varepsilon_{0}r^{2}}\mathbf{r}^{0}(r > R)
\end{array} \right.\ $$

</td>
</tr>
<tr>
<td></td>
<td>

$$\left\{ \begin{array}{r}
\frac{\lambda}{2\pi\varepsilon_{0}}\ln R + C(r < R) \\
\frac{\lambda}{2\pi\varepsilon_{0}}\ln r + C(r > R)
\end{array} \right.\ $$

</td>
<td>

$$\left\{ \begin{array}{r}
\frac{q}{4\pi\varepsilon_{0}}\frac{1}{R}(r < R) \\
\frac{q}{4\pi\varepsilon_{0}}\frac{1}{r}(r > R)
\end{array} \right.\ $$

</td>
<td></td>
</tr>
</tbody>
</table>
</div>

### 电容

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

定义

</th>
<th>

平行板电容器

</th>
<th>

球形电容器

</th>
<th>

圆柱形电容器

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

孤立导体：$C = \frac{q}{V}$

电容器：$C = \frac{q}{V_{A} - V_{B}}$

</td>
<td>

$$C = \frac{\varepsilon S}{d}$$

</td>
<td>

$$C = 4\pi\varepsilon\frac{R_{A}R_{B}}{R_{B} - R_{A}}$$

$$C = \left( \frac{1}{4\pi\varepsilon}\left( \frac{1}{R_{A}} - \frac{1}{R_{B}} \right) \right)^{- 1}$$

</td>
<td>

$$C = \frac{2\pi\varepsilon L}{\ln\frac{R_{B}}{R_{A}}}$$

</td>
</tr>
</tbody>
</table>
</div>

### 电容器的能量

$$W_{e} = \frac{1}{2}CU^{2} = \frac{Q^{2}}{2C} = \frac{1}{2}QU$$

哪个不变用哪个。

电场的能量密度

$$w_{e} = \frac{W_{e}}{V} = \frac{1}{2}\varepsilon_{0}\varepsilon_{r}E^{2} = \frac{1}{2}DE$$

### 电场的能量

$$W_{e} = \int_{V}^{}{dW_{e}} = \int_{V}^{}{\frac{1}{2}\varepsilon_{0}\varepsilon_{r}E^{2}dV}$$

积分区域为电场不为0的区域。

### 有电介质存在时的高斯定理

$$\oint_{S}^{}{\mathbf{D} \cdot d\mathbf{S}} = \oint_{S}^{}{\mathbf{(}\varepsilon_{0}\mathbf{E + P)} \cdot d\mathbf{S}} = \oint_{S}^{}{\varepsilon\mathbf{E}d\mathbf{S}} = \sum_{}^{}q_{0}$$

对于具有各向同性的电介质，有

D=ε0E + P=ε0E+ε0(εr − 1)E=ε0εrE=εEP = ε0(εr − 1)E
