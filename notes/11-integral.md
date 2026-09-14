---
title: 积分
description: 不定积分、换元与分部积分、有理函数积分、定积分、反常积分、定积分应用。
---

# 积分

[[toc]]

### 不定积分

定义：在区间I上，函数$f(x)$的带有任意常数项的原函数$F(x) + C$称为$f(x)$（或$f(x)dx$）在区间I上的不定积分，记作

$$\int_{}^{}{f(x)dx} = F(x) + C$$

### 第一换元积分法

$$\int_{}^{}{f\left\lbrack \varphi(x) \right\rbrack\varphi'(x)dx} = \left\lbrack \int_{}^{}{f(u)du} \right\rbrack_{u = \varphi(x)}$$

特别地

$$\int_{}^{}{af(x)dx} = \int_{}^{}{f(x)d(ax + b)}$$

$$eg.\int_{}^{}\frac{dx}{x\ln x} = \int_{}^{}{\frac{1}{\ln x}d\ln x} = \ln\left| \ln x \right| + C$$

### 第二换元积分法

$$\int_{}^{}{f(x)dx} = \left\lbrack \int_{}^{}{f\left( \psi(t) \right)\psi'(t)dt} \right\rbrack_{t = \psi^{- 1}(x)}$$

### 分部积分法

$$\int_{}^{}{uv'dx} = uv - \int_{}^{}{u'vdx}\ \text{或}\ \int_{}^{}{udv} = uv - \int_{}^{}{vdu}$$

证明：由$\left\lbrack u(x)v(x) \right\rbrack' = u'(x)v(x) + u(x)v'(x)$，有

$$\frac{duv}{dx} = v\frac{du}{dx} + u\frac{dv}{dx}$$

等式两边同乘$dx$，得

$$duv = vdu + udv$$

两边积分，即得

$$uv = \int_{}^{}{duv} = \int_{}^{}{vdu} + \int_{}^{}{udv}$$

留在前面的优先级：反对幂三指（反三角函数，对数函数，幂函数，三角函数，指数函数，$e^{x}$）

分部积分法亦有如下公式

$$\int_{}^{}{uvdw} = uvw - \int_{}^{}{uwdv} - \int_{}^{}{vwdu}$$

$$\int_{}^{}{\sin{ax}e^{bx}dx} = \frac{1}{a^{2} + b^{2}}\left| \begin{matrix}
\left( e^{bx} \right)' & \left( \sin{ax} \right)' \\
e^{bx} & \sin{ax}
\end{matrix} \right| + C$$

$$\int_{}^{}{\cos{ax}e^{bx}dx} = \frac{1}{a^{2} + b^{2}}\left| \begin{matrix}
\left( e^{bx} \right)' & \left( \cos{ax} \right)' \\
e^{bx} & \cos{ax}
\end{matrix} \right| + C$$

### 有理函数的积分

$$\int_{}^{}\frac{dx}{ax^{2} + bx + c} = \left\{ \begin{array}{r}
\frac{2}{\sqrt{4ac - b^{2}}}\arctan\frac{2ax + b}{\sqrt{4ac - b^{2}}} + C\ \ \left( b^{2} < 4ac \right)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
 - \frac{1}{a\left( x - \frac{b}{2a} \right)} + C\ \ \left( b^{2} = 4ac \right)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\frac{1}{\sqrt{b^{2} - 4ac}}\ln\left| \frac{2ax + b - \sqrt{b^{2} - 4ac}}{2ax + b + \sqrt{b^{2} - 4ac}} \right| + C\ \ \left( b^{2} > 4ac \right)
\end{array} \right.\ $$

$$\int_{}^{}{\frac{x}{ax^{2} + bx + c}dx} = \frac{1}{2a}\ln\left| ax^{2} + bx + c \right| - \frac{b}{2a}\int_{}^{}\frac{dx}{ax^{2} + bx + c}$$

由上面两个积分可以组合分母不超过二次的有理函数的积分

$$\int_{}^{}\frac{dx}{(x - a)^{n}} = \left\{ \begin{array}{r}
\ln|x - a| + C \\
 - \frac{1}{n - 1} \cdot \frac{1}{(x - a)^{n - 1}} + C
\end{array} \right.\ $$

$$I_{n} = \int_{}^{}\frac{dx}{\left( x^{2} + bx + c \right)^{n}} = \frac{2n - 3}{2\left( c - \frac{b^{2}}{4} \right)(n - 1)}I_{n - 1} + \frac{1}{2\left( c - \frac{b^{2}}{4} \right)(n - 1)} \cdot \frac{x + \frac{b}{2}}{\left\lbrack \left( x + \frac{b}{2} \right)^{2} + c - \frac{b^{2}}{4} \right\rbrack^{n - 1}}$$

由上面两个积分可以求出任意有理函数的积分

$$eg.\int_{}^{}{\frac{4x^{3} - 13x^{2} + 3x + 8}{(x + 1)(x - 2)(x - 1)^{2}}dx}$$

$$\frac{4x^{3} - 13x^{2} + 3x + 8}{(x + 1)(x - 2)(x - 1)^{2}} = \frac{A}{x + 1} + \frac{B}{x - 2} + \frac{C}{x - 1} + \frac{D}{(x - 1)^{2}} \Rightarrow$$

$$4x^{3} - 13x^{2} + 3x + 8 = A(x - 2)(x - 1)^{2} + B(x + 1)(x - 1)^{2} + C(x + 1)(x - 2)(x - 1) + D(x + 1)(x - 2)$$

### 常用导数与积分表（C为任意常数）

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

导数

</th>
<th>

积分

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

导数求导法则                                                                                         | 常用积分

</td>
<td>

法则

</td>
</tr>
<tr>
<td>

$$(u \pm v)' = u' \pm v'$$

</td>
<td>

$$\int_{}^{}{(u + v)dx} = \int_{}^{}{udx} + \int_{}^{}{vdx}$$

</td>
</tr>
<tr>
<td>

$$(Cu)' = Cu'$$

</td>
<td>

$$\int_{}^{}{kudx} = k\int_{}^{}{udx}\ \ \left. （k是常数 \right.）$$

</td>
</tr>
<tr>
<td>

$$(uv)' = u'v + iv'$$

</td>
<td>

$$\int_{}^{}{udv} = uv - \int_{}^{}{vdu}$$

</td>
</tr>
<tr>
<td>

$$\left( \frac{u}{v} \right)' = \frac{u'v - uv'}{v^{2}}$$

</td>
<td>

$$\int_{}^{}\frac{dx}{e^{x}} = - \frac{1}{e^{x}}$$

</td>
</tr>
<tr>
<td>

$${f_{x}^{- 1}}'(x) = \frac{1}{f_{y}'(y)}或\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}}$$

</td>
<td></td>
</tr>
<tr>
<td>

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

</td>
<td>

$$\int_{}^{}{f\left\lbrack \varphi(x) \right\rbrack\varphi'(x)dx} = \left\lbrack \int_{}^{}{f(u)du} \right\rbrack_{u = \varphi(x)}$$

</td>
</tr>
<tr>
<td>

$或$

</td>
<td></td>
</tr>
<tr>
<td>

$$y_{x}' = y_{u}' \cdot u_{x}'$$

</td>
<td></td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{f(x)dx} = \left\lbrack \int_{}^{}{f\left( \psi(t) \right)\psi'(t)dt} \right\rbrack_{t = \psi^{- 1}(x)}$$

</td>
</tr>
<tr>
<td>

非三角函数类函数

</td>
<td></td>
</tr>
<tr>
<td>

$$(C)' = 0$$

</td>
<td>

$$\int_{}^{}{kdx} = kx + C\ \ \left. （k \neq 0 \right.）$$

</td>
</tr>
<tr>
<td>

$$\left( x^{\mu} \right)' = \mu x^{\mu - 1}$$

</td>
<td>

$$\int_{}^{}{x^{\mu}dx} = \frac{x^{\mu + 1}}{\mu + 1} + C\ \ (\mu \neq - 1)$$

</td>
</tr>
<tr>
<td>

$$\left( a^{x} \right)' = a^{x}\ln a\ \ (a > 0，a \neq 1)$$

</td>
<td>

$$\int_{}^{}{a^{x}dx} = \frac{a^{x}}{\ln a} + C$$

</td>
</tr>
<tr>
<td>

$$\left( e^{x} \right)' = e^{x}$$

</td>
<td>

$$\int_{}^{}{e^{x}dx} = e^{x} + C$$

</td>
</tr>
<tr>
<td>

$$\left( \log_{a}x \right)' = \frac{1}{x\ln a}\ \ (a > 0，a \neq 1)$$

</td>
<td>

$$\int_{}^{}{\log_{a}xdx} = \frac{1}{\ln a}\left( x\ln x - x \right) + C$$

</td>
</tr>
<tr>
<td>

$$\left( \ln x \right)' = \frac{1}{x}$$

</td>
<td>

$$\int_{}^{}\frac{dx}{x} = \ln|x| + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\ln xdx} = x\ln x - x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}\frac{dx}{x\ln x} = \ln\left| \ln x \right| + C$$

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}\frac{dx}{\sqrt{a^{2} - x^{2}}} = \arcsin\frac{x}{a} + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\sqrt{a^{2} - x^{2}}dx} = \frac{a^{2}}{2}\arcsin\frac{x}{a} + \frac{1}{2}x\sqrt{a^{2} - x^{2}} + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}\frac{dx}{\sqrt{x^{2} + a^{2}}} = \ln\left( x + \sqrt{x^{2} + a^{2}} \right) + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\sqrt{x^{2} + a^{2}}dx} = \frac{1}{2}\left( x\sqrt{x^{2} + a^{2}} + a^{2}\ln\left| x + \sqrt{x^{2} + a^{2}} \right| \right) + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}\frac{dx}{\sqrt{x^{2} - a^{2}}} = \ln\left| x + \sqrt{x^{2} - a^{2}} \right| + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\sqrt{x^{2} - a^{2}}dx} = \frac{1}{2}\left( x\sqrt{x^{2} - a^{2}} - a^{2}\ln\left| x + \sqrt{x^{2} - a^{2}} \right| \right) + C$$

</td>
</tr>
<tr>
<td>

三角函数

</td>
<td></td>
</tr>
<tr>
<td>

$$\left( \sin x \right)' = \cos x$$

</td>
<td>

$$\int_{}^{}{\sin xdx} = - \cos x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\sin^{2}xdx} = \frac{1}{2}x - \frac{1}{4}\sin{2x} + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\sin^{3}xdx} = - \cos x + \frac{1}{3}\cos^{3}x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\sin^{4}xdx} = \frac{3}{8}x - \frac{1}{4}\sin{2x} + \frac{1}{32}\sin{4x} + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$I_{n} = \int_{}^{}{\sin^{n}xdx} = - \frac{1}{n}\sin^{n - 1}x\cos x + \frac{n - 1}{n}I_{n - 2}$$

</td>
</tr>
<tr>
<td>

$$\left( \cos x \right)' = - \sin x$$

</td>
<td>

$$\int_{}^{}{\cos xdx} = \sin x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\cos^{2}xdx} = \frac{1}{2}x + \frac{1}{4}\sin{2x} + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\cos^{3}xdx} = \sin x - \frac{1}{3}\sin^{3}x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\cos^{4}xdx} = \frac{3}{8}x + \frac{1}{4}\sin{2x} + \frac{1}{32}\sin{4x} + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$I_{n} = \int_{}^{}{\cos^{n}xdx} = \frac{1}{n}\cos^{n - 1}x\sin x + \frac{n - 1}{n}I_{n - 2}$$

</td>
</tr>
<tr>
<td>

$$\left( \tan x \right)' = \frac{1}{\cos^{2}x} = \sec^{2}x$$

</td>
<td>

$$\int_{}^{}\frac{dx}{\cos^{2}x} = \int_{}^{}{\sec^{2}xdx} = \tan x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\tan xdx} = - \ln\left| \cos x \right| + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\tan^{2}xdx} = \tan x - x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\tan^{3}xdx} = \frac{1}{2}\tan^{2}x + \ln\left| \cos x \right| + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\tan^{4}xdx} = \frac{1}{3}\tan^{3}x - \tan x + x + C$$

</td>
</tr>
<tr>
<td>

$$\left( \cot x \right)' = - \frac{1}{\sin^{2}x} = - \csc^{2}x$$

</td>
<td>

$$\int_{}^{}\frac{dx}{\sin^{2}x} = \int_{}^{}{\csc^{2}xdx} = - \cos x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\cot xdx} = \ln\left| \sin x \right| + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\cot^{2}xdx} = - \cot x - x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\cot^{3}xdx} = - \frac{1}{2}\cot^{2}x - \ln\left| \sin x \right| + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\cot^{4}xdx} = - \frac{1}{3}\cot^{3}x + \cot x + x + C$$

</td>
</tr>
<tr>
<td>

$$\left( \sec x \right)' = \frac{\tan x}{\cos x} = \sec x\tan x$$

</td>
<td>

$$\int_{}^{}{\sec x\tan xdx} = \sec x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\sec xdx} = \ln\left| \tan\left( \frac{\pi}{4} + \frac{x}{2} \right) \right| + C = \ln\left| \sec x + \tan x \right| + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\sec^{2}xdx} = \tan x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\sec^{3}xdx} = \frac{1}{2}\left( \sec x\tan x + \ln\left| \sec x + \tan x \right| \right) + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\sec^{4}xdx} = \frac{1}{3}\tan^{3}x + \tan x + C$$

</td>
</tr>
<tr>
<td>

$$\left( \csc x \right)' = - \frac{\cos x}{\sin^{2}x} = - \frac{1}{\sin x\tan x} = - {\csc x\cot}x$$

</td>
<td>

$$\int_{}^{}{\csc x\cot xdx} = - \csc x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\csc xdx} = \ln{\left| \tan\frac{x}{2} \right|\ } + C = \ln\left| \csc x - \cot x \right| + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\csc^{2}xdx} = - \cot x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\csc^{3}xdx} = \frac{1}{2}\left( - \csc x\cot x + \ln\left| \csc x - \cot x \right| \right)$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\csc^{4}xdx} = - \frac{1}{3}\cot^{3}x - \cot x + C$$

</td>
</tr>
<tr>
<td>

反三角函数

</td>
<td></td>
</tr>
<tr>
<td>

$$\left( \arcsin x \right)' = \frac{1}{\sqrt{1 - x^{2}}}$$

</td>
<td>

$$\int_{}^{}{\frac{1}{\sqrt{a^{2} - x^{2}}}dx} = \arcsin\frac{x}{a} + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\arcsin xdx} = x\arcsin x + \sqrt{1 - x^{2}} + C$$

</td>
</tr>
<tr>
<td>

$$\left( \arccos x \right)' = - \frac{1}{\sqrt{1 - x^{2}}}$$

</td>
<td>

$$\int_{}^{}{- \frac{dx}{\sqrt{1 - x^{2}}}} = \arccos x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\arccos xdx} = x\arccos x - \sqrt{1 - x^{2}} + C$$

</td>
</tr>
<tr>
<td>

$$\left( \arctan x \right)' = \frac{1}{1 + x^{2}}$$

</td>
<td>

$$\int_{}^{}\frac{dx}{a^{2} + x^{2}} = \frac{1}{a}\arctan\frac{x}{a} + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\arctan xdx} = x\arctan x - \frac{1}{2}\ln\left( 1 + x^{2} \right) + C$$

</td>
</tr>
<tr>
<td>

$$\left( {arccot}x \right)' = - \frac{1}{1 + x^{2}}$$

</td>
<td>

$$\int_{}^{}{- \frac{dx}{1 + x^{2}}} = {arccot}x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\,{arccot}xdx\,} = x{arccot}x + \frac{1}{2}\ln\left( 1 + x^{2} \right) + C$$

</td>
</tr>
<tr>
<td>

$$\left( {arcsec}x \right)' = \frac{1}{|x|\sqrt{x^{2} - 1}}$$

</td>
<td>

$$\int_{}^{}\frac{dx}{|x|\sqrt{x^{2} - 1}} = {arcsec}x + C$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\,{arcsec}xdx\,} = x{arcsec}x - \ln\left( x + \sqrt{x^{2} - 1} \right) + C$$

</td>
</tr>
<tr>
<td>

$$\left( {arccot}x \right)' = - \frac{1}{|x|\sqrt{x^{2} - 1}}$$

</td>
<td>

$$\int_{}^{}{- \frac{dx}{|x|\sqrt{x^{2} - 1}}} = \left( {arccot}x \right)'$$

</td>
</tr>
<tr>
<td></td>
<td>

+------------------------------------------------------------------------------------------------------------------------------------------------

</td>
</tr>
<tr>
<td></td>
<td>

$$\int_{}^{}{\,{arccsc}xdx\,} = x{arccsc}x + \ln\left( x + \sqrt{x^{2} - 1} \right) + C$$

</td>
</tr>
<tr>
<td>

双曲函数

</td>
<td></td>
</tr>
<tr>
<td>

$$\left( \sinh x \right)' = \cosh x$$

</td>
<td>

$$\int_{}^{}{\,{sinh}xdx\,} = \cosh x + C$$

</td>
</tr>
<tr>
<td>

$$\left( \cosh x \right)' = \sinh x$$

</td>
<td>

$$\int_{}^{}{\cosh xdx} = \sinh x + C$$

</td>
</tr>
<tr>
<td>

$$\left( \tanh x \right)' = \frac{1}{\cosh^{2}x}$$

</td>
<td>

$$\int_{}^{}\frac{dx}{\cosh^{2}x} = \tanh x + C$$

</td>
</tr>
<tr>
<td>

$$\left( \coth x \right)' = - {csch}^{2}x$$

</td>
<td></td>
</tr>
<tr>
<td>

$$\left( {sech}x \right)' = - \tanh x{sech}x$$

</td>
<td></td>
</tr>
<tr>
<td>

$$\left( {csch}x \right)' = - \coth x{csch}x$$

</td>
<td></td>
</tr>
<tr>
<td>

反双曲函数

</td>
<td></td>
</tr>
<tr>
<td>

$$\left( {arsh}x \right)' = \frac{1}{\sqrt{1 + x^{2}}}$$

</td>
<td>

$$\int_{}^{}{\frac{1}{\sqrt{1 + x^{2}}}dx} = {arsh}x + C$$

</td>
</tr>
<tr>
<td>

$$\left( {arch}x \right)' = \frac{1}{\sqrt{x^{2} - 1}}$$

</td>
<td>

$$\int_{}^{}{\frac{1}{\sqrt{x^{2} - 1}}dx} = {arch}x + C$$

</td>
</tr>
<tr>
<td>

$$\left( {arth}x \right)' = \frac{1}{1 - x^{2}}$$

</td>
<td>

$$\int_{}^{}{\frac{1}{1 - x^{2}}dx} = {arth}x + C$$

</td>
</tr>
</tbody>
</table>
</div>

### 定积分

定义：设有常数$I$，如果对于任意给定的正数$\varepsilon$，总存在一个正数$\delta$，使得对于区间$\lbrack a\text{，}b\rbrack$的任何分法，不论$\xi_{i}$在$\left\lbrack x_{i - 1}\text{，}x_{i} \right\rbrack$中怎样选取，只要$\lambda = \max\left| \Delta x_{1}\text{，}\cdots \text{，}\Delta x_{n} \right| < \delta$，总有

$$\left| \sum_{i = 1}^{n}{f\left( \xi_{i} \right)\Delta x_{i}} - I \right| < \varepsilon$$

成立，那么称$I$是$f(x)$在区间$\lbrack a\text{，}b\rbrack$上的定积分，记作

$$I = \int_{a}^{b}{f(x)dx} = \lim_{\lambda \rightarrow 0}{\sum_{i = 1}^{n}{f\left( \xi_{i} \right)\Delta x_{i}}}$$

其中$f(x)$叫做被积函数，$f(x)dx$叫做被积表达式，$x$叫做积分变量，$a$叫做积分下限，$b$叫做积分上限，$\lbrack a\text{，}b\rbrack$叫做积分区间，$\sum_{i = 1}^{n}{f\left( \xi_{i} \right)\Delta x_{i}}$叫做积分和。

这里选用$\lambda \rightarrow 0$而非$n \rightarrow + \infty$是因为分法是任意的，只有$\lambda \rightarrow 0$才能保证所有的区间都是越来越小的，否则会出现某一区间恒定而其它区间缩小的情况。

### 定积分的性质

### 积分第一中值定理

设$f(x)\text{，}g(x)$和都在$\lbrack a\text{，}b\rbrack$上可积，$g(x)$在$\lbrack a\text{，}b\rbrack$上不变号，则存在$\eta \in \lbrack m\text{，}M\rbrack$，使得

$$\int_{a}^{b}{f(x)g(x)dx} = \eta\int_{a}^{b}{g(x)dx}$$

其中$M$和$m$分别表示$f(x)$在$\lbrack a\text{，}b\rbrack$的上确界和下确界。

特别地，若$f(x)$在$\lbrack a\text{，}b\rbrack$上连续，则存在$\xi \in \lbrack a\text{，}b\rbrack$，使得

$$\int_{a}^{b}{f(x)g(x)dx} = \eta\int_{a}^{b}{g(x)dx}$$

特别地，当若$f(x)$在$\lbrack a\text{，}b\rbrack$上连续，$g(x) \equiv 1$，则存在$\xi \in \lbrack a\text{，}b\rbrack$（其实$\xi \in (a\text{，}b)$即可），使得（积分中值公式）

$$\int_{a}^{b}{f(x)dx} = f(\xi)(b - a)$$

### 积分上限函数

$$\int_{a}^{x}{f(t)dt}$$

有如下结论

$$\frac{d}{dx}\int_{a}^{x}{f(t)dt} = f(x)\text{，}x \in \lbrack a\text{，}b\rbrack$$

$$\frac{d}{dx}\int_{a}^{g(x)}{f(t)dt} = f\left\lbrack g(x) \right\rbrack g'(x)$$

$$\frac{d}{dx}\int_{h(x)}^{g(x)}{f(t)dt} = f\left\lbrack g(x) \right\rbrack g'(x) - f\left\lbrack h(x) \right\rbrack h'(x)$$

$$\frac{d}{dx}\int_{h(x)}^{g(x)}{f(x\text{，}t)dt} = f\left\lbrack x\text{，}g(x) \right\rbrack g'(x) - f\left\lbrack x\text{，}h(x) \right\rbrack h'(x) + \int_{h(x)}^{g(x)}{\frac{\partial f(x\text{，}t)}{\partial x}dt}$$

微积分基本定理（Newton-Leibniz（牛顿---莱布尼兹）公式）

设$f(x)$在$\lbrack a\text{，}b\rbrack$上连续，$F(x)$是$f(x)$在$\lbrack a\text{，}b\rbrack$上的一个原函数，则

$$\int_{a}^{b}{f(x)dx} = F(b) - F(a) = F(x)\ \left| \begin{array}{r}
b \\
a
\end{array} \right.\ $$

有关定积分的证明题常用换元法，换元前可能需要拆分，换元有两种考虑，一种是考虑换元后的积分上限和积分下限，常用$t = \text{积分上限} - x$；另一种是考虑被积函数的性质，使得换元后函数括号内容与求证接近。

$$\text{区间再现公式：}\int_{a}^{b}{f(x)dx} = \int_{a}^{b}{f(a + b - x)dx}$$

$$\text{证明：}\int_{a}^{b}{f(a + b - x)dx}\overset{\ t = a + b - x\ }{\Rightarrow} - \int_{b}^{a}{f(t)dt} = \int_{a}^{b}{f(x)dx}$$

$$\text{常取}a = 0\text{，得}\int_{0}^{a}{f(x)dx} = \int_{0}^{a}{f(a - x)dx}$$

$$\cdot \int_{- a}^{a}{f(x)dx} = \int_{0}^{a}{\left\lbrack f(x) + f( - x) \right\rbrack dx}$$

$$\text{特别地，当}f(x)\text{是偶函数和奇函数时分别有}\int_{- a}^{a}{f(x)dx} = 2\int_{0}^{a}{f(x)dx}\text{，}\int_{- a}^{a}{f(x)dx} = 0$$

$$\text{证明：}\int_{- a}^{a}{f(x)dx} = \int_{- a}^{0}{f(x)dx} + \int_{0}^{a}{f(x)dx}\overset{\ t = - x\ }{\Rightarrow} - \int_{a}^{0}{f( - t)dt} + \int_{0}^{a}{f(x)dx} = \int_{0}^{a}{f( - x)dx} + \int_{0}^{a}{f(x)dx} = \int_{0}^{a}{\left\lbrack f(x) + f( - x) \right\rbrack dx}$$

$$\cdot \int_{0}^{\frac{\pi}{2}}{f\left( \sin x \right)dx} = \int_{0}^{\frac{\pi}{2}}{f\left( \cos x \right)dx}$$

$$\text{证明：}\int_{0}^{\frac{\pi}{2}}{f\left( \sin x \right)dx}\overset{\ \text{区间再现}\ }{\Rightarrow} = \int_{0}^{\frac{\pi}{2}}{f\left\lbrack \sin\left( \frac{\pi}{2} - x \right) \right\rbrack dx} = \int_{0}^{\frac{\pi}{2}}{f\left( \cos x \right)dx}$$

$$\cdot \int_{0}^{\pi}{xf\left( \sin x \right)dx} = \frac{\pi}{2}\int_{0}^{\pi}{f\left( \sin x \right)dx}$$

$$\text{证明：}\int_{0}^{\pi}{xf\left( \sin x \right)dx}\overset{\ \text{区间再现}\ }{\Rightarrow}\int_{0}^{\pi}{(\pi - x)f\left( \sin x \right)dx} = \pi\int_{0}^{\pi}{f\left( \sin x \right)dx} - \int_{0}^{\pi}{xf\left( \sin x \right)dx} \Rightarrow \int_{0}^{\pi}{xf\left( \sin x \right)dx} = \frac{\pi}{2}\int_{0}^{\pi}{f\left( \sin x \right)dx}$$

$$\cdot \int_{a}^{a + T}{f(x)dx} = \int_{0}^{T}{f(x)dx}$$

$$\text{证明：}\int_{a}^{a + T}{f(x)dx} = \int_{a}^{0}{f(x)dx} + \int_{0}^{T}{f(x)dx} + \int_{T}^{a + T}{f(x)dx}\overset{\ t = x - T\ }{\Rightarrow}\int_{a}^{0}{f(x)dx} + \int_{0}^{T}{f(x)dx} + \int_{0}^{a}{f(t + T)dt} = \int_{a}^{0}{f(x)dx} + \int_{0}^{T}{f(x)dx} - \int_{a}^{0}{f(x)dx} = \int_{0}^{T}{f(x)dx}$$

$$\text{证明：令}\Phi(a) = \int_{a}^{a + T}{f(x)dx}\text{，则}\Phi'(a) = \left\lbrack \int_{a}^{a + T}{f(x)dx} \right\rbrack' = f(a + T) - f(a) = 0$$

$$\text{所以}\Phi(a)\text{是一个常函数，可以取}\ \Phi(a) = \Phi(0) = \int_{0}^{T}{f(x)dx}\text{，即}\int_{a}^{a + T}{f(x)dx} = \int_{0}^{T}{f(x)dx}$$

$$\cdot \int_{a}^{a + nT}{f(x)dx} = n\int_{0}^{T}{f(x)dx}\ \ \left( n\mathbb{\in N} \right)$$

$$\text{证明：}\int_{a}^{a + nT}{f(x)dx} = \int_{a}^{a + T}{f(x)dx} + \int_{a + T}^{a + 2T}{f(x)dx} + \int_{a + 2T}^{a + 3T}{f(x)dx} + \cdots + \int_{a + (n - 1)T}^{a + nT}{f(x)dx} = n\int_{0}^{T}{f(x)dx}$$

$$\cdot I_{n} = \int_{0}^{\frac{\pi}{2}}{\sin^{n}xdx} = \int_{0}^{\frac{\pi}{2}}{\cos^{n}xdx} = \frac{n - 1}{n}I_{n - 2} = \left\{ \begin{array}{r}
\frac{n - 1}{n} \cdot \frac{n - 3}{n - 2} \cdot \cdots \cdot \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2}\text{，}n\text{为正偶数}\ \ \ \ \ \ \ \  \\
\frac{n - 1}{n} \cdot \frac{n - 3}{n - 2} \cdot \cdots \cdot \frac{4}{5} \cdot \frac{2}{3}\text{，}n\text{为大于}1\text{的奇数}
\end{array} \right.\ $$

$$\text{其中}I_{0} = \frac{\pi}{2}\text{，}I_{1} = 1$$

$$\text{证明：由}\int_{0}^{\frac{\pi}{2}}{f\left( \sin x \right)dx} = \int_{0}^{\frac{\pi}{2}}{f\left( \cos x \right)dx}\text{，得}\int_{0}^{\frac{\pi}{2}}{\sin^{n}xdx} = \int_{0}^{\frac{\pi}{2}}{\cos^{n}xdx}$$

$$I_{n} = - \int_{0}^{\frac{\pi}{2}}{\sin^{n}xd\left( \cos x \right)} = \left\lbrack - \cos x\sin^{n - 1}x \right\rbrack_{0}^{\frac{\pi}{2}} + (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n - 2}x\cos^{2}xdx} = (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n - 2}x\left( 1 - \sin^{2}x \right)dx} = (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n - 2}xdx} - (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n}xdx} = (n - 1)I_{n - 2} - (n - 1)I_{n}$$

得到递推式

$$I_{n} = \frac{n - 1}{n}I_{n - 2}$$

对$n$的奇偶分类讨论即可。

$$\cdot \int_{0}^{1}{x^{m}(1 - x)^{n}dx} = \int_{0}^{1}{x^{n}(1 - x)^{m}dx}\ \ \left( m\text{，}n\mathbb{\in Z} \right)$$

$$\text{证明：}\int_{0}^{1}{x^{m}(1 - x)^{n}dx}\overset{t = 1 - x}{\Rightarrow} - \int_{1}^{0}{(1 - t)^{m}t^{n}dt} = \int_{0}^{1}{(1 - x)^{m}x^{n}dx}$$

$$\cdot \int_{\frac{n}{2}\pi}^{\frac{n + 1}{2}\pi}{f\left( \left| \sin x \right| \right)dx} = \int_{\frac{n}{2}\pi}^{\frac{n + 1}{2}\pi}{f\left( \left| \cos x \right| \right)dx} = \int_{0}^{\frac{\pi}{2}}{f(\sin x)dx}$$

$$\int_{\frac{n}{2}\pi}^{\frac{n + 1}{2}\pi}{f\left( \left| \sin x \right| \right)dx}\overset{t = x + \frac{\pi}{2}}{\Rightarrow}$$

$$\int_{a}^{b}{\frac{f(x)}{f(a + b - x) + f(x)}dx} = \frac{b - a}{2}$$

$$\left( \int_{a}^{b}{f(x)g(x)dx} \right)^{2} \leq \int_{a}^{b}{f^{2}(x)dx} \cdot \int_{a}^{b}{g^{2}(x)dx}$$

$$\left( \int_{a}^{b}{\left\lbrack f(x) + g(x) \right\rbrack^{2}dx} \right)^{\frac{1}{2}} \leq \left( \int_{a}^{b}{f^{2}(x)dx} \right)^{\frac{1}{2}} + \left( \int_{a}^{b}{g^{2}(x)dx} \right)^{\frac{1}{2}}$$

$$\int_{a}^{b}{f(x)dx} = - \int_{b}^{a}{f(x)dx}$$

$$\left| \int_{a}^{b}{f(x)dx} \right| \leq \int_{a}^{b}{\left| f(x) \right|dx}$$

### 定积分的近似计算

设$f(x)$在$\lbrack a\text{，}b\rbrack$连续，用分点$a = x_{0}x_{1}x_{2}\cdots x_{n} = b$将$\lbrack a\text{，}b\rbrack$分成n个长度相等的区间，每个小区间的长为

$$\Delta x = \frac{b - a}{n}$$

记$f\left( x_{i} \right) = y_{i}$

### 1.矩形法

$$\int_{a}^{b}{f(x)dx} \approx \frac{b - a}{n}\left( y_{1} + y_{2} + \cdots + y_{n} \right)$$

### 2.梯形法

$$\int_{a}^{b}{f(x)dx} \approx \frac{b - a}{n}\left( \frac{y_{0} + y_{n}}{2} + y_{1} + y_{2} + \cdots + y_{n} \right)$$

3.抛物线法（辛普森法）

$$\int_{a}^{b}{f(x)dx} \approx \frac{b - a}{3n}\left\lbrack y_{0} + y_{n} + 4\left( y_{1} + y_{3} + \cdots + y_{n - 1} \right) + 2(y_{2} + y_{4} + \cdots + y_{n - 2}) \right\rbrack$$

### 定积分的换元积分法

设$f(x)$在区间$\lbrack a\text{，}b\rbrack$上连续，$x = \varphi(t)$在$\lbrack\alpha \text{，}\beta\rbrack$或$\lbrack\beta \text{，}\alpha\rbrack$内有连续导数$\varphi'(x)$，$f(x)$在$R_{\varphi}$上连续，且满足$\varphi(\alpha) = a$和$\varphi(\beta) = b$，则

$$\int_{a}^{b}{f(x)dx} = \int_{\alpha}^{\beta}{f\left( \varphi(t) \right)\varphi'(t)dt}$$

### 定积分的分部积分法

$$\int_{a}^{b}{udv} = \lbrack uv\rbrack_{a}^{b} - \int_{a}^{b}{vdu}$$

### 极坐标下的定积分公式

$$S = \int_{\alpha}^{\beta}{\frac{1}{2}\left\lbrack \rho(\theta) \right\rbrack^{2}d\theta}$$

$\Gamma$函数（第二类欧拉积分）

$$\Gamma(s) = \int_{0}^{+ \infty}{e^{- x}x^{s - 1}dx}$$

性质

$$\Gamma(s + 1) = s\Gamma(s)\ \ (s > 0)$$

$$\Gamma(n + 1) = n!\ \ \left( n \in \mathbb{N}^{*} \right)$$

$$\Gamma(s)\Gamma(1 - s) = \frac{\pi}{\sin{\pi s}}\ \ (0 < s < 1)\ \ (\text{余元公式})\text{，特别地，}\Gamma\left( \frac{1}{2} \right) = \sqrt{\pi}$$

$$\Gamma\left( \frac{2k + 1}{2} \right) = \frac{1 \cdot 3 \cdot 5 \cdot \cdots \cdot (2k - 1)\sqrt{\pi}}{2^{k}}\text{，}k \in \mathbb{N}_{+}$$

$\beta$函数（第一类欧拉积分）

$$\beta(p\text{，}q) = \int_{0}^{1}{x^{p - 1}(1 - x)^{q - 1}dx}\ \ \left( p\text{，}q \in \mathbb{N}^{*} \right)$$

性质

$$\beta(p\text{，}q) = \beta(q\text{，}p)$$

$$\beta(p\text{，}q) = \left\{ \begin{array}{r}
\frac{q - 1}{p + q - 1}\beta(p\text{，}q - 1)\ \ (p > 0\text{，}q > 1)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\frac{p - 1}{p + q - 1}\beta(p - 1\text{，}q)\ \ (p > 1\text{，}q > 0)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\frac{(p - 1)(q - 1)}{(p + q - 1)(p + q - 2)}\beta(p - 1\text{，}q - 1)\ \ (p\text{，}q > 1)
\end{array} \right.\ $$

$$\beta(p\text{，}q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p + q)}$$

$$\beta(p\text{，}1 - p) = \Gamma(p)\Gamma(1 - p)$$

$$\beta(p\text{，}q) = \frac{p + q}{pqC_{p + q}^{p}} = \frac{1}{qC_{p + q + 1}^{p - 1}}\ \ \left( p\text{，}q \in \mathbb{N}^{*} \right)$$

其它

### 反常积分

$$\int_{a}^{b}\frac{dx}{(x - a)^{q}} = \frac{(b - a)^{1 - q}}{1 - - q}\ \ 0 < q < 1$$

### 比较审敛原理

$\text{在此处键入公式。}$

### 定积分的元素法

一般地，如果某一实际问题中的所求量$U$符合下列条件：

（1）$U$是与一个变量$x$的变化区间$\lbrack a\text{，}b\rbrack$有关的量

（2）$U$对于区间$\lbrack a\text{，}b\rbrack$具有可加性，就是说，如果把区间$\lbrack a\text{，}b\rbrack$分成许多部分区间，则$U$相应地分成许多部分量，而$U$等于所有部分量之和。

（3）部分量$\Delta U_{i}$的近似值可表示为$f\left( \xi_{i} \right)\Delta x_{i}$，那么就可考虑用定积分来表达这个量$U$。通常写出这个量$U$的积分表达式的步骤是：

1）根据问题的具体情况，选取一个变量例如$x$为积分变量，并确定它的变化区间$\lbrack a\text{，}b\rbrack$；

2）设想把区间$\lbrack a\text{，}b\rbrack$分成$n$个小区间，取其中任一小区间$\lbrack x\text{，}x + dx\rbrack$并记作，求出相应于这个小区间的部分量$\Delta U$的近似值。如果$\Delta U$能近似地表示为$\lbrack a\text{，}b\rbrack$上的一个连续函数在$x$处的值$f(x)$与$dx$的乘积，就把$f(x)dx$称为量$U$的元素且记作$dU$，即

$$dU = f(x)dx$$

3）以所求量$U$的元素$f(x)dx$为被积表达式，在区间$\lbrack a\text{，}b\rbrack$上作定积分，得

$$U = \int_{a}^{b}{f(x)dx}$$

这就是所求量$U$的积分表达式。

### 平面图形的面积

### 旋转体的面积

### 平面曲线的弧长

$$s = \int_{a}^{b}{\sqrt{1 + {y'}^{2}}dx}$$

若

$$\left\{ \begin{array}{r}
x = \rho(\theta)\cos\theta \\
y = \rho(\theta)\sin\theta
\end{array} \right.\ $$

则

$$s = \int_{a}^{b}{\sqrt{\rho^{2}(\theta) + {\rho'}^{2}(\theta)}d\theta}$$
