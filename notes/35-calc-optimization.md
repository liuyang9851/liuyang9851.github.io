---
title: 最值与微分中值定理
description: 拉格朗日乘数法求最值、费马引理、罗尔定理、拉格朗日中值定理、柯西中值定理、一类中值题的通解、曲率与曲率半径、曲率中心。
---

# 最值与微分中值定理

[[toc]]

$$\left\{ \begin{array}{r}
y_{1} = f_{1}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right) \\
y_{2} = f_{2}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right) \\
\cdots \\
y_{m} = f_{m}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right)
\end{array} \right.\ $$

定义

$$\left( \frac{\partial f_{i}}{\partial x_{j}}\left( \mathbf{x}^{0} \right) \right)_{m \times n} = \mathbf{f}'\left( \mathbf{x}^{0} \right) = \mathbf{Df}\left( \mathbf{x}^{0} \right) = \mathbf{J}_{\mathbf{f}}\left( \mathbf{x}^{0} \right) = \begin{pmatrix}
\frac{\partial f_{1}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) & \frac{\partial f_{1}}{\partial x_{2}}\left( \mathbf{x}^{0} \right) & \cdots & \frac{\partial f_{1}}{\partial x_{n}}\left( \mathbf{x}^{0} \right) \\
\frac{\partial f_{2}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) & \frac{\partial f_{2}}{\partial x_{2}}\left( \mathbf{x}^{0} \right) & \cdots & \frac{\partial f_{2}}{\partial x_{n}}\left( \mathbf{x}^{0} \right) \\
 \vdots & \vdots & & \vdots \\
\frac{\partial f_{m}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) & \frac{\partial f_{m}}{\partial x_{2}}\left( \mathbf{x}^{0} \right) & \cdots & \frac{\partial f_{m}}{\partial x_{n}}\left( \mathbf{x}^{0} \right)
\end{pmatrix}$$

为向量值函数f在x0点的导数或Jacobi（雅可比）矩阵

特别地，对于m = 1的情况，即一元向量值函数，有

$$\mathbf{f}'\left( \mathbf{x}^{0} \right) = \begin{pmatrix}
\frac{\partial f_{1}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) \\
\frac{\partial f_{2}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) \\
 \vdots \\
\frac{\partial f_{m}}{\partial x_{1}}\left( \mathbf{x}^{0} \right)
\end{pmatrix} = \frac{\partial f_{1}}{\partial x_{1}}\mathbf{e}_{1} + \frac{\partial f_{2}}{\partial x_{1}}\mathbf{e}_{2} + \cdots + \frac{\partial f_{m}}{\partial x_{1}}\mathbf{e}_{m}$$

导数的四则运算法则的证明（同济）

$${\left\lbrack f(x) \pm g(x) \right\rbrack' = \lim_{\Delta x \rightarrow 0}\frac{\left\lbrack f(x + \Delta x) \pm g(x + \Delta x) \right\rbrack - \left\lbrack f(x) \pm g(x) \right\rbrack}{\Delta x}
}{= \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x) - f(x)}{\Delta x} \pm \lim_{\Delta x \rightarrow 0}\frac{g(x + \Delta x) - g(x)}{\Delta x}
}{= f'(x) + g'(x)}$$

$${\left\lbrack f(x)g(x) \right\rbrack' = \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x)g(x + \Delta x) - f(x)g(x)}{\Delta x}
}{= \lim_{\Delta x \rightarrow 0}\left\lbrack \frac{f(x + \Delta x) - f(x)}{\Delta x} \cdot g(x + \Delta x) + f(x) \cdot \frac{g(x + \Delta x) - g(x)}{\Delta x} \right\rbrack
}{= \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x) - f(x)}{\Delta x} \cdot \lim_{\Delta x \rightarrow 0}{g(x + \Delta x)} + f(x) \cdot \lim_{\Delta x \rightarrow 0}\frac{g(x + \Delta x) - g(x)}{\Delta x}
}{= f'(x)g(x) + f(x)g'(x)}$$

$${\left\lbrack \frac{f(x)}{g(x)} \right\rbrack' = \lim_{\Delta x \rightarrow 0}\frac{\frac{f(x + \Delta x)}{g(x + \Delta x)} - \frac{f(x)}{g(x)}}{\Delta x}
}{= \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x)g(x) - f(x)g(x + \Delta x)}{g(x + \Delta x)g(x)\Delta x}
}{= \lim_{\Delta x \rightarrow 0}\frac{\left\lbrack f(x + \Delta x) - f(x) \right\rbrack g(x) - f(x)\left\lbrack g(x + \Delta x) - g(x) \right\rbrack}{g(x + \Delta x)g(x)\Delta x}
}{= \lim_{\Delta x \rightarrow 0}\frac{\frac{f(x + \Delta x) - f(x)}{\Delta x}g(x) - f(x)\frac{g(x + \Delta x) - g(x)}{\Delta x}}{g(x + \Delta x)g(x)}
}{= \frac{f'(x)g(x) - f(x)g'(x)}{g^{2}(x)}}$$

部分基本初等函数的导数公式的证明

1.常函数：f(x) = C

$$f'(x) = \lim_{h \rightarrow 0}\frac{f(x + h) - f(x)}{h} = \lim_{h \rightarrow 0}\frac{C - C}{h} = 0$$

2.幂函数（部分）：f(x) = xn  (x > 0)

$$\text{当}n = 1\text{时，}f'(x) = \lim_{h \rightarrow 0}\frac{x + h - x}{h} = 1$$

$$\text{当}n > 1\text{时，}f'(x) = \lim_{h \rightarrow 0}\frac{(x + h)^{n} - x^{n}}{h} = \lim_{h \rightarrow 0}\left\lbrack nx^{n - 1} + \frac{n(n - 1)}{2}x^{n - 2}h + \cdots + h^{n - 1} \right\rbrack = nx^{n - 1}$$

3.正弦函数：f(x) = sin x

$$f'(x) = \lim_{h \rightarrow 0}\frac{\sin(x + h) - \sin x}{h} = \lim_{h \rightarrow 0}{\frac{1}{h} \cdot 2\cos\left( x + \frac{h}{2} \right)\sin\frac{h}{2}} = \lim_{h \rightarrow 0}{\cos\left( x + \frac{h}{2} \right) \cdot \frac{\sin\frac{h}{2}}{\frac{h}{2}}} = \cos x$$

4.余弦函数：f(x) = cos x

$$f'(x) = \lim_{h \rightarrow 0}\frac{\cos(x + h) - \cos x}{h} = \lim_{h \rightarrow 0}{\frac{- 1}{h} \cdot 2\sin\left( x + \frac{h}{2} \right)\sin\frac{h}{2}} = \lim_{h \rightarrow 0}{- \sin\left( x + \frac{h}{2} \right) \cdot \frac{\sin\frac{h}{2}}{\frac{h}{2}}} = - \sin x$$

5.对数函数：f(x) = logax  (a > 0,  a ≠ 1)

$$f'(x) = \lim_{h \rightarrow 0}\frac{\log_{a}(x + h) - \log_{a}x}{h} = \frac{1}{\ln a} \cdot \lim_{h \rightarrow 0}\frac{\ln\left( 1 + \frac{h}{x} \right)}{h} = \frac{1}{\ln a} \cdot \lim_{h \rightarrow 0}\frac{\frac{h}{x}}{h} = \frac{1}{x\ln a}\ \ \ \left( \ln{(1 + x)\ \sim\ }x \right)$$

6.指数函数：f(x) = ax  (a ≠ 0)

$$f'(x) = \lim_{h \rightarrow 0}\frac{a^{x + h} - a^{x}}{h} = a^{x} \cdot \lim_{h \rightarrow 0}\frac{a^{h} - 1}{h} = a^{x} \cdot \lim_{h \rightarrow 0}\frac{h\ln a}{h} = a^{x}\ln a\ \ \left( a^{x} - 1\ \sim\ \ x\ln a \right)$$

7.幂函数：f(x) = xa  (x > 0)

$$f'(x) = \lim_{h \rightarrow 0}\frac{(x + h)^{a} - x^{h}}{h} = x^{a} \cdot \lim_{h \rightarrow 0}\frac{\left( 1 + \frac{h}{x} \right)^{a} - 1}{x \cdot \frac{h}{x}} = x^{a} \cdot \lim_{h \rightarrow 0}\frac{\frac{ah}{x}}{x \cdot \frac{h}{x}} = ax^{a - 1}\ \ \left( (1 + x)^{m} - 1\ \sim\ mx \right)$$

高阶导数

二阶导数、三阶导数、四阶导数、n阶导数可用如下符号表示

$$y^{''}\ \ \frac{d^{2}y}{dx^{2}}\text{，}y^{'''}\ \ \frac{d^{3}y}{dx^{3}}\text{，}y^{(4)}\ \ \frac{d^{4}y}{dx^{4}}\text{，}y^{(n)}\ \ \frac{d^{n}y}{dx^{n}}$$

零阶导数f(0)(x)可视作原函数f(x)

高阶导数的三则运算法则：

$$
\left\lbrack f(x) \pm g(x) \right\rbrack^{(n)} = \left\lbrack f(x) \right\rbrack^{(n)} \pm \left\lbrack g(x) \right\rbrack^{(n)} = f^{(n)}(x) \pm g^{(n)}(x)
$$

$$
\left\lbrack Cf(x) \right\rbrack^{(n)} = C \cdot f^{(n)}(x)
$$

$$Leibniz\text{（莱布尼兹）公式：}\left\lbrack f(x) \cdot g(x) \right\rbrack^{(n)} = \sum_{k = 0}^{n}{C_{n}^{k}f^{(n - k)}(x)g^{(k)}(x)}$$

常见函数的高阶导数：

(ax)(n) = (ln a)nax

$$\left( \sin x \right)^{(n)} = \sin\left( x + \frac{n\pi}{2} \right)$$

$$\left( \cos x \right)^{(n)} = \cos\left( x + \frac{n\pi}{2} \right)$$

$$\left( \sin{kx} \right)^{(n)} = k^{n}\sin\left( kx + \frac{n\pi}{2} \right)$$

$$\left( \cos{kx} \right)^{(n)} = k^{n}\cos\left( kx + \frac{n\pi}{2} \right)$$

$$\left( x^{m} \right)^{(n)} = \left\{ \begin{array}{r}
m(m - 1)\cdots(m - n + 1)x^{m - n} = A_{m}^{n}x^{m - n}\ \ \ \ n \leq m \\
0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ n > m
\end{array} \right.\ $$

(xn)(n) = n!

$$\left( \ln x \right)^{(n)} = ( - 1)^{n - 1}\frac{(n - 1)!}{x^{n}}$$

$$\left( \frac{1}{x} \right)^{(n)} = \left( \ln x \right)^{(n + 1)} = ( - 1)^{n}\frac{n!}{x^{n + 1}}$$

$$\left( \frac{1}{ax + b} \right)^{(n)} = ( - 1)^{n}\frac{a^{n} \cdot n!}{(ax + b)^{n + 1}}$$

复合函数的求导法则

如果函数u = g(x)在点x可导，而y = f(u)在点u = g(x)可导，那么复合函数y = f[g(x)]在点x可导，且其导数为

$$f'(x) = f'(u) \cdot g'(x)\text{，}y_{x}' = y_{u}' \cdot u_{x}'\text{，}\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

证明略。

反函数的求导法则

设函数x = f(y)（自变量y，因变量x，法则f）在区间Iy内单调可导且f′(y) ≠ 0，则其反函数y = f−1(x)（自变量x，因变量y，法则f−1）在区间Ix = {x | x = f(y)，y ∈ Iy}内也可导，且

$$\left\lbrack f^{- 1}(x) \right\rbrack' = \frac{1}{f'(y)}\text{或}\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}}$$

其中[f−1(x)]′和$\frac{dy}{dx}$是指对y = f−1(x)求关于x的导数，即fx−1′(x)，f′(y)和$\frac{dx}{dy}$是指对x = f(y)求关于y的导数。对直接函数和反函数的求导都是对因变量关于自变量的求导。为方便理解，用另一种符号表示如下

$${f_{x}^{- 1}}'(x) = \frac{1}{f_{y}'(y)}\text{或}\frac{df^{- 1}(x)}{dx} = \frac{1}{\frac{df(y)}{dy}}$$

证明：使用复合函数求导法则。

想要得到是y = f−1(x)关于x的导数表达式fx−1′(x)，这个表达式与x = f(y)对y的导数fy′(y)有关。对y = f−1(x)两边关于y求导，即

$$y_{y}' = \left\lbrack f_{y}^{- 1}(x) \right\rbrack'\text{，微分形式为}\ \frac{dy}{dy} = \frac{df^{- 1}(x)}{dy}$$

由复合函数求导法则，得

$$1 = {f_{x}^{- 1}}'(x) \cdot x_{y}' = \frac{df^{- 1}(x)}{dx} \cdot \frac{dx}{dy}$$

故

$${f_{x}^{- 1}}'(x) = \frac{1}{x_{y}'} = \frac{1}{f_{y}'(y)}\text{，微分形式为}\frac{df^{- 1}(x)}{dx} = \frac{1}{\frac{dx}{dy}} = \frac{1}{\frac{df^{- 1}(x)}{dy}}$$

下面更改变量记号重新证明：

令y = f(x)，x = f−1(y)，要求得的是fy−1′(y)（为方便理解，可以把这里的y替换成任意字母。导数的′号在内是因为要的导数是对自变量（这里是y）求导）

对x = f−1(y)两边关于x求导，得

1 = fy−1′(y) ⋅ yx′ = fy−1(y) ⋅ fx′(x)

所以

$${f_{y}^{- 1}}'(y) = \frac{1}{f_{x}'(x)}$$

eg.求y = arctan x的导数yx′

解：令

y = f−1(x) = arctan x，x = f(y) = tan y

$$y_{x}' = {f_{x}^{- 1}}'(x) = \frac{1}{f_{y}'(y)} = \frac{1}{\left( \tan y \right)_{y}'} = \frac{1}{\sec^{2}y} = \frac{1}{1 + \tan^{2}y} = \frac{1}{1 + x^{2}}$$

$$\text{下面推到反函数的二阶导数和三阶导数，方便起见，记}y' = \frac{dy}{dx}\text{，}y^{''} = \frac{d^{2}y}{dx^{2}}\text{，有}$$

$$\frac{d^{2}x}{dy^{2}} = \frac{d}{dy}\left( \frac{dx}{dy} \right) = \frac{d\left( \left( y' \right)^{- 1} \right)}{dy} = \frac{d\left( \left( y' \right)^{- 1} \right)}{dx} \cdot \frac{dx}{dy} = - \frac{y^{''}}{\,{y'}^{2}} \cdot \frac{1}{y'} = - \frac{y^{''}}{\left( y' \right)^{3}}$$

$$\frac{d^{3}x}{dy^{3}} = \frac{d}{dy}\left( \frac{d^{2}x}{dy^{2}} \right) = \frac{d\left( - \frac{y^{''}}{\left( y' \right)^{3}} \right)}{dx} \cdot \frac{dx}{dy} = - \frac{y^{'''}\left( y' \right)^{3} - y^{''} \cdot 3\left( y' \right)^{2}y^{''}}{\left( y' \right)^{6}} \cdot \frac{1}{y'} = \frac{3\left( y^{''} \right)^{2} - y'y^{'''}}{\left( y' \right)^{5}}$$

参数方程的导数

$$y_{x}' = \frac{dy}{dx} = \frac{dy}{dt}\frac{dt}{dx} = \frac{y_{t}'}{x_{t}'}$$

同理

$$\frac{d^{2}y}{dx^{2}} = \frac{d}{dx}\left( \frac{dy}{dx} \right) = \frac{d}{dt}\left( \frac{y'(t)}{x'(t)} \right) \cdot \frac{dt}{dx} = \frac{y^{''}(t)x'(t) - y'(t)x^{''}(t)}{\,{x'}^{2}(t)} \cdot \frac{1}{x'(t)} = \frac{y^{''}(t)x'(t) - y'(t)x^{''}(t)}{\,{x'}^{3}(t)}$$

极坐标下的导数

已知r = f(θ)，求r′

由

x = rcos θ

y = rsin θ

得

x = f(θ)cos θ

y = f(θ)sin θ

$$r_{\theta}' = \frac{dy}{dx} = \frac{dy}{d\theta}\frac{d\theta}{dx} = \frac{y_{\theta}'}{x_{\theta}'}$$

常见函数的导数

见常用导数与积分表。

偏导数

微分

全微分

$$\Delta z = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy + ο(\rho)$$

$$\text{其中}ο(\rho) = \sqrt{(dx)^{2} + (dy)^{2}}$$

$$dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy$$

微分近似公式

一元函数

Δy ≈ dy = f′(x)dx

f(x + Δx) ≈ f(x) + f′(x)Δx

多元函数

Δz ≈ dz = fx(x，y)Δx + fy(x，y)Δy

f(x + Δx，y + Δy) ≈ f(x，y) + fx(x，y)Δx + fy(x，y)Δy

多元复合函数的求导法则

1.u = φ(t)，v = ψ(t)，z = f(u，v)

$$\frac{dz}{dx} = \frac{\partial z}{\partial u}\frac{du}{dt} + \frac{\partial z}{\partial v}\frac{dv}{dt}$$

2.u = φ(x，y)，v = ψ(x，y)，z = f(u，v)

$$\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial x}$$

$$\frac{\partial z}{\partial y} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial y} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial y}$$

全微分形式不变性

设函数z = f(u，v)具有连续偏导数，则有全微分

$$dz = \frac{\partial z}{\partial u}du + \frac{\partial z}{\partial v}dv$$

通过此能得到全导数的概念

D(f) = fx + fy + ⋯

其满足所有求导法则和导数公式

拉格朗日乘数法求最值

（出现形如x ∈ [1，2]之类的条件时，不能判断得出的是极大值还是极小值）

已知目标函数f(x，y)，约束条件φ(x，y) = 0，求f(x，y)的极值

令F(x，y，λ) = f(x，y) + λφ(x，y)，解方程组：

$$\left\{ \begin{array}{r}
F_{x}'(x\text{，}y\text{，}\lambda) = f_{x}'(x\text{，}y) + \lambda\varphi_{x}'(x\text{，}y) = 0 \\
F_{y}'(x\text{，}y\text{，}\lambda) = f_{y}'(x\text{，}y) + \lambda\varphi_{y}'(x\text{，}y) = 0 \\
F_{\lambda}'(x\text{，}y\text{，}\lambda) = \lambda\varphi(x\text{，}y) = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

得到x，y的一组或几组解，验证后代入f(x，y)即得f(x，y)的极值

$$eg.\text{已知}x\text{，}y\text{，}z \in \mathbb{R}_{+}\text{，且}x + y + z = 1\text{，求}\frac{1}{x} + \frac{4}{y} + \frac{9}{z}\text{的最小值}$$

$$\text{解：令}F(x\text{，}y\text{，}z\text{，}\lambda) = \frac{1}{x} + \frac{4}{y} + \frac{9}{z} + \lambda(x + y + z - 1)\text{，求偏导数，可得}$$

$$\left\{ \begin{array}{r}
 - \frac{1}{x^{2}} + 1 = 0\ \ \ \ \ \ \ \ \  \\
 - \frac{4}{y^{2}} + 1 = 0\ \ \ \ \ \ \ \ \  \\
 - \frac{9}{z^{2}} + 1 = 0\ \ \ \ \ \ \ \ \  \\
x + y + z - 1 = 0
\end{array} \right.\ \text{解之，得}x = \frac{1}{6}\text{，}y = \frac{1}{3}\text{，}z = \frac{1}{2}\text{，即得最小值为}36\text{。}$$

该结论可推广到有多个约束条件的情形。

费曼求导法（对数求导法）

对于多个多项式因式的积的导数，其导数为

因式×[]

方括号内是该式的每个因式的处理后的结果的和，该处理方法为：

因式右上角的指数 × (因式)−1 × (因式)′

$$eg.f(t) = \frac{6\left( 1 + 2t^{2} \right)\left( t^{3} - t \right)^{2}}{\sqrt{t + 5t^{2}}(4t)^{\frac{3}{2}}} + \frac{\sqrt{1 + 2t}}{t + \sqrt{1 + t^{2}}}$$

$$f'(t) = \frac{6\left( 1 + 2t^{2} \right)\left( t^{3} - t \right)^{2}}{\sqrt{t + 5t^{2}}(4t)^{\frac{3}{2}}} \cdot \left\lbrack 1 \cdot \frac{4t}{1 + 2t^{2}} + 2 \cdot \frac{3t^{2} - 1}{t^{3} - t} - \frac{1}{2} \cdot \frac{1 + 10t}{t + 5t^{2}} - \frac{3}{2} \cdot \frac{4}{4t} \right\rbrack$$

$$+ \frac{\sqrt{1 + 2t}}{t + \sqrt{1 + t^{2}}} \cdot \left\{ \frac{1}{2}\frac{2}{1 + 2t} - 1\frac{1}{t + \sqrt{1 + t^{2}}}\left\lbrack 1 + \frac{1}{2}\frac{2t}{\sqrt{1 + t^{2}}} \right\rbrack \right\}$$

其中

$$1 \cdot \frac{4t}{1 + 2t^{2}} = \left( 1 + 2t^{2} \right)\text{的指数}(\text{即为}1) \times \frac{1}{1 + 2t^{2}} \times \left( 1 + 2t^{2} \right)'$$

$$2 \cdot \frac{3t^{2} - 1}{t^{3} - t} = \left( t^{3} - t \right)^{2}\text{的指数}(\text{即为}2) \times \frac{1}{t^{3} - t} \times \left( t^{3} - t \right)'$$

$$- \frac{1}{2} \cdot \frac{1 + 10t}{t + 5t^{2}} = \frac{1}{\sqrt{t + 5t^{2}}}\text{的指数}\left( \text{即为}\frac{1}{2} \right) \times \frac{1}{t + 5t^{2}} \times \left( t + 5t^{2} \right)'$$

$$- \frac{3}{2} \cdot \frac{4}{4t} = (4t)^{\frac{3}{2}}\text{的指数}\left( \text{即为} - \frac{3}{2} \right) \times \frac{1}{4t} \times (4t)'$$

$$\frac{1}{2}\frac{2}{1 + 2t} = \sqrt{1 + 2t}\text{的指数}\left( \text{即为}\frac{1}{2} \right) \times \frac{1}{1 + 2t} \times (1 + 2t)'$$

$$- 1\frac{1}{t + \sqrt{1 + t^{2}}}\left\lbrack 1 + \frac{1}{2}\frac{2t}{\sqrt{1 + t^{2}}} \right\rbrack = t + \sqrt{1 + t^{2}}\text{的指数}(\text{即为} - 1) \times \frac{1}{t + \sqrt{1 + t^{2}}} \times \left( t + \sqrt{1 + t^{2}} \right)'$$
