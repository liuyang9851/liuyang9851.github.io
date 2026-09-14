---
title: 函数再研究
description: 映射的定义、函数的全局与局部性质、闭区间上连续函数的性质、连续与间断、可导函数、多元函数、向量值函数。
---

# 函数再研究

[[toc]]

函数再研究

映射的定义

设X、Y是两个非空集合，如果存在一个法则f，使得对X中每一个元素，按法则f，在Y中有唯一确定的元素y与之对应，那么称f为从X到Y的映射，记作

f : X → Y

其中y称为元素x（在映射f下）的像，并记作f(x)，即

y = f(x)

而元素x称为元素y（在映射f下）的一个原像（逆像）；集合X称为映射的定义域；记作Df，即Df = X；X中的所有元素的像所组成的集合称为映射f的值域，记作Rf或f(X)，即

Rf = f(X) = {f(x)|x ∈ X}

函数的全局性质

函数的一般性质

闭区间上连续函数的性质

函数在某点的性质：连续与可导

函数的连续与间断

$$\text{间断点}\left\{ \begin{array}{r}
\text{第一类间断点}\left. \text{（左右极限都存在} \right.\text{）}\left\{ \begin{array}{r}
\text{可去间断点：}\lim_{x \rightarrow x_{0}^{-}}{f(x)} = \lim_{x \rightarrow x_{0}^{+}}{f(x)}\left\{ \begin{array}{r}
 \neq f\left( x_{0} \right)\ \ \ \ \ \ \ \ \  \\
f\left( x_{0} \right)\text{无定义}
\end{array} \right.\ \ \ \  \\
\text{不可去间断点}\left. \text{（跳跃间断点} \right.\text{）：}\lim_{x \rightarrow x_{0}^{-}}{f(x)} \neq \lim_{x \rightarrow x_{0}^{+}}{f(x)}
\end{array} \right.\ \ \ \ \ \ \ \  \\
\text{第二类间断点}\left. \text{（左右极限至少有一个不存在} \right.\text{）}\left\{ \begin{array}{r}
\text{无穷间断点：}\lim_{x \rightarrow x_{0}^{-}}{f(x)} = \infty\lim_{x \rightarrow x_{0}^{+}}{f(x)} = \infty \\
\text{振荡间断点：}\lim_{x \rightarrow x_{0}}{f(x)}\text{振荡}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ \ \  \\
\text{瑕点：}f(x)\text{无界}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
\end{array} \right.\ $$

可导函数

函数f(x)图像的绘制

多元函数

n维向量x = (x1，x2，⋯，xn)到点集的映射称为多元函数，记作y = f(x) = f(x1，x2，⋯，xn)，常见的二元函数可记为z = f(x，y)。

向量值函数

n维向量x = (x1，x2，⋯，xn)到m维向量y = (y1，y2，⋯，ym)的映射称为n元m维向量值函数（多元函数组），记作y = f(x)。利用多元函数可以写为：

$$\left\{ \begin{array}{r}
y_{1} = f_{1}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right) \\
y_{2} = f_{2}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right) \\
\cdots \\
y_{m} = f_{m}\left( x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n} \right)
\end{array} \right.\ $$

其中f1，f2，⋯，fm代表不同的多元函数。

特别地，当n = 1时，称为一元向量值函数：

r = f(t)

常考虑m = 3的情况，即

r = f(t) = f1(t)i + f2(t)j + f3(t)k
