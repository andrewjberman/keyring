"""Exercise matrix for .tools/rcg_sweep_verify.py (ruling CTOB-RCG-001).

Builds a synthetic fixture repo per case, stages a real deletion set in it, and
runs the verifier against it via the --workspace test seam. The live estate is
never touched and no commit is ever made here.

WHY A FIXTURE AND NOT THE REAL REPO: this gate's entire job is to DENY, and every
deny path needs a real mutant to fire on -- a batch that is not deletion-only, a
path that is not ARCHIVE, a package losing its __init__.py. Producing those in the
live estate means staging unratified deletions of real files. A fixture makes each
mutant cheap, exact, and reversible, so the gate is accepted on OBSERVED denials
rather than on the claim that it would deny.

The controls that stop a uniformly-broken gate from passing this suite: P1 must
PERMIT (a gate that denies everything is not a gate), and each deny case asserts
its OWN check id fired -- not merely that something failed.

Usage: python .tools/test_rcg_sweep_verify.py
Author: 1.0.0_SA_CTO~B, 2026-08-04.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VERIFIER = Path(__file__).resolve().parent / "rcg_sweep_verify.py"

CHARTERS = """version: 2
charters:
  infra/:   { content: CODE,     handling: SCORE }
  data/:    { content: DATA,     handling: SCORE }
  docs/:    { content: WORKPRODUCT, handling: SCORE }
  docs/doctrine/: { content: DOCTRINE, handling: PROTECT }
  "*":      { content: REGISTRY, handling: SCORE }
"""


def run(cmd, cwd, **kw):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, **kw)


def build_fixture(tmp: Path) -> Path:
    """A repo whose HEAD carries the ledgers + the files a batch will delete."""
    ws = tmp / "ws"
    (ws / "rcg" / "ledger").mkdir(parents=True)
    run(["git", "init", "-q"], ws)
    run(["git", "config", "user.email", "fixture@test"], ws)
    run(["git", "config", "user.name", "fixture"], ws)
    (ws / "rcg" / "charters.yaml").write_text(CHARTERS, encoding="utf-8")

    files, labels = [], []

    def add(path, label, source="assessed_ratified_by_delegation", ruling="R-0020"):
        p = ws / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"content of {path}\n", encoding="utf-8")
        files.append(path)
        labels.append({"path": path, "label": label, "source": source, "ruling": ruling})

    # the clean batch population -- flat dir, ARCHIVE, SCORE charter
    for i in range(6):
        add(f"data/black_diamond/archive/gold/client_detail/c{i:03d}.json", "ARCHIVE")
    # a KEEP file (C4 mutant target)
    add("data/black_diamond/archive/gold/keepme.json", "KEEP")
    # a PROTECT-charter file (C5 mutant target)
    add("docs/doctrine/LAW.md", "ARCHIVE")
    # an andrew-ratified KEEP cohort (C6 mutant target -- the pyiceberg shape)
    add("infra/aws/lambda/layers/deps/python/click/decorators.py", "KEEP",
        source="andrew_ratification", ruling="R-0019")
    add("infra/aws/lambda/layers/deps/python/click/core.py", "ARCHIVE")
    # a python package (C7 mutant target -- the click shape)
    add("infra/pkg/__init__.py", "ARCHIVE")
    add("infra/pkg/mod.py", "KEEP")
    # a superseded label: earlier ARCHIVE row overridden by a later KEEP row
    # (proves last-row-per-path resolution, the R-0022 semantics)
    add("data/superseded.json", "ARCHIVE")
    labels.append({"path": "data/superseded.json", "label": "KEEP",
                   "source": "andrew_ratification", "ruling": "R-0022"})

    (ws / "rcg" / "ledger" / "LABELS.jsonl").write_text(
        '{"id":"L-0000","type":"genesis"}\n'
        + "\n".join(json.dumps(r) for r in labels) + "\n", encoding="utf-8")

    batch_paths = sorted(f"data/black_diamond/archive/gold/client_detail/c{i:03d}.json"
                         for i in range(6))
    import hashlib
    batch = {"id": "B-0001", "status": "RATIFIED", "paths": batch_paths,
             "count": len(batch_paths), "ruling": "R-0022",
             "sha256": hashlib.sha256("\n".join(sorted(batch_paths)).encode()).hexdigest()}
    (ws / "rcg" / "ledger" / "BATCHES.jsonl").write_text(
        '{"id":"B-0000","type":"genesis"}\n' + json.dumps(batch) + "\n", encoding="utf-8")

    run(["git", "add", "-A"], ws)
    run(["git", "commit", "-q", "-m", "fixture HEAD", "--no-verify"], ws)
    return ws


def verify(ws: Path, cap=100, extra=None, mode="execute"):
    cmd = [sys.executable, str(VERIFIER), "--batch-id", "B-0001", "--mode", mode,
           "--cap", str(cap), "--workspace", str(ws)]
    if extra:
        cmd += extra
    r = run(cmd, ws)
    return r.returncode, r.stdout + r.stderr


def execute_and_record(ws: Path):
    """Land the batch deletion, then record executed_commit -- the real sequence.
    Returns nothing; leaves HEAD at the ledger-update commit."""
    stage_delete(ws, BATCH)
    (ws / "m").write_text("batch\n", encoding="utf-8")
    run(["git", "commit", "-q", "-F", "m", "--no-verify"], ws)
    sha = run(["git", "rev-parse", "HEAD"], ws).stdout.strip()
    bp = ws / "rcg" / "ledger" / "BATCHES.jsonl"
    lines = bp.read_text(encoding="utf-8").strip().splitlines()
    row = json.loads(lines[-1])
    row["executed_commit"] = sha
    lines[-1] = json.dumps(row)
    bp.write_text("\n".join(lines) + "\n", encoding="utf-8")
    run(["git", "add", "-A"], ws)
    (ws / "m").write_text("record executed_commit\n", encoding="utf-8")
    run(["git", "commit", "-q", "-F", "m", "--no-verify"], ws)
    return sha


def stage_revert(ws: Path, sha: str):
    run(["git", "revert", "--no-commit", sha], ws)


def stage_delete(ws: Path, paths):
    for p in paths:
        run(["git", "rm", "-q", "--", p], ws)


BATCH = [f"data/black_diamond/archive/gold/client_detail/c{i:03d}.json" for i in range(6)]
results = []


def case(name, expect_rc, expect_token, mutate, cap=100):
    tmp = Path(tempfile.mkdtemp())
    try:
        ws = build_fixture(tmp)
        mutate(ws)
        rc, out = verify(ws, cap=cap)
        ok = (rc == expect_rc) and (expect_token in out if expect_token else True)
        results.append((ok, name, rc, expect_rc, expect_token, out))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


print("Building fixtures and driving every check to fire...\n")

# --- P1: the PERMIT control. Without this the suite passes on a broken-shut gate.
case("P1 clean ratified batch PERMITS", 0, "PERMIT",
     lambda ws: stage_delete(ws, BATCH))

# --- C1 deletion-only
def _c1(ws):
    stage_delete(ws, BATCH)
    (ws / "infra" / "pkg" / "mod.py").write_text("mutated\n", encoding="utf-8")
    run(["git", "add", "infra/pkg/mod.py"], ws)
case("C1 non-deletion change in the batch DENIES", 2, "[C1]", _c1)

# --- C2 both directions
case("C2 extra unratified deletion DENIES", 2, "[C2]",
     lambda ws: stage_delete(ws, BATCH + ["data/black_diamond/archive/gold/keepme.json"]))
case("C2 batch path not deleted DENIES", 2, "[C2]",
     lambda ws: stage_delete(ws, BATCH[:-1]))

# --- C3 SoD: batch ledger modified in the same commit
def _c3(ws):
    stage_delete(ws, BATCH)
    p = ws / "rcg" / "ledger" / "BATCHES.jsonl"
    p.write_text(p.read_text(encoding="utf-8") + '{"id":"B-9999"}\n', encoding="utf-8")
    run(["git", "add", "rcg/ledger/BATCHES.jsonl"], ws)
case("C3 batch authored in the same commit DENIES (SoD)", 2, "[C3]", _c3)

# --- C4 label not ARCHIVE at HEAD (uses last-row-per-path: superseded.json is KEEP)
case("C4 deleting a non-ARCHIVE path DENIES", 2, "[C4]",
     lambda ws: stage_delete(ws, BATCH + ["data/superseded.json"]))

# --- C5 protected charter
case("C5 deleting under a PROTECT charter DENIES", 2, "[C5]",
     lambda ws: stage_delete(ws, BATCH + ["docs/doctrine/LAW.md"]))

# --- C6 cohort-ratification supremacy (the pyiceberg check)
case("C6 deleting inside an andrew-ratified KEEP subtree DENIES", 2, "[C6]",
     lambda ws: stage_delete(ws, BATCH
                             + ["infra/aws/lambda/layers/deps/python/click/core.py"]))

# --- C7 package coherence (the click check)
case("C7 deleting __init__.py with surviving siblings DENIES", 2, "[C7]",
     lambda ws: stage_delete(ws, BATCH + ["infra/pkg/__init__.py"]))

# --- C8 cap
case("C8 batch over the ramp cap DENIES", 2, "[C8]",
     lambda ws: stage_delete(ws, BATCH), cap=3)

# --- cannot-evaluate is a DENY, never a pass
def _e1(ws):
    stage_delete(ws, BATCH)
    run(["git", "rm", "-q", "--", "rcg/ledger/BATCHES.jsonl"], ws)
    run(["git", "commit", "-q", "-m", "drop batches", "--no-verify"], ws)
    stage_delete(ws, BATCH)
case("E1 missing batch ledger -> rc=3 CANNOT EVALUATE (not a pass)", 3, "CANNOT EVALUATE", _e1)


# ---------------------------------------------------------------- REVERT mode
# The leg that was UNAUTHORABLE until R1-R4 existed. RV1 is the control that
# matters most: the deny suite for revert was vacuously complete before, because
# nothing could legally permit a restore at all.
def rcase(name, expect_rc, expect_token, mutate):
    tmp = Path(tempfile.mkdtemp())
    try:
        ws = build_fixture(tmp)
        mutate(ws)
        rc, out = verify(ws, mode="revert")
        ok = (rc == expect_rc) and (expect_token in out if expect_token else True)
        results.append((ok, name, rc, expect_rc, expect_token, out))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _rv1(ws):
    sha = execute_and_record(ws)
    stage_revert(ws, sha)
rcase("RV1 true restore PERMITS (the leg that had no legal author)", 0, "PERMIT", _rv1)

def _rv2(ws):  # content differs -- revert mode may restore, never author
    sha = execute_and_record(ws)
    stage_revert(ws, sha)
    p = ws / BATCH[0]
    p.write_text("TAMPERED ON THE WAY BACK\n", encoding="utf-8")
    run(["git", "add", "--", BATCH[0]], ws)
rcase("RV2 restore with ALTERED content DENIES (R4 blob identity)", 2, "[R4]", _rv2)

def _rv3(ws):  # an extra file smuggled into the restore
    sha = execute_and_record(ws)
    stage_revert(ws, sha)
    extra = ws / "data" / "black_diamond" / "archive" / "gold" / "smuggled.json"
    extra.write_text("not in the batch\n", encoding="utf-8")
    run(["git", "add", "--", str(extra.relative_to(ws)).replace("\\", "/")], ws)
rcase("RV3 extra path smuggled into a restore DENIES (R2)", 2, "[R2]", _rv3)

def _rv4(ws):  # a deletion staged while in revert mode
    sha = execute_and_record(ws)
    stage_revert(ws, sha)
    run(["git", "rm", "-q", "--", "data/black_diamond/archive/gold/keepme.json"], ws)
rcase("RV4 deletion staged in revert mode DENIES (R1)", 2, "[R1]", _rv4)

def _rv5(ws):  # no executed_commit recorded -> nothing to restore FROM
    stage_delete(ws, BATCH)
    (ws / "m").write_text("batch\n", encoding="utf-8")
    run(["git", "commit", "-q", "-F", "m", "--no-verify"], ws)
    run(["git", "revert", "--no-commit", "HEAD"], ws)
rcase("RV5 no executed_commit -> rc=3 CANNOT EVALUATE", 3, "CANNOT EVALUATE", _rv5)

print()
npass = sum(1 for ok, *_ in results if ok)
for ok, name, rc, exp, tok, out in results:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}   (rc={rc}, expected {exp})")
    if not ok:
        print(f"        wanted token {tok!r}; output was:")
        for line in out.strip().splitlines():
            print(f"        | {line}")
print(f"\nRESULT: {npass}/{len(results)} passed")
sys.exit(0 if npass == len(results) else 1)
