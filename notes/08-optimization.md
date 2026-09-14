---
title: 最优化基础
description: 最优化问题的一般形式、梯度与 Hesse 矩阵、凸性、K-T 条件、一维搜索、无约束与约束优化方法。
---

# 最优化基础

[[toc]]

### 最优化问题的一般形式

$$\min{f(x)}$$

$$s.t.\ \ \ \ c_{i}(x) = 0,i \in E = \left\{ 1,2,3,\cdots,l \right\}$$

$$c_{i}(x) \leq 0,i \in I = \left\{ l + 1,l + 2,\cdots,l + m \right\}$$

$$x \in R^{n}$$

### 欧式空间

$$\left\lbrack \mathbf{x},\mathbf{y} \right\rbrack$$

$$\left\lbrack \mathbf{x} + \mathbf{y},\mathbf{z} \right\rbrack = \left\lbrack \mathbf{x},\mathbf{z} \right\rbrack + \left\lbrack \mathbf{y},\mathbf{z} \right\rbrack$$

### 范数

$$\left\| \mathbf{x} \right\| = \sqrt{x_{1}^{2} + \cdots + x_{n}^{2}}$$

### 三角不等式

$$\left\| \mathbf{x} + \mathbf{y} \right\| \leq \left\| \mathbf{x} \right\| + \left\| \mathbf{y} \right\|$$

### 分块矩阵

$$A_{m \times n} = \left( P_{1},P_{2},\cdots,P_{n} \right),\ \ P_{j} = \begin{pmatrix}
a_{1j} \\
a_{2j} \\
 \vdots \\
a_{mj}
\end{pmatrix}$$

$$A_{m \times n} = \begin{pmatrix}
a_{1}^{T} \\
a_{2}^{T} \\
 \vdots \\
a_{m}^{T}
\end{pmatrix},\ \ a_{i}^{T} = \left( a_{i1},a_{i2},\cdots,a_{in} \right)$$

行满秩：行数小于列数；列满秩：列数小于行数

### 梯度

$$\nabla f\left( \mathbf{x} \right) = \left( \frac{\partial f}{\partial x_{1}},\frac{\partial f}{\partial x_{2}},\cdots,\frac{\partial f}{\partial x_{n}} \right)^{T}$$

### Hesse矩阵

$$\nabla^{2}f\left( \mathbf{x} \right) = \begin{pmatrix}
\frac{\partial^{2}f}{\partial x_{1}\partial x_{1}} & \frac{\partial^{2}f}{\partial x_{1}\partial x_{2}} & \cdots & \frac{\partial^{2}f}{\partial x_{1}\partial x_{n}} \\
\frac{\partial^{2}f}{\partial x_{2}\partial x_{1}} & \frac{\partial^{2}f}{\partial x_{2}\partial x_{2}} & \cdots & \frac{\partial^{2}f}{\partial x_{2}\partial x_{n}} \\
 \vdots & \vdots & & \vdots \\
\frac{\partial^{2}f}{\partial x_{n}\partial x_{1}} & \frac{\partial^{2}f}{\partial x_{1}\partial x_{1}} & \cdots & \frac{\partial^{2}f}{\partial x_{n}\partial x_{n}}
\end{pmatrix}$$

### 二次函数的梯度和Hesse矩阵

$$f\left( \mathbf{x} \right) = \mathbf{x}^{T}A\mathbf{x} + \mathbf{b}^{T}\mathbf{x} + \mathbf{c}$$

$$\nabla f\left( \mathbf{x} \right) = \left( A + A^{T} \right)\mathbf{x} + \mathbf{b}^{T}$$

$$\nabla^{2}f\left( \mathbf{x} \right) = \left( A + A^{T} \right)$$

### Jacobi（雅可比）矩阵

向量函数$F\left( \mathbf{x} \right) = \left( f_{1}\left( \mathbf{x} \right),f_{2}\left( \mathbf{x} \right),\cdots,f_{m}\left( \mathbf{x} \right) \right)^{T}$的定义域为n维，值域为m维，即由m个数字组成的向量，每个分量都是由有n个自变量的函数决定。

$$F'\left( \mathbf{x} \right) = \begin{pmatrix}
\frac{\partial f_{1}}{\partial x_{1}} & \frac{\partial f_{1}}{\partial x_{2}} & \cdots & \frac{\partial f_{1}}{\partial x_{n}} \\
\frac{\partial f_{2}}{\partial x_{1}} & \frac{\partial f_{2}}{\partial x_{2}} & \cdots & \frac{\partial f_{2}}{\partial x_{n}} \\
 \vdots & \vdots & & \vdots \\
\frac{\partial f_{m}}{\partial x_{1}} & \frac{\partial f_{m}}{\partial x_{2}} & \cdots & \frac{\partial f_{m}}{\partial x_{n}}
\end{pmatrix} = \left( \nabla f_{1}\left( \mathbf{x} \right),\nabla f_{2}\left( \mathbf{x} \right),\cdots,\nabla f_{m}\left( \mathbf{x} \right) \right)^{T}$$

### 一阶方向导数

$$\frac{\partial f\left( \overline{\mathbf{x}} \right)}{\partial\mathbf{d}} = \frac{1}{\left\| \mathbf{d} \right\|}\mathbf{d}^{T}\nabla f\left( \overline{\mathbf{x}} \right) = \left\lbrack \nabla f\left( \overline{\mathbf{x}} \right),\frac{\mathbf{d}^{T}}{\left\| \mathbf{d} \right\|} \right\rbrack$$

$\frac{\partial f}{\partial\mathbf{d}} < 0$代表下降方向，$- \nabla f\left( \overline{\mathbf{x}} \right)$为$\overline{\mathbf{x}}$处的最速下降方向。

### 二阶方向导数

$$\frac{\partial^{2}f\left( \overline{\mathbf{x}} \right)}{\partial\mathbf{d}^{2}} = \frac{\mathbf{d}^{T}}{\left\| \mathbf{d} \right\|}\nabla^{2}f\left( \overline{\mathbf{x}} \right)\frac{\mathbf{d}}{\left\| \mathbf{d} \right\|} = \frac{1}{\left\| \mathbf{d} \right\|^{2}}\mathbf{d}^{T}\nabla^{2}f\left( \overline{\mathbf{x}} \right)\mathbf{d}$$

描述函数$f\left( \mathbf{x} \right)$在$\overline{\mathbf{x}}$处沿方向$\mathbf{d}$的凹凸性和弯曲的程度。

### 泰勒展开

一阶

$$f\left( \mathbf{x} \right) = f\left( \overline{\mathbf{x}} \right) + \nabla f\left( \overline{\mathbf{x}} + \theta\left( \mathbf{x -}\overline{\mathbf{x}} \right) \right)\left( \mathbf{x -}\overline{\mathbf{x}} \right)$$

$$f\left( \mathbf{x} \right) = f\left( \overline{\mathbf{x}} \right) + \nabla f\left( \overline{\mathbf{x}} \right)^{T}\left( \mathbf{x -}\overline{\mathbf{x}} \right) + o\left( \left\| \mathbf{x -}\overline{\mathbf{x}} \right\| \right)$$

二阶

$$f\left( \mathbf{x} \right) = f\left( \overline{\mathbf{x}} \right) + \nabla f\left( \overline{\mathbf{x}} \right)^{T}\left( \mathbf{x -}\overline{\mathbf{x}} \right) + \frac{1}{2}\left( \mathbf{x -}\overline{\mathbf{x}} \right)^{T}\nabla^{2}f\left( \overline{\mathbf{x}} + \theta\left( \mathbf{x -}\overline{\mathbf{x}} \right) \right)\left( \mathbf{x -}\overline{\mathbf{x}} \right)$$

$$f\left( \mathbf{x} \right) = f\left( \overline{\mathbf{x}} \right) + \nabla f\left( \overline{\mathbf{x}} \right)^{T}\left( \mathbf{x -}\overline{\mathbf{x}} \right) + \frac{1}{2}\left( \mathbf{x -}\overline{\mathbf{x}} \right)^{T}\nabla^{2}f\left( \overline{\mathbf{x}} \right)\left( \mathbf{x -}\overline{\mathbf{x}} \right) + o\left( \left\| \mathbf{x -}\overline{\mathbf{x}} \right\|^{2} \right)$$

### 凸集的加，减，交仍是凸集

加（类似线性组合）

$$D_{1} + D_{2} = \left\{ x + y\text{|}x \in D_{1},y \in D_{2} \right\}$$

减

$$D_{1} - D_{2} = \left\{ x - y\text{|}x \in D_{1},y \in D_{2} \right\}$$

交

$$D_{1} \cap D_{2} = \left\{ x\text{|}x \in D_{1},x \in D_{2} \right\}$$

凸集内任意点由类似定比分点公式生成的点仍在凸集中。（线性组合，和为1）

### 凸函数

$x^{1}$是点，$\alpha$是向量，$\forall x^{1},x^{2},\alpha \in (0,1)$，有

$$f\left( \alpha x^{1} + (1 - \alpha)x^{2} \right) \leq \alpha f\left( x^{1} \right) + (1 - \alpha)f\left( x^{2} \right)$$

### 严格凸函数

$$f\left( \alpha x^{1} + (1 - \alpha)x^{2} \right) < \alpha f\left( x^{1} \right) + (1 - \alpha)f\left( x^{2} \right)$$

### 凸函数相关定理

$f(x)\text{凸} \Leftrightarrow f(x + \alpha y)\text{凸}$，严格凸类似

$$f(x)\text{凸} \Leftrightarrow f(y) \geq f(x) + \nabla f(x)^{T}(y - x) \Leftrightarrow \frac{f(y) - f(x)}{y - x} \geq \nabla f(x)^{T}\text{，严格凸类似}$$

$$\nabla^{2}f\text{正定} \Rightarrow f(x)\text{严格凸} \Rightarrow \nabla^{2}f\text{半正定} \Rightarrow f(x)\text{凸}$$

### 水平集

$D_{\alpha} = \left\{ x\text{|}f(x) \leq \alpha,x \in D \right\}$，其中$D \subset R^{n}$，$\alpha \in R$，$f(x)$定义在$D$上

凸集上的凸函数对任意$\alpha$得到的$D_{\alpha}$都是凸集。

局部解，全局解，严格局部解，严格全局解。

无约束优化问题的一阶必要性条件（一阶连续可微）

$$\nabla f\left( x^{*} \right) = 0$$

$x^{*}$称为平稳点/驻点，包含最大点，最小点或鞍点。

无约束优化问题的二阶必要性条件（二阶连续可微）

$\nabla f\left( x^{*} \right) = 0$，$\nabla^{2}f\left( x^{*} \right)$半正定

无约束优化问题的二阶充分性条件（二阶连续可微）

$\nabla f\left( x^{*} \right) = 0$，$\nabla^{2}f\left( x^{*} \right)$正定

### 约束优化问题的一阶必要条件（K-T条件）

若无$LD^{*} = FD^{*}$（约束限制条件），则局部解不一定为K-T点。

K-T点不一定是局部解。

前提：

$x^{*}\text{是局部解，}$目标函数和约束函数一阶连续可微，满足约束限制条件$LD^{*} = FD^{*}$

结论：

$$\exists\lambda^{*}\text{，有}\left\{ \begin{array}{r}
\nabla_{x}L\left( x^{*},\lambda^{*} \right) = \nabla f\left( x^{*} \right) + \sum_{i = 1}^{l + m}{\lambda_{i}^{*}\nabla c_{i}\left( x^{*} \right)} = 0\ \ \ \ \ \ \ \ \ \ \ \  \\
c_{i}\left( x^{*} \right) = 0,\ \ i \in E = \left\{ 1,2,\cdots,l \right\}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
c_{i}\left( x^{*} \right) \leq 0,\ \ i \in I = \left\{ l + 1,l + 2,\cdots,l + m \right\}\ \ \ \  \\
\lambda_{i}^{*} \geq 0,\ \ i \in I = \left\{ l + 1,l + 2,\cdots,l + m \right\}\ \ \ \ \ \ \ \ \ \ \  \\
\lambda_{i}^{*}c_{i}\left( x^{*} \right) = 0,\ \ i \in I = \left\{ l + 1,l + 2,\cdots,l + m \right\}
\end{array} \right.\ $$

约束优化问题的二阶充分条件（严格局部解而被严格全局解）（二阶连续偏导数）

前提：

（1）K-T条件成立

（2）目标函数和约束函数存在连续二阶偏导数

（3）$\forall d \in M$，有

$$d^{T}\nabla_{x}^{2}L\left( x^{*},\lambda^{*} \right)d > 0$$

其中

$$M = \left\{ d \in R^{n}\text{|}d \neq 0,\ \ \nabla c_{i}\left( x^{*} \right)d = 0,\ \ i \in E \cup I\left( x^{*} \right) \right\}$$

，$I\left( x^{*} \right)$是$x^{*}$的有效约束指标集。

结论：

是严格局部解。

### 凸规划的最优性条件

若目标函数$f(x)$是凸函数，约束集合$D$是凸集，则称为凸规划

$\left. \ \begin{array}{r}
等式约束是线性函数 \\
不等式约束是凸函数
\end{array} \right\} \Rightarrow D$是凸集

凸规划的局部解必是全局最优解。凸规划的K-T点是全局最优解。

### 迭代基本格式

$$x^{k + 1} = x^{k} + \alpha_{k}d^{k}$$

### 搜索方法

### 精确线性搜索

利用求导的方法直接求函数$\phi(\alpha) = f\left( x^{k} + \alpha d^{k} \right)$就$\alpha$的最小值，找到就$x^{k}$和$d^{k}$上的最优的$\alpha$，即$\alpha_{k}$

不是精确线性搜索的搜索

### 确定搜索区间

目标：

找到$0 \leq a < b < c$，使得$\phi(a) > \phi(b) < \phi(c)$（大-小-大）

步骤：

给定$a_{0} > 0$，拟定步长$h > 0$，系数$\gamma > 0$，求$\phi\left( a_{0} \right)$，$\phi\left( a_{1} = a_{0} + h \right)$

若$\phi\left( a_{0} \right) > \phi\left( a_{1} = a_{0} + h \right)$，则满足大-小-空，继续判断$\phi\left( a_{0} + \gamma h \right)$，$\phi(a_{0} + \gamma^{2}h)$等。

若$\phi\left( a_{0} \right) \leq \phi\left( a_{1} = a_{0} + h \right)$，则满足空-小-大，继续判断$\phi\left( a_{0} - \gamma h \right)$，$\phi(a_{0} - \gamma^{2}h)$等。

### 直接搜索法------0.618法

已知搜索区间$\lbrack a,b\rbrack$，其中函数要求在其上是单峰函数，计算

$$a_{l} = a + (1 - \tau)(b - a),\ \ a_{r} = a + \tau(b - a)$$

这样四个点把搜索区间分为三块：$\left\lbrack a,a_{l} \right\rbrack$，$\left( a_{l},a_{r} \right)$，$\left\lbrack a_{r},b \right\rbrack$。

> 若$\phi_{l} < \phi_{r}$，则极值不在$\left\lbrack a_{r},b \right\rbrack$，修改$b ≔ a_{r}$，计算新的$a_{l}$和$a_{r}$（$a_{r} ≔ a_{l}$）。
>
> 若$\phi_{l} > \phi_{r}$，则极值不在$\left\lbrack a,a_{l} \right\rbrack$，修改$a ≔ a_{l}$，计算新的$a_{l}$和$a_{r}$（$a_{l} ≔ a_{r}$）。

直到$|b - a| < \varepsilon$。

### 均匀搜索法

对初始搜索区间$\lbrack a,b\rbrack$，考虑切割份数$N$，计算区间长度$\delta = \frac{b - a}{N}$，得到区间分别为$\lbrack a_{i},a_{i} + \delta\rbrack$。若某个区间满足搜索区间条件（大-小-大），则令其两端为新的$a\text{，}b$。

### 基于导数信息的二分法

记搜索区间中点$\lambda = \frac{a + b}{2}$，计算$\phi'(\lambda)$。

> 若$\phi'(\lambda) = 0$，则为极值点
>
> 若$\phi'(\lambda) < 0$，说明在$\lambda$附近由大变小，满足大-小-空，则令$a ≔ \lambda$，计算新的$\phi'(\lambda)$。
>
> 若$\phi'(\lambda) > 0$，说明在$\lambda$附近由小变大，满足空-大-小，则令$b ≔ \lambda$，计算新的$\phi'(\lambda)$。

### 非精确一维搜索方法

目标：求$\mu$，使得$\phi(\mu) < \phi(0)$。求$\mu_{\min}$和$\mu_{\max}$

### Goldstein方法

给定$0 < \beta_{1} < \beta_{2} < 1$，给定任意$\mu > 0$，考虑直线

$$y = \phi(0) + \mu\beta_{2}\phi'(0)$$

和$y = \phi(0) + \mu\beta_{1}\phi'(0)$，要求$\phi(\mu)$夹在两条直线之间，即

$$\phi(0) + \mu\beta_{2}\phi'(0) \leq \phi(\mu) < \phi(0) + \mu\beta_{1}\phi'(0) < \phi(0)$$

> 若不满足

$$\phi(0) + \mu\beta_{2}\phi'(0) \leq \phi(\mu)$$

，则令$\mu_{\min} ≔ \mu$
>
> 若不满足$\phi(\mu) < \phi(0) + \mu\beta_{1}\phi'(0)$，则令$\mu_{max} ≔ \mu$
>
> 若$\mu$有界，令$\mu ≔ \frac{\mu_{\min} + \mu_{\max}}{2}$，否则令$\mu ≔ 2\mu_{\min}$

重新判断

$$\phi(0) + \mu\beta_{2}\phi'(0) \leq \phi(\mu) < \phi(0) + \mu\beta_{1}\phi'(0) < \phi(0)$$

直到满足不等式。

### Armijo方法

给定$M > 1,0 < \beta_{1} < 1$，使得

$$\left\{ \begin{array}{r}
\phi(\mu) \leq \phi(0) + \mu\beta_{1}\phi'(0) \\
M \geq \mu,\ \ M \in \lbrack 2,10\rbrack
\end{array} \right.\ $$

### Wolfe-Powell方法

给定$0 < \beta_{1} < \beta_{2} < 1$，使得

$$\beta_{2}\phi'(0) \leq \phi(\mu) \leq \phi(0) + \mu\beta_{1}\phi'(0)$$

### 下降算法的一般迭代格式

（1）给定初始点$x^{1}$，$k ≔ 1$

（2）确定初始下降方向$d$，使得$\nabla f\left( x^{k} \right)^{T}d^{k} < 0$（即$d$是下降的方向）

（3）确定步长$a_{k} > 0$，使得$f\left( x^{k} + \alpha_{k}d^{k} \right) < f\left( x^{k} \right)$（在下降，且步长不太大）

（4）令$x^{k + 1} = x^{k} + \alpha_{k}d^{k}$

（5）若$x^{k + 1}$满足终止准则，则停止；否则令$k ≔ k + 1$，转步骤（1）

由上述步骤得到的$\left\{ x^{k} \right\}$的对应的$\left\{ f\left( x^{k} \right) \right\}$是单调递减的。若$\left\{ f\left( x^{k} \right) \right\}$有界，则$\left\{ f\left( x^{k} \right) \right\}$有极限，但$\left\{ x^{k} \right\}$不一定收敛，甚至不一定有界。即使$\left\{ x^{k} \right\}$收敛，得到的也不一定是平稳点。

局部收敛：初始点选在极小点附近才能收敛到极小点（局部解）。

全局收敛：任意初始点都能收敛到极小点（局部解）。

> $$\text{收敛速率：}\beta = \lim_{k \rightarrow \infty}\frac{\left\| x^{k + 1} - x^{*} \right\|}{\left\| x^{k} - x^{k} \right\|} \Rightarrow \left\{ \begin{array}{r}
> 0 < \beta < 1\text{：线性收敛} \\
> \beta = 0\text{：超线性收敛} \\
> \beta = 1\text{：次线性收敛}
> \end{array} \right.\ $$

### 二次终止性

算法对任意正定二次函数从任意点触发都能在有限步内收敛到极小点。

### 柯西收敛准则

$$\left\| \chi^{m} - \chi^{p} \right\| \leq \varepsilon,\ \ \sqrt{\sum_{i = 1}^{n}\left( \chi^{m} - \chi^{p} \right)^{2}} \leq \varepsilon,\ \ \left\| \chi^{m} - \chi^{p} \right\| \leq \varepsilon_{i} = \frac{\varepsilon}{\sqrt{N}}$$

迭代终止准则（$\varepsilon$常取$10^{- 2}\sim 10^{- 5}$）

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
点距准则

$$\left\| x^{k + 1} - x^{k} \right\| \leq \varepsilon_{1}\text{或}\frac{\left\| x^{k + 1} - x^{k} \right\|}{\left\| x^{k} \right\|} \leq \varepsilon_{2}$$

--------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------
函数值下降量准则

$$\left| f^{k + 1} - f^{k} \right| \leq \varepsilon_{1}\text{或}\frac{\left| f^{k + 1} - f^{k} \right|}{\left| f^{k} \right|} \leq \varepsilon_{2}$$

目标函数梯度准则

$$\left\| \nabla f\left( x^{k} \right) \right\| \leq \varepsilon_{1}$$

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 坐标轴交替下降法

对于每个坐标方向，都用搜索方法找到对应的步长$\alpha_{i}$，和对应的值$y_{i} = y_{i - 1} + \alpha e_{i}$，直到$\left\| \nabla f\left( x^{k} \right) \right\| \leq \varepsilon$。

优点：不需要成本就能获得搜索方向。

缺点：对于一般问题所得点列未必收敛。

### 最速下降法

搜索方向为$d^{k} = - \nabla f\left( x^{k} \right)$，步长常采用精确线性搜索。当采用精确线性搜索时，两次下降方向互相正交。

优点：简单直观，收敛，搜索方向只需计算$\nabla f\left( x^{k} \right)$。

缺点：收敛速度慢，Zigzag现象（正交的搜索方向导致收敛较慢），不具备二次终止性。

### Newton（牛顿）法

要求目标函数二次可微。

由泰勒展开

$$f\left( \mathbf{x} \right) = f\left( \overline{\mathbf{x}} \right) + \nabla f\left( \overline{\mathbf{x}} \right)^{T}\left( \mathbf{x -}\overline{\mathbf{x}} \right) + \frac{1}{2}\left( \mathbf{x -}\overline{\mathbf{x}} \right)^{T}\nabla^{2}f\left( \overline{\mathbf{x}} \right)\left( \mathbf{x -}\overline{\mathbf{x}} \right) + o\left( \left\| \mathbf{x -}\overline{\mathbf{x}} \right\|^{2} \right)$$

转换符号

$$f(x) \approx f\left( x^{k} \right) + \nabla f\left( x^{k} \right)^{T}\left( x - x^{k} \right) + \frac{1}{2}\left( x - x^{k} \right)\nabla^{2}f\left( x^{k} \right)\left( x - x^{k} \right)$$

等号两边对$x$求导

$$\nabla f(x) = \nabla f\left( x^{k} \right) + \nabla^{2}f\left( x^{k} \right)\left( x - x^{k} \right)$$

令$\nabla f(x) = 0$，把$x$换成$x^{k + 1}$，解得

$$x^{k + 1} = x^{k} - \left\lbrack \nabla^{2}f\left( x^{k} \right) \right\rbrack^{- 1}\nabla f\left( x^{k} \right)$$

其中$d^{k} = - \left\lbrack \nabla^{2}f\left( x^{k} \right) \right\rbrack^{- 1}\nabla f\left( x^{k} \right)$，$\alpha^{k} = 1$

优点：二阶收敛，收敛速度快。

缺点：不能保证目标函数值综述下降，当Hesse矩阵奇异时无法计算。

### 阻尼牛顿法

方向$d^{k}$仍为$- \left\lbrack \nabla^{2}f\left( x^{k} \right) \right\rbrack^{- 1}\nabla f\left( x^{k} \right)$，步长使用搜索方法确定。终止条件为$\left\| \nabla f\left( x^{k} \right) \right\| \leq \varepsilon$。

### 拟牛顿法

用不包含二阶导数的矩阵近似Hesse矩阵的逆。

$f(x)$在$x^{k + 1}$的二阶泰勒展开：

$$f(x) \approx f\left( x^{k + 1} \right) + \nabla f\left( x^{k + 1} \right)\left( x - x^{k + 1} \right) + \frac{1}{2}\left( x - x^{k + 1} \right)^{T}\nabla^{2}f\left( x^{k + 1} \right)\left( x - x^{k + 1} \right)$$

等式两边求导，得

$$\nabla f(x) \approx \nabla f\left( x^{k + 1} \right) + \nabla^{2}f\left( x^{k + 1} \right)\left( x - x^{k + 1} \right)$$

带入$x = x^{k}$，得

$$\nabla f\left( x^{k} \right) \approx \nabla f\left( x^{k + 1} \right) + \nabla^{2}f\left( x^{k + 1} \right)\left( x^{k} - x^{k + 1} \right)$$

定义

$$s^{k} ≔ x^{k + 1} - x^{k}$$

$$y^{k} ≔ \nabla f\left( x^{k + 1} \right) - \nabla f\left( x^{k} \right)$$

得

$$s^{k} \approx \nabla^{2}f\left( x^{k + 1} \right)^{- 1}y^{k}$$

得到拟牛顿方程

$$s^{k} = H_{k + 1}y^{k}$$

其中

$$H_{1} = I,\ \ H_{k + 1} = H_{k} + \Delta H_{k}$$

### 对称秩1校正

$$\Delta H_{k} = uv^{T} = \frac{\left( s^{k} - H_{k}y^{k} \right)\left( s^{k} - H_{k}y^{k} \right)^{T}}{\left( s^{k} - H_{k}y^{k} \right)^{T}y^{k}}$$

缺点：$H_{k}$不一定正定，$\Delta H_{k}$可能无界。

### DFP算法（秩2校正）

$$\Delta H_{k} = \alpha u \cdot u^{T} + \beta v \cdot v^{T} = \frac{s^{k}\left( s^{k} \right)^{T}}{\left( s^{k} \right)^{T}y^{k}} - \frac{H_{k}y^{k}\left( y^{k} \right)^{T}H_{k}}{\left( y^{k} \right)^{T}H_{k}y^{k}}$$

优点：$H_{k}$正定，搜索方向是下降的（精确搜索），搜索方向是共轭的。

### BFGS公式

新拟牛顿条件：$y^{k} = B_{k + 1}s^{k}$，把上面的两个公式中的$s$换$y$，$y$换$s$，$H$换$B$即可。

### 共轭梯度法

共轭梯度法是求解正定二次规划的一种优化方法，产生的搜索方向是下降方向，不必计算Hesse矩阵，只计算目标函数值和梯度，具有二次终止性。

使用精确线性搜索时，具有二次终止性。

使用精确线性搜索，有$\nabla f\left( x^{k} \right)^{T}d^{k - 1} = 0$

$$d^{1} = - \nabla f\left( x^{1} \right),\ \ d^{k} = - \nabla f\left( x^{k} \right) + \beta_{k - 1}d^{k - 1}$$

$$\beta_{k - 1} = \left\{ \begin{array}{r}
\frac{\left\| \nabla f\left( x^{k} \right) \right\|^{2}}{\left\| \nabla f\left( x^{k - 1} \right) \right\|^{2}},\ \ FR \\
\frac{\nabla f\left( x^{k} \right)^{T}\left\lbrack \nabla f\left( x^{k} \right) - \nabla f\left( x^{k - 1} \right) \right\rbrack}{\left\| \nabla f\left( x^{k - 1} \right) \right\|^{2}},\ \ PRP
\end{array} \right.\ $$

### 可行方向

设$x^{*}$是可行点，$0 \neq d \in R^{n}$，若存在正数$\alpha$，使得对于$\forall\delta \in \lbrack 0,\alpha\rbrack \text{，有}x^{*} + \delta d \in D$，则称$d$是$x^{*}$的可行方向。

$$FD^{*} = FD\left( x^{*} \right) = \left\{ d\text{|}d\text{是}x^{*}\text{的可行方向} \right\}$$

### 有效约束

设$\widehat{x}$是可行点，若存在$i \in I$，使得$c_{i}\left( \widehat{x} \right) = 0$，则称约束$c_{i}(x) \leq 0$为$\widehat{x}$的有效约束。

### 非有效约束

设$\widehat{x}$是可行点，若存在$i \in I$，使得$c_{i}\left( \widehat{x} \right) < 0$，则称约束$c_{i}(x) \leq 0$为$\widehat{x}$的有效约束。

### 有效约束指标集

对某个可行点$\widehat{x}$，所有有效约束构成的结合$I\left( \widehat{x} \right)$。

$$I\left( \widehat{x} \right) = \left\{ i\text{|}c_{i}\left( \widehat{x} \right) = 0,\ \ i \in I \right\}$$

### 锥

集合$C$是一个锥，当且仅当$\forall x \in C\text{，}\forall\lambda > 0$，有$\lambda x \in C$

### 线性化锥

设$x^{*}$是可行点，则$LD^{*} \cup \left\{ 0 \right\}$称为$x^{*}$处的线性化锥，其中

$$LD^{*} = LD\left( x^{*} \right) = \left\{ d\text{|}d \neq 0,\ d^{T}\nabla c_{i}\left( x^{*} \right) = 0,\ i \in E,\ d^{T}\nabla c_{i}\left( x^{*} \right) \leq 0,\ i \in I \right\}$$

对等式约束要求正交，对不等式约束要求夹角不小于$90{^\circ}$（方向导数非正）

### 下降方向

就是一阶方向导数小于0的方向。

$$DD^{*} = DD^{*}\left( x^{*} \right) = \left\{ d\text{|}d^{T}\nabla f\left( x^{*} \right) < 0 \right\}$$

$FD^{*} \subset LD^{*}$，反过来不一定成立

若$x^{*}$是局部解，则$FD^{*} \cap DD^{*} = \Phi$

约束限制条件：使$FD^{*} = LD^{*}$的条件

$$eg.c_{i}(x)\text{是线性函数；}\nabla c_{i}(x)\text{线性无关，}i \in E \cup I\left( x^{*} \right)$$

### 拉格朗日函数

$$L(x,\lambda) = f(x) + \sum_{i = 1}^{l + m}{\lambda_{i}c_{i}(x)}$$

### 拉格朗日对偶函数

$$d(\lambda) = \inf\left\{ f(x) + \sum_{i = 1}^{l + m}{\lambda_{i}c_{i}(x)}\text{|}x \in X \right\}$$

>

$$\text{即}f(x) + \sum_{i = 1}^{l + m}{\lambda_{i}c_{i}(x)}\text{就}x\text{的最小值，结果是一个关于}\lambda \text{的函数。}$$

>
> 对偶函数是凹函数。

这函数很有可能是分段的。做下面的拉格朗日问题时只保留有界的部分，但约束条件要协商使函数有界的哪些关于$\lambda$的约束条件。

### 拉格朗日问题

$$\max{d(\lambda)},\ \ s.t.\lambda_{i} \geq 0,i \in I$$

### 对偶定理

> 弱对偶定理：原问题可行解对应的最小值大于或等于对偶问题可行解对应的最大值。
>
> 推论：若相等，则为最优解。
>
> 推论：原问题无界$\rightarrow$对偶问题无界，对偶问题无界$\rightarrow$原问题不可行。
>
> 可以"相等"的条件：最常用的那个约束条件+......

### 次梯度法

次梯度：对凹函数的某点$x$，若对$\forall y\text{，}\exists\xi$有$f(y) - f(x) \leq \xi^{T}(y - x)$，则称$\xi$为$x$处的次梯度。可以证明

$$c\left( x_{\lambda} \right) = \left( c_{1}\left( x_{\lambda} \right),c_{2}\left( x_{\lambda} \right),\cdots,c_{l + m}\left( x_{\lambda} \right) \right)^{T}$$

是函数$d(\lambda)\text{在}\lambda$的次梯度。

开始：$\lambda^{1} \in R^{l + m},v^{1} = - \infty,\varepsilon > 0$

终止条件：$\left\| \xi^{k} \right\| \leq \varepsilon$

迭代：

$\xi^{k} = \left( c_{1}\left( x^{k} \right),c_{2}\left( x^{k} \right),\cdots,c_{l + m}\left( x^{k} \right) \right)^{T}$，

$v^{k + 1} = \max\left\{ v^{k},d\left( \lambda^{k} \right) \right\}$，

> $$\lambda_{i}^{k + 1} = \left\{ \begin{array}{r}
> \lambda_{i}^{k} + s_{k}\xi_{i}^{k},\ \ i \in E \\
> \max{\left\{ 0,\lambda_{i}^{k} + s_{k}\xi_{i}^{k} \right\},\ \ i \in I}
> \end{array} \right.\ $$

二次规划的全局最优解的充要条件是$K - T$条件。

$$\min\left\{ f(x) = \frac{1}{2}x^{T}Gx + r^{T}x \right\}$$

$$c_{i}(x) = \alpha_{i}^{T}x - b_{i} = 0,\ \ i \in E = \left\{ 1,2,\cdots,l \right\}$$

$$c_{i}(x) = \alpha_{i}^{T}x - b_{i} \leq 0,\ \ i \in I = \left\{ l + 1,l + 2,\cdots,l + m \right\}$$

### 只有等式约束的二次规划：

$$\min\left\{ f(x) = \frac{1}{2}x^{T}Gx + r^{T}x \right\},\ \ Ax = b$$

### 拉格朗日函数

$$L(x,\lambda) = \frac{1}{2}x^{T}Gx + r^{T}x + \lambda^{T}(Ax - b)$$

其K-T条件为

$$\left\{ \begin{array}{r}
\nabla_{x}L\left( x^{*},\lambda^{*} \right) = 0 \Rightarrow Gx + r + A^{T}\lambda = 0 \\
c_{i}\left( x^{*} \right) = 0 \Rightarrow Ax = b
\end{array} \right.\ $$

把前两个条件组成方程组为

$$\begin{pmatrix}
G & A^{T} \\
A & O
\end{pmatrix}\begin{pmatrix}
x \\
\lambda
\end{pmatrix} = \begin{pmatrix}
 - r \\
b
\end{pmatrix}$$

解方程组，即可得到全局最小点和对应的$\lambda$

也可求解由约束条件构成的线性方程组，回代到目标函数从而得到无约束二次规划，使用二阶充分性条件和一、二阶必要性条件即可。缺点是$A_{B}$可能接近奇异矩阵（一定是非异的）

### 有效集法（G必须正定）

$$\min\left\{ f(x) = \frac{1}{2}x^{T}Gx + r^{T}x \right\}$$

$$c_{i}(x) = \alpha_{i}^{T}x - b_{i} = 0,\ \ i \in E = \left\{ 1,2,\cdots,l \right\}$$

$$c_{i}(x) = \alpha_{i}^{T}x - b_{i} \leq 0,\ \ i \in I = \left\{ l + 1,l + 2,\cdots,l + m \right\}$$

（1）选取初始可行点$x^{1}$满足所有约束条件，确定其有效约束指标集$I\left( x^{1} \right) = \left\{ i\text{|}\alpha_{i}^{T}x^{1} - b_{i} = 0,i \in I \right\}$（即所有有效约束的下标）

（2）求解等式二次约束规划问题（自变量是$d$）

$$\min\left\{ \frac{1}{2}d^{T}Gd + \nabla f\left( x^{k} \right)^{T}d \right\},\ \ \alpha_{i}^{T}d = 0,i \in E \cup I\left( x^{k} \right)$$

该子问题寻找一个可行方向$d$，使得沿着$d$移动一小步后，所有当前有效约束仍然保持为等式。

（3）$d^{k} = 0$，说明在当前点$x^{k}$处，沿着任何保持当前有效约束的方向都不能进一步下降目标函数。

> $\lambda_{i}^{k} \geq 0$，（所有不等式约束）终止。
>
> $\exists\lambda_{i}^{k} < 0$，寻找$q\text{，使得}\lambda_{q} = \min\left\{ \lambda_{i}^{k}\text{|}i \in I\left( x^{k} \right) \right\}$，$x$和$k$递增，$I\left( x^{k + 1} \right) = I\left( x^{k} \right) - \left\{ q \right\}$（把不该要的约束移除），转步骤（2）。

（4）$d^{k} \neq 0$，存在一个可行下降方向，移动后可能产生新的有效约束，需要将其加入有效集，然后迭代。

>

$$\text{定义}{\widehat{\alpha}}_{k} = \frac{b_{p} - \alpha_{p}^{T}x^{k}}{\alpha_{p}^{T}d^{k}} = \min\left\{ \frac{b_{i} - \alpha_{i}^{T}x^{k}}{\alpha_{i}^{T}d^{k}}\text{|}\alpha_{i}^{T}d^{k} > 0,i \in I\backslash I\left( x^{k} \right) \right\}$$

>
>

$$\text{取}\alpha_{k} = \min\left\{ {\widehat{\alpha}}_{k},1 \right\}$$

>
> 若$\alpha_{k} = {\widehat{\alpha}}_{k}$，则$I\left( x^{k + 1} \right) = I\left( x^{k} \right) + \left\{ p \right\}$（加入没被加入的指标），否则$I\left( x^{k + 1} \right) = I\left( x^{k} \right)$，转步骤（2）。
>
> ${\widehat{\alpha}}_{k}$ 是在不违反任何未起作用约束的前提下，沿 $d^{k}$ 能走的最大步长。

### 外罚函数法

### 定义惩罚项

$$\widetilde{P}(x) = \sum_{i = 1}^{l}\left| c_{i}(x) \right|^{\beta} + \sum_{i = l + 1}^{l + m}\left\lbrack \max\left( 0,c_{i}(x) \right) \right\rbrack^{\alpha}$$

其中$\alpha \geq 1$，$\beta \geq 1$，常取$\alpha = \beta = 2$

### 外罚函数

$$P(x,\sigma) = f(x) + \sigma\widetilde{P}(x)$$

其中$\sigma$为惩罚因子。

外罚函数的性质：

（1）$P(x,\sigma) \geq f(x)$，在可行点处取等。

（2）$\left\{ P\left( x^{k},\sigma_{k} \right) \right\}$单调递增

（3）$\left\{ \widetilde{P}\left( x^{k} \right) \right\}$单调递减

（4）$\left\{ f\left( x^{k} \right) \right\}$单调递增

（5）病态性质，即收敛速度与精确性相矛盾

理论步骤：

选择任意的点$x^{k - 1}$，求解无约束规划问题$\min\left\{ P\left( x,\sigma_{k} \right) \right\}$，得到含$\sigma_{k}$的$x^{k}$。

若$\widetilde{P}\left( x^{k} \right) < \varepsilon$，则停止；否则令$\sigma_{k + 1} = c\sigma_{k}(c > 1)$，$k ≔ k + 1$，继续迭代。

计算方法：

利用条件$\nabla_{x}P(x,\sigma) = 0$，就$P(x,\sigma)$对$x$求导，令导数为0解得含$\sigma_{k}$的$x$。然后求$\lim_{\sigma \rightarrow \infty}x$即得极值点。

### 内罚函数法（只有不等式约束）

### 定义障碍函数

$$B(x) = - \sum_{i = 1}^{l}{\ln\left( - c_{i}(x) \right)}\text{或}B(x) = - \sum_{i = 1}^{l}\frac{1}{c_{i}(x)}$$

通常选择对数障碍函数。

### 内罚函数

$$P(x,r) = f(x) + rB(x)$$

其中$r > 0$。

与外罚函数法相反，要令$r \rightarrow 0$。对应的迭代步骤中$r_{k + 1} = cr_{k}$中$0 < c < 1$

优点：每次迭代的点都是可行点，当迭代到一定阶段时，尽管没有达到最优点，但可以接受为一个较好的近似解。

缺点：内罚函数要求$x$在可行域内部移动，故不能处理等式约束条件。也存在病态性。

混合罚函数法：将内罚函数法和外罚函数法结合。

### 乘子法

乘子罚函数（求解对应无约束优化问题，得到$x^{k}$）

$$\phi(x,\lambda,\sigma) = f(x) + \sum_{i = 1}^{l}{\lambda_{i}c_{i}(x)} + \frac{\sigma}{2}\sum_{i = 1}^{l}{c_{i}^{2}(x)} + \frac{1}{2\sigma}\sum_{i = l + 1}^{l + m}\left\{ \left\lbrack \max\left( 0,\lambda_{i} + \sigma c_{i}(x) \right) \right\rbrack^{2} - \lambda_{i}^{2} \right\}$$

### 终止条件

$$\left\{ \sum_{i = 1}^{l}{c_{i}^{2}\left( x^{k} \right)} + \sum_{i = l + 1}^{l + m}\left\lbrack \max\left( c_{i}\left( x^{k} \right), - \frac{\lambda_{i}^{k}}{\sigma_{k}} \right) \right\rbrack^{2} \right\}^{1\text{/}2} \leq \varepsilon$$

迭代公式（$\sigma$不变）

$$\lambda_{i}^{k + 1} = \left\{ \begin{array}{r}
\lambda_{i}^{k} + \sigma_{k}c_{i}\left( x^{k} \right),\ \ i \in \lbrack 1,l\rbrack\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\
\max{\left\{ \lambda_{i}^{k} + \sigma_{k}c_{i}\left( x^{k} \right),0 \right\},\ \ i \in \lbrack l + 1,l + m\rbrack}
\end{array} \right.\ $$

$$\sigma_{k + 1} = \sigma_{k}$$
