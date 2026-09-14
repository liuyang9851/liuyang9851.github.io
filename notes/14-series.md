---
title: 级数
description: 正项级数审敛法、交错级数、幂级数、傅里叶级数。
---

# 级数

[[toc]]

### 性质：收敛+收敛=收敛

### 收敛+发散=发散

### 发散+发散=不定

任意加括号（不能任意拆项）

### 任意去添有限项

必要条件：$\lim_{n \rightarrow \infty}u_{n} = 0$

证明：设级数$\sum_{n = 1}^{\infty}u_{n}$的部分和为$s_{n}$，且$s_{n} \rightarrow s(n \rightarrow \infty)$，则

$$\lim_{n \rightarrow \infty}u_{n} = \lim_{n \rightarrow \infty}\left( s_{n} - s_{n - 1} \right) = \lim_{n \rightarrow \infty}s_{n} - \lim_{n \rightarrow \infty}s_{n - 1} = s - s = 0$$

### 正项级数

设$\sum_{n = 1}^{\infty}u_{n}$和$\sum_{n = 1}^{\infty}v_{n}$都是正项级数

### 比较审敛法

若$u_{n} \leq v_{n}$，则

$$\left\{ \begin{array}{r}
\sum_{n = 1}^{\infty}v_{n}\text{收敛} \Rightarrow \sum_{n = 1}^{\infty}u_{n}\text{收敛} \\
\sum_{n = 1}^{\infty}u_{n}\text{发散} \Rightarrow \sum_{n = 1}^{\infty}v_{n}\text{发散}
\end{array} \right.\ $$

### 推论

### 比较审敛法的极限形式

$$\lim_{n \rightarrow \infty}\frac{u_{n}}{v_{n}} = l \in \left\{ \begin{array}{r}
 + \infty \text{，}\sum_{n = 1}^{\infty}v_{n}\text{发散} \Rightarrow \sum_{n = 1}^{\infty}u_{n}\text{发散} \\
(0\text{，}\infty)\text{，敛散性相同}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
0\text{，}\sum_{n = 1}^{\infty}v_{n}\text{收敛} \Rightarrow \sum_{n = 1}^{\infty}u_{n}\text{收敛}\ \ \ \ 
\end{array} \right.\ $$

比值审敛法（d' Alembert（达朗贝尔）判别法）

$$\lim_{n \rightarrow \infty}\frac{u_{n + 1}}{u_{n}} = \rho \in \left\{ \begin{array}{r}
 < 1\text{，收敛}\ \ \ \ \ \ \ \ \ \ \ \  \\
1\text{，不定}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
(1\text{，} + \infty\rbrack \text{，发散}
\end{array} \right.\ $$

根值审敛法（柯西判别法）

$$\lim_{n \rightarrow \infty}\sqrt[n]{u_{n}} = \rho \in \left\{ \begin{array}{r}
 < 1\text{，收敛}\ \ \ \ \ \ \ \ \ \ \ \  \\
1\text{，不定}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
(1\text{，} + \infty\rbrack \text{，发散}
\end{array} \right.\ $$

### 极限审敛法

$$\left\{ \begin{array}{r}
\lim_{n \rightarrow \infty}{nu_{n}} \in (0\text{，} + \infty\rbrack \text{，收敛}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\lim_{n \rightarrow \infty}{n^{p}u_{n}} \in \lbrack 0\text{，} + \infty)\text{，发散}\ \ (p > 1)
\end{array} \right.\ $$

### 交错级数

$$\sum_{n = 1}^{\infty}{( - 1)^{n - 1}u_{n}}\ \ \left( u_{n} > 0 \right)$$

### 莱布尼茨定理

$$\left. \ \begin{array}{r}
u_{n} \geq u_{n + 1} \\
\lim_{n \rightarrow \infty}u_{n} = 0
\end{array} \right\} \Rightarrow \text{收敛}$$

### 绝对收敛与条件收敛

任意级数$\sum_{n = 1}^{\infty}u_{n}$，有

$$\left\{ \begin{array}{r}
\sum_{n = 1}^{\infty}\left| u_{n} \right|\text{收敛} \Rightarrow \sum_{n = 1}^{\infty}u_{n}\text{收敛} \\
\sum_{n = 1}^{\infty}u_{n}\text{发散} \Rightarrow \sum_{n = 1}^{\infty}\left| u_{n} \right|\text{发散}
\end{array} \right.\ $$

### 绝对收敛级数具有可交换性

### 绝对收敛级数的柯西乘积绝对收敛，且和为原级数的积

### 幂级数

### 收敛半径

$$R = \left( \lim_{n \rightarrow \infty}\left| \frac{a_{n + 1}}{a_{n}} \right| \right)^{- 1} = \frac{1}{\rho}$$

不能直接应用上述公式的则使用比值审敛法等求收敛半径。

幂级数加减乘取最小收敛半径，幂级数求导积分收敛半径不变。

### 三类常见幂级数的和函数

>

$$\sum_{n = 1}^{\infty}x^{n} = \frac{x}{1 - x}\ \ ( - 1\text{，}1)$$

>
>

$$\sum_{n = 1}^{\infty}\frac{x^{n}}{n} = - \ln(1 - x)\ \ \lbrack - 1\text{，}1)$$

>
>

$$\sum_{n = 1}^{\infty}{nx^{n - 1}} = \frac{1}{(1 - x)^{2}}\ \ ( - 1\text{，}1)$$

### 函数展开成幂级数

>

$$e^{x} = \sum_{n = 0}^{\infty}{\frac{1}{n!}x^{n}}\ \ ( - \infty < x < + \infty)$$

>
>

$$\frac{1}{1 - x} = \sum_{n = 0}^{\infty}x^{n}\ \ ( - 1 < x < 1)$$

>
>

$$\sin x = \sum_{n = 0}^{\infty}\frac{( - 1)^{n}}{(2n + 1)!}x^{2n + 1} = \sum_{n = 1}^{\infty}\frac{( - 1)^{n - 1}}{(2n - 1)!}x^{2n - 1}\ \ ( - \infty < x < + \infty)$$

>
>

$$xe^{2x} = x\sum_{n = 0}^{\infty}{\frac{1}{n!}(2x)^{n}} = \sum_{n = 0}^{\infty}{\frac{x^{n}}{n!}x^{n + 1}}\ \ ( - \infty < x < + \infty)$$

>
>

$$\frac{1}{x^{2} + 3x + 2} = \frac{1}{(x + 1)(x + 2)} = \frac{1}{1 + x} - \frac{1}{2 + x} = \frac{1}{1 - ( - x)} - \frac{1}{2} \cdot \frac{1}{1 + \frac{x}{2}} = \sum_{n = 0}^{\infty}( - x)^{n} - \frac{1}{2}\sum_{n = 0}^{\infty}\left( - \frac{x}{2} \right)^{n} = \sum_{n = 0}^{\infty}{( - 1)^{n}\left\lbrack 1 - \frac{1}{2^{n + 1}} \right\rbrack x^{n}}\ \ x \in ( - 1\text{，}1)$$

>
>

$$f(x) = \arctan x$$

>
>

$$f'(x) = \frac{1}{1 + x^{2}} = \frac{1}{1 - \left( - x^{2} \right)} = \sum_{n = 0}^{\infty}{( - 1)^{n}x^{2n}}\ \ \left( \left| - x^{n} \right| < 1 \Rightarrow x \in ( - 1\text{，}1) \right)$$

>
> 两边从$0$到$x$逐项积分
>
>

$$\int_{0}^{x}{\frac{1}{1 + x^{2}}dx} = \int_{0}^{x}{\left\lbrack \sum_{n = 0}^{\infty}{( - 1)^{n}x^{2n}} \right\rbrack dx} \Rightarrow \arctan x - \arctan 0 = \sum_{n = 0}^{\infty}{\int_{0}^{x}{( - 1)^{n}x^{2n}dx}} \Rightarrow \arctan x = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{2n + 1}x^{2n + 1}}\ \ x \in ( - 1\text{，}1)$$

$$\text{当}x = \pm 1\text{时，级数收敛，}\arctan x = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{2n + 1}x^{2n + 1}}\ \ x \in \lbrack - 1\text{，}1\rbrack$$

### 傅里叶级数

$$f(x) = \frac{a_{0}}{2} + \sum_{n = 1}^{\infty}\left( a_{n}\cos\frac{n\pi x}{l} + b_{n}\sin\frac{n\pi x}{l} \right)\ \ (x \in C)$$

其中

$${a_{n} = \frac{1}{l}\int_{- l}^{l}{f(x)\cos\frac{n\pi x}{l}dx}\ \ (n = 0\text{，}1\text{，}2\text{，}\cdots)
}{b_{n} = \frac{1}{l}\int_{- l}^{l}{f(x)\sin{\frac{n\pi x}{l}dx}}\ \ (n = 0\text{，}1\text{，}2\text{，}\cdots)
}{C = \left\{ x\left| f(x) = \frac{1}{2}\left\lbrack f\left( x^{-} \right) + f\left( x^{+} \right) \right\rbrack \right.\  \right\}}$$

$eg.$若$f(x)$的周期为$2\pi$，在$\lbrack - \pi \text{，}\pi)$上的表达式为$f(x) = |x|$，则其傅里叶级数为

$$f(x) = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k = 1}^{\infty}{\frac{1}{(2k - 1)^{2}}\cos{(2k - 1)x}}\ \ ( - \infty < x < + \infty)$$

利用其能得到

$$|x| = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k = 1}^{\infty}{\frac{1}{(2k - 1)^{2}}\cos{(2k - 1)x}}\ \ ( - \pi \leq x \leq \pi)$$

令$x = 0$，得

$$\sum_{k = 1}^{\infty}\frac{1}{(2k - 1)^{2}} = \frac{\pi^{2}}{8}$$

设

>

$$\sigma = 1 + \frac{1}{2^{2}} + \frac{1}{3^{3}} + \frac{1}{4^{2}} + \cdots + \frac{1}{n^{2}} + \cdots$$

>
>

$$\sigma_{1} = 1 + \frac{1}{3^{2}} + \frac{1}{5^{2}} + \cdots + \frac{1}{(2n - 1)^{2}} + \cdots\left( = \frac{\pi^{2}}{8} \right)$$

>
>

$$\sigma_{2} = \frac{1}{2^{2}} + \frac{1}{4^{2}} + \frac{1}{6^{2}} + \cdots + \frac{1}{(2n)^{2}} + \cdots$$

>
>

$$\sigma_{3} = 1 - \frac{1}{2^{2}} + \frac{1}{3^{2}} - \frac{1}{4^{2}} + \cdots + ( - 1)^{n - 1}\frac{1}{n^{2}} + \cdots$$

因为

$$\sigma_{2} = \frac{\sigma}{4} = \frac{\sigma_{1} + \sigma_{2}}{4}$$

所以

$$\sigma_{2} = \frac{\sigma_{1}}{3} = \frac{\pi^{2}}{24}\text{，}\sigma = \sigma_{1} + \sigma_{2} = \frac{\pi^{2}}{8} + \frac{\pi^{2}}{24} = \frac{\pi^{2}}{6}$$

并且

$$\sigma_{3} = 2\sigma_{1} - \sigma = \frac{\pi^{2}}{4} - \frac{\pi^{2}}{6} = \frac{\pi^{2}}{12}$$

### 二元函数可微的充分条件

偏导数存在且

$$\lim_{\begin{array}{r}
\Delta x \rightarrow 0 \\
\Delta y \rightarrow 0
\end{array}}\frac{\left\lbrack f\left( x_{0} + \Delta x\text{，}y_{0} + \Delta y \right) - f\left( x_{0}\text{，}y_{0} \right) \right\rbrack - \left\lbrack f_{x}'\left( x_{0}\text{，}y_{0} \right)\Delta x + f_{y}'\left( x_{0}\text{，}y_{0} \right)\Delta y \right\rbrack}{\sqrt{(\Delta x)^{2} + (\Delta y)^{2}}} = 0$$

其中$f\left( x_{0} + \Delta x\text{，}y_{0} + \Delta y \right) - f\left( x_{0}\text{，}y_{0} \right)$是全增量，$f_{x}'\left( x_{0}\text{，}y_{0} \right)\Delta x + f_{y}'\left( x_{0}\text{，}y_{0} \right)\Delta y$是线性主部，故

$$
\left\lbrack f\left( x_{0} + \Delta x\text{，}y_{0} + \Delta y \right) - f\left( x_{0}\text{，}y_{0} \right) \right\rbrack - \left\lbrack f_{x}'\left( x_{0}\text{，}y_{0} \right)\Delta x + f_{y}'\left( x_{0}\text{，}y_{0} \right)\Delta y \right\rbrack
$$

应为$\sqrt{(\Delta x)^{2} + (\Delta y)^{2}}$的高阶无穷小

常用$x_{0} = y_{0} = 0$的情况，此时为

$$\lim_{\begin{array}{r}
\Delta x \rightarrow 0 \\
\Delta y \rightarrow 0
\end{array}}\frac{\left\lbrack f(\Delta x\text{，}\Delta y) - f\left( x_{0}\text{，}y_{0} \right) \right\rbrack - \left\lbrack f_{x}'(0\text{，}0)\Delta x + f_{y}'(0\text{，}0)\Delta y \right\rbrack}{\sqrt{(\Delta x)^{2} + (\Delta y)^{2}}} = 0$$

简记

$$\lim_{\begin{array}{r}
\Delta x \rightarrow 0 \\
\Delta y \rightarrow 0
\end{array}}\frac{\text{全增量} - \text{线性主部}}{\rho} = 0$$
