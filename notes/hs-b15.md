---
title: "微积分下的大学物理"
hs_seq: "B15"
description: "微积分下的大学物理：如图，质点在绕坐标原点做圆周运动的某时刻的速度为，其中"
---

# 微积分下的大学物理

大学物理初步

质点运动学

位矢（位置矢量）

$\mathbf{r} = \mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$

位矢的大小

$r = \sqrt{x^{2} + y^{2} + z^{2}}$

速度（瞬时速度）

$\mathbf{v} = \frac{d\mathbf{r}}{dt} = \frac{d\mathbf{x}}{dt}\mathbf{i} + \frac{d\mathbf{y}}{dt}\mathbf{i} + \frac{d\mathbf{z}}{dt}\mathbf{i} = v_{x}\mathbf{i} + v_{y}\mathbf{j} + v_{z}\mathbf{k}$

速率

$v = \sqrt{v_{x}^{2} + v_{y}^{2} + v_{z}^{2}}$

加速度

$\mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{d^{2}\mathbf{r}}{dt^{2}} = a_{x}\mathbf{i} + a_{y}\mathbf{j} + a_{z}\mathbf{k}$

加速度的大小

$a = \sqrt{a_{x}^{2} + a_{y}^{2} + a_{z}^{2}}$

自然坐标系下加速度分解

$\mathbf{v} = \frac{ds}{dt}\mathbf{e}_{t} = v\mathbf{e}_{t}$

$\mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{d\left( v\mathbf{e}_{t} \right)}{dt} = \frac{dv}{dt}\mathbf{e}_{t} + \frac{d\mathbf{e}_{t}}{dt}v = \frac{dv}{dt}\mathbf{e}_{t} + \frac{v^{2}}{r}\mathbf{e}_{n} = \mathbf{a}_{t} + \mathbf{a}_{n}$

$\text{其中}\mathbf{a}_{t} = \frac{dv}{dt}\mathbf{e}_{t}\text{称为切向加速度，}\mathbf{a}_{n} = \frac{v^{2}}{r}\mathbf{e}_{n}\text{称为法向}\text{/}\text{向心加速度。}$

向心加速度公式的推导

由上，$\mathbf{a} = \frac{dv}{dt}\mathbf{e}_{t} + \frac{d\mathbf{e}_{t}}{dt}v$，其中$\mathbf{a}_{t} = \frac{dv}{dt}\mathbf{e}_{t}\text{称为切向加速度}$，下面证明

$\mathbf{a}_{n} = \frac{d\mathbf{e}_{t}}{dt}v = \frac{v^{2}}{r}\mathbf{e}_{n}$

如图，质点在绕坐标原点做圆周运动的某时刻的速度为$v\overrightarrow{\mathbf{e}_{t}}\$，其中

$\mathbf{e}_{t} = \left( - \sin\theta \text{，}\cos\theta \right)$

就$v\overrightarrow{\mathbf{e}_{t}}$对$t$求导，有

$\frac{dv\overrightarrow{\mathbf{e}_{t}}}{dt} = v\frac{d\mathbf{e}_{t}}{dt} = v\frac{d( - \sin\theta\mathbf{i} + \cos\theta\mathbf{j})}{dt} = v\left( - \cos\theta\frac{d\theta}{dt}\mathbf{i} - \sin\theta\frac{d\theta}{dt}\mathbf{j} \right) = v\left( - \cos\theta\omega\mathbf{i} - \sin\theta\omega\mathbf{j} \right) = v\omega\left( - \cos\theta\mathbf{i} - \sin\theta\mathbf{j} \right)$

可以看出其方向是与$v\overrightarrow{\mathbf{e}_{t}}$互相垂直的，大小

$a_{n} = v\omega\sqrt{\left( - \cos\theta \right)^{2} + \left( - \sin\theta \right)^{2}} = v\omega$

> $\text{故}\mathbf{a}_{n} = v\omega\mathbf{e}_{n} = \frac{v^{2}}{r}\mathbf{e}_{n}$

角量与线量

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
<th colspan="2">

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

$s$

</td>
<td>

$\theta$

</td>
<td>

$s = \theta r$

</td>
<td>

$a_{n} = \frac{v^{2}}{r}$

</td>
</tr>
<tr>
<td>

速度

</td>
<td>

$v = \frac{ds}{dt}$

</td>
<td>

$\omega = \frac{d\theta}{dt}$

</td>
<td>

$v = \omega r$

</td>
<td>

$a_{n} = v\omega$

</td>
</tr>
<tr>
<td>

加速度

</td>
<td>

$a_{t} = \frac{dv}{dt} = \frac{d^{2}s}{dt^{2}}$

</td>
<td>

$\beta = \frac{d\omega}{dt} = \frac{d^{2}\theta}{dt^{2}}$

</td>
<td>

$a_{t} = \beta r$

</td>
<td>

$a_{n} = \omega^{2}r$

</td>
</tr>
</tbody>
</table>
</div>

质点动力学

动量

$\mathbf{p} = m\mathbf{v}$

力

$\mathbf{F} = \frac{d\mathbf{p}}{dt} = \frac{d\left( m\mathbf{v} \right)}{dt} = m\frac{d\mathbf{v}}{dt} + v\frac{dm}{dt} = m\mathbf{a}$

万有引力定律

$\mathbf{F} = - G\frac{m_{1}m_{2}}{r^{2}}\mathbf{r}_{0}$

其中$\mathbf{F}$表示$m_{2}$受到$m_{1}$的引力，$\mathbf{r}_{0}$表示从$m_{1}$到$m_{2}$的位矢。

胡克定律

$\mathbf{F} = - k\mathbf{x}$

其中质点的受力方向与弹簧形变方向相反。

动量定理

$\mathbf{I}_{b} - \mathbf{I}_{a} = \int_{a}^{b}{\mathbf{F}dt} = \int_{a}^{b}{\frac{d\mathbf{p}}{dt}dt} = \int_{a}^{b}{d\mathbf{p}} = \int_{a}^{b}{md\mathbf{v}} = m\mathbf{v}_{b} - m\mathbf{v}_{a} = \mathbf{p}_{b} - \mathbf{p}_{a}$

功

在恒力$\mathbf{F}$下

$A = \mathbf{F} \cdot \Delta\mathbf{r} = \left| \mathbf{F} \right|\left| \Delta\mathbf{r} \right|\cos{< \mathbf{F}\text{，}\Delta\mathbf{r} >}$

变力做功

$A = \int_{}^{}{dA} = \int_{a}^{b}{\mathbf{F \cdot}d\mathbf{r}} = \int_{a}^{b}{\left( F_{x}dx + F_{y}dy + F_{z}dz \right)\left( dx\mathbf{i} + dy\mathbf{j} + dz\mathbf{k} \right)} = \int_{a}^{b}\left( F_{x}dx + F_{y}dy + F_{z}dz \right)$

动能定理

$A = \int_{}^{}{dA} = \int_{a}^{b}{\mathbf{F \cdot}d\mathbf{r}} = \int_{a}^{b}{\frac{d\mathbf{p}}{dt}d\mathbf{r}} = \int_{a}^{b}{\frac{md\mathbf{v}}{dt}d\mathbf{r}} = \int_{a}^{b}{md\mathbf{v \cdot v}} = \frac{1}{2}m\mathbf{v}^{2}\left| \begin{array}{r} b \\ a \end{array} \right.\  = \frac{1}{2}mv_{b}^{2} - \frac{1}{2}mv_{a}^{2}$

$\int_{a}^{b}{md\mathbf{v \cdot v}} = \int_{a}^{b}{m\left( dv_{x} \cdot \mathbf{i} + dv_{y} \cdot \mathbf{j} + dv_{z} \cdot \mathbf{k} \right)\left( v_{x}\mathbf{i} + v_{y}\mathbf{j} + v_{z}\mathbf{k} \right)} = \int_{a}^{b}{m\left( v_{x}dv_{x} + v_{y}dv_{y} + v_{z}dv_{z} \right)} = \frac{1}{2}m\left( v_{x}^{2} + v_{y}^{2} + v_{z}^{2} \right)\left| \begin{array}{r} b \\ a \end{array} \right.\  = \frac{1}{2}mv^{2}\left| \begin{array}{r} b \\ a \end{array} \right.\$

势能

保守力从$a$点到$b$点做功为

$A = \int_{a}^{b}{\mathbf{F \cdot}d\mathbf{r}} = - \left( E_{p_{b}} - E_{p_{a}} \right)$

保守力做功$= -$势能变化量

重力势能

$A = \int_{a}^{b}{m\mathbf{g}d\mathbf{r}} = \int_{a}^{b}{m\mathbf{g}\left( dx\mathbf{i} + dy\mathbf{j} + dz\mathbf{k} \right)} = \int_{a}^{b}{mgdz} = mgz\left| \begin{array}{r} b \\ a \end{array} \right.\  = - \left( mgh_{a} - mgh_{b} \right) = - \left( E_{p_{b}} - E_{p_{a}} \right)$

引力势能

$A = \int_{a}^{b}{- G\frac{m_{1}m_{2}}{r^{2}}\mathbf{r}_{0}d\mathbf{r}} = - \left\lbrack \left( - G\frac{m_{1}m_{2}}{r_{a}} \right) - \left( - G\frac{m_{1}m_{2}}{r_{b}} \right) \right\rbrack = - \left( E_{p_{b}} - E_{p_{a}} \right)$

弹性势能

$A = \int_{a}^{b}{- kxdx} = - \frac{1}{2}kx^{2}\left| \begin{array}{r} b \\ a \end{array} \right.\  = - \left( \frac{1}{2}kx_{b}^{2} - \frac{1}{2}kx_{a}^{2} \right) = - \left( E_{p_{b}} - E_{p_{a}} \right)$

质点系力学

质心的位矢

$\mathbf{r}_{c} = \frac{\sum_{i}^{}{m_{i}\mathbf{r}_{i}}}{\sum_{i}^{}m_{i}} = \frac{\sum_{i}^{}{m_{i}\mathbf{r}_{i}}}{m}$

质心的速度

$\text{在此处键入公式。}$

线量与角量

<div class="table-scroll">
<table>
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

$\mathbf{x}$

</td>
<td>

$\mathbf{\theta}$

</td>
<td></td>
</tr>
<tr>
<td>

速度

</td>
<td>

$\mathbf{v}$

</td>
<td>

$\mathbf{\omega =}\frac{d\mathbf{\theta}}{dt}$

</td>
<td>

$\mathbf{v = \omega \times r}$

</td>
</tr>
<tr>
<td>

加速度

</td>
<td>

$\mathbf{a}$

</td>
<td>

$\mathbf{\beta} = \frac{d\mathbf{\omega}}{dt}$

</td>
<td>

$\mathbf{a = \beta \times r + \omega \times v =}\mathbf{a}_{t}\mathbf{+}\mathbf{a}_{n}$

</td>
</tr>
</tbody>
</table>
</div>

力矩

$\mathbf{M}_{z} = \mathbf{R}_{\bot} \times \mathbf{F}_{\bot}$

角动量

$\mathbf{L}_{z} = \sum_{i}^{}{\Delta m_{i}r_{i}^{2}}\mathbf{\omega} = J\mathbf{\omega}$

刚体定轴转动的转动定律

$\mathbf{M} = J\mathbf{\beta}$

常见刚体的转动惯量

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

$J = \frac{ml^{2}}{12}$

</td>
<td>

$J = \frac{ml^{2}}{3}$

</td>
<td>

$J = \frac{m\left( R^{2} + r^{2} \right)}{2}$

</td>
<td>

$J = \frac{mR^{2}}{2}$

</td>
<td>

$J = mR^{2}$

</td>
<td>

$J = \frac{2mR^{2}}{5}$

</td>
</tr>
</tbody>
</table>
</div>

简谐振动

> $\text{对于弹簧振子，有}\omega^{2} = \frac{k}{m}\text{。对于单摆，有}\ \omega^{2} = \frac{g}{l}\text{。对于复摆，有}\omega = \frac{mgl}{J}\text{。}$

简谐运动方程的推导

> $- kx = ma\text{，其中}x\left| \underset{t = 0}{} \right.\  = x_{0}\text{，}v\left| \underset{t = 0}{} \right.\  = v_{0}$

解：方程可化为

$\frac{d^{2}x}{dt^{2}} + \frac{k}{m}x = 0$

其特征方程

$r^{2} + \frac{k}{m} = 0$

的根为

$r = \pm \sqrt{\frac{k}{m}}i$

因此方程的通解为

$x = C_{1}\cos\left( \sqrt{\frac{k}{m}}t \right) + C_{2}\sin\left( \sqrt{\frac{k}{m}}t \right)$

代入初值条件$x\left| \underset{t = 0}{} \right.\  = x_{0}\text{，}v\left| \underset{t = 0}{} \right.\  = v_{0}$，得到$C_{1} = x_{0}\text{，}C_{2} = v_{0}\sqrt{\frac{m}{k}}$，得

$x = x_{0}\cos\left( \sqrt{\frac{k}{m}}t \right) + v_{0}\sqrt{\frac{m}{k}}\sin\left( \sqrt{\frac{k}{m}}t \right) = \sqrt{x_{0}^{2} + \frac{m}{k}v_{0}^{2}}\sin\left( \sqrt{\frac{k}{m}}t + \varphi \right)$

> $\text{因此，简谐运动的振幅}A = \sqrt{x_{0}^{2} + \frac{m}{k}v_{0}^{2}}\text{，频率}\omega = \sqrt{\frac{k}{m}}\text{，周期}T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}\text{。}$

简谐运动方程

当时间$t = t_{0}$，相位$\varphi = \varphi_{0}$时，有

$x = A\cos\left( \omega\left( t - t_{0} \right) + \varphi_{0} \right)$

特别地，当$t = 0$时，有

${v = - A\omega\sin\left( \omega t + \varphi_{0} \right) }{= A\omega\cos\left( \omega t + \varphi_{0} + \frac{\pi}{2} \right)}$

${a = - A\omega^{2}\cos\left( \omega t + \varphi_{0} \right) }{= A\omega^{2}\cos\left( \omega t + \varphi_{0} + \pi \right)}$

$\left\{ \begin{array}{r} x_{0} = A\cos\varphi_{0} \\ v_{0} = - A\omega\sin\varphi_{0} \end{array} \right.\  \Leftrightarrow \left\{ \begin{array}{r} A = \sqrt{x_{0}^{2} + \frac{v_{0}^{2}}{\omega^{2}}} \\ \tan\varphi_{0} = - \frac{v_{0}}{\omega x_{0}} \end{array} \right.\  \Leftrightarrow \left\{ \begin{array}{r} \cos\varphi_{0} = \frac{x_{0}}{A} \\ \sin\varphi_{0} = - \frac{v_{0}}{A\omega} \end{array} \right.\$

简谐振动的合成

$\left\{ \begin{array}{r} x_{1} = A_{1}\cos\left( \omega t + \varphi_{10} \right) \\ x_{2} = A_{1}\cos\left( \omega t + \varphi_{10} \right) \end{array} \right.\$

${x = x_{1} + x_{2} = A_{1}\cos\left( \omega t + \varphi_{10} \right) + A_{1}\cos\left( \omega t + \varphi_{10} \right) }{= A_{1}\cos{\omega t}\cos\varphi_{10} - A_{1}\sin{\omega t}\sin\varphi_{10} + A_{2}\cos{\omega t}\cos\varphi_{20} - A_{2}\sin{\omega t}\sin\varphi_{20} }{= \cos{\omega t}\left( A_{1}\cos\varphi_{10} - A_{2}\cos\varphi_{20} \right) - \sin{\omega t}\left( A_{1}\sin\varphi_{10} - A_{2}\sin\varphi_{20} \right) }{= A\cos{\omega t} \cdot \frac{A_{1}\cos\varphi_{10} - A_{2}\cos\varphi_{20}}{A} - A\sin{\omega t} \cdot \frac{A_{1}\sin\varphi_{10} - A_{2}\sin\varphi_{20}}{A} }{= A\cos\left( \omega t + \varphi_{0} \right)}$

其中

$\left\{ \begin{array}{r} \sin\varphi_{0} = \frac{A_{1}\sin\varphi_{10} - A_{2}\sin\varphi_{20}}{A} \\ \cos\varphi_{0} = \frac{A_{1}\cos\varphi_{10} - A_{2}\cos\varphi_{20}}{A} \end{array} \right.\$

故

$\tan\varphi_{0} = \frac{A_{1}\sin\varphi_{10} - A_{2}\sin\varphi_{20}}{A_{1}\cos\varphi_{10} - A_{2}\cos\varphi_{20}}$

因为$\sin^{2}\varphi_{0} + \cos^{2}\varphi_{0} = 1$，即

> ${\left( \frac{A_{1}\sin\varphi_{10} - A_{2}\sin\varphi_{20}}{A} \right)^{2} + \left( \frac{A_{1}\cos\varphi_{10} - A_{2}\cos\varphi_{20}}{A} \right)^{2} }{= \frac{1}{A^{2}} \cdot \left\lbrack \left( A_{1}^{2}\sin^{2}\varphi_{10} + A_{2}^{2}\sin^{2}\varphi_{20} - 2A_{1}A_{2}\sin\varphi_{10}\sin\varphi_{20} \right) + \left( A_{1}^{2}\cos^{2}\varphi_{10} + A_{2}^{2}\cos^{2}\varphi_{20} - 2A_{1}A_{2}\cos\varphi_{10}\cos\varphi_{20} \right) \right\rbrack }{= \frac{1}{A^{2}} \cdot \left\lbrack A_{1}^{2}\left( \sin^{2}\varphi_{10} + \cos^{2}\varphi_{10} \right) + A_{2}^{2}\left( \sin^{2}\varphi_{20} + \cos^{2}\varphi_{20} \right) - 2A_{1}A_{2}\left( \sin\varphi_{10}\sin\varphi_{20} + \cos\varphi_{10}\cos\varphi_{20} \right) \right\rbrack }{= \frac{A_{1}^{2} + A_{2}^{2} - 2A_{1}A_{2}\cos\left( \varphi_{10} - \varphi_{20} \right)}{A^{2}} = 1}$

所以

$A = \sqrt{A_{1}^{2} + A_{2}^{2} - 2A_{1}A_{2}\cos\left( \varphi_{10} - \varphi_{20} \right)}$

$x = \sqrt{A_{1}^{2} + A_{2}^{2} - 2A_{1}A_{2}\cos\left( \varphi_{10} - \varphi_{20} \right)}\cos\left( \omega t + \arctan\frac{A_{1}\sin\varphi_{10} - A_{2}\sin\varphi_{20}}{A_{1}\cos\varphi_{10} - A_{2}\cos\varphi_{20}} \right)$

波函数方程的建立

在$xOy$坐标系下，设在$x = x_{0}$点处的振动方程为

$y = A\cos\left( \omega t + \varphi_{0} \right)$

对于在任意一点$x$处，其比$x_{0}$处振动的传播滞后（波向右（$x$轴正方向）传播）或超前（波向左（$x$轴复方向）传播）

$\Delta t = \frac{x - x_{0}}{u}$

的时间，所以有

$y = A\cos\left\lbrack \omega\left( t \mp \frac{x - x_{0}}{u} \right) + \varphi_{0} \right\rbrack$

取负号时表示波向右传播，取正号时表示波向左传播。

也可以直接操纵相位，由

$\Delta\varphi = 2\pi\frac{\Delta x}{\lambda} = 2\pi\frac{x - x_{0}}{\lambda}$

得到等价方程

$y = A\cos\left\lbrack \omega t + \varphi_{0} \mp 2\pi\frac{x - x_{0}}{\lambda} \right\rbrack$

常取$x_{0} = 0$，得到

$y = A\cos\left\lbrack \omega\left( t \mp \frac{x}{u} \right) + \varphi_{0} \right\rbrack\ \ \text{或}\ \ y = A\cos\left\lbrack \omega t + \varphi_{0} \mp 2\pi\frac{x}{\lambda} \right\rbrack$

若令

$y = A\cos(Bt - Cx + D)$

则有

$\left\{ \begin{array}{r} A = A\ \ \ \ \ \ \ \ \ \ \ \  \\ B = \omega\ \ \ \ \ \ \ \ \ \ \  \\ C = \frac{\omega}{u} = \frac{2\pi}{\lambda} \\ D = \varphi_{0}\ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

波的干涉

波源振动方程为

$\left\{ \begin{array}{r} y_{1} = A_{1}\cos\left( \omega t + \varphi_{10} \right) \\ y_{2} = A_{1}\cos\left( \omega t + \varphi_{10} \right) \end{array} \right.\$

的两波在点$P$出的振幅分别为

$\left\{ \begin{array}{r} y_{1} = A_{1}\cos\left( \omega t + \varphi_{10} - 2\pi\frac{r_{1}}{\lambda} \right) \\ y_{2} = A_{2}\cos\left( \omega t + \varphi_{20} - 2\pi\frac{r_{2}}{\lambda} \right) \end{array} \right.\$

叠加后有

$y_{P} = y_{1} + y_{2} = A_{1}\cos\left( \omega t + \varphi_{10} - 2\pi\frac{r_{1}}{\lambda} \right) + A_{2}\cos\left( \omega t + \varphi_{20} - 2\pi\frac{r_{2}}{\lambda} \right)$

$y_{P} = A\cos\left( \omega t + \varphi_{0} \right)$

其中

$\left\{ \begin{array}{r} \tan\varphi_{0} = \frac{A_{1}\sin\left( \varphi_{10} - 2\pi\frac{r_{1}}{\lambda} \right) + A_{2}\sin\left( \varphi_{20} - 2\pi\frac{r_{2}}{\lambda} \right)}{A_{1}\cos\left( \varphi_{10} - 2\pi\frac{r_{1}}{\lambda} \right) + A_{2}\cos\left( \varphi_{20} - 2\pi\frac{r_{2}}{\lambda} \right)} \\ A\ \ \ \ \  = \sqrt{A_{1}^{2} + A_{2}^{2} - 2A_{1}A_{2}\cos{\Delta\varphi}}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \Delta\varphi\ \ \  = \varphi_{20} - \varphi_{10} - 2\pi\frac{r_{2} - r_{1}}{\lambda}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

驻波

方向相反的两波

$\left\{ \begin{array}{r} y_{1} = A_{1}\cos\left( \omega t - 2\pi\frac{x}{\lambda} \right) \\ y_{2} = A_{1}\cos\left( \omega t + 2\pi\frac{x}{\lambda} \right) \end{array} \right.\$

叠加

$y = y_{1} + y_{2} = 2A\cos\left( 2\pi\frac{x}{\lambda} \right)\cos(\omega t)$

波节和波腹的位置由$\lambda$决定，$x$每相差一个$\lambda\text{/}2$，波节和波腹各出现一次。

波的能量

波的能量是指单位质原所含的动能和势能，有

${{\Delta W}_{k} = \frac{1}{2}\Delta mv^{2} = \frac{1}{2}\rho\Delta VA^{2}\omega^{2}\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack }{{\Delta W}_{p} = E_{k} = \frac{1}{2}\rho\Delta VA^{2}\omega^{2}\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack }{\Delta W = E_{k} + E_{p} = \rho\Delta VA^{2}\omega^{2}\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack}$

能量，平均能量，平均能量密度，能流，平均能流，平均能流密度（强度）

能量

$\Delta W = \rho\Delta VA^{2}\omega^{2}\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack$

能量密度

$w = \frac{\Delta W}{\Delta V} = \rho A^{2}\omega^{2}\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack$

平均能量密度

$\overline{w} = \frac{1}{T}\int_{0}^{T}{wdt} = \frac{1}{2}\rho A^{2}\omega^{2}$

能流

$P = wuS = \rho A^{2}\omega^{2}uS\sin^{2}\left\lbrack \omega\left( t - \frac{x}{u} \right) + \varphi_{0} \right\rbrack$

平均能流

$\overline{P} = \overline{w}uS = \frac{1}{2}\rho A^{2}\omega^{2}uS$

平均能流密度（强度）

$I = \frac{\overline{P}}{S} = \overline{w}u = \frac{1}{2}\rho A^{2}\omega^{2}u$

特别地，相干波叠加后的强度

$I = I_{1} + I_{2} + 2\sqrt{I_{1}I_{2}}\cos{\Delta\varphi}$

洛伦兹变换

$S$系的坐标轴为$x$、$y$和$z$，$S'$系的坐标轴为$x'$、$y'$和$z'$。为了简单，让$x$、$y$和$z$轴分别平行于$x'$、$y$和$z'$轴，$S'$系相对于$S$系以不变速度$u$沿$x$轴的正方向运动，当$t = t' = 0$时，$S$系和$S'$系的原点互相重合。同一个物理事件在$S$系和$S'$系中的时空坐标由下列关系式相联系：

$\left\{ \begin{array}{r} x' = \frac{x - ut}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \frac{x - \beta ct}{\sqrt{1 - \beta^{2}}} = \gamma(x - \beta tc)\ \ \ \  \\ y' = y\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ z' = z\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ t' = \frac{t - \left( u\text{/}c^{2} \right)x}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \frac{t - \beta x\text{/}c}{\sqrt{1 - \beta^{2}}} = \gamma\left( t - \beta x\text{/}c \right) \end{array} \right.\$

其中

$\beta = \frac{u}{c}\text{，}\gamma = \frac{1}{\sqrt{1 - \beta^{2}}}$

逆变换

$\left\{ \begin{array}{r} x = \frac{x + ut'}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \frac{x' + ut'}{\sqrt{1 - \beta^{2}}} = \gamma\left( x' + \beta t'c \right)\ \ \ \ \ \ \  \\ y = y'\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ z = z'\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ t = \frac{t' + \left( u\text{/}c^{2} \right)x'}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \frac{t' + \beta x'\text{/}c}{\sqrt{1 - \beta^{2}}} = \gamma\left( t' + \beta x'\text{/}c \right) \end{array} \right.\$

$\gamma$称为空间缩放系数或尺缩因子。

洛伦兹速度变换式

$v_{x} = \frac{dx}{dt}\text{，}v_{y} = \frac{dy}{dt}\text{，}v_{z} = \frac{dz}{dt}\text{，}v_{x}' = \frac{dx'}{dt'}\text{，}v_{y}' = \frac{dy'}{dt'}\text{，}v_{z}' = \frac{dz'}{dt'}$

得到一个物体对两个惯性系的速度变换关系

$\left\{ \begin{array}{r} v_{x}' = \frac{v_{x} - u}{1 - uv_{x}\text{/}c^{2}} = \frac{v_{x} - u}{1 - \beta v_{x}\text{/}c}\ \ \ \ \  \\ v_{y}' = \frac{v_{y}\sqrt{1 - u^{2}\text{/}c^{2}}}{1 - uv_{x}\text{/}c^{2}} = \frac{v_{y}\text{/}\gamma}{1 - \beta v_{x}\text{/}c} \\ v_{z}' = \frac{v_{z}\sqrt{1 - u^{2}\text{/}c^{2}}}{1 - uv_{x}\text{/}c^{2}} = \frac{v_{z}\text{/}\gamma}{1 - \beta v_{x}\text{/}c} \end{array} \right.\$

特别地，当$v$平行于$x$轴和$x'$轴时，有

$v' = \frac{v - u}{1 - uv\text{/}c^{2}} = \frac{v - u}{1 - \beta v\text{/}c}$

时间延缓效应

设有相对运动的两惯性系$S$和$S'$，$S'$系相对$S$系的运动速度为$u$，某物理对象与$S'$系保持相对静止，在$S$系下观察该物理对象发生某个物理过程经历的时间$\Delta t$与在$S'$系下观察该物理对象发生同个物理过程经历的时间$\Delta\tau$（固有时/本征时间间隔）满足

$\Delta t = \gamma\Delta\tau$

其中

$\gamma = \frac{1}{\sqrt{1 - \beta^{2}}}\text{，}\beta = \frac{u}{c}$

从外界观察某物理过程经历的时间$\Delta t$大于该物理过程自身观察所得时间$\Delta\tau$

证明：设在$S'$系下看到同一地点$x_{0}'$处先后发生了两个事件，对应时间$t_{1}'$和$t_{2}'$，由逆变换，有

$\left\{ \begin{array}{r} t_{1} = \frac{t_{1}' + \left( u\text{/}c^{2} \right)x_{0}'}{\sqrt{1 - u^{2}\text{/}c^{2}}} \\ t_{2} = \frac{t_{2}' + \left( u\text{/}c^{2} \right)x_{0}'}{\sqrt{1 - u^{2}\text{/}c^{2}}} \end{array} \right.\$

两式相减，得

$\Delta t = t_{2} - t_{1} = \left( t_{2}' - t_{1}' \right)\text{/}\sqrt{1 - u^{2}\text{/}c^{2}} = \Delta\tau\text{/}\sqrt{1 - u^{2}\text{/}c^{2}}$

长度收缩效应

设有相对运动的两惯性系$S$和$S'$，$S'$系相对$S$系的运动速度为$u$，某物理对象与$S'$系保持相对静止，在$S$系下观察该物理对象的长度$l$与在$S'$系下观察该物理对象的长度$l_{0}$（固有长度/本征长度）满足

$l = l_{0}\sqrt{1 - u^{2}\text{/}c^{2}} = l_{0}\text{/}\gamma$

证明：

$\left\{ \begin{array}{r} x_{1}' = \frac{x_{1} - ut_{1}}{\sqrt{1 - u^{2}\text{/}c^{2}}} \\ x_{2}' = \frac{x_{2} - ut_{2}}{\sqrt{1 - u^{2}\text{/}c^{2}}} \end{array} \right.\$

由$t_{1} = t_{2}$，两式相减，得

$l_{0} = x_{2}' - x_{1}' = \frac{x_{1} - x_{2}}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \frac{l}{\sqrt{1 - u^{2}\text{/}c^{2}}}$

质量膨胀效应

设有相对运动的两惯性系$S$和$S'$，$S'$系相对$S$系的运动速度为$u$，某物理对象与$S'$系保持相对静止，在$S$系下观察该物理对象的质量$m$与在$S'$系下观察该物理对象的质量$m_{0}$（静止质量）满足

$m = \frac{m_{0}}{\sqrt{1 - u^{2}\text{/}c^{2}}} = \gamma m_{0}$

动量

$\mathbf{p} = m\mathbf{v}$

力

$\mathbf{F} = \frac{d\mathbf{p}}{dt} = \frac{d\left( m\mathbf{v} \right)}{dt} = \mathbf{v}\frac{dm}{dt} + m\frac{d\mathbf{v}}{dt}$

动能

${E_{k} = \int_{0}^{l}{\mathbf{f} \cdot d\mathbf{s}} }{= \int_{0}^{l}{\frac{d\left( m\mathbf{v} \right)}{dt} \cdot d\mathbf{s}} = \int_{0}^{l}{d\left( m\mathbf{v} \right) \cdot \frac{d\mathbf{s}}{dt}} }{= \int_{0}^{v}{d\left( m\mathbf{v} \right) \cdot d\mathbf{v}} = \int_{0}^{v}{\mathbf{v} \cdot d\left( \gamma m_{0}\mathbf{v} \right)} }{= \gamma m_{0}v^{2} - m_{0}\int_{0}^{v}{\gamma\mathbf{v} \cdot d\mathbf{v}} }{= \gamma m_{0}v^{2} + m_{0}c^{2}\text{/}\gamma - m_{0}c^{2} }{= mc^{2} - m_{0}c^{2} = \left( m - m_{0} \right)c^{2}}$

动能的近似

$E_{k} = mc^{2} - m_{0}c^{2} = \left( \frac{1}{\sqrt{1 - u^{2}\text{/}c^{2}}} - 1 \right)m_{0}c^{2}$

> $\text{把}\frac{u^{2}}{c^{2}}\text{看作整体，对}\frac{1}{\sqrt{1 - u^{2}\text{/}c^{2}}}\text{做泰勒展开，得}$

$E_{k} = \left( 1 + \frac{1}{2}\frac{v^{2}}{c^{2}} + o\left( \frac{v^{2}}{c^{2}} \right) - 1 \right)m_{0}c^{2} = \frac{1}{2}m_{0}v^{2}$

物体的能量

$E = E_{k} + m_{0}c^{2} = mc^{2} - m_{0}c^{2} + m_{0}c^{2} = mc^{2} = \gamma m_{0}c^{2}$

$E = mc^{2}$

其中$m_{0}c^{2}$称为静止能量。

推论

$m^{2}c^{2} - m^{2}v^{2} = m_{0}^{2}c^{2}$

> $\text{证明：}m = \gamma m_{0} = \frac{m_{0}}{\sqrt{1 - v^{2}\text{/}c^{2}}} \Rightarrow m^{2} = \frac{m_{0}^{2}}{1 - v^{2}\text{/}c^{2}} = \frac{m_{0}^{2}c^{2}}{c^{2} - v^{2}} \Rightarrow m^{2}c^{2} - m^{2}v^{2} = m_{0}^{2}c^{2}$

$p^{2}c^{2} = E^{2} - E_{0}^{2}$

> $m^{2}c^{2} - m^{2}v^{2} = m_{0}^{2}c^{2} \Rightarrow m^{2}c^{4} - m^{2}v^{2}c^{2} = m_{0}^{2}c^{4} \Rightarrow \left( mc^{2} \right)^{2} - (pc)^{2} = \left( m_{0}c^{2} \right)^{2} \Rightarrow p^{2}c^{2} = E^{2} - E_{0}^{2}$

热学

理想气体状态方程

由实验，有

$\frac{pV}{T} = C$

特别地有一组数据（标准状态）

$T_{0} = 273.15K\text{，}p_{0} = 1.013 \times 10^{5}Pa\text{，}V_{0} = \frac{M}{M_{mol}}V_{mol} = \frac{M}{M_{mol}} \cdot 22.4L$

则相应地得出

$pV = CT = \frac{p_{0}V_{0}}{T_{0}}T = \frac{p_{0}V_{mol}}{T_{0}}\frac{M}{M_{mol}}T\overset{R = \frac{p_{0}V_{mol}}{T_{0}}}{=}R\frac{M}{M_{mol}}T = R\frac{Nm}{N_{A}m}T = N\frac{R}{N_{A}}T\left\{ \begin{array}{r} \overset{k_{B} = \frac{R}{N_{A}}}{=}Nk_{B}T \\ \overset{\nu = \frac{N}{N_{A}}}{=}\nu RT\ \ \ \end{array} \right.\$

$p = \frac{N}{V}k_{B}T\overset{n = \frac{N}{V}}{=}nk_{B}T$

其中$R = 8.31J \cdot mol^{- 1} \cdot K^{- 1}$称为普适气体常量，$k_{B} = 1.38 \times 10^{- 23}J \cdot K^{- 1}$为玻尔兹曼常量，$p$为气体的压强，$V$为气体的体积，$T$为气体的温度，$M$为气体的质量，$M_{mol}$为气体摩尔质量，$N$为气体所含分子数，$m$为每个气体分子的质量，$\nu$为气体的物质的量（摩尔数），$n$为单位体积的分子数（分子数密度）。

气体分子平均速度

$\overline{v_{x}} = \left( \sum_{i = 1}^{N}v_{ix} \right)\text{/}N = 0\text{，}\overline{v_{y}} = \left( \sum_{i = 1}^{N}v_{iy} \right)\text{/}N = 0\text{，}\overline{v_{z}} = \left( \sum_{i = 1}^{N}v_{iz} \right)\text{/}N = 0$

$\text{定义}\overline{v_{x}^{2}} = \left( \sum_{i = 1}^{N}v_{ix}^{2} \right)\text{/}N\text{，}\overline{v_{y}^{2}} = \left( \sum_{i = 1}^{N}v_{iy}^{2} \right)\text{/}N\text{，}\overline{v_{z}^{2}} = \left( \sum_{i = 1}^{N}v_{iz}^{2} \right)\text{/}N\text{，由}\left\{ \begin{array}{r} \overline{v_{x}^{2}} = \overline{v_{y}^{2}} = \overline{v_{z}^{2}}\ \ \ \ \ \ \ \ \ \  \\ \overline{v_{x}^{2}} + \overline{v_{y}^{2}} + \overline{v_{z}^{2}} = \overline{v^{2}} \end{array} \right.\ \text{，得}$

$\overline{v_{x}^{2}} = \overline{v_{y}^{2}} = \overline{v_{z}^{2}} = \frac{1}{3}\overline{v^{2}}$

理想气体的压强公式

$p = \frac{1}{3}nm\overline{v^{2}}\overset{\overline{\varepsilon_{t}} = \frac{1}{2}m\overline{v^{2}}}{=}\frac{2}{3}n\overline{\varepsilon_{t}}$

其中$\overline{\varepsilon_{t}}$称为气体分子的平均平动动能

理想气体的温度公式

$\text{联立}\left\{ \begin{array}{r} p = nk_{B}T \\ p = \frac{2}{3}n\overline{\varepsilon_{t}} \end{array} \right.\ \text{，得分子平均平动动能}\overline{\varepsilon_{t}} = \frac{3}{2}kT$

气体分子的方均根速率

$\sqrt{\overline{v^{2}}} = \sqrt{\frac{3p}{nm}}\overset{\rho = nm}{=}\sqrt{\frac{3p}{\rho}}$

其中$\rho = nm$称为气体密度

气体分子的自由度

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

分子类型

</th>
<th>

平动自由度$t$

</th>
<th>

转动自由度$r$

</th>
<th>

振动自由度$s$

</th>
<th>

自由度

</th>
<th>

$i = t + r + 2s$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

单原子分子

</td>
<td>

$3$

</td>
<td>

$0$

</td>
<td>

$0$

</td>
<td>

$3$

</td>
<td>

$3$

</td>
</tr>
<tr>
<td>

双原子刚性分子

</td>
<td>

$3$

</td>
<td>

$2$

</td>
<td>

$0$

</td>
<td>

$5$

</td>
<td>

$5$

</td>
</tr>
<tr>
<td>

双原子非刚性分子

</td>
<td>

$3$

</td>
<td>

$2$

</td>
<td>

$1$

</td>
<td>

$6$

</td>
<td>

$7$

</td>
</tr>
<tr>
<td>

多原子刚性分子

（各原子不排列在一条直线上）

</td>
<td>

$3$

</td>
<td>

$3$

</td>
<td>

$0$

</td>
<td>

$6$

</td>
<td>

$6$

</td>
</tr>
<tr>
<td>

多原子非刚性分子

</td>
<td>

$3$

</td>
<td>

$3$

</td>
<td>

$3n - 6$

</td>
<td>

$3n$

</td>
<td>

$6n - 6$

</td>
</tr>
</tbody>
</table>
</div>

能量按自由度均分定理

在温度为$T$的平衡态下，气体分子每个自由度的平均动能都相等，其大小都等于$kT\text{/}2$。

记忆：由

$\left\{ \begin{array}{r} \overline{\varepsilon_{t}} = \frac{1}{2}mv^{2} = \frac{3}{2}kT\ \ \ \  \\ \overline{v_{x}^{2}} = \overline{v_{y}^{2}} = \overline{v_{z}^{2}} = \frac{1}{3}\overline{v^{2}} \end{array} \right.\$

得

$\frac{1}{2}m\overline{v_{x}^{2}} = \frac{1}{2}m\overline{v_{y}^{2}} = \frac{1}{2}m\overline{v_{z}^{2}} = \frac{1}{2}m\left( \frac{1}{3}\overline{v^{2}} \right) = \frac{1}{3}\left( \frac{1}{2}m\overline{v^{2}} \right) = \frac{1}{3}\left( \frac{3}{2}kT \right) = \frac{1}{2}kT$

表明分子在每一个平动自由度上具有相同的平均平动动能，大小为$kT\text{/}2$，而每个转动自由度和振动自由度的平均动能大小也等于每一个平动自由度的平均平动动能，即$kT\text{/}2$。

单个气体分子的平均总动能

$\overline{\varepsilon_{k}} = \frac{1}{2}(t + r + r)kT$

其中$t$是平动自由度，$r$是转动自由度，$r$是振动自由度。

单个气体分子的平均总能量

$\overline{\varepsilon} = \frac{1}{2}(t + r + 2s)kT\overset{i = t + r + 2s}{=}\frac{i}{2}kT$

这是因为振动自由度下除了振动动能还有振动势能，且振动势能等于振动动能。

理想气体的内能

理想气体的内能为气体分子的能量与分子间势能之和，因为理想气体要求不考虑分子间作用力，所以分子间势能为$0$。

$1mol$理想气体的内能为

$E_{mol} = \frac{i}{2}RT$

质量为$M$，摩尔质量$M_{mol}$为的理想气体的内能为

$E = \frac{M}{M_{mol}}\frac{i}{2}RT = \nu\frac{i}{2}RT$

麦克斯韦速率分布律

平衡态下，气体分子速率在$v\sim v + dv$区间的分子数占总分子数的百分比为

$\frac{dN}{N} = 4\pi\left( \frac{m}{2\pi kT} \right)^{3\text{/}2}v^{2}e^{- mv^{2}\text{/}2kT}dv$

对应速率分布函数

$f(v) = 4\pi\left( \frac{m}{2\pi kT} \right)^{3\text{/}2}v^{2}e^{- mv^{2}\text{/}2kT}$

在有限速率区间$v_{1}\sim v_{2}$内分子数占总分子树的百分比为

$\int_{v_{1}}^{v_{2}}{f(v)dv}$

气体分子的三个速率

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

最概然速率$v_{p}$

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

$\sqrt{\frac{2kT}{m}} = \sqrt{\frac{2RT}{M_{mol}}} \approx 1.41\sqrt{\frac{RT}{M_{mol}}}$

</td>
<td>

$\sqrt{\frac{8kT}{\pi m}} = \sqrt{\frac{8RT}{\pi M_{mol}}} \approx 1.60\sqrt{\frac{RT}{M_{mol}}}$

</td>
<td>

$\sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M_{mol}}} \approx 1.73\sqrt{\frac{RT}{M_{mol}}}$

</td>
</tr>
</tbody>
</table>
</div>

热力学第一定律

系统从外界吸收的热量$Q$等于系统内能的增量$\Delta E$和系统对外做功$A$的和

$Q = \Delta E + A$

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

$> 0$

</th>
<th>

$< 0$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$Q$

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

$A$

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

$\Delta E$

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

$C = \frac{dQ}{dT}\ \left( J \cdot K^{- 1} \right)$

比热（容）：$c\ \left( J \cdot kg^{- 1} \cdot K^{- 1} \right)$

摩尔热容量：$C_{m}\ \left( J \cdot mol^{- 1} \cdot K^{- 1} \right)$

$C = Mc\ \ \ C = \frac{M}{M_{mol}}C_{m}$

等体摩尔热容

在等体过程中，气体的吸热为

$Q = \nu C_{V,m}\left( T_{2} - T_{1} \right)$

$C_{V,m} = \frac{dQ\left. \  \right|_{V}}{dT}\underset{dA = 0}{\overset{dQ = dE + dA}{=}}\frac{dE}{dT}\underset{\nu = 1}{\overset{dE = \frac{i}{2}\nu RdT}{=}}\frac{i}{2}R\overset{E = \frac{i}{2}\nu RT}{\Rightarrow}E = \nu C_{V,m}T$

$C_{V,m} = \frac{i}{2}R\text{，}E = \nu C_{V,m}T$

等压摩尔热容

在等压过程中，气体的吸热为

$Q = \nu C_{V,m}\left( T_{2} - T_{1} \right)$

因为

$pV = \nu RT\overset{\nu = 1}{=}RT \Rightarrow pdV + Vdp = RdT\underset{dp = 0}{\overset{\ p\text{不变}\ }{\Rightarrow}}pdV = RdT\overset{\ dA = pdV\ }{\Rightarrow}dA = RdT$

所以

$C_{p,m} = \frac{dQ\left. \  \right|_{p}}{dT}\overset{dQ = dE + dA}{=}\frac{(dE + dA)\left. \  \right|_{p}}{dT}\overset{dA = RdT}{=}\frac{dE + RdT}{dT}\overset{C_{V,m} = \frac{dE}{dT}}{=}C_{V,m} + R$

$C_{p,m} = C_{V,m} + R = \left( \frac{i}{2} + 1 \right)R$

等值过程系统的做功、吸热和内能变化

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

等值过程

</th>
<th>

等体过程

$(n = + \infty)$

</th>
<th>

等压过程

$(n = 0)$

</th>
<th>

等温过程

$(n = 1)$

</th>
<th>

绝热过程

$(n = \gamma)$

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

$pV^{\gamma} = C$

$\gamma = C_{p,m}\text{/}C_{V,m}$

</td>
<td>

$pV^{n} = C$

</td>
</tr>
<tr>
<td>

状态参量

</td>
<td>

$\frac{p_{1}}{T_{1}} = \frac{p_{2}}{T_{2}}$

</td>
<td>

$\frac{V_{1}}{T_{1}} = \frac{V_{2}}{T_{2}}$

</td>
<td>

$p_{1}V_{1} = p_{2}V_{2}$

</td>
<td>

$p_{1}V_{1}^{\gamma} = p_{2}V_{2}^{\gamma}$

</td>
<td>

$p_{1}V_{1}^{n} = p_{2}V_{2}^{n}$

</td>
</tr>
<tr>
<td>

做功$A$

$\int_{V_{1}}^{V_{2}}{pdV}$

</td>
<td>

$0$

</td>
<td>

$p\left( V_{2} - V_{1} \right)$

$\nu R\left( T_{2} - T_{1} \right)$

</td>
<td>

$\nu RT\ln\frac{V_{2}}{V_{1}}$

</td>
<td>

$\frac{p_{1}V_{1} - p_{2}V_{2}}{\gamma - 1}$

</td>
<td>

$\frac{p_{1}V_{1} - p_{2}V_{2}}{n - 1}\ \ (n \neq 1)$

</td>
</tr>
<tr>
<td>

吸热$Q$

$A + \Delta E$

</td>
<td>

$\nu C_{V,m}\left( T_{2} - T_{1} \right)$

</td>
<td>

$\nu C_{p,m}\left( T_{2} - T_{1} \right)$

</td>
<td>

$\nu RT\ln\frac{V_{2}}{V_{1}}$

</td>
<td>

$0$

</td>
<td>

$\nu\left( C_{V,m} - \frac{R}{n - 1} \right)\left( T_{2} - T_{1} \right)$

$(n \neq 1)$

</td>
</tr>
<tr>
<td>

内能增量$\Delta E$

$\nu C_{V,m}\left( T_{2} - T_{1} \right)$

</td>
<td></td>
<td></td>
<td></td>
<td>

$- A$

</td>
<td></td>
</tr>
</tbody>
</table>
</div>

热机的效率

$\eta = \frac{W_{\text{有}}}{Q_{\text{吸}}} = \frac{Q_{\text{吸}} - Q_{\text{放}}}{Q_{\text{吸}}} = 1 - \frac{Q_{\text{放}}}{Q_{\text{吸}}}$

卡诺循环

$\eta = 1 - \frac{T_{2}}{T_{1}}$
