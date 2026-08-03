"""RCG feature assembly: join scan + mark + lexicon into the model matrix (W1 stage C input).

Emits, per SCOREABLE file (protected charters excluded by design -- they are never
scored): features.jsonl + seed_labels.jsonl (high-confidence bootstrap labels only) into
the newest scan vintage. Model target space v0 is BINARY {KEEP, ARCHIVE_CANDIDATE} --
the full disposition classes arrive with Andrew's ratifications, never from seeds.

BOUNDARY DECLARATION (printed every run):
  address_space      scoreable population of the newest vintage; lexical pass reads
                     DOC/EXEC/REG text (first 512KB).
  traversal_residue  ref_lex_in (inbound mention split) deferred to v2 -- inbound
                     mechanics already carried by ref_mech_in_live; era join is
                     APPROXIMATED (retired project-code tokens in path + text), not a
                     full registry-timeline join, declared; EXEC lexical pass reads the
                     whole file, not only docstrings/comments (over-counts, declared).
  presentation       features.jsonl is the truth; the print is counts.
  failure_direction  seeds: PRECISION over recall (a wrong seed poisons training; a
                     missed seed costs nothing -- the grader finds it later).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

WS = Path(__file__).resolve().parents[2]
PROTECTED = {"APPEND_ONLY_RECORD", "DOCTRINE", "PROTECTED_LIVE_CORE", "EXCLUDED"}
DEAD_MARKERS = {"SUPERSEDED", "DEPRECATED", "RETIRED", "OBSOLETE", "ARCHIVED", "DO NOT USE"}
CANON_MARKERS = {"CANONICAL", "AUTHORITATIVE"}
MAX_LEX_BYTES = 512_000


def newest_scan() -> Path:
    scans = sorted((WS / "rcg" / "scans").glob("*/marked.jsonl"))
    if not scans:
        print("BLOCKED: no marked vintage -- run scan.py then mark.py first")
        sys.exit(3)
    return scans[-1].parent


def load_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", errors="replace") as h:
        return [json.loads(line) for line in h]


def build_lex_patterns(scan_dir: Path) -> tuple:
    lex = json.loads((scan_dir / "lexicon.json").read_text(encoding="utf-8"))
    live, retired = [], []
    for e in lex["entries"]:
        (live if e["status"] == "LIVE" else
         retired if e["status"] == "RETIRED" else []).append(re.escape(e["token"]))
    mk = lambda toks: re.compile(r"\b(?:" + "|".join(  # noqa: E731
        sorted(toks, key=len, reverse=True)) + r")\b") if toks else None
    return mk(live), mk(retired), len(live), len(retired)


def main() -> int:
    scan_dir = newest_scan()
    inventory = {r["path"]: r for r in load_jsonl(scan_dir / "inventory.jsonl")}
    marked = {r["path"]: r for r in load_jsonl(scan_dir / "marked.jsonl")}
    live_rx, retired_rx, n_live, n_retired = build_lex_patterns(scan_dir)
    print(f"[features] vintage {scan_dir.name}; lexicon {n_live} LIVE / "
          f"{n_retired} RETIRED tokens")

    rows, seeds = [], []
    n_lex_scanned = 0
    for path, inv in inventory.items():
        if inv["charter"] in PROTECTED:
            continue
        mk = marked[path]
        lex_live = lex_retired = 0
        if inv["class"] in ("DOC", "EXEC", "REG"):
            try:
                text = (WS / path).read_text(encoding="utf-8",
                                             errors="ignore")[:MAX_LEX_BYTES]
                n_lex_scanned += 1
            except OSError:
                text = ""
            if text:
                lex_live = len(live_rx.findall(text)) if live_rx else 0
                lex_retired = len(retired_rx.findall(text)) if retired_rx else 0
        path_retired = bool(retired_rx.search(path)) if retired_rx else False
        statuses = set(inv["s_header_status"])
        row = {
            "path": path,
            "fs_root": inv["root"], "fs_charter": inv["charter"],
            "f_class": inv["class"], "fs_depth": inv["fs_depth"],
            "sig_dated": int("dated" in inv["fs_name_signal"]),
            "sig_testish": int("testish" in inv["fs_name_signal"]),
            "sig_versioned": int("versioned" in inv["fs_name_signal"]),
            "sig_relocated": int("relocated" in inv["fs_name_signal"]),
            "s_dead_marker": int(bool(statuses & DEAD_MARKERS)),
            "s_canon_marker": int(bool(statuses & CANON_MARKERS)),
            "s_draft_marker": int(bool(statuses & {"DRAFT", "WIP", "PROPOSAL"})),
            "t_age_days": inv["t_age_days"], "t_last_touch_days": inv["t_last_touch_days"],
            "t_commits": inv["t_commits"], "t_author_count": len(inv["t_authors"]),
            "reach_from_root": int(mk["reach_from_root"]),
            "reach_hops": mk["reach_hops"] if mk["reach_hops"] is not None else -1,
            "ref_mech_in_live": mk["ref_mech_in_live"],
            "ref_dangling_out": mk["ref_dangling_out"],
            "lex_out_live": lex_live, "lex_out_retired": lex_retired,
            "lex_retired_ratio": round(lex_retired / (lex_live + lex_retired), 3)
            if (lex_live + lex_retired) else 0.0,
            "era_retired_code_in_path": int(path_retired),
        }
        rows.append(row)
        # seeds: PRECISION over recall
        if (statuses & DEAD_MARKERS) or "relocated" in inv["fs_name_signal"] or \
                "/archive/" in path:
            seeds.append({"path": path, "label": "ARCHIVE_CANDIDATE",
                          "source": "seed:declared-dead"})
        elif mk["reach_root_type"] is not None or mk["ref_mech_in_live"] >= 3:
            seeds.append({"path": path, "label": "KEEP", "source": "seed:root-or-cited"})

    with (scan_dir / "features.jsonl").open("w", encoding="utf-8", newline="\n") as h:
        for r in rows:
            h.write(json.dumps(r) + "\n")
    with (scan_dir / "seed_labels.jsonl").open("w", encoding="utf-8", newline="\n") as h:
        for s in seeds:
            h.write(json.dumps(s) + "\n")

    n_keep = sum(1 for s in seeds if s["label"] == "KEEP")
    n_arch = len(seeds) - n_keep
    print(f"[features] {len(rows)} scoreable rows ({n_lex_scanned} lexical-scanned); "
          f"seeds {len(seeds)} = KEEP {n_keep} + ARCHIVE_CANDIDATE {n_arch}; "
          f"unlabeled {len(rows) - len(seeds)}")
    print("[boundary] " + __doc__.split("BOUNDARY DECLARATION", 1)[1].strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
