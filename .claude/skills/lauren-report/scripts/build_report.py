#!/usr/bin/env python3
"""Build an Opal Capital quarterly EARNINGS UPDATE (.docx) in Lauren Harmon's format. Python 3.8+ stdlib only.

    python build_report.py report.json "<out dir or .docx path>"

Layout (her ASML / UNH 2Q26 and 3Q26 updates): US Letter portrait, Calibri 11; a bold title block; the Excel-style
header block (identity / pricing / balance sheet) over the Financial Summary (10 quarters + last FY + 4 estimate
years, the annual block shaded); Recommendation; Headline results (Positives / Negatives); Geographic and Segment
highlights; Headwinds and risks; Guidance; Rating actions and target price changes (optional broker table);
Appendix of numbered figures, two per row, as NATIVE Word charts (bar, line, 100% stacked, clustered, bar+line
combo on a secondary axis); Why we own. A figure whose data is not supplied renders as a labelled placeholder
(e.g. AlphaSense-only data), never as invented numbers. Spec: ../references/report_spec.md; worked example:
../references/example_asml_2q26.json. Exit 0 prints "OK: <path>"; a spec error exits 2 naming the block.
"""
import datetime
import json
import os
import re
import sys
import zipfile
from xml.sax.saxutils import escape

PAGE_W, PAGE_H, MARGIN = 12240, 15840, 720
TEXT_W = PAGE_W - 2 * MARGIN                      # 10800 twips
EMU_PER_TWIP = 635
PALETTE = ["5B9BD5", "ED7D31", "A5A5A5", "FFC000", "4472C4", "70AD47", "264478", "9E480E"]
GRID, ANNUAL_FILL, TICKER_FILL, HEAD_FILL = "2F3E9E", "BDD7EE", "FFFF00", "1F3864"

NS_W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
NS_R = 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
NS_WP = 'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"'
NS_A = 'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"'
NS_C = 'xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart"'


class SpecError(Exception):
    pass


# ---------------------------------------------------------------- text primitives

def run(text, bold=False, italic=False, size=None, color=None, highlight=None):
    rpr = ("<w:b/>" if bold else "") + ("<w:i/>" if italic else "")
    if color:
        rpr += '<w:color w:val="%s"/>' % color
    if size:
        rpr += '<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (size, size)
    if highlight:
        rpr += '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % highlight
    parts = str(text).split("\n")
    body = "<w:br/>".join('<w:t xml:space="preserve">%s</w:t>' % escape(p) for p in parts)
    return "<w:r><w:rPr>%s</w:rPr>%s</w:r>" % (rpr, body)


def rich(text, size=None):
    """**bold** and _italic_ inside prose."""
    out = []
    for tok in re.split(r"(\*\*.+?\*\*|(?<![\w])_[^_]+?_(?![\w]))", str(text)):
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**"):
            out.append(run(tok[2:-2], bold=True, size=size))
        elif tok.startswith("_") and tok.endswith("_") and len(tok) > 2:
            out.append(run(tok[1:-1], italic=True, size=size))
        else:
            out.append(run(tok, size=size))
    return "".join(out)


def para(content, ppr=""):
    return "<w:p><w:pPr>%s</w:pPr>%s</w:p>" % (ppr, content)


# ---------------------------------------------------------------- blocks

def b_title(blk):
    return (para(run(blk["company_line"], bold=True), '<w:spacing w:after="0"/>')
            + para(run(blk["period_line"], bold=True), '<w:spacing w:after="240"/>'))


def b_heading(blk):
    return para(run(blk["text"], bold=True), '<w:keepNext/><w:spacing w:before="240" w:after="0"/>')


def b_subhead(blk):
    return para(run(blk["text"], italic=True), '<w:keepNext/><w:spacing w:after="0"/>')


def b_para(blk):
    return para(rich(blk["text"]), '<w:spacing w:after="0"/>')


def b_dash(blk):
    """'-' hanging bullets; an item may be {"topic": ..., "text": ...} -> 'Topic - text'."""
    out = []
    for item in blk["items"]:
        if isinstance(item, dict):
            content = run(item["topic"] + " \u2013 ") + rich(item["text"])
        else:
            content = rich(item)
        out.append(para(run("-") + '<w:r><w:tab/></w:r>' + content,
                        '<w:tabs><w:tab w:val="left" w:pos="360"/></w:tabs><w:spacing w:after="0"/>'
                        '<w:ind w:left="360" w:hanging="360"/>'))
    return "".join(out)


def b_pagebreak(blk):
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def _tc(width, content, fill=None, borders=None, align="left", span=1, size=14, valign="center", border_color=GRID):
    pr = '<w:tcW w:w="%d" w:type="dxa"/>' % width
    if span > 1:
        pr += '<w:gridSpan w:val="%d"/>' % span
    if borders:
        pr += "<w:tcBorders>%s</w:tcBorders>" % "".join(
            '<w:%s w:val="single" w:sz="%d" w:space="0" w:color="%s"/>' % (side, sz, border_color) for side, sz in borders)
    if fill:
        pr += '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % fill
    pr += ('<w:tcMar><w:top w:w="0" w:type="dxa"/><w:left w:w="40" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/>'
           '<w:right w:w="40" w:type="dxa"/></w:tcMar><w:vAlign w:val="%s"/>' % valign)
    jc = '<w:jc w:val="%s"/>' % align if align != "left" else ""
    mark = '<w:rPr><w:sz w:val="%d"/><w:szCs w:val="%d"/></w:rPr>' % (size, size)   # empty cells take the cell's size
    return ('<w:tc><w:tcPr>%s</w:tcPr><w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/>%s%s</w:pPr>%s</w:p></w:tc>'
            % (pr, jc, mark, content))


def _tbl(widths, rows_xml, borders_outer=True):
    grid = "".join('<w:gridCol w:w="%d"/>' % w for w in widths)
    bd = ""
    if borders_outer:
        bd = ("<w:tblBorders>%s</w:tblBorders>" % "".join(
            '<w:%s w:val="single" w:sz="6" w:space="0" w:color="%s"/>' % (s, GRID) for s in ("top", "left", "bottom", "right")))
    return ('<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/><w:tblLayout w:type="fixed"/>%s'
            '<w:tblCellMar><w:left w:w="40" w:type="dxa"/><w:right w:w="40" w:type="dxa"/></w:tblCellMar>'
            '<w:tblLook w:val="0000"/></w:tblPr><w:tblGrid>%s</w:tblGrid>%s</w:tbl>' % (sum(widths), bd, grid, "".join(rows_xml)))


def b_summary(blk, where):
    """Header block + Financial Summary, one Excel-style grid (7pt).

    header: {"left": [[label, v1, v2?], ...], "middle": [[label, value, label2, value2], ...],
             "right": [[label, amount, pct, label2, amount2, pct2], ...]}
    summary: {"quarters": [...10], "annual": [...5], "rows": [{"label", "q": [...], "a": [...], "kind": "growth|bold|"}]}
    """
    S = 14  # 7pt
    hdr = blk["header"]
    fs = blk["summary"]
    nq, na = len(fs["quarters"]), len(fs["annual"])
    label_w = 1300
    a_first, a_rest = 860, 700                     # the last-FY column carries the "0.8%-1.5%" ranges
    q_w = (TEXT_W - label_w - a_first - a_rest * (na - 1)) // nq
    widths = [label_w] + [q_w] * nq + [a_first] + [a_rest] * (na - 1)
    widths[-1] += TEXT_W - sum(widths)
    rows = []
    # ---- header block: 9 rows, laid over the same grid (label | 3 cols left | 4 cols middle | rest right)
    left, mid, right = hdr.get("left", []), hdr.get("middle", []), hdr.get("right", [])
    n = max(len(left), len(mid), len(right))
    lspan, mspan = 3, 6                            # panels ~28% / 32% / 40% of the width
    rspan = nq + na - lspan - mspan
    for i in range(n):
        L = left[i] if i < len(left) else ["", "", ""]
        M = mid[i] if i < len(mid) else ["", "", "", ""]
        R = right[i] if i < len(right) else ["", "", "", "", "", ""]
        lab = run(L[0], size=S, highlight=TICKER_FILL if i == 0 else None, bold=(i == 0))
        lv = run(L[1], size=S, highlight=TICKER_FILL if i == 0 else None) + (run("      " + L[2], size=S) if len(L) > 2 and L[2] else "")
        T = '<w:r><w:rPr><w:sz w:val="%d"/></w:rPr><w:tab/></w:r>' % S
        mtext = run(M[0], size=S) + T + run(M[1], size=S) + T + run(M[2], size=S) + T + run(M[3], size=S)
        rtext = T.join(run(v, size=S) for v in R[:6])
        mw = sum(widths[1 + lspan:1 + lspan + mspan])
        rw = sum(widths[1 + lspan + mspan:])
        mid_tabs = '<w:tabs><w:tab w:val="right" w:pos="%d"/><w:tab w:val="left" w:pos="%d"/><w:tab w:val="right" w:pos="%d"/></w:tabs>' % (
            int(mw * 0.52), int(mw * 0.55), int(mw * 0.97))
        r_tabs = '<w:tabs><w:tab w:val="right" w:pos="%d"/><w:tab w:val="right" w:pos="%d"/><w:tab w:val="left" w:pos="%d"/><w:tab w:val="right" w:pos="%d"/><w:tab w:val="right" w:pos="%d"/></w:tabs>' % (
            int(rw * 0.30), int(rw * 0.44), int(rw * 0.46), int(rw * 0.80), int(rw * 0.97))
        cells = [_tc(widths[0], lab, size=S),
                 _tc(sum(widths[1:1 + lspan]), lv, span=lspan, borders=[("right", 6)], size=S),
                 _tc(mw, mtext, span=mspan, borders=[("right", 6)], size=S).replace("<w:pPr>", "<w:pPr>" + mid_tabs, 1),
                 _tc(rw, rtext, span=rspan, size=S).replace("<w:pPr>", "<w:pPr>" + r_tabs, 1)]
        rows.append('<w:tr><w:trPr><w:cantSplit/></w:trPr>%s</w:tr>' % "".join(cells))
    # ---- Financial Summary header row
    head = [_tc(widths[0], run("Financial Summary", bold=True, size=S, color="FFFFFF"), fill=HEAD_FILL, borders=[("top", 6)], size=S)]
    for j, q in enumerate(fs["quarters"] + fs["annual"]):
        head.append(_tc(widths[1 + j], run(q, bold=True, size=S, color="FFFFFF"), fill=HEAD_FILL, borders=[("top", 6)],
                        align="center", size=S))
    rows.append('<w:tr><w:trPr><w:cantSplit/></w:trPr>%s</w:tr>' % "".join(head))
    for r in fs["rows"]:
        kind = r.get("kind", "")
        q, a = list(r.get("q", [])), list(r.get("a", []))
        q += [""] * (nq - len(q))
        a += [""] * (na - len(a))
        if len(q) != nq or len(a) != na:
            raise SpecError("%s: row %r has %d quarters / %d annual, want %d / %d" % (where, r["label"], len(q), len(a), nq, na))
        it = kind == "growth"
        cells = [_tc(widths[0], run(("  " if it else "") + r["label"], italic=it, size=S), size=S,
                     borders=[("top", 4)] if kind == "rule" else None)]
        for j, v in enumerate(q + a):
            annual = j >= nq
            cells.append(_tc(widths[1 + j], run(v, italic=it, size=S, color=r.get("color")), fill=ANNUAL_FILL if annual else None,
                             align="right", size=S, borders=([("left", 6)] if j == nq else None)))
        rows.append('<w:tr><w:trPr><w:cantSplit/></w:trPr>%s</w:tr>' % "".join(cells))
    return _tbl(widths, rows) + para("", '<w:spacing w:after="120"/>')


def b_table(blk, where):
    """Plain grid table (e.g. the broker table): header row bold, all borders."""
    rows = blk["rows"]
    ncols = len(rows[0])
    widths = blk.get("widths") or [TEXT_W * 85 // 100 // ncols] * ncols
    out = []
    for i, r in enumerate(rows):
        if len(r) != ncols:
            raise SpecError("%s: row %d has %d cells, want %d" % (where, i, len(r), ncols))
        cells = [_tc(widths[k], run(v, bold=(i == 0), size=22), borders=[("top", 4), ("left", 4), ("bottom", 4), ("right", 4)],
                     size=22) for k, v in enumerate(r)]
        out.append('<w:tr><w:trPr><w:trHeight w:val="400"/></w:trPr>%s</w:tr>' % "".join(cells))
    return '<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="center"/><w:tblLayout w:type="fixed"/><w:tblLook w:val="0000"/></w:tblPr><w:tblGrid>%s</w:tblGrid>%s</w:tbl>' % (
        sum(widths), "".join('<w:gridCol w:w="%d"/>' % w for w in widths), "".join(out)) + para("", '<w:spacing w:after="120"/>')


# ---------------------------------------------------------------- charts

class Charts:
    def __init__(self):
        self.parts = []      # (name, xml)

    def add(self, xml):
        n = len(self.parts) + 1
        self.parts.append(("chart%d.xml" % n, xml))
        return n


def _txpr(size, bold=False, color="595959"):
    return ('<c:txPr><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="%d" b="%d"><a:solidFill><a:srgbClr val="%s"/></a:solidFill>'
            '<a:latin typeface="Calibri"/></a:defRPr></a:pPr><a:endParaRPr lang="en-US"/></a:p></c:txPr>' % (size, 1 if bold else 0, color))


def _num(v):
    return "" if v is None or v == "" else repr(float(v))


def _ser(i, s, cats, line, labels, fmt):
    color = s.get("color") or PALETTE[i % len(PALETTE)]
    vals = s["values"]
    if len(vals) != len(cats):
        raise SpecError("series %r has %d values for %d categories" % (s.get("name"), len(vals), len(cats)))
    cat = ('<c:cat><c:strRef><c:f>Sheet1!$A$2:$A$%d</c:f><c:strCache><c:ptCount val="%d"/>%s</c:strCache></c:strRef></c:cat>'
           % (len(cats) + 1, len(cats), "".join('<c:pt idx="%d"><c:v>%s</c:v></c:pt>' % (k, escape(str(c))) for k, c in enumerate(cats))))
    pts = "".join('<c:pt idx="%d"><c:v>%s</c:v></c:pt>' % (k, _num(v)) for k, v in enumerate(vals) if v not in (None, ""))
    val = ('<c:val><c:numRef><c:f>Sheet1!$%s$2:$%s$%d</c:f><c:numCache><c:formatCode>%s</c:formatCode><c:ptCount val="%d"/>%s</c:numCache></c:numRef></c:val>'
           % (chr(66 + i), chr(66 + i), len(cats) + 1, escape(fmt), len(cats), pts))
    if line:
        sppr = ('<c:spPr><a:ln w="22225" cap="rnd"><a:solidFill><a:srgbClr val="%s"/></a:solidFill><a:round/></a:ln></c:spPr>'
                '<c:marker><c:symbol val="circle"/><c:size val="4"/><c:spPr><a:solidFill><a:srgbClr val="%s"/></a:solidFill>'
                '<a:ln><a:solidFill><a:srgbClr val="%s"/></a:solidFill></a:ln></c:spPr></c:marker>' % (color, color, color))
    else:
        sppr = '<c:spPr><a:solidFill><a:srgbClr val="%s"/></a:solidFill></c:spPr><c:invertIfNegative val="0"/>' % color
    lab = s.get("labels", labels)
    if lab == "none":
        dl = '<c:dLbls><c:delete val="1"/></c:dLbls>'
    else:
        common = ('<c:numFmt formatCode="%s" sourceLinked="0"/><c:spPr><a:noFill/><a:ln><a:noFill/></a:ln></c:spPr>%s'
                  % (escape(fmt), _txpr(700, bold=True, color="404040")))
        flags = '<c:showLegendKey val="0"/><c:showVal val="1"/><c:showCatName val="0"/><c:showSerName val="0"/><c:showPercent val="0"/><c:showBubbleSize val="0"/>'
        if lab == "last":
            last = max(k for k, v in enumerate(vals) if v not in (None, ""))
            off = flags.replace('<c:showVal val="1"/>', '<c:showVal val="0"/>')
            dl = ('<c:dLbls><c:dLbl><c:idx val="%d"/>%s%s%s</c:dLbl><c:spPr><a:noFill/><a:ln><a:noFill/></a:ln></c:spPr>%s</c:dLbls>'
                  % (last, common, '<c:dLblPos val="r"/>' if line else "", flags, off))
        else:
            pos = '<c:dLblPos val="t"/>' if line else ""
            dl = "<c:dLbls>%s%s%s</c:dLbls>" % (common, pos, flags)
    return ('<c:ser><c:idx val="%d"/><c:order val="%d"/><c:tx><c:strRef><c:f>Sheet1!$%s$1</c:f><c:strCache><c:ptCount val="1"/>'
            '<c:pt idx="0"><c:v>%s</c:v></c:pt></c:strCache></c:strRef></c:tx>%s%s%s%s%s</c:ser>'
            % (i, i, chr(66 + i), escape(s.get("name", "series %d" % (i + 1))), sppr, dl, cat, val,
               '<c:smooth val="0"/>' if line else ""))


def _axes(cat_id, val_id, fmt, pos_val="l", delete_cat=False, crosses="autoZero", pct=False):
    grid = '<c:majorGridlines><c:spPr><a:ln w="6350"><a:solidFill><a:srgbClr val="D9D9D9"/></a:solidFill></a:ln></c:spPr></c:majorGridlines>' if pos_val == "l" else ""
    cat = ('<c:catAx><c:axId val="%d"/><c:scaling><c:orientation val="minMax"/></c:scaling><c:delete val="%d"/><c:axPos val="b"/>'
           '<c:numFmt formatCode="General" sourceLinked="0"/><c:majorTickMark val="none"/><c:minorTickMark val="none"/>'
           '<c:tickLblPos val="low"/><c:spPr><a:ln w="6350"><a:solidFill><a:srgbClr val="BFBFBF"/></a:solidFill></a:ln></c:spPr>'
           '<c:txPr><a:bodyPr rot="-5400000" vert="horz"/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="700"><a:solidFill><a:srgbClr val="595959"/></a:solidFill></a:defRPr></a:pPr><a:endParaRPr lang="en-US"/></a:p></c:txPr>'
           '<c:crossAx val="%d"/><c:crosses val="autoZero"/><c:auto val="1"/><c:lblAlgn val="ctr"/><c:lblOffset val="100"/>'
           '<c:noMultiLvlLbl val="0"/></c:catAx>' % (cat_id, 1 if delete_cat else 0, val_id))
    val = ('<c:valAx><c:axId val="%d"/><c:scaling><c:orientation val="minMax"/></c:scaling><c:delete val="0"/><c:axPos val="%s"/>%s'
           '<c:numFmt formatCode="%s" sourceLinked="0"/><c:majorTickMark val="none"/><c:minorTickMark val="none"/><c:tickLblPos val="nextTo"/>'
           '<c:spPr><a:ln><a:noFill/></a:ln></c:spPr>%s<c:crossAx val="%d"/><c:crosses val="%s"/><c:crossBetween val="between"/></c:valAx>'
           % (val_id, pos_val, grid, "0%" if pct else escape(fmt), _txpr(700), cat_id, crosses))
    return cat + val


def chart_xml(fig):
    kind = fig.get("type", "bar")
    cats = fig["categories"]
    series = fig["series"]
    fmt = fig.get("format", "0.0")
    labels = fig.get("labels", "all")
    title = ('<c:title><c:tx><c:rich><a:bodyPr/><a:lstStyle/><a:p><a:pPr><a:defRPr sz="1000" b="1"><a:solidFill><a:srgbClr val="595959"/></a:solidFill></a:defRPr></a:pPr>'
             '<a:r><a:rPr lang="en-US" sz="1000" b="1"><a:solidFill><a:srgbClr val="595959"/></a:solidFill></a:rPr><a:t>%s</a:t></a:r></a:p></c:rich></c:tx>'
             '<c:overlay val="0"/></c:title><c:autoTitleDeleted val="0"/>' % escape(fig["title"]))
    plot = []
    if kind in ("bar", "clustered", "stacked100", "stacked"):
        grouping = {"bar": "clustered", "clustered": "clustered", "stacked100": "percentStacked", "stacked": "stacked"}[kind]
        overlap = '<c:overlap val="100"/>' if grouping != "clustered" else '<c:overlap val="-10"/>'
        sers = "".join(_ser(i, s, cats, False, labels, fmt) for i, s in enumerate(series))
        plot.append('<c:barChart><c:barDir val="col"/><c:grouping val="%s"/><c:varyColors val="0"/>%s<c:gapWidth val="%d"/>%s'
                    '<c:axId val="101"/><c:axId val="102"/></c:barChart>' % (grouping, sers, 50 if grouping != "clustered" else 80, overlap))
        plot.append(_axes(101, 102, fmt, pct=(grouping == "percentStacked")))
        legend = len(series) > 1
    elif kind == "line":
        sers = "".join(_ser(i, s, cats, True, labels, fmt) for i, s in enumerate(series))
        plot.append('<c:lineChart><c:grouping val="standard"/><c:varyColors val="0"/>%s<c:marker val="1"/>'
                    '<c:axId val="101"/><c:axId val="102"/></c:lineChart>' % sers)
        plot.append(_axes(101, 102, fmt))
        legend = len(series) > 1
    elif kind == "combo":
        bars = [s for s in series if s.get("as", "bar") == "bar"]
        lines = [s for s in series if s.get("as") == "line"]
        if not bars or not lines:
            raise SpecError("combo figure %r needs bar and line series" % fig["title"])
        b = "".join(_ser(i, s, cats, False, labels, fmt) for i, s in enumerate(bars))
        ln = "".join(_ser(len(bars) + i, s, cats, True, s.get("labels", "last"), s.get("format", fmt)) for i, s in enumerate(lines))
        plot.append('<c:barChart><c:barDir val="col"/><c:grouping val="clustered"/><c:varyColors val="0"/>%s<c:gapWidth val="60"/>'
                    '<c:axId val="101"/><c:axId val="102"/></c:barChart>' % b)
        plot.append('<c:lineChart><c:grouping val="standard"/><c:varyColors val="0"/>%s<c:marker val="1"/>'
                    '<c:axId val="103"/><c:axId val="104"/></c:lineChart>' % ln)
        plot.append(_axes(101, 102, fmt))
        plot.append(_axes(103, 104, lines[0].get("format", fmt), pos_val="r", delete_cat=True, crosses="max"))
        legend = True
    else:
        raise SpecError("figure %r: unknown type %r" % (fig["title"], kind))
    leg = ('<c:legend><c:legendPos val="b"/><c:overlay val="0"/>%s</c:legend>' % _txpr(700)) if legend else ""
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><c:chartSpace %s %s %s><c:roundedCorners val="0"/>'
            '<c:chart>%s<c:plotArea><c:layout/>%s<c:spPr><a:noFill/></c:spPr></c:plotArea>%s<c:plotVisOnly val="1"/>'
            '<c:dispBlanksAs val="gap"/></c:chart><c:spPr><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>'
            '<a:ln w="6350"><a:solidFill><a:srgbClr val="D9D9D9"/></a:solidFill></a:ln></c:spPr>%s</c:chartSpace>'
            % (NS_C, NS_A, NS_R, title, "".join(plot), leg, _txpr(700)))


def inline_chart(n, cx, cy):
    return ('<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="%d" cy="%d"/>'
            '<wp:effectExtent l="0" t="0" r="0" b="0"/><wp:docPr id="%d" name="Chart %d"/><wp:cNvGraphicFramePr/>'
            '<a:graphic %s><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/chart">'
            '<c:chart %s %s r:id="rIdChart%d"/></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>'
            % (cx, cy, 1000 + n, n, NS_A, NS_C, NS_R, n))


def placeholder(fig, w):
    note = fig.get("pending_note") or "Data pending"
    return _tc(w, run(fig["title"], bold=True, size=18, color="595959") + run("\n\n" + note, italic=True, size=16, color="7F7F7F"),
               borders=[("top", 4), ("left", 4), ("bottom", 4), ("right", 4)], align="center", size=18, border_color="D9D9D9")


def b_figures(blk, where, charts):
    """Two figures per row as native charts; {"note": "..."} entries break the grid with a paragraph."""
    col_w = TEXT_W // 2
    cx, cy = (col_w - 160) * EMU_PER_TWIP, int(blk.get("height_in", 2.65) * 914400)
    out, row = [], []

    def flush():
        if not row:
            return
        cells = []
        for fig in row:
            if fig.get("pending") or not fig.get("series"):
                cells.append(placeholder(fig, col_w))
            else:
                n = charts.add(chart_xml(fig))
                cells.append('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/><w:vAlign w:val="top"/></w:tcPr><w:p><w:pPr><w:spacing w:after="80"/><w:jc w:val="center"/></w:pPr>%s</w:p></w:tc>'
                             % (col_w, inline_chart(n, cx, cy)))
        while len(cells) < 2:
            cells.append('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/></w:tcPr><w:p/></w:tc>' % col_w)
        out.append('<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/><w:tblLayout w:type="fixed"/><w:tblLook w:val="0000"/></w:tblPr>'
                   '<w:tblGrid><w:gridCol w:w="%d"/><w:gridCol w:w="%d"/></w:tblGrid><w:tr><w:trPr><w:cantSplit/><w:trHeight w:val="%d" w:hRule="atLeast"/></w:trPr>%s</w:tr></w:tbl>'
                   % (TEXT_W, col_w, col_w, cy // EMU_PER_TWIP + 100, "".join(cells)))
        row.clear()

    for i, fig in enumerate(blk["items"]):
        if "note" in fig:
            flush()
            out.append(para(rich(fig["note"]), '<w:spacing w:before="120" w:after="120"/>'))
            continue
        for k in ("title",):
            if k not in fig:
                raise SpecError("%s item %d: missing %s" % (where, i, k))
        row.append(fig)
        if len(row) == 2:
            flush()
    flush()
    return "".join(out)


BLOCKS = {"title": b_title, "heading": b_heading, "subhead": b_subhead, "para": b_para, "dash": b_dash,
          "pagebreak": b_pagebreak}


# ---------------------------------------------------------------- package

def document_xml(spec, charts):
    body = []
    for i, blk in enumerate(spec["blocks"]):
        t = blk.get("type")
        where = "blocks[%d] (%s)" % (i, t)
        try:
            if t == "summary":
                body.append(b_summary(blk, where))
            elif t == "table":
                body.append(b_table(blk, where))
            elif t == "figures":
                body.append(b_figures(blk, where, charts))
            elif t in BLOCKS:
                body.append(BLOCKS[t](blk))
            else:
                raise SpecError("%s: unknown block type" % where)
        except KeyError as e:
            raise SpecError("%s: missing field %s" % (where, e))
    sect = ('<w:sectPr><w:footerReference w:type="default" r:id="rIdFooter1"/><w:pgSz w:w="%d" w:h="%d"/>'
            '<w:pgMar w:top="%d" w:right="%d" w:bottom="%d" w:left="%d" w:header="360" w:footer="360" w:gutter="0"/></w:sectPr>'
            % (PAGE_W, PAGE_H, MARGIN, MARGIN, MARGIN, MARGIN))
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document %s %s %s %s %s><w:body>%s%s</w:body></w:document>'
            % (NS_W, NS_R, NS_WP, NS_A, NS_C, "".join(body), sect))


FOOTER = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr %s><w:p><w:pPr><w:jc w:val="right"/></w:pPr>'
          '<w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
          '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>1</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r>'
          '</w:p></w:ftr>' % NS_W)

STYLES = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles %s><w:docDefaults><w:rPrDefault><w:rPr>'
          '<w:rFonts w:ascii="Calibri" w:eastAsia="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/><w:sz w:val="22"/><w:szCs w:val="22"/>'
          '<w:lang w:val="en-US"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:after="0" w:line="264" w:lineRule="auto"/>'
          '</w:pPr></w:pPrDefault></w:docDefaults><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/>'
          '<w:qFormat/></w:style><w:style w:type="table" w:default="1" w:styleId="TableNormal"><w:name w:val="Normal Table"/>'
          '<w:semiHidden/><w:tblPr><w:tblInd w:w="0" w:type="dxa"/><w:tblCellMar><w:top w:w="0" w:type="dxa"/>'
          '<w:left w:w="108" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr>'
          '</w:style></w:styles>' % NS_W)


def build(spec, out):
    charts = Charts()
    doc = document_xml(spec, charts)
    meta = spec["meta"]
    if os.path.isdir(out) or out.endswith(("/", "\\")):
        os.makedirs(out, exist_ok=True)
        out = os.path.join(out, "%s earnings update %s.docx" % (meta["ticker_short"], meta["period"]))
    ct = ['<Override PartName="/word/charts/%s" ContentType="application/vnd.openxmlformats-officedocument.drawingml.chart+xml"/>' % n
          for n, _ in charts.parts]
    content_types = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                     '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                     '<Default Extension="xml" ContentType="application/xml"/>'
                     '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
                     '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
                     '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
                     '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
                     '%s</Types>' % "".join(ct))
    rels = ['<Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>',
            '<Relationship Id="rIdFooter1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>']
    rels += ['<Relationship Id="rIdChart%d" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/chart" Target="charts/%s"/>'
             % (k + 1, n) for k, (n, _) in enumerate(charts.parts)]
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    core = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<dc:title>%s</dc:title><dc:creator>%s</dc:creator><dcterms:created xsi:type="dcterms:W3CDTF">%s</dcterms:created>'
            '<dcterms:modified xsi:type="dcterms:W3CDTF">%s</dcterms:modified></cp:coreProperties>'
            % (escape("%s earnings update %s" % (meta["ticker_short"], meta["period"])), escape(meta.get("author", "Opal Capital")), now, now))
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
                   '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/></Relationships>')
        z.writestr("word/document.xml", doc)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/footer1.xml", FOOTER)
        z.writestr("word/_rels/document.xml.rels", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">%s</Relationships>' % "".join(rels))
        z.writestr("docProps/core.xml", core)
        for name, xml in charts.parts:
            z.writestr("word/charts/" + name, xml)
    return out, len(charts.parts)


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as f:
        spec = json.load(f)
    try:
        path, n = build(spec, argv[2])
    except SpecError as e:
        print("ERROR: %s" % e)
        return 2
    print("OK: %s (%d native charts)" % (os.path.abspath(path), n))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
