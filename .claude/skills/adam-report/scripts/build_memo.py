#!/usr/bin/env python3
"""Build an Opal Capital investment memo (.docx) from a memo JSON spec. Python 3.8+ standard library only.

    python build_memo.py memo.json "<out dir or .docx path>"

The layout reproduces the house memo (T-Mobile US, Adam Muller, 2026-10-13): US Letter landscape, Calibri 10pt
body, navy/teal banner, ruled section heads, 7.5pt financial tables, teal italics for Opal-derived figures, and a
"Page X of Y" footer. The spec format is in ../references/memo_spec.md; ../references/example_tmus.json is a full
worked example. Exit 0 prints "OK: <path>"; a spec error exits 2 naming the block.
"""
import datetime
import json
import os
import re
import sys
import zipfile
from xml.sax.saxutils import escape

NAVY, TEAL, GREY, BLACK, WHITE, PALE = "0E2841", "156082", "595959", "000000", "FFFFFF", "BFD7E3"
HEAD_FILL, LIGHT_FILL, HIGHLIGHT_FILL, RULE = "0E2841", "E8EEF2", "EAF3F7", "BFC9D1"
TEXT_WIDTH = 14256  # twips between the 792-twip side margins of a landscape Letter page

W_NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')


class SpecError(Exception):
    pass


def _t(text):
    """Text runs: a newline becomes a line break."""
    parts = str(text).split("\n")
    out = []
    for i, p in enumerate(parts):
        if i:
            out.append("<w:br/>")
        out.append('<w:t xml:space="preserve">%s</w:t>' % escape(p))
    return "".join(out)


def run(text, color=BLACK, bold=False, italic=False, size=None):
    rpr = ("<w:b/>" if bold else "") + ("<w:i/>" if italic else "") + '<w:color w:val="%s"/>' % color
    if size:
        rpr += '<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (size, size)
    return "<w:r><w:rPr>%s</w:rPr>%s</w:r>" % (rpr, _t(text))


def para(runs, ppr=""):
    return "<w:p><w:pPr>%s</w:pPr>%s</w:p>" % (ppr, "".join(runs))


def rich(text, color=BLACK, size=None):
    """Inline markup inside prose: **bold navy** and _teal italic (Opal-derived)_."""
    out = []
    for tok in re.split(r"(\*\*.+?\*\*|(?<![\w])_[^_]+?_(?![\w]))", str(text)):
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**"):
            out.append(run(tok[2:-2], NAVY, bold=True, size=size))
        elif tok.startswith("_") and tok.endswith("_") and len(tok) > 2:
            out.append(run(tok[1:-1], TEAL, italic=True, size=size))
        else:
            out.append(run(tok, color, size=size))
    return out


# ---------------------------------------------------------------- blocks

def b_banner(meta):
    line1 = para([run("  OPAL CAPITAL", WHITE, bold=True), run("   |   Investment Memo", PALE)],
                 '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % NAVY)
    name = "  %s (%s: %s)" % (meta["company"], meta["exchange"], meta["ticker"])
    line2 = para([run(name, WHITE, bold=True)], '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % NAVY)
    sub = "  %s  |  %s  |  Prepared by %s, %s" % (meta["industry"], meta["hq"], meta["author"], meta["date"])
    line3 = para([run(sub, WHITE)], '<w:shd w:val="clear" w:color="auto" w:fill="%s"/><w:spacing w:after="100"/>' % TEAL)
    return line1 + line2 + line3


def b_section(blk):
    return para([run(blk["text"].upper(), NAVY, bold=True)],
                '<w:keepNext/><w:pBdr><w:bottom w:val="single" w:sz="10" w:space="2" w:color="%s"/></w:pBdr>'
                '<w:spacing w:before="110" w:after="50"/>' % TEAL)


def b_subhead(blk):
    return para([run(blk["text"], NAVY, bold=True)], '<w:keepNext/><w:spacing w:before="140" w:after="30"/>')


def b_label(blk):
    return para([run(blk["text"], GREY, bold=True)], '<w:keepNext/><w:spacing w:after="30"/>')


def b_notes(blk):
    out = []
    for item in blk["items"]:
        out.append(para([run("\u2022 ", GREY)] + rich(item, GREY),
                        '<w:spacing w:after="20"/><w:ind w:left="180" w:hanging="180"/>'))
    return "".join(out)


def b_para(blk):
    return para(rich(blk["text"]), '<w:spacing w:after="60" w:line="232" w:lineRule="auto"/>')


def b_findings(blk):
    """'What the data shows' paragraphs: a bold navy lead ending in a colon, then the finding."""
    out = []
    for item in blk["items"]:
        lead = item["lead"].rstrip()
        if not lead.endswith(":"):
            lead += ":"
        out.append(para([run(lead + " ", NAVY, bold=True)] + rich(item["text"]),
                        '<w:spacing w:before="20" w:after="20"/><w:ind w:left="180" w:hanging="180"/>'))
    return "".join(out)


def b_bullets(blk):
    """Thesis / risks / management / questions: teal square, bold navy lead sentence, then body."""
    out = []
    for item in blk["items"]:
        lead = item["lead"].rstrip() + " "
        runs = [run("\u25a0", TEAL, size=12), '<w:r><w:rPr><w:color w:val="%s"/><w:sz w:val="12"/></w:rPr><w:tab/></w:r>' % TEAL,
                run(lead, NAVY, bold=True)] + rich(item["text"])
        out.append(para(runs, '<w:tabs><w:tab w:val="left" w:pos="260"/></w:tabs>'
                              '<w:spacing w:after="25" w:line="232" w:lineRule="auto"/><w:ind w:left="260" w:hanging="260"/>'))
    return "".join(out)


def _cell_xml(width, content_runs, align, fill=None, span=1, pad=25):
    borders = ('<w:tcBorders><w:top w:val="single" w:sz="2" w:space="0" w:color="%s"/>'
               '<w:left w:val="none" w:sz="0" w:space="0" w:color="FFFFFF"/>'
               '<w:bottom w:val="single" w:sz="2" w:space="0" w:color="%s"/>'
               '<w:right w:val="none" w:sz="0" w:space="0" w:color="FFFFFF"/></w:tcBorders>' % (RULE, RULE))
    tcpr = '<w:tcW w:w="%d" w:type="dxa"/>' % width
    if span > 1:
        tcpr += '<w:gridSpan w:val="%d"/>' % span
    tcpr += borders
    if fill:
        tcpr += '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % fill
    tcpr += ('<w:tcMar><w:top w:w="%d" w:type="dxa"/><w:left w:w="50" w:type="dxa"/><w:bottom w:w="%d" w:type="dxa"/>'
             '<w:right w:w="50" w:type="dxa"/></w:tcMar><w:vAlign w:val="center"/>' % (pad, pad))
    ppr = '<w:jc w:val="%s"/>' % align if align != "left" else ""
    return "<w:tc><w:tcPr>%s</w:tcPr><w:p><w:pPr>%s</w:pPr>%s</w:p></w:tc>" % (tcpr, ppr, "".join(content_runs))


def _norm_cell(c):
    if isinstance(c, dict):
        return dict(c)
    return {"t": "" if c is None else str(c)}


# Cell style tokens -> (color, bold, italic). "teal" is the house mark for an Opal-derived figure.
STYLES_TOK = {"plain": (BLACK, False, False), "bold": (BLACK, True, False), "navy": (NAVY, True, False),
              "teal": (TEAL, False, True), "tealb": (TEAL, True, True), "grey": (GREY, False, True),
              "greyp": (GREY, False, False), "head": (WHITE, True, False), "headl": (GREY, False, False)}
FILLS = {"navy": HEAD_FILL, "light": LIGHT_FILL, "highlight": HIGHLIGHT_FILL, "none": None}

# Row kinds -> (label style, value style, derived-value style, row fill)
ROW_KINDS = {"": ("plain", "plain", "teal", None), "bold": ("bold", "plain", "teal", None),
             "strong": ("bold", "bold", "tealb", None),
             "sub": ("grey", "teal", "teal", None), "total": ("bold", "bold", "tealb", "light"),
             "highlight": ("navy", "bold", "tealb", "highlight"), "median": ("tealb", "teal", "teal", None),
             "key": ("navy", "navy", "navy", None)}


def infer_cell(blk, row, ri, ci, col):
    """The (style, fill, align) a cell gets when it carries no override. Shared with the converter."""
    header_rows = blk.get("header_rows", 1)
    ncols = len(blk["widths"])
    if ri < header_rows:
        light = blk.get("header_style") == "light"
        fill = "light" if light else "navy"
        for c in blk.get("gap_cols", []):
            if col == c:
                fill = "none"
        align = "center" if (light or ci) else "left"
        if not light and ci and blk.get("align"):
            align = blk["align"][col] if blk["align"][col] != "left" else "center"
        return ("headl" if light else "head"), fill, align
    kind = row.get("kind", "")
    lab, val, der, rfill = ROW_KINDS[kind]
    if ci == 0:
        style = lab
    else:
        style = der if row.get("derived") else val
        cs = blk.get("col_styles", {}).get(str(col))
        if cs and kind in ("", "bold", "strong", "total"):
            style = {"teal": "tealb", "plain": "bold"}.get(cs, cs) if kind in ("strong", "total") else cs
    fill = rfill
    cf = blk.get("col_fills", {})
    if str(col) in cf and fill is None:
        fill = cf[str(col)]
    if col in blk.get("gap_cols", []):
        fill = None
    align = (blk.get("align") or (["left"] + ["right"] * (ncols - 1)))[col]
    return style, fill, align


def b_table(blk, where):
    rows = blk.get("rows") or []
    if not rows:
        raise SpecError("%s: table has no rows" % where)
    size = blk.get("size", 15)          # half-points: 15 = 7.5pt (financial tables); null = body 10pt
    header_rows = blk.get("header_rows", 1)
    ncols = blk.get("ncols") or max(sum(_norm_cell(c).get("span", 1) for c in (r["cells"] if isinstance(r, dict) else r)) for r in rows)
    widths = blk.get("widths")
    if not widths:
        first = blk.get("first_col", 0)
        if first:
            rest = (TEXT_WIDTH - first) // max(ncols - 1, 1)
            widths = [first] + [rest] * (ncols - 1)
        else:
            widths = [TEXT_WIDTH // ncols] * ncols
        blk = dict(blk, widths=widths)
    if len(widths) != ncols:
        raise SpecError("%s: %d widths for %d columns" % (where, len(widths), ncols))
    if blk.get("align") and len(blk["align"]) != ncols:
        raise SpecError("%s: %d align entries for %d columns" % (where, len(blk["align"]), ncols))
    pad = blk.get("pad", 25 if size is None else 0)
    grid = "".join('<w:gridCol w:w="%d"/>' % w for w in widths)
    out = ['<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="center"/><w:tblLayout w:type="fixed"/>'
           '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>'
           '</w:tblPr><w:tblGrid>%s</w:tblGrid>' % (sum(widths), grid)]
    for ri, r in enumerate(rows):
        row = r if isinstance(r, dict) else {"cells": r}
        if row.get("kind", "") not in ROW_KINDS:
            raise SpecError("%s row %d: unknown kind %r" % (where, ri, row.get("kind")))
        cells = [_norm_cell(c) for c in row["cells"]]
        is_head = ri < header_rows
        trpr = "<w:cantSplit/>" + ("<w:tblHeader/>" if is_head else "") + '<w:jc w:val="center"/>'
        tr = ["<w:tr><w:trPr>%s</w:trPr>" % trpr]
        col = 0
        for ci, c in enumerate(cells):
            span = int(c.get("span", 1))
            if col + span > ncols:
                raise SpecError("%s row %d: cells overflow %d columns" % (where, ri, ncols))
            style, fill, align = infer_cell(blk, row, ri, ci, col)
            if c.get("d"):
                style = "tealb" if style in ("bold", "tealb") else "teal"
            style = c.get("s", style)
            if style not in STYLES_TOK:
                raise SpecError("%s row %d: unknown style %r" % (where, ri, style))
            fill = FILLS.get(c.get("fill", fill), c.get("fill", fill)) if c.get("fill", fill) else None
            align = c.get("align", align)
            color, bold, italic = STYLES_TOK[style]
            lines = str(c.get("t", "")).split("\n")
            runs = [run(lines[0], color, bold, italic, size)] if lines[0] else []
            for extra in lines[1:]:   # a name cell's ticker / price lines: grey 8pt
                runs.append('<w:r><w:rPr><w:color w:val="%s"/><w:sz w:val="16"/></w:rPr><w:br/>'
                            '<w:t xml:space="preserve">%s</w:t></w:r>' % (GREY, escape(extra)))
            tr.append(_cell_xml(sum(widths[col:col + span]), runs, align, fill, span, pad))
            col += span
        for k in range(col, ncols):
            style, fill, align = infer_cell(blk, row, ri, k, k)
            tr.append(_cell_xml(widths[k], [], align, FILLS.get(fill, fill) if fill else None, 1, pad))
        tr.append("</w:tr>")
        out.append("".join(tr))
    out.append("</w:tbl>")
    out.append(para([], '<w:spacing w:after="40"/>'))
    return "".join(out)


def b_pagebreak(blk):
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


BLOCKS = {"pagebreak": b_pagebreak, "section": b_section, "subhead": b_subhead, "label": b_label, "notes": b_notes, "para": b_para,
          "findings": b_findings, "bullets": b_bullets}


# ---------------------------------------------------------------- package

def document_xml(spec):
    meta = spec["meta"]
    for k in ("company", "exchange", "ticker", "industry", "hq", "author", "date"):
        if not meta.get(k):
            raise SpecError("meta.%s is required" % k)
    body = [b_banner(meta)]
    for i, blk in enumerate(spec.get("blocks", [])):
        kind = blk.get("type")
        where = "blocks[%d] (%s)" % (i, kind)
        if kind == "table":
            body.append(b_table(blk, where))
        elif kind in BLOCKS:
            try:
                body.append(BLOCKS[kind](blk))
            except KeyError as e:
                raise SpecError("%s: missing field %s" % (where, e))
        else:
            raise SpecError("%s: unknown block type" % where)
    sect = ('<w:sectPr><w:footerReference w:type="default" r:id="rIdFooter1"/>'
            '<w:pgSz w:w="15840" w:h="12240" w:orient="landscape"/>'
            '<w:pgMar w:top="560" w:right="792" w:bottom="560" w:left="792" w:header="720" w:footer="300" w:gutter="0"/>'
            '</w:sectPr>')
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document %s><w:body>%s%s</w:body></w:document>'
            % (W_NS, "".join(body), sect))


def footer_xml(meta):
    title = meta.get("footer_title") or "%s Investment Memo" % meta.get("short_name", meta["company"])

    def fld(code):
        return ('<w:r><w:rPr><w:color w:val="%s"/><w:sz w:val="14"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>'
                '<w:r><w:rPr><w:color w:val="%s"/><w:sz w:val="14"/></w:rPr><w:instrText xml:space="preserve"> %s </w:instrText></w:r>'
                '<w:r><w:rPr><w:color w:val="%s"/><w:sz w:val="14"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r>'
                '<w:r><w:rPr><w:color w:val="%s"/><w:sz w:val="14"/></w:rPr><w:t>1</w:t></w:r>'
                '<w:r><w:rPr><w:color w:val="%s"/><w:sz w:val="14"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r>'
                % (GREY, GREY, code, GREY, GREY, GREY))
    p = ('<w:p><w:pPr><w:jc w:val="center"/></w:pPr>%s%s%s%s</w:p>'
         % (run("Opal Capital  |  %s  |  Internal use only  |  Page " % title, GREY, size=14), fld("PAGE"),
            run(" of ", GREY, size=14), fld("NUMPAGES")))
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr %s>%s</w:ftr>' % (W_NS, p)


STYLES = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
          '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:eastAsia="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>'
          '<w:sz w:val="20"/><w:szCs w:val="20"/><w:lang w:val="en-US"/></w:rPr></w:rPrDefault>'
          '<w:pPrDefault><w:pPr><w:spacing w:after="200" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'
          '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/>'
          '<w:pPr><w:spacing w:after="0"/></w:pPr><w:rPr><w:rFonts w:ascii="Calibri" w:eastAsia="Calibri" w:hAnsi="Calibri"/>'
          '<w:sz w:val="20"/></w:rPr></w:style>'
          '<w:style w:type="table" w:default="1" w:styleId="TableNormal"><w:name w:val="Normal Table"/><w:semiHidden/>'
          '<w:tblPr><w:tblInd w:w="0" w:type="dxa"/><w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/>'
          '<w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>'
          '</w:styles>')

CONTENT_TYPES = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                 '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                 '<Default Extension="xml" ContentType="application/xml"/>'
                 '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
                 '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
                 '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
                 '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
                 '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
                 '</Types>')

ROOT_RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
             '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
             '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
             '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>'
             '</Relationships>')

DOC_RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rIdStyles" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
            '<Relationship Id="rIdFooter1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>'
            '</Relationships>')


def core_xml(meta):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    title = "%s Investment Memo" % meta["company"]
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            '<dc:title>%s</dc:title><dc:creator>%s</dc:creator>'
            '<dcterms:created xsi:type="dcterms:W3CDTF">%s</dcterms:created>'
            '<dcterms:modified xsi:type="dcterms:W3CDTF">%s</dcterms:modified></cp:coreProperties>'
            % (escape(title), escape(meta["author"]), now, now))


APP = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
       '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">'
       '<Application>Opal report-gen</Application></Properties>')


def default_name(meta):
    safe = re.sub(r"[^A-Za-z0-9-]+", "_", meta.get("short_name") or meta["company"]).strip("_")
    d = meta.get("file_date") or datetime.date.today().strftime("%Y_%m_%d")
    return "%s_Investment_Memo_%s.docx" % (safe, d)


def build(spec, out):
    doc = document_xml(spec)
    meta = spec["meta"]
    if os.path.isdir(out) or out.endswith(("/", "\\")):
        os.makedirs(out, exist_ok=True)
        out = os.path.join(out, default_name(meta))
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", ROOT_RELS)
        z.writestr("word/document.xml", doc)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/footer1.xml", footer_xml(meta))
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("docProps/core.xml", core_xml(meta))
        z.writestr("docProps/app.xml", APP)
    return out


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as f:
        spec = json.load(f)
    try:
        path = build(spec, argv[2])
    except SpecError as e:
        print("ERROR: %s" % e)
        return 2
    print("OK: %s" % os.path.abspath(path))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
