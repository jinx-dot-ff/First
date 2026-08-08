# 幂型复合条件下鞅 Hardy–Orlicz 空间的对偶性研究（修订稿）

本目录依据初稿逐章重写。正文统一采用以下原则：

- 所有鞅从 \(0\) 出发；
- \(H_S^\Phi\) 表示平方函数型空间，\(H_s^\Phi\) 表示条件平方函数型空间；
- 一般适应序列与鞅差序列分别定义；
- \(\|\cdot\|_{\Phi,L}\) 表示 Luxemburg 范数，\(\|\cdot\|_{\Phi,O}\) 表示 associate 范数；
- Hardy 型对偶与 \(K^\Psi\) 型对偶分别陈述；
- 尚待核对原始文献的凸性、极大及 Fefferman–Garsia 不等式均作为显式假设。

## 目录

0. [中英文摘要与符号说明](00-frontmatter.md)
1. [绪论](01-introduction.md)
   1. 研究背景与意义
   2. 国内外研究现状
   3. 研究问题与主要内容
   4. 主要工作与特点
   5. 研究范围与局限
   6. 论文结构
   7. 本章小结
2. [基本记号与预备知识](02-preliminaries.md)
   1. 概率空间、过滤与鞅
   2. Young 函数及其共轭
   3. Orlicz 空间及两种范数
   4. Hardy–Orlicz 鞅空间
   5. 适应序列与鞅差序列空间
   6. \(K^\Psi\) 与 \(\widetilde K^\Psi\)
   7. 结构假设与辅助不等式
   8. 本章小结
3. [幂型复合条件下的对偶表示](03-duality.md)
   1. 向量值 Orlicz 表示
   2. 适应序列投影
   3. 普通平方函数型对偶
   4. 条件平方函数型对偶
   5. \(\widetilde K^\Psi\) 代表
   6. 从 \(\widetilde K^\Psi\) 到 \(K^\Psi\)
   7. \(K^\Psi\) 型对偶
   8. \(H_S^\Psi\) 与 \(K^\Psi\) 的包含关系
   9. 本章小结
4. [空间关系与条件边界](04-relations.md)
   1. 与经典 \(H^p\) 的关系
   2. 幂型复合函数类
   3. 两条对偶路线
   4. 条件依赖关系
   5. 理论边界与文献定位
   6. 本章小结
5. [结论与展望](05-conclusion.md)
   1. 主要结论
   2. 局限性
   3. 后续研究方向
- [参考文献与引用说明](references.md)
- [研究成果与致谢](06-achievements-acknowledgments.md)

> 说明：本稿是一份数学内容修订底稿，不替代学校 Word/LaTeX 模板。标记为“外部假设”的结果须在最终送审前依据原始论文逐条核对定理编号、指标范围和 \(K\) 空间定义。

## Word 版本

已生成按《中南大学研究生学位论文撰写规范（2022）》设置的 Word 文件：

`幂型复合条件下鞅Hardy-Orlicz空间对偶性研究_修订稿.docx`

主要版式包括 A4 页面、146 mm 正文宽度、正文小四号宋体/Times New Roman、固定 20 磅行距、分级标题、原生 Word 数学公式、前置部分罗马页码、正文阿拉伯页码、正文页眉和自动目录域。

重新生成：

```bash
python3 -m pip install -r requirements-docx.txt
python3 tools/build_thesis_docx.py
```

首次用 Word 打开后，请选择目录并执行“更新整个目录”，同时核对学校提供的正式封面附件、UDC、中图分类号、答辩日期和签名栏。
