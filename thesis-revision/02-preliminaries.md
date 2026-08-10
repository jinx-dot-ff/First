# 第2章 基本记号与预备知识

## 2.1 概率空间、过滤与鞅

固定概率空间 \((\Omega,\mathcal F,\mathbb P)\) 和过滤

\[
\mathcal F_0\subseteq\mathcal F_1\subseteq\cdots,\qquad
\mathcal F=\sigma\!\left(\bigcup_{n\ge0}\mathcal F_n\right).
\]

记 \(E_nZ=E(Z\mid\mathcal F_n)\)。所有鞅均满足 \(X_0=0\)。其鞅差为

\[
dX_n=X_n-X_{n-1},\qquad E_{n-1}dX_n=0.
\]

平方函数和条件平方函数分别为

\[
S(X)=\left(\sum_{n\ge1}|dX_n|^2\right)^{1/2},
\qquad
s(X)=\left(\sum_{n\ge1}E_{n-1}|dX_n|^2\right)^{1/2}.
\]

## 2.2 Young 函数及其共轭

函数 \(\Phi:[0,\infty)\to[0,\infty)\) 称为 Young 函数，如果它凸、左连续、非减，满足 \(\Phi(0)=0\)，且 \(\Phi(t)\to\infty\) 当 \(t\to\infty\)。本文主要定理默认 \(\Phi\) 有限值且在 \((0,\infty)\) 上为正。

\(\Phi\) 的 Young–Fenchel 共轭定义为

\[
\Psi(y)=\sup_{x\ge0}\{xy-\Phi(x)\}.
\]

于是

\[
xy\le\Phi(x)+\Psi(y),\qquad x,y\ge0.
\]

## 2.3 Orlicz 空间及两种范数

定义 Orlicz 模

\[
\rho_\Phi(Z)=E\Phi(|Z|),
\]

以及

\[
L^\Phi=\{Z:\rho_\Phi(Z/\lambda)<\infty\text{ 对某个 }\lambda>0\}.
\]

Luxemburg 范数为

\[
\|Z\|_{\Phi,L}
=\inf\{\lambda>0:\rho_\Phi(Z/\lambda)\le1\}.
\]

associate 范数为

\[
\|Z\|_{\Phi,O}
=\sup_{\rho_\Psi(W)\le1}E|ZW|.
\]

二者满足

\[
\|Z\|_{\Phi,L}\le\|Z\|_{\Phi,O}\le2\|Z\|_{\Phi,L},
\]

并有 Orlicz–Hölder 不等式

\[
E|ZW|\le2\|Z\|_{\Phi,L}\|W\|_{\Psi,L}.
\]

后文若无特别说明，\(\|\cdot\|_\Phi\) 表示 Luxemburg 范数。

若 \(\Phi\) 满足全局 \(\Delta_2\) 条件

\[
\Phi(2t)\le C_\Phi\Phi(t),
\]

则在本文采用的有限概率空间设置中，\(L^\Phi\) 的范数具有序连续性；有限支撑向量值函数稠密；连续对偶不含奇异泛函部分。本文用 \((D_\Phi)\) 表示这一条件，用 \((D_\Psi)\) 表示 \(\Psi\) 的对应条件。

## 2.4 Hardy–Orlicz 鞅空间

定义

\[
H_S^\Phi=\{X:X_0=0,\ X\text{ 为鞅},\ S(X)\in L^\Phi\},
\qquad
\|X\|_{H_S^\Phi}=\|S(X)\|_\Phi,
\]

以及

\[
H_s^\Phi=\{X:X_0=0,\ X\text{ 为鞅},\ s(X)\in L^\Phi\},
\qquad
\|X\|_{H_s^\Phi}=\|s(X)\|_\Phi.
\]

除非另有比较定理，不把两者视为同一空间。

## 2.5 适应序列与鞅差序列空间

令

\[
\mathcal X_\Phi=L^\Phi(\Omega;\ell_2)
=\left\{\theta:
\left(\sum_n|\theta_n|^2\right)^{1/2}\in L^\Phi\right\}.
\]

其适应子空间为

\[
\mathcal A_S^\Phi
=\{\theta\in\mathcal X_\Phi:\theta_n\text{ 为 }\mathcal F_n\text{-可测}\},
\]

鞅差子空间为

\[
\mathcal D_S^\Phi
=\{\theta\in\mathcal A_S^\Phi:E_{n-1}\theta_n=0,\ n\ge1\}.
\]

映射 \(X\mapsto(dX_n)\) 给出

\[
H_S^\Phi\cong\mathcal D_S^\Phi.
\]

条件平方函数型鞅差空间定义为

\[
\mathcal D_s^\Phi
=\left\{\theta:
\theta_n\in L^1(\mathcal F_n),\
E_{n-1}\theta_n=0,\
\left(\sum_nE_{n-1}|\theta_n|^2\right)^{1/2}\in L^\Phi
\right\},
\]

范数为

\[
\|\theta\|_{\mathcal D_s^\Phi}
=\left\|
\left(\sum_nE_{n-1}|\theta_n|^2\right)^{1/2}
\right\|_\Phi.
\]

同样有 \(H_s^\Phi\cong\mathcal D_s^\Phi\)。

## 2.6 \(K^\Psi\) 与 \(\widetilde K^\Psi\)

为保证正定性，所有终端代表元均归一化为 \(E_0Y=0\)，并令 \(Y_n=E_nY\)。

对 \(Y\in L^1\) 且 \(E_0Y=0\)，定义

\[
\Gamma_\Psi(Y)=
\left\{\gamma\in L^\Psi_+:
E_n|Y-Y_{n-1}|\le E_n\gamma,\ n\ge1
\right\}.
\]

令

\[
K^\Psi=\{Y:\Gamma_\Psi(Y)\ne\varnothing\},\qquad
\|Y\|_{K^\Psi}=\inf_{\gamma\in\Gamma_\Psi(Y)}\|\gamma\|_\Psi.
\]

对 \(Y\in L^2\) 且 \(E_0Y=0\)，定义

\[
\widetilde\Gamma_\Psi(Y)=
\left\{\gamma\in L^\Psi_+\cap L^2:
E_n|Y-Y_{n-1}|^2\le E_n(\gamma^2),\ n\ge1
\right\},
\]

以及

\[
\widetilde K^\Psi
=\{Y:\widetilde\Gamma_\Psi(Y)\ne\varnothing\},\qquad
\|Y\|_{\widetilde K^\Psi}
=\inf_{\gamma\in\widetilde\Gamma_\Psi(Y)}\|\gamma\|_\Psi.
\]

在未证明等价范数前，后一量称为拟范数。全文固定使用上述二阶定义，不与

\[
\big(E_n|Y-Y_n|^2\big)^{1/2}\le E_n\gamma
\]

混用。

## 2.7 结构假设与辅助不等式

### 2.7.1 幂型复合条件

\[
(P_{\Phi,r}):\qquad
\Phi(t)=\Phi_1(t^r),\quad r\ge2,
\]

其中 \(\Phi_1\) 为满足 \(\Delta_2\) 的 Young 函数。

定义

\[
A_\Phi(u)=\Phi(\sqrt u)=\Phi_1(u^{r/2}).
\]

另设

\[
(P_{\Psi,s}):\qquad
\Psi(t)=\Psi_1(t^s),\quad s\ge2.
\]

其中 \(\Psi_1\) 为 Young 函数。\((P_{\Phi,r})\) 与 \((P_{\Psi,s})\) 分别用于两条替代性路线，不默认对同一对共轭函数同时成立。

### 2.7.2 条件期望凸性假设

在 \((P_{\Phi,r})\) 下，\(A_\Phi\) 是 Young 函数。进一步假设 \((C_\Phi)\)：对所有有限非负序列 \((Z_n)\)，存在 \(C_A\) 使

\[
\left\|\sum_nE_nZ_n\right\|_{A_\Phi}
\le C_A\left\|\sum_nZ_n\right\|_{A_\Phi},
\]

且把 \(E_n\) 换为 \(E_{n-1}\) 后同样成立。

由

\[
\|W^2\|_{A_\Phi}=\|W\|_\Phi^2
\]

可推出坐标条件期望在 \(L^\Phi(\ell_2)\) 上有界。该不等式对应 Mogyoródi 型凸性结果[10-12]；最终稿须核对原始定理编号和完整条件。

### 2.7.3 极大及尾量假设

\((M_{\Psi_1})\) 表示

\[
\left\|\sup_nE_nZ\right\|_{\Psi_1}
\le C_{\Psi_1}\|Z\|_{\Psi_1}.
\]

二者是不同假设。

\((G_\Psi)\) 表示：若

\[
g=\left(\sum_n|\sigma_n|^2\right)^{1/2}\in L^\Psi,\qquad
dY_n=E_n\sigma_n-E_{n-1}\sigma_n,
\]

则 \(Y_n=\sum_{k\le n}dY_k\) 有 \(L^2\) 终端值 \(Y\)，且存在 \(\gamma\in L^\Psi_+\cap L^2\) 满足

\[
E_n|Y-Y_{n-1}|^2\le E_n(\gamma^2),\qquad
\|\gamma\|_\Psi\le C_G\|g\|_\Psi.
\]

\((FG_\Phi)\) 表示对有限鞅 \(X\) 和 \(Y\in K^\Psi\)，

\[
|E(X_NY_N)|
\le C_{FG}\|X\|_{H_S^\Phi}\|Y\|_{K^\Psi}.
\]

\((G_\Psi)\)、\((M_{\Psi_1})\) 和 \((FG_\Phi)\) 分别对应 Garsia 型尾量理论、Orlicz 极大不等式及 Fefferman–Garsia 型配对[4,12,13,17]，但仍须按原始文献核查具体版本。

## 2.8 本章小结

本章固定了两类 Hardy–Orlicz 空间、两类序列空间、两种 Orlicz 范数和两个条件尾量空间。后文每个定理将直接列明使用哪些假设；有限幂、\(\Delta_2\)、凸性不等式和极大不等式不再混写。
