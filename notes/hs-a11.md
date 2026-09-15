---
title: "统计"
hs_seq: "A11"
description: "统计：分类：放回简单随机抽样和不放回简单随机抽样"
---

# 统计

统计的基本概念与方法

抽样

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

总体

</td>
<td>

一个调查中对象的全体

</td>
</tr>
<tr>
<td>

个体

</td>
<td>

组成总体的每一个调查对象

</td>
</tr>
<tr>
<td>

全面调查

</td>
<td>

对每一个调查对象进行调查的方法，又称普查

</td>
</tr>
<tr>
<td>

抽样调查

</td>
<td>

根据一定的目的，从总体中抽取一部分个体进行调查，并以此为依据对总体的情况作出估计和推断的调查方法

</td>
</tr>
<tr>
<td>

样本

</td>
<td>

从总体中抽取的那部分个体

</td>
</tr>
<tr>
<td>

样本量

</td>
<td>

样本中包含的个体数

</td>
</tr>
<tr>
<td>

样本数据

</td>
<td>

调查样本获得的变量值

</td>
</tr>
</tbody>
</table>
</div>

简单随机抽样

分类：放回简单随机抽样和不放回简单随机抽样

方法：抽签法和随机数法

分层随机抽样

按一个或多个变量把总体划分成若干个子总体，每个个体属于且仅属于资一个子总体，在每个子总体中独立地进行抽样，再把所有子总体中抽取的样本合在一起作为样本，这样的抽样方法称为分层随机抽样。

频率分布直方图

求极差，决定组距和组数，将数据分组，列频率分布表，画频率分布直方图

统计图表

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

统计图表

</th>
<th>

应用场景

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

扇形图

</td>
<td>

用于直观描述各类数据占总数的比例

</td>
</tr>
<tr>
<td>

条形图

</td>
<td>

用于直观描述离散型数据分布在不同类别的频数或频率

</td>
</tr>
<tr>
<td>

直方图

</td>
<td>

用于直观描述连续型数据分布在不同类别的频数或频率

</td>
</tr>
<tr>
<td>

折线图

</td>
<td>

用于描述数据随时间的变化趋势

</td>
</tr>
</tbody>
</table>
</div>

平均数

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

层

</th>
<th>

样本平均数

</th>
<th>

总体平均数

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

单层

</td>
<td>

$\overline{x} = \sum_{i = 1}^{n}x_{i}$

</td>
<td>

$\overline{X} = \sum_{i = 1}^{N}X_{i}$

</td>
</tr>
<tr>
<td>

两层

</td>
<td>

$\overline{w} = \frac{m}{m + n}\overline{x} + \frac{n}{m + n}\overline{y}$

</td>
<td>

$\overline{W} = \frac{m}{m + n}\overline{X} + \frac{n}{m + n}\overline{Y}$

</td>
</tr>
</tbody>
</table>
</div>

加权平均数

众数

一组数据中出现次数最多的数，众数可有多个。

中位数 百分位数

中位数：将一组数据按大小顺序排好，处于中间位置的数（或中间两个数的平均数）称为这组数据的中位数。

百分位数：一般地，一组数据的百分位数是这样一个值，它使得这组数据中至少有$p\%$的数据小于或等于这个值，且至少有$(100 - p)\%$的数据大于或等于这个值。中位数是第50百分位数，与第25百分位数（第一四分位数/下四分位数），第75百分位数（第三四分位数/上四分位数）统称为四分位数。

> 计算方法：

1. 按从小到大排列数据。
2. 计算$i = n \times p\%$。
3. 若$i$不是整数，则百分位数为第$(i + 1)$项数据；若$i$是整数，则百分位数为第$i$项数据与第$(i + 1)$项数据的平均数。

> $\text{频率分布直方图：左横坐标} + \text{组距} \times \frac{\text{百分位数} - \text{左横坐标所对百分数}}{\text{右横坐标所对百分数} - \text{左横坐标所对百分数}}$

平均差

$\frac{1}{n}\sum_{i = 1}^{n}{|x_{i} - \overline{x}|}$

方差与标准差

单层

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
<th>

样本方差

</th>
<th>

总体方差

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

非加权

</td>
<td>

$s^{2} = \frac{1}{n}\sum_{i = 1}^{n}\left( x_{i} - \overline{x} \right)^{2} = \frac{1}{n}\sum_{i = 1}^{n}x_{i}^{2} - {\overline{x}}^{2}$

</td>
<td>

$S^{2} = \frac{1}{N}\sum_{i = 1}^{N}\left( X_{i} - \overline{X} \right)^{2} = \frac{1}{N}\sum_{i = 1}^{N}X_{i}^{2} - {\overline{X}}^{2}$

</td>
</tr>
<tr>
<td>

加权

</td>
<td>

$s^{2} = \frac{1}{n}\sum_{i = 1}^{k}{f_{i}\left( y_{i} - \overline{y} \right)^{2}}$

</td>
<td>

$S^{2} = \frac{1}{N}\sum_{i = 1}^{k}{f_{i}\left( Y_{i} - \overline{Y} \right)^{2}}$

</td>
</tr>
<tr>
<td colspan="3">

定义：总体的n/N个变量值中，不同的值共有k个$(k \leq n/N)$，记为$y_{1}/Y_{1}\text{，}y_{2}/Y_{2}\text{，}\cdots \text{，}y_{n}/Y_{N}$，其中$y_{i}/Y_{i}$出现的频率为$f_{i}$

</td>
</tr>
</tbody>
</table>
</div>

两层

$S_{z}^{2} = \frac{1}{m + n}\left\lbrack \sum_{i = 1}^{m}\left( \overline{z} - x_{i} \right)^{2} + \sum_{i = 1}^{n}\left( \overline{z} - y_{i} \right)^{2} \right\rbrack = \frac{m}{m + n}\left\lbrack S_{x}^{2} + \left( \overline{x} - \overline{z} \right)^{2} \right\rbrack + \frac{n}{m + n}n\left\lbrack S_{y}^{2} + \left( \overline{y} - \overline{z} \right)^{2} \right\rbrack$

频率分布直方图

绘制：求极差，决定组距与组数，将数据分组，列频率分布表，画频率分布直方图

$\text{小长方形的面积} = \text{组距} \times \frac{\text{频率}}{\text{组距}} = \text{频率}$

一般来说，对一个单峰的频率分布直方图来说，如果直方图的形状是对称的，那么平均数和中位数应该大体上差不多；如果直方图在右边“拖尾”，那么平均数大于中位数；如果直方图在左边“拖尾”，那么平均数小于中位数。也就是说，和中位数相比，平均数总是在“长尾巴”那边。

成对数据的统计分析

样本相关系数

已知数据$\left( x_{1}\text{，}y_{1} \right)\text{，}\left( x_{2}\text{，}y_{2} \right)\text{，}\cdots \text{，}\left( x_{n}\text{，}y_{n} \right)$，定义

$s_{x} = \sqrt{\frac{1}{n}\sum_{i = 1}^{n}\left( x_{i} - \overline{x} \right)^{2}}\text{，}s_{y} = \sqrt{\frac{1}{n}\sum_{i = 1}^{n}\left( y_{i} - \overline{y} \right)^{2}}\text{，}x_{i}' = \frac{x_{i} - \overline{x}}{s_{x}}\text{，}y_{i}' = \frac{y_{i} - \overline{y}}{s_{y}}$

则有

> ${r = \frac{1}{n}\sum_{i = 1}^{n}{x_{i}'y_{i}'} = \frac{1}{n}\sum_{i = 1}^{n}{\frac{x_{i} - \overline{x}}{s_{x}} \cdot \frac{y_{i} - \overline{y}}{s_{y}}} = \frac{1}{n} \cdot \frac{1}{s_{x}s_{y}}\sum_{i = 1}^{n}{\left( x_{i} - \overline{x} \right)\left( y_{i} - \overline{y} \right)} }{= \frac{\sum_{i = 1}^{n}{\left( x_{i} - \overline{x} \right)\left( y_{i} - \overline{y} \right)}}{\sqrt{\sum_{i = 1}^{n}\left( x_{i} - \overline{x} \right)^{2}}\sqrt{\sum_{i = 1}^{n}\left( y_{i} - \overline{y} \right)^{2}}} }{= \frac{\sum_{i = 1}^{n}{x_{i}y_{i}} - n\overline{x}\overline{y}}{\sqrt{\sum_{i = 1}^{n}x_{i}^{2} - n{\overline{x}}^{2}}\sqrt{\sum_{i = 1}^{n}y_{i}^{2} - n{\overline{y}}^{2}}}}$

设有n维向量

$\mathbf{x}' = \left( x_{1}'\text{，}x_{2}'\text{，}\cdots \text{，}x_{n}' \right)\text{，}\mathbf{y}' = \left( y_{1}'\text{，}y_{2}'\text{，}\cdots \text{，}y_{n}' \right)$

则

$r = \frac{1}{n}\mathbf{x}' \cdot \mathbf{y}^{\mathbf{'}}\mathbf{=}\frac{1}{n}\left| \mathbf{x}' \right|\left| \mathbf{y}^{\mathbf{'}} \right|\cos\theta = \frac{1}{n}\sqrt{n} \cdot \sqrt{n}\cos\theta = \cos\theta$

所以

$- 1 \leq r \leq 1$

一元线性回归模型

$\left\{ \begin{array}{r} Y = bx + a + e\text{，}\ \ \ \ \ \ \ \ \ \ \ \ \  \\ E(e) = 0\text{，}D(e) = \sigma^{2}\text{，} \end{array} \right.\$

与之对应的经验回归方程

$\widehat{y} = \widehat{b}x + \widehat{a}$

其中

$\left\{ \begin{array}{r} \widehat{a} = \overline{y} - \widehat{b}x\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \widehat{b} = \frac{\sum_{i = 1}^{n}{\left( x_{i} - \overline{x} \right)\left( y_{i} - \overline{y} \right)}}{\sum_{i = 1}^{n}\left( x_{i} - \overline{x} \right)^{2}} \end{array} \right.\$

特别地，点$\left( \overline{x}\text{，}\overline{y} \right)$在直线上。$\left( \widehat{y} = \widehat{b}\overline{x} + \overline{y} - \widehat{b}\overline{x} = \overline{y} \right)$

决定系数

$R^{2} = 1 - \frac{\sum_{i = 1}^{n}\left( y_{i} - {\widehat{y}}_{i} \right)^{2}}{\sum_{i = 1}^{n}\left( y_{i} - \overline{y} \right)^{2}}$

$\text{由于}\sum_{i = 1}^{n}\left( y_{i} - {\widehat{y}}_{i} \right)^{2} \leq \sum_{i = 1}^{n}\left( y_{i} - \overline{y} \right)^{2}\text{，所以当}R^{2}\text{越大时，对模型的拟合效果越好。}$

非线性回归模型设法

$y = a + \frac{b}{x}\overset{t = \frac{1}{x}}{\Rightarrow}y = a + bt$

$y = ax^{b} \Rightarrow \ln y = \ln a + b\ln x$

$y = ka^{bx} \Rightarrow \ln y = \ln k + \left( b\ln a \right)x$

列联表与独立性检验

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$X\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Y$

</th>
<th>

$Y = 0$

</th>
<th>

$Y = 1$

</th>
<th>

合计

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$X = 0$

</td>
<td>

$a$

</td>
<td>

$b$

</td>
<td>

$a + b$

</td>
</tr>
<tr>
<td>

$X = 1$

</td>
<td>

$c$

</td>
<td>

$d$

</td>
<td>

$c + d$

</td>
</tr>
<tr>
<td>

合计

</td>
<td>

$a + c$

</td>
<td>

$b + d$

</td>
<td>

$n = a + b + c + d$

</td>
</tr>
</tbody>
</table>
</div>

零假设/原假设$H_{0}$：分类变量$X$和$Y$独立。

定义

$\chi^{2} = \frac{\left\lbrack a - \frac{(a + b)(a + c)}{n} \right\rbrack^{2}}{\frac{(a + b)(a + c)}{n}} + \frac{\left\lbrack b - \frac{(a + b)(b + d)}{n} \right\rbrack^{2}}{\frac{(a + b)(b + d)}{n}} + \frac{\left\lbrack c - \frac{(c + d)(a + c)}{n} \right\rbrack^{2}}{\frac{(c + d)(a + c)}{n}} + \frac{\left\lbrack d - \frac{(c + d)(b + d)}{n} \right\rbrack^{2}}{\frac{(c + d)(b + d)}{n}}$

$= \frac{n(ad - bc)^{2}}{(a + b)(c + d)(a + c)(b + d)}$

则对于任意小概率值（临界值）$\alpha$，可以找到相应的正实数$x_{\alpha}$，使得

$P\left( \chi^{2} \geq x_{\alpha} \right) = \alpha$

成立，则当$\chi^{2} \geq x_{\alpha}$时，认为$H_{0}$不成立（X与Y不独立），该推断犯错误的几率不会超过$\alpha$；当$\chi^{2} < x_{\alpha}$时，认为$H_{0}$成立（X与Y独立）。这种利用取值推断分类变量X和Y是否独立的方法称为$\chi^{2}$独立性检验。

<div class="table-scroll">
<table>
<thead>
<tr>
<th>

$\alpha$

</th>
<th>

$0.5$

</th>
<th>

$0.4$

</th>
<th>

$0.25$

</th>
<th>

$0.15$

</th>
<th>

$0.1$

</th>
<th>

$0.05$

</th>
<th>

$0.025$

</th>
<th>

$0.01$

</th>
<th>

$0.005$

</th>
<th>

$0.001$

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

$x_{\alpha}$

</td>
<td>

$0.455$

</td>
<td>

$0.780$

</td>
<td>

$1.323$

</td>
<td>

$2.072$

</td>
<td>

$2.706$

</td>
<td>

$3.841$

</td>
<td>

$5.024$

</td>
<td>

$6.635$

</td>
<td>

$7.879$

</td>
<td>

$10.828$

</td>
</tr>
</tbody>
</table>
</div>

> 书写步骤
>
> 零假设为
>
> $H_{0}\text{：}\cdots\cdots \text{之间无关联}/\text{关系}/\text{差异}$
>
> 根据列联表中的数据，经计算得到
>
> $\chi^{2} = \cdots \approx \cdots > ( < )\cdots = x_{\alpha}$
>
> 根据小概率值$\alpha = \cdots$的独立性检验，
>
> 1.$x > x_{\alpha}$
>
> 我们推断$H_{0}$不成立，即认为$\cdots\cdots \text{之间有关联}/\text{关系}/\text{差异}$，此推断犯错误的概率不大于$\cdots\left( x_{\alpha} \right)$。
>
> 2.$x < x_{\alpha}$
>
> 没有充分证据推断$H_{0}$不成立，因此可以认为$H_{0}$成立，即认为$\cdots\cdots \text{之间无关联}/\text{关系}/\text{差异}$。

极大似然法

极大似然法用于已知概率模型（如二项分布、正态分布等）但模型的参数未知（如二项分布中的$q$，正态分布中的$\sigma$和$\mu$）的情况。运用该方法得到的模型的参数会使得已知样本结果出现的可能性最大。

$eg.$不透明袋子中装有除颜色外完全相同的黑球和白球，进行100次有放回随机抽样，抽到黑球70次，白球30次。袋子中黑球与白球的比例最可能为多少？

解：设袋子中黑球的比例为$p$，则抽到70次黑球30次白球的概率为

$C_{100}^{70}p^{70} \cdot (1 - p)^{30}$

根据极大似然估计的思想，要寻找$p$，使得上式的值最大（即出现这个情况的概率最大），于是设

$f(x) = C_{100}^{70}x^{70} \cdot (1 - x)^{30}\ \ \left( x \in (0\text{，}1) \right)$

令其导函数等于0，得

$f'(x) = C_{100}^{70}\left\lbrack 70x^{69}(1 - x)^{30} - 30x^{70}(1 - x)^{29} \right\rbrack = C_{100}^{70}x^{69}(1 - x)^{29}\left\lbrack 70(1 - x) - 30x \right\rbrack = 0$

解得$x = 0.7$，得到袋子中黑球与白球的比例最可能为$7:3$。
