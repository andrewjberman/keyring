#!/usr/bin/env python3
"""
NFRA_GCONTR -- the period-contracts Q1/Q2 engine (TO-2, AE / globgrph lane).

The value-layer never-widen machinery, shared by `comp-aws contract-diff` and
`comp-surface-check check` (the ADVISORY contract layer). THREE limbs, one
declaration (PRD docs/architecture/NFRA_GCONTR_PRD.md, seed
docs/briefs/period-contracts-seed-benchmark-20260615.md):

  Q1 (structure -- the graph diff): snapshot-diff the WRITES edges into a
      contracted artifact's bucket(s). `+smartx -> json/benchmarks` is the
      structural delta. Read-only.
  Q2 (policy  -- the contract JOIN): JOIN the Q1 delta + the observed writers
      at HEAD against `graph_contracts`. A writer NOT in `canonical_writer`
      (or present in `forbidden_writers`) with NO accompanying ratified
      contract edit in the window = UNSANCTIONED. A ratified contract edit in
      the window = SANCTIONED (the recorded never-widen sign-off).
  Q3 (value -- period_defs) is CVO-owned (PRD section 9 value_check homing) and
      is NOT implemented here -- this engine does structure + policy only.

Data sources (dev-box read path -- the Nessie REST catalog is in-VPC ONLY):
  * graph (nodes+edges WITH full edge properties incl. `via_role`) <- the
    archived derive snapshots `s3://opal-313476888478-globgrph/snapshots/...`.
    The persisted Iceberg `graph_edges` table is STRIPPED to 5 columns and
    drops `via_role`, so it cannot carry the writer-principal the contract is
    keyed on -- the snapshot tarball is the full-fidelity source.
  * graph_contracts <- the Iceberg table read via pyiceberg `StaticTable`
    (located via the F6 branch-head marker, else newest-metadata mtime scan --
    mirrors kuzu_nessie_load). The table starts EMPTY (CVO TO-3 authors rows);
    an empty/unreachable table degrades to "uncontracted = LOUD unreviewed",
    never a crash.

Grain note (flagged to CVO): WRITES edges are BUCKET-grain (S3 collapsed to
bucket), so the JOIN is "who can write the contracted bucket vs
canonical_writer" -- aligned with the seed's iam_backstop
(DenyNonYangWriteBenchmarks). `artifact_keys` are object-level; each maps to
its bucket for the JOIN. opal-data-portal-v2 has ~74 writer-roles (shared
bucket), so `forbidden_writers` (the KNOWN-bad set) is the high-signal v1
trigger; a non-forbidden non-canonical writer is an advisory-soft note.

Best-effort everywhere: any S3 / Iceberg / parse failure degrades to a loud
ADVISORY note + a clean verdict. This engine NEVER raises to its callers and
NEVER changes a commit's exit code (the TO-2 advisory ramp; the hard-block
flip is a later one-line CTO ramp-flip).
"""
from __future__ import annotations

import datetime as _dt
import io
import json
import os
import tarfile

WAREHOUSE_BUCKET = "opal-313476888478-globgrph"
WAREHOUSE_NS_PREFIX = "warehouse/globgrph/"
MARKER_KEY = "warehouse/_branch_head.main.json"
SNAPSHOTS_LATEST_KEY = "snapshots/latest.txt"
CONTRACTS_TABLE = "graph_contracts"

_HERE = os.path.dirname(os.path.abspath(__file__))
# org/modules/graph -> modules -> org -> workspace root
_WS = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))


# ---------------------------------------------------------------------------
# small AWS helpers (all best-effort)
# ---------------------------------------------------------------------------

def _s3():
    """S3 client with SHORT timeouts: this runs on the commit-time path
    (comp-surface-check), so a slow/hung S3 must fail fast into an advisory skip,
    never stall a commit. 3s connect / 5s read / 1 retry."""
    import boto3
    cfg = boto3.session.Config(connect_timeout=3, read_timeout=5,
                               retries={"max_attempts": 1})
    return boto3.client("s3", region_name="us-east-1", config=cfg)


def _read_marker():
    try:
        obj = _s3().get_object(Bucket=WAREHOUSE_BUCKET, Key=MARKER_KEY)
        return json.loads(obj["Body"].read())
    except Exception:
        return None


def _latest_table_metadata(s3, table_prefix: str):
    """Newest *.metadata.json for one table (mtime fallback when the marker does
    not carry the table). None if not found.

    The S3 Prefix is SCOPED to the table dir (warehouse/globgrph/<table>) so S3
    filters server-side and returns only that table's handful of objects -- NOT
    the whole ~56k-object warehouse. Scanning the full prefix here would stall
    the commit-time path; the tight prefix keeps "absent" cheap to discover too
    (0 objects returned -> fast None)."""
    newest = None
    scoped = WAREHOUSE_NS_PREFIX + table_prefix
    try:
        pg = s3.get_paginator("list_objects_v2")
        for page in pg.paginate(Bucket=WAREHOUSE_BUCKET, Prefix=scoped):
            for obj in page.get("Contents", []):
                if obj["Key"].endswith(".metadata.json"):
                    if newest is None or obj["LastModified"] > newest[1]:
                        newest = (obj["Key"], obj["LastModified"])
    except Exception:
        return None
    if newest is None:
        return None
    return f"s3://{WAREHOUSE_BUCKET}/{newest[0]}"


def contracts_metadata_uri():
    """Locate the graph_contracts Iceberg metadata.json. Prefer the F6
    branch-head marker (the true HEAD); else the newest-metadata mtime scan.
    Returns the s3:// metadata URI or None (table not created yet)."""
    marker = _read_marker()
    tm = ((marker or {}).get("table_metadata") or {})
    loc = (tm.get(CONTRACTS_TABLE) or {}).get("metadata_location")
    if loc:
        return loc
    try:
        return _latest_table_metadata(_s3(), CONTRACTS_TABLE)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# contracts table read (StaticTable -- in-VPC catalog NOT required)
# ---------------------------------------------------------------------------

def _coerce_map(v) -> dict:
    if isinstance(v, dict):
        return {str(k): ("" if vv is None else str(vv)) for k, vv in v.items()}
    if isinstance(v, list):  # pyarrow map -> list of (k, v) pairs
        out = {}
        for item in v:
            try:
                k, vv = item
                out[str(k)] = "" if vv is None else str(vv)
            except Exception:
                continue
        return out
    return {}


def _coerce_list(v) -> list:
    if v is None:
        return []
    if isinstance(v, (list, tuple)):
        return [str(x) for x in v if x is not None]
    return [str(v)]


def _row_to_contract(row: dict) -> dict:
    enf = row.get("enforcement")
    if not isinstance(enf, dict):
        enf = {}
    return {
        "contract_id": str(row.get("contract_id") or ""),
        "surface": str(row.get("surface") or ""),
        "artifact_keys": _coerce_list(row.get("artifact_keys")),
        "canonical_writer": str(row.get("canonical_writer") or ""),
        "canonical_producer": str(row.get("canonical_producer") or ""),
        "source_of_truth": str(row.get("source_of_truth") or ""),
        "period_defs": _coerce_map(row.get("period_defs")),
        "models": _coerce_list(row.get("models")),
        "forbidden_writers": _coerce_list(row.get("forbidden_writers")),
        "enforcement": {
            "iam_backstop": str(enf.get("iam_backstop") or ""),
            "surface_gate": str(enf.get("surface_gate") or ""),
            "value_check": str(enf.get("value_check") or ""),
        },
        "ratified_by": _coerce_list(row.get("ratified_by")),
        "ratified_at": str(row.get("ratified_at") or ""),
        "active": bool(row.get("active")) if row.get("active") is not None else True,
    }


def load_contracts(metadata_uri: str | None = None, active_only: bool = True):
    """Read graph_contracts. Returns (contracts, status) where status is one of
    'ok' (table read; may be 0 rows), 'absent' (table not created yet), or
    'unavailable:<why>' (read failed -- treat as advisory). NEVER raises."""
    uri = metadata_uri or contracts_metadata_uri()
    if not uri:
        return [], "absent"
    try:
        from pyiceberg.table import StaticTable
        tbl = StaticTable.from_metadata(uri)
        rows = tbl.scan().to_arrow().to_pylist()
    except Exception as e:
        return [], f"unavailable:{type(e).__name__}"
    out = [_row_to_contract(r) for r in rows]
    if active_only:
        out = [c for c in out if c.get("active", True)]
    return out, "ok"


# ---------------------------------------------------------------------------
# graph snapshot read (full-fidelity derive JSON, WITH via_role on WRITES)
# ---------------------------------------------------------------------------

def _graph_from_tar_bytes(raw: bytes) -> dict:
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as tar:
        member = next(m for m in tar.getmembers() if m.name.endswith(".json"))
        return json.load(tar.extractfile(member))


def load_graph_snapshot(ref: str = "latest") -> dict:
    """Load a full derive-graph JSON. `ref` is one of:
      'latest'            -> snapshots/latest.txt pointer
      'YYYYMMDD'          -> snapshots/{date}/graph-{date}.tar.gz
      a local path        -> .json or .tar.gz on disk
      an s3://.../*.tar.gz key
    Returns the graph dict ({"edges":[...], "classes_data":{...}}). Raises on a
    genuinely unreadable ref (callers wrap best-effort)."""
    # local file
    if os.path.exists(ref):
        if ref.endswith(".tar.gz") or ref.endswith(".tgz"):
            with open(ref, "rb") as f:
                return _graph_from_tar_bytes(f.read())
        with open(ref, encoding="utf-8") as f:
            return json.load(f)
    s3 = _s3()
    if ref.startswith("s3://"):
        _, _, rest = ref.partition("s3://")
        bucket, _, key = rest.partition("/")
    elif ref == "latest":
        key = _s3().get_object(Bucket=WAREHOUSE_BUCKET, Key=SNAPSHOTS_LATEST_KEY)["Body"].read().decode().strip()
        bucket = WAREHOUSE_BUCKET
    else:  # a YYYYMMDD date
        date = ref
        bucket = WAREHOUSE_BUCKET
        key = f"snapshots/{date}/graph-{date}.tar.gz"
    raw = s3.get_object(Bucket=bucket, Key=key)["Body"].read()
    return _graph_from_tar_bytes(raw)


# ---------------------------------------------------------------------------
# NFRA_GCONTR.TO-5 -- live IAM-role resolution (fail-loud on an inert tripwire)
# ---------------------------------------------------------------------------

def live_iam_roles(graph: dict) -> set:
    """The set of EXTANT IAM role identifiers in the live graph
    (classes_data.iam.nodes -- each an IAM_ROLE node). Returns the id / name / arn
    forms so an EXACT match on any canonical role identity resolves.

    Used by q2_join (TO-5) to detect an INERT forbidden_writer: a forbidden_writers
    entry that resolves to 0 live IAM roles can NEVER fire (the exact-match never
    hits a non-existent principal), so a 'clean' verdict there is a FALSE NEGATIVE on
    a never-widen guard -- an IAM rename / authoring typo silently disarms it. We
    surface that LOUD rather than silently clean (no-silent-Unknown platform law)."""
    out: set = set()
    nodes = (graph.get("classes_data", {}).get("iam", {}) or {}).get("nodes", []) or []
    for n in nodes:
        if not isinstance(n, dict):
            if n:
                out.add(str(n))
            continue
        # the iam class is IAM_ROLE nodes; tolerate a missing/!=IAM_ROLE type defensively
        if n.get("type") and n.get("type") != "IAM_ROLE":
            continue
        for k in ("id", "name", "arn"):
            v = n.get(k)
            if v:
                out.add(str(v))
    return out


# ---------------------------------------------------------------------------
# Q1 -- WRITES-edge snapshot diff (structure)
# ---------------------------------------------------------------------------

def _bucket_arn(b: str) -> str:
    return b if b.startswith("arn:") else f"arn:aws:s3:::{b}"


def artifact_bucket(key: str) -> str:
    """s3://bucket/path/obj.json -> bucket (or 'bucket' if already bare)."""
    k = key.strip()
    if k.startswith("s3://"):
        k = k[len("s3://"):]
    return k.split("/", 1)[0]


def contract_bucket_arns(contract: dict) -> set:
    """The set of bucket ARNs governed by a contract's artifact_keys."""
    return {_bucket_arn(artifact_bucket(k)) for k in contract.get("artifact_keys", []) if k}


def writes_into(graph: dict, bucket_arns: set):
    """Return (named, wildcard) where:
      named    = set of (via_role, target_arn) WRITES edges into the buckets
      wildcard = set of via_role with a broad `*:writes` capability edge
    The wildcard set is the broad-s3-capability roles (advisory-soft -- a role
    that COULD write anything, not a concrete edge into THIS bucket)."""
    named, wildcard = set(), set()
    for e in graph.get("edges", []):
        if e.get("edge_type") != "WRITES":
            continue
        role = str(e.get("via_role") or "")
        tgt = str(e.get("target") or "")
        if tgt in bucket_arns:
            named.add((role, tgt))
        elif e.get("wildcard") and tgt.startswith("*:"):
            if role:
                wildcard.add(role)
    return named, wildcard


def q1_writes_diff(base_graph: dict, cur_graph: dict, contracts: list):
    """Per-contract structural delta of WRITES writer-edges into the contracted
    bucket(s). Returns {contract_id: {"added": [...], "removed": [...],
    "observed_now": [...], "buckets": [...]}}. added/removed/observed are sorted
    (via_role, target) tuples."""
    out = {}
    for c in contracts:
        buckets = contract_bucket_arns(c)
        if not buckets:
            continue
        base_named, _ = writes_into(base_graph, buckets) if base_graph else (set(), set())
        cur_named, cur_wild = writes_into(cur_graph, buckets)
        out[c["contract_id"]] = {
            "buckets": sorted(buckets),
            "observed_now": sorted(cur_named),
            "observed_wildcard_roles": sorted(cur_wild),
            "added": sorted(cur_named - base_named),
            "removed": sorted(base_named - cur_named),
        }
    return out


# ---------------------------------------------------------------------------
# Q2 -- the contract JOIN (policy)
# ---------------------------------------------------------------------------

def _parse_date(s: str):
    """Parse 'YYYY-MM-DD' or an ISO timestamp into a date; None if not a date
    (e.g. a Nessie commit hash)."""
    s = (s or "").strip()
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            return _dt.datetime.strptime(s[:len(fmt) + 6 if "%z" in fmt else len(fmt)], fmt).date()
        except Exception:
            continue
    # last resort: leading YYYY-MM-DD
    try:
        return _dt.date.fromisoformat(s[:10])
    except Exception:
        return None


def ratified_in_window(contract: dict, window: tuple | None) -> bool:
    """True if the contract's ratified_at marks a sign-off WITHIN the diff
    window (the recorded never-widen edit). window = (start_date, end_date) of
    `datetime.date`, or None (= 'no window known' -> conservative False).

    v1 convention: ratified_at is treated as a DATE. If it is a Nessie commit
    HASH (no date), we cannot date-bound it here and return False conservatively
    (false-clean-avoiding -- an unprovable sign-off does NOT grant a pass). The
    hash-based exact check is a CVO-convergence follow-on (ratified_at = the
    authorizing-commit hash; see the TO-2<->TO-3 schema-usage convergence)."""
    if not window:
        return False
    d = _parse_date(contract.get("ratified_at", ""))
    if d is None:
        return False
    start, end = window
    return start <= d <= end


def q2_join(contracts: list, q1_delta: dict, window: tuple | None = None,
            live_roles: set | None = None):
    """Classify each contract: CLEAN / WATCH / SANCTIONED / UNSANCTIONED /
    UNRESOLVED_FORBIDDEN_WRITER.
    Returns {contract_id: verdict} where verdict = {
        "status": "CLEAN"|"WATCH"|"SANCTIONED"|"UNSANCTIONED"|"UNRESOLVED_FORBIDDEN_WRITER",
        "canonical_writer": str,
        "observed_writers": [via_role...],
        "intruders": [via_role...],          # observed - {canonical_writer} (FULL set)
        "forbidden_hits": [via_role...],     # observed & forbidden_writers
        "added_forbidden": [via_role...],    # forbidden writer in the Q1 ADDED delta
        "unresolved_forbidden": [name...],   # forbidden entries naming 0 live IAM role (TO-5)
        "wildcard_roles": [via_role...],     # broad *:writes capability (advisory-soft)
        "ratified_in_window": bool,
        "reason": str,
    }.

    UNRESOLVED_FORBIDDEN_WRITER (TO-5): emitted when a forbidden_writers entry resolves
    to NO live IAM role (passed via `live_roles`) and is not itself observed -- the
    tripwire is INERT (an exact-match can never hit a non-existent principal), so a clean
    verdict would be a FALSE NEGATIVE on a never-widen guard. Ranked ABOVE WATCH (an inert
    guard is louder than shared-bucket capability noise) but BELOW a real forbidden hit. The
    match stays EXACT (no fuzzy-stem; the fix is to NAME forbidden_writers verbatim). When
    `live_roles is None` the check is skipped (back-compat).

    Trigger model (the LOW-FP refinement over the seed's literal "any intruder
    -> UNSANCTIONED"): on a SHARED bucket many roles legitimately hold s3:put
    (opal-data-portal-v2 has ~12 distinct non-canonical writer-roles), so a bare
    "non-canonical writer present" is noise -- it would pin every shared-bucket
    contract permanently UNSANCTIONED and make the eventual hard-block ramp
    impossible. The curated `forbidden_writers` set is the real never-widen
    tripwire (CVO's hand-audited KNOWN-bad principals + the IAM Deny backstop is
    PREFIX-scoped, which the bucket-grain WRITES edge overstates). So:
      * UNSANCTIONED  = a FORBIDDEN writer present (observed OR newly-added) AND
                        no ratified contract edit in the window. (BMKAUD: +smartx)
      * SANCTIONED    = a forbidden writer present BUT a ratified edit lands in
                        the window (the recorded never-widen sign-off).
      * WATCH         = non-canonical, non-forbidden writer(s) present (shared-
                        bucket capability noise) -- surfaced, NOT warned/blocked.
      * CLEAN         = only the canonical writer.
    This divergence from the literal seed is a documented fidelity choice
    (TO-2 RAVC); CVO can tighten artifact_keys / add a prefix dimension later."""
    out = {}
    for c in contracts:
        cid = c["contract_id"]
        d = q1_delta.get(cid)
        if d is None:
            continue
        canonical = c.get("canonical_writer", "")
        forbidden = set(c.get("forbidden_writers", []))
        observed = sorted({role for (role, _tgt) in d.get("observed_now", []) if role})
        added_roles = {role for (role, _tgt) in d.get("added", []) if role}
        intruders = sorted(r for r in observed if r and r != canonical)
        forbidden_hits = sorted(r for r in observed if r in forbidden)
        added_forbidden = sorted(added_roles & forbidden)
        wildcard_roles = sorted(d.get("observed_wildcard_roles", []))
        ratified = ratified_in_window(c, window)
        trigger = sorted(set(forbidden_hits) | set(added_forbidden))
        # TO-5 fail-loud-on-unresolved: a forbidden_writers entry that resolves to NO
        # live IAM role can never fire (exact-match vs a non-existent principal) -> the
        # tripwire is INERT. Only checked when the caller supplies the live-role set
        # (back-compat: live_roles=None -> [] -> behaviour unchanged). An OBSERVED
        # forbidden writer is resolved-by-writing, so it is excluded from `unresolved`
        # (it already counts as a real hit via forbidden_hits/trigger above).
        observed_set = set(observed)
        unresolved = sorted(
            fw for fw in forbidden
            if live_roles is not None and fw not in live_roles and fw not in observed_set
        )

        # TO-5 part-3 (CTO call 165140Z): forbidden_writers enforceability depends on GRAIN.
        # The derive's WRITES edges are BUCKET-grain (no key/prefix), so on a SHARED-BUCKET
        # surface a bucket-grain forbidden match cannot distinguish a real value-key breach
        # from a benign co-tenant write in the same bucket (CVO proved benchmark is exactly
        # this: smartx writes _smartx_-namespaced co-tenant keys, NOT yang's benchmark value
        # keys). Hard-flipping there is a FALSE POSITIVE on a never-widen guard. So a contract
        # whose forbidden_writers are only bucket-grain-checkable declares
        # enforcement.forbidden_writer_grain="bucket" (DECLARATIVE): the forbidden axis becomes
        # ADVISORY (annotated coarse), NEVER a hard UNSANCTIONED/UNRESOLVED -- enforcement is
        # canonical_writer + the value-limb (served-value provenance) + bucket policy.
        # DEFAULT = "bucket" (CTO 170120Z, fail-safe): WRITE data is bucket-grain today (no
        # key-grain derive yet), so a "key"-default would FALSE-POSITIVE on every shared bucket
        # (flag a benign co-tenant UNSANCTIONED) -- NOISY-by-default, not secure, and it stalls
        # the section-9 advisory->hard-block ramp by keeping the FP-rate high. It forfeits ZERO
        # real-breach coverage (canonical_writer + value-limb fire regardless; the forbidden axis
        # is defense-in-depth). A contract asserts grain="key" ONLY when the surface is genuinely
        # key-grain-enforceable (single-tenant bucket today, or ANY surface once the deferred
        # Option-A key-grain derive lands -> promote per-surface via the hook).
        fw_grain = str((c.get("enforcement") or {}).get("forbidden_writer_grain") or "bucket").lower()
        declarative = fw_grain == "bucket"
        declared_fb = sorted(set(forbidden_hits) | set(unresolved)) if declarative else []

        if declarative:
            # Advisory-only forbidden axis: never hard-flip. Status from the canonical/intruder
            # axis; the forbidden observations + unresolved names are carried as a coarse note.
            note = ("forbidden_writers DECLARATIVE (grain=bucket, coarse / possible "
                    "over-attribution on a shared bucket) -- enforced via canonical_writer + "
                    "value-limb, NOT the writer-axis; not hard-flipped [TO-5 part-3]")
            if intruders:
                status = "WATCH"
                reason = (f"{len(intruders)} non-canonical writer(s) hold s3:put on the shared "
                          f"bucket(s); {note}"
                          + (f"; declared-forbidden seen/unresolved: {declared_fb}" if declared_fb else ""))
            else:
                status = "CLEAN"
                reason = f"only canonical_writer={canonical!r} observed; {note}"
        elif trigger and ratified:
            status = "SANCTIONED"
            reason = (f"forbidden writer(s) {trigger} present BUT a ratified contract edit "
                      f"(ratified_at={c.get('ratified_at')!r}) lands in the window -- the "
                      f"recorded never-widen sign-off")
        elif trigger:
            status = "UNSANCTIONED"
            how = f"NEWLY-ADDED {added_forbidden}" if added_forbidden else f"observed {forbidden_hits}"
            reason = (f"FORBIDDEN writer(s) {how} into a contracted bucket; NO ratified contract "
                      f"edit in the window (ratified_at={c.get('ratified_at')!r}) -- a forbidden "
                      f"writer appeared and nobody re-drew the line (the BMKAUD class)")
        elif unresolved:
            # An inert never-widen guard is LOUDER than shared-bucket noise: rank above WATCH.
            status = "UNRESOLVED_FORBIDDEN_WRITER"
            reason = (f"forbidden_writer(s) {unresolved} resolve to 0 live IAM roles -- the "
                      f"never-widen tripwire is INERT (can never fire: exact-match vs a "
                      f"non-existent principal; an IAM rename or authoring typo silently disarmed "
                      f"it). FAIL-LOUD, NOT 0-hits-clean -- name forbidden_writers with verbatim "
                      f"live IAM role-ids (exact-match is correct; the NAMES are wrong). [TO-5]")
        elif intruders:
            status = "WATCH"
            reason = (f"{len(intruders)} non-canonical, non-forbidden writer(s) hold s3:put on the "
                      f"contracted bucket(s) (shared-bucket capability noise; advisory only) -- "
                      f"none are in forbidden_writers")
        else:
            status, reason = "CLEAN", f"only canonical_writer={canonical!r} observed"
        out[cid] = {
            "status": status,
            "canonical_writer": canonical,
            "observed_writers": observed,
            "intruders": intruders,
            "forbidden_hits": forbidden_hits,
            "added_forbidden": added_forbidden,
            "unresolved_forbidden": unresolved,  # TO-5: inert (0-live-resolution) forbidden entries
            "forbidden_grain": fw_grain,         # TO-5 part-3: "key" (enforced) | "bucket" (declarative)
            "forbidden_declarative": declared_fb,  # forbidden seen/unresolved on a declarative surface (advisory)
            "wildcard_roles": wildcard_roles,
            "ratified_in_window": ratified,
            "reason": reason,
        }
    return out


# ---------------------------------------------------------------------------
# surface -> contract resolution (for comp-surface-check)
# ---------------------------------------------------------------------------

def contract_for_surface(surface_id: str, contracts: list):
    """Return the contract governing a critical-surface id (e.g.
    'model_portfolios.benchmark'), matched against the contract's `surface`
    field (which embeds 'critical-surfaces:<id>'). None if uncontracted."""
    sid = (surface_id or "").strip()
    if not sid:
        return None
    for c in contracts:
        surf = c.get("surface", "")
        if sid in surf or surf == sid:
            return c
        # also match the bare id inside a 'critical-surfaces:<id> | pipescript:...' blob
        for tok in surf.replace("|", " ").split():
            if tok.endswith(sid) or tok == sid or tok == f"critical-surfaces:{sid}":
                return c
    return None


# ---------------------------------------------------------------------------
# high-level convenience: run the full structure+policy check
# ---------------------------------------------------------------------------

def run_contract_check(base_ref: str | None = None,
                       current_ref: str = "latest",
                       contracts=None,
                       window: tuple | None = None):
    """Load (snapshots + contracts as needed) and run Q1 then Q2. Returns
    (result, status) where result = {contract_id: {**q1, **q2_verdict}} and
    status in {'ok','absent','unavailable:...'}. Best-effort: a snapshot read
    failure returns ({}, 'unavailable:<why>')."""
    if contracts is None:
        contracts, cstatus = load_contracts()
    else:
        cstatus = "ok"
    if cstatus.startswith("unavailable"):
        return {}, cstatus
    if not contracts:
        return {}, ("absent" if cstatus == "absent" else "ok")  # ok-but-empty
    try:
        cur = load_graph_snapshot(current_ref)
        base = load_graph_snapshot(base_ref) if base_ref else None
    except Exception as e:
        return {}, f"unavailable:{type(e).__name__}"
    if window is None and base_ref is None:
        # default window = today only (commit-time Q2-at-HEAD). A contract whose
        # ratified_at is today is treated as a fresh sign-off.
        today = _dt.date.today()
        window = (today, today)
    q1 = q1_writes_diff(base, cur, contracts)
    # TO-5: resolve forbidden_writers against the live IAM-role set from the current
    # snapshot -> an inert (0-live-resolution) tripwire reads LOUD, not silently clean.
    q2 = q2_join(contracts, q1, window, live_roles=live_iam_roles(cur))
    result = {}
    for cid, dd in q1.items():
        result[cid] = {**dd, **q2.get(cid, {})}
    return result, "ok"
