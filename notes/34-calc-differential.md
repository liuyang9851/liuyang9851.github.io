---
title: 导数与微分
description: 一元函数的导数与微分、多元函数的偏导数、向量值函数的导数、高阶导数、复合与反函数求导、参数方程与极坐标下的导数、全微分与微分近似、多元复合函数求导、全微分形式不变性。
---

# 导数与微分

[[toc]]

导数与微分

导数与微分一体两面，虽然微积分以微分和积分著称，但实际中导数先于微分的概念出现，导数也较微分更常使用。导数和微分分别从变化率和增量两方面探究函数的性质，最后可以发现两者的统一。

导数的定义

一元函数的导数

设函数y = f(x)在点x0的某个邻域内有定义，当自变量x在x0处取得增量Δx（点x0 + Δx仍在该邻域内）时，相应地，因变量取得增量Δy = f(x0 + Δx) − f(x0)；如果Δy与Δx之比当Δx → 0时的极限存在，那么称函数y = f(x)在点x0处可导，并称这个极限为函数y = f(x)在点x0处的导数，记为f′(x)，即

$$f'\left( x_{0} \right) = \lim_{\mathrm{\Delta}x \rightarrow 0}\frac{\mathrm{\Delta}y}{\mathrm{\Delta}x} = \lim_{\mathrm{\Delta}x \rightarrow 0}\frac{f\left( x_{0} + \mathrm{\Delta}x \right) - f\left( x_{0} \right)}{\mathrm{\Delta}x}$$

$$\text{也可记作}y'\left. \  \right|_{x = x_{0}}\text{，}\frac{dy}{dx}\left| \begin{array}{r}
 \\
\underset{x = x_{0}}{}
\end{array} \right.\ \text{或}\frac{df(x)}{dx}\left| \begin{array}{r}
 \\
\underset{x = x_{0}}{}
\end{array} \right.\ $$

于是得到导函数的定义式

$$y' = y_{x} = y_{x}' = f'(x) = f_{x}'(x) = \frac{dy}{dx} = \frac{df(x)}{dx} = \lim_{\mathrm{\Delta}x \rightarrow 0}\frac{f(x + \mathrm{\Delta}x) - f(x)}{\mathrm{\Delta}x}$$

且有

f′(x0) = f′(x) |x = x0

微分的定义

微分的定义在目前几乎是无法讲得清楚的，现在几乎所有的高数教材和数学分析的定义都有不足。下面是同济高数的定义：

一元函数的微分

设函数y = f(x)在点x0的某个邻域内有定义，当自变量x在x0处取得增量Δx（点x0 + Δx仍在该邻域内）时，相应地，因变量取得增量Δy = f(x0 + Δx) − f(x0)，若存在只与x0有关而与Δx无关的数g(x0)，满足

Δy = g(x0)Δx + o(Δx)

则称f(x)在x0处的微分存在，亦称f(x)在x0处可微。

定义dx = Δx，dy = limΔx → 0Δy = limΔx → 0g(x0)Δx + o(Δx) = g(x0)dx

下面举一例来说明这个定义的问题：令y = x2，  x = t3，则有

dy = 2xΔx， Δx = 3t2Δt + o(Δt)，

dy = 2t3(3t2Δt + o(Δt)) = 6t5Δt + 2t3o(Δt)

但由y = x2 = (t3)2 = t6，得

dy = 6t5Δt

可以发现，无穷小量2t3o(Δt)消失了，这是一个矛盾。

dy和dx不能被简单认识为变量、函数或是→ 0的一个过程，而是“微分形式”，可以参考：为什么几乎所有教科书上对微分的讲解都不明不白？ - 王泰翔的回答 - 知乎

https://www.zhihu.com/question/438795295/answer/2394202555

多元函数的偏导数

对于二元函数z = f(x，y)，定义偏导数

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

向量值函数的导数

对向量值函数y = f(x)，即
