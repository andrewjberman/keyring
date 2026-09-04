"""NFRA_CLDGRPH CG-s-7 (TO-CG-D-4) battery for the operator status read's R4 repoint.

`comp-graph status` used to stat two LOCAL files under infra/aws/globgrph/ (kuzu_db,
stitch_graph) that were the wrong artifacts (brief F6). It now begins at the projection
pointer (`projection/current.json`), applies the reader straddle rule, and answers
"did it refresh last night" with yes/no + a time from the served manifest's own record.

Run at both required file grains:
  python .tools/tests/test_cg7_status_read_battery.py
  python -m pytest -q .tools/tests/test_cg7_status_read_battery.py

Arms (denominator 5, each with its own record; two carry a RED mutant proving the check
discriminates a broken reader from a correct one -- CLAUDE.md s.22 DISCRIMINATION):
  (i)   live-shaped fixture: a full manifest 2h inside the nightly window -> YES at <built_at>.
  (ii)  the PLANT committed under this TO's deliverables/plant/: newest full 30h before the
        boundary, nothing inside the window -> NO (last full: <built_at>). RED mutant: forcing
        every listed vintage into the window makes the plant wrongly read YES.
  (iii) an unreadable pointer -> UNVERIFIABLE (never a silent pass/default). RED mutant: the
        unreachable branch's message is broken so it wrongly claims NO instead of UNVERIFIABLE.
  (iv)  --json carries `refreshed_last_night` and `vintage` on the projection.last_night record.
  (v)   R4 census: the engine source carries no sns/cloudwatch/put_metric/events/schedule call
        (denominator = source line count scanned).

Fixtures for (i)/(iii)/(iv) are built under the test's own temp dir, never under infra/. Arm
(ii) exercises the actual committed plant so the same fixture backs both this battery and
acceptance criterion D4-AC2.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "org" / "modules" / "graph" / "graph_status_cli.py"
PLANT_POINTER = (
    ROOT / "org" / "missions" / "D0" / "NFRA" / "NFRA_CLDGRPH" / "deliverables"
    / "0.9.0_WK_NFRA_CLDGRPH~3" / "plant" / "current.json"
)
RESULTS: list[tuple[str, bool, str]] = []


def _record(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, ok, detail.replace("\n", " ")[:500]))


def _run_status(pointer_path=None, json_mode=False, tool: Path = ENGINE, timeout: int = 60):
    env = dict(os.environ)
    if pointer_path is not None:
        env["COMP_GRAPH_POINTER_URI"] = str(pointer_path)
    args = [sys.executable, str(tool), "status"]
    if json_mode:
        args.append("--json")
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True,
                          timeout=timeout, env=env)


def _mutant_tool(needle: str, replacement: str) -> Path:
    source = ENGINE.read_text(encoding="utf-8")
    count = source.count(needle)
    if count != 1:
        raise AssertionError("mutation anchor count != 1 for %r: %d" % (needle, count))
    path = ENGINE.parent / (".graph_status_cli_cg7_mutant_%s.tmp.py" % uuid.uuid4().hex)
    path.write_text(source.replace(needle, replacement, 1), encoding="utf-8")
    return path


def _iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")


def _write_fixture(tmpdir: Path, vintage_dt: datetime, mode: str, writer_id: str,
                   built_at_dt: datetime | None = None) -> Path:
    """Build a pointer + manifest pair under tmpdir, mirroring the S3 layout (':' -> '_' in the
    local vintage directory name, matching the production reader's own escape)."""
    vintage = _iso(vintage_dt)
    built_at = _iso(built_at_dt or (vintage_dt + timedelta(minutes=15)))
    manifest = {
        "schema_version": 1,
        "vintage": vintage,
        "committed_at": vintage,
        "age_line": "Built from the estate as of %s UTC." % vintage_dt.strftime("%Y-%m-%d %H:%M:%S"),
        "nessie_commit_hash": "a" * 64,
        "nodes_snapshot_id": 1111111111111111111,
        "edges_snapshot_id": 2222222222222222222,
        "writer_id": writer_id,
        "built_at": built_at,
        "producer": {"mode": mode, "engine": "kuzu", "engine_version": "0.11.3",
                     "source_commit": "b" * 40},
        "node_count": 27000,
        "edge_count": 58000,
        "edges_skipped_missing_endpoint": 400,
        "artifact": {
            "format": "kuzu-raw-v0.11",
            "files": [{"name": "kuzu_nessie_db", "size_bytes": 47000000, "sha256": "c" * 64}],
            "total_size_bytes": 47000000,
            "expected_publish_set_size_band_bytes": {
                "baseline": 46994310, "minimum": 42294879, "maximum": 51693741,
            },
        },
    }
    manifest_bytes = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode("utf-8")
    sha = hashlib.sha256(manifest_bytes).hexdigest()
    dirname = vintage.replace(":", "_")
    vdir = tmpdir / dirname
    vdir.mkdir(parents=True, exist_ok=True)
    (vdir / "_build_manifest.json").write_bytes(manifest_bytes)
    pointer = {
        "schema_version": 1,
        "vintage": vintage,
        "artifact_prefix": "projection/%s/" % vintage,
        "manifest_key": "projection/%s/_build_manifest.json" % vintage,
        "manifest_sha256": sha,
    }
    pointer_path = tmpdir / "current.json"
    pointer_path.write_bytes(json.dumps(pointer, sort_keys=True, separators=(",", ":")).encode("utf-8"))
    return pointer_path


def _boundary_now():
    now = datetime.now(timezone.utc)
    boundary = now.replace(hour=2, minute=0, second=0, microsecond=0)
    if now < boundary:
        boundary -= timedelta(days=1)
    return boundary


def _run_battery() -> None:
    if RESULTS:
        return

    boundary = _boundary_now()

    # --- Arm (i): live-shaped fixture, full vintage 2h inside the window -> YES at ------------
    with tempfile.TemporaryDirectory() as td:
        pointer_path = _write_fixture(Path(td), boundary + timedelta(hours=2), "full", "derive_runner")
        r = _run_status(pointer_path)
        ok = (r.returncode == 0
              and re.search(r"REFRESHED LAST NIGHT: YES at 20\d\d-\d\d-\d\dT\d\d:\d\d:\d\d", r.stdout) is not None)
        _record("ARM-I-LIVE-SHAPED-YES", ok, r.stdout[-600:] + "|stderr:" + r.stderr[-300:])

    # --- Arm (ii): the committed plant, newest full 30h before boundary -> NO (last full: -----
    if not PLANT_POINTER.exists():
        _record("ARM-II-PLANT-NO", False, "plant fixture missing at %s" % PLANT_POINTER)
    else:
        r = _run_status(PLANT_POINTER)
        ok = r.returncode == 0 and "REFRESHED LAST NIGHT: NO (last full:" in r.stdout
        _record("ARM-II-PLANT-NO", ok, r.stdout[-600:] + "|stderr:" + r.stderr[-300:])

        # RED MUTANT: forcing every listed vintage into the window makes the empty-window plant
        # wrongly read YES -- "a reader that prints YES when the window is empty" (the exact class
        # the TO names). Proves ARM-II discriminates a broken reader from a correct one.
        mutant = _mutant_tool(
            "in_window = [(dt, v) for dt, v in parsed if boundary <= dt < window_end]",
            "in_window = [(dt, v) for dt, v in parsed]",
        )
        try:
            mr = _run_status(PLANT_POINTER, tool=mutant)
            mutant_wrongly_yes = "REFRESHED LAST NIGHT: YES at" in mr.stdout
            correct_no_gone = "REFRESHED LAST NIGHT: NO (last full:" not in mr.stdout
            _record("ARM-II-RED-MUTANT-EMPTY-WINDOW-YES",
                    mutant_wrongly_yes and correct_no_gone,
                    "mutant stdout tail: " + mr.stdout[-400:])
        finally:
            if mutant.exists():
                mutant.unlink()

    # --- Arm (iii): an unreadable pointer -> UNVERIFIABLE, never a default --------------------
    with tempfile.TemporaryDirectory() as td:
        missing = Path(td) / "does-not-exist" / "current.json"
        r = _run_status(missing)
        ok = r.returncode == 0 and "REFRESHED LAST NIGHT: UNVERIFIABLE (" in r.stdout
        _record("ARM-III-UNREADABLE-POINTER-UNVERIFIABLE", ok,
                r.stdout[-600:] + "|stderr:" + r.stderr[-300:])

        # RED MUTANT: break the UNVERIFIABLE message on the unreachable branch so it silently
        # claims NO instead -- proves ARM-III discriminates a reader that stops saying
        # UNVERIFIABLE on a real read failure.
        mutant = _mutant_tool(
            'f"REFRESHED LAST NIGHT: UNVERIFIABLE ({reason})"',
            'f"REFRESHED LAST NIGHT: NO (last full: none -- pointer unreachable)"',
        )
        try:
            mr = _run_status(missing, tool=mutant)
            desc_unverifiable_gone = "REFRESHED LAST NIGHT: UNVERIFIABLE (" not in mr.stdout
            desc_now_wrongly_no = "REFRESHED LAST NIGHT: NO (last full: none" in mr.stdout
            _record("ARM-III-RED-MUTANT-SILENT-NO", desc_unverifiable_gone and desc_now_wrongly_no,
                    "mutant stdout tail: " + mr.stdout[-400:])
        finally:
            if mutant.exists():
                mutant.unlink()

    # --- Arm (iv): --json carries refreshed_last_night and vintage ---------------------------
    with tempfile.TemporaryDirectory() as td:
        pointer_path = _write_fixture(Path(td), boundary + timedelta(hours=1), "full", "derive_runner")
        r = _run_status(pointer_path, json_mode=True)
        ok = False
        detail = r.stdout[-600:] + "|stderr:" + r.stderr[-300:]
        try:
            data = json.loads(r.stdout)
            rows = [g for g in data.get("graphs", []) if g.get("name") == "projection.last_night"]
            ok = (r.returncode == 0 and len(rows) == 1
                  and "refreshed_last_night" in rows[0] and "vintage" in rows[0]
                  and rows[0]["refreshed_last_night"] is True)
            detail = json.dumps(rows[0]) if rows else detail
        except Exception as e:  # noqa: BLE001
            detail = "%s: %s | %s" % (type(e).__name__, e, detail)
        _record("ARM-IV-JSON-REFRESHED-LAST-NIGHT-AND-VINTAGE", ok, detail)

    # --- Arm (v): R4 census -- no sns/cloudwatch/put_metric/events/schedule call --------------
    source = ENGINE.read_text(encoding="utf-8")
    lines = source.splitlines()
    banned = re.compile(r"\bsns\b|\bcloudwatch\b|put_metric|events\.put|create_alarm|schedule\(",
                        re.IGNORECASE)
    hits = [(i + 1, ln) for i, ln in enumerate(lines) if banned.search(ln)]
    _record("ARM-V-R4-CENSUS-NO-ALARM-SNS-SCHEDULE (0/%d source line(s) scanned)" % len(lines),
            len(hits) == 0, str(hits))


def _report() -> int:
    _run_battery()
    failed = [(name, detail) for name, ok, detail in RESULTS if not ok]
    for name, ok, detail in RESULTS:
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name, "" if ok else " -- " + detail))
    print("CG7-STATUS-READ BATTERY: %d/%d PASS (denominator %d)" %
          (len(RESULTS) - len(failed), len(RESULTS), len(RESULTS)))
    return 1 if failed else 0


def test_all_arms_pass():
    _run_battery()
    failed = [(name, detail) for name, ok, detail in RESULTS if not ok]
    assert not failed, "CG-s-7 status-read battery failures: %r" % failed


if __name__ == "__main__":
    raise SystemExit(_report())
