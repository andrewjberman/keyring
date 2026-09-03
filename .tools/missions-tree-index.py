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
import ast
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


def _resolve_enum(path: Path, symbol: str) -> tuple:
    """Read ONE module-level literal assignment from a Python source by AST -- no import, no execution.

    The gate's enum is the only carrier (contract `value_enums`); a copy here would be a second
    carrier that drifts. Missing file or symbol FAILS CLOSED: an empty enum would read every row
    as invalid or every row as valid, and both are wrong silently."""
    if not path.is_file():
        raise SystemExit(f"ERROR: value-enum source {path} not found -- refusing to run without the gate's enum")
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == symbol:
                    val = ast.literal_eval(node.value)
                    if not isinstance(val, (tuple, list)) or not val:
                        raise SystemExit(f"ERROR: {symbol} in {path} is not a non-empty tuple/list literal")
                    return tuple(str(v) for v in val)
    raise SystemExit(f"ERROR: {symbol} not found as a module-level literal in {path} -- refusing to run without the gate's enum")


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
        # value enums: resolved from the GATE's source by AST (contract `value_enums`), one carrier
        self.enums = {}
        self.enum_sources = {}
        self.enum_norm = {}
        for field, spec in (self.contract.get("value_enums") or {}).items():
            if field.startswith("_") or not isinstance(spec, dict) or spec.get("no_enum"):
                continue
            src = _WS / spec["source"]
            self.enums[field] = _resolve_enum(src, spec["symbol"])
            self.enum_sources[field] = f"{spec['source']}:{spec['symbol']}"
            self.enum_norm[field] = spec.get("normalize", "exact")

    def _norm(self, field, value):
        v = str(value)
        return v.strip().lower() if self.enum_norm.get(field) == "lower" else v

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
            # ROW-ENUM: present-but-wrong against the gate's own enum (absence is ROW-FIELD above)
            for f, allowed in self.enums.items():
                v = row.get(f)
                if v not in (None, "") and self._norm(f, v) not in allowed:
                    viol.append(("ROW-ENUM", path, f"{f}={v!r} not in {allowed} (source {self.enum_sources[f]})"))
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
            # R6 the close: a CLOSED row needs the COO's report and the CTO's grades, on the header's outcomes, all REALIZED
            if str(row.get("dep_stage")) == CLOSE_STAGE:
                home = self.root / t["D"] / t["M"] / t["code"]
                hdr, rep, gr, errs = load_close_artifacts(home, t["code"], _WS / CLOSE_SCHEMA_REL)
                for rid, msg in close_violations(t["code"], hdr, rep, gr, errs):
                    viol.append((rid, path, msg))
                    ok = False
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
            "value_enums": {f: {"values": list(vals), "source": self.enum_sources[f]} for f, vals in self.enums.items()},
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
    for f, spec in denom.get("value_enums", {}).items():
        print(f"  value enum {f}: {len(spec['values'])} values from {spec['source']} (read by AST at run time)")
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
# ---- R6, THE CLOSE (Andrew-direct at the CTO terminal 2026-09-03 ~05:2xZ, record org/tier1_exec/1.0.0_SA_CTO/
# deliverables/ANDREW_DIRECT_20260903_052xZ_WHO_DECIDES_DONE_COO_COMPLETION_REPORT_CTO_GRADES_TWO_READS.md; spine L10
# "The close"). A tree row may read dep_stage CLOSED only when two documents exist under the project's ledger/ for the
# same round -- the COO's COMPLETION_REPORT (coverage: one row per outcome, the cells that served it, each proof) and the
# CTO's COMPLETION_GRADES (realization: one verdict per outcome against the exercised artifact) -- both valid against
# org/standards/COMPLETION_REPORT.schema.json, both covering EXACTLY the PRD header's endpoint_outcomes, and every grade
# REALIZED. Two reads on two axes; the flip is mechanical on the second. Nothing here waits on Andrew after L2.
CLOSE_STAGE = "CLOSED"
CLOSE_SCHEMA_REL = "org/standards/COMPLETION_REPORT.schema.json"
_ROUND_RE = re.compile(r"\.round(\d+)\.json$")
_FENCE_RE = re.compile(r"```json\s*(.*?)```", re.S)


def header_outcomes(prd_text):
    """The PRD header's endpoint_outcomes (the FIRST fenced json block of the PRD), or None when unreadable."""
    m = _FENCE_RE.search(prd_text or "")
    if not m:
        return None
    try:
        h = json.loads(m.group(1))
    except ValueError:
        return None
    v = h.get("endpoint_outcomes") if isinstance(h, dict) else None
    return [str(x) for x in v] if isinstance(v, list) else None


def close_violations(code, header_fwds, report, grades, schema_errors=()):
    """R6, PURE. `report` / `grades` are the parsed documents or None when absent; `schema_errors` are the
    jsonschema complaints the loader collected. Returns [(rule_id, message)] -- empty means the row may close."""
    out = []
    if header_fwds is None:
        return [("R6", f"{code}: PRD header endpoint_outcomes unreadable -- a CLOSED row cannot be graded; REFUSED fail-closed")]
    if report is None:
        out.append(("R6", f"{code}: dep_stage CLOSED but no ledger/COMPLETION_REPORT.round<N>.json -- the COO's report is the close's first read"))
    if grades is None:
        out.append(("R6", f"{code}: dep_stage CLOSED but no ledger/COMPLETION_GRADES.round<N>.json -- the CTO's grades are the close's second read"))
    for e in schema_errors:
        out.append(("R6", f"{code}: {e}"))
    if out:
        return out
    if report.get("kind") != "COMPLETION_REPORT" or grades.get("kind") != "COMPLETION_GRADES":
        out.append(("R6", f"{code}: close documents carry kind {report.get('kind')!r} / {grades.get('kind')!r}"))
    if report.get("round") != grades.get("round"):
        out.append(("R6", f"{code}: report round {report.get('round')!r} != grades round {grades.get('round')!r} -- the grades must grade THIS report"))
    want = set(header_fwds)
    rep_ids = [str(o.get("fwd_id")) for o in (report.get("outcomes") or [])]
    gr_ids = [str(r.get("fwd_id")) for r in (grades.get("rows") or [])]
    for label, ids_ in (("report", rep_ids), ("grades", gr_ids)):
        s = set(ids_)
        if len(ids_) != len(s):
            out.append(("R6", f"{code}: {label} repeats an fwd_id ({len(ids_)} rows, {len(s)} distinct)"))
        if s != want:
            out.append(("R6", f"{code}: {label} outcomes {sorted(s)} != PRD header {sorted(want)} (missing {sorted(want - s)}, extra {sorted(s - want)})"))
    not_real = [(r.get("fwd_id"), r.get("verdict")) for r in (grades.get("rows") or []) if r.get("verdict") != "REALIZED"]
    if not_real:
        out.append(("R6", f"{code}: CLOSED with {len(not_real)} of {len(gr_ids)} grade(s) not REALIZED: {not_real} -- a NOT_REALIZED re-enters at L5 or L2; NOT_EVALUATED is not a verdict"))
    # THE STATE BAR, mechanical (2026-09-03, 3.0.0_SA_CVO~A 93500: "the bar that produces that answer currently lives in a
    # message, which R6 cannot read"): a card whose DONE WHEN is EXERCISED is not met by an APPLIED citation, and no card is
    # met by ABSENT. The report row carries the card's state (done_when_state), the grade row carries what the grader saw
    # (state_observed); R6 compares the two per outcome. APPLIED is met by APPLIED or EXERCISED; EXERCISED only by EXERCISED.
    rank = {"ABSENT": 0, "APPLIED": 1, "EXERCISED": 2}
    want_state = {str(o.get("fwd_id")): o.get("done_when_state") for o in (report.get("outcomes") or [])}
    under = []
    for r in (grades.get("rows") or []):
        if r.get("verdict") != "REALIZED":
            continue
        need, seen = want_state.get(str(r.get("fwd_id"))), r.get("state_observed")
        if need in rank and (seen not in rank or rank[seen] < rank[need]):
            under.append((r.get("fwd_id"), need, seen))
    if under:
        out.append(("R6", f"{code}: {len(under)} REALIZED grade(s) cite a state BELOW the card's DONE WHEN: "
                          f"{[(f, 'needs ' + str(n), 'saw ' + str(s)) for f, n, s in under]} -- an EXERCISED card is not met by an APPLIED citation, and nothing is met by ABSENT"))
    wb = str(report.get("written_by") or "").split("~", 1)[0]
    gb = str(grades.get("graded_by") or "").split("~", 1)[0]
    if wb != "2.0.0_SA_COO":
        out.append(("R6", f"{code}: report written_by {report.get('written_by')!r}, not 2.0.0_SA_COO (the seat that knows the decomposition is spent)"))
    if gb != "1.0.0_SA_CTO":
        out.append(("R6", f"{code}: grades graded_by {grades.get('graded_by')!r}, not 1.0.0_SA_CTO (the owner of the DONE WHEN criteria)"))
    return out


def load_close_artifacts(home: Path, code: str, schema_path: Path):
    """(header_fwds, report, grades, schema_errors) for one project home. Reads the PRD header and the LATEST round
    of each close document under ledger/; validates each against the close schema. Fail-closed by construction:
    an unparseable document or an unimportable validator becomes a schema_error, never a skip."""
    prd = home / "prd" / f"{code}_PRD.md"
    hdr = header_outcomes(prd.read_text(encoding="utf-8")) if prd.is_file() else None
    errors = []

    def latest(glob):
        led = home / "ledger"
        cands = []
        if led.is_dir():
            for p in led.glob(glob):
                m = _ROUND_RE.search(p.name)
                if m:
                    cands.append((int(m.group(1)), p))
        if not cands:
            return None
        _n, p = max(cands)
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(f"{p.name} does not parse as JSON ({exc})")
            return None

    report = latest("COMPLETION_REPORT.round*.json")
    grades = latest("COMPLETION_GRADES.round*.json")
    if report is not None or grades is not None:
        try:
            import jsonschema  # noqa: WPS433 -- local import so the module loads without it
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            for label, doc in (("COMPLETION_REPORT", report), ("COMPLETION_GRADES", grades)):
                if doc is None:
                    continue
                for err in sorted(jsonschema.Draft7Validator(schema).iter_errors(doc), key=lambda e: list(e.path))[:5]:
                    ptr = "/" + "/".join(str(x) for x in err.path) if err.path else "/"
                    errors.append(f"{label} schema violation at {ptr} -- {err.message[:120]}")
        except ImportError:
            errors.append("jsonschema is not importable -- the close documents cannot be validated; REFUSED fail-closed")
        except (OSError, ValueError) as exc:
            errors.append(f"close schema {schema_path.name} unreadable ({exc}) -- REFUSED fail-closed")
    return hdr, report, grades, errors


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
        # 14. value enums resolve from the GATE by AST and agree with an independent regex read (grain)
        est = fresh("t14")
        gate_src = (_WS / ".tools" / "to-pipeline-gate.py").read_text(encoding="utf-8")

        def rx_enum(sym):
            m = re.search(r"^" + sym + r"\s*=\s*\((.*?)\)\s*$", gate_src, re.M)
            return tuple(s.strip().strip("'\"") for s in m.group(1).split(",") if s.strip()) if m else None

        chk("value enums resolved by AST == independent regex read of the gate (dep_stage, fabric)",
            est.enums.get("dep_stage") == rx_enum("DEP_STAGE_ENUM") and est.enums.get("fabric") == rx_enum("FABRIC_ENUM") and len(est.enums["dep_stage"]) >= 6,
            f"ast={est.enums} regex={rx_enum('DEP_STAGE_ENUM')},{rx_enum('FABRIC_ENUM')}")
        # 15. ROW-ENUM mutants: dep_stage BOGUS; fabric moon; fabric case-insensitive like the gate
        est = fresh("t15")
        plant(est, "D8", "ETFS", "ETFS_GUARDRAIL", dep_stage="BOGUS")
        est.derive(write=True)
        viol, _, _, _ = est.check()
        chk("mutant ROW-ENUM (dep_stage=BOGUS) -> exactly [ROW-ENUM]", ids(viol) == ["ROW-ENUM"], str(ids(viol)))
        # 16. R6 THE CLOSE -- pure arms first, then the loader end-to-end on a planted estate.
        H = ["FWD-1", "FWD-2"]
        rep_ok = {"kind": "COMPLETION_REPORT", "round": 2, "written_by": "2.0.0_SA_COO",
                  "outcomes": [{"fwd_id": "FWD-1"}, {"fwd_id": "FWD-2"}]}
        gr_ok = {"kind": "COMPLETION_GRADES", "round": 2, "graded_by": "1.0.0_SA_CTO",
                 "rows": [{"fwd_id": "FWD-1", "verdict": "REALIZED"}, {"fwd_id": "FWD-2", "verdict": "REALIZED"}]}
        r6 = lambda *a, **k: [m for _r, m in close_violations(*a, **k)]  # noqa: E731
        chk("R6 pure: header unreadable -> fail-closed", any("fail-closed" in m for m in r6("X", None, rep_ok, gr_ok)), "")
        chk("R6 pure: no report -> named", any("COMPLETION_REPORT" in m for m in r6("X", H, None, gr_ok)), "")
        chk("R6 pure: no grades -> named", any("COMPLETION_GRADES" in m for m in r6("X", H, rep_ok, None)), "")
        chk("R6 pure: both present, ids == header, all REALIZED -> admitted", r6("X", H, rep_ok, gr_ok) == [], str(r6("X", H, rep_ok, gr_ok)))
        gr_ne = json.loads(json.dumps(gr_ok))
        gr_ne["rows"][1]["verdict"] = "NOT_EVALUATED"
        chk("R6 pure: one NOT_EVALUATED -> refused, names it", any("not REALIZED" in m and "FWD-2" in m for m in r6("X", H, rep_ok, gr_ne)), "")
        gr_short = json.loads(json.dumps(gr_ok))
        gr_short["rows"].pop()
        chk("R6 pure: grades miss FWD-2 -> denominator mismatch named", any("missing ['FWD-2']" in m for m in r6("X", H, rep_ok, gr_short)), str(r6("X", H, rep_ok, gr_short)))
        gr_rd = json.loads(json.dumps(gr_ok))
        gr_rd["round"] = 1
        chk("R6 pure: grades grade a different round -> refused", any("round" in m for m in r6("X", H, rep_ok, gr_rd)), "")
        gr_who = json.loads(json.dumps(gr_ok))
        gr_who["graded_by"] = "2.0.0_SA_COO"
        chk("R6 pure: grades by the COO -> refused (author separation)", any("graded_by" in m for m in r6("X", H, rep_ok, gr_who)), "")
        chk("R6 pure: schema errors surface as R6", any("boom" in m for m in r6("X", H, rep_ok, gr_ok, ["boom"])), "")
        # the state bar: the report's done_when_state vs the grade's state_observed
        rep_st = json.loads(json.dumps(rep_ok))
        rep_st["outcomes"] = [{"fwd_id": "FWD-1", "done_when_state": "EXERCISED"}, {"fwd_id": "FWD-2", "done_when_state": "APPLIED"}]
        gr_st = json.loads(json.dumps(gr_ok))
        gr_st["rows"] = [{"fwd_id": "FWD-1", "verdict": "REALIZED", "state_observed": "APPLIED"},
                         {"fwd_id": "FWD-2", "verdict": "REALIZED", "state_observed": "APPLIED"}]
        chk("R6 pure: EXERCISED card met by an APPLIED citation -> refused, names FWD-1 only",
            any("BELOW the card" in m and "FWD-1" in m and "FWD-2" not in m for m in r6("X", H, rep_st, gr_st)), str(r6("X", H, rep_st, gr_st)))
        gr_st2 = json.loads(json.dumps(gr_st))
        gr_st2["rows"][0]["state_observed"] = "EXERCISED"
        chk("R6 pure: EXERCISED met by EXERCISED, APPLIED met by APPLIED -> admitted", r6("X", H, rep_st, gr_st2) == [], str(r6("X", H, rep_st, gr_st2)))
        gr_st3 = json.loads(json.dumps(gr_st2))
        gr_st3["rows"][1]["state_observed"] = "ABSENT"
        chk("R6 pure: a REALIZED grade citing ABSENT -> refused", any("BELOW the card" in m and "FWD-2" in m for m in r6("X", H, rep_st, gr_st3)), "")
        gr_st4 = json.loads(json.dumps(gr_st2))
        gr_st4["rows"][1]["state_observed"] = "EXERCISED"
        chk("R6 pure: APPLIED card met by EXERCISED -> admitted (a stronger state satisfies a weaker card)", r6("X", H, rep_st, gr_st4) == [], "")
        # loader end-to-end: CLOSED row with nothing under ledger/ -> R6; with two valid docs -> no R6
        est = fresh("t16r6")
        plant(est, "D8", "ETFS", "ETFS_GUARDRAIL", dep_stage="CLOSED")
        est.derive(write=True)
        viol, _, _, _ = est.check()
        chk("planted CLOSED row, no close documents -> R6 present", "R6" in ids(viol), str(ids(viol)))
        home16 = est.root / "D8" / "ETFS" / "ETFS_GUARDRAIL"
        (home16 / "prd").mkdir(exist_ok=True)
        (home16 / "prd" / "ETFS_GUARDRAIL_PRD.md").write_text("# x\n\n```json\n{\"endpoint_outcomes\": [\"FWD-1\"]}\n```\n", encoding="utf-8")
        (home16 / "ledger").mkdir(exist_ok=True)
        (home16 / "ledger" / "COMPLETION_REPORT.round1.json").write_text(json.dumps({
            "kind": "COMPLETION_REPORT", "schema_version": "1.0", "project": "ETFS_GUARDRAIL", "round": 1,
            "written_by": "2.0.0_SA_COO", "written_utc": "2026-09-03T05:30Z", "decomposition_ref": "org/x/DECOMP.md@abcdef1234",
            "denominators": {"fwd_in_prd_header": 1, "cells_in_decomposition": 1, "task_orders": 1, "task_orders_terminal_with_valid_proof": 1},
            "outcomes": [{"fwd_id": "FWD-1", "done_when_state": "APPLIED", "done_when_text": "the list is in the PRD",
                          "cells": [{"cell_id": "C1", "task_orders": [{"id": "TO-1", "status": "complete", "proof_of_spec_ref": "org/x/TO-1.proof.json@abcdef1234"}]}],
                          "claim": "COVERED"}]}), encoding="utf-8")
        (home16 / "ledger" / "COMPLETION_GRADES.round1.json").write_text(json.dumps({
            "kind": "COMPLETION_GRADES", "schema_version": "1.0", "project": "ETFS_GUARDRAIL", "round": 1,
            "graded_by": "1.0.0_SA_CTO", "graded_utc": "2026-09-03T05:31Z", "report_ref": "org/x/ledger/COMPLETION_REPORT.round1.json@abcdef1234",
            "rows": [{"fwd_id": "FWD-1", "verdict": "REALIZED", "artifact_ref": "org/x/PRD.md@abcdef1234", "state_observed": "APPLIED"}]}), encoding="utf-8")
        viol, _, _, _ = est.check()
        chk("planted CLOSED row with valid report + grades, all REALIZED -> no R6", "R6" not in ids(viol), str(ids(viol)))
        (home16 / "ledger" / "COMPLETION_GRADES.round1.json").write_text("{not json", encoding="utf-8")
        viol, _, _, _ = est.check()
        chk("mutant: grades file unparseable -> R6 (fail-closed, never a skip)", "R6" in ids(viol), str(ids(viol)))
        est = fresh("t16")
        plant(est, "D8", "ETFS", "ETFS_GUARDRAIL", fabric="moon")
        est.derive(write=True)
        viol, _, _, _ = est.check()
        chk("mutant ROW-ENUM (fabric=moon) -> exactly [ROW-ENUM]", ids(viol) == ["ROW-ENUM"], str(ids(viol)))
        est = fresh("t17")
        plant(est, "D8", "ETFS", "ETFS_GUARDRAIL", fabric="Laptop")
        est.derive(write=True)
        viol, _, _, _ = est.check()
        chk("fabric 'Laptop' passes like the gate (lower-normalized) -> 0 violations", not viol, str(ids(viol)))

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
