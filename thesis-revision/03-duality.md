# 第3章 幂型复合条件下的对偶表示

## 3.1 向量值 Orlicz 表示

记

\[
\mathcal X_\Phi=L^\Phi(\Omega;\ell_2),\qquad
\|\theta\|_{\mathcal X_\Phi}
=\left\|\left(\sum_n|\theta_n|^2\right)^{1/2}\right\|_\Phi.
\]

### 定理3.1

设 \((\Phi,\Psi)\) 为共轭 Young 函数，且 \((D_\Phi)\) 成立。则每个 \(L\in(\mathcal X_\Phi)^*\) 都存在唯一的 \(\eta\in\mathcal X_\Psi\)，使

\[
L(\theta)=E\sum_{n\ge1}\theta_n\eta_n,
\]

且

\[
\|\eta\|_{\mathcal X_\Psi}\le C\|L\|.
\]

上述级数绝对收敛。

#### 证明

先在每个单坐标上应用标量 Orlicz 对偶，得到 \(\eta_n\in L^\Psi\)。对

\[
G_N=\left(\sum_{n=1}^N|\eta_n|^2\right)^{1/2}
\]

及任意非负 \(Z\) 满足 \(E\Phi(Z)\le1\)，取

\[
\theta_n=Z\eta_nG_N^{-1}\mathbf1_{\{G_N>0\}},\qquad n\le N.
\]

则 \(\|\theta\|_{\mathcal X_\Phi}\le1\)，故 \(E(ZG_N)\le\|L\|\)。由 associate 范数表示和 Fatou 性质，

\[
\left\|\left(\sum_n|\eta_n|^2\right)^{1/2}\right\|_\Psi\le C\|L\|.
\]

\((D_\Phi)\) 保证有限支撑序列在 \(\mathcal X_\Phi\) 中稠密，因此表示延拓到所有 \(\theta\)。最后，

\[
E\sum_n|\theta_n\eta_n|
\le E\!\left[
\left(\sum_n|\theta_n|^2\right)^{1/2}
\left(\sum_n|\eta_n|^2\right)^{1/2}
\right]<\infty.
\]

唯一性由单坐标有界测试得到。证毕。

## 3.2 适应序列投影

在有限支撑序列上定义

\[
(P\theta)_n=E_n\theta_n,\qquad
(P^-\theta)_n=E_{n-1}\theta_n,\qquad
Q=P-P^-.
\]

在 \((P_{\Phi,r})+(C_\Phi)\) 下，条件 Jensen 不等式给出

\[
\|P\theta\|_{\mathcal X_\Phi}
+\|P^-\theta\|_{\mathcal X_\Phi}
\le C\|\theta\|_{\mathcal X_\Phi}.
\]

故三者延拓为有界算子，且

\[
\operatorname{Ran}P=\mathcal A_S^\Phi,\qquad
\operatorname{Ran}Q=\mathcal D_S^\Phi.
\]

相对于向量值 Orlicz 配对，

\[
(P^*\eta)_n=E_n\eta_n,\qquad
((P^-)^*\eta)_n=E_{n-1}\eta_n,
\]

\[
(Q^*\eta)_n=E_n\eta_n-E_{n-1}\eta_n.
\]

这一步由原空间上投影有界性推出对偶侧有界性，不预先假设待证代表序列属于 \(L^\Psi(\ell_2)\)，因而不存在循环论证。

### 引理3.2

在 \((D_\Phi)+(P_{\Phi,r})+(C_\Phi)\) 下，每个 \(\Lambda\in(\mathcal A_S^\Phi)^*\) 存在唯一的适应序列 \(\sigma\in\mathcal A_S^\Psi\)，使

\[
\Lambda(\theta)=E\sum_n\theta_n\sigma_n,
\qquad
\|\sigma\|_{\mathcal X_\Psi}\le C\|\Lambda\|.
\]

此外

\[
\left\|
\left(\sum_n|E_{n-1}\sigma_n|^2\right)^{1/2}
\right\|_\Psi\le C\|\Lambda\|.
\]

#### 证明

由 Hahn–Banach 把 \(\Lambda\) 延拓到 \(\mathcal X_\Phi\)，再由定理3.1得到 \(\eta\in\mathcal X_\Psi\)。令 \(\sigma=P^*\eta\)。对适应 \(\theta\)，

\[
\Lambda(\theta)=\langle P\theta,\eta\rangle
=\langle\theta,P^*\eta\rangle.
\]

第一项估计来自 \(P^*\) 有界性；又

\[
E_{n-1}\sigma_n=E_{n-1}\eta_n,
\]

第二项估计来自 \((P^-)^*\) 有界性。绝对收敛由 Orlicz–Hölder 得到。证毕。

## 3.3 普通平方函数型对偶

### 定理3.3

设 \((D_\Phi)+(P_{\Phi,r})+(C_\Phi)\) 成立，则

\[
(H_S^\Phi)^*\simeq H_S^\Psi.
\]

更准确地，对 \(X\in H_S^\Phi\)、\(Y\in H_S^\Psi\)，

\[
\langle X,Y\rangle
=\sum_{n\ge1}E(dX_n\,dY_n)
=\lim_{N\to\infty}E(X_NY_N)
\]

绝对收敛，且

\[
|\langle X,Y\rangle|
\le2\|X\|_{H_S^\Phi}\|Y\|_{H_S^\Psi}.
\]

反之，每个 \(F\in(H_S^\Phi)^*\) 存在唯一 \(Y\in H_S^\Psi\) 表示，且

\[
\|Y\|_{H_S^\Psi}\le C\|F\|.
\]

#### 证明

逐点 Cauchy–Schwarz 给出

\[
\sum_n|dX_n\,dY_n|\le S(X)S(Y),
\]

故配对绝对收敛。鞅差正交性说明第 \(N\) 个部分和等于 \(E(X_NY_N)\)。

对 \(F\)，把 \(H_S^\Phi\) 等距识别为 \(\mathcal D_S^\Phi\)，再延拓到 \(\mathcal A_S^\Phi\)。由引理3.2得到适应 \(\sigma\)，定义

\[
dY_n=\sigma_n-E_{n-1}\sigma_n.
\]

则

\[
S(Y)\le
\left(\sum_n|\sigma_n|^2\right)^{1/2}
+
\left(\sum_n|E_{n-1}\sigma_n|^2\right)^{1/2},
\]

故 \(Y\in H_S^\Psi\)。又因 \(E_{n-1}dX_n=0\)，

\[
F(X)=\sum_nE(dX_n\sigma_n)
=\sum_nE(dX_n\,dY_n).
\]

若 \(Y,Z\) 表示同一泛函，令 \(W=Y-Z\)。固定 \(m\) 和 \(A\in\mathcal F_m\)，取单层差

\[
dX_m=\mathbf1_A-E_{m-1}\mathbf1_A.
\]

则 \(E(\mathbf1_A dW_m)=0\) 对所有 \(A\in\mathcal F_m\) 成立，故 \(dW_m=0\)。由 \(m\) 任意且二者从零出发，得到 \(Y=Z\)。证毕。

## 3.4 条件平方函数型对偶

设

\[
A_\Phi(u)=\Phi(\sqrt u).
\]

由 Luxemburg 范数定义，

\[
\|U^2\|_{A_\Phi}=\|U\|_\Phi^2.
\]

### 引理3.4

设 \((D_\Phi)+(P_{\Phi,r})+(C_\Phi)\) 成立。若 \(\Lambda\in(\mathcal D_s^\Phi)^*\)，则存在唯一 \(\sigma\in\mathcal D_s^\Psi\)，使

\[
\Lambda(\theta)=\sum_nE(\theta_n\sigma_n),
\qquad
\|s(\sigma)\|_\Psi\le C\|\Lambda\|.
\]

#### 证明

固定 \(n\)，先只取

\[
X\in L^\infty(\mathcal F_n),\qquad E_{n-1}X=0.
\]

由条件 Jensen，

\[
\|(E_{n-1}|X|^2)^{1/2}\|_\Phi\le\|X\|_\Phi.
\]

故单坐标泛函关于 \(L^\Phi\) 范数有界。Hahn–Banach 和标量 Orlicz 对偶给出 \(\widetilde\sigma_n\in L^\Psi(\mathcal F_n)\)。令

\[
\sigma_n=\widetilde\sigma_n-E_{n-1}\widetilde\sigma_n.
\]

于是有限有界中心化差列具有所需表示。

下面估计 \(s(\sigma)\)。固定 \(N,M\)，令

\[
\eta_n^{(M)}=\sigma_n\mathbf1_{\{|\sigma_n|\le M\}},\quad
a_n^{(M)}=E_{n-1}|\eta_n^{(M)}|^2,\quad
G_{N,M}=\left(\sum_{n=1}^Na_n^{(M)}\right)^{1/2}.
\]

对 \(Z\ge0\)、\(E\Phi(Z)\le1\)，置

\[
H_l=\min\{Z/G_{N,M},l\}\mathbf1_{\{G_{N,M}>0\}},\qquad
H_{n,l}=E_{n-1}H_l,
\]

\[
\theta_n^{(M,l)}
=H_{n,l}\big(\eta_n^{(M)}-E_{n-1}\eta_n^{(M)}\big).
\]

该序列有界、有限支撑且中心化。直接计算得

\[
\Lambda(\theta^{(M,l)})=E(H_lG_{N,M}^2).
\]

又由条件方差估计和 \((C_\Phi)\)，

\[
\|s(\theta^{(M,l)})\|_\Phi\le C.
\]

令 \(l\to\infty\)，得到

\[
E(ZG_{N,M})\le C\|\Lambda\|.
\]

取 associate 范数上确界，再依次令 \(M,N\to\infty\)，由 Fatou 性质得到

\[
\|s(\sigma)\|_\Psi\le C\|\Lambda\|.
\]

最后，对一般 \(\theta\)，采用中心化截断

\[
\theta_{n,k}
=\theta_n\mathbf1_{\{|\theta_n|\le k\}}
-E_{n-1}\big(\theta_n\mathbf1_{\{|\theta_n|\le k\}}\big),
\]

先令 \(k\to\infty\)，再令时间截断 \(N\to\infty\)。\((D_\Phi)\) 保证上述逼近在 \(\mathcal D_s^\Phi\) 范数中收敛。条件 Cauchy–Schwarz和 Orlicz–Hölder给出表示级数绝对收敛。唯一性由单层有界中心化测试得到。证毕。

### 定理3.5

在引理3.4的假设下，

\[
(H_s^\Phi)^*\simeq H_s^\Psi.
\]

#### 证明

对 \(X\in H_s^\Phi\)、\(Y\in H_s^\Psi\)，

\[
\sum_nE|dX_n\,dY_n|
\le E[s(X)s(Y)]
\le2\|X\|_{H_s^\Phi}\|Y\|_{H_s^\Psi}.
\]

故配对绝对收敛。反方向把泛函转到 \(\mathcal D_s^\Phi\)，应用引理3.4，并令 \(dY_n=\sigma_n\)。范数控制和唯一性随即得到。证毕。

## 3.5 \(\widetilde K^\Psi\) 代表

### 定理3.6

设 \((D_\Phi)+(G_\Psi)\) 成立。则每个 \(F\in(H_S^\Phi)^*\) 存在唯一的 \(Y\in\widetilde K^\Psi\)，使

\[
F(X)=\lim_{N\to\infty}E(X_NY_N),
\qquad
\|Y\|_{\widetilde K^\Psi}\le C\|F\|.
\]

#### 证明

把 \(F\) 经鞅差嵌入延拓到 \(\mathcal X_\Phi\)。由定理3.1得到

\[
\sigma\in\mathcal X_\Psi,\qquad
F(X)=E\sum_ndX_n\sigma_n.
\]

定义

\[
dY_n=E_n\sigma_n-E_{n-1}\sigma_n.
\]

\((G_\Psi)\) 给出 \(L^2\) 终端值 \(Y\) 及控制函数 \(\gamma\)，故 \(Y\in\widetilde K^\Psi\)。对有限鞅，

\[
E(dX_n\sigma_n)=E(dX_n\,dY_n),
\]

从而 \(F(X)=E(X_NY_N)\)。\((D_\Phi)\) 保证停止鞅 \(X^{[N]}\to X\) 于 \(H_S^\Phi\)，故表示延拓到一般 \(X\)。

唯一性独立地重复单层有界鞅差测试：若两个终端代表给出同一泛函，则其每一层鞅差与所有有界中心化 \(\mathcal F_m\)-可测随机变量的配对均为零，从而逐层相等。证毕。

若进一步有 \((D_\Psi)\)，令

\[
g_N=\left(\sum_{n>N}|\sigma_n|^2\right)^{1/2}.
\]

则 \(\|g_N\|_\Psi\to0\)。对尾序列重新应用 \((G_\Psi)\)，得到

\[
\|Y-Y_N\|_{\widetilde K^\Psi}\le C\|g_N\|_\Psi\to0.
\]

没有 \((D_\Psi)\) 时不能保留这一拟范数收敛结论。

## 3.6 从 \(\widetilde K^\Psi\) 到 \(K^\Psi\)

### 定理3.7

设 \((P_{\Psi,s})+(M_{\Psi_1})\) 成立，则

\[
\widetilde K^\Psi\hookrightarrow K^\Psi,\qquad
\|Y\|_{K^\Psi}\le C\|Y\|_{\widetilde K^\Psi}.
\]

#### 证明

取 \(\gamma\in\widetilde\Gamma_\Psi(Y)\)。由条件矩单调性，

\[
E_n|Y-Y_{n-1}|
\le(E_n\gamma^2)^{1/2}
\le(E_n|\gamma|^s)^{1/s}.
\]

令

\[
M^*=\sup_mE_m|\gamma|^s,\qquad \eta=(M^*)^{1/s}.
\]

记 \(A_n=(E_n|\gamma|^s)^{1/s}\)。因 \(A_n\le\eta\) 且 \(A_n\) 为 \(\mathcal F_n\)-可测，

\[
A_n=E_nA_n\le E_n\eta.
\]

故 \(\eta\in\Gamma_\Psi(Y)\)。又

\[
\|\eta\|_\Psi^s
=\|M^*\|_{\Psi_1}
\le C\||\gamma|^s\|_{\Psi_1}
=C\|\gamma\|_\Psi^s.
\]

取下确界即得结论。证毕。

当 \(\Psi_1(u)=u\) 时，该证明需要 \(L^1\) Doob 强型不等式，一般不成立；此端点必须另行处理。

## 3.7 \(K^\Psi\) 型对偶

### 定理3.8

设

\[
(D_\Phi)+(G_\Psi)+(P_{\Psi,s})+(M_{\Psi_1})+(FG_\Phi)
\]

成立，则

\[
(H_S^\Phi)^*\simeq K^\Psi.
\]

#### 证明

由定理3.6和3.7，每个泛函有唯一 \(K^\Psi\) 代表，且代表范数受泛函范数控制。

反之，对 \(Y\in K^\Psi\)，先在有限鞅上定义

\[
F_Y(X)=E(X_NY_N).
\]

\((FG_\Phi)\) 给出一致有界性；\((D_\Phi)\) 给出有限鞅稠密性，因此 \(F_Y\) 唯一延拓到 \(H_S^\Phi\)，且

\[
F_Y(X)=\lim_NE(X_NY_N),\qquad
\|F_Y\|\le C\|Y\|_{K^\Psi}.
\]

单层测试保证代表元唯一。证毕。

## 3.8 \(H_S^\Psi\) 与 \(K^\Psi\) 的包含关系

### 定理3.9

若定理3.3及 \((FG_\Phi)\) 成立，则

\[
K^\Psi\hookrightarrow H_S^\Psi.
\]

事实上，\(Y\in K^\Psi\) 先定义 \(H_S^\Phi\) 上的泛函；定理3.3给出 \(Z\in H_S^\Psi\) 表示同一泛函；唯一性推出 \(Y\) 的正则鞅与 \(Z\) 相同。

### 定理3.10

若定理3.8成立，则

\[
H_S^\Psi\hookrightarrow K^\Psi.
\]

事实上，\(Y\in H_S^\Psi\) 通过绝对收敛平方函数配对定义 \(H_S^\Phi\) 上的泛函；定理3.8给出 \(K^\Psi\) 代表；唯一性推出二者相同。

只有两组条件同时成立时，才能写

\[
H_S^\Psi=K^\Psi
\]

并得到范数等价。

## 3.9 本章小结

本章建立了两条分层证明链：

\[
(D_\Phi)+(P_{\Phi,r})+(C_\Phi)
\Longrightarrow
(H_S^\Phi)^*\simeq H_S^\Psi,\quad
(H_s^\Phi)^*\simeq H_s^\Psi,
\]

以及

\[
F\longmapsto\sigma
\xrightarrow{(G_\Psi)}
Y\in\widetilde K^\Psi
\xrightarrow{(P_{\Psi,s})+(M_{\Psi_1})}
Y\in K^\Psi.
\]

完整 \(K^\Psi\) 对偶还需要 \((FG_\Phi)\)。这些外部假设的原始版本尚须逐项核对，故不能把最终等式写成一般 Young 函数下的无条件结论。
