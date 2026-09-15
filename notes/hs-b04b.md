---
title: "数学奠基"
hs_seq: "B4"
description: "数学奠基：概括公理（axiomschemaofcomprehension）与罗素悖论（Russell'sParadox）"
---

# 数学奠基

公理化集合论

概括公理（axiom schema of comprehension）与罗素悖论（Russell's Paradox）

概括公理：

对每一个公式 $P(x)$，存在一个以满足 $P\$的所有对象为元素的集合$\ Y = \left\{ x\text{：}P(x) \right\}$

这里的“公式”指集合$Y$中的元素满足的条件，把这种条件记为$P(x)$。即$Y$中的任一元素$x$满足 $P(x)$。公理认为可以按照任意的“条件”找出满足这种条件的所有元素组成的集合。

但概括公理是错误的，下面举一个例子。假定集合$A = \left\{ x\text{：}x \notin x \right\}$，其中$x$代表集合。表示集合$A$包含这样的元素：它是集合，并且不包含自身。那么考虑集合$A$是否是集合$A$中的元素。假设集合$A$是集合$A$中的元素，即$A \in A$，但根据定义“并且不包含自身”，说明假设错误，即$A \notin A$，但又根据定义“并且不包含自身”，发现满足了定义，使得$A \in A$，这样就得出了矛盾。（“有一位理发师在广告上声称：‘将为本城所有不给自己刮胡子的人刮胡子，我也只给这些人刮胡子。’但有一天，这位理发师从镜子里看见自己的胡子长了，那他能不能给他自己刮胡子呢?如果他不给自己刮，他就属于‘不给自己刮胡子的人’，他就要给自己刮胡子，而如果他给自己刮胡子呢?他又属于‘给自己刮胡子的人’，他就不该给自己刮胡子了。”这是罗素的著名举例，但它不是罗素悖论的实例。）

通过构造这样的集合，我们否定了概括公理的正确性。这种矛盾被称为罗素悖论。

罗素悖论曾经导致了所谓“第三次数学危机”，它指出集合论需要严格化，经过长时间的研究和思考，数学家们最后普遍接受了一套被称为 ZFC 的公理系统.

ZFC（Zermelo–Fraenkel 公理集合论）

外延公理（axiom of extension）

如果两个集合有相同的元素，则它们相等

$\forall u(u \in x \leftrightarrow u \in y) \rightarrow x = y$

这条公理给出了判断集合相等的方法。

分离公理（axiom schema of separation）

设$S(x)$是一个公式，或者说叫关于自由变量$x$的一个性质，则对任意的集合$X$，存在一个集合$Y$，它的所有元素恰是$X$中满足$S(x)$的元素

$\forall X\exists Y\forall x\left( x \in Y \leftrightarrow x \in X \land S(x) \right)$

分离公理是概括公理的弱化版，它规避了罗素悖论。

配对公理（axiom of pairing）

如果x，y 是集合, 那么存在一个集合恰包含x，y两个元素

$\forall x\forall y\exists z\forall u(u \in z \leftrightarrow u = x \vee u = y)$

配对公理提供了由已知的集合构造新的集合的最基础的方式

并集公理(axiom of union)

如果C是一个集族，那么存在一个集合U，它的元素恰是C的元素的元素

$\forall C\exists U\forall x\left( x \in U \leftrightarrow \exists y(y \in C \land x \in y) \right)$

幂集公理(axiom of power set)

对任意集合$x$，存在一个集合 $P_{x}$ ，它的元素恰是$x$的子集

$\forall x\exists Px\forall y\left( y \in P_{x} \leftrightarrow \forall z(z \in y \rightarrow z \in x) \right)$

基于ZFC的自然数定义

数学归纳法

自然数与整数的性质

有理数与稠密性

实数的定义：戴德金分割定义与极限定义

实数五大基本定理

确界存在定理：非空有上界的数集必有上确界，非空有下界的数集必有下确界。

单调有界数列收敛定理：单调有界数列必定收敛。

闭区间套定理：如果$\left\{ \left\lbrack a_{n}\text{，}b_{n} \right\rbrack \right\}$构成一个闭区间套，则存在唯一的实数$\xi$属于所有的闭区间$\left\lbrack a_{n}\text{，}b_{n} \right\rbrack$，且$\xi = \lim_{n \rightarrow \infty}a_{n} = \lim_{n \rightarrow \infty}b_{n}$。

Bolzano-Weierstrass定理：有界数列必有收敛子数列。

Cauchy（柯西）收敛原理：数列$\left\{ x_{n} \right\}$收敛的充要条件是$\left\{ x_{n} \right\}$是基本数列。

基本数列$\left\{ x_{n} \right\}$满足：对于任意的$\varepsilon > 0$，存在正整数$N$，使得当$n,m > N$时$\left| x_{n} - x_{m} \right| < \varepsilon$恒成立。

皮亚诺公理体系与戴德金分割

~~皮亚诺公理体系是把数学建立在坚实的基础上。~~

皮亚诺公理体系

皮亚诺从公理化集合论出发，重新定义了我们习以为常的正整数，自然数，整数和分数。

皮亚诺的五条公理：

> 1、0是自然数。
>
> 2、每一个确定的自然数$a$，都具有确定的后继数$a'$，$a'$也是自然数。
>
> 3、0不是任何自然数的后继数。
>
> 4、不同的自然数有不同的后继数，如果自然数$b$、$c$的后继数都是自然数$a$，那么$b = c$。
>
> 5、（归纳公理）设$S \subseteq N$（自然数），且满足2个条件：（i）$0 \in S$；（ii）如果$\forall n \in S$，那么$n' \in S$。
>
> 则$S$是包含全体自然数的集合，即$S = N$。
>
> （简易表述：若集合$S$中全是自然数，且满足两个条件：（1）$0$在集合$S$中。（2）若任给实数$n$在集合$S$中，那么$n$的后继数$n'$也在$S$中，那么$S$是包含全体自然数的集合。）

加法运算：定义

> 1、$\forall m \in N\text{，}0 + m = m$
>
> 2、$\forall m\text{，}n \in N\text{，}n' + m = \left. \text{（}n + m \right.\text{）}'$
>
> 加法满足交换律和结合律。
>
> $eg.1 + 1 = 0' + 1 = (0 + 1)' = 1' = 2$

乘法运算：定义

> 1、$\forall m \in N\text{，}m \cdot 0 = 0$
>
> 2、$\forall m\text{，}n \in N\text{，}m \cdot n' = m \cdot n + m$
>
> 乘法满足交换律、结合律和分配律。

之后通过引入减法可以得到整数系，再引入除法得到有理数体系，通过计算有理数序列的极限或者对有理数系进行分割（戴德金分割）得到实数系。

Dedekind（戴德金）分割

有理数可以表示为所有真分数与假分数的集体，但非完全平方数的平方根以及$\pi e\gamma$等并不是无理数的全部，Dedekind分割通过无穷的有理数的稠密性出发，可以构造出全部的有理数和无理数，即全部的实数。随之产生的Dedekind切割定理说明了不能通过分割的方法定义不是实数的数，亦说明了实数与数轴上的点一一对应。这就把微积分建立在扎实的基础上。

有理数的分割

设两个非空有理数集合和满足：，且对于任意的与任意的，成立，则称和构成一个切割，记为

数系

代数基本定理

任何复系数一元n次多项式方程（$n \in \mathbb{N}^{*}$）在复数域上至少有一根。

推论：n次复系数多项式方程在复数域内有且只有n个根（重根按重数计算）

线性空间与抽象定义

函数与方程的关系

方程的近似解
