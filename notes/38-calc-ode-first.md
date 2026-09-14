---
title: 微分方程（一阶与可降阶）
description: 可分离变量的方程、齐次方程、可化为齐次的方程、一阶线性方程、伯努利方程、可降阶的高阶微分方程。
---

# 微分方程（一阶与可降阶）

[[toc]]

若

$$\left\{ \begin{array}{r}
x = \rho(\theta)\cos\theta \\
y = \rho(\theta)\sin\theta
\end{array} \right.\ $$

则

$$s = \int_{a}^{b}{\sqrt{\rho^{2}(\theta) + {\rho'}^{2}(\theta)}d\theta}$$

微分方程

可分离变量的微分方程

g(y)dy = f(x)dx

有

∫g(y)dy = ∫f(x)dx

即

G(y) = F(x) + C

eg.解方程mg − kv = ma，其中$v\left| \underset{t = 0}{} \right.\  = 0$

解：分离变量，得

$$\frac{dv}{mg - kv} = \frac{dt}{m}$$

由mg − kv > 0，两端积分，得

$$- \frac{1}{k}\ln(mg - kv) = \frac{t}{m} + C_{1}$$

即

$$v = \frac{mg}{k} + C_{2}e^{- \frac{k}{m}t}\ \ \left( C_{2} = - \frac{e^{- kC_{1}}}{k} \right)$$

代入初值条件$v\left| \underset{t = 0}{} \right.\  = 0$，得

$$C_{2} = - \frac{mg}{k}$$

得到

$$v = \frac{mg}{k}\left( 1 - e^{- \frac{k}{m}t} \right)$$

两边积分，得

$$x = \frac{mg}{k}t + ge^{- \frac{k}{m}t} + C_{3}$$

取$x\left| \underset{t = 0}{} \right.\  = 0$，得

C3 = −g

得到

$$x = g\left( e^{- \frac{k}{m}t} - 1 \right)$$

$$\text{又由于}v = \frac{mg}{k}\left( 1 - e^{- \frac{k}{m}t} \right)\text{，将}1 - e^{- \frac{k}{m}t} = \frac{kv}{mg}\text{代入，得}$$

$$x = - \frac{k}{m}v$$

这样就得到了所谓的“另类加速度”。

齐次微分方程

$$\frac{dy}{dx} = \varphi\left( \frac{y}{x} \right)$$

$$\text{令}u = \frac{y}{x}\text{，则}\ y = xu\text{，有}$$

$$\frac{dy}{dx} = (xu)' = u + x\frac{du}{dx}$$

因此有

$$\varphi\left( \frac{y}{x} \right) = \varphi(u) = u + x\frac{du}{\ dx}$$

是一个可分离变量的方程，整理得

$$\frac{du}{\varphi(u) - u} = \frac{dx}{x}$$

即

$$\int_{}^{}{\frac{1}{\varphi\left( \frac{y}{x} \right) - \frac{y}{x}}d\left( \frac{y}{x} \right)} = \int_{}^{}\frac{dx}{x} = \ln|x| + C$$

可化为齐次的微分方程

方程

$$\frac{dy}{dx} = f\left( \frac{ax + by + c}{a_{1}x + b_{1}y + c_{1}} \right)$$

$$\text{若}\left| \begin{matrix}
a & b \\
a_{1} & b_{1}
\end{matrix} \right| \neq 0\text{，则令}\ x = X + h\text{，}y = Y + k\text{，则}dx = dX\text{，}dy = dY\text{，则}$$

$$\frac{dY}{dX} = f\left( \frac{aX + bY + ah + bk + c}{a_{1}X + b_{1}Y + a_{1}h + b_{1}k + c} \right)$$

解方程

$$\left\{ \begin{array}{r}
ah + bk + c\ \ \ \  = 0 \\
a_{1}h + b_{1}k + c = 0
\end{array} \right.\ $$

得

$$h = \frac{\left| \begin{matrix}
 - c & b \\
 - c & b_{1}
\end{matrix} \right|}{\left| \begin{matrix}
a & b \\
a_{1} & b_{1}
\end{matrix} \right|}\text{，}k = \frac{\left| \begin{matrix}
a & - c \\
a_{1} & - c
\end{matrix} \right|}{\left| \begin{matrix}
a & b \\
a_{1} & b_{1}
\end{matrix} \right|}$$

$$\text{若}\left| \begin{matrix}
a & b \\
a_{1} & b_{1}
\end{matrix} \right| = 0\text{，令}\frac{a_{1}}{a} = \frac{b_{1}}{b} = \lambda \text{，}\nu = ax + by\text{，得}$$

$$\frac{d\nu}{dx} = a + b\frac{dy}{dx} = a + bf\left( \frac{ax + by + c}{\lambda(ax + by) + c_{1}} \right)$$

所以

$$\frac{1}{b}\left( \frac{d\nu}{dx} - a \right) = f\left( \frac{\nu + c}{\lambda\nu + c_{1}} \right)$$

一阶齐次线性微分方程

$$\frac{dy}{dx} + P(x)y = 0$$

分离变量，得

$$\frac{dy}{y} = - P(x)dx$$

两端积分，得

ln |y| = −∫P(x)dx + C

通解

y = Ce−∫P(x)dx  (C = ±eC1)

此处的∫P(x)dx表示P(x)的某个确定的原函数（即不用加常数C），下同。

一阶线性微分方程

$$\frac{dy}{dx} + P(x)y = Q(x)\ \ y' + P(x)y = Q(x)$$

的通解为

y = e−∫P(x)dx(∫Q(x)e∫P(x)dxdx + C)

= exp (−∫P(x)dx)(∫Q(x)exp (∫P(x)dx)dx + C)

y = Ce−∫P(x)dx + e−∫P(x)dx∫Q(x)e∫P(x)dxdx

证明：常数变易法

$$\text{设}y = ue^{- \int_{}^{}{P(x)dx}}\text{是方程}\frac{dy}{dx} + P(x)y = Q(x)\text{的通解}\ \left. \text{（}u\text{是所谓}``\text{变易}"\text{的函数} \right.\text{）}\ \text{，则}$$

$$\frac{dy}{dx} = u'e^{- \int_{}^{}{P(x)dx}} - uP(x)e^{- \int_{}^{}{P(x)dx}}$$

$$\text{将}y = ue^{- \int_{}^{}{P(x)dx}}\text{和}\ \frac{dy}{dx} = u'e^{- \int_{}^{}{P(x)dx}} - uP(x)e^{- \int_{}^{}{P(x)dx}}\text{代入}\ \frac{dy}{dx} + P(x)y = Q(x)\text{，得}$$

u′e−∫P(x)dx − uP(x)e−∫P(x)dx + P(x)ue−∫P(x)dx = Q(x)

后两项抵消，得

u′e−∫P(x)dx = Q(x)

u′ = Q(x)e∫P(x)dx

两端积分，得

u = ∫Q(x)e∫P(x)dxdx + C

把这个结果代入y = ue−∫P(x)dx，得

y = e−∫P(x)dx(∫Q(x)e∫P(x)dxdx + C) = Ce−∫P(x)dx + e−∫P(x)dx∫Q(x)e−∫P(x)dxdx

这个证明过程类似于“原函数与导函数混合还原”中等号右边为非0式的做法。

伯努利方程

$$\frac{dy}{dx} + P(x)y = Q(x)y^{n}$$

两边同除yn，得

$$y^{- n}\frac{dy}{dx} + P(x)y^{1 - n} = Q(x)$$

令z = y1 − n，对z求导得

$$\frac{dz}{dy} = (1 - n)y^{- n}\frac{dy}{dx}$$

将该式代入上式，得

$$y^{- n}\frac{1}{(1 - n)y^{- n}}\frac{dz}{dx} + P(x)y^{1 - n} = Q(x)$$

两边同乘(1 − n)，并把y1 − n代为z，得

$$\frac{dz}{dx} + (1 - n)P(x)z = (1 - n)Q(x)$$

此式为一阶线性方程，其通解为

y1 − n = Ce−∫(1 − n)P(x)dx + e−∫(1 − n)P(x)dx∫(1 − n)Q(x)e−∫(1 − n)P(x)dxdx

记g(x) = −∫(1 − n)P(x)dx，则其可表示为

y1 − x = Ceg(x) + eg(x)∫(1 − n)Q(x)eg(x)dx
