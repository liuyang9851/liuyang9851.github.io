---
title: 三角类函数
description: 三角函数的级数定义、三角与双曲函数公式对比、各类三角函数与反函数的定义域值域、导数与积分。
---
# 三角类函数

[[toc]]

三角类函数

## 三角函数的严格定义

三角函数可用级数严格地定义，其形式为

>

$$\sin x = x - \frac{x^{3}}{3!} + \frac{x^{5}}{5!} - \frac{x^{7}}{7!} + \ldots = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{(2n + 1)!}x^{2n + 1}}$$

>
>

$$\cos x = 1 - \frac{x^{2}}{2!} + \frac{x^{4}}{4!} - \frac{x^{6}}{6!} + \ldots = \sum_{n = 0}^{\infty}{\frac{( - 1)^{n}}{(2n)!}x^{2n}}$$

## 三角函数与双曲函数公式对比

我们先得到一个三角恒等式，然后把里面的sin或者cos全部转为sinh或cosh，如果在公式中出现两个sin相乘，那么把前面的符号改成负号

$$\sinh(ix) = i\sin x$$

$$\cosh(ix) = \cos x$$

<div class="table-scroll">
<table>

<thead>
<tr>
<th></th>
<th>

三角函数

</th>
<th>

双曲函数

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

定义

</td>
<td>

$$\sin\alpha = \frac{y}{r}\ \ \ \cos\alpha = \frac{x}{r}$$

$$\tan\alpha = \frac{y}{x}\ \ \ \cot\alpha = \frac{x}{y}$$

$$\sec\alpha = \frac{r}{x}\ \ \ \csc\alpha = \frac{r}{y}$$

</td>
<td>

$${sinh}x = \frac{e^{x} - e^{- x}}{2}\ \ \ \cosh x = \frac{e^{x} + e^{- x}}{2}$$

$$\tanh x = \frac{e^{x} - e^{- x}}{e^{x} + e^{- x}}\ \ \ \coth x = \frac{e^{x} + e^{- x}}{e^{x} - e^{- x}}$$

$${sech}x = \frac{2}{e^{x} + e^{- x}}\ \ \ {csch}x = \frac{2}{e^{x} - e^{- x}}$$

</td>
</tr>
<tr>
<td>

速记图

</td>
<td></td>
<td></td>
</tr>
<tr>
<td>

倒数关系

</td>
<td>

sin α ⋅ csc α = 1

cos α ⋅ sec α = 1

tan α ⋅ cot α = 1

</td>
<td>

sin hx ⋅ cschx = 1

cosh x ⋅ sinh x = 1

tanh x ⋅ coth x = 1

</td>
</tr>
<tr>
<td>

商数关系

</td>
<td>

sin α = cos α ⋅ tan α

cos α = sin α ⋅ cot α

tan α = sin α ⋅ sec α

cot α = cos α ⋅ csc α

sec α = tan α ⋅ csc α

csc α = cot α ⋅ sec α

</td>
<td>

sinh x = cosh x ⋅ tanh x

cosh x = sinh x ⋅ coth x

tanh x = sinh x ⋅ sechx

coth x = cosh x ⋅ cschx

sechx = tanh x ⋅ cschx

cschx = coth x ⋅ sechx

</td>
</tr>
<tr>
<td>

平方关系

</td>
<td>

sin2α + cos2α = 1

tan2α + 1 = sec2α

1 + cot2α = csc2α

</td>
<td>

sinh2x + 1 = cosh2x

tanh2x + sech2x = 1

1 + csch2x = coth2x

</td>
</tr>
<tr>
<td>

和/差角公式

</td>
<td>

sin (α + β) = sin αcos β + cos αsin β

sin (α − β) = sin αcos β − cos αsin β

cos (α + β) = cos αcos β − sin αsin β

cos (α − β) = cos αcos β + sin αsin β

$$\tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta}$$

$$\tan(\alpha - \beta) = \frac{\tan\alpha - \tan\beta}{1 + \tan\alpha\tan\beta}$$

</td>
<td>

sinh (x + y) = sinh xcosh y + cosh xsinh y

sinh (x − y) = sinh xcosh y − cosh xsinh y

cosh (x + y) = cosh xcosh y + sinh xsinh y

cosh (x − y) = cosh xcosh y − sinh xsinh y

$$\tanh(x + y) = \frac{\tanh x + \tanh y}{1 + \tanh x\tanh y}$$

$$\tanh(x - y) = \frac{\tanh x - \tanh y}{1 - \tanh x\tanh y}$$

</td>
</tr>
<tr>
<td>

二倍角公式

</td>
<td>

$$\sin{2\alpha} = 2\sin\alpha\cos\alpha = \frac{2\tan\alpha}{1 + \tan^{2}\alpha}$$

$$\cos{2\alpha} = \cos^{2}\alpha - \sin^{2}\alpha = 2\cos^{2}\alpha - 1 = 1 - 2\sin^{2}\alpha = \frac{1 - \tan^{2}\alpha}{1 + \tan^{2}\alpha}$$

$$\tan{2\alpha} = \frac{2\tan\alpha}{1 - \tan^{2}\alpha}$$

</td>
<td>

$$\sinh{2x} = 2\sinh x\cosh x = \frac{2\tanh x}{1 - \tanh^{2}x}$$

$$\cosh{2x} = \sinh^{2}x + \cosh^{2}x = 2\sinh^{2}x + 1 = 2\cosh^{2}x - 1 = \frac{1 + \tanh^{2}x}{1 - \tanh^{2}x}$$

$$\tanh{2x} = \frac{2\tanh x}{1 + \tanh^{2}x}$$

</td>
</tr>
<tr>
<td>

万能公式

</td>
<td>

$$\sin\alpha = \frac{2\tan\frac{\alpha}{2}}{1 + \tan^{2}\frac{\alpha}{2}}$$

$$\cos\alpha = \frac{1 - \tan^{2}\frac{\alpha}{2}}{1 + \tan^{2}\frac{\alpha}{2}}$$

$$\tan\alpha = \frac{2\tan\frac{\alpha}{2}}{1 - \tan^{2}\frac{\alpha}{2}}$$

</td>
<td>

$$\sinh x = \frac{2\tanh\frac{x}{2}}{1 - \tanh^{2}\frac{x}{2}}$$

$$\cosh x = \frac{1 + \tanh^{2}\frac{x}{2}}{1 - \tanh^{2}\frac{x}{2}}$$

$$\tanh x = \frac{2\tanh\frac{x}{2}}{1 + \tanh^{2}\frac{x}{2}}$$

</td>
</tr>
<tr>
<td>

降幂扩角公式

</td>
<td>

$$\sin^{2}\alpha = \frac{1 - \cos{2\alpha}}{2}$$

$$\cos^{2}\alpha = \frac{1 + \cos{2\alpha}}{2}$$

$$\tan^{2}\alpha = \frac{1 - \cos{2\alpha}}{1 + \cos{2\alpha}}$$

$$\sin\alpha\cos\alpha = \frac{1}{2}\sin{2\alpha}$$

</td>
<td>

$$\sinh^{2}x = \frac{\cosh{2x} - 1}{2}$$

$$\cosh^{2}x = \frac{\cosh{2x} + 1}{2}$$

$$\tanh^{2}x = \frac{\cosh{2x} - 1}{\cosh{2x} + 1}$$

</td>
</tr>
<tr>
<td>

三倍角公式

</td>
<td>

$$\sin{3\alpha} = 3\sin\alpha - 4\sin^{3}\alpha = 4\sin\alpha\sin\left( \frac{\pi}{3} + \alpha \right)\sin\left( \frac{\pi}{3} - \alpha \right)$$

$$\cos{3\alpha} = - 3\cos\alpha + 4\cos^{3}\alpha = 4\cos\alpha\cos\left( \frac{\pi}{3} + \alpha \right)\cos\left( \frac{\pi}{3} - \alpha \right)$$

$$\tan{3\alpha} = \frac{3\tan\alpha - \tan^{3}\alpha}{1 - 3\tan^{2}\alpha} = \tan\alpha\tan\left( \frac{\pi}{3} + \alpha \right)\tan\left( \frac{\pi}{3} - \alpha \right)$$

</td>
<td>

sinh 3x = 3sinh x + 4sinh3x

cosh 3x = −3cosh x + 4cosh3x

</td>
</tr>
<tr>
<td>

和差化积公式

</td>
<td>

$$\sin\alpha + \sin\beta = 2\sin\left( \frac{\alpha + \beta}{2} \right)\cos\left( \frac{\alpha - \beta}{2} \right)$$

$$\sin\alpha - \sin\beta = 2\cos\left( \frac{\alpha + \beta}{2} \right)\sin\left( \frac{\alpha - \beta}{2} \right)$$

$$\cos\alpha + \cos\beta = 2\cos\left( \frac{\alpha + \beta}{2} \right)\cos\left( \frac{\alpha - \beta}{2} \right)$$

$$\cos\alpha - \cos\beta = - 2\sin\left( \frac{\alpha + \beta}{2} \right)\sin\left( \frac{\alpha - \beta}{2} \right)$$

tan α + tan β = tan (α + β)(1 − tan αtan β)

tan α − tan β = tan (α − β)(1 + tan αtan β)

</td>
<td>

$$\sinh x + \sinh y = 2\sinh\frac{x + y}{2}\cosh\frac{x - y}{2}$$

$$\sinh x - \sinh y = 2\cosh\frac{x + y}{2}\sinh\frac{x - y}{2}$$

$$\cosh x + \cosh y = 2\cosh\frac{x + y}{2}\cosh\frac{x - y}{2}$$

$$\cosh x - \cosh y = 2\sinh\frac{x + y}{2}\sinh\frac{x - y}{2}$$

</td>
</tr>
<tr>
<td>

积化和差公式

</td>
<td>

$$\sin\alpha\sin\beta = - \frac{1}{2}\left\lbrack \cos(\alpha + \beta) - \cos(\alpha - \beta) \right\rbrack$$

$$\sin\alpha\cos\beta = \frac{1}{2}\left\lbrack \sin(\alpha + \beta) + \sin(\alpha - \beta) \right\rbrack$$

$$\cos\alpha\sin\beta = \frac{1}{2}\left\lbrack \sin(\alpha + \beta) - \sin(\alpha - \beta) \right\rbrack$$

$$\cos\alpha\cos\beta = \frac{1}{2}\left\lbrack \cos(\alpha + \beta) + \cos(\alpha - \beta) \right\rbrack$$

$$\tan\alpha\tan\beta = 1 - \frac{\tan\alpha + \tan\beta}{\tan(\alpha + \beta)} = \frac{\tan\alpha - \tan\beta}{\tan(\alpha - \beta)} - 1$$

</td>
<td>

$$\sinh x\sinh y = \frac{1}{2}\left\lbrack \cosh(x + y) - \cosh(x - y) \right\rbrack$$

$$\sinh x\cosh y = \frac{1}{2}\left\lbrack \sinh(x + y) + \sinh(x - y) \right\rbrack$$

$$\cosh x\cosh y = \frac{1}{2}\left\lbrack \sinh(x + y) - \sinh(x - y) \right\rbrack$$

$$\cosh x\cosh y = \frac{1}{2}\left\lbrack \cosh(x + y) + \cosh(x - y) \right\rbrack$$

</td>
</tr>
<tr>
<td>

半角公式

</td>
<td>

$$\sin\frac{\alpha}{2} = \pm \sqrt{\frac{1 - \cos\alpha}{2}}$$

$$\cos\frac{\alpha}{2} = \pm \sqrt{\frac{1 + \cos\alpha}{2}}$$

$$\tan\frac{\alpha}{2} = \pm \sqrt{\frac{1 - \cos\alpha}{1 + \cos\alpha}} = \frac{\sin\alpha}{1 + \cos\alpha} = \frac{1 - \cos\alpha}{\sin\alpha}$$

</td>
<td>

$$\sinh\frac{x}{2} = \pm \sqrt{\frac{\cosh x - 1}{2}}$$

$$\cosh\frac{x}{2} = \pm \sqrt{\frac{\cosh x + 1}{2}}$$

$$\tanh\frac{x}{2} = \pm \sqrt{\frac{\cosh x - 1}{\cosh x + 1}} = \frac{\sinh x}{1 + \cosh x} = \frac{\cosh x - 1}{\sinh x}$$

</td>
</tr>
</tbody>
</table>
</div>

通过这两个函数，就可以定义出其他的函数。

## 三角函数类的定义

下面用表格形式给出所有三角函数与其相关函数、类似函数的定义，导数与积分

<div class="table-scroll">
<table style="width:100%;">

<thead>
<tr>
<th>

函数

</th>
<th>

符号

</th>
<th>

定义

</th>
<th>

导数

</th>
<th>

积分

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

正弦

反正弦

</td>
<td>

sin

arcsin

</td>
<td>

$$\frac{y}{r}$$

sin的反函数

</td>
<td>

cos x

$$\frac{1}{\sqrt{1 - x^{2}}}$$

</td>
<td>

−cos x + C

$$x\arcsin x + \sqrt{1 - x^{2}} + C$$

</td>
</tr>
<tr>
<td>

余弦

反余弦

</td>
<td>

cos

arccos

</td>
<td>

$$\frac{x}{r}$$

cos的反函数

</td>
<td>

−sin x

$$- \frac{1}{\sqrt{1 - x^{2}}}$$

</td>
<td>

sin x + C

$$x\arccos x - \sqrt{1 - x^{2}} + C$$

</td>
</tr>
<tr>
<td>

正切

反正切

</td>
<td>

tan

arctan

</td>
<td>

$$\frac{y}{x}\text{/}\frac{\sin x}{\cos x}$$

tan的反函数

</td>
<td>

sec2x

$$\frac{1}{1 + x^{2}}$$

</td>
<td>

−ln |cos x| + C

$$x\arctan x - \frac{1}{2}\ln\left( 1 + x^{2} \right) + C$$

</td>
</tr>
<tr>
<td>

余切

反余切

</td>
<td>

cot

arccot

</td>
<td>

$$\frac{x}{y}\text{/}\frac{1}{\tan x}$$

cot的反函数

</td>
<td>

−csc2x

$$- \frac{1}{1 + x^{2}}$$

</td>
<td>

ln |sin x| + C

$$x{arccot}x + \frac{1}{2}\ln\left( 1 + x^{2} \right) + C$$

</td>
</tr>
<tr>
<td>

正割

反正割

</td>
<td>

sec

acrsec

</td>
<td>

$$\frac{r}{x}\text{/}\frac{1}{\cos x}$$

sec的反函数

</td>
<td>

sec xtan x

$$\frac{1}{x^{2}\sqrt{1 - x^{- 2}}}$$

</td>
<td>

$$\ln\left| \tan\left( \frac{\pi}{4} + \frac{x}{2} \right) \right| + C = \ln\left| \sec x + \tan x \right| + C$$

$$x{arcsec}x - \ln\left( x + \sqrt{x^{2} - 1} \right) + C$$

</td>
</tr>
<tr>
<td>

余割

反余割

</td>
<td>

csc

arccsc

</td>
<td>

$$\frac{r}{y}\text{/}\frac{1}{\sin x}$$

csc的反函数

</td>
<td>

−csc xcot x

$$- \frac{1}{x^{2}\sqrt{1 - x^{- 2}}}$$

</td>
<td>

$$\ln\left| \tan\frac{x}{2} \right| + C = \ln\left| \csc x - \cot x \right| + C$$

$$x{arccsc}x + \ln\left( x + \sqrt{x^{2} - 1} \right) + C$$

</td>
</tr>
<tr>
<td>

正矢

半正矢

</td>
<td>

versin

haversin

</td>
<td>

1 − cos x

$$\frac{1 - \cos x}{2}$$

</td>
<td>

sin x

$$\frac{\sin x}{2}$$

</td>
<td>

x − sin x + C

$$\frac{x - \sin x}{2} + C$$

</td>
</tr>
<tr>
<td>

余矢

半余矢

</td>
<td>

coversin

hacoversin

</td>
<td>

1 − sin x

$$\frac{1 - \sin x}{2}$$

</td>
<td>

−cos x

$$- \frac{\cos x}{2}$$

</td>
<td>

x + cos x + C

$$\frac{x + \cos x}{2} + C$$

</td>
</tr>
<tr>
<td>

外正割

</td>
<td>

exsec

</td>
<td>

sec x − 1

</td>
<td>

sec xtan x

</td>
<td>

$$\ln\left| \tan\left( \frac{\pi}{4} + \frac{x}{2} \right) \right| - x + C$$

= ln |sec x + tan x| − x + C

</td>
</tr>
<tr>
<td>

外余割

</td>
<td>

excec

</td>
<td>

csc x − 1

</td>
<td>

−csc xcot x

</td>
<td>

$$\ln\left| \tan\frac{x}{2} \right| - x + C$$

= ln |csc x − cot x| + C

</td>
</tr>
<tr>
<td>

双曲正弦

反双曲正弦

</td>
<td>

sinh

arsinh

</td>
<td>

$$\frac{e^{x} - e^{- x}}{2}$$

$$\ln\left( x + \sqrt{x^{2} + 1} \right)$$

</td>
<td>

cosh x

$$\frac{1}{\sqrt{1 + x^{2}}}$$

</td>
<td>

cosh x + C

</td>
</tr>
<tr>
<td>

双曲余弦

反双曲余弦

</td>
<td>

cosh

arcosh

</td>
<td>

$$\frac{e^{x} + e^{- x}}{2}$$

$$\ln\left( x + \sqrt{x^{2} - 1} \right)$$

</td>
<td>

sinh x

$$\frac{1}{\sqrt{x^{2} - 1}}$$

</td>
<td>

sinh x + C

</td>
</tr>
<tr>
<td>

双曲正切

反双曲正切

</td>
<td>

tanh

artanh

</td>
<td>

$$\frac{e^{x} - e^{- x}}{e^{x} + e^{- x}}$$

$$\frac{1}{2}\ln\frac{1 + x}{1 - x}$$

</td>
<td>

sech2x

$$\frac{1}{1 - x^{2}}$$

</td>
<td>

ln (cosh x) + C

</td>
</tr>
<tr>
<td>

双曲余切

反双曲余切

</td>
<td>

coth

arcoth

</td>
<td>

$$\frac{e^{x} + e^{- x}}{e^{x} - e^{- x}}$$

$$\frac{1}{2}\ln\frac{x + 1}{x - 1}$$

</td>
<td>

−csch2x

$$\frac{1}{1 - x^{2}}$$

</td>
<td>

ln (sinh x) + C

</td>
</tr>
<tr>
<td>

双曲正割

反双曲正割

</td>
<td>

sech

arsech

</td>
<td>

$$\frac{2}{e^{x} + e^{- x}}$$

</td>
<td>

−tanh xsechx

</td>
<td>

arctan (sinh x) + C

</td>
</tr>
<tr>
<td>

双曲余割

反双曲余割

</td>
<td>

csch

arcsch

</td>
<td>

$$\frac{2}{e^{x} - e^{- x}}$$

</td>
<td>

−coth xcschx

</td>
<td>

$$\ln\left| \tanh\frac{x}{2} \right| + C$$

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

三角函数

</th>
<th>

正弦

</th>
<th>

余弦

</th>
<th>

正切

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

解析式

</td>
<td>

y = sin x

</td>
<td>

y = cos x

</td>
<td>

y = tan x

</td>
</tr>
<tr>
<td>

定义域

</td>
<td>

ℝ

</td>
<td>

ℝ

</td>
<td>

$$\left\{ x|x \neq \frac{\pi}{2} + k\pi,k\mathbb{\in Z} \right\}$$

</td>
</tr>
<tr>
<td>

值域

</td>
<td>

[0，1]

</td>
<td>

[0，1]

</td>
<td>

ℝ

</td>
</tr>
<tr>
<td>

奇偶性

</td>
<td>

奇函数

</td>
<td>

偶函数

</td>
<td>

奇函数

</td>
</tr>
<tr>
<td>

周期

</td>
<td>

2π

</td>
<td>

2π

</td>
<td>

π

</td>
</tr>
<tr>
<td>

对称轴

</td>
<td>

$$x = \frac{\pi}{2} + k\pi$$

</td>
<td>

x = kπ

</td>
<td></td>
</tr>
<tr>
<td>

对称中心

</td>
<td>

(kπ，0)

</td>
<td>

$$\left( \frac{\pi}{2} + k\pi \text{，}0 \right)$$

</td>
<td>

$$\left( \frac{k}{2}\pi \text{，}0 \right)$$

</td>
</tr>
<tr>
<td>

单调区间

</td>
<td>

增区间

</td>
<td>

$$\left( - \frac{\pi}{2}\text{，}\frac{\pi}{2} \right) + 2k\pi$$

</td>
<td>

(−π，0) + 2kπ

</td>
<td>

$$\left( - \frac{\pi}{2}\text{，}\frac{\pi}{2} \right) + k\pi$$

</td>
</tr>
<tr>
<td>

减区间

</td>
<td>

$$\left( \frac{\pi}{2}\text{，}\frac{3\pi}{2} \right) + 2k\pi$$

</td>
<td>

(0，π) + 2kπ

</td>
<td></td>
</tr>
<tr>
<td>

极值点

</td>
<td>

极大值点

</td>
<td>

$$x = \frac{\pi}{2} + 2k\pi$$

</td>
<td>

x = 2kπ

</td>
<td></td>
</tr>
<tr>
<td>

极小值点

</td>
<td>

$$x = - \frac{\pi}{2} + 2k\pi$$

</td>
<td>

x = π + 2kπ

</td>
</tr>
<tr>
<td>

简图的特殊点

</td>
<td>

$(0\text{，}0)\ \left( \frac{\pi}{2}\text{，}1 \right)\ (\pi \text{，}0)$

$\left( \frac{3}{2}\pi \text{，} - 1 \right)\ (2\pi \text{，}0)$

</td>
<td>

$(0\text{，}1)\ \left( \frac{\pi}{2}\text{，}0 \right)\ (\pi \text{，} - 1)$

$\left( \frac{3}{2}\pi \text{，}0 \right)\ (2\pi \text{，}1)$

</td>
<td></td>
</tr>
<tr>
<td>

三角函数

</td>
<td>

余割

</td>
<td>

正割

</td>
<td>

余切

</td>
</tr>
<tr>
<td>

解析式

</td>
<td>

y = csc x

</td>
<td>

y = sec x

</td>
<td>

y = cot x

</td>
</tr>
<tr>
<td>

定义域

</td>
<td>

{x | x ≠ kπ，k ∈ ℤ}

</td>
<td>

$$\left\{ x\ |\ x \neq \frac{\pi}{2} + k\pi \text{，}k\mathbb{\in Z} \right\}$$

</td>
<td>

{x | x ≠ kπ，k ∈ ℤ}

</td>
</tr>
<tr>
<td>

值域

</td>
<td>

(−∞， − 1] ∪ [1， + ∞)

</td>
<td>

(−∞， − 1] ∪ [1， + ∞)

</td>
<td>

ℝ

</td>
</tr>
<tr>
<td>

奇偶性

</td>
<td>

奇函数

</td>
<td>

偶函数

</td>
<td>

奇函数

</td>
</tr>
<tr>
<td>

周期

</td>
<td>

2π

</td>
<td>

2π

</td>
<td>

π

</td>
</tr>
<tr>
<td>

对称轴

</td>
<td>

$$x = \frac{\pi}{2} + k\pi$$

</td>
<td>

x = kπ

</td>
<td></td>
</tr>
<tr>
<td>

对称中心

</td>
<td>

(kπ，0)

</td>
<td>

$$\left( \frac{\pi}{2} + k\pi \text{，}0 \right)$$

</td>
<td>

$$\left( \frac{k}{2}\pi \text{，}0 \right)$$

</td>
</tr>
<tr>
<td>

单调区间

</td>
<td>

增区间

</td>
<td>

$$\left( \frac{\pi}{2}\text{，}\pi \right) + 2k\pi \text{，}$$

$$\left( \pi \text{，}\frac{3\pi}{2} \right) + 2k\pi$$

</td>
<td>

$$\left( 0\text{，}\frac{\pi}{2} \right) + 2k\pi \text{，}$$

$$\left( \frac{\pi}{2}\text{，}\pi \right) + 2k\pi$$

</td>
<td></td>
</tr>
<tr>
<td>

减区间

</td>
<td>

$$\left( - \frac{\pi}{2}\text{，}0 \right) + 2k\pi \text{，}$$

$$\left( 0\text{，}\frac{\pi}{2} \right) + 2k\pi$$

</td>
<td>

$$\left( - \pi \text{，} - \frac{\pi}{2} \right) + 2k\pi \text{，}$$

$$\left( - \frac{\pi}{2}\text{，}0 \right) + 2k\pi$$

</td>
<td>

(0，π) + kπ

</td>
</tr>
<tr>
<td>

极值点

</td>
<td>

极大值点

</td>
<td>

$$x = - \frac{\pi}{2} + 2k\pi$$

</td>
<td>

x = π + 2kπ

</td>
<td></td>
</tr>
<tr>
<td>

极小值点

</td>
<td>

$$x = \frac{\pi}{2} + 2k\pi$$

</td>
<td>

x = 2kπ

</td>
</tr>
</tbody>
</table>
</div>

<div class="table-scroll">
<table style="width:100%;">

<thead>
<tr>
<th>

反三角函数

</th>
<th>

反正弦

</th>
<th>

反余弦

</th>
<th>

反正切

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

解析式

</td>
<td>

y = arcsin x

</td>
<td>

y = arccos x

</td>
<td>

y = arctan x

</td>
</tr>
<tr>
<td>

定义域

</td>
<td>

[−1，1]

</td>
<td>

[−1，1]

</td>
<td>

ℝ

</td>
</tr>
<tr>
<td>

值域

</td>
<td>

$$\left\lbrack - \frac{\pi}{2}\text{，}\frac{\pi}{2} \right\rbrack$$

</td>
<td>

[1，π]

</td>
<td>

$$\left\lbrack - \frac{\pi}{2}\text{，}\frac{\pi}{2} \right\rbrack$$

</td>
</tr>
<tr>
<td>

奇偶性

</td>
<td>

奇函数

</td>
<td>

非奇非偶函数

</td>
<td>

奇函数

</td>
</tr>
<tr>
<td>

周期

</td>
<td></td>
</tr>
<tr>
<td>

对称轴

</td>
<td></td>
</tr>
<tr>
<td>

对称中心

</td>
<td>

(0，0)

</td>
<td>

$$\left( 0\text{，}\frac{\pi}{2} \right)$$

</td>
<td>

(0，0)

</td>
</tr>
<tr>
<td>

单调区间

</td>
<td>

增区间

</td>
<td>

[−1，1]

</td>
<td></td>
<td>

ℝ

</td>
</tr>
<tr>
<td>

减区间

</td>
<td></td>
<td>

[−1，1]

</td>
<td></td>
</tr>
<tr>
<td>

极值点

</td>
<td>

极大值点

</td>
<td></td>
</tr>
<tr>
<td>

极小值点

</td>
</tr>
<tr>
<td>

反三角函数

</td>
<td>

反余割

</td>
<td>

反正割

</td>
<td>

反余切

</td>
</tr>
<tr>
<td>

解析式

</td>
<td>

y = arccscx

</td>
<td>

y = arcsecx

</td>
<td>

y = arccotx

</td>
</tr>
<tr>
<td>

定义域

</td>
<td>

(−∞， − 1] ∪ [1， + ∞)

</td>
<td>

(−∞， − 1] ∪ [1， + ∞)

</td>
<td>

ℝ

</td>
</tr>
<tr>
<td>

值域

</td>
<td>

$$\left\lbrack 0\text{，}\frac{\pi}{2} \right)\  \cup \ \left( \frac{\pi}{2}\text{，}\ \pi \right\rbrack$$

</td>
<td>

$$\left\lbrack 0\text{，}\frac{\pi}{2} \right)\  \cup \ \left( \frac{\pi}{2}\text{，}\ \pi \right\rbrack$$

</td>
<td>

$$\left\lbrack - \frac{\pi}{2}\text{，}\frac{\pi}{2} \right\rbrack$$

</td>
</tr>
<tr>
<td>

奇偶性

</td>
<td>

非奇非偶函数

</td>
<td>

非奇非偶函数

</td>
<td>

奇函数

</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

周期

</td>
<td></td>
</tr>
<tr>
<td>

对称轴

</td>
<td></td>
</tr>
<tr>
<td>

对称中心

</td>
<td>

$$\left( 0\text{，}\frac{\pi}{2} \right)$$

</td>
<td>

$$\left( 0\text{，}\frac{\pi}{2} \right)$$

</td>
<td>

(0，0)

</td>
</tr>
<tr>
<td>

单调区间

</td>
<td>

增区间

</td>
<td></td>
<td>

(−∞， − 1] ∪ [1， + ∞)

</td>
<td></td>
</tr>
<tr>
<td>

减区间

</td>
<td>

(−∞， − 1] ∪ [1， + ∞)

</td>
<td></td>
<td>

ℝ

</td>
</tr>
<tr>
<td>

极值点

</td>
<td>

极大值点

</td>
<td></td>
</tr>
<tr>
<td>

极小值点

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

双曲函数

</th>
<th>

双曲正弦

</th>
<th>

双曲余弦

</th>
<th>

双曲正切

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

解析式

</td>
<td>

y = sinh x

$$y = \frac{e^{x} - e^{- x}}{2}$$

</td>
<td>

y = cosh x

$$y = \frac{e^{x} + e^{- x}}{2}$$

</td>
<td>

y = tanh x

$$y = \frac{e^{x} - e^{- x}}{e^{x} + e^{- x}}$$

</td>
</tr>
<tr>
<td>

定义域

</td>
<td>

ℝ

</td>
<td>

ℝ

</td>
<td>

ℝ

</td>
</tr>
<tr>
<td>

值域

</td>
<td>

ℝ

</td>
<td>

[1， + ∞)

</td>
<td>

(−1，1)

</td>
</tr>
<tr>
<td>

奇偶性

</td>
<td>

奇函数

</td>
<td>

偶函数

</td>
<td>

奇函数

</td>
</tr>
<tr>
<td>

周期

</td>
<td></td>
</tr>
<tr>
<td>

对称轴

</td>
<td></td>
<td>

x = 0

</td>
<td></td>
</tr>
<tr>
<td>

对称中心

</td>
<td>

(0，0)

</td>
<td></td>
<td>

(0，0)

</td>
</tr>
<tr>
<td>

单调区间

</td>
<td>

增区间

</td>
<td>

ℝ

</td>
<td>

(−∞，0)

</td>
<td>

ℝ

</td>
</tr>
<tr>
<td>

减区间

</td>
<td></td>
<td>

(0， + ∞)

</td>
<td></td>
</tr>
<tr>
<td>

极值点

</td>
<td>

极大值点

</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

极小值点

</td>
<td>

x = 0

</td>
</tr>
<tr>
<td>

双曲函数

</td>
<td>

双曲余割

</td>
<td>

双曲正割

</td>
<td>

双曲余切

</td>
</tr>
<tr>
<td>

解析式

</td>
<td>

y = cschx

$$y = \frac{2}{e^{x} - e^{- x}}$$

</td>
<td>

y = sechx

$$y = \frac{2}{e^{x} + e^{- x}}$$

</td>
<td>

y = coth x

$$y = \frac{e^{x} + e^{- x}}{e^{x} - e^{- x}}$$

</td>
</tr>
<tr>
<td>

定义域

</td>
<td>

(−∞，0) ∪ (0， + ∞)

</td>
<td>

ℝ

</td>
<td>

(−∞，0) ∪ (0， + ∞)

</td>
</tr>
<tr>
<td>

值域

</td>
<td>

(−∞，0) ∪ (0， + ∞)

</td>
<td>

(0，1]

</td>
<td>

(−∞， − 1) ∪ (1， + ∞)

</td>
</tr>
<tr>
<td>

奇偶性

</td>
<td>

奇函数

</td>
<td>

偶函数

</td>
<td>

奇函数

</td>
</tr>
<tr>
<td>

周期

</td>
<td></td>
</tr>
<tr>
<td>

对称轴

</td>
<td></td>
<td>

x = 0

</td>
<td></td>
</tr>
<tr>
<td>

对称中心

</td>
<td>

(0，0)

</td>
<td></td>
<td>

(0，0)

</td>
</tr>
<tr>
<td>

单调区间

</td>
<td>

增区间

</td>
<td></td>
<td>

(−∞，0)

</td>
<td></td>
</tr>
<tr>
<td>

减区间

</td>
<td>

(−∞，0)，(0， + ∞)

</td>
<td>

(0， + ∞)

</td>
<td>

(−∞，0)，(0， + ∞)

</td>
</tr>
<tr>
<td>

极值点

</td>
<td>

极大值点

</td>
<td></td>
<td>

x = 0

</td>
<td></td>
</tr>
<tr>
<td>

极小值点

</td>
<td></td>
</tr>
</tbody>
</table>
</div>

<div class="table-scroll">
<table>

<thead>
<tr>
<th>

反双曲函数

</th>
<th>

反双曲正弦

</th>
<th>

反双曲余弦

</th>
<th>

反双曲正切

</th>
</tr>
</thead>
<tbody>
<tr>
<td>

解析式

</td>
<td>

y = arsinhx

$$y = \ln\left( x + \sqrt{x^{2} + 1} \right)$$

</td>
<td>

y = arcoshx

$$y = \ln\left( x + \sqrt{x^{2} - 1} \right)$$

</td>
<td>

y = artanhx

$$y = \frac{1}{2}\ln\frac{1 + x}{1 - x}$$

</td>
</tr>
<tr>
<td>

定义域

</td>
<td>

ℝ

</td>
<td>

[1， + ∞)

</td>
<td>

(−1，1)

</td>
</tr>
<tr>
<td>

值域

</td>
<td>

ℝ

</td>
<td>

[0， + ∞)

</td>
<td>

ℝ

</td>
</tr>
<tr>
<td>

奇偶性

</td>
<td>

奇函数

</td>
<td>

非奇非偶函数

</td>
<td>

奇函数

</td>
</tr>
<tr>
<td>

周期

</td>
<td></td>
</tr>
<tr>
<td>

对称轴

</td>
<td></td>
</tr>
<tr>
<td>

对称中心

</td>
<td>

(0，0)

</td>
<td></td>
<td>

(0，0)

</td>
</tr>
<tr>
<td>

单调区间

</td>
<td>

增区间

</td>
<td>

ℝ

</td>
<td>

[1， + ∞)

</td>
<td>

(−1，1)

</td>
</tr>
<tr>
<td>

减区间

</td>
<td></td>
</tr>
<tr>
<td>

极值点

</td>
<td>

极大值点

</td>
<td></td>
</tr>
<tr>
<td>

极小值点

</td>
</tr>
<tr>
<td>

反双曲函数

</td>
<td>

反双曲余割

</td>
<td>

反双曲正割

</td>
<td>

反双曲余切

</td>
</tr>
<tr>
<td>

解析式

</td>
<td>

y = arcschx

$$y = \ln\frac{1 + \sqrt{1 + x^{2}}}{x}$$

</td>
<td>

y = arsechx

$$y = \ln\frac{1 + \sqrt{1 - x^{2}}}{x}$$

</td>
<td>

y = arcothx

$$y = \frac{1}{2}\ln\frac{x + 1}{x - 1}$$

</td>
</tr>
<tr>
<td>

定义域

</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

值域

</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

奇偶性

</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

周期

</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

对称轴

</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

对称中心

</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

单调区间

</td>
<td>

增区间

</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

减区间

</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

极值点

</td>
<td>

极大值点

</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>

极小值点

</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>
