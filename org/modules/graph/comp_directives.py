#!/usr/bin/env python3
"""comp_directives -- the DIRECTIVES-NATIVE retirement compiler + mechanical check (LD-0433).

THE MECHANISM (CVO proposal @da758c3a43 + AMENDMENT 1 @92f88d908f directives-native + AMENDMENT 2
@52db6f2835 Andrew "recs approved, proceed"): FACT + MOVE + CHECK.
  FACT  -- human/sovereign only: the register owner (MSTR) writes a presence-based
           `retired: {at, by, authority}` block ON the live row. THE MACHINE NEVER WRITES A FACT.
  MOVE  -- `comp-directives retire`: rows carrying a COMPLETE record are CUT from the live view
           and land in DIRECTIVES_RETIRED.yaml as byte-frozen literal blocks with a stamped
           vintage. THE RETIRED VIEW IS 100% MACHINE-WRITTEN -- never hand-drawn.
  CHECK -- `comp-directives check`: partition + conservation + form + freeze invariants,
           mechanical; a hand edit in the retired view FAILS it (exercised, not claimed).

TWO FENCES, VERBATIM BY RULING (they ride here so they cannot drift):
  - CTO 63580: "the missions disposition must NOT become this proposal's dependency in either
    direction... Ship the mechanism; let the candidate be a candidate." This is a
    comp-directives-class tool, NOT a comp_missions extension: no missions machinery is read,
    extended, or waited on -- the PATTERN (build-artifact banner, post-commit refresh, mechanical
    recomputability) survives as a pattern; the SUBSTRATE is directives-native.
  - ANDREW ruling (c) @52db6f2835: NO attribution leg, EVER, absent his fresh word.

PATH DISCIPLINE: the register home is the REGISTER OWNER's word (MSTR 63620:
org/missions/DIRECTIVES.yaml, sibling beside it) -- never inferred from "conceptually".
OPAL_DIRECTIVES_DIR overrides BOTH paths for scratch exercise (the OPAL_RESOLVER_OUT pattern:
a fix whose only test is production is not tested, it is deployed).

Freeze law (proposal sec.4): a retired row's stances NEVER change after the cut --
closed-period-immutable, no TTL aging on a closed judgment. The freeze is verifiable by
construction: per-row sha256 over the frozen bytes + a whole-file emit hash.

Author: 0.8.0_AE_CloudComp (LD0433.RETIRE @67a9b8caf6, COO GO 63615). Rule-24 record: the
proposal sec.2 (presence-based, ZERO enum tokens minted, Lifecycle_Stage reuse REJECTED on grain
-- vertical-lifecycle vs work-completion are different grains); CTO gates the schema act.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
_DIR = os.environ.get("OPAL_DIRECTIVES_DIR") or os.path.join(WS, "org", "missions")
LIVE = os.path.join(_DIR, "DIRECTIVES.yaml")
RETIRED = os.path.join(_DIR, "DIRECTIVES_RETIRED.yaml")

_ROW_RE = re.compile(r"^  (D\d+):\s*$")          # a directive row opens at 2-space indent
_BREADCRUMB = ("# RETIRED rows live in DIRECTIVES_RETIRED.yaml (machine-cut by comp-directives; "
               "the retired view is 100% machine-written -- hand edits FAIL `comp-directives check`).")

_RETIRED_BANNER = """\
# org/missions/DIRECTIVES_RETIRED.yaml -- the RETIRED partition of the directives register.
#
# >> 100% MACHINE-WRITTEN (comp-directives retire). NEVER EDIT BY HAND -- every row is
#    byte-FROZEN at its cut vintage (closed-period-immutable: no TTL aging on a closed judgment)
#    and sealed by per-row + whole-file hashes; ANY hand edit FAILS `comp-directives check`.
#    The FACT (`retired: {at, by, authority}`) is the opposite pole: HUMAN/SOVEREIGN-written by
#    the register owner on the live row, with citation -- the machine only reacts to it.
#    TRIPWIRE (directives-native, per AMENDMENT 1): recomputable from the directives source of
#    record alone or it is rejected. <<
#
# Mechanism: LD-0433 (CVO proposal + amendments, Andrew-approved 2026-08-20). Owner of the LIVE
# register + all facts: 0.0.0_AB_MSTR per org/missions/.register-owner. This file's writer:
# comp-directives (0.8.0_AE_CloudComp lane).
"""


def _read(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return fh.read()


def _sha(text: str) -> str:
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _split_rows(live_text: str):
    """(preamble, [(id, block_text)]) -- text-surgical: the live register is HAND-WRITTEN and
    comment-rich, so the cut must preserve every byte it does not remove. pyyaml round-trip would
    rewrite MSTR's file; we never do that."""
    lines = live_text.splitlines(keepends=True)
    starts = [i for i, ln in enumerate(lines) if _ROW_RE.match(ln)]
    if not starts:
        return live_text, []
    pre = "".join(lines[:starts[0]])
    rows = []
    for j, s in enumerate(starts):
        e = starts[j + 1] if j + 1 < len(starts) else len(lines)
        rows.append((_ROW_RE.match(lines[s]).group(1), "".join(lines[s:e])))
    return pre, rows


def _dedent_block(block: str) -> str:
    """CANONICAL row form: the block dedented by its common leading indent (register rows sit at
    2 spaces under `directives:`). The freeze hash + frozen_row both use THIS form because a yaml
    literal block round-trips at its own block indent -- hashing raw live-file bytes would break
    the freeze compare on every clean emit (caught by self-test check 4, first run). Semantic
    bytes preserved exactly; only the container's uniform indent is normalized."""
    lines = block.splitlines()
    indents = [len(ln) - len(ln.lstrip()) for ln in lines if ln.strip()]
    cut = min(indents) if indents else 0
    return "\n".join((ln[cut:] if ln.strip() else "") for ln in lines).rstrip("\n") + "\n"


def _complete_record(row_block: str):
    """Parse the row block; return the retired record dict IFF complete (at+by+authority all
    present and non-empty), else None. AN INCOMPLETE RECORD IS NOT A THIRD STATE -- the check
    fails it; the MOVE refuses it (never a silent partial cut)."""
    import yaml
    try:
        doc = yaml.safe_load(row_block)
    except Exception:  # noqa: BLE001
        return None
    if not isinstance(doc, dict) or len(doc) != 1:
        return None
    row = next(iter(doc.values())) or {}
    rec = row.get("retired")
    if isinstance(rec, dict) and all(str(rec.get(k) or "").strip() for k in ("at", "by", "authority")):
        return rec
    return None


def _load_retired():
    """The retired view, parsed. Returns (doc, raw_text) or ({}, '') when absent (first emit)."""
    import yaml
    if not os.path.exists(RETIRED):
        return {}, ""
    raw = _read(RETIRED)
    return (yaml.safe_load(raw) or {}), raw


def _emit_retired(doc: dict) -> str:
    """Serialize the retired view DETERMINISTICALLY, machine-only, and seal it: emit_hash =
    sha256 over every line above the emit_hash line. ANY hand edit -- content, order, whitespace
    -- breaks the seal."""
    body = [_RETIRED_BANNER,
            "version: 1",
            'tripwire: "recomputable from the directives source of record alone"',
            "ever_minted: [%s]" % ", ".join(sorted(doc.get("ever_minted", []),
                                                   key=lambda d: int(d[1:]))),
            "emit_log:"]
    for e in doc.get("emit_log", []):
        body.append("  - " + json.dumps(e, sort_keys=True))
    body.append("directives:")
    dirs = doc.get("directives", {}) or {}
    for did in sorted(dirs, key=lambda d: int(d[1:])):
        row = dirs[did]
        body.append("  %s:" % did)
        body.append("    frozen_row: |")
        for ln in row["frozen_row"].splitlines():
            body.append("      " + ln if ln.strip() else "")
        # KEY LINEAGE (2026-08-26): emitted ONLY when present, and emitted HERE rather than
        # left to a hand edit, because this serializer is an ALLOWLIST -- a field it does not
        # know is DROPPED at the next `retire`, and the emit_hash seal makes a hand edit
        # detectable but not durable. A marker the tool does not write is not a marker.
        kr = row.get("key_reused_on")
        if kr:
            body.append("    key_reused_on:")
            for k in ("at", "by_commit", "note"):
                if k in kr:
                    body.append("      %s: %s" % (k, json.dumps(kr[k])))
        rv = row["retired_vintage"]
        body.append("    retired_vintage:")
        for k in ("cut_at", "stances_as_of", "row_sha256"):
            # json.dumps, deliberately NOT yaml.safe_dump: safe_dump on a bare scalar appends a
            # `...` document-end marker that .strip() does not remove -- it leaked into the emit
            # and ENDED the yaml document mid-file (caught by self-test check 4, first run).
            body.append("      %s: %s" % (k, json.dumps(rv[k])))
    text = "\n".join(body) + "\n"
    return text + "emit_hash: %s\n" % _sha(text)


def _stances_as_of(live_pre: str) -> str:
    m = re.search(r'^as_of:\s*"?([0-9-]+)"?', live_pre, re.M)
    return m.group(1) if m else "UNKNOWN"


def retire(dry_run: bool = False) -> int:
    """The MOVE. Cuts every live row carrying a COMPLETE retired record into the retired view.
    Idempotent: a no-new-facts run changes nothing and says so with its denominator."""
    live_text = _read(LIVE)
    pre, rows = _split_rows(live_text)
    to_cut = [(did, blk, _complete_record(blk)) for did, blk in rows]
    cut = [(d, b, r) for d, b, r in to_cut if r is not None]
    keep = [(d, b) for d, b, r in to_cut if r is None]
    print("comp-directives retire: %d live row(s) scanned, %d carry a COMPLETE retired record, "
          "%d stay live%s" % (len(rows), len(cut), len(keep), " [DRY-RUN]" if dry_run else ""))
    # A row with a PARTIAL record is a defect, not a candidate -- refuse loudly, cut nothing.
    partial = []
    import yaml
    for did, blk in rows:
        row = (yaml.safe_load(blk) or {}).get(did) or {}
        rec = row.get("retired")
        if rec is not None and _complete_record(blk) is None:
            partial.append(did)
    if partial:
        print("  REFUSED: %s carry an INCOMPLETE retired record (at/by/authority all required; "
              "a bare flag is not a fact). Nothing cut. Fix the record (register owner's hand)."
              % ", ".join(partial), file=sys.stderr)
        return 2
    if not cut:
        print("  Nothing to move -- the views are already partitioned (idempotent no-op).")
        return 0
    doc, _raw = _load_retired()
    dirs = doc.get("directives", {}) or {}
    already = [d for d, _b, _r in cut if d in dirs]
    if already:
        print("  REFUSED: %s already in the retired view while still live -- PARTITION breach; "
              "run `comp-directives check`." % ", ".join(already), file=sys.stderr)
        return 2
    as_of = _stances_as_of(pre)
    for did, blk, _rec in cut:
        canon = _dedent_block(blk)
        dirs[did] = {"frozen_row": canon,
                     "retired_vintage": {"cut_at": _now(), "stances_as_of": as_of,
                                          "row_sha256": _sha(canon)}}
    ever = sorted(set(doc.get("ever_minted", [])) | {d for d, _ in rows} | set(dirs),
                  key=lambda d: int(d[1:]))
    doc = {"ever_minted": ever,
           "emit_log": (doc.get("emit_log", []) or []) + [
               {"at": _now(), "cut": sorted(d for d, _b, _r in cut), "tool": "comp-directives"}],
           "directives": dirs}
    new_live = pre + "".join(b for _d, b in keep)
    if _BREADCRUMB not in new_live:
        lines = new_live.splitlines(keepends=True)
        ins = 1 if lines and lines[0].startswith("#") else 0
        lines.insert(ins, _BREADCRUMB + "\n")
        new_live = "".join(lines)
    if dry_run:
        print("  DRY-RUN: would cut %s; live -> %d row(s); retired -> %d row(s). No writes."
              % (", ".join(d for d, _b, _r in cut), len(keep), len(dirs)))
        return 0
    with open(RETIRED, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(_emit_retired(doc))
    with open(LIVE, "w", encoding="utf-8", newline="") as fh:
        fh.write(new_live)
    print("  CUT %s -> DIRECTIVES_RETIRED.yaml (frozen @ stances as_of %s); live view: %d row(s) "
          "remain; ever_minted: %d." % (", ".join(d for d, _b, _r in cut), as_of, len(keep), len(ever)))
    return 0


def mark_reused(did: str, note: str, by_commit: str = "") -> int:
    """Declare that a RETIRED directive's KEY has been re-issued to a new live directive.

    Exists because the retired view is SEALED (emit_hash) and its serializer is an ALLOWLIST:
    a hand-added marker breaks the seal now and is dropped at the next `retire`. This routes the
    edit through the emitter, so the marker persists and the seal stays machine-computed.
    """
    doc, _raw = _load_retired()
    dirs = (doc.get("directives") or {}) if doc else {}
    if did not in dirs:
        print("  REFUSED: %s is not in the retired view -- nothing to mark." % did, file=sys.stderr)
        return 2
    live_ids = [d for d, _ in _split_rows(_read(LIVE))[1]]
    if did not in live_ids:
        print("  REFUSED: %s is not LIVE -- a key that is not re-issued is not re-minted; this "
              "marker would assert a re-mint that has not happened." % did, file=sys.stderr)
        return 2
    dirs[did]["key_reused_on"] = {"at": _now(), "by_commit": by_commit, "note": note}
    with open(RETIRED, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(_emit_retired(doc))
    print("  MARKED %s key_reused_on -- retired view re-emitted and re-sealed." % did)
    return 0


def check() -> int:
    """The CHECK. rc 0 = all invariants hold | 2 = violation (each printed) | 1 = tool error.
    Every verdict prints its denominator."""
    import yaml
    v = []
    live_text = _read(LIVE)
    pre, rows = _split_rows(live_text)
    live_ids = [d for d, _ in rows]
    doc, raw = _load_retired()
    dirs = (doc.get("directives") or {}) if doc else {}
    ret_ids = list(dirs)
    # 1. PARTITION -----------------------------------------------------------------------------
    both = sorted(set(live_ids) & set(ret_ids))
    # A RE-MINT is a legal both-views state: the KEY is re-issued to a NEW directive while the
    # prior one stays frozen in the retired view. It is exempt ONLY when the retired row DECLARES
    # it (key_reused_on). An undeclared both-views key is still a breach -- the marker is what
    # separates a deliberate re-mint from a partition failure, and without it the two are
    # byte-identical to this check.
    reused = [d for d in both if (dirs.get(d) or {}).get("key_reused_on")]
    undeclared = [d for d in both if d not in reused]
    if undeclared:
        v.append("PARTITION: %s appear in BOTH views" % ", ".join(undeclared))
    if reused:
        # NOT a violation, but NEVER silent: an exemption nobody can see is how a real breach
        # later hides behind a marker somebody added years ago.
        print("  KEY-LINEAGE: %s re-minted (declared); PARTITION exempt for %d key(s)."
              % (", ".join(reused), len(reused)))
    for did in ret_ids:
        if _complete_record(dirs[did].get("frozen_row", "")) is None:
            v.append("PARTITION/FORM: retired %s lacks a COMPLETE retired record (at/by/authority)"
                     % did)
    for did, blk in rows:
        if _complete_record(blk) is not None:
            v.append("PARTITION: live %s carries a complete retired record -- the MOVE is owed "
                     "(run comp-directives retire)" % did)
    # 2. CONSERVATION --------------------------------------------------------------------------
    ever = set(doc.get("ever_minted", []) if doc else [])
    missing = sorted(ever - set(live_ids) - set(ret_ids))
    if missing:
        v.append("CONSERVATION: %s in ever_minted but in NEITHER view (silent deletion)"
                 % ", ".join(missing))
    # 3. FORM (both views: reference-only members, no globs/attach) ----------------------------
    def _form(did, row_yaml_text, view):
        try:
            row = (yaml.safe_load(row_yaml_text) or {}).get(did) or {}
        except Exception as e:  # noqa: BLE001
            v.append("FORM: %s row %s unparseable (%s)" % (view, did, type(e).__name__))
            return
        if "attach" in row:
            v.append("FORM: %s row %s carries `attach` (tripwire: members are references only)"
                     % (view, did))
        mem = row.get("members") or {}
        for kind in ("subgroups", "projects"):
            for tok in (mem.get(kind) or []):
                if any(c in str(tok) for c in "/\\*?"):
                    v.append("FORM: %s row %s member %r is a path/glob -- references only "
                             "(the tripwire)" % (view, did, tok))
    for did, blk in rows:
        _form(did, blk, "live")
    for did in ret_ids:
        _form(did, dirs[did].get("frozen_row", ""), "retired")
    # 4. FREEZE (per-row hash + whole-file seal) -----------------------------------------------
    for did in ret_ids:
        rv = dirs[did].get("retired_vintage") or {}
        want = rv.get("row_sha256", "")
        got = _sha(dirs[did].get("frozen_row", ""))
        if want != got:
            v.append("FREEZE: retired %s stance bytes CHANGED after the cut (hash %s.. != "
                     "stamped %s..) -- a closed judgment was edited" % (did, got[:12], want[:12]))
    if raw:
        m = re.search(r"^emit_hash: ([0-9a-f]{64})\s*$", raw, re.M)
        if not m:
            v.append("FREEZE: retired view carries NO emit_hash seal -- not a machine emit")
        else:
            body = raw[:m.start()]
            if _sha(body) != m.group(1):
                v.append("FREEZE: emit_hash seal BROKEN -- the retired view was edited by hand "
                         "after the machine wrote it (recompute %s.. != stored %s..)"
                         % (_sha(body)[:12], m.group(1)[:12]))
    print("comp-directives check: live=%d retired=%d ever_minted=%d -- %d violation(s)"
          % (len(live_ids), len(ret_ids), len(ever), len(v)))
    for msg in v:
        print("  VIOLATION: " + msg)
    if not v:
        print("  PARTITION + CONSERVATION + FORM + FREEZE all hold (denominators above).")
    return 2 if v else 0


def self_test() -> int:
    """Scratch-dir battery: every invariant BOTH directions + the two ruling-named mutants."""
    import shutil
    import tempfile
    global _DIR, LIVE, RETIRED
    keep = (_DIR, LIVE, RETIRED)
    ok = []

    def chk(name, cond):
        ok.append(bool(cond))
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))

    scratch = tempfile.mkdtemp(prefix="comp_directives_st_")
    try:
        _DIR = scratch
        LIVE = os.path.join(scratch, "DIRECTIVES.yaml")
        RETIRED = os.path.join(scratch, "DIRECTIVES_RETIRED.yaml")
        fixture = (
            "# fixture register (self-test scratch -- NEVER the real file)\n"
            'version: 1\nas_of: "2026-08-19"\n\ndirectives:\n'
            "  D1:\n    title: \"alpha\"\n    directive: \"docs/architecture/D1.md\"\n"
            "    placement: \"LAPTOP\"\n    members:\n      subgroups: [A.B]\n      projects: []\n"
            "    stance: \"live work\"\n"
            "  D8:\n    title: \"bravo\"\n    directive: \"docs/architecture/D8.md\"\n"
            "    placement: \"SITEZ\"\n    members:\n      subgroups: [C.D]\n      projects: [P1]\n"
            "    stance: \"done per sovereign word\"\n"
            "    retired:\n      at: \"2026-08-20\"\n      by: 0.0.0_AB_MSTR\n"
            "      authority: 'Andrew-direct + record @x'\n"
        )
        with open(LIVE, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(fixture)
        import contextlib
        import io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc1 = retire()
        live_after = _read(LIVE)
        chk("1 MOVE: the recorded row (D8) is CUT to the retired view, rc 0", rc1 == 0
            and "  D8:" not in live_after and os.path.exists(RETIRED))
        chk("2 MUTANT unrecorded-move: the UNRECORDED row (D1) did NOT move -- its bytes survive "
            "verbatim in the live view", "  D1:" in live_after and "title: \"alpha\"" in live_after)
        chk("3 breadcrumb: the live view points at the retired sibling once",
            live_after.count("DIRECTIVES_RETIRED.yaml (machine-cut") == 1)
        with contextlib.redirect_stdout(buf):
            rc2 = check()
        chk("4 CHECK green on a clean machine emit (rc 0)", rc2 == 0)
        with contextlib.redirect_stdout(buf):
            rc3 = retire()
        chk("5 idempotent: a no-new-facts re-run changes nothing, rc 0",
            rc3 == 0 and _read(LIVE) == live_after)
        # MUTANT: the planted hand edit in the retired view MUST fail the check.
        raw = _read(RETIRED)
        with open(RETIRED, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(raw.replace("done per sovereign word", "done per sovereign word (edited)"))
        with contextlib.redirect_stdout(buf):
            rc4 = check()
        chk("6 MUTANT hand-edit: a stance edit in the retired view FAILS the check (rc 2, "
            "freeze + seal)", rc4 == 2)
        with open(RETIRED, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(raw)
        with contextlib.redirect_stdout(buf):
            _rc7 = check()
        chk("7 restore control: reverting the hand edit returns the check to green", _rc7 == 0)
        # CONSERVATION mutant: deleting a retired row entirely (id vanishes from both views).
        import yaml
        doc = yaml.safe_load(raw)
        body_missing = raw.replace("  D8:\n", "  D8_GONE_MARKER:\n", 1)
        # simpler: drop D8 from ever_minted? No -- delete the row block, keep ever_minted:
        lines = raw.splitlines(keepends=True)
        s = next(i for i, ln in enumerate(lines) if ln.startswith("  D8:"))
        e = next((i for i in range(s + 1, len(lines))
                  if lines[i].startswith("emit_hash:") or re.match(r"^  D\d+:", lines[i])), len(lines))
        mutated = "".join(lines[:s] + lines[e:])
        with open(RETIRED, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(mutated)
        with contextlib.redirect_stdout(buf):
            rc5 = check()
        chk("8 CONSERVATION mutant: deleting the retired row (id in neither view) FAILS (rc 2)",
            rc5 == 2)
        with open(RETIRED, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(raw)
        # PARTIAL-record refusal: a bare flag is not a fact.
        with open(LIVE, "a", encoding="utf-8", newline="\n") as fh:
            fh.write("  D9:\n    title: \"charlie\"\n    directive: \"docs/architecture/D9.md\"\n"
                     "    placement: \"SITEZ\"\n    members:\n      subgroups: []\n"
                     "      projects: []\n    stance: \"live\"\n    retired:\n      at: \"2026-08-20\"\n")
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            rc6 = retire()
        chk("9 PARTIAL record REFUSED (at only, no by/authority): rc 2, nothing cut",
            rc6 == 2 and "  D9:" in _read(LIVE))
        _t = yaml.safe_load(_read(RETIRED))
        chk("10 shape: frozen_row + retired_vintage{cut_at, stances_as_of, row_sha256} + "
            "ever_minted + emit seal all present (ever_minted is EMIT-maintained, so D9 -- added "
            "live after the last successful emit -- correctly not yet in it)",
            "D8" in _t["directives"] and set(_t["directives"]["D8"]["retired_vintage"]) ==
            {"cut_at", "stances_as_of", "row_sha256"} and _t["ever_minted"] == ["D1", "D8"]
            and "emit_hash" in _t)
        _ = (doc, body_missing)  # keep locals honest for debuggers; no functional role
    finally:
        _DIR, LIVE, RETIRED = keep
        shutil.rmtree(scratch, ignore_errors=True)
    n = sum(1 for x in ok if x)
    print("--- comp-directives self-test: %d/%d passed ---" % (n, len(ok)))
    return 0 if n == len(ok) else 1


_USAGE = """comp-directives -- the directives-native retirement compiler + check (LD-0433). Usage:
  comp-directives retire [--dry-run]   the MOVE: cut rows carrying a COMPLETE human-written
                                       retired record into DIRECTIVES_RETIRED.yaml (machine-only)
  comp-directives check                the CHECK: partition/conservation/form/freeze (0|2|1)
  comp-directives --self-test          scratch battery incl. BOTH ruling-named mutants
  comp-directives --help | -h          this usage (never writes)
An UNKNOWN argument REFUSES (rc 2) -- never falls through to a write (the comp-system --help lesson)."""


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or "--help" in args or "-h" in args:
        print(_USAGE)
        return 0
    if args[0] == "mark-reused":
        # <Dn> <note>  -- declare a re-minted key. Positional, so it does not pass through the
        # exact-match `known` filter below.
        if len(args) < 3:
            print("comp-directives mark-reused <Dn> <note> [<by_commit>] -- REFUSED (rc 2), "
                  "nothing written.", file=sys.stderr)
            return 2
        try:
            return mark_reused(args[1], args[2], args[3] if len(args) > 3 else "")
        except Exception as e:  # noqa: BLE001
            print("comp-directives: ERROR (%s: %s)" % (type(e).__name__, e), file=sys.stderr)
            return 1
    known = {"retire", "check", "--self-test", "--dry-run"}
    unknown = [a for a in args if a not in known]
    if unknown:
        print("comp-directives: UNKNOWN argument(s): %s -- REFUSED (rc 2), nothing written.\n%s"
              % (", ".join(unknown), _USAGE), file=sys.stderr)
        return 2
    if "--self-test" in args:
        return self_test()
    try:
        if "retire" in args:
            return retire(dry_run="--dry-run" in args)
        if "check" in args:
            return check()
    except Exception as e:  # noqa: BLE001 -- a tool that cannot evaluate is an ERROR, never a pass
        print("comp-directives: ERROR (%s: %s)" % (type(e).__name__, e), file=sys.stderr)
        return 1
    print(_USAGE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
