#!/usr/bin/env python3
"""issuer_check_sc_e45.py -- MDPF_SECCLASS round 9 issuer check for cell SC-e-45 (FWD-5): the writer stops re-presented.

Runs the three round-8 issuer checks of the writer stops (R10_CHECKS/r10_bd_old_list_writers_check.py, r10_cot_old_list_writer_check.py,
r10_inf_old_list_writer_check.py; each must exit 0), then reads the three half requests
(M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_{BD_OLD_LIST_WRITERS,COT_OLD_LIST_WRITER,INF_OLD_LIST_WRITER}_20261007.md): each must carry a
'## Readers switched' section with at least one 'READER:' line per real reader of the newest M/OLD_LIST_READER_TRACE_BD_*.md and of
M/OLD_LIST_READER_TRACE_20261007.md (sections whose VERDICT is NEEDS-OLD-LIST or REPOINTABLE), and a 'PRODUCER-LIVE-WRITES:' line
holding an integer above 0. Prints SC-E45-STOPS ok=<bool> checks=<n> of 3 halves=<n> of 3 readers=<n>. Read-only. Run from the repo root.
"""
import glob
import os
import re
import subprocess
import sys

M = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")
CHECKS = ("r10_bd_old_list_writers_check.py", "r10_cot_old_list_writer_check.py", "r10_inf_old_list_writer_check.py")
HALVES = ("BD_OLD_LIST_WRITERS", "COT_OLD_LIST_WRITER", "INF_OLD_LIST_WRITER")


def real_readers():
    paths = sorted(glob.glob(os.path.join(M, "OLD_LIST_READER_TRACE_BD_*.md")))[-1:]
    paths.append(os.path.join(M, "OLD_LIST_READER_TRACE_20261007.md"))
    out = []
    for p in paths:
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as fh:
            for s in re.split(r"^## READER:", fh.read(), flags=re.MULTILINE)[1:]:
                v = re.search(r"^VERDICT:\s*(\S+)", s, re.MULTILINE)
                if v and v.group(1) in ("NEEDS-OLD-LIST", "REPOINTABLE"):
                    out.append(s.splitlines()[0].strip())
    return out


def half_ok(path, n_readers):
    if not os.path.exists(path):
        return False
    with open(path, encoding="utf-8") as fh:
        part = fh.read().split("## Readers switched", 1)
    if len(part) < 2:
        return False
    named = len(re.findall(r"^READER:", part[1], re.MULTILINE))
    live = re.search(r"^PRODUCER-LIVE-WRITES:\s*(\d+)", part[1], re.MULTILINE)
    return bool(n_readers) and named >= n_readers and bool(live) and int(live.group(1)) > 0


def main():
    ok_checks = 0
    for c in CHECKS:
        r = subprocess.run([sys.executable, os.path.join(M, "R10_CHECKS", c)], capture_output=True, text=True, timeout=35, check=False)
        ok_checks += int(r.returncode == 0)
    readers = real_readers()
    ok_halves = sum(int(half_ok(os.path.join(M, f"NEVER_WIDEN_HALF_REQUEST_SECCLASS_{h}_20261007.md"), len(readers))) for h in HALVES)
    ok = ok_checks == 3 and ok_halves == 3 and bool(readers)
    print(f"SC-E45-STOPS ok={ok} checks={ok_checks} of 3 halves={ok_halves} of 3 readers={len(readers)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
