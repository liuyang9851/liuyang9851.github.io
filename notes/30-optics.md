---
title: 光学
description: 光程与半波损失、杨氏双缝干涉、薄膜干涉与等倾干涉、牛顿环、惠更斯-菲涅耳原理、单缝与圆孔衍射、光栅衍射、光的偏振、马吕斯定律与布鲁斯特定律。
---

# 光学

[[toc]]

L = c ⋅ Δt

由

$$\Delta t = \frac{l}{v},\ \ v = \frac{c}{n}$$

得

L = nl

### 波程差

$$\Delta\varphi = 2\pi\frac{\Delta r}{\lambda}$$

### 半波损失

光波由光疏介质入射到光密介质时，反射光会有π的相位突变。

### 相干光的光程差与相位差

$$\delta = n_{2}r_{2} - n_{1}r_{1},\ \ \Delta\varphi = 2\pi\frac{\delta}{\lambda}$$

## 杨氏双缝干涉

![杨氏双缝干涉示意图：两缝间距 2a，缝到屏距离 D](/images/physics/young-double-slit.png)

在折射率为n的介质中，光程差满足

$$\delta = \Delta r = r_{2} - r_{1} = nd\frac{x}{D} = n2a\frac{x}{D} = \left\{ \begin{array}{r}
2k \cdot \frac{\lambda}{2}\ \ \ \ \ \ \ \ \ \ \ \ (\text{明纹}) \\
(2k + 1) \cdot \frac{\lambda}{2}\ (\text{暗纹})
\end{array} \right.\ ,\ \ k = 0,1,2,\cdots$$

特别地

$$\Delta x = \frac{D\lambda}{nd} = \frac{D\lambda}{2an}$$

条纹重叠时，有

(k + 1)λmin = kλmax

得

$$k = \frac{\lambda_{\min}}{\lambda_{\max} - \lambda_{\min}} = \frac{\lambda_{\min}}{\Delta\lambda}$$

实际中取[k]（向上取整）

![薄膜干涉示意图：上表面反射光 2、3 的干涉光路](/images/physics/thin-film-interference.png)

## 薄膜干涉的光程差

![薄膜干涉示意图：上下表面反射光的干涉光路](/images/physics/equal-inclination.png)

上表面的干涉（2和3）

$$\delta = 2e\sqrt{n_{2}^{2} - n_{1}^{2}\sin^{2}i} + \frac{\lambda}{2}$$

下表面的干涉（4和5）

$$\delta = 2e\sqrt{n_{2}^{2} - n_{1}^{2}\sin^{2}i}$$

## 等倾干涉

![等倾干涉示意图：同一倾角的光线形成同一级干涉条纹](/images/physics/equal-inclination-2.png)

$$\delta = 2e\sqrt{n_{2}^{2} - n_{1}^{2}\sin^{2}i} + \frac{\lambda}{2} = \left\{ \begin{array}{r}
2k \cdot \frac{\lambda}{2}\ \ \ \ \ \ \ \ \ \ \ \ (\text{明环}) \\
(2k + 1) \cdot \frac{\lambda}{2}\ (\text{暗环})
\end{array} \right.\ $$

劈尖干涉（等厚干涉）

![劈尖干涉（等厚干涉）示意图：两玻璃板夹一劈尖，相邻条纹厚度差 Δe](/images/physics/wedge-interference.png)

$$\delta = 2n_{2}e_{k} + \left( \frac{\lambda}{2} \right),\ \ \Delta e = \frac{\lambda}{2n_{2}} = \frac{\lambda'}{2},\ \ l = \frac{\Delta e}{\sin\theta} = \frac{\lambda}{2n_{2}\theta}$$

![牛顿环示意图：平凸透镜与平板玻璃间的环形等厚干涉条纹](/images/physics/newton-rings.png)

## 牛顿环

$$r = \left\{ \begin{array}{r}
\sqrt{\frac{(2k - 1)R\lambda}{2n_{2}}},\ \ k = 1,2,3,\cdots \\
\sqrt{\frac{kR\lambda}{n_{2}}},\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ k = 0,1,2,\cdots
\end{array} \right.\ $$

惠更斯—菲涅耳原理

$$E = \int_{S}^{}{dE} = C\int_{S}^{}{\frac{k(\theta)}{r}\cos\left( \omega t - \frac{2\pi nr}{\lambda} \right)dS}$$

## 单缝夫琅禾费衍射

![单缝夫琅禾费衍射装置示意图：缝宽 a，衍射角 φ](/images/physics/single-slit-setup.png)![单缝衍射半波带示意图：缝宽被分为若干半波带](/images/physics/single-slit-bands.png)

![单缝衍射半波带示意图（续）：不同衍射角对应的半波带数](/images/physics/single-slit-bands-2.png)![单缝衍射光程差与半波带分布示意图](/images/physics/single-slit-bands-3.png)

光程差

$$\delta = a\sin\varphi = \left\{ \begin{array}{r}
 \pm (2k + 1)\frac{\lambda}{2},\ \ k = 1,2,3,\cdots \\
 \pm 2k\frac{\lambda}{2},\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ k = 1,2,3,\cdots
\end{array} \right.\ $$

这里的(2k + 1)和2k代表有几个半波带。

### 角位置

![单缝衍射明暗纹角位置示意图：衍射角 φ 与级次 k 的关系](/images/physics/single-slit-angular.png)

$$\varphi = \left\{ \begin{array}{r}
 \pm \arcsin\left\lbrack (2k + 1)\frac{\lambda}{2a} \right\rbrack = \pm (2k + 1)\frac{\lambda}{2a},\ \ k = 1,2,3,\cdots \\
 \pm \arcsin\left\lbrack (2k)\frac{\lambda}{2a} \right\rbrack = \pm (2k)\frac{\lambda}{2a},\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ k = 1,2,3,\cdots
\end{array} \right.\ $$

位置

$$x = f\tan\varphi = f\sin\varphi = f \cdot \frac{1}{a} \cdot \delta = \left\{ \begin{array}{r}
 \pm (2k + 1)\frac{\lambda}{2a}f,\ \ k = 1,2,3,\cdots \\
 \pm 2k\frac{\lambda}{2a}f,\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ k = 1,2,3,\cdots
\end{array} \right.\ $$

### 明纹宽度

![单缝衍射明纹宽度示意图：中心明纹与其它明纹在屏上的线位置](/images/physics/single-slit-width.png)

$$\left\{ \begin{array}{r}
l_{0} = 2f\frac{\lambda}{a}\ (\text{中心明纹}) \\
l = f\frac{\lambda}{a}\ \ \ \ \ \ (\text{其它明纹})
\end{array} \right.\ $$

### 光强

$$\frac{I}{I_{0}} = \frac{A^{2}}{A_{0}^{2}} = \left( \frac{\sin u}{u} \right)^{2}$$

## 圆孔夫琅禾费衍射

![圆孔夫琅禾费衍射示意图：艾里斑与角半径 θ₀](/images/physics/single-slit-intensity.png)

$$\theta_{0} = \delta\theta = 1.22\frac{\lambda}{D}$$

$$R = \frac{1}{\theta_{0}} = \frac{D}{1.22\lambda}$$

## 光栅衍射

光栅常数：d = a + b，其中a透光，b不透光。一般的光栅每毫秒有100 ∼ 1000条（1/d）划线

相邻两个主极大条纹之间有N − 1个暗纹，N − 2个次极大明纹。

![光栅衍射示意图：光栅常数 d = a + b，相邻主极大间有暗纹](/images/physics/circular-aperture.png)![光栅衍射光路示意图：多缝干涉与单缝衍射的共同作用](/images/physics/grating-setup.png)

光栅方程（明纹）

dsin φ = (a + b)sin φ = ±kλ

### 看到的最多级次

取sin φ = 1，得

$$k_{\max} = \frac{a + b}{\lambda}\text{，取整数部分或减一}$$

### 明纹的角位置

$$\varphi_{k} = \arcsin\frac{k\lambda}{a + b}$$

### 明纹的线位置

$$x_{k} = f\tan\varphi_{k} \approx f\sin\varphi_{k} \approx f\frac{\pm k\lambda}{a + b}$$

### 单色平行光斜入射时的光栅方程

![单色平行光斜入射光栅示意图：入射角 θ 与衍射角 φ](/images/physics/grating-oblique.png)

(a + b)(sin θ ± sin φ) = ±kλ

### 光栅的缺级

$$\left\{ \begin{array}{r}
(a + b)\sin\varphi = \pm k\lambda \\
a\sin\varphi = \pm 2k'\frac{\lambda}{2}\ \ \ \ \ \ 
\end{array} \right.\  \Rightarrow k = \frac{a + b}{a}k',\ \ k' = 1,2,3,\cdots$$

### 光栅的分辨本领

$$R = \frac{\lambda}{d\lambda} = kN$$

## 光的偏振

### 自然光

![自然光示意图：光矢量在各方向均匀分布且无固定相位关系](/images/physics/natural-light.png)

### 完全偏振光

![完全偏振光（线偏振光）示意图：光矢量只沿一个方向振动](/images/physics/linear-polarized.png)

### 部分偏振光

![部分偏振光示意图：某一方向的光振动占优势](/images/physics/partial-polarized.png)

### 马吕斯定律

入射光强为I0的线偏振光经过偏振器后的透射光强I满足

$$\frac{I}{I_{0}} = \frac{A^{2}}{A_{0}^{2}} = \frac{A_{0}^{2}\cos^{2}\alpha}{A_{0}^{2}} = \cos^{2}\alpha$$

其中α是入射光光振动方向与偏振器透光方向的夹角。

特别地，对于IS的自然光，有

$$I_{0} = \frac{1}{2}I_{S}$$

![马吕斯定律示意图：线偏振光经偏振器后透射光强随夹角 α 变化](/images/physics/malus-law.png)

### 布鲁斯特定律

![布鲁斯特角示意图：反射光与折射光相互垂直，反射光为完全偏振光](/images/physics/brewster-angle.png)![布鲁斯特角光路示意图（续一）](/images/physics/brewster-2.png)

$$\tan i_{0} = \frac{n_{2}}{n_{1}} = n_{21},\ \ \cos i_{0} = \sin\gamma$$

### 是布鲁斯特角的情况

![布鲁斯特角光路示意图（续二）](/images/physics/brewster-3.png)![布鲁斯特角光路示意图（续四）](/images/physics/brewster-5.png)![布鲁斯特角光路示意图（续五）](/images/physics/brewster-6.png)

### 不是布鲁斯特角的情况

![原文档中的偏振光截图（非必要图，内容为对应章节的公式列表）](/images/physics/polarization-doc.png)![原文档中的偏振光截图（续，非必要图）](/images/physics/polarization-doc-2.png)

## 量子相关概念

$$\overset{\circ}{A} = 10^{- 10}m,\ \ 1eV \approx 1.6 \times 10^{- 19}J$$

$$E = h\nu,\ \ \nu = \frac{E}{h},\ \ p = \frac{h}{\lambda},\ \ \lambda = \frac{h}{p},\ \ p = mv$$

$$E = mc^{2},\ \ m = \frac{m_{0}}{\sqrt{1 - \left( v\text{/}c \right)^{2}}}$$

辐射出射度（辐出度）

物体（在温度为T时）单位时间单位面积辐射的各种波长的电磁波能量的总和。

M,  M(T)

### 单色辐出度

物体单位时间单位面积在λ ∼ λ + dλ范围内辐射的电磁波与dλ之比。辐出度随波长的变化率。
