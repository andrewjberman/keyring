#!/usr/bin/env python3
"""dormant_guard -- the comp-debt KEYSTONE: the dormant-by-design vs dead guard.

MILESTONE 2 (NFRA_COMPDEBT_PRD.md 8.2 / 5). CTO arch-gates this specifically -- it is
THE governance guard, the thing that must NEVER false-decommission a deliberate belt.

WHY THIS IS THE PRODUCT: mechanical signals PROVABLY cannot discriminate keep-from-kill.
A deliberate belt and a corpse are identical on every signal (both DISABLED, both
0-invocation, both 0-consumer). Only the INTENT ANNOTATION separates them. Proof (both
literally say "dormant"):
  KEEP: inf-pipeline/eventbridge.tf:315 -- state=DISABLED, "WIRED-NOT-ARMED ... arm via
        state=ENABLED" (a deliberate belt).
  DEAD: bd-pipeline/lambdas.tf:241 -- "DECOMMISSIONED ... superseded by D_02" (a corpse).

THE GUARD'S DISPOSITION (4-way, fail-safe toward KEEP):
  KEEP-DORMANT-REGISTERED  -- an explicit keep-dormant.yaml entry (Tier A/B). Strongest.
  KEEP-DORMANT-ANNOTATED   -- not registered, but an adjacent Tier-A/B keep intent-annotation
                              is present (recommend adding to the registry).
  KEEP-DORMANT-FAILSAFE    -- only mechanical Tier-C signals, NO keep-signal AND NO positive
                              dead-marker => DEFAULT to keep (PRD 5 fail-safe). NEVER DEBT.
  DEBT-ELIGIBLE            -- a Tier-A/B keep-signal is affirmatively RULED OUT (absent) AND a
                              positive dead-marker is present. ONLY this disposition lets
                              fuse.py proceed toward DEBT -- and even then fuse.py still
                              requires >=2 CONFIRMED signals + no contra live-use (ruling-2).

KEEP WINS on conflict: a "superseded by X" that co-occurs with any keep verb stays KEEP
(fail-safe). A false-negative (miss a corpse) is recoverable; a false-positive
(decommission a deliberate belt) is THE named failure mode (Andrew, PRD 5).

DECAY (RULING 1): every registry entry carries a `revalidate_by`. An entry PAST its window
is flagged STALE ("re-confirm still-a-belt or promote to DEBT") -- a belt DECAYS into a
corpse over time. STALE stays KEEP; it demands a HUMAN re-grounding, never an auto-promote.

EMIT-ONLY: the guard rules; it NEVER acts.
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

REPO = Path(__file__).resolve().parents[4]
REGISTRY_PATH = REPO / "org" / "modules" / "graph" / "keep-dormant.yaml"

# ---- dispositions -------------------------------------------------------------------------
KEEP_REGISTERED = "KEEP-DORMANT-REGISTERED"
KEEP_ANNOTATED = "KEEP-DORMANT-ANNOTATED"
KEEP_FAILSAFE = "KEEP-DORMANT-FAILSAFE"
DEBT_ELIGIBLE = "DEBT-ELIGIBLE"
_KEEP_DISPOSITIONS = frozenset({KEEP_REGISTERED, KEEP_ANNOTATED, KEEP_FAILSAFE})

# ---- discriminators (regex vocab mirrors keep-dormant.yaml `discriminators`) ---------------
# Tier-A: any ~sufficient => KEEP-DORMANT. Bias is DELIBERATELY toward keep -- over-matching
# a keep is safe (false-negative is recoverable); over-matching a kill is the named failure.
_TIER_A_RE = re.compile(
    r"wired[\s-]?not[\s-]?armed"
    r"|arm\s+via\s+(?:state\s*=\s*)?enabled"
    r"|deployed[\s-]?dormant"
    r"|go[\s-]?live\s+gated"
    r"|disabled\s+by[\s-]?design"
    r"|by[\s-]?design[^\n]{0,40}(?:disabled|dormant|keep[\s_-]?alive|keep[\s-]?warm|idle)"
    r"|keep[\s_-]?alive"
    r"|keep[\s-]?warm"
    r"|ignore_changes"                 # a lifecycle rollback lever / operationally-set value
    r"|\brollback\b"
    r"|\blever\b"
    r"|armed\s+fallback"
    r"|do\s+not\s+fire\s+without"
    r"|deliberately\s+not\s+terraform[\s-]?managed"
    r"|never\s+lands?\s+in\s+terraform\s+state"
    r"|manual/(?:future|emergency)\s+path"
    r"|manual[\s-]?dispatch\s+by\s+design",
    re.I,
)
# Tier-B: corroborating (supports a keep). Includes "target live via another path".
_TIER_B_RE = re.compile(
    r"runbook|\bSOP\b|emergency\s+path|manual\s+path"
    r"|acknowledges?\s+the\s+idle"
    r"|live\s+via\s+another\s+path|target\s+is\s+live"
    r"|now\s+fires\s+on|runner\s+now\s+fires",
    re.I,
)
# Positive dead-markers: only flips to DEBT-ELIGIBLE when NO keep-signal is present.
_DEAD_MARKER_RE = re.compile(
    r"decommissioned|superseded\s+by|not\s+consumed|\bno\s+consumer\b"
    r"|cleanup\s+tracked|removal\s+tracked|marked\s+for\s+removal|\bgraveyard\b",
    re.I,
)


@dataclass
class KeepDormantRuling:
    disposition: str                       # one of the four above
    ruled_keep: bool                       # a Tier-A/B keep-signal is present
    keep_ruled_out: bool                   # NO keep-signal AND a dead-marker present
    tier: str | None                       # A|B|C|None
    evidence: str                          # registry cite | intent-annotation | dead-marker
    stale: bool = False                    # registered entry past its revalidate_by
    registry_entry: dict | None = field(default=None, repr=False)
    matched_keep: list = field(default_factory=list)
    matched_dead: list = field(default_factory=list)
    notes: list = field(default_factory=list)

    @property
    def is_keep(self) -> bool:
        return self.disposition in _KEEP_DISPOSITIONS

    def to_dict(self) -> dict:
        # the PRD 4 verdict-schema `keep_dormant` block
        return {"ruled": self.is_keep, "disposition": self.disposition,
                "tier": self.tier, "evidence": self.evidence, "stale": self.stale,
                "keep_ruled_out": self.keep_ruled_out}


# ---- registry ------------------------------------------------------------------------------
_REGISTRY_CACHE: dict | None = None


def load_registry(path: Path = REGISTRY_PATH) -> dict:
    global _REGISTRY_CACHE
    if _REGISTRY_CACHE is not None:
        return _REGISTRY_CACHE
    if yaml is None:
        raise RuntimeError("PyYAML not available -- cannot load keep-dormant.yaml")
    with open(path, "r", encoding="utf-8") as fh:
        _REGISTRY_CACHE = yaml.safe_load(fh) or {}
    return _REGISTRY_CACHE


def _entry_aliases(entry: dict) -> set[str]:
    """All id-forms an entry can be matched by (resource_id + every `match` value)."""
    out = {str(entry.get("resource_id", "")).strip().lower()}
    for v in (entry.get("match") or {}).values():
        if isinstance(v, str):
            out.add(v.strip().lower())
    out.discard("")
    return out


def _today() -> dt.date:
    return dt.date.today()


def _parse_date(v) -> dt.date | None:
    if isinstance(v, dt.date):
        return v
    try:
        return dt.date.fromisoformat(str(v))
    except (ValueError, TypeError):
        return None


def lookup(resource_id: str, *, firm: str | None = None, aliases: list[str] | None = None,
           registry: dict | None = None) -> tuple[dict | None, bool]:
    """Find a registry entry matching resource_id (or any alias), firm-scoped.
    Returns (entry_or_None, stale). Firm-separation is enforced: an entry only matches
    when its firm equals the queried firm (or the query firm is None)."""
    reg = registry if registry is not None else load_registry()
    keys = {resource_id.strip().lower()}
    keys.update(a.strip().lower() for a in (aliases or []))
    keys.discard("")
    for entry in reg.get("entries", []) or []:
        if firm and entry.get("firm") and entry["firm"] != firm:
            continue  # firm-separation: never cross bd/cot/inf
        if keys & _entry_aliases(entry):
            rev = _parse_date(entry.get("revalidate_by"))
            stale = bool(rev and _today() > rev)
            return entry, stale
    return None, False


# ---- annotation reading --------------------------------------------------------------------
def read_annotation_window(spec: str, *, before: int = 30, after: int = 5,
                           repo: Path = REPO) -> str:
    """Read a window of text around a `file` or `file:line` cite. TF/py intent annotations
    sit ABOVE the resource block, so we read mostly-before. Returns '' on any error."""
    path_part, _, line_part = spec.partition(":")
    fp = (repo / path_part) if not Path(path_part).is_absolute() else Path(path_part)
    try:
        lines = fp.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return ""
    if line_part.isdigit():
        ln = int(line_part)
        lo, hi = max(0, ln - 1 - before), min(len(lines), ln + after)
        return "\n".join(lines[lo:hi])
    return "\n".join(lines[:200])  # no line -> read the head (small files / file-level notes)


# ---- the guard -----------------------------------------------------------------------------
def rule(resource_id: str, *, firm: str | None = None, annotation_text: str = "",
         annotation_cite: str | None = None, aliases: list[str] | None = None,
         registry: dict | None = None) -> KeepDormantRuling:
    """Rule a resource KEEP-DORMANT vs DEBT-ELIGIBLE. See module docstring for the 4-way.

    resource_id      : the <type>:<id> the signals emit.
    firm             : bd|cot|inf|mdpf|imo|shared (firm-scopes the registry lookup).
    annotation_text  : the resource's adjacent intent-annotation text (from the signals).
    annotation_cite  : a `file` or `file:line` to READ the annotation from if text absent.
    """
    # 1. Registry lookup (strongest keep-signal).
    entry, stale = lookup(resource_id, firm=firm, aliases=aliases, registry=registry)
    if entry:
        note = []
        if stale:
            note.append(f"STALE: past revalidate_by={entry.get('revalidate_by')} -- "
                        "re-confirm still-a-belt or promote to DEBT (human re-grounding)")
        return KeepDormantRuling(
            disposition=KEEP_REGISTERED, ruled_keep=True, keep_ruled_out=False,
            tier=entry.get("tier"), stale=stale, registry_entry=entry,
            evidence=f"keep-dormant.yaml:{entry.get('resource_id')} "
                     f"(cite {entry.get('annotation_cite')})",
            notes=note)

    # 2. Not registered -> parse the intent annotation.
    text = annotation_text or ""
    if annotation_cite and not text:
        text = read_annotation_window(annotation_cite)
    a_hits = _TIER_A_RE.findall(text)
    b_hits = _TIER_B_RE.findall(text)
    dead_hits = _DEAD_MARKER_RE.findall(text)
    keep_present = bool(a_hits or b_hits)

    if keep_present:
        # KEEP WINS on conflict (fail-safe). Recommend registering it.
        tier = "A" if a_hits else "B"
        cite = annotation_cite or "annotation-text"
        note = ["not in keep-dormant.yaml -- RECOMMEND adding (grounded keep intent found)"]
        if dead_hits:
            note.append(f"NOTE dead-marker(s) {sorted(set(dead_hits))} co-occur but a "
                        "keep verb is present -> KEEP wins (fail-safe)")
        return KeepDormantRuling(
            disposition=KEEP_ANNOTATED, ruled_keep=True, keep_ruled_out=False, tier=tier,
            evidence=f"Tier-{tier} intent-annotation @ {cite}: "
                     f"{sorted(set(a_hits or b_hits))}",
            matched_keep=sorted(set(a_hits + b_hits)), matched_dead=sorted(set(dead_hits)),
            notes=note)

    if dead_hits:
        # keep-signal RULED OUT (absent) AND a positive dead-marker present => DEBT-ELIGIBLE.
        # (fuse.py still requires >=2 CONFIRMED signals + no-contra before DEBT-DECOMMISSION.)
        cite = annotation_cite or "annotation-text"
        return KeepDormantRuling(
            disposition=DEBT_ELIGIBLE, ruled_keep=False, keep_ruled_out=True, tier=None,
            evidence=f"dead-marker @ {cite}: {sorted(set(dead_hits))}; NO Tier-A/B keep-signal",
            matched_dead=sorted(set(dead_hits)),
            notes=["DEBT-ELIGIBLE only -- fuse.py must still gate on >=2 CONFIRMED signals + "
                   "no contra live-use (ruling-2) before DEBT-DECOMMISSION"])

    # 3. Only mechanical Tier-C signals, no keep, no dead-marker => FAIL-SAFE default keep.
    return KeepDormantRuling(
        disposition=KEEP_FAILSAFE, ruled_keep=False, keep_ruled_out=False, tier="C",
        evidence="only mechanical Tier-C signals; no keep-annotation, no dead-marker -> "
                 "fail-safe default KEEP-DORMANT (PRD 5)",
        notes=["default fail-safe: a resource tripping only mechanical signals is NEVER DEBT"])


# ---- registry validation + decay audit -----------------------------------------------------
_REQUIRED_FIELDS = ("resource_id", "firm", "tier", "reason", "rearm_condition",
                    "annotation_cite", "added", "revalidate_by")


def validate_registry(registry: dict | None = None) -> tuple[list[str], list[str]]:
    """Ruling-1 enforcement: every entry MUST carry a grounded reason + rearm + cite +
    revalidate_by. Returns (errors, stale_warnings). An entry missing a required field is
    itself unreviewable debt."""
    reg = registry if registry is not None else load_registry()
    errors, stale = [], []
    seen_ids: set[str] = set()
    for i, entry in enumerate(reg.get("entries", []) or []):
        rid = entry.get("resource_id", f"<entry#{i}>")
        for fld in _REQUIRED_FIELDS:
            if not entry.get(fld):
                errors.append(f"{rid}: missing required field '{fld}' (ruling-1: an "
                              "ungrounded keep is itself debt)")
        reason = str(entry.get("reason", "")).strip()
        if reason and len(reason) < 40:
            errors.append(f"{rid}: reason too thin ({len(reason)} chars) -- must be a "
                          "grounded justification, not a label")
        if rid in seen_ids:
            errors.append(f"{rid}: duplicate resource_id")
        seen_ids.add(rid)
        if entry.get("firm") not in ("bd", "cot", "inf", "mdpf", "imo", "shared", None):
            errors.append(f"{rid}: unknown firm '{entry.get('firm')}'")
        rev = _parse_date(entry.get("revalidate_by"))
        if entry.get("revalidate_by") and rev is None:
            errors.append(f"{rid}: revalidate_by '{entry.get('revalidate_by')}' not ISO date")
        elif rev and _today() > rev:
            stale.append(f"{rid}: STALE (revalidate_by={rev} < today={_today()}) -- re-ground")
    return errors, stale


# ---- CLI -----------------------------------------------------------------------------------
def _print_ruling(rid: str, r: KeepDormantRuling) -> None:
    print(f"resource : {rid}")
    print(f"verdict  : {r.disposition}  (is_keep={r.is_keep})")
    print(f"tier     : {r.tier}   ruled_keep={r.ruled_keep}  keep_ruled_out={r.keep_ruled_out}")
    print(f"evidence : {r.evidence}")
    if r.stale:
        print("STALE    : registry entry past its revalidate_by window")
    for n in r.notes:
        print(f"  note   : {n}")


def _self_test() -> int:
    """Deterministic fixtures over an in-memory registry -- no I/O, no network. Proves the
    4-way disposition + KEEP-WINS + fail-safe-default + decay."""
    reg = {"entries": [
        {"resource_id": "event_rule:inf-gold-incremental-daily", "firm": "inf", "tier": "A",
         "match": {"tf_address": "aws_cloudwatch_event_rule.inf_gold_incremental_daily"},
         "reason": "x" * 50, "rearm_condition": "flip ENABLED",
         "annotation_cite": "eventbridge.tf:315", "added": "2026-07-02",
         "revalidate_by": "2026-12-29"},
        {"resource_id": "lever:stale-belt", "firm": "mdpf", "tier": "A",
         "reason": "x" * 50, "rearm_condition": "manual", "annotation_cite": "x:1",
         "added": "2026-01-01", "revalidate_by": "2026-01-02"},  # past -> STALE
    ]}
    cases = []

    # 1. registered by resource_id -> KEEP-REGISTERED
    r = rule("event_rule:inf-gold-incremental-daily", firm="inf", registry=reg)
    cases.append(("registered => KEEP-REGISTERED", r.disposition == KEEP_REGISTERED and r.is_keep))

    # 2. registered by alias (tf_address) -> KEEP-REGISTERED
    r = rule("aws_cloudwatch_event_rule.inf_gold_incremental_daily", firm="inf", registry=reg)
    cases.append(("alias match => KEEP-REGISTERED", r.disposition == KEEP_REGISTERED))

    # 3. firm-separation: same id queried under wrong firm -> NOT matched (falls through)
    r = rule("event_rule:inf-gold-incremental-daily", firm="bd", registry=reg,
             annotation_text="")
    cases.append(("firm-separation blocks cross-firm match", r.disposition == KEEP_FAILSAFE))

    # 4. unregistered + Tier-A annotation -> KEEP-ANNOTATED
    r = rule("event_rule:foo", firm="inf", registry=reg,
             annotation_text="state=DISABLED, WIRED-NOT-ARMED -- arm via state=ENABLED")
    cases.append(("Tier-A annotation => KEEP-ANNOTATED", r.disposition == KEEP_ANNOTATED and r.tier == "A"))

    # 5. unregistered + dead-marker only -> DEBT-ELIGIBLE
    r = rule("lambda:bd_portal_advisor_publisher", firm="bd", registry=reg,
             annotation_text="bd_portal_advisor_publisher DECOMMISSIONED 2026-06-03, superseded by D_02")
    cases.append(("dead-marker only => DEBT-ELIGIBLE", r.disposition == DEBT_ELIGIBLE and r.keep_ruled_out))

    # 6. KEEP WINS: dead-marker + keep verb co-occur -> KEEP-ANNOTATED
    r = rule("event_rule:bd-49f-interim", firm="bd", registry=reg,
             annotation_text="SUPERSEDED by the session chain (DISABLED; runner now fires on bd-49f-session-complete)")
    cases.append(("superseded+keep-verb => KEEP wins", r.is_keep and r.matched_dead))

    # 7. fail-safe default: only mechanical, no annotation -> KEEP-FAILSAFE (never DEBT)
    r = rule("lambda:mystery", firm="inf", registry=reg, annotation_text="")
    cases.append(("mechanical-only => KEEP-FAILSAFE", r.disposition == KEEP_FAILSAFE and r.is_keep))

    # 8. decay: a registered entry past revalidate_by -> KEEP but stale
    r = rule("lever:stale-belt", firm="mdpf", registry=reg)
    cases.append(("past revalidate_by => STALE keep", r.is_keep and r.stale))

    # 9. ignore_changes secret -> KEEP (Tier-A, the TF-DRIFT FP trap)
    r = rule("secret_version:x", firm="cot", registry=reg,
             annotation_text="ignore_changes=[secret_string] -- never lands in Terraform state")
    cases.append(("un-managed secret => KEEP (FP trap)", r.is_keep))

    # 10. registry validation on the good in-memory reg (entry 2 is stale but valid-shape)
    errs, st = validate_registry(reg)
    cases.append(("validate_registry: 0 errors, 1 stale", errs == [] and len(st) == 1))

    npass = sum(1 for _, ok in cases if ok)
    for name, ok in cases:
        print(f"  {'OK  ' if ok else 'FAIL'} {name}")
    print(f"dormant_guard self-test: {npass}/{len(cases)} passed")
    return 0 if npass == len(cases) else 1


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(
        prog="comp-debt.dormant_guard",
        description="The dormant-by-design vs dead guard (comp-debt keystone). EMIT-ONLY.")
    ap.add_argument("--check", metavar="RESOURCE_ID", help="rule a resource KEEP vs DEBT-ELIGIBLE")
    ap.add_argument("--firm", default=None, help="bd|cot|inf|mdpf|imo|shared (firm-scopes lookup)")
    ap.add_argument("--annotation", default="", help="the resource's intent-annotation text")
    ap.add_argument("--annotation-cite", default=None, help="file or file:line to read the annotation from")
    ap.add_argument("--alias", action="append", default=[], help="an alternate id form to match (repeatable)")
    ap.add_argument("--list", action="store_true", help="list registry entries (+ firm filter)")
    ap.add_argument("--validate", action="store_true", help="validate the registry (ruling-1 enforcement)")
    ap.add_argument("--audit", action="store_true", help="list entries PAST their revalidate_by (decay)")
    ap.add_argument("--self-test", action="store_true", help="run deterministic fixtures (no I/O)")
    args = ap.parse_args(argv)

    if args.self_test:
        return _self_test()

    if args.validate:
        errs, stale = validate_registry()
        for e in errs:
            print(f"ERROR: {e}")
        for s in stale:
            print(f"WARN:  {s}")
        print(f"keep-dormant.yaml: {len(errs)} error(s), {len(stale)} stale entry(ies)")
        return 1 if errs else 0

    if args.audit:
        _, stale = validate_registry()
        if not stale:
            print("OK: no keep-dormant entries past their revalidate_by window.")
        for s in stale:
            print(f"STALE: {s}")
        return 0

    if args.list:
        reg = load_registry()
        entries = [e for e in reg.get("entries", [])
                   if not args.firm or e.get("firm") == args.firm]
        print(f"keep-dormant.yaml -- {len(entries)} entry(ies)"
              + (f" (firm={args.firm})" if args.firm else ""))
        for e in entries:
            print(f"  [{e.get('tier')}] {e.get('resource_id'):<52} firm={e.get('firm'):<6} "
                  f"revalidate_by={e.get('revalidate_by')}  cite={e.get('annotation_cite')}")
        return 0

    if args.check:
        r = rule(args.check, firm=args.firm, annotation_text=args.annotation,
                 annotation_cite=args.annotation_cite, aliases=args.alias)
        _print_ruling(args.check, r)
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
