#!/usr/bin/env python3
"""docstring-claim-lint -- a docstring that names a bucket / prefix / cadence the
module does not implement, with the literals sitting in the same file.

CTO spec, verbatim (2026-07-09, via COO 222342Z):
    "a docstring naming a prefix / bucket / cadence the module does not implement,
     with the literals in the same file."
Cheap, lexical, no dataflow needed -- the literals are right there.

WHY (four instances in four trees, one night)
---------------------------------------------
    cot_bronze_ingest.py:79-80                 misdescribes a mechanism
    A_01.advisor_assignments.py:18-19          misdescribes a mechanism
    build_mdpf_wse_49f_non_model_aua.py:69-72  misdescribes a mechanism
    convert_schwab_rps_to_silver.py:9          ASSERTS A FRESHNESS GUARANTEE THAT DOES NOT EXIST

The fourth reads: "...`opal-data-schwab/01_raw/` which IS maintained daily by
`sync_schwab_onedrive_to_s3.py`."

It is not maintained daily. The producer is a HUMAN running a script against a
OneDrive folder. `schwab/silver/rps/`'s last partition is `date=20260706`, and
`07-03` is missing entirely -- it was already not daily before it stopped. That
line sits in the converter feeding the custody number currently frozen behind the
49F residual corruption.

    "If anyone had read that line while debugging the 49F plug, they would have
     looked somewhere else entirely."  -- 0.4.0_DS_ClientPlatform

The other three misdescribe a mechanism. **This one misdirects an investigation.**
A docstring is documentation everywhere except in the moment someone is debugging
under time pressure -- and then it is evidence.

RULES (default output = D1 + D2 only)
-------------------------------------
  D1  the docstring names an S3 BUCKET that appears in NO code literal in the same
      file. Buckets are almost always written literally, so their absence IS
      evidence the module never touches what it describes.  [22 on `data/`]
  D2  the docstring asserts a CADENCE ("maintained daily", "written nightly",
      "every N minutes") -- a freshness GUARANTEE. A module cannot guarantee the
      cadence of a producer it does not run. Where the cadence is attributed to
      another module ("by <other>.py"), it is an unverifiable claim about a third
      party -- the exact shape that misdirected the 49F investigation.  [8]
  D4  (INFO, --all) a PREFIX named in the docstring but absent from this file's
      literals. Real signal, weak evidence: prefixes are routinely assembled at
      runtime (f-strings, config, imported constants).  [626]
  D3  (INFO, --all) a `<module>.py` named but neither imported nor referenced. [470]

WHAT IT ACTUALLY CATCHES, MEASURED -- not what the spec advertised
-----------------------------------------------------------------
The brief said all four instances "would have been caught." They are not:

  convert_schwab_rps_to_silver.py  CAUGHT by D1 *and* D2 (independent rules)  <- the dangerous one
  build_mdpf_wse_49f_non_model_aua.py   D4 only (prefix claims)  -> informational
  A_01.advisor_assignments.py           D4 only (prefix claims)  -> informational
  cot_bronze_ingest.py:79-80            OUT OF SCOPE -- it is a COMMENT, not a docstring

Catching the middle two at D1 severity would mean shipping 626 findings, and **a
lint that cries wolf gets muted** -- this lint's own failure mode, and the trap
`suppressed-error-lint` (b7813dfd9) hit at 165 findings before it was tiered. So
the one that MISDIRECTS AN INVESTIGATION is caught twice over, and the two that
merely misdescribe a mechanism are reported without blocking. Tuning the rules
until the advertisement came true would have produced a tool nobody runs.

D1/D2 count a claim as IMPLEMENTED if the token appears anywhere in the file's code
string-literals -- including an f-string fragment or a parameterised bucket var.
Deliberately permissive: a false positive here costs a reader's trust in the only
tool that reads docstrings at all.

WARN-mode by default; `--strict` exits 1. Read-only -- it never edits a file.
Deliberate exceptions carry an inline `# claim-ok: <why the module really does
implement / verify this>`. ASCII only.
"""
from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path

OK_MARKER = re.compile(r"#\s*claim-ok:")

# Buckets and prefixes as they appear in prose/backticks.
S3_URI = re.compile(r"s3://([a-z0-9][a-z0-9._-]+)/([a-z0-9._/{}-]*)", re.I)
BUCKET = re.compile(r"\b(opal-data-[a-z0-9-]+|opal-[a-z0-9-]*bucket[a-z0-9-]*)\b", re.I)
PREFIX = re.compile(r"[`'\"]([a-z0-9_]+(?:/[a-z0-9_{}=-]+){1,4}/?)[`'\"]", re.I)
# BARE prose prefixes ("Scans silver/transactions/ chronologically") carry the same
# claim as backticked ones -- A_01's false mechanism is written exactly that way.
# Anchored to the known medallion/layer segments so the rule stays quiet: an
# unanchored bare-slash match would fire on "and/or" and the lint would be muted.
LAYERS = r"(?:silver|gold|bronze|platinum|raw|warehouse|schwab|artifacts|01_raw|02_|03_)"
BARE_PREFIX = re.compile(rf"\b({LAYERS}[a-z0-9_]*(?:/[a-z0-9_{{}}=-]+){{1,4}}/?)", re.I)
MODREF = re.compile(r"[`'\"]?\b([a-z0-9_]+\.py)\b[`'\"]?", re.I)

# A cadence GUARANTEE, not a mere mention of a word.
CADENCE = re.compile(
    r"\b(?:is\s+)?(?:maintained|written|refreshed|updated|produced|synced|populated|regenerated)"
    r"\s+(?:\w+\s+){0,2}(daily|nightly|hourly|weekly|every\s+\d+\s*\w+)"
    r"|\b(daily|nightly|hourly)\s+(?:by|via|from)\b",
    re.I,
)
ATTRIB = re.compile(r"\bby\s+[`'\"]?([a-z0-9_]+\.py)[`'\"]?", re.I)


def code_literals(tree: ast.AST, src: str) -> str:
    """Every string constant that is NOT a docstring, plus all identifiers.

    Concatenated into one haystack. Permissive on purpose: an f-string fragment or
    a parameterised bucket variable counts as 'the module implements it'.
    """
    docstrings = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            d = ast.get_docstring(node, clean=False)
            if d:
                docstrings.add(d)
    parts = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if node.value not in docstrings:
                parts.append(node.value)
        elif isinstance(node, ast.Name):
            parts.append(node.id)
        elif isinstance(node, ast.Attribute):
            parts.append(node.attr)
    # Import names too -- `import sync_schwab_onedrive_to_s3` counts as a reference.
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            parts.extend(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            parts.append(node.module or "")
            parts.extend(a.name for a in node.names)
    return "\n".join(parts)


def claims_from(doc: str) -> tuple:
    buckets, prefixes, mods = set(), set(), set()
    for m in S3_URI.finditer(doc):
        buckets.add(m.group(1))
        if m.group(2):
            prefixes.add(m.group(2).rstrip("/"))
    for m in BUCKET.finditer(doc):
        buckets.add(m.group(1))
    for m in PREFIX.finditer(doc):
        p = m.group(1).rstrip("/")
        if "/" in p and not p.endswith(".py"):
            prefixes.add(p)
    for m in BARE_PREFIX.finditer(doc):
        p = m.group(1).rstrip("/")
        if "/" in p and not p.endswith(".py"):
            prefixes.add(p)
    for m in MODREF.finditer(doc):
        mods.add(m.group(1))
    return buckets, prefixes, mods


def scan(path: Path) -> list:
    try:
        src = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(src)
    except Exception as e:  # noqa: BLE001 -- surface, never drop
        return [(0, "E0", f"unparseable: {type(e).__name__}: {e}")]
    if OK_MARKER.search(src):
        return []

    hay = code_literals(tree, src)
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        doc = ast.get_docstring(node, clean=False)
        if not doc:
            continue
        line = getattr(node, "lineno", 1)
        buckets, prefixes, mods = claims_from(doc)

        for b in sorted(buckets):
            if b not in hay:
                out.append((line, "D1", f"docstring names bucket `{b}` -- absent from every code literal"))
        # PREFIX claims are D4 (informational), NOT D1. Measured on `data/`: 626 prefix
        # findings against 22 bucket findings. Prefixes are routinely assembled at runtime
        # (f-strings, config, constants imported from a lib), so "absent from this file's
        # literals" is weak evidence the module does not touch them. Buckets are almost
        # always literal, so their absence IS evidence.
        #
        # A lint that cries wolf gets muted -- which is this lint's own failure mode, and
        # the same trap the suppressed-error lint (b7813dfd9) hit at 165 findings. Default
        # output is D1+D2 (30 on `data/`), not 1,126.
        for p in sorted(prefixes):
            tail = p.split("/")[-1]
            if p not in hay and tail not in hay:
                out.append((line, "D4", f"docstring names prefix `{p}` -- absent from this file's literals "
                                        f"(often assembled at runtime; weak evidence)"))

        m = CADENCE.search(doc)
        if m:
            # WINDOWED attribution. A whole-docstring search grabs the FIRST `by <mod>.py`,
            # which for convert_schwab_rps_to_silver.py named the wrong module entirely
            # (`convert_schwab_rps_to_parquet.py` instead of `sync_schwab_onedrive_to_s3.py`).
            # A lint about false attribution that itself misattributes is worse than none.
            who = ATTRIB.search(doc, m.end(), m.end() + 120)
            if who:
                out.append((line, "D2", f"asserts cadence '{m.group(0).strip()}' GUARANTEED BY "
                                        f"`{who.group(1)}` -- an unverifiable claim about a third party"))
            else:
                out.append((line, "D2", f"asserts a cadence guarantee: '{m.group(0).strip()}' -- "
                                        f"the module cannot enforce a producer's schedule"))

        for mod in sorted(mods):
            stem = mod[:-3]
            if stem not in hay and mod not in hay:
                out.append((line, "D3", f"docstring names `{mod}` -- neither imported nor referenced"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Find docstrings claiming what the module does not implement")
    ap.add_argument("paths", nargs="*", default=None)
    ap.add_argument("--strict", action="store_true", help="exit 1 on any D1/D2")
    ap.add_argument("--rule", help="only this rule (D1/D2/D3/D4)")
    ap.add_argument("--all", action="store_true", help="include informational D3/D4")
    args = ap.parse_args()

    roots = [Path(p) for p in (args.paths or ["data"])]
    files: list[Path] = []
    for r in roots:
        if r.is_file() and r.suffix == ".py":
            files.append(r)
        elif r.is_dir():
            files.extend(f for f in r.rglob("*.py"))

    by_rule: dict = {}
    total = 0
    for f in sorted(files):
        for line, rule, msg in scan(f):
            if args.rule and rule != args.rule:
                continue
            if rule in ("D3", "D4") and not (args.all or args.rule):
                continue  # informational: opt in with --all
            total += 1
            by_rule.setdefault(rule, []).append((str(f).replace("\\", "/"), line, msg))

    print(f"docstring-claim-lint -- scanned {len(files)} file(s) under {[str(r) for r in roots]}")
    print()
    if not total:
        print("OK: no docstring claims contradicted by the file's own literals.")
        return 0

    for rule in sorted(by_rule):
        rows = by_rule[rule]
        print(f"{rule} ({len(rows)}):")
        for path, line, msg in rows:
            print(f"  {path}:{line}")
            print(f"      {msg}")
        print()

    hard = len(by_rule.get("D1", [])) + len(by_rule.get("D2", []))
    print(f"{total} finding(s); {hard} are D1/D2 (actionable). Mark a deliberate one with an inline")
    print("`# claim-ok: <why the module really does implement or verify this>`.")
    print()
    print("A docstring is documentation everywhere except in the moment someone is debugging")
    print("under time pressure -- and then it is evidence.")
    if args.strict and hard:
        return 1
    print("WARN: advisory mode -- rerun with --strict to enforce.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
