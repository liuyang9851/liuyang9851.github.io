---
title: 定积分及其应用
description: 定积分的定义与性质、积分第一中值定理、积分上限函数、定积分的换元与分部积分法、极坐标下的定积分、定积分的近似计算、定积分的元素法及其应用（平面图形面积、旋转体、平面曲线弧长）。
---

# 定积分及其应用

[[toc]]

积分

不定积分

定义：在区间I上，函数f(x)的带有任意常数项的原函数F(x) + C称为f(x)（或f(x)dx）在区间I上的不定积分，记作

∫f(x)dx = F(x) + C

第一换元积分法

∫f[φ(x)]φ′(x)dx = [∫f(u)du]u = φ(x)

特别地

∫af(x)dx = ∫f(x)d(ax + b)

$$eg.\int_{}^{}\frac{dx}{x\ln x} = \int_{}^{}{\frac{1}{\ln x}d\ln x} = \ln\left| \ln x \right| + C$$

第二换元积分法

∫f(x)dx = [∫f(ψ(t))ψ′(t)dt]t = ψ−1(x)

分部积分法

∫uv′dx = uv − ∫u′vdx 或 ∫udv = uv − ∫vdu

证明：由[u(x)v(x)]′ = u′(x)v(x) + u(x)v′(x)，有

$$\frac{duv}{dx} = v\frac{du}{dx} + u\frac{dv}{dx}$$

等式两边同乘dx，得

duv = vdu + udv

两边积分，即得

uv = ∫duv = ∫vdu + ∫udv

$$eg.\int_{}^{}{\ln xdx} = x\ln x - \int_{}^{}{xd\ln x} = x\ln x - \int_{}^{}{x \cdot \frac{1}{x}dx} = x\ln x - x + C$$

eg.∫x2exdx = ∫x2dex = x2ex − ∫exdx2 = x2ex − ∫2xexdx

又∫2xexdx = 2∫xexdx = 2xex − 2∫exdx = 2xex − 2ex + C

故∫x2exdx = x2ex − 2xex + 2ex + C

留在前面的优先级：反对幂三指（反三角函数，对数函数，幂函数，三角函数，指数函数，ex）

分部积分法亦有如下公式

∫uvdw = uvw − ∫uwdv − ∫vwdu

有理函数的积分

$$\text{两个多项式的商}\frac{P(x)}{Q(x)}\text{称为有理函数，又称有理分式。当}P(x)\text{的次数小于}Q(x)\text{的次数时，称这有理分式为}$$

真分式，否则称为假分式。可以将一个假分式转化成一个多项式与一个真分式的和的形式。

由代数数论的知识可以证明，可以把Q(x)按如下形式分解：

$$Q(x) = \prod_{k = 1}^{i}\left( x - \alpha_{k} \right)^{m_{k}} \cdot \prod_{k = 1}^{j}\left( x^{2} + 2\xi_{k}x + \eta_{k}^{2} \right)^{n_{k}}$$

意思是可以把Q(x)分解成若干个一次多项式和二次多项式的积。

$$\text{可以证明真分式}\frac{P(x)}{Q(x)}\text{可以被按如下方式分解}$$

$$\frac{P(x)}{Q(x)} = \sum_{k = 1}^{i}{\sum_{r = 1}^{m_{k}}\frac{\lambda_{kr}}{\left( x - \alpha_{k} \right)^{r}}} + \sum_{k = 1}^{j}{\sum_{r = 1}^{n_{k}}\frac{\mu_{kr}x + \nu_{kr}}{\left( x^{2} + 2\xi_{k}x + \eta_{k}^{2} \right)^{n_{k}}}}$$

其中α，λ，μ，ν，ξ，η是任意实数，i，j，k，m，n，r是正整数。

举例说明（大写字母代表待定的实数系数）

$$1.\frac{4x^{3} - 13x^{2} + 3x + 8}{(x + 1)(x - 2)(x - 1)^{2}} = \frac{A}{x + 1} + \frac{B}{x - 2} + \frac{C}{x - 1} + \frac{D}{(x - 1)^{2}}$$

$$2.\frac{x^{4} + x^{3} + 3x^{2} - 1}{\left( x^{2} + 1 \right)^{2}(x - 1)} = \frac{A}{x - 1} + \frac{Bx + C}{x^{2} + 1} + \frac{Dx + E}{\left( x^{2} + 1 \right)^{2}}$$

$$3.\frac{1}{(x + 1)^{2}\left( x^{2} - 2x + 3 \right)^{3}} = \frac{A}{x + 1} + \frac{B}{(x + 1)^{2}} + \frac{Cx + D}{x^{2} - 2x + 3} + \frac{Ex + F}{\left( x^{2} - 2x + 3 \right)^{2}} + \frac{Gx + H}{\left( x^{2} - 2x + 3 \right)^{3}}$$

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

4x3 − 13x2 + 3x + 8 = A(x − 2)(x − 1)2 + B(x + 1)(x − 1)2 + C(x + 1)(x − 2)(x − 1) + D(x + 1)(x − 2)

常用导数与积分表（C为任意常数）

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

导数求导法则

</td>
<td>

常用积分法则

</td>
</tr>
<tr>
<td>

(u ± v)′ = u′ ± v′

</td>
<td>

∫(u + v)dx = ∫udx + ∫vdx

</td>
</tr>
<tr>
<td>

(Cu)′ = Cu′

</td>
<td>

∫kudx = k∫udx  （k是常数）

</td>
</tr>
<tr>
<td>

(uv)′ = u′v + iv′

</td>
<td>

∫udv = uv − ∫vdu

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

$${f_{x}^{- 1}}'(x) = \frac{1}{f_{y}'(y)}\text{或}\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}}$$

</td>
<td></td>
</tr>
<tr>
<td>

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

或

yx′ = yu′ ⋅ ux′

</td>
<td>

∫f[φ(x)]φ′(x)dx = [∫f(u)du]u = φ(x)

</td>
</tr>
<tr>
<td>

∫f(x)dx = [∫f(ψ(t))ψ′(t)dt]t = ψ−1(x)

</td>
</tr>
<tr>
<td>

非三角函数类函数

</td>
</tr>
<tr>
<td>

(C)′ = 0

</td>
<td>

∫kdx = kx + C  （k ≠ 0）

</td>
</tr>
<tr>
<td>

(xμ)′ = μxμ − 1

</td>
<td>

$$\int_{}^{}{x^{\mu}dx} = \frac{x^{\mu + 1}}{\mu + 1} + C\ \ (\mu \neq - 1)$$

</td>
</tr>
<tr>
<td>

(ax)′ = axln a  (a > 0，a ≠ 1)

</td>
<td>

$$\int_{}^{}{a^{x}dx} = \frac{a^{x}}{\ln a} + C$$

</td>
</tr>
<tr>
<td>

(ex)′ = ex

</td>
<td>

∫exdx = ex + C

</td>
</tr>
<tr>
<td>

$$\left( \log_{a}x \right)' = \frac{1}{x\ln a}\ \ (a > 0\text{，}a \neq 1)$$

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
<td>

∫ln xdx = xln x − x + C

</td>
</tr>
<tr>
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
<td>

$$\int_{}^{}{\sqrt{a^{2} - x^{2}}dx} = \frac{a^{2}}{2}\arcsin\frac{x}{a} + \frac{1}{2}x\sqrt{a^{2} - x^{2}} + C$$

</td>
</tr>
<tr>
<td>

$$\int_{}^{}\frac{dx}{\sqrt{x^{2} + a^{2}}} = \ln\left( x + \sqrt{x^{2} + a^{2}} \right) + C$$

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\sqrt{x^{2} + a^{2}}dx} = \frac{1}{2}\left( x\sqrt{x^{2} + a^{2}} + a^{2}\ln\left| x + \sqrt{x^{2} + a^{2}} \right| \right) + C$$

</td>
</tr>
<tr>
<td>

$$\int_{}^{}\frac{dx}{\sqrt{x^{2} - a^{2}}} = \ln\left| x + \sqrt{x^{2} - a^{2}} \right| + C$$

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\sqrt{x^{2} - a^{2}}dx} = \frac{1}{2}\left( x\sqrt{x^{2} - a^{2}} - a^{2}\ln\left| x + \sqrt{x^{2} - a^{2}} \right| \right) + C$$

</td>
</tr>
<tr>
<td>

三角函数

</td>
</tr>
<tr>
<td>

(sin x)′ = cos x

</td>
<td>

∫sin xdx = −cos x + C

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\sin^{2}xdx} = \frac{1}{2}x - \frac{1}{4}\sin{2x} + C$$

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\sin^{3}xdx} = - \cos x + \frac{1}{3}\cos^{3}x + C$$

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\sin^{4}xdx} = \frac{3}{8}x - \frac{1}{4}\sin{2x} + \frac{1}{32}\sin{4x} + C$$

</td>
</tr>
<tr>
<td>

$$I_{n} = \int_{}^{}{\sin^{n}xdx} = - \frac{1}{n}\sin^{n - 1}x\cos x + \frac{n - 1}{n}I_{n - 2}$$

</td>
</tr>
<tr>
<td>

(cos x)′ = −sin x

</td>
<td>

∫cos xdx = sin x + C

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\cos^{2}xdx} = \frac{1}{2}x + \frac{1}{4}\sin{2x} + C$$

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\cos^{3}xdx} = \sin x - \frac{1}{3}\sin^{3}x + C$$

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\cos^{4}xdx} = \frac{3}{8}x + \frac{1}{4}\sin{2x} + \frac{1}{32}\sin{4x} + C$$

</td>
</tr>
<tr>
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
<td>

∫tan xdx = −ln |cos x| + C

</td>
</tr>
<tr>
<td>

∫tan2xdx = tan x − x + C

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\tan^{3}xdx} = \frac{1}{2}\tan^{2}x + \ln\left| \cos x \right| + C$$

</td>
</tr>
<tr>
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
<td>

∫cot xdx = ln |sin x| + C

</td>
</tr>
<tr>
<td>

∫cot2xdx = −cot x − x + C

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\cot^{3}xdx} = - \frac{1}{2}\cot^{2}x - \ln\left| \sin x \right| + C$$

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\cot^{4}xdx} = - \frac{1}{3}\cot^{3}x + \cot x + x + C$$

</td>
</tr>
<tr>
<td>

$$\left( \sec x \right)' = \frac{\tan x}{\cos x} = \sec x\tan x$$

</td>
<td>

∫sec xtan xdx = sec x + C

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\sec xdx} = \ln\left| \tan\left( \frac{\pi}{4} + \frac{x}{2} \right) \right| + C = \ln\left| \sec x + \tan x \right| + C$$

</td>
</tr>
<tr>
<td>

∫sec2xdx = tan x + C

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\sec^{3}xdx} = \frac{1}{2}\left( \sec x\tan x + \ln\left| \sec x + \tan x \right| \right) + C$$

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\sec^{4}xdx} = \frac{1}{3}\tan^{3}x + \tan x + C$$

</td>
</tr>
<tr>
<td>

$$\left( \csc x \right)' = - \frac{\cos x}{\sin^{2}x} = - \frac{1}{\sin x\tan x} = - {\csc x\cot}x$$

</td>
<td>

∫csc xcot xdx = −csc x + C

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\csc xdx} = \ln{\left| \tan\frac{x}{2} \right|\ } + C = \ln\left| \csc x - \cot x \right| + C$$

</td>
</tr>
<tr>
<td>

∫csc2xdx = −cot x + C

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\csc^{3}xdx} = \frac{1}{2}\left( - \csc x\cot x + \ln\left| \csc x - \cot x \right| \right)$$

</td>
</tr>
<tr>
<td>

$$\int_{}^{}{\csc^{4}xdx} = - \frac{1}{3}\cot^{3}x - \cot x + C$$

</td>
</tr>
<tr>
<td>

反三角函数

</td>
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
<td>

$$\int_{}^{}{\,{arccot}xdx} = x{arccot}x + \frac{1}{2}\ln\left( 1 + x^{2} \right) + C$$

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
<td>

$$\int_{}^{}{\,{arcsec}xdx} = x{arcsec}x - \ln\left( x + \sqrt{x^{2} - 1} \right) + C$$

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
<td>

$$\int_{}^{}{\,{arccsc}xdx} = x{arccsc}x + \ln\left( x + \sqrt{x^{2} - 1} \right) + C$$

</td>
</tr>
<tr>
<td>

双曲函数

</td>
</tr>
<tr>
<td>

(sinh x)′ = cosh x

</td>
<td>

∫sinhxdx = cosh x + C

</td>
</tr>
<tr>
<td>

(cosh x)′ = sinh x

</td>
<td>

∫cosh xdx = sinh x + C

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

(coth x)′ = −csch2x

</td>
<td></td>
</tr>
<tr>
<td>

(sechx)′ = −tanh xsechx

</td>
<td></td>
</tr>
<tr>
<td>

(cschx)′ = −coth xcschx

</td>
<td></td>
</tr>
<tr>
<td>

反双曲函数

</td>
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
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

定积分

定义：设有常数I，如果对于任意给定的正数ε，总存在一个正数δ，使得对于区间[a，b]的任何分法，不论ξi在[xi − 1，xi]中怎样选取，只要λ = max |Δx1，⋯，Δxn| < δ，总有

$$\left| \sum_{i = 1}^{n}{f\left( \xi_{i} \right)\Delta x_{i}} - I \right| < \varepsilon$$

成立，那么称I是f(x)在区间[a，b]上的定积分，记作

$$I = \int_{a}^{b}{f(x)dx} = \lim_{\lambda \rightarrow 0}{\sum_{i = 1}^{n}{f\left( \xi_{i} \right)\Delta x_{i}}}$$

其中f(x)叫做被积函数，f(x)dx叫做被积表达式，x叫做积分变量，a叫做积分下限，b叫做积分上限，[a，b]叫做积分区间，$\sum_{i = 1}^{n}{f\left( \xi_{i} \right)\Delta x_{i}}$叫做积分和。

这里选用λ → 0而非n → +∞是因为分法是任意的，只有λ → 0才能保证所有的区间都是越来越小的，否则会出现某一区间恒定而其它区间缩小的情况。

定积分的性质

积分第一中值定理

设f(x)，g(x)和都在[a，b]上可积，g(x)在[a，b]上不变号，则存在η ∈ [m，M]，使得

∫abf(x)g(x)dx = η∫abg(x)dx

其中M和m分别表示f(x)在[a，b]的上确界和下确界。

特别地，若f(x)在[a，b]上连续，则存在ξ ∈ [a，b]，使得

∫abf(x)g(x)dx = η∫abg(x)dx

特别地，当若f(x)在[a，b]上连续，g(x) ≡ 1，则存在ξ ∈ [a，b]（其实ξ ∈ (a，b)即可），使得（积分中值公式）

∫abf(x)dx = f(ξ)(b − a)

积分上限函数

∫axf(t)dt

有如下结论

$$\frac{d}{dx}\int_{a}^{x}{f(t)dt} = f(x)\text{，}x \in \lbrack a\text{，}b\rbrack$$

$$\frac{d}{dx}\int_{a}^{g(x)}{f(t)dt} = f\left( \left\lbrack g(x) \right\rbrack' \right)$$

$$\frac{d}{dx}\int_{h(x)}^{g(x)}{f(t)dt} = f\left( \left\lbrack g(x) \right\rbrack' \right) - f\left( \left\lbrack h(x) \right\rbrack' \right)$$

微积分基本定理（Newton-Leibniz（牛顿—莱布尼兹）公式）

设f(x)在[a，b]上连续，F(x)是f(x)在[a，b]上的一个原函数，则

$$\int_{a}^{b}{f(x)dx} = F(b) - F(a) = F(x)\ \left| \begin{array}{r}
b \\
a
\end{array} \right.\ $$

有关定积分的证明题常用换元法，换元前可能需要拆分，换元有两种考虑，一种是考虑换元后的积分上限和积分下限，常用t = 积分上限 − x；另一种是考虑被积函数的性质，使得换元后函数括号内容与求证接近。

⋅∫abf(x)dx = ∫abf(a + b − x)dx

$$\text{证明：}\int_{a}^{b}{f(a + b - x)dx}\overset{\ t = a + b - x\ }{\Rightarrow} - \int_{b}^{a}{f(t)dt} = \int_{a}^{b}{f(x)dx}$$

⋅∫−aaf(x)dx = ∫0a[f(x) + f(−x)]dx

特别地，当f(x)是偶函数和奇函数时分别有∫−aaf(x)dx = 2∫0af(x)dx，∫−aaf(x)dx = 0

$$\text{证明：}\int_{- a}^{a}{f(x)dx} = \int_{- a}^{0}{f(x)dx} + \int_{0}^{a}{f(x)dx}\overset{\ t = - x\ }{\Rightarrow} - \int_{a}^{0}{f( - t)dt} + \int_{0}^{a}{f(x)dx} = \int_{0}^{a}{f( - x)dx} + \int_{0}^{a}{f(x)dx} = \int_{0}^{a}{\left\lbrack f(x) + f( - x) \right\rbrack dx}$$

$$\cdot \int_{0}^{\frac{\pi}{2}}{f\left( \sin x \right)dx} = \int_{0}^{\frac{\pi}{2}}{f\left( \cos x \right)dx}$$

$$\text{证明：}\int_{0}^{\frac{\pi}{2}}{f\left( \sin x \right)dx}\overset{\ t = \frac{\pi}{2} - x\ }{\Rightarrow} - \int_{\frac{\pi}{2}}^{0}{f\left\lbrack \sin\left( \frac{\pi}{2} - t \right) \right\rbrack dt} = \int_{0}^{\frac{\pi}{2}}{f\left( \cos t \right)dt} = \int_{0}^{\frac{\pi}{2}}{f\left( \cos x \right)dx}$$

$$\cdot \int_{0}^{\pi}{xf\left( \sin x \right)dx} = \frac{\pi}{2}\int_{0}^{\pi}{f\left( \sin x \right)dx}$$

$$\text{证明：}\int_{0}^{\pi}{xf\left( \sin x \right)dx}\overset{\ t = \pi - x\ }{\Rightarrow} - \int_{\pi}^{0}{(\pi - t)f\left\lbrack \sin(\pi - t) \right\rbrack dt} = \int_{0}^{\pi}{(\pi - t)f\left( \sin t \right)dt} = \pi\int_{0}^{\pi}{f\left( \sin x \right)dx} - \int_{0}^{\pi}{xf\left( \sin x \right)dx} \Rightarrow \int_{0}^{\pi}{xf\left( \sin x \right)dx} = \frac{\pi}{2}\int_{0}^{\pi}{f\left( \sin x \right)dx}$$

⋅∫aa + Tf(x)dx = ∫0Tf(x)dx

$$\text{证明：}\int_{a}^{a + T}{f(x)dx} = \int_{a}^{0}{f(x)dx} + \int_{0}^{T}{f(x)dx} + \int_{T}^{a + T}{f(x)dx}\overset{\ t = x - T\ }{\Rightarrow}\int_{a}^{0}{f(x)dx} + \int_{0}^{T}{f(x)dx} + \int_{0}^{a}{f(t + T)dt} = \int_{a}^{0}{f(x)dx} + \int_{0}^{T}{f(x)dx} - \int_{a}^{0}{f(x)dx} = \int_{0}^{T}{f(x)dx}$$

证明：令Φ(a) = ∫aa + Tf(x)dx，则Φ′(a) = [∫aa + Tf(x)dx]′ = f(a + T) − f(a) = 0

所以Φ(a)是一个常函数，可以取 Φ(a) = Φ(0) = ∫0Tf(x)dx，即∫aa + Tf(x)dx = ∫0Tf(x)dx

⋅∫aa + nTf(x)dx = n∫0Tf(x)dx  (n ∈ ℕ)

证明：∫aa + nTf(x)dx = ∫aa + Tf(x)dx + ∫a + Ta + 2Tf(x)dx + ∫a + 2Ta + 3Tf(x)dx + ⋯ + ∫a + (n − 1)Ta + nTf(x)dx = n∫0Tf(x)dx

$$\cdot I_{n} = \int_{0}^{\frac{\pi}{2}}{\sin^{n}xdx} = \int_{0}^{\frac{\pi}{2}}{\cos^{n}xdx} = \frac{n - 1}{n}I_{n - 2} = \left\{ \begin{array}{r}
\frac{n - 1}{n} \cdot \frac{n - 3}{n - 2} \cdot \cdots \cdot \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2}\text{，}n\text{为正偶数}\ \ \ \ \ \ \ \  \\
\frac{n - 1}{n} \cdot \frac{n - 3}{n - 2} \cdot \cdots \cdot \frac{4}{5} \cdot \frac{2}{3}\text{，}n\text{为大于}1\text{的奇数}
\end{array} \right.\ $$

$$\text{其中}I_{0} = \frac{\pi}{2}\text{，}I_{1} = 1$$

$$\text{证明：由}\int_{0}^{\frac{\pi}{2}}{f\left( \sin x \right)dx} = \int_{0}^{\frac{\pi}{2}}{f\left( \cos x \right)dx}\text{，得}\int_{0}^{\frac{\pi}{2}}{\sin^{n}xdx} = \int_{0}^{\frac{\pi}{2}}{\cos^{n}xdx}$$

$$I_{n} = - \int_{0}^{\frac{\pi}{2}}{\sin^{n}xd\left( \cos x \right)} = \left\lbrack - \cos x\sin^{n - 1}x \right\rbrack_{0}^{\frac{\pi}{2}} + (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n - 2}x\cos^{2}xdx} = (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n - 2}x\left( 1 - \sin^{2}x \right)dx} = (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n - 2}xdx} - (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n}xdx} = (n - 1)I_{n - 2} - (n - 1)I_{n}$$

得到递推式

$$I_{n} = \frac{n - 1}{n}I_{n - 2}$$

对n的奇偶分类讨论即可。

⋅∫01xm(1 − x)ndx = ∫01xn(1 − x)mdx  (m，n ∈ ℤ)

$$\text{证明：}\int_{0}^{1}{x^{m}(1 - x)^{n}dx}\overset{t = 1 - x}{\Rightarrow} - \int_{1}^{0}{(1 - t)^{m}t^{n}dt} = \int_{0}^{1}{(1 - x)^{m}x^{n}dx}$$

$$\cdot \int_{\frac{n}{2}\pi}^{\frac{n + 1}{2}\pi}{f\left( \left| \sin x \right| \right)dx} = \int_{\frac{n}{2}\pi}^{\frac{n + 1}{2}\pi}{f\left( \left| \cos x \right| \right)dx} = \int_{0}^{\frac{\pi}{2}}{f(\sin x)dx}$$

$$\int_{\frac{n}{2}\pi}^{\frac{n + 1}{2}\pi}{f\left( \left| \sin x \right| \right)dx}\overset{t = x + \frac{\pi}{2}}{\Rightarrow}$$

$$\int_{a}^{b}{\frac{f(x)}{f(a + b - x) + f(x)}dx} = \frac{b - a}{2}$$

(∫abf(x)g(x)dx)2 ≤ ∫abf2(x)dx ⋅ ∫abg2(x)dx

$$\left( \int_{a}^{b}{\left\lbrack f(x) + g(x) \right\rbrack^{2}dx} \right)^{\frac{1}{2}} \leq \left( \int_{a}^{b}{f^{2}(x)dx} \right)^{\frac{1}{2}} + \left( \int_{a}^{b}{g^{2}(x)dx} \right)^{\frac{1}{2}}$$

∫abf(x)dx = −∫baf(x)dx

|∫abf(x)dx| ≤ ∫ab|f(x)|dx

定积分的近似计算

设f(x)在[a，b]连续，用分点a = x0x1x2⋯xn = b将[a，b]分成n个长度相等的区间，每个小区间的长为

$$\Delta x = \frac{b - a}{n}$$

记f(xi) = yi

1.矩形法

$$\int_{a}^{b}{f(x)dx} \approx \frac{b - a}{n}\left( y_{1} + y_{2} + \cdots + y_{n} \right)$$

2.梯形法

$$\int_{a}^{b}{f(x)dx} \approx \frac{b - a}{n}\left( \frac{y_{0} + y_{n}}{2} + y_{1} + y_{2} + \cdots + y_{n} \right)$$

3.抛物线法（辛普森法）

$$\int_{a}^{b}{f(x)dx} \approx \frac{b - a}{3n}\left\lbrack y_{0} + y_{n} + 4\left( y_{1} + y_{3} + \cdots + y_{n - 1} \right) + 2(y_{2} + y_{4} + \cdots + y_{n - 2}) \right\rbrack$$

定积分的换元积分法

设f(x)在区间[a，b]上连续，x = φ(t)在[α，β]或[β，α]内有连续导数φ′(x)，f(x)在Rφ上连续，且满足φ(α) = a和φ(β) = b，则

∫abf(x)dx = ∫abf(φ(t))φ′(t)dt

定积分的分部积分法

∫abudv = [uv]ab − ∫abvdu

极坐标下的定积分公式

$$S = \int_{\alpha}^{\beta}{\frac{1}{2}\left\lbrack \rho(\theta) \right\rbrack^{2}d\theta}$$

Γ函数（第二类欧拉积分）

Γ(s) = ∫0+∞e−xxs − 1dx

性质

Γ(s + 1) = sΓ(s)  (s > 0)

Γ(n + 1) = n!  (n ∈ ℕ*)

$$\Gamma(s)\Gamma(1 - s) = \frac{\pi}{\sin{\pi s}}\ \ (0 < s < 1)\ \ (\text{余元公式})\text{，特别地，}\Gamma\left( \frac{1}{2} \right) = \sqrt{\pi}$$

$$\Gamma\left( \frac{2k + 1}{2} \right) = \frac{1 \cdot 3 \cdot 5 \cdot \cdots \cdot (2k - 1)\sqrt{\pi}}{2^{k}}\text{，}k \in \mathbb{N}_{+}$$

β函数（第一类欧拉积分）

β(p，q) = ∫01xp − 1(1 − x)q − 1dx  (p，q ∈ ℕ*)

性质

β(p，q) = β(q，p)

$$\beta(p\text{，}q) = \left\{ \begin{array}{r}
\frac{q - 1}{p + q - 1}\beta(p\text{，}q - 1)\ \ (p > 0\text{，}q > 1)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\frac{p - 1}{p + q - 1}\beta(p - 1\text{，}q)\ \ (p > 1\text{，}q > 0)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\frac{(p - 1)(q - 1)}{(p + q - 1)(p + q - 2)}\beta(p - 1\text{，}q - 1)\ \ (p\text{，}q > 1)
\end{array} \right.\ $$

$$\beta(p\text{，}q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p + q)}$$

β(p，1 − p) = Γ(p)Γ(1 − p)

$$\beta(p\text{，}q) = \frac{p + q}{pqC_{p + q}^{p}} = \frac{1}{qC_{p + q + 1}^{p - 1}}\ \ \left( p\text{，}q \in \mathbb{N}^{*} \right)$$

其它

定积分的元素法

一般地，如果某一实际问题中的所求量U符合下列条件：

（1）U是与一个变量x的变化区间[a，b]有关的量

（2）U对于区间[a，b]具有可加性，就是说，如果把区间[a，b]分成许多部分区间，则U相应地分成许多部分量，而U等于所有部分量之和。

（3）部分量ΔUi的近似值可表示为f(ξi)Δxi，那么就可考虑用定积分来表达这个量U。通常写出这个量U的积分表达式的步骤是：

1）根据问题的具体情况，选取一个变量例如x为积分变量，并确定它的变化区间[a，b]；

2）设想把区间[a，b]分成n个小区间，取其中任一小区间[x，x + dx]并记作，求出相应于这个小区间的部分量ΔU的近似值。如果ΔU能近似地表示为[a，b]上的一个连续函数在x处的值f(x)与dx的乘积，就把f(x)dx称为量U的元素且记作dU，即

dU = f(x)dx

3）以所求量U的元素f(x)dx为被积表达式，在区间[a，b]上作定积分，得

U = ∫abf(x)dx

这就是所求量U的积分表达式。

平面图形的面积

旋转体的面积

平面曲线的弧长

$$s = \int_{a}^{b}{\sqrt{1 + {y'}^{2}}dx}$$
