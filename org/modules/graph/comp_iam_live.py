#!/usr/bin/env python3
"""comp-iam LIVE-PRIMARY plane: the real estate is the population; Terraform is an overlay.

Andrew-direct 2026-07-22: "Instead of keying off terraform resources as primary, it keys off the real
state as primary, which should all be discoverable via kuzu anyway."

WHY THE FLIP IS CORRECT -- and it is a stronger reason than "the terraform doesn't exist yet"
------------------------------------------------------------------------------------------------
comp-iam's DESIRED->APPLIED join is exact string equality on RoleName. Terraform source is a TEMPLATE:
names, ARNs and ids are resolved at APPLY time. So `iam_cli` holds a parsed role literally named

    opal-assets-silver-${each.key}-role

-- one template row that can never equal any of the six real roles it produces. THE UNJOINABLE CLASS
IS NOT A PARSER GAP; IT IS A CATEGORY ERROR. A template has no name, so it cannot be joined by name,
and no amount of better parsing fixes that. Keying off live state is not merely "more logical": it is
the only plane on which identifiers are actually identifiers.

FEDERATE, DO NOT BUILD
----------------------
The live-vs-declared reconciliation ALREADY EXISTS and is already correct. `comp-aws derive` is
0.7.0's certed live-boto3 + TF reconciler (oracle-scored), and `infra/aws/globgrph/fedobs/
fedobs_emit.py:200-218` states the principle verbatim: "FEDERATE-NOT-BUILD ... this adapter READS its
derive JSON only, never calls AWS itself." Its output is what kuzu's `drift_class` is built from.

Crucially, the derive joins on ARN IDENTITY and carries the TF ADDRESS as provenance
(`tf_module` / `tf_resource` / `tf_type`), not the rendered name -- which is exactly why it gets the
interpolated fleet right where comp-iam and a literal grep both got it wrong. Verified 2026-07-22:
all six opal-assets-silver-* roles and all three opal-*-served-guard roles come back DECLARED with a
real tf_resource address.

So this module does NOT re-derive drift. It CONSUMES the certed derive, applies the vintage discipline
the derive artifact lacks, and reports live-primary with stated denominators.

THE VINTAGE PROBLEM IS NOT SOLVED BY THE FLIP -- IT MOVES
---------------------------------------------------------
The derive artifact is a file on disk with no self-declared vintage, exactly like the 2026-06-03
census. Measured 2026-07-22: the on-disk IAM derive reported live=183 while a fresh
get-account-authorization-details returned 205. Twenty-two live roles had appeared since it was
written, and nothing in the artifact says so.

    A LIVE-PRIMARY TOOL READING A STALE SNAPSHOT OF "LIVE" IS NOT LIVE-PRIMARY. It is
    Terraform-primary's failure mode wearing the other plane's clothes -- and it fails in the
    same direction, reporting a smaller population than exists, so MISSING reads as ABSENT.

Hence: the same fail-closed gate built for the census applies here, keyed on the derive's own mtime
(the honest observed_at that fedobs already uses) and cross-checked against a fresh census population
when one is supplied. A population delta is reported as a STALENESS finding, not silently absorbed.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
WORKSPACE = _HERE.parent.parent.parent

# Where comp-aws derive writes, and where fedobs reads it from. Same default, same env override --
# if these ever diverge, the two tools are reading different estates and neither would say so.
DERIVE_DIR = Path(os.environ.get("FEDOBS_LIVE_AWS_DERIVE_DIR",
                                 str(WORKSPACE / ".fedobs_tmp" / "live_aws")))

DEFAULT_DERIVE_TTL_HOURS = 24


def load_iam_derive(derive_dir: Path | None = None):
    """Load comp-aws derive's IAM class. Returns (payload, path, observed_at) or (None, path, None).

    observed_at is the FILE MTIME, which is what fedobs_emit calls the "honest vintage -- when the
    observer actually saw the estate". Using mtime is legitimate HERE and illegitimate for the census:
    the derive artifact has no internal stamp and mtime is the only observation time available, so it
    is a declared best-effort; the census DOES stamp itself at read time, so falling back to mtime
    there would replace a real measurement with a proxy. Different artifacts, different honest answer.
    """
    ddir = derive_dir or DERIVE_DIR
    path = ddir / "comp_aws_derive_iam.json"
    if not path.exists():
        return None, path, None
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None, path, None
    iam = ((doc.get("classes_data") or {}).get("iam")) or None
    if iam is None:
        return None, path, None
    observed = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    iam = dict(iam)
    iam["_account"] = ((doc.get("meta") or {}).get("account"))
    return iam, path, observed


def derive_age_hours(observed_at, now=None) -> float | None:
    if observed_at is None:
        return None
    return ((now or datetime.now(timezone.utc)) - observed_at).total_seconds() / 3600.0


def population_delta(derive_iam: dict, census: dict | None):
    """Cross-check the derive's live population against a freshly-read census population.

    This is the staleness DETECTOR the derive cannot perform on itself. Two independent reads of the
    same estate; a difference means the older one is under-enumerating, and under-enumeration is the
    dangerous direction -- every role the snapshot lacks reads as a role that does not exist.

    Returns None when no census is supplied (the check is UNAVAILABLE, which is reported as such and
    never as agreement -- two sources cannot agree when only one is present).
    """
    if not census:
        return None
    derive_names = {str(n.get("id") or n.get("name")) for n in (derive_iam.get("nodes") or [])}
    census_names = {str(r.get("role_name")) for r in (census.get("roles") or [])}
    return {
        "derive_population": len(derive_names),
        "census_population": len(census_names),
        "in_census_not_in_derive": sorted(census_names - derive_names),
        "in_derive_not_in_census": sorted(derive_names - census_names),
    }


def classify(derive_iam: dict) -> dict:
    """Live-primary partition of the derive's nodes. No re-derivation -- the drift_class is the
    certed reconciler's verdict and is reported, not recomputed."""
    nodes = derive_iam.get("nodes") or []
    out = {"DECLARED": [], "LIVE-no-DECLARED": [], "OTHER": []}
    for n in nodes:
        dc = str(n.get("drift_class") or "OTHER")
        out.setdefault(dc, out["OTHER"] if dc not in out else out[dc])
        (out[dc] if dc in ("DECLARED", "LIVE-no-DECLARED") else out["OTHER"]).append(n)
    return out


def service_linked(node: dict) -> bool:
    """AWS-managed service-linked roles, identified on the STRUCTURED /aws-service-role/ ARN path
    segment -- not a name-prefix heuristic. They are live and undeclared BY DESIGN; counting them as
    ungoverned findings is how a real signal gets buried under expected noise."""
    return "/aws-service-role/" in str(node.get("arn") or "")
