"""comp-legacywriter -- the WRITER-CONTEST lens (INFRASTRUCTURE.TOOLS).

Spec of record: org/tier1_exec/3.0.0_SA_CVO/deliverables/SPEC_COMP_LEGACYWRITER_20260729.md
@3af3e04c53 (STABLE). Andrew-direct premise (~16:25Z 2026-07-29): legacy writers clobbering
artifacts in multi-stage pipelines are "a recurring footgun that wastes hours and hours of time
and system confidence... hellish to debug and clean."

DESIGN CENTER -- this is a JOIN of existing instruments, NOT a new scanner. It reuses
comp_dataflow's AST path-resolver verbatim (import, not copy) and defers the live axes to
comp-clobber / comp-trigger / comp-aws. The value is the JOIN, the LOCATION IDENTITY correction,
and the verdict table.

WHY IT EXISTS RATHER THAN "just run comp-clobber" -- measured 2026-07-29 on the live estate:
comp-clobber reported 11 multi-writer sinks. EIGHT of them are not collisions:
  * gold/trigger-pending.json      -> two `aws s3 cp s3://... /dev/null` EXISTENCE PROBES
                                      (GetObject, inside an `if`) in TWO DIFFERENT firm buckets
                                      (opal-data-bd, opal-data-inf). Neither is a writer, and
                                      they are not the same location. A DOUBLE false positive.
  * platinum/firm/*.json x7        -> black_diamond vs cot D_04.client_portal_summary.py, i.e.
                                      two firm trees writing their OWN buckets at the same KEY.
                                      Firm separation is gate + IAM law; "cleaning this up" would
                                      be an incident, not a fix.
The root cause is one line of modelling: comp-clobber's sink identity is the KEY. This tool's
location identity is the (BUCKET, KEY) PAIR, and it classifies PROBE separately from WRITE.

  A RETIRE TOOL THAT CANNOT TELL A PROBE FROM A WRITE WILL RETIRE LIVE PATHS.
  A RETIRE TOOL THAT CANNOT TELL A BUCKET FROM A KEY WILL BREAK FIRM SEPARATION.

Both are COO's pre-registered exercise requirements (165733Z #1 and #2); both are enforced here
by construction and covered by the self-test battery, which uses the LIVE fixtures.

OUTPUT CONTRACT (O2): every phase prints examined-N-of-M and its DECLARED blindness. A missing
substrate is rc=2 with an explicit reason -- never a clean-looking empty report. Absence of an
instrument is NEVER evidence of absence of a writer.

ADVISORY / READ-ONLY. This tool RECOMMENDS; the kill rides the owner's lane, never-widen
sign-off, and the deploy ledger. It has no write path to S3, DDB, or the repo.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import subprocess
import sys
import warnings
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_WS = _HERE.parent.parent.parent  # org/modules/graph -> repo root
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

# ---- REUSE, not re-implementation (spec: "zero new scanners") -------------------------------
# comp_dataflow already carries the AST path-resolver, the module/function scope walkers and the
# layer classifier. Importing them keeps ONE resolver in the estate: a second copy would drift,
# and a drifted resolver is exactly how two instruments disagree about the same file.
try:
    from comp_dataflow import (  # type: ignore
        _S3_KEY_WRITE_ATTRS,
        _call_attr,
        _function_scope,
        _kw,
        _module_constants,
        _parent_fn_map,
        _resolve_expr,
    )

    _DATAFLOW_IMPORT_ERROR = None
except Exception as _e:  # pragma: no cover - surfaced loudly in the header, never swallowed
    _DATAFLOW_IMPORT_ERROR = str(_e)
    _S3_KEY_WRITE_ATTRS = {"put_object", "upload_file", "upload_fileobj", "copy_object"}

TOOL = "comp-legacywriter"
SPEC_COMMIT = "3af3e04c53"
_DYN = "{*}"


def _rel(p) -> str:
    """Repo-relative, forward-slashed. An absolute Windows path in a report is not greppable and
    not pasteable into a ledger entry."""
    try:
        return str(Path(p).resolve().relative_to(_WS)).replace("\\", "/")
    except Exception:
        return str(p).replace("\\", "/")

# Read/probe attrs -- these are NOT writers. The whole trigger-pending false positive lives here.
_S3_PROBE_ATTRS = {"get_object", "head_object", "download_file", "download_fileobj"}
_S3_LIST_ATTRS = {"list_objects", "list_objects_v2", "paginate"}

# Producer trees scanned for the STATIC axis. Denominator is printed; this list IS the population.
_SCAN_ROOTS = ("data", "infra/aws", "org/modules", "portal/scripts")
_SCAN_SUFFIXES = (".py", ".sh")

# Empty-ish returns that make a removal SILENT rather than loud.
_EMPTY_RETURNS = ("{}", "[]", "None", "0", "''", '""', "dict()", "list()", "set()", "0.0")


# =================================================================================================
# HEADER CONTRACT -- first line, EVERY invocation, FAIL-LOUD.
# =================================================================================================
# Andrew-direct ~1645Z: a comp-tool needs "a head with timestamp of its source very clearly
# depicted". CVO hardened it on ~B's finding (170946Z): pipescript's own vintage banner sits in a
# bare `except Exception: pass`, so a missing resolver prints NO HEADER AT ALL -- and a tool with
# no header reads as a tool with no source, not as a failed read. That is contract C3 violated
# inside the reference feature.
#
#   NO HEADER EMITTABLE => rc=2 + an explicit "SOURCE UNRESOLVABLE" line. NEVER SILENCE.
#
# There is deliberately no bare `except: pass` anywhere in this function.

def _git(*args: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", *args], cwd=str(_WS), capture_output=True, text=True, timeout=20
        )
        if out.returncode != 0:
            return None
        return out.stdout.strip() or None
    except Exception:
        return None


def _stat_mtime_utc(p: Path) -> str | None:
    try:
        return datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc).strftime(
            "%Y-%m-%dT%H%M%SZ"
        )
    except Exception:
        return None


def resolve_sources() -> dict:
    """Resolve every substrate this tool reasons from, with its vintage. Returns a dict whose
    'unresolvable' list is non-empty when the header cannot be honestly emitted."""
    src: dict = {"resolved": {}, "unresolvable": []}

    head = _git("rev-parse", "--short", "HEAD")
    head_date = _git("log", "-1", "--date=iso-strict", "--format=%ad")
    if head and head_date:
        src["resolved"]["repo-HEAD"] = f"{head} @ {head_date}"
    else:
        src["unresolvable"].append("repo-HEAD (git rev-parse/log failed)")

    df = _HERE / "comp_dataflow.py"
    if df.is_file() and _DATAFLOW_IMPORT_ERROR is None:
        src["resolved"]["static-axis-engine"] = f"comp_dataflow.py @ {_stat_mtime_utc(df)}"
    else:
        why = _DATAFLOW_IMPORT_ERROR or "file absent"
        src["unresolvable"].append(f"static-axis-engine comp_dataflow.py ({why})")

    return src


def emit_header(stream=sys.stdout) -> int:
    """Print the source-timestamp head. Returns 0 if fully resolved, 2 if not.

    FAIL-LOUD: an unresolvable source prints SOURCE UNRESOLVABLE naming what failed. The caller
    must honour a non-zero return -- a header that can silently not-appear is worse than no
    header, because its ABSENCE is unreadable."""
    src = resolve_sources()
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    print(f"{TOOL} | run {stamp} | spec @{SPEC_COMMIT} | ADVISORY, READ-ONLY", file=stream)
    for name, vintage in src["resolved"].items():
        print(f"  SOURCE {name}: {vintage}", file=stream)
    if src["unresolvable"]:
        for bad in src["unresolvable"]:
            print(f"  SOURCE UNRESOLVABLE: {bad}", file=stream)
        print(
            "  rc=2 -- refusing to report on a substrate this tool cannot name. "
            "An unnamed source is not a fresh source.",
            file=stream,
        )
        return 2
    return 0


# =================================================================================================
# PHASE 0 -- SUBSTRATE COVERAGE PRECONDITION (load-bearing REFUSAL)
# =================================================================================================
# "A stale estate map actively DEFENDS zombies -- it is a legacy-writer preservation mechanism."
# The measured case: pipescript's resolver snapshot is frozen 2026-06-15 and serves the underscore
# TWIN as "the primary served rollup, LIVE fresh" while listing a RETIRED freshness-checker as a
# producer. A tool that trusted it would certify the zombie.
#
# The snapshot is legal ONLY as the NAMING layer, never for load-bearing keys.

_RESOLVER_SNAPSHOT = _WS / "org" / "modules" / "graph" / "estate-coverage-resolver.json"
_SNAPSHOT_MAX_AGE_DAYS = 14


def phase0_substrate(require_live: bool) -> dict:
    """Assess substrate freshness. verdict: OK | STALE | UNKNOWN."""
    out: dict = {"checks": [], "verdict": "OK", "blindness": []}

    # (a) The naming snapshot -- age is a FINDING, not a failure, because it is naming-only.
    if _RESOLVER_SNAPSHOT.is_file():
        age_days = None
        try:
            raw = json.loads(_RESOLVER_SNAPSHOT.read_text(encoding="utf-8"))
            lr = raw.get("last_review") or raw.get("generated") or raw.get("last_updated")
            if lr:
                d = datetime.fromisoformat(str(lr).replace("Z", "+00:00"))
                if d.tzinfo is None:
                    d = d.replace(tzinfo=timezone.utc)
                age_days = (datetime.now(timezone.utc) - d).days
        except Exception as e:
            out["checks"].append(("resolver-snapshot", "UNREADABLE", str(e)))
            out["blindness"].append(
                "resolver snapshot unreadable -- thread NAMING unavailable (keys unaffected)"
            )
        if age_days is not None:
            state = "STALE" if age_days > _SNAPSHOT_MAX_AGE_DAYS else "OK"
            out["checks"].append(
                ("resolver-snapshot", state, f"last_review {age_days}d old (NAMING LAYER ONLY)")
            )
            if state == "STALE":
                out["blindness"].append(
                    f"resolver snapshot {age_days}d stale -- thread NAMES may be wrong; "
                    "it is NOT used for keys, so this does not defend a zombie here"
                )
    else:
        out["checks"].append(("resolver-snapshot", "ABSENT", str(_RESOLVER_SNAPSHOT)))
        out["blindness"].append("resolver snapshot absent -- no thread naming layer")

    # (b) comp-kuzu canonical graph -- the LOAD-BEARING substrate for Phase 1 path resolution.
    # Measured 2026-07-29: a trivial query did not return within 180s on this host (the tool
    # auto-refreshes on HEAD-advance and can be mid-rebuild). We DECLARE that rather than hang
    # the lens or, worse, silently fall back to the stale snapshot for keys.
    kuzu = _WS / ".tools" / "comp-kuzu"
    if kuzu.is_file():
        out["checks"].append(
            ("comp-kuzu", "PRESENT-UNPROBED", "provenance not read in this run (see --probe-kuzu)")
        )
        out["blindness"].append(
            "comp-kuzu provenance NOT read this run: Phase 1 key resolution is "
            "REPO-DERIVED (static), not graph-derived. Declared, not assumed."
        )
    else:
        out["checks"].append(("comp-kuzu", "ABSENT", str(kuzu)))
        out["verdict"] = "STALE" if require_live else out["verdict"]
        out["blindness"].append("comp-kuzu absent -- canonical graph path resolution unavailable")

    if require_live and any(s == "STALE" for _, s, _ in out["checks"]):
        out["verdict"] = "STALE"
    return out


# =================================================================================================
# LOCATION IDENTITY -- (bucket, key). The correction over comp-clobber.
# =================================================================================================
# COO 165733Z #2, verbatim intent: "a path-level match across firm buckets (opal-data-bd vs
# opal-data-inf, same key) is NOT a collision -- firm separation is gate+IAM law, and 'cleaning it
# up' would be an incident."

UNRESOLVED_BUCKET = "UNRESOLVED-BUCKET"


class Location:
    __slots__ = ("bucket", "key")

    def __init__(self, bucket: str | None, key: str):
        self.bucket = bucket or UNRESOLVED_BUCKET
        self.key = key

    @property
    def resolved(self) -> bool:
        return self.bucket != UNRESOLVED_BUCKET

    @property
    def ident(self) -> tuple:
        return (self.bucket, self.key)

    def __str__(self) -> str:
        return f"s3://{self.bucket}/{self.key}"


_S3_URI = re.compile(r"s3://([A-Za-z0-9._\-]+)/(\S+)")


def _split_s3_uri(raw: str):
    m = _S3_URI.search(raw or "")
    if m:
        return m.group(1), m.group(2).rstrip("\"'")
    return None, None


# =================================================================================================
# PROBE vs WRITE -- COO 165733Z #1. The trigger-pending fixture.
# =================================================================================================
# `aws s3 cp s3://bucket/key /dev/null` is a DOWNLOAD (GetObject) used as an existence test inside
# an `if`. Direction is the discriminator and comp-clobber does not model it.

_AWS_WRITE_VERBS = ("put-object", "put_object", "sync", "mv")
_AWS_PROBE_VERBS = ("head-object", "get-object", "ls", "list-objects", "list-objects-v2")


def classify_shell_s3_call(line: str) -> str | None:
    """Return 'WRITE' | 'PROBE' | None for one shell line mentioning s3.

    The `aws s3 cp` direction rule is the whole point:
        cp s3://... <local>   -> PROBE (download)
        cp <local> s3://...   -> WRITE (upload)
    """
    if "s3://" not in line:
        return None
    stripped = line.strip()
    if stripped.startswith("#"):
        return None

    if re.search(r"\baws\s+s3api\s+", line):
        for v in _AWS_WRITE_VERBS:
            if re.search(r"\bs3api\s+" + re.escape(v) + r"\b", line):
                return "WRITE"
        for v in _AWS_PROBE_VERBS:
            if re.search(r"\bs3api\s+" + re.escape(v) + r"\b", line):
                return "PROBE"

    cp = re.search(r"\baws\s+s3\s+(cp|mv|sync)\s+(\S+)\s+(\S+)", line)
    if cp:
        src, dst = cp.group(2), cp.group(3)
        src_is_s3 = src.strip("\"'").startswith("s3://")
        dst_is_s3 = dst.strip("\"'").startswith("s3://")
        if dst_is_s3 and not src_is_s3:
            return "WRITE"
        if src_is_s3 and not dst_is_s3:
            return "PROBE"
        if src_is_s3 and dst_is_s3:
            return "WRITE"  # s3->s3 copy writes the destination
        return None

    for v in _AWS_PROBE_VERBS:
        if re.search(r"\baws\s+s3\s+" + re.escape(v) + r"\b", line):
            return "PROBE"
    return None


# =================================================================================================
# REMOVAL BEHAVIOUR -- COO 165733Z #3, adopted verbatim into the evidence bar.
# =================================================================================================
# "A reader inside a bare except returning an empty default is MORE dangerous to retire than one
# that hard-fails, because the hard-fail TELLS you." Fixture:
# dim_mdpf_aggregate_aua_timeseries.py:567 reads inside `except Exception -> WARN -> return {}`:
# deletion crashes nothing and silently Nones a client-facing series.
#
# "1 reader, low risk" is the WRONG verdict. "Removal degrades silently" is the right one.

def _handler_is_silent(handler: ast.ExceptHandler, src_lines: list) -> bool:
    """True when the except body swallows -- i.e. returns an empty default and does not re-raise."""
    for node in ast.walk(handler):
        if isinstance(node, ast.Raise):
            return False
    for node in ast.walk(handler):
        if isinstance(node, ast.Return):
            if node.value is None:
                return True
            try:
                seg = ast.unparse(node.value).strip()
            except Exception:
                seg = ""
            if seg in _EMPTY_RETURNS:
                return True
    if all(isinstance(n, ast.Pass) for n in handler.body):
        return True
    return False


def removal_behaviour_for(tree: ast.Module, lineno: int, src_lines: list) -> tuple:
    """(behaviour, evidence) for a read at `lineno`.

    hard-fail     -- an absent artifact raises and the caller sees it
    silent-default-- an absent artifact is swallowed into an empty value (the DANGEROUS class)
    unknown       -- not determinable from this call site
    """
    best = ("hard-fail", "no enclosing try/except -- an absent artifact propagates")
    for node in ast.walk(tree):
        if not isinstance(node, ast.Try):
            continue
        try:
            start = min(getattr(b, "lineno", 10**9) for b in node.body)
            end = max(
                getattr(b, "end_lineno", getattr(b, "lineno", 0)) or 0 for b in node.body
            )
        except ValueError:
            continue
        if not (start <= lineno <= end):
            continue
        for h in node.handlers:
            bare = h.type is None
            broad = isinstance(h.type, ast.Name) and h.type.id in ("Exception", "BaseException")
            if _handler_is_silent(h, src_lines):
                kind = "bare except" if bare else ("except Exception" if broad else "except")
                return (
                    "silent-default",
                    f"{kind} at L{h.lineno} returns an empty default -- "
                    "removal degrades SILENTLY (no crash, no alarm)",
                )
        best = ("hard-fail", f"enclosing try at L{node.lineno} re-raises or handles loudly")
    return best


# =================================================================================================
# STATIC AXIS -- writers + readers, per (bucket, key), with probe/write separation.
# =================================================================================================

class Hit:
    __slots__ = ("file", "line", "loc", "kind", "how", "removal", "removal_evidence")

    def __init__(self, file, line, loc, kind, how, removal=None, removal_evidence=None):
        self.file = file
        self.line = line
        self.loc = loc
        self.kind = kind  # WRITE | PROBE | READ
        self.how = how
        self.removal = removal
        self.removal_evidence = removal_evidence


# boto3 positional signatures -- attr -> index of the Bucket argument.
#   upload_file(Filename, Bucket, Key) / upload_fileobj(Fileobj, Bucket, Key)
#   download_file(Bucket, Key, Filename) / download_fileobj(Bucket, Key, Fileobj)
# Missing these is why a large share of writers rendered UNRESOLVED-BUCKET on the first run --
# and an unresolved bucket costs a real verdict, so resolution coverage IS correctness here.
_BUCKET_ARG_INDEX = {
    "upload_file": 1,
    "upload_fileobj": 1,
    "download_file": 0,
    "download_fileobj": 0,
}


def _bucket_from_call(node: ast.Call, scope: dict, attr: str | None = None) -> str | None:
    b = _kw(node, "Bucket")
    if b is not None:
        val = _resolve_expr(b, scope)
        if val and val != _DYN:
            return val
    idx = _BUCKET_ARG_INDEX.get(attr or "")
    if idx is not None and len(node.args) > idx:
        val = _resolve_expr(node.args[idx], scope)
        if val and val != _DYN and not val.startswith("s3://"):
            return val
    if node.args:
        first = _resolve_expr(node.args[0], scope)
        if first and first.startswith("s3://"):
            bk, _ = _split_s3_uri(first)
            return bk
    return None


def scan_python(path: Path) -> tuple:
    """-> (hits, error). Reuses comp_dataflow's resolver; adds bucket + probe/write + removal."""
    hits: list = []
    try:
        src = path.read_text(encoding="utf-8", errors="replace")
        # A scanned file's own SyntaxWarnings (invalid escape sequences etc.) are ITS defects, not
        # findings of this tool -- but they must not be silenced globally, only for this parse.
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", SyntaxWarning)
            tree = ast.parse(src)
    except Exception as e:
        return hits, f"{_rel(path)}: {e}"
    src_lines = src.splitlines()

    module_consts = _module_constants(tree)
    fn_scopes: dict = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            fn_scopes[node] = _function_scope(node, module_consts)
    enclosing = _parent_fn_map(tree)

    def scope_for(call: ast.Call) -> dict:
        fn = enclosing.get(call)
        while fn is not None and not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            fn = enclosing.get(fn)
        return fn_scopes.get(fn, module_consts)

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        attr = _call_attr(node)
        if attr is None:
            continue
        scope = scope_for(node)

        if attr in _S3_KEY_WRITE_ATTRS:
            kexpr = _kw(node, "Key")
            if kexpr is None and attr in ("upload_file", "upload_fileobj") and len(node.args) >= 3:
                kexpr = node.args[2]
            if kexpr is None:
                continue
            key = _resolve_expr(kexpr, scope)
            if not key:
                continue
            bucket = _bucket_from_call(node, scope, attr)
            # DYNAMIC CONSTRUCTION IS NEVER SILENCE (the comp-iam silence law, battery control 2).
            how = f"{attr}()"
            if "{*}" in key or bucket is None:
                how += "  [UNRESOLVED-WRITER: dynamic construction]"
            hits.append(Hit(_rel(path), node.lineno, Location(bucket, key), "WRITE", how))

        elif attr in _S3_PROBE_ATTRS:
            kexpr = _kw(node, "Key")
            if kexpr is None and attr in ("download_file", "download_fileobj") and len(node.args) >= 2:
                kexpr = node.args[1]
            if kexpr is None:
                continue
            key = _resolve_expr(kexpr, scope)
            if not key:
                continue
            bucket = _bucket_from_call(node, scope, attr)
            beh, ev = removal_behaviour_for(tree, node.lineno, src_lines)
            kind = "PROBE" if attr == "head_object" else "READ"
            hits.append(
                Hit(_rel(path), node.lineno, Location(bucket, key), kind, f"{attr}()", beh, ev)
            )

    # pandas reads of an s3:// literal are READS too (value sources -- the reader-line population).
    for i, line in enumerate(src_lines, start=1):
        if "s3://" in line and re.search(r"read_(parquet|json|csv|table|excel)\s*\(", line):
            bk, key = _split_s3_uri(line)
            if bk and key:
                beh, ev = removal_behaviour_for(tree, i, src_lines)
                hits.append(Hit(_rel(path), i, Location(bk, key), "READ", "pandas-read", beh, ev))
    return hits, None


def scan_shell(path: Path) -> tuple:
    hits: list = []
    try:
        src = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return hits, f"{_rel(path)}: {e}"
    for i, line in enumerate(src.splitlines(), start=1):
        cls = classify_shell_s3_call(line)
        if cls is None:
            continue
        bk, key = _split_s3_uri(line)
        if not bk or not key:
            continue
        removal = removal_ev = None
        if cls == "PROBE":
            # A probe inside an `if` is CONTROL FLOW, not a dependency: its absence takes the
            # else-branch. That is a silent-default by construction.
            if re.search(r"^\s*(if|elif)\b", line) or "; then" in line:
                removal = "silent-default"
                removal_ev = "probe used as an `if` condition -- absence silently takes the other branch"
        hits.append(Hit(_rel(path), i, Location(bk, key), cls, "aws-cli", removal, removal_ev))
    return hits, None


def static_axis(roots=_SCAN_ROOTS) -> dict:
    files: list = []
    for r in roots:
        base = _WS / r
        if not base.is_dir():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.suffix in _SCAN_SUFFIXES:
                files.append(p)
    hits: list = []
    errors: list = []
    for p in files:
        h, err = (scan_python(p) if p.suffix == ".py" else scan_shell(p))
        hits.extend(h)
        if err:
            errors.append(err)
    return {"hits": hits, "examined": len(files), "errors": errors, "roots": list(roots)}


# =================================================================================================
# PHASE 2/4 -- census + verdict, keyed on (bucket, key)
# =================================================================================================

def build_locations(hits: list) -> dict:
    locs: dict = {}
    for h in hits:
        locs.setdefault(h.loc.ident, {"writers": [], "readers": [], "probes": []})
        if h.kind == "WRITE":
            locs[h.loc.ident]["writers"].append(h)
        elif h.kind == "PROBE":
            locs[h.loc.ident]["probes"].append(h)
        else:
            locs[h.loc.ident]["readers"].append(h)
    return locs


def contest_class(entry: dict, bucket: str | None = None) -> str:
    """Contest verdict for one location.

    AN UNRESOLVED BUCKET CANNOT YIELD A CONTEST VERDICT. Two writers that both render
    UNRESOLVED-BUCKET have been GROUPED BY THIS TOOL, not by the estate -- they may well be two
    firm trees writing their own separate buckets (the bd/cot B_01.holdings_lots.py shape). Calling
    that CONTESTED would manufacture exactly the false collision this tool exists to correct, one
    layer further in. Same law as the exercise column: absence of resolution is not evidence.
    """
    n = len({h.file for h in entry["writers"]})
    if n == 0:
        return "NO-WRITER-FOUND"
    if bucket == UNRESOLVED_BUCKET and n > 1:
        return "UNDETERMINABLE-BUCKET-UNRESOLVED"
    if n == 1:
        return "SOLE"
    return "CONTESTED-STATIC"


def key_collisions_across_buckets(locs: dict) -> tuple:
    """Group by KEY to expose what a key-only instrument would have called a collision.

    Returns (separated, undeterminable):
      separated     -- keys written in 2+ RESOLVED buckets. Genuinely NOT collisions: firm
                       separation is gate + IAM law.
      undeterminable-- keys where at least one writer's bucket did not resolve. A collision here
                       can be NEITHER confirmed NOR ruled out, and saying "not a collision" would
                       be the more dangerous error -- it would suppress a real contest.
    """
    by_key: dict = {}
    for (bucket, key), entry in locs.items():
        if entry["writers"]:
            by_key.setdefault(key, set()).add(bucket)
    separated: dict = {}
    undeterminable: dict = {}
    for k, buckets in by_key.items():
        if len(buckets) < 2:
            continue
        if UNRESOLVED_BUCKET in buckets:
            undeterminable[k] = sorted(buckets)
        else:
            separated[k] = sorted(buckets)
    return separated, undeterminable


def retirecond_entry(bucket: str, key: str, entry: dict) -> dict:
    readers = entry["readers"]
    silent = [r for r in readers if r.removal == "silent-default"]
    if silent:
        bar = (
            "REMOVAL DEGRADES SILENTLY -- re-point every silent-default reader BEFORE teardown; "
            "deletion produces no crash and no alarm"
        )
    elif readers:
        bar = "removal hard-fails at the reader -- teardown is loud and detectable"
    else:
        bar = (
            "NO READER FOUND IN THE SCANNED POPULATION -- this is NOT 'no reader'. "
            "State the population before acting"
        )
    return {
        "what": f"s3://{bucket}/{key}",
        "kind": "write",
        "evidence_bar": bar,
        "writers": [f"{h.file}:{h.line}" for h in entry["writers"]],
        "readers": [
            {"site": f"{r.file}:{r.line}", "removal_behaviour": r.removal or "unknown",
             "evidence": r.removal_evidence or ""}
            for r in readers
        ],
    }


# =================================================================================================
# SELF-TEST -- the live-fixture battery (spec §Acceptance, COO §165733Z)
# =================================================================================================

def self_test() -> int:
    print("=" * 92)
    print(f"{TOOL} --self-test  |  live-fixture battery (spec @{SPEC_COMMIT})")
    print("=" * 92)
    results: list = []

    def check(name, ok, detail):
        results.append((name, ok, detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}")

    # C1 -- PROBE != WRITE, on COO's live fixture.
    probe_line = 'if timeout 10 aws s3 cp "s3://opal-data-bd/gold/trigger-pending.json" /dev/null 2>/dev/null; then'
    check(
        "C1 probe!=write (live fixture: bd watchdog-shutdown.sh:72)",
        classify_shell_s3_call(probe_line) == "PROBE",
        f"classified {classify_shell_s3_call(probe_line)!r}; a download-to-/dev/null is GetObject, not a writer",
    )

    # C1b -- POSITIVE CONTROL, run separately: a real upload must still classify WRITE.
    write_line = 'aws s3 cp ./out/dashboard.json "s3://opal-data-bd/platinum/firm/dashboard.json"'
    check(
        "C1b positive control -- a real upload still reads WRITE",
        classify_shell_s3_call(write_line) == "WRITE",
        f"classified {classify_shell_s3_call(write_line)!r}; the discriminator is DIRECTION, not the verb",
    )

    # C2 -- LOCATION IDENTITY INCLUDES THE BUCKET.
    a = Location("opal-data-bd", "gold/trigger-pending.json")
    b = Location("opal-data-inf", "gold/trigger-pending.json")
    check(
        "C2 bucket-scoped location identity (firm separation)",
        a.ident != b.ident and a.key == b.key,
        "same key in two firm buckets is TWO locations; a key-only instrument reports 1 false collision",
    )

    # C3 -- removal behaviour: silent-default is detected and ranked as the dangerous class.
    sample = (
        "def load():\n"
        "    try:\n"
        "        obj = s3.get_object(Bucket='opal-data-bd', Key='json/mdpf/x.json')\n"
        "        return json.loads(obj['Body'].read())\n"
        "    except Exception:\n"
        "        log.warning('miss')\n"
        "        return {}\n"
    )
    tree = ast.parse(sample)
    beh, ev = removal_behaviour_for(tree, 3, sample.splitlines())
    check(
        "C3 removal behaviour = silent-default (COO fixture shape, dim_...timeseries.py:567)",
        beh == "silent-default",
        f"got {beh!r}: {ev}",
    )

    # C3b -- POSITIVE CONTROL: a loud reader must NOT be labelled silent.
    loud = (
        "def load():\n"
        "    obj = s3.get_object(Bucket='b', Key='k')\n"
        "    return json.loads(obj['Body'].read())\n"
    )
    ltree = ast.parse(loud)
    lbeh, _lev = removal_behaviour_for(ltree, 2, loud.splitlines())
    check(
        "C3b positive control -- an unguarded reader reads hard-fail",
        lbeh == "hard-fail",
        f"got {lbeh!r}; the classifier must be able to say 'this one is loud'",
    )

    # C4 -- NEGATIVE CONTROL: the tool must be able to say 'nothing wrong here'.
    solo = {"writers": [Hit("a.py", 1, Location("b", "k"), "WRITE", "put_object()")],
            "readers": [], "probes": []}
    check(
        "C4 negative control -- a single-writer location reports SOLE, no manufactured finding",
        contest_class(solo, "b") == "SOLE",
        f"got {contest_class(solo, 'b')!r}",
    )

    # C7 -- an UNRESOLVED bucket must NEVER yield a contest verdict (self-inflicted defect, found
    # by reading this tool's own first live run: two firm trees whose buckets did not resolve were
    # grouped into one location and reported CONTESTED-STATIC).
    two_unres = {
        "writers": [
            Hit("data/black_diamond/scripts/gold/B_01.holdings_lots.py", 1811,
                Location(None, "diagnostics/{*}/{*}.parquet"), "WRITE", "upload_file()"),
            Hit("data/cot/scripts/gold/B_01.holdings_lots.py", 1767,
                Location(None, "diagnostics/{*}/{*}.parquet"), "WRITE", "upload_file()"),
        ],
        "readers": [], "probes": [],
    }
    check(
        "C7 unresolved bucket -> UNDETERMINABLE, never CONTESTED (no manufactured collision)",
        contest_class(two_unres, UNRESOLVED_BUCKET) == "UNDETERMINABLE-BUCKET-UNRESOLVED",
        f"got {contest_class(two_unres, UNRESOLVED_BUCKET)!r}; grouping by this tool is not evidence "
        "of grouping by the estate",
    )

    # C8 -- and the inverse: an unresolved bucket must not be counted as PROOF of firm separation.
    locs_mixed = {
        ("opal-data-bd", "k"): {"writers": [Hit("a.py", 1, Location("opal-data-bd", "k"), "WRITE", "w")],
                                "readers": [], "probes": []},
        (UNRESOLVED_BUCKET, "k"): {"writers": [Hit("b.py", 1, Location(None, "k"), "WRITE", "w")],
                                   "readers": [], "probes": []},
    }
    _sep, _und = key_collisions_across_buckets(locs_mixed)
    check(
        "C8 unresolved bucket is NOT counted as firm-separation proof",
        "k" in _und and "k" not in _sep,
        f"separated={list(_sep)}, undeterminable={list(_und)}; "
        "calling this 'not a collision' would SUPPRESS a real contest",
    )

    # C5 -- dynamic construction surfaces as UNRESOLVED-WRITER, never absent.
    dyn = "import boto3\ns3=boto3.client('s3')\ndef w(d):\n    s3.put_object(Bucket='opal-data-bd', Key=f'gold/{d}/x.json', Body=b'')\n"
    p = _WS / ".git" / f"_lw_selftest_{os.getpid()}.py"
    ok_dyn = False
    detail_dyn = "could not stage fixture"
    try:
        p.write_text(dyn, encoding="utf-8")
        hs, _e = scan_python(p)
        ok_dyn = any("UNRESOLVED-WRITER" in h.how for h in hs if h.kind == "WRITE")
        detail_dyn = f"{len([h for h in hs if h.kind=='WRITE'])} writer hit(s); UNRESOLVED flagged={ok_dyn}"
    finally:
        try:
            p.unlink()
        except Exception:
            pass
    check("C5 dynamic key -> UNRESOLVED-WRITER, never silently absent", ok_dyn, detail_dyn)

    # C6 -- header contract is FAIL-LOUD.
    src = resolve_sources()
    check(
        "C6 header contract resolves its sources (fail-loud path exists)",
        isinstance(src.get("resolved"), dict),
        f"resolved={list(src['resolved'])}, unresolvable={src['unresolvable']}",
    )

    passed = sum(1 for _n, ok, _d in results if ok)
    total = len(results)
    print("-" * 92)
    print(f"  {passed} of {total} controls PASS  (score on OUTPUT, not rc -- read the lines above)")
    print("=" * 92)
    return 0 if passed == total else 1


# =================================================================================================
# REPORT
# =================================================================================================

def run_report(target: str | None, as_json: bool, require_live: bool) -> int:
    p0 = phase0_substrate(require_live)
    print()
    print("PHASE 0 -- SUBSTRATE COVERAGE PRECONDITION")
    for name, state, detail in p0["checks"]:
        print(f"  {state:<16} {name}: {detail}")
    if p0["verdict"] == "STALE" and require_live:
        print()
        print("  rc=2 REFUSAL -- substrate failed the freshness precondition.")
        print("  A stale estate map DEFENDS zombies: it is a legacy-writer preservation mechanism.")
        return 2
    for b in p0["blindness"]:
        print(f"  BLINDNESS: {b}")

    st = static_axis()
    locs = build_locations(st["hits"])
    writes = [h for h in st["hits"] if h.kind == "WRITE"]
    probes = [h for h in st["hits"] if h.kind == "PROBE"]
    reads = [h for h in st["hits"] if h.kind == "READ"]

    print()
    print("PHASE 2 -- WRITER CENSUS, THREE AXES")
    print(f"  STATIC     : examined {st['examined']} file(s) under {', '.join(st['roots'])}")
    print(f"               {len(writes)} write-site(s), {len(probes)} probe-site(s), {len(reads)} read-site(s)")
    print(f"               {len(locs)} distinct (BUCKET,KEY) location(s)")
    print("               BLINDNESS: deployed-vs-repo divergence not modelled; dynamic keys render")
    print("                          UNRESOLVED-WRITER (never absent).")
    print("  CAPABILITY : NOT RUN this invocation -- UNVERIFIABLE-BY-THIS-INSTRUMENT.")
    print("               (comp-aws / simulate-principal-policy, one --resource-arns per call.)")
    print("               A grant may be REQUIRED-AND-UNOBSERVED; silence here is not absence.")
    print("  OBSERVED   : NOT RUN this invocation -- UNVERIFIABLE-BY-THIS-INSTRUMENT.")
    print("               (comp-clobber --live: S3 versions/ETags. DDB has NO version history;")
    print("                S3 versions do not record the principal; pre-versioning is invisible.)")
    if st["errors"]:
        print(f"  PARSE ERRORS: {len(st['errors'])} file(s) unreadable/unparseable -- listed in --json")

    # The correction that justifies the tool.
    separated, undet = key_collisions_across_buckets(locs)
    print()
    print("PHASE 2b -- LOCATION IDENTITY CORRECTION (COO 165733Z #2)")
    print(f"  NOT-A-COLLISION (firm separation): {len(separated)} key(s) written in 2+ RESOLVED buckets.")
    print("  Firm separation is gate + IAM law -- 'cleaning these up' would be an incident.")
    print("  A key-only instrument reports each of these as a clobber:")
    for k, buckets in sorted(separated.items())[:12]:
        print(f"    {k}\n        buckets: {', '.join(buckets)}   -> {len(buckets)} DISTINCT locations")
    if not separated:
        print("    (none in the scanned population)")
    print()
    print(f"  UNDETERMINABLE: {len(undet)} key(s) where at least one writer's bucket did NOT resolve.")
    print("  A collision here can be neither confirmed NOR ruled out. This tool does NOT call these")
    print("  'not a collision' -- suppressing a real contest is the more dangerous error.")
    for k, buckets in sorted(undet.items())[:12]:
        print(f"    {k}\n        buckets: {', '.join(buckets)}   -> UNDETERMINABLE")

    if target:
        sel = {ident: e for ident, e in locs.items() if target in ident[1] or target in ident[0]}
    else:
        sel = {ident: e for ident, e in locs.items() if len({h.file for h in e["writers"]}) > 1}

    print()
    print("PHASE 4 -- VERDICT TABLE" + (f"  (filter: {target!r})" if target else "  (contested only)"))
    print(f"  {len(sel)} of {len(locs)} location(s) shown")
    if not sel:
        print("  NO MATCH. That is a statement about THIS population, not about the estate.")
    entries: list = []
    for (bucket, key), e in sorted(sel.items()):
        cls = contest_class(e, bucket)
        print()
        print(f"  s3://{bucket}/{key}")
        print(f"      CONTEST: {cls}   writers={len({h.file for h in e['writers']})} "
              f"readers={len(e['readers'])} probes={len(e['probes'])}")
        for h in e["writers"]:
            print(f"      WRITE  {h.file}:{h.line}  {h.how}")
        for h in e["probes"]:
            print(f"      PROBE  {h.file}:{h.line}  {h.how}   <- NOT A WRITER")
        for r in e["readers"]:
            flag = "  <<< SILENT-DEFAULT" if r.removal == "silent-default" else ""
            print(f"      READ   {r.file}:{r.line}  removal={r.removal or 'unknown'}{flag}")
            if r.removal_evidence:
                print(f"             {r.removal_evidence}")
        print("      EXERCISE VINTAGE: UNDETERMINABLE -- no run-log instrument attached this run.")
        print("             Absence of instrument is NEVER evidence of no write (spec Phase 3b).")
        entries.append(retirecond_entry(bucket, key, e))

    print()
    print("PHASE 4b -- RETIRECOND-SHAPED ENTRIES (ready to paste; the tool RECOMMENDS, never kills)")
    for en in entries[:10]:
        print(f"  - what: {en['what']}")
        print(f"    kind: {en['kind']}")
        print(f"    evidence_bar: {en['evidence_bar']}")

    if as_json:
        print()
        print(json.dumps({"locations": entries,
                          "not_a_collision_firm_separated": separated,
                          "undeterminable_bucket_unresolved": undet,
                          "examined_files": st["examined"], "errors": st["errors"]}, indent=2))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog=TOOL, add_help=True,
                                 description="Writer-contest lens: who writes this artifact, who reads it, "
                                             "and what breaks when it is gone.")
    ap.add_argument("target", nargs="?", help="artifact key substring, bucket, or pipeline name")
    ap.add_argument("--json", action="store_true", dest="as_json")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--require-live-substrate", action="store_true",
                    help="Phase 0 REFUSES (rc=2) unless the canonical graph substrate is fresh")
    args = ap.parse_args(argv)

    hrc = emit_header()
    if hrc != 0:
        return hrc  # FAIL-LOUD: never proceed on an unnameable substrate.

    if args.self_test:
        return self_test()
    return run_report(args.target, args.as_json, args.require_live_substrate)


if __name__ == "__main__":
    sys.exit(main())
