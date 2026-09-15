#!/usr/bin/env python3
"""_comprail.py -- shared helpers for the NFRA_COMPRAIL on-rails primitives (comp-grep,
comp-glob). Single-sources the tricky bits so the two CLIs can't drift:

  * repo_root()            -- the workspace root (git toplevel, .tools/.. fallback)
  * gitignore_aware_files  -- the CORPUS-SELECTABLE working set, RECURSING nested git repos
                              (portal is a tracked gitlink, NOT a .gitmodules submodule;
                              git ls-files in the parent sees only the pointer, so a naive
                              enumeration silently misses all 1000+ portal files -- the bug
                              this module exists to prevent).
  * log_rail               -- best-effort parseable telemetry to org/mcp/comp-which-rail.log
                              (the TO-5 coverage-audit feed).
  * out_of_corpus_count    -- HIDDEN-FILE TRACKING: how many files in a scope the DEFAULT corpus
                              cannot see, split searchable vs ephemeral floor. Lets a caller tell
                              "0 hits, nothing here" apart from "0 hits, and I could not look".

CORPUS MODES (Andrew-direct 2026-08-27): default | all | ignored | raw -- see the CORPUS SELECTION
block below. The default is the historical population and is unchanged; every other mode is opt-in.

NOTE on Windows safety: only ever shells out to git.exe (a native exe -- safe via subprocess);
never `bash -c` (which can silently return empty rc0 on this box). ASCII-only.
"""
from __future__ import annotations

import datetime
import os
import re
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))


# ---- SYSTEMS-UNDERSTANDING classifier (the interplay, Andrew-direct 2026-06-22) -------------
# A grep match read as isolated text is failure-mode #2: skimming a file without understanding
# its dependencies. classify_path maps a matched FILE to the comp-tool that explains ITS place
# in the Opal dependency graph -- so every comp-grep hit arrives WITH the "and here is how this
# file connects" hook. grep stays fully flexible; the systems-understanding rides alongside.
def classify_path(p: str):
    """-> (role_label, [comp-tool hooks]) for a system-significant file, else None."""
    pl = p.replace("\\", "/").lower()
    base = os.path.basename(p.replace("\\", "/"))
    stem = re.sub(r"\.[A-Za-z0-9]+$", "", base)
    if re.search(r"/scripts/gold/[^/]+\.py$", pl):
        return ("gold producer script",
                ["comp-pipescript io %s" % base, "comp-blast <fn-in-this-file>"])
    if re.search(r"/scripts/(silver|bronze)/[^/]+\.py$", pl):
        tier = "silver" if "/silver/" in pl else "bronze"
        return ("%s producer script" % tier,
                ["comp-pipescript io %s" % base, "comp-pipescript postdeps %s" % base])
    if "/lambda/" in pl and pl.endswith(".py"):
        return ("lambda source", ["comp-iam service <fn>", "comp-aws", "pipescript --resource <fn>"])
    if pl.endswith(".tsx") or "/portal/src/" in pl:
        comp = stem
        if stem.lower() in ("index", "main"):  # index.tsx -> the parent dir is the real component
            parent = os.path.basename(os.path.dirname(p.replace("\\", "/")))
            comp = parent or stem
        return ("portal component", ["comp-transform schema-check %s" % comp, "comp-routes behaviors"])
    if pl.endswith(".tf") or "/infra/aws/" in pl:
        return ("infra / terraform", ["comp-aws", "comp-iam gaps"])
    if re.search(r"/(gold|platinum|silver)/[^/]*\.(json|parquet)$", pl):
        return ("served artifact", ["pipescript --resource %s" % base, "comp-freshness %s" % base])
    return None


def systems_context(paths, limit: int = 12):
    """Render the SYSTEMS CONTEXT block for a set of matched/listed files. Returns a list of
    ASCII lines (empty if nothing system-significant). This is what turns a flat grep result
    into a dependency-aware one."""
    seen = []
    roles = {}
    for p in paths:
        c = classify_path(p)
        if not c:
            continue
        role, hooks = c
        roles.setdefault(role, 0)
        roles[role] += 1
        if len(seen) < limit and p not in [s[0] for s in seen]:
            seen.append((p, role, hooks))
    if not seen:
        return []
    out = ["", "SYSTEMS CONTEXT -- these matches sit in the Opal dependency graph; do NOT read them",
           "as isolated text. Per file, the comp-tool that explains what feeds/consumes it:"]
    for p, role, hooks in seen:
        out.append("  %s  [%s]" % (p, role))
        out.append("     -> %s" % "   |   ".join(hooks))
    extra = sum(roles.values()) - len(seen)
    if extra > 0:
        out.append("  (+%d more system-significant file(s); roles: %s)" % (
            extra, ", ".join("%s x%d" % (r, n) for r, n in sorted(roles.items()))))
    return out


def harden_stdout() -> None:
    """Make stdout/stderr UNCRASHABLE on this Windows box. We print content read from
    arbitrary repo files; a cp1252 console crashes on the first non-ASCII byte
    (UnicodeEncodeError -- the charmap class CLAUDE.md warns about). errors='replace'
    means an unencodable char becomes '?' instead of killing the whole search."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="replace")  # py3.7+
        except Exception:
            pass


# Control bytes other than TAB / LF / CR are replaced on emit. NFRA_COMPRAIL-S1 (CVO, 2026-08-24):
# a NUL echoed from matched content made `comp-find | grep` print "Binary file (standard input)
# matches" and drop EVERY hit at exit 0 -- a retrieval failure returning a well-formed value on
# the path Rule 21 mandates. ASCII-encoding alone does not catch it: NUL is valid ASCII.
_CTRL_TABLE = {c: "?" for c in range(0x00, 0x20) if c not in (0x09, 0x0A, 0x0D)}
_CTRL_TABLE[0x7F] = "?"


def ascii_safe(s: str) -> str:
    """Force a string to printable ASCII (CLAUDE.md: no non-ASCII in tool stdout). Belt to the
    harden_stdout suspenders -- keeps output grep/CloudWatch-clean regardless of codepage. Control
    bytes (NUL, BS, ESC, ...) become '?' so a pipe downstream never sees a "binary" stream."""
    try:
        return s.encode("ascii", "replace").decode("ascii").translate(_CTRL_TABLE)
    except Exception:
        return s


def repo_root() -> str:
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             cwd=_HERE, capture_output=True, text=True, timeout=15)
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except Exception:
        pass
    return os.path.dirname(_HERE)


def corpus_root() -> str:
    """The tree the CALLER is standing in -- i.e. what a search should SCAN.

    repo_root() resolves from _HERE, this file's own on-disk location. That is CORRECT for the
    rail's own logs and data (one install, one log) and WRONG for the corpus: a caller inside a
    linked worktree gets the MAIN checkout scanned and a MEASURED denominator over the wrong tree,
    where a false zero is indistinguishable from a true absence. Recorded as LIMIT 4 in
    org/modules/graph/INSTRUMENT_LIMITS.md; rule 14b mandates the worktree that provokes it.

    Falls back to repo_root(), so a caller outside any worktree behaves exactly as before.
    """
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             cwd=os.getcwd(), capture_output=True, text=True, timeout=15)
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except Exception:
        pass
    return repo_root()


def _utc_ts() -> str:
    try:
        return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return "?"


def log_rail(rail_log: str, decision: str, tool: str, term: str, extra: str = "") -> None:
    term1 = (term or "-").replace("\n", " ").replace("\r", " ")[:120]
    # extra was written RAW -- a multi-line pathspec/fragment wrote continuation lines whose first
    # token then parsed as a rail TAG (the "=== junk-row class). Sanitize every interpolated field.
    extra1 = (extra or "").replace("\n", " ").replace("\r", " ")[:200]
    # SRC ATTRIBUTION (NFRA_COMPCLOSE 2026-07-14, COMPASSURANCE TO-8d): a comp-grep row spawned by
    # comp-which's fallback was byte-identical to a direct agent invocation, so RUN-GREP could not
    # be attributed and the Rule-21 rail could not answer the question it exists to answer.
    src = "comp-which" if os.environ.get("COMP_WHICH_CHILD") else "direct"
    # SERIAL (best-effort, same pass): the route->run outcome join's REJECTED limb is "the agent
    # ran a fallback grep instead of the routed tool" -- unprovable while rail rows carried no
    # actor. env first; the LD-0290 session-keyed serial file second; absent stays absent (never
    # guessed from the shared .agent_context -- that file answers "what TO", never "who").
    serial = os.environ.get("OPAL_AGENT_SERIAL", "")
    if not serial:
        sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
        if sid:
            try:
                sp = os.path.join(os.path.dirname(rail_log), "sessions", sid + ".serial")
                with open(sp, encoding="utf-8", errors="replace") as fh:
                    first = fh.read().strip().splitlines()
                serial = first[0].strip() if first else ""
            except Exception:
                serial = ""
    line = "%s  %s  tool=%s  term=%s  src=%s  serial=%s  %s\n" % (
        _utc_ts(), decision, tool, term1, src, serial or "-", extra1)
    try:
        os.makedirs(os.path.dirname(rail_log), exist_ok=True)
        with open(rail_log, "a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass  # best-effort; never break a search on a log failure


def _ls_files(cwd: str, prefix: str = ""):
    """tracked + untracked-not-ignored, NUL-safe. Returns (list, err)."""
    cmd = ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"]
    try:
        out = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=60)
    except Exception as e:
        return None, "git ls-files failed in %s: %s" % (cwd, e)
    if out.returncode != 0:
        return None, "git ls-files rc=%d in %s: %s" % (out.returncode, cwd, (out.stderr or "").strip()[:160])
    return [prefix + p for p in out.stdout.split("\0") if p], None


def _gitlinks(cwd: str):
    """nested-repo paths (mode 160000 in the index) -- catches portal + every gitlink,
    independent of .gitmodules registration."""
    try:
        out = subprocess.run(["git", "ls-files", "--stage"], cwd=cwd,
                             capture_output=True, text=True, timeout=30)
    except Exception:
        return []
    if out.returncode != 0:
        return []
    paths = []
    for line in out.stdout.splitlines():
        # format: "<mode> <sha> <stage>\t<path>"
        if line.startswith("160000 "):
            tab = line.find("\t")
            if tab != -1:
                paths.append(line[tab + 1:])
    return paths


def _norm(p: str) -> str:
    return p.replace("\\", "/").strip("/")


def _touches(repo: str, ps: str) -> bool:
    """does pathspec ps intersect nested repo path? (repo under ps, or ps into repo, or '.')"""
    r, s = _norm(repo), _norm(ps)
    if s in ("", "."):
        return True
    return r == s or r.startswith(s + "/") or s.startswith(r + "/")


def _under(f: str, ps: str) -> bool:
    f, s = _norm(f), _norm(ps)
    if s in ("", "."):
        return True
    return f == s or f.startswith(s + "/")


_EXCLUDE_MAGIC = re.compile(r"^:(?:\(exclude\)|!|\^)")


def _split_pathspec(pathspec):
    """(includes, excludes): git's exclude magic -- :(exclude)X, :!X, :^X -- names a path to SUBTRACT.
    Read as a literal prefix it matched nothing, so an exclude-only scope scanned 0 files and an
    exclude beside an include was silently dropped (LGIC_ENFORCE-W1-S3). No includes means the whole
    working set, as in git."""
    inc, exc = [], []
    for ps in pathspec or []:
        m = _EXCLUDE_MAGIC.match(ps)
        if m:
            exc.append(ps[m.end():])
        else:
            inc.append(ps)
    return inc, exc


# ---- NFRA_COMPRAIL sovereign-held guard (GG1) -----------------------------------------------
# A bare / broad invocation returns the WHOLE repo working set and the caller then READS every
# file -- including the section-8 sovereign-held trees (data/black_diamond/, canonical schwab
# silver). gitignore_aware_files EXCLUDES those prefixes BY DEFAULT via a string-prefix predicate
# (it NEVER opens a held file to decide) and hands the caller a LOUD note, so a bare search cannot
# silently read bd AND an excluded held path is NEVER reported as "confirmed absent" (that would
# make the never-dead-end rail LIE). data/inf + data/cot are IN-SCOPE firms -- deliberately NOT
# excluded. --include-held (caller flag) is the audited directed override. Mirrors the
# comp-constants CC2 guard: enforce the hold at the shared chokepoint, string-only, never read to decide.
#
# LIFTED 2026-07-14 (1.0.0_SA_CTO, executing Andrew-direct ~03:3xZ to COO, verbatim: "49 is back on
# the menu now, take the sovereign block off completely, that is no excuse to not verify the work.").
# The two entries below WERE the 2026-07-09 49F/Schwab/bd sovereign block; both lift with it. The
# INF-chain hold is a SEPARATE mechanism (frozen individual FILES + Door 5/6 -- never these trees)
# and is deliberately not expressible here. THE GUARD MACHINERY STAYS: a future hold is a one-line
# re-add to this tuple, and --include-held / the LOUD held_note keep working unchanged.
# Was: ("data/black_diamond/", "data/canonical/schwab/silver/")
HELD_PREFIXES = ()


def _is_held(path: str) -> bool:
    """String-prefix test against the section-8 sovereign-held prefixes. NEVER opens/reads the file."""
    p = _norm(path)
    return any(p == pre.rstrip("/") or p.startswith(pre) for pre in HELD_PREFIXES)


def _names_held(pathspec) -> bool:
    """True if a pathspec entry is AT or INSIDE a held prefix (a DIRECTED held search)."""
    for ps in (pathspec or []):
        s = _norm(ps)
        if s in ("", "."):
            continue
        for pre in HELD_PREFIXES:
            pn = pre.rstrip("/")
            if s == pn or s.startswith(pn + "/"):
                return True
    return False


# ---- CORPUS SELECTION (NFRA_COMPRAIL corpus extension, Andrew-direct 2026-08-27) -------------
# THE PREMISE THAT WAS WRONG, AND THE MEASUREMENT THAT CORRECTED IT (0.8.0_AE_CloudComp,
# 2026-08-27, this device): the build spec recorded comp-find's corpus as "TRACKED FILES ONLY".
# IT IS NOT. _ls_files runs `git ls-files --cached --others --exclude-standard`, and `--others`
# puts UNTRACKED-BUT-NOT-IGNORED files IN the corpus already. Positive control, same turn:
# data/assets/scripts/gold/runners_49f/fit_reports/fit_report_2026-08-07.json -- confirmed
# untracked via `git ls-files --error-unmatch` -- returned `1 hit across 1 file(s) scanned` for
# a token in its body.  ==> THE CORPUS BOUNDARY IS THE .gitignore, AND ONLY THE .gitignore.
# Had the spec's premise been built to, "add untracked files" would have added NOTHING.
#
# Populations measured at this device, same turn:
#   IN corpus (tracked + untracked-not-ignored)    27,370 scanned (+13 unreadable, +1,951 binary)
#   IGNORED -- invisible to every comp-find to date    449,884
#
# WHY `--corpus all` IS NOT A LITERAL ALL. Enumerating the ignored set alone costs 11.7s, and the
# in-corpus sweep of 27,370 files already costs 25.7s (~0.94ms/file); a literal 449,884-file sweep
# is ~7 minutes, and a rail nobody waits for is a rail nobody uses. The mass is EPHEMERA, not
# content:
#   .runtmp/portal-promote-*   326,639   10 dead promote worktrees
#   org/mcp                     80,873   agent inbox mail -- REAL search value, keep it
#   infra/aws                   31,152   vendored lambda layer deps
# Dropping the declared floor below leaves 93,771 -- a 79% cut that removes almost no answerable
# content. THE FLOOR IS PRINTED, NEVER SILENT: a corpus that quietly discards 356k files is the
# same false-absence machine this rail exists to prevent. --corpus raw disables the floor.
# FLOOR MEMBERSHIP, MEASURED AT THIS DEVICE 2026-08-27 (files matched per entry):
#   .runtmp 328,445 | node_modules 345,742 | __pycache__ 3,715 | .ruff_cache 243
#   .pytest_cache 10 | .pyc 3,715 | .o 277
#   NOT FIRING TODAY (kept -- these are PROSPECTIVE, and each CAN fire the moment such a tree
#   appears; node_modules itself did not exist here before portal): .venv venv .git .mypy_cache
#   .next .turbo .pyo .class .so.dbg
# `dist-info` WAS listed and was REMOVED: this predicate is an EXACT SEGMENT match and real dirs
# are named `<pkg>-<ver>.dist-info`, so that entry could never fire BY CONSTRUCTION -- a declared
# control that cannot fire reads as coverage while providing none. A member that has not fired YET
# is defensive; a member that CANNOT fire is a lie in the floor's own denominator.
EPHEMERAL_DIRS = (".runtmp", "node_modules", "__pycache__", ".venv", "venv", ".git",
                  ".ruff_cache", ".mypy_cache", ".pytest_cache", ".next", ".turbo")
EPHEMERAL_EXT = (".pyc", ".pyo", ".class", ".o", ".so.dbg")
CORPUS_MODES = ("default", "all", "ignored", "raw")


def _is_ephemeral(path: str) -> bool:
    """Declared ephemeral/vendor noise floor. String-only on the PATH -- never opens the file."""
    p = _norm(path)
    for seg in p.split("/"):
        if seg in EPHEMERAL_DIRS:
            return True
    return p.endswith(EPHEMERAL_EXT)


def _ls_ignored(cwd: str, pathspec, prefix: str = ""):
    """The IGNORED set -- files git is deliberately hiding. `--directory` is deliberately NOT
    passed: it would collapse an ignored directory to one entry and the files inside would be
    invisible again, which is the exact defect this function exists to remove. Returns (list, err).

    The pathspec is pushed DOWN into git (`-- <ps>...`) rather than filtered in python: scoping
    org/mcp costs 1.35s against 11.7s unscoped (measured), so a targeted --corpus all stays usable.
    """
    cmd = ["git", "ls-files", "-z", "--others", "--ignored", "--exclude-standard"]
    if pathspec:
        cmd.append("--")
        cmd.extend([p for p in pathspec if p not in ("", ".")])
    try:
        out = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=180)
    except Exception as e:
        return None, "git ls-files --ignored failed in %s: %s" % (cwd, e)
    if out.returncode != 0:
        return None, "git ls-files --ignored rc=%d in %s: %s" % (
            out.returncode, cwd, (out.stderr or "").strip()[:160])
    return [prefix + p for p in out.stdout.split("\0") if p], None


def out_of_corpus_count(ws: str, pathspec):
    """HIDDEN-FILE TRACKING. How many files sit in this scope that the DEFAULT corpus cannot see?

    This is the instrument for the trap the build spec named: a comp-find zero whose denominator
    reads `across 0 file(s)` is OUT OF CORPUS, not absence -- and until now nothing in the tool
    could tell those two apart. A zero over a scope holding N ignored files is a DIFFERENT claim
    from a zero over a scope holding none, and the caller must be told which one they have.

    Returns (searchable, ephemeral, err). `searchable` = ignored files a --corpus all WOULD read;
    `ephemeral` = the declared noise floor, reported separately so the number is never a mystery.
    On any error returns (None, None, msg) -- the caller prints UNKNOWN and NEVER prints a zero,
    because a failed count and a true zero are the same value and must not render the same way.
    """
    ig, err = _ls_ignored(ws, pathspec)
    if ig is None:
        return None, None, err
    eph = sum(1 for f in ig if _is_ephemeral(f))
    return len(ig) - eph, eph, None


def gitignore_aware_files(ws: str, pathspec, include_held: bool = False,
                          corpus: str = "default", stats: dict = None):
    """The .gitignore-aware working set across the parent repo AND nested git repos (portal etc.),
    pathspec-filtered, with the section-8 sovereign-held trees EXCLUDED BY DEFAULT (GG1).

    `corpus` selects the POPULATION (Andrew-direct 2026-08-27):
      default  tracked + untracked-not-ignored          (unchanged; what every caller had)
      all      default + ignored MINUS the ephemeral floor
      ignored  ONLY the ignored set minus the floor     (targeted "is it in the hidden files?")
      raw      default + ALL ignored, floor disabled    (the honest, slow, everything sweep)

    Returns (files, held_note, err):
      * err       -- non-None ONLY on a hard git failure -> callers surface it LOUD (never read
                     absence as 'no matches'). On err, files is None.
      * held_note -- non-None when the sovereign-held guard acted: a LOUD line the caller MUST
                     print, so an excluded held path is never mistaken for 'confirmed absent' and
                     an --include-held override is never silent. None when no held path was involved.
      * files     -- the working set MINUS held prefixes (unless include_held)."""
    if corpus not in CORPUS_MODES:
        return None, None, "unknown corpus mode %r (valid: %s)" % (corpus, ", ".join(CORPUS_MODES))
    # THE FLOOR MUST BE COUNTED WHEREVER IT ACTS, NOT ONLY IN --hidden. Measured 2026-08-27, and it
    # was MY defect in the commit that declared "the floor is PRINTED, never silent": `--corpus
    # ignored .runtmp` returned `0 hit(s) across 0 file(s)` over a scope holding 326,639 gitignored
    # files, every one of them floor-excluded and NONE of them mentioned. That is the precise string
    # Rule 21 teaches means OUT-OF-CORPUS -- emitted for a population the caller had just been told
    # this mode covers. A floor that is printed in one verb and silent in the search path is not a
    # printed floor. `stats` carries the count out so the caller can name it on the denominator.
    if stats is not None:
        stats["floor"] = 0
    if corpus == "ignored":
        parent, err = _ls_ignored(ws, pathspec)
        if parent is None:
            return None, None, err
        kept = [f for f in parent if not _is_ephemeral(f)]
        if stats is not None:
            stats["floor"] = len(parent) - len(kept)
        parent = kept
    else:
        parent, err = _ls_files(ws)
        if parent is None:
            return None, None, err
        if corpus in ("all", "raw"):
            ig, ierr = _ls_ignored(ws, pathspec)
            # A FAILED IGNORED ENUMERATION IS A HARD ERROR HERE, NOT A DEGRADED SEARCH. Falling
            # back to the default corpus would answer a --corpus all question with a default-corpus
            # population and print `all` beside it -- a wrong denominator wearing the right label,
            # which is worse than no answer.
            if ig is None:
                return None, None, ierr
            if corpus == "all":
                kept_ig = [f for f in ig if not _is_ephemeral(f)]
                if stats is not None:
                    stats["floor"] = len(ig) - len(kept_ig)
                ig = kept_ig
            seen = set(_norm(f) for f in parent)
            parent = parent + [f for f in ig if _norm(f) not in seen]
    _inc, _exc = _split_pathspec(pathspec)
    nested = _gitlinks(ws)
    nested_set = set(_norm(n) for n in nested)
    # drop the bare gitlink pointer entries from the parent set (they are not files)
    files = [f for f in parent if _norm(f) not in nested_set]
    for r in nested:
        if _inc and not any(_touches(r, ps) for ps in _inc):
            continue
        if any(_under(r, ps) for ps in _exc):
            continue
        rdir = os.path.join(ws, r)
        if not os.path.exists(os.path.join(rdir, ".git")):
            continue  # gitlink whose worktree is absent/uninitialized -> skip quietly
        # THE NESTED REPO GETS THE SAME CORPUS AS THE PARENT. A --corpus all that widened the
        # parent but left portal on the default set would report `corpus=all` over a population
        # that is only partly `all` -- the nested-repo half of the very bug this module's header
        # says it exists to prevent (a naive enumeration silently missing all 1000+ portal files).
        # pathspec is NOT pushed down: it is parent-relative, and the _under filter below is what
        # scopes nested paths -- same contract _ls_files has always had here.
        sub = []
        if corpus != "ignored":
            sub, _serr = _ls_files(rdir, _norm(r) + "/")
            sub = sub or []
        if corpus in ("all", "raw", "ignored"):
            sig, _ierr = _ls_ignored(rdir, None, _norm(r) + "/")
            if sig:
                if corpus != "raw":
                    sig = [f for f in sig if not _is_ephemeral(f)]
                have = set(_norm(f) for f in sub)
                sub += [f for f in sig if _norm(f) not in have]
        if sub:
            files += sub
    if pathspec:
        files = [f for f in files if (not _inc or any(_under(f, ps) for ps in _inc))
                 and not any(_under(f, ps) for ps in _exc)]
    # sovereign-held guard (string-prefix on the path list -- never opens a held file)
    held = [f for f in files if _is_held(f)]
    if include_held:
        note = (("WARN: OVERRIDE --include-held -- searching %d sovereign-HELD path(s) "
                 "(sovereign hold bypassed; audited)." % len(held)) if held else None)
        return files, note, None
    if held:
        files = [f for f in files if not _is_held(f)]
        if _names_held(pathspec):
            note = ("WARN: %d sovereign-HELD path(s) matched your pathspec but were NOT searched "
                    "(sovereign hold) -- NOT confirmed absent. Pass --include-held to search them."
                    % len(held))
        else:
            note = ("note: %d sovereign-held path(s) EXCLUDED from the working set (sovereign hold) "
                    "-- NOT searched, not confirmed absent; --include-held to search them." % len(held))
        return files, note, None
    return files, None, None
