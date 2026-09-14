---
title: 狭义相对论
description: 洛伦兹变换与速度变换、时间延缓、长度收缩、质量膨胀、相对论动量与能量。
---

# 狭义相对论

[[toc]]

## 洛伦兹变换

S系的坐标轴为x、y和z，S′系的坐标轴为x′、y′和z′。为了简单，让x、y和z轴分别平行于x′、y和z′轴，S′系相对于S系以不变速度u沿x轴的正方向运动，当t = t′ = 0时，S系和S′系的原点互相重合。同一个物理事件在S系和S′系中的时空坐标由下列关系式相联系：

$$\left\{ \begin{array}{r}
x' = \frac{x - ut}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \frac{x - \beta ct}{\sqrt{1 - \beta^{2}}} = \gamma(x - \beta tc)\ \ \ \  \\
y' = y\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
z' = z\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
t' = \frac{t - \left( u\text{/}c^{2} \right)x}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \frac{t - \beta x\text{/}c}{\sqrt{1 - \beta^{2}}} = \gamma\left( t - \beta x\text{/}c \right)
\end{array} \right.\ $$

其中

$$\beta = \frac{u}{c}\text{，}\gamma = \frac{1}{\sqrt{1 - \beta^{2}}}$$

逆变换

$$\left\{ \begin{array}{r}
x = \frac{x + ut'}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \frac{x' + ut'}{\sqrt{1 - \beta^{2}}} = \gamma\left( x' + \beta t'c \right)\ \ \ \ \ \ \  \\
y = y'\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
z = z'\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
t = \frac{t' + \left( u\text{/}c^{2} \right)x'}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \frac{t' + \beta x'\text{/}c}{\sqrt{1 - \beta^{2}}} = \gamma\left( t' + \beta x'\text{/}c \right)
\end{array} \right.\ $$

γ称为空间缩放系数或尺缩因子。

### 洛伦兹速度变换式

$$v_{x} = \frac{dx}{dt}\text{，}v_{y} = \frac{dy}{dt}\text{，}v_{z} = \frac{dz}{dt}\text{，}v_{x}' = \frac{dx'}{dt'}\text{，}v_{y}' = \frac{dy'}{dt'}\text{，}v_{z}' = \frac{dz'}{dt'}$$

得到一个物体对两个惯性系的速度变换关系

$$\left\{ \begin{array}{r}
v_{x}' = \frac{v_{x} - u}{1 - uv_{x}\text{/}c^{2}} = \frac{v_{x} - u}{1 - \beta v_{x}\text{/}c}\ \ \ \ \  \\
v_{y}' = \frac{v_{y}\sqrt{1 - u^{2}\text{/}c^{2}}}{1 - uv_{x}\text{/}c^{2}} = \frac{v_{y}\text{/}\gamma}{1 - \beta v_{x}\text{/}c} \\
v_{z}' = \frac{v_{z}\sqrt{1 - u^{2}\text{/}c^{2}}}{1 - uv_{x}\text{/}c^{2}} = \frac{v_{z}\text{/}\gamma}{1 - \beta v_{x}\text{/}c}
\end{array} \right.\ $$

特别地，当v平行于x轴和x′轴时，有

$$v' = \frac{v - u}{1 - uv\text{/}c^{2}} = \frac{v - u}{1 - \beta v\text{/}c}$$

### 时间延缓效应

设有相对运动的两惯性系S和S′，S′系相对S系的运动速度为u，某物理对象与S′系保持相对静止，在S系下观察该物理对象发生某个物理过程经历的时间Δt与在S′系下观察该物理对象发生同个物理过程经历的时间Δτ（固有时/本征时间间隔）满足

Δt = γΔτ

其中

$$\gamma = \frac{1}{\sqrt{1 - \beta^{2}}}\text{，}\beta = \frac{u}{c}$$

从外界观察某物理过程经历的时间Δt大于该物理过程自身观察所得时间Δτ

证明：设在S′系下看到同一地点x0′处先后发生了两个事件，对应时间t1′和t2′，由逆变换，有

$$\left\{ \begin{array}{r}
t_{1} = \frac{t_{1}' + \left( u\text{/}c^{2} \right)x_{0}'}{\sqrt{1 - u^{2}\text{/}c^{2}}} \\
t_{2} = \frac{t_{2}' + \left( u\text{/}c^{2} \right)x_{0}'}{\sqrt{1 - u^{2}\text{/}c^{2}}}
\end{array} \right.\ $$

两式相减，得

$$\Delta t = t_{2} - t_{1} = \left( t_{2}' - t_{1}' \right)\text{/}\sqrt{1 - u^{2}\text{/}c^{2}} = \Delta\tau\text{/}\sqrt{1 - u^{2}\text{/}c^{2}}$$

### 长度收缩效应

设有相对运动的两惯性系S和S′，S′系相对S系的运动速度为u，某物理对象与S′系保持相对静止，在S系下观察该物理对象的长度l与在S′系下观察该物理对象的长度l0（固有长度/本征长度）满足

$$l = l_{0}\sqrt{1 - u^{2}\text{/}c^{2}} = l_{0}\text{/}\gamma$$

证明：

$$\left\{ \begin{array}{r}
x_{1}' = \frac{x_{1} - ut_{1}}{\sqrt{1 - u^{2}\text{/}c^{2}}} \\
x_{2}' = \frac{x_{2} - ut_{2}}{\sqrt{1 - u^{2}\text{/}c^{2}}}
\end{array} \right.\ $$

由t1 = t2，两式相减，得

$$l_{0} = x_{2}' - x_{1}' = \frac{x_{1} - x_{2}}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \frac{l}{\sqrt{1 - u^{2}\text{/}c^{2}}}$$

### 质量膨胀效应

设有相对运动的两惯性系S和S′，S′系相对S系的运动速度为u，某物理对象与S′系保持相对静止，在S系下观察该物理对象的质量m与在S′系下观察该物理对象的质量m0（静止质量）满足

$$m = \frac{m_{0}}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \gamma m_{0}$$

### 动量

p = mv

### 力

$$\mathbf{F} = \frac{d\mathbf{p}}{dt} = \frac{d\left( m\mathbf{v} \right)}{dt} = \mathbf{v}\frac{dm}{dt} + m\frac{d\mathbf{v}}{dt}$$

### 动能

$${E_{k} = \int_{0}^{l}{\mathbf{f} \cdot d\mathbf{s}}
}{= \int_{0}^{l}{\frac{d\left( m\mathbf{v} \right)}{dt} \cdot d\mathbf{s}} = \int_{0}^{l}{d\left( m\mathbf{v} \right) \cdot \frac{d\mathbf{s}}{dt}}
}{= \int_{0}^{v}{d\left( m\mathbf{v} \right) \cdot d\mathbf{v}} = \int_{0}^{v}{\mathbf{v} \cdot d\left( \gamma m_{0}\mathbf{v} \right)}
}{= \gamma m_{0}v^{2} - m_{0}\int_{0}^{v}{\gamma\mathbf{v} \cdot d\mathbf{v}}
}{= \gamma m_{0}v^{2} + m_{0}c^{2}\text{/}\gamma - m_{0}c^{2}
}{= mc^{2} - m_{0}c^{2} = \left( m - m_{0} \right)c^{2}}$$

动能的近似

$$E_{k} = mc^{2} - m_{0}c^{2} = \left( \frac{1}{\sqrt{1 - u^{2}\text{/}c^{2}}} - 1 \right)m_{0}c^{2}$$

$$\text{把}\frac{u^{2}}{c^{2}}\text{看作整体，对}\frac{1}{\sqrt{1 - u^{2}\text{/}c^{2}}}\text{做泰勒展开，得}$$

$$E_{k} = \left( 1 + \frac{1}{2}\frac{v^{2}}{c^{2}} + o\left( \frac{v^{2}}{c^{2}} \right) - 1 \right)m_{0}c^{2} = \frac{1}{2}m_{0}v^{2}$$

### 物体的能量

E = Ek + m0c2 = mc2 − m0c2 + m0c2 = mc2 = γm0c2

E = mc2

其中m0c2称为静止能量。

推论

m2c2 − m2v2 = m02c2

$$\text{证明：}m = \gamma m_{0} = \frac{m_{0}}{\sqrt{1 - v^{2}\text{/}c^{2}}} \Rightarrow m^{2} = \frac{m_{0}^{2}}{1 - v^{2}\text{/}c^{2}} = \frac{m_{0}^{2}c^{2}}{c^{2} - v^{2}} \Rightarrow m^{2}c^{2} - m^{2}v^{2} = m_{0}^{2}c^{2}$$

p2c2 = E2 − E02

m2c2 − m2v2 = m02c2 ⇒ m2c4 − m2v2c2 = m02c4 ⇒ (mc2)2 − (pc)2 = (m0c2)2 ⇒ p2c2 = E2 − E02
