---
title: 质点运动学
description: 位矢与位移、速度与加速度、自然坐标系下的加速度分解、角量与线量。
---

# 质点运动学

[[toc]]

## 质点运动学

位矢（位置矢量）

r = r(t) = x(t)i + y(t)j + z(t)k = xi + yj + zk

### 位矢的大小

$$r = \sqrt{x^{2} + y^{2} + z^{2}}$$

速度（瞬时速度）

$$\mathbf{v} = \frac{d\mathbf{r}}{dt} = \frac{d\mathbf{x}}{dt}\mathbf{i} + \frac{d\mathbf{y}}{dt}\mathbf{i} + \frac{d\mathbf{z}}{dt}\mathbf{i} = v_{x}\mathbf{i} + v_{y}\mathbf{j} + v_{z}\mathbf{k}$$

### 速率

$$v = \sqrt{v_{x}^{2} + v_{y}^{2} + v_{z}^{2}}$$

### 加速度

$$\mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{d^{2}\mathbf{r}}{dt^{2}} = a_{x}\mathbf{i} + a_{y}\mathbf{j} + a_{z}\mathbf{k}$$

### 加速度的大小

$$a = \sqrt{a_{x}^{2} + a_{y}^{2} + a_{z}^{2}}$$

### 自然坐标系下加速度分解

$$\mathbf{v} = \frac{ds}{dt}\mathbf{e}_{t} = v\mathbf{e}_{t}$$

$$\mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{d\left( v\mathbf{e}_{t} \right)}{dt} = \frac{dv}{dt}\mathbf{e}_{t} + \frac{d\mathbf{e}_{t}}{dt}v = \frac{dv}{dt}\mathbf{e}_{t} + \frac{v^{2}}{r}\mathbf{e}_{n} = \mathbf{a}_{t} + \mathbf{a}_{n}$$

$$\text{其中}\mathbf{a}_{t} = \frac{dv}{dt}\mathbf{e}_{t}\text{称为切向加速度，}\mathbf{a}_{n} = \frac{v^{2}}{r}\mathbf{e}_{n}\text{称为法向}\text{/}\text{向心加速度。}$$

### 向心加速度公式的推导

由上，$\mathbf{a} = \frac{dv}{dt}\mathbf{e}_{t} + \frac{d\mathbf{e}_{t}}{dt}v$，其中$\mathbf{a}_{t} = \frac{dv}{dt}\mathbf{e}_{t}\text{称为切向加速度}$，下面证明

$$\mathbf{a}_{n} = \frac{d\mathbf{e}_{t}}{dt}v = \frac{v^{2}}{r}\mathbf{e}_{n}$$

如图，质点在绕坐标原点做圆周运动的某时刻的速度为$v\overrightarrow{\mathbf{e}_{t}}\ $，其中

et = (−sin θ，cos θ)

就$v\overrightarrow{\mathbf{e}_{t}}$对t求导，有

$$\frac{dv\overrightarrow{\mathbf{e}_{t}}}{dt} = v\frac{d\mathbf{e}_{t}}{dt} = v\frac{d( - \sin\theta\mathbf{i} + \cos\theta\mathbf{j})}{dt} = v\left( - \cos\theta\frac{d\theta}{dt}\mathbf{i} - \sin\theta\frac{d\theta}{dt}\mathbf{j} \right) = v\left( - \cos\theta\omega\mathbf{i} - \sin\theta\omega\mathbf{j} \right) = v\omega\left( - \cos\theta\mathbf{i} - \sin\theta\mathbf{j} \right)$$

可以看出其方向是与$v\overrightarrow{\mathbf{e}_{t}}$互相垂直的，大小

$$a_{n} = v\omega\sqrt{\left( - \cos\theta \right)^{2} + \left( - \sin\theta \right)^{2}} = v\omega$$

$$\text{故}\mathbf{a}_{n} = v\omega\mathbf{e}_{n} = \frac{v^{2}}{r}\mathbf{e}_{n}$$

### 角量与线量

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

物理量

</th>
<th>

线量

</th>
<th>

角量

</th>
<th>

线量与角量的关系

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

位移

</td>
<td>

s

</td>
<td>

θ

</td>
<td>

s = θr

</td>
<td>

$$a_{n} = \frac{v^{2}}{r}$$

</td>
</tr>
<tr>
<td>

速度

</td>
<td>

$$v = \frac{ds}{dt}$$

</td>
<td>

$$\omega = \frac{d\theta}{dt}$$

</td>
<td>

v = ωr

</td>
<td>

an = vω

</td>
</tr>
<tr>
<td>

加速度

</td>
<td>

$$a_{t} = \frac{dv}{dt} = \frac{d^{2}s}{dt^{2}}$$

</td>
<td>

$$\beta = \frac{d\omega}{dt} = \frac{d^{2}\theta}{dt^{2}}$$

</td>
<td>

at = βr

</td>
<td>

an = ω2r

</td>
</tr>
</tbody>
</table>
</div>
