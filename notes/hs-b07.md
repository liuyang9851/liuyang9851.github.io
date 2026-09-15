---
title: "数列"
hs_seq: "B7"
description: "数列：使等号左边任意项和为零，并给出一定的值（初值条件），求。"
---

# 数列

伸缩级数

$\sum_{i = a}^{b}\left( f(i) - f(i - 1) \right) = f(b) - f(a - 1)$

应用（就是裂项）

$1.\sum_{i = 1}^{n}(2i - 1) = \sum_{i = 1}^{n}\left( i^{2} - (i - 1)^{2} \right) = n^{2} - 0^{2} = n^{2}$

即前个n奇数的和为$n^{2}$

$2.\sum_{i = 1}^{n}(2i - 1) = 2\sum_{i = 1}^{n}i - \sum_{i = 1}^{n}1 = n^{2} \Rightarrow \sum_{i = 1}^{n}i = \frac{1}{2}\left( n^{2} + \sum_{i = 1}^{n}1 \right) = \frac{n(n + 1)}{2}$

$3.\sum_{i = 1}^{n}\left( i^{3} - (i - 1)^{3} \right) = n^{3} \Rightarrow 3\sum_{i = 1}^{n}i^{2} - 3\sum_{i = 1}^{n}i - n = n^{3} \Rightarrow \sum_{i = 1}^{n}i^{2} = \frac{1}{3}\left( n^{3} + \frac{3n(n + 1)}{2} - n \right) = \frac{n(n + 1)(2n + 1)}{6}$

$4.\sum_{i = 1}^{n}i^{3} = \left( \frac{n(n + 1)}{2} \right)^{2}$

n阶线性递推数列

齐次线性递推方程

数列$\left\{ a_{n} \right\}$满足

$a_{n} + p_{k - 1}a_{n - 1} + p_{k - 2}a_{n - 2} + \cdots + p_{0}a_{1} = 0$

使等号左边任意项和为零，并给出一定的值（初值条件），求$\left\{ a_{n} \right\}$。

考虑特征方程

$x^{n} + p_{k - 1}x^{n - 1} + p_{k - 2}x^{n - 2} + \cdots + p_{0}x = 0$

它有n个复数根$x_{1}\text{，}x_{2}\text{，}\cdots \text{，}x_{n}$，并且其中有s个重根（相等的根）$x_{s1}\text{，}x_{s2}\text{，}\cdots \text{，}x_{ss}$，则数列的通项为

$a_{n} = C_{1}x_{1}^{n} + C_{2}x_{2}^{n} + \cdots + \left( C_{s1}x_{s1}^{n} + nC_{s2}x_{s2}^{n} + n^{2}C_{s3}x_{s3}^{n} + \cdots + n^{s - 1}C_{ss}x_{ss}^{n} \right) + \cdots + C_{n}x_{n}^{n}$

特别地，当这n个复数根全部为1的n次方根时，该数列为周期数列

为了求出$C_{1}\text{，}C_{2}\text{，}\cdots \text{，}C_{n}$的值，可以把$a_{1}a_{2}\cdots$的值分别代入上式，得到含有b个方程，b个未知数的关于$C_{1}\text{，}C_{2}\text{，}\cdots \text{，}C_{n}$的一次方程组，求解，得到通项公式

$eg.\text{已知}a_{n} = a_{n - 1} + a_{n - 2}\text{，}a_{1} = a_{2} = 1\text{，求}\left\{ a_{n} \right\}$

$\text{解：解特征方程}x^{2} - x - 1\text{，得}x_{1} = \frac{1 + \sqrt{5}}{2}\text{，}x_{2} = \frac{1 - \sqrt{5}}{2}$

$\text{得到通项公式}a_{n} = C_{1}x_{1}^{n} + C_{2}x_{2}^{n} = C_{1}\left( \frac{1 + \sqrt{5}}{2} \right)^{n} + C_{2}\left( \frac{1 - \sqrt{5}}{2} \right)^{n}$

代入$a_{1} = a_{2} = 1$，得

$\left\{ \begin{array}{r} a_{1} = C_{1}\frac{1 + \sqrt{5}}{2} + C_{2}\frac{1 - \sqrt{5}}{2} = 1\ \ \ \ \ \ \ \ \ \ \ \ \  \\ a_{2} = C_{1}\left( \frac{1 + \sqrt{5}}{2} \right)^{2} + C_{2}\left( \frac{1 - \sqrt{5}}{2} \right)^{2} = 1 \end{array} \right.\ \text{，解得}\left\{ \begin{array}{r} C_{1} = \frac{\sqrt{5}}{5}\ \ \ \  \\ C_{2} = - \frac{\sqrt{5}}{5} \end{array} \right.\ \text{，即得斐波那契数列通项公式}$

$a_{n} = \frac{\sqrt{5}}{5}\left( \frac{1 + \sqrt{5}}{2} \right)^{n} - \frac{\sqrt{5}}{5}\left( \frac{1 - \sqrt{5}}{2} \right)^{n} = \frac{\sqrt{5}}{5}\left\lbrack \left( \frac{1 + \sqrt{5}}{2} \right)^{n} - \left( \frac{1 - \sqrt{5}}{2} \right)^{n} \right\rbrack$

非齐次线性递推方程

$a_{n} + p_{k - 1}a_{n - 1} + p_{k - 2}a_{n - 2} + \cdots + p_{0}a_{1} = f(n)$

特别地，当$f(n)$是一个关于n的多项式与某个数的n次方的积时（$f(n) = \lambda^{n}P_{m}(x)$），类似于求“二阶常系数非齐次线性微分方程”的特解，该特解为

$a_{n}^{*} = n^{k}R_{m}(n)$

其中

$k = \left\{ \begin{array}{r} 0\text{，}\lambda \text{不是特征方程的根}\ \  \\ s\text{，}\lambda \text{是特征方程的}s\text{重根} \end{array} \right.\$

$R_{m}(n)$是与$P_{m}(x)$同次的多项式，可设为$A + Bn + Cn^{2} + \cdots Pn^{m}$，代入原递推关系求得系数

总结求

对于任意可写成该形式的数列都可以用该方法求得通项公式。

$eg.\text{已知}a_{n} - a_{n - 1} - a_{n - 2} = - n\text{，}a_{1} = 5\text{，}a_{2} = 8\text{，求}\left\{ a_{n} \right\}$

解：求递推方程的特解：

$- n = 1^{n}Pm(x) \Rightarrow \lambda = 1 \neq \frac{1 \pm \sqrt{5}}{2} \Rightarrow k = 0$，得到方程的特解

$a_{n}^{*} = n^{0}R_{m}(n) = C_{1}n + C_{2}$

把$a_{n}^{*}$代入非齐次递推关系$a_{n} = a_{n - 1} + a_{n - 2} - n$，得

$C_{1}n + C_{2} = C_{1}(n - 1) + C_{2} + C_{1}(n - 2) + C_{2} - n \Rightarrow \left( C_{1} - 1 \right)n + C_{2} - 3C_{1} = 0$，得$C_{1} = 1\text{，}C_{2} = 3$

故特解为$a_{n}^{*} = n + 3$

求递推方程的通解：

由特征方程的解$x_{1} = \frac{1 + \sqrt{5}}{2}\text{，}x_{2} = \frac{1 - \sqrt{5}}{2}$，得非齐次线性方程的通解

$a_{n} = C_{1}\frac{1 + \sqrt{5}}{2} + C_{2}\frac{1 - \sqrt{5}}{2} + n + 3$

代入初值条件$a_{1} = 5\text{，}a_{2} = 8\text{，}$解得

$a_{n} = \left( \frac{1 + \sqrt{5}}{2} \right)^{n} - \left( \frac{1 - \sqrt{5}}{2} \right)^{n} + n + 3$

$eg.\text{已知}a_{n} - 2a_{n - 1} + a_{n - 2} = 2\text{，}a_{1} = 1\text{，}a_{2} = 4\text{，求}\left\{ a_{n} \right\}$

解：原递推关系转化为

$a_{n} - 2a_{n - 1} - a_{n - 2} = 2$

求递推方程的特解：

解特征方程

$x^{2} - 2x + 1 = 0$

得根

$x_{1} = x_{2} = 1$

$2 = 1^{n}P_{m}(x) \Rightarrow \lambda = 1 = x_{1,2} \Rightarrow k = 2(\text{两重根})$，得到方程的特解

$a_{n}^{*} = n^{2}R_{m}(n) = C_{1}n^{2}$

把$a_{n}^{*}$代入非齐次递推关系$a_{n} - 2a_{n - 1} + a_{n - 2} = 2$，得

$C_{1}n^{2} - 2C_{1}(n - 1)^{2} + C_{1}(n - 2)^{2} = 2$

解得$C_{1} = 1$，故特解为$a_{n}^{*} = n^{2}$

求递推方程的通解：

由特征方程的解$x_{1} = x_{2} = 1$，得非齐次线性方程的通解

$a_{n} = C_{1}1^{n} + nC_{2}1^{n} + n^{2}$

代入初值条件$a_{1} = 1\text{，}a_{2} = 4\text{，}$解得

$C_{1} = C_{2} = 0$

$a_{n} = n^{2}$

阿贝尔求和

$\text{设数列}\left\{ a_{n} \right\} \text{，}\left\{ b_{n} \right\} \text{，和式}A_{k} = \sum_{i = 1}^{k}a_{i}\text{，}B_{k} = \sum_{i = 1}^{k}b_{i}\text{，则}$

$\sum_{k = 1}^{n}{a_{k}b_{k}} = a_{n}B_{n} + \sum_{k = 1}^{n - 1}{\left( a_{k} - a_{k + 1} \right)B_{k}}$

证明：

$\sum_{k = 1}^{n}{a_{n}b_{n}} = a_{1}b_{1} + \sum_{k = 2}^{n}{a_{k}b_{k}} = a_{1}B_{1} + \sum_{k = 2}^{n}{a_{k}\left( B_{k} - B_{k - 1} \right)} = a_{1}B_{1} + \sum_{k = 2}^{n}{a_{k}B_{k}} - \sum_{k = 2}^{n}{a_{k}B_{k - 1}} = \sum_{k = 1}^{n - 1}{a_{k}B_{k}} + a_{n}B_{n} - \sum_{k = 1}^{n - 1}{a_{k + 1}B_{k}} = a_{n}B_{n} + \sum_{k = 1}^{n - 1}{\left( a_{k} - a_{k + 1} \right)B_{k}}$

阿贝尔求和可以看作分部积分的离散版本，而阿贝尔求和又与差分有关。也就是说，微分与差分有一定关系。

$\sum_{i = m + 1}^{n}{\left( b_{i} - b_{i - 1} \right)a_{i}} + \sum_{i = m + 1}^{n}{\left( a_{i} - a_{i - 1} \right)b_{i}} = a_{n}b_{n} - a_{m}b_{m} = \sum_{i = m + 1}^{n}{\left( b_{i} - b_{i - 1} \right)a_{i - 1}} + \sum_{i = m + 1}^{n}{\left( a_{i} - a_{i - 1} \right)b_{i - 1}}$

Gosper算法与机械求和法

Gosper算法

> 约定代求数列是$t(k)$，裂项后得到的数列满足$t(k) = T(k + 1) - T(k)$
>
> $d_{f}$表示多项式$f(x)$的最高次项的系数（特别地，当$f(x) = 0$时，$d_{f} = - 1$）
>
> $s(k)$是待定系数的d次多项式，可以设为$a + bk + ck^{2}\cdots$

$1.\text{求}\frac{t(k + 1)}{t(k)}\text{，确定}p(k)\text{，}q(k)\text{，}r(k)\text{，使得}\$

$\frac{t(k + 1)}{t(k)} = \frac{p(k + 1)}{p(k)} \cdot \frac{q(k)}{r(k + 1)}$

$\text{且}q(k)\text{，}r(k)\text{不能被因式分解成含一次式的多项式，或一次式的常数项之差不为整数。}$

> 一种确定方法：
>
> 1.令$p(k) = 1$，$q(k) =$分母，$r(k + 1) =$分子，判定条件，成功进入下一步，失败则
>
> 2.由$q(k)$一次式的系数$\alpha$大于$r(k)$一次式的系数$\beta$，令
>
> $p(k) \leftarrow p(k)(k + \beta + 1)(k + \beta + 2)\cdots(k + \alpha - 1)$
>
> $\text{根据}\frac{t(k + 1)}{t(k)}\text{得到}q(k)r(k)\text{重新判定，成功进入下一步，失败则重复该步。}$

2.计算指标d

> $1.\text{构造}Q(k) = q(k) - r(k)\text{，}R(k) = q(k) + r(k)$
>
> $2.\left\{ \begin{array}{r} d_{Q} \geq d_{R} \Rightarrow d = d_{p} - d_{Q}\ \ \ \ \ \ \ \  \\ d_{Q} < d_{R} \Rightarrow d = d_{p} - d_{R} + 1 \end{array} \right.\$

3.计算Gasper方程

$p(k) = q(k)s(k + 1) - r(k)s(k)$

4.得出$T(k)$

$T(k) = \frac{r(k)s(k)t(k)}{p(k)}$

$eg.t(k) = k \cdot 2^{k}$

> $1.\frac{t(k + 1)}{t(k)} = \frac{2(k + 1)}{k}$
>
> $p(k) = 1\text{，}q(k) = 2(k + 1)\text{，}r(k + 1) = k\text{，}r(k) = k - 1\text{，}\alpha = 1\text{，}\beta = - 1\text{，}\alpha - \beta = 2$
>
> $p(k) = 1 \cdot \left( k + ( - 1) + 1 \right) = k\text{，}q(k) = 2\text{，}r(k) = 1\text{，}\alpha \text{，}\beta \text{不存在，成功}$
>
> $2.Q(k) = q(k) - r(k) = 2 - 1 = 11.R(k) = q(k) + r(k) = 2 + 1 = 3$
>
> $d_{Q} = d_{R} \Rightarrow d = d_{p} - d_{Q} = 1 - 0 = 1$
>
> $3.s(k) = ak + bp(k) = q(k)r(k + 1) - r(k)s(k) \Rightarrow$
>
> $k = 2\left\lbrack a(k + 1) + b \right\rbrack - (ak + b) \Rightarrow \left\{ \begin{array}{r} a = 1\ \ \  \\ b = - 1 \end{array} \right.\  \Rightarrow r(k) = k - 2$
>
> $4.T(k) = \frac{r(k)s(k)t(k)}{p(k)} = \frac{(k - 2)k \cdot 2^{k}}{k} = (k - 2)2^{k}$

$eg.t(k) = ( - 1)^{k - 1}\left( \begin{array}{r} 2n \\ k \end{array} \right)^{- 1} = ( - 1)^{k - 1}\frac{k!(2n - k)!}{(2n)!}$

> $1.\frac{t(k + 1)}{t(k)} = \frac{k + 1}{k - 2n}$
>
> $p(k) = 1\text{，}q(k) = k + 1\text{，}r(k + 1) = k - 2n\text{，}r(k) = k - 2n - 1\text{，}\alpha = 1\text{，}\beta = - 2n - 1\alpha - \beta = 2n + 2\mathbf{\text{（有}}\mathbf{n}\mathbf{\text{就成功）}}$
>
> $2.Q(k) = k + 1 - (k - 2n - 1) = 2n + 2R(k) = 2k - 4n - 1d_{Q} < d_{R} \Rightarrow d = 0 - 1 + 1 = 0$
>
> $3.s(k) = a1 = (k + 1)a - (k - 2n - 1)a = (2n + 2)a \Rightarrow a = \frac{1}{2n + 2}$
>
> $4.T(k) = \frac{(k - 2n - 1)( - 1)^{k - 1}}{2n + 2}\left( \begin{array}{r} 2n \\ k \end{array} \right)^{- 1}$

$eg.t(k) = (ak + b)q^{k - 1}$

> $1.\frac{t(k + 1)}{t(k)} = q \cdot \frac{ak + a + b}{ak + b}p(k) = ak + bq(k) = kr(k) = 1$
>
> $2.d = 1s(k) = mk + n$
>
> $3.ak + b = q(mk + m + n) - (mk + n)m = \frac{a}{q - 1}n = \frac{b - \frac{aq}{q - 1}}{q - 1}$
>
> $4.T(k) = \left( \frac{ak}{q - 1} + \frac{b - \frac{aq}{q - 1}}{q - 1} \right)q^{k - 1}$

斐波那契数列

定义

满足条件

$a_{n} = a_{n - 1} + a_{n - 2}\text{，}a_{1} = a_{2} = 1$

的数列

$1\text{，}1\text{，}2\text{，}3\text{，}5\text{，}8\text{，}13\text{，}21\text{，}34\text{，}55\text{，}89\text{，}144\text{，}\cdots$

被称为斐波那契数列

通项公式

$a_{n} = \frac{1}{\sqrt{5}}\left\lbrack \left( \frac{1 + \sqrt{5}}{2} \right)^{n} - \left( \frac{1 - \sqrt{5}}{2} \right)^{n} \right\rbrack$

尾数循环（即每一项的个位数）：

$11235\text{，}83145\text{，}94370\text{，}77145\text{，}61785\text{，}38190\text{，}99875\text{，}27965\text{，}16730\text{，}33695\text{，}49325\text{，}72910$

是一个$60$步的循环

进一步，斐波那契数列的最后两位数是一个$300$步的循环，最后三位数是一个$1500$步的循环，最后四位数是一个$15000$步的循环，最后五位数是一个$150000$步的循环。

性质

$1.\text{平方与前后项：}a_{n}^{2} - a_{n - 1} \cdot a_{n + 1} = ( - 1)^{n - 1}$

$2.\text{奇数项求和与偶数项求和：}a_{1} + a_{3} + a_{5} + \cdots + a_{2n - 1} = a_{2n}\text{，}a_{2} + a_{4} + a_{6} + \cdots + a_{2n} = a_{2n + 1} - 1$

$3.\text{平方求和：}a_{1}^{2} + a_{2}^{2} + a_{3}^{2} + \cdots + a_{n}^{2} = a_{n} \cdot a_{n + 1}$

$4.\text{隔项关系：}a_{2n - 2m - 2}\left( a_{2n} + a_{2n + 2} \right) = a_{2m + 2} + a_{4n - 2m}\ \ (n > m \geq - 1\text{，}n \geq 1)$

$5.\text{两倍项关系：}\frac{a_{2n}}{a_{n}} = a_{n - 1} + a_{n + 1}$

$6.a_{m + n + 1} = a_{m}a_{n} + a_{m + 1}a_{n + 1}$
