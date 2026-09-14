---
title: 不定积分
description: 不定积分的定义、第一与第二换元积分法、分部积分法、有理函数的积分。
---

# 不定积分

[[toc]]

微分中值定律

Fermat（费马）引理

设x0是f(x)的一个极值点，且f(x)在x0处导数存在，则

f′(x0) = 0

证：设x0是f(x)的极大（小）值点，由极大（小）值点的定义，f(x)在x0的某个邻域O(x0，δ)上有定义，满足

f(x) ≤ f(x0)  （或f(x) ≥ f(x0)）

当x < x0时，有$\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \geq 0\ \ \left. \text{（或}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \leq 0 \right.\text{）}$；当x > x0时，有$\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \leq 0\ \ \left. \text{（或}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \geq 0 \right.\text{）}$。因为f(x)在x0可导，所以f′(x0) = f+′(x0) = f−′(x0)，又因为

$$f_{-}'\left( x_{0} \right) = \lim_{x \rightarrow x_{0}^{-}}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \geq 0\text{，}f_{+}'\left( x_{0} \right) = \lim_{x \rightarrow x_{0}^{+}}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \leq 0$$

$$\text{或}f_{-}'\left( x_{0} \right) = \lim_{x \rightarrow x_{0}^{-}}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \leq 0\text{，}f_{+}'\left( x_{0} \right) = \lim_{x \rightarrow x_{0}^{+}}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \geq 0\ \ \ \ $$

所以

f′(x0) = 0

Rolle（罗尔）定理

如果函数f(x)满足

（1）在闭区间[a，b]上连续；

（2）在开区间(a，b)上可导；

（3）在区间端点处的函数值相等，即f(a) = f(b)，

那么在(a，b)内至少有一点ξ (a < ξ < b)，使得f′(ξ) = 0。

证：由闭区间上的连续函数的有界性定理，存在ξ，η ∈ [a，b]，满足

f(ξ) = M，f(η) = m

其中M和m分别f(x)是在[a，b]上的最大值和最小值。

当M = m时，f(x)在[a，b]恒为常数，结论成立。

当M > m时，有M = f(ξ) > f(a) = f(b)和m = f(η) < f(a) = f(b)两者之一成立，根据极值点的定义，x = ξ或x = η是f(x)的极大值点或极小值点，由Fermat引理

f′(ξ) = 0或f′(η) = 0

一类中值题的通解

对于f(x)，求证∃ξ，满足

f′(ξ) + p(ξ)f(ξ) = q(ξ)

可设辅助函数F(x)

f(x) = e−∫p(x)dx(∫q(x)e∫p(x)dxdx + F(x))

可以看出，这是一阶线性微分方程的通解，这种做法于“原函数于导函数混合还原”的微分方程解法类似。

拉格朗日中值定理

如果函数f(x)满足

（1）在闭区间[a，b]上连续；

（2）在开区间(a，b)上可导；

那么在(a，b)内至少有一点ξ (a < ξ < b)，使等式

$$\frac{f(b) - f(a)}{b - a} = f'(\xi)$$

成立。

证：作辅助函数

$$g(x) = f(x) - \frac{f(b) - f(a)}{b - a}x$$

则

$$g(a) = g(b) = \frac{bf(a) - af(b)}{b - a}$$

$$g'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}$$

由罗尔定理，至少有一点ξ (a < ξ < b)，使

$$g'(\xi) = f'(\xi) - \frac{f(b) - f(a)}{b - a}$$

把定理改写成f(b) − f(a) = f′(ξ)(b − a)，记Δx = b − a，Δy = f(b) − f(a)，把a替换为自变量x，因为(a < ξ < b)，可以令ξ = x + θΔx  θ ∈ (0，1)，得到有限增量公式：

Δy = f′(x + θΔx) ⋅ Δx  (0 < θ < 1)

相比Δy = f′(x)dx + o(Δx)，有限增量公式更加精确地描述了Δy。

柯西中值定理

如果函数f(x)及F(x)满足

（1）在闭区间[a，b]上连续；

（2）在开区间(a，b)上可导；

（3）对任一x ∈ (a，b)，F′(x) ≠ 0，

那么在(a，b)内至少有一点ξ (a < ξ < b)，使等式

$$\frac{f(b) - f(a)}{F(b) - F(a)} = \frac{f'(\xi)}{F'(\xi)}$$

成立

证明：作辅助函数

$$g(x) = f(x) - \frac{f(b) - f(a)}{F(b) - F(a)}F(x)$$

$$g(a) = g(b) = \frac{F(b)f(a) - F(a)f(b)}{F(b) - F(a)}$$

g(x)在[a，b]上连续，在(a，b)上可导，由罗尔定理，至少有一点ξ (a < ξ < b)，使

$$g'(\xi) = f'(\xi) - \frac{f(b) - f(a)}{F(b) - F(a)}F'(\xi) = 0$$

整理即得。

柯西中值定理可以看成

$$\frac{\frac{f(b) - f(a)}{b - a}}{\frac{F(b) - F(a)}{b - a}} = \frac{f'(\xi)}{F'(\xi)}$$

如果函数f(x)及g(x)在闭区间[a，b]上连续，在开区间(a，b)上可导，则存在ξ ∈ (a，b)，使得

$$\left| \begin{matrix}
f(a) & f(b) \\
g(a) & g(b)
\end{matrix} \right| = (b - a)\left| \begin{matrix}
f(a) & f'(\xi) \\
g(a) & g'(\xi)
\end{matrix} \right|$$

曲率

弧微分

函数y = f(x)的有向弧段的微元为

$$ds = \sqrt{1 + {y'}^{2}}dx$$

证明：由勾股定理

$$ds = \sqrt{(dx)^{2} + (dy)^{2}} = \sqrt{(dx)^{2} + \left( y'dx \right)^{2}} = \sqrt{1 + {y'}^{2}}dx$$

曲率

定义曲率

$$K = \left| \frac{d\alpha}{ds} \right|$$

即弧长对转角α的变化率，有

$$K = \frac{\left| y^{''} \right|}{\left( 1 + {y'}^{2} \right)^{3/2}}$$

证明：由tan α = y′，得α = arctan y′

所以

$$d\alpha = \left( \arctan y' \right)'dx = \frac{y^{''}}{1 + \left( y' \right)^{2}}dx$$

又因为

$$ds = \sqrt{1 + {y'}^{2}}dx$$

所以

$$K = \left| \frac{d\alpha}{ds} \right| = \left| \frac{\frac{y^{''}}{1 + \left( y' \right)^{2}}dx}{\sqrt{1 + {y'}^{2}}dx} \right| = \frac{\left| y^{''} \right|}{\left( 1 + {y'}^{2} \right)^{3/2}}$$

曲率半径

曲线在某点处的曲率K (K ≠ 0)与曲率半径ρ满足

$$\rho = \frac{1}{K}\text{，}K = \frac{1}{\rho}$$

曲率中心

曲率中心（即曲率圆的圆心）D(α，β)的坐标为

$$\left\{ \begin{array}{r}
\alpha = x - \frac{y'(1 + y^{'2})}{y^{''}} \\
\beta = y + \frac{1 + y^{'2}}{y^{''}}\ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

点沿曲线C移动时，相应的曲率中心D的轨迹曲线G称为曲线C的渐屈线，而曲线C称为曲线G的渐伸线，设C : y = f(x)，则其渐屈线的参数方程为

$$\left\{ \begin{array}{r}
\alpha = x - \frac{y'(1 + y^{'2})}{y^{''}} \\
\beta = y + \frac{1 + y^{'2}}{y^{''}}\ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

其中α，β分别为渐屈线上某点的横、纵坐标。
