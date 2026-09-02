#!/usr/bin/env python3
"""missions-tree-index.py -- the project tree's generator + validator (spec s.2 A+B; s.8 prerequisite 3).

THE ONE READER THAT LEARNS THE TREE. Every other reader keeps reading the flat index
org/projects/<CODE>.json unchanged; this tool keeps that index TRUE for tree projects and REFUSES
the states the contract names. Contract (DATA): org/standards/PROJECT_TREE.contract.json.
Macro enum (DATA): org/missions/MACROS.yaml.

  check              (default) tree <-> index <-> DIRECTIVES.yaml; every denominator printed;
                     exit 0 clean / 1 violation(s) / 2 error. NEVER writes.
  check --json       the same as machine-readable JSON (violations + denominators).
  derive             print the index entries the tree implies and the DIRECTIVES.yaml additions.
  derive --write     write/refresh GENERATED index entries ONLY (an entry carrying `home`). A
                     hand-written flat row is never overwritten (refusal R3). DIRECTIVES.yaml is
                     NEVER written: it is validated (R5) and the exact additions are printed.
  --self-test        N/N on a scratch estate: the empty-tree baseline, a planted valid project
                     (red INDEX-MISSING -> derive --write -> green), and one planted mutant per
                     refusal. Every arm asserts the EXACT violation-id set, so a green arm is
                     reachable only from a different truth than the red ones. Run it before
                     trusting a report.

RED-FIRST BASELINE (s.8 prerequisite 3): against today's flat register with an EMPTY tree, `check`
reports 0 tree projects and 0 violations. DIRECTIVES.yaml's projects: lists stay hand-edited for
flat projects (s.8: no migration); this tool adds nothing to them and refuses when a TREE project
is missing from them.

Paths are derived from this file's location (workspace root = parent of .tools/); every path can
be overridden for fixtures (--root/--projects/--directives/--macros/--contract). No non-ASCII.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:  # fail closed, loud -- a YAML-less read would report a false zero
    yaml = None

_WS = Path(__file__).resolve().parent.parent
_DEFAULTS = {
    "contract": _WS / "org" / "standards" / "PROJECT_TREE.contract.json",
    "root": _WS / "org" / "missions",
    "projects": _WS / "org" / "projects",
    "directives": _WS / "org" / "missions" / "DIRECTIVES.yaml",
    "macros": _WS / "org" / "missions" / "MACROS.yaml",
}
TOOL_NAME = ".tools/missions-tree-index.py"


class Estate:
    """One estate = one contract + one tree root + one flat index + one DIRECTIVES + one MACROS."""

    def __init__(self, contract: Path, root: Path, projects: Path, directives: Path, macros: Path):
        if yaml is None:
            raise SystemExit("ERROR: PyYAML is not importable -- refusing to read DIRECTIVES.yaml/MACROS.yaml without it")
        self.contract = json.loads(Path(contract).read_text(encoding="utf-8"))
        self.root = Path(root)
        self.projects = Path(projects)
        self.directives_path = Path(directives)
        self.macros_path = Path(macros)
        lv = {level["name"]: level for level in self.contract["levels"]}
        self.re_dir = re.compile(lv["directive"]["regex"])
        self.re_mac = re.compile(lv["macro"]["regex"])
        self.re_prj = re.compile(lv["project"]["regex"])
        self.ratified_prefix = lv["macro"].get("ratified_value_prefix", "RATIFIED")
        self.row_file = self.contract["project_folder"]["row"]
        self.required = list(self.contract["project_folder"]["row_required_fields"])
        self.idx_marker = self.contract["index"]["generated_marker_field"]
        self.compared = list(self.contract["index"]["compared_fields"])
        self.index_root_rel = self.contract["index"]["root"]
        self.tree_root_rel = self.contract["root"]

    # ---------- loaders ----------
    def load_macros(self):
        d = yaml.safe_load(self.macros_path.read_text(encoding="utf-8")) or {}
        out = {}
        for D, v in (d.get("directives") or {}).items():
            out[str(D)] = {
                "macros": [str(m) for m in (v.get("macros") or [])],
                "ratification": str(v.get("ratification") or ""),
            }
        return out

    def load_directives(self):
        d = yaml.safe_load(self.directives_path.read_text(encoding="utf-8")) or {}
        out = {}
        for D, v in (d.get("directives") or {}).items():
            mem = (v or {}).get("members") or {}
            projs = mem.get("projects") if isinstance(mem, dict) else None
            if projs is None:
                projs = (v or {}).get("projects") or []
            out[str(D)] = [str(p) for p in projs]
        return out

    def load_flat(self):
        """{code: (row, is_generated, path)} over org/projects/*.json; parse errors are rows too."""
        out = {}
        errors = []
        if not self.projects.is_dir():
            return out, errors
        for p in sorted(self.projects.glob("*.json")):
            try:
                row = json.loads(p.read_text(encoding="utf-8"))
            except Exception as e:  # noqa: BLE001
                errors.append((p, f"parse error: {e}"))
                continue
            if not isinstance(row, dict):
                errors.append((p, "not a JSON object"))
                continue
            code = str(row.get("project_code") or p.stem)
            out[code] = (row, bool(row.get(self.idx_marker)), p)
        return out, errors

    def scan_tree(self):
        """Yield dicts: {D, M, code, folder, row|None, problems[]} plus level-name violations."""
        found = []
        level_viol = []
        if not self.root.is_dir():
            return found, level_viol
        for Dp in sorted(self.root.iterdir()):
            if not Dp.is_dir() or not self.re_dir.match(Dp.name):
                continue  # the MSTR mission register lives beside the tree and is not read
            for Mp in sorted(Dp.iterdir()):
                if not Mp.is_dir():
                    continue
                if not self.re_mac.match(Mp.name):
                    level_viol.append(("R1", self._rel(Mp), f"macro folder {Mp.name!r} fails {self.re_mac.pattern}"))
                    continue
                for Pp in sorted(Mp.iterdir()):
                    if not Pp.is_dir():
                        continue
                    if not self.re_prj.match(Pp.name):
                        level_viol.append(("R1", self._rel(Pp), f"project folder {Pp.name!r} fails {self.re_prj.pattern}"))
                        continue
                    rowp = Pp / self.row_file
                    row = None
                    problems = []
                    if not rowp.is_file():
                        problems.append(("ROW-MISSING", f"no {self.row_file}"))
                    else:
                        try:
                            row = json.loads(rowp.read_text(encoding="utf-8"))
                            if not isinstance(row, dict):
                                row = None
                                problems.append(("ROW-FIELD", "row is not a JSON object"))
                        except Exception as e:  # noqa: BLE001
                            problems.append(("ROW-FIELD", f"row parse error: {e}"))
                    found.append({"D": Dp.name, "M": Mp.name, "code": Pp.name, "folder": Pp, "row": row, "problems": problems})
        return found, level_viol

    def _rel(self, p: Path) -> str:
        try:
            return str(Path(p).resolve().relative_to(self.root.resolve().parent.parent)).replace("\\", "/")
        except Exception:  # noqa: BLE001
            return str(p).replace("\\", "/")

    def home_of(self, t) -> str:
        return f"{self.tree_root_rel}/{t['D']}/{t['M']}/{t['code']}"

    # ---------- the check ----------
    def check(self):
        macros = self.load_macros()
        directives = self.load_directives()
        flat, flat_errors = self.load_flat()
        tree, viol = self.scan_tree()
        viol = list(viol)
        for p, msg in flat_errors:
            viol.append(("ROW-FIELD", self._rel(p), msg))
        seen = {}
        valid = []
        for t in tree:
            path = self.home_of(t)
            for pid, msg in t["problems"]:
                viol.append((pid, path, msg))
            row = t["row"]
            if row is None:
                continue
            ok = True
            for f in self.required:
                if f not in row or row[f] in (None, ""):
                    viol.append(("ROW-FIELD", path, f"missing required field {f!r}"))
                    ok = False
            code = str(row.get("project_code") or "")
            if code and not self.re_prj.match(code):
                viol.append(("R1", path, f"project_code {code!r} fails {self.re_prj.pattern}"))
                ok = False
            # R4 path agreement
            if str(row.get("directive")) != t["D"]:
                viol.append(("R4", path, f"row directive {row.get('directive')!r} != folder {t['D']!r}"))
                ok = False
            if str(row.get("macro_code")) != t["M"]:
                viol.append(("R4", path, f"row macro_code {row.get('macro_code')!r} != folder {t['M']!r}"))
                ok = False
            if code and code.split("_", 1)[0] != t["M"]:
                viol.append(("R4", path, f"code prefix {code.split('_', 1)[0]!r} != macro folder {t['M']!r}"))
                ok = False
            if code != t["code"]:
                viol.append(("R4", path, f"row project_code {code!r} != folder {t['code']!r}"))
                ok = False
            # R2 macro ratified under this directive
            m = macros.get(t["D"])
            if m is None or t["M"] not in m["macros"]:
                viol.append(("R2", path, f"macro {t['M']!r} not in MACROS.yaml directives.{t['D']}.macros"))
                ok = False
            elif not m["ratification"].startswith(self.ratified_prefix):
                viol.append(("R2", path, f"MACROS.yaml directives.{t['D']}.ratification = {m['ratification']!r} (not {self.ratified_prefix})"))
                ok = False
            # R3 uniqueness
            key = t["code"]
            if key in seen:
                viol.append(("R3", path, f"project_code {key!r} also at {seen[key]}"))
                ok = False
            seen[key] = path
            if key in flat and not flat[key][1]:
                viol.append(("R3", path, f"hand-written flat row {self._rel(flat[key][2])} carries the same code -- delete it in the same commit as the tree row (the move), then derive --write"))
                ok = False
            # R5 directives list
            if key not in directives.get(t["D"], []):
                viol.append(("R5", path, f"{key!r} absent from DIRECTIVES.yaml directives.{t['D']}.members.projects"))
            if ok:
                valid.append(t)
        # index consistency for valid tree projects
        tree_homes = {self.home_of(t): t for t in tree if t["row"] is not None}
        for t in valid:
            key = t["code"]
            if key not in flat:
                viol.append(("INDEX-MISSING", self.home_of(t), f"no {self.index_root_rel}/{key}.json (remedy: derive --write)"))
                continue
            row, gen, p = flat[key]
            if not gen:
                continue  # already an R3 above
            expect = self.compose_index(t)
            for f in self.compared:
                if row.get(f) != expect.get(f):
                    viol.append(("INDEX-DRIFT", self._rel(p), f"{f}: index={row.get(f)!r} tree={expect.get(f)!r}"))
            if str(row.get(self.idx_marker)) != self.home_of(t):
                viol.append(("INDEX-DRIFT", self._rel(p), f"home: index={row.get(self.idx_marker)!r} tree={self.home_of(t)!r}"))
        for code, (row, gen, p) in flat.items():
            if gen and str(row.get(self.idx_marker)) not in tree_homes:
                viol.append(("INDEX-ORPHAN", self._rel(p), f"home {row.get(self.idx_marker)!r} has no tree row"))
        denom = {
            "tree_projects": len(tree),
            "tree_directive_folders": len({t["D"] for t in tree}),
            "tree_valid": len(valid),
            "flat_rows": len(flat),
            "flat_generated": sum(1 for v in flat.values() if v[1]),
            "flat_hand_written": sum(1 for v in flat.values() if not v[1]),
            "flat_parse_errors": len(flat_errors),
            "directives_listed": len(directives),
            "directives_entries": sum(len(v) for v in directives.values()),
            "macros_directives": len(macros),
            "macros_ratified": sum(1 for v in macros.values() if v["ratification"].startswith(self.ratified_prefix)),
        }
        viol.sort(key=lambda v: (v[0], v[1], v[2]))
        return viol, denom, valid, directives

    # ---------- derive ----------
    def compose_index(self, t) -> dict:
        row = t["row"]
        out = {
            "project_code": t["code"],
            self.idx_marker: self.home_of(t),
            "directive": t["D"],
            "macro_code": t["M"],
            "fabric": row.get("fabric"),
            "dep_stage": row.get("dep_stage"),
            "status": row.get("status"),
            "name": row.get("name"),
            "generated_from": f"{self.home_of(t)}/{self.row_file}",
            "generated_by": TOOL_NAME,
        }
        return out

    def derive(self, write: bool):
        viol, denom, valid, directives = self.check()
        flat, _ = self.load_flat()
        tree, _ = self.scan_tree()
        written, refused, planned = [], [], []
        valid_codes = {t["code"] for t in valid}
        for t in tree:
            key = t["code"]
            if t["row"] is None:
                continue
            if key in flat and not flat[key][1]:
                refused.append((key, "hand-written flat row exists (R3) -- not overwritten"))
                continue
            if key not in valid_codes:
                refused.append((key, "tree row has check violations -- run `check`"))
                continue
            entry = self.compose_index(t)
            target = self.projects / f"{key}.json"
            planned.append((key, entry))
            if write:
                existing = flat[key][0] if key in flat else {}
                entry["generated_at"] = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                same = all(existing.get(f) == entry.get(f) for f in self.compared + [self.idx_marker, "generated_from"])
                if same and existing:
                    continue
                self.projects.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps(entry, indent=1, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")
                written.append(key)
        additions = {}
        for t in valid:
            if t["code"] not in directives.get(t["D"], []):
                additions.setdefault(t["D"], []).append(t["code"])
        return planned, written, refused, additions, viol, denom


# ---------- CLI ----------
def _print_check(viol, denom, as_json=False):
    if as_json:
        print(json.dumps({"violations": [{"id": a, "path": b, "detail": c} for a, b, c in viol], "denominators": denom}, indent=1))
        return
    print("missions-tree-index check: tree={tree_projects} project(s) under {tree_directive_folders} directive folder(s), {tree_valid} valid"
          " | flat index rows={flat_rows} (generated={flat_generated}, hand-written={flat_hand_written}, parse-errors={flat_parse_errors})"
          " | DIRECTIVES.yaml: {directives_entries} entries across {directives_listed} directives"
          " | MACROS.yaml: {macros_ratified} of {macros_directives} directive(s) RATIFIED".format(**denom))
    for a, b, c in viol:
        print(f"  [{a}] {b}: {c}")
    print(f"RESULT: {len(viol)} violation(s)  (denominators on the first line; 0 tree projects is the s.8 baseline, not a blank read)")


def _estate(args) -> Estate:
    return Estate(args.contract, args.root, args.projects, args.directives, args.macros)


def cmd_check(args) -> int:
    viol, denom, _, _ = _estate(args).check()
    _print_check(viol, denom, args.json)
    return 1 if viol else 0


def cmd_derive(args) -> int:
    planned, written, refused, additions, viol, denom = _estate(args).derive(args.write)
    print(f"missions-tree-index derive: {len(planned)} generated entr{'y' if len(planned) == 1 else 'ies'} implied by the tree"
          f" ({'WRITTEN ' + str(len(written)) if args.write else 'dry run, nothing written'}); {len(refused)} refused")
    for key, entry in planned:
        print(f"  {'WRITE' if args.write and key in written else 'PLAN '} org/projects/{key}.json  home={entry['home']} dep_stage={entry['dep_stage']} fabric={entry['fabric']} status={entry['status']}")
    for key, why in refused:
        print(f"  REFUSE {key}: {why}")
    if additions:
        print("DIRECTIVES.yaml additions needed (NOT written -- lane TIER0_DIRECTIVES_REGISTER):")
        for D, codes in sorted(additions.items()):
            print(f"  directives.{D}.members.projects += {codes}")
    else:
        print("DIRECTIVES.yaml: no additions needed")
    other = [v for v in viol if v[0] not in ("INDEX-MISSING",)]
    if other:
        print(f"check violations present ({len(other)}) -- run `check`; derive only writes for VALID tree projects")
    return 1 if other else 0


# ---------- self-test ----------
def self_test() -> int:
    results = []

    def chk(name, ok, detail=""):
        results.append((name, ok, detail))

    real_contract = _DEFAULTS["contract"]
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)

        def fresh(name):
            e = base / name
            (e / "org" / "missions").mkdir(parents=True)
            (e / "org" / "projects").mkdir(parents=True)
            (e / "org" / "missions" / "MACROS.yaml").write_text(
                "version: 1\ndirectives:\n  D8:\n    macros: [ETFS]\n    ratification: RATIFIED test\n  D0:\n    macros: [NFRA]\n    ratification: PROPOSED\n",
                encoding="utf-8")
            (e / "org" / "missions" / "DIRECTIVES.yaml").write_text(
                "version: 1\ndirectives:\n  D8:\n    members:\n      projects: [ETFS_GUARDRAIL, MDPF_FLATONE]\n  D0:\n    members:\n      projects: []\n",
                encoding="utf-8")
            (e / "org" / "projects" / "MDPF_FLATONE.json").write_text(
                json.dumps({"project_code": "MDPF_FLATONE", "directive": "D8", "macro_code": "MDPF", "status": "active", "dep_stage": "PRD", "fabric": "laptop"}),
                encoding="utf-8")
            return Estate(real_contract, e / "org" / "missions", e / "org" / "projects", e / "org" / "missions" / "DIRECTIVES.yaml", e / "org" / "missions" / "MACROS.yaml")

        def plant(est, D, M, code, **over):
            folder = est.root / D / M / code
            folder.mkdir(parents=True, exist_ok=True)
            row = {"project_code": code, "macro_code": M, "directive": D, "fabric": "laptop", "dep_stage": "PRD", "status": "active", "name": f"{code} name"}
            row.update(over)
            (folder / "project.json").write_text(json.dumps(row), encoding="utf-8")
            return folder

        def ids(viol):
            return sorted({v[0] for v in viol})

        # 1. empty-tree baseline: flat rows only, 0 violations, listed == flat
        est = fresh("t1")
        viol, denom, _, dirs = est.check()
        chk("baseline empty tree -> 0 violations, 0 tree projects", not viol and denom["tree_projects"] == 0, str(ids(viol)))
        chk("baseline denominators name the flat register", denom["flat_rows"] == 1 and denom["flat_hand_written"] == 1 and denom["directives_entries"] == 2, json.dumps(denom))

        # 2. red: valid tree project, no index entry -> exactly INDEX-MISSING
        est = fresh("t2")
        plant(est, "D8", "ETFS", "ETFS_GUARDRAIL")
        viol, denom, _, _ = est.check()
        chk("planted valid project without index -> exactly [INDEX-MISSING]", ids(viol) == ["INDEX-MISSING"], str(ids(viol)))
        # 3. derive --write -> entry with home; check green
        planned, written, refused, additions, _, _ = est.derive(write=True)
        idx = est.projects / "ETFS_GUARDRAIL.json"
        chk("derive --write writes one generated entry carrying home", written == ["ETFS_GUARDRAIL"] and idx.is_file() and json.loads(idx.read_text(encoding="utf-8")).get("home") == "org/missions/D8/ETFS/ETFS_GUARDRAIL", str(written))
        viol, _, _, _ = est.check()
        chk("after derive --write -> 0 violations (green reached from the red)", not viol, str(ids(viol)))
        chk("derive reports no DIRECTIVES.yaml additions when listed", additions == {}, str(additions))
        # 4. R1 bad project folder name
        est = fresh("t4")
        plant(est, "D8", "ETFS", "ETFS_gd")
        viol, _, _, _ = est.check()
        chk("mutant R1 (folder fails regex) -> exactly [R1]", ids(viol) == ["R1"], str(ids(viol)))
        # 5. R2a macro not in list
        est = fresh("t5")
        plant(est, "D8", "MDPF", "MDPF_TESTONE")
        viol, _, _, _ = est.check()
        chk("mutant R2 (macro not in enum) -> [R2, R5]", ids(viol) == ["R2", "R5"], str(ids(viol)))
        # 6. R2b macro listed but PROPOSED
        est = fresh("t6")
        plant(est, "D0", "NFRA", "NFRA_TESTONE")
        viol, _, _, _ = est.check()
        chk("mutant R2 (enum PROPOSED, not RATIFIED) -> [R2, R5]", ids(viol) == ["R2", "R5"], str(ids(viol)))
        # 7. R3 hand-written flat row with the same code
        est = fresh("t7")
        plant(est, "D8", "ETFS", "ETFS_GUARDRAIL")
        (est.projects / "ETFS_GUARDRAIL.json").write_text(json.dumps({"project_code": "ETFS_GUARDRAIL", "directive": "D8", "status": "active"}), encoding="utf-8")
        viol, _, _, _ = est.check()
        chk("mutant R3 (hand-written flat twin) -> exactly [R3]", ids(viol) == ["R3"], str(ids(viol)))
        planned, written, refused, _, _, _ = est.derive(write=True)
        chk("derive --write REFUSES to overwrite the hand-written twin", written == [] and refused and "home" not in json.loads((est.projects / "ETFS_GUARDRAIL.json").read_text(encoding="utf-8")), str(refused))
        # 8. R4 row/path disagreement
        est = fresh("t8")
        plant(est, "D8", "ETFS", "ETFS_GUARDRAIL", directive="D0")
        viol, _, _, _ = est.check()
        chk("mutant R4 (row directive != folder) -> exactly [R4]", ids(viol) == ["R4"], str(ids(viol)))
        # 9. R5 tree project absent from DIRECTIVES list
        est = fresh("t9")
        plant(est, "D8", "ETFS", "ETFS_OTHERONE")
        est.derive(write=True)
        viol, _, _, _ = est.check()
        chk("mutant R5 (not in DIRECTIVES.yaml) -> exactly [R5]", ids(viol) == ["R5"], str(ids(viol)))
        _, _, _, additions, _, _ = est.derive(write=False)
        chk("derive names the exact DIRECTIVES.yaml addition", additions == {"D8": ["ETFS_OTHERONE"]}, str(additions))
        # 10. INDEX-DRIFT
        est = fresh("t10")
        plant(est, "D8", "ETFS", "ETFS_GUARDRAIL")
        est.derive(write=True)
        p = est.projects / "ETFS_GUARDRAIL.json"
        j = json.loads(p.read_text(encoding="utf-8"))
        j["dep_stage"] = "EXECUTING"
        p.write_text(json.dumps(j), encoding="utf-8")
        viol, _, _, _ = est.check()
        chk("mutant INDEX-DRIFT (generated entry edited) -> exactly [INDEX-DRIFT]", ids(viol) == ["INDEX-DRIFT"], str(ids(viol)))
        # 11. INDEX-ORPHAN
        est = fresh("t11")
        folder = plant(est, "D8", "ETFS", "ETFS_GUARDRAIL")
        est.derive(write=True)
        (folder / "project.json").unlink()
        folder.rmdir()
        viol, _, _, _ = est.check()
        chk("mutant INDEX-ORPHAN (tree row removed) -> exactly [INDEX-ORPHAN]", ids(viol) == ["INDEX-ORPHAN"], str(ids(viol)))
        # 12. ROW-MISSING
        est = fresh("t12")
        (est.root / "D8" / "ETFS" / "ETFS_GUARDRAIL").mkdir(parents=True)
        viol, _, _, _ = est.check()
        chk("mutant ROW-MISSING (folder without project.json) -> exactly [ROW-MISSING]", ids(viol) == ["ROW-MISSING"], str(ids(viol)))
        # 13. non-tree siblings under the root are ignored
        est = fresh("t13")
        (est.root / "INFRASTRUCTURE" / "GRAPH").mkdir(parents=True)
        (est.root / "INFRASTRUCTURE" / "GRAPH" / "state.yaml").write_text("x: 1\n", encoding="utf-8")
        viol, denom, _, _ = est.check()
        chk("MSTR mission register beside the tree is not read", not viol and denom["tree_projects"] == 0, str(ids(viol)))

    n_ok = sum(1 for _, ok, _ in results if ok)
    for name, ok, detail in results:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + ("" if ok else f"  -- {detail}"))
    print(f"missions-tree-index --self-test: {n_ok}/{len(results)} {'PASS' if n_ok == len(results) else 'FAIL'}")
    return 0 if n_ok == len(results) else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="missions-tree-index", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", nargs="?", default="check", choices=["check", "derive"])
    ap.add_argument("--write", action="store_true", help="derive: write generated index entries")
    ap.add_argument("--json", action="store_true", help="check: machine-readable output")
    ap.add_argument("--self-test", action="store_true")
    for k, v in _DEFAULTS.items():
        ap.add_argument(f"--{k}", default=str(v))
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    try:
        return cmd_check(args) if args.mode == "check" else cmd_derive(args)
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
