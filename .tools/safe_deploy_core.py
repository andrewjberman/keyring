#!/usr/bin/env python3
"""safe_deploy_core.py -- core logic for safe-deploy.sh (ADHC_DSFLOW.005).

Provides: file->pipeline mapping, detect changed scripts, S3 deploy + verify,
bypass audit logging. Callable directly or importable by test_safe_deploy.py.
"""
from __future__ import annotations

import contextlib
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from typing import Optional

WORKSPACE = pathlib.Path(__file__).parent.parent

# ---------------------------------------------------------------------------
# CODE_TREES -- THE ONE DECLARATION (INFRA.TOOLS; CTO ruling 20260728T203649Z:
# "ONE PLAN, all three registries, or none").
#
# WHAT THIS REPLACES. The same population was previously described by THREE
# machine-readable authorities that each RESTATED the layout at their own call
# site, and all three were wrong in different ways:
#   1. PIPELINE_MAP + VALID_LAYERS here -- single-layout: emitted code/<layer>/
#      and knew only {gold,silver,bronze}, so mdpf could not be expressed at all.
#   2. pipeline_cli.py:1945 -- a hardcoded 4-layer tuple against SIX live layers.
#   3. EC2_MANIFEST.json code_prefix -- one path segment too coarse to address
#      the code tree.
# Consumers now DERIVE from this table. Same principle as the row-13 per-source
# grammar declaration and the roster-derived partner cohorts: DERIVE FROM ONE
# DECLARED AUTHORITY, NEVER RESTATE AT A CALL SITE.
#
# >> WHY A LAYER *LIST* IS NOT ENOUGH, AND WHY THE OBVIOUS FIX IS A SILENT NO-OP:
# THE REPO HOME IS NOT DERIVABLE FROM THE TREE NAME. Every consumer used to
# assume data/<tree>/scripts/<layer>/. For mdpf that is FALSE -- ONE S3 code tree
# is fed by TWO repo trees:
#     s3 code/scripts/assets_gold/  <- data/assets/scripts/gold      (NOT data/mdpf/)
#     s3 code/scripts/silver/       <- data/assets/scripts/silver    (NOT data/mdpf/)
# Adding "assets_gold"/"silver" to a layer list would glob a nonexistent
# data/mdpf/scripts/<layer>/, hit `continue`, and report a CLEAN summary with a
# layer list that merely LOOKS complete -- converting a visible gap into an
# invisible one. Hence per-(tree, layer) -> (repo_home, s3_prefix). <<
#
# deploy_gated: True  = in the Rule-13 deploy gate (file_to_s3_target resolves;
#                       a push DEPLOYS it). bd/inf/cot -- unchanged, byte-identical.
# deploy_gated: False = DECLARED CHECK-ONLY. Visible to staleness sweeps, NOT a
#                       deploy target.
# mdpf FLIPPED True 2026-08-04 on ANDREW-DIRECT (0.2.0_DS terminal ~18:4xZ,
# verbatim record ANDREW_DIRECT_20260804_DS_RESOURCE_DEPLOYMENT_ABILITY.md; CTO
# shape-approval 185213Z, COO 185209Z): "If you are editing these scripts you
# need to be able to deploy them so we do not keep ending up in this situation."
# The prior False carried an in-code note that the flip was "CTO's call" -- that
# pending call, never made, is the mechanism under the 2026-08-04
# committed-but-never-deployed incidents (acct-dist 12-day stale fold et al.).
# SHARED-HOME layers (tree["shared_repo_homes"]) deploy under the S3-MEMBERSHIP
# GUARD in main(): key-exists = update (enforced); 404 = SKIP-NOT-MEMBER, loud,
# printing the probed key + prefix denominator (first-mints stay explicit/manual).
# Membership is keyed on S3-KEY-EXISTENCE, never on local path -- so a repo-home
# migration (e.g. CANRTE W-4 moving the cot slice/pair) changes NOTHING here.
# ---------------------------------------------------------------------------
CODE_TREES: dict[str, dict] = {
    "black_diamond": {
        "bucket": "opal-data-bd",
        "label": "bd",
        "deploy_gated": True,
        "layers": {
            "gold": ("data/black_diamond/scripts/gold", "code/gold/"),
            "silver": ("data/black_diamond/scripts/silver", "code/silver/"),
            "bronze": ("data/black_diamond/scripts/bronze", "code/bronze/"),
        },
    },
    "inf": {
        "bucket": "opal-data-inf",
        "label": "inf",
        "deploy_gated": True,
        "layers": {
            "gold": ("data/inf/scripts/gold", "code/gold/"),
            "silver": ("data/inf/scripts/silver", "code/silver/"),
            "bronze": ("data/inf/scripts/bronze", "code/bronze/"),
        },
    },
    "cot": {
        "bucket": "opal-data-cot",
        "label": "cot",
        "deploy_gated": True,
        "layers": {
            "gold": ("data/cot/scripts/gold", "code/gold/"),
            "silver": ("data/cot/scripts/silver", "code/silver/"),
            "bronze": ("data/cot/scripts/bronze", "code/bronze/"),
        },
        # SECOND DEPLOY TARGETS (CPR-5 2026-08-11; CTO-ruled remedy, COO
        # 063335Z staffing; DS owns, AE verifies the landing). ONE source, N
        # declared targets -- the fan-out declared ONCE at the convergence
        # point, closing the drift class by construction (the bd copy froze at
        # 08-04 while running daily precisely because no deploy leg served it).
        # WHY THE SECOND HOME EXISTS AT ALL (Model B, ADVI_BDAPIMIG P1-B,
        # 06-25 deploy record): the bd-49f runner Lambdas execute this
        # cot-authored single source FIRM-BOUND, and their role carries an
        # explicit Deny on opal-data-cot -- firm separation itself forces the
        # engine to be staged bd-side. This is a sanctioned shared-engine
        # deploy, NOT a bd<->cot data mirror (which stays gate-banned).
        # Semantics per Rule 13's shared-home membership guard, target-grain:
        # key-EXISTS = update ENFORCED; 404 = LOUD SKIP (never a silent
        # first-mint into another firm's bucket); UNDETERMINED = fail closed.
        "second_targets": {
            "data/cot/scripts/bronze/cot_bronze_ingest.py": [
                ("opal-data-bd", "code/bronze/cot_bronze_ingest.py"),
            ],
        },
    },
    # DEPLOY-GATED since 2026-08-04 (Andrew-direct; see the flip note above).
    # Non-standard layout: preserves scripts/<layer>/ under code/, and two of its
    # six layers are fed from data/assets/, not data/mdpf/ (shared homes -- the
    # membership guard governs those two; the mdpf-native four deploy
    # unconditionally like bd/inf/cot).
    "mdpf": {
        "bucket": "opal-data-mdpf",
        "label": "mdpf",
        "deploy_gated": True,
        # SHARED repo homes: data/assets/scripts/{gold,silver} serve MULTIPLE
        # destinations, and only a SUBSET of each is deployed to mdpf's tree
        # (3 of 7 under gold; 1 of 13 under silver, measured 2026-07-28). For a
        # shared home the S3 side is the authority on membership: a repo file
        # with no counterpart at the mdpf prefix was never meant to be there and
        # is NOT a missing deploy. Without this the sweep emits ~16 false
        # MISSING_ON_S3 rows -- and a sweep with more false positives than
        # findings trains people to ignore it, which is the same end state as
        # the blindness it replaced. The INVERSE direction is unaffected: an S3
        # object with no repo counterpart still surfaces as UNCOVERED.
        "shared_repo_homes": {"assets_gold", "silver"},
        # NON-SCRIPT ARTIFACTS that must be PRESENT in the synced runtime prefix.
        # Raised by 0.7.0_AE_CloudOps base (210149Z), measured live: the dispatch
        # syncs code/scripts/ with --delete, so a hand-placed config copy is
        # SILENTLY REVERTED on the next run; the tree currently carries 34 objects
        # and partner_roster.json is ABSENT. A model that only knows .py files
        # excludes this class entirely, and the next person solves it with a
        # one-off `aws s3 cp` that the following --delete undoes.
        #
        # s3_key None = DECLARED, TARGET UNRESOLVED. The destination key is a real
        # decision (code/scripts/ is fed by two repo trees), and picking one here
        # would be exactly the call-site literal this table exists to abolish.
        # Declared-with-an-unknown is auditable; omitted is not -- the same
        # sentinel shape ruled for the manifest trigger field.
        "artifacts": {
            "partner_roster": {
                "repo_path": "data/mdpf/config/partner_roster.json",
                # RESOLVED 2026-07-28T2333Z (CTO 233212Z/233329Z insert; DS's
                # DEPLOYED resolver defines the contract -- script-adjacent,
                # checked FIRST at /opt/mdpf/scripts/gold/partner_roster.json).
                # Published + ETag==local-md5 verified (a22fc62be04777eb...).
                # DURABILITY: safe-deploy uploads are per-file `s3 cp` (no S3
                # prefix --delete), so this object survives DS gold deploys; the
                # runner's S3->EC2 sync then propagates it every run.
                "s3_key": "code/scripts/gold/partner_roster.json",
                "owner": "0.7.0_AE_CloudOps base / 1.0.0_SA_CTO",
                # THE REFRESH MECHANISM (one line, per CTO 233329Z): AE-base
                # republishes this key on ANY commit touching repo_path -- the
                # repo copy is the ONE authority; the S3 copy is a deploy of it.
                "republish_on_change_by": "0.7.0_AE_CloudOps",
                # SUPERSEDED 2026-08-11 (X-iii, CTO-blessed bundle shape 060208Z):
                # the roster now ships INSIDE bundles.accrual_bridge; this loose
                # S3 object is DEPRECATED-IN-PLACE (frozen rollback target, never
                # updated, never deleted) and the AE republish duty above is
                # RETIRED with it (AE notified 062039Z). Declaration kept so the
                # frozen object stays modelled, not rediscovered as cruft.
                "superseded_by": "bundles.accrual_bridge",
                "why": "canonical partner roster; gold consumers need it in the "
                       "gold runtime. Cross-tree import RAISEs, repo-relative read "
                       "fail-closes, --delete reverts a hand-placed RUNNER copy "
                       "(the S3->EC2 sync direction; the S3 object is durable).",
            },
        },
        # HASH-STAMPED BUNDLES (X-iii 2026-08-11; CTO-blessed shape 060208Z;
        # DS+AE joint act). A bundle is ONE deployable tar.gz whose members are
        # materialized at PACKAGE TIME from their committed authorities -- a
        # member is not independently mutable (CTO 08-06 no-S3-roster-twin
        # ruling); mutation = republish the whole hash-stamped bundle. The
        # packaging step lives HERE in the deploy map/flow (CTO condition 1:
        # never a free-standing packaging script). A member script listed in a
        # bundle EXITS the loose per-file leg: its old loose S3 objects are
        # DEPRECATED-IN-PLACE (frozen rollback target for the AE trigger's env
        # repoint; never updated, never deleted). NOTE the instrument
        # consequence: comp-pipescript deployed still compares the repo script
        # to the FROZEN loose key, so bundle-routed scripts are excluded from
        # the per-file pipescript verify -- the mint's own sha-stamped verify
        # (ETag + metadata) is their acceptance surface.
        "bundles": {
            "accrual_bridge": {
                # {tar member name -> authority}; flat member names so the AE
                # trigger's `tar -xzf` into /opt/mdpf/scripts/gold/ lands the
                # roster SCRIPT-ADJACENT (the script's resolution location 1).
                "members": {
                    "build_portal_gold_accrual.py": {
                        "repo_path": "data/mdpf/scripts/gold/build_portal_gold_accrual.py",
                        "sha_metadata_key": "script-sha256",
                    },
                    "partner_roster.json": {
                        "repo_path": "data/mdpf/config/partner_roster.json",
                        "sha_metadata_key": "roster-authority-sha256",
                    },
                },
                "bucket": "opal-data-assets",
                "s3_key": "portal/gold/mdpf/_code/mdpf-accrual-bridge.tar.gz",
            },
            # IRPT FIRST-MINT 2026-09-11 (IRPT_BCKEND.TO-IB-rt-5; the CTO's
            # round-1 analysis ruling 3(c) opens the Rule-13 gate; DS act).
            # The two investor-reporting runners were COMMITTED in round 1 and
            # never SERVED: their shared-home keys under
            # code/scripts/assets_gold/investor_reporting/ 404, so every push
            # read SKIP-NOT-MEMBER and the loose leg CANNOT first-mint by
            # design (first-mints stay explicit). Declaring the pair as ONE
            # bundle routes both through the in-flow mint, which is the only
            # explicit first-mint mechanism the guard carries.
            #
            # >> DISTINCT sha_metadata_key PER MEMBER, AND THAT IS LOAD-BEARING.
            # build_bundle_payload assigns shas[spec["sha_metadata_key"]] inside
            # a loop over sorted members, so two members sharing ONE key
            # silently COLLIDE: only the last-sorted member's sha reaches S3,
            # and the object then carries a stamp that verifies ONE file while
            # reading as though it covered both -- a false green on the exact
            # surface the mint's verify leg exists to police. accrual_bridge is
            # per-member (script-sha256 + roster-authority-sha256) for the same
            # reason. <<
            #
            # tests/ is NOT a member: only declared members enter the tar.
            #
            # >> ids.py IS A DISTRIBUTION, NOT A SECOND DEFINITION, AND THE DIFFERENCE IS THE
            # WHOLE POINT (IRPT_BCKEND.TO-IB-rt-6 amendment H3; row IRPT_BCKEND-W2-S44).
            # MEASURED ON THE HOST 2026-09-12: `import directory_runner` on the mdpf-daily-runner
            # fails `ModuleNotFoundError: No module named 'ids'` -- the runner imports BOTH
            # trading_calendar and ids at MODULE level (directory_runner.py:108, :115, col 0) and
            # uses _ids.opaque at :146, so it cannot be imported at all without them, and the
            # bundle carried only the two runner files.
            #
            # A FILE COPY into data/assets/scripts/gold/investor_reporting/ would have been a
            # SECOND DEFINITION of THE ONE opaque-id normalizer, which irpt-holdings'
            # BUILD_MANIFEST.json forbids in those words ("never vendored beside the function,
            # because a second copy of either is the defect the layer exists to prevent").
            # Declaring it HERE is different in kind: `build_bundle_payload` resolves
            # `repo_path` from the repository at build time, so the ONE authority stays
            # infra/aws/lambda/investor-reporting/_ids/ids.py and the bundle carries a copy the
            # way every Lambda zip already does -- lambda-source-map.json declares the same file
            # as a flat build input for three functions, and `trading_calendar` already reaches
            # that same host from its own distribution (measured byte-identical to lib/).
            # NO FILE IS COPIED INTO THE REPO BY THIS LINE.
            #
            # The member name is FLAT (`ids.py`), which is what makes it importable: the runner
            # is executed as a script, so its own directory is sys.path[0] and the unpacked
            # sibling resolves as `ids` without the repo-shaped `_IDS_DIR` existing on the box.
            #
            # DISTINCT sha_metadata_key, per the rule stated above this dict: two members sharing
            # one key silently collide and the object then carries a stamp that verifies ONE file
            # while reading as though it covered both. `ids-sha256` is its own key. <<
            "investor_reporting": {
                "members": {
                    "directory_runner.py": {
                        "repo_path": "data/assets/scripts/gold/investor_reporting/directory_runner.py",
                        "sha_metadata_key": "directory-runner-sha256",
                    },
                    "holdings_snapshot.py": {
                        "repo_path": "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py",
                        "sha_metadata_key": "holdings-snapshot-sha256",
                    },
                    "ids.py": {
                        "repo_path": "infra/aws/lambda/investor-reporting/_ids/ids.py",
                        "sha_metadata_key": "ids-sha256",
                    },
                    # THE ESTATE'S ONE TRADING-DAY FRONTIER, DISTRIBUTED AND NOT COPIED (cell
                    # IB-rt-6, the same distinction amendment H3 drew for ids.py above). Both
                    # runners in this bundle import it -- `directory_runner.py:104-108` inserts
                    # `<repo>/lib` on sys.path and does `import trading_calendar as tcal` at
                    # MODULE level, so without this member the runner cannot be imported at all,
                    # let alone run. MEASURED, not predicted: the first real SSM dispatch of this
                    # bundle printed
                    #   [irpt-directory] IMPORT-FAIL ... ModuleNotFoundError: No module named
                    #   'trading_calendar'
                    # on the host (command 940c828f-c176-4a2d-afcc-1693d3d97fe6, Failed rc=1) for
                    # 3 of 3 firms.
                    #
                    # DECLARING A MEMBER THAT RESOLVES FROM `lib/trading_calendar.py` IS A
                    # DISTRIBUTION; putting a second copy of the frontier in the runner's own
                    # directory would be a SECOND DEFINITION and is refused. CLAUDE.md: "One
                    # frontier: lib/trading_calendar.py". The tar carries a copy the way every
                    # tar does, and it is minted from the one authority every time.
                    "trading_calendar.py": {
                        "repo_path": "lib/trading_calendar.py",
                        "sha_metadata_key": "trading-calendar-sha256",
                    },
                },
                "bucket": "opal-data-mdpf",
                "s3_key": "code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz",
            },
        },
        "layers": {
            "gold": ("data/mdpf/scripts/gold", "code/scripts/gold/"),
            "backfill": ("data/mdpf/scripts/backfill", "code/scripts/backfill/"),
            "feeders": ("data/mdpf/scripts/feeders", "code/scripts/feeders/"),
            "bronze": ("data/mdpf/scripts/bronze", "code/scripts/bronze/"),
            "assets_gold": ("data/assets/scripts/gold", "code/scripts/assets_gold/"),
            "silver": ("data/assets/scripts/silver", "code/scripts/silver/"),
        },
    },
    # ADVI tree (CTO RULED 2026-08-18 172006Z, on the mdpf _code/ precedent above:
    # portal/gold/mdpf/_code/ already exists in bundles.accrual_bridge s3_key).
    # The 49F canonical runner chain's S3 code home is the atom-2 ONE deploy target
    # inside the already-ratified product root -- NOT the mdpf bucket (cross-product,
    # the measured-violation class). Repo home is a SUBTREE of the shared
    # data/assets/scripts/gold home: resolution is LONGEST-PREFIX (see
    # file_to_s3_target), so runners_49f files land here and every OTHER assets_gold
    # file keeps its mdpf mapping unchanged. First-mints stay EXPLICIT per the
    # membership guard; membership at this prefix is exact (runners_49f only), so
    # the shared-home false-MISSING class cannot arise on this row.
    # GOLDHOME re-point 2026-08-18 (Andrew ~1730Z, TO @1b2ee34db7; CTO pin 174449Z): the
    # 49F chain's code home is the PER-CLIENT bucket's BUCKET-ROOT _code/ (NOT under gold/ --
    # gold/ is the parquet data tree and the agentic-query root; _code stays FLAT until a
    # second product joins the bucket, and THAT act adds the product level).
    "advi": {
        "bucket": "opal-data-49financial",
        "label": "advi",
        "deploy_gated": True,
        "layers": {
            "gold": ("data/assets/scripts/gold/runners_49f", "_code/"),
        },
    },
}

# Pipeline detection table: data_dir_name -> (s3_bucket, pipeline_label).
# DERIVED -- the deploy gate is exactly the deploy_gated trees. Byte-identical to
# the hand-written table it replaces: {black_diamond, inf, cot}.
PIPELINE_MAP: dict[str, tuple[str, str]] = {
    name: (tree["bucket"], tree["label"])
    for name, tree in CODE_TREES.items()
    if tree["deploy_gated"]
}

BYPASS_AUDIT_LOG = WORKSPACE / "org" / "safe-deploy-bypass-audit.log"

# DERIVED -- the layer vocabulary of the GATED trees. WIDENED 2026-08-04 by the
# mdpf flip (adds backfill/feeders/assets_gold to the union). NOTE: this is a
# UNION vocabulary, not a per-tree fact -- crossing PIPELINE_MAP x VALID_LAYERS
# uniformly mints phantom (tree, layer) pairs (bd has no backfill). Consumers
# enumerate a TREE's real legs via tree_layers(name), never this cross-product
# (deploy_ledger corrected with the flip).
VALID_LAYERS = {
    layer
    for tree in CODE_TREES.values()
    if tree["deploy_gated"]
    for layer in tree["layers"]
}


def tree_layers(tree_name: str) -> dict[str, tuple[str, str]]:
    """Return {layer: (repo_home, s3_prefix)} for a declared tree.

    Raises KeyError on an undeclared tree -- NEVER returns {} for one, because a
    silent empty layer set is exactly the false-clean this table exists to end.
    """
    return CODE_TREES[tree_name]["layers"]

# ---------------------------------------------------------------------------
# Phase-1 serve-gate (CTO, Andrew-approved). A committed deploy-scope .py does
# NOT auto-serve on push if it carries a SERVE-HELD sentinel; REMOVING that
# sentinel (old had it, current does not) is authorizing serve, so it is gated
# behind an in-message SERVE-RELEASE-ACK (tied to NEVER#2 never-widen).
# All three checks FAIL CLOSED: any unreadable file / git error BLOCKS the deploy.
# ---------------------------------------------------------------------------
# A held file carries a line like:   # DEPLOY-SERVE-HELD: waiting on CTO signoff
# Horizontal-whitespace-only ([ \t]) around the reason so a MALFORMED / no-reason
# sentinel still MATCHES (stays HELD) -- fail-closed direction: never fall through
# to serve on a parse ambiguity.
SERVE_HELD_RE = re.compile(r"^[ \t]*#[ \t]*DEPLOY-SERVE-HELD\b[ \t]*:?[ \t]*(.*?)[ \t]*$")
# An authorizing commit carries a line like:  SERVE-RELEASE-ACK: <reason>
# [ \t]* (NOT \s*) is load-bearing: \s* would cross the newline and let an EMPTY
# `SERVE-RELEASE-ACK:` falsely capture the NEXT commit line as its "reason" -- a
# fail-OPEN inversion of the gate. The reason MUST be non-empty and on the SAME line.
SERVE_RELEASE_ACK_RE = re.compile(
    r"^[ \t]*SERVE-RELEASE-ACK:[ \t]*(\S.*?)[ \t]*$", re.MULTILINE
)

# ---------------------------------------------------------------------------
# Canonical code-prefix registry (ADVI_INFETL.BRONZE-FIX #1 + NFRA_DEBTSCAN
# TOOL-03; machine-readable surface for the deploy-completion ledger, TO #5).
#
# The COMPLETE canonical map of every code location on a firm bucket is:
#   standard layers: PIPELINE_MAP x VALID_LAYERS
#       repo data/<dir>/scripts/<layer>/*.py -> s3://<bucket>/code/<layer>/
#       (file_to_s3_target -- the Rule-13 deploy gate; ONE prefix per layer,
#       upload target == every consumer's sync source. The 2026-06-12 inf-ADVI
#       P0 was a violation of this invariant: orchestrator deploys landed at
#       code/bronze/ while the runner synced code/bronze-runner/.)
#   auxiliary prefixes: AUX_CODE_PREFIXES below
#       CHECK-ONLY locations outside the deploy gate. Value = repo-home dir for
#       same-basename comparison (comp-pipescript deployed [aux:<prefix>] rows);
#       None = no unambiguous repo home -> the tool reports UNCOVERED, never
#       silent-clean. Consumers: comp-pipescript (pipeline_cli imports this),
#       deploy-ledger leg enumeration (TO #5).
#
#   inf bronze-runner/ -- runner-OPS assets ONLY post-collapse (fetch script,
#     watchdog, backfill helpers; repo home infra/aws/ec2/inf-bronze-runner)
#     + the manual_api mirror sub-prefix (remaining consolidation leg).
#     PIPELINE code no longer lives here -- the runner syncs orchestrator.py
#     from code/bronze/ (BRONZE-FIX #1).
#   inf manual_api/ -- Orion REST dim-pull scripts, consumed by the inf GOLD
#     runner's 4-prefix flat sync (collision-guarded); repo home
#     data/inf/manual_api.
# ---------------------------------------------------------------------------
AUX_CODE_PREFIXES: dict[str, dict[str, Optional[str]]] = {
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


def file_to_s3_target(rel_path: str) -> Optional[tuple[str, str, str]]:
    """Map a repo-relative file path to (bucket, s3_key, pipeline_label).

    Scope: data/<pipeline_dir>/scripts/{gold,silver,bronze}[/lib]/*.py
    Returns None if path is not in a recognized deploy scope.
    """
    norm = rel_path.replace("\\", "/")
    p = pathlib.PurePosixPath(norm)
    parts = p.parts
    # Minimum: data / <pd> / scripts / <layer> / <file>.py  (5 parts)
    if len(parts) < 5:
        return None
    if parts[0] != "data":
        return None
    if not norm.endswith(".py"):
        return None

    # DERIVED from CODE_TREES -- the layout is no longer hardcoded here. Only
    # deploy_gated trees resolve; a check-only tree (mdpf) returns None exactly as
    # before, so the Rule-13 gate's behavior is unchanged.
    # LONGEST-PREFIX resolution (2026-08-18, the advi row): the advi gold home is a
    # SUBTREE of mdpf's shared assets_gold home, so first-match-in-dict-order would
    # make the answer depend on insertion order -- an order-dependent gate is a trap.
    # Longest repo_home wins: behavior-identical for every pre-existing file (no
    # other overlaps exist) and deterministic for nested homes regardless of order.
    best: Optional[tuple[str, str, str]] = None
    best_len = -1
    for tree in CODE_TREES.values():
        if not tree["deploy_gated"]:
            continue
        for layer, (repo_home, s3_prefix) in tree["layers"].items():
            if not norm.startswith(repo_home + "/"):
                continue
            # Remainder after the layer dir, preserving any [lib/] subpath.
            suffix = norm[len(repo_home) + 1:]
            if not suffix:
                continue
            if len(repo_home) > best_len:
                best_len = len(repo_home)
                best = (tree["bucket"], f"{s3_prefix}{suffix}", tree["label"])
    return best


def resolve_tree_layer(rel_path: str) -> Optional[tuple[str, dict, str]]:
    """Resolve rel_path to (tree_name, tree_dict, layer_name) for deploy-gated trees.

    The membership-guard companion to file_to_s3_target: the caller needs to know
    WHICH layer matched to test `layer in tree["shared_repo_homes"]`. Same loop,
    same LONGEST-PREFIX semantics (2026-08-18, with the advi row -- the two
    resolvers MUST agree or the guard tests a different layer than the deploy
    targets); returns None exactly where file_to_s3_target does."""
    norm = rel_path.replace("\\", "/")
    if not norm.endswith(".py"):
        return None
    best: Optional[tuple[str, dict, str]] = None
    best_len = -1
    for name, tree in CODE_TREES.items():
        if not tree["deploy_gated"]:
            continue
        for layer, (repo_home, _s3_prefix) in tree["layers"].items():
            if norm.startswith(repo_home + "/") and norm[len(repo_home) + 1:]:
                if len(repo_home) > best_len:
                    best_len = len(repo_home)
                    best = (name, tree, layer)
    return best


def s3_key_exists(bucket: str, key: str) -> tuple[Optional[bool], str]:
    """head-object existence probe for the shared-home membership guard.

    Returns (True, "") exists / (False, "") 404 / (None, err) UNDETERMINED --
    the caller must fail closed on None (an unreachable S3 is not a 404).
    Uses the same aws resolution as deploy_file (the .tools shim path)."""
    aws_bin = _find_aws()
    if not aws_bin:
        return None, "aws CLI not found"
    r = subprocess.run(
        [aws_bin, "s3api", "head-object", "--bucket", bucket, "--key", key],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30, env=_aws_env(),
    )
    if r.returncode == 0:
        return True, ""
    if "(404)" in r.stderr or "Not Found" in r.stderr:
        return False, ""
    return None, r.stderr.strip()[:200]


def s3_prefix_keycount(bucket: str, prefix: str) -> str:
    """Best-effort member count under a prefix, for the SKIP-NOT-MEMBER audit line.
    Single list-objects-v2 page (<=1000): honest for these code prefixes (~3-40
    objects); labeled as page-bounded so the denominator is never read as a
    paginated total (the CLAUDE.md length()-per-page trap)."""
    aws_bin = _find_aws()
    if not aws_bin:
        return "?"
    # MATERIALIZED count, not --query: this box's CLI v1 response carries NO
    # KeyCount field at all (measured: keys = Contents/Prefix/RequestCharged, so
    # `--query KeyCount` prints "None"), and a `length(Contents)` query is the
    # CLAUDE.md per-page-length trap waiting for a >1000-key prefix. Parse the
    # JSON, count the materialized list; the single-page bound stays labeled at
    # the call site.
    r = subprocess.run(
        [aws_bin, "s3api", "list-objects-v2", "--bucket", bucket,
         "--prefix", prefix, "--output", "json"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30, env=_aws_env(),
    )
    if r.returncode != 0:
        return "?"
    try:
        return str(len(json.loads(r.stdout or "{}").get("Contents", [])))
    except Exception:
        return "?"


def _changed_paths(commit_range: Optional[str]) -> list[str]:
    """Raw changed-path list (ACMRT) for a commit range, repo-relative.

    Extracted from detect_script_files unchanged so the bundle-member detector
    reads the SAME population -- two detectors over two diffs would drift."""
    if commit_range:
        old_sha = commit_range.split("..")[0] if ".." in commit_range else ""
        if old_sha.startswith("0000000"):
            # New branch: diff against main
            cmd = ["git", "diff", "--name-only", "--diff-filter=ACMRT", "origin/main...HEAD"]
        else:
            cmd = ["git", "diff", "--name-only", "--diff-filter=ACMRT", commit_range]
    else:
        cmd = ["git", "diff", "--name-only", "--diff-filter=ACMRT", "HEAD~1..HEAD"]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(WORKSPACE), timeout=30
        )
        return [f.strip() for f in result.stdout.splitlines() if f.strip()]
    except Exception:
        return []


def detect_script_files(
    commit_range: Optional[str] = None,
    explicit_files: Optional[list[str]] = None,
) -> list[str]:
    """Return list of repo-relative deploy-scope .py paths.

    Priority: explicit_files > commit_range > git diff HEAD~1..HEAD.
    """
    if explicit_files:
        return [f for f in explicit_files if file_to_s3_target(f) is not None]
    return [f for f in _changed_paths(commit_range) if file_to_s3_target(f) is not None]


def detect_bundle_member_files(
    commit_range: Optional[str] = None,
    explicit_files: Optional[list[str]] = None,
) -> list[str]:
    """Changed paths that are BUNDLE MEMBER AUTHORITIES (any extension).

    The .py member also appears in detect_script_files; the non-script member
    (e.g. the roster json) appears ONLY here -- without this, a roster-only
    commit would never re-mint its bundle (the exact silent-config-leg class the
    an-atomic-commit-is-not-an-atomic-deploy incident named)."""
    authorities = {
        m["repo_path"]
        for tree in CODE_TREES.values()
        for b in tree.get("bundles", {}).values()
        for m in b["members"].values()
    }
    pool = explicit_files if explicit_files else _changed_paths(commit_range)
    return [f for f in pool if f.replace("\\", "/") in authorities]


def _local_md5(path: pathlib.Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def _aws_env() -> dict[str, str]:
    env = os.environ.copy()
    env.setdefault("AWS_EC2_METADATA_DISABLED", "true")
    env.setdefault("AWS_METADATA_SERVICE_NUM_ATTEMPTS", "1")
    env.setdefault("AWS_PAGER", "")
    return env


def _find_aws() -> Optional[str]:
    return shutil.which("aws") or shutil.which("aws.cmd") or shutil.which("aws.exe")


def _index_blob(rel_path: str) -> tuple[Optional[bytes], str]:
    """The bytes git HAS RECORDED for rel_path -- `git show :<path>`, the INDEX, not the worktree.

    BYTES, never text: decoding here would re-introduce the newline translation this whole
    change exists to remove. Returns (blob, "") or (None, stderr) -- never a worktree fallback,
    because falling back to the worktree on a lookup failure would silently restore exactly the
    behaviour being replaced.
    """
    r = subprocess.run(["git", "show", ":" + rel_path.replace("\\", "/")],
                       capture_output=True, cwd=str(WORKSPACE), timeout=30)
    if r.returncode != 0:
        return None, (r.stderr or b"").decode("utf-8", "replace").strip()
    return r.stdout, ""


def deploy_file(
    local_path: pathlib.Path,
    bucket: str,
    s3_key: str,
    rel_path: Optional[str] = None,
) -> tuple[str, str]:
    """Upload the INDEX BLOB for rel_path to S3 and verify ETag == the INDEX blob's MD5.

    ADHC_DSFLOW.TO-INDEXBYTES-DEPLOY (IB-1/IB-2/IB-3). WHAT CHANGED AND WHY:

    This function used to md5 the WORKTREE file, `aws s3 cp` that same worktree file, and then
    compare the returned ETag against that same worktree md5. Every term came from one source, so
    the comparison was SELF-CONSISTENT and could not fail on the defect it was standing guard over:
    on an autocrlf checkout the worktree carries CRLF while the recorded blob is LF, and the gate
    served the CRs and reported MATCH. MEASURED on a scratch key before this change, subject
    .tools/git_bash_resolver.py: served ETag 5e77db0a48a4602aac3d3707a88c0ae0 (the CRLF worktree,
    75 CRs) against index md5 d87543e266b74dfa8a0591098826ff8b (0 CRs) -- status MATCH.

    Now: the uploaded bytes ARE the index blob, and the ETag is asserted against THAT blob's md5.
    The two terms come from different places, so the assertion can fail. The worktree is read for
    ONE purpose only -- counting its CRs for the IB-3 line -- and is never served.

    Returns (status, detail):
      ("MATCH", "")
      ("LOCAL_MISSING", "")
      ("INDEX_MISSING", "<path> -- <git stderr>")
      ("UPLOAD_FAIL", stderr)
      ("SHA_MISMATCH", "key:<s3 uri> etag:<etag> index_md5:<md5>")   -> the caller REFUSES rc=2
      ("S3_ERROR", stderr)
    """
    if not local_path.exists():
        return "LOCAL_MISSING", str(local_path)

    aws_bin = _find_aws()
    if not aws_bin:
        return "UPLOAD_FAIL", "aws CLI not found in PATH (checked aws, aws.cmd, aws.exe)"

    if rel_path is None:
        try:
            rel_path = str(local_path.resolve().relative_to(WORKSPACE)).replace(os.sep, "/")
        except ValueError:
            return "INDEX_MISSING", f"{local_path} is outside the workspace; no index entry"

    index_bytes, git_err = _index_blob(rel_path)
    if index_bytes is None:
        return "INDEX_MISSING", f"{rel_path} -- git show :{rel_path} failed: {git_err}"
    index_md5 = hashlib.md5(index_bytes).hexdigest()

    # IB-3: the divergence is PRINTED on every deployed file, and never served.
    worktree_crs = local_path.read_bytes().count(b"\r")
    index_crs = index_bytes.count(b"\r")
    print(f"           worktree CR count {worktree_crs} / index CR count {index_crs} / uploaded: index")

    env = _aws_env()

    # Upload the INDEX bytes. Written to a temp file because `aws s3 cp` takes a path, not stdin;
    # the temp file is the transport, never the source of truth.
    tmp = tempfile.NamedTemporaryFile(prefix="safedeploy-index-", suffix=pathlib.Path(rel_path).suffix,
                                      delete=False)
    try:
        tmp.write(index_bytes)
        tmp.close()
        cp_result = subprocess.run(
            [aws_bin, "s3", "cp", tmp.name, f"s3://{bucket}/{s3_key}"],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60, env=env,
        )
    finally:
        with contextlib.suppress(OSError):
            os.unlink(tmp.name)
    if cp_result.returncode != 0:
        return "UPLOAD_FAIL", cp_result.stderr.strip()

    ho_result = subprocess.run(
        [aws_bin, "s3api", "head-object",
         "--bucket", bucket, "--key", s3_key,
         "--query", "ETag", "--output", "text"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=15, env=env,
    )
    if ho_result.returncode != 0:
        return "S3_ERROR", ho_result.stderr.strip()

    s3_etag = ho_result.stdout.strip().strip('"')
    if index_md5 == s3_etag:
        return "MATCH", ""
    # IB-2: all THREE values, because a mismatch is only actionable if the reader can see which
    # side moved -- the key, what S3 holds, and what the record says it should hold.
    return "SHA_MISMATCH", (f"key:s3://{bucket}/{s3_key} etag:{s3_etag} index_md5:{index_md5}")


# ---------------------------------------------------------------------------
# X-iii hash-stamped bundles -- packaging INSIDE the deploy flow (CTO cond. 1).
# ---------------------------------------------------------------------------

def find_bundle(name: str) -> Optional[tuple[str, str, dict]]:
    """Resolve a bundle by name across trees -> (tree_label, name, bundle)."""
    for tree in CODE_TREES.values():
        b = tree.get("bundles", {}).get(name)
        if b is not None:
            return tree["label"], name, b
    return None


def bundle_for_member(rel_path: str) -> Optional[tuple[str, str, dict]]:
    """(tree_label, bundle_name, bundle) when rel_path is a member authority."""
    norm = rel_path.replace("\\", "/")
    for tree in CODE_TREES.values():
        for bname, b in tree.get("bundles", {}).items():
            if any(m["repo_path"] == norm for m in b["members"].values()):
                return tree["label"], bname, b
    return None


def second_targets_for(rel_path: str) -> list[tuple[str, str]]:
    """Declared (bucket, key) second deploy targets for a source file (CPR-5)."""
    norm = rel_path.replace("\\", "/")
    out: list[tuple[str, str]] = []
    for tree in CODE_TREES.values():
        for src, targets in tree.get("second_targets", {}).items():
            if src == norm:
                out.extend(tuple(t) for t in targets)
    return out


def build_bundle_payload(b: dict) -> tuple[Optional[bytes], dict, str]:
    """Deterministic tar.gz of the bundle members -> (payload, shas, err).

    Deterministic on purpose: sorted member order, zeroed mtime/uid/gid, gzip
    mtime=0 -- identical member bytes yield an identical archive, so a re-mint
    with no content change is a byte-identical idempotent overwrite (and the
    S3 ETag is a stable content address, not a timestamp lottery)."""
    import gzip
    import io
    import tarfile

    shas: dict[str, str] = {}
    raw = io.BytesIO()
    with tarfile.open(fileobj=raw, mode="w", format=tarfile.GNU_FORMAT) as tar:
        for member_name in sorted(b["members"]):
            spec = b["members"][member_name]
            src = WORKSPACE / spec["repo_path"].replace("/", os.sep)
            if not src.exists():
                return None, {}, f"member authority missing: {spec['repo_path']}"
            data = src.read_bytes()
            shas[spec["sha_metadata_key"]] = hashlib.sha256(data).hexdigest()
            info = tarfile.TarInfo(name=member_name)
            info.size = len(data)
            info.mtime = 0
            info.uid = info.gid = 0
            info.uname = info.gname = ""
            tar.addfile(info, io.BytesIO(data))
    gz = io.BytesIO()
    with gzip.GzipFile(fileobj=gz, mode="wb", mtime=0) as fh:
        fh.write(raw.getvalue())
    return gz.getvalue(), shas, ""


def mint_bundle(label: str, bname: str, b: dict) -> tuple[str, str, dict]:
    """Build + upload + verify the bundle. Returns (status, detail, shas).

    Statuses reuse deploy_file's vocabulary. Verification is two-legged:
    ETag == local md5 (bytes landed) AND the sha metadata echoed back on
    head-object (the stamp landed) -- an upload whose metadata was dropped is
    a FAIL even with matching bytes."""
    import tempfile

    payload, shas, err = build_bundle_payload(b)
    if payload is None:
        return "LOCAL_MISSING", err, {}
    aws_bin = _find_aws()
    if not aws_bin:
        return "UPLOAD_FAIL", "aws CLI not found in PATH", shas

    metadata = dict(shas)
    metadata["source-repo-paths"] = ";".join(
        sorted(m["repo_path"] for m in b["members"].values())
    )
    local_md5 = hashlib.md5(payload).hexdigest()
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="safe_deploy_bundle_"))
    local = tmp / pathlib.PurePosixPath(b["s3_key"]).name
    local.write_bytes(payload)

    env = _aws_env()
    meta_arg = ",".join(f"{k}={v}" for k, v in sorted(metadata.items()))
    cp = subprocess.run(
        [aws_bin, "s3", "cp", str(local), f"s3://{b['bucket']}/{b['s3_key']}",
         "--metadata", meta_arg],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120, env=env,
    )
    if cp.returncode != 0:
        return "UPLOAD_FAIL", cp.stderr.strip(), shas

    ho = subprocess.run(
        [aws_bin, "s3api", "head-object", "--bucket", b["bucket"],
         "--key", b["s3_key"], "--output", "json"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30, env=env,
    )
    if ho.returncode != 0:
        return "S3_ERROR", ho.stderr.strip(), shas
    try:
        head = json.loads(ho.stdout)
    except ValueError as exc:
        return "S3_ERROR", f"head-object unparseable: {exc}", shas
    etag = str(head.get("ETag", "")).strip('"')
    if etag != local_md5:
        return "SHA_MISMATCH", f"local:{local_md5} s3:{etag}", shas
    echoed = head.get("Metadata", {})
    missing = [k for k in metadata if k not in echoed or echoed[k] != metadata[k]]
    if missing:
        return "SHA_MISMATCH", f"metadata stamp(s) absent/wrong on S3: {missing}", shas
    return "MATCH", f"md5={local_md5}", shas


def _find_pipeline_cli() -> Optional[str]:
    """Locate pipeline_cli.py -- the engine BEHIND the extensionless `comp-pipescript` bash
    wrapper (the wrapper just runs `python org/modules/graph/pipeline_cli.py "$@"`).

    We target the Python entry, NOT the wrapper, on purpose: subprocess-exec of the
    extensionless bash wrapper raises OSError WinError 193 ("%1 is not a valid Win32
    application") on Windows -- the S3 cp already SUCCEEDED, so the verify step silently
    crashes and the deploy reads GREEN while UNVERIFIED (latent false-green; CTO 20260701T1511Z,
    surfaced by DS~A on the ADVI_TAGATTR leg-2 bd deploy). Invoking the Python entry directly via
    sys.executable is the ratified cross-platform pattern (harness.py/kuzu_cli, commit 572a5d9b8:
    "no bash hop -- the WSL /bin/bash relay is broken from Windows-python")."""
    candidate = WORKSPACE / "org" / "modules" / "graph" / "pipeline_cli.py"
    if candidate.exists():
        return str(candidate)
    # PATH fallback via the wrapper's location (git hooks don't source bashrc), resolving the
    # sibling engine relative to a discovered wrapper if the canonical path ever moves.
    wrapper = shutil.which("comp-pipescript")
    if wrapper:
        sib = pathlib.Path(wrapper).resolve().parent.parent / "org" / "modules" / "graph" / "pipeline_cli.py"
        if sib.exists():
            return str(sib)
    return None


def _pipescript_output_ok(output: str) -> bool:
    """Parse a `comp-pipescript deployed <script>` result: True = clean, False = STALE/MISSING.

    Reads the 'Summary: N MATCH, N STALE, N MISSING_ON_S3, ...' COUNTS -- NOT a bare substring.
    The summary line literally contains the tokens 'STALE'/'MISSING_ON_S3' even at count 0, so the
    old `"STALE" in output` test FALSE-FAILED every COMPLETED run (it only ever "passed" because
    the check never completed on Windows -- WinError-193 crash, then big-layer timeout; the
    scope-to-changed-script fix (b) makes it complete reliably and surfaced this). Failure semantics
    are unchanged from the original intent: STALE or MISSING_ON_S3 => fail. Falls back to a per-line
    status scan when no summary line is present (no '0 STALE' summary to confuse it there)."""
    m = re.search(r"Summary:\s*([^\n]+)", output)
    if m:
        counts = {tok: int(n) for n, tok in re.findall(r"(\d+)\s+([A-Z0-9_-]+)", m.group(1))}
        return counts.get("STALE", 0) == 0 and counts.get("MISSING_ON_S3", 0) == 0
    return not re.search(r"\b(STALE|MISSING_ON_S3)\b", output)


def run_pipescript_verify(rel_path: str) -> tuple[bool, str]:
    """Run `comp-pipescript deployed <rel_path>` (via its pipeline_cli.py engine) for ONE
    just-deployed script; return (match, output).

    Scoped to the CHANGED script, not the whole label-layer (CTO ruling (b) 20260701T1735Z): the
    deploy-verify's job is "did THIS deploy's scripts land", so we verify exactly what was PUSHED.
    A repo-relative `data/<tree>/scripts/...` path auto-detects the firm/tree in pipeline_cli's
    scope-resolution and checks ONLY that script against its own bucket. This (a) scales with the
    deploy size (1-few scripts -> seconds), so it NEVER times out on a big layer, and (b) removes
    the fail-open-WARN-on-timeout soft-no-op -- a completing per-script check FAILS LOUD on
    STALE/MISSING. Estate-wide drift (are UNCHANGED scripts current?) is a different job =
    comp-pipescript's no-arg sweep, NOT the deploy-verify's.

    Treats STALE or MISSING_ON_S3 in output as failure.
    Invoked as [sys.executable, pipeline_cli.py, ...] rather than the extensionless bash wrapper so
    the verify actually EXECUTES on Windows (the WinError-193 gate-hole fix -- see _find_pipeline_cli).
    If the engine is unreachable, warns and returns True (MD5 verify already passed).
    """
    cli = _find_pipeline_cli()
    if not cli:
        return True, "WARN: pipeline_cli.py not found; skipping pipescript verify (MD5 verify passed)"

    env = _aws_env()
    try:
        result = subprocess.run(
            [sys.executable, cli, "deployed", rel_path],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120, env=env,
        )
    except subprocess.TimeoutExpired:
        return True, f"WARN: pipescript verify {rel_path} timed out; skipping (MD5 passed)"
    output = result.stdout + result.stderr
    return _pipescript_output_ok(output), output


def write_bypass_audit(
    author: str,
    files: list[str],
    commit_sha: str,
    reason: str,
    kind: str = "ALLOW-STALE",
) -> None:
    """Append an audit line. `kind` tags the row: ALLOW-STALE (the --allow-stale
    bypass, default -- unchanged) or SERVE-RELEASE (a gated serve-hold removal)."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    BYPASS_AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    detail = ",".join(files[:5])
    if len(files) > 5:
        detail += f"...+{len(files) - 5}"
    entry = (
        f"{ts} {kind}  {author}  {len(files)}  ({detail})"
        f"  sha:{commit_sha}  reason:{reason}\n"
    )
    with open(BYPASS_AUDIT_LOG, "a", encoding="utf-8") as fh:
        fh.write(entry)


# ---------------------------------------------------------------------------
# Phase-1 serve-gate helpers. Every function here FAILS CLOSED: a read/git error
# is reported as "held" (skip, safe) or "undetermined -> refuse" (block, safe),
# never silently treated as clear-to-serve.
# ---------------------------------------------------------------------------

def _git_env() -> dict[str, str]:
    """Env for git subprocesses. MSYS_NO_PATHCONV=1 keeps a `<ref>:<path>` arg and
    a `-- <path>` pathspec from being mangled by the Git-for-Windows path rewriter
    (CLAUDE.md Git note); harmless where no path arg is present."""
    env = os.environ.copy()
    env["MSYS_NO_PATHCONV"] = "1"
    return env


def _text_has_serve_held(text: str) -> bool:
    """True if any line of `text` is a DEPLOY-SERVE-HELD sentinel."""
    for line in text.splitlines():
        if SERVE_HELD_RE.match(line):
            return True
    return False


def _serve_held_reason(rel_path: str) -> Optional[str]:
    """Feature 1. Return the hold reason if the CURRENT (working-tree) content of
    `rel_path` -- the exact bytes deploy_file would upload -- carries a SERVE-HELD
    sentinel, else None (clear to serve).

    FAIL CLOSED: an unreadable candidate is treated as HELD (returns a reason), so
    it is skipped/reported, never silently served.
    """
    local_path = WORKSPACE / rel_path.replace("/", os.sep)
    try:
        text = local_path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:  # unreadable -> held (safe)
        return f"READ-ERROR treated-as-held ({exc})"
    for line in text.splitlines():
        m = SERVE_HELD_RE.match(line)
        if m:
            return m.group(1).strip() or "(no reason given)"
    return None


def _old_blob_has_serve_held(old_ref: str, rel_path: str) -> tuple[Optional[bool], str]:
    """Feature 2 half A. Did `old_ref`'s version of `rel_path` carry the sentinel?

    Returns (had_sentinel, detail):
      (True,  "")            old blob had the sentinel
      (False, "absent-in-old") file did not exist at old_ref -> a NEW file, not a removal
      (False, "")            old blob determinably did NOT carry it
      (None,  <error>)       UNDETERMINED -> caller MUST fail-closed (refuse)
    """
    ref_arg = f"{old_ref}:{rel_path}"
    try:
        r = subprocess.run(
            ["git", "show", ref_arg],
            capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(WORKSPACE), timeout=30,
            env=_git_env(),
        )
    except Exception as exc:  # git unavailable / timeout -> undetermined -> refuse
        return None, f"git show {ref_arg} failed: {exc}"
    if r.returncode != 0:
        stderr = (r.stderr or "").lower()
        # A path missing from old_ref is a NEW file, not a serve-hold removal.
        if "does not exist in" in stderr or "exists on disk" in stderr:
            return False, "absent-in-old"
        # Anything else (bad ref, corrupt object, ...) is undetermined -> refuse.
        return None, (r.stderr or "").strip() or f"git show rc={r.returncode}"
    return _text_has_serve_held(r.stdout), ""


def _find_serve_release_ack(old_ref: str, new_ref: str) -> tuple[bool, str, Optional[str]]:
    """Feature 2 half B. Scan commit messages in old_ref..new_ref for a
    `SERVE-RELEASE-ACK: <reason>` line.

    Returns (present, reason, error). error non-None => the log could not be read
    -> caller MUST fail-closed (treat as NO ack -> refuse).
    """
    rng = f"{old_ref}..{new_ref}"
    try:
        r = subprocess.run(
            ["git", "log", rng, "--format=%B"],
            capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(WORKSPACE), timeout=30,
            env=_git_env(),
        )
    except Exception as exc:
        return False, "", f"git log {rng} failed: {exc}"
    if r.returncode != 0:
        return False, "", (r.stderr or "").strip() or f"git log rc={r.returncode}"
    m = SERVE_RELEASE_ACK_RE.search(r.stdout)
    if m:
        return True, m.group(1).strip(), None
    return False, "", None


def _file_author(range_expr: str, rel_path: str) -> str:
    """Feature 3. Last author to touch `rel_path` within `range_expr`. Informational
    (transparency), so it FAILS SOFT to 'unknown' -- an author-lookup miss must never
    block a legitimate deploy."""
    try:
        r = subprocess.run(
            ["git", "log", range_expr, "--format=%an", "-1", "--", rel_path],
            capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(WORKSPACE), timeout=15,
            env=_git_env(),
        )
        if r.returncode == 0:
            lines = [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]
            if lines:
                return lines[0]
    except Exception:
        pass
    return "unknown"


def _resolve_serve_refs(
    commit_range: Optional[str], explicit_files: Optional[list[str]]
) -> tuple[str, str, bool]:
    """Resolve (old_ref, new_ref, is_new_branch) for the serve-release removal gate.

    is_new_branch True => there is no comparable old version (new-branch push,
    remote sha 0000...) => the gate is skipped (spec: not a removal).
    """
    if commit_range and ".." in commit_range:
        parts = commit_range.split("..")
        old = parts[0].strip()
        new = (parts[1].strip() if len(parts) > 1 else "") or "HEAD"
        if not old or old.startswith("0000000"):
            return "", new, True
        return old, new, False
    # No range (explicit files or bare invocation): mirror detect_script_files' default.
    return "HEAD~1", "HEAD", False


def _current_commit_sha() -> str:
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(WORKSPACE), timeout=10,
        )
        return r.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def main(argv: list[str]) -> int:
    import argparse

    ap = argparse.ArgumentParser(
        prog="safe-deploy",
        description="Atomic deploy: S3 cp + SHA verify + comp-pipescript confirm. ADHC_DSFLOW.005",
    )
    ap.add_argument("files", nargs="*", help="Explicit file list (repo-relative)")
    ap.add_argument("--commit-range", default=None,
                    help="git diff range, e.g. abc123..def456 (used by pre-push hook)")
    ap.add_argument("--allow-stale", action="store_true",
                    help="Skip verify; write audit entry. Use only for emergency/docstring-only changes.")
    ap.add_argument("--reason", default="",
                    help="Reason for --allow-stale bypass (required with --allow-stale)")
    ap.add_argument("--author", default="",
                    help="Agent identity for audit log (e.g. 0.4.0_DS_ClientPlatform)")
    ap.add_argument("--no-pipescript", action="store_true",
                    help="Skip comp-pipescript verify phase (upload + SHA only)")
    ap.add_argument("--mint-bundle", default=None, metavar="NAME",
                    help="Mint one declared bundle now (first-mints/re-mints run "
                         "through this same in-flow path -- Rule 13 QA-deploy, "
                         "never a side script)")

    args = ap.parse_args(argv)

    # ----- X-iii: explicit bundle mint (first mint / forced re-mint) -----
    if args.mint_bundle:
        hit = find_bundle(args.mint_bundle)
        if hit is None:
            declared = sorted(n for t in CODE_TREES.values() for n in t.get("bundles", {}))
            print(f"ERROR: no bundle named {args.mint_bundle!r} declared (declared: {declared})",
                  file=sys.stderr)
            return 2
        label, bname, b = hit
        held_members = [m["repo_path"] for m in b["members"].values()
                        if m["repo_path"].endswith(".py")
                        and _serve_held_reason(m["repo_path"]) is not None]
        if held_members:
            print(f"SERVE-HELD: bundle {bname} NOT minted -- member script(s) carry the "
                  f"sentinel: {held_members}")
            return 1
        status, detail, shas = mint_bundle(label, bname, b)
        dest = f"s3://{b['bucket']}/{b['s3_key']}"
        if status == "MATCH":
            print(f"BUNDLE MINTED  [{label}] {bname} -> {dest}  ({detail})")
            for k, v in sorted(shas.items()):
                print(f"  {k}={v}")
            return 0
        print(f"ERROR  {status}  bundle {bname} -> {dest}")
        if detail:
            print(f"         {detail}")
        return 1

    # Detect files
    files = detect_script_files(
        commit_range=args.commit_range,
        explicit_files=args.files if args.files else None,
    )
    bundle_member_files = detect_bundle_member_files(
        commit_range=args.commit_range,
        explicit_files=args.files if args.files else None,
    )

    if not files and not bundle_member_files:
        print("OK: safe-deploy -- no deploy-scope script files detected, nothing to do")
        return 0

    # Feature 3: author-enumeration notice -- make "you are about to serve
    # <someone else>'s gold" visible. Author lookup fails soft to 'unknown'
    # (transparency, not a gate); the S3 target prefix comes from file_to_s3_target
    # (scope logic untouched).
    author_range = args.commit_range or "HEAD~1..HEAD"
    # THE RECEIPT ENUMERATES THE ACTUAL UPLOAD SET, EACH LEG NAMED (CTO GO 2026-08-20T0020Z).
    # It previously printed `len(files)` and iterated `files` alone -- while :997 gates the
    # nothing-to-do exit on files OR bundle_member_files, and the bundle leg below deploys the
    # bundle members. So a change touching ONLY a bundle member printed a receipt saying
    # "0 script file(s) to deploy" and then deployed one. EXERCISED before the fix:
    #     input ['data/mdpf/config/partner_roster.json']
    #       detect_script_files   -> []   (what the receipt counted)
    #       detect_bundle_members -> [that path]  (what also deployed)
    # That is the roster-only case this leg was BUILT for -- its own docstring names the
    # an-atomic-commit-is-not-an-atomic-deploy incident -- so the one path most likely to use it
    # was the one the receipt could not see. A receipt that under-reports its own act is the
    # records-that-read-authoritative-while-wrong family: the deploy was correct, the RECORD of it
    # was not, and the record is what the next reader trusts.
    _bundle_only = [f for f in bundle_member_files if f not in files]
    _total = len(files) + len(_bundle_only)
    print(f"safe-deploy: {_total} path(s) to deploy "
          f"({len(files)} script, {len(_bundle_only)} bundle-member)")
    for f in files:
        target = file_to_s3_target(f)
        # Full destination prefix, not code/<segment>/ -- mdpf's non-standard
        # layout (code/scripts/<layer>/) truncated wrong under the old split.
        dest = target[1].rsplit("/", 1)[0] + "/" if target else "?"
        author = _file_author(author_range, f)
        print(f"  [script]        {f}  (authored by {author}) -> {dest}")
    for f in _bundle_only:
        # No file_to_s3_target: a bundle member's destination is the BUNDLE's, resolved at the
        # mint below. Naming the leg honestly beats printing a '?' destination that reads as a
        # broken lookup rather than a different mechanism.
        author = _file_author(author_range, f)
        print(f"  [bundle-member] {f}  (authored by {author}) -> bundle mint (leg below)")
    print()

    # --allow-stale bypass (unchanged: no S3 upload happens, so nothing SERVES;
    # the serve-gate below governs the actual deploy path, not this bypass).
    if args.allow_stale:
        if not args.reason:
            print("ERROR: --allow-stale requires --reason", file=sys.stderr)
            return 2
        sha = _current_commit_sha()
        write_bypass_audit(args.author or "UNKNOWN", files, sha, args.reason)
        print(f"WARN: --allow-stale bypass active; {len(files)} file(s) NOT deployed to S3")
        print(f"  Audit: {BYPASS_AUDIT_LOG}")
        print(f"  Reason: {args.reason}")
        return 0

    # ----- Feature 1: SERVE-HELD sentinel -- skip held files (fail closed) -----
    # A deploy-scope file whose CURRENT content carries `# DEPLOY-SERVE-HELD` is a
    # deliberate hold: it is NOT uploaded and NOT an error, but IS reported loud.
    to_deploy: list[str] = []
    held: list[tuple[str, str]] = []
    for f in files:
        reason = _serve_held_reason(f)   # unreadable -> treated as held (safe)
        if reason is None:
            to_deploy.append(f)
        else:
            held.append((f, reason))
    for f, reason in held:
        print(
            f"SERVE-HELD: {f} -- committed but NOT served (reason: {reason}); "
            "remove the sentinel to serve."
        )
    if held:
        print()

    # ----- Feature 2: gated sentinel-removal (removing a hold = authorizing serve) -----
    # For each file that will deploy (current content lacks the sentinel), if its
    # OLD (old_ref) version HAD the sentinel, this push is REMOVING the serve-hold.
    # Refuse the whole push unless a commit in the range carries SERVE-RELEASE-ACK.
    old_ref, new_ref, is_new_branch = _resolve_serve_refs(
        args.commit_range, args.files if args.files else None
    )
    if not is_new_branch:
        removed: list[str] = []
        for f in to_deploy:
            had, detail = _old_blob_has_serve_held(old_ref, f)
            if had is None:   # UNDETERMINED -> fail closed
                print(
                    f"BLOCKED: safe-deploy serve-release check could not evaluate {f} "
                    f"(old_ref={old_ref}): {detail}"
                )
                print("  (fail-closed: refusing the deploy; removal check incomplete)")
                return 1
            if had:
                removed.append(f)
        if removed:
            present, ack_reason, ack_err = _find_serve_release_ack(old_ref, new_ref)
            if ack_err is not None:   # log unreadable -> fail closed
                print(
                    "BLOCKED: safe-deploy serve-release ACK scan could not read the "
                    f"commit log ({old_ref}..{new_ref}): {ack_err}"
                )
                print("  (fail-closed: refusing the deploy)")
                return 1
            lst = ", ".join(removed)
            if not present:
                print(
                    f"SERVE-RELEASE BLOCKED: this push removes the serve-hold on "
                    f"{len(removed)} file(s): {lst}. They WILL serve. Add "
                    '"SERVE-RELEASE-ACK: <reason>" to a commit in this push to '
                    "authorize (tied to NEVER#2 never-widen)."
                )
                return 1
            # Authorized: record the release + reason + files, then let them deploy.
            sha = _current_commit_sha()
            write_bypass_audit(
                args.author or "UNKNOWN", removed, sha, ack_reason, kind="SERVE-RELEASE"
            )
            print(
                f"OK: SERVE-RELEASE authorized -- serve-hold removed on {len(removed)} "
                f"file(s): {lst} (reason: {ack_reason})"
            )
            print(f"  Audit: {BYPASS_AUDIT_LOG}")
            print()

    if not to_deploy:
        print("OK: safe-deploy -- all deploy-scope file(s) are SERVE-HELD; nothing served.")
        return 0

    # ----- X-iii bundle routing: member commits mint the bundle, never the loose leg -----
    # A member SCRIPT exits the per-file loop here (its loose S3 objects are
    # frozen-in-place as the rollback target); a member CONFIG (roster json)
    # only ever arrives via detect_bundle_member_files. Each triggered bundle
    # mints ONCE per push regardless of how many members changed.
    triggered: dict[str, tuple[str, dict]] = {}
    loose: list[str] = []
    for rel_path in to_deploy:
        hit = bundle_for_member(rel_path)
        if hit is not None:
            label, bname, b = hit
            triggered[bname] = (label, b)
            print(f"BUNDLE-ROUTED: {rel_path} -> bundle {bname} "
                  f"(loose leg frozen 2026-08-11, X-iii)")
        else:
            loose.append(rel_path)
    for rel_path in bundle_member_files:
        if rel_path in to_deploy:
            continue   # script member already routed above
        hit = bundle_for_member(rel_path)
        if hit is not None:
            label, bname, b = hit
            held_members = [m["repo_path"] for m in b["members"].values()
                            if m["repo_path"].endswith(".py")
                            and _serve_held_reason(m["repo_path"]) is not None]
            if held_members:
                print(f"SERVE-HELD: bundle {bname} NOT minted (config member {rel_path} "
                      f"changed, but member script(s) hold the sentinel: {held_members})")
                continue
            triggered[bname] = (label, b)
            print(f"BUNDLE-ROUTED: {rel_path} (config member) -> bundle {bname}")
    to_deploy = loose
    if triggered:
        print()

    # Deploy phase: upload all NON-HELD files, fail fast on any error
    deployed: list[tuple[str, str, str]] = []   # (rel_path, bucket, s3_key)
    # SKIP-NOT-MEMBER audit (1.0.0_SA_CTO~Z arch-gate, 2026-08-27). Recorded because the
    # final summary line used to be UNCONDITIONAL: when every path skipped, `deployed` was
    # empty, the verify loop ran zero times, and the gate printed "all files deployed and
    # verified" -- a universal quantified over an EMPTY SET, which is vacuously true and
    # reads as "they all shipped". Measured TWICE the same day on the same two files, the
    # second time PREDICTED IN ADVANCE by 0.0.0_AB_MSTR~Z and then observed, so it is
    # reproducible and fires on EVERY all-skipped push. The integrator nearly reported a
    # deploy that did not happen. The SKIP is correct (Rule 13: 404 = loud skip, first-mints
    # explicit); the SENTENCE was the defect.
    skipped_not_member: list[str] = []
    failed = False
    etag_refusal = False   # IB-2: S3 holds a byte the record does not carry -- rc=2, not rc=1

    for bname, (label, b) in sorted(triggered.items()):
        status, detail, shas = mint_bundle(label, bname, b)
        dest = f"s3://{b['bucket']}/{b['s3_key']}"
        if status == "MATCH":
            print(f"  BUNDLE MINTED  [{label}] {bname} -> {dest}  ({detail})")
            for k, v in sorted(shas.items()):
                print(f"    {k}={v}")
        else:
            print(f"  ERROR  {status}  bundle {bname} -> {dest}")
            if detail:
                print(f"           {detail}")
            failed = True
            break

    for rel_path in to_deploy:
        if failed:
            break
        target = file_to_s3_target(rel_path)
        if target is None:
            continue
        bucket, s3_key, label = target
        tag = f"[{label}] {rel_path}"

        # SHARED-HOME MEMBERSHIP GUARD (Andrew-direct flip 2026-08-04; CTO riders
        # 185213Z). A shared repo home serves MULTIPLE destinations and only a
        # subset belongs to this tree -- the S3 side is the authority on
        # membership: key-exists = an UPDATE (deploy enforced); 404 = not a
        # member (skip LOUD, printing the exact probed key + the prefix
        # denominator so the skip is auditable against what it actually probed);
        # any other probe outcome = UNDETERMINED (fail closed -- an unreachable
        # S3 is not a 404). First-mints of a NEW shared-home script stay an
        # explicit manual step. Membership keys on S3-KEY-EXISTENCE, never local
        # path, so a repo-home migration (CANRTE W-4 class) needs no edit here.
        rtl = resolve_tree_layer(rel_path)
        if rtl is not None:
            _name, tree, layer = rtl
            if layer in tree.get("shared_repo_homes", set()):
                exists, err = s3_key_exists(bucket, s3_key)
                if exists is None:
                    print(f"  ERROR  MEMBERSHIP_PROBE_FAILED  {tag}")
                    print(f"           s3://{bucket}/{s3_key}: {err}")
                    failed = True
                    break
                if exists is False:
                    prefix = s3_key.rsplit("/", 1)[0] + "/"
                    n = s3_prefix_keycount(bucket, prefix)
                    print(f"  SKIP-NOT-MEMBER  {tag}")
                    print(f"           probed s3://{bucket}/{s3_key} -> 404; "
                          f"prefix {prefix} carries {n} member(s) (single page). "
                          f"A NEW shared-home script first-mints explicitly, "
                          f"never via the push gate.")
                    skipped_not_member.append(rel_path)
                    continue

        local_path = WORKSPACE / rel_path.replace("/", os.sep)
        status, detail = deploy_file(local_path, bucket, s3_key, rel_path)
        if status == "SHA_MISMATCH":
            etag_refusal = True
        if status == "MATCH":
            print(f"  DEPLOYED  {tag}")
            deployed.append((rel_path, bucket, s3_key))
        else:
            print(f"  ERROR  {status}  {tag}")
            if detail:
                print(f"           {detail}")
            failed = True
            break   # fail fast; don't leave partial state

        # ----- CPR-5 second deploy targets: the declared fan-out for a ONE-source
        # shared engine (Model B). Membership-guard semantics at TARGET grain:
        # key-exists = update enforced; 404 = LOUD skip (a vanished second home is
        # never re-minted silently into another firm's bucket); UNDETERMINED =
        # fail closed. Second targets are deliberately NOT appended to `deployed`
        # -- comp-pipescript does not model the second home (instrument note in
        # the declaration) and the ETag verify here is their acceptance.
        for st_bucket, st_key in second_targets_for(rel_path):
            st_tag = f"[{label}->2nd] {rel_path} -> s3://{st_bucket}/{st_key}"
            exists, err = s3_key_exists(st_bucket, st_key)
            if exists is None:
                print(f"  ERROR  SECOND_TARGET_PROBE_FAILED  {st_tag}")
                print(f"           {err}")
                failed = True
                break
            if exists is False:
                print(f"  SKIP-SECOND-TARGET-ABSENT  {st_tag}")
                print("           declared second target key does not exist -- first-mints "
                      "are explicit, never via the push gate. Surface to the owner.")
                continue
            st_status, st_detail = deploy_file(local_path, st_bucket, st_key, rel_path)
            if st_status == "SHA_MISMATCH":
                etag_refusal = True
            if st_status == "MATCH":
                print(f"  DEPLOYED-SECOND-TARGET  {st_tag}")
            else:
                print(f"  ERROR  {st_status}  {st_tag}")
                if st_detail:
                    print(f"           {st_detail}")
                failed = True
                break
        if failed:
            break

    if failed:
        print()
        if etag_refusal:
            # IB-2: a served byte the RECORD does not carry is a distinct verdict from a transport
            # failure, and it must never share an rc with one. rc=2 says: something is on S3 that
            # git does not have; do not close the ledger on it.
            print("REFUSED (rc=2): safe-deploy read-back does NOT match the index blob.")
            print("  The three values are printed above: the key, the ETag S3 returned, and the")
            print("  md5 of the bytes git has RECORDED. S3 holds something the record does not.")
            print("  LEDGER: leave the org/critical_paths/change_management/ entry OPEN. This is")
            print("  not a transport error to retry -- re-running uploads the same index bytes and")
            print("  will refuse again until the divergence is explained.")
            return 2
        print("ERROR: safe-deploy gate FAILED -- S3 deploy or SHA verify error")
        print("  Partial deploy state: files listed above as DEPLOYED may already be on S3.")
        print("  Fix the error and re-run; the gate is idempotent.")
        return 1

    print()

    if not args.no_pipescript:
        # comp-pipescript verify phase: per CHANGED SCRIPT (CTO ruling (b) 20260701T1735Z).
        # Iterate `deployed` -- the exact set of scripts that landed on S3 this run -- and verify
        # each individually. Verifying what THIS deploy pushed (not the whole label-layer) scopes
        # the check to the deploy size, so it completes in seconds and never times out on a big
        # layer, and it fails LOUD on STALE/MISSING instead of soft-no-op-on-timeout.
        verify_ok = True
        for rel_path, _bucket, _s3_key in deployed:
            ok, output = run_pipescript_verify(rel_path)
            if ok:
                print(f"  VERIFY OK  comp-pipescript deployed {rel_path}")
            else:
                print(f"  VERIFY FAIL  comp-pipescript deployed {rel_path}")
                print(output[:800])
                verify_ok = False

        if not verify_ok:
            print()
            print("ERROR: safe-deploy gate FAILED -- comp-pipescript STALE/MISSING after upload")
            return 1

    # THE SUMMARY STATES ITS DENOMINATOR AND NEVER QUANTIFIES OVER AN EMPTY SET.
    # rc is UNCHANGED in every branch: an all-skip is still a PASS (the guard did its job and
    # the push is legitimate) -- what changes is that the line can no longer be read as
    # evidence of a deploy. A gate that reports what it DID cannot be misquoted as reporting
    # what it did not.
    # STOP: KEYED ON THE OUTCOME (`n_dep`), NEVER ON THE ENUMERATED CAUSES.
    # CORRECTED 2026-08-27 by 1.0.0_SA_CTO~Z on 0.4.0_DS_ClientPlatform~W, who read this fix at
    # SOURCE rather than trusting the author's claim that it worked. The first version gated on
    # `n_skip` -- the ONE skip reason just instrumented -- so a run depositing nothing for any
    # other reason still printed "all 0 file(s) deployed and verified": the same vacuous
    # universal, one bucket over.
    #
    # STOP: THE JUSTIFICATION I FIRST COMMITTED OVERCLAIMED, AND THE CORRECTION MATTERS MORE THAN
    # THE CODE. I named three "reachable" paths to the zero-deploy branch. ALL THREE ARE NOT:
    #   SERVE-HELD family ......... FALSE. :1120 `if not to_deploy: ... return 0` returns EARLY
    #                               with its own honest sentence and never reaches this summary.
    #                               (0.4.0_DS_ClientPlatform~W found and retracted this themselves.)
    #   `target is None` (:1192) .. LATENT. detect_script_files() admits only paths where
    #                               file_to_s3_target(f) is not None, and that function is pure,
    #                               so re-evaluating it here cannot return None. Defensive code.
    #   SKIP-SECOND-TARGET (:1255)  CANNOT produce n_dep == 0 ALONE: the second-target loop
    #                               (:1246) sits INSIDE the deploy loop AFTER the primary
    #                               deployed.append (:1231), so reaching it means that file
    #                               already deployed.
    # >> SO THE n_dep == 0 / n_skip == 0 BRANCH IS UNREACHABLE UNDER TODAY'S CONFIG. It is
    #    DEFENSIVE, not a live-defect fix, and saying otherwise would have had a successor hunt
    #    three live paths that do not exist. The LIVE defect was the SKIP-NOT-MEMBER all-skip,
    #    measured TWICE and predicted-then-observed by 0.0.0_AB_MSTR~Z; that one is real. <<
    # The structure still stands on its own merits: `n_dep == 0` is correct BY CONSTRUCTION rather
    # than by an enumeration that happens to be complete today, and it stays correct the moment
    # anything builds `to_deploy` by a route that bypasses detect_script_files. Enumerating skip
    # reasons is the six-sites-when-there-are-eight error.
    n_dep, n_skip = len(deployed), len(skipped_not_member)
    if not n_dep:
        detail = f"; {n_skip} SKIPPED (first-mint, 404)" if n_skip else ""
        print(f"OK: safe-deploy gate PASS -- 0 file(s) deployed{detail}. NOTHING WAS DEPLOYED.")
        print("     This line is NOT evidence of a deploy. A first-mint is an EXPLICIT act in the")
        print("     owning lane, never this gate. Measure the artifact, not this sentence.")
        for rel in skipped_not_member:
            print(f"       NOT DEPLOYED  {rel}")
    elif n_skip:
        print(f"OK: safe-deploy gate PASS -- {n_dep} deployed and verified; "
              f"{n_skip} SKIPPED (first-mint, 404), listed above and NOT deployed.")
    else:
        print(f"OK: safe-deploy gate PASS -- all {n_dep} file(s) deployed and verified")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
