#!/usr/bin/env python3
"""census_substrate -- the descriptor-driven APPLIED-plane census engine (2026-08-05).

Extracted from TWO WORKING INSTANCES at Andrew's word (record
ANDREW_DIRECT_20260805_0050Z_descriptor_substrate_extraction.md): comp-iam's refresh-census
(the vintage gate + CLI transport + _meta stamp; built 07-22, made operational 08-05
@c6f1d98fc) and comp-lambdamap's live-sha sweep (the enumerate-the-live-population shape).
Generalized FROM proven code, never from the abstract.

THE THESIS (Andrew, 2026-08-04 ~2233Z, verbatim in the fan-out record): these wrap-an-AWS-
resource tools "should just be some kind of expanded wrapper of an aws tool that uses aws
cli/api to just beam right into the given node versus some kind of scraping/regex/
hand-drawn-rule/etc layout" -- at scale, "first for AWS, but eventually as a cloud solution
with associated cloud provider's cli as a generalized foundational concept." The estate held
four independent implementations of that pattern (comp-tagauthz, comp-iam census, lambdamap
sha, comp-aws derive); this module is their one home going forward. A NEW SERVICE = ONE
DESCRIPTOR ROW, not a new scraper. Multi-cloud = the `provider` column, later.

WHAT LIVES HERE (generic, extracted):
  - THE VINTAGE GATE -- FRESH / STALE / NO_VINTAGE / FUTURE + clock-skew tolerance. MOVED from
    comp_iam_census, which now RE-EXPORTS the same objects (back-compat; the commit_stream
    extraction pattern ruled the same night). ONE gate, one home; its behavior is pinned by
    org/modules/graph/tests/test_iam_census_vintage.py (12 tests) which imports via the
    re-export and must stay green through this move.
  - THE CLI TRANSPORT -- explicit executable resolution (Windows .cmd shim aware: a bare
    subprocess argv cannot run an extensionless bash shim) + the THREE NAMED FAILURE CLASSES:
    CLI-NOT-FOUND (tooling/PATH, not AWS), CLI-SAID-NO (rc!=0 with stderr), and
    EMPTY-STDOUT-RC0 (the false-clean: a successful-looking read that produced nothing).
    Collapsing these sends a reader hunting the wrong cause; each raises with its own name.
  - THE _META STAMP -- {generated_utc (stamped AT THE READ from the reader's clock -- never
    a filename, never an mtime: those date the ARTIFACT, not the MEASUREMENT), provider,
    service, api, account, tool, accounts_swept, scope}.
  - DESCRIPTORS -- data rows. A simple service (lambda) is PURE DATA: items_key + a field
    projection. A service whose payload needs bespoke normalization (iam's policy-document
    expansion) declares shaper "custom:<where>" and keeps that shaper AT ITS TOOL --
    honesty over uniformity: this table does not pretend AAD normalization is a field list.

WHAT DELIBERATELY DOES NOT LIVE HERE:
  - freshness POLICY (each consumer picks its TTL; the gate only measures),
  - authorization VERDICTS (Rule 22a: `comp-iam simulate` is the only oracle; a census is a
    DETECTOR substrate, and nothing built on it may masquerade as allow/deny),
  - any SCHEDULED refresh (the standing moratorium: no alarm/cron machinery; the fail-closed
    gate names the remedy -- run the refresh -- at the moment of need).

STDLIB-ONLY at import time; subprocess is touched lazily inside the transport so every
predicate here is importable and testable with zero AWS (the comp_iam_census posture, kept).

PAGINATION LAW (banked from the estate's own scar, CLAUDE.md Git section): the AWS CLI
auto-paginates `list-*` calls and MERGES pages in `--output json` -- but applies `--query`
PER PAGE, so `--query 'length(...)'` returns a PAGE size wearing a total's clothing. This
transport therefore forbids --query in inventory_op rows and counts the materialized list.
"""
from __future__ import annotations

import json
import shutil
import subprocess
from datetime import datetime, timezone

# ---------------------------------------------------------------------------------------------
# THE VINTAGE GATE (moved verbatim from comp_iam_census 2026-08-05; that module re-exports).
# History that must not be lost in the move: FUTURE exists because CVO's 07-22 mutant proved a
# future-dated census read FRESHER the further forward it was pushed -- an unaudited one-field
# bypass cheaper than the audited override. NO_VINTAGE is not a kind of STALE: "I cannot tell
# how old" and "I can tell, and it is too old" are different epistemic states.
# ---------------------------------------------------------------------------------------------
DEFAULT_TTL_HOURS = 24
FRESH = "FRESH"
STALE = "STALE"
NO_VINTAGE = "NO_VINTAGE"
FUTURE = "FUTURE"
CLOCK_SKEW_TOLERANCE_HOURS = 0.25
_ISO_Z = "%Y-%m-%dT%H:%M:%SZ"


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def parse_generated_utc(census: dict):
    """Aware datetime from _meta.generated_utc, or None (first-class: absence is reportable,
    never defaulted, and NEVER substituted from file mtime -- mtime tracks byte movement, not
    when the cloud was read)."""
    meta = census.get("_meta") or {}
    raw = meta.get("generated_utc")
    if not raw:
        return None
    try:
        return datetime.strptime(str(raw), _ISO_Z).replace(tzinfo=timezone.utc)
    except (ValueError, TypeError):
        return None


def census_age_hours(census: dict, now=None):
    gen = parse_generated_utc(census)
    if gen is None:
        return None
    return ((now or _utcnow()) - gen).total_seconds() / 3600.0


def census_freshness(census: dict, ttl_hours: float = DEFAULT_TTL_HOURS, now=None):
    """(verdict, age_hours_or_None); verdict in {FRESH, STALE, NO_VINTAGE, FUTURE}."""
    age = census_age_hours(census, now=now)
    if age is None:
        return NO_VINTAGE, None
    if age < -CLOCK_SKEW_TOLERANCE_HOURS:
        return FUTURE, age
    return (FRESH if age <= ttl_hours else STALE), age


# ---------------------------------------------------------------------------------------------
# THE CLI TRANSPORT (lifted from comp_iam_census.build_census, which now rides it).
# ---------------------------------------------------------------------------------------------
class CliNotFound(RuntimeError):
    """The cloud CLI is absent from PATH: a TOOLING failure, not a cloud/permissions failure."""


class CliCallFailed(RuntimeError):
    """The CLI ran and said no (rc!=0): the cloud's answer, stderr attached."""


class CliEmptyStdout(RuntimeError):
    """rc=0 with empty stdout: a successful-looking read that produced NOTHING -- the
    false-clean class. Named so a caller never meets it as a json.loads('') parse error."""


def run_cli_json(op_args: list, cli_bin: str = "aws", _runner=None) -> dict:
    """Run one structured inventory read and return parsed JSON. `_runner` is injectable for
    hermetic tests (takes the argv list, returns (rc, stdout, stderr))."""
    if any(a == "--query" or str(a).startswith("--query") for a in op_args):
        raise ValueError("--query is FORBIDDEN in inventory ops (per-page application makes a "
                         "page size wear a total's clothing); project fields AFTER the read.")
    if _runner is None:
        exe = shutil.which(cli_bin) or shutil.which(cli_bin + ".cmd")
        if not exe:
            raise CliNotFound(
                "cloud CLI NOT FOUND on PATH (looked for %r and %r). Tooling/PATH failure, "
                "not a cloud or permissions failure; NO census was generated."
                % (cli_bin, cli_bin + ".cmd"))
        proc = subprocess.run([exe] + list(op_args), capture_output=True, text=True)
        rc, out, err = proc.returncode, proc.stdout, proc.stderr
    else:
        rc, out, err = _runner(list(op_args))
    if rc != 0:
        raise CliCallFailed("inventory read FAILED (rc=%s). Census NOT generated.\nSTDERR:\n%s"
                            % (rc, (err or "").strip()[:2000]))
    if not (out or "").strip():
        raise CliEmptyStdout("inventory read returned EMPTY stdout with rc=0 -- census NOT "
                             "generated (the false-clean class, named at the fetch).")
    return json.loads(out)


# ---------------------------------------------------------------------------------------------
# DESCRIPTORS -- the table. Adding a service = adding a row (projection shaper) or a row plus a
# bespoke shaper AT THE TOOL (custom). Every row states its joins so consumers never invent them.
# ---------------------------------------------------------------------------------------------
DESCRIPTORS = {
    "aws.iam": {
        "provider": "aws",
        "service": "iam",
        "inventory_op": ["iam", "get-account-authorization-details", "--output", "json"],
        "api": "iam:GetAccountAuthorizationDetails",
        "pagination": "api-internal single logical read (CLI merges)",
        "id_field": "Arn",
        "join_tf": "RoleName exact; name_prefix -> bounded startswith",
        "join_graph": "arn == CloudNode.node_id",
        "default_ttl_hours": DEFAULT_TTL_HOURS,
        "shaper": "custom:comp_iam_census.build_census",  # AAD normalization is not a field list
    },
    "aws.lambda": {
        "provider": "aws",
        "service": "lambda",
        "inventory_op": ["lambda", "list-functions", "--output", "json"],
        "api": "lambda:ListFunctions",
        "pagination": "CLI auto-paginates and merges pages in --output json",
        "items_key": "Functions",
        "fields": ["FunctionName", "FunctionArn", "CodeSha256", "LastModified", "Runtime",
                   "MemorySize", "Timeout"],
        "id_field": "FunctionArn",
        "join_tf": "FunctionName exact (lambda-source-map + TF function name)",
        "join_graph": "FunctionArn == CloudNode.node_id",
        "default_ttl_hours": DEFAULT_TTL_HOURS,
        "shaper": "projection",
    },
}


def stamp_meta(descriptor: dict, tool: str, account=None, extra_scope: str = "") -> dict:
    """The _meta block, stamped AT THE READ from the reader's clock."""
    return {
        "generated_utc": _utcnow().strftime(_ISO_Z),
        "provider": descriptor["provider"],
        "service": descriptor["service"],
        "api": descriptor["api"],
        "account": account,
        "tool": tool,
        "accounts_swept": 1,
        "scope": ("single-account, full population returned by %s%s"
                  % (descriptor["api"], ("; " + extra_scope) if extra_scope else "")),
    }


def build_descriptor_census(key: str, tool: str, cli_bin: str = "aws", _runner=None) -> dict:
    """The PROJECTION path: run the descriptor's inventory op, project its declared fields.
    Custom-shaper descriptors refuse here BY NAME -- their census builds at their tool."""
    if key not in DESCRIPTORS:
        raise KeyError("unknown descriptor %r -- known: %s" % (key, sorted(DESCRIPTORS)))
    d = DESCRIPTORS[key]
    if d["shaper"] != "projection":
        raise ValueError("descriptor %r declares shaper=%r -- its census builds at its own "
                         "tool, not via the projection path (honesty over uniformity)." %
                         (key, d["shaper"]))
    payload = run_cli_json(d["inventory_op"], cli_bin=cli_bin, _runner=_runner)
    items_raw = payload.get(d["items_key"]) or []
    items = [{f: it.get(f) for f in d["fields"]} for it in items_raw]
    account = None
    for it in items:  # account from the ARN's fixed 6-field colon layout, never a regex
        parts = str(it.get(d["id_field"]) or "").split(":", 5)
        if len(parts) >= 5 and parts[4]:
            account = parts[4]
            break
    return {
        "_meta": stamp_meta(d, tool=tool, account=account,
                            extra_scope="fields projected: " + ",".join(d["fields"])),
        "summary": {"item_count": len(items), "items_key": d["items_key"]},
        "items": items,
    }
