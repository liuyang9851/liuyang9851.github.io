---
title: "积分表与积分选做"
hs_seq: "Bx"
description: "积分表与积分选做：积分表（必须写：（C为任意常数））"
---

# 积分表与积分选做

积分表（必须写：（C为任意常数））

该表突破常规的以非考试目的堆砌的积分的写法，具有详细的推导过程。

$I_{1} = \int_{}^{}\frac{dx}{a^{2} + x^{2}} = \int_{}^{}{\frac{1}{a^{2}} \cdot \frac{dx}{1 + \left( \frac{x}{a} \right)^{n}}} = \frac{1}{a}\int_{}^{}{\frac{1}{1 + \left( \frac{x}{a} \right)^{2}}d\left( \frac{x}{2} \right)} = \frac{1}{a}\arctan\frac{x}{a} + C$

$I_{n} = \int_{}^{}\frac{dx}{\left( x^{2} + a^{2} \right)^{n}} = \frac{1}{a^{2}}\int_{}^{}{\frac{x^{2} + a^{2} - x^{2}}{\left( x^{2} + a^{2} \right)^{n}}dx} = \frac{1}{a^{2}}\int_{}^{}{\frac{x^{2} + a^{2}}{\left( x^{2} + a^{2} \right)^{n}}dx} + \frac{1}{a^{2}}\int_{}^{}{\frac{- x^{2}}{\left( x^{2} + a^{2} \right)^{n}}dx} = \frac{1}{a^{2}}\int_{}^{}\frac{dx}{\left( x^{2} + a^{2} \right)^{n - 1}} + \frac{1}{2a^{2}(n - 1)}\int_{}^{}{xd\frac{1}{\left( x^{2} + a^{2} \right)^{n - 1}}} = \frac{1}{a^{2}}I_{n - 1} + \frac{1}{2a^{2}(n - 1)} \cdot \frac{x}{\left( x^{2} + a^{2} \right)^{n - 1}} - \frac{1}{2a^{2}(n - 1)}I_{n - 1} = \frac{2n - 3}{2a^{2}(n - 1)}I_{n - 1} + \frac{1}{2a^{2}(n - 1)} \cdot \frac{x}{\left( x^{2} + a^{2} \right)^{n - 1}}$

$\int_{}^{}\frac{dx}{x^{2} - a^{2}} = \frac{1}{2a}\int_{}^{}{\left( \frac{1}{x - a} - \frac{1}{x + a} \right)dx} = \frac{1}{2a}\ln\left| \frac{x - a}{x + a} \right| + C$

$\int_{}^{}\frac{dx}{\sqrt{a^{2} - x^{2}}} = \int_{}^{}{\frac{1}{a} \cdot \frac{dx}{\sqrt{1 - \left( \frac{x}{a} \right)^{2}}}} = \int_{}^{}\frac{d\frac{x}{a}}{\sqrt{1 - \left( \frac{x}{a} \right)^{2}}} = \arcsin\frac{x}{a} + C$

$\int_{}^{}{\sqrt{a^{2} - x^{2}}dx}\overset{x = a\sin t}{\Leftrightarrow}\int_{}^{}{a \cdot \cos tda\sin t} = a^{2}\int_{}^{}{\cos^{2}tdt} = a^{2}\int_{}^{}{\frac{1 + \cos{2t}}{2}dt} = \frac{a^{2}}{4}\int_{}^{}{\left( 1 + \cos{2t} \right)d2t} = \frac{a^{2}}{4}\left( 2t + \sin{2t} \right) + C = \frac{a^{2}}{4}t + \frac{a^{2}}{2}\sin t\cos t + C\underset{\cos t = \frac{\sqrt{a^{2} - x^{2}}}{a}}{\overset{\ \ \ \ \ \ \ \ \sin t = \frac{x}{a}\ \ \ \ \ \ \ }{\Leftrightarrow}}\frac{a^{2}}{2}\arcsin\frac{x}{a} + \frac{1}{2}x\sqrt{a^{2} - x^{2}} + C$

$\int_{}^{}\frac{dx}{\sqrt{x^{2} + a^{2}}}\overset{x = a\tan t}{\Leftrightarrow}\int_{}^{}\frac{da\tan t}{a\sec t} = \int_{}^{}{\sec tdt} = \ln\left| \sec t + \tan t \right| + C\underset{\begin{array}{r} \sin t = \frac{x}{a} \\ \cos t = \frac{\sqrt{a^{2} - x^{2}}}{a} \end{array}}{\overset{\ \ \ \ \ t = \arcsin\frac{x}{a}\ \ \ \ \ }{\Leftrightarrow}}\ln\left( \frac{x}{a} + \frac{\sqrt{x^{2} + a^{2}}}{a} \right) + C = \ln\left( x + \sqrt{x^{2} + a^{2}} \right) + C$

$\int_{}^{}{\sqrt{x^{2} + a^{2}}dx} = x\sqrt{x^{2} + a^{2}} - \int_{}^{}{\frac{x^{2}}{\sqrt{x^{2} + a^{2}}}dx} = x\sqrt{x^{2} + a^{2}} - \int_{}^{}{\frac{x^{2} + a^{2} - a^{2}}{\sqrt{x^{2} + a^{2}}}dx} = x\sqrt{x^{2} + a^{2}} + \int_{}^{}{\frac{a^{2}}{\sqrt{a^{2} + x^{2}}}dx} - \int_{}^{}{\sqrt{x^{2} + a^{2}}dx} \Rightarrow \int_{}^{}{\sqrt{x^{2} + a^{2}}dx} = \frac{1}{2}\left( x\sqrt{x^{2} + a^{2}} + \int_{}^{}{\frac{a^{2}}{\sqrt{x^{2} + a^{2}}}dx} \right) = \frac{1}{2}\left( x\sqrt{x^{2} + a^{2}} + a^{2}\ln\left| x + \sqrt{x^{2} + a^{2}} \right| \right)$

$\int_{}^{}\frac{dx}{\sqrt{x^{2} - a^{2}}}\left\{ \begin{array}{r} x > a\ :\overset{x = a\sec t}{\Leftrightarrow}\int_{}^{}\frac{da\sec t}{a\tan t} = \int_{}^{}{\sec tdt} = \ln\left| \sec t + \tan t \right| + C = \ln\left( \sec t + \tan t \right) + C \\ = \ln\left( \frac{x}{a} + \frac{\sqrt{x^{2} - a^{2}}}{a} \right) + C = \ln\left( x + \sqrt{x^{2} - a^{2}} \right) + C\ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ x < - a\ :\underset{x = - u}{\overset{\ x < - a\ }{\Leftrightarrow}} - \int_{}^{}\frac{du}{\sqrt{u^{2} - a^{2}}} = - \ln\left( u + \sqrt{u^{2} - a^{2}} \right) + C = \ln\frac{1}{- x + \sqrt{x^{2} - a^{2}}} + C\ \ \ \  \\ = \ln\frac{- x - \sqrt{x^{2} - a^{2}}}{a^{2}} = \ln\left( - x - \sqrt{x^{2} - a^{2}} \right)\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \end{array} \right.\$

$\Rightarrow \int_{}^{}\frac{dx}{\sqrt{x^{2} - a^{2}}} = \ln\left| x + \sqrt{x^{2} - a^{2}} \right| + C$

$\int_{}^{}{\sqrt{x^{2} - a^{2}}dx} = x\sqrt{x^{2} - a^{2}} - \int_{}^{}{\frac{x^{2}}{\sqrt{x^{2} - a^{2}}}dx} = x\sqrt{x^{2} - a^{2}} - \int_{}^{}{\frac{x^{2} - a^{2} + a^{2}}{\sqrt{x^{2} - a^{2}}}dx} = x\sqrt{x^{2} + a^{2}} - \int_{}^{}{\frac{a^{2}}{\sqrt{x^{2} - a^{2}}}dx} - \int_{}^{}{\sqrt{x^{2} - a^{2}}dx} \Rightarrow \int_{}^{}{\sqrt{x^{2} - a^{2}}dx} = \frac{1}{2}\left( x\sqrt{x^{2} - a^{2}} - \int_{}^{}{\frac{a^{2}}{\sqrt{x^{2} - a^{2}}}dx} \right) = \frac{1}{2}\left( x\sqrt{x^{2} - a^{2}} - a^{2}\ln\left| x + \sqrt{x^{2} - a^{2}} \right| \right) + C$

$\int_{}^{}{\ln xdx} = x\ln x - \int_{}^{}{xd\ln x} = x\ln x - \int_{}^{}{dx} = x\ln x - x + C$

$\int_{}^{}{\sin xdx} = - \cos x + C$

$\int_{}^{}{\cos xdx} = \sin x + C$

$\int_{}^{}{\tan xdx} = \int_{}^{}{\frac{\sin x}{\cos x}dx} = - \int_{}^{}{\frac{1}{\cos x}d\cos x} = - \ln\left| \cos x \right| + C$

$\int_{}^{}{\cot xdx} = \int_{}^{}{\frac{\cos x}{\sin x}dx} = \int_{}^{}{\frac{1}{\sin x}d\sin x} = \ln\left| \sin x \right| + C$

$\int_{}^{}{\csc xdx} = \int_{}^{}\frac{dx}{\sin x} = \int_{}^{}\frac{dx}{2\sin\frac{x}{2}\cos\frac{x}{2}} = \int_{}^{}\frac{d\frac{x}{2}}{\tan\frac{x}{2} \cdot \cos^{2}\frac{x}{2}} = \int_{}^{}\frac{d\tan\frac{x}{2}}{\tan\frac{x}{2}} = \ln\left| \tan\frac{x}{2} \right| + C$

$= \ln\left| \frac{1 - \cos x}{\sin x} \right| + C = \ln\left| \csc x - \cot x \right| + C$

$\int_{}^{}{\sec xdx} = \int_{}^{}{\csc\left( x + \frac{\pi}{2} \right)d\left( x + \frac{\pi}{2} \right)} = \ln\left| \tan\frac{x + \frac{\pi}{2}}{2} \right| + C = \ln\left| \frac{1 + \tan\frac{x}{2}}{1 - \tan\frac{x}{2}} \right| + C$

$= \ln\left| \csc\left( x + \frac{\pi}{2} \right) - \cot\left( x + \frac{\pi}{2} \right) \right| + C = \ln\left| \sec x + \tan x \right| + C$

$\int_{}^{}{\sin^{2}xdx} = \int_{}^{}{\frac{1 - \cos{2x}}{2}dx} = \frac{1}{2}x - \frac{1}{4}\sin{2x} + C$

$\int_{}^{}{\cos^{2}xdx} = \int_{}^{}{\frac{1 + \cos{2x}}{2}dx} = \frac{1}{2}x + \frac{1}{4}\sin{2x} + C$

$\int_{}^{}{\tan^{2}xdx} = \int_{}^{}{\left( \sec^{2}x - 1 \right)dx} = \tan x - x + C$

$\int_{}^{}{\cot^{2}xdx} = \int_{}^{}{\left( \csc^{2}x - 1 \right)dx} = - \cot x - x + C$

$\int_{}^{}{\sec^{2}xdx} = \tan x + C$

$\int_{}^{}{\csc^{2}xdx} = - \cot x + C$

$\int_{}^{}{\sin^{3}xdx} = \int_{}^{}{\sin^{2}x \cdot \sin xdx} = - \int_{}^{}{\left( 1 - \cos^{2}x \right)d\cos x} = - \cos x + \frac{1}{3}\cos^{3}x + C$

$\int_{}^{}{\cos^{3}xdx} = \int_{}^{}{\cos^{2}x \cdot \cos xdx} = \int_{}^{}{\left( 1 - \sin^{2}x \right)d\sin x} = \sin x - \frac{1}{3}\sin^{3}x + C$

$\int_{}^{}{\tan^{3}xdx} = \int_{}^{}{\left( \sec^{2}x - 1 \right)\tan xdx} = \int_{}^{}{\sec^{2}x\tan xdx} - \int_{}^{}{\tan xdx} = \int_{}^{}{\tan xd\tan x} - \int_{}^{}{\tan xdx} = \frac{1}{2}\tan^{2}x + \ln\left| \cos x \right| + C$

$\int_{}^{}{\cot^{3}xdx} = \int_{}^{}{\left( \csc^{2}x - 1 \right)\cot xdx} = \int_{}^{}{\csc^{2}x\cot xdx} - \int_{}^{}{\cot xdx} = - \int_{}^{}{\cot xd\cot x} - \int_{}^{}{\cot x} = - \frac{1}{2}\cot^{2}x - \ln\left| \sin x \right| + C$

$\int_{}^{}{\sec^{3}xdx} = \int_{}^{}{\sec xd\tan x} = \sec x\tan x - \int_{}^{}{\sec x\tan^{2}xdx} = \sec x\tan x - \int_{}^{}{\sec x\left( \sec^{2}x - 1 \right)dx} = \sec x\tan x - \int_{}^{}{\sec^{3}xdx} + \int_{}^{}{\sec xdx} = \sec x\tan x + \ln\left| \sec x + \tan x \right| - \int_{}^{}{\sec^{3}xdx} \Rightarrow \int_{}^{}{\sec^{3}xdx} = \frac{1}{2}\left( \sec x\tan x + \ln\left| \sec x + \tan x \right| \right) + C$

$\int_{}^{}{\csc^{3}xdx} = - \int_{}^{}{\csc xd\cot x} = - \left( \csc x\cot x + \int_{}^{}{\csc x\cot^{2}xdx} \right) = - \csc x\cot x - \int_{}^{}{\csc x\left( \csc^{2}x - 1 \right)dx} = - \csc x\cot x - \int_{}^{}{\csc^{3}xdx} + \int_{}^{}{\csc xdx} = - \csc x\cot x + \ln\left| \csc x - \cot x \right| - \int_{}^{}{\csc^{3}xdx} \Rightarrow \int_{}^{}{\csc^{3}xdx} = \frac{1}{2}\left( - \csc x\cot x + \ln\left| \csc x - \cot x \right| \right)$

$\int_{}^{}{\sin^{4}xdx} = \int_{}^{}{\left( \sin^{2}x \right)^{2}dx} = \int_{}^{}{\left( \frac{1 - \cos{2x}}{2} \right)^{2}dx} = \int_{}^{}{\frac{1 - 2\cos{2x} + \cos^{2}{2x}}{4}dx} = \frac{1}{4}x - \frac{1}{4}\sin{2x} + \frac{1}{4}\int_{}^{}{\frac{1 + \cos{4x}}{2}dx} = \frac{3}{8}x - \frac{1}{4}\sin{2x} + \frac{1}{32}\sin{4x} + C$

$\int_{}^{}{\cos^{4}xdx} = \int_{}^{}{\left( \cos^{2}x \right)^{2}dx} = \int_{}^{}{\left( \frac{1 + \cos{2x}}{2} \right)^{2}dx} = \int_{}^{}{\frac{1 + 2\cos{2x} + \cos^{2}{2x}}{4}dx} = \frac{1}{4}x + \frac{1}{4}\sin{2x} + \frac{1}{4}\int_{}^{}{\frac{1 + \cos{4x}}{2}dx} = \frac{3}{8}x + \frac{1}{4}\sin{2x} + \frac{1}{32}\sin{4x} + C$

$\int_{}^{}{\tan^{4}xdx} = \int_{}^{}{\tan^{2}x \cdot \tan^{2}xdx} = \int_{}^{}{\tan^{2}x\left( \sec^{2}x - 1 \right)dx} = \int_{}^{}{\tan^{2}x \cdot \sec^{2}xdx} - \int_{}^{}{\tan^{2}xdx} = \int_{}^{}{\tan^{2}xd\tan x} - \int_{}^{}{\left( \sec^{2}x - 1 \right)dx} = \frac{1}{3}\tan^{3}x - \tan x + x + C$

$\int_{}^{}{\cot^{4}xdx} = \int_{}^{}{\cot^{2}x \cdot \cot^{2}xdx} = \int_{}^{}{\cot^{2}x\left( \csc^{2}x - 1 \right)dx} = \int_{}^{}{\cot^{2}x \cdot \csc^{2}xdx} - \int_{}^{}{\cot^{2}xdx} = - \int_{}^{}{\cot^{2}xd\cot x} - \int_{}^{}{\left( \csc^{2}x - 1 \right)dx} = - \frac{1}{3}\cot^{3}x + \cot x + x + C$

$\int_{}^{}{\sec^{4}xdx} = \int_{}^{}{\left( \tan^{2}x + 1 \right)\sec^{2}xdx} = \int_{}^{}{\left( \tan^{2}x + 1 \right)d\tan x} = \frac{1}{3}\tan^{3}x + \tan x + C$

$\int_{}^{}{\csc^{4}xdx} = \int_{}^{}{\left( \cot^{2}x + 1 \right)\csc^{2}xdx} = - \int_{}^{}{\left( \cot^{2}x + 1 \right)d\cot x} = - \frac{1}{3}\cot^{3}x - \cot x + C$

${I_{n} = \int_{}^{}{\sin^{n}xdx} = - \int_{}^{}{\sin^{n - 1}xd\cos x} = - \sin^{n - 1}x\cos x + (n - 1)\int_{}^{}{\sin^{n - 2}x\cos^{2}xdx} }{= - \sin^{n - 1}x\cos x + (n - 1)\int_{}^{}{\sin^{n - 2}x\left( 1 - \sin^{2}x \right)dx} }{= - \sin^{n - 1}x\cos x + (n - 1)\left( I_{n - 2} - I_{n} \right) }{\Leftrightarrow I_{n} = - \frac{1}{n}\sin^{n - 1}x\cos x + \frac{n - 1}{n}I_{n - 2}}$

$I_{n} = \int_{}^{}{\cos^{n}xdx}$

$\int_{}^{}{\arcsin xdx} = x \cdot \arcsin x - \int_{}^{}{xd\arcsin x} = x \cdot \arcsin x - \int_{}^{}{x \cdot \frac{1}{\sqrt{1 - x^{2}}}dx} = x \cdot \arcsin x + \frac{1}{2}\int_{}^{}{\frac{1}{\sqrt{1 - x^{2}}}d\left( 1 - x^{2} \right)} = x \cdot \arcsin x + \sqrt{1 - x^{2}} + C$

$= \int_{}^{}{td\sin t} = t \cdot \sin t - \int_{}^{}{\sin tdt} = t \cdot \sin t + \cos t + C = x \cdot \arcsin x + \sqrt{1 - x^{2}} + C$

$\int_{}^{}{\arccos xdx} = x \cdot \arccos x - \int_{}^{}{xd\arccos x} = x \cdot \arccos x - \int_{}^{}{\frac{x}{\sqrt{1 - x^{2}}}dx} = x \cdot \arccos x - \frac{1}{2}\int_{}^{}{\frac{1}{\sqrt{1 - x^{2}}}d\left( 1 - x^{2} \right)} = x \cdot \arccos x - \sqrt{1 - x^{2}} + C$

$= \int_{}^{}{td\cos t} = t \cdot \cos t - \int_{}^{}{\cos tdt} = t \cdot \cos t - \sin t + C = x \cdot \arccos x - \sqrt{1 - x^{2}} + C$

$\int_{}^{}{\arctan xdx} = x \cdot \arctan x - \int_{}^{}{xd\arctan x} = x \cdot \arctan x - \int_{}^{}{\frac{x}{1 + x^{2}}dx} = x \cdot \arctan x - \frac{1}{2}\int_{}^{}{\frac{1}{1 + x^{2}}d\left( 1 + x^{2} \right)} = x \cdot \arctan x - \frac{1}{2}\ln\left( 1 + x^{2} \right) + C$

$= \int_{}^{}{td\tan t} = t \cdot \tan t - \int_{}^{}{\tan tdt}$

$\int_{}^{}{{arccot}xdx} = x \cdot {arccot}x - \int_{}^{}{xd{arccot}x} = x \cdot {arccot}x + \int_{}^{}{\frac{x}{1 + x^{2}}dx} = x \cdot {arccot}x + \frac{1}{2}\int_{}^{}{\frac{1}{1 + x^{2}}d\left( 1 + x^{2} \right)} = x \cdot {arccot}x + \frac{1}{2}\ln\left( 1 + x^{2} \right) + C$

$\int_{}^{}{{arcsec}xdx} =$

$\int_{}^{}{{arccsc}xdx} =$

$\int_{}^{}\frac{dx}{ax + b} = \frac{1}{a}\ln|ax + b| + C$

$I_{1} = \int_{}^{}\frac{dx}{x^{2} + bx + c} = \int_{}^{}\frac{d\left( x + \frac{b}{2} \right)}{\left( x + \frac{b}{2} \right)^{2} + c - \frac{b^{2}}{4}} = \left\{ \begin{array}{r} \Delta < 0:\  = \frac{1}{\sqrt{c - \frac{b^{2}}{4}}}\arctan\frac{x + \frac{b}{2}}{\sqrt{c - \frac{b^{2}}{4}}} + C\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \Delta = 0:\  = - \frac{1}{x + \frac{b}{2}} + C\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \Delta > 0:\  = \frac{1}{2\sqrt{\frac{b^{2}}{4} - c}}\ln\left| \frac{2x + b - \sqrt{b^{2} - 4c}}{2x + b + \sqrt{b^{2} - 4c}} \right| \end{array} \right.\ \left( \Delta = b^{2} - 4c \right)$

$\int_{}^{}\frac{dx}{ax^{2} + bx + c} = \frac{1}{a}\int_{}^{}\frac{dx}{x^{2} + \frac{b}{a}x + \frac{c}{a}} = \left\{ \begin{array}{r} \Delta < 0:\  = \frac{2}{\sqrt{4ac - b^{2}}}\arctan\frac{2ax + b}{\sqrt{4ac - b^{2}}} + C\ \ \ \ \ \ \ \  \\ \Delta = 0:\  = - \frac{1}{a\left( x - \frac{b}{2a} \right)} + C\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \Delta > 0:\  = \frac{1}{\sqrt{b^{2} - 4ac}}\ln\left| \frac{2ax + b - \sqrt{b^{2} - 4ac}}{2ax + b + \sqrt{b^{2} - 4ac}} \right| \end{array} \right.\ \left( \Delta = b^{2} - 4ac \right)$

$\int_{}^{}{\frac{x}{ax^{2} + bx + c}dx} = \int_{}^{}{\frac{x + p - p}{ax^{2} + bx + c}dx}$

$= \int_{}^{}\frac{d\left( \frac{1}{2}x^{2} + px \right)}{ax^{2} + bx6c} - p\int_{}^{}\frac{dx}{ax^{2} + bx + c}\underset{p = \frac{b}{2a}}{\overset{2ap = b}{=}}\frac{1}{2a}\int_{}^{}\frac{d\left( ax^{2} + bx + c \right)}{ax^{2} + bx + c} - \frac{b}{2a}\int_{}^{}\frac{dx}{ax^{2} + bx + c}$

$= \frac{1}{2a}\ln\left| ax^{2} + bx + c \right| - \frac{b}{2a} \cdot \left\{ \begin{array}{r} \Delta < 0:\ \ \ \frac{2}{\sqrt{4ac - b^{2}}}\arctan\frac{2ax + b}{\sqrt{4ac - b^{2}}} + C\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \Delta = 0:\ \ \  - \frac{1}{a\left( x - \frac{b}{2a} \right)} + C\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \Delta > 0:\ \ \ \frac{1}{\sqrt{b^{2} - 4ac}}\ln\left| \frac{2ax + b - \sqrt{b^{2} - 4ac}}{2ax + b + \sqrt{b^{2} - 4ac}} \right| + C \end{array} \right.\$

$\int_{}^{}\frac{dx}{(x - a)^{n}} = \left\{ \begin{array}{r} \ln|x - a| + C\ \ (n = 1)\ \ \ \ \  \\ - \frac{1}{n - 1} \cdot \frac{1}{(x - a)^{n - 1}} + C \end{array} \right.\$

$I_{n} = \int_{}^{}\frac{dx}{\left( x^{2} + bx + c \right)^{n}} = \int_{}^{}\frac{dx}{\left\lbrack \left( x + \frac{b}{2} \right)^{2} + c - \frac{b^{2}}{4} \right\rbrack^{n}} = \frac{2n - 3}{2\left( c - \frac{b^{2}}{4} \right)(n - 1)}I_{n - 1} + \frac{1}{2\left( c - \frac{b^{2}}{4} \right)(n - 1)} \cdot \frac{x + \frac{b}{2}}{\left\lbrack \left( x + \frac{b}{2} \right)^{2} + c - \frac{b^{2}}{4} \right\rbrack^{n - 1}}$

$\int_{}^{}{\frac{x + e}{\left( x^{2} + bx + c \right)^{n}}dx} = \frac{1}{2}\int_{}^{}{\frac{2x + b}{\left( x^{2} + bx + c \right)^{n}}dx} + \int_{}^{}{\frac{e - \frac{b}{2}}{\left( x^{2} + bx + c \right)^{n}}dx} = \frac{1}{2}\int_{}^{}\frac{d\left( x^{2} + bx + c \right)}{\left( x^{2} + bx + c \right)^{n}} + \left( e - \frac{b}{2} \right)\int_{}^{}{\frac{1}{\left( x^{2} + bx + c \right)^{n}}dx}$

<div class="table-scroll">
<table>
<thead>
<tr>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>

$\int_{}^{}{{sinh}xdx} = \cosh x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\cosh xdx} = \sinh x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}\frac{dx}{\cosh^{2}x} = \tanh x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\frac{1}{\sqrt{1 + x^{2}}}dx} = {arsh}x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\frac{1}{\sqrt{x^{2} - 1}}dx} = {arch}x + C$

</td>
</tr>
<tr>
<td>

$\int_{}^{}{\frac{1}{1 - x^{2}}dx} = {arth}x + C$

</td>
</tr>
</tbody>
</table>
</div>

$= \ \overset{}{=}\underset{}{\overset{}{=}}\$

$\Leftrightarrow \ \ \ \overset{}{\Leftrightarrow}\ \ \ \underset{}{\overset{}{\Leftrightarrow}}$

积分选做

$\int_{}^{}{\frac{1}{1 - \sin x}dx} = \int_{}^{}{\frac{1 + \sin x}{\left( 1 - \sin x \right)\left( 1 + \sin x \right)}dx} = \int_{}^{}{\frac{1 + \sin x}{\cos^{2}x}dx} = \int_{}^{}{\sec^{2}xdx} + \int_{}^{}{\tan x\sec xdx}$

$\int_{}^{}{\frac{1}{1 - \sin x}dx} = \int_{}^{}{\frac{1}{1 - 2\sin\frac{x}{2}\cos\frac{x}{2}}dx} = \int_{}^{}{\frac{1}{\left( \sin\frac{x}{2} - \cos\frac{x}{2} \right)^{2}}dx} = \int_{}^{}{\frac{1}{\mathbf{\cos}^{\mathbf{2}}\frac{\mathbf{x}}{\mathbf{2}}\left( \tan\frac{x}{2} - 1 \right)^{2}}dx} = \int_{}^{}{\frac{1}{\left( \tan\frac{x}{2} - 1 \right)^{2}}d\left( \mathbf{\tan}\mathbf{x}\mathbf{- 1} \right)} = - \frac{2}{\tan\frac{x}{2} - 1} + C$

$\int_{}^{}{\left( \mathbf{x}^{\mathbf{3}}\mathbf{+ x} \right)e^{- x^{2}}dx} = - \frac{1}{2}\int_{}^{}{\left( \mathbf{x}^{\mathbf{2}}\mathbf{+ 1} \right)d\mathbf{e}^{\mathbf{-}\mathbf{x}^{\mathbf{2}}}} = - \frac{1}{2}\left\lbrack \left( x^{2} + 1 \right)e^{- x^{2}} - \int_{}^{}e^{- x^{2}}d\left( x^{2} + 1 \right) \right\rbrack$

$\int_{}^{}{\ln\left( 1 + \sqrt{x} \right)dx}\overset{\sqrt{x} = t}{\Leftrightarrow}\int_{}^{}{\ln{(1 + t)dt^{2}}} = \cdots = t^{2}\ln(1 + t) - \int_{}^{}{\frac{\mathbf{t}^{\mathbf{2}}}{\mathbf{1 + t}}\mathbf{d}\mathbf{t}} = t^{2}\ln(1 + t) - \int_{}^{}{\frac{\left( \mathbf{t}^{\mathbf{2}}\mathbf{- 1} \right)\mathbf{+ 1}}{\mathbf{1 + t}}\mathbf{d}\mathbf{t}} = t^{2}\ln(1 + t) - \int_{}^{}{\left( \mathbf{t - 1} \right)dt} - \int_{}^{}{\frac{1}{1 + t}dt}$

$\int_{}^{}{\ln\left( x + \sqrt{x^{2} + 4} \right)dx} = x\ln\left( x + \sqrt{x^{2} + 4} \right) - \int_{}^{}{x\mathbf{d}\mathbf{\ln}\left( \mathbf{x +}\sqrt{\mathbf{x}^{\mathbf{2}}\mathbf{+ 4}} \right)} = x\ln\left( x + \sqrt{x^{2} + 4} \right) - \int_{}^{}{x \cdot \frac{1}{\sqrt{x^{2} + 4}\ }dx}$

$\int_{}^{}{\frac{x^{3}}{\sqrt{1 + x^{2}}}dx} = \left\{ \begin{array}{r} \int_{}^{}{x^{2}d\sqrt{1 + x^{2}}} = x^{2}\sqrt{1 + x^{2}} - \int_{}^{}{\sqrt{\mathbf{1 +}\mathbf{x}^{\mathbf{2}}}\mathbf{d}\mathbf{x}^{\mathbf{2}}} = x^{2}\sqrt{1 + x^{2}} - \int_{}^{}{\sqrt{\mathbf{1 +}\mathbf{x}^{\mathbf{2}}}\mathbf{d}\left( \mathbf{1 + x}^{\mathbf{2}} \right)}\mathbf{\ \ \ \ \ \ \ \ \ } \\ \overset{t = \sqrt{1 + x^{2}}\mathbf{,}\mathbf{x}^{\mathbf{2}}\mathbf{=}\mathbf{t}^{\mathbf{2}}\mathbf{- 1,2}\mathbf{x}\mathbf{d}\mathbf{x = 2}\mathbf{t}\mathbf{d}\mathbf{t}}{\Leftrightarrow}\int_{}^{}{\frac{t^{2} - 1}{t} \cdot tdt}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \frac{1}{2}\int_{}^{}{\frac{x^{2}}{\sqrt{1 + x^{2}}}dx^{2}}\overset{x^{2} = t}{\Leftrightarrow}\frac{1}{2}\int_{}^{}{\frac{\mathbf{t}}{\sqrt{\mathbf{1 + t}}}\mathbf{d}\mathbf{t}} = \frac{1}{2}\int_{}^{}{\frac{\left( \mathbf{t + 1} \right)\mathbf{- 1}}{\sqrt{1 + t}}dt} = \frac{1}{2}\int_{}^{}{\sqrt{\mathbf{1 + t}}\mathbf{d}\mathbf{t}} - \frac{1}{2}\int_{}^{}{\frac{1}{\sqrt{1 + t}}dt} \end{array} \right.\$

$\int_{}^{}{\frac{1}{x\left( x^{7} + 2 \right)}dx} = \left\{ \begin{array}{r} \overset{x = \frac{1}{t}}{\Leftrightarrow} - \int_{}^{}{\frac{t^{6}}{1 + 2t^{7}}dt}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \frac{1}{2}\int_{}^{}{\frac{\left( \mathbf{x}^{\mathbf{7}}\mathbf{+ 2} \right)\mathbf{-}\mathbf{x}^{\mathbf{7}}}{x\left( x^{7} + 2 \right)}dx} = \frac{1}{2}\int_{}^{}{\left\lbrack \frac{1}{x} - \frac{\mathbf{x}^{\mathbf{7}}}{\mathbf{x}\left( x^{7} + 2 \right)} \right\rbrack dx} = \frac{1}{2}\int_{}^{}{\frac{1}{x}dx} - \frac{1}{2}\int_{}^{}{\frac{\mathbf{x}^{\mathbf{6}}}{\mathbf{x}^{\mathbf{7}}\mathbf{+ 2}}dx} \\ \int_{}^{}{\frac{\mathbf{x}^{\mathbf{6}}}{\mathbf{x}^{\mathbf{7}}\left( x^{7} + 2 \right)}dx} = \frac{1}{7}\int_{}^{}{\frac{1}{x^{7}\left( x^{7} + 2 \right)}\mathbf{d}\mathbf{x}^{\mathbf{7}}}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  \\ \int_{}^{}{\frac{1}{\mathbf{x}^{\mathbf{8}}\left( \mathbf{1 + 2}\mathbf{x}^{\mathbf{- 7}} \right)}dx} = \int_{}^{}{\frac{1}{\left( 1 + 2x^{- 7} \right)} \cdot \mathbf{x}^{\mathbf{- 8}}dx} = - \frac{1}{14}\int_{}^{}{\frac{1}{1 + 2x^{- 7}}d\left( 1 + \mathbf{2}\mathbf{x}^{\mathbf{- 7}} \right)} \end{array} \right.\$

原函数不是初等函数的积分

$\int_{}^{}{e^{ax^{2}}dx}\ \ \ \ \int_{}^{}{x^{2n}e^{ax^{2}}dx}\ \ (a \neq ,n\mathbb{\in N)}$

$\int_{}^{}{\frac{\sin x}{x^{n}}dx}\int_{}^{}{\frac{\cos x}{x^{n}}dx}\int_{}^{}{\frac{\tan x}{x^{n}}dx}\ \ (n\mathbb{\in N)}$

$\int_{}^{}{\sin x^{2}dx}\int_{}^{}{\cos x^{2}dx}\int_{}^{}{\tan x^{2}dx}$

$\int_{}^{}{\frac{e^{x}}{x}dx}\ \ \int_{}^{}{\frac{e^{- x}}{x}dx}\ \ \int_{}^{}{\frac{e^{x}}{1 + x}dx}\ \ \int_{}^{}{\frac{e^{x}}{1 + x^{2}}dx}\ \ \int_{}^{}{\frac{e^{x}}{x(1 + x)}dx}$

$\int_{}^{}\frac{dx}{\ln x}$

$\int_{}^{}{\sqrt{1 + x^{3}}dx}$

$\int_{}^{}{\sqrt{1 - k^{2}\sin^{2}x}dx}\ \ \left( 0 < k^{2} < 1 \right)$

$\int_{}^{}{}$
