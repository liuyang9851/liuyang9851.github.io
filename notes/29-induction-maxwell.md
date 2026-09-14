---
title: 电磁感应与电磁波
description: 电动势、法拉第电磁感应定律、动生与感生电动势、自感与互感、麦克斯韦方程组。
---

# 电磁感应与电磁波

[[toc]]

### 电动势

$$\varepsilon = \frac{A}{q} = \underset{\text{电源内部}}{\int_{-}^{+}{\mathbf{E}_{k} \cdot dl}} = \oint_{L}^{}{\mathbf{E}_{k} \cdot dl}$$

## 法拉第电磁感应感应定律

$$\varepsilon_{i} = - N\frac{d\Phi_{m}}{dt} = - \frac{d\psi_{m}}{dt}$$

根据规定的回路绕行方向做右手螺旋得到的正法线方向确定$\frac{d\Phi_{m}}{dt}\text{的正负，如果}\varepsilon_{i} > 0$，则感应电动势方向与绕行方向相同，否则相反。

或者随便选取Φm的一个正方向，根据此方向用右手螺旋得到对应的绕行方向，算出εi为正则与绕行方向相同，反之相反。

### 动生电动势

εi = ∫L(v × B) ⋅ dl = ∫L|v × B|cos  < (v × B), dl>dl = ∫LvBsin  < v,  B>cos  < (v × B), dl>dl

其中εi > 0说明电动势方向与选定L方向相同，否则相反。

或v × B指向高电势端。

绕一端旋转的情况

$$\varepsilon = \frac{1}{2}BvL = \frac{1}{2}B\omega L^{2}$$

### 感生电动势

$$\varepsilon_{i} = \oint_{L}^{}{\mathbf{E}_{\text{旋}} \cdot dl} = - \frac{d}{dt}\iint_{S}^{}{\mathbf{B} \cdot d\mathbf{S}} = - \iint_{S}^{}{\frac{\partial\mathbf{B}}{\partial t} \cdot d\mathbf{S}}$$

根据规定的回路绕行方向做右手螺旋得到的正法线方向确定$\frac{\partial\mathbf{B}}{\partial t}\text{的正负，如果}\varepsilon_{i} > 0$，则感应电动势方向与正法线方向相同，否则相反。

### 自感

$$L = \frac{\psi_{m}}{I}$$

L取决于线圈形状、大小、匝数和周围磁介质分布情况。对于非铁磁介质，L与线圈中电流无关。

![长直螺线管示意图：长度 l、截面积 S、总匝数 N，管内充磁导率 μ 的介质](/images/physics/solenoid-self-inductance.svg)长直螺线管，长为l，截面积S，线圈总匝数N，管中充有磁导率μ的介质，自感系数为

L = μN2V = μN2lS

$$\text{自感线圈存储的磁能为}W_{m} = \frac{1}{2}LI^{2}\text{（适用于自感系数}L\text{一定的任意线圈），对比电容器}W_{e} = \frac{1}{2}CU^{2}$$

$$\text{磁场的能量密度为}w_{m} = \frac{1}{2}\mathbf{D} \cdot \mathbf{E}\text{，对比电场的能量密度为}w_{e} = \frac{1}{2}\mathbf{B} \cdot \mathbf{H}$$

### 互感

$$M = \frac{\psi_{21}}{I_{1}} = \frac{\psi_{12}}{I_{2}}$$

M与两个回路的大小、形状、匝数、相对位置以及周围磁介质的性质有关。在没有铁磁质时，M为常量。

## 麦克斯韦方程组

$$\left\{ \begin{array}{r}
\oint_{S}^{}{\mathbf{D} \cdot d\mathbf{S}} = \sum_{}^{}q_{i},\ \ \text{高斯电场定理：电荷激发电场}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\oint_{L}^{}{\mathbf{E} \cdot d\mathbf{l}} = - \iint_{}^{}{\frac{\partial\mathbf{B}}{\partial t} \cdot d\mathbf{S}},\ \ \text{法拉第电磁感应定律：变化的磁场激发电场}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\oint_{S}^{}{\mathbf{B} \cdot d\mathbf{S}} = 0,\ \ \text{高斯磁场定理：磁感线是闭合曲线}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\oint_{L}^{}{\mathbf{H} \cdot d\mathbf{l}} = \iint_{S}^{}{\left( \mathbf{j}_{0} + \frac{\partial\mathbf{D}}{\partial t} \right) \cdot d\mathbf{S}},\ \ \text{安培} - \text{麦克斯韦环路定理：位移电流和传导电流激发磁场}\ \ 
\end{array} \right.\ $$

### 无阻尼电磁振荡

$$\omega = \frac{1}{\sqrt{LC}},\ \ T = 2\pi\sqrt{LC},\ \ \nu = \frac{1}{2\pi\sqrt{LC}}$$

### 电磁波的波速

$$u = \frac{1}{\sqrt{\varepsilon\mu}} = \frac{1}{\sqrt{\varepsilon_{0}\varepsilon_{r}\mu_{0}\mu_{r}}}$$

### 介质的绝对折射率

$$n = \frac{c}{u} = \sqrt{\varepsilon_{r}\mu_{r}}$$

### 电磁波的能量体密度

$$w = w_{e} + w_{m} = \frac{1}{2}\mathbf{D} \cdot \mathbf{E} + \frac{1}{2}\mathbf{B} \cdot \mathbf{H} = \frac{1}{2}\varepsilon E^{2} + \frac{1}{2}\mu H^{2} = \frac{1}{2}\left( \varepsilon E^{2} + \mu H^{2} \right)$$

### 电磁波的能流密度

$$S = w\frac{dl}{dt} = \frac{u}{2}\left( \varepsilon E^{2} + \mu H^{2} \right)\overset{u = \frac{1}{\sqrt{\varepsilon\mu}}}{=}EH$$

S = E × H（坡印亭矢量）

## 光程
