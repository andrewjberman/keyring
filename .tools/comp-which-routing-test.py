#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""comp-which ROUTING-QUALITY HARNESS -- NFRA_COMPASSURANCE TO-1.

Measures comp-which against A DENOMINATOR NOBODY ON THIS PROJECT AUTHORED.

WHY THIS FILE WAS REPLACED (read before you "simplify" it back)
---------------------------------------------------------------
The harness that stood here scored a fixed corpus: each tool fed its OWN use_case
sentence (TEST 1), 20 hand-written paraphrases, 3 audit cases. Its own docstring
already confessed the flaw -- "TEST 1 is near-tautological ... a green TEST 1 says
nothing about how an AGENT actually phrases a question" -- and it kept TEST 1 as a
blocking assertion anyway.

    A probe drawn from a catalog entry's own description, scored against a catalog
    built from that same text, measures STRING SELF-IDENTITY -- not routing. It is
    not merely weak. It is ANTI-CORRELATED with the defect: brightest exactly where
    catalog and agent vocabulary COINCIDE (where there is NO hole) and dimmest where
    they diverge (where the hole IS).
                        IT IS BRIGHTEST WHERE THE GAP IS DEEPEST.

MEASURED (2.0.0_SA_COO~Z, @52d008f4c): catalog-derived probes report an 18.2%
coverage hole. Real agent questions: 44.4%. It UNDERSTATES THE DEFECT IT EXISTS TO
MEASURE BY 2.4x -- while printing an honest-looking denominator and passing its own
control. An anti-correlated instrument survives every control that catches a merely
noisy one: it passes them BY BEING WRONG IN THE USEFUL DIRECTION.

AND THE OLD HARNESS WAS NOT A BYSTANDER -- IT WAS THE POLLUTER. It shelled out to the
live binary against the real workspace, so every run appended ROUTE rows to the very
rail log this harness must measure. Fingerprint (strings that exist ONLY in that file,
counted in the log): "could the AdvisorsTab leak a client SSN to the browser?" x39,
"which directories are dead and safe to delete?" x41. IT RAN AT LEAST 41 TIMES.
76.0% of q-bearing ROUTE rows are a fixed corpus replayed at machine pacing.

    ==> THE INSTRUMENT BUILT TO MEASURE THE ROUTER HAD BECOME THE LARGEST SINGLE
        AUTHOR OF THE TRAFFIC IT WAS MEASURING.

    ==> IF YOU EVER IMPROVE THE HEADLINE BY CHANGING HOW THE PROBES ARE MADE: STOP.
        YOU HAVE JUST RE-AUTHORED THE DENOMINATOR.

THE THREE COHORTS
-----------------
  R  REAL / HEADLINE   de-duplicated organic tail of the rail log. AGENTS WROTE IT,
                       NOT US. Metric = ZERO-SCORE RATE, and it is LABEL-FREE: "what
                       fraction of real agent questions does the catalog have no
                       vocabulary for" needs no ground truth, no hand-labeling, and
                       nothing to argue about. Reported as a BRACKET (R_raw upper /
                       R_strict lower) -- NEVER a point estimate.
  C  CATALOG / FLOOR   generated from use_case. Labeled by construction. A SELF-
                       CONSISTENCY CHECK, EXPLICITLY NOT THE HEADLINE. If C is not
                       near-ceiling that is its own finding: the catalog cannot
                       retrieve itself.
  G  GIBBERISH / GATE  GENERATED (seeded), never hand-picked -- a hand-chosen negative
                       control measures the AUTHOR; a generated one measures the
                       INSTRUMENT. ANY gibberish probe that returns a route FAILS the
                       run. Zero-tolerance, not a rate: a gibberish query has no
                       correct route, so one route is not noise -- it is the defect
                       reproducing itself in front of you.

TWO LAYERS -- GRADING THE WRONG ONE IS THE CLASSIC FAILURE HERE
---------------------------------------------------------------
  L1 RULES   comp-which's own _score_rule over its own RULES (n=46).
             KEYWORDS ARE r[0]. r[1] is the DESCRIPTION STRING; passing it makes
             _score_rule iterate its CHARACTERS, match " " as a phrase, and award
             +3 PER SPACE -- gibberish then scores 33 and every number in the table
             is a space count wearing a score's costume. This harness reproduces that
             bug ON PURPOSE as an anti-control (see r1_anticontrol).
  L2 LIVE    the real binary, in a real subprocess. The RULES layer PASSES the
             gibberish control at 100% zero; the live MIS-ROUTE happens DOWNSTREAM in
             the POSTERIOR / manifest-fuzzy backstop. A harness that grades only RULES
             GRADES THE LAYER THAT IS NOT FAILING -- F-1 ("the guard exists; the live
             path never reaches it") turned on the harness itself.

THE MEASURING ACT MUST NOT MUTATE THE MEASURED THING
----------------------------------------------------
comp-which appends a ROUTE row to the rail log on EVERY invocation (_log_rail; no
suppress flag; WS is derived from __file__ so the path is not overridable) and a row
to the training queue. Cohort R is the set of questions seen EXACTLY ONCE. So probing
the live binary with cohort R would make every R-probe a duplicate and EJECT IT FROM
THE NEXT RUN'S COHORT R -- the instrument would destroy its own denominator on first
use, AND THE DESTROYED RUN WOULD NOT LOOK BROKEN (a plausible n, a plausible rate; a
silently-swapped denominator reads exactly like a real improvement).
  ==> We run the binary inside a SCRATCH MIRROR whose WS resolves to a temp tree, so
      RAIL_LOG lands there. The real log is never written -- PROVEN every run, not
      assumed. An assertion never exercised has never been tested.

THE COHORT IS FROZEN, NOT RE-DERIVED
------------------------------------
The rail log is APPEND-LIVE and the whole fabric routes through comp-which.
    A COHORT DEFINED BY A QUERY OVER A MUTABLE LOG IS NOT A POPULATION.
    IT IS A TIMESTAMP.
So --freeze materializes THE ACTUAL PROBE STRINGS into a committed artifact, and every
later run measures THAT LIST. TO-2/TO-3 regress against the frozen list; they do not
re-derive it. A baseline that re-derives its own population is a fresh measurement
wearing a baseline's name.

AND THE SAME RULE BINDS ANYONE QUOTING A HEADLINE **DELTA** (CVO~Z P2, 3d816c650; the
framing AMENDED by its own author at 04968a7f3 -- see below). The RULE: a delta quoted
across two runs must have BOTH ENDS measured against ONE cohort. Re-freeze a comparison
cohort (--freeze), measure both ends against that list, or print both denominators next
to both numbers.

  PROVENANCE, because a doctrine line should not rest on a claim its author retracted:
  CVO~Z first justified this by saying cohort R "re-derives from the live rail log each
  run." THAT IS WRONG AND SHE RETRACTED IT HERSELF -- the cohort IS frozen (:87-93, :879
  of this file). The DOCTRINE SURVIVES THE RETRACTION on the stronger ground she then
  used in practice: a delta is only interpretable when BOTH ENDS sit on the SAME frozen
  cohort, which is exactly how she measured 26.441% -> 25.050% (n=562, one cohort, both
  ends). A self-retracted premise is a better artifact than an unexamined one; the rule
  is kept, its bad justification is not.

A FIXTURE THAT CANNOT REACH THE CAP CANNOT TEST THE CAP
-------------------------------------------------------
(NFRA_INSTDRILL F1, 2026-07-14. CVO~Z found it in comp-icedrill; it is a doctrine line,
not a bug report, and it belongs here beside the other controls that lied.)

comp-icedrill silently truncated an S3 listing at 2,000 keys and presented the HORIZON
as a COMPLETE ANSWER. It shipped with a GREEN self-test on top of the bug. The test could
not have failed: its stub returned every object in ONE page, so the fixture was
CAP-BLIND BY CONSTRUCTION -- no number of additional cases would ever have reached the
2,000-key boundary. The suite was not weak. It was STRUCTURALLY INCAPABLE of the finding.

    A CONTROL IS ONLY A CONTROL AT THE SCALE IT CAN ACTUALLY REACH.
    ASK OF EVERY FIXTURE: WHAT IS THE SMALLEST INPUT THAT WOULD MAKE THIS FAIL --
    AND CAN MY FIXTURE EVEN PRODUCE IT?

Two corollaries, both paid for:
  * THE "INDEPENDENT" CHECK THAT SHARES THE FLAW AGREES WITH ITSELF. The live acceptance
    claimed parity with "an independent aws s3 ls" -- but the independent check evidently
    read the same capped axis, so it CORROBORATED the lie. An independent instrument that
    shares your defect is not a second opinion; it is an echo.
  * THE CHEAPEST REFUTATION IS AN INTERNAL ONE. What actually killed it needed no external
    truth at all: a CHILD scope reported 2,000 while its PARENT reported 1,394.
    child > parent is impossible. LOOK FOR THE INVARIANT YOUR OWN OUTPUT MUST OBEY --
    it is available even when ground truth is not, and it cannot be corrupted by the
    same bug.
Both are now assertions in comp_icedrill's own suite (paginating stub; parent >= child).

THE SUBJECT IS PINNED TO A VINTAGE
----------------------------------
Other lanes edit .tools/comp-which mid-flight (observed twice in one hour during this
TO's own construction). --binary-ref extracts the binary from a git ref and STAMPS THE
BLOB HASH, so the artifact always states WHICH BYTES it measured.
    A LINE CITATION WITHOUT A VINTAGE IS NOT A CITATION, and a provenance record that
    captures WHAT but not WHEN is not provenance.

EXIT CODES -- three, because "broken" has two very different meanings
---------------------------------------------------------------------
  0  PASS              controls held, no pollution, comp-which abstained on ALL gibberish.
  1  SUBJECT FAILED    comp-which ROUTED gibberish. THE DEFECT, faithfully reported.
                       Expected TODAY. TO-2 (the abstain) is what flips this to 0.
  2  INSTRUMENT FAILED the harness's OWN controls failed. DISCARD ITS NUMBERS.
                       An instrument that cannot fail is not an instrument.

usage:
  python .tools/comp-which-routing-test.py --freeze <rail-log-snapshot>
  python .tools/comp-which-routing-test.py                      # baseline @ HEAD
  python .tools/comp-which-routing-test.py --binary-ref WORKING # the dirty tree
  python .tools/comp-which-routing-test.py --mutate zero|nine   # prove it can FAIL

-- 0.8.0_AE_CloudComp~Z   (NFRA_COMPASSURANCE.TO-1)
"""
from __future__ import annotations

import argparse
import collections
import datetime
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import types

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BINARY = os.path.join(WS, ".tools", "comp-which")
RAIL_LOG = os.path.join(WS, "org", "mcp", "comp-which-rail.log")
TRAINING_QUEUE = os.path.join(WS, "org", "mcp", "comproute-routing.jsonl")
MANIFEST = os.path.join(WS, "org", "modules", "graph", "graph-call-manifest.yaml")
GRAPH_MODS = os.path.join(WS, "org", "modules", "graph")
# The artifacts live in the AUTHORING LANE'S deliverables dir, not in org/modules/graph/.
# org/modules/graph/ is an ANY_EXEC owned-path (exec agents only) and the owned-paths gate
# correctly BLOCKED an AE writing there. The gate is right and it was not bypassed:
# --force exists and is audited, and amending a permission config to admit your own change
# is how a guard dies. FILE WHERE THE RULES ALLOW; DO NOT MOVE THE RULES.
_DELIV = os.path.join(WS, "org", "tier2_senior", "0.8.0_AE_CloudComp", "deliverables")
FROZEN = os.path.join(_DELIV, "comp-which-routing-cohort.frozen.json")
BASELINE = os.path.join(_DELIV, "comp-which-routing-baseline.json")

GIBBERISH_SEED = 7
GIBBERISH_N = 40
TOPK = 3  # Andrew-direct: k=3, NEVER 1. Not a tuning knob.

# The POSITIVE control. A question the catalog demonstrably owns. Run in ISOLATION --
# a control batched with its target is corrupted by its own presence (Rule 22a).
POSITIVE_CONTROL = "what breaks if I change this function"

# Exact-match strip list -> R_strict, the LOWER bound of the bracket. These are agents'
# OWN probe strings; they legitimately score zero and SHOULD. The list is PRINTED IN
# FULL, as strings, every run -- a judgment you cannot audit must be TRUSTED, while a
# judgment whose every input is printed can be CHECKED by someone who has never met the
# author and disagrees with them.
# WHEN IN DOUBT, DO NOT STRIP. An un-stripped probe inflates R_raw -- a bound we already
# declare unsafe to defend. A wrongly-stripped one silently deletes a real coverage gap
# AND MAKES US LOOK BETTER. Only one of those two errors flatters us. Prefer the other.
PROBE_TOKENS = (
    "xyzzy",
    "asdkfjhaskdjfh",
    "asdfqwerzxcv",
    "qwerasdf",
    "zzz probe",
    "nonsense control",
    "todo fixme",
    "lorem ipsum",
)


def _utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# AC14 -- a HUD-INJECTED SEARCH PATTERN, not a natural-language question.
# comp-tool-hud.sh:291 pipes the agent's RAW SEARCH QUERY into `comp-which --route-only`,
# and --route-only still writes the rail row. So the log carries glob/grep PATTERNS
# ('**/*COMPASSURANCE*') that were never questions. They score zero BECAUSE THEY ARE NOT
# QUESTIONS -- not because the catalog lacks vocabulary for them -- and they INFLATE the
# headline. This detector is a REPORTING aid, never a silent strip: it has known false
# positives, and a hand-authored strip measures the AUTHOR. It WIDENS the bracket.
_PATTERN_RX = re.compile(
    r"\*\*/|[\[\]{}]|\\[dwsb]|^[-.]|\.(?:py|tsx?|jsx?|json|ya?ml|md|sh|tf|hcl)$|^\*")


def _IS_PATTERN(q):
    q = (q or "").strip()
    return bool(_PATTERN_RX.search(q)) or (" " not in q)


# =============================================================================
# PUBLIC CONTRACT -- DO NOT DELETE. A FAIL-CLOSED COMMIT GATE CALLS THIS.
# =============================================================================
# `comp-manifest-check` loads THIS FILE as module `cwrt` (SourceFileLoader) and calls
# self_route_verdicts(). It is a REPO-WIDE, FAIL-CLOSED invariant: if the symbol is
# missing the gate BLOCKS EVERY AGENT'S COMMIT OF EVERY FILE -- including .md files --
# and --force does NOT bypass it. Exported deliberately at 5e9bfea7b as "the ONE
# definition of the self-routing property" so a gate would not fork its own invariant.
#
# I DELETED IT IN THE FIRST DRAFT OF THIS REWRITE AND BLOCKED THE ENTIRE WORKTREE.
# Two instruments failed to warn me, and the second one was me:
#   1. `comp-blast comp-which` -> NOT-FOUND. THE COMPILER GRAPH DOES NOT MODEL THE
#      COMPILER TOOLS (PRD F-5), so no comp-tool we own CAN surface a consumer of a
#      .tools/ module. Every instrument said it was safe to delete.
#   2. My own reverse-dependency grep -- WHICH I PIPED THROUGH `head` AND THEN REASONED
#      FROM AS IF IT WERE COMPLETE. The consumer was below the cut.
#
#      A TRUNCATED SCAN IS NOT A NEGATIVE RESULT. PRINT THE DENOMINATOR OF EVERY SCAN
#      YOU REASON FROM -- INCLUDING THE ONE YOU RAN TO PROVE YOURSELF SAFE.
#
# BEHAVIOUR PRESERVED VERBATIM (working tree, real binary, real subprocess). It is NOT
# routed through this harness's non-polluting mirror, because that would silently change
# a gate's semantics -- the gate deliberately checks the WORKING TREE, and redesigning
# another lane's gate is not this TO's business.
# KNOWN CONSEQUENCE, FLAGGED NOT FIXED: this function shells the live binary once per
# tool against the REAL workspace, so every gate run APPENDS ROUTE ROWS TO THE RAIL LOG.
# It is a confirmed author of the machine-replayed traffic this harness had to route
# around (fingerprint: fixed corpus strings at 39-41x). That is a real finding and it
# belongs to TO-2/TO-4 -- NOT to a worker who happens to be holding the file.
# =============================================================================
COMP_WHICH = BINARY
# THE THREE PRIMITIVES STAY HARD-CODED, AND ONLY THEY. comp-grep/comp-glob are the never-dead-end
# FALLBACK (surfaced via route()'s kind="fallback", not as scored candidates) and comp-which is the
# router itself -- three tools that are structurally unrankable, not three tools somebody decided to
# skip. Everything else is exempted BY DECLARED STATUS below, never by adding a name here.
EXCLUDE = {"comp-grep", "comp-glob", "comp-which"}

# ---- DECLARED-STATUS EXEMPTION (NFRA_CLDGRPH R14a, PRD v0.12 @b77a6c3a27; 2.0.0_SA_COO~A's
#      in-grant ruling on row NFRA_CLDGRPH-W6-S2, cell CG-s-30) ---------------------------------
# WHY THIS EXISTS: "registered-implies-reachable" is the right invariant and it was enforced with
# the wrong rule. comp-aws was DEPRECATED FOR AGENT USE and pulled out of comp-which selection on
# Andrew's word (2026-09-09), which makes "comp-which returns nothing naming it" the DELIVERABLE --
# and this member hard-blocked the very commit that produced it. The fix is not to widen EXCLUDE:
# an enumerated ban list lapses SILENTLY the moment a name changes (CLAUDE.md s.5), and a tool
# deprecated tomorrow would rediscover this block from scratch.
#
# THE RULE: a tool is exempt from the self-route requirement iff it DECLARES a status of `retired`
# or `deprecated`, at EITHER grain --
#   TOOL grain   org/modules/graph/comp-coverage-map.yaml  tools[]/meta_tools[] `status:`
#                (the population authority, CTO ruling #1)
#   ENTRY grain  org/modules/graph/graph-call-manifest.yaml tools_index[t] `status:`  (R14/R14a)
# R14a binds the two: an entry may carry `deprecated` ONLY when its tool is `deprecated` at TOOL
# grain, so the grains never disagree; both values are do-not-route and only `retired` is
# do-not-call. Reading BOTH is deliberate -- either grain alone would make this member's answer
# depend on which file a lane happened to edit first.
#
# NEVER A SILENT SKIP: selfroute_exempt_set() returns the set WITH its reason per tool, and the
# caller PRINTS it as a denominator (`SELFROUTE_EXEMPT=<n> (deprecated: ...; retired: ...)`).
# An exemption nobody can see is indistinguishable from a check that stopped running.
# FAIL-CLOSED: an unreadable map or manifest yields an EMPTY exempt set, so the invariant keeps its
# full strength rather than exempting everything on a parse error.
_EXEMPT_STATUSES = ("retired", "deprecated")
COVERAGE_MAP = os.path.join(WS, "org", "modules", "graph", "comp-coverage-map.yaml")

_ARROW = re.compile(r"^\s*->\s*(\S+)")


def _declared_status_by_tool(manifest):
    """{tool: (status, grain)} for every tool DECLARING an exempting status at either grain.

    The TOOL grain (the population authority) is read first because it is the authority; the ENTRY
    grain is read second and only fills in a tool the map did not already name, so a disagreement
    can never silently downgrade the authority's value. R14a forbids the disagreement outright;
    this order of reads means a violation of R14a shows up as the map's value, not the manifest's.
    """
    out = {}
    try:
        import yaml
        with open(COVERAGE_MAP, encoding="utf-8") as fh:
            cm = yaml.safe_load(fh) or {}
        for section in ("tools", "meta_tools"):
            for row in (cm.get(section) or []):
                if isinstance(row, dict) and row.get("tool"):
                    st = str(row.get("status") or "active").strip()
                    if st in _EXEMPT_STATUSES:
                        out[str(row["tool"]).strip()] = (st, "map-tool-grain")
    except Exception:
        pass  # fail-closed: no exemption from a grain that could not be read
    try:
        for tool, entry in (manifest.get("tools_index", {}) or {}).items():
            if not isinstance(entry, dict):
                continue
            st = str(entry.get("status") or "").strip()
            if st in _EXEMPT_STATUSES and tool not in out:
                out[str(tool).strip()] = (st, "manifest-entry-grain")
    except Exception:
        pass
    return out


def selfroute_exempt_set(manifest):
    """({tool: (status, grain)}, printable_line). The line is the DENOMINATOR a caller prints."""
    ex = _declared_status_by_tool(manifest)
    if not ex:
        line = "SELFROUTE_EXEMPT=0 (no tool declares status retired|deprecated at either grain)"
        return ex, line
    by_status = {}
    for tool, (st, grain) in sorted(ex.items()):
        by_status.setdefault(st, []).append("%s[%s]" % (tool, grain))
    parts = "; ".join("%s: %s" % (st, ", ".join(v)) for st, v in sorted(by_status.items()))
    return ex, "SELFROUTE_EXEMPT=%d (%s)" % (len(ex), parts)


def _load_manifest():
    import yaml
    with open(MANIFEST, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _run_comp_which(q: str) -> str:
    r = subprocess.run([sys.executable, COMP_WHICH, q],
                       cwd=WS, capture_output=True, text=True, timeout=60)
    return (r.stdout or "") + (r.stderr or "")


# --- WARM IN-PROCESS ROUTE (NFRA_TOOLARCH self-route gate, 0.8.0_AE_CloudComp~B 2026-07-24) ------
# WHY: the member spawned 68 subprocesses at ~1357ms each. The cost driver is INTERPRETER STARTUP +
# the import graph, paid 68 times to do 68 vocabulary lookups -- not the check. This pays it ONCE.
# COST-PER-ITEM ONLY: the denominator does not move by a single tool (CTO~Z standing constraint).
#
# WHY A WARM INVOCATION OF comp-which's OWN main() AND NOT A RE-IMPLEMENTATION of _score_rule:
# verdict-identity becomes TRUE BY CONSTRUCTION rather than something proven across 68 and then
# re-proven forever -- same code, same ranking, same emitted text. A re-implementation would drift
# SILENTLY the moment comp-which's ranking changed, and the gate would keep passing while measuring
# a router nobody runs. (CTO~Z adopted this over their own _score_rule direction, 034628Z.)
# DECISIVE, and the reason a re-implementation could not have worked here at all: the consumer is NOT
# only the `-> ` regex -- `self_route_verdict` also does `if tool not in out`, a substring test over
# the WHOLE stdout+stderr text. Only re-emitting comp-which's real output can reproduce that.
#
# STEP 2 (0.8.0_AE_CloudComp~B): verdict-identity proven 65/65 (see NFRA_TOOLARCH.GATEBOUND TO,
# `<inherited_state_do_not_rederive>`). NOTHING was switched yet at that point -- `_run_comp_which`
# stayed the live path deliberately, so the gate never passed through a half-switched state.
#
# STEP 3 / FLIP (0.8.0_AE_CloudComp~D, 2026-07-25, NFRA_TOOLARCH.GATEBOUND Stage A): `self_route_
# verdict` now calls `_run_comp_which_warm_bounded` (below), NOT `_run_comp_which`. The flip landed
# only after mutants (a)/(b) held per the TO's acceptance criteria 1-4 -- see the GATEBOUND
# deliverable for the mutant runs. `_run_comp_which` is INTENTIONALLY KEPT, unused by the live path:
# it is the pre-flip reference implementation the regression check (verdict-identity, re-run POST-
# flip) compares against. Deleting it would remove the only independent oracle for that regression.
_COMP_WHICH_MOD = None


def _load_comp_which():
    """Load comp-which ONCE under a NON-'__main__' module name so its `if __name__ == '__main__'`
    entry does not fire on import. Cached across calls -- that cache IS the win."""
    global _COMP_WHICH_MOD
    if _COMP_WHICH_MOD is None:
        import importlib.machinery
        import importlib.util
        spec = importlib.util.spec_from_loader(
            "comp_which_warm",
            importlib.machinery.SourceFileLoader("comp_which_warm", COMP_WHICH),
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _COMP_WHICH_MOD = mod
    return _COMP_WHICH_MOD


def _run_comp_which_warm(q: str) -> str:
    """Warm equivalent of `_run_comp_which`: same argv shape, same cwd, same combined stdout+stderr.

    Matches the subprocess contract deliberately: subprocess.run used cwd=WS, so we chdir to WS for
    the call and restore -- comp-which resolves paths relative to cwd, and a cwd difference would be
    a silent behavioural divergence rather than a loud one.
    SystemExit is caught because main() is normally invoked via `raise SystemExit(main())`.
    """
    import contextlib
    import importlib.machinery  # noqa: F401  (used via importlib.machinery in _load_comp_which)
    import io
    mod = _load_comp_which()
    buf_out, buf_err = io.StringIO(), io.StringIO()
    argv_saved, cwd_saved = sys.argv[:], os.getcwd()
    try:
        os.chdir(WS)
        sys.argv = [COMP_WHICH, q]
        with contextlib.redirect_stdout(buf_out), contextlib.redirect_stderr(buf_err):
            try:
                mod.main()
            except SystemExit:
                pass
    finally:
        sys.argv = argv_saved
        try:
            os.chdir(cwd_saved)
        except OSError:
            pass
    return buf_out.getvalue() + buf_err.getvalue()


# --- WATCHDOG BOUND on the warm path (NFRA_TOOLARCH.GATEBOUND Stage A, 0.8.0_AE_CloudComp~D
# 2026-07-25) ----------------------------------------------------------------------------------
# INHERITED FACT, do not re-derive: comp-which has exactly ONE hang-capable call --
# `subprocess.call([...])` at comp-which:1201 (the comp-grep/comp-glob fallback), no timeout.
# `_run_comp_which_warm` reaches it via `mod.main()`, so the warm path inherits the same
# unbounded-hang exposure the subprocess path always had. THIS WRAPPER BOUNDS THE GATE. IT DOES
# NOT KILL THE HANG -- Python has no API to force-terminate another thread, only to stop waiting
# on it. That is Design B's job (comp-which:1201 itself gets timeout+kill), landing separately.
# Report this distinction explicitly wherever this function's behavior is described: a caller
# that times out here has PROVEN THE GATE COMPLETES, not that the underlying compute stopped.
#
# WHY A LOCK, NOT JUST A DEADLINE: `_run_comp_which_warm` mutates PROCESS-GLOBAL state
# (`sys.argv`, `os.getcwd()`, and -- via `contextlib.redirect_stdout/stderr` -- `sys.stdout`/
# `sys.stderr` themselves). None of that is thread-local. If a timed-out call's worker thread is
# simply abandoned and a LATER call starts a second worker thread while the first is still
# inside `mod.main()`, the two threads race the same globals: the second call's redirect can
# silently steal the first (still-running) call's output mid-flight, corrupting BOTH results
# without either one raising. A non-blocking `Lock` closes this: once a worker thread is
# abandoned past its deadline, it is NEVER released, so every SUBSEQUENT call in this process
# fails `acquire(blocking=False)` immediately and reports UNEVALUABLE without ever touching the
# shared globals -- no race, no silent corruption, and the failure mode after one hang is "every
# further self-route call in this process returns fast and UNEVALUABLE," which is the honest,
# bounded shape Design A promises (once one call hangs, the REST of the run finishes in
# O(remaining tools) time instead of hanging again per tool).
_WARM_LOCK = threading.Lock()

# 20s is not tuned against a measured warm-call latency distribution -- it is chosen to be an
# order of magnitude above any observed warm call (sub-second to low single-digit seconds per
# TO-1's own cost accounting) while remaining far below the 84-minute hang class this bound
# exists to catch. If real warm latency is ever shown to approach this, raise it with evidence;
# do not lower it without re-measuring.
WARM_DEADLINE_S = 20.0


def _run_comp_which_warm_bounded(q: str, deadline: float = None):
    """(ok, text). ok=False means UNEVALUABLE -- either this call's own worker thread did not
    finish inside `deadline`, or an EARLIER call's worker thread is still holding `_WARM_LOCK`
    (see the module comment above for why that must fail closed rather than race).

    The abandoned worker thread is a daemon thread: it is never force-killed (CPython cannot do
    that), it keeps running until it finishes or the process exits, and it keeps `_WARM_LOCK`
    held forever if it never finishes. That is CONTINUED-PAST, not KILLED -- state it that way,
    never as "the hang was stopped."

    `deadline=None` (not `=WARM_DEADLINE_S`) DELIBERATELY -- a mutable-looking module global as
    a DEFAULT ARGUMENT VALUE binds at FUNCTION-DEFINITION time, not call time (CVO~Z, GATEBOUND
    Stage A verification, 2026-07-25): `WARM_DEADLINE_S = 2.0` after import silently does
    NOTHING to a caller relying on the default, because the def-time value is already baked into
    the function object. The knob LOOKS settable and silently isn't -- resolving it inside the
    body, against the CURRENT module global, is what makes it actually tunable.
    """
    if deadline is None:
        deadline = WARM_DEADLINE_S
    got_lock = _WARM_LOCK.acquire(blocking=False)
    if not got_lock:
        return False, None
    result = {}

    def _worker():
        try:
            result["text"] = _run_comp_which_warm(q)
        except Exception as e:  # surfaced to the caller only on the fast path, below
            result["error"] = e

    t = threading.Thread(target=_worker, daemon=True)
    t.start()
    t.join(deadline)
    if t.is_alive():
        return False, None  # deadline breached; _WARM_LOCK intentionally NOT released
    _WARM_LOCK.release()
    if "error" in result:
        raise result["error"]
    return True, result.get("text", "")


def self_route_query(manifest, tool):
    """The tool's OWN richest sentence -- its manifest use_case if it has one, else its
    tools_index `does`."""
    by_tool = {}
    for e in (manifest.get("entries") or []):
        by_tool.setdefault(str(e.get("tool", "")).split()[0], []).append(e)
    ucs = by_tool.get(tool, [])
    ti = manifest.get("tools_index", {})
    return (ucs[0]["use_case"] if ucs else ti.get(tool, {}).get("does", "")).strip().rstrip("?.")


def self_route_verdict(manifest, tool):
    """(verdict, ranked, query) for ONE tool. verdict in {RANK1, NEARTIE, MISS, UNEVALUABLE}.

    MISS    -- comp-which does not surface the tool AT ALL for its own use_case.
               DETERMINISTIC + role-invariant -> a gate MAY hard-block on it.
    NEARTIE -- surfaces, but never rank-1. THRESHOLD-shaped -> a gate must only WARN.
    RANK1   -- the router decided on it.
    UNEVALUABLE -- the call did not complete inside the watchdog deadline (GATEBOUND Stage A,
               0.8.0_AE_CloudComp~D 2026-07-25), or an earlier call in this process hung and
               never released the shared warm-call resource. NOT a claim the tool fails to
               route -- a claim the ROUTE IS UNKNOWN. Must be reported as its own outcome,
               never folded into MISS (a false "does not route" is worse than an honest
               "could not confirm") and never silently dropped from the population.
    (CTO ruling: "every hard-blocking member asserts a DETERMINISTIC fact; anything
    threshold-shaped REPORTS.")

    NOTE FOR TO-2/TO-4, NOT ACTED ON HERE: this is the catalog-self-identity probe --
    a tool fed its OWN use_case text and asked whether the catalog can find it. It is a
    SELF-CONSISTENCY check (cohort C), NOT a coverage measurement, and it must never be
    read as one. It is exactly the anti-correlated design this harness was rewritten to
    stop reporting as a headline.
    """
    q = self_route_query(manifest, tool)
    ok, out = _run_comp_which_warm_bounded(q)
    if not ok:
        return "UNEVALUABLE", [], q
    ranked = [m.group(1) for m in (_ARROW.match(ln) for ln in out.split("\n")) if m]
    if tool not in out:
        return "MISS", ranked, q
    if ranked and ranked[0] == tool:
        return "RANK1", ranked, q
    return "NEARTIE", ranked, q


def self_route_verdicts(manifest, tools=None):
    """{tool: (verdict, ranked, query)} over `tools` (default: every routable tools_index
    tool). THE one definition of the self-routing property -- comp-manifest-check imports
    this rather than reimplementing it, because a gate that forks its invariant drifts
    from the tool agents actually run, and then disagrees with it."""
    ti = manifest.get("tools_index", {})
    # R14a @b77a6c3a27: a tool that DECLARES retired|deprecated at either grain is exempt from the
    # self-route requirement -- "registered-implies-reachable" was never meant to bind a tool the
    # estate has deliberately unrouted. The exempt set is PRINTED by the caller, never silent.
    exempt, exempt_line = selfroute_exempt_set(manifest)
    universe = [t for t in sorted(ti) if t not in EXCLUDE and t not in exempt]
    targets = [t for t in (tools if tools is not None else universe) if t in universe]
    print("  %s" % exempt_line)
    return {t: self_route_verdict(manifest, t) for t in targets}
# =============================== END PUBLIC CONTRACT =========================


# ---------------------------------------------------------------------------
# the subject under test -- pinned to a vintage
# ---------------------------------------------------------------------------
def git_blob_sha(ref):
    try:
        out = subprocess.run(["git", "-C", WS, "rev-parse", "%s:.tools/comp-which" % ref],
                             capture_output=True, text=True, timeout=20)
        return out.stdout.strip() if out.returncode == 0 else None
    except Exception:
        return None


def working_tree_blob():
    try:
        out = subprocess.run(["git", "-C", WS, "hash-object", BINARY],
                             capture_output=True, text=True, timeout=20)
        return out.stdout.strip() if out.returncode == 0 else None
    except Exception:
        return None


def extract_binary(ref, dest):
    """Materialize the binary AT A NAMED VINTAGE. Measuring the working tree would
    silently baseline whatever half-landed change another lane is mid-way through."""
    if ref is None:
        shutil.copyfile(BINARY, dest)
        return ("WORKING-TREE", working_tree_blob())
    out = subprocess.run(["git", "-C", WS, "show", "%s:.tools/comp-which" % ref],
                         capture_output=True, timeout=30)
    if out.returncode != 0 or not out.stdout:
        raise SystemExit("FATAL: cannot extract .tools/comp-which at ref '%s'" % ref)
    with open(dest, "wb") as fh:
        fh.write(out.stdout)
    return (ref, git_blob_sha(ref))


def load_module(path):
    """exec the binary to reach its OWN scorer over its OWN RULES. Not a
    reimplementation -- a reimplementation would measure my guess at the scorer."""
    src = open(path, encoding="utf-8").read()
    mod = types.ModuleType("cw_under_test")
    mod.__name__ = "cw_not_main"
    mod.__file__ = os.path.abspath(path)
    exec(compile(src, path, "exec"), mod.__dict__)  # noqa: S102
    return mod


def build_mirror(binary_src):
    """A scratch WS so RAIL_LOG lands in temp. comp-which derives WS from __file__, so
    moving the file moves every path it writes. The binary is BYTE-IDENTICAL -- only its
    filesystem root moves. This IS the live binary, not a stand-in."""
    root = tempfile.mkdtemp(prefix="cwrt_")
    os.makedirs(os.path.join(root, ".tools"))
    os.makedirs(os.path.join(root, "org", "mcp"))
    os.makedirs(os.path.join(root, ".comp-graph"))
    shutil.copyfile(binary_src, os.path.join(root, ".tools", "comp-which"))
    # "_compbudget.py" ADDED (NFRA_COMPEFFICACY CE-t-3, Rule T): comp-which now imports it
    # UNGUARDED at module level, same as comp-find's own precedent. Found live: the mirror's
    # POSITIVE-CONTROL invocation below (a real subprocess, not the warm in-process path) crashed
    # on ModuleNotFoundError before ever reaching main() -- zero stdout, zero rail row -- which
    # `run_no_pollution_check`'s own v4 alibi correctly read as MIRROR CAPTURES NOTHING and failed
    # the run (exit 2), exactly the absence-of-evidence class limb (b) exists to catch. This is not
    # a false alarm the control should be silenced for -- it is the control doing its job against
    # a genuine missing runtime dependency of the binary under test.
    for aux in ("comp-grep", "comp-glob", "_comprail.py", "_trino_fed.py", "_compbudget.py"):
        src = os.path.join(WS, ".tools", aux)
        if os.path.exists(src):
            shutil.copyfile(src, os.path.join(root, ".tools", aux))
    shutil.copytree(GRAPH_MODS, os.path.join(root, "org", "modules", "graph"))
    return root


# ---------------------------------------------------------------------------
# the two layers
# ---------------------------------------------------------------------------
def rules_score(mod, q):
    """L1. KEYWORDS ARE r[0]. See the r1_anticontrol for why this comment exists."""
    qtok = mod._tokens(q)
    scores = [mod._score_rule(q.lower(), qtok, r[0]) for r in mod.RULES]
    return max(scores) if scores else 0


_ROUTE_RX = re.compile(r"^\s*(?:\d+\.\s+score\s+[-\d.]+\s+|->\s*)(comp-\S+)")


_INVOCATIONS = [0]  # every live-binary route we issue. Our alibi has to add up.
_LAST_RC = []            # programmatic abstain  -- a SCRIPT sees this
_LAST_WARNED = []        # agent-facing abstain  -- an AGENT sees this
_LAST_RAN_FALLBACK = []  # PRD C-3: did it ACTUALLY RUN the primitive, or only print it?

# The agent-facing abstain banner. THIS IS THE LINE I MISSED BY SLICING STDOUT TO 6 LINES.
_ABSTAIN_RX = re.compile(
    r"NO CURATED RULE MATCHED|FUZZY GUESSES|CATALOG DOES NOT COVER IT|NO FIT", re.I)

# EXECUTION evidence -- proof the fallback RAN, not that it was RECOMMENDED.
# PRD C-3 requires comp-which to ACTUALLY RUN comp-grep/comp-glob: "No subjunctive."
#   the original defect:  "it WOULD RUN comp-grep -- never a dead-end"   (a promise)
#   the shipped fix:      "or search directly: comp-grep 'smbhbrej'"     (a suggestion)
# NEITHER OF THEM RUNS. THE SUBJUNCTIVE SURVIVED THE FIX: it changed GRAMMATICAL MOOD
# and not EPISTEMIC STATUS. A printed command is not a run command.
_EXEC_EVIDENCE_RX = re.compile(r"matches=|files=|scanned=|^\S+:\d+:", re.M)


def live_route(mirror_root, q, timeout=30):
    """L2 -- THE LIVE BINARY, real subprocess, inside the mirror. --route-only guards the
    grep/glob shell-out (the rail write still fires -- which is WHY we are in a mirror).
    Returns (routed, [tools])."""
    exe = os.path.join(mirror_root, ".tools", "comp-which")
    _INVOCATIONS[0] += 1
    try:
        out = subprocess.run([sys.executable, exe, "--route-only", q],
                             capture_output=True, text=True, timeout=timeout,
                             cwd=mirror_root)
    except Exception:
        return (False, [])
    text = out.stdout or ""
    tools = [] if "NO-ROUTE" in text else [
        m.group(1) for m in (_ROUTE_RX.match(ln) for ln in text.splitlines()) if m]
    # FOUR SIGNALS, MEASURED SEPARATELY AND ADJUDICATED BY NOBODY HERE.
    #
    # An earlier version of this function measured TWO and I built a finding on their
    # disagreement: "rc=1 fires but stdout still shows a menu -- AN AGENT READS STDOUT,
    # AN AGENT DOES NOT READ $?; the abstain is INVISIBLE." THAT CLAIM WAS FALSE, AND I
    # SHIPPED IT TO MY COO.
    #
    # It was false because I had printed the first SIX LINES of stdout and reasoned about
    # "what an agent sees" from the slice. The refutation was on line 11: a prominent
    # banner reading "NO CURATED RULE MATCHED ... These are FUZZY GUESSES, not a routing
    # decision ... do not pick one." THE ABSTAIN IS IN STDOUT. It is not invisible.
    #
    #     I TRUNCATED MY OWN EVIDENCE AND THEN REASONED FROM THE SLICE AS IF IT WERE THE
    #     WHOLE. It is the same error as the `head` that let me delete a gate's symbol,
    #     committed a third time, in the very argument I was most confident about.
    #     A TRUNCATED SCAN IS NOT A NEGATIVE RESULT -- INCLUDING WHEN IT IS YOUR OWN
    #     OUTPUT, AND ESPECIALLY WHEN IT AGREES WITH YOU.
    #
    # So we now capture EVERY signal and let the reader see all four:
    #   rc            the PROGRAMMATIC abstain (a script sees this)
    #   warned        the AGENT-FACING abstain banner (an agent sees this) -- I MISSED IT
    #   tools         a ranked, scored menu -- printed ABOVE the warning
    #   ran_fallback  did it ACTUALLY RUN comp-grep/comp-glob, per PRD C-3 ("no subjunctive")
    _LAST_RC.append(out.returncode)
    _LAST_WARNED.append(bool(_ABSTAIN_RX.search(text)))
    _LAST_RAN_FALLBACK.append(bool(_EXEC_EVIDENCE_RX.search(text)))
    return (bool(tools), tools)


def histogram(scores):
    """THE FULL SCORE DISTRIBUTION. PRD Q2: TO-2 must SET the abstain floor FROM this,
    not PICK a number. Hand TO-2 a zero-rate alone and it will guess a floor -- which is
    the exact failure Q2 exists to prevent."""
    h = collections.Counter(scores)
    return {str(k): h[k] for k in sorted(h)}


# ---------------------------------------------------------------------------
# cohort construction
# ---------------------------------------------------------------------------
def load_catalog():
    import yaml
    d = yaml.safe_load(open(MANIFEST, encoding="utf-8"))
    return [e for e in (d.get("entries") or []) if e.get("use_case")]


def gen_gibberish(n=GIBBERISH_N, seed=GIBBERISH_SEED):
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        out.append(" ".join(
            "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz")
                    for _ in range(rnd.randint(4, 9)))
            for _ in range(rnd.randint(3, 6))))
    return out


def is_probe_string(q):
    low = q.lower()
    return any(t in low for t in PROBE_TOKENS)


# THE ROW-TAG FILTER. Read the comment before you touch the regex.
#
# The FIRST version of this filter was `'ROUTE-' in line` -- WITH A HYPHEN. It could
# not see the 1,487 BARE `ROUTE` rows emitted by the LEGACY/curated-strong cascade
# (_log_rail("ROUTE", ...) at :1280/:1331/:1349). All of them carry a q=.
#
# AND IT WAS NOT MERELY PARTIAL -- IT WAS BIASED, IN THE FLATTERING DIRECTION.
# The legacy cascade only fires when a CURATED RULE MATCHES STRONGLY. So
# "was this row logged as ROUTE- ?" is CORRELATED WITH THE CATALOG FAILING, and the
# filter silently selected FOR the very failure it was measuring:
#     rows the hyphen filter KEPT   (n=350)  zero-rate 44.6%   <- catalog struggling
#     rows the hyphen filter MISSED (n=196)  zero-rate 14.8%   <- catalog doing WELL
#     the CORRECTED cohort          (n=544)  zero-rate 34.0%
# 36% of the headline cohort was invisible, and it was the 36% that moderated the claim.
#
#     A FILTER YOU DID NOT ENUMERATE THE COMPLEMENT OF IS A FILTER YOU HAVE NOT TESTED.
#
# That is why tally_row_tags() below prints EVERY tag in the log, consumed or not,
# BEFORE anything is filtered. Do not remove it. It is the control that catches this.
_ROUTE_FAMILY = re.compile(r"^\S+\s+ROUTE[\s-]")
_TAG_RX = re.compile(r"^\S+\s+(\S+)")


def tally_row_tags(path):
    """EVERY distinct row-tag in the log, with counts -- BEFORE any filtering, and
    including the ones we do NOT consume. If a tag exists that our filter ignores, we
    SAY SO and say why. A tally that only counts what you expected is not a tally."""
    tags = collections.Counter()
    q_by_tag = collections.Counter()
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            m = _TAG_RX.match(line)
            if not m:
                tags["<unparseable>"] += 1
                continue
            tag = m.group(1)
            tags[tag] += 1
            if re.search(r'q="', line):
                q_by_tag[tag] += 1
    return tags, q_by_tag


def freeze(snapshot_path):
    qs = collections.Counter()
    route_rows = q_rows = 0
    total_lines = 0
    tags, q_by_tag = tally_row_tags(snapshot_path)
    with open(snapshot_path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            total_lines += 1
            if not _ROUTE_FAMILY.match(line):
                continue
            route_rows += 1
            m = re.search(r'q="([^"]*)"', line)
            if m:
                q_rows += 1
                qs[m.group(1)] += 1

    catalog = load_catalog()
    catalog_pref = {e["use_case"].strip()[:60] for e in catalog}

    singletons = [q for q, c in qs.items() if c == 1]
    r_raw = [q for q in singletons if q.strip()[:60] not in catalog_pref]
    stripped = [q for q in r_raw if is_probe_string(q)]
    r_strict = [q for q in r_raw if not is_probe_string(q)]
    replayed = sum(c for c in qs.values() if c >= 50)

    # MATCH RATES. A ZERO-MATCH FILTER MUST ANNOUNCE ITSELF.
    # The catalog-text strip compares HISTORICAL rail-log questions against TODAY'S
    # manifest -- and the manifest MOVES. You cannot strip yesterday's catalog with
    # today's catalog. Prefix vs exact is printed side by side precisely because an
    # EXACT-equality strip against this lossy record matches almost nothing while
    # LOOKING like a clean, confident filter.
    exact_cat = {e["use_case"].strip() for e in catalog}
    all_q = list(qs)
    rates = [
        filter_match_rate("catalog-strip (60-char PREFIX -- the one we use)",
                          catalog_pref, [q.strip()[:60] for q in all_q],
                          "removes verbatim catalog text replayed into the log"),
        filter_match_rate("catalog-strip (EXACT equality -- shown as the CONTROL)",
                          exact_cat, [q.strip() for q in all_q],
                          "if this is far below the prefix rate, the record is LOSSY and "
                          "an exact-match strip would have silently matched almost nothing"),
        filter_match_rate("probe-token strip (R_raw -> R_strict)",
                          set(stripped), r_raw,
                          "agents' own gibberish probes; they legitimately score zero"),
    ]

    cohort = {
        "_README": "FROZEN COHORT. TO-2/TO-3 RE-RUN AGAINST THIS LIST -- they do NOT "
                   "re-derive it. A cohort re-derived from an append-live log is not a "
                   "population, it is a timestamp, and the regression it reports is "
                   "uninterpretable.",
        "frozen_at": _utc(),
        "snapshot_lines": total_lines,
        "row_tag_tally": {
            "_why": "EVERY tag in the log, consumed or not, BEFORE filtering. The first "
                    "cohort filter matched 'ROUTE-' and silently missed 1,487 bare-ROUTE "
                    "rows from the legacy cascade -- rows that fire only on a STRONG "
                    "curated match, i.e. exactly where the catalog SUCCEEDS. The filter "
                    "was BIASED toward the failure it was measuring. A FILTER YOU DID NOT "
                    "ENUMERATE THE COMPLEMENT OF IS A FILTER YOU HAVE NOT TESTED.",
            "all_tags": dict(tags.most_common()),
            "tags_carrying_q": dict(q_by_tag.most_common()),
            "consumed_by_cohort_R": sorted(t for t in tags if re.match(r"^ROUTE([\s-]|$)", t)),
            "NOT_consumed": sorted(t for t in tags if not re.match(r"^ROUTE([\s-]|$)", t)),
            "why_not_consumed": "RUN-GREP/RUN-GLOB/RUN-OVERRIDE/RUN-LS are the on-rails "
                                "PRIMITIVE-EXECUTION rows, not routing decisions. NOTE: "
                                "RUN-GREP has TWO producers -- comp-grep logging itself "
                                "when an agent calls it DIRECTLY (Rule 21 working as "
                                "designed), and comp-which's own fallback. They are NOT "
                                "interchangeable and must never be summed as 'abstains'.",
        },
        "denominator": {
            "route_events": route_rows,
            "route_events_with_q": q_rows,
            "route_events_without_q": route_rows - q_rows,
            "distinct_questions": len(qs),
            "organic_singletons": len(singletons),
            "cohort_R_raw": len(r_raw),
            "cohort_R_strict": len(r_strict),
            "machine_replayed_rows_count_ge_50": replayed,
            "machine_replayed_share_pct": round(100.0 * replayed / q_rows, 1) if q_rows else 0.0,
        },
        "cohort_R_raw": sorted(r_raw),
        "cohort_R_strict": sorted(r_strict),
        "cohort_R_stripped": sorted(stripped),
        "strip_rule": {
            "method": "case-insensitive substring match",
            "tokens": list(PROBE_TOKENS),
            "why_printed": "A judgment you cannot audit must be TRUSTED; a judgment "
                           "whose every input is PRINTED can be CHECKED -- and UNDONE -- "
                           "by a reader who has never met the author and disagrees.",
            "bias_direction": "WHEN IN DOUBT WE DO NOT STRIP. An un-stripped probe "
                              "inflates R_raw (a bound already declared unsafe to "
                              "defend). A wrongly-stripped one deletes a real coverage "
                              "gap AND FLATTERS US.",
        },
        "filter_match_rates": rates,
        "residual_bias": (
            "COHORT R IS SINGLETONS ONLY, so it EXCLUDES legitimately-repeated REAL "
            "questions -- and a question two agents both asked is MORE likely to be a "
            "common one the catalog COVERS. THE HEADLINE MAY THEREFORE STILL BIAS UPWARD. "
            "This is a NAMED, BOUNDED limit of the number, not a defect to be fixed: "
            "re-admitting repeats would re-admit the ~87.6% machine-replayed corpus, "
            "which is a far larger error in the same direction. State the limit; do not "
            "trade a small known bias for a large one."),
        "cohort_C": [{"q": e["use_case"], "label": str(e["tool"]).split()[0]} for e in catalog],
        "cohort_G": gen_gibberish(),
        "cohort_G_seed": GIBBERISH_SEED,
    }
    with open(FROZEN, "w", encoding="utf-8") as fh:
        json.dump(cohort, fh, indent=1, ensure_ascii=True)
    return cohort


# ---------------------------------------------------------------------------
# the harness testing ITSELF
# ---------------------------------------------------------------------------
def run_controls(mod, gibberish):
    """EVERY ONE OF THESE EXISTS BECAUSE AN INSTRUMENT ON THIS PROJECT ALREADY LIED.
    Care is not a control. Care is what you have instead of one."""
    c = {}

    pos = rules_score(mod, POSITIVE_CONTROL)
    c["positive_isolated"] = {"q": POSITIVE_CONTROL, "score": pos, "pass": pos > 0}

    gib = [rules_score(mod, q) for q in gibberish]
    nonzero = sum(1 for s in gib if s != 0)
    c["gibberish_rules_all_zero"] = {"n": len(gib), "nonzero": nonzero,
                                     "max": max(gib or [0]), "pass": nonzero == 0}

    # THE r[1] ANTI-CONTROL. Reproduce the KNOWN bug on purpose and require that it
    # PRODUCES THE LIE. If passing r[1] does NOT inflate gibberish, this harness is not
    # attached to the real scorer and the control above proves nothing.
    # A CONTROL THAT CANNOT DETECT THE BUG IT WAS WRITTEN FOR IS A DECORATION.
    qtok = mod._tokens(gibberish[0])
    poisoned = max(mod._score_rule(gibberish[0].lower(), qtok, r[1]) for r in mod.RULES)
    clean = rules_score(mod, gibberish[0])
    c["r1_anticontrol"] = {"poisoned_r1": poisoned, "clean_r0": clean,
                           "pass": poisoned > 0 and clean == 0}
    return c


def mutation_test(mod, gibberish):
    """FORCE the scorer to lie, BOTH directions, and require the harness to NOTICE.
    A PASSING ASSERTION THAT WAS NEVER MUTATED HAS NEVER BEEN TESTED. If this harness
    cannot fail, it is not a harness -- it is a decoration, and it is the fifth lying
    instrument in this project's history."""
    out = {}
    original = mod._score_rule

    # MUTANT A -- every score 0. The POSITIVE control must collapse and FAIL.
    mod._score_rule = lambda q, qtok, kw: 0
    pos = rules_score(mod, POSITIVE_CONTROL)
    out["mutant_all_zero"] = {"positive_control": pos, "pass": pos == 0}

    # MUTANT B -- every score 9. The GIBBERISH control must fire. This is the exact
    # SHAPE of the r[1] space-count bug (gibberish scoring high).
    mod._score_rule = lambda q, qtok, kw: 9
    gib = [rules_score(mod, q) for q in gibberish[:5]]
    out["mutant_all_nine"] = {"gibberish": gib, "pass": sum(1 for s in gib if s) > 0}

    mod._score_rule = original
    # A mutation test that leaves the mutant in place is sabotage. Prove restoration.
    out["restored"] = {"positive_control": rules_score(mod, POSITIVE_CONTROL),
                       "pass": rules_score(mod, POSITIVE_CONTROL) > 0}
    return out


# ---------------------------------------------------------------------------
def pct(n, d):
    return (100.0 * n / d) if d else 0.0


def _row(label, per_probe):
    rules = [p["score"] for p in per_probe]
    zero = sum(1 for s in rules if s == 0)
    routed = sum(1 for p in per_probe if p["routed"])
    n = len(per_probe)
    return {"cohort": label, "n": n, "zero_score_count": zero,
            "zero_score_rate_pct": round(pct(zero, n), 1),
            "rules_score_distribution": histogram(rules),
            "live_routed": routed, "live_no_route": n - routed,
            "live_route_rate_pct": round(pct(routed, n), 1)}


def measure(mod, mirror, probes, label, detail=False):
    per_probe = []
    for q in probes:
        ok, _t = live_route(mirror, q)
        per_probe.append({"q": q, "score": rules_score(mod, q), "routed": ok})
    row = _row(label, per_probe)
    return (row, per_probe) if detail else row


def derive_subset(per_probe, keep, label):
    """The bracket's two bounds MUST come from ONE measurement of ONE population."""
    return _row(label, [p for p in per_probe if p["q"] in keep])


def recall_at_k(mirror, cohort_c, k=TOPK):
    """MULTI-LABEL: 'is a USABLE tool visible in the top-k' -- NEVER 'did argmax equal my
    one label'. A bare precision@1 measures the LABEL-WRITER, not the router.
    Reported on cohort C ONLY, because C is labeled BY CONSTRUCTION. Cohort R has no
    labels AND THAT IS THE POINT, not a gap."""
    hit = 0
    for item in cohort_c:
        _ok, tools = live_route(mirror, item["q"])
        if item["label"] in tools[:k]:
            hit += 1
    return {"k": k, "n": len(cohort_c), "hit": hit,
            "recall_at_k_pct": round(pct(hit, len(cohort_c)), 1)}


def _readlines(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.readlines()


def pollution_check(before_lines, probes, mirror_root, invocations):
    """DID *WE* WRITE TO THE LIVE RAIL LOG?

    THIS CHECK HAS BEEN WRONG TWICE. Both failures are instructive and both are recorded
    here, because the third version is only trustworthy if you can see why the first two
    were not.

    v1 -- A COUNT DELTA. Confounded by concurrency: the fabric routes through comp-which
      while we run, so other lanes' rows land in the log and a before/after delta ACCUSES
      US OF THEIR WRITES. It reported '+2 POLLUTED' and refused to publish a baseline over
      2 rows that were not ours. IT FIRED CORRECTLY FOR THE WRONG REASON -- its own kind of lie.

    v2 -- ATTRIBUTION BY PROBE STRING ("does a new row carry a question we probed?").
      Better, and still WRONG -- IN THE ACCUSING DIRECTION. Our probe set is DRAWN FROM
      THE LOG, so those strings are exactly the questions agents actually ask. Another
      lane asking one of them CONCURRENTLY looks byte-identical to us writing it. A
      false-positive here does not merely annoy: it makes the harness refuse to publish a
      SOUND baseline. (Observed: 1/4 new rows flagged as 'ours' on a run where the mirror
      had provably captured every single one of our routes.)

    v3 -- POSITIVE, STRUCTURAL PROOF, and it is immune to concurrency because it does not
      look at the shared file at all:
          EVERY route we issued went to the MIRROR's rail log.
          If the mirror captured N routes and we issued N routes, NONE ESCAPED.
      Do not infer our innocence from the absence of our fingerprints on a shared object
      that other people are also touching. PROVE where our writes went instead.

          AN ALIBI BEATS A DENIAL. Account for your own writes; do not merely fail to
          find them somewhere else.

    v4 (NFRA_COMPCLOSE 2026-07-14, CTO~Z) -- v3'S OWN ASSUMPTION EXPIRED UNDER IT. v3 expected
      mirror_rows == routes_issued because `--route-only` still wrote a rail row per route. Then
      the route-only rail-silence fix landed in the binary (comp-which:793 -- the very finding #3
      this harness's author flagged) and every --route-only probe now writes ZERO rail rows --
      so v3 read 0 >= 713 and convicted the harness of polluting a log it never touched. AN ALIBI
      KEYED TO A WRITE THE SUBJECT NO LONGER MAKES CONVICTS THE INNOCENT THE MOMENT THE SUBJECT
      IMPROVES. v4 binds to what the binary writes NOW, in two limbs, both required:
        (a) SILENCE LIMB: the --route-only sweep leaves the mirror rail log EMPTY (route-only is
            rail-silent by design; any row here means the silence regressed and our probes DID
            write somewhere -- fail).
        (b) POSITIVE-CONTROL LIMB: ONE deliberate NON-route-only invocation inside the mirror
            MUST land >= 1 row in the MIRROR's rail log. Without this, limb (a)'s empty file is
            indistinguishable from a broken mirror -- an absence-of-evidence control, the exact
            class this file exists to kill. The control proves the capture path works; the sweep
            proves it stayed silent. Together: every write the binary CAN make lands in the
            mirror, and the sweep made none.

    The live-log delta is still REPORTED -- as UNATTRIBUTABLE concurrent traffic, which is
    what it is -- but it can no longer fail the run, because it cannot distinguish us from
    the fabric and a control that cannot discriminate must not be allowed to convict.
    """
    mirror_rail = os.path.join(mirror_root, "org", "mcp", "comp-which-rail.log")
    sweep_rows = len(_readlines(mirror_rail))

    # (b) the positive control: one NON-route-only invocation, inside the mirror, that must
    # write a mirror rail row (a curated-strong route -- routes + logs, never runs a primitive).
    exe = os.path.join(mirror_root, ".tools", "comp-which")
    try:
        subprocess.run([sys.executable, exe, POSITIVE_CONTROL],
                       capture_output=True, text=True, timeout=60, cwd=mirror_root)
    except Exception:
        pass
    control_rows = len(_readlines(mirror_rail)) - sweep_rows

    after = _readlines(RAIL_LOG)
    new = after[len(before_lines):]
    probe_set = set(probes)
    coincident = []
    for ln in new:
        m = re.search(r'q="([^"]*)"', ln)
        if m and m.group(1) in probe_set:
            coincident.append(m.group(1))

    return {
        "method": "AN ALIBI BEATS A DENIAL (v4). --route-only is rail-silent by design "
                  "(comp-which:793), so the sweep must leave the mirror rail EMPTY -- and an "
                  "empty file only counts as silence because the POSITIVE CONTROL (one "
                  "non-route-only invocation in the mirror) proves the capture path works. "
                  "Every write the binary can make lands in the mirror; the sweep made none. "
                  "Immune to concurrency: never looks at the shared file to decide.",
        "routes_issued": invocations,
        "mirror_rows_from_route_only_sweep": sweep_rows,
        "route_only_stayed_silent": sweep_rows == 0,
        "mirror_rows_from_positive_control": control_rows,
        "mirror_capture_path_proven": control_rows >= 1,
        "pass": (sweep_rows == 0 and control_rows >= 1),
        "live_log_new_rows": len(new),
        "live_log_rows_matching_a_probe_string": len(coincident),
        "unattributable_note":
            "These rows are UNATTRIBUTABLE, not ours-by-proof: our probe set is drawn "
            "FROM this log, so a concurrent agent asking one of these questions is "
            "byte-identical to us writing it. Reported, never used to convict.",
    }


def filter_match_rate(name, needles, haystack, note=""):
    """PRINT THE MATCH RATE OF EVERY FILTER YOU WRITE. A ZERO-MATCH FILTER MUST ANNOUNCE
    ITSELF.

    Equality against a LOSSY RECORD is not a test. The catalog-text strip below compares
    rail-log questions (historical, truncated to 120 chars by _log_rail) against TODAY'S
    manifest text -- and the manifest MOVES. YOU CANNOT STRIP YESTERDAY'S CATALOG WITH
    TODAY'S CATALOG. A strip that silently matches nothing looks identical to a strip
    with nothing to match, and both print a confident, clean number."""
    hit = sum(1 for h in haystack if h in needles)
    return {"filter": name, "matched": hit, "of": len(haystack),
            "rate_pct": round(pct(hit, len(haystack)), 1), "note": note}


def main():
    ap = argparse.ArgumentParser(description="comp-which routing-quality harness (TO-1)")
    ap.add_argument("--freeze", metavar="SNAPSHOT",
                    help="materialize the cohort from a rail-log SNAPSHOT, then exit")
    ap.add_argument("--binary-ref", default="HEAD",
                    help="git ref to measure (default HEAD). 'WORKING' = the dirty tree.")
    ap.add_argument("--mutate", choices=("zero", "nine"),
                    help="run ONLY the mutation test (prove the harness CAN fail)")
    ap.add_argument("--out", metavar="PATH", default=None,
                    help="write the report JSON here instead of the committed TO-1 baseline "
                         "artifact. A LATER VINTAGE MUST NOT CLOBBER A COMMITTED BASELINE: the "
                         "default path IS the blob-pinned PRE record, and the first post-fix "
                         "run of this harness overwrote it in the working tree (caught at "
                         "git-status, restored from HEAD -- NFRA_COMPCLOSE 2026-07-14). "
                         "Regression runs pass --out; only a deliberate re-baseline omits it.")
    args = ap.parse_args()

    if args.freeze:
        c = freeze(args.freeze)
        d = c["denominator"]
        print("FROZEN -> %s" % os.path.relpath(FROZEN, WS))
        print("  ROUTE events           %6d" % d["route_events"])
        print("  ... carrying a q=      %6d   (%d rows carry NO question)"
              % (d["route_events_with_q"], d["route_events_without_q"]))
        print("  DISTINCT questions     %6d" % d["distinct_questions"])
        print("  ORGANIC singletons     %6d" % d["organic_singletons"])
        print("  cohort R_raw           %6d   (verbatim catalog text removed)" % d["cohort_R_raw"])
        print("  cohort R_strict        %6d   (probe strings stripped too)" % d["cohort_R_strict"])
        print("  cohort C               %6d" % len(c["cohort_C"]))
        print("  cohort G               %6d   (seed %d)" % (len(c["cohort_G"]), c["cohort_G_seed"]))
        print("  machine-replayed share %5.1f%%  <- a fixed corpus, replayed at machine pacing"
              % d["machine_replayed_share_pct"])
        return 0

    if not os.path.exists(FROZEN):
        sys.stderr.write("FATAL: no frozen cohort at %s\n" % os.path.relpath(FROZEN, WS))
        sys.stderr.write("       run:  --freeze <rail-log-snapshot>  first.\n")
        sys.stderr.write("       A cohort re-derived from the append-live log is NOT a baseline.\n")
        return 2
    cohort = json.load(open(FROZEN, encoding="utf-8"))
    gibberish = cohort["cohort_G"]

    rail_before = _readlines(RAIL_LOG)
    train_before = len(_readlines(TRAINING_QUEUE))
    all_probes = (cohort["cohort_R_raw"] + cohort["cohort_R_strict"]
                  + [x["q"] for x in cohort["cohort_C"]] + gibberish + [POSITIVE_CONTROL])

    ref = None if args.binary_ref.upper() == "WORKING" else args.binary_ref
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix="_comp-which")
    tmp.close()
    vintage, blob = extract_binary(ref, tmp.name)
    mod = load_module(tmp.name)
    mirror = build_mirror(tmp.name)

    if args.mutate:
        mt = mutation_test(mod, gibberish)
        key = "mutant_all_zero" if args.mutate == "zero" else "mutant_all_nine"
        r = mt[key]
        print("MUTATION TEST -- %s" % key)
        print("  harness DETECTED the mutant: %s" % ("YES" if r["pass"] else "NO"))
        print("  %s" % ("A harness that survives its own mutant is a decoration."
                        if not r["pass"] else "The assertion is real: it fails when the scorer lies."))
        shutil.rmtree(mirror, ignore_errors=True)
        os.unlink(tmp.name)
        return 0 if r["pass"] else 2

    print("=" * 78)
    print("comp-which ROUTING-QUALITY HARNESS   --   NFRA_COMPASSURANCE TO-1")
    print("=" * 78)
    print("SUBJECT : .tools/comp-which @ %s" % vintage)
    print("          blob %s   captured %s" % (blob, _utc()))
    print("          (a vintage is not 'the working tree' -- the working tree is a VERB)")
    wt = working_tree_blob()
    if blob and wt and wt != blob:
        print("  NOTE  : the WORKING TREE is blob %s -- IT DIFFERS FROM THE SUBJECT." % wt)
        print("          Another lane is editing the binary. This run measures the PINNED")
        print("          vintage, deliberately. That is what makes it a baseline.")

    ctrl = run_controls(mod, gibberish)
    mut = mutation_test(mod, gibberish)
    print("")
    print("-" * 78)
    print("INSTRUMENT CONTROLS   (if these fail, DISCARD every number below)")
    print("-" * 78)
    p, g, a = ctrl["positive_isolated"], ctrl["gibberish_rules_all_zero"], ctrl["r1_anticontrol"]
    print("  POSITIVE (isolated)   score=%-3d              %s" % (p["score"], "PASS" if p["pass"] else "FAIL"))
    print("  GIBBERISH @ RULES     n=%-3d nonzero=%-3d max=%-2d %s"
          % (g["n"], g["nonzero"], g["max"], "PASS" if g["pass"] else "FAIL"))
    print("  r[1] ANTI-CONTROL     poisoned=%-3d clean=%-3d   %s"
          % (a["poisoned_r1"], a["clean_r0"], "PASS" if a["pass"] else "FAIL"))
    print("     ^ reproduces the space-count bug ON PURPOSE. Gibberish scores %d via r[1]"
          % a["poisoned_r1"])
    print("       and %d via r[0]. If this stopped reproducing, the harness would no longer"
          % a["clean_r0"])
    print("       be attached to the real scorer -- and the control above would prove nothing.")
    print("  MUTATION all-zero     detected: %s" % ("YES" if mut["mutant_all_zero"]["pass"] else "NO <-- BLIND"))
    print("  MUTATION all-nine     detected: %s" % ("YES" if mut["mutant_all_nine"]["pass"] else "NO <-- BLIND"))
    print("  scorer restored       %s" % ("PASS" if mut["restored"]["pass"] else "FAIL"))
    instrument_ok = all([p["pass"], g["pass"], a["pass"], mut["mutant_all_zero"]["pass"],
                         mut["mutant_all_nine"]["pass"], mut["restored"]["pass"]])

    tt = cohort.get("row_tag_tally", {})
    if tt:
        print("")
        print("-" * 78)
        print("EVERY ROW-TAG IN THE LOG, BEFORE ANY FILTERING")
        print("-" * 78)
        for tag, n in (tt.get("all_tags") or {}).items():
            mark = "  <- cohort R" if tag in (tt.get("consumed_by_cohort_R") or []) else ""
            print("  %-26s %6d%s" % (tag, n, mark))
        print("")
        print("  NOT consumed by cohort R: %s" % ", ".join(tt.get("NOT_consumed") or []))
        print("  WHY: RUN-* are PRIMITIVE-EXECUTION rows, not routing decisions.")
        print("  AND NOTE: RUN-GREP has TWO producers -- comp-grep logging ITSELF when an")
        print("  agent calls it directly (Rule 21 working as designed) and comp-which's own")
        print("  fallback. THEY MUST NEVER BE SUMMED AS 'comp-which ABSTAINS'.")
        print("")
        print("  A FILTER YOU DID NOT ENUMERATE THE COMPLEMENT OF IS A FILTER YOU HAVE NOT")
        print("  TESTED. The first cohort filter here matched 'ROUTE-' and silently missed")
        print("  1,487 bare-ROUTE rows -- and those rows fire only on a STRONG curated match,")
        print("  i.e. exactly where the catalog SUCCEEDS. IT SELECTED FOR THE FAILURE IT WAS")
        print("  MEASURING. This tally exists so that can never happen silently again.")

    d = cohort["denominator"]
    print("")
    print("-" * 78)
    print('THE DENOMINATOR, DECOMPOSED  ("6,308 routing decisions" is NOT 6,308 questions)')
    print("-" * 78)
    print("  ROUTE events                %6d" % d["route_events"])
    print("  ... carrying a q= field     %6d    (%d rows carry NO question at all)"
          % (d["route_events_with_q"], d["route_events_without_q"]))
    print("  DISTINCT questions          %6d    <- ~13x duplicated" % d["distinct_questions"])
    print("  ORGANIC singletons          %6d" % d["organic_singletons"])
    print("  COHORT R_raw                %6d    <- verbatim catalog text removed" % d["cohort_R_raw"])
    print("  COHORT R_strict             %6d    <- probe strings stripped too" % d["cohort_R_strict"])
    print("")
    print("  MACHINE-REPLAYED SHARE      %5.1f%%    <- a FIXED CORPUS replayed at machine"
          % d["machine_replayed_share_pct"])
    print("                                        pacing. The harness this file REPLACES")
    print("                                        is a confirmed author of it.")

    # R_strict is a SUBSET of R_raw, so it is derived from the SAME probe results rather
    # than re-probed. Re-probing it would double the live-binary calls AND -- because the
    # two runs would hit the binary at different moments -- could silently disagree.
    # THE BRACKET MUST COME FROM ONE MEASUREMENT, OR IT IS NOT A BRACKET, IT IS TWO GUESSES.
    strict_set = set(cohort["cohort_R_strict"])
    r_raw, per_probe = measure(mod, mirror, cohort["cohort_R_raw"], "R_raw", detail=True)
    r_str = derive_subset(per_probe, strict_set, "R_strict")
    c_row = measure(mod, mirror, [x["q"] for x in cohort["cohort_C"]], "C")
    del _LAST_RC[:], _LAST_WARNED[:], _LAST_RAN_FALLBACK[:]
    g_row, g_probes = measure(mod, mirror, gibberish, "G", detail=True)
    g_rc = sum(1 for rc in _LAST_RC if rc != 0)
    g_warned = sum(1 for w in _LAST_WARNED if w)
    g_ran = sum(1 for r in _LAST_RAN_FALLBACK if r)
    g_row["live_rc_nonzero"] = g_rc
    g_row["agent_facing_abstain_banner"] = g_warned
    g_row["actually_ran_fallback"] = g_ran
    # AN UNGUARDED MISROUTE = a TOOL WAS PRESENTED **and** there was NO abstain signal on
    # EITHER channel. All three conjuncts are load-bearing:
    #   - TOOL PRESENTED. A no-route is NOT a misroute -- it is the fallback path working.
    #     An earlier version omitted this and convicted 40/40 on the PRE binary, when only
    #     2 of those probes were ever shown a tool and the other 38 correctly dead-ended.
    #     IT ACCUSED THE TOOL OF 38 FAILURES IT DID NOT COMMIT. A control that convicts the
    #     innocent is not strict, it is BROKEN -- and it would have made the PRE/POST delta
    #     unreadable by saturating the metric at 100% before the fix could move it.
    #   - NO rc SIGNAL and NO WARNING. A menu under an explicit "these are FUZZY GUESSES --
    #     do not pick one" banner is a HEDGE, not a route. Convicting on it would be grading
    #     the tool against a definition it never agreed to.
    unguarded = sum(1 for i, p in enumerate(g_probes)
                    if p["routed"] and _LAST_RC[i] == 0 and not _LAST_WARNED[i])
    g_row["unguarded_misroutes"] = unguarded
    g_row["four_signals"] = {
        "programmatic_abstain_rc_nonzero": g_rc,
        "agent_facing_abstain_banner": g_warned,
        "ranked_menu_still_printed": g_row["live_routed"],
        "actually_ran_the_fallback": g_ran,
        "unguarded_misroutes": unguarded,
        "note": "MEASURED, NOT ADJUDICATED. The gate fails ONLY on an UNGUARDED misroute "
                "(a menu with NO abstain signal on either channel). The PRD-3.1 contract "
                "gap (a scored menu printed ABOVE the warning, where 3.1 says 'MATCHES: "
                "none') and the C-3 gap (the fallback is PRINTED, never RUN) are REPORTED "
                "as contract divergences for TO-2's owner to rule on. They are not mine "
                "to convict on.",
    }

    # THE TWO NAMED METRICS. Compute the NL-only rate HERE, before it is named -- an
    # earlier version printed R_strict (33.1%) under the label "NATURAL-LANGUAGE
    # QUESTIONS", and that was FALSE: R_strict still contains the HUD-injected glob
    # patterns. I LABELLED A NUMBER AS SOMETHING IT WAS NOT. Naming a metric is a claim
    # about what it measures, and a mislabelled metric lies more efficiently than a wrong
    # one -- a wrong number invites checking; a mislabelled one invites trust.
    pats = [p for p in per_probe if p["q"] in strict_set and _IS_PATTERN(p["q"])]
    nls = [p for p in per_probe if p["q"] in strict_set and not _IS_PATTERN(p["q"])]
    rn = pct(sum(1 for p in nls if p["score"] == 0), len(nls))   # NATURAL-LANGUAGE only
    hi = r_raw["zero_score_rate_pct"]                            # EVERYTHING it is asked
    lo = rn

    print("")
    print("=" * 78)
    print(">>>  COHORT R  --  THE HEADLINE.  LABEL-FREE.  A BRACKET, NEVER A POINT.  <<<")
    print("=" * 78)
    print('  "What fraction of REAL agent questions does the catalog have NO vocabulary')
    print('   for?"  -- no ground truth, no hand-labeling, nothing to argue about.')
    print("   A DENOMINATOR NOBODY ON THIS PROJECT AUTHORED. AGENTS WROTE IT, NOT US.")
    print("")
    print("   ZERO-SCORE RATE (RULES layer -- the coverage metric):")
    print("     R_raw     n=%-4d zero=%-4d %5.1f%%   <- UPPER bound (nothing stripped)"
          % (r_raw["n"], r_raw["zero_score_count"], r_raw["zero_score_rate_pct"]))
    print("     R_strict  n=%-4d zero=%-4d %5.1f%%   <- LOWER bound (probe strings out)"
          % (r_str["n"], r_str["zero_score_count"], r_str["zero_score_rate_pct"]))
    print("")
    print("   ==> TWO NAMED METRICS. *** THIS IS NOT AN ERROR BAR. DO NOT AVERAGE IT. ***")
    print("       They answer DIFFERENT QUESTIONS. There is no true value 'in between'.")
    print("")
    print("         %5.1f%%   \"Of EVERYTHING comp-which is ASKED, what has no catalog"
          % hi)
    print("                  vocabulary?\"   (includes HUD-injected glob patterns)")
    print("         %5.1f%%   \"Of NATURAL-LANGUAGE QUESTIONS AGENTS ASKED, what has none?\""
          % lo)
    print("                  <- THE COVERAGE HOLE PROPER. The metric's actual claim.")
    print("")
    print("       A reader WILL average a bracket. That is why this is not presented as one.")
    c_zero = c_row["zero_score_rate_pct"]
    if c_zero:
        print("       vs COHORT C (catalog-derived) %.1f%%  ->  the catalog-probe design would"
              % c_zero)
        print("       UNDERSTATE this hole by %.2fx." % ((lo + hi) / 2.0 / c_zero))
    print("")
    print("   THE DIRECTION IS THE FINDING. THE DIGIT IS NOT.")
    print("   An earlier statement of this hedged the THIRD significant figure while the")
    print("   error was in the FIRST (a cohort filter that could not see the legacy-cascade")
    print("   rows -- and those rows were the ones the catalog handled WELL, so the filter")
    print("   was BIASED toward the failure it was measuring, not merely partial).")
    print("   QUOTE THE BRACKET. DO NOT QUOTE A DIGIT YOU DID NOT RE-DERIVE.")
    print("")
    print("   LIVE BINARY: routed %d/%d (%.1f%%), no-route %d"
          % (r_raw["live_routed"], r_raw["n"], r_raw["live_route_rate_pct"], r_raw["live_no_route"]))
    print("")
    print("   EVERY FILTER'S MATCH RATE  (a ZERO-MATCH filter must ANNOUNCE ITSELF):")
    for fr in cohort.get("filter_match_rates", []):
        print("     %-52s %4d/%-5d %5.1f%%"
              % (fr["filter"], fr["matched"], fr["of"], fr["rate_pct"]))
    print("     ^ equality against a LOSSY record is not a test. These questions were")
    print("       logged against a manifest that has since MOVED -- YOU CANNOT STRIP")
    print("       YESTERDAY'S CATALOG WITH TODAY'S CATALOG. If the EXACT rate is far")
    print("       below the PREFIX rate, an exact-match strip would have silently matched")
    print("       almost nothing while printing a clean, confident number.")
    print("")
    # AC14 -- THE HUD-INJECTED CONTAMINATION, QUANTIFIED. IT MOVES THE HEADLINE AGAINST US.
    if pats:
        zp = sum(1 for p in pats if p["score"] == 0)
        zn = sum(1 for p in nls if p["score"] == 0)
        rp = pct(zp, len(pats))
        print("")
        print("   [AC14] HUD-INJECTED SEARCH PATTERNS INSIDE THE HEADLINE COHORT")
        print("     The HUD hook (comp-tool-hud.sh:291) passes the agent's RAW SEARCH QUERY")
        print("     to comp-which --route-only, and --route-only still _log_rail()s. So the")
        print("     rail log contains GLOB/GREP PATTERNS ('**/*COMPASSURANCE*') that were")
        print("     NEVER natural-language questions. THEY SCORE ZERO BECAUSE THEY ARE NOT")
        print("     QUESTIONS -- NOT BECAUSE THE CATALOG LACKS VOCABULARY FOR THEM.")
        print("")
        print("       R_strict as published    n=%-4d zero=%-4d %5.1f%%"
              % (r_str["n"], r_str["zero_score_count"], r_str["zero_score_rate_pct"]))
        print("       ... GLOB/GREP patterns   n=%-4d zero=%-4d %5.1f%%   <- cannot score"
              % (len(pats), zp, rp))
        print("       ... NATURAL-LANGUAGE     n=%-4d zero=%-4d %5.1f%%   <- what the metric MEANS"
              % (len(nls), zn, rn))
        print("")
        print("     ==> THE HEADLINE IS INFLATED BY ~%.1f POINTS (%.1f%% -> %.1f%%)."
              % (r_str["zero_score_rate_pct"] - rn, r_str["zero_score_rate_pct"], rn))
        print("         THIS MAKES THE DEFECT LOOK WORSE THAN IT IS. WE REPORT IT ANYWAY,")
        print("         AND WE REPORT IT LOUDLY, BECAUSE IT CUTS AGAINST OUR OWN FINDING.")
        print("         An error that flatters you is the one you must hunt hardest.")
        print("")
        print("     NOT SILENTLY RESTRIPPED. The pattern-detector below is MY OWN filter and")
        print("     it HAS false positives (it catches '--json could this column expose a")
        print("     client SSN', which IS a real question). A hand-authored strip measures")
        print("     the AUTHOR -- so this WIDENS the bracket; it does not replace it.")
        print("     The strip rule belongs to the TO owner, not to the instrument.")
        print("")
        print("     >>> HONEST RANGE FOR THE REAL COVERAGE HOLE:  [ %.0f%% .. %.0f%% ]  <<<"
              % (min(rn, r_str["zero_score_rate_pct"]), max(rn, r_raw["zero_score_rate_pct"])))
        if c_row["zero_score_rate_pct"]:
            print("         vs cohort C %.1f%% -- the catalog-probe design STILL understates the"
                  % c_row["zero_score_rate_pct"])
            print("         hole by %.2fx even at the most conservative end. THE FINDING SURVIVES"
                  % (rn / c_row["zero_score_rate_pct"]))
            print("         ITS OWN CORRECTION -- which is the only reason to trust it.")

    print("")
    print("   [!!] THE CORRECTION SEQUENCE IS MONOTONIC. THIS NUMBER IS NOT A FLOOR.")
    print("   Every correction to this finding has moved it the SAME WAY -- smaller:")
    print("       2.40x  ->  1.87x  ->  1.84x  ->  1.59x   (understatement vs cohort C)")
    print("   A RANDOM error process corrects in BOTH directions. A MONOTONIC sequence is")
    print("   the signature of a SYSTEMATIC BIAS THAT IS STILL ONLY PARTLY UNCOVERED.")
    print("")
    print("   >>> RESIDUAL RISK, STATED IN THE DIRECTION IT IS LIKELY TO BE WRONG: further")
    print("       contamination, if found, is LIKELIER TO SHRINK THIS THAN TO GROW IT. <<<")
    print("")
    print("   A FOURTH CONTAMINANT IS ALREADY CONFIRMED AND IS *NOT* FULLY REMOVED:")
    print("   agents' OWN gibberish and off-domain probes survive in cohort R. Found by")
    print("   READING 25 RANDOM ZERO-SCORING STRINGS (not by looking at any rate):")
    print("       \"phhpk cpeaj djfkc\"      <- generated gibberish, an agent's own probe")
    print("       \"banana bread recipe\"    <- an off-domain control probe")
    print("   The exact-token strip list CANNOT catch these: GENERATED gibberish is")
    print("   unpredictable BY CONSTRUCTION -- that is the entire point of generating it.")
    print("   2 in a sample of 25 (~8%), and n=25 IS NOT A POINT ESTIMATE and is not quoted")
    print("   as one. They score zero LEGITIMATELY. They are not coverage gaps.")
    print("")
    print("   EVERY CONTAMINANT IN THIS PROJECT WAS FOUND BY READING THE STRINGS AND NONE")
    print("   BY READING THE AGGREGATE. If a fifth exists, that is where it is.")
    print("")
    print("   RESIDUAL BIAS -- NAMED AND BOUNDED, NOT FIXED:")
    print("     Cohort R is SINGLETONS, so it excludes legitimately-REPEATED real")
    print("     questions -- and a question two agents both asked is MORE likely to be a")
    print("     common one the catalog COVERS. SO THIS HEADLINE MAY STILL BIAS UPWARD.")
    print("     We do NOT 'fix' it by re-admitting repeats: that re-admits the ~87.6%")
    print("     machine-replayed corpus -- a far larger error in the SAME direction.")
    print("     Do not trade a small known bias for a large one.")
    print("")
    print("   STRIPPED FROM R_strict -- THE FULL LIST, AS STRINGS, NOT A COUNT:")
    for s in cohort["cohort_R_stripped"] or []:
        print('     - "%s"' % s[:86])
    if not cohort["cohort_R_stripped"]:
        print("     (none)")

    print("")
    print("-" * 78)
    print("COHORT C  --  SELF-CONSISTENCY FLOOR.   *** NOT THE HEADLINE. ***")
    print("-" * 78)
    print("  The catalog describing ITSELF, scored against a catalog built from that SAME")
    print("  text. It measures STRING SELF-IDENTITY, not routing, and it is ANTI-CORRELATED")
    print("  with the defect -- BRIGHTEST WHERE THE GAP IS DEEPEST. DO NOT PROMOTE IT.")
    print("     C   n=%-4d zero=%-4d %5.1f%%"
          % (c_row["n"], c_row["zero_score_count"], c_row["zero_score_rate_pct"]))
    if c_row["zero_score_rate_pct"] > 10.0:
        print("     !! C IS NOT NEAR-CEILING -- THE CATALOG CANNOT RETRIEVE ITSELF. !!")
        print("        That is a finding in its own right; it routes to TO-4 (catalog truth).")

    print("")
    print("-" * 78)
    print("COHORT G  --  THE GATE.  GENERATED GIBBERISH.  ZERO-TOLERANCE.")
    print("-" * 78)
    n = g_row["n"]
    print("  FOUR SIGNALS, MEASURED SEPARATELY. THE GATE CONVICTS ON ONLY ONE OF THEM.")
    print("")
    print("     G @ RULES        zero on %d/%d  (%.1f%%)   <- the RULES layer PASSES"
          % (g_row["zero_score_count"], n, g_row["zero_score_rate_pct"]))
    print("     G @ rc           abstained  %d/%d          <- PROGRAMMATIC (a SCRIPT sees this)"
          % (g_row["live_rc_nonzero"], n))
    print("     G @ warning      banner on  %d/%d          <- AGENT-FACING (an AGENT sees this)"
          % (g_row["agent_facing_abstain_banner"], n))
    print("     G @ menu         tools shown %d/%d         <- printed ABOVE the warning"
          % (g_row["live_routed"], n))
    print("     G @ fallback     ACTUALLY RAN %d/%d        <- PRD C-3: 'no subjunctive'"
          % (g_row["actually_ran_fallback"], n))
    print("")
    print("     UNGUARDED MISROUTES (a menu with NO abstain on EITHER channel): %d/%d"
          % (g_row["unguarded_misroutes"], n))
    gate_failed = g_row["unguarded_misroutes"] > 0
    if gate_failed:
        print("")
        print("     *** GATE FAILED: %d/%d GIBBERISH PROBES GET A CONFIDENT TOOL WITH NO"
              % (g_row["unguarded_misroutes"], n))
        print("         WARNING AND NO NONZERO EXIT. An unguarded misroute is not noise --")
        print("         IT IS THE DEFECT REPRODUCING ITSELF IN FRONT OF YOU. ***")
    else:
        print("     ==> GATE PASSES. Every gibberish probe is guarded on at least one channel.")

    # The two CONTRACT DIVERGENCES. Reported, never convicted on -- they are TO-2's call.
    if g_row["live_routed"] and g_row["agent_facing_abstain_banner"]:
        print("")
        print("     [CONTRACT GAP -- PRD 3.1, REPORTED NOT CONVICTED]")
        print("     3.1 says NO FIT prints 'MATCHES: none' + 'VERDICT: NO FIT'. The binary")
        print("     prints 'MATCHES (top 3 of 41)' -- a ranked, scored, described menu --")
        print("     ABOVE the warning. A scored menu FIRST and 'do not pick one' SECOND is a")
        print("     MIXED SIGNAL. The exit code is not the contract; THE OUTPUT IS.")
        print("     (An earlier version of this harness called the abstain INVISIBLE. THAT")
        print("      WAS FALSE -- the banner is in stdout. The author had sliced stdout to 6")
        print("      lines and reasoned from the slice. A TRUNCATED SCAN IS NOT A NEGATIVE")
        print("      RESULT -- ESPECIALLY WHEN IT IS YOUR OWN OUTPUT AND IT AGREES WITH YOU.)")
    if g_row["live_rc_nonzero"] and not g_row["actually_ran_fallback"]:
        print("")
        print("     [CONTRACT GAP -- PRD C-3, REPORTED NOT CONVICTED]")
        print("     C-3 requires NO FIT to *ACTUALLY RUN* comp-grep/comp-glob -- 'no")
        print("     subjunctive'. Zero execution evidence in %d/%d abstains: it PRINTS the"
              % (g_row["live_rc_nonzero"] - g_row["actually_ran_fallback"],
                 g_row["live_rc_nonzero"]))
        print("     command, it does not RUN it.")
        print("         the original defect:  'it WOULD RUN comp-grep -- never a dead-end'")
        print("         the shipped fix:      'or search directly: comp-grep <term>'")
        print("     >>> THE SUBJUNCTIVE SURVIVED THE FIX. IT CHANGED GRAMMATICAL MOOD AND")
        print("         NOT EPISTEMIC STATUS. 'it would run' became 'you could run', and")
        print("         NEITHER OF THEM RUNS. <<<")
        print("     Whether printing beats auto-running a slow grep is a genuine DESIGN")
        print("     question -- but it is a DECISION, and right now it is an unremarked")
        print("     DIVERGENCE FROM THE CONTRACT. That call is TO-2's, not this harness's.")

    rk = recall_at_k(mirror, cohort["cohort_C"])
    print("")
    print("-" * 78)
    print("RECALL@%d   (MULTI-LABEL: 'is a USABLE tool visible in the top-%d')" % (TOPK, TOPK))
    print("-" * 78)
    print("  A bare precision@1 measures the LABEL-WRITER, not the router. k=3, NEVER 1.")
    print("     recall@%d = %d/%d = %.1f%%   (cohort C only -- labeled by construction;"
          % (rk["k"], rk["hit"], rk["n"], rk["recall_at_k_pct"]))
    print("                                     R is deliberately label-free)")

    print("")
    print("-" * 78)
    print("SCORE DISTRIBUTIONS  (PRD Q2: TO-2 must SET the floor FROM these, not PICK one)")
    print("-" * 78)
    for row in (r_raw, r_str, c_row, g_row):
        print("  %-9s %s" % (row["cohort"], json.dumps(row["rules_score_distribution"])))
    print("  ^ hand TO-2 a zero-rate alone and it will GUESS a floor. That guess is the")
    print("    exact failure PRD Q2 exists to prevent.")

    poll = pollution_check(rail_before, all_probes, mirror, _INVOCATIONS[0])
    td = len(_readlines(TRAINING_QUEUE)) - train_before
    print("")
    print("-" * 78)
    print("DID *WE* MUTATE THE MEASURED THING?   (a POSITIVE ALIBI, not a denial)")
    print("-" * 78)
    print("  routes we issued (--route-only)       %d" % poll["routes_issued"])
    print("  mirror rail rows from the sweep        %d   %s"
          % (poll["mirror_rows_from_route_only_sweep"],
             "SILENT (by design)" if poll["route_only_stayed_silent"] else "*** ROUTE-ONLY WROTE THE RAIL -- silence regressed ***"))
    print("  mirror rail rows from POSITIVE CONTROL %d   %s"
          % (poll["mirror_rows_from_positive_control"],
             "capture path PROVEN" if poll["mirror_capture_path_proven"] else "*** MIRROR CAPTURES NOTHING -- empty is not silence ***"))
    print("")
    print("  AN ALIBI BEATS A DENIAL (v4). --route-only is rail-silent by design, so the sweep")
    print("  must leave the mirror rail EMPTY -- and that empty file only counts as silence")
    print("  because ONE deliberate non-route-only invocation in the mirror DID land a row")
    print("  (the capture path works; the sweep chose silence). Every write the binary can")
    print("  make lands in the mirror; none landed in the live log. Immune to concurrency:")
    print("  the verdict never reads the shared file.")
    print("")
    print("  live-log rows added during our run    %d   (UNATTRIBUTABLE, reported only)"
          % poll["live_log_new_rows"])
    print("  ... that match one of our probes      %d" % poll["live_log_rows_matching_a_probe_string"])
    print("  training-queue rows added             %d" % td)
    print("  ^ our probe set is DRAWN FROM this log, so a concurrent agent asking one of")
    print("    these questions is BYTE-IDENTICAL to us writing it. This CANNOT convict us")
    print("    and it is not allowed to: a control that cannot discriminate must never be")
    print("    permitted to fail the run. (v2 of this check did exactly that.)")
    clean = poll["pass"]

    # PROVENANCE, CONDITIONAL ON THE ACTUAL CAPTURE STATE. A note baked to describe ONE
    # historical capture becomes FALSE on the next re-baseline: working_tree_differs would
    # read CLEAN while the frozen prose still says "captured mid-edit". The lesson that
    # earned this field -- the 2026-07-18 baseline was captured minutes before a lane began
    # editing the binary, "sound by luck" until verified -- is kept in BOTH branches as
    # HISTORY, never asserted as THIS run's condition. A PROVENANCE RECORD THAT CAPTURES
    # *WHAT* BUT NOT *WHEN* (OR MIS-STATES THE WHEN) IS NOT PROVENANCE.
    if bool(wt and blob and wt != blob):
        prov = (
            "WORKING TREE DIFFERS from the measured vintage: this run measured the PINNED "
            "blob %s, NOT the dirty tree %s -- another lane is mid-edit and the working "
            "tree is a VERB. (History: the ORIGINAL TO-1 baseline, 2026-07-18, was captured "
            "minutes before a lane began editing; 'sound by luck', then by verification -- "
            "which is why this field exists.) A PROVENANCE RECORD THAT CAPTURES *WHAT* BUT "
            "NOT *WHEN* IS NOT PROVENANCE -- the blob AND the capture time are stamped above."
            % (blob, wt))
    else:
        prov = (
            "WORKING TREE IS CLEAN and equal to the measured vintage %s: no lane was "
            "mid-edit, so this measurement is sound BY CONSTRUCTION, not by luck. (History: "
            "the ORIGINAL TO-1 baseline, 2026-07-18, was NOT so lucky -- captured minutes "
            "before a lane began editing the binary, which is why this field exists.) A "
            "PROVENANCE RECORD THAT CAPTURES *WHAT* BUT NOT *WHEN* IS NOT PROVENANCE -- the "
            "blob AND the capture time are stamped above." % blob)

    baseline = {
        "to": "NFRA_COMPASSURANCE.TO-1",
        "author": "0.8.0_AE_CloudComp~Z",
        "measured_at": _utc(),
        "subject": {"vintage": vintage, "blob": blob, "working_tree_blob": wt,
                    "working_tree_differs": bool(wt and blob and wt != blob)},
        "provenance_note": prov,
        "denominator": d,
        "cohorts": {"R_raw": r_raw, "R_strict": r_str, "C": c_row, "G": g_row},
        "headline": {
            "metric": "zero-score rate on REAL agent questions (LABEL-FREE)",
            "TWO_NAMED_METRICS_NOT_AN_ERROR_BAR": {
                "everything_it_is_asked_pct": hi,
                "everything_it_is_asked_means":
                    "Of EVERYTHING comp-which is ASKED, what has no catalog vocabulary? "
                    "Includes HUD-injected glob patterns (comp-tool-hud.sh:291).",
                "natural_language_questions_pct": lo,
                "natural_language_questions_means":
                    "Of NATURAL-LANGUAGE QUESTIONS AGENTS ASKED, what has none? "
                    "THE COVERAGE HOLE PROPER -- what the metric actually claims to mean.",
                "DO_NOT_AVERAGE":
                    "These answer DIFFERENT QUESTIONS. They are not bounds on each other "
                    "and there is no true value between them. A reader WILL average a "
                    "bracket, so this is not presented as one.",
            },
            "glob_patterns_are_a_correct_abstain_miscounted_as_a_hole":
                "'**/*COMPASSURANCE*' HAS a right answer -- comp-glob. A glob scoring zero "
                "on the curated rules and falling through to the primitive is THE FALLBACK "
                "WORKING AS DESIGNED. Counting it as a coverage hole SCORES A SUCCESS AS A "
                "FAILURE.",
            "MONOTONIC_DRIFT_WARNING":
                "The correction sequence is 2.40x -> 1.87x -> 1.84x -> 1.59x. EVERY "
                "correction moved the SAME WAY. A random error process corrects in BOTH "
                "directions; a MONOTONIC sequence is the signature of a systematic bias "
                "still only partly uncovered. DO NOT TREAT 1.59x AS A FLOOR. Further "
                "contamination, if found, is LIKELIER TO SHRINK THIS THAN TO GROW IT.",
            "fourth_contaminant_CONFIRMED_NOT_REMOVED":
                "Agents' own gibberish + off-domain probes survive in cohort R ('phhpk "
                "cpeaj djfkc', 'banana bread recipe'). An exact-token strip CANNOT catch "
                "GENERATED gibberish -- it is unpredictable by construction. Found by "
                "reading 25 random strings; 2/25 (~8%), NOT quoted as a point estimate.",
            "rule": "Cohort C is NOT the headline. Quote the named metric, never a digit "
                    "you did not re-derive.",
        },
        "recall_at_k": rk,
        "controls": ctrl,
        "mutation": mut,
        "no_pollution": dict(poll, training_delta=td),
        "row_tag_tally": cohort.get("row_tag_tally", {}),
    }
    out_path = args.out or BASELINE
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(baseline, fh, indent=1, ensure_ascii=True)

    shutil.rmtree(mirror, ignore_errors=True)
    os.unlink(tmp.name)

    print("")
    print("=" * 78)
    if not instrument_ok:
        print("VERDICT: *** INSTRUMENT FAILED (exit 2) *** -- the harness's OWN controls")
        print("         did not hold. DISCARD EVERY NUMBER ABOVE. An instrument that")
        print("         cannot fail is not an instrument; one whose controls failed is")
        print("         worse -- it is a liar with a denominator.")
        print("=" * 78)
        return 2
    if not clean:
        print("VERDICT: *** INSTRUMENT FAILED (exit 2) *** -- the harness POLLUTED the rail")
        print("         log. It corrupted the very denominator it exists to measure.")
        print("=" * 78)
        return 2
    if gate_failed:
        print("VERDICT: SUBJECT FAILED (exit 1) -- comp-which ROUTED GIBBERISH.")
        print("         This is THE DEFECT, faithfully reported. It is NOT a harness bug.")
        print("         TO-2 (the abstain) is what flips this to exit 0. Until it lands,")
        print("         every question this fabric cannot answer gets a confident answer.")
        print("         baseline -> %s" % os.path.relpath(args.out or BASELINE, WS))
        print("=" * 78)
        return 1
    print("VERDICT: PASS -- controls held, zero pollution, and comp-which ABSTAINED on")
    print("         100%% of generated gibberish.")
    print("         baseline -> %s" % os.path.relpath(args.out or BASELINE, WS))
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
