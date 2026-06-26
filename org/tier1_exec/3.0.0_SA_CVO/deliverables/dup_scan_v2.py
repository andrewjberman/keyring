#!/usr/bin/env python3
"""DESIGN RECORD / re-export shim -- NOT the engine.

The canonical comp-dups engine was RELOCATED to org/modules/graph/debtscan/dup_scan.py
(2026-06-26, COO convention-lock 4d56eb0db; invoked via the `comp-dups` PATH tool). This file
remains only as the design-record pointer referenced by
CVO_bm25_dup_deadtwin_scanner_design_findings_20260626.md, and re-execs the canonical engine so
`python dup_scan_v2.py` still resolves.

DO NOT add scanner logic here -- one engine, one home. A forked engine body is exactly the
content-dup class comp-dups exists to flag (it would dogfood-flag itself).
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

_ENGINE = Path(__file__).resolve().parents[4] / "org" / "modules" / "graph" / "debtscan" / "dup_scan.py"

if __name__ == "__main__":
    sys.argv[0] = str(_ENGINE)
    runpy.run_path(str(_ENGINE), run_name="__main__")
