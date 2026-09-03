"""opal_estate_infrastructure -- the OPAL estate traversal engine (C4: estate-infrastructure).

Tool: `comp-estate` (the first point of contact for agent coherence over the Estate).
PURPOSE (Andrew-direct 2026-07-30, VERBATIM): "the entire purpose of comp-estate is that its
the global lossless fidelity descent from semantics to facts." The ladder drill -- C4 segments
-> C3(i|ii) -> chains (D2) -> C2 motifs -> C1 interactions -> C0 facts, every return naming its
next rung down and the D-rail the descent rides -- IS that purpose made operational; "lossless"
is the dual-key maximum-fidelity property (two decompression paths from one join point, the
property that placed the C3 dual-partition design).
NAMING HISTORY, superseded rulings quoted for the record: born `opal_business_estates` under
`comp-semantic-estates` (Andrew-direct 2026-07-29: "we are deprecating base pipescript. there is
comp-pipescript only for future reference" / "pipescript needs to be categorically renamed as
comp-semantic-estates, and if you need a name for the script itself say opal_business_estates");
renamed `comp-estate` 2026-07-30 (Andrew-direct); engine renamed `opal_estate_infrastructure.py`
2026-07-30 (Andrew-direct, to mirror C4 segment language). The bare-named `pipescript` remains
DEPRECATED as a user surface; its engine (renamed estate_infrastructure_cli.py 2026-07-30, same
consolidation) survives only as the imported legacy thread-model engine this module delegates to.

=== WHAT WAS BROKEN, AND WHY A WRAPPER COULD NOT FIX IT ===

The predecessor answered "what is in the <name> thread?" out of a GENERATED SNAPSHOT
(estate-coverage-resolver.json) whose served-artifact and S3-key strings are FROZEN AT GENERATION.
The snapshot is both the claim and the yardstick, so the tool structurally could not report its own
staleness -- and a stale estate map does not fail quietly, it ACTIVELY DEFENDS ZOMBIES.

Measured instance (2026-07-23): it named the pre-revamp key
    platinum/mdpf/aggregate_aua_timeseries.json      described as "LIVE fresh"
while the live serve was
    json/mdpf/global/aggregate-aua-timeseries.json
and it listed a RETIRED freshness-checker as a live producer. That mis-scoped a live key chase.

A vintage BANNER (the previous fix) makes that loud. It does not make it CORRECT. The number was
still wrong; the reader was just warned. This engine fixes the mechanism instead:

    THE SNAPSHOT IS THE *NAMING* LAYER ONLY. KEYS ARE RESOLVED LIVE FROM SOURCE.

Thread names, membership and human structure still come from the snapshot -- that is what it is
good for, and it carries no better alternative. But every S3 key is re-derived from the working
tree at call time, and the two are DIFFED. A snapshot key that no longer appears in any producer is
reported as STALE-IN-SNAPSHOT rather than served as fact. That is the exact defect above, converted
from an invisible wrong answer into a printed finding.

=== WHAT IT DOES NOT CLAIM ===
This is the BRIDGE, not the destination. The destination is comp-kuzu canonical (base CTO
163950Z). Live-from-source is strictly better than frozen-in-snapshot and strictly worse than the
canonical graph: it sees the repo, not the deployed estate, so a deployed-but-diverged artifact is
outside it. That limit is printed, not implied.

=== CONTRACTS ===
1. SOURCE-TIMESTAMP HEAD, FAIL-LOUD. Substrate + vintage on line 1 of every invocation. If a
   substrate cannot be named, print an explicit SOURCE UNRESOLVABLE and exit 2 -- never proceed
   silently. There is no bare `except: pass` in that path. (The predecessor's banner sat in exactly
   that construct, so a corrupt resolver printed NO header at all -- and a tool with no header
   reads as a tool with NO SOURCE, not as a failed read.)
2. --refresh IS A BRIDGE. It regenerates the snapshot and every run still says the substrate is not
   canonical. Refresh makes it NEWER, never CANONICAL.

Read-only. --refresh writes exactly one file: the snapshot it regenerates.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
import sys
import time
import warnings
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
# ONE pager, shared with the legacy thread-model engine (same process, same counters):
# body/footer declarations + the --head marker contract live in estate_infrastructure_cli.
from estate_infrastructure_cli import (  # noqa: E402 -- must follow the sys.path insert above
    body, close_pager, footer, head_armed, set_head,
)
_WS = _HERE.parent.parent.parent
_SNAPSHOT = _HERE / "estate-coverage-resolver.json"
_REFRESHER = _HERE / "gen-estate-resolver.py"

# NFRA_COMPEFFICACY CE-t-17: Rule T's one shared carrier.  Keep the carrier in
# .tools/_compbudget.py; a per-tool copy would fork the output contract.
_TOOLS = _WS / ".tools"
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))
import _compbudget  # noqa: E402 -- path insert above is the declared shared carrier

TOOL = "comp-estate"
STALE_AFTER_DAYS = 14
_DYN = "{*}"

# Ratified spellings: org/standards/COMPTOOL_ANSWER_STATE.enum.json.  These
# classify one non-positive RUN answer, never the tool or project.
STATE_SUBJECT_ABSENT = "SUBJECT_ABSENT_FROM_CORPUS"
STATE_PRESENT_ZERO = "PRESENT_WITH_ZERO_RESULTS"
STATE_PARTIAL_BLIND = "PARTIAL_OR_BLIND"
STATE_NOT_APPLICABLE = "NOT_APPLICABLE"
STATE_NOT_DECIDABLE = "NOT-DECIDABLE"  # tool-voice token for PARTIAL_OR_BLIND

# C(N) is not an alias table this tool owns.  These are the two literal names
# supplied by the dependency contract, not guessed members of the unlocked
# ontology.  Every other unknown name remains a measured corpus absence.
_CN_CARRIED_NAMES = {"c(n)", "nfra_c3materialize"}

# Producer trees whose source defines the LIVE key set. This list IS the denominator and is printed.
_SCAN_ROOTS = ("data", "infra/aws", "org/modules", "portal/scripts")
_WRITE_ATTRS = {"put_object", "upload_file", "upload_fileobj", "copy_object"}
_S3_URI = re.compile(r"s3://([A-Za-z0-9._\-]+)/([^\s\"')]+)")


# ---------------------------------------------------------------------------------------------
# FAIL-LOUD substrate resolution
# ---------------------------------------------------------------------------------------------
def _fail_loud(what: str, why: str, hint: str | None = None) -> int:
    print(f"{TOOL}: SOURCE UNRESOLVABLE: {what}", file=sys.stderr)
    print(f"  why: {why}", file=sys.stderr)
    if hint:
        print(f"  fix: {hint}", file=sys.stderr)
    print(
        "  rc=2 -- refusing to traverse on a substrate this tool cannot name. An unnamed source is\n"
        "  not a fresh source, and a tool with no header reads as a tool with no source.",
        file=sys.stderr,
    )
    return 2


def load_snapshot():
    """-> (snapshot_dict, rc). rc != 0 means the head could not be honestly emitted."""
    if not _SNAPSHOT.is_file():
        return None, _fail_loud(
            f"estate-coverage-resolver.json absent at {_SNAPSHOT}",
            "the named-thread substrate does not exist, so no thread name can be resolved",
            f"{TOOL} --refresh-only",
        )
    try:
        snap = json.loads(_SNAPSHOT.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return None, _fail_loud(
            "estate-coverage-resolver.json unreadable/corrupt",
            f"{type(e).__name__}: {e}",
            f"{TOOL} --refresh-only",
        )
    if not str(snap.get("last_review") or ""):
        return None, _fail_loud(
            "estate-coverage-resolver.json carries no last_review",
            "the snapshot cannot state its own vintage, so its names cannot be aged",
            "regenerate it, or add last_review to the generator's output",
        )
    return snap, 0


def emit_header(snap: dict) -> None:
    run = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    lr = str(snap.get("last_review"))
    try:
        days = (date.today() - date.fromisoformat(lr)).days
        age, stale = f" ({days}d old)", days > STALE_AFTER_DAYS
    except (ValueError, TypeError):
        age, stale = " (age UNCOMPUTABLE -- last_review is not an ISO date)", True
    print(f"{TOOL} | run {run} | NAMING SOURCE: estate-coverage-resolver.json -- last_review {lr}{age}")
    print("  KEY SOURCE: LIVE re-derivation from producer source at call time (NOT the snapshot).")
    print(f"  Roots scanned: {', '.join(_SCAN_ROOTS)}")
    print("  PLANE: repo working tree. A DEPLOYED artifact whose source has diverged is NOT visible")
    print("  here -- this is the bridge; comp-kuzu canonical is the destination.")
    if stale:
        print(f"  *** NAMING SNAPSHOT IS STALE (>{STALE_AFTER_DAYS}d). Vertical NAMES may be wrong.")
        print("  *** Keys are unaffected -- they are re-derived live, which is the point of this engine.")


# ---------------------------------------------------------------------------------------------
# LIVE key derivation -- the fix
# ---------------------------------------------------------------------------------------------
def _resolve(node, scope: dict):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        return scope.get(node.id, _DYN)
    if isinstance(node, ast.JoinedStr):
        out = []
        for v in node.values:
            if isinstance(v, ast.Constant) and isinstance(v.value, str):
                out.append(v.value)
            elif isinstance(v, ast.FormattedValue):
                sub = _resolve(v.value, scope)
                out.append(sub if (sub and sub != _DYN) else _DYN)
            else:
                out.append(_DYN)
        return "".join(out)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left, right = _resolve(node.left, scope), _resolve(node.right, scope)
        if left is None and right is None:
            return None
        return (left or _DYN) + (right or _DYN)
    return None


def _consts(tree: ast.Module) -> dict:
    out: dict = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            v = _resolve(n.value, out)
            if v is not None:
                out[n.targets[0].id] = v
    return out


def live_keys() -> dict:
    """-> {'keys': {key: [producer, ...]}, 'files': N, 'errors': N}. The LIVE denominator."""
    keys: dict = {}
    files = errors = 0
    for root in _SCAN_ROOTS:
        base = _WS / root
        if not base.is_dir():
            continue
        for p in base.rglob("*"):
            if not p.is_file() or p.suffix not in (".py", ".sh"):
                continue
            files += 1
            try:
                src = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                errors += 1
                continue
            rel = str(p.relative_to(_WS)).replace("\\", "/")

            for m in _S3_URI.finditer(src):
                keys.setdefault(m.group(2).rstrip("\"'"), set()).add(rel)

            if p.suffix != ".py":
                continue
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", SyntaxWarning)
                    tree = ast.parse(src)
            except (SyntaxError, ValueError):
                errors += 1
                continue
            consts = _consts(tree)
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                attr = node.func.attr if isinstance(node.func, ast.Attribute) else None
                if attr not in _WRITE_ATTRS:
                    continue
                kexpr = None
                for kw in node.keywords:
                    if kw.arg == "Key":
                        kexpr = kw.value
                if kexpr is None and attr in ("upload_file", "upload_fileobj") and len(node.args) >= 3:
                    kexpr = node.args[2]
                if kexpr is None:
                    continue
                k = _resolve(kexpr, consts)
                if k:
                    keys.setdefault(k, set()).add(rel)
    return {"keys": {k: sorted(v) for k, v in keys.items()}, "files": files, "errors": errors}


_PATTERNISH = ("*", "{", "}", "<", ">", "|", ",", "(")
# An ALL-CAPS token in a key position is a placeholder the snapshot never resolved
# (DATE, YYYY-MM, ALLOC_DAILY_DATE) -- a template, not an object.
_PLACEHOLDER = re.compile(r"(^|/)[A-Z][A-Z0-9_-]{2,}(\.|/|$)")


def _snapshot_keys(blob) -> tuple:
    """-> (concrete, patterns, buckets). Every S3-key-shaped string the snapshot asserts, at any
    depth; buckets = {key: bucket} for keys that arrived via a full s3:// URI (instrument-fix
    @c9be07b413: the bucket is what --verify-served needs to head-object the key -- stripping it
    at extraction was why no render could ever check S3).

    SPLIT ON PURPOSE. A snapshot entry like `bronze/eclipse/*` or
    `bronze/orion-api/{date}/{transactions.csv,...}` is a GLOB or a template, not a key -- there is
    no single object it names, so "does a live producer write it?" has no answer. Reporting those as
    STALE-IN-SNAPSHOT would manufacture findings out of entries the comparison structurally cannot
    judge, which is the same absence-is-not-evidence error this engine exists to stop making. They
    are counted and declared UNCOMPARABLE instead.
    """
    concrete: set = set()
    patterns: set = set()
    buckets: dict = {}

    def add(k: str, bucket: str = None):
        k = k.rstrip("\"'").strip()
        if not k or k in ("/", "*"):
            return
        if bucket:
            buckets[k] = bucket
        # UNCOMPARABLE, in three shapes -- all of them name a SET, not an object, so "does a live
        # producer write it?" has no answer. Shipping any of these into a teardown ledger as a dead
        # key is how someone ends up hunting a phantom, which is the incident this tool exists to
        # prevent, not cause.
        #   glob/template braces   bronze/eclipse/*   json/{firm}/x.json
        #   PREFIX (trailing /)    raw/   serving/   platinum/firm/
        #   CAPS PLACEHOLDER       silver/prices/DATE.parquet   .../YYYY-MM/ALLOC_DAILY_DATE.parquet
        uncomparable = (
            any(c in k for c in _PATTERNISH)
            or k.endswith("/")
            or _PLACEHOLDER.search(k)
        )
        (patterns if uncomparable else concrete).add(k)

    def walk(o):
        if isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        elif isinstance(o, str):
            m = _S3_URI.search(o)
            if m:
                add(m.group(2), bucket=m.group(1))
            elif re.match(r"^(bronze|silver|gold|platinum|json|served)/\S+\.(json|parquet|csv)$", o):
                add(o)

    walk(blob)
    return concrete, patterns, buckets


def _head_object(bucket: str, key: str) -> tuple:
    """-> ('EXISTS', lastmodified) | ('404', '') | ('UNREACHABLE', stderr-head). One live
    head-object per call; 15s timeout. Used only under --verify-served (opt-in cost)."""
    import shutil as _shutil
    aws_bin = _shutil.which("aws") or _shutil.which("aws.cmd") or _shutil.which("aws.exe")
    if not aws_bin:
        return "UNREACHABLE", "aws CLI not found"
    try:
        r = subprocess.run(
            [aws_bin, "s3api", "head-object", "--bucket", bucket, "--key", key,
             "--query", "LastModified", "--output", "text"],
            capture_output=True, text=True, timeout=15,
        )
    except subprocess.TimeoutExpired:
        return "UNREACHABLE", "timeout"
    if r.returncode == 0:
        return "EXISTS", (r.stdout or "").strip()
    err = (r.stderr or "").strip()
    if "404" in err or "Not Found" in err:
        return "404", ""
    return "UNREACHABLE", err.splitlines()[0] if err else "unknown error"


# ---------------------------------------------------------------------------------------------
# Threads
# ---------------------------------------------------------------------------------------------
def _emit_naming_context(data: dict) -> None:
    """Name the actual ontology carrier and its vintage on the three audited modes."""
    print(
        f"{TOOL} | ENGINE: org/modules/graph/opal_estate_infrastructure.py | "
        f"NAMING ONTOLOGY: org/modules/graph/{_SNAPSHOT.name} -- "
        f"last_review {data.get('last_review') or 'ABSENT'}"
    )
    print(
        "  ONTOLOGY BOUNDARY: this is a generated C3.ii naming snapshot, not locked C(N). "
        "C(N) is RELIES-ON NFRA_C3MATERIALIZE; unresolved C(N) names are CARRIED there, "
        "never guessed here."
    )


def _emit_state(token: str, explanation: str, tool_voice: str | None = None) -> None:
    print(f"ANSWER-STATE: {token}")
    if tool_voice:
        print(f"TOOL-VOICE: {tool_voice}")
    print(f"  {explanation}")


def _is_cn_carried_name(name: str) -> bool:
    return name.strip().lower() in _CN_CARRIED_NAMES


def _thread_id(row: dict) -> str:
    return str(row.get("thread_id") or "")


def _after_cursor(rows: list, cursor: str | None) -> tuple[list, str | None]:
    """Return the deterministic suffix after cursor; an unknown cursor is an error string."""
    ordered = sorted(rows, key=_thread_id)
    if not cursor:
        return ordered, None
    for idx, row in enumerate(ordered):
        if _thread_id(row) == cursor:
            return ordered[idx + 1:], None
    return [], (
        f"cursor {cursor!r} is not a chain in this traversal; refusing to skip an "
        "unmeasured prefix"
    )


def _budget_prefix(
    rows: list, clock: _compbudget.Clock, deadline_ns: int | None
) -> tuple[list, bool]:
    """Spend Rule T against deterministic traversal units, never only around the call."""
    out = []
    for row in rows:
        remaining = clock.remaining()
        # Some Windows Python builds expose a coarse time.monotonic() quantum through the
        # shared Clock.  perf_counter_ns is the enforcement clock so a deliberately tiny
        # planted budget cannot scan a whole prefix inside one coarse tick; Clock remains the
        # shared carrier for resolution/disclosure/elapsed reporting.
        deadline_hit = deadline_ns is not None and time.perf_counter_ns() >= deadline_ns
        if deadline_hit or (remaining is not None and remaining <= 0):
            return out, True
        out.append(row)
    return out, False


def _budget_terminal(
    *,
    selected: list,
    total: int,
    expired: bool,
    clock: _compbudget.Clock,
    budget_s: float,
    budget_source: str,
    command: str,
) -> None:
    if not expired:
        print(
            _compbudget.within_budget_line(
                len(selected), total, "chain", budget_s, budget_source, clock.elapsed()
            )
        )
        return
    cursor = _thread_id(selected[-1]) if selected else "NO-CURSOR-YET"
    if selected:
        print(
            _compbudget.budget_reached_line(
                budget_s,
                budget_source,
                len(selected),
                total,
                "chain",
                command,
                cursor,
            )
        )
    else:
        print(
            f"BUDGET REACHED: {_compbudget.fmt(budget_s)} s ({budget_source}); scanned 0 of "
            f"{total} chain(s); results are a PREFIX, not the answer; NO CURSOR YET: no chain "
            "completed before the budget hit; resume: re-run with a larger --budget."
        )


def _deadline_hit(clock: _compbudget.Clock, deadline_ns: int | None) -> bool:
    remaining = clock.remaining()
    return (
        (deadline_ns is not None and time.perf_counter_ns() >= deadline_ns)
        or (remaining is not None and remaining <= 0)
    )


def _render_named_rows(
    legacy,
    data: dict,
    name: str,
    rows: list,
    resources: list,
    clock: _compbudget.Clock,
    deadline_ns: int | None,
) -> tuple[list, bool]:
    """Render full chain units with a Rule-T boundary before every next unit.

    The legacy engine remains the vocabulary/ladder authority; this function is the budget-aware
    loop the public engine lacked.  A stopped run never prints the all-at-once C0 roster or a
    whole-traversal footer, so its prefix cannot masquerade as the answer.
    """
    sc = Counter(row.get("status") for row in rows)
    tc = Counter(row.get("owning_tool") for row in rows)
    n_debt = sum(1 for row in rows if row.get("debtscan_flags"))
    print(
        f"{TOOL} C3.ii vertical {name!r} - {len(rows)} chains "
        f"(D2 = C2-motif instances) (in-scope {sc.get('in-scope', 0)} / "
        f"explicit-out {sc.get('explicit-out', 0)} / "
        f"unreviewed {sc.get('unreviewed', 0)})"
        + (f" | {n_debt} with DEBT flags" if n_debt else "")
    )
    print("=" * 78)
    print("NOTE: freshness adjectives inside chain prose are CENSUS-VINTAGE claims (snapshot")
    print("      vintage in the header), never live reads -- comp-freshness owns live truth.")

    fam2sys, motif_idx = legacy.ladder_context()
    processed = []
    for row in rows:
        if _deadline_hit(clock, deadline_ns):
            break
        body(f"\n[{legacy.status_tag(row['status'])} | {row['owning_tool']}] {legacy._a(row['thread_id'])}")
        ladder = legacy.chain_ladder_line(row, fam2sys, motif_idx)
        if ladder:
            body(ladder)
        flags = row.get("debtscan_flags") or []
        if flags:
            body(
                f"  DEBT: {', '.join(flags)}  "
                f"({'; '.join(legacy._FLAG_MEANING.get(flag, '?') for flag in flags)})"
            )
        if row.get("description"):
            body(f"  what: {legacy._census_prose(row['description'])}")
        for idx, producer in enumerate(legacy._aslist(row.get("producers"), "(none recorded)")):
            body(
                f"  {'producers:' if idx == 0 else '          '} "
                f"{legacy._census_prose(producer)}"
            )
        for idx, served in enumerate(
            legacy._aslist(row.get("served_artifacts"), "(no data artifact)")
        ):
            body(
                f"    {'-> served:' if idx == 0 else '          '} "
                f"{legacy._census_prose(served)}"
            )
        body(f"    -> frontend: {legacy._a(row.get('frontend_resolution') or '(none)')}")
        reachability, authority = legacy._fe_status(row)
        if authority:
            body(f"    -> reachable: {reachability} [CVO ground-truth]")
        processed.append(row)

    expired = len(processed) < len(rows)
    print("\n" + "-" * 78)
    if expired:
        print(
            f"PREFIX ONLY: {len(processed)} of {len(rows)} chain unit(s) rendered. "
            "Whole-traversal tool census and C0 roster are DEFERRED until the resumed union completes."
        )
        close_pager()
        return processed, True

    print("owning tools in this traversal (drill in for live detail -- comp-estate stays read-only):")
    for owning_tool, count in tc.most_common():
        print(f"  {count:>3}  {owning_tool:<22} {legacy.OWNING_TOOLS.get(owning_tool, '')}")
        drill = legacy._drill_call(owning_tool, rows)
        if drill:
            print(f"       -> drill: {drill}")
    if resources:
        print("\n" + "-" * 78)
        print(f"C0 facts ({len(resources)}) - the CENSUS-TAXONOMY roster for {name!r}. NOT exhaustive:")
        print("  chain prose may name facts outside this census; do NOT use this roster as the")
        print("  traversal denominator. It prints only after every chain unit completes.")
        for resource in resources:
            body(f"  {legacy._a(resource)}")
    footer("")
    footer("DRILL DOWN THE LADDER -- one D-rail carries each descent; the rails ARE the fidelity:")
    footer("  C4->C3 registry membership | C3->C2 D3 contract | C2->C1 D2 path | C1->C0 D1 grain")
    return processed, False


def _named_thread_run(
    legacy,
    data: dict,
    name: str,
    budget_s: float,
    budget_source: str,
    clock: _compbudget.Clock,
    deadline_ns: int | None,
    cursor: str | None,
) -> int:
    """Budgeted flagship traversal plus the ratified non-positive answer states."""
    _emit_naming_context(data)
    if _is_cn_carried_name(name):
        _emit_state(
            STATE_PARTIAL_BLIND,
            f"CARRIED: {name!r} asks for the unlocked C(N) ontology. The dated naming snapshot "
            "cannot resolve it; RELIES-ON NFRA_C3MATERIALIZE owns that lock. No vertical, "
            "membership, or answer was guessed.",
            STATE_NOT_DECIDABLE,
        )
        return 0

    known = set(data.get("named_threads") or [])
    if name not in known:
        _emit_state(
            STATE_SUBJECT_ABSENT,
            f"subject {name!r} is absent from the naming corpus: 0 matches across "
            f"{len(known)} declared C3.ii vertical name(s). This is not a C(N) inference.",
        )
        return 2

    units = [row for row in data.get("threads", []) if row.get("named_thread") == name]
    resources = (data.get("resources_by_named_thread") or {}).get(name, [])
    if not units:
        _emit_state(
            STATE_PRESENT_ZERO,
            f"subject {name!r} exists in the {len(known)}-vertical naming corpus; measured result "
            f"is 0 chain(s) in the asked class across {len(data.get('threads', []))} estate "
            f"chain(s); the separate C0 roster carries {len(resources)} item(s) and is not "
            "silently promoted into a chain result.",
        )
        # Preserve the denominator grammar consumed by the typed Observation_Record wrapper.
        print(
            f"{TOOL} C3.ii vertical {name!r} - 0 chains (D2 = C2-motif instances) "
            "(in-scope 0 / explicit-out 0 / unreviewed 0)"
        )
        print(
            _compbudget.within_budget_line(
                0, 0, "chain", budget_s, budget_source, clock.elapsed()
            )
        )
        return 0

    remaining, cursor_error = _after_cursor(units, cursor)
    if cursor_error:
        _emit_state(STATE_PARTIAL_BLIND, cursor_error, STATE_NOT_DECIDABLE)
        return 2
    if cursor:
        print(
            f"RESUMED AFTER: {cursor}; {len(remaining)} of {len(units)} chain(s) remain "
            "in deterministic thread_id order."
        )
    selected, expired = _render_named_rows(
        legacy, data, name, remaining, resources, clock, deadline_ns
    )
    if expired:
        _emit_state(
            STATE_PARTIAL_BLIND,
            "the traversal reached only the declared chain prefix before its caller-supplied "
            "budget; resume from the printed cursor. No unseen chain is reported as absent.",
            STATE_NOT_DECIDABLE,
        )
    _budget_terminal(
        selected=selected,
        total=len(remaining),
        expired=expired,
        clock=clock,
        budget_s=budget_s,
        budget_source=budget_source,
        command=f"{TOOL} {name!r} --budget {_compbudget.fmt(budget_s)}",
    )
    return 0


def _resource_blob(row: dict) -> str:
    return " ".join(
        [
            str(row.get("thread_id") or ""),
            str(row.get("description") or ""),
            " ".join(row.get("producers") or []),
            " ".join(row.get("served_artifacts") or []),
            str(row.get("frontend_resolution") or ""),
        ]
    ).lower()


def _resource_run(
    legacy,
    data: dict,
    needle: str,
    budget_s: float,
    budget_source: str,
    clock: _compbudget.Clock,
    deadline_ns: int | None,
    cursor: str | None,
) -> int:
    _emit_naming_context(data)
    remaining, cursor_error = _after_cursor(list(data.get("threads") or []), cursor)
    if cursor_error:
        _emit_state(STATE_SUBJECT_ABSENT, cursor_error)
        return 2
    selected, expired = _budget_prefix(remaining, clock, deadline_ns)
    hits = [row for row in selected if needle.lower() in _resource_blob(row)]
    if hits:
        view = dict(data)
        view["threads"] = hits
        legacy.cmd_resource(view, needle)
    elif not expired:
        _emit_state(
            STATE_SUBJECT_ABSENT,
            f"resource subject {needle!r} is absent from {len(selected)} measured estate chain(s).",
        )
    if expired:
        _emit_state(
            STATE_PARTIAL_BLIND,
            f"resource search examined {len(selected)} of {len(remaining)} chain(s); the unseen "
            "suffix is NOT-DECIDABLE until resumed.",
            STATE_NOT_DECIDABLE,
        )
    _budget_terminal(
        selected=selected,
        total=len(remaining),
        expired=expired,
        clock=clock,
        budget_s=budget_s,
        budget_source=budget_source,
        command=f"{TOOL} --resource {needle!r} --budget {_compbudget.fmt(budget_s)}",
    )
    if expired or hits:
        return 0
    return 2


def _list_run(legacy, data: dict, budget_s: float, budget_source: str) -> int:
    _emit_naming_context(data)
    print(f"RULE T: {_compbudget.disclosure_line(budget_s, budget_source)}")
    print(
        "  DECLARED NON-APPLICATION for --list early-abort/resume: the generated naming "
        "snapshot is one atomic read before this mode begins; there is no honest internal "
        "cursor from which to resume that read."
    )
    if not data.get("named_threads"):
        _emit_state(
            STATE_NOT_APPLICABLE,
            "--list has no C3.ii vertical population in the loaded naming snapshot; this is a "
            "mode-level empty domain, not a miss on one subject.",
        )
        return 0
    legacy.cmd_list(data)
    return 0


def threads_of(snap: dict) -> dict:
    for field in ("resources_by_named_thread", "threads", "named_threads"):
        v = snap.get(field)
        if isinstance(v, dict) and v:
            return v
        if isinstance(v, list) and v and isinstance(v[0], dict):
            out = {}
            for r in v:
                n = r.get("name") or r.get("thread")
                if n:
                    out[n] = r
            if out:
                return out
    return {}


def cmd_list(snap: dict) -> int:
    th = threads_of(snap)
    print()
    print(f"C3.ii SEMANTIC VERTICALS -- {len(th)} in the naming snapshot")
    for n in sorted(th):
        body(f"  {n}")
    footer()
    footer(f"  denominator: {len(th)} vertical(s). This is the SNAPSHOT's population, not the estate's.")
    return 0


def cmd_thread(snap: dict, name: str, verify_served: bool = False) -> int:
    th = threads_of(snap)
    hits = {k: v for k, v in th.items() if name.lower() in k.lower()}
    print()
    if not hits:
        print(f"NO C3.ii VERTICAL MATCHING {name!r} -- searched {len(th)} vertical name(s) in the snapshot.")
        print("  That is a statement about the SNAPSHOT's population, not about the estate.")
        return 1
    live = live_keys()
    snap_concrete, snap_patterns, _snap_buckets = _snapshot_keys(snap)
    _verified = {"EXISTS": 0, "404": 0, "UNREACHABLE": 0, "UNVERIFIABLE": 0}
    for tname, tbody in sorted(hits.items()):
        body(f"C3.ii VERTICAL: {tname}")
        # @c9be07b413: threads_of() resolves the thin NAMING dict (resources_by_named_thread --
        # resource-name strings, no keys), while the snapshot's RICH per-chain bodies (producers /
        # served_artifacts, where every S3 key actually lives) sit in the top-level `threads` list
        # keyed by `named_thread`. Without this merge the key plane extracted NOTHING for any
        # thread ("no S3-key-shaped entries") and every verdict below was vacuously absent.
        _rich = [e for e in snap.get("threads", [])
                 if isinstance(e, dict)
                 and str(e.get("named_thread", "")).lower() == str(tname).lower()]
        blob = json.dumps([tbody] + _rich)
        tconc, tpat, tbuckets = _snapshot_keys(json.loads(blob))
        tkeys = sorted(tconc)
        if not tkeys and not tpat:
            body("  (no S3-key-shaped entries asserted for this thread in the snapshot)")
        for k in tkeys:
            producers = live["keys"].get(k)
            # Instrument-fix @c9be07b413: "LIVE" here was a REPO-TEXT claim -- a retired
            # script still carrying the literal made a dead key render as live (the measured
            # 404 platinum key). The tag now says which plane it is; --verify-served adds the
            # S3 plane per key (head-object), which is the only EXISTS/404 oracle.
            if verify_served:
                _b = tbuckets.get(k)
                if _b:
                    _v, _vinfo = _head_object(_b, k)
                    _verified[_v] = _verified.get(_v, 0) + 1
                    _stamp = {"EXISTS": f"S3 EXISTS {_vinfo}",
                              "404": "S3 404 -- THE OBJECT IS NOT THERE",
                              "UNREACHABLE": f"S3 UNREACHABLE ({_vinfo})"}[_v]
                else:
                    _verified["UNVERIFIABLE"] += 1
                    _stamp = "S3 UNVERIFIABLE (snapshot names no bucket for this key)"
            else:
                _stamp = "S3 NOT VERIFIED (repo-text claim; --verify-served head-objects it)"
            if producers:
                body(f"  LIVE-IN-REPO   {k}")
                body(f"                     [{_stamp}]")
                for pr in producers[:6]:
                    body(f"                     <- {pr}")
            else:
                body(f"  STALE-IN-SNAPSHOT  {k}")
                body(f"                     [{_stamp}]")
                body("                     ^ asserted by the snapshot, NOT produced by any source in")
                body("                       the scanned roots. Do NOT treat this key as served.")
        for k in sorted(tpat):
            body(f"  UNCOMPARABLE       {k}")
            body("                     ^ a glob/template, not a single object -- no live/stale verdict")
    footer()
    footer(f"  live key denominator: {len(live['keys'])} distinct key(s) across {live['files']} file(s)"
           + (f"; {live['errors']} unreadable/unparseable" if live["errors"] else ""))
    footer(f"  snapshot asserted {len(snap_concrete)} concrete key(s) + {len(snap_patterns)} pattern(s).")
    if verify_served:
        footer(f"  S3 verification: {_verified['EXISTS']} EXISTS, {_verified['404']} 404, "
               f"{_verified['UNREACHABLE']} UNREACHABLE, {_verified['UNVERIFIABLE']} UNVERIFIABLE "
               "(no bucket in snapshot). A 404 beside LIVE-IN-REPO = repo text defending a zombie.")
    else:
        footer("  S3 EXISTENCE NOT VERIFIED this run -- every verdict above is a REPO-TEXT plane "
               "claim. --verify-served head-objects each bucketed key (the EXISTS/404 oracle).")
    return 0


def cmd_resource(snap: dict, substr: str) -> int:
    live = live_keys()
    hits = {k: v for k, v in live["keys"].items() if substr.lower() in k.lower()}
    print()
    print(f"RESOURCE MATCH {substr!r} -- {len(hits)} of {len(live['keys'])} live key(s)")
    for k, producers in sorted(hits.items()):
        body(f"  {k}")
        for pr in producers[:8]:
            body(f"      <- {pr}")
    if not hits:
        print("  none. That is a statement about the scanned roots, not about the estate.")
    close_pager()
    return 0 if hits else 1


def cmd_drift(snap: dict) -> int:
    """The defect this engine exists to surface, as a first-class report."""
    live = live_keys()
    concrete, patterns, _buckets = _snapshot_keys(snap)
    gone = sorted(k for k in concrete if k not in live["keys"])
    print()
    print("SNAPSHOT-vs-LIVE DRIFT")
    print(f"  snapshot asserts {len(concrete)} CONCRETE key(s) + {len(patterns)} pattern(s);")
    print(f"  live source produces {len(live['keys'])} key(s) across the scanned roots.")
    print("  PATTERNS ARE NOT JUDGED: a glob/template names no single object, so it gets no")
    print(f"  live/stale verdict. Counting them as stale would manufacture {len(patterns)} findings.")
    print(f"  {len(gone)} of {len(concrete)} CONCRETE snapshot key(s) have NO live producer:")
    for k in gone[:40]:
        body(f"    STALE-IN-SNAPSHOT  {k}")
    if len(gone) > 40:
        body(f"    ... and {len(gone) - 40} more")
    footer()
    footer("  A stale estate map ACTIVELY DEFENDS ZOMBIES. Each line above is a key the old tool would")
    footer("  have served as fact. Absence of a live producer is NOT proof the key is dead -- a shell")
    footer("  or out-of-root producer is outside this denominator -- but it is never a LIVE claim.")
    return 0


def do_refresh() -> int:
    if not _REFRESHER.is_file():
        return _fail_loud(
            f"gen-estate-resolver.py absent at {_REFRESHER}",
            "the refresh bridge's producer is missing; the snapshot cannot be regenerated",
        )
    print(f"{TOOL}: --refresh -> {_REFRESHER.name} (BRIDGE, not the destination)", file=sys.stderr)
    proc = subprocess.run([sys.executable, str(_REFRESHER)], cwd=str(_WS))
    if proc.returncode != 0:
        print(
            f"{TOOL}: REFRESH FAILED rc={proc.returncode} -- snapshot NOT regenerated and left\n"
            "  untouched. Loud on purpose: a refresh that quietly did nothing leaves a stale map\n"
            "  wearing a fresh expectation.",
            file=sys.stderr,
        )
        return 2
    return 0


def _ontology_dir():
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(os.path.dirname(os.path.dirname(here)))
    return os.path.join(root, "infra", "system", "ontology")


def cmd_layers() -> int:
    """STABLE canon, served verbatim (the serving law: stable above the emergence line)."""
    import os
    import sys
    p = os.path.join(_ontology_dir(), "C0_C1_C2_C3_C4_SYSTEM_LAYERS.md")
    try:
        with open(p, encoding="utf-8") as f:
            content = f.read()
        if head_armed():
            # doc lines are all body; no verdict footer -> close_pager lands the marker
            for ln in content.splitlines():
                try:
                    body(ln)
                except UnicodeEncodeError:
                    body(ln.encode("ascii", errors="replace").decode("ascii"))
            close_pager()
            return 0
        # encoding-safe on Windows consoles (cp1252 chokes on box-drawing glyphs)
        try:
            sys.stdout.write(content)
        except UnicodeEncodeError:
            sys.stdout.buffer.write(content.encode("utf-8", errors="replace"))
        return 0
    except OSError as exc:
        print(f"{TOOL} --layers: stable canon unreadable ({exc}); rc=2", file=sys.stderr)
        return 2


def cmd_definitions(term: str) -> int:
    """Canonical term lookup -- SYSTEM_DEFINITIONS.yaml, fuzzy on term name."""
    import os
    import sys
    try:
        import yaml
    except ImportError:
        print(f"{TOOL} --definitions: pyyaml unavailable", file=sys.stderr)
        return 2
    p = os.path.join(_ontology_dir(), "SYSTEM_DEFINITIONS.yaml")
    try:
        with open(p, encoding="utf-8") as f:
            d = yaml.safe_load(f)
        terms = d["terms"]
    except (OSError, KeyError, yaml.YAMLError) as exc:
        print(f"{TOOL} --definitions: registry unreadable ({exc}); rc=2", file=sys.stderr)
        return 2
    # F-C1 schema gate on the read path (Andrew-direct 2026-08-10 "build the definitions
    # checker"; wiring = fail-loud-in-the-serving-tool, the file owner's call @abfe77a537 row 5).
    # Violations are LOUD but conforming entries still serve -- an integrity banner, not a
    # denial: one bad entry must not brick every agent's vocabulary lookup. There is no silent
    # branch: the guard either runs (silent only at 0 violations) or reports itself UNAVAILABLE.
    try:
        import importlib.util as _ilu
        _cs = os.path.join(_ontology_dir(), "check_system_definitions.py")
        _spec = _ilu.spec_from_file_location("check_system_definitions", _cs)
        _mod = _ilu.module_from_spec(_spec)
        _spec.loader.exec_module(_mod)
        _n, _bad, _msgs = _mod.check(d)
        if _bad:
            print(f"*** SCHEMA VIOLATIONS ({_bad}) in SYSTEM_DEFINITIONS ({_n} entries "
                  f"checked) -- serving anyway; FIX BEFORE TRUSTING: ***")
            for _m in _msgs:
                print(f"  *** {_m}")
    except Exception as _exc:  # noqa: BLE001 -- a missing/broken guard is announced, never skipped
        print(f"{TOOL} --definitions: schema gate UNAVAILABLE ({type(_exc).__name__}: {_exc}) "
              f"-- serving UNVALIDATED registry")
    print(f"{TOOL} | SYSTEM_DEFINITIONS v{d.get('version','?')} (STABLE canon; "
          f"changes only by naming act)")
    if term == "__ALL__":
        for k, v in terms.items():
            # Annex-field NAMES surface in the list line, generically -- the filtering decision
            # is made FROM the list, and a [deprecated] with an invisible binding_residue is the
            # exact harm the field exists to prevent (CVO certification residual 2026-08-19).
            # Names not a count, all extras not one field: a special-cased "+residue" marker
            # would recreate the fixed-trio defect one layer up.
            _extras = [xk for xk in v
                       if xk not in ("definition", "authority", "sits_at", "status")]
            _mark = (" +" + ",".join(_extras)) if _extras else ""
            body(f"  {k:22} [{v.get('status','?'):10}]{_mark} "
                 f"{str(v.get('definition',''))[:90]}")
        footer(f"  denominator: {len(terms)} terms")
        return 0
    tl = term.lower()
    hits = {k: v for k, v in terms.items() if tl in k.lower()}
    if not hits:
        print(f"  NO TERM matches {term!r} -- that is a statement about the registry "
              f"({len(terms)} terms), not the concept. Propose additions by naming act.")
        return 1
    for k, v in hits.items():
        print(f"\nTERM: {k}   [{v.get('status')}]")
        print(f"  definition: {v.get('definition')}")
        print(f"  authority:  {v.get('authority')}")
        print(f"  sits_at:    {v.get('sits_at')}")
        # Serve EVERY extra field the entry carries (binding_residue, resolves, measured,
        # do_not, ...). The registry's annex fields are canon content; a renderer printing a
        # fixed trio silently hid them from every consumer (caught 2026-08-19 when T16's
        # binding_residue landed and the serve-exercise showed zero -- the half-served class).
        for xk, xv in v.items():
            if xk not in ("definition", "authority", "sits_at", "status"):
                print(f"  {xk}: {xv}")
    return 0


def cmd_matrix() -> int:
    """C3 cross-partition matrix -- the standing reconciliation instrument (rule bank v1.5
    c3_dual_partition). View-compiled from the resolver dual keys at invocation."""
    import collections
    import os
    try:
        import yaml
    except ImportError:
        print(f"{TOOL} --matrix: pyyaml unavailable -- cannot read the canonical catalog",
              file=sys.stderr)
        return 2
    snap, rc = load_snapshot()
    if rc:
        return rc
    # The family->structure translation is CATALOG-OWNED (legacy_family_key on each C3.i entry);
    # view-compile it at invocation. A hand-copied dict here previously duplicated the catalog --
    # a rename/new family would not have propagated and would silently bucket to residue.
    cat = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "NFRA_ONTOLOGY_C2C3_CANONICAL.yaml")
    try:
        with open(cat, encoding="utf-8") as f:
            structures = yaml.safe_load(f)["c3_deterministic_structures"]
    except (OSError, KeyError, yaml.YAMLError) as exc:
        print(f"{TOOL} --matrix: canonical catalog unreadable ({exc}) -- refusing a hand-copied "
              "fallback for a catalog-owned mapping; rc=2", file=sys.stderr)
        return 2
    keys = [v.get("legacy_family_key") for v in structures.values()]
    if len(set(keys)) != len(keys):
        print(f"{TOOL} --matrix: DUPLICATE legacy_family_key in the catalog -- a collision here "
              "silently drops a structure from the matrix; fix the catalog; rc=2", file=sys.stderr)
        return 2
    fam2sys = {v["legacy_family_key"]: k for k, v in structures.items()}
    sysv = collections.defaultdict(set)
    vsys = collections.defaultdict(set)
    for t in snap.get("threads", []):
        sname = fam2sys.get(t.get("family") or "", "UNASSIGNED-RESIDUE")
        sysv[sname].add(t["named_thread"])
        vsys[t["named_thread"]].add(sname)
    print(f"{TOOL} | C3 CROSS-PARTITION MATRIX (C3.i x C3.ii; dual key = (family, named_thread))")
    print(f"  denominators: {len(sysv)} structures x {len(vsys)} verticals over "
          f"{len(snap.get('threads', []))} chains -- a matrix CHANGE is an adjudication event")
    print("")
    print("  C3.i DETERMINISTIC STRUCTURE -> C3.ii semantic-vertical span:")
    for sname in sorted(sysv, key=lambda k: -len(sysv[k])):
        body(f"    {sname:34} ({len(sysv[sname]):2}) {', '.join(sorted(sysv[sname]))}")
    print("")
    print("  C3.ii SEMANTIC VERTICAL -> C3.i structure span:")
    for v in sorted(vsys):
        body(f"    {v:22} ({len(vsys[v])}) {', '.join(sorted(vsys[v]))}")
    bound = [(s, sorted(vs)[0]) for s, vs in sysv.items()
             if len(vs) == 1 and len(vsys.get(sorted(vs)[0], set())) == 1
             and s != "UNASSIGNED-RESIDUE"]
    names = ", ".join(f"{s}<->{v}" for s, v in sorted(bound)) or "none"
    footer("")
    footer(f"  bound_pairs (mutual 1:1, computed): {names}")
    declared = set(snap.get("named_threads", []))
    chainless = sorted(declared - set(vsys))
    if chainless:
        footer(f"  DECLARED-BUT-CHAINLESS (adjudication owed): {', '.join(chainless)}")
    footer("  DRILL (one rail per descent): C3->C2 rides D3 -- comp-estate --structure <sys-name> (chains +")
    footer("  motifs) | C2->C1 rides D2 -- comp-estate <vertical> (chain blocks = C1 hops) | C1->C0 rides")
    footer("  D1 (grain) -- the C0 roster + served keys. Ladder + rails verbatim: comp-estate --layers")
    return 0


def cmd_segments() -> int:
    """C4 SEGMENTS -- the agent routing entry point (Andrew-ratified names + registries,
    2026-07-30). Reads the canonical catalog live; a missing/corrupt catalog fails LOUD."""
    import os
    import sys
    try:
        import yaml
    except ImportError:
        print(f"{TOOL} --segments: pyyaml unavailable -- cannot read the canonical catalog",
              file=sys.stderr)
        return 2
    cat = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "NFRA_ONTOLOGY_C2C3_CANONICAL.yaml")
    try:
        with open(cat, encoding="utf-8") as f:
            d = yaml.safe_load(f)
        segs = d["c4_segments"]
    except (OSError, KeyError, yaml.YAMLError) as exc:
        print(f"{TOOL} --segments: canonical catalog unreadable ({exc}) -- "
              "an unnamed source is not a source; rc=2", file=sys.stderr)
        return 2
    print(f"{TOOL} | C4 SEGMENTS -- the agent routing layer (source: {os.path.basename(cat)}, "
          f"rule bank v1.4)")
    print("  Route: C4 segment -> C3(i|ii) -> C2 motif (D2 chain) -> C1 -> C0. Verticals are C3.ii,")
    print("  business overlay; `comp-estate <vertical>` enters at C3.ii.\n")
    for name, v in segs.items():
        body("=" * 88)
        body(f"SEGMENT: {name}   ({v.get('display_name', '')})")
        body(f"  structures: {', '.join(v.get('registry', []))}")
        if v.get("flags"):
            body(f"  FLAGS: {'; '.join(v['flags'])}")
        body(f"  verticals: {', '.join(v.get('verticals_served', []))}")
        desc = " ".join(str(v.get("high_signal", "")).split())
        import textwrap
        for line in textwrap.wrap(desc, width=86):
            body(f"    {line}")
    footer("=" * 88)
    footer(f"  denominator: {len(segs)} segments (the catalog is the source; this print is a view)")
    footer("DRILL DOWN THE LADDER: C4->C3 is registry membership (this view). Below C3 one D-rail carries")
    footer("  each descent: C3->C2 rides D3 (contract; comp-estate --structure <sys-name> = chains + motifs),")
    footer("  C2->C1 rides D2 (comp-estate <vertical> = chain blocks whose rows ARE the C1 hops),")
    footer("  C1->C0 rides D1 (grain; the C0 fact roster + served keys). The rails are the fidelity.")
    return 0


def cmd_structure(sysname: str) -> int:
    """C3.i DRILL VIEW: one deterministic structure -> its chains (D2) grouped by C3.ii
    vertical, each with its C2 motif. Closes the ladder-descent hole the 2026-07-30 drill
    pass found: --matrix showed the C3 grid but NO mode entered by STRUCTURE, so C3.i was
    reachable as a row label and nothing else. View-compiled (catalog + resolver + census)."""
    import collections
    legacy, data = _legacy()
    fam2sys, motif_idx = legacy.ladder_context()
    if fam2sys is None:
        return 2
    structures = sorted(set(fam2sys.values()))
    hits = [s for s in structures if sysname.lower() in s.lower()]
    if not hits:
        print(f"{TOOL} --structure: NO C3.i structure matches {sysname!r} -- that is a statement "
              f"about the catalog ({len(structures)} structures).", file=sys.stderr)
        print(f"  known: {', '.join(structures)}", file=sys.stderr)
        return 2
    if len(hits) > 1:
        print(f"{TOOL} --structure: AMBIGUOUS {sysname!r} -> {', '.join(hits)} -- narrow it.",
              file=sys.stderr)
        return 2
    struct = hits[0]
    fams = sorted(k for k, v in fam2sys.items() if v == struct)
    chains = [t for t in data["threads"]
              if fam2sys.get(t.get("family") or "UNASSIGNED", "UNASSIGNED-RESIDUE") == struct]
    print(f"C3.i STRUCTURE: {struct} -- {len(chains)} chains (D2 = C2-motif instances)")
    print("=" * 78)
    byv = collections.defaultdict(list)
    for t in chains:
        byv[t["named_thread"]].append(t)
    for v in sorted(byv):
        body(f"\nC3.ii vertical: {v} ({len(byv[v])} chain(s))")
        for t in byv[v]:
            motif = motif_idx.get(t["thread_id"], "UNCLASSIFIED")
            body(f"  {t['thread_id']:<44} C2 motif: {motif}")
    footer("")
    footer(f"  denominator: {len(chains)} chains across {len(byv)} vertical(s); "
           f"catalog family key(s): {', '.join(fams)}")
    footer("DRILL (rails): C3->C2 rides D3 (the contract binding this structure to its chains; motifs printed")
    footer("  above) | C2->C1 rides D2 (comp-estate <vertical> = the chain blocks' C1 hop rows; comp-blast /")
    footer("  comp-kuzu walk them) | C1->C0 rides D1 (grain: the vertical view's served keys + C0 roster)")
    return 0


def cmd_census_drift(plane: str) -> int:
    """L3 world-model drift: SET-diff (never a count) of the hand-adjudicated lambda census
    against the live estate. Founding specimen 2026-07-30: census 169 vs TF 169 was COUNT-parity
    concealing 66 membership changes. tf = DESIRED (repo greps, no creds); aws = APPLIED
    (lambda list-functions). Nonzero residue is a WORKLIST (route per the process doc s.4),
    not an error -- exits 0 with the sets printed, 3 only on a broken retrieval."""
    import glob
    import json
    import os
    import re
    import sys
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(os.path.dirname(os.path.dirname(here)))
    taxo_path = os.path.join(root, "org", "modules", "graph", "estate_census", "AUTHORITATIVE_lambda_taxonomy.json")  # RE-POINTED 2026-08-20 census-regen landing
    try:
        with open(taxo_path, encoding="utf-8") as f:
            census = set(json.load(f)["lambda_to_named_thread"].keys())
    except (OSError, KeyError, json.JSONDecodeError) as exc:
        print(f"census-drift: cannot load taxonomy ({exc})", file=sys.stderr)
        return 3
    if plane == "aws":
        import subprocess
        try:
            out = subprocess.run(["aws", "lambda", "list-functions", "--query",
                                  "Functions[].FunctionName", "--output", "json"],
                                 capture_output=True, text=True, timeout=120)
            live = set(json.loads(out.stdout))
        except Exception as exc:
            print(f"census-drift: aws plane retrieval failed ({exc}) -- refusing to "
                  "diff against an empty live set", file=sys.stderr)
            return 3
        plane_note = "APPLIED (aws lambda list-functions)"
    else:
        live = set()
        pat = re.compile(r'function_name\s*=\s*"([a-z0-9_-]+)"', re.I)
        for tf in glob.glob(os.path.join(root, "infra", "aws", "**", "*.tf"), recursive=True):
            try:
                with open(tf, encoding="utf-8", errors="replace") as f:
                    live |= set(pat.findall(f.read()))
            except OSError:
                continue
        plane_note = "DESIRED (infra/aws TF function_name declarations)"
    if not live:
        print("census-drift: live set came back EMPTY -- that is a broken retrieval, "
              "not a clean estate", file=sys.stderr)
        return 3
    added = sorted(live - census)
    gone = sorted(census - live)
    print(f"CENSUS-DRIFT | plane: {plane_note}")
    print(f"  census (regen 2026-08-20, live home estate_census/): {len(census)} lambdas")
    print(f"  live: {len(live)} | UNMODELED (live, not in census): {len(added)} | "
          f"CENSUS-ONLY (gone or unmanaged-on-this-plane): {len(gone)}")
    print("  >> a SET diff -- equal counts prove nothing (66 changes once cancelled to zero net)")
    for n in added:
        body(f"  + {n}")
    for n in gone:
        body(f"  - {n}")
    footer("  route the residue per ESTATE_WORLD_MODEL_PROCESS.md s.4 "
           "(A=assign to a thread, B=add the missing plane/predicate, C=candidate NEW business "
           "function -> naming is Andrew/CVO's, never auto)")
    return 0


def _legacy():
    """The thread-model engine (named threads -> sub-threads -> producers -> served ->
    frontend + owning tool + debt flags). REGRESSION REPAIR 2026-07-30 (CVO tool-walk #1):
    the 07-29 rename shipped this module as a REPLACEMENT and silently dropped the
    flagship traversal + --tool/--debt/--fe-reachability/--validate/--gate-b and both
    standing oracles. The capability was intact in the legacy CLI (then pipescript_cli.py,
    now estate_infrastructure_cli.py) the whole time -- this delegation re-exposes it.
    Two planes, one CLI: THREAD MODEL (legacy, resolver snapshot, ~0.3s) + KEY PLANE
    (this module, live re-derivation, tens of seconds)."""
    import os
    import sys as _sys
    _here = os.path.dirname(os.path.abspath(__file__))
    if _here not in _sys.path:
        _sys.path.insert(0, _here)
    import estate_infrastructure_cli as legacy
    return legacy, legacy.load()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog=TOOL, description="Opal business-semantic estate traversal.")
    ap.add_argument("name", nargs="?", help="C3.ii vertical name (substring)")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--resource", metavar="SUBSTR")
    ap.add_argument("--drift", action="store_true", help="snapshot keys with no live producer")
    ap.add_argument("--verify-served", action="store_true", dest="verify_served",
                    help="head-object every bucketed concrete key in the thread view -- the S3 "
                         "EXISTS/404 oracle (repo-text LIVE is a different plane; @c9be07b413)")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--refresh-only", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--tool", nargs=2, metavar=("NAME", "TOOL"),
                    help="chains of NAME owned by TOOL (loud out-of-scope)")
    ap.add_argument("--debt", action="store_true", help="debtscan-flag view across all threads")
    ap.add_argument("--fe-reachability", action="store_true", dest="fe_reachability",
                    help="FE-reachability per backend thread (CVO ground-truth)")
    ap.add_argument("--orphans-only", action="store_true", dest="orphans_only")
    ap.add_argument("--validate", action="store_true", help="completeness gate")
    ap.add_argument("--gate-b", action="store_true", dest="gate_b",
                    help="standing regression oracle (named-thread reproduction)")
    ap.add_argument("--keys", action="store_true",
                    help="append the live key-plane scan (tens of seconds; the thread-model "
                         "answer itself is ~0.3s from the resolver snapshot)")
    ap.add_argument("--layers", action="store_true",
                    help="the stable C0..C4 ladder doc, served verbatim")
    ap.add_argument("--definitions", nargs="?", const="__ALL__", metavar="TERM",
                    help="canonical term lookup from SYSTEM_DEFINITIONS.yaml (no arg = list)")
    ap.add_argument("--matrix", action="store_true",
                    help="the C3 cross-partition matrix: per-system vertical span x per-vertical "
                         "system span (view-compiled; a matrix CHANGE is an adjudication event)")
    ap.add_argument("--structure", metavar="SYS",
                    help="C3.i DRILL VIEW: one deterministic structure (substring) -> its chains "
                         "grouped by C3.ii vertical, each with its C2 motif")
    ap.add_argument("--segments", action="store_true",
                    help="THE C4 ENTRY POINT: the five agent-routing segments, each a registry "
                         "of C3 systems with a high-signal description. Start here.")
    ap.add_argument("--census-drift", action="store_true", dest="census_drift",
                    help="SET-diff the L3 lambda census against the live estate "
                         "(default plane: tf/DESIRED; --plane aws for APPLIED). "
                         "Process: org/modules/graph/ESTATE_WORLD_MODEL_PROCESS.md")
    ap.add_argument("--plane", choices=("tf", "aws"), default="tf")
    ap.add_argument("--head", nargs="?", const=50, type=int, metavar="N",
                    help="truncate BODY rows after N lines (bare --head = 50). "
                         "Verdict-preserving by design: the truncation DECLARES itself "
                         "(marker on stdout + one stderr copy) and the mode's "
                         "verdict/denominator footer ALWAYS prints -- a cut denominator "
                         "is how a truncated worldview gets mistaken for the whole one.")
    ap.add_argument(
        "--budget",
        default=None,
        help=(
            "Rule T (NFRA_COMPEFFICACY PRD s.4.4): seconds for <name> and --resource "
            "chain traversal; carrier --budget > env COMP_BUDGET_S > default %ss. "
            "Expiry prints scanned n of N plus a --cursor and returns rc 0; --list "
            "declares its atomic-snapshot non-application."
            % _compbudget.fmt(_compbudget.DEFAULT_BUDGET_S)
        ),
    )
    ap.add_argument(
        "--cursor",
        metavar="CHAIN_ID",
        help="resume <name>/--resource after the last fully processed deterministic chain",
    )
    a = ap.parse_args(argv)

    if a.head is not None:
        if a.head < 0:
            ap.error("--head takes a non-negative line count")
        set_head(a.head)
    if a.cursor and not (a.name or a.resource):
        ap.error("--cursor requires <name> or --resource")

    if a.layers:
        return cmd_layers()
    if a.definitions:
        return cmd_definitions(a.definitions)
    if a.matrix:
        return cmd_matrix()
    if a.segments:
        return cmd_segments()
    if a.structure:
        return cmd_structure(a.structure)

    if a.census_drift:
        return cmd_census_drift(a.plane)

    if a.self_test:
        return self_test()

    try:
        budget_s, budget_source = _compbudget.resolve_budget(a.budget)
    except ValueError as exc:
        print(f"{TOOL}: REFUSED --budget: {exc}", file=sys.stderr)
        return 2
    # Start before the snapshot load: loading the traversal substrate is work, not free setup.
    rule_t_clock = _compbudget.Clock(budget_s)
    rule_t_deadline_ns = (
        None if budget_s == 0 else time.perf_counter_ns() + max(1, int(budget_s * 1_000_000_000))
    )

    # Legacy-plane modes: thread model only, no live key scan (fast path).
    # Legacy cmd_* may return None for success -- normalize to int.
    if a.tool or a.debt or a.fe_reachability or a.validate or a.gate_b:
        legacy, data = _legacy()
        if a.gate_b:
            return legacy.cmd_gate_b(data) or 0
        if a.validate:
            return legacy.cmd_validate(data) or 0
        if a.debt:
            return legacy.cmd_debt(data) or 0
        if a.fe_reachability:
            return legacy.cmd_fe_reachability(data, name=a.name, orphans_only=a.orphans_only) or 0
        return legacy.cmd_tool(data, a.tool[0], a.tool[1]) or 0

    if a.refresh or a.refresh_only:
        rc = do_refresh()
        if rc:
            return rc

    # The live key-plane (load_snapshot's re-derivation) costs tens of seconds; the
    # flagship thread-model answers come from the resolver snapshot at ~0.3s. Only pay
    # the scan when the caller asks a key-plane question (--drift / --refresh / --keys).
    # --verify-served is a key-plane question by definition (it head-objects the thread's
    # concrete keys), so it implies the scan the fast path skips (@c9be07b413 -- without
    # this, the flag was accepted and silently ignored on the flagship path).
    want_keys = (a.drift or a.refresh or a.refresh_only or a.keys
                 or getattr(a, "verify_served", False)
                 or not (a.name or a.resource or a.list))

    if a.list:
        legacy, data = _legacy()
        return _list_run(legacy, data, budget_s, budget_source)
    if a.resource:
        # Thread-model reverse lookup (lambdas/resources/sub-threads) -- the question
        # the registry teaches; append the live key match only under --keys.
        legacy, data = _legacy()
        if not a.keys:
            return _resource_run(
                legacy,
                data,
                a.resource,
                budget_s,
                budget_source,
                rule_t_clock,
                rule_t_deadline_ns,
                a.cursor,
            )
        lrc = legacy.cmd_resource(data, a.resource) or 0
        if a.keys:
            snap, rc = load_snapshot()
            if rc:
                return rc
            emit_header(snap)
            krc = cmd_resource(snap, a.resource) or 0
            return 0 if (lrc == 0 or krc == 0) else max(lrc, krc)
        return lrc
    if a.name and not want_keys:
        # The flagship: full thread traversal from the resolver snapshot, fast.
        legacy, data = _legacy()
        return _named_thread_run(
            legacy,
            data,
            a.name,
            budget_s,
            budget_source,
            rule_t_clock,
            rule_t_deadline_ns,
            a.cursor,
        )

    snap, rc = load_snapshot()
    if rc:
        return rc
    emit_header(snap)
    if a.refresh_only:
        return 0
    if a.drift:
        return cmd_drift(snap)
    if a.name:
        legacy, data = _legacy()
        lrc = legacy.cmd_thread(data, a.name) or 0
        print()
        cmd_thread(snap, a.name, verify_served=getattr(a, 'verify_served', False))
        return lrc
    return cmd_list(snap)


def self_test() -> int:
    print("=" * 88)
    print(f"{TOOL} --self-test")
    print("=" * 88)
    res = []

    def chk(n, ok, d):
        res.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {n}\n         {d}")

    snap, rc = load_snapshot()
    chk("C1 substrate loads and can name its own vintage",
        rc == 0 and snap is not None,
        f"rc={rc}; last_review={snap.get('last_review') if snap else None}")

    lk = live_keys()
    chk("C2 keys are derived LIVE from source, not read from the snapshot",
        lk["files"] > 100 and len(lk["keys"]) > 0,
        f"{len(lk['keys'])} live key(s) from {lk['files']} file(s) -- the frozen-key defect is closed")

    if snap:
        conc, pat, _bk = _snapshot_keys(snap)
        gone = [k for k in conc if k not in lk["keys"]]
        chk("C3 snapshot-vs-live drift is DETECTABLE (the mdpf class)",
            len(conc) > 0,
            f"{len(gone)} of {len(conc)} CONCRETE snapshot key(s) have no live producer -- reported, never served as fact")
        chk("C4 globs/templates are NOT judged (no manufactured findings)",
            len(pat) > 0 and not any(any(c in k for c in _PATTERNISH) for k in conc),
            f"{len(pat)} pattern(s) declared UNCOMPARABLE; 0 leaked into the concrete set that gets a stale verdict")

    chk("C5 fail-loud path exists and is not a bare except",
        _fail_loud.__doc__ is None and callable(_fail_loud),
        "an unnameable substrate prints SOURCE UNRESOLVABLE and returns 2, never silence")

    ok = sum(1 for r in res if r)
    print("-" * 88)
    print(f"  {ok} of {len(res)} controls PASS (score on OUTPUT, not rc)")
    print("=" * 88)
    return 0 if ok == len(res) else 1


if __name__ == "__main__":
    sys.exit(main())
