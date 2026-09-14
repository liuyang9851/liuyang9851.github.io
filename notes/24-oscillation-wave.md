---
title: 振动与波动
description: 简谐运动的微分方程与运动方程、简谐振动的合成、拍频、波函数的建立、波的干涉、驻波、波的能量与能流。
---

# 振动与波动

[[toc]]

## 简谐振动

$$\text{对于弹簧振子，有}\omega^{2} = \frac{k}{m}\text{。对于单摆，有}\ \omega^{2} = \frac{g}{l}\text{。对于复摆，有}\omega^{2} = \frac{mgl}{J}\text{。}$$

### 简谐运动方程的推导

$$- kx = ma\text{，其中}x\left| \underset{t = 0}{} \right.\  = x_{0}\text{，}v\left| \underset{t = 0}{} \right.\  = v_{0}$$

解：方程可化为

$$\frac{d^{2}x}{dt^{2}} + \frac{k}{m}x = 0$$

其特征方程

$$r^{2} + \frac{k}{m} = 0$$

的根为

$r = \pm \sqrt{\frac{k}{m}}i$

因此方程的通解为

$$
x = C_{1}\cos\left( \sqrt{\frac{k}{m}}t \right) + C_{2}\sin\left( \sqrt{\frac{k}{m}}t \right)
$$

代入初值条件

$$
x\left| \underset{t = 0}{} \right.\  = x_{0}\text{，}v\left| \underset{t = 0}{} \right.\  = v_{0}
$$

，得到$C_{1} = x_{0}\text{，}C_{2} = v_{0}\sqrt{\frac{m}{k}}$，得

$$
x = x_{0}\cos\left( \sqrt{\frac{k}{m}}t \right) + v_{0}\sqrt{\frac{m}{k}}\sin\left( \sqrt{\frac{k}{m}}t \right) = \sqrt{x_{0}^{2} + \frac{m}{k}v_{0}^{2}}\sin\left( \sqrt{\frac{k}{m}}t + \varphi \right)
$$

$$\text{因此，简谐运动的振幅}A = \sqrt{x_{0}^{2} + \frac{m}{k}v_{0}^{2}}\text{，频率}\omega = \sqrt{\frac{k}{m}}\text{，周期}T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}\text{。}$$

### 简谐运动方程

当时间t = t0，相位φ = φ0时，有

x = Acos (ω(t − t0) + φ0)

特别地，当t = 0时，有

$${v = - A\omega\sin\left( \omega t + \varphi_{0} \right)
}{= A\omega\cos\left( \omega t + \varphi_{0} + \frac{\pi}{2} \right)}$$

a = −Aω2cos (ωt + φ0) = Aω2cos (ωt + φ0 + π)

$$\left\{ \begin{array}{r}
x_{0} = A\cos\varphi_{0}\ \ \ \ \ \  \\
v_{0} = - A\omega\sin\varphi_{0}
\end{array} \right.\  \Leftrightarrow \left\{ \begin{array}{r}
A = \sqrt{x_{0}^{2} + \frac{v_{0}^{2}}{\omega^{2}}}\ \  \\
\tan\varphi_{0} = - \frac{v_{0}}{\omega x_{0}}
\end{array} \right.\  \Leftrightarrow \left\{ \begin{array}{r}
\cos\varphi_{0} = \frac{x_{0}}{A}\ \ \ \ \ \  \\
\sin\varphi_{0} = - \frac{v_{0}}{A\omega}
\end{array} \right.\ $$

### 简谐振动的合成

$$\left\{ \begin{array}{r}
x_{1} = A_{1}\cos\left( \omega t + \varphi_{10} \right) \\
x_{2} = A_{1}\cos\left( \omega t + \varphi_{10} \right)
\end{array} \right.\ $$

$${x = x_{1} + x_{2} = A_{1}\cos\left( \omega t + \varphi_{10} \right) + A_{1}\cos\left( \omega t + \varphi_{10} \right)
}{= A_{1}\cos{\omega t}\cos\varphi_{10} - A_{1}\sin{\omega t}\sin\varphi_{10} + A_{2}\cos{\omega t}\cos\varphi_{20} - A_{2}\sin{\omega t}\sin\varphi_{20}
}{= \cos{\omega t}\left( A_{1}\cos\varphi_{10} + A_{2}\cos\varphi_{20} \right) - \sin{\omega t}\left( A_{1}\sin\varphi_{10} + A_{2}\sin\varphi_{20} \right)
}{= A\cos{\omega t} \cdot \frac{A_{1}\cos\varphi_{10} + A_{2}\cos\varphi_{20}}{A} - A\sin{\omega t} \cdot \frac{A_{1}\sin\varphi_{10} + A_{2}\sin\varphi_{20}}{A}
}{= A\cos\left( \omega t + \varphi_{0} \right)}$$

其中

$$\left\{ \begin{array}{r}
\sin\varphi_{0} = \frac{A_{1}\sin\varphi_{10} + A_{2}\sin\varphi_{20}}{A}\  \\
\cos\varphi_{0} = \frac{A_{1}\cos\varphi_{10} + A_{2}\cos\varphi_{20}}{A}
\end{array} \right.\ $$

故

$$\tan\varphi_{0} = \frac{A_{1}\sin\varphi_{10} + A_{2}\sin\varphi_{20}}{A_{1}\cos\varphi_{10} - A_{2}\cos\varphi_{20}}$$

因为sin2φ0 + cos2φ0 = 1，即

$${\left( \frac{A_{1}\sin\varphi_{10} + A_{2}\sin\varphi_{20}}{A} \right)^{2} + \left( \frac{A_{1}\cos\varphi_{10} + A_{2}\cos\varphi_{20}}{A} \right)^{2}
}{= \frac{1}{A^{2}} \cdot \left\lbrack \left( A_{1}^{2}\sin^{2}\varphi_{10} + A_{2}^{2}\sin^{2}\varphi_{20} + 2A_{1}A_{2}\sin\varphi_{10}\sin\varphi_{20} \right) + \left( A_{1}^{2}\cos^{2}\varphi_{10} + A_{2}^{2}\cos^{2}\varphi_{20} + 2A_{1}A_{2}\cos\varphi_{10}\cos\varphi_{20} \right) \right\rbrack
}{= \frac{1}{A^{2}} \cdot \left\lbrack A_{1}^{2}\left( \sin^{2}\varphi_{10} + \cos^{2}\varphi_{10} \right) + A_{2}^{2}\left( \sin^{2}\varphi_{20} + \cos^{2}\varphi_{20} \right) + 2A_{1}A_{2}\left( \sin\varphi_{10}\sin\varphi_{20} + \cos\varphi_{10}\cos\varphi_{20} \right) \right\rbrack
}{= \frac{A_{1}^{2} + A_{2}^{2} + 2A_{1}A_{2}\cos\left( \varphi_{10} - \varphi_{20} \right)}{A^{2}} = 1}$$

所以

$$A = \sqrt{A_{1}^{2} + A_{2}^{2} + 2A_{1}A_{2}\cos\left( \varphi_{10} - \varphi_{20} \right)}$$

$$x = \sqrt{A_{1}^{2} + A_{2}^{2} + 2A_{1}A_{2}\cos\left( \varphi_{10} - \varphi_{20} \right)}\cos\left( \omega t + \arctan\frac{A_{1}\sin\varphi_{10} + A_{2}\sin\varphi_{20}}{A_{1}\cos\varphi_{10} - A_{2}\cos\varphi_{20}} \right)$$

### 同方向、频率相近的简谐振动的合成

设ω2 > ω1，且|ω2 − ω1| ≪ ω1 + ω2，φ10 = φ20 = 0，A1 = A2 = A0，得

x = x1 + x2 = A0cos ω1t + A0cos ω2t

$$= 2A_{0}\cos\left( \frac{\omega_{2} - \omega_{1}}{2}t \right)\cos\left( \frac{\omega_{2} + \omega_{1}}{2}t \right)$$

由|ω2 − ω1| ≪ ω1 + ω2，把它看作振幅为

$$
\left| 2A_{0}\cos\left( \frac{\omega_{2} - \omega_{1}}{2}t \right) \right|
$$

，频率为ω1或ω2的简谐振动。合振幅变化的周期为

$$\tau = \left| \frac{2\pi}{\omega_{2} - \omega_{1}} \right|$$

合振幅变化的频率（称为拍频）为

$$\nu = \frac{1}{\tau} = \left| \nu_{2} - \nu_{1} \right|$$

## 波函数方程的建立

在xOy坐标系下，设在x = x0点处的振动方程为

y = Acos (ωt + φ0)

对于在任意一点x处，其比x0处振动的传播滞后（波向右（x轴正方向）传播）或超前（波向左（x轴负方向）传播）

$$\Delta t = \frac{x - x_{0}}{u}$$

的时间，所以有

$$y = A\cos\left\lbrack \omega\left( t \mp \frac{x - x_{0}}{u} \right) + \varphi_{0} \right\rbrack$$

取负号时表示波向右传播，取正号时表示波向左传播。

也可以直接操纵相位，由

$$\Delta\varphi = 2\pi\frac{\Delta x}{\lambda} = 2\pi\frac{x - x_{0}}{\lambda}$$

得到等价方程

$$y = A\cos\left\lbrack \omega t + \varphi_{0} \mp 2\pi\frac{x - x_{0}}{\lambda} \right\rbrack$$

常取x0 = 0，得到

$$y = A\cos\left\lbrack \omega\left( t \mp \frac{x}{u} \right) + \varphi_{0} \right\rbrack\ \ \text{或}\ \ y = A\cos\left\lbrack \omega t + \varphi_{0} \mp 2\pi\frac{x}{\lambda} \right\rbrack$$

若令

y = Acos (Bt − Cx + D)

则有

$$\left\{ \begin{array}{r}
A = A\ \ \ \ \ \ \ \ \ \ \ \  \\
B = \omega\ \ \ \ \ \ \ \ \ \ \  \\
C = \frac{\omega}{u} = \frac{2\pi}{\lambda} \\
D = \varphi_{0}\ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

## 波的干涉

波源振动方程为

$$\left\{ \begin{array}{r}
y_{1} = A_{1}\cos\left( \omega t + \varphi_{10} \right) \\
y_{2} = A_{1}\cos\left( \omega t + \varphi_{10} \right)
\end{array} \right.\ $$

的两波在点P出的振幅分别为

$$\left\{ \begin{array}{r}
y_{1} = A_{1}\cos\left( \omega t + \varphi_{10} - 2\pi\frac{r_{1}}{\lambda} \right) \\
y_{2} = A_{2}\cos\left( \omega t + \varphi_{20} - 2\pi\frac{r_{2}}{\lambda} \right)
\end{array} \right.\ $$

叠加后有

$$y_{P} = y_{1} + y_{2} = A_{1}\cos\left( \omega t + \varphi_{10} - 2\pi\frac{r_{1}}{\lambda} \right) + A_{2}\cos\left( \omega t + \varphi_{20} - 2\pi\frac{r_{2}}{\lambda} \right)$$

yP = Acos (ωt + φ0)

其中

$$\left\{ \begin{array}{r}
\tan\varphi_{0} = \frac{A_{1}\sin\left( \varphi_{10} - 2\pi\frac{r_{1}}{\lambda} \right) + A_{2}\sin\left( \varphi_{20} - 2\pi\frac{r_{2}}{\lambda} \right)}{A_{1}\cos\left( \varphi_{10} - 2\pi\frac{r_{1}}{\lambda} \right) + A_{2}\cos\left( \varphi_{20} - 2\pi\frac{r_{2}}{\lambda} \right)} \\
A\ \ \ \ \  = \sqrt{A_{1}^{2} + A_{2}^{2} + 2A_{1}A_{2}\cos{\Delta\varphi}}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\Delta\varphi\ \ \  = \varphi_{20} - \varphi_{10} - 2\pi\frac{r_{2} - r_{1}}{\lambda}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

### 驻波

方向相反的两波

$$\left\{ \begin{array}{r}
y_{1} = A_{1}\cos\left( \omega t - 2\pi\frac{x}{\lambda} \right) \\
y_{2} = A_{1}\cos\left( \omega t + 2\pi\frac{x}{\lambda} \right)
\end{array} \right.\ $$

叠加

$$y = y_{1} + y_{2} = 2A\cos\left( 2\pi\frac{x}{\lambda} \right)\cos(\omega t)$$

波节和波腹的位置由λ决定，x每相差一个λ/2，波节和波腹各出现一次。

### 波的能量

波的能量是指单位质元所含的动能和势能，有

$${\,{\Delta W}_{k} = \frac{1}{2}\Delta mv^{2} = \frac{1}{2}\rho\Delta VA^{2}\omega^{2}\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack
}{\,{\Delta W}_{p} = E_{k} = \frac{1}{2}\rho\Delta VA^{2}\omega^{2}\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack
}{\Delta W = E_{k} + E_{p} = \rho\Delta VA^{2}\omega^{2}\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack}$$

能量，平均能量，平均能量密度，能流，平均能流，平均能流密度（强度）

能量

$$\Delta W = \rho\Delta VA^{2}\omega^{2}\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack$$

能量密度

$$w = \frac{\Delta W}{\Delta V} = \rho A^{2}\omega^{2}\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack$$

平均能量密度

$$\overline{w} = \frac{1}{T}\int_{0}^{T}{wdt} = \frac{1}{2}\rho A^{2}\omega^{2}$$

能流

$$P = wuS = \rho A^{2}\omega^{2}uS\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack$$

平均能流

$$\overline{P} = \overline{w}uS = \frac{1}{2}\rho A^{2}\omega^{2}uS$$

平均能流密度（强度）

$$I = \frac{\overline{P}}{S} = \overline{w}u = \frac{1}{2}\rho A^{2}\omega^{2}u$$

特别地，相干波叠加后的强度

$$I = I_{1} + I_{2} + 2\sqrt{I_{1}I_{2}}\cos{\Delta\varphi}$$
