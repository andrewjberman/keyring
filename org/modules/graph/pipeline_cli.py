#!/usr/bin/env python3
"""
comp-pipescript -- authoritative pipeline dependency tool.

Usage:
    comp-pipescript dag                        # full execution DAG with I/O edges
    comp-pipescript io D_00                    # inputs + outputs for one script
    comp-pipescript chain downstream           # show chain membership + order
    comp-pipescript chain full                 # show full chain
    comp-pipescript feeds D_00                 # what scripts feed D_00 (upstream)
    comp-pipescript consumers D_00             # what scripts consume D_00 output
    comp-pipescript overlap D_00 D_03          # shared S3 artifacts between two scripts
    comp-pipescript inject                     # inject pipeline edges into comp-trace graph
    comp-pipescript stats                      # graph statistics

Data sources (authoritative, not heuristic):
    lib/s3_layout.py      -- every S3 key as a named constant
    gold_dispatch.sh      -- execution order, chains, groups, catalog
    each script's AST     -- from lib.s3_layout import (...) block
"""
from __future__ import annotations  # lazy annotations: quoted 'list[dict]' hints resolve on py39 (FA100)

import argparse
import ast  # module-scope so quoted 'ast.FunctionDef' forward-ref annotations resolve (bodies use local `import ast as _ast`)
import json
import os
import re
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))
sys.path.insert(0, str(_WORKSPACE / ".tools"))  # safe_deploy_core lives in .tools/

import _compbudget  # noqa: E402 -- Rule T's one shared budget carrier

# NFRA_TOOLPASS C: the deployed-guard's held-BUCKET check + lift signal delegate to sovereign_held.
from org.modules.graph.sovereign_held import is_held_bucket, include_held  # noqa: E402
from org.modules.graph.extract_pipeline import (  # noqa: E402
    build_pipeline_dag, inject_pipeline_edges,
    build_inf_gold_dag, build_silver_dag, build_multi_pipeline_dag,
    build_inf_manual_api_dag, build_mdpf_dag,
    _parse_dispatch, _parse_orion_dispatch,
)

_PIPELINE_CHOICES = ("bd-gold", "inf-gold", "bd-silver", "inf-silver", "bd-bronze", "inf-bronze", "cot-bronze", "inf-manual-api", "mdpf", "cot-gold", "cot-silver", "cot", "advi", "all", "bd", "inf")

# ---------------------------------------------------------------------------
# NFRA_DEBTSCAN.TOOL-01: single-source tree registry for the all-trees deployed
# sweep + --firm/path-autodetect scope resolution.
#
# Firm trees (bd/inf/cot) derive bucket+label from safe_deploy_core.PIPELINE_MAP --
# the canonical deploy map (CLAUDE.md Rule 13) -- so the firm-bucket mapping can never
# drift from the deploy gate. mdpf is appended as a CHECK-ONLY tree: it is deliberately
# NOT in the deploy-gate PIPELINE_MAP (Rule 13 = bd/inf/cot; mdpf deploys via its own
# mechanism and uses a non-standard, internally-INCONSISTENT S3 layout -- both
# code/<layer>/ and code/scripts/<layer>/ exist on opal-data-mdpf, so it cannot live in
# file_to_s3_target's single-layout derivation). comp-pipescript STILL checks its
# deployed status because MDPF_COUNTS (2026-06-05) proved an mdpf script can strand stale
# on S3 -- the exact blind spot this TO closes.
try:
    from safe_deploy_core import PIPELINE_MAP as _DEPLOY_PIPELINE_MAP  # noqa: E402
except Exception:  # defensive: .tools/ unimportable in some invocation contexts
    # Fallback MUST stay byte-equal to safe_deploy_core.PIPELINE_MAP (Rule 13).
    _DEPLOY_PIPELINE_MAP = {
        "black_diamond": ("opal-data-bd", "bd"),
        "inf": ("opal-data-inf", "inf"),
        "cot": ("opal-data-cot", "cot"),
    }

# CODE_TREES is the ONE declaration of per-(tree, layer) repo homes + S3 prefixes
# (safe_deploy_core). DELIBERATELY NO FALLBACK COPY: a hand-maintained duplicate
# here is precisely the divergence this table was introduced to end -- the 4-vs-6
# mdpf layer drift lived in exactly such a restatement. If the import fails we
# carry None and the consumer reports UNCOVERED loudly; it never enumerates a
# guessed layer set.
try:
    from safe_deploy_core import CODE_TREES as _CODE_TREES  # noqa: E402
except Exception:
    _CODE_TREES = None

def classify_digest(local_bytes, s3_etag):
    """Compare a local file's bytes to an S3 ETag. Returns (status, info_lines).

    PURE and module-level ON PURPOSE: the comparison used to live inside a closure, so the
    only way to exercise it was a live S3 sweep -- which cannot plant a mutant and therefore
    could only ever demonstrate the MATCH arm. A fix whose failing arm is unreachable is not
    verified. tests/test_pipescript_digest.py exercises THIS function, not a copy of it.

    A DIGEST WITHOUT ITS NORMALISATION IS NOT AN IDENTITY. Every verdict prints its basis.
    """
    import hashlib as _h
    local_md5 = _h.md5(local_bytes).hexdigest()

    # RULE 28 Q7 -- what does this return when it CANNOT answer, and is that DISTINGUISHABLE
    # from a genuine STALE? A multipart-upload ETag is "<md5-of-md5s>-<partcount>" and is NOT
    # the object's md5, so NO local digest can ever equal it. Comparing anyway renders a
    # permanent STALE indistinguishable from a real one -- the same defect class this function
    # exists to remove, one cause over. Say "cannot answer" instead.
    if "-" in s3_etag:
        return "ETAG_NOT_COMPARABLE", [
            "s3 ETag:  %s  (multipart -- NOT an md5 of the object)" % s3_etag,
            "basis:    NONE -- md5 comparison is undefined for a multipart ETag.",
            "          This is NOT a staleness verdict.",
        ]

    if local_md5 == s3_etag:
        return "MATCH", ["basis:  raw bytes (working tree and S3 object are byte-identical)"]

    # Line-ending normalisation ONLY -- collapses CRLF->LF and nothing else, so a real content
    # difference still reports STALE. The fix cannot manufacture a false MATCH.
    lf_bytes = local_bytes.replace(b"\r\n", b"\n")
    if lf_bytes != local_bytes:
        lf_md5 = _h.md5(lf_bytes).hexdigest()
        if lf_md5 == s3_etag:
            return "MATCH", [
                "basis:  LF-NORMALISED -- working tree is CRLF, S3 object is LF; content IDENTICAL",
                "        raw local md5 %s != s3 %s" % (local_md5, s3_etag),
                "        LF  local md5 %s == s3 %s" % (lf_md5, s3_etag),
            ]
        return "STALE", [
            "local raw: %s" % local_md5,
            "local LF:  %s" % lf_md5,
            "s3:        %s" % s3_etag,
            "basis:     BOTH raw and LF-normalised digests differ from S3 -- a real content difference.",
        ]
    return "STALE", [
        "local:  %s" % local_md5,
        "s3:     %s" % s3_etag,
        "basis:  raw bytes; working tree has no CRLF, so normalisation would not change this.",
    ]



def resolve_pipeline_from_arg(raw_script: str) -> str:
    """Map a `deployed` filter argument to the pipeline-key whose branch handles it.

    THREE CASES, in precedence order, and the third is deliberately preserved:

    1. DATA-DIR PATH -- `data/<dir>/scripts/...` where <dir> owns its own tree
       (black_diamond / inf / cot / mdpf). Unchanged behaviour.
    2. CROSS-TREE REPO HOME -- a path under a repo home DECLARED by CODE_TREES but
       whose directory is not itself a tree name. mdpf's assets_gold + silver layers
       are fed from `data/assets/`, which is NOT a data-dir key, so case 1 matched
       nothing and these fell to bd-gold: WRONG TREE in the header, all-zero summary,
       rc=0 -- a deploy-verification instrument failing OPEN, on the exact path shape
       the cottonwood STALE findings came from (CTO measured it himself, 213109Z).
       DERIVED from CODE_TREES, never a fourth hardcoded dir list.
    3. BARE ID -> 'bd-gold'. **PRESERVED DELIBERATELY** (documented backward-compat
       for bare bd ids like D_00; CTO made preservation an explicit requirement).
       This is NOT the bug case 2 fixes: the bug was a PATH naming a real tree and
       resolving to the wrong one. A bare id cannot reach cases 1 or 2 at all --
       both require a `data/.../` prefix -- so closing the path case leaves this
       interface untouched BY CONSTRUCTION rather than by luck.
    """
    np = (raw_script or "").replace("\\", "/")
    for _dir, _pk in _DATADIR_TO_PIPELINE.items():
        if f"data/{_dir}/scripts/" in np or np.startswith(f"data/{_dir}/"):
            return _pk
    if _CODE_TREES is not None:
        # LONGEST-PREFIX across every declared repo home (TRUNCLASS PSCRIPT2 P1, mirroring
        # file_to_s3_target's OWN documented rule -- safe_deploy_core's 2026-08-18 advi row).
        # The prior first-match dict-order iteration let mdpf's `data/assets/scripts/gold`
        # home shadow advi's LONGER `data/assets/scripts/gold/runners_49f` subtree: standalone
        # invocations swept the mdpf tree, matched 0, and emitted a clean false-ABSENT while
        # the SAME file verified correctly inside safe-deploy (which rides file_to_s3_target).
        # THAT first-match-vs-longest-prefix split was the standalone/in-harness divergence point.
        best = None  # (len(repo_home), pipeline_key) -- longest declared home wins
        for tree in _CODE_TREES.values():
            for repo_home, _prefix in tree["layers"].values():
                if np.startswith(repo_home + "/"):
                    resolved = _FIRM_TO_PIPELINE.get(tree["label"])
                    if resolved and (best is None or len(repo_home) > best[0]):
                        best = (len(repo_home), resolved)
        if best is not None:
            return best[1]
    # Case 3 SUPERSEDED (Andrew-direct stub ruling 2026-07-30, extending @10d1bb29e3 to
    # `deployed` after ~C's exercise showed a mirrored bare basename silently answering
    # for bd with a clean MATCH rc=0 -- the exact wrong-tree class, on the deploy verifier
    # itself). The former deliberate 'bd-gold' backward-compat fallback is the silent
    # default the ruling kills: a bare id now returns None and the caller REFUSES with
    # the disk-scan list. Path-qualified resolution (cases 1-2) is untouched; WS4 owns
    # the proper resolver.
    return None


# firm label -> the cmd_deployed pipeline-key whose branch enumerates that tree
# (gold + silver for the firm; mdpf covers its 4 layers in its own branch).
_LABEL_TO_DEPLOYED_PIPELINE = {"bd": "bd-gold", "inf": "inf-gold", "cot": "cot-gold"}

# data-dir name -> pipeline-key (generalizes the former cot-only path auto-detect to
# every tree). Built from the canonical map; mdpf appended (check-only).
_DATADIR_TO_PIPELINE = {
    dirname: _LABEL_TO_DEPLOYED_PIPELINE[label]
    for dirname, (_bucket, label) in _DEPLOY_PIPELINE_MAP.items()
    if label in _LABEL_TO_DEPLOYED_PIPELINE
}
_DATADIR_TO_PIPELINE["mdpf"] = "mdpf"


def _discover_script_trees():
    """WS-1 THE PREDICATE: re-derive the script-tree universe from the FILESYSTEM at call time.

    Returns {tree: sorted[layer]} for every `data/<tree>/scripts/<layer>/` on disk -- NOT a frozen
    list. This is the roster-to-predicate move (Andrew-direct 2026-08-05: comp-pipescript "needs to
    be a script io generalist, not bound to a handful of gold pipelines"), and it is the same
    a-predicate-is-not-a-roster class CTO ruled 2026-08-04.

    MEASURED, which is why a predicate and not an extended list: `_DATADIR_TO_PIPELINE` derives from
    the DEPLOY map (4 trees / 262 scripts). The filesystem carries TEN trees -- assets(77, the
    OPAL_ASSETS monolith, DEPLOYABLE per Rule 13), smartx, seeking-alpha, etfs, demo, yang_pkl -- so
    52.6% of data/*/scripts .py had no resolvable home. A longer hand-list would have gone stale the
    next time someone adds a tree; a predicate cannot.
    """
    trees = {}
    root = _THIS_DIR.parent.parent.parent
    scripts_root = root / "data"
    if not scripts_root.is_dir():
        return trees
    for tree_dir in sorted(scripts_root.iterdir()):
        sdir = tree_dir / "scripts"
        if not sdir.is_dir():
            continue
        layers = sorted(d.name for d in sdir.iterdir() if d.is_dir() and not d.name.startswith("__"))
        if layers:
            trees[tree_dir.name] = layers
    return trees


def _resolve_tree_from_path(raw):
    """Parse `data/<tree>/scripts/<layer>/...` -> (tree, layer, in_roster) for ANY tree on disk.

    THE DISTINCTION THIS TURNS ON, and it is what makes WS-1 additive rather than a relaxation of
    the 07-30 ruling: that ruling forbids a SILENT GUESS about which tree a script belongs to (the
    old bd-gold default returned clean zeros for other trees' scripts). A path that NAMES ITS OWN
    TREE is not a guess -- it is the caller stating the tree explicitly, in the argument itself. So
    refusing a fully-qualified path for want of a --pipeline flag is OVER-refusal: it demands the
    caller repeat, in a flag, what they already said in the path.

    Returns None when the argument does not name a tree -- and a bare id still refuses, unchanged,
    because for a bare id there genuinely is nothing to resolve from.
    """
    p = (raw or "").replace("\\", "/").strip()
    if "data/" not in p:
        return None
    seg = p.split("data/", 1)[1].split("/")
    if len(seg) < 3 or seg[1] != "scripts":
        return None
    tree, layer = seg[0], seg[2]
    known = _discover_script_trees()
    if tree not in known:
        return None
    return (tree, layer, tree in _DATADIR_TO_PIPELINE)

# --firm flag value -> pipeline-key.
_FIRM_TO_PIPELINE = {"bd": "bd-gold", "inf": "inf-gold", "cot": "cot-gold", "mdpf": "mdpf",
                     "advi": "advi"}  # advi: the 49F runner chain (PSCRIPT2; key = CODE_TREES label)


def _autowalk_pipeline_for_script(raw_id):
    """F2 (NFRA_COMPTOOL_USEPATHS, Andrew-direct 2026-06-25): resolve a BARE gold-script id
    (no path, no --firm) to its OWNING pipeline by walking the gold trees -- so a non-bd id
    like `mdpf_aggregate_aua` routes to its real pipeline instead of falling to the bd-gold
    default -> 'Unknown script' (the bd-only-id-convention gap COO/AE surfaced for MDPF).
    Registry-primary + auto-walk-fallback: this is the auto-walk fallback (the explicit
    registry layers on top later). Precise match only (exact stem / id-prefix-before-dot);
    ambiguous (id in >1 tree) -> None so the caller's normal disambiguation handles it."""
    import os as _os
    stem = _os.path.basename(str(raw_id or "")).replace(".py", "").strip()
    if not stem:
        return None
    su = stem.upper()
    hits = []
    for _dir, _pk in _DATADIR_TO_PIPELINE.items():
        gold = _WORKSPACE / "data" / _dir / "scripts" / "gold"
        if not gold.is_dir():
            continue
        for f in gold.glob("*.py"):
            fu = f.stem.upper()
            if su == fu or fu.startswith(su + ".") or fu.split(".")[0] == su:
                hits.append(_pk)
                break
    uniq = sorted(set(hits))
    return uniq[0] if len(uniq) == 1 else None

# Ordered (pipeline-key, bucket) the no-arg sweep iterates. Firm trees from the canonical
# map (each reads ONLY its own bucket -- firm separation); mdpf appended check-only.
_ALL_DEPLOYED_TREES = [
    (_LABEL_TO_DEPLOYED_PIPELINE[label], bucket)
    for dirname, (bucket, label) in _DEPLOY_PIPELINE_MAP.items()
    if label in _LABEL_TO_DEPLOYED_PIPELINE
] + [("mdpf", "opal-data-mdpf")] + (
    # advi appended (PSCRIPT2): bucket from the ONE declaration; absent CODE_TREES = absent
    # row, and the sweep's per-tree loop reports what it iterates -- never a guessed bucket.
    [("advi", _CODE_TREES["advi"]["bucket"])] if _CODE_TREES is not None else []
)

# ---------------------------------------------------------------------------
# NFRA_DEBTSCAN.TOOL-03: bronze + auxiliary-prefix coverage.
#
# BRONZE is a first-class deploy layer (safe_deploy_core.VALID_LAYERS) but the
# pre-TOOL-03 deployed check enumerated only gold+silver for bd/inf -- so the
# Rule-13 cycle was UNVERIFIABLE for every bd/inf bronze deploy (the 2026-06-12
# inf-ADVI stranded-deploy class). Bronze repo dirs derive from the same
# canonical PIPELINE_MAP (data/<dir>/scripts/bronze -> code/bronze/).
#
# AUXILIARY prefixes are S3 code locations OUTSIDE the standard code/<layer>/
# deploy layout (mdpf precedent: CHECK-ONLY -- swept for staleness, never part
# of the deploy gate's upload derivation). Mapping value = repo-home dir for
# same-basename MD5 comparison; None = no unambiguous repo home -> every sweep
# emits an explicit UNCOVERED row (NEVER silent-clean: tool-blindness must not
# be countable as cleanliness -- the TOOL-02 false-clean discipline).
#
#   inf bronze-runner/ -- post-BRONZE-FIX#1 this is the runner-OPS assets
#     prefix only (fetch script, watchdog, backfill helpers; repo home
#     infra/aws/ec2/inf-bronze-runner) + the manual_api mirror sub-prefix
#     (remaining consolidation leg). The runner's PIPELINE code
#     (orchestrator.py) now syncs from canonical code/bronze/ -- the
#     2026-06-12 P0 dual-prefix is collapsed.
#   inf manual_api/ -- Orion REST pull scripts, repo home data/inf/manual_api
#     (ADHC_COMPIL_V4.008 graph anchor); consumed by the inf GOLD runner's
#     collision-guarded 4-prefix flat sync.
#   inf runner/ exporter/ cleanup/ -- EC2 service/dispatch assets with no
#     single repo-home mapping -> UNCOVERED.
#
# Single-sourced from safe_deploy_core.AUX_CODE_PREFIXES (BRONZE-FIX #1 +
# deploy-ledger TO #5 machine surface); fallback MUST stay byte-equal.
try:
    from safe_deploy_core import AUX_CODE_PREFIXES as _AUX_CHECK_ONLY_PREFIXES  # noqa: E402
except Exception:
    _AUX_CHECK_ONLY_PREFIXES = {
        "bd": {},
        "inf": {
            "bronze-runner": "infra/aws/ec2/inf-bronze-runner",
            "manual_api": "data/inf/manual_api",
            "runner": None,
            "exporter": None,
            "cleanup": None,
        },
        "cot": {},
    }

# Standard deploy-layout prefixes under code/ (everything else found live on a
# firm bucket that is not in _AUX_CHECK_ONLY_PREFIXES surfaces as UNCOVERED).
_STANDARD_CODE_PREFIXES = {"gold", "silver", "bronze"}


def _refuse_no_pipeline(script_hint=None):
    """ANDREW-DIRECT STUB 2026-07-30: the silent bd-gold default answered about a tree the
    caller never asked for (a clean zero on the WRONG TREE -- WS4 spec pipeline_cli.py:221).
    Until the WS4 hardening lands, NO tree given = LOUD REFUSAL, never a guess."""
    import os as _os
    import sys as _sys
    lines = ["REFUSED (rc=2): --pipeline/-p is now REQUIRED -- this tool previously defaulted to",
             "bd-gold and could return a clean zero for a script living in another tree",
             "(Andrew-direct 2026-07-30; WS4 hardening pending). NO GUESS IS MADE."]
    if script_hint:
        base = _os.path.basename(str(script_hint))
        tree_map = {"data/black_diamond/scripts": ("bd", "bd-{layer}"),
                    "data/inf/scripts": ("inf", "inf-{layer}"),
                    "data/cot/scripts": ("cot", "cot-{layer}")}
        hits = []
        for root, (firm, fmt) in tree_map.items():
            for dirp, _dirs, files in _os.walk(root):
                if base in files:
                    layer = _os.path.basename(dirp)
                    hits.append((firm, fmt.format(layer=layer), _os.path.join(dirp, base)))
        if hits:
            lines.append("This script exists in %d tree(s) -- re-run with the one you mean:" % len(hits))
            for firm, choice, path in hits:
                lines.append("  --pipeline %-12s  (%s)" % (choice, path))
        else:
            lines.append("Script %r not found under data/*/scripts/ -- if it is an mdpf/aux script," % base)
            lines.append("pass --pipeline mdpf or the aux tree explicitly; the no-arg `deployed` sweep")
            lines.append("covers all trees firm-separated.")
    print("\n".join(lines), file=_sys.stderr)
    raise SystemExit(2)


def _build_dag(pipeline: str = None):
    """Return the appropriate DAG for the given pipeline scope.

    pipeline="bd-gold"     → existing BD-gold DAG (backward-compatible default)
    pipeline="bd"          → shorthand alias for bd-gold (disambiguation flag)
    pipeline="inf-gold"    → INF gold DAG only
    pipeline="inf"         → shorthand alias for inf-gold (disambiguation flag)
    pipeline="bd-silver"   → BD silver DAG only
    pipeline="inf-silver"  → INF silver DAG only
    pipeline="inf-manual-api" → INF manual_api DAG (Orion REST pull scripts; ADHC_COMPIL_V4.008)
    pipeline="all"         → combined multi-pipeline DAG (namespaced IDs)
    """
    if pipeline is None:
        _refuse_no_pipeline()
    if pipeline in ("bd-gold", "bd"):
        return build_pipeline_dag(_WORKSPACE)
    if pipeline in ("inf-gold", "inf"):
        return build_inf_gold_dag(_WORKSPACE)
    if pipeline == "bd-silver":
        return build_silver_dag(_WORKSPACE, "bd-silver", "data/black_diamond/scripts/silver")
    if pipeline == "inf-silver":
        return build_silver_dag(_WORKSPACE, "inf-silver", "data/inf/scripts/silver")
    if pipeline == "inf-manual-api":
        return build_inf_manual_api_dag(_WORKSPACE)
    # NFRA_DEBTSCAN.TOOL-02: cot + mdpf get their OWN graphs. Before this, any
    # unmapped key fell through to the bd graph SILENTLY -- `io --pipeline
    # cot-gold` analyzed bd scripts under a [bd-gold] header and reported
    # Unknown for every real cot id, which a coverage grep miscounted as clean
    # (the D2X false-clean class).
    if pipeline in ("cot-gold", "cot"):
        return build_pipeline_dag(_WORKSPACE,
                                  _WORKSPACE / "data" / "cot" / "scripts" / "gold",
                                  pipeline="cot-gold")
    if pipeline == "cot-silver":
        return build_silver_dag(_WORKSPACE, "cot-silver", "data/cot/scripts/silver")
    if pipeline == "mdpf":
        return build_mdpf_dag(_WORKSPACE)
    if pipeline == "bd-bronze":
        return build_silver_dag(_WORKSPACE, "bd-bronze", "data/black_diamond/scripts/bronze")
    if pipeline == "inf-bronze":
        return build_silver_dag(_WORKSPACE, "inf-bronze", "data/inf/scripts/bronze")
    if pipeline == "cot-bronze":
        return build_silver_dag(_WORKSPACE, "cot-bronze", "data/cot/scripts/bronze")
    # Bundle items (1)+(3) (CTO 20260722T210151Z/211318Z): the assets monolith trees.
    # Before this, build_dim_model_portfolio and the silver converter family were
    # UNREGISTERED -- io/feeds/consumers dead-ended on the exact scripts the
    # MDPF_3FIRMS TOs mandate io on (the D2X false-clean class, assets flavor).
    if pipeline == "assets-gold":
        return build_silver_dag(_WORKSPACE, "assets-gold", "data/assets/scripts/gold")
    if pipeline == "assets-silver":
        return build_silver_dag(_WORKSPACE, "assets-silver", "data/assets/scripts/silver")
    # PSCRIPT2 P3: the 49F runner chain's io registry row. runners_49f is a SUBDIR of the
    # shared assets gold home, invisible to assets-gold's non-recursive glob -- the chain
    # had NO io coverage at all (a comp-tool coverage gap is a DEFECT, standing Andrew law).
    if pipeline == "advi":
        return build_silver_dag(_WORKSPACE, "advi", "data/assets/scripts/gold/runners_49f")
    if pipeline == "all":
        return build_multi_pipeline_dag(_WORKSPACE)
    # FALSE-CLEAN GUARD (TOOL-02): an unknown key must NEVER silently become
    # the bd graph -- that is tool-blindness masquerading as an answer.
    print(f"UNCOVERED: no graph builder for pipeline {pipeline!r} -- "
          f"this tree is NOT analyzed (not clean, not dirty, UNVERIFIED).")
    sys.exit(2)


# ---------------------------------------------------------------------------
# ID-form resolver (ADHC_COMPIL.011) — auto-detects pipeline from script ID
# ---------------------------------------------------------------------------

# Dispatcher names: maps CLI name -> (pipeline_label, dispatch_filename, gold_dir_rel)
_DISPATCHER_NODES = {
    "inf-gold-dispatch": ("inf-gold", "orion-gold-dispatch.sh",
                          "data/inf/scripts/gold"),
    "orion-gold-dispatch": ("inf-gold", "orion-gold-dispatch.sh",
                             "data/inf/scripts/gold"),
    "bd-gold-dispatch": ("bd-gold", "gold_dispatch.sh",
                          "data/black_diamond/scripts/gold"),
}


def _format_dispatcher_io(dispatcher_name):
    """Print chain declaration for a dispatcher script and exit."""
    lower = dispatcher_name.lower()
    if lower not in _DISPATCHER_NODES:
        print(f"Unknown dispatcher: {dispatcher_name}")
        sys.exit(1)
    pipeline_label, dispatch_filename, gold_dir_rel = _DISPATCHER_NODES[lower]
    gold_dir = _WORKSPACE / gold_dir_rel
    dispatch_file = gold_dir / dispatch_filename

    if pipeline_label == "bd-gold":
        chains, _groups, catalog = _parse_dispatch(gold_dir)
    else:
        chains, _groups, catalog = _parse_orion_dispatch(gold_dir)

    print(f"DISPATCHER: {lower} ({dispatch_filename}) [{pipeline_label}]")
    print(f"  Source: {dispatch_file.relative_to(_WORKSPACE)}")
    print()

    if chains:
        print(f"  CHAINS ({len(chains)}):")
        for chain_name, members in sorted(chains.items()):
            print(f"    {chain_name} ({len(members)} scripts):")
            for i in range(0, len(members), 8):
                chunk = members[i:i + 8]
                print(f"      {' '.join(chunk)}")
        print()

    if catalog:
        print(f"  CATALOG ({len(catalog)} entries):")
        for script_id, filename in sorted(catalog.items()):
            print(f"    {script_id:<22} -> {filename}")
        print()

    sys.exit(0)


def _canonicalize_script_id(raw: str) -> str:
    """Strip path prefix and filename suffix to get the bare script ID string.

    Handles all three input forms agents use:
      data/black_diamond/scripts/gold/B_01.holdings_lots.py  -> B_01
      B_01.holdings_lots.py                                  -> B_01
      B_01.holdings_lots                                     -> B_01
      B_01.py / INF_D_04.py                                  -> B_01 / INF_D_04
      B_01 / INF_D_04                                        -> pass-through

    Does NOT uppercase -- callers uppercase as needed.
    """
    s = raw.strip().replace('\\', '/')
    # Rule 2: extract filename from full data/ path.
    #
    # DECLARED REPO HOMES FIRST (CTO 213109Z). The hardcoded alternation below omits
    # data/assets/ and the assets_gold layer, so a `data/assets/scripts/gold/x.py`
    # argument was NEVER stripped to its stem -- the filter then compared a full path
    # against a bare stem, matched nothing, and produced an all-zero summary. That is
    # the SECOND half of the same false-clean: fixing the router alone yields the
    # correct header over an empty result, which is arguably worse than the wrong
    # header because it looks authoritative. Derived from CODE_TREES so a new repo
    # home never has to be restated here.
    if _CODE_TREES is not None:
        for _tree in _CODE_TREES.values():
            for _repo_home, _prefix in _tree["layers"].values():
                if s.startswith(_repo_home + "/"):
                    s = s[len(_repo_home) + 1:]
                    break
            else:
                continue
            break
    # Legacy alternation retained for the shapes CODE_TREES does not model
    # (notably data/schwab/, which is not a declared code tree).
    m = re.search(
        r'data/(?:black_diamond|inf|schwab|cot|mdpf)/scripts/(?:gold|silver|bronze|backfill|feeders)/(.+)', s
    )
    if m:
        s = m.group(1)
    # Strip .py suffix
    if s.lower().endswith('.py'):
        s = s[:-3]
    # Rule 1: strip .<name> suffix for <ID>.<name> filename form (e.g. B_01.holdings_lots -> B_01)
    m2 = re.match(r'^([A-Za-z0-9_]+)\..+$', s)
    if m2:
        s = m2.group(1)
    return s


def _ci_lookup(scripts, ident):
    """Case-insensitive exact-key lookup into a DAG's scripts dict.

    Returns the canonical key if `ident` matches a key ignoring case, else None.
    The orion-gold dispatch catalog carries lowercase chain-step suffixes
    (INF_D_00c, INF_D_05a, INF_B_01b, ...) that a blanket .upper() mangles.
    """
    if ident in scripts:
        return ident
    il = ident.lower()
    for k in scripts:
        if k.lower() == il:
            return k
    return None


def _auto_resolve_script_id(raw_id, pipeline_hint=None):
    """Resolve a script ID to (dag, canonical_id) across all indexed pipelines.

    Handles:
      - INF_* prefix  -> inf-gold DAG
      - *-dispatch    -> dispatcher handler (prints and exits)
      - bare snake_case -> bd-silver + inf-silver
      - BD/INF gold IDs -> bd-gold, then inf-gold (collision = disambiguation error)
      - Filename forms (B_01.holdings_lots.py) -> exact filename match, then bare ID

    pipeline_hint: 'bd' restricts to BD pipelines; 'inf' restricts to INF pipelines.
    On failure: prints closest-match suggestion and calls sys.exit(1).
    """
    from difflib import get_close_matches

    # Step 1: strip data/ path prefix and .py suffix only — no .<name> stripping yet.
    _norm = raw_id.strip().replace('\\', '/')
    _pm = re.search(
        r'data/(?:black_diamond|inf|schwab|cot|mdpf)/scripts/(?:gold|silver|bronze|backfill|feeders)/(.+)', _norm
    )
    if _pm:
        _norm = _pm.group(1)
    if _norm.lower().endswith('.py'):
        _norm = _norm[:-3]

    # Step 2: filename-form detection — if stem still has a dot (e.g. B_01.holdings_lots),
    # resolve by exact filename match before bare-ID canonicalization (AC1/AC3).
    if '.' in _norm:
        _ftarget = _norm + '.py'
        _bd_only_pre = pipeline_hint in ("bd",)
        _inf_only_pre = pipeline_hint in ("inf",)
        _found_dag = None
        _found_id = None

        def _search_dag_for_filename(dag):
            nonlocal _found_dag, _found_id
            for sid, sio in dag.scripts.items():
                if sio.filename and sio.filename.lower() == _ftarget.lower():
                    if _found_dag is None:
                        _found_dag = dag
                        _found_id = sid
                    else:
                        print(f"Ambiguous filename: {_ftarget!r} found in multiple pipelines.")
                        sys.exit(1)

        try:
            if not _inf_only_pre:
                _search_dag_for_filename(_build_dag("bd-gold"))
            if not _bd_only_pre:
                _search_dag_for_filename(_build_dag("inf-gold"))
            if not _inf_only_pre:
                _search_dag_for_filename(_build_dag("bd-silver"))
            if not _bd_only_pre:
                _search_dag_for_filename(_build_dag("inf-silver"))
        except SystemExit:
            raise
        except Exception:
            pass

        if _found_dag is not None:
            raw = _found_id
        else:
            _bare = re.match(r'^([A-Za-z0-9_]+)', _norm)
            _bare_id = _bare.group(1) if _bare else _norm
            print(f"Script not found: {raw_id}. Did you mean: {_bare_id}?")
            sys.exit(1)
    else:
        # Bare ID form — path already stripped, .py already stripped, no dot remaining
        raw = _norm

    lower = raw.lower()
    upper = raw.upper()

    bd_only = pipeline_hint in ("bd",)
    inf_only = pipeline_hint in ("inf",)

    # --- Dispatcher names ---
    if lower in _DISPATCHER_NODES:
        _format_dispatcher_io(lower)  # prints + sys.exit(0) — does not return

    # --- INF-prefixed gold scripts ---
    if upper.startswith("INF_") and not bd_only:
        dag = _build_dag("inf-gold")
        hit = _ci_lookup(dag.scripts, raw)
        if hit:
            return dag, hit
        matches = [s for s in dag.scripts if lower in s.lower()]
        if len(matches) == 1:
            return dag, matches[0]
        if len(matches) > 1:
            print(f"Multiple INF matches for {raw!r}: {', '.join(sorted(matches))}")
            sys.exit(1)
        close = get_close_matches(raw, list(dag.scripts.keys()), n=3, cutoff=0.45)
        hint = f"Did you mean: {', '.join(close)}?" if close else \
               f"Available INF scripts: {', '.join(sorted(dag.scripts.keys()))}"
        print(f"Script not found: {raw}. {hint}")
        sys.exit(1)

    # --- INF manual_api scripts (ADHC_COMPIL_V4.008) ---
    # Patterns: pull_inflection_*, orion_*_dim, probe_inflec_*, create_*_query
    is_manual_api_like = (
        not bd_only and (
            lower.startswith("pull_inflection") or
            lower.startswith("orion_") or
            lower.startswith("probe_inflec") or
            (lower.startswith("create_") and "query" in lower) or
            (lower.startswith("diagnose_") and "performance" in lower)
        )
    )
    if is_manual_api_like:
        manual_dag = _build_dag("inf-manual-api")
        if lower in manual_dag.scripts:
            return manual_dag, lower
        # Also try the raw form (case-preserved) in case scripts have mixed-case names
        if raw in manual_dag.scripts:
            return manual_dag, raw

    # --- Bare silver script names (snake_case, no LETTER_NN pattern) ---
    is_silver_like = (
        not re.match(r"^[A-Z]_\d", raw) and
        not upper.startswith("INF_") and
        "_" in raw and
        lower not in _DISPATCHER_NODES and
        not is_manual_api_like
    )
    if is_silver_like:
        candidates = []
        if not inf_only:
            bd_s = _build_dag("bd-silver")
            if lower in bd_s.scripts:
                candidates.append(("bd-silver", bd_s, lower))
        if not bd_only:
            inf_s = _build_dag("inf-silver")
            if lower in inf_s.scripts:
                candidates.append(("inf-silver", inf_s, lower))
            # Fallback: also check inf-manual-api for snake_case scripts that don't
            # match the explicit prefix patterns above
            inf_m = _build_dag("inf-manual-api")
            if lower in inf_m.scripts:
                candidates.append(("inf-manual-api", inf_m, lower))
        # Assets monolith trees (bundle items 1+3): snake_case names, no pipeline
        # hint namespace of their own -- checked unconditionally.
        for _apl in ("assets-gold", "assets-silver"):
            _adag = _build_dag(_apl)
            if lower in _adag.scripts:
                candidates.append((_apl, _adag, lower))

        if len(candidates) == 1:
            _, dag, cid = candidates[0]
            return dag, cid
        if len(candidates) > 1:
            print(f"Ambiguous script ID: {raw!r} found in multiple pipelines:")
            for pl, _, cid in candidates:
                print(f"  [{pl}] {cid}")
            print("  Use --pipeline bd or --pipeline inf to disambiguate.")
            sys.exit(1)
        # Not found in silver — fall through to gold check

    # --- BD gold + INF gold ---
    bd_dag = None
    inf_dag = None
    bd_cid = None
    inf_cid = None

    if not inf_only:
        bd_dag = _build_dag("bd-gold")
        bd_hit = _ci_lookup(bd_dag.scripts, raw)
        if bd_hit:
            bd_cid = bd_hit
        else:
            bd_matches = [s for s in bd_dag.scripts if lower in s.lower()]
            if len(bd_matches) == 1:
                bd_cid = bd_matches[0]

    if not bd_only:
        inf_dag = _build_dag("inf-gold")
        # Exact match only for cross-pipeline disambiguation.
        # INF-unique scripts have INF_ prefixes and are handled above; shared-logic scripts
        # use the same bare IDs as BD. Substring match creates false collisions (e.g. D_04
        # would spuriously match INF_D_04). Only fire disambiguation when the exact same ID
        # exists in both pipeline DAGs.
        inf_hit = _ci_lookup(inf_dag.scripts, raw)
        if inf_hit:
            inf_cid = inf_hit

    if bd_cid and inf_cid:
        print(f"Ambiguous script ID: {raw!r} found in multiple pipelines:")
        print(f"  [bd-gold]  {bd_cid}")
        print(f"  [inf-gold] {inf_cid}")
        print("  Use --pipeline bd or --pipeline inf to disambiguate.")
        sys.exit(1)

    if bd_cid:
        return bd_dag, bd_cid
    if inf_cid:
        return inf_dag, inf_cid

    # Not found anywhere -- aggregate close matches across all pipelines. NFRA_TOOLCHECK P2
    # (discoverability, 0.8.0_AE_CloudComp~D 2026-07-08): match the raw token against BOTH the IDs
    # AND the script FILENAMES/descriptors, so a DESCRIPTIVE guess ("client_portal_summary") or a
    # PARTIAL ("portal_summary") resolves to its ID -- the 21% name-resolution friction (agents can't
    # guess the bare-ID convention). Was: fuzzy on IDs only. Error-path only -> zero success-path change.
    all_ids = []
    id_by_desc = {}   # descriptor token (filename stem + each dotted part) -> canonical id

    def _index_dag(_dag):
        if not _dag:
            return
        for _sid, _sio in _dag.scripts.items():
            all_ids.append(_sid)
            _fn = (getattr(_sio, "filename", "") or "").replace(".py", "")
            for _tok in filter(None, [_fn] + _fn.split(".")):   # full stem + each dotted part (id, descriptor)
                id_by_desc.setdefault(_tok.lower(), _sid)

    _index_dag(bd_dag)
    _index_dag(inf_dag)
    try:
        if not inf_only:
            _index_dag(_build_dag("bd-silver"))
        if not bd_only:
            _index_dag(_build_dag("inf-silver"))
        _index_dag(_build_dag("assets-gold"))
        _index_dag(_build_dag("assets-silver"))
    except Exception:
        pass

    rlow = raw.lower()
    suggestions = []
    # (1) SUBSTRING: the raw token appears in (or contains) a filename/descriptor -> that id.
    for _desc, _sid in id_by_desc.items():
        if len(rlow) >= 3 and (rlow in _desc or _desc in rlow) and _sid not in suggestions:
            suggestions.append(_sid)
    # (2) FUZZY on ids (edit-distance) -- the original behavior, preserved.
    for _m in get_close_matches(raw, all_ids, n=3, cutoff=0.45):
        if _m not in suggestions:
            suggestions.append(_m)
    # (3) FUZZY on descriptors -> their ids (catches a near-miss descriptive guess).
    for _m in get_close_matches(rlow, list(id_by_desc.keys()), n=3, cutoff=0.5):
        _sid = id_by_desc.get(_m)
        if _sid and _sid not in suggestions:
            suggestions.append(_sid)

    if suggestions:
        print(f"Script not found: {raw}. Did you mean: {', '.join(suggestions[:5])}?  "
              f"(matched by id or filename/descriptor)")
    else:
        print(f"Unknown script: {raw}")
        bd_valid = sorted(bd_dag.scripts.keys()) if bd_dag else []
        if bd_valid:
            print(f"BD-gold IDs: {', '.join(bd_valid)}")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_dag(args):
    pipeline = getattr(args, 'pipeline', 'bd-gold') or 'bd-gold'
    dag = _build_dag(pipeline)

    if args.json:
        result = {}
        for sid, sio in sorted(dag.scripts.items(), key=lambda x: x[1].run_order):
            result[sid] = {
                "filename": sio.filename,
                "pipeline": sio.pipeline,
                "group": sio.group,
                "run_order": sio.run_order,
                "reads": sio.read_keys,
                "writes": sio.write_keys,
                "feeds_from": [(u, k) for u, k, _ in dag.feeds(sid)],
                "feeds_to": [(d, k) for d, k, _ in dag.consumers(sid)],
            }
        print(json.dumps(result, indent=2))
        return

    # ADHC_COMPIL_V4.021 Cat 5.4: also count detected paths via hardcoded extraction
    # (INF/silver lack s3_layout.py named constants; only BD has dag.s3_keys populated).
    detected_paths: set = set()
    for _sio in dag.scripts.values():
        for k in _sio.read_keys:
            detected_paths.add(k)
        for k in _sio.write_keys:
            detected_paths.add(k)

    print("PIPELINE DAG")
    print(f"  Pipeline: [{pipeline}]")
    print(f"  Scripts: {len(dag.scripts)}")
    if dag.s3_keys:
        print(f"  S3 keys (named): {len(dag.s3_keys)} | detected paths: {len(detected_paths)}")
    else:
        print(f"  S3 keys (named): 0 | detected paths: {len(detected_paths)} (hardcoded)")
    print()

    for sid, sio in sorted(dag.scripts.items(), key=lambda x: x[1].run_order):
        upstream = dag.feeds(sid)
        downstream = dag.consumers(sid)
        label = f"[{sio.pipeline}]" if sio.pipeline != "bd-gold" else ""
        print(f"  {sid} ({sio.filename}){' ' + label if label else ''}")
        print(f"    Group: {sio.group} | Order: {sio.run_order}")
        print(f"    Reads:  {len(sio.read_keys)} keys | Writes: {len(sio.write_keys)} keys")
        if upstream:
            scripts = sorted(set(u for u, _, _ in upstream))
            print(f"    Fed by: {', '.join(scripts)}")
        if downstream:
            scripts = sorted(set(d for d, _, _ in downstream))
            print(f"    Feeds:  {', '.join(scripts)}")
        print()


def scan_lambda_io(content: str) -> dict:
    """ADHC_COMPIL_V5 TO-VAL AC-VAL-Y -- public Lambda I/O scanner.

    Extracted from _lambda_pipescript_io so the graph-extraction pass in
    extract_s3.extract_lambda_s3_edges can reuse the same regex + AST +
    call-graph DFA pipeline without duplicating logic. Returns a dict:

        {
            "s3_reads": set[str],          # resolved S3 keys read
            "s3_writes": set[str],         # resolved S3 keys written
            "s3_prefix_reads": set[str],   # prefix patterns ending with '*'
            "ddb_tables": set[str],        # DynamoDB table names
            "dynamic_refs": list[str],     # s3:// + f-string refs not in s3_reads/writes
        }

    Reusable from BOTH the CLI print path (comp-pipescript io <Lambda-path>)
    AND the graph-extraction pass (build_graph -> extract_lambda_s3_edges ->
    Lambda<->S3_ARTIFACT edges queryable via comp-trace + comp-blast).
    """
    constants: dict[str, str] = {}
    for m in re.finditer(
        r"""^([A-Z_][A-Z0-9_]*)\s*=\s*['"]([^'"\n]+)['"]\s*$""",
        content,
        re.MULTILINE,
    ):
        constants[m.group(1)] = m.group(2)

    def _resolve(var_or_lit: str) -> str:
        return constants.get(var_or_lit, var_or_lit)

    s3_reads: set[str] = set()
    s3_writes: set[str] = set()
    s3_prefix_reads: set[str] = set()
    ddb_tables: set[str] = set()

    from org.modules.graph.extract_pipeline import _collapse_multiline_calls
    collapsed = _collapse_multiline_calls(content)

    for m in re.finditer(
        r"""(?:get_object|head_object|download_file|download_fileobj)\s*\([^)]*Key\s*=\s*(?:f?['"]([^'"]+)['"]|([A-Za-z_][A-Za-z_0-9.]*))""",
        collapsed,
    ):
        key = _resolve(m.group(1) or m.group(2) or "")
        if key:
            s3_reads.add(re.sub(r"\{[^}]+\}", "{*}", key))
    for m in re.finditer(
        r"""(?:list_objects(?:_v2)?)\s*\([^)]*Prefix\s*=\s*(?:f?['"]([^'"]+)['"]|([A-Za-z_][A-Za-z_0-9.]*))""",
        collapsed,
    ):
        pfx = _resolve(m.group(1) or m.group(2) or "")
        if pfx:
            s3_prefix_reads.add(re.sub(r"\{[^}]+\}", "{*}", pfx) + "*")
    for m in re.finditer(
        r"""(?:put_object|upload_file|upload_fileobj|copy_object)\s*\([^)]*Key\s*=\s*(?:f?['"]([^'"]+)['"]|([A-Za-z_][A-Za-z_0-9.]*))""",
        collapsed,
    ):
        key = _resolve(m.group(1) or m.group(2) or "")
        if key:
            s3_writes.add(re.sub(r"\{[^}]+\}", "{*}", key))
    for m in re.finditer(
        r"""dynamodb\.Table\s*\(\s*(?:['"]([^'"]+)['"]|([A-Za-z_][A-Za-z_0-9]*))\s*\)""",
        collapsed,
    ):
        tbl = _resolve(m.group(1) or m.group(2) or "")
        if tbl:
            ddb_tables.add(tbl)
    for m in re.finditer(
        r"""TableName\s*=\s*(?:['"]([^'"]+)['"]|([A-Za-z_][A-Za-z_0-9]*))""",
        collapsed,
    ):
        tbl = _resolve(m.group(1) or m.group(2) or "")
        if tbl:
            ddb_tables.add(tbl)

    # AST-based helper-fn call-graph + intermediate-var DFA
    try:
        import ast as _ast
        tree = _ast.parse(content)

        local_var_maps: dict[str, dict[str, str]] = {}

        def _eval_str_expr(value_node) -> str | None:
            if isinstance(value_node, _ast.Constant) and isinstance(value_node.value, str):
                return value_node.value
            if isinstance(value_node, _ast.Name):
                return constants.get(value_node.id)
            if isinstance(value_node, _ast.JoinedStr):
                parts: list[str] = []
                for v in value_node.values:
                    if isinstance(v, _ast.Constant) and isinstance(v.value, str):
                        parts.append(v.value)
                    elif isinstance(v, _ast.FormattedValue):
                        if isinstance(v.value, _ast.Name) and v.value.id in constants:
                            parts.append(constants[v.value.id])
                        else:
                            parts.append("{*}")
                    else:
                        parts.append("{*}")
                return "".join(parts)
            return None

        for fn_node in _ast.walk(tree):
            if not isinstance(fn_node, _ast.FunctionDef):
                continue
            local: dict[str, str] = {}
            for inner in _ast.walk(fn_node):
                if not isinstance(inner, _ast.Assign):
                    continue
                if len(inner.targets) != 1:
                    continue
                tgt = inner.targets[0]
                if not isinstance(tgt, _ast.Name):
                    continue
                if tgt.id in local:
                    continue
                resolved = _eval_str_expr(inner.value)
                if resolved is not None:
                    local[tgt.id] = resolved
            local_var_maps[fn_node.name] = local

        helper_key_param: dict[str, tuple[str, str]] = {}
        S3_READ_FNS = {"get_object", "head_object", "download_file", "download_fileobj"}
        S3_WRITE_FNS = {"put_object", "upload_file", "upload_fileobj", "copy_object"}
        for node in _ast.walk(tree):
            if not isinstance(node, _ast.FunctionDef):
                continue
            for inner in _ast.walk(node):
                if not isinstance(inner, _ast.Call):
                    continue
                attr = getattr(inner.func, "attr", None)
                if attr in S3_READ_FNS | S3_WRITE_FNS:
                    for kw in inner.keywords:
                        if kw.arg == "Key" and isinstance(kw.value, _ast.Name):
                            param_name = kw.value.id
                            params = [a.arg for a in node.args.args]
                            if param_name in params:
                                kind = "write" if attr in S3_WRITE_FNS else "read"
                                helper_key_param[node.name] = (param_name, kind)

        for node in _ast.walk(tree):
            if not isinstance(node, _ast.Call):
                continue
            fname = None
            if isinstance(node.func, _ast.Name):
                fname = node.func.id
            elif isinstance(node.func, _ast.Attribute):
                fname = node.func.attr
            if not fname or fname not in helper_key_param:
                continue
            param_name, op_kind = helper_key_param[fname]
            params: list[str] = []
            for fn_node in _ast.walk(tree):
                if isinstance(fn_node, _ast.FunctionDef) and fn_node.name == fname:
                    params = [a.arg for a in fn_node.args.args]
                    break
            try:
                idx = params.index(param_name)
            except ValueError:
                continue
            arg_node = None
            if idx < len(node.args):
                arg_node = node.args[idx]
            else:
                for kw in node.keywords:
                    if kw.arg == param_name:
                        arg_node = kw.value
                        break
            if arg_node is None:
                continue
            enclosing_fn: str | None = None
            for fn_node in _ast.walk(tree):
                if not isinstance(fn_node, _ast.FunctionDef):
                    continue
                for inner in _ast.walk(fn_node):
                    if inner is node:
                        enclosing_fn = fn_node.name
                        break
                if enclosing_fn:
                    break
            local = local_var_maps.get(enclosing_fn, {}) if enclosing_fn else {}
            resolved_key: str | None = _eval_str_expr(arg_node)
            if resolved_key is None and isinstance(arg_node, _ast.Name):
                resolved_key = local.get(arg_node.id)
            if resolved_key:
                normalized = re.sub(r"\{[^}]+\}", "{*}", resolved_key)
                if op_kind == "write":
                    s3_writes.add(normalized)
                else:
                    s3_reads.add(normalized)

        for ph in ("key", "Key", "k", "object_key", "s3_key"):
            s3_writes.discard(ph)
            s3_reads.discard(ph)
    except (SyntaxError, ValueError):
        pass

    from org.modules.graph.extract_pipeline import _extract_dynamic_refs
    dynamic = _extract_dynamic_refs(content)
    covered = s3_reads | s3_writes | s3_prefix_reads
    dynamic_refs = [d for d in dynamic if d not in covered and d.rstrip("/") not in covered]

    return {
        "s3_reads": s3_reads,
        "s3_writes": s3_writes,
        "s3_prefix_reads": s3_prefix_reads,
        "ddb_tables": ddb_tables,
        "dynamic_refs": dynamic_refs,
    }


def _lambda_pipescript_io(script_path_arg: str) -> bool:
    """ADHC_COMPIL_V5.002 -- Lambda-side I/O manifest scan.

    When `args.script_id` is a path to a Lambda function file (under
    `infra/aws/lambda/**/lambda_function.py`), bypass the BD-gold DAG lookup
    and produce an I/O manifest by ad-hoc scanning the Lambda source for
    boto3 S3 + DynamoDB operations. Mirrors the BD-gold-side I/O MANIFEST
    format so the output is consumable by the same comp-pipescript users.

    Returns True if the path was Lambda-side and printed; False if not a
    Lambda path (caller falls through to the BD-gold DAG path).

    Empirical anchor (AC2): reproduces DS 0.1.0 YALP_MKTOVR.001 brief §11
    Level-1 mapping for market-overview-tiered-generator + sister Lambdas.
    """
    # Detect Lambda-path-mode: arg contains a / and points to an existing .py
    # file under infra/aws/lambda/.
    if "/" not in script_path_arg and "\\" not in script_path_arg:
        return False
    normalized = script_path_arg.replace("\\", "/")
    if "infra/aws/lambda/" not in normalized:
        return False
    abs_path = _WORKSPACE / normalized
    if not abs_path.exists() or not abs_path.is_file():
        return False

    try:
        content = abs_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        print(f"ERROR: cannot read {script_path_arg}")
        return True  # consumed the arg even on read error

    # Module-level string-constant resolution: many Lambdas write
    #   DYNAMODB_TABLE = 'opal-portal-market-data'
    #   s3_client.put_object(..., Key=key)
    # where the actual S3/DDB target hides behind a variable. Build a name->value
    # map from top-level assignments so Key=VAR / TableName=VAR resolve cleanly.
    constants: dict[str, str] = {}
    for m in re.finditer(
        r"""^([A-Z_][A-Z0-9_]*)\s*=\s*['"]([^'"\n]+)['"]\s*$""",
        content,
        re.MULTILINE,
    ):
        constants[m.group(1)] = m.group(2)

    def _resolve(var_or_lit: str) -> str:
        return constants.get(var_or_lit, var_or_lit)

    # Extract per-operation S3 + DDB references with direction (read/write).
    s3_reads: set[str] = set()
    s3_writes: set[str] = set()
    s3_prefix_reads: set[str] = set()
    ddb_reads: set[tuple[str, str]] = set()   # (table, op)
    ddb_writes: set[tuple[str, str]] = set()

    # S3 op patterns -- collapse multiline so multi-line kwargs match
    from org.modules.graph.extract_pipeline import _collapse_multiline_calls
    collapsed = _collapse_multiline_calls(content)

    # READ ops: get_object, download_file, head_object, list_objects, list_objects_v2
    for m in re.finditer(
        r"""(?:get_object|head_object|download_file|download_fileobj)\s*\([^)]*Key\s*=\s*(?:f?['"]([^'"]+)['"]|([A-Za-z_][A-Za-z_0-9.]*))""",
        collapsed,
    ):
        key = _resolve(m.group(1) or m.group(2) or "")
        if key:
            s3_reads.add(re.sub(r"\{[^}]+\}", "{*}", key))
    for m in re.finditer(
        r"""(?:list_objects(?:_v2)?)\s*\([^)]*Prefix\s*=\s*(?:f?['"]([^'"]+)['"]|([A-Za-z_][A-Za-z_0-9.]*))""",
        collapsed,
    ):
        pfx = _resolve(m.group(1) or m.group(2) or "")
        if pfx:
            s3_prefix_reads.add(re.sub(r"\{[^}]+\}", "{*}", pfx) + "*")

    # WRITE ops: put_object, upload_file, upload_fileobj, copy_object
    for m in re.finditer(
        r"""(?:put_object|upload_file|upload_fileobj|copy_object)\s*\([^)]*Key\s*=\s*(?:f?['"]([^'"]+)['"]|([A-Za-z_][A-Za-z_0-9.]*))""",
        collapsed,
    ):
        key = _resolve(m.group(1) or m.group(2) or "")
        if key:
            s3_writes.add(re.sub(r"\{[^}]+\}", "{*}", key))

    # DDB ops: literal-string + module-constant via dynamodb.Table(...)
    for m in re.finditer(
        r"""dynamodb\.Table\s*\(\s*(?:['"]([^'"]+)['"]|([A-Za-z_][A-Za-z_0-9]*))\s*\)""",
        collapsed,
    ):
        tbl = _resolve(m.group(1) or m.group(2) or "")
        if tbl:
            ddb_reads.add((tbl, "ddb-read"))
            ddb_writes.add((tbl, "ddb-write"))
    # DDB TableName= kwargs (low-level client.X(TableName=...) form)
    for m in re.finditer(
        r"""TableName\s*=\s*(?:['"]([^'"]+)['"]|([A-Za-z_][A-Za-z_0-9]*))""",
        collapsed,
    ):
        tbl = _resolve(m.group(1) or m.group(2) or "")
        if tbl:
            ddb_reads.add((tbl, "ddb-read"))
            ddb_writes.add((tbl, "ddb-write"))

    # Specific DDB op-direction patterns (more precise)
    for m in re.finditer(
        r"""\.(?:get_item|query|scan|batch_get_item)\s*\(""", collapsed
    ):
        pass  # already captured generally above
    for m in re.finditer(
        r"""\.(?:put_item|update_item|delete_item|batch_write_item)\s*\(""", collapsed
    ):
        pass

    # ADHC_COMPIL_V5 TO-VAL AC-VAL-X: helper-fn call-graph resolution.
    # Many Lambdas wrap put_object/get_object in a helper (`save_to_s3(key, data)`)
    # called from elsewhere with literal Key arguments. Straight regex scan above
    # sees `Key=key` inside the helper body and can't resolve `key` (function param,
    # not module constant). AST walk finds these helpers and follows call-sites to
    # extract the literal/constant Key values actually written. Empirical anchor:
    # DS 0.1.0 YALP_MKTOVR.001 brief §11 reproduction for market-overview-tiered-
    # generator (SUMMARY_KEY via save_to_s3 helper at line 491).
    try:
        import ast as _ast

        tree = _ast.parse(content)

        # ADHC_COMPIL_V5 TO-VAL AC-VAL-X intermediate-var resolution:
        # Build per-function local name->value map for `<name> = <literal|f-string>`
        # assignments. Lets us resolve call-site args like
        #   key = f"{DETAILS_PREFIX}{ticker}.json"
        #   save_to_s3(key, ...)
        # by looking up `key` in the enclosing FunctionDef's local map. First
        # assignment wins (covers common ship-once pattern); reassignment ignored
        # to keep MVP-simple. Module-constants map (built upstream) takes
        # precedence when name matches a top-level CONST.
        local_var_maps: dict[str, dict[str, str]] = {}  # fn_qualname -> {name: value}

        def _eval_str_expr(value_node) -> str | None:
            """Best-effort: resolve an AST expression to a string literal using
            constants + (later) the enclosing local_var map. Returns None if
            non-resolvable. f-strings collapse non-literal parts to {*}."""
            if isinstance(value_node, _ast.Constant) and isinstance(value_node.value, str):
                return value_node.value
            if isinstance(value_node, _ast.Name):
                return constants.get(value_node.id)
            if isinstance(value_node, _ast.JoinedStr):
                parts: list[str] = []
                for v in value_node.values:
                    if isinstance(v, _ast.Constant) and isinstance(v.value, str):
                        parts.append(v.value)
                    elif isinstance(v, _ast.FormattedValue):
                        if isinstance(v.value, _ast.Name) and v.value.id in constants:
                            parts.append(constants[v.value.id])
                        else:
                            parts.append("{*}")
                    else:
                        parts.append("{*}")
                return "".join(parts)
            return None

        for fn_node in _ast.walk(tree):
            if not isinstance(fn_node, _ast.FunctionDef):
                continue
            local: dict[str, str] = {}
            for inner in _ast.walk(fn_node):
                if not isinstance(inner, _ast.Assign):
                    continue
                if len(inner.targets) != 1:
                    continue
                tgt = inner.targets[0]
                if not isinstance(tgt, _ast.Name):
                    continue
                if tgt.id in local:
                    continue  # first-assignment-wins
                resolved = _eval_str_expr(inner.value)
                if resolved is not None:
                    local[tgt.id] = resolved
            local_var_maps[fn_node.name] = local

        # Pass 1: helper FunctionDefs containing S3 ops with Key=<param>
        helper_key_param: dict[str, tuple[str, str]] = {}

        S3_READ_FNS = {"get_object", "head_object", "download_file", "download_fileobj"}
        S3_WRITE_FNS = {"put_object", "upload_file", "upload_fileobj", "copy_object"}

        for node in _ast.walk(tree):
            if not isinstance(node, _ast.FunctionDef):
                continue
            for inner in _ast.walk(node):
                if not isinstance(inner, _ast.Call):
                    continue
                attr = getattr(inner.func, "attr", None)
                if attr in S3_READ_FNS | S3_WRITE_FNS:
                    for kw in inner.keywords:
                        if kw.arg == "Key" and isinstance(kw.value, _ast.Name):
                            param_name = kw.value.id
                            params = [a.arg for a in node.args.args]
                            if param_name in params:
                                kind = "write" if attr in S3_WRITE_FNS else "read"
                                helper_key_param[node.name] = (param_name, kind)

        # Pass 2: call-sites of helper functions; extract literal Key values
        for node in _ast.walk(tree):
            if not isinstance(node, _ast.Call):
                continue
            fname = None
            if isinstance(node.func, _ast.Name):
                fname = node.func.id
            elif isinstance(node.func, _ast.Attribute):
                fname = node.func.attr
            if not fname or fname not in helper_key_param:
                continue
            param_name, op_kind = helper_key_param[fname]
            params: list[str] = []
            for fn_node in _ast.walk(tree):
                if isinstance(fn_node, _ast.FunctionDef) and fn_node.name == fname:
                    params = [a.arg for a in fn_node.args.args]
                    break
            try:
                idx = params.index(param_name)
            except ValueError:
                continue
            arg_node = None
            if idx < len(node.args):
                arg_node = node.args[idx]
            else:
                for kw in node.keywords:
                    if kw.arg == param_name:
                        arg_node = kw.value
                        break
            if arg_node is None:
                continue
            # Identify the enclosing FunctionDef of THIS call-site for local-var
            # lookup (intermediate-var resolution path).
            enclosing_fn: str | None = None
            for fn_node in _ast.walk(tree):
                if not isinstance(fn_node, _ast.FunctionDef):
                    continue
                for inner in _ast.walk(fn_node):
                    if inner is node:
                        enclosing_fn = fn_node.name
                        break
                if enclosing_fn:
                    break
            local = local_var_maps.get(enclosing_fn, {}) if enclosing_fn else {}

            resolved_key: str | None = _eval_str_expr(arg_node)
            # If straight eval returned None for a Name, try local-var map
            if resolved_key is None and isinstance(arg_node, _ast.Name):
                resolved_key = local.get(arg_node.id)
            if resolved_key:
                normalized = re.sub(r"\{[^}]+\}", "{*}", resolved_key)
                if op_kind == "write":
                    s3_writes.add(normalized)
                else:
                    s3_reads.add(normalized)

        # Remove unresolved param-name placeholders that AST-walk now resolved
        for ph in ("key", "Key", "k", "object_key", "s3_key"):
            s3_writes.discard(ph)
            s3_reads.discard(ph)
    except (SyntaxError, ValueError):
        pass

    # Dynamic s3:// + f-string keys via existing extractor
    from org.modules.graph.extract_pipeline import _extract_dynamic_refs
    dynamic = _extract_dynamic_refs(content)

    rel_path = str(abs_path.relative_to(_WORKSPACE)).replace("\\", "/")
    function_name = abs_path.parent.name

    print(f"I/O MANIFEST: {function_name} ({rel_path}) [lambda_pipeline_script]")
    print("  Source: infra/aws/lambda/...; node-class: lambda_pipeline_script (ADHC_COMPIL_V5.002)")
    print()

    if s3_reads or s3_prefix_reads:
        total = len(s3_reads) + len(s3_prefix_reads)
        print(f"  READS ({total}):")
        for k in sorted(s3_reads):
            print(f"    s3:GetObject: {k}")
        for p in sorted(s3_prefix_reads):
            print(f"    s3:ListObjects: {p}  [PREFIX]")
    else:
        print("  READS: (none detected via boto3 get_object/list_objects/head_object/download_file patterns)")

    print()

    if s3_writes:
        print(f"  WRITES ({len(s3_writes)}):")
        for k in sorted(s3_writes):
            print(f"    s3:PutObject: {k}")
    else:
        print("  WRITES: (none detected via boto3 put_object/upload_file/copy_object patterns)")

    if ddb_reads or ddb_writes:
        print()
        ddb_tables = sorted({t for t, _ in (ddb_reads | ddb_writes)})
        print(f"  DYNAMODB ({len(ddb_tables)} table(s)):")
        for t in ddb_tables:
            print(f"    Table: {t}  [read+write inferred from boto3 Table() / dynamodb.X(TableName=...) patterns]")

    if dynamic:
        # Filter ones already covered by direct s3_reads/writes
        covered = s3_reads | s3_writes | s3_prefix_reads
        new_dynamic = [d for d in dynamic if d not in covered and d.rstrip("/") not in covered]
        if new_dynamic:
            print()
            print(f"  S3-DYNAMIC ({len(new_dynamic)}) [f-string / s3:// URI / pandas read]:")
            for path in new_dynamic:
                print(f"    {path}  [read-at-runtime]")

    if not (s3_reads or s3_writes or s3_prefix_reads or ddb_reads or ddb_writes or dynamic):
        print()
        print("  WARN: no S3 or DynamoDB operations detected.")
        print("  Lambda may use non-boto3 patterns or compute-only logic.")

    print()
    print("  NOTE: AC5 graph-traversal integration (comp-trace + comp-blast) -- partial.")
    print("        Lambda nodes not yet linked into the BD-gold pipeline DAG; use ad-hoc")
    print("        comp-iam service <name> for IAM-side coverage + this comp-pipescript io")
    print("        <path> for I/O-side coverage. Full traversal integration deferred to")
    print("        TO-VAL composite update OR follow-on TO per ws COO sequencing.")
    return True


# ---------------------------------------------------------------------------
# NFRA_PIPESCRIPT P1b.1: generalize the TOOL-02 false-clean guard INTO comp-pipescript.
# When io/postdeps is queried about a NON-medallion estate thread/resource (owned by
# globgrph/stitch/portal-consumer-tools/none per the estate-coverage resolver), emit the
# LOUD canonical "OUT-OF-SCOPE for comp-pipescript -> see {owning_tool}" + exit 2 -- never a
# silent "Unknown" a coverage grep miscounts as clean (the find-dualbiz io=Unknown trigger;
# folds the G3 ruling + the io/postdeps bd-only silent-Unknown class). comp-pipescript-owned
# (medallion) args and genuinely-unknown args fall through to the existing handling.
# (deployed already emits explicit per-tree UNCOVERED rows by TOOL-01/03 design -- non-silent.)
# ---------------------------------------------------------------------------
_ESTATE_RESOLVER = Path(__file__).resolve().parent / "estate-coverage-resolver.json"
_ESTATE_OWNER_CACHE = None


def _load_estate_owner_map():
    global _ESTATE_OWNER_CACHE
    if _ESTATE_OWNER_CACHE is not None:
        return _ESTATE_OWNER_CACHE
    m = {"thread": {}, "resource": {}, "nt_owners": {}}
    try:
        data = json.loads(_ESTATE_RESOLVER.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        _ESTATE_OWNER_CACHE = m
        return m
    for t in data.get("threads", []):
        m["thread"][t.get("thread_id", "")] = (t.get("named_thread", ""), t.get("owning_tool", ""))
        m["nt_owners"].setdefault(t.get("named_thread", ""), set()).add(t.get("owning_tool", ""))
    for nt, rs in data.get("resources_by_named_thread", {}).items():
        for r in rs:
            m["resource"][r] = nt
    _ESTATE_OWNER_CACHE = m
    return m


def _emit_oos(raw, nt, tool):
    sys.stderr.write(
        f"OUT-OF-SCOPE for comp-pipescript -> see {tool} "
        f"(estate thread '{nt}' / '{raw}' is {tool}-owned, NOT medallion; comp-pipescript "
        f"models only the medallion data-pipeline). Run `pipescript {nt}` for its traversal.\n"
    )
    sys.exit(2)


def _estate_oos_guard(raw):
    """LOUD OUT-OF-SCOPE + exit 2 if `raw` names a non-medallion estate thread/resource.

    No-op (returns) for comp-pipescript-owned (medallion) args + genuinely-unknown args
    (those fall through to the caller's existing Unknown handling). Fail-open if the resolver
    is unreadable -- never block on missing data, and the caller's Unknown path is still LOUD.
    """
    if not raw:
        return
    m = _load_estate_owner_map()
    if not m["thread"]:
        return
    key = re.sub(r"\.(py|json|ya?ml)$", "", str(raw).replace("\\", "/").split("/")[-1])
    hit = m["thread"].get(raw) or m["thread"].get(key)
    if hit and hit[1] and hit[1] != "comp-pipescript":
        _emit_oos(raw, hit[0], hit[1])
    nt = m["resource"].get(raw) or m["resource"].get(key)
    if nt and "comp-pipescript" not in m["nt_owners"].get(nt, set()):
        owners = "/".join(sorted(o for o in m["nt_owners"].get(nt, set()) if o))
        _emit_oos(raw, nt, owners or "globgrph")


def _generalist_io_fallback(raw_id, pipeline_tried):
    """R-2 GENERALIST FALLBACK: derive I/O by AST for a real .py the curated DAG does not carry.

    Returns True if it HANDLED the request (printed a manifest), False to let the caller run its
    normal unknown-script path. Deliberately conservative about when it fires:

      - only for an argument that resolves to an EXISTING FILE on disk (a bare unknown script ID
        is still a genuine unknown-in-tree, and saying so remains the right answer);
      - only for .py.

    WHY IT PRINTS PROVENANCE LOUDLY: this manifest is a DIFFERENT KIND OF ANSWER than the curated
    DAG's -- no chain membership, no run order, no column gaps, no portal consumers, because AST
    cannot see those. A reader who cannot tell which engine answered would over-trust the thinner
    one, so the header names the engine and the limits. (Same discipline as comp-iam's DESIRED-vs-
    APPLIED split: the instrument must say what KIND of claim it is making.)
    """
    cand = (raw_id or '').replace('\\', '/')
    if not cand.endswith('.py'):
        return False
    path = cand if os.path.isfile(cand) else None
    if path is None:
        # Repo-root-relative retry, so the fallback works from a subdirectory too. Root is derived
        # from THIS file's location (org/modules/graph/ -> up 3), not from cwd -- cwd is exactly
        # what a caller in portal/ or data/ would have wrong.
        alt = _THIS_DIR.parent.parent.parent / cand
        if alt.is_file():
            path = str(alt)
    if path is None:
        return False
    try:
        import script_io_ast as _sio
    except ImportError:
        try:
            from org.modules.graph import script_io_ast as _sio      # noqa: F401
        except ImportError:
            return False
    res = _sio.derive_script_io(path)
    print(f"OUT-OF-GRAPH SCRIPT -- the [{pipeline_tried}] curated DAG does not carry this file.")
    print("Answering from a DETERMINISTIC AST DERIVATION instead of refusing (R-2 generalist).")
    print("  ENGINE:  AST (deterministic, source-derived) -- NOT the curated pipeline graph.")
    print("  ABSENT:  chain membership, run order, column gaps, portal consumers. AST cannot see")
    print("           those; do NOT read their absence here as their absence in the estate.")
    print()
    print(_sio.render(res, rel=cand))
    return True


def cmd_io(args):
    # ADHC_COMPIL_V5.002 -- Lambda-path-mode short-circuit (AC1+AC2+AC3+AC4)
    if _lambda_pipescript_io(args.script_id):
        return

    # NFRA_PIPESCRIPT P1b.1: LOUD OUT-OF-SCOPE (exit 2) for a non-medallion estate thread/
    # resource -- never a silent Unknown counted as clean (the find-dualbiz io=Unknown class).
    _estate_oos_guard(args.script_id)

    pipeline = getattr(args, 'pipeline', 'bd-gold') or 'bd-gold'

    # NFRA_DEBTSCAN.TOOL-02 scope resolution (mirrors `deployed`): --firm beats
    # path auto-detect beats the bd-gold default. A data/<dir>/scripts/... path
    # routes to that tree's OWN graph -- never the bd fallback.
    _firm = getattr(args, 'firm', None)
    _matched = False
    if _firm:
        pipeline = _FIRM_TO_PIPELINE[_firm]
    elif getattr(args, 'pipeline', None) in (None, 'bd-gold'):
        _np = (args.script_id or '').replace('\\', '/')
        for _dir, _pk in _DATADIR_TO_PIPELINE.items():
            if f"data/{_dir}/scripts/" in _np or _np.startswith(f"data/{_dir}/"):
                pipeline = _pk
                _matched = True
                break
        if not _matched:
            # F2 (NFRA_COMPTOOL_USEPATHS): no path hint -> AUTO-WALK the gold trees so a bare
            # non-bd id (mdpf_aggregate_aua, a cot/canonical stem) resolves to its OWN pipeline
            # instead of the bd-gold default -> Unknown. Precise/unique match only (else fall through).
            _aw = _autowalk_pipeline_for_script(args.script_id)
            if _aw:
                pipeline = _aw
                _matched = True

    if pipeline not in ('bd-gold', 'bd', 'inf'):
        # Explicit specific pipeline: direct DAG lookup (no cross-pipeline disambiguation needed)
        dag = _build_dag(pipeline)
        # Canonicalize so path/filename forms match graph ids (TOOL-02; ADHC_COMPIL.008)
        script_id = _canonicalize_script_id(args.script_id).upper()
        sio = dag.scripts.get(script_id)
        if not sio:
            # mdpf/silver-style graphs key by exact stem (case-sensitive)
            _stem = _canonicalize_script_id(args.script_id)
            sio = dag.scripts.get(_stem)
            if sio:
                script_id = _stem
        if not sio:
            matches = [s for s in dag.scripts if script_id in s.upper()]
            if len(matches) == 1:
                sio = dag.scripts[matches[0]]
                script_id = matches[0]
            elif matches:
                print(f"Multiple matches: {', '.join(matches)}")
                sys.exit(1)
            else:
                # GENERALIST FALLBACK (R-2, Andrew-direct 2026-08-05: "it needs to be a script io
                # generalist, not bound to a handful of gold pipelines"). Before declaring the
                # script unknown, check whether it is a REAL first-party .py that simply lives
                # outside the curated DAG's roster -- 6 script trees do, incl. data/assets (77
                # files, the OPAL_ASSETS monolith, DEPLOYABLE per Rule 13). For those, answer the
                # question ASKED from a deterministic AST derivation rather than refusing.
                # The DAG stays authoritative wherever it HAS the script; this only runs on a miss.
                if _generalist_io_fallback(args.script_id, pipeline):
                    return
                print(f"Unknown script in tree [{pipeline}]: {script_id}")
                print(f"  (this is the {pipeline} graph -- NOT a bd fallback; TOOL-02 provenance)")
                print(f"Valid IDs: {', '.join(sorted(dag.scripts.keys()))}")
                sys.exit(1)
    else:
        # WS-2 (NFRA_SCRIPTGEN, Andrew-direct 2026-08-05: "curated-first, AST-always dispatch"):
        # nothing resolved this id to a curated tree at all (no explicit --pipeline/--firm, no
        # data/<tree>/scripts/ path match, no auto-walk hit -- pipeline is sitting on the bare
        # 'bd-gold' default with _matched False). Before handing it to the bd/inf-only resolver
        # (whose failure path is a bd-scoped "Script not found"), try the deterministic AST
        # generalist on a real .py file so an out-of-roster tree (data/assets, data/smartx, ...)
        # gets answered instead of misreported against the wrong graph. Only fires when the caller
        # gave NO disambiguating signal at all; an explicit --pipeline bd-gold / --firm / bd|inf
        # hint is respected literally and skips this (WS-1 acceptance: existing values keep their
        # meaning).
        if not _matched and not _firm and getattr(args, 'pipeline', None) is None:
            # Name the REAL tree via the predicate when the path carries one, instead of the
            # "<no curated tree>" placeholder. A reader who is told which tree they are in can act;
            # a placeholder just says the tool gave up.
            _pred_io = _resolve_tree_from_path(args.script_id)
            _tree_label = f"{_pred_io[0]}/{_pred_io[1]} (no curated DAG)" if _pred_io else "<no curated tree>"
            if _generalist_io_fallback(args.script_id, _tree_label):
                return
        # Default/shorthand: always route through resolver so disambiguation fires before any result
        hint = pipeline if pipeline in ('bd', 'inf') else None
        dag, script_id = _auto_resolve_script_id(args.script_id, hint)
        sio = dag.scripts[script_id]

    if args.json:
        # NFRA_COMPTOOLS.PREFIX-READS: the JSON surface gets the prefix edges too. Leaving it
        # keyed on dag.s3_keys alone would keep every MACHINE consumer blind while the text
        # output reads complete -- the same silence this TO closes, in the surface where it is
        # harder to notice. Purely ADDITIVE: existing entries keep their shape, so a consumer
        # reading `reads` sees more rows, never differently-shaped ones.
        _lpr = getattr(sio, 'local_prefix_reads', {})
        _reads = [{"constant": c, "s3_key": dag.s3_keys[c].s3_path,
                   "kind": "PREFIX" if dag.s3_keys[c].is_prefix else "KEY"}
                  for c in sio.reads if c in dag.s3_keys]
        _reads += [{"constant": c, "s3_key": p, "kind": "PREFIX", "source": "local-const"}
                   for c, p in sorted(_lpr.items()) if p]
        print(json.dumps({
            "script_id": script_id,
            "filename": sio.filename,
            "pipeline": sio.pipeline,
            "group": sio.group,
            "run_order": sio.run_order,
            "reads": _reads,
            "writes": [{"constant": c, "s3_key": dag.s3_keys[c].s3_path}
                       for c in sio.writes if c in dag.s3_keys],
            # NEVER dropped -- an empty list is a measured zero, not an absent field.
            "unresolved_prefix_reads": sorted(c for c, p in _lpr.items() if not p),
        }, indent=2))
        return

    print(f"I/O MANIFEST: {script_id} ({sio.filename}) [{sio.pipeline}]")
    print(f"  Group: {sio.group} | Order: {sio.run_order}")
    print()

    if sio.reads:
        print(f"  READS ({len(sio.reads)}):")
        for const in sio.reads:
            sk = dag.s3_keys.get(const)
            # NFRA_COMPTOOLS.PREFIX-READS: a locally-defined prefix constant has no s3_layout
            # entry, so it resolves from the script's own module scope instead.
            local_pfx = getattr(sio, 'local_prefix_reads', {}).get(const)
            if sk:
                key = sk.s3_path
            elif local_pfx:
                key = local_pfx
            elif const.startswith('[hardcoded] '):
                key = const[len('[hardcoded] '):]
            else:
                key = '?'
            is_prefix_row = bool((sk and sk.is_prefix) or local_pfx)
            prefix_tag = " [PREFIX]" if is_prefix_row else ""
            func_tag = " [FUNC]" if sk and sk.is_function else ""
            hc_tag = " [HARDCODED]" if const.startswith('[hardcoded] ') else ""
            local_tag = " [LOCAL-CONST]" if local_pfx and not sk else ""
            # Show who writes this key (direct edges)
            writers = dag._writers.get(key, [])
            writers = [w for w in writers if w != script_id]
            # GAP 2: for PREFIX reads, also check implicit FUNC-write providers
            implicit = []
            if is_prefix_row:
                implicit = [w for w in dag._implicit_writers.get(key, [])
                            if w != script_id and w not in writers]
            if writers and implicit:
                writer_str = f" <- {', '.join(writers)}, IMPLICIT: {', '.join(implicit)} (via FUNC-key)"
            elif implicit:
                writer_str = f" <- IMPLICIT: {', '.join(implicit)} (via FUNC-key)"
            elif writers:
                writer_str = f" <- {', '.join(writers)}"
            else:
                writer_str = " <- (external/silver)"
            display_const = key if const.startswith('[hardcoded] ') else const
            print(f"    {display_const}: {key}{prefix_tag}{func_tag}{hc_tag}{local_tag}{writer_str}")
    else:
        print("  READS: (none detected)")

    # NFRA_COMPTOOLS.PREFIX-READS: a Prefix= argument the extractor could NOT resolve to a
    # literal. Printed ALWAYS and never folded into the count above, because the whole defect
    # this closes is an unseeable input reading as no input -- an unresolved prefix must cost
    # the reader a visible row, not silence. The trace is the bonus; the row is the mechanism.
    _unresolved_pfx = sorted(k for k, v in getattr(sio, 'local_prefix_reads', {}).items() if not v)
    if _unresolved_pfx:
        print()
        print(f"  UNRESOLVED-PREFIX ({len(_unresolved_pfx)}) -- a paginated read whose Prefix= is dynamic:")
        for arg in _unresolved_pfx:
            print(f"    {arg}: <dynamic> [UNRESOLVED-PREFIX] <- (cannot resolve statically; open the script)")

    # Bundle item 4 (CTO 20260722T211318Z): monolith silver reads are DYNAMIC-KEY
    # (silver_table(s3, "fact_x", date)), structurally invisible to the path
    # extractor above -- io on all six MDPF consumers showed only hardcoded gold
    # paths while every silver read was missing. Same literal derivation as the
    # comp-blast extract_assets pass, so the names printed here ARE graph nodes
    # (s3:assets-silver/<name>) and comp-blast resolves each one.
    try:
        from extract_assets import _fact_names_in_strings as _fact_names
    except ImportError:
        from .extract_assets import _fact_names_in_strings as _fact_names
    _spath = Path(sio.file_path) if sio.file_path else None
    if _spath is not None and not _spath.is_absolute():
        _spath = _WORKSPACE / _spath
    _fnames = _fact_names(_spath) if _spath and _spath.exists() else set()
    if _fnames:
        print()
        print(f"  MONOLITH SILVER READS ({len(_fnames)}) -- name-grain, literal-derived"
              " (dynamic keys; the path extractor above cannot see these):")
        for _fn in sorted(_fnames):
            print(f"    {_fn} -> s3:assets-silver/{_fn}  (graph node; comp-blast resolves)")

    # GAP 3: surface rolling-window candidates with a warning
    if sio.rolling_window_candidates:
        print()
        rw_set = set(sio.rolling_window_candidates)
        print(f"  ROLLING-WINDOW WARNING ({len(sio.rolling_window_candidates)} key(s)):")
        print("  The following FUNC keys appear in BOTH READS and WRITES for this script.")
        print("  This is commonly a prior-run (rolling-window) self-read pattern, OR")
        print("  a false positive from alias collision (`key = func(arg)` matches")
        print("  unrelated `get_object(Key=key)` calls elsewhere in the file).")
        print("  ACTION: verify manually -- is this read from a PRIOR run or current run?")
        for const in sorted(rw_set):
            sk = dag.s3_keys.get(const)
            key = sk.s3_path if sk else '?'
            writers = dag._writers.get(key, [])
            other_writers = [w for w in writers if w != script_id]
            src_str = f" <- {', '.join(other_writers)}" if other_writers else " <- (self-write only)"
            print(f"    {const}: {key} [ROLLING-WINDOW?]{src_str}")

    # Column gap analysis: find parquet columns accessed but not in _load_parquet columns= list
    try:
        script_path = _WORKSPACE / sio.file_path
        if script_path.exists():
            from org.modules.graph.extract_pipeline import _extract_column_gaps
            # C io-threading: comp-pipescript io honors COMP_PIPESCRIPT_INCLUDE_HELD (or COMP_INCLUDE_HELD)
            # like `deployed` -- with the override set, a bd gold script's column-gaps ARE read.
            col_gaps = _extract_column_gaps(
                script_path, include_held_override=include_held("COMP_PIPESCRIPT_INCLUDE_HELD"))
            if col_gaps:
                print()
                print(f"  COLUMN GAPS ({len(col_gaps)}) -- columns accessed but not in _load_parquet columns= list:")
                for gap in col_gaps:
                    print(f"    !! {gap['var']}.{gap['col']}")
                    print(f"       accessed at line {gap['access_line']}, not in _load_parquet({gap['key_const']}, columns=[...]) at line {gap['load_line']}")
                    print(f"       loaded cols ({len(gap['loaded_cols'])}): {', '.join(gap['loaded_cols'][:6])}{'...' if len(gap['loaded_cols']) > 6 else ''}")
                    print(f"       FIX: add '{gap['col']}' to the columns= list at line {gap['load_line']}")
    except Exception:
        pass  # Don't break io output if column gap analysis fails

    print()

    if sio.writes:
        print(f"  WRITES ({len(sio.writes)}):")
        for const in sio.writes:
            sk = dag.s3_keys.get(const)
            if sk:
                key = sk.s3_path
            elif const.startswith('[hardcoded] '):
                key = const[len('[hardcoded] '):]
            else:
                key = '?'
            func_tag = " [FUNC]" if sk and sk.is_function else ""
            hc_tag = " [HARDCODED]" if const.startswith('[hardcoded] ') else ""
            # Show who reads this key
            readers = dag._readers.get(key, [])
            readers = [r for r in readers if r != script_id]
            reader_str = f" -> {', '.join(readers)}" if readers else " -> (terminal)"
            display_const = key if const.startswith('[hardcoded] ') else const
            print(f"    {display_const}: {key}{func_tag}{hc_tag}{reader_str}")
    else:
        print("  WRITES: (none detected)")

    # Dynamic refs: non-constant S3 reads (dim files, s3:// URIs, pandas reads)
    from org.modules.graph.extract_pipeline import _extract_dynamic_refs
    try:
        script_path = _WORKSPACE / sio.file_path
        script_content = script_path.read_text(encoding="utf-8", errors="replace")
        dynamic_refs = _extract_dynamic_refs(script_content)
        # Filter out paths already covered by hardcoded extraction
        covered = set(sio.read_keys) | set(sio.write_keys)
        new_dynamic = [d for d in dynamic_refs if not any(
            c.endswith(d.replace('{*}', '').rstrip('/')) or
            d.replace('{*}', '').rstrip('/') in c
            for c in covered
        )]
        if new_dynamic:
            print()
            print(f"  S3-DYNAMIC READS ({len(new_dynamic)}) [runtime-resolved, not in s3_layout]:")
            for path in new_dynamic:
                print(f"    {path}  [read-at-runtime]")
    except Exception:
        pass

    if not sio.reads and not sio.writes:
        print()
        print("  WARN: no s3_layout constants or hardcoded S3 paths detected.")
        print("  Script may use dynamic key construction, DynamoDB, SQS, or non-standard S3 patterns.")
        print("  Manual review of the script body is required for accurate I/O mapping.")

    # Platinum downstream: resolve platinum/* write targets to portal components
    platinum_writes = []
    for const in sio.writes:
        if const.startswith('[hardcoded] '):
            key = const[len('[hardcoded] '):]
        else:
            sk = dag.s3_keys.get(const)
            key = sk.s3_path if sk else None
        if key and 'platinum/' in key:
            platinum_writes.append(key)

    if platinum_writes and not args.no_portal:
        print()
        print("  PORTAL CONSUMERS (platinum keys -> routes -> components):")
        try:
            from org.modules.graph.extract_routes import build_routing_table
            rt = build_routing_table(_WORKSPACE)
            found_any = False
            for key in sorted(set(platinum_writes)):
                # Match routes: exact match or parameterized match ({*} in key)
                key_pattern = re.escape(key).replace(r'\{\*\}', '[^/]+') if '{*}' in key else None
                matching = []
                for r in rt.routes:
                    if not r.s3_key:
                        continue
                    if key_pattern:
                        if re.fullmatch(key_pattern, r.s3_key):
                            matching.append(r)
                    else:
                        # Exact or suffix match
                        if r.s3_key == key or r.s3_key.endswith(key) or key.endswith(r.s3_key):
                            matching.append(r)
                if matching:
                    found_any = True
                    print(f"    {key}")
                    for r in matching:
                        comps = ', '.join(r.components) if r.components else '(unknown component)'
                        auth_str = 'edge' if r.auth_edge else ('api-gw' if r.auth_api_gw else 'none')
                        print(f"      endpoint: {r.endpoint_function or '(unnamed)'} -> {r.url_pattern}")
                        print(f"      auth: {auth_str} | origin: {r.cf_origin_type}")
                        print(f"      components: {comps}")
            if not found_any:
                print("    (no route matches -- these platinum keys may be served via catch-all behavior)")
                print("    TIP: comp-platinum reverse <key> for a targeted reverse lookup")
        except Exception as e:
            print(f"    (routing table load failed: {e})")
    elif platinum_writes and args.no_portal:
        print()
        print(f"  PORTAL CONSUMERS: {len(platinum_writes)} platinum write(s) -- skipped (--no-portal)")


def cmd_chain(args):
    # ADHC_COMPIL_V4.019 Bug 1.2 fix: honor --pipeline flag (was silently
    # ignored — chain --pipeline inf-gold returned BD chain regardless).
    pipeline = getattr(args, 'pipeline', 'bd-gold') or 'bd-gold'
    dag = _build_dag(pipeline)
    chain_name = args.chain_name.lower()

    if chain_name not in dag.chains:
        print(f"Unknown chain: {chain_name} for pipeline {pipeline}")
        if dag.chains:
            print(f"Valid chains for {pipeline}: {', '.join(sorted(dag.chains.keys()))}")
        else:
            print(f"No chains registered for pipeline {pipeline}.")
            print("Chain config lives in gold_pipeline_deps.yaml; INF-side chain config not yet populated.")
        sys.exit(1)

    script_ids = dag.chains[chain_name]
    print(f"CHAIN [{pipeline}]: {chain_name} ({len(script_ids)} scripts)")
    print()

    for i, sid in enumerate(script_ids, 1):
        sio = dag.scripts.get(sid)
        if sio:
            print(f"  {i:2d}. {sid:6s} {sio.filename}")
            print(f"         reads: {len(sio.read_keys)} | writes: {len(sio.write_keys)}")
        else:
            print(f"  {i:2d}. {sid:6s} (not found in scripts)")


def cmd_feeds(args):
    pipeline = getattr(args, 'pipeline', 'bd-gold') or 'bd-gold'
    dag = _build_dag(pipeline)
    script_id = args.script_id.upper()
    sio = dag.scripts.get(script_id)
    if not sio:
        matches = [s for s in dag.scripts if script_id in s.upper()]
        if len(matches) == 1:
            sio = dag.scripts[matches[0]]
            script_id = matches[0]
        elif matches:
            print(f"Multiple matches: {', '.join(matches)}")
            sys.exit(1)
        else:
            explicit = pipeline
            if explicit not in ('bd-gold', 'bd', 'inf'):
                print(f"Unknown script: {script_id}")
                sys.exit(1)
            hint = explicit if explicit in ('bd', 'inf') else None
            dag, script_id = _auto_resolve_script_id(args.script_id, hint)
            sio = dag.scripts[script_id]

    upstream = dag.feeds(script_id)
    if not upstream:
        print(f"{script_id}: no upstream pipeline dependencies (reads from silver or external)")
        return

    if args.json:
        print(json.dumps([
            {"script": u, "s3_key": k, "constant": c}
            for u, k, c in upstream
        ], indent=2))
        return

    print(f"UPSTREAM FEEDS into {script_id}:")
    print()
    # Group by upstream script
    by_script: dict[str, list[tuple[str, str]]] = {}
    for u_script, s3_key, const in upstream:
        by_script.setdefault(u_script, []).append((s3_key, const))

    for u_script, keys in sorted(by_script.items()):
        print(f"  {u_script}:")
        for s3_key, const in keys:
            print(f"    {const}: {s3_key}")
    print()
    print(f"  Total: {len(upstream)} artifacts from {len(by_script)} scripts")


def cmd_consumers(args):
    pipeline = getattr(args, 'pipeline', 'bd-gold') or 'bd-gold'
    dag = _build_dag(pipeline)
    script_id = args.script_id.upper()
    sio = dag.scripts.get(script_id)
    if not sio:
        matches = [s for s in dag.scripts if script_id in s.upper()]
        if len(matches) == 1:
            sio = dag.scripts[matches[0]]
            script_id = matches[0]
        elif matches:
            print(f"Multiple matches: {', '.join(matches)}")
            sys.exit(1)
        else:
            explicit = pipeline
            if explicit not in ('bd-gold', 'bd', 'inf'):
                print(f"Unknown script: {script_id}")
                sys.exit(1)
            hint = explicit if explicit in ('bd', 'inf') else None
            dag, script_id = _auto_resolve_script_id(args.script_id, hint)
            sio = dag.scripts[script_id]

    downstream = dag.consumers(script_id)
    if not downstream:
        print(f"{script_id}: no downstream pipeline consumers (terminal or portal-only)")
        return

    if args.json:
        print(json.dumps([
            {"script": d, "s3_key": k, "constant": c}
            for d, k, c in downstream
        ], indent=2))
        return

    print(f"DOWNSTREAM CONSUMERS of {script_id}:")
    print()
    by_script: dict[str, list[tuple[str, str]]] = {}
    for d_script, s3_key, const in downstream:
        by_script.setdefault(d_script, []).append((s3_key, const))

    for d_script, keys in sorted(by_script.items()):
        print(f"  {d_script}:")
        for s3_key, const in keys:
            print(f"    {const}: {s3_key}")
    print()
    print(f"  Total: {len(downstream)} artifacts consumed by {len(by_script)} scripts")


def cmd_overlap(args):
    dag_a, a = _auto_resolve_script_id(args.script_a)
    dag_b, b = _auto_resolve_script_id(args.script_b)
    # Overlap is meaningful within one pipeline; use the first script's dag
    dag = dag_a
    if b not in dag.scripts:
        print(f"Scripts {a!r} and {b!r} are in different pipelines; cross-pipeline overlap not supported.")
        print("  Use --pipeline bd or --pipeline inf to scope both scripts to one pipeline.")
        sys.exit(1)

    result = dag.overlap(a, b)
    if not result:
        print(f"No shared S3 artifacts between {a} and {b}")
        return

    print(f"OVERLAP: {a} <-> {b}")
    print()
    for relationship, keys in result.items():
        print(f"  {relationship}:")
        for key in keys:
            print(f"    {key}")
    print()


def cmd_inject(args):
    dag = _build_dag()
    added = inject_pipeline_edges(dag, _WORKSPACE)
    if added is None:
        print("No comp-trace graph cache found. Run comp-build first.")
        sys.exit(1)
    print(f"Injected {added} pipeline edges into comp-trace graph cache.")


def cmd_stats(args):
    dag = _build_dag()
    print("PIPELINE STATISTICS")
    print(f"  Scripts:    {len(dag.scripts)}")
    print(f"  S3 keys:    {len(dag.s3_keys)} ({sum(1 for k in dag.s3_keys.values() if k.is_prefix)} prefixes, {sum(1 for k in dag.s3_keys.values() if k.is_function)} functions)")
    print(f"  Chains:     {len(dag.chains)}")
    print(f"  Groups:     {len(dag.groups)}")
    print(f"  Catalog:    {len(dag.catalog)} entries")
    print()

    # Edge counts
    total_reads = sum(len(s.read_keys) for s in dag.scripts.values())
    total_writes = sum(len(s.write_keys) for s in dag.scripts.values())
    print(f"  Total read edges:  {total_reads}")
    print(f"  Total write edges: {total_writes}")
    print()

    # Scripts with no detected reads (likely missing extraction)
    no_reads = [sid for sid, s in dag.scripts.items() if not s.reads]
    if no_reads:
        print(f"  WARNING: {len(no_reads)} scripts with no detected reads:")
        for sid in sorted(no_reads):
            print(f"    {sid}")
    print()

    # Scripts with no detected writes
    no_writes = [sid for sid, s in dag.scripts.items() if not s.writes]
    if no_writes:
        print(f"  NOTE: {len(no_writes)} scripts with no detected writes:")
        for sid in sorted(no_writes):
            print(f"    {sid}")


def _get_ec2_manifest_service(service_key: str) -> dict:
    """Read a service entry from EC2_MANIFEST.json. Returns {} if not found."""
    manifest_path = _WORKSPACE / "infra" / "aws" / "ec2" / "EC2_MANIFEST.json"
    try:
        import json as _json
        data = _json.loads(manifest_path.read_text(encoding="utf-8"))
        return data.get("services", {}).get(service_key, {})
    except Exception:
        return {}


def _deployed_sweep_all(args):
    """NFRA_DEBTSCAN.TOOL-01: sweep EVERY tree (bd + inf + cot from PIPELINE_MAP, + mdpf
    check-only). Each tree runs its own single-tree deployed check against ONLY its own
    bucket (firm separation -- no cross-bucket read). A per-tree banner names the bucket
    so every MATCH/STALE/MISSING row is bucket-attributed (an un-attributed row is how a
    stranded-deploy blind spot hides -- the MDPF_COUNTS class)."""
    import copy
    print("DEPLOYED SWEEP: all trees -- firm-separated, each reads ONLY its own bucket")
    print(f"  Trees: {', '.join(f'{pk} -> s3://{b}' for pk, b in _ALL_DEPLOYED_TREES)}")
    print()
    for pk, bucket in _ALL_DEPLOYED_TREES:
        print(f"=== TREE {pk}  ->  s3://{bucket} ===")
        _a = copy.copy(args)
        _a.pipeline = pk
        _a.script_id = ''
        _a.firm = None
        rc = cmd_deployed(_a)
        if rc:
            return rc
        print()
    return 0


RC_NOT_DECIDABLE = 4  # FWD-10: a verdict-bearing partial is neither clean nor a finding.


class _PipescriptBudgetReached(Exception):
    """Raised only after the Rule-T partial verdict has been rendered."""


def cmd_deployed(args):
    """Public deployed command: preserve its verdict-bearing partial rc at the boundary."""
    try:
        return _cmd_deployed(args)
    except _PipescriptBudgetReached:
        return RC_NOT_DECIDABLE


def _cmd_deployed(args):
    """Compare local gold + silver script files against their S3-uploaded code versions.

    Default (--pipeline bd-gold): BD gold + BD silver vs opal-data-bd.
    --pipeline inf-gold: INF gold scripts vs opal-data-inf/code/gold/
      (runner key read from EC2_MANIFEST.json: inf-gold-layer-runner).
    --pipeline bd-silver: BD silver scripts only.
    --pipeline inf-silver: INF silver scripts vs opal-data-inf/code/silver/.
    --pipeline mdpf: MDPF scripts (gold + backfill + feeders + bronze) vs
      s3://opal-data-mdpf/code/scripts/<layer>/ (ADHC_DEPINT widen 2026-06-08 --
      closes the opal-data-bd-only blind spot that hid the stale MDPF rollup
      behind the MDPF_COUNTS incident). MDPF preserves scripts/<layer>/ under
      code/, a different layout than BD/INF; enumerated by directory glob (no DAG).
    --pipeline {bd,inf,cot}-bronze: bronze tree only (NFRA_DEBTSCAN.TOOL-03).
      Bronze is also folded into the full-tree views (bd-gold/inf-gold/cot)
      and the all-trees sweep. Aux prefixes (bronze-runner/runner/exporter/
      cleanup/manual_api) ride along as CHECK-ONLY rows; an unmapped prefix
      emits UNCOVERED, never silent-clean.

    Output is prefixed [bd-gold] / [inf-gold] / [bd-silver] / [inf-silver] /
    [BRONZE] / [aux:<prefix>] / [mdpf:<layer>].
    Uses S3 ETag (MD5) comparison."""
    import shutil
    import subprocess

    budget_state = getattr(args, "_pipescript_budget_state", None)
    if budget_state is None:
        try:
            budget_s, budget_source = _compbudget.resolve_budget(getattr(args, "budget", None))
        except ValueError as exc:
            print(f"comp-pipescript deployed: ERROR: --budget {exc}")
            return 2
        budget_state = {
            "budget_s": budget_s,
            "budget_source": budget_source,
            "clock": _compbudget.Clock(budget_s),
            "units": 0,
            "deferred_reasons": [],
        }
        # The all-trees sweep copies argparse's namespace once per tree. Keeping the state on
        # that namespace gives every timeout-bearing operation ONE wall-clock allowance rather
        # than silently handing each firm a fresh 90 seconds.
        setattr(args, "_pipescript_budget_state", budget_state)
    budget_s = budget_state["budget_s"]
    budget_source = budget_state["budget_source"]
    budget_clock = budget_state["clock"]

    def _budget_reached(unit, reason):
        """Render the Rule-T partial state before ending this verdict-bearing sweep."""
        budget_state["deferred_reasons"].append(f"{unit}: {reason}")
        print("  BUDGET REACHED: %s s (%s); scanned 0 of 1 %s; results are a PREFIX, not the "
              "answer; the timeout-bearing operation was DEFERRED, not run; NO CURSOR: this is "
              "one indivisible remote operation -- the supplied --cursor is unchanged; re-run "
              "with a larger --budget."
              % (_compbudget.fmt(budget_s), budget_source, unit))
        print("  STATE: NOT-DECIDABLE  (rc=%d, distinct from a complete deployed verdict; "
              "a PREFIX carries no verdict)" % RC_NOT_DECIDABLE)
        for line in _compbudget.deferred_bucket(1, 1, unit, budget_state["deferred_reasons"]):
            print("  " + line)
        raise _PipescriptBudgetReached()

    def _run_budgeted(argv, timeout_s, unit, **kwargs):
        """Every deployed timeout derives from the one shared clock's remaining allowance."""
        remaining = budget_clock.remaining()
        if remaining is not None and remaining <= 0:
            _budget_reached(unit, "budget exhausted before this operation could start")
        effective_timeout = timeout_s if remaining is None else min(timeout_s, remaining)
        try:
            result = subprocess.run(argv, timeout=effective_timeout, **kwargs)
        except subprocess.TimeoutExpired:
            if remaining is not None and remaining <= timeout_s:
                _budget_reached(unit, "did not return inside the remaining shared budget")
            raise
        budget_state["units"] += 1
        return result

    # --- NFRA_DEBTSCAN.TOOL-01: scope resolution (--firm / path-autodetect / all-trees sweep) ---
    # --pipeline default is None (argparse) so we can tell "user chose a tree" from "no scope given".
    pipeline = getattr(args, 'pipeline', None)
    firm = getattr(args, 'firm', None)
    _raw_script = (getattr(args, 'script_id', '') or '')

    if firm:
        # Explicit single-tree scope by firm/tree (sweeps that tree, its bucket only).
        pipeline = _FIRM_TO_PIPELINE[firm]
    elif _raw_script:
        # Path auto-detect: a data/<dir>/scripts/... filter routes to that tree's pipeline.
        # Generalizes the former cot-only auto-route to every PIPELINE_MAP tree + mdpf
        # (firm separation: each tree's branch reads ONLY its own bucket). A bare id
        # now REFUSES with the tree list (Andrew-direct 2026-07-30; the bd fallback was
        # the wrong-tree clean-MATCH hole ~C exercised on A_01.advisor_assignments.py).
        if not pipeline:
            pipeline = resolve_pipeline_from_arg(_raw_script)
            if pipeline is None:
                _refuse_no_pipeline(_raw_script)
    elif not pipeline:
        # No filter, no firm, no explicit --pipeline -> SWEEP ALL TREES (bd+inf+cot+mdpf).
        return _deployed_sweep_all(args)

    S3_BUCKET = "opal-data-bd"
    S3_GOLD_PREFIX = "code/gold/"
    S3_SILVER_PREFIX = "code/silver/"

    # Table-driven pipeline -> local silver dir (ADHC_DSFLOW.005 INF coverage fix)
    _PIPELINE_SILVER_DIRS = {
        "bd-gold":   _WORKSPACE / "data" / "black_diamond" / "scripts" / "silver",
        "bd-silver": _WORKSPACE / "data" / "black_diamond" / "scripts" / "silver",
        "inf-gold":  _WORKSPACE / "data" / "inf" / "scripts" / "silver",
        "inf-silver": _WORKSPACE / "data" / "inf" / "scripts" / "silver",
        # cot (Cottonwood) — COMPLETELY separate firm pipeline (NFRA_DTAFLP, Andrew
        # sovereign 2026-06-10): deploys to opal-data-cot, never opal-data-bd.
        "cot-gold":  _WORKSPACE / "data" / "cot" / "scripts" / "silver",
        "cot-silver": _WORKSPACE / "data" / "cot" / "scripts" / "silver",
        "cot":       _WORKSPACE / "data" / "cot" / "scripts" / "silver",
    }
    SILVER_LOCAL_DIR = _PIPELINE_SILVER_DIRS.get(
        pipeline, _WORKSPACE / "data" / "black_diamond" / "scripts" / "silver"
    )

    # INF pipeline overrides
    if pipeline in ("inf-gold", "inf-silver", "inf-bronze"):
        S3_BUCKET = "opal-data-inf"

    # MDPF pipeline override (ADHC_DEPINT widen 2026-06-08): MDPF deploys to a
    # DIFFERENT layout -- s3://opal-data-mdpf/code/scripts/<layer>/ (it preserves
    # the scripts/<layer>/ subpath), unlike BD (code/{gold,silver}/) and INF. The
    # stale build_aggregate_aua_timeseries.py at code/scripts/backfill/ caused the
    # MDPF_COUNTS incident because comp-pipescript deployed was opal-data-bd-only.
    if pipeline == "mdpf":
        S3_BUCKET = "opal-data-mdpf"

    # ADVI override (TRUNCLASS PSCRIPT2): the 49F canonical runner chain deploys to the
    # per-client bucket's BUCKET-ROOT _code/ (CTO GOLDHOME re-point 2026-08-18). Bucket
    # derives from the ONE declaration, never a second literal.
    if pipeline == "advi":
        S3_BUCKET = (_CODE_TREES["advi"]["bucket"] if _CODE_TREES is not None
                     else "opal-data-49financial")

    # cot pipeline override (NFRA_DTAFLP, Andrew sovereign 2026-06-10): cot is a
    # COMPLETELY separate firm pipeline. Its gold/silver/bronze deploy to
    # opal-data-cot/code/{gold,silver,bronze}/ (standard BD/INF layout, different
    # bucket) -- NEVER opal-data-bd. Closes the cot deployed-check blind spot.
    if pipeline in ("cot-gold", "cot-silver", "cot-bronze", "cot"):
        S3_BUCKET = "opal-data-cot"

    # Sovereign hold (CTO ruling 20260710T233307Z): the bd deploy-verify branch reads LOCAL bd
    # SOURCE content -- hashlib.md5(local_path.read_bytes()) over data/black_diamond/scripts/{gold,
    # silver}/*.py -- AND head-objects opal-data-bd. Both are held touches under the bd/49F
    # prohibition. SKIP the bd branch for a normal agent invocation, NAMED as held (never a silent
    # drop -- the pipescript no-silent-Unknown thesis). COMP_PIPESCRIPT_INCLUDE_HELD=1 re-enables it
    # for the DS deploy-verify cycle (Rule 13) / when the hold lifts. Gating HERE -- before aws_bin
    # and before any local read_bytes -- guarantees no held file is ever opened.
    if is_held_bucket(S3_BUCKET) and not include_held("COMP_PIPESCRIPT_INCLUDE_HELD"):
        print("  SKIP: opal-data-bd (bd) deploy-verify HELD under the sovereign prohibition -- "
              "set COMP_PIPESCRIPT_INCLUDE_HELD=1 (or COMP_INCLUDE_HELD=1) for the DS deploy-verify path.")
        print("  " + _compbudget.within_budget_line(
            budget_state["units"], budget_state["units"], "timeout_bearing_operation",
            budget_s, budget_source, round(budget_clock.elapsed(), 2)))
        for line in _compbudget.deferred_bucket(0, budget_state["units"],
                                                "timeout_bearing_operation", []):
            print("  " + line)
        return 0

    # Resolve aws CLI once, full path -- avoids subprocess PATH-loss on some shells.
    aws_bin = shutil.which("aws") or shutil.which("aws.cmd") or shutil.which("aws.exe")
    if not aws_bin:
        print("  ERROR: aws CLI not found in PATH (checked aws, aws.cmd, aws.exe)")
        sys.exit(2)

    raw_filter = args.script_id.strip() if args.script_id else ""
    if raw_filter:
        # Canonicalize: strip path prefix + .<name>.py suffix (ADHC_COMPIL.008)
        _cf = _canonicalize_script_id(raw_filter)
        script_filter_upper = _cf.upper()
        script_filter_lower = _cf.lower()
        silver_filter_stem = script_filter_lower  # .py and .<name> already stripped
    else:
        script_filter_upper = None
        script_filter_lower = None
        silver_filter_stem = None

    aws_env = os.environ.copy()
    aws_env.setdefault("AWS_EC2_METADATA_DISABLED", "true")
    aws_env.setdefault("AWS_METADATA_SERVICE_NUM_ATTEMPTS", "1")
    aws_env.setdefault("AWS_PAGER", "")

    # Instrument-fix @c9be07b413 (gap 1+4): every s3_key any pass probes is recorded here,
    # so the S3-side enumeration below can tell rendered objects from invisible ones.
    _checked_s3_keys = set()

    def _check_one(layer_tag, label, local_path, s3_key):
        """Returns (status, info_lines). Prints nothing -- caller does."""
        _checked_s3_keys.add(s3_key)
        if not local_path.exists():
            return "LOCAL_MISSING", []
        # A DIGEST WITHOUT ITS NORMALISATION IS NOT AN IDENTITY (2026-08-26, 0.8.0_AE_CloudComp~F,
        # routed by 0.6.2_AE_PartnerETL~A). This read was raw bytes only: a CRLF working-tree file
        # against an LF S3 object digests differently FOREVER, so the row reported STALE no matter
        # how many times it was uploaded -- 16 of 160 tracked .py under the assets/mdpf script trees
        # are CRLF in the tree. Two harms, and the second is the one that matters: a lane chasing
        # MATCH re-uploads forever (each a production write), and A VERDICT THAT CAN NEVER TURN
        # GREEN IS NOT A CHECK, IT IS NOISE WEARING A CHECK'S UNIFORM -- permanent false STALEs
        # sitting beside real ones train a reader to discount the signal.
        local_bytes = local_path.read_bytes()
        try:
            result = _run_budgeted(
                [aws_bin, "s3api", "head-object",
                 "--bucket", S3_BUCKET,
                 "--key", s3_key,
                 "--query", "ETag",
                 "--output", "text"],
                15, "s3_head_object", capture_output=True, text=True, env=aws_env,
            )
        except subprocess.TimeoutExpired:
            return "TIMEOUT", [f"(aws CLI hung; AWS_EC2_METADATA_DISABLED={aws_env.get('AWS_EC2_METADATA_DISABLED', '')})"]
        if result.returncode != 0:
            stderr = (result.stderr or "").strip()
            # Disambiguate "S3 says no such key" from "we couldn't reach S3 at all".
            # MISSING_ON_S3 should only fire on a genuine 404 from HeadObject; any credential/network
            # failure is AWS_UNREACHABLE -- MATCH vs MISSING was never verifiable.
            _unreach_sig = (
                'Unable to locate credentials',
                'could not be found',         # bad/missing profile
                'ExpiredToken',
                'InvalidAccessKeyId',
                'SignatureDoesNotMatch',
                'InvalidClientTokenId',
                'Could not connect to the endpoint',
                'EndpointConnectionError',
                'ConnectTimeoutError',
                'ReadTimeoutError',
                'AccessDenied',
            )
            if any(sig in stderr for sig in _unreach_sig):
                return "AWS_UNREACHABLE", [stderr]
            if stderr:
                return "MISSING_ON_S3", [stderr]
            return "MISSING_ON_S3", []
        s3_etag = result.stdout.strip().strip('"')
        return classify_digest(local_bytes, s3_etag)

    # Header varies by pipeline
    if pipeline == "inf-gold":
        inf_svc = _get_ec2_manifest_service("inf-gold-layer-runner")
        inf_instance = inf_svc.get("instance_id", "unknown")
        print("DEPLOYED STATUS [inf-gold]: local repo vs s3://opal-data-inf/code/{gold,silver,bronze}/")
        print(f"  Runner: inf-gold-layer-runner ({inf_instance})")
    elif pipeline == "mdpf":
        _hdr_layers = (
            ",".join(sorted(_CODE_TREES["mdpf"]["layers"]))
            if _CODE_TREES is not None
            else "UNKNOWN -- CODE_TREES unavailable"
        )
        print(
            "DEPLOYED STATUS [mdpf]: local repo vs "
            f"s3://opal-data-mdpf/code/scripts/{{{_hdr_layers}}}"
        )
        print("  Runner: mdpf-daily-runner")
    elif pipeline == "advi":
        print(f"DEPLOYED STATUS [advi]: local repo vs s3://{S3_BUCKET}/_code/ "
              "(49F canonical runner chain; repo home data/assets/scripts/gold/runners_49f "
              "-- longest-prefix subtree of the shared assets gold home)")
    elif pipeline in ("bd-silver", "inf-silver", "cot-silver"):
        print(f"DEPLOYED STATUS [{pipeline}]: local repo vs s3://{S3_BUCKET}/code/silver/")
    elif pipeline in ("bd-bronze", "inf-bronze", "cot-bronze"):
        print(f"DEPLOYED STATUS [{pipeline}]: local repo vs s3://{S3_BUCKET}/code/bronze/ (NFRA_DEBTSCAN.TOOL-03)")
    elif pipeline in ("cot-gold", "cot"):
        print(f"DEPLOYED STATUS [{pipeline}]: local repo vs s3://opal-data-cot/code/{{gold,silver,bronze}}/")
        print("  Runner: cot-exporter (Cottonwood; NFRA_DTAFLP separate firm pipeline)")
    else:
        print("DEPLOYED STATUS: local repo vs s3://opal-data-bd/code/{gold,silver,bronze}/")
    print()

    matched, stale, missing_s3, local_missing, timed_out, aws_unreach = [], [], [], [], [], []
    # ETAG_NOT_COMPARABLE gets its OWN bucket. The elif chains below carry no else, so an
    # unrecognised status PRINTS but lands in no tally -- it would vanish from every summary
    # count while looking handled. A new verdict without a bucket is a silent drop.
    uncomparable = []
    uncovered = []  # TOOL-03 false-clean guard: tool-blindness, named -- NEVER silent
    aux_drift = []  # TOOL-03 aux CHECK-ONLY drift: visible but NEVER the deploy-gate token
    not_in_tree = []  # SHARED-home non-members: informational, NEVER a defect -- but COUNTED.
    # Why counted (CVO~B 2026-08-05, P8 cold descent): a not-in-tree row was printed and
    # tallied NOWHERE -- not even in UNCOVERED -- so a run whose ONLY rows were not-in-tree
    # produced an all-zero Summary at rc=0, byte-identical to a clean verified run. The
    # reclassification below is CORRECT (absent-on-S3 in a shared home means NOT A MEMBER,
    # not a missing deploy); the defect was that it left no trace in the denominator. The
    # TOOL-02/03 false-clean guard covered the PREFIX-miss case and not the ROSTER-miss one.
    checked_any = False

    # ADHC_COMPIL_V4.019 Bug 1.1 fix: initialize skip_gold so silver-section gating
    # at line ~1010 doesn't UnboundLocalError on inf-gold or silver-only paths.
    # Default True = "gold was skipped"; bd-gold and inf-gold branches flip to False.
    skip_gold = True

    # ---- GOLD layer (DAG-driven for BD/INF; directory-glob for MDPF) ----
    # For non-BD pipelines, skip BD gold entirely unless pipeline == "bd-gold" (default)
    if pipeline == "mdpf":
        # MDPF has no comp-graph DAG -> enumerate the deployed script layers directly.
        # Layout: data/mdpf/scripts/<layer>/X.py -> s3://opal-data-mdpf/code/scripts/<layer>/X.py
        skip_gold = False
        # DERIVED from safe_deploy_core.CODE_TREES -- previously a hardcoded
        # 4-tuple ("gold","backfill","feeders","bronze") against SIX live layers,
        # which made assets_gold/ and silver/ structurally invisible: 4 of 28 .py,
        # including Stage-6 build_dim_model_portfolio.py and BOTH cottonwood
        # scripts. Those two layers are fed from data/assets/, NOT data/mdpf/ --
        # which is why a layer LIST could not express this tree and why adding
        # two names to the old tuple would have skipped both silently.
        if _CODE_TREES is None:
            uncovered.append(
                "[mdpf] CODE_TREES UNAVAILABLE -- safe_deploy_core did not import; "
                "layer set UNKNOWN, refusing to guess"
            )
            _mdpf_layers = {}
        else:
            _mdpf_layers = _CODE_TREES["mdpf"]["layers"]
        _mdpf_shared = (
            set()
            if _CODE_TREES is None
            else set(_CODE_TREES["mdpf"].get("shared_repo_homes", ()))
        )
        for _layer, (_repo_home, _s3_prefix) in sorted(_mdpf_layers.items()):
            _ldir = _WORKSPACE / _repo_home
            if not _ldir.is_dir():
                # FAIL LOUDLY, NEVER `continue`. A declared layer whose repo home
                # is absent is a DECLARATION DEFECT, not an empty layer -- the old
                # silent `continue` is what let a wrong layer list read as a clean
                # sweep (0 MATCH / 0 UNCOVERED / rc=0). This check sits UPSTREAM of
                # the skip, which is the only place it can fire: a guard downstream
                # of the routing it audits cannot see what the routing dropped.
                uncovered.append(
                    f"[mdpf:{_layer}] DECLARED repo_home MISSING: {_repo_home} "
                    "-- declaration and repo disagree"
                )
                checked_any = True
                print(
                    f"  [mdpf:{_layer}] {'(declared repo_home absent)':<44} "
                    f"{'UNCOVERED':<14}"
                )
                print(f"             declared: {_repo_home}")
                continue
            for p in sorted(_ldir.glob("*.py")):
                if p.name.startswith("__") or p.name.endswith("_fixtures.py"):
                    continue
                if script_filter_lower and script_filter_lower not in p.stem.lower():
                    continue
                label = f"[mdpf:{_layer}] {p.name}"
                checked_any = True
                status, extras = _check_one("mdpf", label, p, f"{_s3_prefix}{p.name}")
                # SHARED repo home: only a subset of the dir deploys to this
                # prefix, so "absent on S3" means NOT A MEMBER, not a missing
                # deploy. Reclassified as informational and NOT counted as a
                # defect. STALE/MATCH still bind -- those are real membership.
                if status == "MISSING_ON_S3" and _layer in _mdpf_shared:
                    # TOKEN RENAMED 2026-08-19 (CTO ruling, H8): `not-in-tree` read as
                    # "the tool does not cover this tree" -- which is how it reached CTO as a
                    # routed coverage defect -- when it means "this file is not a MEMBER of
                    # THIS shared home's deploy set". The NOTHING-VERIFIED banner below already
                    # says the right thing, but A ROW TOKEN TRAVELS IN REPORTS WITHOUT ITS
                    # BANNER, so the token had to carry its own frame. "(no verdict)" is the
                    # load-bearing half: it states that nothing was concluded about this file.
                    print(f"  [mdpf:{_layer}] {p.name:<44} {'NOT-A-MEMBER (no verdict)':<26}")
                    not_in_tree.append(label)
                    continue
                print(f"  [mdpf:{_layer}] {p.name:<44} {status:<14}")
                for line in extras:
                    print(f"             {line}")
                if status == "MATCH":
                    matched.append(label)
                elif status == "STALE":
                    stale.append(label)
                elif status == "MISSING_ON_S3":
                    missing_s3.append(label)
                elif status == "LOCAL_MISSING":
                    local_missing.append(label)
                elif status == "TIMEOUT":
                    timed_out.append(label)
                elif status == "AWS_UNREACHABLE":
                    aws_unreach.append(label)
                elif status == "ETAG_NOT_COMPARABLE":
                    uncomparable.append(label)
    elif pipeline == "advi":
        # ADVI (TRUNCLASS PSCRIPT2): the 49F canonical runner chain, CODE_TREES-driven like
        # mdpf -- layers derive from the ONE declaration, never a second dir list. Membership
        # at _code/ is exact (runners_49f only, per the declaration's own note), so
        # MISSING_ON_S3 is a REAL verdict here -- no shared-home NOT-A-MEMBER reclass.
        skip_gold = False
        if _CODE_TREES is None:
            uncovered.append(
                "[advi] CODE_TREES UNAVAILABLE -- safe_deploy_core did not import; "
                "layer set UNKNOWN, refusing to guess"
            )
        else:
            for _layer, (_repo_home, _s3_prefix) in sorted(_CODE_TREES["advi"]["layers"].items()):
                _ldir = _WORKSPACE / _repo_home
                if not _ldir.is_dir():
                    uncovered.append(
                        f"[advi:{_layer}] DECLARED repo_home MISSING: {_repo_home} "
                        "-- declaration and repo disagree"
                    )
                    checked_any = True
                    print(f"  [advi:{_layer}] {'(declared repo_home absent)':<44} {'UNCOVERED':<14}")
                    print(f"             declared: {_repo_home}")
                    continue
                for p in sorted(_ldir.glob("*.py")):
                    if p.name.startswith("__") or p.name.endswith("_fixtures.py"):
                        continue
                    # Filter matches stem OR posix subpath: _canonicalize_script_id keeps the
                    # runners_49f/ segment for paths under the shared home, so a stem-only
                    # test would skip the very file the caller named.
                    if script_filter_lower and (script_filter_lower not in p.stem.lower()
                                                and script_filter_lower not in p.as_posix().lower()):
                        continue
                    label = f"[advi:{_layer}] {p.name}"
                    checked_any = True
                    status, extras = _check_one("advi", label, p, f"{_s3_prefix}{p.name}")
                    print(f"  [advi:{_layer}] {p.name:<44} {status:<14}")
                    for line in extras:
                        print(f"             {line}")
                    if status == "MATCH":
                        matched.append(label)
                    elif status == "STALE":
                        stale.append(label)
                    elif status == "MISSING_ON_S3":
                        missing_s3.append(label)
                    elif status == "LOCAL_MISSING":
                        local_missing.append(label)
                    elif status == "TIMEOUT":
                        timed_out.append(label)
                    elif status == "AWS_UNREACHABLE":
                        aws_unreach.append(label)
                    elif status == "ETAG_NOT_COMPARABLE":
                        uncomparable.append(label)
    elif pipeline in ("inf-gold",):
        # INF gold: check against opal-data-inf/code/gold/
        inf_dag = _build_dag("inf-gold")
        inf_candidates = sorted(inf_dag.scripts.items(), key=lambda x: x[1].run_order)
        skip_gold = False
        if script_filter_upper:
            any_inf_match = any(script_filter_upper in sid.upper() for sid, _ in inf_candidates)
            if not any_inf_match:
                skip_gold = True
        for sid, sio in inf_candidates:
            if script_filter_upper and script_filter_upper not in sid.upper():
                continue
            local_path = _WORKSPACE / sio.file_path
            label = f"[inf-gold] {sid}"
            checked_any = True
            status, extras = _check_one("inf-gold", label, local_path, f"{S3_GOLD_PREFIX}{sio.filename}")
            print(f"  [inf-gold] {sid:<10} {status:<14} {sio.filename}")
            for line in extras:
                print(f"             {line}")
            if status == "MATCH":
                matched.append(label)
            elif status == "STALE":
                stale.append(label)
            elif status == "MISSING_ON_S3":
                missing_s3.append(label)
            elif status == "LOCAL_MISSING":
                local_missing.append(label)
            elif status == "TIMEOUT":
                timed_out.append(label)
            elif status == "AWS_UNREACHABLE":
                aws_unreach.append(label)
            elif status == "ETAG_NOT_COMPARABLE":
                uncomparable.append(label)
    elif pipeline in ("cot-gold", "cot"):
        # cot (Cottonwood): no comp-graph DAG -> direct directory glob (MDPF pattern),
        # standard code/<layer>/ layout against opal-data-cot. gold here; silver by
        # the SILVER section below; bronze by the generic BRONZE section (TOOL-03 --
        # was a cot-branch special case, now uniform across firms).
        skip_gold = False
        _cot_root = _WORKSPACE / "data" / "cot" / "scripts"
        for _layer in ("gold",):
            _ldir = _cot_root / _layer
            if not _ldir.is_dir():
                continue
            for p in sorted(_ldir.glob("*.py")):
                if p.name.startswith("__"):
                    continue
                if script_filter_lower and script_filter_lower not in p.stem.lower():
                    continue
                label = f"[cot:{_layer}] {p.name}"
                checked_any = True
                status, extras = _check_one("cot", label, p, f"code/{_layer}/{p.name}")
                print(f"  [cot:{_layer}] {p.name:<44} {status:<14}")
                for line in extras:
                    print(f"             {line}")
                if status == "MATCH":
                    matched.append(label)
                elif status == "STALE":
                    stale.append(label)
                elif status == "MISSING_ON_S3":
                    missing_s3.append(label)
                elif status == "LOCAL_MISSING":
                    local_missing.append(label)
                elif status == "TIMEOUT":
                    timed_out.append(label)
                elif status == "AWS_UNREACHABLE":
                    aws_unreach.append(label)
                elif status == "ETAG_NOT_COMPARABLE":
                    uncomparable.append(label)
    elif pipeline not in ("bd-silver", "inf-silver", "cot-silver",
                          "bd-bronze", "inf-bronze", "cot-bronze"):
        dag = _build_dag("bd-gold")
        gold_candidates = sorted(dag.scripts.items(), key=lambda x: x[1].run_order)
        skip_gold = False
        if script_filter_upper:
            any_gold_match = any(script_filter_upper in sid.upper() for sid, _ in gold_candidates)
            if not any_gold_match:
                skip_gold = True

        if not skip_gold:
            for sid, sio in gold_candidates:
                if script_filter_upper and script_filter_upper not in sid.upper():
                    continue
                local_path = _WORKSPACE / sio.file_path
                label = f"[bd-gold] {sid}"
                checked_any = True
                status, extras = _check_one("bd-gold", label, local_path, f"{S3_GOLD_PREFIX}{sio.filename}")
                print(f"  [bd-gold] {sid:<8} {status:<14} {sio.filename}")
                for line in extras:
                    print(f"           {line}")
                if status == "MATCH":
                    matched.append(label)
                elif status == "STALE":
                    stale.append(label)
                elif status == "MISSING_ON_S3":
                    missing_s3.append(label)
                elif status == "LOCAL_MISSING":
                    local_missing.append(label)
                elif status == "TIMEOUT":
                    timed_out.append(label)
                elif status == "AWS_UNREACHABLE":
                    aws_unreach.append(label)
                elif status == "ETAG_NOT_COMPARABLE":
                    uncomparable.append(label)

    # ---- SILVER layer (directory-walk-driven) ----
    # MDPF handles all its layers (gold/backfill/feeders/bronze) in the gold-section
    # branch above; it has no separate silver dir, and SILVER_LOCAL_DIR would wrongly
    # point at BD silver for the mdpf pipeline -- so skip the silver section for mdpf.
    silver_files = []
    if (pipeline != "mdpf" and not pipeline.endswith("-bronze")
            and SILVER_LOCAL_DIR.is_dir()):
        for p in sorted(SILVER_LOCAL_DIR.glob("*.py")):
            if p.name.startswith("__"):
                continue
            silver_files.append(p)

    skip_silver = False
    if silver_filter_stem:
        any_silver_match = any(silver_filter_stem in p.stem.lower() for p in silver_files)
        # Silver filter only: if no silver match AND the filter clearly isn't a silver-shaped name,
        # leave skip_silver False so user sees "no matches" cleanly. But if gold matched and
        # silver has no match, suppress silver section entirely to avoid noise.
        if not any_silver_match and not skip_gold:
            skip_silver = True

    if not skip_silver and silver_files:
        for p in silver_files:
            if silver_filter_stem and silver_filter_stem not in p.stem.lower():
                continue
            label = f"[SILVER] {p.name}"
            checked_any = True
            status, extras = _check_one("SILVER", label, p, f"{S3_SILVER_PREFIX}{p.name}")
            print(f"  [SILVER] {p.name:<48} {status:<14}")
            for line in extras:
                print(f"           {line}")
            if status == "MATCH":
                matched.append(label)
            elif status == "STALE":
                stale.append(label)
            elif status == "MISSING_ON_S3":
                missing_s3.append(label)
            elif status == "LOCAL_MISSING":
                local_missing.append(label)
            elif status == "TIMEOUT":
                timed_out.append(label)
            elif status == "AWS_UNREACHABLE":
                aws_unreach.append(label)
            elif status == "ETAG_NOT_COMPARABLE":
                uncomparable.append(label)

    # ---- BRONZE layer (NFRA_DEBTSCAN.TOOL-03; directory-walk like silver) ----
    # First-class deploy layer: data/<dir>/scripts/bronze/*.py -> code/bronze/.
    # Closes the Rule-13 bronze-verifiability gap (2026-06-12 inf-ADVI incident:
    # the inf bronze orchestrator could only be verified by hand-diff).
    _BRONZE_ELIGIBLE = {
        "bd-gold", "bd", "bd-bronze",
        "inf-gold", "inf", "inf-bronze",
        "cot-gold", "cot", "cot-bronze",
    }
    _LABEL_TO_DATADIR = {label: dirname
                         for dirname, (_b, label) in _DEPLOY_PIPELINE_MAP.items()}
    _firm_label = pipeline.split("-")[0] if pipeline in _BRONZE_ELIGIBLE else None

    if _firm_label:
        _bronze_dir = _WORKSPACE / "data" / _LABEL_TO_DATADIR[_firm_label] / "scripts" / "bronze"
        if _bronze_dir.is_dir():
            for p in sorted(_bronze_dir.glob("*.py")):
                if p.name.startswith("__"):
                    continue
                if silver_filter_stem and silver_filter_stem not in p.stem.lower():
                    continue
                label = f"[BRONZE] {p.name}"
                checked_any = True
                status, extras = _check_one("BRONZE", label, p, f"code/bronze/{p.name}")
                print(f"  [BRONZE] {p.name:<48} {status:<14}")
                for line in extras:
                    print(f"           {line}")
                if status == "MATCH":
                    matched.append(label)
                elif status == "STALE":
                    stale.append(label)
                elif status == "MISSING_ON_S3":
                    missing_s3.append(label)
                elif status == "LOCAL_MISSING":
                    local_missing.append(label)
                elif status == "TIMEOUT":
                    timed_out.append(label)
                elif status == "AWS_UNREACHABLE":
                    aws_unreach.append(label)
                elif status == "ETAG_NOT_COMPARABLE":
                    uncomparable.append(label)

    # ---- AUXILIARY prefixes (NFRA_DEBTSCAN.TOOL-03; CHECK-ONLY, mdpf pattern) ----
    # S3-driven: enumerate what is actually AT the aux prefix and compare each
    # object against its same-basename repo counterpart in the mapped repo-home.
    # No repo counterpart / no mapped home -> explicit UNCOVERED (never silent).
    # Layer-scoped *-bronze keys check ONLY bronze-homed aux prefixes (e.g. inf
    # bronze-runner -- the 2026-06-12 dual-prefix) so an unrelated aux staleness
    # cannot fail a bronze deploy's safe-deploy verify phase.
    if _firm_label:
        _aux_table = _AUX_CHECK_ONLY_PREFIXES.get(_firm_label, {})
        _bronze_only_view = pipeline.endswith("-bronze")
        for _aux_prefix, _aux_home in sorted(_aux_table.items()):
            if _bronze_only_view and _aux_home != f"data/{_LABEL_TO_DATADIR[_firm_label]}/scripts/bronze":
                continue
            if _aux_home is None:
                if not silver_filter_stem:
                    row = (f"[aux:{_aux_prefix}] s3://{S3_BUCKET}/code/{_aux_prefix}/ "
                           f"(no repo-home mapping)")
                    uncovered.append(row)
                    print(f"  [aux:{_aux_prefix}] {'(whole prefix)':<44} UNCOVERED      s3://{S3_BUCKET}/code/{_aux_prefix}/")
                continue
            try:
                _ls = _run_budgeted(
                    [aws_bin, "s3", "ls", f"s3://{S3_BUCKET}/code/{_aux_prefix}/"],
                    20, "aux_prefix_listing", capture_output=True, text=True, env=aws_env,
                )
            except subprocess.TimeoutExpired:
                timed_out.append(f"[aux:{_aux_prefix}] (listing)")
                print(f"  [aux:{_aux_prefix}] {'(listing)':<44} TIMEOUT")
                continue
            if _ls.returncode != 0:
                aws_unreach.append(f"[aux:{_aux_prefix}] (listing)")
                print(f"  [aux:{_aux_prefix}] {'(listing)':<44} AWS_UNREACHABLE")
                continue
            _home_dir = _WORKSPACE / _aux_home.replace("/", os.sep)
            for _ls_line in _ls.stdout.splitlines():
                _parts = _ls_line.split()
                if not _parts:
                    continue
                if _parts[0] == "PRE":
                    if not silver_filter_stem:
                        row = (f"[aux:{_aux_prefix}] s3://{S3_BUCKET}/code/{_aux_prefix}/{_parts[1]} "
                               f"(sub-prefix, not swept)")
                        uncovered.append(row)
                    continue
                if len(_parts) < 4:
                    continue
                _fname = _parts[3]
                if not (_fname.endswith(".py") or _fname.endswith(".sh")):
                    continue
                _stem = _fname.rsplit(".", 1)[0]
                if silver_filter_stem and silver_filter_stem not in _stem.lower():
                    continue
                _repo_file = _home_dir / _fname
                _row_label = f"[aux:{_aux_prefix}] {_fname}"
                if not _repo_file.exists():
                    uncovered.append(f"{_row_label} (no repo counterpart in {_aux_home})")
                    print(f"  [aux:{_aux_prefix}] {_fname:<44} UNCOVERED      no repo counterpart in {_aux_home}")
                    continue
                checked_any = True
                status, extras = _check_one("aux", _row_label, _repo_file,
                                            f"code/{_aux_prefix}/{_fname}")
                # CHECK-ONLY contract (TOOL-03): aux drift must be VISIBLE but must
                # not corrupt the deploy gate -- safe-deploy's verify phase greps
                # the literal token STALE, so full-tree views report aux drift as
                # DRIFT. Exception: in the layer-scoped *-bronze view the
                # bronze-homed aux (inf bronze-runner) IS the deploy gate -- the
                # runner syncs that prefix, so drift there is a live stranded
                # bronze deploy and reports real STALE (fails the bronze verify).
                if status == "STALE" and not _bronze_only_view:
                    status = "DRIFT"
                print(f"  [aux:{_aux_prefix}] {_fname:<44} {status:<14} CHECK-ONLY vs {_aux_home}")
                for line in extras:
                    print(f"           {line}")
                if status == "MATCH":
                    matched.append(_row_label)
                elif status == "STALE":
                    stale.append(_row_label)
                elif status == "DRIFT":
                    aux_drift.append(_row_label)
                elif status == "MISSING_ON_S3":
                    missing_s3.append(_row_label)
                elif status == "LOCAL_MISSING":
                    local_missing.append(_row_label)
                elif status == "TIMEOUT":
                    timed_out.append(_row_label)
                elif status == "AWS_UNREACHABLE":
                    aws_unreach.append(_row_label)
                elif status == "ETAG_NOT_COMPARABLE":
                    uncomparable.append(_row_label)

        # Unmapped-prefix enumeration (false-clean guard): any live code/ prefix
        # that is neither a standard deploy layer nor in the aux registry is
        # UNCOVERED -- a NEW prefix appearing on a firm bucket self-surfaces.
        # Skipped on filtered runs (focused view) and bronze-only views.
        if not silver_filter_stem and not _bronze_only_view:
            try:
                _ls_root = _run_budgeted(
                    [aws_bin, "s3", "ls", f"s3://{S3_BUCKET}/code/"],
                    20, "code_prefix_listing", capture_output=True, text=True, env=aws_env,
                )
                if _ls_root.returncode == 0:
                    for _ls_line in _ls_root.stdout.splitlines():
                        _parts = _ls_line.split()
                        if len(_parts) == 2 and _parts[0] == "PRE":
                            _pname = _parts[1].rstrip("/")
                            if (_pname not in _STANDARD_CODE_PREFIXES
                                    and _pname not in _aux_table):
                                row = (f"[aux:{_pname}] s3://{S3_BUCKET}/code/{_pname}/ "
                                       f"(prefix not in tool registry)")
                                uncovered.append(row)
                                print(f"  [aux:{_pname}] {'(whole prefix)':<44} UNCOVERED      not in tool registry")
            except subprocess.TimeoutExpired:
                timed_out.append("[aux] (code/ prefix enumeration)")

    # ---- S3-SIDE ENUMERATION (instrument-fix @c9be07b413 gaps 1+4) ----
    # The standard-layer passes above enumerate REPO->S3 (DAG or dir-glob), so an S3
    # object with no repo/DAG membership -- including the EXTRA homes of a MULTI-HOMED
    # script (DS's live specimen: one script at code/gold/ + code/manual_api/, rendered
    # as ONE aux row) -- was structurally invisible. This section lists each standard
    # prefix S3-SIDE (same `s3 ls` instrument the aux section already uses), prints the
    # DENOMINATOR (objects at S3 vs checked this run), renders every never-probed object
    # as S3-ONLY (informational -- NEVER the deploy-gate STALE token), and names every
    # basename living at 2+ prefixes. Aux prefixes join the multi-home/basename map but
    # emit no S3-ONLY rows (the aux section already emits UNCOVERED for those).
    s3_only = []
    multi_home = {}
    if pipeline == "mdpf":
        _enum_prefixes = (
            {} if _CODE_TREES is None
            else {_l: _p for _l, (_rh, _p) in _CODE_TREES["mdpf"]["layers"].items()}
        )
        _aux_enum_names = set()
    elif pipeline == "advi":
        _enum_prefixes = (
            {} if _CODE_TREES is None
            else {_l: _p for _l, (_rh, _p) in _CODE_TREES["advi"]["layers"].items()}
        )
        _aux_enum_names = set()
    elif _firm_label:
        _enum_prefixes = {p: f"code/{p}/" for p in sorted(_STANDARD_CODE_PREFIXES)}
        _aux_enum_names = set()
        for _ap in _AUX_CHECK_ONLY_PREFIXES.get(_firm_label, {}):
            _enum_prefixes[_ap] = f"code/{_ap}/"
            _aux_enum_names.add(_ap)
    else:
        _enum_prefixes = {}
        _aux_enum_names = set()
    _basename_homes = {}
    for _ename, _eprefix in sorted(_enum_prefixes.items()):
        try:
            _els = _run_budgeted(
                [aws_bin, "s3", "ls", f"s3://{S3_BUCKET}/{_eprefix}"],
                20, "s3_prefix_enumeration", capture_output=True, text=True, env=aws_env,
            )
        except subprocess.TimeoutExpired:
            timed_out.append(f"[s3-enum:{_ename}] (listing)")
            print(f"  [s3-enum:{_ename}] {'(listing)':<44} TIMEOUT")
            continue
        if _els.returncode != 0:
            aws_unreach.append(f"[s3-enum:{_ename}] (listing)")
            print(f"  [s3-enum:{_ename}] {'(listing)':<44} AWS_UNREACHABLE")
            continue
        _objs = []
        for _eline in _els.stdout.splitlines():
            _ep = _eline.split()
            if len(_ep) >= 4 and (_ep[3].endswith(".py") or _ep[3].endswith(".sh")):
                _objs.append(_ep[3])
        _total_at_prefix = len(_objs)
        if script_filter_lower:
            # PSCRIPT2: a canonicalized filter can carry a repo SUBPATH (runners_49f/x) that no
            # S3 basename contains -- the old stem-only test then printed 'matched 0 of N' beside
            # a MATCHed verdict row (a false-0 in the denominator's own frame). Match the
            # filter's BASENAME as well; the full-string test keeps its precision when given.
            _fstem = script_filter_lower.rsplit("/", 1)[-1]
            _objs = [o for o in _objs
                     if script_filter_lower in o.rsplit(".", 1)[0].lower()
                     or _fstem in o.rsplit(".", 1)[0].lower()]
        for _o in _objs:
            _basename_homes.setdefault(_o, set()).add(_ename)
        _unrendered = [o for o in _objs if f"{_eprefix}{o}" not in _checked_s3_keys]
        _denom_filter = (
            f" (filter {script_filter_lower!r} matched {len(_objs)} of {_total_at_prefix})"
            if script_filter_lower else ""
        )
        print(f"  DENOMINATOR [{_ename}]: s3://{S3_BUCKET}/{_eprefix} = "
              f"{len(_objs)} object(s), {len(_objs) - len(_unrendered)} checked this run, "
              f"{len(_unrendered)} unrendered{_denom_filter}")
        if _ename in _aux_enum_names:
            continue  # aux S3-side gaps already surfaced as UNCOVERED by the aux section
        for _o in _unrendered:
            s3_only.append(f"[s3-only:{_ename}] {_o}")
            print(f"  [s3-only:{_ename}] {_o:<44} {'S3-ONLY':<14} "
                  "at S3, never probed by the repo/DAG pass -- outside this tool's universe")
    for _bn, _homes in sorted(_basename_homes.items()):
        if len(_homes) >= 2:
            multi_home[_bn] = sorted(_homes)
            print(f"  MULTI-HOME: {_bn} deployed at {len(_homes)} prefixes: "
                  f"{'+'.join(sorted(_homes))} -- each home is a separate deploy target; "
                  "a single-row read undercounts it")

    # ---- DECLARED BOUNDARIES (@c9be07b413 items 2+3: honest limits, distinct from gaps) ----
    declared_unswept = []
    if pipeline == "mdpf":
        declared_unswept.append(
            "bundle channel s3://opal-data-assets/portal/gold/mdpf/_code/ (X-iii delivery) "
            "-- acceptance rides the mint's sha-verify, not this ETag sweep")
    if _enum_prefixes:
        declared_unswept.append(
            "lambda-zip code channel (deployed lambda bundles) -- covered by the "
            "deployed-AST graph leg, not this ETag sweep")
    for _db in declared_unswept:
        print(f"  DECLARED-UNSWEPT: {_db}")

    print()
    print(f"  Summary: {len(matched)} MATCH, {len(stale)} STALE, "
          f"{len(missing_s3)} MISSING_ON_S3, {len(local_missing)} LOCAL_MISSING, "
          f"{len(timed_out)} TIMEOUT, {len(aws_unreach)} AWS_UNREACHABLE, "
          f"{len(uncomparable)} ETAG_NOT_COMPARABLE, "
          f"{len(uncovered)} UNCOVERED, {len(aux_drift)} AUX-DRIFT, "
          f"{len(not_in_tree)} NOT-A-MEMBER(no-verdict), {len(s3_only)} S3-ONLY, "
          f"{len(multi_home)} MULTI-HOME, {len(declared_unswept)} DECLARED-UNSWEPT")
    print("  " + _compbudget.within_budget_line(
        budget_state["units"], budget_state["units"], "timeout_bearing_operation", budget_s, budget_source,
        round(budget_clock.elapsed(), 2)))
    for line in _compbudget.deferred_bucket(0, budget_state["units"], "timeout_bearing_operation", []):
        print("  " + line)
    # NOTHING-VERIFIED guard (CVO~B 2026-08-05): rows were seen but not one of them was
    # actually verified against S3. The common cause is a script OUTSIDE this tool's
    # universe -- the path auto-detected into a tree it does not belong to, every file
    # read as a shared-home non-member, and the old Summary reported that as all zeros.
    # DELIBERATELY NARROW: fires only when the verified-outcome counters are ALL empty,
    # so a real sweep carrying legitimate not-in-tree rows beside genuine MATCHes is
    # untouched, and the deploy-gate tokens keep their exact meaning.
    _verified_any = bool(matched or stale or missing_s3 or local_missing)
    _nothing_verified = bool(not_in_tree) and not _verified_any
    if _nothing_verified:
        print()
        print(f"  NOTHING VERIFIED: {len(not_in_tree)} row(s) resolved to a SHARED repo home as "
              "non-members, and 0 script(s) were checked against S3.")
        print("  This is NOT a clean result -- it is the tool reporting that it could not place "
              "what you gave it.")
        print("  Most likely: the script lives outside this tool's pipeline universe "
              "(see `--pipeline` choices); a data/<tree>/scripts/... path auto-detects, and the "
              "auto-detected tree may not be the script's real one.")
    if uncovered:
        print(f"  UNCOVERED ({len(uncovered)}) -- the tool CANNOT verify these; not clean, not dirty, UNVERIFIED:")
        for u in uncovered:
            print(f"    {u}")
        print("  Do not count tool-blindness as cleanliness (TOOL-02/03 false-clean guard).")
    if aux_drift:
        print(f"  AUX-DRIFT ({len(aux_drift)}) -- CHECK-ONLY prefix differs from its repo home (informational; not the deploy gate):")
        for d in aux_drift:
            print(f"    {d}")
        print("  Investigate whether the aux prefix or the repo copy is the stale side before syncing.")
    if aws_unreach:
        print(f"  AWS_UNREACHABLE: {', '.join(aws_unreach)}")
    if uncomparable:
        print(f"  ETAG_NOT_COMPARABLE: {', '.join(uncomparable)}")
        print("  AWS credentials/network could not reach S3; MATCH/MISSING is NOT verified.")
        print("  Fix: check AWS_PROFILE / credentials / VPN, then re-run. See `aws sts get-caller-identity` to confirm.")
    if stale:
        print(f"  STALE: {', '.join(stale)}")
        print("  Run build-and-upload.sh (gold) or the silver upload pathway to sync.")
    elif timed_out:
        print(f"  TIMEOUT: {', '.join(timed_out)}")
        print("  AWS CLI resolution works, but head-object did not return before timeout.")
        print("  Check caller credentials/network, or rerun with AWS_EC2_METADATA_DISABLED=true in the invoking shell.")
    elif not stale and not missing_s3 and (matched or local_missing):
        if uncovered or aux_drift:
            print("  All deploy-gate scripts are up-to-date on S3 "
                  "(UNCOVERED = unverified / AUX-DRIFT = check-only divergence -- see above).")
        else:
            print("  All checked scripts are up-to-date on S3.")
    elif not checked_any and not uncovered:
        # PSCRIPT2 P2 -- THE ABSENCE LAW: an ABSENT verdict names its searched tree and the
        # trees it did NOT search. A bare "no match" over one tree reads as estate-wide
        # absence to every downstream consumer -- the clean false-ABSENT that dispatched
        # this fix (a 404 in the wrong bucket is the wrong question asked cleanly).
        _unsearched = sorted({_pk for _pk, _b in _ALL_DEPLOYED_TREES} - {pipeline})
        print(f"  No scripts matched filter: {raw_filter!r} -- ABSENT IN TREE [{pipeline}] ONLY; "
              f"trees NOT searched this run: {', '.join(_unsearched) or '(none)'}")
    if _nothing_verified:
        return 2  # UNVERIFIED -- consistent with this tool's existing rc=2 "cannot answer"
    return 0


def _resolve_gold_script(script_id: str) -> 'tuple[Path | None, str]':
    """Find a gold script file by ID prefix.

    Checks data/inf/scripts/gold/ first, then data/black_diamond/scripts/gold/.
    Returns (path, normalized_stem) or (None, '').
    """
    gold_dirs = [
        _WORKSPACE / 'data' / 'inf' / 'scripts' / 'gold',
        _WORKSPACE / 'data' / 'black_diamond' / 'scripts' / 'gold',
    ]
    for gd in gold_dirs:
        if not gd.exists():
            continue
        for p in sorted(gd.glob('*.py')):
            if p.stem == script_id:
                return p, p.stem
        prefix_matches = sorted(p for p in gd.glob(f'{script_id}*.py') if not p.name.startswith('__'))
        if prefix_matches:
            return prefix_matches[0], prefix_matches[0].stem
    return None, ''


def _extract_merge_sites(func_node: 'ast.FunctionDef', source: str) -> 'list[dict]':
    """Extract merge() call sites from a function AST node.

    Returns list of dicts: {line, result_var, left_expr, right_expr, on_cols, how, func_name}
    """
    import ast as _ast

    sites: list[dict] = []

    def _visit(node: '_ast.AST') -> None:
        if isinstance(node, (_ast.Assign,)):
            val = node.value
            if (isinstance(val, _ast.Call)
                    and isinstance(val.func, _ast.Attribute)
                    and val.func.attr == 'merge'):
                result_var = None
                if len(node.targets) == 1 and isinstance(node.targets[0], _ast.Name):
                    result_var = node.targets[0].id
                left_expr = _ast.unparse(val.func.value)
                right_expr = _ast.unparse(val.args[0]) if val.args else '?'
                on_cols: list[str] = []
                how = 'inner'
                for kw in val.keywords:
                    if kw.arg == 'on':
                        if isinstance(kw.value, _ast.Constant):
                            on_cols = [kw.value.value]
                        elif isinstance(kw.value, _ast.List):
                            on_cols = [e.value for e in kw.value.elts
                                       if isinstance(e, _ast.Constant) and isinstance(e.value, str)]
                    elif kw.arg == 'how' and isinstance(kw.value, _ast.Constant):
                        how = kw.value.value
                sites.append({
                    'line': val.lineno,
                    'result_var': result_var or '?',
                    'left_expr': left_expr,
                    'right_expr': right_expr,
                    'on_cols': on_cols,
                    'how': how,
                    'func_name': func_node.name,
                })
        for child in _ast.iter_child_nodes(node):
            _visit(child)

    for stmt in func_node.body:
        _visit(stmt)
    return sites


def _extract_col_accesses(func_node: 'ast.FunctionDef', target_var: str) -> 'list[dict]':
    """Find column accesses on target_var within a function body.

    Returns list of {line, pattern, columns}.
    """
    import ast as _ast

    accesses: list[dict] = []

    def _check(node: '_ast.AST') -> None:
        if (isinstance(node, _ast.Subscript)
                and isinstance(node.value, _ast.Name)
                and node.value.id == target_var):
            sl = node.slice
            if isinstance(sl, _ast.Constant) and isinstance(sl.value, str):
                accesses.append({'line': node.lineno, 'pattern': 'subscript', 'columns': [sl.value]})
            elif isinstance(sl, _ast.List):
                cols = [e.value for e in sl.elts if isinstance(e, _ast.Constant) and isinstance(e.value, str)]
                if cols:
                    accesses.append({'line': node.lineno, 'pattern': 'subscript_multi', 'columns': cols})

        if (isinstance(node, _ast.Call)
                and isinstance(node.func, _ast.Attribute)
                and isinstance(node.func.value, _ast.Name)
                and node.func.value.id == target_var):
            method = node.func.attr
            if method == 'dropna':
                for kw in node.keywords:
                    if kw.arg == 'subset' and isinstance(kw.value, _ast.List):
                        cols = [e.value for e in kw.value.elts
                                if isinstance(e, _ast.Constant) and isinstance(e.value, str)]
                        accesses.append({'line': node.lineno, 'pattern': 'dropna_subset', 'columns': cols})
            elif method in ('sort_values', 'drop_duplicates'):
                for kw in node.keywords:
                    if kw.arg in ('by', 'subset'):
                        if isinstance(kw.value, _ast.Constant):
                            accesses.append({'line': node.lineno, 'pattern': method, 'columns': [kw.value.value]})
                        elif isinstance(kw.value, _ast.List):
                            cols = [e.value for e in kw.value.elts
                                    if isinstance(e, _ast.Constant) and isinstance(e.value, str)]
                            accesses.append({'line': node.lineno, 'pattern': method, 'columns': cols})
            elif method == 'groupby':
                if node.args:
                    arg = node.args[0]
                    if isinstance(arg, _ast.Constant):
                        accesses.append({'line': node.lineno, 'pattern': 'groupby', 'columns': [arg.value]})
                    elif isinstance(arg, _ast.List):
                        cols = [e.value for e in arg.elts
                                if isinstance(e, _ast.Constant) and isinstance(e.value, str)]
                        accesses.append({'line': node.lineno, 'pattern': 'groupby', 'columns': cols})

    for node in _ast.walk(func_node):
        _check(node)
    return accesses


def cmd_postmerge_cols(args: 'argparse.Namespace') -> None:
    """postmerge-cols subcommand: flag suffix-collision risks at merge() call sites.

    For each pd.DataFrame.merge() call in the script, reports the post-merge
    column access sites and flags any accessed column that is NOT in the on=
    join key list (potential _x/_y suffix-collision or KeyError risk).

    Writes per-script manifest to org/modules/graph/postmerge-cols/{script_id}.yaml.
    --strict exits 1 on any flagged access.
    """
    import ast as _ast
    import yaml as _yaml

    script_id = args.postmerge_script_id
    strict = getattr(args, 'strict', False)

    script_path, normalized_id = _resolve_gold_script(script_id)
    if script_path is None:
        print(f'ERROR: gold script not found for {script_id!r}', file=sys.stderr)
        print('  Checked: data/inf/scripts/gold/ + data/black_diamond/scripts/gold/', file=sys.stderr)
        sys.exit(1)

    rel_path = script_path.relative_to(_WORKSPACE).as_posix()

    try:
        source = script_path.read_text(encoding='utf-8')
        tree = _ast.parse(source, filename=str(script_path))
    except SyntaxError as e:
        print(f'ERROR: syntax error in {rel_path}: {e}', file=sys.stderr)
        sys.exit(1)

    print(f'COMP-PIPESCRIPT postmerge-cols: {normalized_id}')
    print(f'  Script: {rel_path}')
    print()

    func_nodes = [n for n in _ast.walk(tree)
                  if isinstance(n, (_ast.FunctionDef, _ast.AsyncFunctionDef))]

    all_sites: list[dict] = []
    for fn in func_nodes:
        for site in _extract_merge_sites(fn, source):
            accesses = _extract_col_accesses(fn, site['result_var'])
            flagged: list[dict] = []
            for acc in accesses:
                for col in acc['columns']:
                    if col not in site['on_cols'] and not col.endswith('_x') and not col.endswith('_y'):
                        flagged.append({'col': col, 'line': acc['line'], 'pattern': acc['pattern']})
            site['flagged_cols'] = flagged
            site['downstream_accesses'] = accesses
            all_sites.append(site)

    flag_count = 0
    for site in all_sites:
        on_str = ', '.join(repr(c) for c in site['on_cols']) if site['on_cols'] else '(none)'
        status = 'WARN' if site['flagged_cols'] else 'OK  '
        print(f'  {status}  line {site["line"]:4d}  {site["func_name"]}()')
        print(f'         {site["left_expr"]}.merge({site["right_expr"]}, on=[{on_str}], how={site["how"]!r})')
        print(f'         result_var: {site["result_var"]}')
        for fc in site['flagged_cols']:
            print(f'         WARN: col {fc["col"]!r} accessed at line {fc["line"]} ({fc["pattern"]})'
                  f' — NOT in on=[{on_str}]; may become {fc["col"]!r}_x/{fc["col"]!r}_y after merge')
            flag_count += 1
        if not site['flagged_cols']:
            print('         No unguarded post-merge column accesses detected')
        print()

    output_dir = _WORKSPACE / 'org' / 'modules' / 'graph' / 'postmerge-cols'
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        'script_id': normalized_id,
        'path': rel_path,
        'merge_sites': [
            {
                'line': s['line'],
                'func_name': s['func_name'],
                'result_var': s['result_var'],
                'left_expr': s['left_expr'],
                'right_expr': s['right_expr'],
                'on_cols': s['on_cols'],
                'how': s['how'],
                'flagged_cols': s['flagged_cols'],
            }
            for s in all_sites
        ],
    }
    yaml_path = output_dir / f'{normalized_id}.yaml'
    with open(yaml_path, 'w', encoding='utf-8') as f:
        _yaml.dump(manifest, f, default_flow_style=False, sort_keys=False)

    print(f'  Summary: {len(all_sites)} merge site(s) | {flag_count} flag(s)')
    print(f'  Manifest: {yaml_path.relative_to(_WORKSPACE)}')
    print()

    if strict and flag_count > 0:
        print(f'FAIL: --strict: {flag_count} post-merge column access risk(s) detected (exit 1)')
        sys.exit(1)

    print('PASS: postmerge-cols analysis complete')


def _extract_lock_in_chain(func_node: 'ast.FunctionDef') -> 'list[dict]':
    """Extract the post-condition lock-in chain from a function body.

    A lock-in chain link is any operation that requires a column/type precondition
    that a prior op in the same function could invalidate:
      - dropna(subset=[...])  — requires column existence
      - astype(...)           — requires dtype compatibility
      - merge(on=[...])       — requires column existence on both sides
      - fillna(...)           — column must exist
      - sort_values(by=[...]) — column must exist

    Returns list of chain links sorted by line number.
    """
    import ast as _ast

    chain: list[dict] = []

    def _visit(node: '_ast.AST') -> None:
        if not isinstance(node, _ast.Call):
            for child in _ast.iter_child_nodes(node):
                _visit(child)
            return

        func = node.func
        if not isinstance(func, _ast.Attribute):
            for child in _ast.iter_child_nodes(node):
                _visit(child)
            return

        method = func.attr
        receiver = _ast.unparse(func.value)

        if method == 'dropna':
            for kw in node.keywords:
                if kw.arg == 'subset' and isinstance(kw.value, _ast.List):
                    cols = [e.value for e in kw.value.elts
                            if isinstance(e, _ast.Constant) and isinstance(e.value, str)]
                    chain.append({
                        'line': node.lineno,
                        'op': 'dropna_subset',
                        'receiver': receiver,
                        'columns': cols,
                        'assumption': f'Columns {cols} must exist in {receiver}',
                    })

        elif method == 'astype':
            if node.args:
                arg = node.args[0]
                dtype_str = _ast.unparse(arg)
                chain.append({
                    'line': node.lineno,
                    'op': 'astype',
                    'receiver': receiver,
                    'dtype': dtype_str,
                    'assumption': f'{receiver} must be castable to {dtype_str}',
                })

        elif method == 'merge':
            on_cols: list[str] = []
            how = 'inner'
            for kw in node.keywords:
                if kw.arg == 'on':
                    if isinstance(kw.value, _ast.Constant):
                        on_cols = [kw.value.value]
                    elif isinstance(kw.value, _ast.List):
                        on_cols = [e.value for e in kw.value.elts
                                   if isinstance(e, _ast.Constant) and isinstance(e.value, str)]
                elif kw.arg == 'how' and isinstance(kw.value, _ast.Constant):
                    how = kw.value.value
            right = _ast.unparse(node.args[0]) if node.args else '?'
            chain.append({
                'line': node.lineno,
                'op': 'merge',
                'receiver': receiver,
                'right': right,
                'on_cols': on_cols,
                'how': how,
                'assumption': f'Columns {on_cols} must exist on both {receiver} and {right}; non-join shared cols will get _x/_y suffix',
            })

        elif method in ('sort_values', 'drop_duplicates', 'groupby'):
            cols: list[str] = []
            for kw in node.keywords:
                if kw.arg in ('by', 'subset'):
                    if isinstance(kw.value, _ast.Constant):
                        cols = [kw.value.value]
                    elif isinstance(kw.value, _ast.List):
                        cols = [e.value for e in kw.value.elts
                                if isinstance(e, _ast.Constant) and isinstance(e.value, str)]
            if node.args:
                arg = node.args[0]
                if isinstance(arg, _ast.Constant):
                    cols = [arg.value]
                elif isinstance(arg, _ast.List):
                    cols = [e.value for e in arg.elts
                            if isinstance(e, _ast.Constant) and isinstance(e.value, str)]
            if cols:
                chain.append({
                    'line': node.lineno,
                    'op': method,
                    'receiver': receiver,
                    'columns': cols,
                    'assumption': f'Columns {cols} must exist in {receiver}',
                })

        for child in _ast.iter_child_nodes(node):
            _visit(child)

    for stmt in func_node.body:
        _visit(stmt)

    return sorted(chain, key=lambda x: x['line'])


def cmd_shadow_detect(args: 'argparse.Namespace') -> None:
    """shadow-detect subcommand: enumerate the post-condition lock-in chain for a function.

    Static mode: walks the named function body and enumerates all assertion-class
    operations (dropna, astype, merge, sort_values, groupby) that form the lock-in
    chain. Each link assumes a precondition that prior ops may invalidate — a cascade
    of sequential fixes (bug-shadows pattern) surfaces as multiple chain links each
    touched by a different commit.

    --recent-failures <Nd>: cross-references git log (--since=<N>d) for commits
    that touched the named function (via git log -S pickaxe); flags cascade pattern
    when 3+ commits each touch distinct chain links.

    Writes manifest to org/modules/graph/shadow-detect/{script_stem}.{func}.yaml.
    """
    import ast as _ast
    import subprocess
    import yaml as _yaml

    func_name = args.shadow_function
    recent_failures = getattr(args, 'recent_failures', None)

    gold_dirs = [
        _WORKSPACE / 'data' / 'inf' / 'scripts' / 'gold',
        _WORKSPACE / 'data' / 'black_diamond' / 'scripts' / 'gold',
    ]

    # Search all gold scripts for the named function
    found_fn: '_ast.FunctionDef | None' = None
    found_path: 'Path | None' = None
    found_stem: str = ''

    for gd in gold_dirs:
        if not gd.exists():
            continue
        for script_path in sorted(gd.glob('*.py')):
            try:
                source = script_path.read_text(encoding='utf-8')
                tree = _ast.parse(source, filename=str(script_path))
            except SyntaxError:
                continue
            for node in _ast.walk(tree):
                if (isinstance(node, (_ast.FunctionDef, _ast.AsyncFunctionDef))
                        and node.name == func_name):
                    found_fn = node
                    found_path = script_path
                    found_stem = script_path.stem
                    break
            if found_fn is not None:
                break
        if found_fn is not None:
            break

    if found_fn is None:
        print(f'ERROR: function {func_name!r} not found in any gold script', file=sys.stderr)
        sys.exit(1)

    rel_path = found_path.relative_to(_WORKSPACE).as_posix()  # type: ignore[union-attr]

    print(f'COMP-PIPESCRIPT shadow-detect: {func_name}()')
    print(f'  Found in: {rel_path}  (lines {found_fn.lineno}-{found_fn.end_lineno})')
    print()

    chain = _extract_lock_in_chain(found_fn)

    print(f'  Lock-in chain ({len(chain)} link(s)):')
    for i, link in enumerate(chain, 1):
        cols = link.get('columns') or link.get('on_cols') or []
        op_str = link['op']
        if op_str == 'astype':
            detail = f"dtype={link.get('dtype', '?')}"
        elif cols:
            detail = f"cols={cols}"
        else:
            detail = ''
        print(f'  [{i:2d}] line {link["line"]:5d}  {op_str:20s}  {link["receiver"]}  {detail}')
        print(f'         assumption: {link["assumption"]}')
    print()

    # --recent-failures mode: git log -S <func_name> pickaxe
    cascade_commits: list[dict] = []
    if recent_failures:
        # Parse duration: "7d" -> since="7 days ago"
        duration_str = recent_failures.rstrip('dDhHmM')
        unit = recent_failures[len(duration_str):]
        unit_map = {'d': 'days', 'h': 'hours', 'm': 'minutes', 'D': 'days', 'H': 'hours', 'M': 'minutes'}
        since_str = f'{duration_str} {unit_map.get(unit, "days")} ago'

        print(f'  --recent-failures: git log -S {func_name!r} --since={since_str!r}')
        try:
            result = subprocess.run(
                ['git', 'log', '--all', '--oneline', f'--since={since_str}', '-S', func_name],
                capture_output=True, text=True, cwd=str(_WORKSPACE),
            )
            commits = [line.strip() for line in result.stdout.splitlines() if line.strip()]
            if commits:
                print(f'  Commits touching {func_name!r} (last {recent_failures}):')
                for i, commit_line in enumerate(commits, 1):
                    sha = commit_line[:9]
                    subject = commit_line[10:]
                    cascade_commits.append({'sha': sha, 'subject': subject, 'depth': i})
                    print(f'    [{i}] {sha}  {subject}')
                if len(commits) >= 3:
                    print(f'  CASCADE PATTERN DETECTED: {len(commits)} commits in {recent_failures} window'
                          f' touching {func_name!r} — bug-shadows cascade (fix #1 unmasks #2 unmasks #3)')
                elif len(commits) == 2:
                    print(f'  WATCH: 2 commits in {recent_failures} window — potential bug-shadows developing')
                else:
                    print('  OK: 1 commit; no cascade pattern')
            else:
                print(f'  No commits found touching {func_name!r} in last {recent_failures}')
        except Exception as e:
            print(f'  WARN: git log failed: {e}', file=sys.stderr)
        print()

    # Write manifest
    output_dir = _WORKSPACE / 'org' / 'modules' / 'graph' / 'shadow-detect'
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        'function': func_name,
        'script': found_stem,
        'path': rel_path,
        'func_lines': f'{found_fn.lineno}-{found_fn.end_lineno}',
        'lock_in_chain': chain,
        'cascade_commits': cascade_commits,
    }
    safe_func = func_name.lstrip('_')
    yaml_path = output_dir / f'{found_stem}.{safe_func}.yaml'
    with open(yaml_path, 'w', encoding='utf-8') as f:
        _yaml.dump(manifest, f, default_flow_style=False, sort_keys=False)

    print(f'  Manifest: {yaml_path.relative_to(_WORKSPACE)}')
    print()
    print('PASS: shadow-detect analysis complete')


# NFRA_DEBTSCAN.TOOL-02: per-tree postdeps config registry. Before this,
# cmd_postdeps hardcoded the bd yaml -- a cot/inf/mdpf query silently answered
# from bd's config (or printed bd's "no dependencies declared"), which a
# coverage grep miscounted as clean. None = the tree has NO deps config ->
# UNCOVERED, never silent-0-deps.
_POSTDEPS_CONFIGS: 'dict[str, str | None]' = {
    "bd": "data/black_diamond/scripts/gold/gold_pipeline_deps.yaml",
    "inf": "data/inf/scripts/gold/orion_pipeline_deps.yaml",
    "cot": "data/cot/scripts/gold/gold_pipeline_deps.yaml",
    "mdpf": None,
}


def cmd_postdeps(args):
    """Show and validate post-step dependencies and preconditions for gold scripts."""
    # NFRA_PIPESCRIPT P1b.1: LOUD OUT-OF-SCOPE (exit 2) for a non-medallion estate thread/
    # resource before the medallion config lookup -- closes the io/postdeps silent-Unknown class.
    _estate_oos_guard(getattr(args, 'script_name', ''))

    # TOOL-02 scope resolution: --firm beats path auto-detect beats bd default.
    firm = getattr(args, 'firm', None)
    _firm_source = "--firm" if firm else None
    if not firm:
        _np = (getattr(args, 'script_name', '') or '').replace('\\', '/')
        for _dir, _pk in _DATADIR_TO_PIPELINE.items():
            if f"data/{_dir}/scripts/" in _np or _np.startswith(f"data/{_dir}/"):
                firm = _pk.split('-')[0]
                _firm_source = "path auto-detect"
                break
    # Dial F1 half (b): the bd default SURVIVES but is NAMED LOUD below, never silent.
    # Required-flag (io-family precedent) was REJECTED on the live-caller inventory:
    # 3 dispatch-gate call sites (bd/cot/inf gold_dispatch check_partial_deps) invoke
    # postdeps flagless with rc+stderr swallowed and stdout-grep parsing -- a flagless
    # rc=2 would silently vacuate the WORKING bd $22M-class gate (empty stdout = zero
    # [BLOCKING] lines = vacuous pass). With the half-(a) unknown-id guard below,
    # flagless+unknown still refuses rc=2, so the F1 composition stays closed.
    _firm_defaulted = firm is None
    firm = firm or "bd"

    deps_rel = _POSTDEPS_CONFIGS.get(firm)
    if deps_rel is None:
        # FALSE-CLEAN GUARD: no config for this tree means postdeps coverage
        # DOES NOT EXIST here -- which is not the same as "no dependencies".
        print(f"PIPELINE DEPENDENCIES [{firm}]")
        print(f"  UNCOVERED: tree {firm!r} has no postdeps config registered -- "
              f"post-step dependencies are UNVERIFIED for this tree (not 0-deps).")
        print("  Do not count tool-blindness as cleanliness (TOOL-02 false-clean guard).")
        sys.exit(2)

    # Try PyYAML first; fall back to a minimal inline parser for our specific YAML shape
    deps_file = _WORKSPACE / Path(deps_rel)
    if not deps_file.exists():
        print(f"PIPELINE DEPENDENCIES [{firm}]")
        print(f"  UNCOVERED: registered config missing on disk: {deps_rel}")
        print("  Post-step dependencies are UNVERIFIED for this tree (not 0-deps).")
        sys.exit(2)

    raw = deps_file.read_text(encoding="utf-8")

    try:
        import yaml as _yaml
        deps = _yaml.safe_load(raw)
    except ImportError:
        # Minimal fallback parser: handles the specific structure in gold_pipeline_deps.yaml.
        # Supports top-level keys, script-name sub-keys, and flat key:value leaf pairs.
        # Not a general YAML parser -- only covers two-level dicts + lists of dicts.
        deps = _parse_deps_yaml_fallback(raw)

    if not isinstance(deps, dict):
        print(f"Failed to parse {deps_file.name}: unexpected structure.")
        sys.exit(1)

    post_steps = deps.get('post_steps') or {}
    preconditions = deps.get('preconditions') or {}

    # Canonicalize filter: strip path + .<name>.py suffix so filename forms match YAML keys
    if args.script_name:
        script_filter = _canonicalize_script_id(args.script_name).lower()
    else:
        script_filter = None

    # Provenance header (TOOL-02): name the tree + the exact config answering.
    print(f"PIPELINE DEPENDENCIES [{firm}]")
    print(f"  Config: {deps_rel}")
    if _firm_defaulted:
        print("  DEFAULT-TREE NOTICE: no --firm given and the script arg names no tree --")
        print("  answering from the DEFAULT tree 'bd'. If you meant inf/cot/mdpf, re-run")
        print("  with --firm <tree>.")
    print()

    has_output = False

    # Post-steps
    for script_name, steps in sorted(post_steps.items()):
        if script_filter and script_filter not in script_name.lower():
            continue
        if not isinstance(steps, list):
            continue
        print(f"  POST-STEPS for {script_name}:")
        for step in steps:
            blocking = "BLOCKING" if step.get('blocking', True) else "ADVISORY"
            print(f"    [{blocking}] Must run: {step['script']}")
            print(f"             Reason: {step['reason']}")
            if 'incident' in step:
                print(f"             Incident: {step['incident']}")
        print()
        has_output = True

    # Preconditions
    for script_name, conditions in sorted(preconditions.items()):
        if script_filter and script_filter not in script_name.lower():
            continue
        if not isinstance(conditions, list):
            continue
        print(f"  PRECONDITIONS for {script_name}:")
        for cond in conditions:
            blocking = "BLOCKING" if cond.get('blocking', True) else "WARN-ONLY"
            if 'artifact_s3' in cond:
                print(f"    [{blocking}] S3 artifact must exist: {cond['artifact_s3']}")
            elif 'condition' in cond:
                print(f"    [{blocking}] Condition: {cond['condition']}")
            print(f"             Reason: {cond['reason']}")
            if 'incident' in cond:
                print(f"             Incident: {cond['incident']}")
        print()
        has_output = True

    if not has_output:
        if script_filter:
            # Dial F1 half (a): discriminate UNKNOWN from KNOWN-with-no-deps. An unknown
            # script id must never read as clean on the $22M-class mode. The validation
            # universe is DERIVED AT RUNTIME from the same maps the tool resolves trees
            # from -- tree DAG script ids (_build_dag via _FIRM_TO_PIPELINE) UNION the
            # deps-config keys just parsed -- never a hand-copied roster
            # (memory/feedback_a_predicate_is_not_a_roster.md). A tree widening that
            # extends the DAG registry / _POSTDEPS_CONFIGS extends this guard with
            # zero edits here. Matching mirrors the filter loop above (substring on
            # lowered keys) so anything that COULD have matched a deps key is known.
            _deps_keys = {str(k).lower() for k in post_steps} | {str(k).lower() for k in preconditions}
            _tree_ids = set()
            _tree_note = ""
            try:
                _dag = _build_dag(_FIRM_TO_PIPELINE[firm])
                _tree_ids = {str(s).lower() for s in _dag.scripts}
            except Exception as _e:
                _tree_note = f"; tree ids UNDERIVABLE ({_e.__class__.__name__}) -- validated against deps keys only"
            _known = any(script_filter in k for k in _deps_keys) or \
                     any(script_filter in s for s in _tree_ids)
            if not _known:
                _n = len(_tree_ids | _deps_keys)
                _res = "DEFAULTED to bd" if _firm_defaulted else (_firm_source or "resolved")
                print(f"  REFUSED (rc=2): unknown script id {script_filter!r} -- not found in tree {firm!r}.")
                print(f"  (universe searched: {len(_tree_ids)} tree script ids + {len(_deps_keys)} declared"
                      f" deps keys = {_n} distinct{_tree_note}; tree resolution: {_res}.)")
                print("  A typo must never read as 'clear to run' on the $22M-class guard (dial F1).")
                print("  Re-run with a real script id, or name the tree: --firm bd|inf|cot|mdpf.")
                sys.exit(2)
            print(f"  No dependencies declared for: {script_filter}")
        else:
            print("  No dependencies declared.")


def _parse_deps_yaml_fallback(text: str) -> dict:
    """Minimal YAML parser for gold_pipeline_deps.yaml structure.
    Handles: top-level keys, script-name sub-keys, and lists of flat key:value dicts.
    Does NOT support anchors, multiline strings, or complex nesting beyond 3 levels.
    """
    result: dict = {}
    lines = text.splitlines()

    current_top: str | None = None        # e.g. 'post_steps'
    current_script: str | None = None     # e.g. 'build_canonical_prices_v2.py'
    current_list: list | None = None      # list being built under current_script
    current_item: dict | None = None      # dict being built for current list item

    def _flush_item():
        if current_list is not None and current_item:
            current_list.append(dict(current_item))

    def _unquote(s: str) -> str:
        s = s.strip()
        if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
            return s[1:-1]
        return s

    for raw_line in lines:
        stripped = raw_line.rstrip()
        if not stripped or stripped.lstrip().startswith('#'):
            continue

        indent = len(stripped) - len(stripped.lstrip())
        content = stripped.lstrip()

        # Remove inline comment (simple: find ' #' not inside quotes)
        if ' #' in content:
            # Only strip if the # is not inside a quoted string
            in_q = False
            q_char = None
            for ci, ch in enumerate(content):
                if ch in ('"', "'") and not in_q:
                    in_q = True
                    q_char = ch
                elif in_q and ch == q_char:
                    in_q = False
                elif ch == '#' and not in_q and ci > 0 and content[ci - 1] == ' ':
                    content = content[:ci].rstrip()
                    break

        # Top-level key (indent 0): post_steps: or preconditions:
        if indent == 0 and content.endswith(':') and ' ' not in content:
            _flush_item()
            current_item = None
            current_list = None
            current_script = None
            current_top = content[:-1]
            result[current_top] = {}
            continue

        # Script-name sub-key (indent 2): build_canonical_prices_v2.py:
        if indent == 2 and content.endswith(':') and current_top is not None:
            _flush_item()
            current_item = None
            current_script = content[:-1]
            current_list = []
            result[current_top][current_script] = current_list
            continue

        # List item marker (indent 4): - script: ...  or  - artifact_s3: ...
        if indent == 4 and content.startswith('- ') and current_list is not None:
            _flush_item()
            current_item = {}
            kv_part = content[2:].strip()
            if ':' in kv_part:
                k, _, v = kv_part.partition(':')
                v = v.strip()
                val: object = _unquote(v) if v else True
                if val == 'true':
                    val = True
                elif val == 'false':
                    val = False
                current_item[k.strip()] = val
            continue

        # Continuation key under list item (indent 6):   key: value
        if indent == 6 and ':' in content and current_item is not None:
            k, _, v = content.partition(':')
            v = v.strip()
            val = _unquote(v) if v else True
            if val == 'true':
                val = True
            elif val == 'false':
                val = False
            current_item[k.strip()] = val
            continue

    _flush_item()
    return result


# ---------------------------------------------------------------------------
# .025 skipgate — per-partition SKIP/COMPUTE/MISSING-INPUT preview
# ---------------------------------------------------------------------------

# Script-to-input-prefix mapping for Pattern A scripts
_SKIPGATE_INPUT_PREFIXES = {
    'INF_B_00': ('s3://opal-data-inf/gold/canonical/', 'holdings_', '.parquet'),
    'INF_B_03': ('s3://opal-data-inf/gold/canonical/', 'nna_', '.parquet'),
    'INF_A_03': ('s3://opal-data-inf/gold/canonical/', 'flows_', '.parquet'),
    'INF_C_00': ('s3://opal-data-inf/gold/canonical/', 'performance_', '.parquet'),
    'INF_C_01': ('s3://opal-data-inf/gold/canonical/', 'nna_canonical_', '.parquet'),
}
_SKIPGATE_META_BASE = 's3://opal-data-inf/gold/meta/'
_SKIPGATE_CURRENT_SCHEMA_VERSION = 1


def _skipgate_list_s3_dates(script_id: str) -> list[str]:
    """List input partition dates for a Pattern A script via S3 listing."""
    import subprocess
    prefix_info = _SKIPGATE_INPUT_PREFIXES.get(script_id)
    if not prefix_info:
        return []
    s3_bucket_prefix, key_prefix, key_suffix = prefix_info
    result = subprocess.run(
        [sys.executable, '-m', 'awscli', 's3', 'ls', s3_bucket_prefix],
        capture_output=True, text=True, timeout=30,
    )
    if result.returncode != 0:
        return []
    dates = []
    for line in result.stdout.splitlines():
        m = re.search(rf'{re.escape(key_prefix)}(\d{{4}}-\d{{2}}-\d{{2}}){re.escape(key_suffix)}', line)
        if not m:
            # Also handle date-only filenames like holdings_2019-09-17.parquet
            m = re.search(rf'{re.escape(key_prefix)}(\d{{4}}-\d{{2}}-\d{{2}})', line)
        if m:
            dates.append(m.group(1))
    return sorted(set(dates))


def _skipgate_check_provenance(script_id: str, date: str) -> dict | None:
    """Check partition_provenance manifest for (script_id, date). Returns None if missing."""
    import subprocess
    import json as _json
    s3_key = f'{_SKIPGATE_META_BASE}partition_provenance/{script_id}/{date}.json'
    result = subprocess.run(
        [sys.executable, '-m', 'awscli', 's3', 'cp', s3_key, '-'],
        capture_output=True, text=True, timeout=10,
    )
    if result.returncode != 0 or not result.stdout:
        return None
    try:
        return _json.loads(result.stdout)
    except Exception:
        return None


def _skipgate_decide(script_id: str, date: str, manifest: dict | None,
                     rebuild_start: str | None, rebuild_end: str | None) -> tuple[str, str]:
    """Return (status, reason) for a single partition."""
    # Rebuild window override
    if rebuild_start and rebuild_end:
        if rebuild_start <= date <= rebuild_end:
            return 'COMPUTE', f'in rebuild window {rebuild_start}:{rebuild_end}'

    # No provenance manifest
    if manifest is None:
        return 'COMPUTE', 'no partition_provenance manifest (not yet computed or Phase 2 not applied)'

    # Schema version check
    stored_schema = manifest.get('schema_version', 0)
    if stored_schema < _SKIPGATE_CURRENT_SCHEMA_VERSION:
        return 'COMPUTE', f'schema_version {stored_schema} < current {_SKIPGATE_CURRENT_SCHEMA_VERSION}'

    # Empty sentinel
    if manifest.get('empty_sentinel', False):
        return 'SKIP', 'empty sentinel -- no rows for this date (valid skip)'

    # All checks pass
    return 'SKIP', 'manifest current; no upstream silver changes detected'


def cmd_skipgate(args) -> None:
    script_id = args.skipgate_script_id.upper().replace('-', '_')

    rebuild_start = rebuild_end = None
    if args.rebuild_window:
        parts = args.rebuild_window.split(':')
        if len(parts) == 2:
            rebuild_start, rebuild_end = parts[0].strip(), parts[1].strip()

    print(f'COMP-PIPESCRIPT SKIPGATE: {script_id}')

    # Phase 1: list input partitions
    dates = _skipgate_list_s3_dates(script_id)
    if not dates:
        # Fallback: generic canonical listing
        print(f'  WARN: no date partitions found for {script_id} via known prefix mapping')
        print('  Hint: add script to _SKIPGATE_INPUT_PREFIXES or verify S3 canonical path')
        return

    print(f'  Input partitions: {len(dates):,} dates ({dates[0]} to {dates[-1]})')

    # Phase 2: check provenance manifests (batch — parallel would require threading)
    # For large partition sets, check a sample for speed then extrapolate
    sample_dates = dates if len(dates) <= 100 else (dates[:10] + dates[-10:])
    print(f'  Checking provenance manifests (sampling {len(sample_dates)} of {len(dates):,} for speed)...')

    rows: list[tuple[str, str, str]] = []
    has_any_manifest = False
    for date in sample_dates:
        manifest = _skipgate_check_provenance(script_id, date)
        if manifest:
            has_any_manifest = True
        status, reason = _skipgate_decide(script_id, date, manifest, rebuild_start, rebuild_end)
        rows.append((date, status, reason))

    # For remaining dates (non-sampled), fast-path: no manifest = COMPUTE
    if len(dates) > len(sample_dates):
        sampled_set = set(sample_dates)
        for date in dates:
            if date not in sampled_set:
                status, reason = _skipgate_decide(script_id, date, None, rebuild_start, rebuild_end)
                rows.append((date, status, reason))
        rows.sort()

    # Filter --manifest-fresh-only (filter to dates where manifest exists or COMPUTE needed)
    if args.manifest_fresh_only:
        rows = [(d, s, r) for d, s, r in rows if 'no partition_provenance' not in r]

    # Summarize
    skip_count = sum(1 for _, s, _ in rows if s == 'SKIP')
    compute_count = sum(1 for _, s, _ in rows if s == 'COMPUTE')
    missing_count = sum(1 for _, s, _ in rows if s == 'MISSING-INPUT')

    print(f'\n  {"DATE":<12}  {"STATUS":<16}  REASON')
    print(f'  {"-"*12}  {"-"*16}  {"-"*55}')

    limit = args.limit if args.limit > 0 else len(rows)
    for date, status, reason in rows[:limit]:
        print(f'  {date:<12}  {status:<16}  {reason[:55]}')

    if len(rows) > limit:
        print(f'  ... ({len(rows) - limit} more rows; use --limit 0 to see all)')

    print(f'\n  Summary: {skip_count} SKIP / {compute_count} COMPUTE / {missing_count} MISSING-INPUT')
    if not has_any_manifest:
        print(f'  INFO: no partition_provenance manifests found -- ADVI_INFINC Phase 2 not yet applied to {script_id}')
        print(f'        All {len(dates):,} partitions show COMPUTE (expected pre-Phase-2 state)')

    if rebuild_window := args.rebuild_window:
        in_window = sum(1 for d, s, _ in rows if rebuild_start <= d <= rebuild_end and s == 'COMPUTE')
        print(f'  Rebuild window {rebuild_window}: {in_window} partition(s) forced to COMPUTE')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog='comp-pipescript',
        description='Authoritative pipeline dependency tool for gold layer scripts.',
    )
    sub = parser.add_subparsers(dest='command')

    _pipeline_help = (
        'Pipeline scope: bd-gold (default), inf-gold, bd-silver, inf-silver, all. '
        'bd-gold is the BD gold layer (backward-compatible default). '
        'inf-gold checks INF gold scripts against opal-data-inf. '
        'all builds a combined cross-pipeline DAG with namespaced IDs.'
    )

    # dag
    p_dag = sub.add_parser('dag', help='Full execution DAG with I/O edges')
    p_dag.add_argument('--json', action='store_true', help='JSON output')
    p_dag.add_argument('--pipeline', '-p', default=None, choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # io
    p_io = sub.add_parser('io', help='Input/output manifest for one script')
    p_io.add_argument('script_id', help='Script ID (e.g., D_00, I_D00, convert_assets_to_silver)')
    p_io.add_argument('--json', action='store_true', help='JSON output')
    p_io.add_argument('--no-portal', action='store_true', dest='no_portal',
                      help='Skip routing table lookup for portal consumer resolution')
    p_io.add_argument('--pipeline', '-p', default=None, choices=_PIPELINE_CHOICES, help=_pipeline_help)
    p_io.add_argument('--firm', default=None, choices=('bd', 'inf', 'cot', 'mdpf'),
                      help='NFRA_DEBTSCAN.TOOL-02: route to this tree\'s OWN graph '
                           '(a data/<tree>/scripts/... path auto-detects; never a bd fallback).')

    # chain
    p_chain = sub.add_parser('chain', help='Show chain membership and order')
    p_chain.add_argument('chain_name', help='Chain name (full, canonical, downstream, foundation, rebuild)')
    p_chain.add_argument('--pipeline', '-p', default=None, choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # feeds
    p_feeds = sub.add_parser('feeds', help='What scripts feed this one (upstream)')
    p_feeds.add_argument('script_id', help='Script ID')
    p_feeds.add_argument('--json', action='store_true', help='JSON output')
    p_feeds.add_argument('--pipeline', '-p', default=None, choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # consumers
    p_consumers = sub.add_parser('consumers', help='What scripts consume this one (downstream)')
    p_consumers.add_argument('script_id', help='Script ID')
    p_consumers.add_argument('--json', action='store_true', help='JSON output')
    p_consumers.add_argument('--pipeline', '-p', default=None, choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # overlap
    p_overlap = sub.add_parser('overlap', help='Shared S3 artifacts between two scripts')
    p_overlap.add_argument('script_a', help='First script ID')
    p_overlap.add_argument('script_b', help='Second script ID')
    p_overlap.add_argument('--pipeline', '-p', default=None, choices=_PIPELINE_CHOICES, help=_pipeline_help)

    # inject
    sub.add_parser('inject', help='Inject pipeline edges into comp-trace graph cache')

    # stats
    sub.add_parser('stats', help='Pipeline graph statistics')

    # deployed
    p_deployed = sub.add_parser('deployed', help='Compare local scripts against S3-uploaded versions')
    p_deployed.add_argument('script_id', nargs='?', default='',
                            help='Optional: check only this script (e.g. D_00, or a '
                                 'data/<tree>/scripts/... path which auto-detects the tree, '
                                 'incl. bronze paths per NFRA_DEBTSCAN.TOOL-03). '
                                 'Omit (with no --firm/--pipeline) to SWEEP ALL trees.')
    # NFRA_DEBTSCAN.TOOL-01: default None so a bare `deployed` sweeps every tree
    # (bd+inf+cot+mdpf). An explicit --pipeline/--firm/path scopes to one tree.
    p_deployed.add_argument('--pipeline', '-p', default=None, choices=_PIPELINE_CHOICES, help=_pipeline_help)
    p_deployed.add_argument('--firm', default=None, choices=('bd', 'inf', 'cot', 'mdpf'),
                            help='NFRA_DEBTSCAN.TOOL-01: single-tree scope by firm/tree. '
                                 'Sweeps that tree against ONLY its own bucket (firm separation).')
    p_deployed.add_argument('--budget', metavar='N', default=None,
                            help='RULE T (PRD s.4.4): one wall-clock ceiling for every timeout-bearing '
                                 'remote operation (carrier: --budget > env COMP_BUDGET_S > default %s s); '
                                 '--budget 0 = unbounded. At expiry deployed returns rc=%d and '
                                 'NOT-DECIDABLE because its rc is verdict-bearing.'
                                 % (_compbudget.fmt(_compbudget.DEFAULT_BUDGET_S), RC_NOT_DECIDABLE))
    p_deployed.add_argument('--cursor', metavar='UNIT', default=None,
                            help='Reserved Rule-T resume cursor. A timeout-bearing operation is indivisible; '
                                 'an expiry leaves this supplied cursor unchanged and directs a larger-budget re-run.')

    # postdeps
    p_postdeps = sub.add_parser('postdeps', help='Show post-step and precondition dependencies for gold scripts')
    p_postdeps.add_argument('script_name', nargs='?', default='',
                            help='Optional: filter to this script name (e.g. D_01 or build_canonical_prices_v2.py). '
                                 'A data/<tree>/scripts/... path auto-detects the tree (TOOL-02).')
    p_postdeps.add_argument('--firm', default=None, choices=('bd', 'inf', 'cot', 'mdpf'),
                            help='NFRA_DEBTSCAN.TOOL-02: read this tree\'s OWN deps config '
                                 '(bd/inf/cot yaml; mdpf = UNCOVERED, no config exists).')

    # postmerge-cols (ADHC_COMPIL_V4.027)
    p_postmerge = sub.add_parser(
        'postmerge-cols',
        help='Flag suffix-collision risks at merge() call sites (ADHC_COMPIL_V4.027)',
    )
    p_postmerge.add_argument('postmerge_script_id',
                             help='Script ID to analyze (e.g. INF_D_00c, D_02)')
    p_postmerge.add_argument('--strict', action='store_true',
                             help='Exit 1 on any unguarded post-merge column access')

    # skipgate (ADHC_COMPIL_V4.025)
    p_skipgate = sub.add_parser(
        'skipgate',
        help='Per-partition SKIP/COMPUTE/MISSING-INPUT preview for Pattern A scripts (ADHC_COMPIL_V4.025)',
    )
    p_skipgate.add_argument('skipgate_script_id',
                            help='Script ID to preview (e.g. INF_B_00, INF_C_00)')
    p_skipgate.add_argument('--rebuild-window', dest='rebuild_window', default=None,
                            metavar='START:END',
                            help='Force COMPUTE for partitions in date range (e.g. 2026-05-01:2026-05-14)')
    p_skipgate.add_argument('--manifest-fresh-only', dest='manifest_fresh_only', action='store_true',
                            help='Filter to partitions where input mtime > last skip-gate emit')
    p_skipgate.add_argument('--limit', type=int, default=50,
                            help='Limit rows displayed (default 50; 0 = all)')

    # shadow-detect (ADHC_COMPIL_V4.028)
    p_shadow = sub.add_parser(
        'shadow-detect',
        help='Enumerate post-condition lock-in chain for a function (ADHC_COMPIL_V4.028)',
    )
    p_shadow.add_argument('shadow_function',
                          help='Function name to analyze (e.g. _aggregate_gro_per_advisor_window)')
    p_shadow.add_argument('--recent-failures', dest='recent_failures', default=None,
                          metavar='DURATION',
                          help='Cross-reference git log for cascade pattern (e.g. 7d, 14d)')

    args = parser.parse_args()

    # ANDREW-DIRECT STUB 2026-07-30: no silent tree default. Scoped to the six subcommands
    # whose None previously meant a SILENT bd-gold fallback (the wrong-tree clean-zero class).
    # `deployed` is exempt: its pipeline=None is the legitimate all-trees sweep / autodetect
    # mode (TOOL-01), not a silent default -- WS4 owns its hardening.
    #
    # WS-1 (NFRA_SCRIPTGEN, Andrew-direct 2026-08-05): replace "you must name a member of the
    # --pipeline roster" with a RE-DERIVED PREDICATE -- try path-derived tree, then auto-walk,
    # BEFORE refusing. This is the a-predicate-is-not-a-roster fix (CTO, 2026-08-04) applied to
    # this gate: a new tree under data/ becomes resolvable with no allowlist edit. Explicit
    # --pipeline (args.pipeline not None) is untouched -- it never reaches this block.
    #
    # `io` is further exempted from the hard refusal here (WS-2, curated-first / AST-always
    # dispatch): cmd_io runs its own copy of this same path/auto-walk resolution and, on a
    # genuine miss, tries the deterministic AST generalist on a real .py file before falling
    # through to the bd/inf resolver's own not-found message (a real bd/inf bare id must keep
    # resolving exactly as before -- WS-1 acceptance: in-universe scripts stay byte-identical).
    if getattr(args, 'command', None) in ('dag', 'io', 'chain', 'feeds', 'consumers', 'overlap') \
            and getattr(args, 'pipeline', 'x') is None:
        _hint = None
        for _attr in ('script_id', 'script', 'name', 'target'):
            _v = getattr(args, _attr, None)
            if _v:
                _hint = _v
                break
        # REGRESSION REPAIR 2026-08-05 (3.0.0_SA_CVO~B, mine to fix): I had inserted an `io`
        # carve-out + `if False:` scaffolding here while 1.0.0_SA_CTO~C was implementing WS-1 in
        # this same shared worktree. My uncommitted fragment was swept into their commit
        # @e73873f163, and the `if False:` made THEIR path-derived resolution UNREACHABLE --
        # dag/chain/feeds/consumers/overlap refused a path-qualified argument at rc=2 instead of
        # resolving it. Their feature shipped dead, in their name, because of my scaffolding.
        # The carve-out was also redundant: their design already falls `io` through (see the else
        # branch below), so removing my block restores the intended flow exactly.
        if args.command != 'io':
            _gate_resolved = None
            if _hint:
                _gnp = _hint.replace('\\', '/')
                for _gdir, _gpk in _DATADIR_TO_PIPELINE.items():
                    if f"data/{_gdir}/scripts/" in _gnp or _gnp.startswith(f"data/{_gdir}/"):
                        _gate_resolved = _gpk
                        break
                if _gate_resolved is None:
                    _gate_resolved = _autowalk_pipeline_for_script(_hint)
            if _gate_resolved:
                args.pipeline = _gate_resolved
            else:
                # WS-1 COMPLETION (3.0.0_SA_CVO~B 2026-08-05, finishing the pass ~C left):
                # the roster loop above answers only for the FOUR deploy-map trees. The PREDICATE
                # sees SEVEN on disk, so a path in assets/etfs/demo fell through to a refusal
                # reading "--pipeline/-p is now REQUIRED ... re-run with the one you mean".
                #
                # THAT MESSAGE IS FALSE FOR THOSE TREES, and falsely blames the caller: --pipeline
                # has NO valid value for `assets` (it is not in _PIPELINE_CHOICES), so the tool
                # demanded a flag that cannot be supplied and called it user error. An instruction
                # the user cannot follow is worse than a refusal, because it sends them looking for
                # a spelling that does not exist.
                #
                # Split the two cases HONESTLY -- the predicate is what distinguishes them:
                _pred = _resolve_tree_from_path(_hint)
                if _pred and not _pred[2]:          # real tree on disk, NO curated graph
                    _ptree, _players = _pred[0], ', '.join(_discover_script_trees().get(_pred[0], []))
                    print(f"NO CURATED GRAPH for tree '{_ptree}' (layers on disk: {_players}).",
                          file=sys.stderr)
                    print(f"  `{args.command}` needs a curated pipeline DAG and this tree has none, "
                          "so there is no --pipeline value to pass -- this is NOT a missing flag.",
                          file=sys.stderr)
                    print(f"  WHAT WORKS TODAY: `comp-pipescript io {_hint}` answers from the "
                          "deterministic AST generalist (reads/writes + denominator).", file=sys.stderr)
                    print(f"  Curated trees: {', '.join(sorted(_DATADIR_TO_PIPELINE))}.",
                          file=sys.stderr)
                    sys.exit(2)
                _refuse_no_pipeline(_hint)
        # else: 'io' falls through to cmd_io with args.pipeline still None -- cmd_io resolves
        # (path/auto-walk/generalist) or refuses itself; see cmd_io.
    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        'dag': cmd_dag,
        'io': cmd_io,
        'chain': cmd_chain,
        'feeds': cmd_feeds,
        'consumers': cmd_consumers,
        'overlap': cmd_overlap,
        'inject': cmd_inject,
        'stats': cmd_stats,
        'deployed': cmd_deployed,
        'postdeps': cmd_postdeps,
        'postmerge-cols': cmd_postmerge_cols,
        'shadow-detect': cmd_shadow_detect,
        'skipgate': cmd_skipgate,
    }
    _rc = commands[args.command](args)
    # Let a command signal a non-zero rc by RETURNING one (CVO~B 2026-08-05). Previously the
    # return value was discarded, so every command that did not sys.exit() itself was pinned
    # to rc=0 -- which is how `deployed` reported a nothing-verified run as success. Guarded
    # on isinstance(int) so a command returning data (not a code) can never become an exit
    # status; a 0/None return keeps the existing behaviour exactly.
    if isinstance(_rc, int) and _rc:
        sys.exit(_rc)


if __name__ == '__main__':
    main()
