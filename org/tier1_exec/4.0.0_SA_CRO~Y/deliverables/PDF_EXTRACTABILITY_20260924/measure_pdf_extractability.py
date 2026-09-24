"""PDF extractability of the research corpus skeleton -- 4.0.0_SA_CRO~Y, 2026-09-24.

Andrew-direct "Begin with PDF Extractibility" (record ANDREW_DIRECT_20260924_030xZ_...).
Answers the dossier brief's O7 / Part VIII-5: can the Class A / B skeleton (INVESTMENT
THESIS pillars, RISKS, MANAGEMENT/BOARD, RECOMMENDATION, the three cases) be read from the
PDF packs to the same shape the ruled docx path reads, for every PDF under the 93 folders.

READ-ONLY over the synced library (C-CORPUS-READ-ONLY): every file is opened 'rb'; nothing
is written, moved or deleted under the root. Reading a OneDrive placeholder hydrates it
(a download), which the ingest cell also does; the count is printed, not hidden.

Reuses the estate's own rules, never a parallel one:
  - extract._pdf_page_lines / the size-or-bold heading heuristic (extract.py:229-285)
  - extract._extract_docx + continuation._thesis_pillar_paragraphs for the docx side
    (the RULED pillar rule) -- the POSITIVE CONTROL's expected value.
The PDF pillar rule under test is stated in pdf_pillars() and is the candidate for the
addendum; it is graded here against the docx rule on every docx+pdf pair of the same stem.

Output (this folder): per_file.json, summary.json, and the printed summary.
"""
from __future__ import annotations

import json
import os
import re
import statistics
import sys
from collections import Counter, defaultdict

import fitz  # PyMuPDF, already installed (extract.py uses it)

from lib.research.corpus import library
from lib.research.corpus import extract as ex
from lib.research.corpus import continuation as cont

PLACEHOLDER_BIT = 0x400000  # FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS
HEAD_CAP = ex._HEADING_WORD_CAP
SIZE_RATIO = ex._PDF_SIZE_RATIO
BOLD_BIT = ex._PDF_BOLD_FLAG_BIT
PILLAR_RE = cont._PILLAR_LEAD_RE
# VARIANT under test: the ruled docx regex caps a lead at 80 characters; the PFOE author's leads run
# longer ("Leading position in chip design software and IP with a strong and defensible moat", 84).
PILLAR_RE_WIDE = re.compile(r"^([A-Z][^:]{2,140}?):\s*(.+)$")

SKELETON = {
    "INVESTMENT THESIS": ("INVESTMENT THESIS",),
    "RISKS": ("RISKS AND CONSIDERATIONS", "RISKS AND CONSDIERATIONS", "RISKS", "HEADWINDS AND RISKS",
              "KEY RISKS AND CONSIDERATIONS", "KEY RISKS AND CONSDIERATIONS", "KEY RISKS"),
    "MANAGEMENT": ("MANAGEMENT/BOARD", "MANAGEMENT / BOARD", "MANAGEMENT", "MANAGEMENT-BOARD",
                   "MANAGEMENT AND CAPITAL ALLOCATION"),
    "RECOMMENDATION": ("RECOMMENDATION",),
    "CASES": ("UPSIDE CASE", "BASE CASE", "DOWNSIDE CASE"),
    "CSC": ("COMMON STOCK COMPARISON",),
    "FINANCIAL SUMMARY": ("FINANCIAL SUMMARY",),
    "HEADLINE RESULTS": ("HEADLINE RESULTS", "HEADLINE NUMBERS"),
    "GUIDANCE": ("GUIDANCE",),
    "SEGMENT HIGHLIGHTS": ("SEGMENT HIGHLIGHTS",),
    "PERFORMANCE VS FUND": ("PERFORMANCE VS FUND",),
    # MEASURED 2026-09-24 on the PFOE author's "Research Note" packs and earnings updates (CDNS, NFLX,
    # ASML, INTU): section labels are INLINE BOLD LEADS on body lines, not standalone headings.
    "COMPANY DESCRIPTION": ("COMPANY DESCRIPTION",),
    "GROWTH ALGORITHM": ("LONG-TERM GROWTH ALGORITHM AND EXPECTED RETURN", "LONG-TERM GROWTH ALGORITHM"),
    "OWNERSHIP": ("OWNERSHIP",),
    "SPECIAL ITEMS": ("SPECIAL ITEMS",),
    "WHY WE OWN": ("WHY WE OWN",),
    "POSITIVES": ("POSITIVES",),
    "NEGATIVES": ("NEGATIVES",),
    "ANALYST SENTIMENT": ("CHANGES IN ANALYST SENTIMENT",),
    "INVESTMENT CONSIDERATIONS": ("INVESTMENT CONSIDERATIONS",),
    "OPPOSING VIEW": ("OPPOSING VIEW",),
}


def norm(t):
    return re.sub(r"\s+", " ", (t or "").strip()).rstrip(":").strip().upper()


def pdf_lines(body):
    """Flat line list across pages, each with its spans kept: {text, page, size, bold_all,
    bold_first, lead_prefix (concatenated leading bold spans' text), spans}."""
    doc = fitz.open(stream=body, filetype="pdf")
    out = []
    text_chars = 0
    try:
        for pi in range(doc.page_count):
            page = doc[pi]
            text_chars += len(page.get_text("text"))
            d = page.get_text("dict")
            page_lines = []
            for block in d.get("blocks", []) or []:
                for line in block.get("lines", []) or []:
                    spans = []
                    for sp in line.get("spans", []) or []:
                        t = sp.get("text", "") or ""
                        if not t.strip():
                            continue
                        flags = int(sp.get("flags", 0) or 0)
                        font = (sp.get("font", "") or "").lower()
                        bold = bool(flags & BOLD_BIT) or ("bold" in font)
                        spans.append({"t": t, "b": bold, "s": float(sp.get("size", 0.0) or 0.0)})
                    if not spans:
                        continue
                    text = "".join(s["t"] for s in spans).strip()
                    if not text:
                        continue
                    lead = ""
                    for s in spans:
                        if s["b"]:
                            lead += s["t"]
                        else:
                            break
                    page_lines.append({
                        "text": text, "page": pi,
                        "size": max(s["s"] for s in spans),
                        "bold_all": all(s["b"] for s in spans),
                        "bold_first": spans[0]["b"],
                        "lead_prefix": lead.strip(),
                        "n_spans": len(spans),
                    })
            sizes = [ln["size"] for ln in page_lines if ln["size"] > 0]
            med = statistics.median(sizes) if sizes else 0.0
            for ln in page_lines:
                wc = len(ln["text"].split())
                large = med > 0 and ln["size"] > SIZE_RATIO * med
                ln["heading"] = (0 < wc <= HEAD_CAP) and (large or ln["bold_all"])
                out.append(ln)
        return out, doc.page_count, text_chars
    finally:
        doc.close()


def section_name_of(ln):
    """The section name this line OPENS, or None. Two shapes, both measured: a standalone heading
    (all-bold or large, the whole line is the name) and an INLINE lead (the leading bold spans are
    the name followed by ':' and body text on the same line -- the PFOE author's packs)."""
    if ln["heading"] or ln["bold_all"]:
        n = norm(ln["text"])
        if n in ALL_SECTION_NAMES:
            return n
    lp = norm(ln["lead_prefix"])
    if lp and lp in ALL_SECTION_NAMES and ln["bold_first"]:
        return lp
    return None


def find_heading(lines, names, start=0):
    for i in range(start, len(lines)):
        s = section_name_of(lines[i])
        if s is not None and s in names:
            return i
    return None


def inline_remainder(ln):
    """Body text on the same line after an inline section lead's colon (the one-sentence summary the
    PFOE packs put after 'INVESTMENT THESIS:'), or ''."""
    t = ln["text"]
    return t.split(":", 1)[1].strip() if ":" in t else ""


# MEASURED 2026-09-24: 'Valuation' is a PILLAR lead in the Word-author packs (BB Seguridade, Petrobras:
# the last of seven), so it is NOT a section name here; only names the heading censuses carry are.
ALL_SECTION_NAMES = frozenset(n for names in SKELETON.values() for n in names) | frozenset({
    "OTHER POSITIVES", "OTHER NEGATIVES", "SEGMENTS", "COMPANY OVERVIEW",
    "INVESTMENT CONSIDERATIONS", "MANAGEMENT/BOARD 80", "INVESTMENT THESIS 250", "COMPANY OVERVIEW (250)",
    "INVESTMENT CONSIDERATIONS 100", "HEADWINDS AND RISKS", "GEOGRAPHIC HIGHLIGHTS", "BROKER COMMENTARY",
    "TRADING HISTORY", "EARNINGS ESTIMATE PROGRESSION", "HISTORICAL VALUATION", "PRICE CHART",
})


def is_section_heading(ln):
    """A known section name opens on this line (standalone heading OR inline bold lead).
    MEASURED 2026-09-24: the team's PDF headings carry a trailing colon ('RISKS AND CONSDIERATIONS:'),
    which the first version of this rule read as a pillar lead -- every 'extra' pillar in the positive
    control was a RISKS item. A named section closes the block whatever punctuation follows it."""
    return section_name_of(ln) is not None


def block_after(lines, i):
    """Lines after heading i until the next SECTION heading. A short all-bold line ending in ':' that
    is NOT a known section name is a pillar lead on its own line and stays inside the block; an
    unnamed large/bold heading (a chart title, a page header) also closes the block."""
    out = []
    for j in range(i + 1, len(lines)):
        ln = lines[j]
        if is_section_heading(ln):
            break
        if ln["heading"] and not _looks_like_lead_only(ln):
            break
        out.append(ln)
    return out


def _looks_like_lead_only(ln):
    # An all-bold short line ending with ':' is a pillar lead on its own line, not a section heading.
    return ln["bold_all"] and ln["text"].rstrip().endswith(":")


def pdf_pillars(lines, wide=False):
    """CANDIDATE PDF PILLAR RULE (under test; wide=True uses the 140-char lead cap):
    block = lines after the INVESTMENT THESIS heading up to the next section heading;
    a pillar starts at a line whose LEADING BOLD SPANS end at a colon (lead_prefix matches
    '^<Lead>:' or lead_prefix + ':' opens the line) OR an all-bold line ending in ':';
    its body is the non-bold remainder of that line plus following non-heading, non-lead lines.
    Returns None when no INVESTMENT THESIS heading exists; else the list of (lead, body)."""
    i = find_heading(lines, SKELETON["INVESTMENT THESIS"])
    if i is None:
        return None
    blk = block_after(lines, i)
    pillars = []
    cur = None
    rx = PILLAR_RE_WIDE if wide else PILLAR_RE
    # An INLINE 'INVESTMENT THESIS: <summary>' lead: the summary sentence continues on the following
    # non-lead lines and is not a pillar; it is recorded by the caller as thesis_summary.
    for ln in blk:
        text = ln["text"].lstrip("•-– ").strip()
        lead = ln["lead_prefix"].lstrip("•-– ").strip()
        is_lead = False
        lead_txt = ""
        body = ""
        if lead:
            m = rx.match(text)
            if m and lead.rstrip(":").strip() and text.startswith(lead) and m.group(1).strip().startswith(lead.rstrip(":").strip()[: max(3, len(lead.rstrip(':').strip()) - 1)]):
                is_lead = True
                lead_txt = m.group(1).strip()
                body = m.group(2).strip()
            elif text.endswith(":") and (ln["bold_all"] or norm(text) == norm(lead)):
                # A lead alone on its line (all bold, or bold up to a NON-BOLD colon -- the PFOE
                # shape, measured on CDNS's second pillar): the body follows on the lines below.
                is_lead = True
                lead_txt = text.rstrip(":").strip()
                body = ""
        if is_lead and norm(lead_txt) in ALL_SECTION_NAMES:
            is_lead = False  # a section label is never a pillar
        if is_lead:
            if cur:
                pillars.append(cur)
            cur = {"lead": lead_txt, "body": body, "page": ln["page"]}
        elif cur is not None:
            cur["body"] = (cur["body"] + " " + text).strip()
    if cur:
        pillars.append(cur)
    return pillars


def thesis_summary(lines):
    i = find_heading(lines, SKELETON["INVESTMENT THESIS"])
    if i is None:
        return None
    ln = lines[i]
    if ln["heading"] or ln["bold_all"]:
        return ""  # standalone heading: no inline summary (the Word-author shape)
    s = inline_remainder(ln)
    for j in range(i + 1, min(i + 6, len(lines))):
        nxt = lines[j]
        if nxt["bold_first"] or nxt["heading"]:
            break
        s = (s + " " + nxt["text"]).strip()
    return s[:300]


def pdf_section(lines, key):
    i = find_heading(lines, SKELETON[key])
    if i is None:
        return None
    blk = block_after(lines, i)
    return {"page": lines[i]["page"], "lines": len(blk), "chars": sum(len(ln["text"]) for ln in blk)}


def pdf_recommendation(lines):
    for i, ln in enumerate(lines):
        n = norm(ln["text"])
        if n.startswith("RECOMMENDATION") and (ln["bold_first"] or ln["heading"] or n.startswith("RECOMMENDATION:")):
            rest = ln["text"].split(":", 1)[1].strip() if ":" in ln["text"] else ""
            if not rest:
                for j in range(i + 1, min(i + 4, len(lines))):
                    if lines[j]["text"].strip():
                        rest = lines[j]["text"].strip()
                        break
            return {"page": ln["page"], "text": rest[:160]}
    return None


def pdf_cases(lines):
    found = set()
    for ln in lines:
        n = norm(ln["text"])
        for c in SKELETON["CASES"]:
            if c in n:
                found.add(c)
    return sorted(found)


def classify_pdf(lines, fname):
    fl = fname.lower()
    if "stock move" in fl:
        return "D"
    if find_heading(lines, SKELETON["INVESTMENT THESIS"]) is not None:
        return "A"
    for ln in lines:
        n = norm(ln["text"])
        if n.startswith("RECOMMENDATION: MAINTAIN") or n in SKELETON["HEADLINE RESULTS"]:
            return "B"
    if re.search(r"earnings update|q[1-4]|[1-4]q\d\d|quarter", fl):
        return "B?"
    return "OTHER"


def docx_leads(body):
    paragraphs, headings, tables = ex._extract_docx(body)
    doc = {"type": "docx", "extractable": True, "paragraphs": paragraphs}
    p = cont._thesis_pillar_paragraphs(doc)
    if p is None:
        return None
    return [lead for (_j, lead, _body, _full) in p]


def key_lead(s):
    return re.sub(r"\s+", " ", s or "").strip().rstrip(":").strip().casefold()


def main():
    root = library.library_root()
    folders = library.list_folders(root)
    per_file = []
    placeholders_before = 0
    read_failed = 0
    docx_by_stem = {}
    pdf_by_stem = {}
    for f in folders:
        fdir = os.path.join(root, f)
        for name in sorted(os.listdir(fdir)):
            path = os.path.join(fdir, name)
            if not os.path.isfile(path):
                continue
            ext = os.path.splitext(name)[1].lower()
            if ext not in (".pdf", ".docx"):
                continue
            st = os.stat(path, follow_symlinks=False)
            ph = bool(getattr(st, "st_file_attributes", 0) & PLACEHOLDER_BIT)
            placeholders_before += int(ph)
            try:
                with open(path, "rb") as fh:
                    body = fh.read()
            except OSError as e:
                read_failed += 1
                per_file.append({"folder": f, "file": name, "type": ext[1:], "read_failed": str(e)[:120]})
                continue
            stem = os.path.splitext(name)[0]
            rec = {"folder": f, "file": name, "type": ext[1:], "bytes": len(body), "placeholder_before": ph}
            if ext == ".docx":
                try:
                    leads = docx_leads(body)
                    rec["docx_pillars"] = None if leads is None else len(leads)
                    rec["docx_leads"] = None if leads is None else [x[:100] for x in leads[:12]]
                except Exception as e:  # a measurement records the failure, never hides it
                    rec["error"] = "%s: %s" % (type(e).__name__, str(e)[:120])
                docx_by_stem[(f, stem)] = rec
            else:
                try:
                    lines, pages, chars = pdf_lines(body)
                    rec.update({"pages": pages, "text_chars": chars, "zero_text": chars == 0,
                                "lines": len(lines), "headings": sum(1 for ln in lines if ln["heading"]),
                                "bold_lines": sum(1 for ln in lines if ln["bold_first"])})
                    hits = {}
                    for k, names in SKELETON.items():
                        if k == "CASES":
                            continue
                        hits[k] = find_heading(lines, names) is not None
                    rec["skeleton_hits"] = hits
                    rec["class"] = classify_pdf(lines, name)
                    p = pdf_pillars(lines)
                    rec["pdf_pillars"] = None if p is None else len(p)
                    rec["pdf_leads"] = None if p is None else [x["lead"][:100] for x in p[:12]]
                    rec["pdf_pillar_body_chars"] = None if p is None else [len(x["body"]) for x in p[:12]]
                    pw = pdf_pillars(lines, wide=True)
                    rec["pdf_pillars_wide"] = None if pw is None else len(pw)
                    rec["pdf_leads_wide"] = None if pw is None else [x["lead"][:140] for x in pw[:12]]
                    rec["thesis_summary"] = thesis_summary(lines)
                    rec["risks"] = pdf_section(lines, "RISKS")
                    rec["management"] = pdf_section(lines, "MANAGEMENT")
                    rec["recommendation"] = pdf_recommendation(lines)
                    rec["cases"] = pdf_cases(lines)
                    for k in ("COMPANY DESCRIPTION", "GROWTH ALGORITHM", "OWNERSHIP", "SPECIAL ITEMS",
                              "WHY WE OWN", "POSITIVES", "NEGATIVES", "ANALYST SENTIMENT"):
                        rec["sec_" + k.lower().replace(" ", "_")] = pdf_section(lines, k) is not None
                except Exception as e:  # a measurement records the failure, never hides it
                    rec["error"] = "%s: %s" % (type(e).__name__, str(e)[:120])
                pdf_by_stem[(f, stem)] = rec
            per_file.append(rec)

    # ---- positive control: docx+pdf pairs of the same stem ----
    pairs = []
    for k, d in docx_by_stem.items():
        p = pdf_by_stem.get(k)
        if not p:
            continue
        exp = d.get("docx_leads")
        row = {"folder": k[0], "stem": k[1][:80], "docx_pillars": d.get("docx_pillars")}
        for suffix, got in (("", p.get("pdf_leads")), ("_wide", p.get("pdf_leads_wide"))):
            if exp is None:
                status = "DOCX_NO_THESIS_BLOCK"
                matched = None
            elif got is None:
                status = "PDF_NO_THESIS_HEADING"
                matched = 0
            else:
                ek = [key_lead(x) for x in exp]
                gk = [key_lead(x) for x in got]
                matched = sum(1 for x in ek if x in gk)
                status = "FULL" if matched == len(ek) and len(gk) == len(ek) else ("PARTIAL" if matched else "NONE")
            row["status" + suffix] = status
            row["matched" + suffix] = matched
            row["pdf_pillars" + suffix] = p.get("pdf_pillars" + suffix)
        pairs.append(row)

    # ---- folder classes (same rule as the census) ----
    fclass = {}
    for f in folders:
        exts = Counter(os.path.splitext(x)[1].lower() for x in os.listdir(os.path.join(root, f))
                       if os.path.isfile(os.path.join(root, f, x)))
        n = sum(exts.values())
        hd, hp = exts.get(".docx", 0) > 0, exts.get(".pdf", 0) > 0
        fclass[f] = ("EMPTY" if n == 0 else "DOCX+PDF" if hd and hp else "DOCX-ONLY" if hd
                     else "PDF-ONLY" if hp else "NO-PROSE")

    pdfs = [r for r in per_file if r.get("type") == "pdf" and "error" not in r and "read_failed" not in r]
    docxs = [r for r in per_file if r.get("type") == "docx"]
    by_fc = defaultdict(list)
    for r in pdfs:
        by_fc[fclass[r["folder"]]].append(r)

    def stat(rs):
        return {
            "pdfs": len(rs),
            "zero_text": sum(1 for r in rs if r["zero_text"]),
            "class_A": sum(1 for r in rs if r["class"] == "A"),
            "class_B": sum(1 for r in rs if r["class"].startswith("B")),
            "class_D": sum(1 for r in rs if r["class"] == "D"),
            "class_OTHER": sum(1 for r in rs if r["class"] == "OTHER"),
            "thesis_heading": sum(1 for r in rs if r["skeleton_hits"]["INVESTMENT THESIS"]),
            "pillars_ge1": sum(1 for r in rs if (r["pdf_pillars"] or 0) >= 1),
            "pillars_total": sum(r["pdf_pillars"] or 0 for r in rs),
            "pillars_ge1_wide": sum(1 for r in rs if (r.get("pdf_pillars_wide") or 0) >= 1),
            "pillars_total_wide": sum(r.get("pdf_pillars_wide") or 0 for r in rs),
            "risks_heading": sum(1 for r in rs if r["skeleton_hits"]["RISKS"]),
            "management_heading": sum(1 for r in rs if r["skeleton_hits"]["MANAGEMENT"]),
            "recommendation_line": sum(1 for r in rs if r["recommendation"]),
            "cases_all3": sum(1 for r in rs if len(r["cases"]) == 3),
            "any_skeleton_heading": sum(1 for r in rs if any(r["skeleton_hits"].values())),
            "thesis_summary_inline": sum(1 for r in rs if r.get("thesis_summary")),
            "company_description": sum(1 for r in rs if r.get("sec_company_description")),
            "growth_algorithm": sum(1 for r in rs if r.get("sec_growth_algorithm")),
            "ownership": sum(1 for r in rs if r.get("sec_ownership")),
            "why_we_own": sum(1 for r in rs if r.get("sec_why_we_own")),
            "positives_negatives": sum(1 for r in rs if r.get("sec_positives") and r.get("sec_negatives")),
        }

    # per PDF-only folder: does the folder's BEST pdf yield pillars / management / rec / cases
    pdf_only = [f for f in folders if fclass[f] == "PDF-ONLY"]
    folder_rows = []
    for f in pdf_only:
        rs = [r for r in pdfs if r["folder"] == f]
        folder_rows.append({
            "folder": f, "pdfs": len(rs),
            "has_class_A": any(r["class"] == "A" for r in rs),
            "pillars_max": max([r["pdf_pillars"] or 0 for r in rs] + [0]),
            "pillars_max_wide": max([r.get("pdf_pillars_wide") or 0 for r in rs] + [0]),
            "management": any(r["management"] for r in rs),
            "recommendation": any(r["recommendation"] for r in rs),
            "cases_all3": any(len(r["cases"]) == 3 for r in rs),
            "risks": any(r["risks"] for r in rs),
            "description": any(r.get("sec_company_description") for r in rs),
            "why_we_own": any(r.get("sec_why_we_own") for r in rs),
            "thesis_summary": any(r.get("thesis_summary") for r in rs),
        })

    summary = {
        "root": root, "folders": len(folders), "folder_classes": dict(Counter(fclass.values())),
        "files_read": {"pdf": len([r for r in per_file if r.get("type") == "pdf"]), "docx": len(docxs)},
        "placeholders_before": placeholders_before, "read_failed": read_failed,
        "errors": sum(1 for r in per_file if "error" in r),
        "all_pdfs": stat(pdfs),
        "by_folder_class": {k: stat(v) for k, v in sorted(by_fc.items())},
        "positive_control_pairs": {
            "pairs": len(pairs),
            "status_counts": dict(Counter(p["status"] for p in pairs)),
            "status_counts_wide": dict(Counter(p["status_wide"] for p in pairs)),
            "expected_pillars": sum(p["docx_pillars"] or 0 for p in pairs if p["docx_pillars"]),
            "matched_pillars": sum(p["matched"] or 0 for p in pairs),
            "matched_pillars_wide": sum(p["matched_wide"] or 0 for p in pairs),
        },
        "pdf_only_folders": {
            "folders": len(pdf_only),
            "with_class_A_pdf": sum(1 for r in folder_rows if r["has_class_A"]),
            "pillars_ge1": sum(1 for r in folder_rows if r["pillars_max"] >= 1),
            "management": sum(1 for r in folder_rows if r["management"]),
            "recommendation": sum(1 for r in folder_rows if r["recommendation"]),
            "cases_all3": sum(1 for r in folder_rows if r["cases_all3"]),
            "risks": sum(1 for r in folder_rows if r["risks"]),
            "description": sum(1 for r in folder_rows if r["description"]),
            "why_we_own": sum(1 for r in folder_rows if r["why_we_own"]),
            "thesis_summary": sum(1 for r in folder_rows if r["thesis_summary"]),
            "pillars_or_why_we_own": sum(1 for r in folder_rows if r["pillars_max"] >= 1 or r["why_we_own"]),
            "rows": folder_rows,
        },
        "pairs": pairs,
        "docx_with_pillars": sum(1 for r in docxs if (r.get("docx_pillars") or 0) >= 1),
        "docx_total": len(docxs),
    }
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "per_file.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(per_file, fh, indent=1)
    with open(os.path.join(here, "summary.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(summary, fh, indent=1)
    s = dict(summary)
    s.pop("pairs")
    s["pdf_only_folders"] = {k: v for k, v in s["pdf_only_folders"].items() if k != "rows"}
    print(json.dumps(s, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
