---
title: 热学
description: 理想气体状态方程、压强与温度公式、自由度与能量均分定理、内能、麦克斯韦速率分布律、热力学第一定律、摩尔热容、等值过程、热机效率与卡诺循环。
---

# 热学

[[toc]]

## 热学

## 理想气体状态方程

由实验，有

$$\frac{pV}{T} = C$$

特别地有一组数据（标准状态）

$$T_{0} = 273.15K\text{，}p_{0} = 1.013 \times 10^{5}Pa\text{，}V_{0} = \frac{M}{M_{mol}}V_{mol} = \frac{M}{M_{mol}} \cdot 22.4L$$

则相应地得出

$$pV = CT = \frac{p_{0}V_{0}}{T_{0}}T = \frac{p_{0}V_{mol}}{T_{0}}\frac{M}{M_{mol}}T\overset{R = \frac{p_{0}V_{mol}}{T_{0}}}{=}R\frac{M}{M_{mol}}T = R\frac{Nm}{N_{A}m}T = N\frac{R}{N_{A}}T\left\{ \begin{array}{r}
\overset{k_{B} = \frac{R}{N_{A}}}{=}Nk_{B}T \\
\overset{\nu = \frac{N}{N_{A}}}{=}\nu RT\ \ \ 
\end{array} \right.\ $$

$$p = \frac{N}{V}k_{B}T\overset{n = \frac{N}{V}}{=}nk_{B}T$$

其中R = 8.31J ⋅ mol−1 ⋅ K−1称为普适气体常量，kB = 1.38 × 10−23J ⋅ K−1为玻尔兹曼常量，p为气体的压强，V为气体的体积，T为气体的温度，M为气体的质量，Mmol为气体摩尔质量，N为气体所含分子数，m为每个气体分子的质量，ν为气体的物质的量（摩尔数），n为单位体积的分子数（分子数密度）。

### 气体分子平均速度

$$\overline{v_{x}} = \left( \sum_{i = 1}^{N}v_{ix} \right)\text{/}N = 0\text{，}\overline{v_{y}} = \left( \sum_{i = 1}^{N}v_{iy} \right)\text{/}N = 0\text{，}\overline{v_{z}} = \left( \sum_{i = 1}^{N}v_{iz} \right)\text{/}N = 0$$

$$\text{定义}\overline{v_{x}^{2}} = \left( \sum_{i = 1}^{N}v_{ix}^{2} \right)\text{/}N\text{，}\overline{v_{y}^{2}} = \left( \sum_{i = 1}^{N}v_{iy}^{2} \right)\text{/}N\text{，}\overline{v_{z}^{2}} = \left( \sum_{i = 1}^{N}v_{iz}^{2} \right)\text{/}N\text{，由}\left\{ \begin{array}{r}
\overline{v_{x}^{2}} = \overline{v_{y}^{2}} = \overline{v_{z}^{2}}\ \ \ \ \ \ \ \ \ \  \\
\overline{v_{x}^{2}} + \overline{v_{y}^{2}} + \overline{v_{z}^{2}} = \overline{v^{2}}
\end{array} \right.\ \text{，得}$$

$$\overline{v_{x}^{2}} = \overline{v_{y}^{2}} = \overline{v_{z}^{2}} = \frac{1}{3}\overline{v^{2}}$$

### 理想气体的压强公式

$$p = \frac{1}{3}nm\overline{v^{2}}\overset{\overline{\varepsilon_{t}} = \frac{1}{2}m\overline{v^{2}}}{=}\frac{2}{3}n\overline{\varepsilon_{t}}$$

其中$\overline{\varepsilon_{t}}$称为气体分子的平均平动动能

### 理想气体的温度公式

$$\text{联立}\left\{ \begin{array}{r}
p = nk_{B}T \\
p = \frac{2}{3}n\overline{\varepsilon_{t}}
\end{array} \right.\ \text{，得分子平均平动动能}\overline{\varepsilon_{t}} = \frac{3}{2}kT$$

### 气体分子的方均根速率

$$\sqrt{\overline{v^{2}}} = \sqrt{\frac{3p}{nm}}\overset{\rho = nm}{=}\sqrt{\frac{3p}{\rho}}$$

其中ρ = nm称为气体密度

### 气体分子的自由度

<div class="table-scroll">
<table style="width:100%;">

<thead>
<tr>
<th>

分子类型

</th>
<th>

平动自由度t

</th>
<th>

转动自由度r

</th>
<th>

振动自由度s

</th>
<th>

自由度

</th>
<th>

i = t + r + 2s

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

单原子分子

</td>
<td>

3

</td>
<td>

0

</td>
<td>

0

</td>
<td>

3

</td>
<td>

3

</td>
</tr>
<tr>
<td>

双原子刚性分子

</td>
<td>

3

</td>
<td>

2

</td>
<td>

0

</td>
<td>

5

</td>
<td>

5

</td>
</tr>
<tr>
<td>

双原子非刚性分子

</td>
<td>

3

</td>
<td>

2

</td>
<td>

1

</td>
<td>

6

</td>
<td>

7

</td>
</tr>
<tr>
<td>

多原子刚性分子

（各原子不排列在一条直线上）

</td>
<td>

3

</td>
<td>

3

</td>
<td>

0

</td>
<td>

6

</td>
<td>

6

</td>
</tr>
<tr>
<td>

多原子非刚性分子

</td>
<td>

3

</td>
<td>

3

</td>
<td>

3n − 6

</td>
<td>

3n

</td>
<td>

6n − 6

</td>
</tr>
</tbody>
</table>
</div>

### 能量按自由度均分定理

在温度为T的平衡态下，气体分子每个自由度的平均动能都相等，其大小都等于kT/2。

记忆：由

$$\left\{ \begin{array}{r}
\overline{\varepsilon_{t}} = \frac{1}{2}mv^{2} = \frac{3}{2}kT\ \ \ \  \\
\overline{v_{x}^{2}} = \overline{v_{y}^{2}} = \overline{v_{z}^{2}} = \frac{1}{3}\overline{v^{2}}
\end{array} \right.\ $$

得

$$\frac{1}{2}m\overline{v_{x}^{2}} = \frac{1}{2}m\overline{v_{y}^{2}} = \frac{1}{2}m\overline{v_{z}^{2}} = \frac{1}{2}m\left( \frac{1}{3}\overline{v^{2}} \right) = \frac{1}{3}\left( \frac{1}{2}m\overline{v^{2}} \right) = \frac{1}{3}\left( \frac{3}{2}kT \right) = \frac{1}{2}kT$$

表明分子在每一个平动自由度上具有相同的平均平动动能，大小为kT/2，而每个转动自由度和振动自由度的平均动能大小也等于每一个平动自由度的平均平动动能，即kT/2。

单个气体分子的平均总动能

$$\overline{\varepsilon_{k}} = \frac{1}{2}(t + r + r)kT$$

其中t是平动自由度，r是转动自由度，r是振动自由度。

单个气体分子的平均总能量

$$\overline{\varepsilon} = \frac{1}{2}(t + r + 2s)kT\overset{i = t + r + 2s}{=}\frac{i}{2}kT$$

这是因为振动自由度下除了振动动能还有振动势能，且振动势能等于振动动能。

### 理想气体的内能

理想气体的内能为气体分子的能量与分子间势能之和，因为理想气体要求不考虑分子间作用力，所以分子间势能为0。

1mol理想气体的内能为

$$E_{mol} = \frac{i}{2}RT$$

质量为M，摩尔质量Mmol为的理想气体的内能为

$$E = \frac{M}{M_{mol}}\frac{i}{2}RT = \nu\frac{i}{2}RT$$

## 麦克斯韦速率分布律

平衡态下，气体分子速率在v ∼ v + dv区间的分子数占总分子数的百分比为

$$\frac{dN}{N} = 4\pi\left( \frac{m}{2\pi kT} \right)^{3\text{/}2}v^{2}e^{- mv^{2}\text{/}2kT}dv$$

对应速率分布函数

$$f(v) = 4\pi\left( \frac{m}{2\pi kT} \right)^{3\text{/}2}v^{2}e^{- mv^{2}\text{/}2kT}$$

在有限速率区间v1 ∼ v2内分子数占总分子树的百分比为

∫v1v2f(v)dv

### 气体分子的三个速率

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

最概然速率vp

</th>
<th>

平均速率$\overline{v}$

</th>
<th>

方均根速率$\sqrt{\overline{v^{2}}}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$$\sqrt{\frac{2kT}{m}} = \sqrt{\frac{2RT}{M_{mol}}} \approx 1.41\sqrt{\frac{RT}{M_{mol}}}$$

</td>
<td>

$$\sqrt{\frac{8kT}{\pi m}} = \sqrt{\frac{8RT}{\pi M_{mol}}} \approx 1.60\sqrt{\frac{RT}{M_{mol}}}$$

</td>
<td>

$$\sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M_{mol}}} \approx 1.73\sqrt{\frac{RT}{M_{mol}}}$$

</td>
</tr>
</tbody>
</table>
</div>

## 热力学第一定律

系统从外界吸收的热量Q等于系统内能的增量ΔE和系统对外做功A的和

Q = ΔE + A

<div class="table-scroll">
<table style="width:49%;">

<thead>
<tr>
<th></th>
<th>

> 0

</th>
<th>

< 0

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

Q

</td>
<td>

系统从外界吸收热量

</td>
<td>

系统向外界放出热量

</td>
</tr>
<tr>
<td>

A

</td>
<td>

系统对外界做功

</td>
<td>

外界对系统做功

</td>
</tr>
<tr>
<td>

ΔE

</td>
<td>

系统的内能增加

</td>
<td>

系统的内能减少

</td>
</tr>
</tbody>
</table>
</div>

热容（量）

$$C = \frac{dQ}{dT}\ \left( J \cdot K^{- 1} \right)$$

比热（容）：c (J ⋅ kg−1 ⋅ K−1)

摩尔热容量：Cm (J ⋅ mol−1 ⋅ K−1)

$$C = Mc\ \ \ C = \frac{M}{M_{mol}}C_{m}$$

### 等体摩尔热容

在等体过程中，气体的吸热为

Q = νCV, m(T2 − T1)

$$C_{V,m} = \frac{dQ\left. \  \right|_{V}}{dT}\underset{dA = 0}{\overset{dQ = dE + dA}{=}}\frac{dE}{dT}\underset{\nu = 1}{\overset{dE = \frac{i}{2}\nu RdT}{=}}\frac{i}{2}R\overset{E = \frac{i}{2}\nu RT}{\Rightarrow}E = \nu C_{V,m}T$$

$$C_{V,m} = \frac{i}{2}R\text{，}E = \nu C_{V,m}T$$

### 等压摩尔热容

在等压过程中，气体的吸热为

Q = νCV, m(T2 − T1)

因为

$$pV = \nu RT\overset{\nu = 1}{=}RT \Rightarrow pdV + Vdp = RdT\underset{dp = 0}{\overset{\ p\text{不变}\ }{\Rightarrow}}pdV = RdT\overset{\ dA = pdV\ }{\Rightarrow}dA = RdT$$

所以

$$C_{p,m} = \frac{dQ\left. \  \right|_{p}}{dT}\overset{dQ = dE + dA}{=}\frac{(dE + dA)\left. \  \right|_{p}}{dT}\overset{dA = RdT}{=}\frac{dE + RdT}{dT}\overset{C_{V,m} = \frac{dE}{dT}}{=}C_{V,m} + R$$

$$C_{p,m} = C_{V,m} + R = \left( \frac{i}{2} + 1 \right)R$$

### 等值过程系统的做功、吸热和内能变化

<div class="table-scroll">
<table style="width:100%;">

<thead>
<tr>
<th>

等值过程

</th>
<th>

等体过程

(n = +∞)

</th>
<th>

等压过程

(n = 0)

</th>
<th>

等温过程

(n = 1)

</th>
<th>

绝热过程

(n = γ)

</th>
<th>

多方过程

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

图像

</td>
<td>

竖直直线

</td>
<td>

水平直线

</td>
<td>

双曲线

</td>
<td>

pVγ = C

γ = Cp, m/CV, m

</td>
<td>

pVn = C

</td>
</tr>
<tr>
<td>

状态参量

</td>
<td>

$$\frac{p_{1}}{T_{1}} = \frac{p_{2}}{T_{2}}$$

</td>
<td>

$$\frac{V_{1}}{T_{1}} = \frac{V_{2}}{T_{2}}$$

</td>
<td>

p1V1 = p2V2

</td>
<td>

p1V1γ = p2V2γ

</td>
<td>

p1V1n = p2V2n

</td>
</tr>
<tr>
<td>

做功A

∫V1V2pdV

</td>
<td>

0

</td>
<td>

p(V2 − V1)

νR(T2 − T1)

</td>
<td>

$$\nu RT\ln\frac{V_{2}}{V_{1}}$$

</td>
<td>

$$\frac{p_{1}V_{1} - p_{2}V_{2}}{\gamma - 1}$$

</td>
<td>

$$\frac{p_{1}V_{1} - p_{2}V_{2}}{n - 1}\ \ (n \neq 1)$$

</td>
</tr>
<tr>
<td>

吸热Q

A + ΔE

</td>
<td>

νCV, m(T2 − T1)

</td>
<td>

νCp, m(T2 − T1)

</td>
<td>

$$\nu RT\ln\frac{V_{2}}{V_{1}}$$

</td>
<td>

0

</td>
<td>

$$\nu\left( C_{V,m} - \frac{R}{n - 1} \right)\left( T_{2} - T_{1} \right)$$

(n ≠ 1)

</td>
</tr>
<tr>
<td>

内能增量ΔE

νCV, m(T2 − T1)

</td>
<td></td>
<td></td>
<td></td>
<td>

−A

</td>
<td></td>
</tr>
</tbody>
</table>
</div>

## 热机的效率

$$\eta = \frac{W_{\text{有}}}{Q_{\text{吸}}} = \frac{Q_{\text{吸}} - Q_{\text{放}}}{Q_{\text{吸}}} = 1 - \frac{Q_{\text{放}}}{Q_{\text{吸}}}$$

## 卡诺循环

$$\eta = 1 - \frac{T_{2}}{T_{1}}$$

dS = 2πrdr   dV = 4πr2dr
