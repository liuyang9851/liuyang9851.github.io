---
title: 极限
description: 数列与函数的极限、泰勒展开、洛必达法则、等价无穷小、夹逼与 Stolz 定理。
---

# 极限

[[toc]]

### 泰勒公式

> $${f(x) = \sum_{n = 1}^{N}{\frac{f^{(n)}\left( x_{0} \right)}{n!}\left( x - x_{0} \right)^{n}} + R_{n}(x)
> }{= \frac{f\left( x_{0} \right)}{0!} + \frac{f'\left( x_{0} \right)}{1!}\left( x - x_{0} \right) + \frac{f^{''}\left( x_{0} \right)}{2!}\left( x - x_{0} \right)^{2} + \ldots + \frac{f^{(n)}\left( x_{0} \right)}{n!}\left( x - x_{0} \right)^{n} + R_{n}(x)}$$

其中$R_{n}(x)$称为余项，其具体有如下几种形式

$$\text{佩亚诺余项：}o\left( \left( x - x_{0} \right)^{n} \right)$$

$$\text{拉格朗日余项：}\frac{f^{(n + 1)}(\xi)}{(n + 1)!}\left( x - x_{0} \right)^{n + 1}\ \ \left( \xi \text{是}x_{0}\text{与}x\text{之间的某个值} \right)$$

### 麦克劳林公式

令一般式中的$x_{0} = 0$，得

$$f(x) = \sum_{n = 1}^{N}{\frac{f^{(n)}(0)}{n!}x^{n}} + R_{n}(x) = \frac{f(0)}{0!} + \frac{f'(0)}{1!}x + \frac{f^{''}(0)}{2!}x^{2} + \ldots + \frac{f^{(n)}(0)}{n!}x^{n} + R_{n}(x)$$

### 常用函数的泰勒展开

>

$$1.e^{x} = 1 + \frac{x}{1} + \frac{x^{2}}{2} + \frac{x^{3}}{6} + \ldots + x^{n} + o\left( x^{n} \right) = \sum_{n = 0}^{\infty}\frac{x^{n}}{n!}\ \ $$

>
>

$$\Rightarrow \ \ a^{x} = e^{x\ln a} = \sum_{n = 0}^{\infty}\frac{\left( \ln a \right)^{n}x^{n}}{n!}$$

>
>

$$2.\sin x = \frac{x}{1!} - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + \ldots + \frac{( - 1)^{n}}{(2n + 1)!}x^{2n + 1} + o\left( x^{2n + 2} \right) = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{(2n + 1)!}x^{2n + 1}}$$

>
>

$$3.\cos x = 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} - \frac{x^{6}}{6!} + \ldots + \frac{( - 1)^{n}}{(2n)!}x^{2n} + o\left( x^{2n} \right) = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{(2n)!}x^{2n}}$$

>
>

$$4.\ln(1 + x) = x - \frac{x^{2}}{2!} + \frac{x^{3}}{3!} - \frac{x^{4}}{4!} + \ldots + \frac{( - 1)^{n - 1}}{n!}x^{n} + o\left( x^{n} \right) = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n - 1}}{n!}x^{n}}\ \ $$

>
>

$$\  \Rightarrow \ln(1 - x) = - x - \frac{x^{2}}{2!} - \frac{x^{3}}{3!} - \frac{x^{4}}{4!} + \ldots = \sum_{n = 0}^{\infty}{\frac{- 1}{n!}x^{n}}\ \ \left( |x| < 1 \right)\ \ $$

>
>

$$\Rightarrow \ln\frac{1 + x}{1 - x} = 2\left( x + \frac{1}{3}x^{3} + \frac{1}{5}x^{5} + \cdots \right) = 2\sum_{n = 0}^{\infty}\frac{x^{2n + 1}}{2n + 1}\ \ \left( |x| < 1 \right)$$

>
> $$5.(1 + x)^{m} = 1 + mx + \frac{m(m - 1)}{2!}x^{2} + \cdots + \begin{pmatrix}
> m \\
> n
> \end{pmatrix}x^{n} + o\left( x^{n} \right) = \sum_{n = 0}^{\infty}{\begin{pmatrix}
> m \\
> n
> \end{pmatrix}x^{n}}\ \ \left( m\mathbb{\in N} \right)$$
>
>

$$6.(1 + x)^{a} = 1 + ax + \frac{a(a - 1)}{2!}x^{2} + \cdots + \frac{a(a - 1)\cdots(a - n + 1)}{a!}x^{n} + o(1)\ \ \left( a\mathbb{\in R} \right)$$

>
>

$$\Rightarrow \sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^{2}}{8} + \frac{x^{3}}{16} - \frac{5x^{4}}{128} + \ldots$$

>
>

$$\Rightarrow \frac{1}{1 + x} = 1 - x + x^{2} - x^{3} + \cdots = \sum_{n = 0}^{\infty}{( - 1)^{n}x^{n}}\ \ \left( |x| < 1 \right)\ \ $$

>
>

$$\Rightarrow \ \ \frac{1}{1 + x^{2}} = \sum_{n = 0}^{\infty}{( - 1)^{n}x^{2n}}\ \ \left( |x| < 1 \right)$$

>
>

$$\Rightarrow \frac{1}{1 - x} = 1 + x + x^{2} + x^{3} + \cdots = \sum_{n = 0}^{\infty}x^{n}\ \ \left( |x| < 1 \right)$$

>
>

$$7.\tan x = x + \frac{1}{3}x^{3} + \frac{2}{15}x^{5} + \cdots$$

因此，考虑$\xi$的值，使上式取最大值，所得到的范围即为误差范围

### L'Hospital（洛必达）法则

$$\text{设}f(x)\text{，}g(x)\text{可导，}\ g'(x) \neq 0\text{，}\lim\frac{f'(x)}{g'(x)}\text{存在，当满足以下两个条件}$$

$$1.\lim{f(x)} = \lim{g(x)} = 0$$

$$2.\lim{g(x)} = \infty$$

中的一个时，即有

$$\lim\frac{f(x)}{g(x)} = \lim\frac{f'(x)}{g'(x)}$$

### 特殊极限定义式及推论

$$1.\lim_{x \rightarrow 0}\frac{\sin x}{x} = 1$$

$$2.\lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n} = \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n + 1} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{1}{x} \right)^{x} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{k}{x} \right)^{x} = \lim_{\frac{x}{k} \rightarrow \infty}\left( 1 + \frac{1}{\frac{x}{k}} \right)^{\frac{x}{k} \cdot k} = e^{k} \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{a}{x} \right)^{bx + c} = e^{ab}$$

$$\text{特别地，}e^{x} = \lim_{n \rightarrow \infty}\left( 1 + \frac{x}{n} \right)^{n} = \exp(x)$$

$$\lim{u(x)^{v(x)}} = e^{\lim\left\lbrack \left( u(x) - 1 \right)v(x) \right\rbrack}\text{，其中在同一过程中}\lim{u(x)} = 1\text{，}\lim{v(x)} = \infty$$

$$3.\lim_{n \rightarrow \infty}\left( 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} - \ln n \right) = \gamma = 0.557\ 215\ 664\ 90\cdots$$

### 等价无穷小代换

常见的等价无穷小可以用洛必达法则轻易地得出，等价无穷小替换可以视为泰勒公式的简易应用。

一阶：

$$
x\ \ \sim\ \ \sin x\ \ \sim\ \ \tan x\ \ \sim\ \ \arcsin{x\ \ }\sim\ \ \arctan x\ \ \sim\ \ e^{x} - 1\ \ \sim\ \ \ln(1 + x)\ \  \sim \ \ \sqrt{1 + x} - \sqrt{1 - x}
$$

$$\text{二阶：}\frac{1}{2}x^{2}\ \  \sim \ \ 1 - \cos x\ \ \sim\ \ x - \ln(1 + x)\ \  \sim \ \ e^{x} - x - 1\sim - \ln{\cos x}$$

三阶：

$$\frac{1}{2}x^{3}\ \  \sim \ \tan x - \sin x\ \  \sim \ \ \arcsin x - \arctan x$$

$$\frac{1}{3}x^{3}\ \  \sim \ \ \tan x - x\ \  \sim \ \ x - \arctan x\ \  \sim \ \ \arcsin x - \sin x$$

$$\frac{2}{3}x^{3}\ \  \sim \ \ \tan x - \arctan x$$

$$- \frac{1}{3}x^{3}\ \  \sim \ \ x - \ln(1 + x) - \frac{x^{2}}{2}$$

$$\frac{1}{6}x^{3}\  \sim \ \ x - \sin x\  \sim \ \tan x - \arcsin x\  \sim \ \arcsin x - x\  \sim \ \sin x - \arctan x$$

其它：

$$(1 + x)^{m} - 1\sim mx$$

$$\log_{a}(1 + x)\sim\frac{x}{\ln a}$$

$$a^{x} - 1\sim x\ln a$$

$$1 - x\sim - \ln x\ \ (x \rightarrow 1)$$

### 一些等价无穷小代换的证明

$$\lim_{x \rightarrow 0}\frac{\sin x}{x} = 1$$

$$\lim_{x \rightarrow 0}\frac{\tan x}{x} = \lim_{x \rightarrow 0}\left( \frac{x}{\sin x} \cdot \cos x \right) = \lim_{x \rightarrow 0}\frac{x}{\sin x} \cdot \lim_{x \rightarrow 0}{\cos x} = 1$$

$$\lim_{x \rightarrow 0}\frac{\arcsin x}{x} = \lim_{t \rightarrow 0}\frac{t}{\sin t} = 1$$

$$\lim_{x \rightarrow 0}\frac{\arctan x}{x} = \lim_{t \rightarrow 0}\frac{t}{\tan t} = 1$$

$$\lim_{x \rightarrow 0}\frac{\ln(1 + x)}{x} = \lim_{x \rightarrow 0}{\ln(1 + x)^{\frac{1}{x}}} = \ln{\lim_{x \rightarrow 0}(1 + x)^{\frac{1}{x}}} = \ln e = 1$$

$$\lim_{x \rightarrow 0}\frac{e^{x} - 1}{x} = \lim_{t \rightarrow 0}\frac{t}{\ln(1 + t)} = 1$$

$$\lim_{x \rightarrow 0}\frac{(1 + x)^{\alpha} - 1}{\alpha x} = \lim_{x \rightarrow 0}\left( \frac{(1 + x)^{\alpha} - 1}{\ln(1 + x)^{\alpha}} \cdot \frac{\alpha\ln(1 + x)}{\alpha x} \right)\overset{(1 + x)^{\alpha} - 1 = t}{\Leftrightarrow}\lim_{t \rightarrow 0}\frac{t}{\ln(1 + t)} \cdot \lim_{x \rightarrow 0}\frac{\alpha\left( 1 + \ln x \right)}{\alpha x} = 1$$

$$- \ln{\cos x} = - \ln\left\lbrack 1 + \left( \cos x - 1 \right) \right\rbrack\sim - \left( \cos x - 1 \right)\sim\frac{1}{2}x^{2}$$

$$\ln(x + 1)\sim x\ \ (x \rightarrow 0)\overset{t = x + 1}{\Leftrightarrow}\ln t\sim t - 1\ \ (t \rightarrow 1) \Leftrightarrow - \ln x\sim 1 - x\ \ (x \rightarrow 1)$$

### 与极限有关的定理和结论

### 1.夹逼定理

数列$\left\{ x_{n} \right\} \text{，}\left\{ y_{n} \right\} \text{，}\left\{ z_{n} \right\}$从某项起开始满足

$$x_{n} \leq y_{n} \leq z_{n}\text{，}\lim_{n \rightarrow \infty}x_{n} = \lim_{n \rightarrow \infty}z_{n} = a$$

则

$$\lim_{n \rightarrow \infty}y_{n} = a$$

### 2.Stolz定理

对数列$\left\{ x_{n} \right\} \text{，}\left\{ y_{n} \right\}$

$$\left. \text{（}1 \right.\text{）若}\left\{ y_{n} \right\} \text{严格单调递增趋于}\  + \infty \text{，且}\lim_{n \rightarrow \infty}\frac{x_{n} - x_{n - 1}}{y_{n} - y_{n - 1}} = a\text{，则}\ \lim_{n \rightarrow \infty}\frac{x_{n}}{y_{n}} = a\ \ (a\text{可以为某数或} \pm \infty)$$

$$(2)\text{若}\left\{ y_{n} \right\} \text{严格单调递减趋于}\ 0\text{，}\left\{ x_{n} \right\} \text{趋于}0\text{，且}\lim_{n \rightarrow \infty}\frac{x_{n} - x_{n - 1}}{y_{n} - y_{n - 1}} = a\text{，则}\ \lim_{n \rightarrow \infty}\frac{x_{n}}{y_{n}} = a\ \ (a\text{可以为某数或} \pm \infty)$$

3.单调有界收敛定理：单调有界数列必定收敛。

4\. 闭区间套定理：如果$\left\{ \left\lbrack a_{n}\text{，}b_{n} \right\rbrack \right\}$构成一个闭区间套，则存在唯一的实数$\xi$属于所有的闭区间$\left\lbrack a_{n}\text{，}b_{n} \right\rbrack$，且$\xi = \lim_{n \rightarrow \infty}a_{n} = \lim_{n \rightarrow \infty}b_{n}$。

5.若数列$\left\{ x_{n} \right\}$收敛于$a$，则其任何子数列也收敛于$a$。

6.Cauchy（柯西）收敛原理：数列$\left\{ x_{n} \right\}$收敛的充要条件是$\left\{ x_{n} \right\}$是基本数列。基本数列$\left\{ x_{n} \right\}$满足：对于任意的$\varepsilon > 0$，存在正整数$N$，使得当$n,m > N$时$\left| x_{n} - x_{m} \right| < \varepsilon$恒成立。

### 常见极限

$$\cdot \lim_{x \rightarrow 0}\frac{a_{0}x^{m} + a_{1}x^{m - 1} + \cdots + a_{m}}{b_{0}x^{n} + b_{1}x^{n - 1} + \cdots + b_{n}} = \left\{ \begin{array}{r}
0\text{，当}a_{m} = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\frac{a_{m}}{b_{n}}\text{，当}a_{m} \neq 0\text{且}b_{n} \neq 0 \\
\infty \text{，当}b_{n} = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ \ \ \ \left( a_{m}\text{，}b_{n}\text{不同时为}0 \right)$$

$$\cdot \lim_{x \rightarrow \infty}\frac{a_{0}x^{m} + a_{1}x^{m - 1} + \cdots + a_{m}}{b_{0}x^{n} + b_{1}x^{n - 1} + \cdots + b_{n}} = \left\{ \begin{array}{r}
0\text{，当}n > m \\
\frac{a_{0}}{b_{0}}\text{，当}n = m \\
\infty \text{，当}n < m
\end{array} \right.\ $$

$$\cdot \lim_{n \rightarrow \infty}{n\sin\frac{180{^\circ}}{n}} = \pi \Rightarrow \lim_{n \rightarrow + \infty}\frac{\sin\frac{\pi}{n}}{\frac{\pi}{n}} = 1 \Rightarrow \lim_{x \rightarrow 0}\frac{\sin x}{x} = 1$$

$$\cdot \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n} = \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n + 1} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{1}{x} \right)^{x} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{k}{x} \right)^{x} = \lim_{\frac{x}{k} \rightarrow \infty}\left( 1 + \frac{1}{\frac{x}{k}} \right)^{\frac{x}{k} \cdot k} = e^{k} \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{a}{x} \right)^{bx + c} = e^{ab}$$

$$\text{特别地，}e^{x} = \lim_{n \rightarrow \infty}\left( 1 + \frac{x}{n} \right)^{n} = \exp(x)$$

$$\cdot \lim_{x \rightarrow \infty}\frac{x^{n}}{e^{\lambda x}} = 0$$

$$\cdot \lim_{x \rightarrow \infty}\frac{a^{x}}{x!} = 0$$

$$\cdot \lim_{x \rightarrow 0}{x\ln x} = 0$$

$$\cdot \lim_{x \rightarrow \infty}\left( x - \ln x \right) = + \infty$$

$$\cdot \lim_{n \rightarrow \infty}\sqrt[n]{n} = 1$$

$$\cdot \lim_{n \rightarrow \infty}\sqrt[n]{n^{k}} = 1$$

$$\cdot \text{若}\lim_{n \rightarrow \infty}a_{n} = a\text{，则}\ \lim_{n \rightarrow \infty}\frac{a_{1} + a_{2} + \cdots + a_{n}}{n} = a$$

$$\cdot \lim_{n \rightarrow \infty}\left( a_{1}^{n} + a_{2}^{n} + \cdots + a_{p}^{n} \right)^{\frac{1}{n}} = \max_{1 \leq i \leq p}\left\{ a_{i} \right\}$$

$$\cdot \lim_{n \rightarrow \infty}{n\left( \sqrt{n^{2} + 1} - \sqrt{n^{2} - 1} \right)} = 1$$

$$\text{若}\ \lim_{n \rightarrow \infty}a_{n} = a\text{，则}\ \lim_{n \rightarrow \infty}\sqrt[n]{a_{1}a_{2}\cdots a_{n}} = a$$

$$\cdot \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} - \ln n \right) = \gamma = 0.557\ 215\ 664\ 90\cdots$$
