#!/usr/bin/env python3
"""Build the standalone detailed proof of generalized Lemma 3.1."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pypandoc
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt

from build_thesis_docx import (
    ROOT,
    SRC,
    add_body_header,
    add_page_footer,
    configure_reference_doc,
    set_page_numbering,
)


SOURCE = SRC / "lemma3.1-detailed.md"
OUTPUT = SRC / "引理3.1_r次幂复合条件_完整证明.docx"


def polish(doc: Document) -> None:
    settings = doc.settings._element
    update_fields = settings.find(qn("w:updateFields"))
    if update_fields is None:
        update_fields = OxmlElement("w:updateFields")
        settings.append(update_fields)
    update_fields.set(qn("w:val"), "true")

    for index, paragraph in enumerate(doc.paragraphs):
        fmt = paragraph.paragraph_format
        if paragraph.style.name in {"Normal", "Body Text", "First Paragraph"}:
            fmt.line_spacing_rule = WD_LINE_SPACING.EXACTLY
            fmt.line_spacing = Pt(20)
            fmt.space_after = Pt(0)
            if paragraph.text.strip():
                fmt.first_line_indent = Pt(24)
        if paragraph._p.xpath(".//m:oMath | .//m:oMathPara"):
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            fmt.first_line_indent = Pt(0)
        if paragraph.text.startswith("[") and paragraph.text[1:2].isdigit():
            fmt.first_line_indent = Pt(-24)
            fmt.left_indent = Pt(24)
        if index == 0:
            fmt.page_break_before = False
        for run in paragraph.runs:
            run.font.name = "Times New Roman"
            run._element.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "宋体")

    section = doc.sections[0]
    set_page_numbering(section, "decimal", 1)
    add_page_footer(section)
    add_body_header(section)


def build() -> Path:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        reference = tmp_path / "reference.docx"
        generated = tmp_path / "lemma31.docx"
        configure_reference_doc(reference)
        pypandoc.convert_file(
            str(SOURCE),
            "docx",
            outputfile=str(generated),
            extra_args=[
                f"--reference-doc={reference}",
                "--from=markdown+raw_attribute+raw_tex+tex_math_single_backslash",
                "--standalone",
            ],
        )
        doc = Document(generated)
        polish(doc)
        doc.core_properties.title = "引理3.1：幂型复合条件下适应序列空间上泛函的表示"
        doc.core_properties.subject = "基于二次复合证明路线的 r 次幂推广"
        doc.core_properties.author = "杜闻伦"
        doc.core_properties.keywords = "Hardy–Orlicz; Young函数; 对偶表示; 幂型复合"
        doc.save(OUTPUT)
    return OUTPUT


if __name__ == "__main__":
    print(build())
