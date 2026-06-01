#!/usr/bin/env python3
"""comp-lambdamap -- derive/verify the Lambda source-map against ground truth.

Phase 1 (this file): `check` -- read-only drift detection. Compares
infra/aws/lambda/ci/lambda-source-map.json against the two real sources of
truth (Terraform function->source_dir + the on-disk lambda dirs) and reports
drift classes. NO map mutation (zero blast radius). CI-gate friendly: exits 1
on any drift, 0 when clean.

Drift classes:
  WRONG_SOURCE_DIR   source-map source_dir != TF source_dir, or the dir is absent
  MISLOCATED         entry is a TOP-LEVEL key (outside functions{}) -> no sha-refresh/provenance
  INCOMPLETE_SCHEMA  functions{} entry missing source_dir (build-and-upload can't build it)
  MISSING_ENTRY      TF-backed lambda with NO functions{} entry (CI-drift-blind)
  ORPHAN_ENTRY       functions{} entry with no TF resource AND no on-disk dir

Phase 2 (future): derive [--write] + provenance. Not implemented here.

Origin: BMKAUD source-map audit (CVO 359375d87) + CTO charter (f9e70457a).
Author: 0.7.0_AE_CloudOps.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

SRCMAP_REL = "infra/aws/lambda/ci/lambda-source-map.json"
TF_ROOT_REL = "infra/aws/terraform"
LAMBDA_ROOT_REL = "infra/aws/lambda"
# top-level source-map keys that are metadata, not function entries
META_KEYS = {"_description", "_updated", "_note", "functions", "_last_deploy_recorded"}


def workspace_root() -> str:
    # this file lives at <root>/org/modules/graph/lambdamap_cli.py
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def load_srcmap(root: str) -> dict:
    with open(os.path.join(root, SRCMAP_REL), encoding="utf-8") as fh:
        return json.load(fh)


def _strip_interp(val: str) -> str:
    # normalize "${local.lambda_base_dir}/x" -> "infra/aws/lambda/x"
    val = val.replace("${local.lambda_base_dir}", "infra/aws/lambda")
    val = re.sub(r"\$\{[^}]+\}", "", val)
    return val.strip().strip("/")


def parse_tf(root: str) -> dict:
    """Return {function_name: {'source_dir': <rel or None>, 'tf_file': <rel>}}.

    Matches both `module "x" { ... function_name=.. source_dir=.. }` (yang-lambda
    module pattern) and raw `resource "aws_lambda_function" "x" { function_name=.. }`.
    Regex-based (mirrors comp-iam's HCL approach) -- sufficient for these stanzas.
    """
    out: dict = {}
    tf_root = os.path.join(root, TF_ROOT_REL)
    block_re = re.compile(
        r'(?:module|resource)\s+(?:"aws_lambda_function"\s+)?"[^"]+"\s*\{', re.M)
    for dirpath, dirnames, filenames in os.walk(tf_root):
        if ".terraform" in dirpath:
            continue
        for fn in filenames:
            if not fn.endswith(".tf"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, root).replace("\\", "/")
            try:
                text = open(path, encoding="utf-8").read()
            except Exception:
                continue
            # split into top-level brace blocks (greedy-safe: scan by stanza start)
            for m in block_re.finditer(text):
                start = m.end()
                depth = 1
                i = start
                while i < len(text) and depth:
                    if text[i] == "{":
                        depth += 1
                    elif text[i] == "}":
                        depth -= 1
                    i += 1
                blk = text[start:i - 1]
                fnm = re.search(r'function_name\s*=\s*"([^"$]+)"', blk)
                if not fnm:
                    continue
                name = fnm.group(1)
                sdm = re.search(r'source_dir\s*=\s*"([^"]+)"', blk)
                sd = _strip_interp(sdm.group(1)) if sdm else None
                # last writer wins is fine; dedupe by name, prefer one with source_dir
                if name not in out or (sd and not out[name].get("source_dir")):
                    out[name] = {"source_dir": sd, "tf_file": rel}
    return out


def check(root: str) -> int:
    sm = load_srcmap(root)
    funcs = sm.get("functions", {})
    top_level = {k: v for k, v in sm.items() if k not in META_KEYS}
    tf = parse_tf(root)

    findings: list[tuple[str, str, str]] = []  # (class, name, detail)

    # MISLOCATED: any non-meta top-level key
    for name in top_level:
        findings.append(("MISLOCATED", name,
                         "top-level key outside functions{} -> no sha-refresh/provenance"))

    # per functions{} entry: WRONG_SOURCE_DIR / INCOMPLETE_SCHEMA / ORPHAN_ENTRY
    for name, e in funcs.items():
        sd = e.get("source_dir")
        if not sd:
            findings.append(("INCOMPLETE_SCHEMA", name, "no source_dir"))
        elif sd == "EXTERNAL":
            # intentional sentinel: code lives outside the repo (not drift)
            continue
        else:
            abs_sd = os.path.join(root, sd)
            if not os.path.isdir(abs_sd):
                findings.append(("WRONG_SOURCE_DIR", name,
                                 f"source_dir absent on disk: {sd}"))
            elif name in tf and tf[name].get("source_dir") and \
                    tf[name]["source_dir"].rstrip("/") != sd.rstrip("/"):
                findings.append(("WRONG_SOURCE_DIR", name,
                                 f"source-map={sd} != TF={tf[name]['source_dir']}"))
        # ORPHAN: not TF-backed and dir (if any) absent
        if name not in tf:
            if not sd or not os.path.isdir(os.path.join(root, sd)):
                findings.append(("ORPHAN_ENTRY", name,
                                 "no TF resource and no on-disk source_dir"))

    # MISSING_ENTRY: TF-backed lambda with no functions{} entry
    for name in tf:
        if name not in funcs:
            findings.append(("MISSING_ENTRY", name,
                             f"TF-backed (in {tf[name]['tf_file']}) but no functions{{}} entry"))

    # report
    order = ["WRONG_SOURCE_DIR", "MISSING_ENTRY", "INCOMPLETE_SCHEMA",
             "MISLOCATED", "ORPHAN_ENTRY"]
    findings.sort(key=lambda f: (order.index(f[0]) if f[0] in order else 99, f[1]))
    print("comp-lambdamap check -- source-map vs TF + on-disk dirs (read-only)")
    print(f"  source-map functions: {len(funcs)} | top-level non-meta: {len(top_level)} "
          f"| TF lambdas: {len(tf)}")
    if not findings:
        print("  CLEAN: no drift. source-map matches TF + dirs.")
        return 0
    counts: dict = {}
    for cls, _, _ in findings:
        counts[cls] = counts.get(cls, 0) + 1
    print("  DRIFT: " + ", ".join(f"{counts[c]} {c}" for c in order if c in counts))
    for cls, name, detail in findings:
        print(f"    [{cls}] {name}: {detail}")
    return 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="comp-lambdamap")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("check", help="read-only drift detection (Phase 1)")
    args = ap.parse_args(argv)
    root = workspace_root()
    if args.cmd in (None, "check"):
        return check(root)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
