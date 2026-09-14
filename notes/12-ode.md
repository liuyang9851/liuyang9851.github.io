---
title: 微分方程
description: 可分离变量、齐次、一阶线性、伯努利、可降阶、常系数线性方程、欧拉方程。
---

# 微分方程

[[toc]]

### 可分离变量的微分方程

$$g(y)dy = f(x)dx$$

有

$$\int_{}^{}{g(y)dy} = \int_{}^{}{f(x)dx}$$

即

$$G(y) = F(x) + C$$

$eg.\text{解方程}mg - kv = ma$，其中$v\left| \underset{t = 0}{} \right.\  = 0$

解：分离变量，得

$$\frac{dv}{mg - kv} = \frac{dt}{m}$$

由$mg - kv > 0$，两端积分，得

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

$$C_{3} = - g$$

得到

$$x = g\left( e^{- \frac{k}{m}t} - 1 \right)$$

$$\text{又由于}v = \frac{mg}{k}\left( 1 - e^{- \frac{k}{m}t} \right)\text{，将}1 - e^{- \frac{k}{m}t} = \frac{kv}{mg}\text{代入，得}$$

$$x = - \frac{k}{m}v$$

这样就得到了所谓的"另类加速度"。

### 齐次微分方程

$$\frac{dy}{dx} = \varphi\left( \frac{y}{x} \right)$$

$$\text{令}u = \frac{y}{x}\text{，则}\ y = xu\text{，有}$$

$$\frac{dy}{dx} = (xu)' = u + x\frac{du}{dx}$$

因此有

$$\varphi\left( \frac{y}{x} \right) = \varphi(u) = u + x\frac{du}{\ dx}$$

是一个可分离变量的方程，整理得

$$\frac{du}{\varphi(u) - u} = \frac{dx}{x}$$

即

$$\int_{}^{}{\frac{1}{\varphi\left( \frac{y}{x} \right) - \frac{y}{x}}d\left( \frac{y}{x} \right)} = \int_{}^{}\frac{dx}{x} = \ln|x| + C$$

### 可化为齐次的微分方程

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

### 一阶齐次线性微分方程

$$\frac{dy}{dx} + P(x)y = 0$$

分离变量，得

$$\frac{dy}{y} = - P(x)dx$$

两端积分，得

$$\ln|y| = - \int_{}^{}{P(x)dx} + C$$

通解

$$y = Ce^{- \int_{}^{}{P(x)dx}}\ \ \left( C = \pm e^{C_{1}} \right)$$

此处的$\int_{}^{}{P(x)dx}$表示$P(x)$的某个确定的原函数（即不用加常数$C$），下同。

### 一阶线性微分方程

$$\frac{dy}{dx} + P(x)y = Q(x)\text{或}y' + P(x)y = Q(x)$$

的通解为

$$y = e^{- \int_{}^{}{P(x)dx}}\left( \int_{}^{}{Q(x)e^{\int_{}^{}{P(x)dx}}dx} + C \right)$$

$$= \exp\left( - \int_{}^{}{P(x)dx} \right)\left( \int_{}^{}{Q(x)\exp\left( \int_{}^{}{P(x)dx} \right)dx} + C \right)$$

$$y = Ce^{- \int_{}^{}{P(x)dx}} + e^{- \int_{}^{}{P(x)dx}}\int_{}^{}{Q(x)e^{\int_{}^{}{P(x)dx}}dx}$$

证明：常数变易法

$$\text{设}y = ue^{- \int_{}^{}{P(x)dx}}\text{是方程}\frac{dy}{dx} + P(x)y = Q(x)\text{的通解}\ \left. \text{（}u\text{是所谓}``\text{变易}"\text{的函数} \right.\text{）}\ \text{，则}$$

$$\frac{dy}{dx} = u'e^{- \int_{}^{}{P(x)dx}} - uP(x)e^{- \int_{}^{}{P(x)dx}}$$

$$\text{将}y = ue^{- \int_{}^{}{P(x)dx}}\text{和}\ \frac{dy}{dx} = u'e^{- \int_{}^{}{P(x)dx}} - uP(x)e^{- \int_{}^{}{P(x)dx}}\text{代入}\ \frac{dy}{dx} + P(x)y = Q(x)\text{，得}$$

$$u'e^{- \int_{}^{}{P(x)dx}} - uP(x)e^{- \int_{}^{}{P(x)dx}} + P(x)ue^{- \int_{}^{}{P(x)dx}} = Q(x)$$

后两项抵消，得

$$u'e^{- \int_{}^{}{P(x)dx}} = Q(x)$$

$$u' = Q(x)e^{\int_{}^{}{P(x)dx}}$$

两端积分，得

$$u = \int_{}^{}{Q(x)e^{\int_{}^{}{P(x)dx}}dx} + C$$

把这个结果代入$y = ue^{- \int_{}^{}{P(x)dx}}$，得

$$y = e^{- \int_{}^{}{P(x)dx}}\left( \int_{}^{}{Q(x)e^{\int_{}^{}{P(x)dx}}dx} + C \right) = Ce^{- \int_{}^{}{P(x)dx}} + e^{- \int_{}^{}{P(x)dx}}\int_{}^{}{Q(x)e^{- \int_{}^{}{P(x)dx}}dx}$$

这个证明过程类似于"原函数与导函数混合还原"中等号右边为非0式的做法。

### 伯努利方程

$$\frac{dy}{dx} + P(x)y = Q(x)y^{n}$$

两边同除$y^{n}$，得

$$y^{- n}\frac{dy}{dx} + P(x)y^{1 - n} = Q(x)$$

令$z = y^{1 - n}$，对z求导得

$$\frac{dz}{dy} = (1 - n)y^{- n}\frac{dy}{dx}$$

将该式代入上式，得

$$y^{- n}\frac{1}{(1 - n)y^{- n}}\frac{dz}{dx} + P(x)y^{1 - n} = Q(x)$$

两边同乘$(1 - n)$，并把$y^{1 - n}$代为z，得

$$\frac{dz}{dx} + (1 - n)P(x)z = (1 - n)Q(x)$$

此式为一阶线性方程，其通解为

$$y^{1 - n} = Ce^{- \int_{}^{}{(1 - n)P(x)dx}} + e^{- \int_{}^{}{(1 - n)P(x)dx}}\int_{}^{}{(1 - n)Q(x)e^{- \int_{}^{}{(1 - n)P(x)dx}}dx}$$

记$g(x) = - \int_{}^{}{(1 - n)P(x)dx}$，则其可表示为

$$y^{1 - x} = Ce^{g(x)} + e^{g(x)}\int_{}^{}{(1 - n)Q(x)e^{g(x)}dx}$$

### 可降阶的高阶微分方程

1\.

$$y^{(n)} = f(x)$$

连续积分即得

2\.

$$y^{''} = f\left( x\text{，}y' \right)$$

令$p = y'$，得

$$p' = f(x\text{，}p)$$

此是关于x和p的一阶微分方程，如果能求得其通解

$$p = \varphi\left( x\text{，}C_{1} \right)$$

则原方程的通解为

$$y = \int_{}^{}{\varphi\left( x\text{，}C_{1} \right)dx} + C_{2}$$

3\.

$$y^{''} = f\left( y\text{，}y' \right)$$

令$p = y'$，得

$$y^{''} = \frac{dp}{dx} = \frac{dp}{dy}\frac{dy}{dx} = p\frac{dp}{dy}$$

代入原方程得

$$p\frac{dp}{dy} = f\left( y\text{，}y' \right)$$

此是关于y和p的一阶微分方程，如果能求得其通解

$$p = \varphi\left( y\text{，}C_{1} \right)$$

则原方程的通解为

$$\int_{}^{}\frac{dy}{\varphi\left( y\text{，}C_{1} \right)} = x + C_{2}$$

### 二阶常系数齐次线性微分方程

$$y^{''} + py' + qy = 0$$

考虑特征方程

$$r^{2} + pr + q = 0$$

（1）当$\Delta > 0$时，有两个不等实根

$$r_{1} = \frac{- p + \sqrt{p^{2} - 4q}}{2}\text{，}r_{2} = \frac{- p - \sqrt{p^{2} - 4q}}{2}$$

此时方程的通解为

$$y = C_{1}e^{r_{1}x} + C_{2}e^{r_{2}x}$$

（2）当$\Delta = 0$时，有两个等根

$$r = - \frac{p}{2}$$

此时方程的通解为

$$y = \left( C_{1} + C_{2}x \right)e^{rx}$$

（3）当$\Delta < 0$时，有两个共轭复根

$$r_{1} = \alpha + \beta i\text{，}r_{2} = \alpha - \beta i$$

其中

$$\alpha = - \frac{p}{2}\text{，}\beta = \frac{\sqrt{4q - p^{2}}}{2}$$

此时方程的通解为

$$t = e^{\alpha x}\left( C_{1}\cos{\beta x} + C_{2\ }\sin{\beta x} \right)$$

### 二阶常系数非齐次线性微分方程

$$y^{''} + py' + q = f(x)$$

（1）$f(x) = e^{\lambda x}P_{m}(x)$，其中

$$P_{m}(x) = a_{0} + a_{1}x + a_{2}x^{2} + \cdots + a_{m}x^{m}\ \ \ \left. \text{（即}P_{m}(x)\text{的次数为}m \right.\text{）}$$

考虑特征方程

$$r^{2} + pr + q = 0$$

则方程的一个特解为

$$y^{*} = x^{k}e^{\lambda x}R_{m}(x)$$

其中$R_{m}(x)$是与$P_{m}(x)$同次（m次）的多项式（系数全部待定），k按照$\lambda$不是特征方程的根、是特征方程的单根$\left( \lambda \neq - \frac{p}{2} \right)$或是特征方程的重根$\left( \lambda = - \frac{p}{2} \right)$依次取0、1或2。换种表述如下：

$$R_{m}(x) = b_{0} + b_{1}x + b_{2}x^{2} + \cdots + b_{m}x^{m}\text{，}k = \left\{ \begin{array}{r}
0\text{，}\lambda \neq r_{1} \neq r_{2}\ \ \ \  \\
1\text{，}\lambda = r_{12} \neq r_{21} \\
2\text{，}\lambda \neq r_{1} \neq r_{2}\ \ \ \ 
\end{array} \right.\ $$

（2）

$$
f(x) = e^{\lambda x}\left\lbrack P_{l}(x)\cos{\omega x} + Q_{n}(x)\sin{\omega x} \right\rbrack
$$

，其中$\lambda \text{，}\omega$是常数，$\omega \neq 0$，$P_{l}(x)$、$Q_{n}(x)$分别是x的l次、n次多项式，且仅有一个可为零

考虑特征方程

$$r^{2} + pr + q = 0$$

则方程的一个特解为

$$y^{*} = x^{k}e^{\lambda x}\left\lbrack R_{m}^{(1)}(x)\cos{\omega x} + R_{m}^{(2)}(x)\sin{\omega x} \right\rbrack$$

其中$R_{m}^{(1)}(x)$、$R_{m}^{(2)}(x)$是m次多项式，$m = \max\left\{ l\text{，}n \right\}$，而k按照$\lambda + \omega i\text{或}(\lambda - \omega i)$不是特征方程的根、或是特征方程的单根依次取0或1。

求解时，为了得到$R_{m}(x)$各系数的值，可以将其代入原方程求得系数的值（即待定系数法）。

### n阶常系数齐次线性微分方程

$$y^{(n)} + p_{1}y^{(n - 1)} + p_{2}y^{(n - 2)} + \cdots + p_{n - 1}y' + p_{n}y = 0$$

$$\text{记}D = \frac{d}{dx}\text{，}Dy = \frac{dy}{dx}\text{，}D^{n}y = \frac{d^{n}y}{dx^{n}}\text{，则}$$

$$L(D) = D^{n} + p_{1}D^{n - 1} + \cdots + p_{n - 1}D + p_{n} = 0$$

考虑特征方程

$$r^{n} + p_{1}r^{n - 1} + p_{2}r^{n - 2} + \cdots + p_{n - 1}r + p_{n} = 0$$

对应情况如下

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
特征方程的根                 微分方程通解中的对应项
------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
单实根r                   给出一项： $Ce^{rx}$

一对单复根$r_{1,2} = \alpha \pm \beta i$   给出两项： $e^{\alpha x}\left( C_{1}\cos{\beta x} + C_{2}\sin{\beta x} \right)$

k重实根r                   给出k项： $e^{rx}\left( C_{1} + C_{2}x + \cdots + C_{k}x^{k - 1} \right)$

一对k重复根$r_{1,2} = \alpha \pm \beta i$  给出2k项：

$$
e^{\alpha x}\left\lbrack \left( C_{1} + C_{2}x + \cdots + C_{k}x^{k - 1} \right)\cos{\beta x} + \left( D_{1} + D_{2}x + \cdots + D_{k}x^{k - 1} \right)\sin{\beta x} \right\rbrack
$$

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### n阶常系数非齐次线性微分方程

$$y^{(n)} + p_{1}y^{(n - 1)} + p_{2}y^{(n - 2)} + \cdots + p_{n - 1}y' + p_{n}y = f(x)$$

（1）$f(x) = e^{\lambda x}P_{m}(x)$，其中

$$P_{m}(x) = a_{0}x^{m} + a_{1}x^{m - 1} + \cdots + a_{m - 1}x + a_{m}$$

考虑特征方程

$$r^{n} + p_{1}r^{n - 1} + p_{2}r^{n - 2} + \cdots + p_{n - 1}r + p_{n} = 0$$

则方程的一个特解为

$$y^{*} = x^{k}e^{\lambda x}R_{m}(x)$$

其中$R_{m}(x)$是与$P_{m}(x)$同次（m次）的多项式，$k$按照$\lambda$不是特征方程的根或是特征方程的$s$重根取0或s

（2）$f(x) = e^{\lambda x}\left\lbrack P_{l}(x)\cos{\omega x} + Q_{n}(x)\sin{\omega x} \right\rbrack$，其中$\lambda \text{，}\omega$是常数，$\omega \neq 0$，$P_{l}(x)$、$Q_{n}(x)$分别是$x$的$l$次、$n$次多项式，且仅有一个可为零

考虑特征方程

$$r^{n} + p_{1}r^{n - 1} + p_{2}r^{n - 2} + \cdots + p_{n - 1}r + p_{n} = 0$$

则方程的一个特解为

$$y^{*} = x^{k}e^{\lambda x}\left\lbrack R_{m}^{(1)}(x)\cos{\omega x} + R_{m}^{(2)}(x)\sin{\omega x} \right\rbrack$$

其中$R_{m}^{(1)}(x)$、$R_{m}^{(2)}(x)$是$m$次多项式，$m = \max\left\{ l\text{，}n \right\}$，而$k$按照$\lambda + \omega i\text{或}(\lambda - \omega i)$不是特征方程的根、或是特征方程的$s$重根取$0$或$s$。

### 欧拉方程

$$x^{n}y^{(n)} + p_{1}x^{n - 1}y^{(n - 1)} + p_{2}x^{n - 2}y^{(n - 2)} + \cdots + p_{n - 1}xy' + p_{n}y = f(x)$$

当$x > 0$时，令$t = \ln x$，得（当$x < 0$时，令$t = \ln( - x)$）

$$\frac{dy}{dx} = \frac{dy}{dx} \cdot \frac{dt}{dx} = \frac{1}{x}\frac{dy}{dt}$$

### 线性微分方程的解的结构

### 二阶齐次线性微分方程

定理1：二阶齐次线性微分方程的两个解的线性组合也是该二阶齐次线性微分方程的解。

若$y_{1}(x)\text{、}y_{2}(x)$满足$y^{''} + P(x)y' + Q(x)y = 0$，则解$C_{1}y_{1}(x) + C_{2}y_{2}(x)$亦满足该方程。

定理2：二阶齐次线性微分方程的两个线性无关的解（不一定是"特解"）的线性组合是该二阶齐次线性微分方程的通解。

>

$$\text{若两特解}y_{1}(x)\text{、}y_{2}(x)\text{满足}y_{1}(x) \neq ky_{2}(x)\text{，则}y^{''} + P(x)y' + Q(x)y = 0\text{的通解为}C_{1}y_{1}(x) + C_{2}y_{2}(x)$$

### 二阶非齐次线性微分方程

定理3：二阶非齐次线性微分方程的一个解（不一定是"特解"）加上对应的二阶齐次线性微分方程的通解是该二阶非齐次线性微分方程的通解。（即$y = Y + y^{*}$）

定理4（叠加原理）：把一个二阶非齐次线性微分方程的自由项拆成两个函数，形成的两个新的二阶非齐次线性微分方程的特解的和是原二阶非齐次线性微分方程的一个特解。

若$y_{1}^{*}$和$y_{2}^{*}$分别是$y^{''} + P(x)y' + Q(x)y = f_{1}(x)$和$y^{''} + P(x)y' + Q(x)y = f_{2}(x)$的特解，则$y_{1}^{*} + y_{2}^{*}$是$y^{''} + P(x)y' + Q(x)y = f_{1}(x) + f_{2}(x)$的特解。

$n$阶线性微分方程

定理1：$n$阶齐次线性微分方程的$n$个线性无关的特解的线性组合是该$n$阶齐次线性微分方程的通解。

定理2：$n$阶非齐次线性微分方程的一个解（不一定是"特解"）加上对应的$n$阶齐次线性微分方程的通解是该$n$阶非齐次线性微分方程的通解。

定理3：把一个$n$阶非齐次线性微分方程的自由项拆成两个函数，形成的两个新的$n$阶非齐次线性微分方程的特解的和是原$n$阶非齐次线性微分方程的一个特解。

解题时常用到如下的一个结论

若$y_{1}(x)\text{、}y_{2}(x)$是$n$阶非齐次线性微分方程的两个解，则$y_{1}(x) - y_{2}(x)$是对应的$n$阶齐次线性微分方程的解。

一般来说，题目通常会给出二阶非齐次线性微分方程的三个解，这就需要合理地对这三个解做差以找出线性无关的二阶齐次线性微分方程的两个解，这样就找到了二阶齐次线性微分方程的通解，进而得到二阶非齐次线性微分方程的通解。

### 常系数线性微分方程组

（1）从方程组中校消去一些未知函数及其各阶导数，得到只含有一个未知函数的高阶常系数线性微分方程。

（2）解此高阶微分方程，求出满足该方程的未知函数。

（3）把已求得都函数代入原方程组，一般来说，不必经过积分就可求出其余的未知函数

现将这些方程的解总结如下

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
类型                                             表达式                                             特解                                              通解
-------------------------------------------------- ------------------------------------------------- ------------------------------------------------- -------------------------------------------------
                                                                                                                                                         

                                                                                                                                                         

                                                                                                                                                         

                                                                                                                                                         

                                                                                                                                                         

                                                                                                                                                         

                                                                                                                                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

$$\text{若}g(x)\sim ax^{m}\text{，}f(x)\sim bx^{n}\text{，则}\int_{0}^{g(x)}{f(t)dt}\sim\int_{0}^{ax^{m}}{bt^{n}dt}$$

### 斯特林公式

$$\lim_{n \rightarrow + \infty}\frac{e^{n}n!}{n^{n}\sqrt{n}} = \sqrt{2\pi}$$

用它可以近似$n!$

$$n! = \lim_{n \rightarrow + \infty}\frac{n^{n}\sqrt{2\pi n}}{e^{n}}$$

当n很大时，亦即

$$n! = \sqrt{2\pi n}\left( \frac{n}{e} \right)^{n}$$

$$eg.20! = 2,432,902,008,176,640,000 \approx 2,422,786,846,761,135,000$$

$$50! = 3.0414093201713884 \times 10^{64} \approx 3.036344593938168 \times 10^{64}$$
