---
title: "集合论与逻辑术语"
hs_seq: "B1"
description: "集合论与逻辑术语：证明：由两个集合的容斥原理得"
---

# 集合论与逻辑术语

朴素集合论与逻辑术语

外延公理：$(\forall u\text{，}u \in X \Leftrightarrow u \in Y) \Leftrightarrow X = Y$

配对公理：

朴素集合论

集合定律

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

容斥原理

证明：由两个集合的容斥原理得

$|A + B + C| = \left| (A + B) + C \right| = |A + B| + |C| - \left| (A + B)C \right| = |A| + |B| - |AB| + |C| - |AC + BC| = |A| + |B| - |AB| + |C| - |AC| - |BC| + \left| (AC)(BC) \right| = |A| + |B| + |C| - |AB| - |AC| - |BC| + |ABC|$

同理可得

$|A \cup B \cup C \cup D| = |A| + |B| + |C| + |D| - |A \cap B| - |A \cap C| - |A \cap D| - |B \cap C| - |B \cap D| - |C \cap D| + |A \cap B \cap C| + |A \cap B \cap D| + |A \cap C \cap D| + |B \cap C \cap D| - |A \cap B \cap C \cap D|$

运用数学归纳法，可以完成n个集合情况的证明

$|A \cap B \cap C| \geq |A| + |B| + |C| - 2|A \cup B \cup C|$

集合的直积

$A \times B = \left\{ (x\text{，}y)|x \in A\text{，}y \in B \right\}$

逻辑术语

命题

命题的定义在各领域不同，且有模糊和分歧，当前可定义如下：

定义：一般地，在数学中，我们把用语言、符号或式子表达的，可以判断真假的陈述句叫做命题。其中判断为真的语句叫做真命题，判断为假的语句叫做假命题。

在当前，可以把命题看作是非真即假的，命题的真假也被称为真值，真命题对应T（1），假命题对应F（0）。这种逻辑也称为二值逻辑。这类似于电路与编程。

用模糊的语言表达的判断真假的陈述句在数学上不算命题。

对于含有变量的语句，如果变量有全称量词或存在量词（或者说明确写明了取值范围），则该语句是命题，否则便不是命题，在在自变量在全体实数范围时正确的语句，即使它没有全称量词或存在量词，也是命题。

下面给出一些例子

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

语句

</th>
<th>

是否为命题

</th>
<th>

如果是命题，它的真假

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$2 + 2 = 5$

</td>
<td>

是

</td>
<td>

假

</td>
</tr>
<tr>
<td>

后天放假吗？

</td>
<td>

否

</td>
<td></td>
</tr>
<tr>
<td>

这才是好题。

</td>
<td>

否

</td>
<td></td>
</tr>
<tr>
<td>

他是个好人。

</td>
<td>

否

</td>
<td></td>
</tr>
<tr>
<td>

血是红色的。

</td>
<td colspan="2">

否（在未限定范围的情况下无法判断真假）

</td>
</tr>
<tr>
<td>

$2x + 1$是整数

</td>
<td>

否

</td>
<td></td>
</tr>
<tr>
<td>

$\forall x\mathbb{\in R}\text{，}x\text{是整数}$

</td>
<td>

是

</td>
<td>

假

</td>
</tr>
<tr>
<td>

$x > 2$

</td>
<td>

否

</td>
<td></td>
</tr>
<tr>
<td>

$\forall x < 1\text{，}x > 2$

</td>
<td>

是

</td>
<td>

假

</td>
</tr>
<tr>
<td>

$x^{2} + 1 > 0$

</td>
<td>

是

</td>
<td>

真

</td>
</tr>
<tr>
<td>

$x > 1\text{或}x \leq 1$

</td>
<td>

是

</td>
<td>

真

</td>
</tr>
</tbody>
</table>
</div>

联结词

1.否定词“$\neg$”

$\neg P\text{读作}``\text{非}P"\text{。当且仅当}P\text{为假时，}\neg P\text{为真。}$

2.合取词“$\land$”

$P \land Q\text{读作}``P\text{且}Q"\text{或}``P\text{合取}Q"\text{。当且仅当}P\text{和}Q\text{都为真时，}P \land Q\text{为真。}$

3.析取词“$\vee$”

$P \vee Q\text{读作}``P\text{或}Q"\text{或}``P\text{析取}Q"\text{。当且仅当}P\text{和}Q\text{都为假时，}P \vee Q\text{为假。}$

4.蕴含词“$\rightarrow$”

$P \rightarrow Q\text{读作}``P\text{推}Q"\text{或}``P\text{蕴含}Q"\text{。当且仅当}P\text{真而}Q\text{假时，}P \rightarrow Q\text{为假。}$

其中$P$被称为前提/前件，$Q$称为结论/后件，$P \rightarrow Q$称为假言命题/条件命题。

当$P$为真时，$Q$的真假决定了$P \rightarrow Q$的真假；当$P$为假时，实际上的$P \rightarrow Q$情况是未知的。为了让蕴含词有一个明确的定义，本着不轻易进行否定的思想，作了这种定义。

蕴含式与充分条件/必要条件不同。充分条件/必要条件中$P \Rightarrow Q$的$P$是一个条件（不加验证地正确），而蕴含式$P \rightarrow Q$中的$P$是一个命题，可以为真也可以为假。

对蕴含式的理解与生活经验有不同。因为$P$可以是假的，$P$与$Q$可以是完全无关的，例如对于以下命题

$P\text{：}1 + 1 = 0 \rightarrow Q\text{：小河豚是奥运冠军}$

由于$1 + 1 = 0$是假命题，所以$P \rightarrow Q$为真。

5.双条件词/等价词“$\leftrightarrow$”

$P \leftrightarrow Q\text{读作}``P\text{等价}Q"\text{或}``P\text{当且仅当}Q"\text{。当且仅当}P\text{和}Q\text{真值相同时，}P \leftrightarrow Q\text{为真。}$

上述的联结词更像是门电路或编程中的逻辑运算符，而与日常有差异，这中点体现在析取词、蕴含词和双条件词/等价词上。

下面给出其真值表

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$P$

</th>
<th>

$Q$

</th>
<th>

$\neg P$

</th>
<th>

$\neg Q$

</th>
<th>

$P \land Q$

</th>
<th>

$P \vee Q$

</th>
<th>

$P \rightarrow Q$

</th>
<th>

$P \leftrightarrow Q$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

0

</td>
<td>

0

</td>
<td>

1

</td>
<td>

0

</td>
<td>

0

</td>
<td>

0

</td>
<td>

1

</td>
<td>

1

</td>
</tr>
<tr>
<td>

0

</td>
<td>

1

</td>
<td>

1

</td>
<td>

1

</td>
<td>

0

</td>
<td>

1

</td>
<td>

1

</td>
<td>

0

</td>
</tr>
<tr>
<td>

1

</td>
<td>

0

</td>
<td>

0

</td>
<td>

0

</td>
<td>

0

</td>
<td>

1

</td>
<td>

0

</td>
<td>

0

</td>
</tr>
<tr>
<td>

1

</td>
<td>

1

</td>
<td>

0

</td>
<td>

1

</td>
<td>

1

</td>
<td>

1

</td>
<td>

1

</td>
<td>

1

</td>
</tr>
</tbody>
</table>
</div>

并举例（把联结词转化为对应的读法）

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

命题

</th>
<th>

真值

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$1 + 1 = 2\text{且}2 + 2 = 5$

</td>
<td>

0

</td>
</tr>
<tr>
<td>

$1 + 1 = 2\text{或}2 + 2 = 5$

</td>
<td>

1

</td>
</tr>
<tr>
<td>

$1 + 1 = 2\text{推}2 + 2 = 5$

</td>
<td>

1

</td>
</tr>
<tr>
<td>

$2 + 2 = 5\text{推}1 + 1 = 2$

</td>
<td>

1

</td>
</tr>
<tr>
<td>

$1 + 1 = 2\text{等价}2 + 2 = 5$

</td>
<td>

0

</td>
</tr>
<tr>
<td>

$1 + 1 = 2\text{等价}x^{2} + 1 > 0$

</td>
<td>

1

</td>
</tr>
<tr>
<td>

$2 + 2 = 5\text{等价}x^{2} + 1 < 0$

</td>
<td>

1

</td>
</tr>
</tbody>
</table>
</div>

量词

全称量词$(\forall)$ 存在量词$(\exists)$

命题的形式

逆命题：对于两个命题，如果一个命题的条件和结论分别是另外一个命题的结论和条件，那么这两个命题叫做互逆命题，其中一个命题叫做原命题，另外一个命题叫做原命题的逆命题。

否命题：对于两个命题，如果一个命题的条件和结论分别是另外一个命题的条件的否定和结论的否定，那么这两个命题叫做互否命题，其中一个命题叫做原命题，另外一个命题叫做原命题的否命题。

逆否命题：对于两个命题，如果一个命题的条件和结论分别是另外一个命题的结论的否定和条件的否定，那么这两个命题叫做互为逆否命题，其中一个命题叫做原命题，另外一个命题叫做原命题的逆否命题。

命题的否定：将命题的结论否定（把“是”改成“不是”），而将所有的全称量词与存在量词翻转。

下面给出一些例子

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

原命题

</th>
<th>

逆命题

</th>
<th>

否命题

</th>
<th>

逆否命题

</th>
<th>

命题的否定

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$1 + 1 = 2$

</td>
<td>

无

</td>
<td>

无

</td>
<td>

无

</td>
<td>

$1 + 1 \neq 2$

</td>
</tr>
<tr>
<td>

三角形的面积是$\pi r^{2}$。

</td>
<td>

面积满足$\pi r^{2}$的几何图形是三角形。

</td>
<td>

三角形的面积不是$\pi r^{2}$。

</td>
<td>

面积不满足$\pi r^{2}$的几何图形不是三角形。

</td>
<td>

三角形的面积不是$\pi r^{2}$。

</td>
</tr>
<tr>
<td colspan="5">

该例中，否命题与命题的否定相同。

</td>
</tr>
<tr>
<td>

$\forall x\mathbb{\in R}\text{，}x > 2$（$x\mathbb{\in R \Rightarrow}x > 2$）

</td>
<td>

$x > 2 \Rightarrow x\mathbb{\in R}$

</td>
<td>

不$\exists x\mathbb{\in R}$使得$x \leq 2$

</td>
<td>

若$x \leq 2$，则$x$不是实数

</td>
<td>

$\forall x\mathbb{\in R}\text{，}x < 2$

</td>
</tr>
<tr>
<td>

$a > 3 \Rightarrow a > 2$

</td>
<td>

$a > 2 \Rightarrow a > 3$

</td>
<td>

$a \leq 3 \Rightarrow a \leq 2$

</td>
<td>

$a \leq 2 \Rightarrow a \leq 3$

</td>
<td>

$a > 3 \nRightarrow a > 2$（$a > 3 \Rightarrow a \leq 2$）

</td>
</tr>
<tr>
<td>

若$x > 1$，则$f\left. \text{（}x \right.\text{）} = (x - 1)^{2}$单调递增。

</td>
<td>

若$f\left. \text{（}x \right.\text{）} = (x - 1)^{2}$单调递增，则$x > 1$

</td>
<td>

若$x \leq 1$，则$f\left. \text{（}x \right.\text{）} = (x - 1)^{2}$不单调递增。

</td>
<td>

若$f\left. \text{（}x \right.\text{）} = (x - 1)^{2}$不单调递增，则$x \leq 1$。

</td>
<td>

若$x > 1$，则$f\left. \text{（}x \right.\text{）} = (x - 1)^{2}$不单调递增

</td>
</tr>
<tr>
<td>

我爱你。（如果有一个人是我，那么这个人爱你。）

</td>
<td>

如果有个人爱你，那么这个人是我。

</td>
<td>

如果有个人不是我，那么这个人不爱你。

</td>
<td>

如果一个人不爱你，那么这个人不是我。

</td>
<td>

我不爱你。（如果有一个人是我，那么这个人不爱你。）

</td>
</tr>
<tr>
<td colspan="5">

上述例子中，否命题与命题的否定不同。

</td>
</tr>
</tbody>
</table>
</div>

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

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

命题

</th>
<th>

原命题

</th>
<th>

逆命题

</th>
<th>

否命题

</th>
<th>

逆否命题

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

表达形式

</td>
<td>

若$p$则$q\ \ (p \Rightarrow q)$

</td>
<td>

若$q$则$p\ \ (q \Rightarrow p)$

</td>
<td>

若$\neg p$则$\neg q\ \ (p \Rightarrow \neg q)$

</td>
<td>

若$\neg q$则$\neg p\ \ (\neg q \Rightarrow \neg p)$

</td>
</tr>
<tr>
<td rowspan="4">

真假对应关系

</td>
<td>

真

</td>
<td>

可真可假

</td>
<td>

可真可假

</td>
<td>

真

</td>
</tr>
<tr>
<td>

假

</td>
<td>

可真可假

</td>
<td>

可真可假

</td>
<td>

假

</td>
</tr>
<tr>
<td>

可真可假

</td>
<td>

真

</td>
<td>

真

</td>
<td>

可真可假

</td>
</tr>
<tr>
<td>

可真可假

</td>
<td>

假

</td>
<td>

假

</td>
<td>

可真可假

</td>
</tr>
</tbody>
</table>
</div>

“真假对应关系”某一行上的判断同时成立。
