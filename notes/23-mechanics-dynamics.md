---
title: 质点动力学与刚体
description: 动量与力、万有引力与胡克定律、动量定理、功与动能定理、势能、质心、力矩与角动量、刚体定轴转动、转动惯量。
---

# 质点动力学与刚体

[[toc]]

## 质点动力学

### 动量

p = mv

### 力

$$\mathbf{F} = \frac{d\mathbf{p}}{dt} = \frac{d\left( m\mathbf{v} \right)}{dt} = m\frac{d\mathbf{v}}{dt} + v\frac{dm}{dt} = m\mathbf{a}$$

### 万有引力定律

$$\mathbf{F} = - G\frac{m_{1}m_{2}}{r^{2}}\mathbf{r}_{0}$$

其中F表示m2受到m1的引力，r0表示从m1到m2的位矢。

### 胡克定律

F = −kx

其中质点的受力方向与弹簧形变方向相反。

### 动量定理

$$\mathbf{I}_{b} - \mathbf{I}_{a} = \int_{a}^{b}{\mathbf{F}dt} = \int_{a}^{b}{\frac{d\mathbf{p}}{dt}dt} = \int_{a}^{b}{d\mathbf{p}} = \int_{a}^{b}{md\mathbf{v}} = m\mathbf{v}_{b} - m\mathbf{v}_{a} = \mathbf{p}_{b} - \mathbf{p}_{a}$$

### 功

在恒力F下

A = F ⋅ Δr = |F||Δr|cos  < F，Δr>

### 变力做功

A = ∫dA = ∫abF⋅dr = ∫ab(Fxdx + Fydy + Fzdz)(dxi + dyj + dzk) = ∫ab(Fxdx + Fydy + Fzdz)

在此处键入公式。

### 动能定理

$$A = \int_{}^{}{dA} = \int_{a}^{b}{\mathbf{F \cdot}d\mathbf{r}} = \int_{a}^{b}{\frac{d\mathbf{p}}{dt}d\mathbf{r}} = \int_{a}^{b}{\frac{md\mathbf{v}}{dt}d\mathbf{r}} = \int_{a}^{b}{md\mathbf{v \cdot v}} = \frac{1}{2}m\mathbf{v}^{2}\left| \begin{array}{r}
b \\
a
\end{array} \right.\  = \frac{1}{2}mv_{b}^{2} - \frac{1}{2}mv_{a}^{2}$$

$$\int_{a}^{b}{md\mathbf{v \cdot v}} = \int_{a}^{b}{m\left( dv_{x} \cdot \mathbf{i} + dv_{y} \cdot \mathbf{j} + dv_{z} \cdot \mathbf{k} \right)\left( v_{x}\mathbf{i} + v_{y}\mathbf{j} + v_{z}\mathbf{k} \right)} = \int_{a}^{b}{m\left( v_{x}dv_{x} + v_{y}dv_{y} + v_{z}dv_{z} \right)} = \frac{1}{2}m\left( v_{x}^{2} + v_{y}^{2} + v_{z}^{2} \right)\left| \begin{array}{r}
b \\
a
\end{array} \right.\  = \frac{1}{2}mv^{2}\left| \begin{array}{r}
b \\
a
\end{array} \right.\ $$

### 势能

保守力从a点到b点做功为

A = ∫abF⋅dr = −(Epb − Epa)

保守力做功= −势能变化量

### 重力势能

$$A = \int_{a}^{b}{m\mathbf{g}d\mathbf{r}} = \int_{a}^{b}{m\mathbf{g}\left( dx\mathbf{i} + dy\mathbf{j} + dz\mathbf{k} \right)} = \int_{a}^{b}{mgdz} = mgz\left| \begin{array}{r}
b \\
a
\end{array} \right.\  = - \left( mgh_{a} - mgh_{b} \right) = - \left( E_{p_{b}} - E_{p_{a}} \right)$$

### 引力势能

$$A = \int_{a}^{b}{- G\frac{m_{1}m_{2}}{r^{2}}\mathbf{r}_{0}d\mathbf{r}} = - \left\lbrack \left( - G\frac{m_{1}m_{2}}{r_{a}} \right) - \left( - G\frac{m_{1}m_{2}}{r_{b}} \right) \right\rbrack = - \left( E_{p_{b}} - E_{p_{a}} \right)$$

### 弹性势能

$$A = \int_{a}^{b}{- kxdx} = - \frac{1}{2}kx^{2}\left| \begin{array}{r}
b \\
a
\end{array} \right.\  = - \left( \frac{1}{2}kx_{b}^{2} - \frac{1}{2}kx_{a}^{2} \right) = - \left( E_{p_{b}} - E_{p_{a}} \right)$$

## 质点系力学

### 质心的位矢

$$\mathbf{r}_{c} = \frac{\sum_{i}^{}{m_{i}\mathbf{r}_{i}}}{\sum_{i}^{}m_{i}} = \frac{\sum_{i}^{}{m_{i}\mathbf{r}_{i}}}{m}$$

### 质心的速度

在此处键入公式。

### 线量与角量

<div class="table-scroll">
<table style="width:55%;">

<thead>
<tr>
<th></th>
<th>

线量

</th>
<th>

角量

</th>
<th>

角量和线量的关系

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

位移

</td>
<td>

x

</td>
<td>

θ

</td>
<td></td>
</tr>
<tr>
<td>

速度

</td>
<td>

v

</td>
<td>

$$\mathbf{\omega =}\frac{d\mathbf{\theta}}{dt}$$

</td>
<td>

v = ω × r

</td>
</tr>
<tr>
<td>

加速度

</td>
<td>

a

</td>
<td>

$$\mathbf{\beta} = \frac{d\mathbf{\omega}}{dt}$$

</td>
<td>

a = β × r + ω × v=at+an

</td>
</tr>
</tbody>
</table>
</div>

### 力矩

Mz = R⊥ × F⊥

### 角动量

$$\mathbf{L}_{z} = \sum_{i}^{}{\Delta m_{i}r_{i}^{2}}\mathbf{\omega} = J\mathbf{\omega}$$

### 刚体定轴转动的转动定律

M = Jβ

### 常见刚体的转动惯量

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

细棒

（转动轴通过中心与棒垂直）

</th>
<th>

细棒

（转动轴通过棒的一端与棒垂直）

</th>
<th>

圆筒

（转动轴沿几何轴）

</th>
<th>

圆柱体

（转动轴沿几何轴）

</th>
<th>

薄圆环

（转动轴沿几何轴）

</th>
<th>

球体

（转动轴沿球的任一直径）

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$$J = \frac{ml^{2}}{12}$$

</td>
<td>

$$J = \frac{ml^{2}}{3}$$

</td>
<td>

$$J = \frac{m\left( R^{2} + r^{2} \right)}{2}$$

</td>
<td>

$$J = \frac{mR^{2}}{2}$$

</td>
<td>

J = mR2

</td>
<td>

$$J = \frac{2mR^{2}}{5}$$

</td>
</tr>
</tbody>
</table>
</div>
