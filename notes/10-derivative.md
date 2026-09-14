---
title: 导数与微分
description: 偏导数、复合与反函数求导、中值定理、曲率、拉格朗日乘数法。
---

# 导数与微分

[[toc]]

### 多元函数的偏导数

对于二元函数$z = f(x\text{，}y)$，定义偏导数

$$f_{x}'\left( x_{0}\text{，}y_{0} \right) = \lim_{\Delta x \rightarrow 0}\frac{f\left( x_{0} + \Delta x\text{，}y_{0} \right) - f\left( x_{0}\text{，}y_{0} \right)}{\Delta x}$$

$$f_{y}'\left( x_{0}\text{，}y_{0} \right) = \lim_{\Delta y \rightarrow 0}\frac{f\left( x_{0}\text{，}y_{0} + \Delta y \right) - f\left( x_{0}\text{，}y_{0} \right)}{\Delta y}$$

$$\frac{\partial z}{\partial x} = \frac{\partial f}{\partial x} = z_{x} = z_{x}' = f_{x}(x\text{，}y) = f_{x}'(x\text{，}y) = \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x\text{，}y) - f(x\text{，}y)}{\Delta x}$$

$$\frac{\partial z}{\partial y} = \frac{\partial f}{\partial y} = z_{y} = z_{y}' = f_{y}(x\text{，}y) = f_{y}'(x\text{，}y) = \lim_{\Delta y \rightarrow 0}\frac{f(x\text{，}y + \Delta y) - f(x\text{，}y)}{\Delta y}$$

$$f_{x}'\left( x_{0}\text{，}y \right) = \frac{\partial f}{\partial x}\left| \begin{array}{r}
 \\
\underset{x = x_{0}}{}
\end{array} \right.\ $$

$$f_{x}'\left( x\text{，}y_{0} \right) = \frac{df\left( x\text{，}y_{0} \right)}{dx} \Rightarrow f_{x}'\left( x_{0}\text{，}y_{0} \right) = \frac{df\left( x\text{，}y_{0} \right)}{dx}\left| \begin{array}{r}
 \\
\underset{x = x_{0}}{}
\end{array} \right.\ $$

$$f_{y}'\left( x_{0}\text{，}y \right) = \frac{df\left( x_{0}\text{，}y \right)}{dy} \Rightarrow f_{y}'\left( x_{0}\text{，}y_{0} \right) = \frac{df\left( x_{0}\text{，}y \right)}{dy}\left| \begin{array}{r}
 \\
\underset{y = y_{0}}{}
\end{array} \right.\ $$

$$f_{y}'\left( x\text{，}y_{0} \right) = \frac{\partial f}{\partial y}\left| \begin{array}{r}
 \\
\underset{y = y_{0}}{}
\end{array} \right.\ $$

$$f_{xx}^{''}\left( x_{0}\text{，}y_{0} \right) = \frac{df_{x}'\left( x\text{，}y_{0} \right)}{dx}\left| \begin{array}{r}
 \\
\underset{x = x_{0}}{}
\end{array} \right.\  = \frac{d^{2}f\left( x\text{，}y_{0} \right)}{dx}\left| \begin{array}{r}
 \\
\underset{x = x_{0}}{}
\end{array} \right.\ $$

$$f_{xy}^{''}\left( x_{0}\text{，}y_{0} \right) = \frac{df_{x}'\left( x_{0}\text{，}y \right)}{dy}\left| \begin{array}{r}
 \\
\underset{y = y_{0}}{}
\end{array} \right.\  = \frac{d}{dy}\left( \frac{\partial f}{\partial x}\left| \begin{array}{r}
 \\
\underset{x = x_{0}}{}
\end{array} \right.\  \right)\left| \begin{array}{r}
 \\
\underset{y = y_{0}}{}
\end{array} \right.\ $$

$$f_{yx}^{''}\left( x_{0}\text{，}y_{0} \right) = \frac{df_{y}'\left( x\text{，}y_{0} \right)}{dx}\left| \begin{array}{r}
 \\
\underset{x = x_{0}}{}
\end{array} \right.\  = \frac{d}{dx}\left( \frac{\partial f}{\partial y}\left| \begin{array}{r}
 \\
\underset{y = y_{0}}{}
\end{array} \right.\  \right)\left| \begin{array}{r}
 \\
\underset{x = x_{0}}{}
\end{array} \right.\ $$

$$f_{yy}^{''}\left( x_{0}\text{，}y_{0} \right) = \frac{df_{y}'\left( x_{0}\text{，}y \right)}{dy}\left| \begin{array}{r}
 \\
\underset{y = y_{0}}{}
\end{array} \right.\  = \frac{d^{2}f\left( x_{0}\text{，}y \right)}{dy}\left| \begin{array}{r}
 \\
\underset{y = y_{0}}{}
\end{array} \right.\ $$

$$f_{xx}^{''}\left( x_{0}\text{，}y_{0} \right) = \lim_{\Delta x \rightarrow 0}\frac{f_{x}'\left( x_{0} + \Delta x\text{，}y_{0} \right) - f_{x}'\left( x_{0}\text{，}y_{0} \right)}{\Delta x} = \lim_{\Delta x \rightarrow 0}\frac{\frac{df\left( x\text{，}y_{0} \right)}{dx}\left| \begin{array}{r}
\underset{x = x_{0} + \Delta x}{\begin{array}{r}
 \\

\end{array}}
\end{array} \right.\  - f_{x}'\left( x_{0}\text{，}y_{0} \right)}{\Delta x}$$

$$f_{xy}^{''}\left( x_{0}\text{，}y_{0} \right) = \lim_{\Delta y \rightarrow 0}\frac{f_{x}'\left( x_{0}\text{，}y_{0} + \Delta y \right) - f_{x}'\left( x_{0}\text{，}y_{0} \right)}{\Delta y} = \lim_{\Delta x \rightarrow 0}\frac{\frac{\partial f}{\partial x}\left| \begin{array}{r}
\underset{\begin{array}{r}
x = x_{0}\ \ \ \ \ \ \ \ \  \\
y = y_{0} + \Delta y
\end{array}}{\begin{array}{r}

\end{array}}
\end{array} \right.\  - f_{x}'\left( x_{0}\text{，}y_{0} \right)}{\Delta x}$$

$$f_{yx}^{''}\left( x_{0}\text{，}y_{0} \right) = \lim_{\Delta x \rightarrow 0}\frac{f_{y}'\left( x_{0} + \Delta x\text{，}y_{0} \right) - f_{y}'\left( x_{0}\text{，}y_{0} \right)}{\Delta x} = \lim_{\Delta x \rightarrow 0}\frac{\frac{\partial f}{\partial y}\left| \begin{array}{r}
\underset{\begin{array}{r}
x = x_{0} + \Delta x \\
y = y_{0}\ \ \ \ \ \ \ \ \ 
\end{array}}{\begin{array}{r}

\end{array}}
\end{array} \right.\  - f_{y}'\left( x_{0}\text{，}y_{0} \right)}{\Delta x}$$

$$f_{yy}^{''}\left( x_{0}\text{，}y_{0} \right) = \lim_{\Delta y \rightarrow 0}\frac{f_{y}'\left( x_{0}\text{，}y_{0} + \Delta y \right) - f_{y}'\left( x_{0}\text{，}y_{0} \right)}{\Delta y} = \lim_{\Delta x \rightarrow 0}\frac{\frac{df\left( x_{0}\text{，}y \right)}{dy}\left| \begin{array}{r}
\underset{y = y_{0} + \Delta y}{\begin{array}{r}
 \\

\end{array}}
\end{array} \right.\  - f_{x}'\left( x_{0}\text{，}y_{0} \right)}{\Delta y}$$

### 向量值函数的导数

对向量值函数$\mathbf{y = f}\left( \mathbf{x} \right)$，即

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

为向量值函数$\mathbf{f}$在$\mathbf{x}^{0}$点的导数或Jacobi（雅可比）矩阵

特别地，对于$m = 1$的情况，即一元向量值函数，有

$$\mathbf{f}'\left( \mathbf{x}^{0} \right) = \begin{pmatrix}
\frac{\partial f_{1}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) \\
\frac{\partial f_{2}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) \\
 \vdots \\
\frac{\partial f_{m}}{\partial x_{1}}\left( \mathbf{x}^{0} \right)
\end{pmatrix} = \frac{\partial f_{1}}{\partial x_{1}}\mathbf{e}_{1} + \frac{\partial f_{2}}{\partial x_{1}}\mathbf{e}_{2} + \cdots + \frac{\partial f_{m}}{\partial x_{1}}\mathbf{e}_{m}$$

高阶导数的三则运算法则：

$$\left\lbrack f(x) \pm g(x) \right\rbrack^{(n)} = \left\lbrack f(x) \right\rbrack^{(n)} \pm \left\lbrack g(x) \right\rbrack^{(n)} = f^{(n)}(x) \pm g^{(n)}(x)$$

$$\left\lbrack Cf(x) \right\rbrack^{(n)} = C \cdot f^{(n)}(x)$$

$$Leibniz\text{（莱布尼兹）公式：}\left\lbrack f(x) \cdot g(x) \right\rbrack^{(n)} = \sum_{k = 0}^{n}{C_{n}^{k}f^{(n - k)}(x)g^{(k)}(x)}$$

常见函数的高阶导数：

$$\left( a^{x} \right)^{(n)} = \left( \ln a \right)^{n}a^{x}$$

$$\left( \sin x \right)^{(n)} = \sin\left( x + \frac{n\pi}{2} \right)$$

$$\left( \cos x \right)^{(n)} = \cos\left( x + \frac{n\pi}{2} \right)$$

$$\left( \sin{kx} \right)^{(n)} = k^{n}\sin\left( kx + \frac{n\pi}{2} \right)$$

$$\left( \cos{kx} \right)^{(n)} = k^{n}\cos\left( kx + \frac{n\pi}{2} \right)$$

$$\left( x^{m} \right)^{(n)} = \left\{ \begin{array}{r}
m(m - 1)\cdots(m - n + 1)x^{m - n} = A_{m}^{n}x^{m - n}\ \ \ \ n \leq m \\
0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ n > m
\end{array} \right.\ $$

$$\left( x^{n} \right)^{(n)} = n!$$

$$\left( \ln x \right)^{(n)} = ( - 1)^{n - 1}\frac{(n - 1)!}{x^{n}}$$

$$\left( \frac{1}{x} \right)^{(n)} = \left( \ln x \right)^{(n + 1)} = ( - 1)^{n}\frac{n!}{x^{n + 1}}$$

$$\left( \frac{1}{ax + b} \right)^{(n)} = ( - 1)^{n}\frac{a^{n} \cdot n!}{(ax + b)^{n + 1}}$$

### 复合函数的求导法则

如果函数$u = g(x)$在点$x$可导，而$y = f(u)$在点$u = g(x)$可导，那么复合函数$y = f\left\lbrack g(x) \right\rbrack$在点$x$可导，且其导数为

$$f'(x) = f'(u) \cdot g'(x)\text{，}y_{x}' = y_{u}' \cdot u_{x}'\text{，}\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

证明略。

### 反函数的求导法则

设函数$x = f(y)$（自变量$y$，因变量$x$，法则$f$）在区间$I_{y}$内单调可导且$f'(y) \neq 0$，则其反函数$y = f^{- 1}(x)$（自变量$x$，因变量$y$，法则$f^{- 1}$）在区间$I_{x} = \left\{ x\ |\ x = f(y)\text{，}y \in I_{y} \right\}$内也可导，且

$$\left\lbrack f^{- 1}(x) \right\rbrack' = \frac{1}{f'(y)}\text{或}\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}}$$

其中$\left\lbrack f^{- 1}(x) \right\rbrack'$和$\frac{dy}{dx}$是指对$y = f^{- 1}(x)$求关于$x$的导数，即${f_{x}^{- 1}}'(x)$，$f'(y)$和$\frac{dx}{dy}$是指对$x = f(y)$求关于$y$的导数。对直接函数和反函数的求导都是对因变量关于自变量的求导。为方便理解，用另一种符号表示如下

$${f_{x}^{- 1}}'(x) = \frac{1}{f_{y}'(y)}\text{或}\frac{df^{- 1}(x)}{dx} = \frac{1}{\frac{df(y)}{dy}}$$

$eg.$求$y = \arctan x$的导数$y_{x}'$

解：令

$$y = f^{- 1}(x) = \arctan x\text{，}x = f(y) = \tan y$$

$$y_{x}' = {f_{x}^{- 1}}'(x) = \frac{1}{f_{y}'(y)} = \frac{1}{\left( \tan y \right)_{y}'} = \frac{1}{\sec^{2}y} = \frac{1}{1 + \tan^{2}y} = \frac{1}{1 + x^{2}}$$

$$\text{下面推到反函数的二阶导数和三阶导数，方便起见，记}y' = \frac{dy}{dx}\text{，}y^{''} = \frac{d^{2}y}{dx^{2}}\text{，有}$$

>

$$\frac{d^{2}x}{dy^{2}} = \frac{d}{dy}\left( \frac{dx}{dy} \right) = \frac{d\left( \left( y' \right)^{- 1} \right)}{dy} = \frac{d\left( \left( y' \right)^{- 1} \right)}{dx} \cdot \frac{dx}{dy} = - \frac{y^{''}}{\,{y'}^{2}\,} \cdot \frac{1}{y'} = - \frac{y^{''}}{\left( y' \right)^{3}}$$

>
>

$$\frac{d^{3}x}{dy^{3}} = \frac{d}{dy}\left( \frac{d^{2}x}{dy^{2}} \right) = \frac{d\left( - \frac{y^{''}}{\left( y' \right)^{3}} \right)}{dx} \cdot \frac{dx}{dy} = - \frac{y^{'''}\left( y' \right)^{3} - y^{''} \cdot 3\left( y' \right)^{2}y^{''}}{\left( y' \right)^{6}} \cdot \frac{1}{y'} = \frac{3\left( y^{''} \right)^{2} - y'y^{'''}}{\left( y' \right)^{5}}$$

### 参数方程的导数

$$y_{x}' = \frac{dy}{dx} = \frac{dy}{dt}\frac{dt}{dx} = \frac{y_{t}'}{x_{t}'}$$

同理

$$\frac{d^{2}y}{dx^{2}} = \frac{d}{dx}\left( \frac{dy}{dx} \right) = \frac{d}{dt}\left( \frac{y'(t)}{x'(t)} \right) \cdot \frac{dt}{dx} = \frac{y^{''}(t)x'(t) - y'(t)x^{''}(t)}{\,{x'}^{2}(t)\,} \cdot \frac{1}{x'(t)} = \frac{y^{''}(t)x'(t) - y'(t)x^{''}(t)}{\,{x'}^{3}(t)\,}$$

### 极坐标下的导数

已知$r = f(\theta)\text{，求}r'$

由

$$x = r\cos\theta$$

$$y = r\sin\theta$$

得

$$x = f(\theta)\cos\theta$$

$$y = f(\theta)\sin\theta$$

$$r_{\theta}' = \frac{dy}{dx} = \frac{dy}{d\theta}\frac{d\theta}{dx} = \frac{y_{\theta}'}{x_{\theta}'}$$

### 常见函数的导数

见常用导数与积分表。

### 偏导数

### 微分

### 全微分

$$\Delta z = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy + ο(\rho)$$

$$\text{其中}ο(\rho) = \sqrt{(dx)^{2} + (dy)^{2}}$$

$$dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy$$

### 微分近似公式

一元函数

$$\Delta y \approx dy = f'(x)dx$$

$$f(x + \Delta x) \approx f(x) + f'(x)\Delta x$$

多元函数

$$\Delta z \approx dz = f_{x}(x\text{，}y)\Delta x + f_{y}(x\text{，}y)\Delta y$$

$$f(x + \Delta x\text{，}y + \Delta y) \approx f(x\text{，}y) + f_{x}(x\text{，}y)\Delta x + f_{y}(x\text{，}y)\Delta y$$

### 拉格朗日乘数法求最值

（出现形如$x \in \lbrack 1\text{，}2\rbrack$之类的条件时，不能判断得出的是极大值还是极小值）

已知目标函数$f(x\text{，}y)$，约束条件$\varphi(x\text{，}y) = 0$，求$f(x\text{，}y)$的极值

令$F(x\text{，}y\text{，}\lambda) = f(x\text{，}y) + \lambda\varphi(x\text{，}y)$，解方程组：

$$\left\{ \begin{array}{r}
F_{x}'(x\text{，}y\text{，}\lambda) = f_{x}'(x\text{，}y) + \lambda\varphi_{x}'(x\text{，}y) = 0 \\
F_{y}'(x\text{，}y\text{，}\lambda) = f_{y}'(x\text{，}y) + \lambda\varphi_{y}'(x\text{，}y) = 0 \\
F_{\lambda}'(x\text{，}y\text{，}\lambda) = \lambda\varphi(x\text{，}y) = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

得到x，y的一组或几组解，验证后代入$f(x\text{，}y)$即得$f(x\text{，}y)$的极值

### 微分中值定律

### Fermat（费马）引理

设$x_{0}$是$f(x)$的一个极值点，且$f(x)$在$x_{0}$处导数存在，则

$$f'\left( x_{0} \right) = 0$$

### Rolle（罗尔）定理

如果函数$f(x)$满足

（1）在闭区间$\lbrack a\text{，}b\rbrack$上连续；

（2）在开区间$(a\text{，}b)$上可导；

（3）在区间端点处的函数值相等，即$f(a) = f(b)$，

那么在$(a\text{，}b)$内至少有一点$\xi\ (a < \xi < b)$，使得$f'(\xi) = 0$。

### 一类中值题的通解

对于$f(x)$，求证$\exists\xi$，满足

$$f'(\xi) + p(\xi)f(\xi) = q(\xi)$$

可设辅助函数$F(x)$

$$f(x) = e^{- \int_{}^{}{p(x)dx}}\left( \int_{}^{}{q(x)e^{\int_{}^{}{p(x)dx}}dx} + F(x) \right)$$

可以看出，这是一阶线性微分方程的通解，这种做法于"原函数于导函数混合还原"的微分方程解法类似。

### 拉格朗日中值定理

如果函数$f(x)$满足

（1）在闭区间$\lbrack a\text{，}b\rbrack$上连续；

（2）在开区间$(a\text{，}b)$上可导；

那么在$(a\text{，}b)$内至少有一点$\xi\ (a < \xi < b)$，使等式

$$\frac{f(b) - f(a)}{b - a} = f'(\xi)$$

成立。

把定理改写成$f(b) - f(a) = f'(\xi)(b - a)$，记$\Delta x = b - a\text{，}\Delta y = f(b) - f(a)$，把$a$替换为自变量$x$，因为$(a < \xi < b)$，可以令$\xi = x + \theta\Delta x\ \ \theta \in (0\text{，}1)$，得到有限增量公式：

$$\Delta y = f'(x + \theta\Delta x) \cdot \Delta x\ \ (0 < \theta < 1)$$

相比$\Delta y = f'(x)dx + o(\Delta x)$，有限增量公式更加精确地描述了$\Delta y$。

### 柯西中值定理

如果函数$f(x)$及$F(x)$满足

（1）在闭区间$\lbrack a\text{，}b\rbrack$上连续；

（2）在开区间$(a\text{，}b)$上可导；

（3）对任一$x \in (a\text{，}b)$，$F'(x) \neq 0$，

那么在$(a\text{，}b)$内至少有一点$\xi\ (a < \xi < b)$，使等式

$$\frac{f(b) - f(a)}{F(b) - F(a)} = \frac{f'(\xi)}{F'(\xi)}$$

成立

证明：作辅助函数

$$g(x) = f(x) - \frac{f(b) - f(a)}{F(b) - F(a)}F(x)$$

$$g(a) = g(b) = \frac{F(b)f(a) - F(a)f(b)}{F(b) - F(a)}$$

$g(x)$在$\lbrack a\text{，}b\rbrack$上连续，在$(a\text{，}b)$上可导，由罗尔定理，至少有一点$\xi\ (a < \xi < b)$，使

$$g'(\xi) = f'(\xi) - \frac{f(b) - f(a)}{F(b) - F(a)}F'(\xi) = 0$$

整理即得。

柯西中值定理可以看成

$$\frac{\frac{f(b) - f(a)}{b - a}}{\frac{F(b) - F(a)}{b - a}} = \frac{f'(\xi)}{F'(\xi)}$$

如果函数$f(x)$及$g(x)$在闭区间$\lbrack a\text{，}b\rbrack$上连续，在开区间$(a\text{，}b)$上可导，则存在$\xi \in (a\text{，}b)$，使得

$$\left| \begin{matrix}
f(a) & f(b) \\
g(a) & g(b)
\end{matrix} \right| = (b - a)\left| \begin{matrix}
f(a) & f'(\xi) \\
g(a) & g'(\xi)
\end{matrix} \right|$$

### 曲率

### 弧微分

函数$y = f(x)$的有向弧段的微元为

$$ds = \sqrt{1 + {y'}^{2}}dx$$

证明：由勾股定理

$$ds = \sqrt{(dx)^{2} + (dy)^{2}} = \sqrt{(dx)^{2} + \left( y'dx \right)^{2}} = \sqrt{1 + {y'}^{2}}dx$$

### 曲率

定义曲率

$$K = \left| \frac{d\alpha}{ds} \right|$$

即弧长对转角$\alpha$的变化率，有

$$K = \frac{\left| y^{''} \right|}{\left( 1 + {y'}^{2} \right)^{3/2}}$$

$$\text{证明：由}\tan\alpha = y'\text{，得}\alpha = \arctan y'$$

$\text{所以}$

$$d\alpha = \left( \arctan y' \right)'dx = \frac{y^{''}}{1 + \left( y' \right)^{2}}dx$$

又因为

$$ds = \sqrt{1 + {y'}^{2}}dx$$

所以

$$K = \left| \frac{d\alpha}{ds} \right| = \left| \frac{\frac{y^{''}}{1 + \left( y' \right)^{2}}dx}{\sqrt{1 + {y'}^{2}}dx} \right| = \frac{\left| y^{''} \right|}{\left( 1 + {y'}^{2} \right)^{3/2}}$$

### 曲率半径

曲线在某点处的曲率$K\ (K \neq 0)$与曲率半径$\rho$满足

$$\rho = \frac{1}{K}\text{，}K = \frac{1}{\rho}$$

### 曲率中心

曲率中心（即曲率圆的圆心）$D(\alpha \text{，}\beta)$的坐标为

$$\left\{ \begin{array}{r}
\alpha = x - \frac{y'(1 + y^{'2})}{y^{''}} \\
\beta = y + \frac{1 + y^{'2}}{y^{''}}\ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

点沿曲线C移动时，相应的曲率中心D的轨迹曲线G称为曲线C的渐屈线，而曲线C称为曲线G的渐伸线，设$C:y = f(x)$，则其渐屈线的参数方程为

$$\left\{ \begin{array}{r}
\alpha = x - \frac{y'(1 + y^{'2})}{y^{''}} \\
\beta = y + \frac{1 + y^{'2}}{y^{''}}\ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

其中$\alpha \text{，}\beta$分别为渐屈线上某点的横、纵坐标。
