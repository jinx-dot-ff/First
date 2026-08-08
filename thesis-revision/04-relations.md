# 第4章 空间关系与条件边界

## 4.1 与经典 \(H^p\) 的关系

当 \(\Phi(t)=t^p\) 时，

\[
H_S^\Phi=H_S^p,\qquad H_s^\Phi=H_s^p.
\]

一般地，若存在 \(c,C,t_0>0\) 使

\[
\Phi_2(t)\ge C\Phi_1(ct),\qquad t\ge t_0,
\]

则在概率空间上

\[
L^{\Phi_2}\hookrightarrow L^{\Phi_1},
\qquad
H_S^{\Phi_2}\hookrightarrow H_S^{\Phi_1}.
\]

例如，对 \(p>1\)，

\[
H_S^p\hookrightarrow H_S^{\,t\log(e+t)}\hookrightarrow H_S^1.
\]

一步鞅可直观看出这一关系。设 \(\mathcal F_0\) 平凡，\(EX=0\)，令 \(f_0=0\)、\(f_n=X\)（\(n\ge1\)）。则 \(S(f)=|X|\)，所以 \(f\in H_S^\Phi\) 当且仅当 \(X\in L^\Phi\)。若

\[
\mathbb P(|X|>t)\asymp \frac1{t^2\log t},
\]

则可以有 \(X\in L\log L\) 而 \(X\notin L^2\)。

## 4.2 幂型复合函数类

若

\[
\Phi(t)=\Phi_1(t^r),\qquad r\ge2,
\]

则对 \(\lambda\ge1\)，由凸性

\[
\Phi(\lambda t)
=\Phi_1(\lambda^rt^r)
\ge\lambda^r\Phi_1(t^r)
=\lambda^r\Phi(t).
\]

故该函数类至少具有 \(r\) 次下增长。

对 \(\Phi(t)=t^p\)，相应外层函数为

\[
\Phi_1(u)=u^{p/r}.
\]

它为 Young 函数至少要求 \(p\ge r\)。因此固定 \(r\) 时只覆盖 \(p\ge r\)；允许选择任意 \(r\ge2\) 时覆盖 \(p\ge2\)，但不覆盖 \(1\le p<2\)。

非纯幂例子为

\[
\Phi_1(u)=u\log(e+u),\qquad
\Phi(t)=t^r\log(e+t^r).
\]

这说明复合条件并不等于只研究 \(H^r\)。

## 4.3 两条对偶路线

Hardy 型路线为

\[
(D_\Phi)+(C_\Phi)
\Longrightarrow
(H_S^\Phi)^*\simeq H_S^\Psi,
\]

以及

\[
(D_\Phi)+(C_\Phi)
\Longrightarrow
(H_s^\Phi)^*\simeq H_s^\Psi.
\]

\(K\) 型路线为

\[
(D_\Phi)+(G_\Psi)
\Longrightarrow
(H_S^\Phi)^*\longrightarrow\widetilde K^\Psi,
\]

\[
(P_{\Psi,s})+(M_{\Psi_1})
\Longrightarrow
\widetilde K^\Psi\hookrightarrow K^\Psi.
\]

再加 \((FG_\Phi)\) 才能得到

\[
(H_S^\Phi)^*\simeq K^\Psi.
\]

因此不能无条件写成

\[
(H_S^\Phi)^*=H_S^\Psi=K^\Psi.
\]

## 4.4 条件依赖关系

各假设作用如下：

| 假设 | 主要作用 |
|---|---|
| \((D_\Phi)\) | 排除奇异泛函、有限鞅稠密、尾范数收敛 |
| \((P_{\Phi,r})\) | 产生辅助函数 \(A_\Phi\) |
| \((C_\Phi)\) | 控制坐标条件期望投影 |
| \((G_\Psi)\) | 从向量值代表构造二阶尾量代表 |
| \((D_\Psi)\) | \(\widetilde K^\Psi\) 拟范数尾收敛 |
| \((P_{\Psi,s})\) | 把二阶矩提升到 \(s\) 阶矩 |
| \((M_{\Psi_1})\) | 控制 \(s\) 阶条件极大函数 |
| \((FG_\Phi)\) | 证明每个 \(K^\Psi\) 元素定义有界泛函 |

\((M_\Psi)\) 与 \((M_{\Psi_1})\) 不能互换；\((D_\Psi)\) 只在需要拟范数收敛时使用。

## 4.5 理论边界与文献定位

本文不覆盖：

1. \(H^1\) 端点；
2. 一般的 \(1<p<2\) 幂型空间；
3. 不具有复合结构的一般 Young 函数；
4. 缺少序连续性时的奇异泛函部分；
5. 连续时间、多参数或未另行验证的过滤结构。

已有文献已经在共轭 Young 函数双方有限幂时建立较一般的 Hardy–Orlicz 对偶。因此，普通平方函数部分主要定位为幂型复合条件下的自足证明、投影机制说明和证明细节补全。若要把 \(K^\Psi\) 部分称为严格推广，必须给出满足本文全部极大不等式、但不属于已有双方有限幂范围的明确 Young 函数例子。

条件平方函数版本也须与现有 Musielak–Orlicz Hardy 空间对偶逐条比较；如果一般定理可直接退化到本文情形，则应把本节定位为特例的直接证明，而不是首创结论。

## 4.6 本章小结

幂型复合条件是结构性充分条件，不是一般 Hardy–Orlicz 对偶的必要充分刻画。\(H_S^\Psi\)、\(\widetilde K^\Psi\) 和 \(K^\Psi\) 分别控制平方函数、二阶尾量和一阶尾量；三者之间的联系必须通过明确假设逐步建立。
