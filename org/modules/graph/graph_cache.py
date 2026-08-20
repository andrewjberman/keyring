#!/usr/bin/env python3
"""
graph_cache.py -- shared query-vs-rebuild freshness contract for the comp-* graph tools.

NFRA_GRAPHS D2 + D3. One uniform freshness model so every rebuild-capable local
graph tool answers "query vs rebuild" the same way (the executable half of the
query-vs-rebuild doctrine catalogued in org/modules/graph/graph-call-manifest.yaml):

  - DEFAULT (no flag): QUERY. Use the cached artifact if it exists and is within
    the TTL (default 300s -- matches the trace-graph 5-min cache in cli.py
    _get_graph). Rebuild only when the cache is missing or past the TTL. The cheap
    warm path agents hit by default.
  - --fresh: re-derive if STALE. Stale = TTL expired OR the source fingerprint has
    drifted since the cache was built. Stricter than DEFAULT: a within-TTL cache is
    still rebuilt when its source files changed under it.
  - --force: always re-derive, regardless of TTL or fingerprint.

`--force` wins over `--fresh` wins over DEFAULT.

The fingerprint is a stat-only (max-mtime, file-count) signal over the source
(dir, glob) pairs that feed a build -- it never reads or parses file contents, so
it stays far cheaper than the rebuild it guards. It is computed at store time
(the build path is already slow) and only re-computed for comparison under
--fresh.

Caches live under .comp-graph/ (gitignored). Payloads are pickled CachePayload
records carrying built_at + the source fingerprint. A load that fails to unpickle
(class drift, truncation) degrades to a cache miss -> rebuild, exactly like the
trace-graph loader's `except Exception: pass`.
"""

from __future__ import annotations

import os
import pickle
import sys
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
WORKSPACE = _THIS_DIR.parent.parent.parent
CACHE_DIR = WORKSPACE / ".comp-graph"
DEFAULT_TTL = 300  # 5 min -- identical to the trace-graph cache (cli.py _get_graph)


class Freshness(str, Enum):
    """The three uniform query-vs-rebuild modes."""
    DEFAULT = "default"   # query within TTL (cheap warm path)
    FRESH = "fresh"       # re-derive if stale (TTL expired OR source drift)
    FORCE = "force"       # always re-derive


FRESH_DEPRECATION = (
    "WARN: --fresh is a no-op alias of default since the head-pin (NFRA_GRAPHUNI P2/D2) -- "
    "default already rebuilds on TTL expiry or source drift. Use default, or --force to rebuild. "
    "This flag is removed next cycle."
)


def resolve_freshness(force: bool = False, fresh: bool = False) -> Freshness:
    """Map the --force / --fresh flag pair to a mode. --force wins over --fresh.

    `--fresh` IS A NO-OP ALIAS OF DEFAULT and is deprecated. load() takes ONE branch for
    DEFAULT/FRESH -- "hit iff cache exists, age < ttl, AND the fingerprint matches" -- and cached()
    supplies the fingerprint for both modes. Exercised across every reachable state, with a control
    that CAN see a difference:

        warm, sources unchanged   default=HIT   fresh=HIT   IDENTICAL
        within TTL, drifted       default=MISS  fresh=MISS  IDENTICAL
        TTL expired, unchanged    default=MISS  fresh=MISS  IDENTICAL
        CONTROL: force vs default default=HIT   force=MISS  DIFFER

    Root cause is honest history: NFRA_GRAPHUNI P2/D2's head-pin CORRECTLY made DEFAULT honor the
    source fingerprint (killing the stale-cache-phantom class, the 1347-vs-1337 catch) and in doing
    so collapsed FRESH into DEFAULT. Nobody retired the flag.

    It WARNS rather than silently aliasing (a silent alias is a lying affordance) or silently
    dropping (it is user-visible). CTO 20260709T201214Z: "remove the lie without breaking the
    contract." Removed next cycle.
    """
    if force:
        return Freshness.FORCE
    if fresh:
        sys.stderr.write(FRESH_DEPRECATION + "\n")
        return Freshness.FRESH   # behaviourally == DEFAULT; kept so the mode name stays truthful
    return Freshness.DEFAULT


def add_freshness_args(parser) -> None:
    """Attach the uniform freshness flags to an argparse parser/subparser.

    The contract is THREE states (CTO GO 20260709T201214Z): default / --check / --force. `--check`
    is owned by each tool (it is a probe over that tool's own artifact); this helper attaches the
    two shared routing flags.
    """
    parser.add_argument(
        "--fresh", action="store_true",
        help="DEPRECATED no-op alias of default (warns; removed next cycle).",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Always re-derive, ignoring the cache (TTL + fingerprint).",
    )


# Directories pruned during the fingerprint walk: vendored / build / cache trees
# that hold no graph-source files yet dominate a naive rglob (the .terraform
# provider cache under infra/aws is ~thousands of files and made an unpruned
# infra/aws *.tf walk ~1.3s -- larger than the rebuild it was meant to cheaply
# guard). Pruning them keeps the walk O(relevant files).
_PRUNE_DIRS = frozenset({
    ".terraform", "node_modules", "__pycache__", ".git", ".runtmp",
    ".mypy_cache", ".pytest_cache", ".next", "dist", "build", "staging",
    ".comp-graph", ".venv", "venv",
})


def _iter_source_files(sources):
    """The ONE file enumeration both fingerprints below ride (same `_PRUNE_DIRS`
    pruning, same glob semantics). Two walks that could disagree would make the
    two fingerprints answer different questions about different file SETS -- the
    shared-derivation discipline, applied to the enumerator."""
    import fnmatch

    for base, pattern in sources:
        base = Path(base)
        if not base.exists():
            continue
        if base.is_file():
            yield base
            continue
        for root, dirs, filenames in os.walk(base):
            # Prune heavy irrelevant subtrees in place (os.walk respects this).
            dirs[:] = [d for d in dirs if d not in _PRUNE_DIRS]
            for fn in filenames:
                if fnmatch.fnmatch(fn, pattern):
                    yield Path(os.path.join(root, fn))


def source_fingerprint(sources) -> tuple:
    """Cheap staleness signal over source (dir, glob-pattern) pairs.

    Returns (max_mtime_rounded, file_count). Stat-only -- never opens file
    contents, and prunes vendored/build/cache dirs (`_PRUNE_DIRS`) mid-walk so it
    stays far cheaper than the parse/AST rebuild it guards. A changed/added/removed
    source file moves either the max mtime or the count.

    KNOW THE INSTRUMENT'S DOMAIN: this answers "did anything get TOUCHED on this
    machine" -- the right question for a DEVICE-LOCAL cache. It is the WRONG
    question for a SHARED artifact's predicate, because a fresh checkout/pull
    re-stamps every mtime BY CONSTRUCTION on a content-identical tree (measured
    at site-Z, CTO ruling addendum @6ae67e724f). Shared predicates use
    `content_fingerprint` below.
    """
    max_mtime = 0.0
    count = 0
    for p in _iter_source_files(sources):
        try:
            st = p.stat()
        except OSError:
            continue
        count += 1
        if st.st_mtime > max_mtime:
            max_mtime = st.st_mtime
    return (round(max_mtime, 3), count)


def content_fingerprint(sources, rel_root=None) -> tuple:
    """CHECKOUT-INVARIANT staleness signal: (sha256-hex-over-content, file_count).

    Answers "did source CONTENT change" -- the question a SHARED tracked
    artifact's predicate must ask (CTO ruling addendum @6ae67e724f, instance 3 of
    the device-axis pair @4484d55608): a fresh checkout/pull re-stamps every
    mtime while bytes stay identical, so the stat-only sibling above manufactures
    staleness on a content-identical tree.

    Hash = sha256 over each file's REL_ROOT-relative posix path + normalized size
    + normalized bytes, in sorted-path order. Properties, each load-bearing:
      - path RELATIVE to `rel_root` (pass the workspace root): two devices'
        checkouts live under different absolute prefixes, and hashing absolute
        paths would break the exact cross-device equality this exists to provide;
      - CRLF normalized to LF before hashing: line-ending materialization is a
        CHECKOUT property (autocrlf), not a content change -- a diff that is
        ONLY line endings is the mtime class one layer down;
      - sorted order: os.walk order is filesystem-dependent;
      - unreadable files SKIPPED like the sibling's failed stat (count excludes
        them) -- absence surfaces as a count change, never a crash.
    Costs one read of every source file; the CACHES deliberately keep the
    stat-only sibling (cache invalidation wants cheap-and-device-local; a shared
    predicate wants checkout-invariant)."""
    import hashlib

    h = hashlib.sha256()
    count = 0

    def _key(p):
        s = str(p)
        if rel_root:
            try:
                s = os.path.relpath(s, rel_root)
            except ValueError:
                pass
        return s.replace(os.sep, "/")

    for p in sorted(_iter_source_files(sources), key=_key):
        try:
            data = p.read_bytes()
        except OSError:
            continue
        data = data.replace(b"\r\n", b"\n")
        h.update(_key(p).encode("utf-8", "replace"))
        h.update(b"\0")
        h.update(str(len(data)).encode("ascii"))
        h.update(b"\0")
        h.update(data)
        count += 1
    return (h.hexdigest(), count)


@dataclass
class CachePayload:
    built_at: float
    fingerprint: tuple = field(default_factory=tuple)
    obj: object = None


def cache_file(name: str) -> Path:
    """Cache path for a logical graph name (e.g. 'platinum.dag.bd')."""
    return CACHE_DIR / f"{name}.cache"


def load(name: str, freshness: Freshness = Freshness.DEFAULT,
         ttl: int = DEFAULT_TTL, current_fingerprint=None):
    """Return (obj, meta) if the cache is usable under `freshness`, else (None, None).

    meta = {"built_at", "age", "fingerprint"} for reporting. Rules:
      - FORCE  -> always miss.
      - DEFAULT/FRESH -> hit iff cache exists, age < ttl, AND (current_fingerprint is None
                  OR it matches the stored fingerprint). Source drift -> miss. (NFRA_GRAPHUNI
                  P2/D2 (b): DEFAULT is now head-pinned -- honors the fingerprint like FRESH, so
                  no tool serves a divergent-vintage cache. cached() supplies the fingerprint for
                  both modes.)
    """
    if freshness == Freshness.FORCE:
        return None, None
    fp = cache_file(name)
    if not fp.exists():
        return None, None
    try:
        with open(fp, "rb") as f:
            payload = pickle.load(f)
    except Exception:
        return None, None
    if not isinstance(payload, CachePayload):
        return None, None
    age = time.time() - payload.built_at
    if age >= ttl:
        return None, None
    # NFRA_GRAPHUNI P2/D2 (b) HEAD-PIN (JOINT VERDICT 20260701): honor the source fingerprint in
    # DEFAULT too (was FRESH-only) -- a within-TTL cache that DRIFTED from the current source is a
    # MISS (rebuild), never a divergent-vintage serve. Kills the stale-cache-phantom class for every
    # gc.cached tool (comp-platinum), matching cli.py::_get_graph. FORCE already returned above.
    if current_fingerprint is not None and payload.fingerprint != tuple(current_fingerprint):
        return None, None
    meta = {"built_at": payload.built_at, "age": age, "fingerprint": payload.fingerprint}
    return payload.obj, meta


def store(name: str, obj, fingerprint=None) -> Path:
    """Pickle `obj` to the named cache with built_at + fingerprint. Atomic replace."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    payload = CachePayload(
        built_at=time.time(),
        fingerprint=tuple(fingerprint) if fingerprint is not None else tuple(),
        obj=obj,
    )
    dest = cache_file(name)
    tmp = Path(str(dest) + ".tmp")
    with open(tmp, "wb") as f:
        pickle.dump(payload, f, protocol=pickle.HIGHEST_PROTOCOL)
    os.replace(tmp, dest)
    return dest


def cached(name: str, builder, sources, freshness: Freshness = Freshness.DEFAULT,
           ttl: int = DEFAULT_TTL):
    """Memoize `builder()` to the named cache under the freshness contract.

    `sources` is the (dir, glob) list whose mtime/count fingerprint gates --fresh.
    The fingerprint is computed once (eagerly only under --fresh, else lazily at
    store time) and stored with the payload so a later --fresh call can compare.
    """
    # HEAD-PIN (b): compute the fingerprint for DEFAULT too (not just FRESH) so a drifted within-TTL
    # cache rebuilds -- head-pinned, no divergent vintage. FORCE skips it (always rebuilds anyway).
    cur_fp = None if freshness == Freshness.FORCE else source_fingerprint(sources)
    obj, _meta = load(name, freshness, ttl=ttl, current_fingerprint=cur_fp)
    if obj is not None:
        return obj
    obj = builder()
    fp = cur_fp if cur_fp is not None else source_fingerprint(sources)
    store(name, obj, fp)
    return obj


def cache_meta(name: str):
    """Stat a named cache without unpickling its full object graph for `status`.

    Returns {"exists", "path", "built_at", "age", "fingerprint", "size"} or
    {"exists": False, "path": ...}. Unpickles the payload (cheap header + object,
    but we only read the metadata fields); a corrupt payload reports exists=True
    with built_at=None so status can flag it.
    """
    fp = cache_file(name)
    if not fp.exists():
        return {"exists": False, "path": fp}
    info = {"exists": True, "path": fp, "size": fp.stat().st_size}
    try:
        with open(fp, "rb") as f:
            payload = pickle.load(f)
        if isinstance(payload, CachePayload):
            info["built_at"] = payload.built_at
            info["age"] = time.time() - payload.built_at
            info["fingerprint"] = payload.fingerprint
        else:
            info["built_at"] = None
    except Exception:
        info["built_at"] = None
    return info
