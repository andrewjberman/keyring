"""RCG stage-A scanner: population, classes, charters, filesystem/status/temporal features.

W1 stage A (NFRA_REPOCOHERENCEGRAPH PRD s.6, s.9). Deterministic. Emits a PINNED SCAN
VINTAGE under rcg/scans/<stamp>_<head8>/ (gitignored -- measurements are ephemeral,
decisions durable): inventory.jsonl (one row per file) + census.json + a printed census
with per-root denominators.

BOUNDARY DECLARATION (printed at every run, per the recall standard):
  address_space      tracked files at HEAD+index (git ls-files). UNTRACKED and gitignored
                     residue is OUT of the v1 population (local-hygiene class, /kill
                     storage territory, not the durable knowledge plane).
  traversal_residue  submodule interiors (portal gitlink skipped, counted); binary CONTENT
                     never parsed (status markers read from text heads only, first 4KB);
                     git history not rename-followed (a renamed file's temporal features
                     start at the rename).
  presentation      the printed census is an AGGREGATE; per-file truth is inventory.jsonl.
  failure_direction  population: LOUD (a git failure exits 3, never a partial count).
                     status markers: UNDER-detection (regex on the head only).
                     temporal: UNDER-counts pre-rename history.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

WS = Path(__file__).resolve().parents[2]
CHARTERS = WS / "rcg" / "charters.yaml"

EXEC_EXT = {".py", ".sh", ".ps1", ".psm1", ".js", ".ts", ".tsx", ".cmd", ".bat"}
REG_EXT = {".yaml", ".yml", ".json", ".toml", ".ini", ".cfg", ".xml"}
DOC_EXT = {".md", ".txt", ".rst", ".docx", ".html"}
DATA_EXT = {".csv", ".tsv", ".parquet", ".jsonl", ".xlsx", ".pkl", ".pdf", ".gz", ".zip"}

NAME_SIGNALS = {
    "dated": re.compile(r"20\d{6}|20\d\d[-_]\d\d[-_]\d\d"),
    "testish": re.compile(r"(^|[_/])(test|tests|tmp|temp|scratch|spike|draft)([_./]|$)", re.I),
    "versioned": re.compile(r"[_-]v\d+([_.]|$)|[_-](old|bak|backup|copy)([_.]|$)", re.I),
    "relocated": re.compile(r"\.RELOCATED\.", re.I),
    "tilde": re.compile(r"~[A-Z]($|[/_.])"),
}
STATUS_PAT = re.compile(
    r"\b(SUPERSEDED|DEPRECATED|RETIRED|OBSOLETE|DO NOT USE|ARCHIVED|STALE|"
    r"CANONICAL|AUTHORITATIVE|DRAFT|PROPOSAL|WIP)\b")


def die(msg: str) -> None:
    print(f"BLOCKED: {msg}")
    sys.exit(3)


def git_lines(*args: str) -> list[str]:
    out = subprocess.run(["git", *args], cwd=WS, capture_output=True, text=True,
                         encoding="utf-8", errors="replace")
    if out.returncode != 0:
        die(f"git {' '.join(args[:2])} rc={out.returncode}: {out.stderr.strip()[:200]}")
    return out.stdout.splitlines()


def compile_charters() -> list[tuple[re.Pattern, str, int]]:
    spec = yaml.safe_load(CHARTERS.read_text(encoding="utf-8"))
    rules = []
    for pat, cfg in spec["charters"].items():
        specificity = len(pat.replace("*", ""))
        rx = re.escape(pat).replace(r"\*\*", "").replace(r"\*", "[^/]*")
        rx = rx.replace("", ".*")
        if pat.endswith("/"):
            rx = rx + ".*"
        rules.append((re.compile("^" + rx + "$"), cfg["charter"], specificity))
    rules.sort(key=lambda r: -r[2])  # most-specific first
    return rules


def charter_of(path: str, rules: list[tuple[re.Pattern, str, int]]) -> str:
    for rx, charter, _ in rules:
        if rx.match(path):
            return charter
    return "UNCHARTERED"


def class_of(path: str, charter: str) -> str:
    if charter == "APPEND_ONLY_RECORD":
        return "RECORD"  # by charter, never extension (PRD s.4)
    ext = Path(path).suffix.lower()
    if ext in EXEC_EXT:
        return "EXEC"
    if ext in REG_EXT:
        return "REG"
    if ext in DOC_EXT:
        return "DOC"
    if ext in DATA_EXT:
        return "DATA"
    return "ASSET"


def temporal_pass(population: set) -> dict:
    """One streaming pass over full history: first/last touch, commits, authors/file."""
    t: dict = {p: {"first": None, "last": None, "n": 0, "authors": set()} for p in population}
    proc = subprocess.Popen(
        ["git", "log", "--format=%x01%at%x02%an", "--name-only"],
        cwd=WS, stdout=subprocess.PIPE, text=True, encoding="utf-8", errors="replace")
    at, an = None, None
    assert proc.stdout is not None
    for line in proc.stdout:
        line = line.rstrip("\n")
        if line.startswith("\x01"):
            at_s, an = line[1:].split("\x02", 1)
            at = int(at_s)
        elif line and at is not None:
            rec = t.get(line)
            if rec is not None:
                rec["n"] += 1
                if rec["last"] is None:
                    rec["last"] = at  # log is newest-first
                rec["first"] = at
                if len(rec["authors"]) < 8:
                    rec["authors"].add(an)
    proc.wait()
    if proc.returncode != 0:
        die(f"git log stream rc={proc.returncode}")
    return t


def main() -> int:
    head = git_lines("rev-parse", "HEAD")[0][:8]
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = WS / "rcg" / "scans" / f"{stamp}_{head}"
    out_dir.mkdir(parents=True, exist_ok=True)

    rules = compile_charters()
    files = [p for p in git_lines("ls-files") if p]
    skipped_submodules = [p for p in files if p == "portal"]
    files = [p for p in files if p != "portal"]
    population = set(files)

    print(f"[scan] vintage {stamp} @ HEAD {head} -- population {len(files)} tracked files "
          f"(+{len(skipped_submodules)} submodule gitlink(s) skipped, declared)")
    print("[scan] temporal: streaming full history (one pass, no rename-follow) ...")
    temporal = temporal_pass(population)
    now = datetime.now(timezone.utc).timestamp()

    rows = []
    census: dict = defaultdict(lambda: defaultdict(int))
    for path in files:
        charter = charter_of(path, rules)
        fclass = class_of(path, charter)
        root = path.split("/", 1)[0] if "/" in path else "(root)"
        signals = sorted(k for k, rx in NAME_SIGNALS.items() if rx.search(path))
        status_markers: list = []
        if fclass in ("DOC", "REG") and charter not in ("EXCLUDED",):
            try:
                head_text = (WS / path).read_text(encoding="utf-8", errors="ignore")[:4096]
                status_markers = sorted(set(STATUS_PAT.findall(head_text)))
            except OSError:
                status_markers = ["UNREADABLE"]
        tp = temporal[path]
        row = {
            "path": path, "root": root, "charter": charter, "class": fclass,
            "fs_depth": path.count("/"),
            "fs_name_signal": signals,
            "s_header_status": status_markers,
            "t_first": tp["first"], "t_last": tp["last"], "t_commits": tp["n"],
            "t_authors": sorted(tp["authors"]),
            "t_age_days": round((now - tp["first"]) / 86400, 1) if tp["first"] else None,
            "t_last_touch_days": round((now - tp["last"]) / 86400, 1) if tp["last"] else None,
        }
        rows.append(row)
        census[root]["files"] += 1
        census[root][f"class:{fclass}"] += 1
        census[root][f"charter:{charter}"] += 1
        if status_markers and set(status_markers) & {"SUPERSEDED", "DEPRECATED", "RETIRED",
                                                     "OBSOLETE", "ARCHIVED"}:
            census[root]["declared_dead_markers"] += 1

    with (out_dir / "inventory.jsonl").open("w", encoding="utf-8", newline="\n") as h:
        for row in rows:
            h.write(json.dumps(row, ensure_ascii=False) + "\n")

    protected = {"APPEND_ONLY_RECORD", "DOCTRINE", "PROTECTED_LIVE_CORE", "EXCLUDED"}
    n_protected = sum(1 for r in rows if r["charter"] in protected)
    n_uncharted = sum(1 for r in rows if r["charter"] == "UNCHARTERED")
    summary = {
        "vintage": {"stamp": stamp, "head": head}, "population": len(files),
        "protected": n_protected, "scoreable": len(files) - n_protected,
        "uncharted": n_uncharted,
        "per_root": {k: dict(v) for k, v in sorted(census.items(),
                                                   key=lambda x: -x[1]["files"])},
    }
    (out_dir / "census.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")

    print(f"\n[census] population {len(files)} = protected {n_protected} + scoreable "
          f"{len(files) - n_protected}; UNCHARTERED {n_uncharted} (amend charters.yaml)")
    print(f"{'root':<22}{'files':>7}{'RECORD':>8}{'EXEC':>7}{'REG':>7}{'DOC':>7}"
          f"{'DATA':>7}{'ASSET':>7}{'dead-mark':>10}")
    for root, c in sorted(census.items(), key=lambda x: -x[1]["files"])[:20]:
        print(f"{root:<22}{c['files']:>7}{c.get('class:RECORD', 0):>8}"
              f"{c.get('class:EXEC', 0):>7}{c.get('class:REG', 0):>7}"
              f"{c.get('class:DOC', 0):>7}{c.get('class:DATA', 0):>7}"
              f"{c.get('class:ASSET', 0):>7}{c.get('declared_dead_markers', 0):>10}")
    print(f"\n[scan] wrote {out_dir.relative_to(WS)}/inventory.jsonl + census.json")
    print("[boundary] " + __doc__.split("BOUNDARY DECLARATION", 1)[1].strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
