---
title: "概率"
hs_seq: "A10"
description: "概率：计数原理、排列组合与二项式定理"
---

# 概率

计数原理、排列组合与二项式定理

分类加法计数原理：完成一件事有两类不同方案，在第1类方案中有m种不同的方法，在第2类方案中有n种不同的方法，那么完成这件事共有$N = m + n$种不同的方法。

分布乘法计数原理：完成一件事需要两个步骤，做第1步有m种不同的方法，做第2步有n种不同的方法，那么完成这件事共有$N = m \times n$种不同的方法。

排列数：从n个不同元素中取出$m\ (m \leq n)$个元素的所有不同排列的个数，叫做从n个不同元素中取出m个元素的排列数。

$A_{n}^{m} = n(n - 1)(n - 2)\cdots(n - m + 1) = \frac{n!}{(n - m)!}\ \ \left( m\text{，}n \in \mathbb{N}^{*}\text{，}m \leq n \right)$

组合数：从n个不同元素中取出$m\ (m \leq n)$个元素的所有不同组合的个数，叫做从n个不同元素中取出m个元素的组合数。

$C_{n}^{m} = \frac{A_{n}^{n}}{A_{m}^{m}}\frac{n(n - 1)(n - 2)\cdots(n - m + 1)}{m!} = \frac{n!}{m!(n - m)!}$

组合数$C_{n}^{m}$也常写作$\left( \begin{array}{r} n \\ m \end{array} \right)$。

排列数与组合数常用公式

$nA_{n}^{n} = (n + 1)! - n! = A_{n + 1}^{n + 1} - A_{n}^{n}$

$A_{n}^{m} = \frac{n}{n - m}A_{n - 1}^{m} = nA_{n - 1}^{m - 1}$

$A_{n + 1}^{m} = A_{n}^{m} + mA_{n}^{m - 1}$

$C_{n + 1}^{m} = C_{n}^{m} + C_{n}^{m - 1}(\text{有某元素，在剩下的}n\text{个里选}m - 1\text{个；没有某元素，在剩下的}n\text{个里选}m\text{个})$

$C_{n}^{m} = C_{n}^{n - m} = \frac{n - m + 1}{m}C_{n}^{m - 1} = \frac{n}{n - m}C_{n - 1}^{m} = \frac{m + 1}{n + 1}C_{n + 1}^{m + 1} = \frac{n}{m}C_{n - 1}^{m - 1}$

$C_{n}^{0} + C_{n}^{1} + C_{n}^{2} + \cdots + C_{n}^{n} = \sum_{i = 0}^{n}C_{n}^{i} = 2^{n}$

$C_{n}^{m} = \frac{m + 1}{n + 1}C_{n + 1}^{m + 1} = \prod_{i = 1}^{p}\left( \frac{m + i}{n + i} \right)C_{n + p}^{m + p}$

$C_{r}^{r} + C_{r + 1}^{r} + C_{r + 2}^{r} + \cdots + C_{r + n}^{r} = C_{r + n + 1}^{r + 1}$

$C_{m}^{r}C_{n}^{0} + C_{m}^{r - 1}C_{n}^{1} + \cdots + C_{m}^{0}C_{n}^{r} = C_{m + n}^{r}$

$C_{n}^{1} + 2C_{n}^{2} + 3C_{n}^{3} + \cdots + nC_{c}^{n} = n2^{n - 1}$

排列组合常用方法

> 直接法：把符合条件的排列数直接列式计算。
>
> 优先法：优先安排特殊元素或特殊位置。
>
> 捆绑法：相隔问题把相邻元素看作一个整体与其他元素一起排列，同时注意捆绑元素的内部排列。
>
> 插空法：对不相邻问题，先考虑不受限制的元素的排列，再将不相邻的元素插在前面元素排列的空中。
>
> 定序问题除法问题：对于定序问题，可先不考虑顺序排列，排列后，再除以定序元素的全排列。
>
> 间接法：正难则反。
>
> 等概率法：对于某些情况，某元素满足题目情况与其它所有情况等概率，则可将总可能数直接乘概率。
>
> 排列组合常见模型

排列组合常见模型

> 1.可重复的排列求幂

定序排列问题

在$n$个元素中，要求有$m$个元素之间的顺序固定不变的排列称为定序排列问题，计算公式为$N = \frac{A_{n}^{n}}{A_{m}^{m}} = \frac{n!}{m!}$。

类似的还可以推广到一般情形，在$n$个元素中，有$n_{1}$个元素之间的顺序固定不变，又另有$n_{2}$个元素之间的顺序固定不变……一直到另有$n_{r}$个元素之间的顺序固定不变，且$n_{1} + n_{2} + \cdots + n_{r} = n$，则其排列数计算公式是$N = \frac{n!}{n_{1}!n_{2}!\cdots n_{r}!}$，

不尽相异的$n$个元素的全排列问题

在$n$个元素中，有$n_{1}$个元素相同，又另有个$n_{2}$元素相同……一直别另有$n_{r}$个元素相同，且$n_{1} + n_{2} + \cdots + n_{r} = n$，这$n$个元素的全排列叫做不尽相异的$n$个元素的全排列问题，其计算公式是$N = \frac{n!}{n_{1}!n_{2}!\cdots n_{r}!}$，其本质是相同元素之间没有顺序差别，类似于定序问题。

8重排问题：允许重复排列的问题的特点是以元素为研究对象，元素不受位置的约束，可以逐一安排各个元素的位置，一般地，$n$个不同元素没有限制地安排在$m$个位置上的排列数为$m^{n}$种，

9多排问题单排法：一般地，元素分成多排的排列问题，可先归结为一排考虑，再分段研究。

10圆排到问题单排法：

$n\left. \text{（}n \geq 3 \right.\text{）}$个不同的元素依照不同的顺序并按一定的方向（顺时针或逆时针）排成环状称为圆排列或环形排到问题，其排列数计算公式为$N = \frac{A_{n}^{n}}{n} = (n - 1)!$，其中，顺序（顺时针）不同排到的区别在于只看顺序而无首位，末位之分。

①有向环形排列。

从$n$个不同元素中任取$m$个不同元素排成一个有向环形（即区别顺时针和逆时针）的排到总数是多少？

假想将如图所示己经排好刣环剪开，随剪法的不同，可以得到以下$m$种不同的线性排到：

$a_{1},a_{2},\cdots a_{m}\text{；}a_{2},a_{3}\cdots a_{m},a_{1}\text{；}a_{3},a_{4},\cdots a_{m},a_{1},a_{2}\text{；}\cdots \text{；}a_{m},a_{1},\cdots,a_{m - 1}$

即$m$个不同的元素的钱性全排列数是环形全排列数的$m$倍，即环形全排刻数是线性全排列数除以$m$，于是有向环形排列的总数为$N = \frac{A_{n}^{m}}{m}$。

②无向环形排列。

从$n$个不同元素中任取$m$个不同元素排成一个无何环形（即不区别顺时针和逆时针）的排列总数是多少？

由无向与有向的区别可知，无向环形排列的总数是有向环环形排列的总数的一半，即总数为$N = \frac{A_{n}^{m}}{2m}$。

（11）小集团问题：先整体后局部，再结合其他策略进行外理。

（12）错排问题：编号为$1$至$n$的小球放入编号为$1$到$n$的$n$个盒子里，每个盒子放一个小球，要求小球与盒子的编号都不同，这种排列称为错为排列，特别地，当$n\text{＝}2\text{，}3\text{，}4\text{，}5$时的错位排列数分别为$1\text{，}2\text{，}9\text{，}44$。

（13）最短路径问题：平面上只有两个方向可选的最短路径问题，可抽象成$m$行，$n$列的表格从左下角到右上角的最短路径问题，易知不走回头路的向上最少步数是$m$步，向右最少步数是$n$步，则总步数是$m + n$步，所以只需要从这$m + n$步中选出向上走的$m$步，或者向右走的$n$步即可，也即最短路径走法总教，当然也等于。

单条件排列

从n个元素中取m个元素的排列。

（1）在位与不在位

1.某（特）元必在某位有$A_{n - 1}^{m - 1}$种。

2.某（特）元不在某位有$A_{n}^{m} - A_{n - 1}^{m - 1}(\text{补集思想}) = A_{n - 1}^{1}A_{n - 1}^{m - 1}(\text{着眼位置}) = A_{n - 1}^{m} + A_{m - 1}^{1}A_{n - 1}^{m - 1}(\text{着眼元素})$种。

（2）紧贴与插空（即相邻与不相邻）

1.定位紧贴：$k(k \leq m \leq n)$个元素在固定位的排列有$A_{k}^{k}A_{n - k}^{m - k}$种。

2.浮动紧贴：n个元素的全排列把k个元排在一起的派发有$A_{n - k + 1}^{n - k + 1}A_{k}^{k}$种。常用捆绑法。

3.插空：两组元素分别有k、h个$(k \leq h + 1)$，把它们合在一起作全排列，$k$个的一组互不能挨近的所有排列数有$A_{h}^{h}A_{h + 1}^{k}$种。

二项式定理

$(a + b)^{n} = C_{n}^{0}a^{n} + C_{n}^{1}a^{n - 1}b + C_{n}^{2}a^{n - 2}b^{2} + \cdots + C_{n}^{n}b^{n} = \sum_{i = 0}^{n}{C_{n}^{i}a^{n - i}b^{i}}\text{，}T_{k + 1} = C_{n}^{k}a^{n - k}b^{k}$

$(1 + x)^{n} = C_{n}^{0} + C_{n}^{1}x + C_{n}^{2}x^{2} + \cdots + C_{n}^{k}x^{k} + \cdots + C_{n}^{n}x^{n}$

当$k < \frac{n + 1}{2}$时，$C_{n}^{k}$随k的增大而增大；当$k > \frac{n + 1}{2}$时，$C_{n}^{k}$随k的增大而减小。

$\text{当}n\text{是偶数时，中间的一项}T_{\frac{n}{2} + 1} = C_{n}^{\frac{n}{2}}\text{取得最大值；当}n\text{是奇数时，中间的两项}C_{n}^{\frac{n - 1}{2}}\text{与}C_{n}^{\frac{n + 1}{2}}\text{相等，且同时}$

取得最大值。

奇数项的二次项系数的和等于偶数项的二次项系数和。

证明：设第k+1项的二项式系数取得最大值，则

$\left\{ \begin{array}{r} C_{n}^{k} \geq C_{n}^{k - 1} \Rightarrow k \leq \frac{n + 1}{2} \\ C_{n}^{k} > C_{n}^{k + 1} \Rightarrow k \geq \frac{n - 1}{2} \end{array} \right.\  \Rightarrow \frac{n - 1}{2} \leq k \leq \frac{n + 1}{2}$

设$(p + qx)^{n} = a_{0} + a_{1}x + a_{2}x^{2} + a_{3}x^{3}\cdots + a_{n}x^{n}$，则有

> $a_{k} = C_{n}^{k}p^{n - k}q^{k}$
>
> $x = 0 \Rightarrow a_{0} = p^{n}$
>
> $x = 1 \Rightarrow a_{0} + a_{1} + \cdots + a_{n} = (p + q)^{n}$
>
> $x = - 1 \Rightarrow a_{0} - a_{1} + a_{2} - a_{3}\cdots + a_{n} = (p - q)^{n}$
>
> $a_{0} + a_{2} + a_{4} + \cdots = \frac{(p + q)^{n} + (p - q)^{n}}{2}$
>
> $a_{1} + a_{3} + a_{5} + \cdots = \frac{(p + q)^{n} - (p - q)^{n}}{2}$
>
> $x = \frac{1}{2} \Rightarrow a_{0} + \frac{a_{1}}{2} + \frac{a_{2}}{4} + \frac{a_{3}}{8} + \cdots + \frac{a_{n}}{2^{n - 1}} = \left( p + \frac{1}{2}q \right)$
>
> $\left( (p + qx)^{n} \right)' = nq(p + qx)^{n - 1} = a_{1} + 2a_{2}x + 3a_{3}x^{2} + \cdots + na_{n}x^{n - 1}$
>
> $np(p + q)^{n - 1} = a_{1} + 2a_{2} + 3a_{3} + \cdots + na_{n}$

集合与概率

有关概率的一些定义

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

名称

</th>
<th>

定义

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

随机试验

</td>
<td>

对随机现象的实现和它的观察，简称试验，常用字母E表示

</td>
</tr>
<tr>
<td>

样本点

</td>
<td>

随机试验E的每个可能的基本结果，常用$\omega$表示

</td>
</tr>
<tr>
<td>

样本空间

</td>
<td>

全体样本点的集合，常用$\Omega$表示

</td>
</tr>
<tr>
<td>

有限样本空间

</td>
<td>

由n个可能结果的随机试验对应的样本空间

</td>
</tr>
<tr>
<td>

随机事件

</td>
<td>

样本空间$\Omega$的子集，简称事件

</td>
</tr>
<tr>
<td>

基本事件

</td>
<td>

只包含一个样本点的事件

</td>
</tr>
<tr>
<td>

事件A发生

</td>
<td>

在每次试验中，当且仅当A中某个样本点出现

</td>
</tr>
<tr>
<td>

必然事件

</td>
<td>

$\Omega$

</td>
</tr>
<tr>
<td>

不可能事件

</td>
<td>

$\varnothing$

</td>
</tr>
<tr>
<td>

包含

</td>
<td>

若事件A发生，则事件B一定发生，就称事件B包含事件A（或事件A包含于事件B），记作$B \supseteq A\text{或}A \subseteq B$

</td>
</tr>
<tr>
<td>

相等

</td>
<td>

事件B包含事件A，事件A也包含事件B，即$B \supseteq A$且$A \subseteq B$，则称事件A与事件B相等，记作$A = B$

</td>
</tr>
<tr>
<td>

并事件

（和事件）

</td>
<td>

事件A与事件B至少有一个发生，这样的一个事件中的样本点或者在事件A中，或者在事件B中，称这个事件为事件A与事件B的并事件（或和事件），记作$A \cup B$（或$A + B$）

</td>
</tr>
<tr>
<td>

交事件

（积事件）

</td>
<td>

事件A与事件B同时发生，这样的一个事件中的样本点既在事件A中，也在事件B中，称这样的一个事件为事件A与事件B的交事件（或积事件），记作$A \cap B$（或$AB$）

</td>
</tr>
<tr>
<td>

互斥

（互不相容）

</td>
<td>

如果事件A与事件B不能同时发生，也就是说$A \cap B$是一个不可能事件，即$A \cap B = \varnothing$，则称事件A与事件B互斥（或互不相容）

</td>
</tr>
<tr>
<td>

互为对立

</td>
<td>

如果事件A与事件B在任何一次试验中有且仅有一个发生，即$A \cup B = \Omega$，且$A \cap B = \varnothing$，那么称事件A与事件B互为对立，事件A的对立事件记为$\overline{A}$

</td>
</tr>
<tr>
<td>

两个事件的独立

（相互独立）

</td>
<td>

对任意两个事件A与B，如果$P(AB) = P(A)P(B)$成立，则称事件A与事件B相互独立，简称为独立

</td>
</tr>
<tr>
<td>

三个事件两两独立

</td>
<td>

$P(AB) = P(A)P(B)\text{，}P(AC) = P(A)P(C)\text{，}P(BC) = P(B)P(C)$

</td>
</tr>
<tr>
<td>

三个事件相互独立

</td>
<td>

$P(AB) = P(A)P(B)\text{，}P(AC) = P(A)P(C)\text{，}P(BC) = P(B)P(C)$

$P(ABC) = P(A)P(B)P(C)$

</td>
</tr>
<tr>
<td>

条件概率

</td>
<td>

$\text{设}A\text{、}B\text{为两个随机事件，且}P(A) > 0\text{，则称}P\left( B \middle| A \right) = \frac{P(AB)}{P(A)}\text{为在事件}A\text{发生的}$

$\text{条件下，事件}B\text{发生的条件概率，简称条件概率}$

</td>
</tr>
</tbody>
</table>
</div>

概率的基本关系

![全概率公式、贝叶斯公式 - 知乎](/images/hs/hs-a10/img01.png)如果事件A与事件B互斥，那么$P(A \cup B) = P(A) + P(B)$

如果事件A与事件B互为对立事件，那么$P(A) + P(B) = 1$

如果$A \subseteq B$，那么$P(A) \leq P(B)$

$P(A \cup B) = P(A + B) = \left\{ \begin{array}{r} P(A) + P(B) - P(A \cap B) \\ P(A) + P(B)(A\text{与}B\text{互斥}) \end{array} \right.\$

$P(A \cap B) = P(A \cdot B) = \left\{ \begin{array}{r} P(A)P\left( B \middle| A \right) = P(B)P\left( A \middle| B \right) \\ P(A)P(B)(A\text{与}B\text{独立})\ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

概率的其它关系

若A与B独立，则$A$与$\overline{B}$，$\overline{A}$与$B$，$\overline{A}$与$\overline{B}$都相互独立

若事件B与事件C互斥，则$P\left( (B + C) \middle| A \right) = P\left( B \middle| A \right) + P\left( C \middle| A \right)$

$P\left( A|B \right) + P\left( \overline{A} \middle| B \right) = 1$

全概率公式

设$A_{1}\text{，}A_{2}\text{，}\cdots \text{，}A_{n}$是一组两两互斥的事件，$A_{1} \cup A_{2} \cup \cdots \cup A_{n} = \Omega$，且$P\left( A_{i} \right) > 0\text{，}i = 1\text{，}2\text{，}\cdots \text{，}n$，则对于任意的事件$B \in \Omega$，有

$P(B) = \sum_{i = 1}^{n}{P\left( A_{i} \right)P\left( B|A_{i} \right)}$

贝叶斯公式

设$A_{1}\text{，}A_{2}\text{，}\cdots \text{，}A_{n}$是一组两两互斥的事件，$A_{1} \cup A_{2} \cup \cdots \cup A_{n} = \Omega$，且$P\left( A_{i} \right) > 0\text{，}i = 1\text{，}2\text{，}\cdots \text{，}n$，则对于任意的事件$B \in \Omega$，$P(B) > 0$，有

$P\left( A_{i} \middle| B \right) = \frac{P\left( A_{i}B \right)}{P(B)} = \frac{P\left( A_{i} \right)P\left( B \middle| A_{i} \right)}{P(B)} = \frac{P\left( A_{i} \right)P\left( B \middle| A_{i} \right)}{\sum_{k = 1}^{n}{P\left( A_{k} \right)P\left( B \middle| A_{k} \right)}}\text{，}i = 1\text{，}2\text{，}\cdots \text{，}n$

对于研究含两个不独立的事件的样本空间，其可以被分为如下互斥的四部分

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$AB$

</th>
<th>

$A\overline{B}$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\overline{A}B$

</td>
<td>

$\overline{A}\overline{B}$

</td>
</tr>
</tbody>
</table>
</div>

类似地，三个事件可以用由八个小正方体组成的大正方体表示。

离散型随机变量与连续型随机变量

均值（数学期望）

$E(X) = x_{i}p_{1} + x_{2}p_{2} + \cdots + x_{n}p_{n} = \sum_{i = 1}^{n}{x_{i}p_{i}}$

$E(aX + b) = aE(X) + b$

方差

> ${D(X) = \left\lbrack x_{1} - E(X) \right\rbrack^{2}p_{1} + \left\lbrack x_{2} - E(X) \right\rbrack^{2}p_{2} + \cdots + \left\lbrack x_{n} - E(X) \right\rbrack^{2}p_{n} }{= \sum_{i = 1}^{n}{\left\lbrack x_{i} - E(X) \right\rbrack^{2}p_{i}} = \sum_{i = 1}^{n}{x_{i}^{2}p_{i}} - \left( E(X) \right)^{2} = E\left( X^{2} \right) - \left( E(X) \right)^{2}}$

$D(aX + b) = a^{2}D(X)$

标准差

$\sigma(X) = \sqrt{D(X)}$

其它性质

$E\left( X_{1} + X_{2} + \cdots + X_{m} \right) = E\left( X_{1} \right) + E\left( X_{2} \right) + \cdots + E\left( X_{m} \right)$

若$X_{1}X_{2}$相互独立，则$E\left( X_{1} \cdot X_{2} \right) = E\left( X_{1} \right) \cdot E\left( X_{2} \right)$

两点分布

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$X$

</th>
<th>

$1$

</th>
<th>

$0$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$P$

</td>
<td>

$p$

</td>
<td>

$1 - p$

</td>
</tr>
</tbody>
</table>
</div>

$E(X) = p\text{，}D(X) = p(1 - p)$

二项分布

一般地，在n重伯努利实验中，设每次实验中事件A发生的概率为$p(0 < p < 1)$，用$X$表示事件$A$发生的次数，则$X$的分布列为

$P(X = k) = C_{n}^{k}p^{k}(1 - p)^{n - k}\text{，}k = 0\text{，}1\text{，}2\text{，}\cdots \text{，}n$

记作$X\sim B(n\text{，}p)$

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$X$

</th>
<th>

$0$

</th>
<th>

$1$

</th>
<th>

$\cdots$

</th>
<th>

$k$

</th>
<th>

$\cdots$

</th>
<th>

$n$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$P$

</td>
<td>

$C_{n}^{0}(1 - p)^{n}$

</td>
<td>

$C_{n}^{1}p(1 - p)^{n - 1}$

</td>
<td>

$\cdots$

</td>
<td>

$C_{n}^{k}p^{k}(1 - p)^{n - k}$

</td>
<td>

$\cdots$

</td>
<td>

$C_{n}^{n}p^{n}$

</td>
</tr>
</tbody>
</table>
</div>

$E(X) = np\text{，}D(X) = np(1 - p)$

二项分布概率取最大值的讨论

1.

$\frac{P(X = k)}{P(X = k - 1)} = 1 + \frac{(n + 1)p - k}{k(1 - p)}$

$\text{当}k < (n + 1)p\text{时，}P(X = k) > P(X = k - 1)\text{，}P(X = k)\text{随}k\text{值的增加而增加；}$

$\text{当}k > (n + 1)p\text{时，时}P(X = k) < P(X = k - 1)\text{，}P(X = k)\text{随}k\text{值的增加而减小。}$

如果$(n + 1)p$为正整数，当$k = (n + 1)p$时，$P(X = k) > P(X = k - 1)$，此时这两项概率均为最大值。

如果$(n + 1)p$为非整数，而$k$取$(n + 1)p$的整数部分，则$P(X = k)$是唯一的最大值。

2.

$(n + 1)p - 1 \leq k \leq (n + 1)p$

超几何分布

一般地，驾驶一批产品共有$N$件，其中有$M$件次品，从$N$件产品中随机抽取$n$件（不放回），用$X$表示抽取的$n$件产品中的次品数，则$X$的分布列为

$P(X = k) = \frac{C_{M}^{k}C_{N - M}^{n - k}}{C_{N}^{n}}\text{，}k = m\text{，}m + 1\text{，}m + 2\text{，}\cdots \text{，}r$

$\text{其中}n\text{，}N \in \mathbb{N}^{*}\text{，}M \leq N\text{，}n \leq N\text{，}m = \max\left\{ 0\text{，}n - N + M \right\} \text{，}r = \min\left\{ n\text{，}M \right\}$

$\text{记作}X\sim H(N\text{，}M\text{，}n)$

$E(X) = n\frac{M}{N}\text{，}D(X) = \frac{nM}{N} - \left( \frac{nM}{N} \right)^{2} + \frac{nM}{N} \cdot \frac{(n - 1)(M - 1)}{(N - 1)}$

$\text{令}p = \frac{M}{N}\text{（次品率）则}$

$E(X) = np\text{，}D(X) = np - (np)^{2} + np \cdot E\left( Y\sim H(N - 1\text{，}M - 1\text{，}n - 1) \right)$

用二项分布近似超几何分布

$P(X = k) = C_{n}^{k}\left( \frac{M}{N} \right)^{k}\left( \frac{N - M}{N} \right)^{1 - k}$

正态分布

服从正态分布的随机变量$X$的概率分布密度函数为

$f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{- \frac{(x - \mu)^{2}}{2\sigma^{2}}}\text{，}x\mathbb{\in R}\text{，其中}\mu = E(X)\text{，}\sigma^{2} = D(X)$

记作$X\sim N\left( \mu \text{，}\sigma^{2} \right)$

特别地，当$\mu = 0\text{，}\sigma = 1$时，称随机变量$X$服从标准正态分布。

$f(x)\text{关于直线}x = \mu \text{对称，在}x = \mu \text{处达到峰值}\frac{1}{\sigma\sqrt{2\pi}}$

$aX + b\sim N\left( a\mu + b\text{，}(a\sigma)^{2} \right)$

$3\sigma$原则

$P(\mu - \sigma \leq X \leq \mu + \sigma) \approx 0.6827\text{，}P(\mu - 2\sigma \leq X \leq \mu + 2\sigma) \approx 0.9545\text{，}P(\mu - 3\sigma \leq X \leq \mu + 3\sigma) \approx 0.9973$

常见离散随机分布与正态分布

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

分布

</th>
<th>

分布列

</th>
<th>

简记

</th>
<th>

均值

</th>
<th>

方差

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

两点分布

</td>
<td>

$P(X = k) = p^{k}(1 - p)^{1 - k}\text{，}k = 0\text{，}1$

</td>
<td></td>
<td>

$p$

</td>
<td>

$pq$

</td>
</tr>
<tr>
<td>

二项分布

</td>
<td>

$P(X = k) = C_{n}^{k}p^{k}(1 - p)^{n - k}\text{，}k = 0\text{，}1\text{，}\cdots \text{，}n$

</td>
<td>

$B(n\text{，}p)$

</td>
<td>

$np$

</td>
<td>

$npq$

</td>
</tr>
<tr>
<td>

超几何分布

</td>
<td>

$P(X = k) = \frac{C_{M}^{k}C_{N - M}^{n - k}}{C_{N}^{n}}$

$k = m\text{，}m + 1\text{，}m + 2\text{，}\cdots \text{，}r$

$n\text{，}N \in \mathbb{N}^{*}\text{，}M \leq N\text{，}n \leq N\text{，}$

$m = \max\left\{ 0\text{，}n - N + M \right\} \text{，}r = \min\left\{ n\text{，}M \right\}$

</td>
<td>

$H(N\text{，}M\text{，}n)$

</td>
<td>

$n\frac{M}{N}$

</td>
<td>

$\frac{nM}{N} - \left( \frac{nM}{N} \right)^{2} +$

$\frac{nM}{N} \cdot \frac{(n - 1)(M - 1)}{(N - 1)}$

</td>
</tr>
<tr>
<td>

泊松分布

</td>
<td>

$P(X = k) = \frac{\lambda^{k}}{k!}e^{\lambda}\text{，}k = 0\text{，}1$

</td>
<td></td>
<td>

$\lambda$

</td>
<td>

$\lambda$

</td>
</tr>
<tr>
<td colspan="5">

泊松分布的参数$\lambda$是单位时间（或单位面积）内随机事件的平均发生次数。

泊松分布适合于描述单位时间内随机事件发生的次数。

当二项分布的$n$很大而$p$很小时，泊松分布可作为二项分布的近似，其中$\lambda$为$np$

</td>
</tr>
<tr>
<td>

几何分布

</td>
<td>

$P(X = k) = p(1 - p)^{k - 1}\text{，}k = 1\text{，}2\text{，}\cdots$

</td>
<td>

$GE(p)$

</td>
<td>

$\frac{1}{p}$

</td>
<td>

$\frac{1 - p}{p^{2}}$

</td>
</tr>
<tr>
<td colspan="5">

定义：在$n$次伯努利试验中，记每次试验中事件$A$发生的概率为$p$，试验进行到事件$A$出现时停止，此时所进行的试验次数为$X\text{的概率。}$

</td>
</tr>
<tr>
<td>

负二项分布

</td>
<td>

$P(X = k) = C_{k - 1}^{r - 1}p^{r}(1 - p)^{k - r}\text{，}k = r\text{，}r + 1\text{，}\cdots$

</td>
<td>

$NB(r\text{，}p)$

</td>
<td>

$\frac{r}{p}$

</td>
<td>

$\frac{r(1 - p)}{p^{2}}$

</td>
</tr>
<tr>
<td colspan="5">

定义：在$n$次伯努利试验中，记每次试验中事件$A$在伯努利试验中发生的概率为$p$，试验进行$r + k$次时事件$A$刚好发生第$r$次的概率。

当$r$是整数时，负二项分布又称帕斯卡分布。

</td>
</tr>
<tr>
<td>

正态分布

</td>
<td>

$P(a < X < b) = \int_{a}^{b}{\frac{1}{\sigma\sqrt{2\pi}}e^{- \frac{(x - \mu)^{2}}{2\sigma^{2}}}}$

</td>
<td>

$N\left( \mu \text{，}\sigma^{2} \right)$

</td>
<td>

$\mu$

</td>
<td>

$\sigma^{2}$

</td>
</tr>
</tbody>
</table>
</div>
