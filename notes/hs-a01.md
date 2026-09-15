---
title: "集合与常用逻辑术语"
hs_seq: "A1"
description: "集合与常用逻辑术语：空集不包含任何元素，空集是任何集合的子集"
---

# 集合与常用逻辑术语

常用数集及其记法

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

数集

</th>
<th>

自然数集（非负整数集）

</th>
<th>

正整数集

</th>
<th>

整数集

</th>
<th>

有理数集

</th>
<th>

实数集

</th>
<th>

复数集

</th>
<th>

空集

</th>
<th>

全集

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

符号

</td>
<td>

$\mathbb{N}$

</td>
<td>

$\mathbb{N}^{*}\text{或}\mathbb{N}_{+}$

</td>
<td>

$\mathbb{Z}$

</td>
<td>

$\mathbb{Q}$

</td>
<td>

$\mathbb{R}$

</td>
<td>

$\mathbb{C}$

</td>
<td>

$\varnothing$

</td>
<td>

$U$

</td>
</tr>
</tbody>
</table>
</div>

> 可以在符号的右下角添加$+$或$-$表示正数部分或负数部分。

空集

空集不包含任何元素，空集是任何集合的子集

集合的性质

> 1.确定性：集合的元素必须是确定的。
>
> $eg.$“所有好学生”不是集合。
>
> 2.互异性：对于一个给定的集合，集合中的元素一定是不同的。
>
> $eg.\text{集合}\left\{ 1\text{，}a\text{，}a^{2} \right\}$中$a$一定不为$\pm 1$。$\left\{ \varnothing \text{，}\left\{ \varnothing \right\} \right\}$是集合。
>
> 3.无序性：集合中的元素可以任意排列。
>
> $eg.\left\{ 1\text{，}2\text{，}3 \right\} = \left\{ 3\text{，}2\text{，}1 \right\} \text{，}\left\{ (1\text{，}2) \right\} \neq \left\{ (2\text{，}1) \right\}$

集合的表示

1.列举法

$eg.$小于10的自然数的集合：$\left\{ 0\text{，}1\text{，}2\text{，}3\text{，}4\text{，}5\text{，}6\text{，}7\text{，}8\text{，}9 \right\}$

2.描述法

$eg.\left\{ x|x \in A\text{，或}x \in B \right\}$

A$\cup \$B

A$\cap \$B

A

B

元素与集合的关系

属于“$\in$”与不属于“$\notin$”。

元素可以是数也可以是集合。集合中的元素可以全是数或是集合，也可以两者兼有，甚至可以是空集或以空集为某个元素的集合。

$eg.1 \in \left\{ 1\text{，}2\text{，}3 \right\} \text{。}\left\{ 1 \right\} \in \left\{ \left\{ 1 \right\} \right\} \text{。}1 \notin \left\{ \left\{ 1 \right\} \right\} \text{。}1 \notin \varnothing \text{。}\varnothing \notin \varnothing(\text{前一个}\varnothing \text{看作元素，后一个}\varnothing \text{看作集合})\text{。}$

$\varnothing \in \left\{ \varnothing \right\} \text{。}\left\{ \varnothing \right\} \in \left\{ \left\{ \varnothing \right\} \right\} \text{。}\varnothing \notin \left\{ \left\{ \varnothing \right\} \right\}$

集合的关系

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

关系

</th>
<th>

定义

</th>
<th>

举例

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

相等集合

</td>
<td>

$\forall x \in A\text{，}x \in B\text{；}\forall x \in B\text{，}x \in A \Rightarrow A = B$

</td>
<td>

$\left\{ 1 \right\} = \left\{ 0.\dot{9} \right\} \text{。}\varnothing \neq \left\{ \varnothing \right\} \neq \left\{ \left\{ \varnothing \right\} \right\} \text{。}\phi = \phi$

</td>
</tr>
<tr>
<td>

子集

</td>
<td>

$\forall x \in A\text{，}x \in B \Rightarrow A \subseteq B\text{或}B \supseteq A$

</td>
<td>

$\mathbb{N \subseteq Z}\text{。}\varnothing \subseteq \varnothing \text{。}\varnothing \subseteq \left\{ \varnothing \right\} \text{。}$

</td>
</tr>
<tr>
<td>

真子集

</td>
<td>

$\forall x \in A\text{，}x \in B\text{；}\exists x \in B\text{，}x \notin A \Rightarrow A \subsetneqq B\text{或}B \supsetneqq A$

</td>
<td>

$\left\{ 1 \right\} \subsetneqq \left\{ 1\text{，}2\text{，}3 \right\} \text{，} \supsetneqq$

</td>
</tr>
<tr>
<td>

并集

</td>
<td>

$A \cap B = \left\{ x|x \in A\text{，或}x \in B \right\}$

</td>
<td>

$\left\{ 1\text{，}2 \right\} \cup \left\{ 2\text{，}3 \right\} = \left\{ 1\text{，}2\text{，}3 \right\}$

</td>
</tr>
<tr>
<td>

交集

</td>
<td>

$A \cup B = \left\{ x|x \in A\text{，且}x \in B \right\}$

</td>
<td>

$\left\{ 1\text{，}2 \right\} \cap \left\{ 2\text{，}3 \right\} = \left\{ 2 \right\}$

</td>
</tr>
<tr>
<td>

相对补集

</td>
<td>

$A/B = A - B = \left\{ x|x \in A\text{，且}x \notin B \right\}$

</td>
<td>

$\left\{ 1\text{，}2 \right\} - \left\{ 2\text{，}3 \right\} = \left\{ 1 \right\}$

</td>
</tr>
<tr>
<td>

绝对补集

</td>
<td>

$\complement_{U}A = \sim A = A' = A^{\complement} = \left\{ x|x \in A\text{，且}x \notin U \right\}$

</td>
<td>

$\complement_{\mathbb{N}}\mathbb{N}^{*} = \left\{ 0 \right\}$

</td>
</tr>
</tbody>
</table>
</div>

区间

对于任意$a < b$，有

$a < x < b \Leftrightarrow x \in (a\text{，}b)\text{，称为开区间。}$

$a \leq x \leq b \Leftrightarrow x \in \lbrack a\text{，}b\rbrack \text{，称为闭区间。}$

> $\begin{matrix} a < x \leq b \Leftrightarrow x \in (a\text{，}b\rbrack \\ a \leq x < b \Leftrightarrow x \in \lbrack a\text{，}b) \end{matrix}\text{，称为半开半闭区间。}$

$\lbrack a\text{，}a\rbrack$称为退化区间，但写作$\left\{ a \right\}$。

含有$\pm \infty$的区间称为无界区间，不属于上述任意一种。

以$x_{0}$为中心的任何开区间称为点$x_{0}$的邻域，记作$U\left( x_{0} \right)$；在$U\left( x_{0} \right)$中去掉中心$x_{0}$后，称为点$x_{0}$的去心邻域，记作$\overset{o}{U}\left( x_{0} \right)$。

元素为数集的集合可被称为类。

集合的运算

交换律：$A \cup B = B \cup A\text{，}A \cap B = B \cap A$

结合律：$A \cup (B \cup C) = (A \cup B) \cup C\text{，}A \cap (B \cap C) = (A \cap B) \cap C$

分配对偶律：$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)\text{，}A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$

对偶律：$(A \cup B)' = A' \cap B'\text{，}(A \cap B)' = A' \cup B'$

同一律：$A \cup \varnothing = A\text{，}A \cap U = A$

求补律：$A \cup A' = U\text{，}A \cap A' = \varnothing$

对合律：$A^{''} = A$

等幂律：$A \cup A = A\text{，}A \cap A = A$

零一律：$A \cup U = U\text{，}A \cap \varnothing = \varnothing$

吸收律：$A \cup (A \cap B) = A\text{，}A \cap (A \cup B) = A$

反演律（德·摩根定律）：$(A \cup B)' = A' \cap B'\text{，}\left( A \cap B' \right) = A' \cup B'$

容斥律：$card(A \cup B) = card(A) + card(B) - card(A \cap B)$

> $card(A \cup B \cup C)$
>
> $= card(A) + card(B) + card(C) - card(A \cap B) - card(A \cap C) - card(B \cap C) - card(A \cap B \cap C)$
>
> （其中$card(A)$表示集合$A$中元素的个数）

集合条件的转化

$A \cup B = A \Longleftrightarrow A \subseteq B \Longleftrightarrow A \cap \complement_{U}B = \varnothing \Leftrightarrow x \in A\text{是}x \in B\text{的充分条件}$

$A \cap B = A \Longleftrightarrow A \supseteq B \Longleftrightarrow \complement_{U}A \cap B = \varnothing \Leftrightarrow x \in A\text{是}x \in B\text{的必要条件}$

充分条件与必要条件

若$p \Rightarrow q$，则称$p$是$q$（成立的）充分条件，$q$是$p$（成立的）必要条件。

$p\ \ \  \Rightarrow \ \ \ q$

充分条件 必要条件

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

p是q的充分不必要条件

</th>
<th>

$p \Rightarrow q\text{且}q \nRightarrow p$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

p是q的必要不充分条件

</td>
<td>

$p \nRightarrow q\text{且}q \Rightarrow p$

</td>
</tr>
<tr>
<td>

p是q的充要条件

</td>
<td>

$p \Leftrightarrow q$

</td>
</tr>
<tr>
<td>

p是q的既不充分也不必要条件

</td>
<td>

$p \nRightarrow q\text{且}q \nRightarrow p$

</td>
</tr>
</tbody>
</table>
</div>

$\text{充要性的证明：}p\text{成立的充要条件是}q \Leftrightarrow q\text{是}p\text{的充要条件}$

若$p \Rightarrow q$，则$\neg q \Rightarrow \neg p$。（$p$是$q$的充分条件$\Leftrightarrow \neg p$是$\neg q$的必要条件）
