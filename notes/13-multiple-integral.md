---
title: 重积分与曲线曲面积分
description: 二重与三重积分、曲线与曲面积分、格林/高斯/斯托克斯公式、梯度散度旋度。
---

# 重积分与曲线曲面积分

[[toc]]

### 1.调换面积元素

$$\iint_{D}^{}{f(x\text{，}y)d\sigma} = \iint_{D}^{}{f(x\text{，}y)dxdy}$$

### 2.选择积分次序

> 先$y$后$x$

$$\iint_{D}^{}{f(x\text{，}y)dxdy} = \int_{}^{}{dx\int_{}^{}{f(x\text{，}y)dy}}$$

> 先$x$后$y$

$$\iint_{D}^{}{f(x\text{，}y)dxdy} = \int_{}^{}{dy\int_{}^{}{f(x\text{，}y)dx}}$$

### 3.确定积分上下限

后计算的积分（即靠左的积分）的上下限由其被积表达式的变量对应的取值范围决定，先计算的积分（即靠右的积分）的上下限由D的边界的函数表达式决定，最后形式为。

> 先$y$后$x$

$$\iint_{D}^{}{f(x\text{，}y)dxdy} = \int_{a}^{b}{dx\int_{\varphi_{1}(x)}^{\varphi_{2}(x)}{f(x\text{，}y)dy}}$$

> 先$x$后$y$

$$\iint_{D}^{}{f(x\text{，}y)dxdy} = \int_{a}^{b}{dy\int_{\psi_{1}(y)}^{\psi_{2}(y)}{f(x\text{，}y)dx}}$$

其中$a\text{，}b$为不随$x\text{，}y$变化的常数。$\varphi_{1}(x)$和$\varphi_{2}(x)$是$D$的"下上边界"对应的$y$关于$x$的函数，$\psi_{1}(y)$和$\psi_{2}(y)$是$D$的"左右边界"分别对应的$y$关于$x$的函数。

计算两次定积分即得。

## 三重积分

$$\iiint_{\Omega}^{}{f(x\text{，}y\text{，}z)dv}$$

### 1.化为一个定积分嵌套于一个二重积分中

$$\iiint_{\Omega}^{}{f(x\text{，}y\text{，}z)dv} = \iint_{D}^{}{dxdy\int_{z_{1}(x,y)}^{z_{2}(x,y)}{f(x\text{，}y\text{，}z)dz}}$$

其中$D$是垂直于$z$轴平面的平面切立体得到的平面，$z_{1}(x,\ y)$和$z_{2}(x,y)$是立体的上下边界面（从z轴方向看）。

### 2.化为一个二重积分嵌套于一个定积分中

$$\iiint_{\Omega}^{}{f(x\text{，}y\text{，}z)dv} = \int_{c_{1}}^{c_{2}}{dz\iint_{D}^{}{f(x\text{，}y\text{，}z)dxdy}}$$

其中$D$是垂直于$z$轴平面的平面切立体得到的平面，$c_{1}$和$c_{2}$是立体的$z$坐标的最小值和最大值。

### 3.利用柱坐标计算

根据柱坐标变换公式

$$\left\{ \begin{array}{r}
x = \rho\cos\theta \\
y = \rho\sin\theta \\
z = z\ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

有

$$\iiint_{\Omega}^{}{f(x\text{，}y\text{，}z)dv} = \iiint_{\Omega}^{}{f\left( \rho\cos\theta \text{，}\rho\sin\theta \text{，}z \right)\rho d\theta d\rho dz}$$

### 4.利用球坐标计算

根据球坐标变换公式

$$\left\{ \begin{array}{r}
x = r\sin\varphi\cos\theta\ \ \ \ \ \ \ \ \ \  \\
y = r\sin\varphi\sin\theta\ \ \ \ \ \ \ \ \ \ \  \\
z = r\cos\varphi\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
dv = r^{2}\sin\varphi drd\varphi d\theta
\end{array} \right.\ $$

$$\iiint_{\Omega}^{}{f(x\text{，}y\text{，}z)dv} = \iiint_{\Omega}^{}{f\left( r\sin\varphi\cos\theta \text{，}r\sin\varphi\sin\theta \text{，}r\cos\varphi \right)r^{2}\sin\varphi d\theta d\varphi dr}$$

### 5.换元法

$$\iiint_{\Omega}^{}{f(x\text{，}y\text{，}z)dv} = \iiint_{\Omega}^{}{f\left( x(u\text{，}v\text{，}w)\text{，}y(u\text{，}v\text{，}w)\text{，}z(u\text{，}v\text{，}w) \right)\left| J(u\text{，}v\text{，}w) \right|dudvdw}$$

其中

$$J(u\text{，}v\text{，}w) = \frac{\partial(x\text{，}y\text{，}z)}{\partial(u\text{，}v\text{，}w)} = \left| \begin{matrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\
\frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w}
\end{matrix} \right|$$

## 第一类曲线积分

设曲线由参数方程$\left\{ \begin{array}{r}
x = \varphi(t) \\
y = \psi(t)
\end{array} \right.\$决定，则

$$\int_{L}^{}{f(x\text{，}y)ds} = \int_{\alpha}^{\beta}{f\left\lbrack \varphi(t)\text{，}\psi(t) \right\rbrack\sqrt{\varphi^{2}(t) + \psi^{2}(t)}dt}$$

$$\text{记忆：}ds = \sqrt{(dx)^{2} + (dy)^{2}} = \sqrt{\left( \frac{dx}{dt} \right)^{2} + \left( \frac{dy}{dt} \right)^{2}} \cdot dt = \sqrt{\varphi^{2}(t) + \psi^{2}(t)}dt$$

特别地，取$t = x$或$t = y$，有

$$\int_{L}^{}{f(x\text{，}y)ds} = \left\{ \begin{array}{r}
\int_{x_{1}}^{x_{2}}{f\left( x\text{，}y(x) \right)\sqrt{1 + {y_{x}'}^{2}}dx} \\
\int_{y_{1}}^{y_{2}}{f\left( x(y)\text{，}y \right)\sqrt{\,{x_{y}'}^{2} + 1\,}}dy
\end{array} \right.\ $$

## 第二类曲线积分

设曲线由参数方程$\left\{ \begin{array}{r}
x = \varphi(t) \\
y = \psi(t)
\end{array} \right.\$决定，则

$$\int_{L}^{}{P(x\text{，}y)dx + Q(x\text{，}y)dy} = \int_{\alpha}^{\beta}{\left\{ P\left\lbrack \varphi(t)\text{，}\psi(t) \right\rbrack\varphi'(t) + Q\left\lbrack \varphi(t)\text{，}\psi(t) \right\rbrack\psi'(t) \right\} dt}$$

特别地，取$t = x$或$t = y$，有

$$\int_{L}^{}{P(x\text{，}y)dx + Q(x\text{，}y)dy} = \left\{ \begin{array}{r}
\int_{x_{1}}^{x_{2}}{\left\lbrack P(x\text{，}y) + Q(x\text{，}y)y_{x}' \right\rbrack dx}\ \ (t = x) \\
\int_{y_{1}}^{y_{2}}{\left\lbrack P(x\text{，}y)x_{y}' + Q(x\text{，}y) \right\rbrack dy}\ \ (t = y)
\end{array} \right.\ $$

特别地，若积分路径无关，从点$A\left( x_{1}\text{，}y_{1} \right)$到点$B(x_{2}\text{，}y_{2})$，有

$$\int_{L}^{}{P(x\text{，}y)dx + Q(x\text{，}y)dy} = \left\{ \begin{array}{r}
\int_{x_{1}}^{x_{2}}{P\left( x\text{，}y_{1} \right)dx} + \int_{y_{1}}^{y_{2}}{Q\left( x_{2}\text{，}y \right)dy}\ \ (\text{先横后竖}) \\
\int_{y_{1}}^{y_{2}}{Q\left( x_{1}\text{，}y \right)dy} + \int_{x_{1}}^{x_{2}}{P\left( x\text{，}y_{2} \right)dx}\ \ (\text{先竖后横})
\end{array} \right.\ $$

## 格林公式

$$\iint_{D}^{}{\left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)dxdy} = \oint_{L}^{}{Pdx + Qdy}$$

$$\text{特别地，若}\left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)\text{，则}Pdx + Qdy\text{是某个函数}u(x\text{，}y)\text{的全微分，且}$$

$$u(x\text{，}y) = \int_{A(0,0)}^{B(x,y)}{Pdx + Qdy} + C\ \ (C\text{为任意常数})$$

## 第一类曲面积分

对于由函数关系$z = z(x\text{，}y)$描述的曲面，有

$$\iint_{\Sigma}^{}{f(x\text{，}y\text{，}z)dS} = \iint_{D_{xy}}^{}{f\left\lbrack x\text{，}y\text{，}z(x\text{，}y) \right\rbrack\sqrt{1 + z_{x}^{2}(x\text{，}y) + z_{y}^{2}(x\text{，}y)}dxdy}$$

其中$D_{xy}$为曲面在$xOy$平面的投影。

## 第二类曲面积分

对于由函数关系$z = z(x\text{，}y)$描述的曲面，有

$${\iint_{\Sigma}^{}{Pdydz + Qdzdx + Rdxdy} = \iint_{\Sigma}^{}{\left\lbrack P \cdot \left( - z_{x}' \right) + Q \cdot \left( - z_{y}' \right) + R \right\rbrack dxdy} = \iint_{\Sigma}^{}{(P\text{，}Q\text{，}R)\left( - z_{x}'\text{，} - z_{y}'\text{，}1 \right)dxdy}
}{= \pm \iint_{D_{xy}}^{}{\left\lbrack P \cdot \left( - z_{x}'(x\text{，}y) \right) + Q \cdot \left( - z_{y}'(x\text{，}y) \right) + R \right\rbrack dxdy}}$$

其中$D_{xy}$为曲面在$xOy$平面的投影。

## 两类曲面积分的关系

$$\iint_{\Sigma}^{}{Pdydz + Qdzdx + Rdxdy} = \iint_{\Sigma}^{}{\left( P\cos\alpha + Q\cos\beta + R\cos\gamma \right)dS}$$

## 高斯公式

$$\iiint_{\Omega}^{}{\left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} \right)dv} = ∯_{\Sigma}^{}{Pdydz + Qdzdx + Rdxdy}$$

## 斯托克斯公式

$$\iint_{\Sigma}^{}{\left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right)dydz + \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right)dzdx + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)dxdy} = \oint_{\Gamma}^{}{Pdx + Qdy + Rdz}$$

### 记忆

$$\left| \begin{matrix}
dydz & dzdx & dxdy \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
P & Q & R
\end{matrix} \right|\ \ \text{或}\ \ \begin{matrix}
x & y & z & x & y & z \\
P & Q & R & P & Q & R
\end{matrix}$$

$\text{在此处键入公式。}$

## 梯度、散度和旋度

函数$f(x\text{，}y\text{，}z)$的梯度

$$\mathbf{grad}\ f = f_{x}'\mathbf{i} + f_{y}'\mathbf{j} + f_{z}'\mathbf{k}$$

向量场

$$
\mathbf{A}(x\text{，}y\text{，}z) = P(x\text{，}y\text{，}z)\mathbf{i} + Q(x\text{，}y\text{，}z)\mathbf{j} + R(x\text{，}y\text{，}z)\mathbf{k}
$$

的散度

$$div\ \mathbf{A} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

### 旋度

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

$$S = \iint_{D}^{}{d\sigma}$$

</td>
<td>

$$V = \iiint_{\Omega}^{}{dv}$$

</td>
<td>

$$L = \int_{C}^{}{ds}$$

</td>
<td>

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
<td>

空间物体对物体外一点$\left( x_{0}\text{，}y_{0}\text{，}z_{0} \right)$处单位质量的质点的引力

$$\mathbf{F} = \left( \iiint_{\Omega}^{}\frac{G\rho\left( x - x_{0} \right)}{r^{3}}\text{，}\iiint_{\Omega}^{}\frac{G\rho\left( y - y_{0} \right)}{r^{3}}\text{，}\iiint_{\Omega}^{}\frac{G\rho\left( z - z_{0} \right)}{r^{3}} \right)$$

</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>
