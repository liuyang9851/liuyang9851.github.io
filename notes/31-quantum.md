---
title: 量子物理
description: 黑体辐射与普朗克公式、光电效应、康普顿散射、玻尔氢原子模型、不确定性原理、波函数与薛定谔方程、一维无限深方势阱、四个量子数与泡利不相容原理。
---

# 量子物理

[[toc]]

$$M_{\lambda}(T) = \frac{dM(T)}{d\lambda}$$

M(T) = ∫0+∞Mλ(T)dλ

![黑体辐射的辐出度随波长变化曲线：不同温度下曲线的峰值波长满足维恩位移定律](/images/physics/blackbody-radiation.png)

吸收比α(λ, T)和反射比ρ(λ, T)

物体在温度为T时吸收/反射的能量与入射能量之比。不透明物体有

α(λ, T) + ρ(λ, T) = 1

绝对黑体在任何温度下α(λ, T) = 1，ρ(λ, T) = 0

### 基尔霍夫定律

任何物体的单色辐出度和单色吸收比之比，都等于同一温度下绝对黑体的单色辐出度。

$$\frac{M_{\lambda}(T)}{\alpha(\lambda,T)} = M_{0\lambda}(T)$$

斯特藩—玻尔兹曼定律

绝对黑体的辐出度与温度的四次方成正比。

M0(T) = σT4

其中σ是一常量。

### 维恩位移定律

单色辐出度最大值所对应的波长λm（峰值波长）与温度T之积为一定值b。

λmT = b

### 维恩公式

$$M_{0\lambda}(T) = \frac{c_{1}}{\lambda^{5}}e^{- \frac{c_{2}}{\lambda T}}$$

瑞利—金斯公式（k是玻尔兹曼常量）

$$M_{0\lambda}(T) = \frac{2\pi ckT}{\lambda^{4}}$$

### 普朗克（黑体辐射）公式

$$M_{0\lambda}(T) = \frac{2\pi hc^{2}}{\lambda^{5}}\frac{1}{e^{hc\text{/}k\lambda T} - 1}$$

## 光电效应

![光电效应实验曲线：遏止电压 U₀ 与入射光频率 ν 的线性关系](/images/physics/photoelectric-effect.png)

### 光电效应方程

$$\frac{1}{2}mv_{0}^{2} = h\nu - eU_{k} = h\left( \nu - \nu_{0} \right) = eU_{0}$$

Ek = ε − A

其中

$$\nu_{0} = \frac{A}{h}\text{为截止频率，}$$

$$U_{k} = \frac{A}{e}\text{为溢出电压，}$$

$$U_{0} = \frac{h}{e}\nu - U_{k}\text{为截止电压，}$$

$$E_{k} = \frac{1}{2}mv_{0}^{2}\text{为最大初动能，}$$

ε = hν为光子的能量，

A = eUk为逸出功，逸出功只与材料有关。

### 光强

I = nhν

其中n为单位时间单位面积的光子数。

### 康普顿散射

当X射线被物质散射时，在被散射的X射线中，除了波长不变的散射光λ0外，还有波长增大的散射光λ出现。这种改变波长的散射称为康普顿效应。结论如下：

θ = 0时，Δλ = λ − λ0 = 0。

θ与Δλ成正相关，且该关系与散射物质无关，即不同物质同一θ下Δλ相等。（$\Delta\lambda = 2\frac{h}{m_{e}c}\sin^{2}\frac{\theta}{2}$）

θ越大，新散射波段λ占比越大。

散射物质原子序数越大，原波段占比程度越大。

## 玻尔氢原子模型

hν = En − Em

![玻尔氢原子模型示意图：电子在量子化轨道上绕核做圆周运动](/images/physics/bohr-model.png)

由

$$\left\{ \begin{array}{r}
\frac{1}{4\pi\varepsilon_{0}}\frac{e^{2}}{r^{2}} = m\frac{v_{n}^{2}}{r},\ \ \text{库仑力下做圆周运动} \\
L = mvr = n\hslash,\ \ \text{角动量量子化条件}\ \ 
\end{array} \right.\ $$

得

$$v_{n} = \frac{1}{2\varepsilon_{0}}\frac{e^{2}}{nh}$$

$$r_{n} = n^{2}\frac{\varepsilon_{0}h^{2}}{\pi me^{2}} = n^{2}r_{1}$$

$$E_{kn} = \frac{1}{2}mv_{n}^{2} = \frac{1}{n^{2}}\frac{me^{4}}{8\varepsilon_{0}^{2}h^{2}} = \frac{1}{n^{2}}E_{k1}$$

$$E_{pn} = - \frac{e^{2}}{4\pi\varepsilon_{0}r_{n}} = - \frac{1}{n^{2}}\frac{me^{4}}{4\varepsilon_{0}^{2}h^{2}} = \frac{1}{n^{2}}E_{p1}$$

$$E_{n} = E_{kn} + E_{pn} = - \frac{1}{n^{2}}\frac{me^{4}}{8\varepsilon_{0}^{2}h^{2}} = \frac{1}{n^{2}}E_{1}$$

$$\nu = \frac{E_{n} - E_{m}}{h} = \frac{me^{4}}{8\varepsilon_{0}^{2}h^{3}}\left( \frac{1}{m^{2}} - \frac{1}{n^{2}} \right) = - \frac{E_{1}}{h}\left( \frac{1}{m^{2}} - \frac{1}{n^{2}} \right)$$

### 广义巴尔默公式

$$\sigma_{mn} = R\left( \frac{1}{m^{2}} - \frac{1}{n^{2}} \right) = \frac{me^{4}}{8\varepsilon_{0}^{2}h^{3}c}\left( \frac{1}{m^{2}} - \frac{1}{n^{2}} \right)$$

其中σmn是从En跃迁Em到时发出的光谱线的波数（频率的倒数）

### 求解薛定谔方程给出的氢原子模型

$$\text{能量量子化：}E_{n} = - \frac{1}{n^{2}}\frac{me^{4}}{8\varepsilon_{0}^{2}h^{2}}$$

角动量量子化：轨道角动量：$L = \sqrt{l(l + 1)}\hslash$

角动量在Z轴（外磁场方向）的投影：LZ = mlℏ，在某一l下的ml的数量决定了角动量有几种取向。

$$\text{自旋量子数：}s = \frac{1}{2}$$

$$\text{电子自旋角动量：}S = \sqrt{s(s + 1)}\hslash = \frac{\sqrt{3}}{2}\hslash$$

$$\text{自旋角动量在}Z\text{轴的投影：}S_{Z} = m_{s}\hslash = \pm \frac{1}{2}\hslash$$

左图：

$$
l = 1,\ \ m_{l} = 0, \pm 1,\ \ L = \sqrt{l(l + 1)}\hslash = \sqrt{2}\hslash,\ \ L_{Z} = m_{l}\hslash = 0, \pm \hslash
$$

右图：

$$
l = 2,\ \ m_{l} = 0, \pm 1, \pm 2,\ \ L = \sqrt{l(l + 1)}\hslash = \sqrt{6}\hslash,\ \ L_{Z} = m_{l}\hslash = 0, \pm \hslash, \pm 2\hslash
$$

![自旋角动量在 Z 轴投影的量子化示意图：S_Z = ±ħ/2](/images/physics/spin-quantization.png)![自旋量子化示意图（续）：左图与右图的对比](/images/physics/spin-quantization-2.png)

## 不确定性原理

$$\left\{ \begin{array}{r}
\Delta x\Delta p_{x} \geq \frac{\hslash}{2} \\
\Delta y\Delta p_{y} \geq \frac{\hslash}{2} \\
\Delta z\Delta p_{z} \geq \frac{\hslash}{2}
\end{array} \right.\ ,\ \ \Delta E\Delta t \geq \frac{\hslash}{2}$$

## 波函数

自由粒子的波函数为

$$\psi(x,t) = \psi_{0}e^{- \frac{i}{\hslash}(Et - px)}$$

$$\psi\left( \mathbf{r},t \right) = \psi_{0}e^{- \frac{i}{\hslash}\left( Et - p_{x}x - p_{y}y - p_{z}z \right)} = \psi_{0}e^{- \frac{i}{\hslash}\left( Et - \mathbf{p} \cdot \mathbf{r} \right)}$$

是一个单值、有限、连续函数。

其中是E粒子的能量，p是粒子的动量，r是粒子的位矢。

### 粒子的概率密度

|ψ(r, t)|2 = ψ*(r, t)ψ(r, t)

表示粒子在t时刻在r处单位体积内出现的概率。

### 波函数的归一化条件

∭|ψ|2dxdydz = 1, ∫−∞+∞|ψ|2dV = 1

薛定谔方程（不适用于m0 = 0的粒子，是非相对论结果）

### 自由运动粒子的含时薛定谔方程

$$- \frac{\hslash^{2}}{2m}\frac{\partial^{2}\psi}{\partial x^{2}} + U(x,t)\psi = i\hslash\frac{\partial\psi}{\partial t}$$

$$- \frac{\hslash^{2}}{2m}\nabla^{2}\psi + U\left( \mathbf{r},t \right)\psi = i\hslash\frac{\partial\psi}{\partial t},\ \ \text{其中}\nabla^{2} = \frac{\partial^{2}}{\partial x^{2}} + \frac{\partial^{2}}{\partial y^{2}} + \frac{\partial^{2}}{\partial z^{2}}$$

其中U(r, t)是粒子的势能。

记忆：对于非相对论情况，有

$$\frac{P^{2}}{2m} + U\left( \mathbf{r},t \right) = E$$

分别对应薛定谔方程的左右。

### 定态薛定谔方程

考虑U(x, t)与t无关，则波函数

$$
\psi\left( \mathbf{r},t \right) = \psi\left( \mathbf{r} \right)f(t) = \psi\left( \mathbf{r} \right)e^{- \frac{i}{\hslash}Et}
$$

$$- \frac{\hslash^{2}}{2m}\nabla^{2}\psi\left( \mathbf{r} \right) + U\left( \mathbf{r} \right)\psi\left( \mathbf{r} \right) = E\psi\left( \mathbf{r} \right)$$

## 一维无限深方势阱

势阱位于(0, a)，经计算可得

处于势阱中质量为m的粒子在束缚态能级为n时具有的能量为（n ≥ 1）

$$E_{n} = \left( \frac{\pi^{2}\hslash^{2}}{2ma^{2}} \right)n^{2} = n^{2}E_{1}$$

对应的波函数为

$$\psi_{n}(x) = \left\{ \begin{array}{r}
\sqrt{2\text{/}a}\sin\frac{n\pi x}{a},\ \ x \in (0,a) \\
0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ ,\ \ \text{其他}\ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

对应的粒子出现位置的概率密度|ψ(x, t)|2为驻波形式，两端点处概率密度为0，区间内概率密度最大点有n个，概率密度最小点有n − 1个。

![一维无限深方势阱中粒子的波函数与概率密度分布示意图](/images/physics/infinite-well-wavefunction.png)

### 原子的四个量子数

主量子数→角量子数→磁量子数，自旋量子数

$$n\underset{}{\overset{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }{\rightarrow}}l\underset{}{\overset{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }{\rightarrow}}m_{l},\ \ {\ \ \ \ \ \ \ \ \ m}_{s}$$

$$\lbrack 1, + \infty) \rightarrow \lbrack 0,n - 1\rbrack \rightarrow \lbrack - l,l\rbrack,\ \  \pm \frac{1}{2}\ \ \ \ \ \ $$

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

n

</th>
<th>

[1, +∞)

</th>
<th>

其值决定原子中电子的能量。

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

l

</td>
<td>

[0, n − 1]

</td>
<td>

其值决定原子中电子的角动量。由于轨道磁矩与自旋磁矩间的相互作用，l对能量也有一定影响，l又称副量子数。

</td>
</tr>
<tr>
<td>

ml

</td>
<td>

[−l, l]

</td>
<td>

其值决定电子轨道角动量在外磁场中的取向。

</td>
</tr>
<tr>
<td>

ms

</td>
<td>

$$\pm \frac{1}{2}$$

</td>
<td>

其值决定电子自旋角动量在外磁场中的取向，同时还影响电子在外磁场中的能量。

</td>
</tr>
</tbody>
</table>
</div>

### 泡利不相容原理

在一个原子中，任何两个电子不可能具有完全相同的一组量子数(n, l, ml, ms)。

### 原子的壳层结构

<div class="table-scroll">
<table style="width:55%;">

<thead>
<tr>
<th>

主量子数n

</th>
<th>

1

</th>
<th>

2

</th>
<th>

3

</th>
<th>

4

</th>
<th>

5

</th>
<th>

6

</th>
<th>

7

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

（主）壳层名

</td>
<td>

K

</td>
<td>

L

</td>
<td>

M

</td>
<td>

N

</td>
<td>

O

</td>
<td>

P

</td>
<td>

Q

</td>
</tr>
<tr>
<td>

量子态数

（能容纳的电子数）

</td>
<td>

2

</td>
<td>

8

</td>
<td>

18

</td>
<td>

32

</td>
<td>

50

</td>
<td>

72

</td>
<td>

98

</td>
</tr>
<tr>
<td>

含有的支壳层

l ∈ [0, n − 1]

</td>
<td>

l=

</td>
<td>

0

1

2

3

4

5

6

</td>
<td>

1s

</td>
<td>

2s

2p

</td>
<td>

3s

3p

3d

</td>
<td>

4s

4p

4d

4f

</td>
<td>

5s

5p

5d

5f

5g

</td>
<td>

6s

6p

6d

6f

6g

6h

</td>
<td>

7s

7p

7d

7f

7g

7h

7i

</td>
</tr>
</tbody>
</table>
</div>

<div class="table-scroll">
<table style="width:59%;">

<thead>
<tr>
<th>

角量子数l

</th>
<th>

0

</th>
<th>

1

</th>
<th>

2

</th>
<th>

3

</th>
<th>

4

</th>
<th>

5

</th>
<th>

6

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

支壳层名

</td>
<td>

s

</td>
<td>

p

</td>
<td>

d

</td>
<td>

f

</td>
<td>

g

</td>
<td>

h

</td>
<td>

i

</td>
</tr>
<tr>
<td>

磁量子数ml

mi ∈ [−l, l]

</td>
<td>

0

</td>
<td>

0

±1

</td>
<td>

0

±1

±2

</td>
<td>

0

±1

±2

±3

</td>
<td>

0

±1

±2

±3

±4

</td>
<td>

0

±1

±2

±3

±4

±5

</td>
<td>

0

±1

±2

±3

±4

±5

±6

</td>
</tr>
<tr>
<td>

1

</td>
<td>

3

</td>
<td>

5

</td>
<td>

7

</td>
<td>

9

</td>
<td>

11

</td>
<td>

13

</td>
</tr>
<tr>
<td>

量子态数

（能容纳的电子数）

（磁量子数ml × 2）

</td>
<td>

2

</td>
<td>

6

</td>
<td>

10

</td>
<td>

14

</td>
<td>

18

</td>
<td>

22

</td>
<td>

16

</td>
</tr>
</tbody>
</table>
</div>

能量最低原理对应的经验公式

1, 22, 33, 434, 545, 6456, 7567, ⋯

n + 0.7l

$$\left\{ \begin{array}{r}
3d:n = 3,l = 2,n + 0.7l = 4.4 \\
4s:n = 4,l = 0,n + 0.7l = 4\ \ \ 
\end{array} \right.\  \Rightarrow 3d > 4s$$
