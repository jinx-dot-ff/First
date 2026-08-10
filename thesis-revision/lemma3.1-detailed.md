# 引理3.1　幂型复合条件下适应序列空间上泛函的表示

本节沿用二次复合情形原论文中引理3.1的证明逻辑，将

\[
\Phi(x)=\Phi_1(x^2)
\]

推广为

\[
\Phi(x)=\Phi_1(x^r),\qquad r\ge2.
\]

证明仍依次采用单坐标 Orlicz 对偶、有限截断、较大序列空间、凸性不等式、Orlicz 范数检验和平移泛函。推广中唯一实质性改变是：原证明直接作用于 \(\Phi_1\) 的凸性不等式，现在应作用于辅助 Young 函数

\[
G(t)=\Phi_1(t^{r/2}).
\]

## 1　记号和预备事实

设 \((\Omega,\mathcal F,\mathbb P)\) 为概率空间，\((\mathcal F_n)_{n\ge0}\) 为递增过滤，并记

\[
E_n(\,\cdot\,)=E(\,\cdot\mid\mathcal F_n).
\]

设 \((\Phi,\Psi)\) 为一对共轭 Young 函数，并假设

\[
\Phi(x)=\Phi_1(x^r),\qquad r\ge2,
\tag{1}
\]

其中 \(\Phi_1\) 为具有有限幂的 Young 函数。设 \(\phi_1\) 为 \(\Phi_1\) 的右导数，并记

\[
p_1
=\sup_{u>0}
\frac{u\phi_1(u)}{\Phi_1(u)}
<\infty.
\tag{2}
\]

对

\[
\Phi(x)=\Phi_1(x^r)
\]

求右导数并令 \(u=x^r\)，可得

\[
\frac{x\Phi'_+(x)}{\Phi(x)}
=r\frac{u\phi_1(u)}{\Phi_1(u)}.
\]

因此 \(\Phi\) 也具有有限幂，并且

\[
p_\Phi=rp_1.
\tag{3}
\]

特别地，\(\Phi\) 满足全局 \(\Delta_2\) 条件，\(L^\Phi\) 的 Luxemburg 范数具有序连续性。

定义

\[
G(t)=\Phi_1(t^{r/2}),\qquad t\ge0.
\tag{4}
\]

因为 \(r/2\ge1\)，函数 \(t\mapsto t^{r/2}\) 凸且递增，所以 \(G\) 是 Young 函数。设 \(g\) 为 \(G\) 的右导数，则

\[
g(t)=\frac r2t^{r/2-1}\phi_1(t^{r/2}).
\]

令 \(u=t^{r/2}\)，得到

\[
\frac{tg(t)}{G(t)}
=\frac r2\frac{u\phi_1(u)}{\Phi_1(u)}.
\]

所以 \(G\) 的有限幂为

\[
q:=p_G=\frac r2p_1.
\tag{5}
\]

当 \(r=2\) 时，\(G=\Phi_1\) 且 \(q=p_1\)，恰好回到原二次复合情形。

证明中使用原论文所引用的 Burkholder–Davis–Gundy 型凸性不等式：若 \(H\) 是有限幂为 \(p_H\) 的 Young 函数，则对任意有限非负可测序列 \((Z_n)\)，

\[
E H\left(
p_H^{-1}\sum_nE_nZ_n
\right)
\le
E H\left(\sum_nZ_n\right).
\tag{6}
\]

对无限序列，先对前 \(N\) 项应用式(6)，再由单调收敛定理令 \(N\to\infty\)。

## 2　引理的陈述

定义适应序列空间

\[
\delta H^\Phi
=
\left\{
\Theta=(\Theta_n)_{n\ge1}:
\Theta_n\in L^\Phi(\Omega,\mathcal F_n,\mathbb P),\
\left\|
\left(\sum_{n=1}^\infty|\Theta_n|^2\right)^{1/2}
\right\|_{\Phi,L}<\infty
\right\},
\]

并令

\[
\|\Theta\|_{\delta H^\Phi}
=
\left\|
\left(\sum_{n=1}^\infty|\Theta_n|^2\right)^{1/2}
\right\|_{\Phi,L}.
\]

这里的元素只要求适应性，不要求 \(E_{n-1}\Theta_n=0\)。

**引理3.1.**　设 \(\Lambda\) 是 \(\delta H^\Phi\) 上的有界线性泛函，即存在 \(B>0\)，使得

\[
|\Lambda(\Theta)|
\le
B\|\Theta\|_{\delta H^\Phi},
\qquad
\Theta\in\delta H^\Phi.
\tag{7}
\]

则存在适应序列

\[
\sigma=(\sigma_n)_{n\ge1},
\qquad
\sigma_n\in L^\Psi(\Omega,\mathcal F_n,\mathbb P),
\]

使得

\[
\Lambda(\Theta)
=
\sum_{n=1}^\infty E(\Theta_n\sigma_n),
\qquad
\Theta\in\delta H^\Phi,
\tag{8}
\]

并且

\[
\left\|
\left(\sum_{n=1}^\infty|\sigma_n|^2\right)^{1/2}
\right\|_{\Psi,L}
\le
\sqrt q\,B
=
\sqrt{\frac r2p_1}\,B,
\tag{9}
\]

同时

\[
\left\|
\left(
\sum_{n=1}^\infty
|E_{n-1}\sigma_n|^2
\right)^{1/2}
\right\|_{\Psi,L}
\le
(\sqrt q+1)B
=
\left(\sqrt{\frac r2p_1}+1\right)B.
\tag{10}
\]

式(10)中的平方位于条件期望之外，即被求和项为

\[
|E(\sigma_n\mid\mathcal F_{n-1})|^2,
\]

而不是 \(E(|\sigma_n|^2\mid\mathcal F_{n-1})\)。

## 3　逐坐标构造代表元

固定 \(n\ge1\)。对任意 \(X\in L^\Phi(\Omega,\mathcal F_n,\mathbb P)\)，定义单坐标序列

\[
\Theta_i^X
=
\begin{cases}
X,&i=n,\\
0,&i\ne n.
\end{cases}
\tag{11}
\]

显然 \(\Theta^X\in\delta H^\Phi\)，并且

\[
\|\Theta^X\|_{\delta H^\Phi}
=\|X\|_{\Phi,L}.
\]

由式(7)，

\[
|\Lambda(\Theta^X)|
\le
B\|X\|_{\Phi,L}.
\tag{12}
\]

因此

\[
X\longmapsto\Lambda(\Theta^X)
\]

是 \(L^\Phi(\Omega,\mathcal F_n,\mathbb P)\) 上的有界线性泛函。因为 \(\Phi\) 具有有限幂，Orlicz 空间对偶定理给出

\[
\sigma_n\in L^\Psi(\Omega,\mathcal F_n,\mathbb P)
\]

使得

\[
\Lambda(\Theta^X)
=E(X\sigma_n),
\qquad
X\in L^\Phi(\Omega,\mathcal F_n,\mathbb P).
\tag{13}
\]

而且相应 associate 范数满足

\[
\|\sigma_n\|_{\Psi,O}\le B.
\tag{14}
\]

由于 Luxemburg 范数不超过 associate 范数，

\[
\|\sigma_n\|_{\Psi,L}\le B.
\tag{15}
\]

对有限支撑序列

\[
\Theta^{(N)}
=(\Theta_1,\ldots,\Theta_N,0,0,\ldots),
\]

由线性性和式(13)，

\[
\Lambda(\Theta^{(N)})
=
\sum_{n=1}^NE(\Theta_n\sigma_n).
\tag{16}
\]

现在取任意 \(\Theta\in\delta H^\Phi\)。因为

\[
\left(
\sum_{n>N}|\Theta_n|^2
\right)^{1/2}
\downarrow0
\quad\text{几乎处处},
\]

且它被

\[
\left(\sum_{n\ge1}|\Theta_n|^2\right)^{1/2}
\in L^\Phi
\]

控制，又因为 \(L^\Phi\) 的 Luxemburg 范数具有序连续性，所以

\[
\|\Theta-\Theta^{(N)}\|_{\delta H^\Phi}
=
\left\|
\left(
\sum_{n>N}|\Theta_n|^2
\right)^{1/2}
\right\|_{\Phi,L}
\longrightarrow0.
\tag{17}
\]

由 \(\Lambda\) 的连续性，

\[
\Lambda(\Theta)
=\lim_{N\to\infty}\Lambda(\Theta^{(N)})
=\lim_{N\to\infty}
\sum_{n=1}^NE(\Theta_n\sigma_n).
\tag{18}
\]

因此式(8)至少作为有限部分和的极限成立。后面证明

\[
\left(\sum_n|\sigma_n|^2\right)^{1/2}\in L^\Psi
\]

之后，还可由 Orlicz–Hölder 不等式说明该级数绝对收敛。

## 4　较大序列空间与条件期望投影

定义较大空间

\[
\widehat{\delta H^\Phi}
=
\left\{
\Theta=(\Theta_n)_{n\ge1}:
\Theta_n\in L^\Phi(\Omega,\mathcal F,\mathbb P),\
\left\|
\left(\sum_{n=1}^\infty|\Theta_n|^2\right)^{1/2}
\right\|_{\Phi,L}<\infty
\right\}.
\]

对 \(\Theta\in\widehat{\delta H^\Phi}\)，定义

\[
P\Theta=(E_n\Theta_n)_{n\ge1}.
\tag{19}
\]

以下证明 \(P\Theta\in\delta H^\Phi\) 并估计 \(P\) 的范数。

令

\[
a
=
\left\|
\left(\sum_{n=1}^\infty|\Theta_n|^2\right)^{1/2}
\right\|_{\Phi,L}.
\tag{20}
\]

若 \(a=0\)，则 \(\Theta_n=0\) 几乎处处，结论显然成立。以下设 \(a>0\)。由 Luxemburg 范数的定义和式(1)，

\[
\begin{aligned}
1
&\ge
E\Phi\left(
a^{-1}
\left(\sum_{n=1}^\infty|\Theta_n|^2\right)^{1/2}
\right)\\
&=
E\Phi_1\left(
a^{-r}
\left(\sum_{n=1}^\infty|\Theta_n|^2\right)^{r/2}
\right)\\
&=
EG\left(
a^{-2}\sum_{n=1}^\infty|\Theta_n|^2
\right).
\end{aligned}
\tag{21}
\]

对有限部分和应用式(6)，其中 \(H=G\)、\(p_H=q\)、\(Z_n=a^{-2}|\Theta_n|^2\)，再令有限项数趋于无穷，得到

\[
EG\left(
q^{-1}a^{-2}
\sum_{n=1}^\infty E_n|\Theta_n|^2
\right)
\le
EG\left(
a^{-2}\sum_{n=1}^\infty|\Theta_n|^2
\right)
\le1.
\tag{22}
\]

另一方面，由条件 Jensen 不等式，

\[
|E_n\Theta_n|^2
\le
E_n|\Theta_n|^2.
\tag{23}
\]

所以

\[
\sum_{n=1}^\infty|E_n\Theta_n|^2
\le
\sum_{n=1}^\infty E_n|\Theta_n|^2.
\tag{24}
\]

由 \(G\) 的单调性以及式(22)，

\[
EG\left(
q^{-1}a^{-2}
\sum_{n=1}^\infty|E_n\Theta_n|^2
\right)
\le1.
\tag{25}
\]

把 \(G(t)=\Phi_1(t^{r/2})\) 代入式(25)，得到

\[
E\Phi_1\left(
q^{-r/2}a^{-r}
\left(
\sum_{n=1}^\infty|E_n\Theta_n|^2
\right)^{r/2}
\right)
\le1.
\tag{26}
\]

再利用 \(\Phi(x)=\Phi_1(x^r)\)，式(26)等价于

\[
E\Phi\left(
q^{-1/2}a^{-1}
\left(
\sum_{n=1}^\infty|E_n\Theta_n|^2
\right)^{1/2}
\right)
\le1.
\tag{27}
\]

因此

\[
\left\|
\left(
\sum_{n=1}^\infty|E_n\Theta_n|^2
\right)^{1/2}
\right\|_{\Phi,L}
\le
\sqrt q\,a.
\tag{28}
\]

这说明 \(P\Theta\in\delta H^\Phi\)，并且

\[
\|P\Theta\|_{\delta H^\Phi}
\le
\sqrt q\,
\|\Theta\|_{\widehat{\delta H^\Phi}}.
\tag{29}
\]

现在定义

\[
\widehat\Lambda(\Theta)
:=\Lambda(P\Theta),
\qquad
\Theta\in\widehat{\delta H^\Phi}.
\tag{30}
\]

这样定义可避免在尚未证明 \(\sigma\in\delta H^\Psi\) 前先假定某个无穷级数收敛。由式(7)和式(29)，

\[
|\widehat\Lambda(\Theta)|
\le
\sqrt q\,B
\|\Theta\|_{\widehat{\delta H^\Phi}}.
\tag{31}
\]

因为 \(P\Theta\in\delta H^\Phi\)，由式(18)，

\[
\begin{aligned}
\widehat\Lambda(\Theta)
&=
\Lambda(P\Theta)\\
&=
\sum_{n=1}^\infty
E\big((E_n\Theta_n)\sigma_n\big).
\end{aligned}
\tag{32}
\]

若 \(\Theta\in\delta H^\Phi\)，则 \(E_n\Theta_n=\Theta_n\)，所以 \(\widehat\Lambda\) 确实延拓了 \(\Lambda\)。

## 5　代表序列平方函数的 \(L^\Psi\) 估计

令

\[
\gamma
=
\left(\sum_{n=1}^\infty|\sigma_n|^2\right)^{1/2},
\qquad
\gamma_N
=
\left(\sum_{n=1}^N|\sigma_n|^2\right)^{1/2}.
\tag{33}
\]

先把 \(\gamma\) 视为取值于 \([0,\infty]\) 的可测函数。取任意

\[
X\ge0,
\qquad
E\Phi(X)\le1.
\tag{34}
\]

对每个 \(N\)，定义有限截断归一化函数

\[
Y_N
=
\begin{cases}
X\gamma_N^{-1},&\gamma_N>0,\\
0,&\gamma_N=0.
\end{cases}
\tag{35}
\]

并定义

\[
\Xi^{(N)}
=
(Y_N\sigma_1,\ldots,Y_N\sigma_N,0,0,\ldots).
\tag{36}
\]

由于

\[
\left(
\sum_{n=1}^N|Y_N\sigma_n|^2
\right)^{1/2}
=Y_N\gamma_N
=X\mathbf1_{\{\gamma_N>0\}}
\le X,
\tag{37}
\]

故

\[
E\Phi\left(
\left(
\sum_{n=1}^N|Y\sigma_n|^2
\right)^{1/2}
\right)
\le
E\Phi(X)
\le1.
\]

因此

\[
\|\Xi^{(N)}\|_{\widehat{\delta H^\Phi}}
\le1.
\tag{38}
\]

由式(31)，

\[
|\widehat\Lambda(\Xi^{(N)})|
\le
\sqrt q\,B.
\tag{39}
\]

另一方面，利用 \(\sigma_n\) 的 \(\mathcal F_n\)-可测性以及条件期望的塔性质，

\[
\begin{aligned}
\widehat\Lambda(\Xi^{(N)})
&=
\sum_{n=1}^N
E\big(E_n(Y_N\sigma_n)\sigma_n\big)\\
&=
\sum_{n=1}^NE(Y_N\sigma_n^2)\\
&=
E(X\gamma_N).
\end{aligned}
\tag{40}
\]

需要注意：这里必须使用有限截断 \(\gamma_N\) 作归一化，而不能在尚未证明 \(\gamma<\infty\) 几乎处处之前直接使用 \(X/\gamma\)。由于

\[
0\le X\gamma_N\uparrow X\gamma
\]

几乎处处，由单调收敛定理和式(39)，

\[
E(X\gamma)
\le
\sqrt q\,B.
\tag{41}
\]

对所有满足式(34)的 \(X\) 取上确界，得到 \(\gamma\) 的 associate 范数估计

\[
\|\gamma\|_{\Psi,O}
=
\sup_{\substack{X\ge0\\E\Phi(X)\le1}}
E(X\gamma)
\le
\sqrt q\,B.
\tag{42}
\]

Luxemburg 范数不超过 associate 范数，所以

\[
\|\gamma\|_{\Psi,L}
\le
\sqrt q\,B.
\tag{43}
\]

结合式(5)，

\[
\left\|
\left(
\sum_{n=1}^\infty|\sigma_n|^2
\right)^{1/2}
\right\|_{\Psi,L}
\le
\sqrt{\frac r2p_1}\,B.
\]

这证明了式(9)，并说明 \(\sigma\in\delta H^\Psi\)。

此时对任意 \(\Theta\in\delta H^\Phi\)，逐点 Cauchy–Schwarz 和 Orlicz–Hölder 不等式给出

\[
\begin{aligned}
\sum_{n=1}^\infty E|\Theta_n\sigma_n|
&=
E\sum_{n=1}^\infty|\Theta_n\sigma_n|\\
&\le
E\left[
\left(\sum_{n=1}^\infty|\Theta_n|^2\right)^{1/2}
\left(\sum_{n=1}^\infty|\sigma_n|^2\right)^{1/2}
\right]\\
&<\infty.
\end{aligned}
\tag{44}
\]

所以式(8)中的级数实际上绝对收敛。

## 6　平移泛函与预测项估计

对任意 \(\Theta=(\Theta_1,\Theta_2,\ldots)\in\delta H^\Phi\)，定义右移序列

\[
\overline\Theta
=(0,\Theta_1,\Theta_2,\ldots).
\tag{45}
\]

因为 \(\Theta_n\) 是 \(\mathcal F_n\)-可测的，所以它也是 \(\mathcal F_{n+1}\)-可测的，从而 \(\overline\Theta\in\delta H^\Phi\)。并且

\[
\|\overline\Theta\|_{\delta H^\Phi}
=
\|\Theta\|_{\delta H^\Phi}.
\tag{46}
\]

定义平移泛函

\[
\overline\Lambda(\Theta)
:=
\Lambda(\overline\Theta).
\tag{47}
\]

由式(7)和式(46)，

\[
|\overline\Lambda(\Theta)|
\le
B\|\Theta\|_{\delta H^\Phi}.
\tag{48}
\]

对 \(\overline\Lambda\) 重复已经证明的第一部分，存在

\[
\mu=(\mu_n)_{n\ge1}\in\delta H^\Psi
\]

使得

\[
\overline\Lambda(\Theta)
=
\sum_{n=1}^\infty E(\Theta_n\mu_n),
\tag{49}
\]

且

\[
\left\|
\left(\sum_{n=1}^\infty|\mu_n|^2\right)^{1/2}
\right\|_{\Psi,L}
\le
\sqrt q\,B.
\tag{50}
\]

另一方面，由 \(\Lambda\) 的表示式，

\[
\begin{aligned}
\overline\Lambda(\Theta)
&=
\Lambda(0,\Theta_1,\Theta_2,\ldots)\\
&=
\sum_{n=1}^\infty E(\Theta_n\sigma_{n+1})\\
&=
\sum_{n=1}^\infty
E\big(\Theta_nE_n\sigma_{n+1}\big).
\end{aligned}
\tag{51}
\]

比较式(49)和式(51)。固定 \(n\)，取只有第 \(n\) 个坐标非零的任意有界 \(\mathcal F_n\)-可测测试变量，可由 \(L^\Phi(\mathcal F_n)\) 与 \(L^\Psi(\mathcal F_n)\) 配对的唯一性得到

\[
\mu_n=E_n\sigma_{n+1}
\qquad\text{几乎处处}.
\tag{52}
\]

由式(50)，

\[
\left\|
\left(
\sum_{n=1}^\infty
|E_n\sigma_{n+1}|^2
\right)^{1/2}
\right\|_{\Psi,L}
\le
\sqrt q\,B.
\tag{53}
\]

剩余首项由条件期望在 Orlicz 空间中的收缩性和式(15)控制：

\[
\|E_0\sigma_1\|_{\Psi,L}
\le
\|\sigma_1\|_{\Psi,L}
\le B.
\tag{54}
\]

逐点有

\[
\begin{aligned}
\left(
\sum_{n=1}^\infty
|E_{n-1}\sigma_n|^2
\right)^{1/2}
&=
\left(
|E_0\sigma_1|^2
+
\sum_{n=1}^\infty
|E_n\sigma_{n+1}|^2
\right)^{1/2}\\
&\le
|E_0\sigma_1|
+
\left(
\sum_{n=1}^\infty
|E_n\sigma_{n+1}|^2
\right)^{1/2}.
\end{aligned}
\tag{55}
\]

由 Luxemburg 范数的三角不等式、式(53)和式(54)，

\[
\left\|
\left(
\sum_{n=1}^\infty
|E_{n-1}\sigma_n|^2
\right)^{1/2}
\right\|_{\Psi,L}
\le
(1+\sqrt q)B.
\tag{56}
\]

代入 \(q=\frac r2p_1\)，即得式(10)。

引理得证。

## 7　与二次复合情形的对应

当 \(r=2\) 时，

\[
G(t)=\Phi_1(t),\qquad
q=p_1.
\]

于是式(9)和式(10)分别化为

\[
\left\|
\left(\sum_n|\sigma_n|^2\right)^{1/2}
\right\|_{\Psi,L}
\le
\sqrt{p_1}\,B,
\]

以及

\[
\left\|
\left(\sum_n|E_{n-1}\sigma_n|^2\right)^{1/2}
\right\|_{\Psi,L}
\le
(\sqrt{p_1}+1)B,
\]

与原论文引理3.1的估计一致。

因此，原二次复合证明能够推广到 \(r\ge2\)。推广并非简单替换指数，而是在凸性不等式处把 \(\Phi_1\) 替换为

\[
G(t)=\Phi_1(t^{r/2}),
\]

并把有限幂常数 \(p_1\) 替换为

\[
q=p_G=\frac r2p_1.
\]

## 参考文献

[1] DAM B K. Connection between the BMO- and the \(K_\Phi\)-spaces[J]. Annales Universitatis Scientiarum Budapestinensis, Sectio Computatorica, 1988, 9: 51-66.

[2] BURKHOLDER D L, DAVIS B J, GUNDY R F. Integral inequalities for convex functions of operators on martingales[C]//Proceedings of the Sixth Berkeley Symposium on Mathematical Statistics and Probability. Berkeley: University of California Press, 1972: 223-240.

[3] KRASNOSELSKII M A, RUTICKII Y B. Convex Functions and Orlicz Spaces[M]. Groningen: Noordhoff, 1961.
