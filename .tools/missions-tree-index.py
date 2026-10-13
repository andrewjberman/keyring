#!/usr/bin/env python3
"""missions-tree-index.py -- the project tree's generator + validator (spec s.2 A+B; s.8 prerequisite 3).

THE ONE READER THAT LEARNS THE TREE. Every other reader keeps reading the flat index
org/projects/<CODE>.json unchanged; this tool keeps that index TRUE for tree projects and REFUSES
the states the contract names. Contract (DATA): org/standards/PROJECT_TREE.contract.json.
Macro enum (DATA): org/missions/MACROS.yaml.

  check              (default) tree <-> index <-> DIRECTIVES.yaml; every denominator printed;
                     exit 0 clean / 1 violation(s) / 2 error. NEVER writes.
  check --json       the same as machine-readable JSON (violations + denominators).
  check --staged     read EVERY input (contract, tree rows, flat index, DIRECTIVES.yaml, MACROS.yaml, close
                     artifacts, the value-enum sources, the close schema) from the GIT INDEX git resolves
                     (honouring GIT_INDEX_FILE and GIT_DIR), never the working tree: the index blobs are
                     materialised into a private temp directory and the same reader runs there.
  check --act PATH   (repeatable; also --act-from-env VAR, newline-separated) scope the refusal to the act: a
                     violation in a project the act does not touch prints `STANDING <CODE> <rule> <path> <detail>`
                     and does not count toward the exit code. See ACT SCOPE below. Without --act: unchanged.
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
import importlib.util
import json
import os
import re
import shutil
import subprocess
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
CONTRACT_REL = "org/standards/PROJECT_TREE.contract.json"
DIRECTIVES_REL = "org/missions/DIRECTIVES.yaml"
MACROS_REL = "org/missions/MACROS.yaml"


# Register-derived value enums (NFRA_CTLPLN.TO-CT-ab-8): the symbols whose gate assignment is `tuple(_fabric_values())`
# rather than a literal. Their values come from the device register through lib/devices.py placement_values(), read at
# the same workspace root the gate is read from; a register that cannot be read FAILS CLOSED.
REGISTER_DERIVED_SYMBOLS = ("FABRIC_ENUM",)
REGISTER_RELS = ("lib/devices.py", "org/devices/DEVICES.json")


def _register_enum(symbol: str, path: Path, ws: Path) -> tuple:
    if symbol not in REGISTER_DERIVED_SYMBOLS:
        raise SystemExit(f"ERROR: {symbol} in {path} is not a literal and is not a register-derived enum -- refusing")
    lib = Path(ws) / "lib" / "devices.py"
    if not lib.is_file():
        raise SystemExit(f"ERROR: {symbol} is register-derived but {lib} is missing -- refusing (fail-closed)")
    spec = importlib.util.spec_from_file_location("opal_devices_for_index", str(lib))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    try:
        vals = mod.placement_values()
    except mod.RegisterError as exc:
        raise SystemExit(f"ERROR: {symbol} is register-derived but the device register cannot be read ({exc}) -- refusing (fail-closed)")
    if not vals:
        raise SystemExit(f"ERROR: {symbol} resolved to no values from the device register -- refusing (fail-closed)")
    return tuple(str(v) for v in vals)


def _resolve_enum(path: Path, symbol: str, ws: Path = None) -> tuple:
    """Read ONE module-level value enum from the gate's source by AST -- no import, no execution of the gate.

    A LITERAL assignment is read by ast.literal_eval. A symbol the gate DERIVES from the device register
    (REGISTER_DERIVED_SYMBOLS: FABRIC_ENUM = tuple(_fabric_values())) is not a literal; its value is the register's
    placement_values(), read through lib/devices.py under `ws`. The gate's assignment must still exist (fail closed).
    The gate's enum is the only carrier (contract `value_enums`); a copy here would be a second carrier that drifts.
    Missing file or symbol FAILS CLOSED: an empty enum would read every row as invalid or every row as valid, and both
    are wrong silently."""
    if not path.is_file():
        raise SystemExit(f"ERROR: value-enum source {path} not found -- refusing to run without the gate's enum")
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == symbol:
                    try:
                        val = ast.literal_eval(node.value)
                    except ValueError:
                        return _register_enum(symbol, path, ws if ws is not None else _WS)
                    if not isinstance(val, (tuple, list)) or not val:
                        raise SystemExit(f"ERROR: {symbol} in {path} is not a non-empty tuple/list literal")
                    return tuple(str(v) for v in val)
    raise SystemExit(f"ERROR: {symbol} not found as a module-level assignment in {path} -- refusing to run without the gate's enum")


class Estate:
    """One estate = one contract + one tree root + one flat index + one DIRECTIVES + one MACROS."""

    def __init__(self, contract: Path, root: Path, projects: Path, directives: Path, macros: Path,
                 ws: Path = None, index_only_scan: bool = True):
        if yaml is None:
            raise SystemExit("ERROR: PyYAML is not importable -- refusing to read DIRECTIVES.yaml/MACROS.yaml without it")
        self.ws = Path(ws) if ws is not None else _WS  # where the enum sources and the close schema are read from
        self.index_only_scan = index_only_scan  # False under --staged: every row is materialised already
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
        self.enum_origins = {}
        self.enum_norm = {}
        for field, spec in (self.contract.get("value_enums") or {}).items():
            if field.startswith("_") or not isinstance(spec, dict) or spec.get("no_enum"):
                continue
            src = self.ws / spec["source"]
            self.enums[field] = _resolve_enum(src, spec["symbol"], self.ws)
            self.enum_sources[field] = f"{spec['source']}:{spec['symbol']}"
            self.enum_origins[field] = ("derived from the device register via lib/devices.py placement_values()"
                                        if spec["symbol"] in REGISTER_DERIVED_SYMBOLS else "literal assignment in the source, read by AST")
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
        if self.index_only_scan:
            found.extend(self._index_only_projects({(t["D"], t["M"], t["code"]) for t in found}))
        return found, level_viol

    def _index_only_projects(self, seen):
        """Project rows the git INDEX holds but the worktree does not materialise -- a worker's sparse cone.

        The walk above sees only what is on disk, so on a sparse cone every project outside the cone read as
        INDEX-ORPHAN (24 false violations, row AMGT_HARVST-Z-W11-S1). The index still carries every path, so
        a row absent on disk is read from its index blob. On a full checkout nothing is index-only and this
        adds nothing; a root outside any git worktree (the self-test's scratch estate) adds nothing either."""
        import subprocess
        try:
            ls = subprocess.run(["git", "-C", str(self.root), "ls-files", "-z", "--full-name", "--", f"*/{self.row_file}"],
                                capture_output=True, text=True, timeout=60)
            top = subprocess.run(["git", "-C", str(self.root), "rev-parse", "--show-toplevel"],
                                 capture_output=True, text=True, timeout=30).stdout.strip()
        except Exception:  # noqa: BLE001
            return []
        if ls.returncode != 0 or not top:
            return []
        try:
            rel_root = self.root.resolve().relative_to(Path(top).resolve()).as_posix()
        except ValueError:
            return []
        out = []
        for full in filter(None, ls.stdout.split("\0")):
            parts = full[len(rel_root) + 1:].split("/") if full.startswith(rel_root + "/") else []
            if len(parts) != 4 or (parts[0], parts[1], parts[2]) in seen:
                continue
            D, M, code, _ = parts
            if not (self.re_dir.match(D) and self.re_mac.match(M) and self.re_prj.match(code)):
                continue
            if (self.root / D / M / code / self.row_file).exists():
                continue
            blob = subprocess.run(["git", "-C", str(self.root), "show", f":{full}"],
                                  capture_output=True, text=True, encoding="utf-8", timeout=30)
            row, problems = None, []
            try:
                row = json.loads(blob.stdout) if blob.returncode == 0 else None
                if not isinstance(row, dict):
                    row = None
                    problems.append(("ROW-FIELD", "row is not a JSON object (index blob)"))
            except Exception as e:  # noqa: BLE001
                problems.append(("ROW-FIELD", f"row parse error (index blob): {e}"))
            out.append({"D": D, "M": M, "code": code, "folder": self.root / D / M / code, "row": row, "problems": problems,
                        "index_only": True})
        return out

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
        r6_not_graded = []
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
            if str(row.get("dep_stage")) == CLOSE_STAGE and t.get("index_only"):
                # the close documents are not on disk outside a sparse cone; R6 is graded on a full checkout
                r6_not_graded.append(t["code"])
            elif str(row.get("dep_stage")) == CLOSE_STAGE:
                home = self.root / t["D"] / t["M"] / t["code"]
                hdr, rep, gr, errs = load_close_artifacts(home, t["code"], self.ws / CLOSE_SCHEMA_REL)
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
            "value_enums": {f: {"values": list(vals), "source": self.enum_sources[f], "origin": self.enum_origins[f]}
                            for f, vals in self.enums.items()},
        }
        if r6_not_graded:
            denom["r6_not_graded_index_only"] = sorted(r6_not_graded)
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

    def row_problems(self, t) -> list:
        """The row-level reasons ONE tree row cannot compose an index entry (ROW-FIELD, R1, ROW-ENUM, R4); [] when it can.
        The register-level rules (R2 macro, R3 uniqueness, R5 members, R6 close) read other files and stay with `check`."""
        row, out = t["row"], []
        if not isinstance(row, dict):
            return ["row is not a JSON object"]
        for f in self.required:
            if f not in row or row[f] in (None, ""):
                out.append(f"missing required field {f!r}")
        code = str(row.get("project_code") or "")
        if code and not self.re_prj.match(code):
            out.append(f"R1 project_code {code!r} fails {self.re_prj.pattern}")
        for f, allowed in self.enums.items():
            v = row.get(f)
            if v not in (None, "") and self._norm(f, v) not in allowed:
                out.append(f"ROW-ENUM {f}={v!r} not in {allowed}")
        if str(row.get("directive")) != t["D"]:
            out.append(f"R4 row directive {row.get('directive')!r} != folder {t['D']!r}")
        if str(row.get("macro_code")) != t["M"]:
            out.append(f"R4 row macro_code {row.get('macro_code')!r} != folder {t['M']!r}")
        if code and code.split("_", 1)[0] != t["M"]:
            out.append(f"R4 code prefix {code.split('_', 1)[0]!r} != macro folder {t['M']!r}")
        if code != t["code"]:
            out.append(f"R4 row project_code {code!r} != folder {t['code']!r}")
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


# ---------- --staged: the index, materialised ----------
class StagedReadError(Exception):
    """The git index could not be read as a whole estate -- fail closed (rc 2), never a partial read."""


def _git(args, repo, env, data=None):
    """Run git. With GIT_DIR or GIT_INDEX_FILE in the env the caller's cwd is kept (a relative value is relative to
    it); otherwise git runs in `repo`. Returns the CompletedProcess (bytes)."""
    cwd = None if (env.get("GIT_DIR") or env.get("GIT_INDEX_FILE")) else str(repo)
    try:
        return subprocess.run(["git"] + list(args), cwd=cwd, env=env, input=data, capture_output=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as e:
        raise StagedReadError(f"git {' '.join(args[:2])} could not run: {e}")


def _index_listing(repo, env, pathspecs):
    """[(mode, oid, stage, path)] for the index entries under the pathspecs."""
    r = _git(["ls-files", "-s", "-z", "--full-name", "--"] + [":(top)" + p for p in pathspecs], repo, env)
    if r.returncode != 0:
        raise StagedReadError("git ls-files failed rc=%s: %s" % (r.returncode, r.stderr.decode("utf-8", "replace").strip()[:300]))
    out = []
    for rec in filter(None, r.stdout.decode("utf-8", "replace").split("\0")):
        meta, _, path = rec.partition("\t")
        parts = meta.split()
        if len(parts) != 3:
            raise StagedReadError(f"unparseable ls-files record {rec[:120]!r}")
        out.append((parts[0], parts[1], parts[2], path))
    return out


def _blobs(repo, env, oids):
    """The bytes of each oid, in order, via ONE git cat-file --batch."""
    if not oids:
        return []
    r = _git(["cat-file", "--batch"], repo, env, data=("\n".join(oids) + "\n").encode("ascii"))
    if r.returncode != 0:
        raise StagedReadError("git cat-file --batch failed rc=%s: %s" % (r.returncode, r.stderr.decode("utf-8", "replace").strip()[:300]))
    buf, pos, out = r.stdout, 0, []
    for oid in oids:
        nl = buf.find(b"\n", pos)
        hdr = buf[pos:nl].split() if nl >= 0 else []
        if len(hdr) != 3 or hdr[1] != b"blob":
            raise StagedReadError(f"blob {oid} not readable from the object store ({buf[pos:nl][:80]!r})")
        size = int(hdr[2])
        out.append(buf[nl + 1:nl + 1 + size])
        pos = nl + 1 + size + 1
    return out


def materialise_index(repo, dest, env=None):
    """Write the inputs `check` reads, FROM THE INDEX, under `dest` at their repo-relative paths. The working tree is
    never read. Returns an Estate argument dict. Files written: the contract, the value-enum sources it names, the
    close schema, DIRECTIVES.yaml, MACROS.yaml, every tree project.json, every <CODE>_PRD.md and COMPLETION_*.json
    under a project, and every flat org/projects/*.json. A directory is made for every tracked path down to the
    project level so ROW-MISSING and the R1 level-name checks see the folders the index implies."""
    env = dict(os.environ if env is None else env)
    dest = Path(dest)

    def put(rel, data):
        f = dest / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(data)

    def stage0(entries, what):
        bad = [e[3] for e in entries if e[2] != "0"]
        if bad:
            raise StagedReadError(f"{what}: {len(bad)} unmerged index entr{'y' if len(bad) == 1 else 'ies'} (e.g. {bad[0]}) -- resolve the merge first")
        return [e for e in entries if e[0] != "160000"]

    ent = stage0(_index_listing(repo, env, [CONTRACT_REL]), "contract")
    if len(ent) != 1:
        raise StagedReadError(f"{CONTRACT_REL} is not in the git index")
    contract_bytes = _blobs(repo, env, [ent[0][1]])[0]
    put(CONTRACT_REL, contract_bytes)
    contract = json.loads(contract_bytes.decode("utf-8"))
    tree_rel, idx_rel = contract["root"], contract["index"]["root"]
    row_file = contract["project_folder"]["row"]
    extra = [CLOSE_SCHEMA_REL] + list(REGISTER_RELS) + [spec["source"] for f, spec in (contract.get("value_enums") or {}).items()
                                  if not f.startswith("_") and isinstance(spec, dict) and not spec.get("no_enum")]
    entries = stage0(_index_listing(repo, env, [tree_rel, idx_rel] + extra), "tree/index/enum sources")
    (dest / tree_rel).mkdir(parents=True, exist_ok=True)
    (dest / idx_rel).mkdir(parents=True, exist_ok=True)
    want, seen_extra, dirs = [], set(), set()
    for _mode, oid, _stage, path in entries:
        if path in extra:
            want.append((oid, path))
            seen_extra.add(path)
        elif path.startswith(tree_rel + "/"):
            parts = path[len(tree_rel) + 1:].split("/")
            if len(parts) >= 2:
                dirs.add(tuple(parts[:-1][:3]))
            n = len(parts)
            if (n == 1 and parts[0] in ("DIRECTIVES.yaml", "MACROS.yaml")) \
                    or (n == 4 and parts[3] == row_file) \
                    or (n == 5 and parts[3] == "prd" and parts[4].endswith("_PRD.md")) \
                    or (n == 5 and parts[3] == "ledger" and parts[4].startswith("COMPLETION_") and parts[4].endswith(".json")):
                want.append((oid, path))
        elif path.startswith(idx_rel + "/") and path.endswith(".json") and "/" not in path[len(idx_rel) + 1:]:
            want.append((oid, path))
    for d in sorted(dirs):
        (dest / tree_rel).joinpath(*d).mkdir(parents=True, exist_ok=True)
    missing = [x for x in extra if x not in seen_extra]
    if missing:
        raise StagedReadError(f"not in the git index: {missing}")
    for (_oid, path), data in zip(want, _blobs(repo, env, [w[0] for w in want])):
        put(path, data)
    return {"contract": dest / CONTRACT_REL, "root": dest / tree_rel, "projects": dest / idx_rel,
            "directives": dest / DIRECTIVES_REL, "macros": dest / MACROS_REL, "ws": dest, "files": len(want) + 1}


class RowCannotCompose(Exception):
    """The staged row of one project cannot be composed into its index entry (rc 1, one-line reason)."""


def derive_staged_one(repo, code, env=None):
    """The index entry `derive --write` would write for ONE project, composed from the git index (GIT_INDEX_FILE /
    GIT_DIR in `env`); the working tree is never read and no file is written. Reads only: the contract, the value-enum
    sources it names, the project's row, and its existing flat entry (for generated_at). Returns the entry dict.
    Raises RowCannotCompose (the row cannot be composed) or StagedReadError (the index cannot be read)."""
    env = dict(os.environ if env is None else env)
    ent = [e for e in _index_listing(repo, env, [CONTRACT_REL]) if e[0] != "160000"]
    if len(ent) != 1 or ent[0][2] != "0":
        raise StagedReadError(f"{CONTRACT_REL} is not in the git index (or is unmerged)")
    contract_bytes = _blobs(repo, env, [ent[0][1]])[0]
    contract = json.loads(contract_bytes.decode("utf-8"))
    tree_rel, idx_rel = contract["root"], contract["index"]["root"]
    row_file = contract["project_folder"]["row"]
    srcs = list(REGISTER_RELS) + [spec["source"] for f, spec in (contract.get("value_enums") or {}).items()
            if not f.startswith("_") and isinstance(spec, dict) and not spec.get("no_enum")]
    rows = [e for e in _index_listing(repo, env, [f"{tree_rel}/*/{code}/{row_file}"])
            if len(e[3][len(tree_rel) + 1:].split("/")) == 4 and e[3].split("/")[-2] == code]
    if not rows:
        raise RowCannotCompose(f"no staged {row_file} for project {code!r} under {tree_rel}/")
    if len(rows) != 1 or rows[0][2] != "0":
        raise RowCannotCompose(f"{code!r}: {len(rows)} staged row entr{'y' if len(rows) == 1 else 'ies'}, "
                               f"stage {','.join(sorted({r[2] for r in rows}))} (unmerged or duplicated)")
    flat_rel = f"{idx_rel}/{code}.json"
    srcl = [e for e in _index_listing(repo, env, srcs + [flat_rel]) if e[0] != "160000" and e[2] == "0"]
    by_path = {e[3]: e[1] for e in srcl}
    missing = [x for x in srcs if x not in by_path]
    if missing:
        raise StagedReadError(f"not in the git index: {missing}")
    want = [rows[0][1]] + [by_path[x] for x in srcs] + ([by_path[flat_rel]] if flat_rel in by_path else [])
    blobs = _blobs(repo, env, want)
    tmp = tempfile.mkdtemp(prefix="mti-one-")
    try:
        for x, data in zip(srcs, blobs[1:1 + len(srcs)]):
            f = Path(tmp) / x
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(data)
        cp = Path(tmp) / CONTRACT_REL
        cp.parent.mkdir(parents=True, exist_ok=True)
        cp.write_bytes(contract_bytes)
        est = Estate(cp, Path(tmp) / tree_rel, Path(tmp) / idx_rel, Path(tmp) / DIRECTIVES_REL, Path(tmp) / MACROS_REL,
                     ws=Path(tmp), index_only_scan=False)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    parts = rows[0][3][len(tree_rel) + 1:].split("/")
    try:
        row = json.loads(blobs[0].decode("utf-8"))
    except ValueError as e:
        raise RowCannotCompose(f"{rows[0][3]} does not parse: {e}")
    t = {"D": parts[0], "M": parts[1], "code": parts[2], "row": row}
    why = est.row_problems(t)
    if why:
        raise RowCannotCompose("; ".join(why))
    entry = est.compose_index(t)
    existing = {}
    if flat_rel in by_path:
        try:
            existing = json.loads(blobs[-1].decode("utf-8"))
        except ValueError:
            existing = {}
    keep = isinstance(existing, dict) and existing.get("generated_at") and \
        all(existing.get(f) == entry.get(f) for f in est.compared + [est.idx_marker, "generated_from"])
    entry["generated_at"] = existing["generated_at"] if keep else _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return entry


# ---------- ACT SCOPE ----------
# A violation belongs to a project: the last segment of its tree home (org/missions/<D>/<M>/<CODE>), or the stem of its
# flat file (org/projects/<CODE>.json). The act's projects are the <CODE>s of the act paths. A register/contract path in the
# act puts EVERY project in-act. A violation not in-act is STANDING: printed, never counted, never refused.
_ACT_TREE_RE = re.compile(r"^org/missions/D(?:0|[1-9][0-9]?)/[^/]+/([^/]+)(?:/|$)")
_ACT_FLAT_RE = re.compile(r"^org/projects/([^/]+)\.json$")
_ACT_ALL = (DIRECTIVES_REL, MACROS_REL, CONTRACT_REL)


def _norm_act(paths):
    out = set()
    for p in paths:
        p = (p or "").strip().replace("\\", "/")
        while p.startswith("./"):
            p = p[2:]
        if p:
            out.add(p)
    return sorted(out)


def act_projects(paths):
    """(codes, all_in_act) for the normalised act paths."""
    codes, all_in = set(), False
    for p in paths:
        if p in _ACT_ALL:
            all_in = True
        m = _ACT_TREE_RE.match(p) or _ACT_FLAT_RE.match(p)
        if m:
            codes.add(m.group(1))
    return codes, all_in


def violation_code(path):
    name = str(path).rstrip("/").rsplit("/", 1)[-1]
    return name[:-5] if name.endswith(".json") else name


def split_by_act(viol, act_paths):
    """(in_act, standing, codes, all_in_act): violations partitioned by whether the act touches their project. A
    violation on a folder (an R1 level-name violation) is also in-act when an act path lies under that folder."""
    act = _norm_act(act_paths)
    codes, all_in = act_projects(act)
    in_act, standing = [], []
    for v in viol:
        vpath = str(v[1])
        hit = all_in or violation_code(vpath) in codes or any(a == vpath or a.startswith(vpath + "/") for a in act)
        (in_act if hit else standing).append(v)
    return in_act, standing, sorted(codes), all_in


# ---------- CLI ----------
def _print_check(viol, denom, as_json=False, scope=None):
    """scope = (standing, codes, all_in_act) under --act, else None. `viol` is then the in-act list."""
    if as_json:
        doc = {"violations": [{"id": a, "path": b, "detail": c} for a, b, c in viol], "denominators": denom}
        if scope is not None:
            doc["standing"] = [{"id": a, "path": b, "detail": c, "project": violation_code(b)} for a, b, c in scope[0]]
            doc["act"] = {"projects": scope[1], "all_projects_in_act": scope[2], "in_act": len(viol), "standing": len(scope[0])}
        print(json.dumps(doc, indent=1))
        return
    print("missions-tree-index check: tree={tree_projects} project(s) under {tree_directive_folders} directive folder(s), {tree_valid} valid"
          " | flat index rows={flat_rows} (generated={flat_generated}, hand-written={flat_hand_written}, parse-errors={flat_parse_errors})"
          " | DIRECTIVES.yaml: {directives_entries} entries across {directives_listed} directives"
          " | MACROS.yaml: {macros_ratified} of {macros_directives} directive(s) RATIFIED".format(**denom))
    for f, spec in denom.get("value_enums", {}).items():
        print(f"  value enum {f}: {len(spec['values'])} values from {spec['source']} ({spec.get('origin', 'origin not recorded')})")
    if denom.get("r6_not_graded_index_only"):
        skipped = denom["r6_not_graded_index_only"]
        print(f"  R6 NOT GRADED for {len(skipped)} CLOSED project(s) outside this sparse cone (read from the git index): {', '.join(skipped)}")
    if scope is not None:
        standing, codes, all_in = scope
        print(f"  ACT SCOPE: in-act={len(viol)} STANDING={len(standing)} (act projects: "
              f"{'ALL (a register/contract path is in the act)' if all_in else (', '.join(codes) or 'none')})")
        for a, b, c in standing:
            print(f"STANDING {violation_code(b)} {a} {b} {c}")
    for a, b, c in viol:
        print(f"  [{a}] {b}: {c}")
    if scope is not None:
        print(f"RESULT: {len(viol)} violation(s) in the act's projects, {len(scope[0])} STANDING  (denominators on the first line)")
        return
    print(f"RESULT: {len(viol)} violation(s)  (denominators on the first line; 0 tree projects is the s.8 baseline, not a blank read)")


def _estate(args) -> Estate:
    return Estate(args.contract, args.root, args.projects, args.directives, args.macros)


def _act_paths(args):
    """The act's paths from --act and --act-from-env, or None when neither is given. An unset/empty env var is an
    ERROR (rc 2): an empty act would read every violation as STANDING and pass them all."""
    if not args.act and not args.act_from_env:
        return None
    paths = list(args.act or [])
    for var in args.act_from_env or []:
        val = os.environ.get(var, "")
        if not val.strip():
            raise StagedReadError(f"--act-from-env {var}: variable unset or empty -- refusing an empty act (it would pass every violation as STANDING)")
        paths.extend(val.replace("\r", "").split("\n"))
    paths = _norm_act(paths)
    if not paths:
        raise StagedReadError("--act given but no usable path -- refusing an empty act")
    return paths


def cmd_check(args) -> int:
    act = _act_paths(args)
    tmp = None
    try:
        if args.staged:
            tmp = tempfile.mkdtemp(prefix="mti-staged-")
            m = materialise_index(_WS, tmp)
            est = Estate(m["contract"], m["root"], m["projects"], m["directives"], m["macros"], ws=m["ws"], index_only_scan=False)
        else:
            est = _estate(args)
        viol, denom, _, _ = est.check()
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)
    if args.staged:
        denom["read_from"] = "git index (--staged)"
    if act is None:
        _print_check(viol, denom, args.json)
        return 1 if viol else 0
    in_act, standing, codes, all_in = split_by_act(viol, act)
    _print_check(in_act, denom, args.json, scope=(standing, codes, all_in))
    return 1 if in_act else 0


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
        # 14. value enums resolve from the GATE (literal by AST; FABRIC_ENUM register-derived) and agree with an
        #     independent read (grain): a regex for the literal enum, lib/devices.py placement_values() for the derived one,
        #     and the gate must NOT carry a fabric literal (a literal here would be a second carrier)
        est = fresh("t14")
        gate_src = (_WS / ".tools" / "to-pipeline-gate.py").read_text(encoding="utf-8")

        def rx_enum(sym):
            m = re.search(r"^" + sym + r"\s*=\s*\((.*?)\)\s*$", gate_src, re.M)
            return tuple(s.strip().strip("'\"") for s in m.group(1).split(",") if s.strip()) if m else None

        _dspec = importlib.util.spec_from_file_location("devices_t14", str(_WS / "lib" / "devices.py"))
        _dmod = importlib.util.module_from_spec(_dspec)
        _dspec.loader.exec_module(_dmod)
        reg_fabric = tuple(_dmod.placement_values())
        chk("value enums resolved == independent read (dep_stage: regex on the gate literal; fabric: register placement_values, gate carries no fabric literal)",
            est.enums.get("dep_stage") == rx_enum("DEP_STAGE_ENUM") and est.enums.get("fabric") == reg_fabric
            and rx_enum("FABRIC_ENUM") is None and len(est.enums["dep_stage"]) >= 6,
            f"ast={est.enums} regex={rx_enum('DEP_STAGE_ENUM')},{rx_enum('FABRIC_ENUM')} register={reg_fabric}")
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


        # 18. --act / STANDING: the pure partition (no git, no files)
        v_own = ("INDEX-DRIFT", "org/projects/AAA_ONE.json", "d1")
        v_by = ("INDEX-DRIFT", "org/projects/BBB_TWO.json", "d2")
        v_home = ("R5", "org/missions/D8/ETFS/BBB_TWO", "d3")
        v_fold = ("R1", "org/missions/D8/etfs", "d4")
        inn, stn, codes, all_in = split_by_act([v_own, v_by, v_home],
                                               ["org/missions/D8/ETFS/AAA_ONE/task-orders/x.md", "./org/projects/AAA_ONE.json"])
        chk("--act pure: a violation in the act's project is in-act, the bystander's two are STANDING",
            inn == [v_own] and stn == [v_by, v_home] and codes == ["AAA_ONE"] and not all_in, f"{inn} {stn} {codes}")
        inn, stn, _c, all_in = split_by_act([v_own, v_by], ["org/missions/DIRECTIVES.yaml"])
        chk("--act pure: a staged DIRECTIVES.yaml puts every project in-act (STANDING empty)", inn == [v_own, v_by] and stn == [] and all_in, f"{inn} {stn}")
        inn, stn, _c, _a = split_by_act([v_fold], ["org/missions/D8/etfs/x.md"])
        chk("--act pure: a folder-level R1 violation is in-act when an act path lies under the folder", inn == [v_fold] and stn == [], f"{inn} {stn}")
        chk("--act pure: STANDING project code is the home's last segment or the flat file's stem",
            violation_code(v_home[1]) == "BBB_TWO" and violation_code(v_by[1]) == "BBB_TWO", "")

        # 19. --staged on a scratch GIT repo: two tree projects, one the act's, one the bystander's
        def git_in(repo, args, env=None, data=None):
            e = {k: v for k, v in os.environ.items() if k not in ("GIT_INDEX_FILE", "GIT_DIR", "GIT_WORK_TREE")}
            e.update(env or {})
            return subprocess.run(["git", "-C", str(repo)] + args, env=e, input=data, capture_output=True, text=True, timeout=60)

        def scratch_repo(name):
            e_ = fresh(name)
            top = e_.root.parent.parent
            (top / "org" / "missions" / "DIRECTIVES.yaml").write_text(
                "version: 1\ndirectives:\n  D8:\n    members:\n      projects: [ETFS_GUARDRAIL, ETFS_SECOND, MDPF_FLATONE]\n  D0:\n    members:\n      projects: []\n",
                encoding="utf-8")
            plant(e_, "D8", "ETFS", "ETFS_GUARDRAIL")
            plant(e_, "D8", "ETFS", "ETFS_SECOND")
            e_.derive(write=True)
            for rel in (CONTRACT_REL, CLOSE_SCHEMA_REL, ".tools/to-pipeline-gate.py") + REGISTER_RELS:
                (top / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(_WS / rel, top / rel)
            git_in(top, ["init", "-q"])
            git_in(top, ["add", "-A"])
            return e_, top

        def cli(top, argv, env=None):
            e = {k: v for k, v in os.environ.items() if k not in ("GIT_INDEX_FILE", "GIT_DIR", "GIT_WORK_TREE")}
            e["GIT_DIR"] = str(top / ".git")
            e.update(env or {})
            r = subprocess.run([sys.executable, str(Path(__file__).resolve()), "check"] + argv, cwd=str(td), env=e,
                               capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
            return r.returncode, (r.stdout or "") + (r.stderr or "")

        e_, top = scratch_repo("t18")
        rc0, out0 = cli(top, ["--staged"])
        chk("--staged: a clean index reads 0 violations on the scratch repo (GIT_DIR honoured)", rc0 == 0 and "RESULT: 0 violation(s)" in out0, out0[-200:])
        second = top / "org" / "missions" / "D8" / "ETFS" / "ETFS_SECOND" / "project.json"
        orig = second.read_text(encoding="utf-8")
        drifted = json.loads(orig)
        drifted["dep_stage"] = "EXECUTING"
        second.write_text(json.dumps(drifted), encoding="utf-8")
        git_in(top, ["add", "org/missions/D8/ETFS/ETFS_SECOND/project.json"])
        second.write_text(orig, encoding="utf-8")  # the working tree is clean again; ONLY the index carries the drift
        wt = Estate(top / CONTRACT_REL, top / "org" / "missions", top / "org" / "projects", top / DIRECTIVES_REL, top / MACROS_REL)
        wv, _d, _v, _x = wt.check()
        chk("--staged control: the working tree alone reads the drifted project as CLEAN (a working-tree read sees nothing)", not wv, str(ids(wv)))
        rc1, out1 = cli(top, ["--staged"])
        chk("--staged reads the index: the staged-only drift is seen -> exactly one INDEX-DRIFT, rc 1",
            rc1 == 1 and "[INDEX-DRIFT] org/projects/ETFS_SECOND.json" in out1 and "RESULT: 1 violation(s)" in out1, out1[-300:])
        own = "org/missions/D8/ETFS/ETFS_SECOND/project.json"
        byst = "org/missions/D8/ETFS/ETFS_GUARDRAIL/project.json"
        rc2, out2 = cli(top, ["--staged", "--act", byst])
        stand = [ln for ln in out2.splitlines() if ln.startswith("STANDING ")]
        chk("--staged --act <bystander>: rc 0 and one column-0 STANDING ETFS_SECOND line naming rule, path and detail",
            rc2 == 0 and len(stand) == 1 and stand[0].startswith("STANDING ETFS_SECOND INDEX-DRIFT org/projects/ETFS_SECOND.json dep_stage:"), f"rc={rc2} {stand}")
        chk("--staged --act prints the denominator line with in-act and STANDING counts", "ACT SCOPE: in-act=0 STANDING=1" in out2, out2[-300:])
        rc3, out3 = cli(top, ["--staged", "--act", own])
        chk("--staged --act <own project> is refused (the difference control): rc 1, no STANDING line", rc3 == 1 and not any(ln.startswith("STANDING ") for ln in out3.splitlines()) and "ACT SCOPE: in-act=1 STANDING=0" in out3, out3[-300:])
        rc4, out4 = cli(top, ["--staged", "--act-from-env", "MTI_ACT"], {"MTI_ACT": byst + "\r\n" + "README.md\n"})
        chk("--staged --act-from-env VAR: newline-separated paths read from the variable (rc 0, STANDING)", rc4 == 0 and "STANDING ETFS_SECOND" in out4, f"rc={rc4} {out4[-200:]}")
        rc5, out5 = cli(top, ["--staged", "--act-from-env", "MTI_ACT_UNSET"])
        chk("--act-from-env with an unset variable is rc 2, never an empty act that passes everything", rc5 == 2 and "unset or empty" in out5, f"rc={rc5} {out5[-200:]}")
        rc6, out6 = cli(top, ["--staged", "--act", "org/missions/DIRECTIVES.yaml"])
        chk("--staged --act org/missions/DIRECTIVES.yaml puts every project in-act: rc 1, STANDING 0", rc6 == 1 and "ACT SCOPE: in-act=1 STANDING=0" in out6 and "ALL" in out6, out6[-300:])
        # GIT_INDEX_FILE is honoured: an alternate index carrying a different drift
        e2, top2 = scratch_repo("t19")
        alt = Path(td) / "alt-index"
        shutil.copyfile(top2 / ".git" / "index", alt)
        g = top2 / "org" / "missions" / "D8" / "ETFS" / "ETFS_GUARDRAIL" / "project.json"
        gd = json.loads(g.read_text(encoding="utf-8"))
        gd["dep_stage"] = "EXECUTING"
        blob = git_in(top2, ["hash-object", "-w", "--stdin"], data=json.dumps(gd)).stdout.strip()
        git_in(top2, ["update-index", "--cacheinfo", f"100644,{blob},org/missions/D8/ETFS/ETFS_GUARDRAIL/project.json"], env={"GIT_INDEX_FILE": str(alt)})
        rcA, outA = cli(top2, ["--staged"])
        rcB, outB = cli(top2, ["--staged"], {"GIT_INDEX_FILE": str(alt)})
        chk("--staged honours GIT_INDEX_FILE: the real index is clean (rc 0), the alternate index is drifted (rc 1)",
            rcA == 0 and rcB == 1 and "[INDEX-DRIFT] org/projects/ETFS_GUARDRAIL.json" in outB, f"{rcA} {rcB} {outB[-200:]}")

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
    ap.add_argument("--staged", action="store_true", help="check: read every input from the git index, not the working tree; derive: with --only CODE --stdout")
    ap.add_argument("--only", metavar="CODE", help="derive --staged: the one project whose index entry is composed")
    ap.add_argument("--stdout", action="store_true", help="derive --staged --only: print the entry (the file's exact content); write nothing")
    ap.add_argument("--act", action="append", default=[], metavar="PATH", help="check: a path the act touches (repeatable); violations outside its projects print STANDING and do not refuse")
    ap.add_argument("--act-from-env", action="append", default=[], metavar="VAR", help="check: env var holding newline-separated act paths")
    for k, v in _DEFAULTS.items():
        ap.add_argument(f"--{k}", default=str(v))
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.staged and args.mode == "derive":
        if not (args.only and args.stdout) or args.write:
            print("ERROR: `derive --staged` needs --only CODE --stdout and takes no --write", file=sys.stderr)
            return 2
        try:
            entry = derive_staged_one(_WS, args.only)
        except RowCannotCompose as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 1
        except (StagedReadError, OSError, ValueError, KeyError) as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 2
        sys.stdout.buffer.write((json.dumps(entry, indent=1, ensure_ascii=True) + "\n").encode("ascii"))
        return 0
    if (args.only or args.stdout) and not (args.staged and args.mode == "derive"):
        print("ERROR: --only/--stdout apply to `derive --staged` only", file=sys.stderr)
        return 2
    try:
        return cmd_check(args) if args.mode == "check" else cmd_derive(args)
    except (FileNotFoundError, StagedReadError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
