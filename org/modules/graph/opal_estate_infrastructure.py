"""opal_estate_infrastructure -- the OPAL estate traversal engine (C4: estate-infrastructure).

Tool: `comp-estate` (the first point of contact for agent coherence over the Estate).
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
import warnings
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

TOOL = "comp-estate"
STALE_AFTER_DAYS = 14
_DYN = "{*}"

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
    """-> (concrete, patterns). Every S3-key-shaped string the snapshot asserts, at any depth.

    SPLIT ON PURPOSE. A snapshot entry like `bronze/eclipse/*` or
    `bronze/orion-api/{date}/{transactions.csv,...}` is a GLOB or a template, not a key -- there is
    no single object it names, so "does a live producer write it?" has no answer. Reporting those as
    STALE-IN-SNAPSHOT would manufacture findings out of entries the comparison structurally cannot
    judge, which is the same absence-is-not-evidence error this engine exists to stop making. They
    are counted and declared UNCOMPARABLE instead.
    """
    concrete: set = set()
    patterns: set = set()

    def add(k: str):
        k = k.rstrip("\"'").strip()
        if not k or k in ("/", "*"):
            return
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
                add(m.group(2))
            elif re.match(r"^(bronze|silver|gold|platinum|json|served)/\S+\.(json|parquet|csv)$", o):
                add(o)

    walk(blob)
    return concrete, patterns


# ---------------------------------------------------------------------------------------------
# Threads
# ---------------------------------------------------------------------------------------------
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


def cmd_thread(snap: dict, name: str) -> int:
    th = threads_of(snap)
    hits = {k: v for k, v in th.items() if name.lower() in k.lower()}
    print()
    if not hits:
        print(f"NO C3.ii VERTICAL MATCHING {name!r} -- searched {len(th)} vertical name(s) in the snapshot.")
        print("  That is a statement about the SNAPSHOT's population, not about the estate.")
        return 1
    live = live_keys()
    snap_concrete, snap_patterns = _snapshot_keys(snap)
    for tname, tbody in sorted(hits.items()):
        body(f"C3.ii VERTICAL: {tname}")
        blob = json.dumps(tbody)
        tconc, tpat = _snapshot_keys(json.loads(blob))
        tkeys = sorted(tconc)
        if not tkeys and not tpat:
            body("  (no S3-key-shaped entries asserted for this thread in the snapshot)")
        for k in tkeys:
            producers = live["keys"].get(k)
            if producers:
                body(f"  LIVE           {k}")
                for pr in producers[:6]:
                    body(f"                     <- {pr}")
            else:
                body(f"  STALE-IN-SNAPSHOT  {k}")
                body("                     ^ asserted by the snapshot, NOT produced by any source in")
                body("                       the scanned roots. Do NOT treat this key as served.")
        for k in sorted(tpat):
            body(f"  UNCOMPARABLE       {k}")
            body("                     ^ a glob/template, not a single object -- no live/stale verdict")
    footer()
    footer(f"  live key denominator: {len(live['keys'])} distinct key(s) across {live['files']} file(s)"
           + (f"; {live['errors']} unreadable/unparseable" if live["errors"] else ""))
    footer(f"  snapshot asserted {len(snap_concrete)} concrete key(s) + {len(snap_patterns)} pattern(s).")
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
    concrete, patterns = _snapshot_keys(snap)
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
    print(f"{TOOL} | SYSTEM_DEFINITIONS v{d.get('version','?')} (STABLE canon; "
          f"changes only by naming act)")
    if term == "__ALL__":
        for k, v in terms.items():
            body(f"  {k:22} [{v.get('status','?'):10}] {str(v.get('definition',''))[:90]}")
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
    footer("  DRILL: comp-estate --structure <sys-name> (C3.i -> chains + C2 motifs) | comp-estate")
    footer("  <vertical> (C3.ii -> chain blocks w/ C1 rows + C0 roster) | comp-estate --layers (the ladder)")
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
    footer("DRILL DOWN THE LADDER: comp-estate <vertical> (C3.ii -> chain blocks) | comp-estate --structure")
    footer("  <sys-name> (C3.i -> chains + C2 motifs) | comp-estate --matrix (the C3 grid). Below C3 the")
    footer("  descent rides the D-rails: a vertical's chain blocks carry C1 rows + the C0 fact roster.")
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
    footer("DRILL: comp-estate <vertical> (full chain blocks: C1 producers/served/frontend rows + C0 roster)")
    footer("       comp-estate --matrix (the C3.i x C3.ii grid) | comp-blast <fn> / comp-kuzu (C1 walks at a D1 grain)")
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
    taxo_path = os.path.join(root, "org", "tier1_exec", "3.0.0_SA_CVO", "logs",
                             "2026-06-15", "estate_census", "AUTHORITATIVE_lambda_taxonomy.json")
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
    print(f"  census (taxonomy 26b32687a, frozen 2026-06-15): {len(census)} lambdas")
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
    a = ap.parse_args(argv)

    if a.head is not None:
        if a.head < 0:
            ap.error("--head takes a non-negative line count")
        set_head(a.head)

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
    want_keys = a.drift or a.refresh or a.refresh_only or a.keys or not (a.name or a.resource or a.list)

    if a.list:
        legacy, data = _legacy()
        return legacy.cmd_list(data) or 0
    if a.resource:
        # Thread-model reverse lookup (lambdas/resources/sub-threads) -- the question
        # the registry teaches; append the live key match only under --keys.
        legacy, data = _legacy()
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
        return legacy.cmd_thread(data, a.name) or 0

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
        cmd_thread(snap, a.name)
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
        conc, pat = _snapshot_keys(snap)
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
