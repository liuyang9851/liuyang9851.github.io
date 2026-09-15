---
title: "微积分初步"
hs_seq: "B10"
description: "微积分初步：设是两个非空集合，如果存在一个法则，使得对中每一个元素，按法则，在中有唯一确定的元素与之对应，那么称为从到的映射，记作"
---

# 微积分初步

函数再研究

映射的定义

设$X\text{、}Y$是两个非空集合，如果存在一个法则$f$，使得对$X$中每一个元素，按法则$f$，在$Y$中有唯一确定的元素$y$与之对应，那么称$f$为从$X$到$Y$的映射，记作

$f:X \rightarrow Y$

其中$y$称为元素$x$（在映射$f$下）的像，并记作$f(x)$，即

$y = f(x)$

而元素$x$称为元素$y$（在映射$f$下）的一个原像（逆像）；集合$X$称为映射的定义域；记作$D_{f}$，即$D_{f} = X$；$X$中的所有元素的像所组成的集合称为映射$f$的值域，记作$R_{f}$或$f(X)$，即

$R_{f} = f(X) = \left\{ f(x)|x \in X \right\}$

一元函数的定义

设数集$D\mathbb{\subset R}$，则称映射$f:D\mathbb{\rightarrow R}$为定义在$D$上的函数，通常简记为

$y = f(x)\text{，}x \in D$

其中$x$称为自变量，$y$称为因变量，$D$称为定义域，记作$D_{f}$，即$D_{f} = D$

函数的定义中，对每个$x \in D$，按对应法则$d$，总有唯一确定的值$y$与之对应，这个值称为函数$f$在$x$处的函数值，记作$f(x)$，即$y = f(x)$。因变量$y$与自变量$x$之间的这种依赖关系，通常称为函数关系。函数值$f(x)$的全体所构成的集合称为函数的值域，记作$D_{f}$或$f(D)$，即

$R_{f} = f(D) = \left\{ y|y = f(x)\text{，}x \in D \right\}$

函数的全局性质

函数的一般性质

闭区间上连续函数的性质

函数在某点的性质：连续与可导

函数的连续与间断

$\text{间断点}\left\{ \begin{array}{r} \text{第一类间断点}\left. \text{（左右极限都存在} \right.\text{）}\left\{ \begin{array}{r} \text{可去间断点：}\lim_{x \rightarrow x_{0}^{-}}{f(x)} = \lim_{x \rightarrow x_{0}^{+}}{f(x)}\left\{ \begin{array}{r} \neq f\left( x_{0} \right)\ \ \ \ \ \ \ \ \  \\ f\left( x_{0} \right)\text{无定义} \end{array} \right.\ \ \ \  \\ \text{不可去间断点}\left. \text{（跳跃间断点} \right.\text{）：}\lim_{x \rightarrow x_{0}^{-}}{f(x)} \neq \lim_{x \rightarrow x_{0}^{+}}{f(x)} \end{array} \right.\ \ \ \ \ \ \ \  \\ \text{第二类间断点}\left. \text{（左右极限至少有一个不存在} \right.\text{）}\left\{ \begin{array}{r} \text{无穷间断点：}\lim_{x \rightarrow x_{0}^{-}}{f(x)} = \infty\lim_{x \rightarrow x_{0}^{+}}{f(x)} = \infty \\ \text{振荡间断点：}\lim_{x \rightarrow x_{0}}{f(x)}\text{振荡}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\ \ \  \\ \text{瑕点：}f(x)\text{无界}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

可导函数

函数$f(x)$图像的绘制

多元函数

$n$维向量$\mathbf{x} = \left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right)$到点集的映射称为多元函数，记作$y = f\left( \mathbf{x} \right) = f\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right)$，常见的二元函数可记为$z = f(x\text{，}y)$。

向量值函数

$n$维向量$\mathbf{x} = \left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right)$到$m$维向量$\mathbf{y} = (y_{1}\text{，}y_{2}\text{，}\cdots \text{，}y_{m})$的映射称为$n$元$m$维向量值函数（多元函数组），记作$\mathbf{y} = \mathbf{f}\left( \mathbf{x} \right)$。利用多元函数可以写为：

$\left\{ \begin{array}{r} y_{1} = f_{1}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right) \\ y_{2} = f_{2}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right) \\ \cdots \\ y_{m} = f_{m}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right) \end{array} \right.\$

其中$f_{1}\text{，}f_{2}\text{，}\cdots \text{，}f_{m}$代表不同的多元函数。

特别地，当$n = 1$时，称为一元向量值函数：

$\mathbf{r} = \mathbf{f}(t)$

常考虑$m = 3$的情况，即

$\mathbf{r} = \mathbf{f}(t) = f_{1}(t)\mathbf{i} + f_{2}(t)\mathbf{j} + f_{3}(t)\mathbf{k}$

一元函数的极限

> $\text{函数的极限}\left\{ \begin{array}{r} \text{类型一：}\frac{0}{0}\text{，}\frac{\infty}{\infty}\text{，}0\text{，}\infty \text{：}\left. \text{（}1 \right.\text{）等价无穷小}\left. \text{（}2 \right.\text{）泰勒公式}\left. \text{（}3 \right.\text{）洛必达法则}\ \ \ \  \\ \text{类型二：}\infty - \infty \text{：通分或乘除某式化为类型一}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \text{类型三：}\left\{ \begin{array}{r} 1^{\infty}\text{：运用}\lim_{x \rightarrow 0}(1 + x)^{\frac{1}{x}} = e\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ 0^{0}\text{，}\infty^{0}\text{：写成指数函数形式，化为类型一} \end{array}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \right.\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

其它极限结论

夹逼定理

离散洛必达

级数转化定积分定义

数列极限的定义

设$\left\{ x_{n} \right\}$为一数列，如果存在任意给定的正数$\varepsilon$（不论它多么小），总存在正整数$N$，使得当$n > N$时，不等式

$\left| x_{n} - a \right| < \varepsilon$

（对任意$n$）都成立，那么就称常数$a$使数列$\left\{ x_{n} \right\}$的极限，或者称数列$\left\{ x_{n} \right\}$收敛于$a$，记为

$\lim_{n \rightarrow \infty}x_{n} = a\ \text{或}\ x_{n} \rightarrow a(n \rightarrow \infty)$

如果不曾在这样的常数$a$，就说数列$\left\{ x_{n} \right\}$没有极限，或者说数列$\left\{ x_{n} \right\}$是发散的，习惯上也说$\lim_{n \rightarrow \infty}x_{n}$不存在。

任意的$\varepsilon$实现了实现了“由大到小”的过程，并且保证了是“任意小”的。而$N$则说明了极限的存在只与数列最后的变化趋势有关，改变某一收敛数列的有限项，无法改变数列的趋势，可以把$N$取在所有改变项的后面，改变项后面的数列每一项仍保留收敛性质，因此对与$n > N$的任意$n$都满足。$x_{n} - a$的绝对值则体现了收敛不一定单调，可以在极限上下震荡中靠近极限值。$<$体现与极限的接近性，在$\varepsilon$越来越小的过程中（实际没有“越来越小”的过程，只是由“任意给定”可以想象在若干次“任意”中$\varepsilon$越来越小），始终$<$，这就避开了xxx$= a$必须用等号写明的尴尬。

函数极限的定义

类比数列极限的定义，推广可得。这种定义方法被成为$\varepsilon - \delta$语言。

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

$f(x) \rightarrow A$

</th>
<th>

$f(x) \rightarrow + \infty$

</th>
<th>

$f(x) \rightarrow + \infty$

</th>
<th>

$f(x) \rightarrow - \infty$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$x \rightarrow x_{0}$

</td>
<td>

$\forall\varepsilon > 0\text{，}\exists\delta > 0\text{，}$

$\forall x\left( 0 < \left| x - x_{0} \right| < \delta \right)$

$:\left| f(x) - A \right| < \ \varepsilon$

</td>
<td>

$\forall M > 0\text{，}\exists\delta > 0\text{，}$

$\forall x\left( 0 < \left| x - x_{0} \right| < \delta \right)$

$:\left| f(x) \right| > M$

</td>
<td>

$\forall M > 0\text{，}\exists\delta > 0\text{，}$

$\forall x\left( 0 < \left| x - x_{0} \right| < \delta \right)$

$:f(x) > M$

</td>
<td>

$\forall M > 0\text{，}\exists\delta > 0\text{，}$

$\forall x\left( 0 < \left| x - x_{0} \right| < \delta \right)$

$:f(x) < - M$

</td>
</tr>
<tr>
<td>

$x \rightarrow x_{0}^{+}$

</td>
<td>

$\forall\varepsilon > 0,\exists\delta > 0,\$

$\forall x\left( 0 < x - x_{0} < \delta \right)$

$:\left| f(x) - A \right| < \ \varepsilon$

</td>
<td>

$\forall M > 0\text{，}\exists\delta > 0\text{，}$

$\forall x\left( 0 < x - x_{0} < \delta \right)$

$:\left| f(x) \right| > M$

</td>
<td>

$\forall M > 0\text{，}\exists\delta > 0\text{，}$

$\forall x\left( 0 < x - x_{0} < \delta \right)$

$:f(x) > M$

</td>
<td>

$\forall M > 0\text{，}\exists\delta > 0\text{，}$

$\forall x\left( 0 < x - x_{0} < \delta \right)$

$:f(x) < - M$

</td>
</tr>
<tr>
<td>

$x \rightarrow x_{0}^{-}$

</td>
<td>

$\forall\varepsilon > 0,\exists\delta > 0\text{，}$

$\forall x\left( 0 > x - x_{0} > - \delta \right)$

$:\left| f(x) - A \right| < \ \varepsilon$

</td>
<td>

$\forall M > 0\text{，}\exists\delta > 0\text{，}$

$\forall x\left( 0 > x - x_{0} > - \delta \right)$

$:\left| f(x) \right| > M$

</td>
<td>

$\forall M > 0\text{，}\exists\delta > 0\text{，}$

$\forall x\left( 0 > x - x_{0} > - \delta \right)$

$:f(x) > M$

</td>
<td>

$\forall M > 0\text{，}\exists\delta > 0\text{，}$

$\forall x\left( 0 > x - x_{0} > - \delta \right)$

$:f(x) < - M$

</td>
</tr>
<tr>
<td>

$x \rightarrow \infty$

</td>
<td>

$\forall\varepsilon > 0\text{，}\exists X > 0\text{，}$

$\forall x\left( |x| > X \right)$

$:\left| f(x) - A \right| < \ \varepsilon$

</td>
<td>

$\forall M > 0\text{，}\exists X > 0\text{，}$

$\forall x\left( |x| > X \right)$

$:\left| f(x) \right| > M$

</td>
<td>

$\forall M > 0\text{，}\exists X > 0\text{，}$

$\forall x\left( |x| > X \right)$

$:f(x) > M$

</td>
<td>

$\forall M > 0\text{，}\exists X > 0\text{，}$

$\forall x\left( |x| > X \right)$

$:f(x) < - M$

</td>
</tr>
<tr>
<td>

$x \rightarrow + \infty$

</td>
<td>

$\forall\varepsilon > 0\text{，}\exists X > 0\text{，}$

$\forall x(x > X)$

$:\left| f(x) - A \right| < \ \varepsilon$

</td>
<td>

$\forall M > 0\text{，}\exists X > 0\text{，}$

$\forall x(x > X)$

$:\left| f(x) \right| > M$

</td>
<td>

$\forall M > 0\text{，}\exists X > 0\text{，}$

$\forall x(x > X)$

$:f(x) > M$

</td>
<td>

$\forall M > 0\text{，}\exists X > 0\text{，}$

$\forall x(x > X)$

$:f(x) < - M$

</td>
</tr>
<tr>
<td>

$x \rightarrow - \infty$

</td>
<td>

$\forall\varepsilon > 0\text{，}\exists X > 0\text{，}$

$\forall x(x < - X)$

$:\left| f(x) - A \right| < \ \varepsilon$

</td>
<td>

$\forall M > 0\text{，}\exists X > 0\text{，}$

$\forall x(x < - X)$

$:\left| f(x) \right| > M$

</td>
<td>

$\forall M > 0\text{，}\exists X > 0\text{，}$

$\forall x(x < - X)$

$:f(x) > M$

</td>
<td>

$\forall M > 0\text{，}\exists X > 0\text{，}$

$\forall x(x < - X)$

$:f(x) < - M$

</td>
</tr>
</tbody>
</table>
</div>

无穷小、无穷大与阶

定义

无穷小：在某个变化过程中，若$\lim{f(x)} = 0$，则称此时$f(x)$是无穷小（量），记作$f(x) = o(1)\ \ (x \rightarrow xxx)$

> 无特殊说明，一般默认是当$x \rightarrow 0$时。

无穷大：在某个变化过程中，若$\lim{f(x)} = 0$，则称此时$f(x)$是无穷大（量）。

运算法则

无穷小：$o(1) \pm o(1) = o(1)$

> $o(1) \cdot o(1) = o(1)$
>
> $o(1) \cdot O(1) = o(1)$
>
> $\frac{\infty}{o(1)} = \infty$

无穷大：$( + \infty) + ( + \infty) = + \infty \text{，}( - \infty) + ( - \infty) = - \infty$

> $( + \infty) - ( - \infty) = + \infty \text{，}( - \infty) - ( + \infty) = - \infty$
>
> $( + \infty) \pm O(1) = + \infty \text{，}( - \infty) \pm O(1) = - \infty$
>
> $( + \infty) \cdot ( + \infty) = + \infty \text{，}( - \infty) \cdot ( - \infty) = + \infty \text{，}( + \infty) \cdot ( - \infty) = - \infty$
>
> $\infty \cdot O(1) = \infty$

无穷小的倒数为无穷大，无穷大的倒数为无穷小，这使得无穷大和无穷小可以相互转换，在实际中更多地用到无穷小。

阶

阶类似于整式的次数概念，是衡量极限逼近速度快慢的指标。代数式的阶在一些情况下为代数式所有项的最大指数或最小指数。

无穷小量阶的比较

设$f(x)\text{，}g(x)$为两个无穷小，则

$\lim\frac{f(x)}{g(x)} = \left\{ \begin{array}{r} 0\ \ \ \ \ \ \ \  \Rightarrow f(x)\text{是}g(x)\text{的高阶无穷小，记作}f(x) = o\left( g(x) \right) \\ \infty\ \ \ \ \ \ \  \Rightarrow f(x)\text{是}g(x)\text{的低阶无穷小，记作}g(x) = o\left( f(x) \right) \\ c \neq 0 \Rightarrow f(x)\text{是}g(x)\text{的同阶无穷小}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ 1\ \ \ \ \ \ \ \  \Rightarrow f(x)\text{是}g(x)\text{的等价无穷小，记作}f(x)\sim g(x)\ \ \ \ \ \ \ \ \ \end{array} \right.\$

> $\lim\frac{f(x)}{g^{k}(x)} = c \neq 0\  \Rightarrow f(x)\text{是}g(x)\text{的}k\text{阶无穷小}$

对于$f(x) = o\left( g(x) \right)$的情形（$x \rightarrow 0$），若是多项式，则可以称$f(x)$的阶为$g(x)$的最高项的次数，如$f(x) = o\left( x^{3} + 2x \right) = o\left( x^{3} \right)$，则$f(x)$的阶为3。

$o()\text{与}O\left. \text{（} \right.\text{）}$

$o()$表示无穷小（一般是对$\rightarrow 0$的），括号内常放入一个幂函数，如$o(x^{3})$表示比$x^{3}$高阶的无穷小，如$x^{4} = o(x^{3})$，$x^{5} = o\left( x^{3} \right)$，表示$x^{4}$，$x^{5}$比$x^{3}$高阶，但反过来$o\left( x^{3} \right)$不能替换为$x^{4}$或$x^{5}$。所以$o()$表示的不是某个确定的函数而是一系列更高阶的函数。

$O()$表示有界，$0 \leq \left| \frac{u(x)}{v(x)} \right| \leq A \Leftrightarrow u(x) = O\left( v(x) \right)$，其中$u(x)$和$v(x)$均为无穷小量。如$x\sin\frac{1}{x} = O(x)$表示当$x \rightarrow 0$时，$x\sin\frac{1}{x}$为有界量。

泰勒公式

泰勒公式的一般形式

> ${f(x) = \sum_{n = 1}^{N}{\frac{f^{(n)}\left( x_{0} \right)}{n!}\left( x - x_{0} \right)^{n}} + R_{n}(x) }{= \frac{f\left( x_{0} \right)}{0!} + \frac{f'\left( x_{0} \right)}{1!}\left( x - x_{0} \right) + \frac{f^{''}\left( x_{0} \right)}{2!}\left( x - x_{0} \right)^{2} + \ldots + \frac{f^{(n)}\left( x_{0} \right)}{n!}\left( x - x_{0} \right)^{n} + R_{n}(x)}$

其中$R_{n}(x)$称为余项，其具体有如下几种形式

$\text{佩亚诺余项：}o\left( \left( x - x_{0} \right)^{n} \right)$

$\text{施勒米希尔}—\text{罗什余项：}f^{(n + 1)}\left\lbrack x_{0} + \theta\left( x - x_{0} \right) \right\rbrack\frac{(1 - \theta)^{n + 1 - p}\left( x - x_{0} \right)^{n + 1}}{n!p}\ \ \left( \theta \in (0\text{，}1)\text{，}p \in \mathbb{R}_{+} \right)$

$\text{拉格朗日余项：}\frac{f^{(n + 1)}(\xi)}{(n + 1)!}\left( x - x_{0} \right)^{n + 1}\ \ \left( \xi \text{是}x_{0}\text{与}x\text{之间的某个值} \right)$

$\text{柯西余项：}f^{(n + 1)}\left\lbrack x_{0} + \theta\left( x - x_{0} \right) \right\rbrack\frac{(1 - \theta)^{n}\left( x - x_{0} \right)^{n + 1}}{n!}$

$\text{积分余项：}\frac{( - 1)^{n}}{n!}\int_{n}^{- x}{(t - x)^{n}f^{(n + 1)}(t)dt}$

$x$的次数为几就称其为第几阶。

麦克劳林公式

令一般式中的$x_{0} = 0$，得

$f(x) = \sum_{n = 1}^{N}{\frac{f^{(n)}(0)}{n!}x^{n}} + R_{n}(x) = \frac{f(0)}{0!} + \frac{f'(0)}{1!}x + \frac{f^{''}(0)}{2!}x^{2} + \ldots + \frac{f^{(n)}(0)}{n!}x^{n} + R_{n}(x)$

常用函数的泰勒展开

> $1.e^{x} = 1 + \frac{x}{1} + \frac{x^{2}}{2} + \frac{x^{3}}{6} + \ldots + x^{n} + o\left( x^{n} \right) = \sum_{n = 0}^{\infty}\frac{x^{n}}{n!}\ \$
>
> $\Rightarrow \ \ a^{x} = e^{x\ln a} = \sum_{n = 0}^{\infty}\frac{\left( \ln a \right)^{n}x^{n}}{n!}$
>
> $2.\sin x = \frac{x}{1!} - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + \ldots + \frac{( - 1)^{n}}{(2n + 1)!}x^{2n + 1} + o\left( x^{2n + 2} \right) = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{(2n + 1)!}x^{2n + 1}}$
>
> $3.\cos x = 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} - \frac{x^{6}}{6!} + \ldots + \frac{( - 1)^{n}}{(2n)!}x^{2n} + o\left( x^{2n} \right) = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{(2n)!}x^{2n}}$
>
> $4.\ln(1 + x) = x - \frac{x^{2}}{2!} + \frac{x^{3}}{3!} - \frac{x^{4}}{4!} + \ldots + \frac{( - 1)^{n - 1}}{n!}x^{n} + o\left( x^{n} \right) = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n - 1}}{n!}x^{n}}\ \$
>
> $\Rightarrow \ln(1 - x) = - x - \frac{x^{2}}{2!} - \frac{x^{3}}{3!} - \frac{x^{4}}{4!} + \ldots = \sum_{n = 0}^{\infty}{\frac{- 1}{n!}x^{n}}\ \ \left( |x| < 1 \right)\ \$
>
> $\Rightarrow \ln\frac{1 + x}{1 - x} = 2\left( x + \frac{1}{3}x^{3} + \frac{1}{5}x^{5} + \cdots \right) = 2\sum_{n = 0}^{\infty}\frac{x^{2n + 1}}{2n + 1}\ \ \left( |x| < 1 \right)$
>
> $5.(1 + x)^{m} = 1 + mx + \frac{m(m - 1)}{2!}x^{2} + \cdots + \begin{pmatrix} m \\ n \end{pmatrix}x^{n} + o\left( x^{n} \right) = \sum_{n = 0}^{\infty}{\begin{pmatrix} m \\ n \end{pmatrix}x^{n}}\ \ \left( m\mathbb{\in N} \right)$
>
> $6.(1 + x)^{a} = 1 + ax + \frac{a(a - 1)}{2!}x^{2} + \cdots + \frac{a(a - 1)\cdots(a - n + 1)}{a!}x^{n} + o(1)\ \ \left( a\mathbb{\in R} \right)$
>
> $\Rightarrow \sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^{2}}{8} + \frac{x^{3}}{16} - \frac{5x^{4}}{128} + \ldots$
>
> $\Rightarrow \frac{1}{1 + x} = 1 - x + x^{2} - x^{3} + \cdots = \sum_{n = 0}^{\infty}{( - 1)^{n}x^{n}}\ \ \left( |x| < 1 \right)\ \$
>
> $\Rightarrow \ \ \frac{1}{1 + x^{2}} = \sum_{n = 0}^{\infty}{( - 1)^{n}x^{2n}}\ \ \left( |x| < 1 \right)$
>
> $\Rightarrow \frac{1}{1 - x} = 1 + x + x^{2} + x^{3} + \cdots = \sum_{n = 0}^{\infty}x^{n}\ \ \left( |x| < 1 \right)$

泰勒公式的误差

由拉格朗日余项，误差不超过

$\left| \frac{f^{(n + 1)}(\xi)}{(n + 1)!}\left( x - x_{0} \right)^{n + 1} \right|$

因此，考虑$\xi$的值，使上式取最大值，所得到的范围即为误差范围

泰勒公式求极限

二元函数的泰勒公式

设$z = f(x\text{，}y)$上有两点$\left( x_{0}\text{，}y_{0} \right)$和$\left( x_{0} + h\text{，}y_{0} + k \right)$，则

> $f\left( x_{0} + h\text{，}y_{0} + k \right)$
>
> $= f\left( x_{0}\text{，}y_{0} \right) + \left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)f\left( x_{0}\text{，}y_{0} \right) + \frac{1}{2!}\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)^{2}f\left( x_{0}\text{，}y_{0} \right) + \cdots + \frac{1}{n!}\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)^{n}f\left( x_{0}\text{，}y_{0} \right) + \frac{1}{(n + 1)!}\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)^{n + 1}f\left( x_{0} + \theta h\text{，}y_{0} + \theta k \right)$

其中

> $\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)\ \ f\left( x_{0}\text{，}y_{0} \right)\text{表示}\ \ hf_{x}\left( x_{0}\text{，}y_{0} \right) + kf_{y}\left( x_{0}\text{，}y_{0} \right)$
>
> $\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)^{2}f\left( x_{0}\text{，}y_{0} \right)\text{表示}\ \ h^{2}f_{xx}\left( x_{0}\text{，}y_{0} \right) + 2hkf_{xy}\left( x_{0}\text{，}y_{0} \right) + k^{2}f_{yy}\left( x_{0}\text{，}y_{0} \right)$
>
> $\cdots\cdots\cdots$
>
> $\left( h\frac{\partial}{\partial x} + k\frac{\partial}{\partial y} \right)^{n}f\left( x_{0}\text{，}y_{0} \right)\text{表示}\ \sum_{p = 0}^{m}{C_{m}^{p}h^{p}k^{m - p}\frac{\partial^{m}f}{\partial x^{p}\partial y^{m - p}}}\left| \underset{\left( x_{0}\text{，}y_{0} \right)}{} \right.\$
>
> $0 < \theta < 1$

也就是说，对于二元函数$f(x\text{，}y)$，有

> $f\left( x + x_{0}\text{，}y + y_{0} \right)$
>
> $= f\left( x_{0}\text{，}y_{0} \right) + \left( x\frac{\partial}{\partial x} + y\frac{\partial}{\partial y} \right)f\left( x_{0}\text{，}y_{0} \right) + \frac{1}{2!}\left( x\frac{\partial}{\partial x} + y\frac{\partial}{\partial y} \right)^{2}f\left( x_{0}\text{，}y_{0} \right) + \cdots + \frac{1}{n!}\left( x\frac{\partial}{\partial x} + y\frac{\partial}{\partial y} \right)^{n}f\left( x_{0}\text{，}y_{0} \right) = \sum_{i = 1}^{n}{\left( x\frac{\partial}{\partial x} + y\frac{\partial}{\partial y} \right)^{i}f\left( x_{0}\text{，}y_{0} \right)}$

$eg.x^{y} = 1 + (x - 1) + (x - 1)(y - 1) + \frac{1}{2}(x - 1)^{2}(y - 1) + R_{3}\ \left( (1\text{，}1)\text{处展开} \right)$

L’Hospital（洛必达）法则

$\text{设}f(x)\text{，}g(x)\text{可导，}\ g'(x) \neq 0\text{，}\lim\frac{f'(x)}{g'(x)}\text{存在，当满足以下两个条件}$

$1.\lim{f(x)} = \lim{g(x)} = 0$

$2.\lim{g(x)} = \infty$

中的一个时，即有

$\lim\frac{f(x)}{g(x)} = \lim\frac{f'(x)}{g'(x)}$

特殊极限定义式及推论

$1.\lim_{x \rightarrow 0}\frac{\sin x}{x} = 1$

$2.\lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n} = \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n + 1} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{1}{x} \right)^{x} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{k}{x} \right)^{x} = \lim_{\frac{x}{k} \rightarrow \infty}\left( 1 + \frac{1}{\frac{x}{k}} \right)^{\frac{x}{k} \cdot k} = e^{k} \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{a}{x} \right)^{bx + c} = e^{ab}$

$\text{特别地，}e^{x} = \lim_{n \rightarrow \infty}\left( 1 + \frac{x}{n} \right)^{n} = \exp(x)$

$\lim{u(x)^{v(x)}} = e^{\lim\left\lbrack \left( u(x) - 1 \right)v(x) \right\rbrack}\text{，其中在同一过程中}\lim{u(x)} = 1\text{，}\lim{v(x)} = \infty$

$3.\lim_{n \rightarrow \infty}\left( 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} - \ln n \right) = \gamma = 0.557\ 215\ 664\ 90\cdots$

等价无穷小代换

常见的等价无穷小可以用洛必达法则轻易地得出，等价无穷小替换可以视为泰勒公式的简易应用。

一阶：$x\ \ \sim\ \ \sin x\ \ \sim\ \ \tan x\ \ \sim\ \ \arcsin{x\ \ }\sim\ \ \arctan x\ \ \sim\ \ e^{x} - 1\ \ \sim\ \ \ln(1 + x)\ \  \sim \ \ \sqrt{1 + x} - \sqrt{1 - x}$

$\text{二阶：}\frac{1}{2}x^{2}\ \  \sim \ \ 1 - \cos x\ \ \sim\ \ x - \ln(1 + x)\ \  \sim \ \ e^{x} - x - 1\sim - \ln{\cos x}$

三阶：

$\frac{1}{2}x^{3}\ \  \sim \ \tan x - \sin x\ \  \sim \ \ \arcsin x - \arctan x$

$\frac{1}{3}x^{3}\ \  \sim \ \ \tan x - x\ \  \sim \ \ x - \arctan x\ \  \sim \ \ \arcsin x - \sin x$

$\frac{2}{3}x^{3}\ \  \sim \ \ \tan x - \arctan x$

$- \frac{1}{3}x^{3}\ \  \sim \ \ x - \ln(1 + x) - \frac{x^{2}}{2}$

$\frac{1}{6}x^{3}\  \sim \ \ x - \sin x\  \sim \ \tan x - \arcsin x\  \sim \ \arcsin x - x\  \sim \ \sin x - \arctan x$

其它：

$(1 + x)^{m} - 1\sim mx$

$\log_{a}(1 + x)\sim\frac{x}{\ln a}$

$a^{x} - 1\sim x\ln a$

$1 - x\sim - \ln x\ \ (x \rightarrow 1)$

一些等价无穷小代换的证明

$\lim_{x \rightarrow 0}\frac{\sin x}{x} = 1$

$\lim_{x \rightarrow 0}\frac{\tan x}{x} = \lim_{x \rightarrow 0}\left( \frac{x}{\sin x} \cdot \cos x \right) = \lim_{x \rightarrow 0}\frac{x}{\sin x} \cdot \lim_{x \rightarrow 0}{\cos x} = 1$

$\lim_{x \rightarrow 0}\frac{\arcsin x}{x} = \lim_{t \rightarrow 0}\frac{t}{\sin t} = 1$

$\lim_{x \rightarrow 0}\frac{\arctan x}{x} = \lim_{t \rightarrow 0}\frac{t}{\tan t} = 1$

$\lim_{x \rightarrow 0}\frac{\ln(1 + x)}{x} = \lim_{x \rightarrow 0}{\ln(1 + x)^{\frac{1}{x}}} = \ln{\lim_{x \rightarrow 0}(1 + x)^{\frac{1}{x}}} = \ln e = 1$

$\lim_{x \rightarrow 0}\frac{e^{x} - 1}{x} = \lim_{t \rightarrow 0}\frac{t}{\ln(1 + t)} = 1$

$\lim_{x \rightarrow 0}\frac{(1 + x)^{\alpha} - 1}{\alpha x} = \lim_{x \rightarrow 0}\left( \frac{(1 + x)^{\alpha} - 1}{\ln(1 + x)^{\alpha}} \cdot \frac{\alpha\ln(1 + x)}{\alpha x} \right)\overset{(1 + x)^{\alpha} - 1 = t}{\Leftrightarrow}\lim_{t \rightarrow 0}\frac{t}{\ln(1 + t)} \cdot \lim_{x \rightarrow 0}\frac{\alpha\left( 1 + \ln x \right)}{\alpha x} = 1$

$- \ln{\cos x} = - \ln\left\lbrack 1 + \left( \cos x - 1 \right) \right\rbrack\sim - \left( \cos x - 1 \right)\sim\frac{1}{2}x^{2}$

$\ln(x + 1)\sim x\ \ (x \rightarrow 0)\overset{t = x + 1}{\Leftrightarrow}\ln t\sim t - 1\ \ (t \rightarrow 1) \Leftrightarrow - \ln x\sim 1 - x\ \ (x \rightarrow 1)$

与极限有关的定理和结论

1.夹逼定理

数列$\left\{ x_{n} \right\} \text{，}\left\{ y_{n} \right\} \text{，}\left\{ z_{n} \right\}$从某项起开始满足

$x_{n} \leq y_{n} \leq z_{n}\text{，}\lim_{n \rightarrow \infty}x_{n} = \lim_{n \rightarrow \infty}z_{n} = a$

则

$\lim_{n \rightarrow \infty}y_{n} = a$

证明：对$\left\{ x_{n} \right\}$和$\left\{ z_{n} \right\}$由定义，有$a - \varepsilon < x_{n} < a + \varepsilon$，$a - \varepsilon < z_{n} < a + \varepsilon$，由$x_{n} \leq y_{n} \leq z_{n}$，有

$a - \varepsilon < x_{n} \leq y_{n} \leq z_{n} < a + \varepsilon$

满足极限的定义，得证。

2.Stolz定理

对数列$\left\{ x_{n} \right\} \text{，}\left\{ y_{n} \right\}$

$\left. \text{（}1 \right.\text{）若}\left\{ y_{n} \right\} \text{严格单调递增趋于}\  + \infty \text{，且}\lim_{n \rightarrow \infty}\frac{x_{n} - x_{n - 1}}{y_{n} - y_{n - 1}} = a\text{，则}\ \lim_{n \rightarrow \infty}\frac{x_{n}}{y_{n}} = a\ \ (a\text{可以为某数或} \pm \infty)$

$(2)\text{若}\left\{ y_{n} \right\} \text{严格单调递减趋于}\ 0\text{，}\left\{ x_{n} \right\} \text{趋于}0\text{，且}\lim_{n \rightarrow \infty}\frac{x_{n} - x_{n - 1}}{y_{n} - y_{n - 1}} = a\text{，则}\ \lim_{n \rightarrow \infty}\frac{x_{n}}{y_{n}} = a\ \ (a\text{可以为某数或} \pm \infty)$

3.单调有界收敛定理：单调有界数列必定收敛。

4. 闭区间套定理：如果$\left\{ \left\lbrack a_{n}\text{，}b_{n} \right\rbrack \right\}$构成一个闭区间套，则存在唯一的实数$\xi$属于所有的闭区间$\left\lbrack a_{n}\text{，}b_{n} \right\rbrack$，且$\xi = \lim_{n \rightarrow \infty}a_{n} = \lim_{n \rightarrow \infty}b_{n}$。

5.若数列$\left\{ x_{n} \right\}$收敛于$a$，则其任何子数列也收敛于$a$。

6.Cauchy（柯西）收敛原理：数列$\left\{ x_{n} \right\}$收敛的充要条件是$\left\{ x_{n} \right\}$是基本数列。基本数列$\left\{ x_{n} \right\}$满足：对于任意的$\varepsilon > 0$，存在正整数$N$，使得当$n,m > N$时$\left| x_{n} - x_{m} \right| < \varepsilon$恒成立。

常见极限

$\cdot \lim_{x \rightarrow 0}\frac{a_{0}x^{m} + a_{1}x^{m - 1} + \cdots + a_{m}}{b_{0}x^{n} + b_{1}x^{n - 1} + \cdots + b_{n}} = \left\{ \begin{array}{r} 0\text{，当}a_{m} = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \frac{a_{m}}{b_{n}}\text{，当}a_{m} \neq 0\text{且}b_{n} \neq 0 \\ \infty \text{，当}b_{n} = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\ \ \ \ \left( a_{m}\text{，}b_{n}\text{不同时为}0 \right)$

$\cdot \lim_{x \rightarrow \infty}\frac{a_{0}x^{m} + a_{1}x^{m - 1} + \cdots + a_{m}}{b_{0}x^{n} + b_{1}x^{n - 1} + \cdots + b_{n}} = \left\{ \begin{array}{r} 0\text{，当}n > m \\ \frac{a_{0}}{b_{0}}\text{，当}n = m \\ \infty \text{，当}n < m \end{array} \right.\$

$\cdot \lim_{n \rightarrow \infty}{n\sin\frac{180{^\circ}}{n}} = \pi \Rightarrow \lim_{n \rightarrow + \infty}\frac{\sin\frac{\pi}{n}}{\frac{\pi}{n}} = 1 \Rightarrow \lim_{x \rightarrow 0}\frac{\sin x}{x} = 1$

$\cdot \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n} = \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{n} \right)^{n + 1} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{1}{x} \right)^{x} = e \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{k}{x} \right)^{x} = \lim_{\frac{x}{k} \rightarrow \infty}\left( 1 + \frac{1}{\frac{x}{k}} \right)^{\frac{x}{k} \cdot k} = e^{k} \Rightarrow \lim_{x \rightarrow \infty}\left( 1 + \frac{a}{x} \right)^{bx + c} = e^{ab}$

$\text{特别地，}e^{x} = \lim_{n \rightarrow \infty}\left( 1 + \frac{x}{n} \right)^{n} = \exp(x)$

$\cdot \lim_{x \rightarrow \infty}\frac{x^{n}}{e^{\lambda x}} = 0$

$\cdot \lim_{x \rightarrow \infty}\frac{a^{x}}{x!} = 0$

$\cdot \lim_{x \rightarrow 0}{x\ln x} = 0$

$\text{对}\ln x\text{关于}1\text{泰勒展开，得}$

$\ln x = 0 + (x - 1) - \frac{1}{2}(x - 1)^{2} + \frac{1}{3}(x - 1)^{3} - \frac{1}{4}(x - 1)^{4} + \cdots$

故

$x\ln x = x(x - 1) - \frac{1}{2}x(x - 1)^{2} + \frac{1}{3}x(x - 1)^{3} - \frac{1}{4}x(x - 1)^{4} + \cdots$

$\text{当}x \rightarrow 0\text{时，由于}(x - 1)^{n} = \pm 1\text{有界，故}x(x - 1)^{n}\text{趋于}0\text{，式子各项趋于}0\text{，得证}$

也可以用洛必达法则

$\lim_{x \rightarrow 0}{x\ln x} = \lim_{x \rightarrow 0}\frac{\ln x}{\frac{1}{x}} = \lim_{x \rightarrow 0}\frac{\frac{1}{x}}{- \frac{1}{x^{2}}} = \lim_{x \rightarrow 0}\frac{- x}{1} = 0$

$\cdot \lim_{x \rightarrow \infty}\left( x - \ln x \right) = + \infty$

$\lim_{x \rightarrow \infty}\left( x - \ln x \right) = \lim_{x \rightarrow 0}\left( \frac{1}{x} - \ln\frac{1}{x} \right) = \lim_{x \rightarrow 0}\left( \frac{1}{x} + \ln x \right) = \lim_{x \rightarrow 0}\left( \frac{1}{x} + \ln x \right) = \lim_{x \rightarrow 0}\left( \frac{1 + x\ln x}{x} \right) = \lim_{x \rightarrow 0}\frac{1}{x} = + \infty$

$\cdot \lim_{n \rightarrow \infty}\sqrt[n]{n} = 1$

$\cdot \lim_{n \rightarrow \infty}\sqrt[n]{n^{k}} = 1$

$\cdot \text{若}\ \lim_{n \rightarrow \infty}a_{n} = a\text{，则}\ \lim_{n \rightarrow \infty}\frac{a_{1} + a_{2} + \cdots + a_{n}}{n} = a$

$\cdot \lim_{n \rightarrow \infty}\left( a_{1}^{n} + a_{2}^{n} + \cdots + a_{p}^{n} \right)^{\frac{1}{n}} = \max_{1 \leq i \leq p}\left\{ a_{i} \right\}$

$\cdot \lim_{n \rightarrow \infty}{n\left( \sqrt{n^{2} + 1} - \sqrt{n^{2} - 1} \right)} = 1$

$\text{若}\ \lim_{n \rightarrow \infty}a_{n} = a\text{，则}\ \lim_{n \rightarrow \infty}\sqrt[n]{a_{1}a_{2}\cdots a_{n}} = a$

$\cdot \lim_{n \rightarrow \infty}\left( 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} - \ln n \right) = \gamma = 0.557\ 215\ 664\ 90\cdots$

导数与微分

导数与微分一体两面，虽然微积分以微分和积分著称，但实际中导数先于微分的概念出现，导数也较微分更常使用。导数和微分分别从变化率和增量两方面探究函数的性质，最后可以发现两者的统一。

导数的定义

一元函数的导数

设函数$y = f(x)$在点$x_{0}$的某个邻域内有定义，当自变量$x$在$x_{0}$处取得增量$\mathrm{\Delta}x$（点$x_{0} + \mathrm{\Delta}x$仍在该邻域内）时，相应地，因变量取得增量$\mathrm{\Delta}y = f\left( x_{0} + \mathrm{\Delta}x \right) - f\left( x_{0} \right)$；如果$\mathrm{\Delta}y$与$\mathrm{\Delta}x$之比当$\mathrm{\Delta}x \rightarrow 0$时的极限存在，那么称函数$y = f(x)$在点$x_{0}$处可导，并称这个极限为函数$y = f(x)$在点$x_{0}$处的导数，记为$f'(x)$，即

$f'\left( x_{0} \right) = \lim_{\mathrm{\Delta}x \rightarrow 0}\frac{\mathrm{\Delta}y}{\mathrm{\Delta}x} = \lim_{\mathrm{\Delta}x \rightarrow 0}\frac{f\left( x_{0} + \mathrm{\Delta}x \right) - f\left( x_{0} \right)}{\mathrm{\Delta}x}$

$\text{也可记作}y'\left. \  \right|_{x = x_{0}}\text{，}\frac{dy}{dx}\left| \begin{array}{r} \\ \underset{x = x_{0}}{} \end{array} \right.\ \text{或}\frac{df(x)}{dx}\left| \begin{array}{r} \\ \underset{x = x_{0}}{} \end{array} \right.\$

于是得到导函数的定义式

$y' = y_{x} = y_{x}' = f'(x) = f_{x}'(x) = \frac{dy}{dx} = \frac{df(x)}{dx} = \lim_{\mathrm{\Delta}x \rightarrow 0}\frac{f(x + \mathrm{\Delta}x) - f(x)}{\mathrm{\Delta}x}$

且有

$f'\left( x_{0} \right) = f'(x)\left. \  \right|_{x = x_{0}}$

微分的定义

微分的定义在目前几乎是无法讲得清楚的，现在几乎所有的高数教材和数学分析的定义都有不足。下面是同济高数的定义：

一元函数的微分

设函数$y = f(x)$在点$x_{0}$的某个邻域内有定义，当自变量$x$在$x_{0}$处取得增量$\mathrm{\Delta}x$（点$x_{0} + \mathrm{\Delta}x$仍在该邻域内）时，相应地，因变量取得增量$\mathrm{\Delta}y = f\left( x_{0} + \mathrm{\Delta}x \right) - f\left( x_{0} \right)$，若存在只与$x_{0}$有关而与$\Delta x$无关的数$g\left( x_{0} \right)$，满足

$\mathrm{\Delta}y = g\left( x_{0} \right)\Delta x + o(\Delta x)$

则称$f(x)$在$x_{0}$处的微分存在，亦称$f(x)$在$x_{0}$处可微。

定义$dx = \Delta x\text{，}dy = \lim_{\Delta x \rightarrow 0}{\mathrm{\Delta}y} = \lim_{\Delta x \rightarrow 0}{g\left( x_{0} \right)\Delta x + o(\Delta x)} = g\left( x_{0} \right)dx$

下面举一例来说明这个定义的问题：令$y = x^{2}\text{，}\ \ x = t^{3}$，则有

$dy = 2x\Delta x\text{，}\ \Delta x = 3t^{2}\Delta t + o(\Delta t)\text{，}$

$dy = 2t^{3}\left( 3t^{2}\Delta t + o(\Delta t) \right) = 6t^{5}\Delta t + 2t^{3}o(\Delta t)$

但由$y = x^{2} = \left( t^{3} \right)^{2} = t^{6}$，得

$dy = 6t^{5}\Delta t$

可以发现，无穷小量$2t^{3}o(\Delta t)$消失了，这是一个矛盾。

$dy$和$dx$不能被简单认识为变量、函数或是$\rightarrow 0$的一个过程，而是“微分形式”，可以参考：[为什么几乎所有教科书上对微分的讲解都不明不白？ - 王泰翔的回答 - 知乎](https://www.zhihu.com/question/438795295/answer/2394202555)

[https://www.zhihu.com/question/438795295/answer/2394202555](https://www.zhihu.com/question/438795295/answer/2394202555)

多元函数的偏导数

对于二元函数$z = f(x\text{，}y)$，定义偏导数

$\frac{\partial z}{\partial x} = \frac{\partial f}{\partial x} = z_{x} = z_{x}' = f_{x}(x\text{，}y) = f_{x}'(x\text{，}y) = \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x\text{，}y) - f(x\text{，}y)}{\Delta x}$

$\frac{\partial z}{\partial y} = \frac{\partial f}{\partial y} = z_{y} = z_{y}' = f_{y}(x\text{，}y) = f_{y}'(x\text{，}y) = \lim_{\Delta y \rightarrow 0}\frac{f(x\text{，}y + \Delta y) - f(x\text{，}y)}{\Delta y}$

向量值函数的导数

对向量值函数$\mathbf{y = f}\left( \mathbf{x} \right)$，即

$\left\{ \begin{array}{r} y_{1} = f_{1}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right) \\ y_{2} = f_{2}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right) \\ \cdots \\ y_{m} = f_{m}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right) \end{array} \right.\$

定义

$\left( \frac{\partial f_{i}}{\partial x_{j}}\left( \mathbf{x}^{0} \right) \right)_{m \times n} = \mathbf{f}'\left( \mathbf{x}^{0} \right) = \mathbf{Df}\left( \mathbf{x}^{0} \right) = \mathbf{J}_{\mathbf{f}}\left( \mathbf{x}^{0} \right) = \begin{pmatrix} \frac{\partial f_{1}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) & \frac{\partial f_{1}}{\partial x_{2}}\left( \mathbf{x}^{0} \right) & \cdots & \frac{\partial f_{1}}{\partial x_{n}}\left( \mathbf{x}^{0} \right) \\ \frac{\partial f_{2}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) & \frac{\partial f_{2}}{\partial x_{2}}\left( \mathbf{x}^{0} \right) & \cdots & \frac{\partial f_{2}}{\partial x_{n}}\left( \mathbf{x}^{0} \right) \\ \vdots & \vdots & & \vdots \\ \frac{\partial f_{m}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) & \frac{\partial f_{m}}{\partial x_{2}}\left( \mathbf{x}^{0} \right) & \cdots & \frac{\partial f_{m}}{\partial x_{n}}\left( \mathbf{x}^{0} \right) \end{pmatrix}$

为向量值函数$\mathbf{f}$在$\mathbf{x}^{0}$点的导数或Jacobi（雅可比）矩阵

特别地，对于$m = 1$的情况，即一元向量值函数，有

$\mathbf{f}'\left( \mathbf{x}^{0} \right) = \begin{pmatrix} \frac{\partial f_{1}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) \\ \frac{\partial f_{2}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) \\ \vdots \\ \frac{\partial f_{m}}{\partial x_{1}}\left( \mathbf{x}^{0} \right) \end{pmatrix} = \frac{\partial f_{1}}{\partial x_{1}}\mathbf{e}_{1} + \frac{\partial f_{2}}{\partial x_{1}}\mathbf{e}_{2} + \cdots + \frac{\partial f_{m}}{\partial x_{1}}\mathbf{e}_{m}$

导数的四则运算法则的证明（同济）

${\left\lbrack f(x) \pm g(x) \right\rbrack' = \lim_{\Delta x \rightarrow 0}\frac{\left\lbrack f(x + \Delta x) \pm g(x + \Delta x) \right\rbrack - \left\lbrack f(x) \pm g(x) \right\rbrack}{\Delta x} }{= \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x) - f(x)}{\Delta x} \pm \lim_{\Delta x \rightarrow 0}\frac{g(x + \Delta x) - g(x)}{\Delta x} }{= f'(x) + g'(x)}$

${\left\lbrack f(x)g(x) \right\rbrack' = \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x)g(x + \Delta x) - f(x)g(x)}{\Delta x} }{= \lim_{\Delta x \rightarrow 0}\left\lbrack \frac{f(x + \Delta x) - f(x)}{\Delta x} \cdot g(x + \Delta x) + f(x) \cdot \frac{g(x + \Delta x) - g(x)}{\Delta x} \right\rbrack }{= \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x) - f(x)}{\Delta x} \cdot \lim_{\Delta x \rightarrow 0}{g(x + \Delta x)} + f(x) \cdot \lim_{\Delta x \rightarrow 0}\frac{g(x + \Delta x) - g(x)}{\Delta x} }{= f'(x)g(x) + f(x)g'(x)}$

${\left\lbrack \frac{f(x)}{g(x)} \right\rbrack' = \lim_{\Delta x \rightarrow 0}\frac{\frac{f(x + \Delta x)}{g(x + \Delta x)} - \frac{f(x)}{g(x)}}{\Delta x} }{= \lim_{\Delta x \rightarrow 0}\frac{f(x + \Delta x)g(x) - f(x)g(x + \Delta x)}{g(x + \Delta x)g(x)\Delta x} }{= \lim_{\Delta x \rightarrow 0}\frac{\left\lbrack f(x + \Delta x) - f(x) \right\rbrack g(x) - f(x)\left\lbrack g(x + \Delta x) - g(x) \right\rbrack}{g(x + \Delta x)g(x)\Delta x} }{= \lim_{\Delta x \rightarrow 0}\frac{\frac{f(x + \Delta x) - f(x)}{\Delta x}g(x) - f(x)\frac{g(x + \Delta x) - g(x)}{\Delta x}}{g(x + \Delta x)g(x)} }{= \frac{f'(x)g(x) - f(x)g'(x)}{g^{2}(x)}}$

部分基本初等函数的导数公式的证明

1.常函数：$f(x) = C$

$f'(x) = \lim_{h \rightarrow 0}\frac{f(x + h) - f(x)}{h} = \lim_{h \rightarrow 0}\frac{C - C}{h} = 0$

2.幂函数（部分）：$f(x) = x^{n}\ \ (x > 0)$

$\text{当}n = 1\text{时，}f'(x) = \lim_{h \rightarrow 0}\frac{x + h - x}{h} = 1$

$\text{当}n > 1\text{时，}f'(x) = \lim_{h \rightarrow 0}\frac{(x + h)^{n} - x^{n}}{h} = \lim_{h \rightarrow 0}\left\lbrack nx^{n - 1} + \frac{n(n - 1)}{2}x^{n - 2}h + \cdots + h^{n - 1} \right\rbrack = nx^{n - 1}$

3.正弦函数：$f(x) = \sin x$

$f'(x) = \lim_{h \rightarrow 0}\frac{\sin(x + h) - \sin x}{h} = \lim_{h \rightarrow 0}{\frac{1}{h} \cdot 2\cos\left( x + \frac{h}{2} \right)\sin\frac{h}{2}} = \lim_{h \rightarrow 0}{\cos\left( x + \frac{h}{2} \right) \cdot \frac{\sin\frac{h}{2}}{\frac{h}{2}}} = \cos x$

4.余弦函数：$f(x) = \cos x$

$f'(x) = \lim_{h \rightarrow 0}\frac{\cos(x + h) - \cos x}{h} = \lim_{h \rightarrow 0}{\frac{- 1}{h} \cdot 2\sin\left( x + \frac{h}{2} \right)\sin\frac{h}{2}} = \lim_{h \rightarrow 0}{- \sin\left( x + \frac{h}{2} \right) \cdot \frac{\sin\frac{h}{2}}{\frac{h}{2}}} = - \sin x$

5.对数函数：$f(x) = \log_{a}x\ \ (a > 0,\ \ a \neq 1)$

$f'(x) = \lim_{h \rightarrow 0}\frac{\log_{a}(x + h) - \log_{a}x}{h} = \frac{1}{\ln a} \cdot \lim_{h \rightarrow 0}\frac{\ln\left( 1 + \frac{h}{x} \right)}{h} = \frac{1}{\ln a} \cdot \lim_{h \rightarrow 0}\frac{\frac{h}{x}}{h} = \frac{1}{x\ln a}\ \ \ \left( \ln{(1 + x)\ \sim\ }x \right)$

6.指数函数：$f(x) = a^{x}\ \ (a \neq 0)$

$f'(x) = \lim_{h \rightarrow 0}\frac{a^{x + h} - a^{x}}{h} = a^{x} \cdot \lim_{h \rightarrow 0}\frac{a^{h} - 1}{h} = a^{x} \cdot \lim_{h \rightarrow 0}\frac{h\ln a}{h} = a^{x}\ln a\ \ \left( a^{x} - 1\ \sim\ \ x\ln a \right)$

7.幂函数：$f(x) = x^{a}\ \ (x > 0)$

$f'(x) = \lim_{h \rightarrow 0}\frac{(x + h)^{a} - x^{h}}{h} = x^{a} \cdot \lim_{h \rightarrow 0}\frac{\left( 1 + \frac{h}{x} \right)^{a} - 1}{x \cdot \frac{h}{x}} = x^{a} \cdot \lim_{h \rightarrow 0}\frac{\frac{ah}{x}}{x \cdot \frac{h}{x}} = ax^{a - 1}\ \ \left( (1 + x)^{m} - 1\ \sim\ mx \right)$

高阶导数

二阶导数、三阶导数、四阶导数、n阶导数可用如下符号表示

$y^{''}\ \ \frac{d^{2}y}{dx^{2}}\text{，}y^{'''}\ \ \frac{d^{3}y}{dx^{3}}\text{，}y^{(4)}\ \ \frac{d^{4}y}{dx^{4}}\text{，}y^{(n)}\ \ \frac{d^{n}y}{dx^{n}}$

零阶导数$f^{(0)}(x)$可视作原函数$f(x)$

高阶导数的三则运算法则：

$\left\lbrack f(x) \pm g(x) \right\rbrack^{(n)} = \left\lbrack f(x) \right\rbrack^{(n)} \pm \left\lbrack g(x) \right\rbrack^{(n)} = f^{(n)}(x) \pm g^{(n)}(x)$

$\left\lbrack Cf(x) \right\rbrack^{(n)} = C \cdot f^{(n)}(x)$

$Leibniz\text{（莱布尼兹）公式：}\left\lbrack f(x) \cdot g(x) \right\rbrack^{(n)} = \sum_{k = 0}^{n}{C_{n}^{k}f^{(n - k)}(x)g^{(k)}(x)}$

常见函数的高阶导数：

$\left( a^{x} \right)^{(n)} = \left( \ln a \right)^{n}a^{x}$

$\left( \sin x \right)^{(n)} = \sin\left( x + \frac{n\pi}{2} \right)$

$\left( \cos x \right)^{(n)} = \cos\left( x + \frac{n\pi}{2} \right)$

$\left( \sin{kx} \right)^{(n)} = k^{n}\sin\left( kx + \frac{n\pi}{2} \right)$

$\left( \cos{kx} \right)^{(n)} = k^{n}\cos\left( kx + \frac{n\pi}{2} \right)$

$\left( x^{m} \right)^{(n)} = \left\{ \begin{array}{r} m(m - 1)\cdots(m - n + 1)x^{m - n} = A_{m}^{n}x^{m - n}\ \ \ \ n \leq m \\ 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ n > m \end{array} \right.\$

$\left( x^{n} \right)^{(n)} = n!$

$\left( \ln x \right)^{(n)} = ( - 1)^{n - 1}\frac{(n - 1)!}{x^{n}}$

$\left( \frac{1}{x} \right)^{(n)} = \left( \ln x \right)^{(n + 1)} = ( - 1)^{n}\frac{n!}{x^{n + 1}}$

$\left( \frac{1}{ax + b} \right)^{(n)} = ( - 1)^{n}\frac{a^{n} \cdot n!}{(ax + b)^{n + 1}}$

复合函数的求导法则

如果函数$u = g(x)$在点$x$可导，而$y = f(u)$在点$u = g(x)$可导，那么复合函数$y = f\left\lbrack g(x) \right\rbrack$在点$x$可导，且其导数为

$f'(x) = f'(u) \cdot g'(x)\text{，}y_{x}' = y_{u}' \cdot u_{x}'\text{，}\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$

证明略。

反函数的求导法则

设函数$x = f(y)$（自变量$y$，因变量$x$，法则$f$）在区间$I_{y}$内单调可导且$f'(y) \neq 0$，则其反函数$y = f^{- 1}(x)$（自变量$x$，因变量$y$，法则$f^{- 1}$）在区间$I_{x} = \left\{ x\ |\ x = f(y)\text{，}y \in I_{y} \right\}$内也可导，且

$\left\lbrack f^{- 1}(x) \right\rbrack' = \frac{1}{f'(y)}\text{或}\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}}$

其中$\left\lbrack f^{- 1}(x) \right\rbrack'$和$\frac{dy}{dx}$是指对$y = f^{- 1}(x)$求关于$x$的导数，即${f_{x}^{- 1}}'(x)$，$f'(y)$和$\frac{dx}{dy}$是指对$x = f(y)$求关于$y$的导数。对直接函数和反函数的求导都是对因变量关于自变量的求导。为方便理解，用另一种符号表示如下

${f_{x}^{- 1}}'(x) = \frac{1}{f_{y}'(y)}\text{或}\frac{df^{- 1}(x)}{dx} = \frac{1}{\frac{df(y)}{dy}}$

证明：使用复合函数求导法则。

想要得到是$y = f^{- 1}(x)$关于$x$的导数表达式${f_{x}^{- 1}}'(x)$，这个表达式与$x = f(y)$对$y$的导数$f_{y}'(y)$有关。对$y = f^{- 1}(x)$两边关于$y$求导，即

$y_{y}' = \left\lbrack f_{y}^{- 1}(x) \right\rbrack'\text{，微分形式为}\ \frac{dy}{dy} = \frac{df^{- 1}(x)}{dy}$

由复合函数求导法则，得

$1 = {f_{x}^{- 1}}'(x) \cdot x_{y}' = \frac{df^{- 1}(x)}{dx} \cdot \frac{dx}{dy}$

故

${f_{x}^{- 1}}'(x) = \frac{1}{x_{y}'} = \frac{1}{f_{y}'(y)}\text{，微分形式为}\frac{df^{- 1}(x)}{dx} = \frac{1}{\frac{dx}{dy}} = \frac{1}{\frac{df^{- 1}(x)}{dy}}$

下面更改变量记号重新证明：

令$y = f(x)\text{，}x = f^{- 1}(y)$，要求得的是${f_{y}^{- 1}}'(y)$（为方便理解，可以把这里的$y$替换成任意字母。导数的$'$号在内是因为要的导数是对自变量（这里是$y$）求导）

对$x = f^{- 1}(y)$两边关于$x$求导，得

$1 = {f_{y}^{- 1}}'(y) \cdot y_{x}' = f_{y}^{- 1}(y) \cdot f_{x}'(x)$

所以

${f_{y}^{- 1}}'(y) = \frac{1}{f_{x}'(x)}$

$eg.$求$y = \arctan x$的导数$y_{x}'$

解：令

$y = f^{- 1}(x) = \arctan x\text{，}x = f(y) = \tan y$

$y_{x}' = {f_{x}^{- 1}}'(x) = \frac{1}{f_{y}'(y)} = \frac{1}{\left( \tan y \right)_{y}'} = \frac{1}{\sec^{2}y} = \frac{1}{1 + \tan^{2}y} = \frac{1}{1 + x^{2}}$

$\text{下面推到反函数的二阶导数和三阶导数，方便起见，记}y' = \frac{dy}{dx}\text{，}y^{''} = \frac{d^{2}y}{dx^{2}}\text{，有}$

> $\frac{d^{2}x}{dy^{2}} = \frac{d}{dy}\left( \frac{dx}{dy} \right) = \frac{d\left( \left( y' \right)^{- 1} \right)}{dy} = \frac{d\left( \left( y' \right)^{- 1} \right)}{dx} \cdot \frac{dx}{dy} = - \frac{y^{''}}{{y'}^{2}} \cdot \frac{1}{y'} = - \frac{y^{''}}{\left( y' \right)^{3}}$
>
> $\frac{d^{3}x}{dy^{3}} = \frac{d}{dy}\left( \frac{d^{2}x}{dy^{2}} \right) = \frac{d\left( - \frac{y^{''}}{\left( y' \right)^{3}} \right)}{dx} \cdot \frac{dx}{dy} = - \frac{y^{'''}\left( y' \right)^{3} - y^{''} \cdot 3\left( y' \right)^{2}y^{''}}{\left( y' \right)^{6}} \cdot \frac{1}{y'} = \frac{3\left( y^{''} \right)^{2} - y'y^{'''}}{\left( y' \right)^{5}}$

参数方程的导数

$y_{x}' = \frac{dy}{dx} = \frac{dy}{dt}\frac{dt}{dx} = \frac{y_{t}'}{x_{t}'}$

同理

$\frac{d^{2}y}{dx^{2}} = \frac{d}{dx}\left( \frac{dy}{dx} \right) = \frac{d}{dt}\left( \frac{y'(t)}{x'(t)} \right) \cdot \frac{dt}{dx} = \frac{y^{''}(t)x'(t) - y'(t)x^{''}(t)}{{x'}^{2}(t)} \cdot \frac{1}{x'(t)} = \frac{y^{''}(t)x'(t) - y'(t)x^{''}(t)}{{x'}^{3}(t)}$

极坐标下的导数

已知$r = f(\theta)\text{，求}r'$

由

$x = r\cos\theta$

$y = r\sin\theta$

得

$x = f(\theta)\cos\theta$

$y = f(\theta)\sin\theta$

$r_{\theta}' = \frac{dy}{dx} = \frac{dy}{d\theta}\frac{d\theta}{dx} = \frac{y_{\theta}'}{x_{\theta}'}$

常见函数的导数

见常用导数与积分表。

偏导数

微分

全微分

$\Delta z = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy + ο(\rho)$

$\text{其中}ο(\rho) = \sqrt{(dx)^{2} + (dy)^{2}}$

$dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy$

微分近似公式

一元函数

$\Delta y \approx dy = f'(x)dx$

$f(x + \Delta x) \approx f(x) + f'(x)\Delta x$

多元函数

$\Delta z \approx dz = f_{x}(x\text{，}y)\Delta x + f_{y}(x\text{，}y)\Delta y$

$f(x + \Delta x\text{，}y + \Delta y) \approx f(x\text{，}y) + f_{x}(x\text{，}y)\Delta x + f_{y}(x\text{，}y)\Delta y$

多元复合函数的求导法则

$1.u = \varphi(t)\text{，}v = \psi(t)\text{，}z = f(u\text{，}v)$

$\frac{dz}{dx} = \frac{\partial z}{\partial u}\frac{du}{dt} + \frac{\partial z}{\partial v}\frac{dv}{dt}$

$2.u = \varphi(x\text{，}y)\text{，}v = \psi(x\text{，}y)\text{，}z = f(u\text{，}v)$

$\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial x}$

$\frac{\partial z}{\partial y} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial y} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial y}$

全微分形式不变性

设函数$z = f(u\text{，}v)$具有连续偏导数，则有全微分

$dz = \frac{\partial z}{\partial u}du + \frac{\partial z}{\partial v}dv$

通过此能得到全导数的概念

$D(f) = f_{x} + f_{y} + \cdots$

其满足所有求导法则和导数公式

拉格朗日乘数法求最值

（出现形如$x \in \lbrack 1\text{，}2\rbrack$之类的条件时，不能判断得出的是极大值还是极小值）

已知目标函数$f(x\text{，}y)$，约束条件$\varphi(x\text{，}y) = 0$，求$f(x\text{，}y)$的极值

令$F(x\text{，}y\text{，}\lambda) = f(x\text{，}y) + \lambda\varphi(x\text{，}y)$，解方程组：

$\left\{ \begin{array}{r} F_{x}'(x\text{，}y\text{，}\lambda) = f_{x}'(x\text{，}y) + \lambda\varphi_{x}'(x\text{，}y) = 0 \\ F_{y}'(x\text{，}y\text{，}\lambda) = f_{y}'(x\text{，}y) + \lambda\varphi_{y}'(x\text{，}y) = 0 \\ F_{\lambda}'(x\text{，}y\text{，}\lambda) = \lambda\varphi(x\text{，}y) = 0\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

得到x，y的一组或几组解，验证后代入$f(x\text{，}y)$即得$f(x\text{，}y)$的极值

> $eg.\text{已知}x\text{，}y\text{，}z \in \mathbb{R}_{+}\text{，且}x + y + z = 1\text{，求}\frac{1}{x} + \frac{4}{y} + \frac{9}{z}\text{的最小值}$
>
> $\text{解：令}F(x\text{，}y\text{，}z\text{，}\lambda) = \frac{1}{x} + \frac{4}{y} + \frac{9}{z} + \lambda(x + y + z - 1)\text{，求偏导数，可得}$

$\left\{ \begin{array}{r} - \frac{1}{x^{2}} + 1 = 0\ \ \ \ \ \ \ \ \  \\ - \frac{4}{y^{2}} + 1 = 0\ \ \ \ \ \ \ \ \  \\ - \frac{9}{z^{2}} + 1 = 0\ \ \ \ \ \ \ \ \  \\ x + y + z - 1 = 0 \end{array} \right.\ \text{解之，得}x = \frac{1}{6}\text{，}y = \frac{1}{3}\text{，}z = \frac{1}{2}\text{，即得最小值为}36\text{。}$

> 该结论可推广到有多个约束条件的情形。

费曼求导法（对数求导法）

对于多个多项式因式的积的导数，其导数为

因式$\times \lbrack\rbrack$

方括号内是该式的每个因式的处理后的结果的和，该处理方法为：

$\text{因式右上角的指数} \times (\text{因式})^{- 1} \times (\text{因式})'$

$eg.f(t) = \frac{6\left( 1 + 2t^{2} \right)\left( t^{3} - t \right)^{2}}{\sqrt{t + 5t^{2}}(4t)^{\frac{3}{2}}} + \frac{\sqrt{1 + 2t}}{t + \sqrt{1 + t^{2}}}$

$f'(t) = \frac{6\left( 1 + 2t^{2} \right)\left( t^{3} - t \right)^{2}}{\sqrt{t + 5t^{2}}(4t)^{\frac{3}{2}}} \cdot \left\lbrack 1 \cdot \frac{4t}{1 + 2t^{2}} + 2 \cdot \frac{3t^{2} - 1}{t^{3} - t} - \frac{1}{2} \cdot \frac{1 + 10t}{t + 5t^{2}} - \frac{3}{2} \cdot \frac{4}{4t} \right\rbrack$

> $+ \frac{\sqrt{1 + 2t}}{t + \sqrt{1 + t^{2}}} \cdot \left\{ \frac{1}{2}\frac{2}{1 + 2t} - 1\frac{1}{t + \sqrt{1 + t^{2}}}\left\lbrack 1 + \frac{1}{2}\frac{2t}{\sqrt{1 + t^{2}}} \right\rbrack \right\}$

其中

$1 \cdot \frac{4t}{1 + 2t^{2}} = \left( 1 + 2t^{2} \right)\text{的指数}(\text{即为}1) \times \frac{1}{1 + 2t^{2}} \times \left( 1 + 2t^{2} \right)'$

$2 \cdot \frac{3t^{2} - 1}{t^{3} - t} = \left( t^{3} - t \right)^{2}\text{的指数}(\text{即为}2) \times \frac{1}{t^{3} - t} \times \left( t^{3} - t \right)'$

$- \frac{1}{2} \cdot \frac{1 + 10t}{t + 5t^{2}} = \frac{1}{\sqrt{t + 5t^{2}}}\text{的指数}\left( \text{即为}\frac{1}{2} \right) \times \frac{1}{t + 5t^{2}} \times \left( t + 5t^{2} \right)'$

$- \frac{3}{2} \cdot \frac{4}{4t} = (4t)^{\frac{3}{2}}\text{的指数}\left( \text{即为} - \frac{3}{2} \right) \times \frac{1}{4t} \times (4t)'$

$\frac{1}{2}\frac{2}{1 + 2t} = \sqrt{1 + 2t}\text{的指数}\left( \text{即为}\frac{1}{2} \right) \times \frac{1}{1 + 2t} \times (1 + 2t)'$

$- 1\frac{1}{t + \sqrt{1 + t^{2}}}\left\lbrack 1 + \frac{1}{2}\frac{2t}{\sqrt{1 + t^{2}}} \right\rbrack = t + \sqrt{1 + t^{2}}\text{的指数}(\text{即为} - 1) \times \frac{1}{t + \sqrt{1 + t^{2}}} \times \left( t + \sqrt{1 + t^{2}} \right)'$

微分中值定律

Fermat（费马）引理

设$x_{0}$是$f(x)$的一个极值点，且$f(x)$在$x_{0}$处导数存在，则

$f'\left( x_{0} \right) = 0$

证：设$x_{0}$是$f(x)$的极大（小）值点，由极大（小）值点的定义，$f(x)$在$x_{0}$的某个邻域$O(x_{0}\text{，}\delta)$上有定义，满足

$f(x) \leq f\left( x_{0} \right)\ \ \left. \text{（或}f(x) \geq f\left( x_{0} \right) \right.\text{）}$

当$x < x_{0}$时，有$\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \geq 0\ \ \left. \text{（或}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \leq 0 \right.\text{）}$；当$x > x_{0}$时，有$\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \leq 0\ \ \left. \text{（或}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \geq 0 \right.\text{）}$。因为$f(x)$在$x_{0}$可导，所以$f'\left( x_{0} \right) = f_{+}'\left( x_{0} \right) = f_{-}'\left( x_{0} \right)$，又因为

$f_{-}'\left( x_{0} \right) = \lim_{x \rightarrow x_{0}^{-}}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \geq 0\text{，}f_{+}'\left( x_{0} \right) = \lim_{x \rightarrow x_{0}^{+}}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \leq 0$

$\text{或}f_{-}'\left( x_{0} \right) = \lim_{x \rightarrow x_{0}^{-}}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \leq 0\text{，}f_{+}'\left( x_{0} \right) = \lim_{x \rightarrow x_{0}^{+}}\frac{f(x) - f\left( x_{0} \right)}{x - x_{0}} \geq 0\ \ \ \$

所以

$f'\left( x_{0} \right) = 0$

Rolle（罗尔）定理

如果函数$f(x)$满足

（1）在闭区间$\lbrack a\text{，}b\rbrack$上连续；

（2）在开区间$(a\text{，}b)$上可导；

（3）在区间端点处的函数值相等，即$f(a) = f(b)$，

那么在$(a\text{，}b)$内至少有一点$\xi\ (a < \xi < b)$，使得$f'(\xi) = 0$。

证：由闭区间上的连续函数的有界性定理，存在$\xi \text{，}\eta \in \lbrack a\text{，}b\rbrack$，满足

$f(\xi) = M\text{，}f(\eta) = m$

其中$M$和$m$分别$f(x)$是在$\lbrack a\text{，}b\rbrack$上的最大值和最小值。

当$M = m$时，$f(x)$在$\lbrack a\text{，}b\rbrack$恒为常数，结论成立。

当$M > m$时，有$M = f(\xi) > f(a) = f(b)$和$m = f(\eta) < f(a) = f(b)$两者之一成立，根据极值点的定义，$x = \xi$或$x = \eta$是$f(x)$的极大值点或极小值点，由Fermat引理

$f'(\xi) = 0\text{或}f'(\eta) = 0$

一类中值题的通解

对于$f(x)$，求证$\exists\xi$，满足

$f'(\xi) + p(\xi)f(\xi) = q(\xi)$

可设辅助函数$F(x)$

$f(x) = e^{- \int_{}^{}{p(x)dx}}\left( \int_{}^{}{q(x)e^{\int_{}^{}{p(x)dx}}dx} + F(x) \right)$

可以看出，这是一阶线性微分方程的通解，这种做法于“原函数于导函数混合还原”的微分方程解法类似。

拉格朗日中值定理

如果函数$f(x)$满足

（1）在闭区间$\lbrack a\text{，}b\rbrack$上连续；

（2）在开区间$(a\text{，}b)$上可导；

那么在$(a\text{，}b)$内至少有一点$\xi\ (a < \xi < b)$，使等式

$\frac{f(b) - f(a)}{b - a} = f'(\xi)$

成立。

证：作辅助函数

$g(x) = f(x) - \frac{f(b) - f(a)}{b - a}x$

则

$g(a) = g(b) = \frac{bf(a) - af(b)}{b - a}$

$g'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}$

由罗尔定理，至少有一点$\xi\ (a < \xi < b)$，使

$g'(\xi) = f'(\xi) - \frac{f(b) - f(a)}{b - a}$

把定理改写成$f(b) - f(a) = f'(\xi)(b - a)$，记$\Delta x = b - a\text{，}\Delta y = f(b) - f(a)$，把$a$替换为自变量$x$，因为$(a < \xi < b)$，可以令$\xi = x + \theta\Delta x\ \ \theta \in (0\text{，}1)$，得到有限增量公式：

$\Delta y = f'(x + \theta\Delta x) \cdot \Delta x\ \ (0 < \theta < 1)$

相比$\Delta y = f'(x)dx + o(\Delta x)$，有限增量公式更加精确地描述了$\Delta y$。

柯西中值定理

如果函数$f(x)$及$F(x)$满足

（1）在闭区间$\lbrack a\text{，}b\rbrack$上连续；

（2）在开区间$(a\text{，}b)$上可导；

（3）对任一$x \in (a\text{，}b)$，$F'(x) \neq 0$，

那么在$(a\text{，}b)$内至少有一点$\xi\ (a < \xi < b)$，使等式

$\frac{f(b) - f(a)}{F(b) - F(a)} = \frac{f'(\xi)}{F'(\xi)}$

成立

证明：作辅助函数

$g(x) = f(x) - \frac{f(b) - f(a)}{F(b) - F(a)}F(x)$

$g(a) = g(b) = \frac{F(b)f(a) - F(a)f(b)}{F(b) - F(a)}$

$g(x)$在$\lbrack a\text{，}b\rbrack$上连续，在$(a\text{，}b)$上可导，由罗尔定理，至少有一点$\xi\ (a < \xi < b)$，使

$g'(\xi) = f'(\xi) - \frac{f(b) - f(a)}{F(b) - F(a)}F'(\xi) = 0$

整理即得。

柯西中值定理可以看成

$\frac{\frac{f(b) - f(a)}{b - a}}{\frac{F(b) - F(a)}{b - a}} = \frac{f'(\xi)}{F'(\xi)}$

如果函数$f(x)$及$g(x)$在闭区间$\lbrack a\text{，}b\rbrack$上连续，在开区间$(a\text{，}b)$上可导，则存在$\xi \in (a\text{，}b)$，使得

$\left| \begin{matrix} f(a) & f(b) \\ g(a) & g(b) \end{matrix} \right| = (b - a)\left| \begin{matrix} f(a) & f'(\xi) \\ g(a) & g'(\xi) \end{matrix} \right|$

曲率

弧微分

函数$y = f(x)$的有向弧段的微元为

$ds = \sqrt{1 + {y'}^{2}}dx$

证明：由勾股定理

$ds = \sqrt{(dx)^{2} + (dy)^{2}} = \sqrt{(dx)^{2} + \left( y'dx \right)^{2}} = \sqrt{1 + {y'}^{2}}dx$

曲率

定义曲率

$K = \left| \frac{d\alpha}{ds} \right|$

即弧长对转角$\alpha$的变化率，有

$K = \frac{\left| y^{''} \right|}{\left( 1 + {y'}^{2} \right)^{3/2}}$

$\text{证明：由}\tan\alpha = y'\text{，得}\alpha = \arctan y'$

$\text{所以}$

$d\alpha = \left( \arctan y' \right)'dx = \frac{y^{''}}{1 + \left( y' \right)^{2}}dx$

又因为

$ds = \sqrt{1 + {y'}^{2}}dx$

所以

$K = \left| \frac{d\alpha}{ds} \right| = \left| \frac{\frac{y^{''}}{1 + \left( y' \right)^{2}}dx}{\sqrt{1 + {y'}^{2}}dx} \right| = \frac{\left| y^{''} \right|}{\left( 1 + {y'}^{2} \right)^{3/2}}$

曲率半径

曲线在某点处的曲率$K\ (K \neq 0)$与曲率半径$\rho$满足

$\rho = \frac{1}{K}\text{，}K = \frac{1}{\rho}$

曲率中心

曲率中心（即曲率圆的圆心）$D(\alpha \text{，}\beta)$的坐标为

$\left\{ \begin{array}{r} \alpha = x - \frac{y'(1 + y^{'2})}{y^{''}} \\ \beta = y + \frac{1 + y^{'2}}{y^{''}}\ \ \ \ \ \ \ \ \end{array} \right.\$

点沿曲线C移动时，相应的曲率中心D的轨迹曲线G称为曲线C的渐屈线，而曲线C称为曲线G的渐伸线，设$C:y = f(x)$，则其渐屈线的参数方程为

$\left\{ \begin{array}{r} \alpha = x - \frac{y'(1 + y^{'2})}{y^{''}} \\ \beta = y + \frac{1 + y^{'2}}{y^{''}}\ \ \ \ \ \ \ \ \end{array} \right.\$

其中$\alpha \text{，}\beta$分别为渐屈线上某点的横、纵坐标。

积分

不定积分

定义：在区间I上，函数$f(x)$的带有任意常数项的原函数$F(x) + C$称为$f(x)$（或$f(x)dx$）在区间I上的不定积分，记作

$\int_{}^{}{f(x)dx} = F(x) + C$

第一换元积分法

$\int_{}^{}{f\left\lbrack \varphi(x) \right\rbrack\varphi'(x)dx} = \left\lbrack \int_{}^{}{f(u)du} \right\rbrack_{u = \varphi(x)}$

特别地

$\int_{}^{}{af(x)dx} = \int_{}^{}{f(x)d(ax + b)}$

$eg.\int_{}^{}\frac{dx}{x\ln x} = \int_{}^{}{\frac{1}{\ln x}d\ln x} = \ln\left| \ln x \right| + C$

第二换元积分法

$\int_{}^{}{f(x)dx} = \left\lbrack \int_{}^{}{f\left( \psi(t) \right)\psi'(t)dt} \right\rbrack_{t = \psi^{- 1}(x)}$

分部积分法

$\int_{}^{}{uv'dx} = uv - \int_{}^{}{u'vdx}\ \text{或}\ \int_{}^{}{udv} = uv - \int_{}^{}{vdu}$

证明：由$\left\lbrack u(x)v(x) \right\rbrack' = u'(x)v(x) + u(x)v'(x)$，有

$\frac{duv}{dx} = v\frac{du}{dx} + u\frac{dv}{dx}$

等式两边同乘$dx$，得

$duv = vdu + udv$

两边积分，即得

$uv = \int_{}^{}{duv} = \int_{}^{}{vdu} + \int_{}^{}{udv}$

$eg.\int_{}^{}{\ln xdx} = x\ln x - \int_{}^{}{xd\ln x} = x\ln x - \int_{}^{}{x \cdot \frac{1}{x}dx} = x\ln x - x + C$

$eg.\int_{}^{}{x^{2}e^{x}dx} = \int_{}^{}{x^{2}de^{x}} = x^{2}e^{x} - \int_{}^{}{e^{x}dx^{2}} = x^{2}e^{x} - \int_{}^{}{2xe^{x}dx}$

$\text{又}\int_{}^{}{2xe^{x}dx} = 2\int_{}^{}{xe^{x}dx} = 2xe^{x} - 2\int_{}^{}{e^{x}dx} = 2xe^{x} - 2e^{x} + C$

$\text{故}\int_{}^{}{x^{2}e^{x}dx} = x^{2}e^{x} - 2xe^{x} + 2e^{x} + C$

留在前面的优先级：反对幂三指（反三角函数，对数函数，幂函数，三角函数，指数函数，$e^{x}$）

分部积分法亦有如下公式

$\int_{}^{}{uvdw} = uvw - \int_{}^{}{uwdv} - \int_{}^{}{vwdu}$

有理函数的积分

$\text{两个多项式的商}\frac{P(x)}{Q(x)}\text{称为有理函数，又称有理分式。当}P(x)\text{的次数小于}Q(x)\text{的次数时，称这有理分式为}$

$\text{真分式，否则称为假分式。可以将一个假分式转化成一个多项式与一个真分式的和的形式。}$

由代数数论的知识可以证明，可以把$Q(x)$按如下形式分解：

$Q(x) = \prod_{k = 1}^{i}\left( x - \alpha_{k} \right)^{m_{k}} \cdot \prod_{k = 1}^{j}\left( x^{2} + 2\xi_{k}x + \eta_{k}^{2} \right)^{n_{k}}$

意思是可以把$Q(x)$分解成若干个一次多项式和二次多项式的积。

$\text{可以证明真分式}\frac{P(x)}{Q(x)}\text{可以被按如下方式分解}$

$\frac{P(x)}{Q(x)} = \sum_{k = 1}^{i}{\sum_{r = 1}^{m_{k}}\frac{\lambda_{kr}}{\left( x - \alpha_{k} \right)^{r}}} + \sum_{k = 1}^{j}{\sum_{r = 1}^{n_{k}}\frac{\mu_{kr}x + \nu_{kr}}{\left( x^{2} + 2\xi_{k}x + \eta_{k}^{2} \right)^{n_{k}}}}$

其中$\alpha \text{，}\lambda \text{，}\mu \text{，}\nu \text{，}\xi \text{，}\eta$是任意实数，$i\text{，}j\text{，}k\text{，}m\text{，}n\text{，}r$是正整数。

举例说明（大写字母代表待定的实数系数）

$1.\frac{4x^{3} - 13x^{2} + 3x + 8}{(x + 1)(x - 2)(x - 1)^{2}} = \frac{A}{x + 1} + \frac{B}{x - 2} + \frac{C}{x - 1} + \frac{D}{(x - 1)^{2}}$

$2.\frac{x^{4} + x^{3} + 3x^{2} - 1}{\left( x^{2} + 1 \right)^{2}(x - 1)} = \frac{A}{x - 1} + \frac{Bx + C}{x^{2} + 1} + \frac{Dx + E}{\left( x^{2} + 1 \right)^{2}}$

$3.\frac{1}{(x + 1)^{2}\left( x^{2} - 2x + 3 \right)^{3}} = \frac{A}{x + 1} + \frac{B}{(x + 1)^{2}} + \frac{Cx + D}{x^{2} - 2x + 3} + \frac{Ex + F}{\left( x^{2} - 2x + 3 \right)^{2}} + \frac{Gx + H}{\left( x^{2} - 2x + 3 \right)^{3}}$

$\int_{}^{}\frac{dx}{ax^{2} + bx + c} = \left\{ \begin{array}{r} \frac{2}{\sqrt{4ac - b^{2}}}\arctan\frac{2ax + b}{\sqrt{4ac - b^{2}}} + C\ \ \left( b^{2} < 4ac \right)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ - \frac{1}{a\left( x - \frac{b}{2a} \right)} + C\ \ \left( b^{2} = 4ac \right)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \frac{1}{\sqrt{b^{2} - 4ac}}\ln\left| \frac{2ax + b - \sqrt{b^{2} - 4ac}}{2ax + b + \sqrt{b^{2} - 4ac}} \right| + C\ \ \left( b^{2} > 4ac \right) \end{array} \right.\$

$\int_{}^{}{\frac{x}{ax^{2} + bx + c}dx} = \frac{1}{2a}\ln\left| ax^{2} + bx + c \right| - \frac{b}{2a}\int_{}^{}\frac{dx}{ax^{2} + bx + c}$

由上面两个积分可以组合分母不超过二次的有理函数的积分

$\int_{}^{}\frac{dx}{(x - a)^{n}} = \left\{ \begin{array}{r} \ln|x - a| + C \\ - \frac{1}{n - 1} \cdot \frac{1}{(x - a)^{n - 1}} + C \end{array} \right.\$

$I_{n} = \int_{}^{}\frac{dx}{\left( x^{2} + bx + c \right)^{n}} = \frac{2n - 3}{2\left( c - \frac{b^{2}}{4} \right)(n - 1)}I_{n - 1} + \frac{1}{2\left( c - \frac{b^{2}}{4} \right)(n - 1)} \cdot \frac{x + \frac{b}{2}}{\left\lbrack \left( x + \frac{b}{2} \right)^{2} + c - \frac{b^{2}}{4} \right\rbrack^{n - 1}}$

由上面两个积分可以求出任意有理函数的积分

$eg.\int_{}^{}{\frac{4x^{3} - 13x^{2} + 3x + 8}{(x + 1)(x - 2)(x - 1)^{2}}dx}$

$\frac{4x^{3} - 13x^{2} + 3x + 8}{(x + 1)(x - 2)(x - 1)^{2}} = \frac{A}{x + 1} + \frac{B}{x - 2} + \frac{C}{x - 1} + \frac{D}{(x - 1)^{2}} \Rightarrow$

$4x^{3} - 13x^{2} + 3x + 8 = A(x - 2)(x - 1)^{2} + B(x + 1)(x - 1)^{2} + C(x + 1)(x - 2)(x - 1) + D(x + 1)(x - 2)$

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

$(u \pm v)' = u' \pm v'$

</td>
<td>

$\int_{}^{}{(u + v)dx} = \int_{}^{}{udx} + \int_{}^{}{vdx}$

</td>
</tr>
<tr>
<td>

$(Cu)' = Cu'$

</td>
<td>

$\int_{}^{}{kudx} = k\int_{}^{}{udx}\ \ \left. \text{（}k\text{是常数} \right.\text{）}$

</td>
</tr>
<tr>
<td>

$(uv)' = u'v + iv'$

</td>
<td>

$\int_{}^{}{udv} = uv - \int_{}^{}{vdu}$

</td>
</tr>
<tr>
<td>

$\left( \frac{u}{v} \right)' = \frac{u'v - uv'}{v^{2}}$

</td>
<td>

$\int_{}^{}\frac{dx}{e^{x}} = - \frac{1}{e^{x}}$

</td>
</tr>
<tr>
<td>

${f_{x}^{- 1}}'(x) = \frac{1}{f_{y}'(y)}\text{或}\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}}$

</td>
<td></td>
</tr>
<tr>
<td rowspan="2">

$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$

$\text{或}$

$y_{x}' = y_{u}' \cdot u_{x}'$

</td>
<td>

$\int_{}^{}{f\left\lbrack \varphi(x) \right\rbrack\varphi'(x)dx} = \left\lbrack \int_{}^{}{f(u)du} \right\rbrack_{u = \varphi(x)}$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{f(x)dx} = \left\lbrack \int_{}^{}{f\left( \psi(t) \right)\psi'(t)dt} \right\rbrack_{t = \psi^{- 1}(x)}$

</td>
</tr>
<tr>
<td colspan="2">

非三角函数类函数

</td>
</tr>
<tr>
<td>

$(C)' = 0$

</td>
<td>

$\int_{}^{}{kdx} = kx + C\ \ \left. \text{（}k \neq 0 \right.\text{）}$

</td>
</tr>
<tr>
<td>

$\left( x^{\mu} \right)' = \mu x^{\mu - 1}$

</td>
<td>

$\int_{}^{}{x^{\mu}dx} = \frac{x^{\mu + 1}}{\mu + 1} + C\ \ (\mu \neq - 1)$

</td>
</tr>
<tr>
<td>

$\left( a^{x} \right)' = a^{x}\ln a\ \ (a > 0\text{，}a \neq 1)$

</td>
<td>

$\int_{}^{}{a^{x}dx} = \frac{a^{x}}{\ln a} + C$

</td>
</tr>
<tr>
<td>

$\left( e^{x} \right)' = e^{x}$

</td>
<td>

$\int_{}^{}{e^{x}dx} = e^{x} + C$

</td>
</tr>
<tr>
<td>

$\left( \log_{a}x \right)' = \frac{1}{x\ln a}\ \ (a > 0\text{，}a \neq 1)$

</td>
<td>

$\int_{}^{}{\log_{a}xdx} = \frac{1}{\ln a}\left( x\ln x - x \right) + C$

</td>
</tr>
<tr>
<td rowspan="3">

$\left( \ln x \right)' = \frac{1}{x}$

</td>
<td>

$\int_{}^{}\frac{dx}{x} = \ln|x| + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\ln xdx} = x\ln x - x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}\frac{dx}{x\ln x} = \ln\left| \ln x \right| + C$

</td>
</tr>
<tr>
<td rowspan="6"></td>
<td>

$\int_{}^{}\frac{dx}{\sqrt{a^{2} - x^{2}}} = \arcsin\frac{x}{a} + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\sqrt{a^{2} - x^{2}}dx} = \frac{a^{2}}{2}\arcsin\frac{x}{a} + \frac{1}{2}x\sqrt{a^{2} - x^{2}} + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}\frac{dx}{\sqrt{x^{2} + a^{2}}} = \ln\left( x + \sqrt{x^{2} + a^{2}} \right) + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\sqrt{x^{2} + a^{2}}dx} = \frac{1}{2}\left( x\sqrt{x^{2} + a^{2}} + a^{2}\ln\left| x + \sqrt{x^{2} + a^{2}} \right| \right) + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}\frac{dx}{\sqrt{x^{2} - a^{2}}} = \ln\left| x + \sqrt{x^{2} - a^{2}} \right| + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\sqrt{x^{2} - a^{2}}dx} = \frac{1}{2}\left( x\sqrt{x^{2} - a^{2}} - a^{2}\ln\left| x + \sqrt{x^{2} - a^{2}} \right| \right) + C$

</td>
</tr>
<tr>
<td colspan="2">

三角函数

</td>
</tr>
<tr>
<td rowspan="5">

$\left( \sin x \right)' = \cos x$

</td>
<td>

$\int_{}^{}{\sin xdx} = - \cos x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\sin^{2}xdx} = \frac{1}{2}x - \frac{1}{4}\sin{2x} + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\sin^{3}xdx} = - \cos x + \frac{1}{3}\cos^{3}x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\sin^{4}xdx} = \frac{3}{8}x - \frac{1}{4}\sin{2x} + \frac{1}{32}\sin{4x} + C$

</td>
</tr>
<tr>
<td>

$I_{n} = \int_{}^{}{\sin^{n}xdx} = - \frac{1}{n}\sin^{n - 1}x\cos x + \frac{n - 1}{n}I_{n - 2}$

</td>
</tr>
<tr>
<td rowspan="5">

$\left( \cos x \right)' = - \sin x$

</td>
<td>

$\int_{}^{}{\cos xdx} = \sin x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\cos^{2}xdx} = \frac{1}{2}x + \frac{1}{4}\sin{2x} + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\cos^{3}xdx} = \sin x - \frac{1}{3}\sin^{3}x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\cos^{4}xdx} = \frac{3}{8}x + \frac{1}{4}\sin{2x} + \frac{1}{32}\sin{4x} + C$

</td>
</tr>
<tr>
<td>

$I_{n} = \int_{}^{}{\cos^{n}xdx} = \frac{1}{n}\cos^{n - 1}x\sin x + \frac{n - 1}{n}I_{n - 2}$

</td>
</tr>
<tr>
<td rowspan="5">

$\left( \tan x \right)' = \frac{1}{\cos^{2}x} = \sec^{2}x$

</td>
<td>

$\int_{}^{}\frac{dx}{\cos^{2}x} = \int_{}^{}{\sec^{2}xdx} = \tan x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\tan xdx} = - \ln\left| \cos x \right| + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\tan^{2}xdx} = \tan x - x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\tan^{3}xdx} = \frac{1}{2}\tan^{2}x + \ln\left| \cos x \right| + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\tan^{4}xdx} = \frac{1}{3}\tan^{3}x - \tan x + x + C$

</td>
</tr>
<tr>
<td rowspan="5">

$\left( \cot x \right)' = - \frac{1}{\sin^{2}x} = - \csc^{2}x$

</td>
<td>

$\int_{}^{}\frac{dx}{\sin^{2}x} = \int_{}^{}{\csc^{2}xdx} = - \cos x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\cot xdx} = \ln\left| \sin x \right| + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\cot^{2}xdx} = - \cot x - x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\cot^{3}xdx} = - \frac{1}{2}\cot^{2}x - \ln\left| \sin x \right| + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\cot^{4}xdx} = - \frac{1}{3}\cot^{3}x + \cot x + x + C$

</td>
</tr>
<tr>
<td rowspan="5">

$\left( \sec x \right)' = \frac{\tan x}{\cos x} = \sec x\tan x$

</td>
<td>

$\int_{}^{}{\sec x\tan xdx} = \sec x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\sec xdx} = \ln\left| \tan\left( \frac{\pi}{4} + \frac{x}{2} \right) \right| + C = \ln\left| \sec x + \tan x \right| + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\sec^{2}xdx} = \tan x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\sec^{3}xdx} = \frac{1}{2}\left( \sec x\tan x + \ln\left| \sec x + \tan x \right| \right) + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\sec^{4}xdx} = \frac{1}{3}\tan^{3}x + \tan x + C$

</td>
</tr>
<tr>
<td rowspan="5">

$\left( \csc x \right)' = - \frac{\cos x}{\sin^{2}x} = - \frac{1}{\sin x\tan x} = - {\csc x\cot}x$

</td>
<td>

$\int_{}^{}{\csc x\cot xdx} = - \csc x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\csc xdx} = \ln{\left| \tan\frac{x}{2} \right|\ } + C = \ln\left| \csc x - \cot x \right| + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\csc^{2}xdx} = - \cot x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\csc^{3}xdx} = \frac{1}{2}\left( - \csc x\cot x + \ln\left| \csc x - \cot x \right| \right)$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\csc^{4}xdx} = - \frac{1}{3}\cot^{3}x - \cot x + C$

</td>
</tr>
<tr>
<td colspan="2">

反三角函数

</td>
</tr>
<tr>
<td rowspan="2">

$\left( \arcsin x \right)' = \frac{1}{\sqrt{1 - x^{2}}}$

</td>
<td>

$\int_{}^{}{\frac{1}{\sqrt{a^{2} - x^{2}}}dx} = \arcsin\frac{x}{a} + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\arcsin xdx} = x\arcsin x + \sqrt{1 - x^{2}} + C$

</td>
</tr>
<tr>
<td rowspan="2">

$\left( \arccos x \right)' = - \frac{1}{\sqrt{1 - x^{2}}}$

</td>
<td>

$\int_{}^{}{- \frac{dx}{\sqrt{1 - x^{2}}}} = \arccos x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\arccos xdx} = x\arccos x - \sqrt{1 - x^{2}} + C$

</td>
</tr>
<tr>
<td rowspan="2">

$\left( \arctan x \right)' = \frac{1}{1 + x^{2}}$

</td>
<td>

$\int_{}^{}\frac{dx}{a^{2} + x^{2}} = \frac{1}{a}\arctan\frac{x}{a} + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\arctan xdx} = x\arctan x - \frac{1}{2}\ln\left( 1 + x^{2} \right) + C$

</td>
</tr>
<tr>
<td rowspan="2">

$\left( {arccot}x \right)' = - \frac{1}{1 + x^{2}}$

</td>
<td>

$\int_{}^{}{- \frac{dx}{1 + x^{2}}} = {arccot}x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{{arccot}xdx} = x{arccot}x + \frac{1}{2}\ln\left( 1 + x^{2} \right) + C$

</td>
</tr>
<tr>
<td rowspan="2">

$\left( {arcsec}x \right)' = \frac{1}{|x|\sqrt{x^{2} - 1}}$

</td>
<td>

$\int_{}^{}\frac{dx}{|x|\sqrt{x^{2} - 1}} = {arcsec}x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{{arcsec}xdx} = x{arcsec}x - \ln\left( x + \sqrt{x^{2} - 1} \right) + C$

</td>
</tr>
<tr>
<td rowspan="2">

$\left( {arccot}x \right)' = - \frac{1}{|x|\sqrt{x^{2} - 1}}$

</td>
<td>

$\int_{}^{}{- \frac{dx}{|x|\sqrt{x^{2} - 1}}} = \left( {arccot}x \right)'$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{{arccsc}xdx} = x{arccsc}x + \ln\left( x + \sqrt{x^{2} - 1} \right) + C$

</td>
</tr>
<tr>
<td colspan="2">

双曲函数

</td>
</tr>
<tr>
<td>

$\left( \sinh x \right)' = \cosh x$

</td>
<td>

$\int_{}^{}{{sinh}xdx} = \cosh x + C$

</td>
</tr>
<tr>
<td>

$\left( \cosh x \right)' = \sinh x$

</td>
<td>

$\int_{}^{}{\cosh xdx} = \sinh x + C$

</td>
</tr>
<tr>
<td>

$\left( \tanh x \right)' = \frac{1}{\cosh^{2}x}$

</td>
<td>

$\int_{}^{}\frac{dx}{\cosh^{2}x} = \tanh x + C$

</td>
</tr>
<tr>
<td>

$\left( \coth x \right)' = - {csch}^{2}x$

</td>
<td></td>
</tr>
<tr>
<td>

$\left( {sech}x \right)' = - \tanh x{sech}x$

</td>
<td></td>
</tr>
<tr>
<td>

$\left( {csch}x \right)' = - \coth x{csch}x$

</td>
<td></td>
</tr>
<tr>
<td colspan="2">

反双曲函数

</td>
</tr>
<tr>
<td>

$\left( {arsh}x \right)' = \frac{1}{\sqrt{1 + x^{2}}}$

</td>
<td>

$\int_{}^{}{\frac{1}{\sqrt{1 + x^{2}}}dx} = {arsh}x + C$

</td>
</tr>
<tr>
<td>

$\left( {arch}x \right)' = \frac{1}{\sqrt{x^{2} - 1}}$

</td>
<td>

$\int_{}^{}{\frac{1}{\sqrt{x^{2} - 1}}dx} = {arch}x + C$

</td>
</tr>
<tr>
<td>

$\left( {arth}x \right)' = \frac{1}{1 - x^{2}}$

</td>
<td>

$\int_{}^{}{\frac{1}{1 - x^{2}}dx} = {arth}x + C$

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

定义：设有常数$I$，如果对于任意给定的正数$\varepsilon$，总存在一个正数$\delta$，使得对于区间$\lbrack a\text{，}b\rbrack$的任何分法，不论$\xi_{i}$在$\left\lbrack x_{i - 1}\text{，}x_{i} \right\rbrack$中怎样选取，只要$\lambda = \max\left| \Delta x_{1}\text{，}\cdots \text{，}\Delta x_{n} \right| < \delta$，总有

$\left| \sum_{i = 1}^{n}{f\left( \xi_{i} \right)\Delta x_{i}} - I \right| < \varepsilon$

成立，那么称$I$是$f(x)$在区间$\lbrack a\text{，}b\rbrack$上的定积分，记作

$I = \int_{a}^{b}{f(x)dx} = \lim_{\lambda \rightarrow 0}{\sum_{i = 1}^{n}{f\left( \xi_{i} \right)\Delta x_{i}}}$

其中$f(x)$叫做被积函数，$f(x)dx$叫做被积表达式，$x$叫做积分变量，$a$叫做积分下限，$b$叫做积分上限，$\lbrack a\text{，}b\rbrack$叫做积分区间，$\sum_{i = 1}^{n}{f\left( \xi_{i} \right)\Delta x_{i}}$叫做积分和。

这里选用$\lambda \rightarrow 0$而非$n \rightarrow + \infty$是因为分法是任意的，只有$\lambda \rightarrow 0$才能保证所有的区间都是越来越小的，否则会出现某一区间恒定而其它区间缩小的情况。

定积分的性质

积分第一中值定理

设$f(x)\text{，}g(x)$和都在$\lbrack a\text{，}b\rbrack$上可积，$g(x)$在$\lbrack a\text{，}b\rbrack$上不变号，则存在$\eta \in \lbrack m\text{，}M\rbrack$，使得

$\int_{a}^{b}{f(x)g(x)dx} = \eta\int_{a}^{b}{g(x)dx}$

其中$M$和$m$分别表示$f(x)$在$\lbrack a\text{，}b\rbrack$的上确界和下确界。

特别地，若$f(x)$在$\lbrack a\text{，}b\rbrack$上连续，则存在$\xi \in \lbrack a\text{，}b\rbrack$，使得

$\int_{a}^{b}{f(x)g(x)dx} = \eta\int_{a}^{b}{g(x)dx}$

特别地，当若$f(x)$在$\lbrack a\text{，}b\rbrack$上连续，$g(x) \equiv 1$，则存在$\xi \in \lbrack a\text{，}b\rbrack$（其实$\xi \in (a\text{，}b)$即可），使得（积分中值公式）

$\int_{a}^{b}{f(x)dx} = f(\xi)(b - a)$

积分上限函数

$\int_{a}^{x}{f(t)dt}$

有如下结论

$\frac{d}{dx}\int_{a}^{x}{f(t)dt} = f(x)\text{，}x \in \lbrack a\text{，}b\rbrack$

$\frac{d}{dx}\int_{a}^{g(x)}{f(t)dt} = f\left( \left\lbrack g(x) \right\rbrack' \right)$

$\frac{d}{dx}\int_{h(x)}^{g(x)}{f(t)dt} = f\left( \left\lbrack g(x) \right\rbrack' \right) - f\left( \left\lbrack h(x) \right\rbrack' \right)$

微积分基本定理（Newton-Leibniz（牛顿—莱布尼兹）公式）

设$f(x)$在$\lbrack a\text{，}b\rbrack$上连续，$F(x)$是$f(x)$在$\lbrack a\text{，}b\rbrack$上的一个原函数，则

$\int_{a}^{b}{f(x)dx} = F(b) - F(a) = F(x)\ \left| \begin{array}{r} b \\ a \end{array} \right.\$

有关定积分的证明题常用换元法，换元前可能需要拆分，换元有两种考虑，一种是考虑换元后的积分上限和积分下限，常用$t = \text{积分上限} - x$；另一种是考虑被积函数的性质，使得换元后函数括号内容与求证接近。

$\cdot \int_{a}^{b}{f(x)dx} = \int_{a}^{b}{f(a + b - x)dx}$

$\text{证明：}\int_{a}^{b}{f(a + b - x)dx}\overset{\ t = a + b - x\ }{\Rightarrow} - \int_{b}^{a}{f(t)dt} = \int_{a}^{b}{f(x)dx}$

$\cdot \int_{- a}^{a}{f(x)dx} = \int_{0}^{a}{\left\lbrack f(x) + f( - x) \right\rbrack dx}$

$\text{特别地，当}f(x)\text{是偶函数和奇函数时分别有}\int_{- a}^{a}{f(x)dx} = 2\int_{0}^{a}{f(x)dx}\text{，}\int_{- a}^{a}{f(x)dx} = 0$

$\text{证明：}\int_{- a}^{a}{f(x)dx} = \int_{- a}^{0}{f(x)dx} + \int_{0}^{a}{f(x)dx}\overset{\ t = - x\ }{\Rightarrow} - \int_{a}^{0}{f( - t)dt} + \int_{0}^{a}{f(x)dx} = \int_{0}^{a}{f( - x)dx} + \int_{0}^{a}{f(x)dx} = \int_{0}^{a}{\left\lbrack f(x) + f( - x) \right\rbrack dx}$

$\cdot \int_{0}^{\frac{\pi}{2}}{f\left( \sin x \right)dx} = \int_{0}^{\frac{\pi}{2}}{f\left( \cos x \right)dx}$

$\text{证明：}\int_{0}^{\frac{\pi}{2}}{f\left( \sin x \right)dx}\overset{\ t = \frac{\pi}{2} - x\ }{\Rightarrow} - \int_{\frac{\pi}{2}}^{0}{f\left\lbrack \sin\left( \frac{\pi}{2} - t \right) \right\rbrack dt} = \int_{0}^{\frac{\pi}{2}}{f\left( \cos t \right)dt} = \int_{0}^{\frac{\pi}{2}}{f\left( \cos x \right)dx}$

$\cdot \int_{0}^{\pi}{xf\left( \sin x \right)dx} = \frac{\pi}{2}\int_{0}^{\pi}{f\left( \sin x \right)dx}$

$\text{证明：}\int_{0}^{\pi}{xf\left( \sin x \right)dx}\overset{\ t = \pi - x\ }{\Rightarrow} - \int_{\pi}^{0}{(\pi - t)f\left\lbrack \sin(\pi - t) \right\rbrack dt} = \int_{0}^{\pi}{(\pi - t)f\left( \sin t \right)dt} = \pi\int_{0}^{\pi}{f\left( \sin x \right)dx} - \int_{0}^{\pi}{xf\left( \sin x \right)dx} \Rightarrow \int_{0}^{\pi}{xf\left( \sin x \right)dx} = \frac{\pi}{2}\int_{0}^{\pi}{f\left( \sin x \right)dx}$

$\cdot \int_{a}^{a + T}{f(x)dx} = \int_{0}^{T}{f(x)dx}$

$\text{证明：}\int_{a}^{a + T}{f(x)dx} = \int_{a}^{0}{f(x)dx} + \int_{0}^{T}{f(x)dx} + \int_{T}^{a + T}{f(x)dx}\overset{\ t = x - T\ }{\Rightarrow}\int_{a}^{0}{f(x)dx} + \int_{0}^{T}{f(x)dx} + \int_{0}^{a}{f(t + T)dt} = \int_{a}^{0}{f(x)dx} + \int_{0}^{T}{f(x)dx} - \int_{a}^{0}{f(x)dx} = \int_{0}^{T}{f(x)dx}$

$\text{证明：令}\Phi(a) = \int_{a}^{a + T}{f(x)dx}\text{，则}\Phi'(a) = \left\lbrack \int_{a}^{a + T}{f(x)dx} \right\rbrack' = f(a + T) - f(a) = 0$

$\text{所以}\Phi(a)\text{是一个常函数，可以取}\ \Phi(a) = \Phi(0) = \int_{0}^{T}{f(x)dx}\text{，即}\int_{a}^{a + T}{f(x)dx} = \int_{0}^{T}{f(x)dx}$

$\cdot \int_{a}^{a + nT}{f(x)dx} = n\int_{0}^{T}{f(x)dx}\ \ \left( n\mathbb{\in N} \right)$

$\text{证明：}\int_{a}^{a + nT}{f(x)dx} = \int_{a}^{a + T}{f(x)dx} + \int_{a + T}^{a + 2T}{f(x)dx} + \int_{a + 2T}^{a + 3T}{f(x)dx} + \cdots + \int_{a + (n - 1)T}^{a + nT}{f(x)dx} = n\int_{0}^{T}{f(x)dx}$

$\cdot I_{n} = \int_{0}^{\frac{\pi}{2}}{\sin^{n}xdx} = \int_{0}^{\frac{\pi}{2}}{\cos^{n}xdx} = \frac{n - 1}{n}I_{n - 2} = \left\{ \begin{array}{r} \frac{n - 1}{n} \cdot \frac{n - 3}{n - 2} \cdot \cdots \cdot \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2}\text{，}n\text{为正偶数}\ \ \ \ \ \ \ \  \\ \frac{n - 1}{n} \cdot \frac{n - 3}{n - 2} \cdot \cdots \cdot \frac{4}{5} \cdot \frac{2}{3}\text{，}n\text{为大于}1\text{的奇数} \end{array} \right.\$

$\text{其中}I_{0} = \frac{\pi}{2}\text{，}I_{1} = 1$

$\text{证明：由}\int_{0}^{\frac{\pi}{2}}{f\left( \sin x \right)dx} = \int_{0}^{\frac{\pi}{2}}{f\left( \cos x \right)dx}\text{，得}\int_{0}^{\frac{\pi}{2}}{\sin^{n}xdx} = \int_{0}^{\frac{\pi}{2}}{\cos^{n}xdx}$

$I_{n} = - \int_{0}^{\frac{\pi}{2}}{\sin^{n}xd\left( \cos x \right)} = \left\lbrack - \cos x\sin^{n - 1}x \right\rbrack_{0}^{\frac{\pi}{2}} + (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n - 2}x\cos^{2}xdx} = (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n - 2}x\left( 1 - \sin^{2}x \right)dx} = (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n - 2}xdx} - (n - 1)\int_{0}^{\frac{\pi}{2}}{\sin^{n}xdx} = (n - 1)I_{n - 2} - (n - 1)I_{n}$

得到递推式

$I_{n} = \frac{n - 1}{n}I_{n - 2}$

对$n$的奇偶分类讨论即可。

$\cdot \int_{0}^{1}{x^{m}(1 - x)^{n}dx} = \int_{0}^{1}{x^{n}(1 - x)^{m}dx}\ \ \left( m\text{，}n\mathbb{\in Z} \right)$

$\text{证明：}\int_{0}^{1}{x^{m}(1 - x)^{n}dx}\overset{t = 1 - x}{\Rightarrow} - \int_{1}^{0}{(1 - t)^{m}t^{n}dt} = \int_{0}^{1}{(1 - x)^{m}x^{n}dx}$

$\cdot \int_{\frac{n}{2}\pi}^{\frac{n + 1}{2}\pi}{f\left( \left| \sin x \right| \right)dx} = \int_{\frac{n}{2}\pi}^{\frac{n + 1}{2}\pi}{f\left( \left| \cos x \right| \right)dx} = \int_{0}^{\frac{\pi}{2}}{f(\sin x)dx}$

$\int_{\frac{n}{2}\pi}^{\frac{n + 1}{2}\pi}{f\left( \left| \sin x \right| \right)dx}\overset{t = x + \frac{\pi}{2}}{\Rightarrow}$

$\int_{a}^{b}{\frac{f(x)}{f(a + b - x) + f(x)}dx} = \frac{b - a}{2}$

$\left( \int_{a}^{b}{f(x)g(x)dx} \right)^{2} \leq \int_{a}^{b}{f^{2}(x)dx} \cdot \int_{a}^{b}{g^{2}(x)dx}$

$\left( \int_{a}^{b}{\left\lbrack f(x) + g(x) \right\rbrack^{2}dx} \right)^{\frac{1}{2}} \leq \left( \int_{a}^{b}{f^{2}(x)dx} \right)^{\frac{1}{2}} + \left( \int_{a}^{b}{g^{2}(x)dx} \right)^{\frac{1}{2}}$

$\int_{a}^{b}{f(x)dx} = - \int_{b}^{a}{f(x)dx}$

$\left| \int_{a}^{b}{f(x)dx} \right| \leq \int_{a}^{b}{\left| f(x) \right|dx}$

定积分的近似计算

设$f(x)$在$\lbrack a\text{，}b\rbrack$连续，用分点$a = x_{0}x_{1}x_{2}\cdots x_{n} = b$将$\lbrack a\text{，}b\rbrack$分成n个长度相等的区间，每个小区间的长为

$\Delta x = \frac{b - a}{n}$

记$f\left( x_{i} \right) = y_{i}$

1.矩形法

$\int_{a}^{b}{f(x)dx} \approx \frac{b - a}{n}\left( y_{1} + y_{2} + \cdots + y_{n} \right)$

2.梯形法

$\int_{a}^{b}{f(x)dx} \approx \frac{b - a}{n}\left( \frac{y_{0} + y_{n}}{2} + y_{1} + y_{2} + \cdots + y_{n} \right)$

3.抛物线法（辛普森法）

$\int_{a}^{b}{f(x)dx} \approx \frac{b - a}{3n}\left\lbrack y_{0} + y_{n} + 4\left( y_{1} + y_{3} + \cdots + y_{n - 1} \right) + 2(y_{2} + y_{4} + \cdots + y_{n - 2}) \right\rbrack$

定积分的换元积分法

设$f(x)$在区间$\lbrack a\text{，}b\rbrack$上连续，$x = \varphi(t)$在$\lbrack\alpha \text{，}\beta\rbrack$或$\lbrack\beta \text{，}\alpha\rbrack$内有连续导数$\varphi'(x)$，$f(x)$在$R_{\varphi}$上连续，且满足$\varphi(\alpha) = a$和$\varphi(\beta) = b$，则

$\int_{a}^{b}{f(x)dx} = \int_{a}^{b}{f\left( \varphi(t) \right)\varphi'(t)dt}$

定积分的分部积分法

$\int_{a}^{b}{udv} = \lbrack uv\rbrack_{a}^{b} - \int_{a}^{b}{vdu}$

极坐标下的定积分公式

$S = \int_{\alpha}^{\beta}{\frac{1}{2}\left\lbrack \rho(\theta) \right\rbrack^{2}d\theta}$

$\Gamma$函数（第二类欧拉积分）

$\Gamma(s) = \int_{0}^{+ \infty}{e^{- x}x^{s - 1}dx}$

性质

$\Gamma(s + 1) = s\Gamma(s)\ \ (s > 0)$

$\Gamma(n + 1) = n!\ \ \left( n \in \mathbb{N}^{*} \right)$

$\Gamma(s)\Gamma(1 - s) = \frac{\pi}{\sin{\pi s}}\ \ (0 < s < 1)\ \ (\text{余元公式})\text{，特别地，}\Gamma\left( \frac{1}{2} \right) = \sqrt{\pi}$

$\Gamma\left( \frac{2k + 1}{2} \right) = \frac{1 \cdot 3 \cdot 5 \cdot \cdots \cdot (2k - 1)\sqrt{\pi}}{2^{k}}\text{，}k \in \mathbb{N}_{+}$

$\beta$函数（第一类欧拉积分）

$\beta(p\text{，}q) = \int_{0}^{1}{x^{p - 1}(1 - x)^{q - 1}dx}\ \ \left( p\text{，}q \in \mathbb{N}^{*} \right)$

性质

$\beta(p\text{，}q) = \beta(q\text{，}p)$

$\beta(p\text{，}q) = \left\{ \begin{array}{r} \frac{q - 1}{p + q - 1}\beta(p\text{，}q - 1)\ \ (p > 0\text{，}q > 1)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \frac{p - 1}{p + q - 1}\beta(p - 1\text{，}q)\ \ (p > 1\text{，}q > 0)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \frac{(p - 1)(q - 1)}{(p + q - 1)(p + q - 2)}\beta(p - 1\text{，}q - 1)\ \ (p\text{，}q > 1) \end{array} \right.\$

$\beta(p\text{，}q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p + q)}$

$\beta(p\text{，}1 - p) = \Gamma(p)\Gamma(1 - p)$

$\beta(p\text{，}q) = \frac{p + q}{pqC_{p + q}^{p}} = \frac{1}{qC_{p + q + 1}^{p - 1}}\ \ \left( p\text{，}q \in \mathbb{N}^{*} \right)$

其它

定积分的元素法

一般地，如果某一实际问题中的所求量$U$符合下列条件：

（1）$U$是与一个变量$x$的变化区间$\lbrack a\text{，}b\rbrack$有关的量

（2）$U$对于区间$\lbrack a\text{，}b\rbrack$具有可加性，就是说，如果把区间$\lbrack a\text{，}b\rbrack$分成许多部分区间，则$U$相应地分成许多部分量，而$U$等于所有部分量之和。

（3）部分量$\Delta U_{i}$的近似值可表示为$f\left( \xi_{i} \right)\Delta x_{i}$，那么就可考虑用定积分来表达这个量$U$。通常写出这个量$U$的积分表达式的步骤是：

1）根据问题的具体情况，选取一个变量例如$x$为积分变量，并确定它的变化区间$\lbrack a\text{，}b\rbrack$；

2）设想把区间$\lbrack a\text{，}b\rbrack$分成$n$个小区间，取其中任一小区间$\lbrack x\text{，}x + dx\rbrack$并记作，求出相应于这个小区间的部分量$\Delta U$的近似值。如果$\Delta U$能近似地表示为$\lbrack a\text{，}b\rbrack$上的一个连续函数在$x$处的值$f(x)$与$dx$的乘积，就把$f(x)dx$称为量$U$的元素且记作$dU$，即

$dU = f(x)dx$

3）以所求量$U$的元素$f(x)dx$为被积表达式，在区间$\lbrack a\text{，}b\rbrack$上作定积分，得

$U = \int_{a}^{b}{f(x)dx}$

这就是所求量$U$的积分表达式。

平面图形的面积

旋转体的面积

平面曲线的弧长

$s = \int_{a}^{b}{\sqrt{1 + {y'}^{2}}dx}$

若

$\left\{ \begin{array}{r} x = \rho(\theta)\cos\theta \\ y = \rho(\theta)\sin\theta \end{array} \right.\$

则

$s = \int_{a}^{b}{\sqrt{\rho^{2}(\theta) + {\rho'}^{2}(\theta)}d\theta}$

微分方程

可分离变量的微分方程

$g(y)dy = f(x)dx$

有

$\int_{}^{}{g(y)dy} = \int_{}^{}{f(x)dx}$

即

$G(y) = F(x) + C$

$eg.\text{解方程}mg - kv = ma$，其中$v\left| \underset{t = 0}{} \right.\  = 0$

解：分离变量，得

$\frac{dv}{mg - kv} = \frac{dt}{m}$

由$mg - kv > 0$，两端积分，得

$- \frac{1}{k}\ln(mg - kv) = \frac{t}{m} + C_{1}$

即

$v = \frac{mg}{k} + C_{2}e^{- \frac{k}{m}t}\ \ \left( C_{2} = - \frac{e^{- kC_{1}}}{k} \right)$

代入初值条件$v\left| \underset{t = 0}{} \right.\  = 0$，得

$C_{2} = - \frac{mg}{k}$

得到

$v = \frac{mg}{k}\left( 1 - e^{- \frac{k}{m}t} \right)$

两边积分，得

$x = \frac{mg}{k}t + ge^{- \frac{k}{m}t} + C_{3}$

取$x\left| \underset{t = 0}{} \right.\  = 0$，得

$C_{3} = - g$

得到

$x = g\left( e^{- \frac{k}{m}t} - 1 \right)$

$\text{又由于}v = \frac{mg}{k}\left( 1 - e^{- \frac{k}{m}t} \right)\text{，将}1 - e^{- \frac{k}{m}t} = \frac{kv}{mg}\text{代入，得}$

$x = - \frac{k}{m}v$

这样就得到了所谓的“另类加速度”。

齐次微分方程

$\frac{dy}{dx} = \varphi\left( \frac{y}{x} \right)$

$\text{令}u = \frac{y}{x}\text{，则}\ y = xu\text{，有}$

$\frac{dy}{dx} = (xu)' = u + x\frac{du}{dx}$

因此有

$\varphi\left( \frac{y}{x} \right) = \varphi(u) = u + x\frac{du}{\ dx}$

是一个可分离变量的方程，整理得

$\frac{du}{\varphi(u) - u} = \frac{dx}{x}$

即

$\int_{}^{}{\frac{1}{\varphi\left( \frac{y}{x} \right) - \frac{y}{x}}d\left( \frac{y}{x} \right)} = \int_{}^{}\frac{dx}{x} = \ln|x| + C$

可化为齐次的微分方程

方程

$\frac{dy}{dx} = f\left( \frac{ax + by + c}{a_{1}x + b_{1}y + c_{1}} \right)$

$\text{若}\left| \begin{matrix} a & b \\ a_{1} & b_{1} \end{matrix} \right| \neq 0\text{，则令}\ x = X + h\text{，}y = Y + k\text{，则}dx = dX\text{，}dy = dY\text{，则}$

$\frac{dY}{dX} = f\left( \frac{aX + bY + ah + bk + c}{a_{1}X + b_{1}Y + a_{1}h + b_{1}k + c} \right)$

解方程

$\left\{ \begin{array}{r} ah + bk + c\ \ \ \  = 0 \\ a_{1}h + b_{1}k + c = 0 \end{array} \right.\$

得

$h = \frac{\left| \begin{matrix} - c & b \\ - c & b_{1} \end{matrix} \right|}{\left| \begin{matrix} a & b \\ a_{1} & b_{1} \end{matrix} \right|}\text{，}k = \frac{\left| \begin{matrix} a & - c \\ a_{1} & - c \end{matrix} \right|}{\left| \begin{matrix} a & b \\ a_{1} & b_{1} \end{matrix} \right|}$

$\text{若}\left| \begin{matrix} a & b \\ a_{1} & b_{1} \end{matrix} \right| = 0\text{，令}\frac{a_{1}}{a} = \frac{b_{1}}{b} = \lambda \text{，}\nu = ax + by\text{，得}$

$\frac{d\nu}{dx} = a + b\frac{dy}{dx} = a + bf\left( \frac{ax + by + c}{\lambda(ax + by) + c_{1}} \right)$

所以

$\frac{1}{b}\left( \frac{d\nu}{dx} - a \right) = f\left( \frac{\nu + c}{\lambda\nu + c_{1}} \right)$

一阶齐次线性微分方程

$\frac{dy}{dx} + P(x)y = 0$

分离变量，得

$\frac{dy}{y} = - P(x)dx$

两端积分，得

$\ln|y| = - \int_{}^{}{P(x)dx} + C$

通解

$y = Ce^{- \int_{}^{}{P(x)dx}}\ \ \left( C = \pm e^{C_{1}} \right)$

此处的$\int_{}^{}{P(x)dx}$表示$P(x)$的某个确定的原函数（即不用加常数$C$），下同。

一阶线性微分方程

$\frac{dy}{dx} + P(x)y = Q(x)\ \ y' + P(x)y = Q(x)$

的通解为

$y = e^{- \int_{}^{}{P(x)dx}}\left( \int_{}^{}{Q(x)e^{\int_{}^{}{P(x)dx}}dx} + C \right)$

$= \exp\left( - \int_{}^{}{P(x)dx} \right)\left( \int_{}^{}{Q(x)\exp\left( \int_{}^{}{P(x)dx} \right)dx} + C \right)$

$y = Ce^{- \int_{}^{}{P(x)dx}} + e^{- \int_{}^{}{P(x)dx}}\int_{}^{}{Q(x)e^{\int_{}^{}{P(x)dx}}dx}$

证明：常数变易法

$\text{设}y = ue^{- \int_{}^{}{P(x)dx}}\text{是方程}\frac{dy}{dx} + P(x)y = Q(x)\text{的通解}\ \left. \text{（}u\text{是所谓}``\text{变易}"\text{的函数} \right.\text{）}\ \text{，则}$

$\frac{dy}{dx} = u'e^{- \int_{}^{}{P(x)dx}} - uP(x)e^{- \int_{}^{}{P(x)dx}}$

$\text{将}y = ue^{- \int_{}^{}{P(x)dx}}\text{和}\ \frac{dy}{dx} = u'e^{- \int_{}^{}{P(x)dx}} - uP(x)e^{- \int_{}^{}{P(x)dx}}\text{代入}\ \frac{dy}{dx} + P(x)y = Q(x)\text{，得}$

$u'e^{- \int_{}^{}{P(x)dx}} - uP(x)e^{- \int_{}^{}{P(x)dx}} + P(x)ue^{- \int_{}^{}{P(x)dx}} = Q(x)$

后两项抵消，得

$u'e^{- \int_{}^{}{P(x)dx}} = Q(x)$

$u' = Q(x)e^{\int_{}^{}{P(x)dx}}$

两端积分，得

$u = \int_{}^{}{Q(x)e^{\int_{}^{}{P(x)dx}}dx} + C$

把这个结果代入$y = ue^{- \int_{}^{}{P(x)dx}}$，得

$y = e^{- \int_{}^{}{P(x)dx}}\left( \int_{}^{}{Q(x)e^{\int_{}^{}{P(x)dx}}dx} + C \right) = Ce^{- \int_{}^{}{P(x)dx}} + e^{- \int_{}^{}{P(x)dx}}\int_{}^{}{Q(x)e^{- \int_{}^{}{P(x)dx}}dx}$

这个证明过程类似于“原函数与导函数混合还原”中等号右边为非0式的做法。

伯努利方程

$\frac{dy}{dx} + P(x)y = Q(x)y^{n}$

两边同除$y^{n}$，得

$y^{- n}\frac{dy}{dx} + P(x)y^{1 - n} = Q(x)$

令$z = y^{1 - n}$，对z求导得

$\frac{dz}{dy} = (1 - n)y^{- n}\frac{dy}{dx}$

将该式代入上式，得

$y^{- n}\frac{1}{(1 - n)y^{- n}}\frac{dz}{dx} + P(x)y^{1 - n} = Q(x)$

两边同乘$(1 - n)$，并把$y^{1 - n}$代为z，得

$\frac{dz}{dx} + (1 - n)P(x)z = (1 - n)Q(x)$

此式为一阶线性方程，其通解为

$y^{1 - n} = Ce^{- \int_{}^{}{(1 - n)P(x)dx}} + e^{- \int_{}^{}{(1 - n)P(x)dx}}\int_{}^{}{(1 - n)Q(x)e^{- \int_{}^{}{(1 - n)P(x)dx}}dx}$

记$g(x) = - \int_{}^{}{(1 - n)P(x)dx}$，则其可表示为

$y^{1 - x} = Ce^{g(x)} + e^{g(x)}\int_{}^{}{(1 - n)Q(x)e^{g(x)}dx}$

可降阶的高阶微分方程

1.

$y^{(n)} = f(x)$

连续积分即得

2.

$y^{''} = f\left( x\text{，}y' \right)$

令$p = y'$，得

$p' = f(x\text{，}p)$

此是关于x和p的一阶微分方程，如果能求得其通解

$p = \varphi\left( x\text{，}C_{1} \right)$

则原方程的通解为

$y = \int_{}^{}{\varphi\left( x\text{，}C_{1} \right)dx} + C_{2}$

3.

$y^{''} = f\left( y\text{，}y' \right)$

令$p = y'$，得

$y^{''} = \frac{dp}{dx} = \frac{dp}{dy}\frac{dy}{dx} = p\frac{dp}{dy}$

代入原方程得

$p\frac{dp}{dy} = f\left( y\text{，}y' \right)$

此是关于y和p的一阶微分方程，如果能求得其通解

$p = \varphi\left( y\text{，}C_{1} \right)$

则原方程的通解为

$\int_{}^{}\frac{dy}{\varphi\left( y\text{，}C_{1} \right)} = x + C_{2}$

二阶常系数齐次线性微分方程

$y^{''} + py' + qy = 0$

考虑特征方程

$r^{2} + pr + q = 0$

（1）当$\Delta > 0$时，有两个不等实根

$r_{1} = \frac{- p + \sqrt{p^{2} - 4q}}{2}\text{，}r_{2} = \frac{- p - \sqrt{p^{2} - 4q}}{2}$

此时方程的通解为

$y = C_{1}e^{r_{1}x} + C_{2}e^{r_{2}x}$

（2）当$\Delta = 0$时，有两个等根

$r = - \frac{p}{2}$

此时方程的通解为

$y = \left( C_{1} + C_{2}x \right)e^{rx}$

（3）当$\Delta < 0$时，有两个共轭复根

$r_{1} = \alpha + \beta i\text{，}r_{2} = \alpha - \beta i$

其中

$\alpha = - \frac{p}{2}\text{，}\beta = \frac{\sqrt{4q - p^{2}}}{2}$

此时方程的通解为

$t = e^{\alpha x}\left( C_{1}\cos{\beta x} + C_{2\ }\sin{\beta x} \right)$

$eg.\text{解方程} - kx = ma\text{，其中}x\left| \underset{t = 0}{} \right.\  = x_{0}\text{，}v\left| \underset{t = 0}{} \right.\  = v_{0}$

解：方程可化为

$\frac{d^{2}x}{dt^{2}} + \frac{k}{m}x = 0$

其特征方程

$r^{2} + \frac{k}{m} = 0$

的根为

$r = \pm \sqrt{\frac{k}{m}}i$

因此方程的通解为

$x = C_{1}\cos\left( \sqrt{\frac{k}{m}}t \right) + C_{2}\sin\left( \sqrt{\frac{k}{m}}t \right)$

代入初值条件$x\left| \underset{t = 0}{} \right.\  = x_{0}\text{，}v\left| \underset{t = 0}{} \right.\  = v_{0}$，得到$C_{1} = x_{0}\text{，}C_{2} = v_{0}\sqrt{\frac{m}{k}}$，得

$x = x_{0}\cos\left( \sqrt{\frac{k}{m}}t \right) + v_{0}\sqrt{\frac{m}{k}}\sin\left( \sqrt{\frac{k}{m}}t \right) = \sqrt{x_{0}^{2} + \frac{m}{k}v_{0}^{2}\ }\sin\left( \sqrt{\frac{k}{m}}t + \varphi \right)$

因此，简谐运动的振幅$A = \sqrt{x_{0}^{2} + \frac{m}{k}v_{0}^{2}}$，频率$\omega = \sqrt{\frac{k}{m}}$，周期$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}$。

不难发现，小角度单摆的$T = 2\pi\sqrt{\frac{m}{k'}} = 2\pi\sqrt{\frac{m}{\frac{mg}{l}}} = 2\pi\sqrt{\frac{l}{g}}$

二阶常系数非齐次线性微分方程

$y^{''} + py' + q = f(x)$

（1）$f(x) = e^{\lambda x}P_{m}(x)$，其中

$P_{m}(x) = a_{0} + a_{1}x + a_{2}x^{2} + \cdots + a_{m}x^{m}\ \ \ \left. \text{（即}P_{m}(x)\text{的次数为}m \right.\text{）}$

考虑特征方程

$r^{2} + pr + q = 0$

则方程的一个特解为

$y^{*} = x^{k}e^{\lambda x}R_{m}(x)$

其中$R_{m}(x)$是与$P_{m}(x)$同次（m次）的多项式（系数全部待定），k按照$\lambda$不是特征方程的根、是特征方程的单根$\left( \lambda \neq - \frac{p}{2} \right)$或是特征方程的重根$\left( \lambda = - \frac{p}{2} \right)$依次取0、1或2。换种表述如下：

$R_{m}(x) = b_{0} + b_{1}x + b_{2}x^{2} + \cdots + b_{m}x^{m}\text{，}k = \left\{ \begin{array}{r} 0\text{，}\lambda \neq r_{1} \neq r_{2}\ \ \ \  \\ 1\text{，}\lambda = r_{12} \neq r_{21} \\ 2\text{，}\lambda \neq r_{1} \neq r_{2}\ \ \ \ \end{array} \right.\$

（2）$f(x) = e^{\lambda x}\left\lbrack P_{l}(x)\cos{\omega x} + Q_{n}(x)\sin{\omega x} \right\rbrack$，其中$\lambda \text{，}\omega$是常数，$\omega \neq 0$，$P_{l}(x)$、$Q_{n}(x)$分别是x的l次、n次多项式，且仅有一个可为零

考虑特征方程

$r^{2} + pr + q = 0$

则方程的一个特解为

$y^{*} = x^{k}e^{\lambda x}\left\lbrack R_{m}^{(1)}(x)\cos{\omega x} + R_{m}^{(2)}(x)\sin{\omega x} \right\rbrack$

其中$R_{m}^{(1)}(x)$、$R_{m}^{(2)}(x)$是m次多项式，$m = \max\left\{ l\text{，}n \right\}$，而k按照$\lambda + \omega i\text{或}(\lambda - \omega i)$不是特征方程的根、或是特征方程的单根依次取0或1。

求解时，为了得到$R_{m}(x)$各系数的值，可以将其代入原方程求得系数的值（即待定系数法）。

n阶常系数齐次线性微分方程

$y^{(n)} + p_{1}y^{(n - 1)} + p_{2}y^{(n - 2)} + \cdots + p_{n - 1}y' + p_{n}y = 0$

$\text{记}D = \frac{d}{dx}\text{，}Dy = \frac{dy}{dx}\text{，}D^{n}y = \frac{d^{n}y}{dx^{n}}\text{，则}$

$L(D) = D^{n} + p_{1}D^{n - 1} + \cdots + p_{n - 1}D + p_{n} = 0$

考虑特征方程

$r^{n} + p_{1}r^{n - 1} + p_{2}r^{n - 2} + \cdots + p_{n - 1}r + p_{n} = 0$

对应情况如下

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

特征方程的根

</th>
<th>

微分方程通解中的对应项

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

单实根r

</td>
<td>

给出一项： $Ce^{rx}$

</td>
</tr>
<tr>
<td>

一对单复根$r_{1,2} = \alpha \pm \beta i$

</td>
<td>

给出两项： $e^{\alpha x}\left( C_{1}\cos{\beta x} + C_{2}\sin{\beta x} \right)$

</td>
</tr>
<tr>
<td>

k重实根r

</td>
<td>

给出k项： $e^{rx}\left( C_{1} + C_{2}x + \cdots + C_{k}x^{k - 1} \right)$

</td>
</tr>
<tr>
<td>

一对k重复根$r_{1,2} = \alpha \pm \beta i$

</td>
<td>

给出2k项：$e^{\alpha x}\left\lbrack \left( C_{1} + C_{2}x + \cdots + C_{k}x^{k - 1} \right)\cos{\beta x} + \left( D_{1} + D_{2}x + \cdots + D_{k}x^{k - 1} \right)\sin{\beta x} \right\rbrack$

</td>
</tr>
</tbody>
</table>
</div>

n阶常系数非齐次线性微分方程

$y^{(n)} + p_{1}y^{(n - 1)} + p_{2}y^{(n - 2)} + \cdots + p_{n - 1}y' + p_{n}y = f(x)$

（1）$f(x) = e^{\lambda x}P_{m}(x)$，其中

$P_{m}(x) = a_{0}x^{m} + a_{1}x^{m - 1} + \cdots + a_{m - 1}x + a_{m}$

考虑特征方程

$r^{n} + p_{1}r^{n - 1} + p_{2}r^{n - 2} + \cdots + p_{n - 1}r + p_{n} = 0$

则方程的一个特解为

$y^{*} = x^{k}e^{\lambda x}R_{m}(x)$

其中$R_{m}(x)$是与$P_{m}(x)$同次（m次）的多项式，$k$按照$\lambda$不是特征方程的根或是特征方程的$s$重根取0或s

（2）$f(x) = e^{\lambda x}\left\lbrack P_{l}(x)\cos{\omega x} + Q_{n}(x)\sin{\omega x} \right\rbrack$，其中$\lambda \text{，}\omega$是常数，$\omega \neq 0$，$P_{l}(x)$、$Q_{n}(x)$分别是$x$的$l$次、$n$次多项式，且仅有一个可为零

考虑特征方程

$r^{n} + p_{1}r^{n - 1} + p_{2}r^{n - 2} + \cdots + p_{n - 1}r + p_{n} = 0$

则方程的一个特解为

$y^{*} = x^{k}e^{\lambda x}\left\lbrack R_{m}^{(1)}(x)\cos{\omega x} + R_{m}^{(2)}(x)\sin{\omega x} \right\rbrack$

其中$R_{m}^{(1)}(x)$、$R_{m}^{(2)}(x)$是$m$次多项式，$m = \max\left\{ l\text{，}n \right\}$，而$k$按照$\lambda + \omega i\text{或}(\lambda - \omega i)$不是特征方程的根、或是特征方程的$s$重根取$0$或$s$。

欧拉方程

$x^{n}y^{(n)} + p_{1}x^{n - 1}y^{(n - 1)} + p_{2}x^{n - 2}y^{(n - 2)} + \cdots + p_{n - 1}xy' + p_{n}y = f(x)$

当$x > 0$时，令$t = \ln x$，得（当$x < 0$时，令$t = \ln( - x)$）

$\frac{dy}{dx} = \frac{dy}{dx} \cdot \frac{dt}{dx} = \frac{1}{x}\frac{dy}{dt}$

线性微分方程的解的结构

二阶齐次线性微分方程

定理1：二阶齐次线性微分方程的两个解的线性组合也是该二阶齐次线性微分方程的解。

若$y_{1}(x)\text{、}y_{2}(x)$满足$y^{''} + P(x)y' + Q(x)y = 0$，则解$C_{1}y_{1}(x) + C_{2}y_{2}(x)$亦满足该方程。

定理2：二阶齐次线性微分方程的两个线性无关的解（不一定是“特解”）的线性组合是该二阶齐次线性微分方程的通解。

> $\text{若两特解}y_{1}(x)\text{、}y_{2}(x)\text{满足}y_{1}(x) \neq ky_{2}(x)\text{，则}y^{''} + P(x)y' + Q(x)y = 0\text{的通解为}C_{1}y_{1}(x) + C_{2}y_{2}(x)$

二阶非齐次线性微分方程

定理3：二阶非齐次线性微分方程的一个解（不一定是“特解”）加上对应的二阶齐次线性微分方程的通解是该二阶非齐次线性微分方程的通解。（即$y = Y + y^{*}$）

定理4（叠加原理）：把一个二阶非齐次线性微分方程的自由项拆成两个函数，形成的两个新的二阶非齐次线性微分方程的特解的和是原二阶非齐次线性微分方程的一个特解。

若$y_{1}^{*}$和$y_{2}^{*}$分别是$y^{''} + P(x)y' + Q(x)y = f_{1}(x)$和$y^{''} + P(x)y' + Q(x)y = f_{2}(x)$的特解，则$y_{1}^{*} + y_{2}^{*}$是$y^{''} + P(x)y' + Q(x)y = f_{1}(x) + f_{2}(x)$的特解。

$n$阶线性微分方程

定理1：$n$阶齐次线性微分方程的$n$个线性无关的特解的线性组合是该$n$阶齐次线性微分方程的通解。

定理2：$n$阶非齐次线性微分方程的一个解（不一定是“特解”）加上对应的$n$阶齐次线性微分方程的通解是该$n$阶非齐次线性微分方程的通解。

定理3：把一个$n$阶非齐次线性微分方程的自由项拆成两个函数，形成的两个新的$n$阶非齐次线性微分方程的特解的和是原$n$阶非齐次线性微分方程的一个特解。

解题时常用到如下的一个结论

若$y_{1}(x)\text{、}y_{2}(x)$是$n$阶非齐次线性微分方程的两个解，则$y_{1}(x) - y_{2}(x)$是对应的$n$阶齐次线性微分方程的解。

一般来说，题目通常会给出二阶非齐次线性微分方程的三个解，这就需要合理地对这三个解做差以找出线性无关的二阶齐次线性微分方程的两个解，这样就找到了二阶齐次线性微分方程的通解，进而得到二阶非齐次线性微分方程的通解。

常系数线性微分方程组

（1）从方程组中校消去一些未知函数及其各阶导数，得到只含有一个未知函数的高阶常系数线性微分方程。

（2）解此高阶微分方程，求出满足该方程的未知函数。

（3）把已求得都函数代入原方程组，一般来说，不必经过积分就可求出其余的未知函数

现将这些方程的解总结如下

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

类型

</th>
<th>

表达式

</th>
<th>

特解

</th>
<th>

通解

</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

傅里叶级数

设周期为$2l$的周期函数$f(x)$满足如下条件（收敛定理的条件）：

（1）在一个周期内连续或只有有限个第一间断点，

（2）在一个周期内至多只有有限个极值点。

则其有傅里叶级数展开式，其为

$f(x) = \frac{a_{0}}{2} + \sum_{n = 1}^{\infty}\left( a_{n}\cos\frac{n\pi x}{l} + b_{n}\sin\frac{n\pi x}{l} \right)\ \ (x \in C)$

其中

${a_{n} = \frac{1}{l}\int_{- l}^{l}{f(x)\cos\frac{n\pi x}{l}dx}\ \ (n = 0\text{，}1\text{，}2\text{，}\cdots) }{b_{n} = \frac{1}{l}\int_{- l}^{l}{f(x)\sin{\frac{n\pi x}{l}dx}}\ \ (n = 0\text{，}1\text{，}2\text{，}\cdots) }{C = \left\{ x\left| f(x) = \frac{1}{2}\left\lbrack f\left( x^{-} \right) + f\left( x^{+} \right) \right\rbrack \right.\  \right\}}$

当$f(x)$为奇函数时，

$f(x) = \sum_{n = 1}^{\infty}{b_{n}\sin\frac{n\pi x}{l}}\ \ (x \in C)$

其中

$b_{n} = \frac{2}{l}\int_{0}^{l}{f(x)\sin{\frac{n\pi x}{l}dx}}\ \ (n = 0\text{，}1\text{，}2\text{，}\cdots)$

当$f(x)$为偶函数时，

$f(x) = \frac{a_{0}}{2} + \sum_{n = 1}^{\infty}{a_{n}\cos\frac{n\pi x}{l}}\ \ (x \in C)$

其中

$a_{n} = \frac{2}{l}\int_{0}^{l}{f(x)\cos{\frac{n\pi x}{l}dx}}\ \ (n = 0\text{，}1\text{，}2\text{，}\cdots)$

$eg.$若$f(x)$的周期为$2\pi$，在$\lbrack - \pi \text{，}\pi)$上的表达式为$f(x) = |x|$，则其傅里叶级数为

$f(x) = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k = 1}^{\infty}{\frac{1}{(2k - 1)^{2}}\cos{(2k - 1)x}}\ \ ( - \infty < x < + \infty)$

利用其能得到

$|x| = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k = 1}^{\infty}{\frac{1}{(2k - 1)^{2}}\cos{(2k - 1)x}}\ \ ( - \pi \leq x \leq \pi)$

令$x = 0$，得

$\sum_{k = 1}^{\infty}\frac{1}{(2k - 1)^{2}} = \frac{\pi^{2}}{8}$

设

> $\sigma = 1 + \frac{1}{2^{2}} + \frac{1}{3^{3}} + \frac{1}{4^{2}} + \cdots + \frac{1}{n^{2}} + \cdots$
>
> $\sigma_{1} = 1 + \frac{1}{3^{2}} + \frac{1}{5^{2}} + \cdots + \frac{1}{(2n - 1)^{2}} + \cdots\left( = \frac{\pi^{2}}{8} \right)$
>
> $\sigma_{2} = \frac{1}{2^{2}} + \frac{1}{4^{2}} + \frac{1}{6^{2}} + \cdots + \frac{1}{(2n)^{2}} + \cdots$
>
> $\sigma_{3} = 1 - \frac{1}{2^{2}} + \frac{1}{3^{2}} - \frac{1}{4^{2}} + \cdots + ( - 1)^{n - 1}\frac{1}{n^{2}} + \cdots$

因为

$\sigma_{2} = \frac{\sigma}{4} = \frac{\sigma_{1} + \sigma_{2}}{4}$

所以

$\sigma_{2} = \frac{\sigma_{1}}{3} = \frac{\pi^{2}}{24}\text{，}\sigma = \sigma_{1} + \sigma_{2} = \frac{\pi^{2}}{8} + \frac{\pi^{2}}{24} = \frac{\pi^{2}}{6}$

并且

$\sigma_{3} = 2\sigma_{1} - \sigma = \frac{\pi^{2}}{4} - \frac{\pi^{2}}{6} = \frac{\pi^{2}}{12}$

$\text{若}g(x)\sim ax^{m}\text{，}f(x)\sim bx^{n}\text{，则}\int_{0}^{g(x)}{f(t)dt}\sim\int_{0}^{ax^{m}}{bt^{n}dt}$

斯特林公式

$\lim_{n \rightarrow + \infty}\frac{e^{n}n!}{n^{n}\sqrt{n}} = \sqrt{2\pi}$

用它可以近似$n!$

$n! = \lim_{n \rightarrow + \infty}\frac{n^{n}\sqrt{2\pi n}}{e^{n}}$

当n很大时，亦即

$n! = \sqrt{2\pi n}\left( \frac{n}{e} \right)^{n}$

$eg.20! = 2,432,902,008,176,640,000 \approx 2,422,786,846,761,135,000$

$50! = 3.0414093201713884 \times 10^{64} \approx 3.036344593938168 \times 10^{64}$

直角坐标系下二重积分的累次计算方法

1.调换面积元素

$\iint_{D}^{}{f(x\text{，}y)d\sigma} = \iint_{D}^{}{f(x\text{，}y)dxdy}$

2.选择积分次序

> 先$y$后$x$

$\iint_{D}^{}{f(x\text{，}y)dxdy} = \int_{}^{}{dx\int_{}^{}{f(x\text{，}y)dy}}$

> 先$x$后$y$

$\iint_{D}^{}{f(x\text{，}y)dxdy} = \int_{}^{}{dy\int_{}^{}{f(x\text{，}y)dx}}$

3.确定积分上下限

后计算的积分（即靠左的积分）的上下限由其被积表达式的变量对应的取值范围决定，先计算的积分（即靠右的积分）的上下限由D的边界的函数表达式决定，最后形式为。

> 先$y$后$x$

$\iint_{D}^{}{f(x\text{，}y)dxdy} = \int_{a}^{b}{dx\int_{\varphi_{1}(x)}^{\varphi_{2}(x)}{f(x\text{，}y)dy}}$

> 先$x$后$y$

$\iint_{D}^{}{f(x\text{，}y)dxdy} = \int_{a}^{b}{dy\int_{\psi_{1}(y)}^{\psi_{2}(y)}{f(x\text{，}y)dx}}$

其中$a\text{，}b$为不随$x\text{，}y$变化的常数。$\varphi_{1}(x)$和$\varphi_{2}(x)$是$D$的“下上边界”对应的$y$关于$x$的函数，$\psi_{1}(y)$和$\psi_{2}(y)$是$D$的“左右边界”分别对应的$y$关于$x$的函数。

计算两次定积分即得。

$eg.\iint_{D}^{}{d\sigma}\text{，其中}D\text{由直线}y = 1\text{，}x = 2\text{，}y = x\text{围成。}$

解：先$y$后$x$：

$\iint_{D}^{}{f(x\text{，}y)d\sigma} = \int_{1}^{2}{dx\int_{1}^{x}{xydy}} = \int_{1}^{2}{\left\lbrack \frac{1}{2}xy^{2} \right\rbrack_{1}^{x}dx} = \int_{1}^{2}{\left( \frac{1}{2}x^{3} - \frac{1}{2}x \right)dx} = \left\lbrack \frac{x^{4}}{8} - \frac{x^{2}}{4} \right\rbrack_{1}^{2} = \frac{9}{8}$

先$x$后$y$：

$\iint_{D}^{}{f(x\text{，}y)d\sigma} = \int_{1}^{2}{dy\int_{y}^{2}{xydx}} = \int_{1}^{2}{\left\lbrack \frac{1}{2}yx^{2} \right\rbrack_{y}^{2}dy} = \int_{1}^{2}{\left( 2y - \frac{1}{2}y^{3} \right)dy} = \left\lbrack y^{2} - \frac{y^{4}}{8} \right\rbrack_{1}^{2} = \frac{9}{8}$

$eg.\iint_{D}^{}{\frac{x^{2}}{y^{2}}d\sigma}\text{，其中}D\text{由直线}y = x\text{，}x = 2\text{，}xy = 1\text{围成。}$

解：先$y$后$x$：

$\iint_{D}^{}{f(x\text{，}y)d\sigma} = \int_{1}^{2}{x^{2}dx\int_{\frac{1}{x}}^{x}{\frac{1}{y^{2}}dy}} = \int_{1}^{2}{x^{2}\left\lbrack - \frac{1}{y} \right\rbrack_{\frac{1}{x}}^{x}dx} = \int_{1}^{2}{\left( x^{3} - x \right)dx}$

先$x$后$y$：

${\iint_{D}^{}{f(x\text{，}y)d\sigma} = \int_{\frac{1}{2}}^{2}{\frac{1}{y^{2}}dy\int_{?}^{2}{x^{2}dx}} }{= \iint_{D_{1}}^{}{\frac{x^{2}}{y^{2}}d\sigma} + \iint_{D_{2}}^{}{\frac{x^{2}}{y^{2}}d\sigma} }{= \int_{\frac{1}{2}}^{2}{\frac{1}{y^{2}}dy\int_{\frac{1}{y}}^{2}{x^{2}dx}} + \int_{\frac{1}{2}}^{2}{\frac{1}{y^{2}}dy\int_{y}^{2}{x^{2}dx}}}$

三重积分

$\iiint_{\Omega}^{}{f(x\text{，}y\text{，}z)dv}$

1.化为一个定积分嵌套于一个二重积分中

$\iiint_{\Omega}^{}{f(x\text{，}y\text{，}z)dv} = \iint_{D}^{}{dxdy\int_{z_{1}(x,y)}^{z_{2}(x,y)}{f(x\text{，}y\text{，}z)dz}}$

其中$D$是垂直于$z$轴平面的平面切立体得到的平面，$z_{1}(x,\ y)$和$z_{2}(x,y)$是立体的上下边界面（从z轴方向看）。

2.化为一个二重积分嵌套于一个定积分中

$\iiint_{\Omega}^{}{f(x\text{，}y\text{，}z)dv} = \int_{c_{1}}^{c_{2}}{dz\iint_{D}^{}{f(x\text{，}y\text{，}z)dxdy}}$

其中$D$是垂直于$z$轴平面的平面切立体得到的平面，$c_{1}$和$c_{2}$是立体的$z$坐标的最小值和最大值。

3.利用柱坐标计算

根据柱坐标变换公式

$\left\{ \begin{array}{r} x = \rho\cos\theta \\ y = \rho\sin\theta \\ z = z\ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

有

$\iiint_{\Omega}^{}{f(x\text{，}y\text{，}z)dv} = \iiint_{\Omega}^{}{f\left( \rho\cos\theta \text{，}\rho\sin\theta \text{，}z \right)\rho d\rho d\theta dz}$

4.利用球坐标计算

根据球坐标变换公式

$\left\{ \begin{array}{r} x = r\sin\varphi\cos\theta\ \ \ \ \ \ \ \ \ \  \\ y = r\sin\varphi\sin\theta\ \ \ \ \ \ \ \ \ \ \  \\ z = r\cos\varphi\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ dv = r^{2}\sin\varphi drd\varphi d\theta \end{array} \right.\$

$\iiint_{\Omega}^{}{f(x\text{，}y\text{，}z)dv} = \iiint_{\Omega}^{}{f\left( r\sin\varphi\cos\theta \text{，}r\sin\varphi\sin\theta \text{，}r\cos\varphi \right)r^{2}\sin\varphi drd\varphi d\theta}$

级数

性质：收敛+收敛=收敛

收敛+发散=发散

发散+发散=不定

任意加括号

任意去添有限项

必要条件：$\lim_{n \rightarrow \infty}u_{n} = 0$

正项级数
