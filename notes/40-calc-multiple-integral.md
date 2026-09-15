---
title: 重积分与曲线曲面积分
description: 斯特林公式、直角坐标系下二重积分的累次计算、三重积分与柱/球坐标、第一与第二类曲线积分、格林公式、第一与第二类曲面积分、高斯公式、斯托克斯公式、梯度散度旋度。
---

# 重积分与曲线曲面积分

[[toc]]

斯特林公式

$$\lim_{n \rightarrow + \infty}\frac{e^{n}n!}{n^{n}\sqrt{n}} = \sqrt{2\pi}$$

用它可以近似n!

$$n! = \lim_{n \rightarrow + \infty}\frac{n^{n}\sqrt{2\pi n}}{e^{n}}$$

当n很大时，亦即

$$n! = \sqrt{2\pi n}\left( \frac{n}{e} \right)^{n}$$

eg.20! = 2, 432, 902, 008, 176, 640, 000 ≈ 2, 422, 786, 846, 761, 135, 000

50! = 3.0414093201713884 × 1064 ≈ 3.036344593938168 × 1064

直角坐标系下二重积分的累次计算方法

1.调换面积元素

∬Df(x，y)dσ = ∬Df(x，y)dxdy

2.选择积分次序

先y后x

∬Df(x，y)dxdy = ∫dx∫f(x，y)dy

先x后y

∬Df(x，y)dxdy = ∫dy∫f(x，y)dx

3.确定积分上下限

后计算的积分（即靠左的积分）的上下限由其被积表达式的变量对应的取值范围决定，先计算的积分（即靠右的积分）的上下限由D的边界的函数表达式决定，最后形式为。

先y后x

∬Df(x，y)dxdy = ∫abdx∫φ1(x)φ2(x)f(x，y)dy

先x后y

∬Df(x，y)dxdy = ∫abdy∫ψ1(y)ψ2(y)f(x，y)dx

其中a，b为不随x，y变化的常数。φ1(x)和φ2(x)是D的“下上边界”对应的y关于x的函数，ψ1(y)和ψ2(y)是D的“左右边界”分别对应的y关于x的函数。

计算两次定积分即得。

eg.∬Ddσ，其中D由直线y = 1，x = 2，y = x围成。

解：先y后x：

$$\iint_{D}^{}{f(x\text{，}y)d\sigma} = \int_{1}^{2}{dx\int_{1}^{x}{xydy}} = \int_{1}^{2}{\left\lbrack \frac{1}{2}xy^{2} \right\rbrack_{1}^{x}dx} = \int_{1}^{2}{\left( \frac{1}{2}x^{3} - \frac{1}{2}x \right)dx} = \left\lbrack \frac{x^{4}}{8} - \frac{x^{2}}{4} \right\rbrack_{1}^{2} = \frac{9}{8}$$

先x后y：

$$\iint_{D}^{}{f(x\text{，}y)d\sigma} = \int_{1}^{2}{dy\int_{y}^{2}{xydx}} = \int_{1}^{2}{\left\lbrack \frac{1}{2}yx^{2} \right\rbrack_{y}^{2}dy} = \int_{1}^{2}{\left( 2y - \frac{1}{2}y^{3} \right)dy} = \left\lbrack y^{2} - \frac{y^{4}}{8} \right\rbrack_{1}^{2} = \frac{9}{8}$$

$$eg.\iint_{D}^{}{\frac{x^{2}}{y^{2}}d\sigma}\text{，其中}D\text{由直线}y = x\text{，}x = 2\text{，}xy = 1\text{围成。}$$

解：先y后x：

$$\iint_{D}^{}{f(x\text{，}y)d\sigma} = \int_{1}^{2}{x^{2}dx\int_{\frac{1}{x}}^{x}{\frac{1}{y^{2}}dy}} = \int_{1}^{2}{x^{2}\left\lbrack - \frac{1}{y} \right\rbrack_{\frac{1}{x}}^{x}dx} = \int_{1}^{2}{\left( x^{3} - x \right)dx}$$

先x后y：

$${\iint_{D}^{}{f(x\text{，}y)d\sigma} = \int_{\frac{1}{2}}^{2}{\frac{1}{y^{2}}dy\int_{?}^{2}{x^{2}dx}}
}{= \iint_{D_{1}}^{}{\frac{x^{2}}{y^{2}}d\sigma} + \iint_{D_{2}}^{}{\frac{x^{2}}{y^{2}}d\sigma}
}{= \int_{\frac{1}{2}}^{2}{\frac{1}{y^{2}}dy\int_{\frac{1}{y}}^{2}{x^{2}dx}} + \int_{\frac{1}{2}}^{2}{\frac{1}{y^{2}}dy\int_{y}^{2}{x^{2}dx}}}$$

三重积分

∭Ωf(x，y，z)dv

1.化为一个定积分嵌套于一个二重积分中

∭Ωf(x，y，z)dv = ∬Ddxdy∫z1(x, y)z2(x, y)f(x，y，z)dz

其中D是垂直于z轴平面的平面切立体得到的平面，z1(x, y)和z2(x, y)是立体的上下边界面（从z轴方向看）。

2.化为一个二重积分嵌套于一个定积分中

∭Ωf(x，y，z)dv = ∫c1c2dz∬Df(x，y，z)dxdy

其中D是垂直于z轴平面的平面切立体得到的平面，c1和c2是立体的z坐标的最小值和最大值。

3.利用柱坐标计算

根据柱坐标变换公式

$$\left\{ \begin{array}{r}
x = \rho\cos\theta \\
y = \rho\sin\theta \\
z = z\ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

有

∭Ωf(x，y，z)dv = ∭Ωf(ρcos θ，ρsin θ，z)ρdθdρdz

4.利用球坐标计算

根据球坐标变换公式

$$\left\{ \begin{array}{r}
x = r\sin\varphi\cos\theta\ \ \ \ \ \ \ \ \ \  \\
y = r\sin\varphi\sin\theta\ \ \ \ \ \ \ \ \ \ \  \\
z = r\cos\varphi\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
dv = r^{2}\sin\varphi drd\varphi d\theta
\end{array} \right.\ $$

∭Ωf(x，y，z)dv = ∭Ωf(rsin φcos θ，rsin φsin θ，rcos φ)r2sin φdθdφdr

第一类曲线积分

设曲线由参数方程$\left\{ \begin{array}{r}
x = \varphi(t) \\
y = \psi(t)
\end{array} \right.\ $决定，则

$$\int_{L}^{}{f(x\text{，}y)ds} = \int_{\alpha}^{\beta}{f\left\lbrack \varphi(t)\text{，}\psi(t) \right\rbrack\sqrt{\varphi^{2}(t) + \psi^{2}(t)}dt}$$

$$\text{记忆：}ds = \sqrt{(dx)^{2} + (dy)^{2}} = \sqrt{\left( \frac{dx}{dt} \right)^{2} + \left( \frac{dy}{dt} \right)^{2}} \cdot dt = \sqrt{\varphi^{2}(t) + \psi^{2}(t)}dt$$

特别地，取t = x或t = y，有

$$\int_{L}^{}{f(x\text{，}y)ds} = \left\{ \begin{array}{r}
\int_{x_{1}}^{x_{2}}{f\left( x\text{，}y(x) \right)\sqrt{1 + {y_{x}'}^{2}}dx} \\
\int_{y_{1}}^{y_{2}}{f\left( x(y)\text{，}y \right)\sqrt{\,{x_{y}'}^{2} + 1}}dy
\end{array} \right.\ $$

第二类曲线积分

设曲线由参数方程$\left\{ \begin{array}{r}
x = \varphi(t) \\
y = \psi(t)
\end{array} \right.\ $决定，则

∫LP(x，y)dx + Q(x，y)dy = ∫αβ{P[φ(t)，ψ(t)]φ′(t) + Q[φ(t)，ψ(t)]ψ′(t)}dt

特别地，取t = x或t = y，有

$$\int_{L}^{}{P(x\text{，}y)dx + Q(x\text{，}y)dy} = \left\{ \begin{array}{r}
\int_{x_{1}}^{x_{2}}{\left\lbrack P(x\text{，}y) + Q(x\text{，}y)y_{x}' \right\rbrack dx}\ \ (t = x) \\
\int_{y_{1}}^{y_{2}}{\left\lbrack P(x\text{，}y)x_{y}' + Q(x\text{，}y) \right\rbrack dy}\ \ (t = y)
\end{array} \right.\ $$

特别地，若积分路径无关，从点A(x1，y1)到点B(x2，y2)，有

$$\int_{L}^{}{P(x\text{，}y)dx + Q(x\text{，}y)dy} = \left\{ \begin{array}{r}
\int_{x_{1}}^{x_{2}}{P\left( x\text{，}y_{1} \right)dx} + \int_{y_{1}}^{y_{2}}{Q\left( x_{2}\text{，}y \right)dy}\ \ (\text{先横后竖}) \\
\int_{y_{1}}^{y_{2}}{Q\left( x_{1}\text{，}y \right)dy} + \int_{x_{1}}^{x_{2}}{P\left( x\text{，}y_{2} \right)dx}\ \ (\text{先竖后横})
\end{array} \right.\ $$

格林公式

$$\iint_{D}^{}{\left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)dxdy} = \oint_{L}^{}{Pdx + Qdy}$$

$$\text{特别地，若}\left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)\text{，则}Pdx + Qdy\text{是某个函数}u(x\text{，}y)\text{的全微分，且}$$

u(x，y) = ∫A(0, 0)B(x, y)Pdx + Qdy + C  (C为任意常数)

第一类曲面积分

对于由函数关系z = z(x，y)描述的曲面，有

$$\iint_{\Sigma}^{}{f(x\text{，}y\text{，}z)dS} = \iint_{D_{xy}}^{}{f\left\lbrack x\text{，}y\text{，}z(x\text{，}y) \right\rbrack\sqrt{1 + z_{x}^{2}(x\text{，}y) + z_{y}^{2}(x\text{，}y)}dxdy}$$

其中Dxy为曲面在xOy平面的投影。

第二类曲面积分

对于由函数关系z = z(x，y)描述的曲面，有

∬ΣPdydz + Qdzdx + Rdxdy = ∬Σ[P ⋅ (−zx′) + Q ⋅ (−zy′) + R]dxdy = ∬Σ(P，Q，R)(−zx′， − zy′，1)dxdy = ±∬Dxy[P ⋅ (−zx′(x，y)) + Q ⋅ (−zy′(x，y)) + R]dxdy

其中Dxy为曲面在xOy平面的投影。

两类曲面积分的关系

∬ΣPdydz + Qdzdx + Rdxdy = ∬Σ(Pcos α + Qcos β + Rcos γ)dS

高斯公式

$$\iiint_{\Omega}^{}{\left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} \right)dv} = ∯_{\Sigma}^{}{Pdydz + Qdzdx + Rdxdy}$$

斯托克斯公式

$$\iint_{\Sigma}^{}{\left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right)dydz + \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right)dzdx + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)dxdy} = \oint_{\Gamma}^{}{Pdx + Qdy + Rdz}$$

记忆

$$\left| \begin{matrix}
dydz & dzdx & dxdy \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
P & Q & R
\end{matrix} \right|\ \ \text{或}\ \ \begin{matrix}
x & y & z & x & y & z \\
P & Q & R & P & Q & R
\end{matrix}$$

在此处键入公式。

梯度、散度和旋度

函数f(x，y，z)的梯度

grad f = fx′i + fy′j + fz′k

向量场A(x，y，z) = P(x，y，z)i + Q(x，y，z)j + R(x，y，z)k的散度

$$div\ \mathbf{A} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

旋度

$$rot\ \mathbf{A} = \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right)\mathbf{i} + \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right)\mathbf{j} + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)\mathbf{k}$$

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

平面板（薄片）

</th>
<th>

空间体

</th>
<th>

曲线

</th>
<th>

曲面

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

几何度量

</td>
<td>

面积

$$S = \iint_{D}^{}{d\sigma}$$

</td>
<td>

体积

$$V = \iiint_{\Omega}^{}{dv}$$

</td>
<td>

弧长

$$L = \int_{C}^{}{ds}$$

</td>
<td>

面积

$$S = \iint_{\Sigma}^{}{dS}$$

</td>
</tr>
<tr>
<td>

质量

</td>
<td>

$$\iint_{D}^{}{\mu d\sigma}$$

</td>
<td>

$$\iiint_{\Omega}^{}{\rho dv}$$

</td>
<td>

$$\int_{C}^{}{fds}$$

</td>
<td>

$$\iint_{\Sigma}^{}{\mu dS}$$

</td>
</tr>
<tr>
<td>

质心

</td>
<td>

$$\overline{x} = \frac{1}{M}\iint_{D}^{}{x\mu d\sigma}$$

$$\overline{y} = \frac{1}{M}\iint_{D}^{}{y\mu d\sigma}$$

$$M = \iint_{D}^{}{\mu d\sigma}$$

</td>
<td>

$$\overline{x} = \frac{1}{M}\iiint_{\Sigma}^{}{x\rho dv}$$

$$\overline{y} = \frac{1}{M}\iiint_{\Sigma}^{}{y\rho dv}$$

$$\overline{z} = \frac{1}{M}\iiint_{\Sigma}^{}{z\rho dv}$$

$$M = \iiint_{\Sigma}^{}{\rho dv}$$

</td>
<td></td>
<td></td>
</tr>
<tr>
<td>

转动惯量

</td>
<td>

$$I_{x} = \iint_{D}^{}{y^{2}\mu d\sigma}$$

$$I_{y} = \iint_{D}^{}{x^{2}\mu d\sigma}$$

</td>
<td>

$$I_{x} = \iiint_{\Omega}^{}{\left( y^{2} + z^{2} \right)\rho dv}$$

$$I_{y} = \iiint_{\Omega}^{}{\left( x^{2} + z^{2} \right)\rho dv}$$

$$I_{z} = \iiint_{\Omega}^{}{\left( x^{2} + y^{2} \right)\rho dv}$$

</td>
<td></td>
<td></td>
</tr>
<tr>
<td>

引力

</td>
<td colspan="4">

空间物体对物体外一点$\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)$处单位质量的质点的引力

$$\mathbf{F} = \left( \iiint_{\Omega}^{}\frac{G\rho\left( x - x_{0} \right)}{r^{3}}\text{，}\iiint_{\Omega}^{}\frac{G\rho\left( y - y_{0} \right)}{r^{3}}\text{，}\iiint_{\Omega}^{}\frac{G\rho\left( z - z_{0} \right)}{r^{3}} \right)$$

</td>
</tr>
</tbody>
</table>
</div>
