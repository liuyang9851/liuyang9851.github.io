---
title: 信息论基础
description: 自信息、信息熵、互信息、相对熵的定义与性质。
---

# 信息论基础

[[toc]]

### 自信息

一个概率为$p(x)$的具体事件发生时，蕴含了多大的"惊人程度"或信息量。

当事件发生以前，等于事件发生的不确定性的大小；当事件发生以后，表示事件所含有或所能提供的信息量。

$$I\left( x_{i} \right) = - \log{p\left( X = x_{i} \right)} = - \log p_{i}$$

$$I(x) = - \log{p(x)}$$

严格递减函数，最小值为0，无上界，

### 联合自信息

$$I(x,y) = - \log{p(x,y)}$$

$$I(x,y) = I(x) + I\left( y\text{|}x \right) = I(y) + I\left( x\text{|}y \right)$$

### 条件自信息

已经知道$Y = y$的前提下，事件$X = x$还能提供多少新的信息量。

$$I\left( x\text{|}y \right) = - \log{p\left( x\text{|}y \right)} = - \log\frac{p(x,y)}{p(y)}$$

### 信息熵（平均自信息）

在观察随机变量$X$前，我们平均每个事件会有多惊讶？即系统整体的不确定性。

做n次试验，问平均做一次能获得多少信息量？

信源输出前，信源的平均不确定度。

信源输出后，每个离散信息所提供的平均信息量。

$$H(X) = E\left\lbrack I(x) \right\rbrack = \sum_{i = 1}^{n}{p\left( x_{i} \right)I\left( x_{i} \right)} = \sum_{x \in X}^{}{p(x)I(x)} = - \sum_{x \in X}^{}{p(x)\log{p(x)}}$$

非负，最大值为$\log n$，其中n是随机变量$X$的可能取值的个数。

上凸函数。

### 联合熵

这对变量一起能带来多少平均不确定性。

$$H(X,Y) = E\left\lbrack I(x,y) \right\rbrack = - \sum_{x \in X}^{}{\sum_{y \in Y}^{}{p(x,y)\log{p(x,y)}}}$$

$$H(X,Y) = H(X) + H\left( Y\text{|}X \right) = H(Y) + H\left( X\text{|}Y \right)$$

$$H(X,Y) = H\left( X\text{|}Y \right) + I(X;Y) + H\left( Y\text{|}X \right)$$

$H(X,Y) \leq H(X) + H(Y)$当$X$，$Y$独立时等号成立

### 条件熵

已知随机变量Y的取值后，随机变量X还剩下的平均不确定性。

$${H\left( X\text{|}Y \right) = E\left\lbrack I\left( x\text{|}y \right) \right\rbrack = - \sum_{x \in X}^{}{\sum_{y \in Y}^{}{p(x,y)\log{p\left( x\text{|}y \right)}}}
}{= - \sum_{y}^{}{p(x,y)\log{p\left( x\text{|}y \right)}}
}{= - \sum_{y}^{}{p(y)\sum_{x}^{}{p\left( x\text{|}y \right)\log{p\left( x\text{|}y \right)}}}
}{= \sum_{y}^{}{p(y) \cdot H\left( X\text{|}Y = y \right)}}$$

$$H\left( X\text{|}Y \right) \leq H(X),\ \ H\left( Y\text{|}X \right) \leq H(Y)$$

### 逐点互信息（互信息量）

对两个离散随机事件集$X\text{，}Y$，事件$y$的出现能提供关于事件$x$的信息量

$$i(x;y) = I(x) - I\left( x\text{|}y \right) = I(y) - I\left( y\text{|}x \right) = I(x) + I(y) - I(x,y) = \log\frac{p(x,y)}{p(x)p(y)}$$

当$x$和$y$独立时，$i(x;y) = 0$

$i(x;y)$可正可负

$i(x;y) > 1$表明$y$的出现有助于肯定$x$的出现，$< 1$表明$y$的出现告知$x$出现的可能性变小了。

$$i(x;y) < I(x),\ \ i(x;y) < I(y)$$

### 互信息

知道了$Y$后，$X$的不确定性减少了多少？等价于两者共享的信息量。

$$I(X;Y) = E\left\lbrack i(x;y) \right\rbrack = H(X) - H\left( X\text{|}Y \right) = H(Y) - H\left( Y\text{|}X \right) = H(X) + H(Y) - H(X,Y)$$

$$= \sum_{x}^{}{\sum_{y}^{}{p(x,y)\log\frac{p(x,y)}{p(x)p(y)}}}$$

$$I(X;Y) \geq 0$$

![互信息与熵的关系：H(X)、H(Y)、H(X\|Y)、I(X;Y)、H(Y\|X)、H(XY)](/images/info-mutual-venn.png)

### 联合互信息

$$I(X;Y,Z) = I(X) - I\left( X\text{|}Y,Z \right) = I(X;Y) + I\left( X;Z\text{|}Y \right)$$

### 逐点条件互信息（条件互信息量）

在已知$z$的前提下，$y$额外提供了多少关于$x$的信息。

你原本对$x$的信念是$p(x\text{|}z)$（已知$z$时的概率）。突然你得知了$y$，信念更新为$p\left( x\text{|}y,z \right)$。信息量就是"新旧信念的比值取对数"。比值越大，说明$y$带来意外惊喜（或惊奇）越多，信息量越大。

$$i\left( x;y\text{|}z \right) = I\left( x\text{|}z \right) - I\left( x\text{|}y,z \right) = \log\frac{p\left( x\text{|}y,z \right)}{p\left( x\text{|}z \right)}$$

$$i(x;y,z) = i(x;y) + i\left( x;z\text{|}y \right)$$

### 条件互信息

$$I\left( X;Y\text{|}Z \right) = E\left\lbrack i\left( x;y\text{|}z \right) \right\rbrack = H\left( X\text{|}Z \right) - H\left( X\text{|}Y,Z \right)$$

$$= \sum_{x}^{}{\sum_{y}^{}{\sum_{z}^{}{p(x,y,z)\log\frac{p\left( x,y\text{|}z \right)}{p\left( x\text{|}z \right)p\left( y\text{|}z \right)}}}}$$

### 相对熵

两个离散概率质量分布函数$p(x)$和$q(x)$之间的相对熵为

$$D\left( p\text{||}q \right) = \sum_{x}^{}{p(x)\log\frac{p(x)}{q(x)}}$$

$$\text{约定}0\log\frac{0}{0} = 0,\ \ 0\log\frac{0}{q} = 0,\ \ p\log\frac{p}{0} = 0$$

$$I(X;Y) = \sum_{x}^{}{\sum_{y}^{}{p(x,y)\log\frac{p(x,y)}{p(x)p(y)}}} = D\left( p(x,y)\text{||}p(x)p(y) \right)$$

$D\left( p\text{||}q \right) \geq 0$当$p\text{，}q$同分布时等号成立。

$$D\left( p(x,y)\text{||}q(x,y) \right) = D\left( p(x)\text{||}q(x) \right) + D\left( p(y)||q(y) \right)$$
