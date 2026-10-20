"""
comp-pulse -- THE ESTATE'S VITAL SIGNS. Read this first, each morning.

NFRA_NERVES L5 (Andrew-direct: "build comp-pulse"). The goal, verbatim:

    "We want to be able to know what is hot, what is cold, what systems are evolving and how,
     danger zones, breakage points, high risk... the graph would kind of evolve based on the
     activity of the agents, like roads that become wider with lots of foot traffic."

This is that, compiled. It INVENTS NOTHING: it composes the NERVES substrate (L2 traffic + L3
co-change + L3b risk edges) and the rail, and every number carries its VINTAGE and its DENOMINATOR.

THE SECTION THAT MATTERS MOST IS **DANGER x TRAFFIC**.
Not "what is dangerous" (the corpus already said that, and L3b made it graph-native). Not "what is
busy" (traffic alone is just noise with a rank). The intersection: **A NODE UNDER A HOLD OR A
RECORDED INCIDENT THAT SOMEONE IS WALKING INTO RIGHT NOW.** That is the estate's immune response --
the danger map firing while the danger is being approached, not after.

DISCIPLINE (NERVES non-negotiables, and they bind here hardest because this is the surface people
will actually read):

  NO FABRICATION, EVER (the comp-system rule). A missing or stale source reads UNKNOWN-VINTAGE and
  the section says so. It NEVER interpolates, NEVER carries a number forward, NEVER prints a
  confident-looking zero for a thing it did not measure. **A CONFIDENT ZERO IS THE MOST DANGEROUS
  OUTPUT A DASHBOARD CAN PRODUCE**, because it reads as "checked, and clean."

  HOT IS NOT GOOD (the Goodhart gate). Traffic is FOOT-FALL, not endorsement. **A WIDE ROAD TO A
  WRONG ANSWER GETS WIDER.** The HOT list is where attention IS, never where it SHOULD be -- and if
  a hot node is also a danger node, that is an ALARM, not a badge.

  UNKNOWN IS A BAND. Unaddressed events, absent sources, blind resources: rendered, never dropped.

COLD is deliberately NOT re-derived here: coldness is a LIVE-AWS question and comp-debris owns it
(one frontier, never two). comp-pulse points at it rather than growing a second, divergent answer.

Read-only. Composes derived artifacts + the rail; no network.

Usage:
    comp-pulse                 # the vital signs
    comp-pulse --days 7        # the attention window (default 7)
    comp-pulse diff [paths..]  # THE PRE-COMMIT RISK REFLEX: score a proposed file set against the
                               # danger map. No paths = the staged set (git diff --cached).
                               # exit 0 clean / 1 danger hit / 2 map absent (CANNOT clear).
    comp-pulse --json
    comp-pulse --self-test
Author: 1.0.0_SA_CTO~Z (NFRA_NERVES L5). 2026-07-14.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))


def _caller_root() -> str:
    """The tree the CALLER is standing in. _WS resolves from _HERE (this file's own location),
    which is right for the danger map and the logs and WRONG for repository SUBJECTS: a commit
    from a linked worktree resolved its staged paths against the MAIN checkout, found them
    'missing', and returned SUBJECT_ABSENT_FROM_CORPUS *before* risk_reflex() ever ran -- so the
    whole commit skipped the reflex, including files that would have flagged. INSTRUMENT_LIMITS.md
    LIMIT 4a. Falls back to _WS, so a caller in the main tree is unchanged."""
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=os.getcwd(),
                             capture_output=True, text=True, timeout=15)
        if out.returncode == 0 and out.stdout.strip():
            return os.path.normpath(out.stdout.strip())
    except Exception:
        pass
    return _WS
sys.path.insert(0, _HERE)
_TOOLS = os.path.join(_WS, ".tools")
if _TOOLS not in sys.path:
    sys.path.insert(0, _TOOLS)

from _compbudget import (Clock, budget_reached_line, disclosure_line,  # noqa: E402
                         resolve_budget, within_budget_line)

RAIL = os.path.join(_WS, "org", "mcp", "comp-which-rail.log")
RUNS = os.path.join(_WS, "org", "mcp", "comp-tool-runs.jsonl")
EDGES = os.path.join(_HERE, "nerves-edges.json")
RISK = os.path.join(_HERE, "nerves-risk-edges.json")

# CVO~Z L5 verify P2-1 (4106268e0): 'memory/...' citations 404 from the repo CWD -- the corpus
# roots them at the agent memory dir (nerves_lexical.py:68-70). Printed once wherever they appear.
_MEMORY_ROOT_NOTE = ("NOTE: memory/... citations root at the AGENT MEMORY DIR, not the repo: "
                     "~/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory")


def _memory_note_if_needed(claims_docs) -> list:
    return ["  " + _MEMORY_ROOT_NOTE] if any(str(d).startswith("memory/") for d in claims_docs) else []

# A derived artifact older than this is STALE -- we still read it, but we SAY SO on every number
# that came out of it. (Rule 20's UNKNOWN-VINTAGE discipline, applied to our own outputs.)
STALE_AFTER_HOURS = 36.0
HALF_LIFE_DAYS = 7.0        # attention decays fast; a road walked last month is not today's road


def _decay(age_days: float) -> float:
    return math.pow(0.5, max(0.0, age_days) / HALF_LIFE_DAYS)


class Source:
    """A source + ITS VINTAGE. Every number in this report is traceable to one of these, and if the
    source is missing the number is NOT PRINTED -- the section prints UNKNOWN-VINTAGE instead."""

    def __init__(self, path: str, label: str):
        self.path = path
        self.label = label
        self.exists = os.path.exists(path)
        self.age_h = None
        self.data = None
        if self.exists:
            self._read_age()

    def _read_age(self):
        try:
            self.age_h = (dt.datetime.now().timestamp() - os.path.getmtime(self.path)) / 3600.0
        except OSError:
            self.age_h = None

    @property
    def stale(self) -> bool:
        return self.age_h is not None and self.age_h > STALE_AFTER_HOURS

    @property
    def vintage(self) -> str:
        if not self.exists:
            return "UNKNOWN-VINTAGE (absent -- this section CANNOT be computed and is NOT guessed)"
        if self.age_h is None:
            return "UNKNOWN-VINTAGE (unreadable mtime)"
        tag = "  !! STALE" if self.stale else ""
        return "%.1fh old%s" % (self.age_h, tag)

    def load_json(self):
        if not self.exists:
            return None
        try:
            with open(self.path, encoding="utf-8") as fh:
                self.data = json.load(fh)
            return self.data
        except Exception:  # noqa: BLE001
            self.exists = False   # unreadable == absent; never a half-trusted source
            return None


# ---------------------------------------------------------------------------
# the danger map: its age, its one rebuild, and the sparse-tree rule (NFRA_CTLPLN round 22, CT-al-3)
# ---------------------------------------------------------------------------
MAP_REL = os.path.join("org", "modules", "graph", "nerves-risk-edges.json")
REBUILD_TIMEOUT_S = 120
REBUILD_LOCK_NAME = ".nerves-risk-edges.rebuild.lock"
REBUILD_LOCK_STALE_S = 600
BUILD_SPAWNS = 0   # counted: a child build actually started in this process (the --sparse arm reads it)


class RiskSource(Source):
    """The danger map. Its AGE is the build time the file carries (built_utc, written by
    nerves_lexical build), never the file's mtime: a checkout rewrites mtime, so a week-old map
    read fresh. A map with no readable built_utc has UNKNOWN age and is STALE."""

    def __init__(self, path: str):
        self.built_utc = None
        super().__init__(path, "danger map (nerves_lexical)")

    def _read_age(self):
        self.age_h = None
        try:
            with open(self.path, encoding="utf-8") as fh:
                doc = json.load(fh)
        except Exception:  # noqa: BLE001
            return
        stamp = doc.get("built_utc") if isinstance(doc, dict) else None
        try:
            built = dt.datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
        except (TypeError, ValueError):
            return
        self.built_utc = stamp
        self.age_h = (dt.datetime.now(dt.timezone.utc) - built).total_seconds() / 3600.0

    @property
    def stale(self) -> bool:
        return self.exists and (self.age_h is None or self.age_h > STALE_AFTER_HOURS)

    @property
    def vintage(self) -> str:
        if not self.exists:
            return "UNKNOWN-VINTAGE (absent -- this section CANNOT be computed and is NOT guessed)"
        if self.age_h is None:
            return "UNKNOWN-VINTAGE (no built_utc in the map: age unknown, treated as STALE)  !! STALE"
        tag = "  !! STALE" if self.stale else ""
        return "%.1fh old%s" % (self.age_h, tag)


def _git(tree: str, *args):
    try:
        out = subprocess.run(["git", "-C", tree, *args], capture_output=True, text=True, timeout=15)
        return out.returncode, out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return 1, ""


def is_sparse_tree(tree: str) -> bool:
    rc, out = _git(tree, "config", "--bool", "core.sparseCheckout")
    return rc == 0 and out == "true"


def main_tree_of(tree: str):
    """The main checkout of this worktree (git's common dir is <main>/.git). None when unknown."""
    rc, common = _git(tree, "rev-parse", "--git-common-dir")
    if rc != 0 or not common:
        return None
    gd = os.path.abspath(os.path.join(tree, common))
    return os.path.dirname(gd) if os.path.basename(gd) == ".git" else None


def build_guard_refusal(builder: str, tree: str):
    """THE SAME GUARD AS THE BUILDER: nerves_lexical.build_refusal, loaded from the builder beside the map
    (importing it runs no build). -> the refusal text, or None when the builder admits this tree."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("nerves_lexical_guard", builder)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.build_refusal(tree)


def rebuild_risk_map(map_path: str, timeout: int = REBUILD_TIMEOUT_S):
    """ONE rebuild of the danger map by its own builder, as a child process capped at `timeout`
    seconds. The build guard is checked FIRST: a refused tree is never built here. A lock file keeps
    two reflexes from building at once. -> (ok, why)."""
    global BUILD_SPAWNS
    graph = os.path.dirname(map_path)
    builder = os.path.join(graph, "nerves_lexical.py")
    if not os.path.isfile(builder):
        return False, "no nerves_lexical.py beside the map"
    tree = os.path.normpath(os.path.join(graph, "..", "..", ".."))
    try:
        refusal = build_guard_refusal(builder, tree)
    except Exception as exc:  # noqa: BLE001 -- a guard that cannot load refuses, it never waves a build through
        refusal = "the guard could not be loaded: %s: %s" % (type(exc).__name__, exc)
    if refusal:
        return False, "NOT-DECIDABLE: danger map STALE and the build guard refused: %s" % refusal
    lock = os.path.join(graph, REBUILD_LOCK_NAME)
    try:
        if os.path.exists(lock) and time.time() - os.path.getmtime(lock) > REBUILD_LOCK_STALE_S:
            os.remove(lock)   # a dead reflex's lock; the map's own age is never read from mtime
        os.close(os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
    except FileExistsError:
        return False, "another reflex holds the rebuild lock"
    except OSError as exc:
        return False, "rebuild lock unavailable (%s)" % exc
    try:
        BUILD_SPAWNS += 1
        p = subprocess.run([sys.executable, builder, "build"], cwd=graph, capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=timeout)
        if p.returncode != 0:
            last = ((p.stdout or "") + (p.stderr or "")).strip().splitlines()
            return False, "build rc=%d: %s" % (p.returncode, last[-1] if last else "no output")
        return True, "rebuilt in place by nerves_lexical build"
    except subprocess.TimeoutExpired:
        return False, "build timed out after %d s" % timeout
    except OSError as exc:
        return False, "build could not start (%s)" % exc
    finally:
        try:
            os.remove(lock)
        except OSError:
            pass


def resolve_risk_map(tree: str, own_map: str, rebuild=rebuild_risk_map):
    """THE ONE DECISION on which danger map the reflex reads. -> (source, note, blind).
    - own map fresh (embedded built_utc inside the limit): read it, nothing is built.
    - sparse tree (core.sparseCheckout true): NEVER builds. Reads the MAIN tree's map; none there
      -> blind=True (the reflex prints BLIND: sparse worktree, no map).
    - own map STALE: rebuilt ONCE by the reflex, then re-read. A failed or timed-out rebuild leaves
      the map STALE, which the reflex reports as NOT-DECIDABLE with the reason.
    - own map ABSENT: no rebuild (absent stays absent: NOT-DECIDABLE, never a silent build)."""
    own = RiskSource(own_map)
    if own.exists and not own.stale:
        return own, None, False
    if is_sparse_tree(tree):
        main = main_tree_of(tree)
        main_map = os.path.join(main, MAP_REL) if main else None
        if main_map and os.path.isfile(main_map):
            return (RiskSource(main_map),
                    "sparse worktree: read the MAIN tree's map (%s); no build here" % main_map, False)
        if own.exists:
            return own, "sparse worktree: own map STALE and no main-tree map; no build here", False
        return own, "sparse worktree: no danger map here or in the main tree", True
    if not own.exists:
        return own, None, False
    # AMGT_HARVST-D1-W183-S11/S17: a LINKED worktree's own map is STALE (a checkout carries the
    # map as last committed) and its build is refused by the guard, so the reflex answered
    # PARTIAL_OR_BLIND on every worker commit. Read the MAIN tree's map when that one is fresh:
    # no build here, and the main map's age is printed as the vintage. A stale main map falls
    # through to the rebuild/refusal below, so a stale map still ends as a named NOT-DECIDABLE.
    main = main_tree_of(tree)
    if main and os.path.normcase(os.path.normpath(main)) != os.path.normcase(os.path.normpath(tree)):
        main_map = os.path.join(main, MAP_REL)
        if os.path.isfile(main_map):
            main_src = RiskSource(main_map)
            if main_src.exists and not main_src.stale:
                return (main_src,
                        "linked worktree: own map STALE; read the MAIN tree's map (%s); no build here"
                        % main_map, False)
    ok, why = rebuild(own_map)
    fresh = RiskSource(own_map)
    if ok and not fresh.stale:
        return fresh, "danger map was STALE; rebuilt once by the reflex (%s)" % why, False
    if why.startswith("NOT-DECIDABLE"):
        return fresh, why, False     # the build guard refused: the reflex says so, it does not build
    return fresh, "danger map STALE; the one rebuild did not clear it (%s)" % why, False


# ---------------------------------------------------------------------------
# signals
# ---------------------------------------------------------------------------
_RAIL_RX = re.compile(r"^(\S+)\s+(\S+)\s+(.*)$")
_KV_RX = re.compile(r"(\w+)=(\S+)")
_PHANTOM_TAGS = {"NOFIT-POSTERIOR", "DENY"}


class _TelemetryScan:
    """One deterministic cursor across the two append-only telemetry streams.
    `False` means a row belongs to a prior cursor; `None` means the Rule-T
    ceiling was reached before this row could be claimed."""

    def __init__(self, clock: Clock, total: int, cursor: int):
        self.clock = clock
        self.total = total
        self.cursor = cursor
        self.position = 0
        self.last_completed = cursor
        self.scanned = 0
        self.exhausted = False

    def take(self):
        if self.exhausted:
            return None
        self.position += 1
        if self.position <= self.cursor:
            return False
        if self.clock.remaining() <= 0:
            self.exhausted = True
            return None
        self.scanned += 1
        self.last_completed = self.position
        return True


def _line_count(path: str) -> int:
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return sum(1 for _ in fh)
    except OSError:
        return 0


def rail_signals(days: int, scan: _TelemetryScan | None = None):
    """-> (attention Counter{ref: decayed_weight}, phantoms Counter{term: n}, denominators).
    The rail is the ONLY stream that carries BOTH what an agent looked for AND whether they found
    it, which is why the phantom-limb map lives here."""
    att = Counter()
    phantom = Counter()
    newest = {}   # term -> age_days of its FRESHEST event (CVO refinement 110333Z: an attention
                  # score quotes its AGE beside its magnitude -- residual foot-fall must not
                  # masquerade as current demand)
    rows = considered = 0
    if not os.path.exists(RAIL):
        return att, phantom, newest, {"rail_rows": 0, "rows_in_window": 0, "available": False}
    now = dt.datetime.now(dt.timezone.utc)
    with open(RAIL, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if scan is not None:
                claimed = scan.take()
                if claimed is None:
                    break
                if not claimed:
                    continue
            m = _RAIL_RX.match(line.strip())
            if not m:
                continue
            rows += 1
            try:
                ts = dt.datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M:%SZ").replace(
                    tzinfo=dt.timezone.utc)
            except Exception:  # noqa: BLE001
                continue
            age_d = (now - ts).total_seconds() / 86400.0
            if age_d > days:
                continue
            considered += 1
            tag, rest = m.group(2), m.group(3)
            kv = dict(_KV_RX.findall(rest))
            w = _decay(age_d)
            term = kv.get("term")
            if term and term not in ("-", "."):
                att[term] += w
                prev = newest.get(term)
                newest[term] = age_d if prev is None else min(prev, age_d)
            matches = kv.get("matches")
            if tag in _PHANTOM_TAGS or (matches is not None and matches == "0"):
                if term and term not in ("-", "."):
                    phantom[term] += 1
    return att, phantom, newest, {"rail_rows": rows, "rows_in_window": considered, "available": True}


def run_signals(days: int, scan: _TelemetryScan | None = None):
    """-> Counter{tool: decayed}. The run sink carries OUTCOMES -- the Goodhart-safe weight."""
    c = Counter()
    fails = Counter()
    n = 0
    if not os.path.exists(RUNS):
        return c, fails, {"available": False, "rows": 0}
    now = dt.datetime.now(dt.timezone.utc).timestamp()
    with open(RUNS, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if scan is not None:
                claimed = scan.take()
                if claimed is None:
                    break
                if not claimed:
                    continue
            try:
                r = json.loads(line)
            except Exception:  # noqa: BLE001
                continue
            n += 1
            age_d = (now - float(r.get("ts_epoch", 0))) / 86400.0
            if age_d > days or age_d < 0:
                continue
            tool = r.get("tool", "?")
            c[tool] += _decay(age_d)
            if str(r.get("result", "")).upper().startswith("FAIL"):
                fails[tool] += 1
    return c, fails, {"available": True, "rows": n}


def evolving(edges_src: Source, top: int):
    """WHAT IS CHANGING TOGETHER -- the co-change graph's busiest couplings (already decayed at
    build time). NOT 'what changed most' (that is git, and it is a popularity contest); the
    COUPLINGS are the interesting object because CO_CHANGE WITHOUT CO_DEPLOY is the drift predictor."""
    d = edges_src.load_json()
    if not d:
        return None, None
    edges = d.get("edges", [])
    stats = d.get("stats", {})
    return sorted(edges, key=lambda e: -e.get("weight", 0))[:top], stats


def _risk_index(edges):
    """Index the danger map by node id + leaf basename (generous by policy -- see nerves_lexical:
    a missed hold can cost the estate; a noisy one costs ten seconds)."""
    by_key = defaultdict(list)
    for e in edges:
        nid = e["node"]
        leaf = nid.split(":")[-1].split("/")[-1]
        by_key[leaf.lower()].append(e)
        by_key[nid.lower()].append(e)
    return by_key


def risk_reflex(risk_src: Source, paths, clock: Clock | None = None, cursor: int = 0):
    """THE PRE-COMMIT REFLEX (NFRA_NERVES L5 endgame): score a PROPOSED file set against the danger
    map BEFORE the commit exists. Returns (hits|None, denominators). None = the map is absent --
    the reflex CANNOT clear the diff, which is not the same as clearing it."""
    # This is a query-only pre-commit reflex. A stale map is as unable to clear
    # a diff as an absent one: freshness is part of the measured corpus.
    if not risk_src.exists or risk_src.stale:
        condition = "STALE" if risk_src.stale else "ABSENT"
        return None, {"files_checked": 0, "danger_nodes": 0, "total_files": len(paths),
                      "cursor": cursor, "reason": "danger map %s" % condition}
    d = risk_src.load_json()
    if d is None:
        return None, {"files_checked": 0, "danger_nodes": 0, "total_files": len(paths),
                      "cursor": cursor, "reason": "danger map UNREADABLE"}
    edges = d.get("edges", [])
    by_key = _risk_index(edges)
    hits, seen = [], set()
    checked = 0
    for index, p in enumerate(paths, start=1):
        if index <= cursor:
            continue
        if clock is not None and clock.remaining() <= 0:
            return None, {"files_checked": checked, "danger_nodes": len(edges),
                          "total_files": len(paths), "cursor": index - 1,
                          "reason": "budget reached"}
        rel = str(p).replace("\\", "/").strip()
        if not rel:
            continue
        checked += 1
        for k in (os.path.basename(rel).lower(), rel.lower(), "file:" + rel.lower()):
            for e in by_key.get(k, []):
                if e["severity"] not in ("HOLD", "RISK"):
                    continue
                key = (rel, e["node"])
                if key in seen:
                    continue
                seen.add(key)
                hits.append({"path": rel, "node": e["node"], "severity": e["severity"],
                             "kinds": e.get("kinds", []), "n_claims": e["n_claims"],
                             "claim": e["claims"][0]})
    hits.sort(key=lambda h: ({"HOLD": 0, "RISK": 1}[h["severity"]], h["path"]))
    return hits, {"files_checked": checked, "danger_nodes": len(edges),
                  "total_files": len(paths), "cursor": len(paths), "reason": None}


def render_reflex(hits, denom, risk_src: Source, invocation: str) -> str:
    L = ["comp-pulse diff -- THE PRE-COMMIT RISK REFLEX (NFRA_NERVES L5)",
         "  INVOCATION (pin beside any quoted result): %s" % invocation,
         "  danger map: %s" % risk_src.vintage]
    if denom.get("rebuild_note"):
        note = denom["rebuild_note"]
        L.append(("  " + note) if note.startswith("NOT-DECIDABLE") else ("  REBUILD: " + note))
    if hits is None:
        reason = denom.get("reason") or "danger map unavailable"
        L += ["  ANSWER STATE: PARTIAL_OR_BLIND",
              "  NOT-DECIDABLE: %s -- the reflex CANNOT clear this diff," % reason,
              "  and 'could not check' is NOT 'checked clean'."]
        return "\n".join(L)
    L.append("  DENOMINATOR: %d file(s) checked against %d danger node(s)"
             % (denom["files_checked"], denom["danger_nodes"]))
    if not hits:
        L.append("  ANSWER STATE: PRESENT_WITH_ZERO_RESULTS")
        L.append("  REFLEX CLEAN -- a MEASURED result (map read, every file checked), not a default.")
        return "\n".join(L)
    L.append("")
    for h in hits:
        c = h["claim"]
        L.append("  [%s] %s" % (h["severity"], h["path"]))
        L.append("        -> %s  (%d recorded claim(s))" % (h["node"], h["n_claims"]))
        L.append("        %s:%d  \"%s\"" % (c["doc"], c["line"], str(c.get("quote", ""))[:70]))
    L += _memory_note_if_needed(h["claim"]["doc"] for h in hits)
    L.append("  ^ THE IMMUNE RESPONSE, PRE-COMMIT: you are about to touch a node the estate has")
    L.append("    WRITTEN WARNINGS ABOUT. GO READ THE CITATION before this commit proceeds.")
    return "\n".join(L)


def danger_x_traffic(risk_src: Source, attention: Counter, top: int, newest=None):
    """*** THE SECTION THAT MATTERS. *** A node under a HOLD or a recorded INCIDENT that someone is
    ACTIVELY TOUCHING. The danger map firing WHILE the danger is approached.

    Matching is deliberately generous on the danger side (a HOLD is over-warned by policy -- see
    nerves_lexical: a missed hold can cost the estate; a noisy one costs ten seconds), and it always
    shows the citation so the reader checks the claim rather than trusting this line."""
    d = risk_src.load_json()
    if not d:
        return None
    edges = d.get("edges", [])
    by_key = _risk_index(edges)
    hits = []
    for ref, w in attention.items():
        for e in by_key.get(ref.lower().split("/")[-1], []):
            if e["severity"] in ("HOLD", "RISK"):
                age = (newest or {}).get(ref)
                hits.append({"ref": ref, "attention": round(w, 2),
                             "newest_age_d": round(age, 1) if age is not None else None,
                             "node": e["node"], "severity": e["severity"],
                             "n_claims": e["n_claims"], "claim": e["claims"][0]})
                break
    hits.sort(key=lambda h: ({"HOLD": 0, "RISK": 1}[h["severity"]], -h["attention"]))
    # CVO~Z L5 verify P2-2 (4106268e0): the section must say census-or-cap -- return the
    # total alongside the shown slice so render can print 'showing N of TOTAL'.
    return hits[:top], len(hits)


# ---------------------------------------------------------------------------
def compile_pulse(days: int = 7, top: int = 8, invocation: str = "",
                  budget_s: float | None = None, budget_source: str = "", cursor: int = 0) -> dict:
    edges_src = Source(EDGES, "co-change edges (nerves_accrete)")
    risk_src = RiskSource(RISK)

    scan = None
    if budget_s is not None:
        scan = _TelemetryScan(Clock(budget_s), _line_count(RAIL) + _line_count(RUNS), cursor)
    att, phantom, newest, rail_stats = rail_signals(days, scan=scan)
    runs, run_fails, run_stats = run_signals(days, scan=scan)
    # The co-change and danger projections must not turn a telemetry prefix
    # into an apparently complete estate conclusion.
    partial = scan is not None and scan.exhausted
    evo, evo_stats = (None, None) if partial else evolving(edges_src, top)
    dxt_res = None if partial else danger_x_traffic(risk_src, att, top, newest)
    dxt, dxt_total = (None, None) if dxt_res is None else dxt_res

    return {
        # CVO~Z verify P2 class (2d2080e1e): a number nobody can re-derive is not evidence --
        # the resolved invocation rides WITH every number this report produces.
        "invocation": invocation or "(not recorded -- direct compile_pulse() call)",
        "window_days": days,
        "generated_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sources": {
            "rail": {"available": rail_stats["available"], "vintage": "live (append-only log)",
                     "rows_total": rail_stats["rail_rows"],
                     "rows_in_window": rail_stats["rows_in_window"]},
            "runs": {"available": run_stats["available"], "vintage": "live (append-only sink)",
                     "rows_total": run_stats["rows"]},
            "cochange": {"available": edges_src.exists, "vintage": edges_src.vintage,
                         "stale": edges_src.stale},
            "danger": {"available": risk_src.exists, "vintage": risk_src.vintage,
                       "stale": risk_src.stale,
                       "rebuild": "the diff reflex rebuilds ONCE when STALE; never in a sparse tree"},
        },
        "hot": [{"ref": r, "attention": round(w, 2),
                 "newest_age_d": round(newest[r], 1) if r in newest else None}
                for r, w in att.most_common(top)],
        "hot_tools": [{"tool": t, "runs_decayed": round(w, 2), "fails": run_fails.get(t, 0)}
                      for t, w in runs.most_common(top)],
        "danger_x_traffic": dxt,          # None => UNKNOWN-VINTAGE, never []
        "danger_x_traffic_total": dxt_total,   # census behind the shown slice (P2-2)
        "evolving": evo,                  # None => UNKNOWN-VINTAGE
        "evolving_stats": evo_stats,
        "phantom_limbs": [{"term": t, "n": n} for t, n in phantom.most_common(top)],
        "phantom_total": sum(phantom.values()),
        "cold": "NOT computed here -- coldness is a LIVE-AWS question and comp-debris owns it "
                "(one frontier, never two). Run: comp-debris --days 30",
        "systems": "UNKNOWN BAND -- system-grain vital signs (which C3 SYSTEMS are hot/fragile) "
                   "need C2/C3 materialized in the graph; C2 measured at 7 nodes 2026-07-14, "
                   "materialization rides MOTIF.P0 (0.8.0~Z, gated on the globgrph apply). This "
                   "band switches on when that lands -- it is declared, never silently omitted.",
        "budget": None if scan is None else {
            "reached": scan.exhausted,
            "scanned": scan.scanned,
            "total": scan.total,
            "cursor": scan.last_completed,
            "budget_s": budget_s,
            "source": budget_source,
            "used_s": scan.clock.elapsed(),
        },
    }


def render(p: dict) -> str:
    W = 78
    L = ["=" * W,
         "comp-pulse -- THE ESTATE'S VITAL SIGNS      window %dd   generated %s"
         % (p["window_days"], p["generated_at"]),
         "  INVOCATION (pin beside any number you quote): %s" % p.get("invocation", "?"),
         "=" * W,
         "SOURCES + VINTAGES (every number below is traceable to one of these):"]
    for k, s in p["sources"].items():
        mark = "  " if s["available"] else "!!"
        L.append("  %s %-9s %s  %s" % (mark, k, "OK     " if s["available"] else "ABSENT ",
                                       s["vintage"]))
    L.append("  ^ NO FABRICATION: an absent source yields UNKNOWN-VINTAGE, never an invented number.")
    L.append("    A CONFIDENT ZERO IS THE MOST DANGEROUS OUTPUT A DASHBOARD CAN PRODUCE.")

    # ---- THE ONE THAT MATTERS ----
    L += ["", "-" * W,
          "[!!] DANGER x TRAFFIC -- a node under a HOLD/INCIDENT that someone is TOUCHING NOW",
          "-" * W]
    dxt = p["danger_x_traffic"]
    if dxt is None:
        L.append("  UNKNOWN-VINTAGE: the danger map is absent. This section is NOT computed and is")
        L.append("  NOT clean -- run `nerves_lexical build` to regenerate it.")
    elif not dxt:
        L.append("  No node under a HOLD or a recorded incident saw traffic in the window.")
        L.append("  (This IS a measured result -- the danger map and the rail were both read.)")
    else:
        L.append("  showing %d of %d matched (the census, not a cap-blind slice):"
                 % (len(dxt), p.get("danger_x_traffic_total") or len(dxt)))
        for h in dxt:
            c = h["claim"]
            age = h.get("newest_age_d")
            age_s = ("newest %sd ago" % age) if age is not None else "age unknown"
            L.append("  %-6s attention=%-5s (%s)  %s" % (h["severity"], h["attention"], age_s, h["node"]))
            L.append("         someone searched/ran: %r" % h["ref"])
            L.append("         %s:%d  \"%s\"" % (c["doc"], c["line"], c["quote"][:72]))
        L += _memory_note_if_needed(h["claim"]["doc"] for h in dxt)
        L.append("  ^ THE IMMUNE RESPONSE: the danger map firing WHILE the danger is approached.")
        L.append("    GO READ THE CITATION before the next keystroke.")

    # ---- HOT ----
    L += ["", "-" * W, "[HOT] where the foot-fall IS -- decayed attention (rail terms, %dd)" % p["window_days"],
          "-" * W]
    if not p["hot"]:
        L.append("  (no rail traffic in the window)")
    for h in p["hot"]:
        age = h.get("newest_age_d")
        age_s = ("newest %sd ago" % age) if age is not None else "age ?"
        L.append("  %-6s (%s) %s" % (h["attention"], age_s, h["ref"][:56]))
    L.append("  ^ HOT IS NOT GOOD. Traffic is foot-fall, never endorsement -- A WIDE ROAD TO A")
    L.append("    WRONG ANSWER GETS WIDER. And AGE RIDES WITH MAGNITUDE: a big score whose newest")
    L.append("    event is a week old is RESIDUAL foot-fall, not current demand (CVO~Z 110333Z).")

    L += ["", "[HOT TOOLS] runs in the window (fails shown -- a busy tool that FAILS is a FIX, not a KEEP):"]
    if not p["hot_tools"]:
        L.append("  (no runs in the window)")
    for t in p["hot_tools"]:
        flag = "   <- %d FAIL" % t["fails"] if t["fails"] else ""
        L.append("  %-6s %-28s%s" % (t["runs_decayed"], t["tool"], flag))

    # ---- EVOLVING ----
    L += ["", "-" * W, "[EVOLVING] what changes TOGETHER (co-change; the drift predictor)", "-" * W]
    if p["evolving"] is None:
        L.append("  UNKNOWN-VINTAGE: the co-change graph is absent. NOT computed, NOT clean --")
        L.append("  run `nerves_accrete build`.")
    else:
        st = p["evolving_stats"] or {}
        L.append("  from %s commits / %s files / %s edges"
                 % (st.get("commits_scanned", "?"), st.get("distinct_files", "?"),
                    st.get("edges_at_min_support", "?")))
        for e in p["evolving"]:
            L.append("  w=%-5s %.0f%%/%.0f%%  %s" % (e.get("weight"), 100 * e.get("conf_src_to_dst", 0),
                                                     100 * e.get("conf_dst_to_src", 0),
                                                     os.path.basename(e.get("src", ""))))
            L.append("                     <> %s" % os.path.basename(e.get("dst", "")))
        L.append("  ^ CO-CHANGE WITHOUT CO-DEPLOY IS THE BREAKAGE PREDICTOR.")

    # ---- PHANTOM LIMBS ----
    L += ["", "-" * W,
          "[PHANTOM LIMBS] what agents LOOKED FOR AND DID NOT FIND -- the demand map for",
          "                knowledge that does not exist yet. %d event(s) in window."
          % p["phantom_total"], "-" * W]
    if not p["phantom_limbs"]:
        L.append("  (none in the window)")
    for ph in p["phantom_limbs"]:
        L.append("  x%-4d %s" % (ph["n"], ph["term"][:66]))
    L.append("  ^ These are the estate's MISSING ORGANS. A repeat phantom is a build-next.")

    # ---- COLD ----
    L += ["", "-" * W, "[COLD]", "-" * W, "  " + p["cold"]]

    # ---- SYSTEMS (declared UNKNOWN until C2/C3 materialize) ----
    L += ["", "-" * W, "[SYSTEMS]", "-" * W, "  " + p["systems"], "=" * W]
    budget = p.get("budget")
    if budget:
        if budget["reached"]:
            L += ["ANSWER STATE: PARTIAL_OR_BLIND", "NOT-DECIDABLE: telemetry scan reached its budget;",
                  budget_reached_line(budget["budget_s"], budget["source"], budget["scanned"],
                                      budget["total"], "telemetry row(s)", "comp-pulse", str(budget["cursor"]))]
        else:
            L.append(within_budget_line(budget["scanned"], budget["total"], "telemetry row(s)",
                                        budget["budget_s"], budget["source"], budget["used_s"]))
    return "\n".join(L)


def _self_test() -> int:
    results = []
    def ck(name, ok, detail=""):
        results.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))

    # ---- THE NO-FABRICATION CONTROL. Point every source at nothing; the report must render, must
    # say UNKNOWN-VINTAGE, and must NOT invent a single number. A dashboard that prints a confident
    # zero for a thing it never measured is worse than no dashboard.
    global EDGES, RISK, RAIL, RUNS
    _e, _r, _rail, _runs = EDGES, RISK, RAIL, RUNS
    EDGES = RISK = RAIL = RUNS = os.path.join(_WS, "__NO_SUCH_FILE__")
    p_absent = compile_pulse(days=7)
    txt = render(p_absent)
    EDGES, RISK, RAIL, RUNS = _e, _r, _rail, _runs

    ck("nofab.absent_sources_are_declared",
       all(not s["available"] for s in p_absent["sources"].values()))
    ck("nofab.danger_is_None_not_empty_list",
       p_absent["danger_x_traffic"] is None,
       "None = 'not computed'; [] would mean 'computed, clean' -- they are NOT the same")
    ck("nofab.evolving_is_None_not_zero", p_absent["evolving"] is None)
    ck("nofab.render_says_UNKNOWN_VINTAGE_and_NOT_clean",
       "UNKNOWN-VINTAGE" in txt and "NOT clean" in txt)
    ck("nofab.no_confident_zero_for_danger",
       "No node under a HOLD" not in txt,
       "an absent map must NEVER render as 'nothing dangerous is being touched'")

    # ---- DANGER x TRAFFIC fires. Fixture: a HOLD node + attention on its basename.
    class _S:  # a Source stand-in carrying fixture data
        exists = True
        stale = False
        vintage = "fixture"
        def __init__(self, d):
            self._d = d
        def load_json(self):
            return self._d

    risk_fx = _S({"edges": [{"node": "file:data/inf/scripts/silver/build_assets_dim.py",
                             "severity": "HOLD", "n_claims": 47,
                             "claims": [{"kind": "HOLD", "doc": "memory/MEMORY.md", "line": 81,
                                         "quote": "the frozen three -- no verb touches them"}]}]})
    att = Counter({"build_assets_dim.py": 3.4, "harmless_thing.py": 9.9})
    hits, dxt_total = danger_x_traffic(risk_fx, att, top=5,
                                       newest={"build_assets_dim.py": 6.8})
    ck("dxt.age_rides_with_magnitude", hits and hits[0].get("newest_age_d") == 6.8,
       "residual foot-fall must not masquerade as current demand (CVO 110333Z)")
    ck("dxt.census_total_rides_with_the_slice", dxt_total == 1,
       "the section says showing-N-of-TOTAL, never a cap-blind slice (P2-2)")
    ck("dxt.fires_on_a_held_node_under_traffic",
       len(hits) == 1 and hits[0]["severity"] == "HOLD"
       and "build_assets_dim" in hits[0]["node"],
       f"{[h['node'] for h in hits]}")
    ck("dxt.ignores_untouched_and_undangerous",
       all("harmless" not in h["node"] for h in hits),
       "a busy-but-safe node is not an alarm; a dangerous-but-idle node is not either")
    ck("dxt.carries_its_citation",
       hits and hits[0]["claim"]["doc"] and hits[0]["claim"]["line"],
       "the alarm points at the claim; it never replaces it")

    # ---- THE PRE-COMMIT REFLEX. Positive control: a staged set containing a held file MUST fire.
    # Negative control (separate assertion, separate fixture path): a safe file must NOT.
    reflex_hits, reflex_denom = risk_reflex(
        risk_fx, ["data/inf/scripts/silver/build_assets_dim.py", "totally/safe/new_file.py"])
    ck("reflex.fires_on_a_held_file_in_the_diff",
       reflex_hits is not None and len(reflex_hits) == 1
       and reflex_hits[0]["severity"] == "HOLD"
       and reflex_hits[0]["path"].endswith("build_assets_dim.py"))
    ck("reflex.does_not_flag_the_safe_file",
       reflex_hits is not None and all("safe" not in h["path"] for h in reflex_hits),
       "an alarm that fires on everything is an alarm nobody reads")
    ck("reflex.denominator_counts_every_file", reflex_denom["files_checked"] == 2)
    ck("reflex.carries_its_citation",
       bool(reflex_hits) and bool(reflex_hits[0]["claim"].get("doc")))

    class _Absent:  # a Source stand-in for a missing danger map
        exists = False
        stale = False
        vintage = "UNKNOWN-VINTAGE (absent)"
        def load_json(self):
            return None

    absent_hits, _ = risk_reflex(_Absent(), ["anything.py"])
    ck("reflex.absent_map_is_None_not_clean", absent_hits is None,
       "'could not check' must NEVER render as 'checked clean'")
    ck("reflex.absent_map_renders_CANNOT_clear",
       "CANNOT clear" in render_reflex(absent_hits, {"files_checked": 1, "danger_nodes": 0},
                                       _Absent(), "test"))

    # ---- decay: this week's road is wider than last month's.
    ck("decay.recent_outweighs_old", _decay(0) > _decay(HALF_LIFE_DAYS) > _decay(30),
       "roads narrow too")

    # ---- LIVE: the real estate renders and the sources are declared.
    live = compile_pulse(days=7, invocation="self-test")
    live_txt = render(live)
    ck("live.renders", isinstance(live_txt, str) and len(live_txt) > 400)
    ck("live.every_number_has_a_source_declared", len(live["sources"]) == 4)
    ck("live.invocation_is_pinned_in_output", "INVOCATION" in live_txt and "self-test" in live_txt,
       "a number nobody can re-derive is not evidence (CVO P2 class, 2d2080e1e)")
    ck("live.systems_band_is_declared_not_omitted", "[SYSTEMS]" in live_txt and "UNKNOWN" in live_txt)

    ok = all(results)
    print("\n" + ("OK: vital signs compile; DANGER x TRAFFIC fires; and an absent source is "
                  "UNKNOWN-VINTAGE, never a confident zero" if ok else "ERROR: comp-pulse FAILED"))
    return 0 if ok else 1


def _staged_files() -> list:
    try:
        out = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=_caller_root(),
                             capture_output=True, text=True, timeout=20)
        return [ln.strip() for ln in out.stdout.splitlines() if ln.strip()]
    except Exception:  # noqa: BLE001
        return []


def _missing_subject_paths(paths: list[str]) -> list[str]:
    """Paths given to `diff` are repository subjects, not arbitrary strings.
    A nonexistent subject is a distinct answer-state from a measured clean
    result, so test it before consulting the danger map."""
    missing = []
    for path in paths:
        candidate = path if os.path.isabs(path) else os.path.join(_caller_root(), path)
        if not os.path.exists(candidate):
            missing.append(str(path))
    return missing


def _render_reflex_state(invocation: str, state: str, detail: str) -> str:
    return "\n".join([
        "comp-pulse diff -- THE PRE-COMMIT RISK REFLEX (NFRA_NERVES L5)",
        "  INVOCATION (pin beside any quoted result): %s" % invocation,
        "  ANSWER STATE: %s" % state,
        "  %s" % detail,
    ])


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-pulse",
                                 description="the estate's vital signs (NFRA_NERVES L5); read first each morning")
    ap.add_argument("cmd", nargs="?", default="pulse", choices=["pulse", "diff"],
                    help="pulse = the vital signs; diff = the pre-commit risk reflex")
    ap.add_argument("paths", nargs="*", help="diff mode: files to score (default: the staged set)")
    ap.add_argument("--days", type=int, default=7, help="attention window (default 7)")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--budget", type=float,
                    help="Rule T work ceiling in seconds (flag > COMP_BUDGET_S > default 90; 0 = unbounded)")
    ap.add_argument("--cursor", type=int, default=0,
                    help="resume after this last fully processed deterministic unit")
    ap.add_argument("--no-population", action="store_true",
                    help="diff mode: state that there is no file population to score")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass

    if args.self_test:
        return _self_test()

    if args.cursor < 0:
        ap.error("--cursor must be >= 0")
    try:
        budget_s, budget_source = resolve_budget(args.budget)
    except ValueError as exc:
        ap.error(str(exc))

    invocation = "cmd=%s days=%d top=%d (argv: %s)" % (
        args.cmd, args.days, args.top, " ".join(sys.argv[1:]) or "<defaults>")

    if args.cmd == "diff":
        paths = [] if args.no_population else (args.paths or _staged_files())
        if not paths:
            print(_render_reflex_state(
                invocation, "NOT_APPLICABLE",
                "no staged or supplied paths: this diff mode has no population to score."))
            print("  " + disclosure_line(budget_s, budget_source))
            return 0
        missing = _missing_subject_paths(paths)
        if missing:
            print(_render_reflex_state(
                invocation, "SUBJECT_ABSENT_FROM_CORPUS",
                "the supplied repository subject(s) do not exist: %s" % ", ".join(missing)))
            print("  " + disclosure_line(budget_s, budget_source))
            return 2
        risk_src, rebuild_note, blind = resolve_risk_map(_WS, RISK)
        if blind:
            print(_render_reflex_state(invocation, "PARTIAL_OR_BLIND",
                                       "BLIND: sparse worktree, no map"))
            print("  " + rebuild_note + " -- NOT-DECIDABLE: the reflex CANNOT clear this diff.")
            print("  " + disclosure_line(budget_s, budget_source))
            return 2
        clock = Clock(budget_s)
        hits, denom = risk_reflex(risk_src, paths, clock=clock, cursor=args.cursor)
        if rebuild_note:
            denom = dict(denom, rebuild_note=rebuild_note)
        if args.json:
            print(json.dumps({"invocation": invocation, "hits": hits, "denominators": denom,
                              "map_vintage": risk_src.vintage,
                              "budget": disclosure_line(budget_s, budget_source)}, indent=1, default=str))
        else:
            print(render_reflex(hits, denom, risk_src, invocation))
            if denom.get("reason") == "budget reached":
                print("  " + budget_reached_line(
                    budget_s, budget_source, denom["files_checked"], denom["total_files"],
                    "file(s)", "comp-pulse diff", str(denom["cursor"])))
            else:
                print("  " + within_budget_line(
                    denom.get("files_checked", 0), denom.get("total_files", len(paths)), "file(s)",
                    budget_s, budget_source, clock.elapsed()))
        # exit contract: 0 clean / 1 the reflex FIRED / 2 the map is absent (CANNOT clear --
        # distinct from clean, because 'could not check' must never read as 'checked clean').
        if hits is None:
            return 2
        return 1 if hits else 0

    p = compile_pulse(args.days, args.top, invocation, budget_s=budget_s,
                      budget_source=budget_source, cursor=args.cursor)
    if args.json:
        print(json.dumps(p, indent=1, default=str))
    else:
        print(render(p))
    # EXIT 1 when the immune response is FIRING: a held/incident node is under active traffic. This
    # is a report, but that condition is not merely informational -- it is the one thing on this
    # page that should stop someone mid-keystroke.
    if (p.get("budget") or {}).get("reached"):
        return 0
    if p["danger_x_traffic"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
