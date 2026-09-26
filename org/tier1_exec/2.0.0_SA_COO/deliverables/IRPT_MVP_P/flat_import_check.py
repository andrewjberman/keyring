#!/usr/bin/env python3
"""Flat-layout cold-start check for the investor-reporting functions, over the WORKING TREE.

Row IRPT_BCKEND-W3-S26: an in-tree test passes on a zip that dies at cold start. This assembles each
function's package the way the build does -- source_dir's listed `files` plus every `staged_from` row at
its `packaged_as` path, from the working tree rather than the row's pin (the point is to test what the NEXT
rebuild ships) -- into a temporary directory, then imports the Terraform handler module in a CLEAN
interpreter whose sys.path is that directory only (plus the site packages the Lambda layer supplies:
boto3/jsonschema are taken from this interpreter), and reads the handler attribute.

It builds nothing for deployment and uploads nothing. Output: one line per function and rc 0 only if every
handler imported.

Usage (backend worktree root):
  python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/flat_import_check.py [--map-root <tree>] [function ...]
--map-root reads lambda-source-map.json from another tree (the publish worktree, where builds run) while the
member CONTENT still comes from this tree -- i.e. "the publish map, re-pinned to this tree's HEAD".
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "infra/aws/lambda/investor-reporting/_authz"))
import routetable as rt  # noqa: E402  the census's own handler derivation

DEFAULT = ("irpt-performance-adapter", "irpt-ycharts-generate", "irpt-status", "irpt-export-render",
           "irpt-narrative", "irpt-directory-search", "irpt-holdings")
PROBE = r"""
import importlib, json, sys
sys.path[:0] = [sys.argv[1]]
module, attr = sys.argv[2], sys.argv[3]
try:
    handler = getattr(importlib.import_module(module), attr)
    print(json.dumps({"ok": callable(handler), "guarded": bool(getattr(handler, "__irpt_guarded__", False)),
                      "routes": len(getattr(handler, "__irpt_routes__", None)
                                    or getattr(getattr(handler, "__irpt_entry__", None), "routes", None) or {})}))
except Exception as exc:
    print(json.dumps({"ok": False, "error": "%s: %s" % (type(exc).__name__, str(exc)[:300])}))
"""


def assemble(function, rec, dest):
    source = ROOT / rec["source_dir"]
    missing = []
    for name in rec.get("files") or []:
        src = source / name
        (dest / name).parent.mkdir(parents=True, exist_ok=True)
        if src.is_file():
            shutil.copy2(src, dest / name)
        else:
            missing.append(str(src.relative_to(ROOT)))
    for row in rec.get("staged_from") or []:
        src, out = ROOT / row["repo_path"], dest / (row.get("packaged_as") or Path(row["repo_path"]).name)
        out.parent.mkdir(parents=True, exist_ok=True)
        if src.is_file():
            shutil.copy2(src, out)
        else:
            missing.append(row["repo_path"])
    return missing


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--map-root", default=None)
    ap.add_argument("functions", nargs="*")
    args = ap.parse_args(argv)
    functions = args.functions or DEFAULT
    fns = rt._source_map(str(Path(args.map_root) / "infra/aws/lambda/ci/lambda-source-map.json")
                         if args.map_root else None)
    env = dict(os.environ, IRPT_DIRECTORY_BUCKET_MAP=os.environ.get("IRPT_DIRECTORY_BUCKET_MAP", "{}"))
    failures = 0
    for function in functions:
        rec = fns.get(function)
        tf = (ROOT / rec["tf_file"]).read_text(encoding="utf-8")
        handler = rt._HANDLER_RE.findall(tf)[0]
        module, _, attr = handler.partition(".")
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            missing = assemble(function, rec, dest)
            proc = subprocess.run([sys.executable, "-c", PROBE, str(dest), module, attr], capture_output=True,
                                  text=True, env=env, cwd=tmp, timeout=120)
        lines = proc.stdout.strip().splitlines()
        result = json.loads(lines[-1]) if lines else {"ok": False, "error": proc.stderr[-300:]}
        result.update(function=function, handler=handler, missing_members=missing)
        failures += 0 if result["ok"] else 1
        print(json.dumps(result))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
