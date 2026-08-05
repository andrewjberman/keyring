"""rcg/ folder-cleanliness gate: the tree must be a subset of MANIFEST.yaml allowed_paths.

The folder contract's enforcement (NFRA_REPOCOHERENCEGRAPH PRD s.12): INTENT = the manifest
allowlist; DENOMINATOR = tracked + staged files under rcg/, enumerated from git at run time;
the GAP is printed and any gap is a DENY (rc=2). append_only files additionally require the
HEAD version to be a byte-prefix of the working version -- history is never edited.

Standalone by design (runnable today, solo posture R-0001); commit-chain wiring is the
D-0001 CTO ferry item. rc: 0 clean / 2 deny / 3 cannot-evaluate (never a silent pass).
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

WS = Path(__file__).resolve().parents[2]
MANIFEST = WS / "rcg" / "MANIFEST.yaml"


def git(*args: str) -> str:
    out = subprocess.run(["git", *args], cwd=WS, capture_output=True, text=True)
    if out.returncode != 0:
        print(f"BLOCKED: git {' '.join(args)} rc={out.returncode}: {out.stderr.strip()}")
        sys.exit(3)
    return out.stdout


def load_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", errors="replace") as h:
        return [json.loads(line) for line in h if line.strip()]


def label_vs_warrant() -> tuple[list[str], list[str]]:
    """Cycle-4 policy s.3 (CTO~B 212158Z): a path's FINAL label (last-row-wins) must match
    the ratified verdict of the covering VERDICTS.jsonl prefix row. Descent-only review
    passed the 2026-08-04 label-constant defect; this pass fails it. A final row citing a
    DIFFERENT ruling than the verdict's is a legitimate later adjudication -> INFO, not
    DENY. Returns (violations, infos); coverage denominator is printed by the caller."""
    verdicts_p = WS / "rcg" / "rulings" / "VERDICTS.jsonl"
    ledger_p = WS / "rcg" / "ledger" / "LABELS.jsonl"
    if not verdicts_p.exists() or not ledger_p.exists():
        return [], []
    rows = load_jsonl(verdicts_p)
    verdicts = [v for v in rows
                if v.get("ruling") and v.get("path_prefix") and v.get("verdict")]
    # law_pinned rows (R-0026 item 4): standing law names the file's home, so any
    # relocation/removal label (MIGRATE, ARCHIVE) is illegal regardless of what ruling
    # the row cites -- label-vs-LAW, the class label-vs-warrant cannot see. Optional
    # path_suffix narrows a prefix (docs/architecture/ + _PRD.md, not the whole dir).
    pins = [v for v in rows if v.get("type") == "law_pinned" and v.get("path_prefix")]
    final: dict[str, dict] = {}
    for r in load_jsonl(ledger_p):
        if r.get("path") and r.get("label"):
            final[r["path"]] = r
    violations: list[str] = []
    infos: list[str] = []
    checked = 0
    for path, row in final.items():
        for pin in pins:
            if not path.startswith(pin["path_prefix"]):
                continue
            if pin.get("path_suffix") and not path.endswith(pin["path_suffix"]):
                continue
            if (row.get("label") or "").upper() in ("MIGRATE", "ARCHIVE"):
                violations.append(
                    f"{path}: final label {row.get('label')} on a LAW-PINNED path "
                    f"({pin.get('cite', pin['path_prefix'])}) -- relocation/removal labels "
                    f"are illegal here regardless of citing ruling")
    for path, row in final.items():
        for v in verdicts:
            if not path.startswith(v["path_prefix"]):
                continue
            checked += 1
            if (row.get("label") or "").upper() == v["verdict"]:
                continue
            msg = (f"{path}: final label {row.get('label')} (source={row.get('source')}, "
                   f"cites {row.get('ruling')}) vs {v['ruling']} verdict {v['verdict']} "
                   f"for prefix {v['path_prefix']}")
            if row.get("ruling") == v["ruling"] or not row.get("ruling"):
                violations.append(msg)
            else:
                infos.append(msg)
    print(f"label-vs-warrant: {checked} final-state path(s) under {len(verdicts)} "
          f"verdict prefix(es); violations {len(violations)}, "
          f"later-ruling overrides (INFO) {len(infos)}")
    return violations, infos


def main() -> int:
    spec = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    allowed = set(spec["allowed_paths"])
    append_only = set(spec.get("append_only", []))

    tracked = {p for p in git("ls-files", "--", "rcg/").splitlines() if p}
    # --diff-filter=d: a staged DELETION leaves the population -- without it, removing a
    # leaked file re-flags the removal itself (measured on the scans/ CRLF-leak cleanup)
    staged = {p for p in git("diff", "--cached", "--name-only", "--diff-filter=d",
                             "--", "rcg/").splitlines() if p}
    population = tracked | staged
    extras = sorted(population - allowed)

    tampered: list[str] = []
    for path in sorted(append_only & population):
        head = subprocess.run(["git", "show", f"HEAD:{path}"], cwd=WS,
                              capture_output=True)
        if head.returncode != 0:
            continue  # not yet in HEAD -- first commit of the file, nothing to protect
        # Compare LINE CONTENT, not raw bytes: git stores LF-normalized blobs while the
        # Windows working copy may carry CRLF (git status reads clean across that gap; a
        # raw startswith read all four ledgers as tampered on the first exercised control).
        current = (WS / path).read_bytes().replace(b"\r\n", b"\n")
        if not current.startswith(head.stdout.replace(b"\r\n", b"\n")):
            tampered.append(path)

    print(f"rcg-manifest-check: DENOMINATOR {len(population)} tracked+staged file(s) under "
          f"rcg/ vs {len(allowed)} allowed; append-only checked: {len(append_only & population)}")
    lvw_violations, lvw_infos = label_vs_warrant()
    for m in lvw_infos:
        print(f"  INFO [later-ruling-override] {m}")
    if extras or tampered or lvw_violations:
        for p in extras:
            print(f"  DENY [not-in-manifest] {p}  -> amend rcg/MANIFEST.yaml in the SAME commit or remove")
        for p in tampered:
            print(f"  DENY [append-only-edited] {p}  -> prior lines are immutable; append, never edit")
        for m in lvw_violations:
            print(f"  DENY [label-vs-warrant] {m}  -> a row's label must implement the verdict of the ruling it cites; ESCALATE, never land")
        return 2
    print("  CLEAN -- tree is a subset of the manifest; append-only intact; labels match warrants.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
