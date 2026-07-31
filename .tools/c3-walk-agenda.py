"""C3 WALK AGENDA BUILDER -- C3L.3 steps 1-2 (SURFACING + PRESENTATION).

Andrew-direct authorization 2026-07-31 ~2100Z: "Just proceed it now i authorize it".
Spec: org/tier2_senior/0.7.0_AE_CloudOps~B/C3_LABELING_LAYER_SPEC_20260731.md
TO:   org/tier2_senior/0.7.0_AE_CloudOps~B/task_orders/C3L.3.kimi-loop-integration.md

*** WHAT THIS IS ***
Layer 2's AGENDA. It selects which C3 items reach a CTO+Andrew walk and renders them. It is the
TRIGGER that makes the walk ride IN the Kimi cycle instead of being a campaign someone remembers to
run -- "a process whose only trigger is a human remembering has no trigger."

*** WHAT THIS IS NOT, AND THE PROHIBITION IS THE POINT ***
>> LAYER 1 NEVER LABELS. SELECTION IS NOT ASSERTION. <<
This tool ORDERS AN AGENDA. It does not infer, suggest, default, rank-by-likely-value, or pre-fill a
lifecycle_class -- not even as a "hint for the reviewer." A surfacing mechanism that suggests values
has become the OBSERVER-INFERENCE ENGINE the rule bank forbids:

    "PRODUCER-ASSERTED, NEVER OBSERVER-INFERRED. The observer cannot distinguish never-yet from dead
     BY LOOKING -- that is the entire problem... ANY implementation inferring lifecycle_class from KEY
     NAMES, DIRECTORY POSITION, or OBSERVED ABSENCE has rebuilt the comp-legacywriter name-pattern
     stopgap with more syntax. Transience cannot be derived; it must be DECLARED."

There is deliberately NO code path in this file that writes or proposes a lifecycle_class value.
AC2 is verified by reading the agenda payload, not by trusting this docstring.

*** REGISTRY PROHIBITION 1 -- NO CACHED VOCABULARY, EVER ***
lifecycle_class values are RESOLVED FROM THE RULE BANK AT READ TIME. No cache outlives a read. If the
rule bank cannot be reached, this FAILS LOUD rather than serving a stale copy. Caching the resolved
enum rebuilds the telemetry appender's frozen VERDICT_EXIT_TOOLS defect -- 434 miscounted verdicts --
"with a performance justification instead of a design one."
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone

REGISTRY_GLOB = "org/modules/graph/estate-contracts/*.contracts.yaml"
RULE_BANK = "org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml"

# Sentinel recorded by WS-E1 when no governance level above the artifact could be cited.
# NOT a failure of the registry -- the registry declining to MANUFACTURE a parent is correct,
# and it is precisely the class only a governance act can resolve (spec s.2.3).
REJECTED = "REJECTED_NO_GOVERNANCE_ABOVE"


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def resolve_lifecycle_enum(root: str) -> list:
    """Read the ratified lifecycle enum FROM THE RULE BANK, at read time. Never cached.

    FAILS LOUD if unreachable (registry prohibition 1). A resolver that falls back to a
    literal is a cache with extra steps.
    """
    path = os.path.join(root, RULE_BANK)
    if not os.path.isfile(path):
        raise SystemExit(
            "ERROR: rule bank unreachable at %s -- REFUSING to serve a stale or literal enum "
            "(estate-contracts README prohibition 1). This is fail-loud by design." % path)
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    m = re.search(r"^\s*enum:\s*\[([^\]]+)\]", text, re.M)
    if not m:
        raise SystemExit(
            "ERROR: could not resolve lifecycle.enum from %s -- FAILING LOUD rather than "
            "assuming a vocabulary." % path)
    return [v.strip() for v in m.group(1).split(",") if v.strip()]


def parse_registry(path: str) -> tuple:
    """Minimal YAML-subset reader for the estate-contracts shape.

    Deliberately NOT a general YAML parser: the registry shape is fixed and narrow, and a
    dependency here would be a new install on every consumer of a governance record.
    Returns (resolution_meta, {subject: {field: value}}).
    """
    meta, contracts = {}, {}
    subject, cur = None, None
    in_contracts = False
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if re.match(r"^resolution:\s*$", line):
                in_contracts = False
                continue
            if re.match(r"^contracts:\s*$", line):
                in_contracts = True
                continue
            m_subj = re.match(r'^\s{2}"([^"]+)":\s*$', line)
            if m_subj and in_contracts:
                subject = m_subj.group(1)
                cur = {}
                contracts[subject] = cur
                continue
            m_kv = re.match(r"^\s{2,}([a-z_]+):\s*(.*)$", line)
            if m_kv:
                key, val = m_kv.group(1), m_kv.group(2).strip()
                val = re.sub(r"\s+#.*$", "", val).strip().strip('"').strip("'")
                if in_contracts and cur is not None:
                    cur[key] = val
                elif not in_contracts:
                    meta[key] = val
    return meta, contracts


def revalidate_state(value: str) -> tuple:
    """Classify revalidate_by. Returns (state, detail).

    >> THE FINDING THIS FUNCTION EXISTS TO REPORT RATHER THAN PAPER OVER: <<
    `revalidate_by` is REQUIRED ON EVERY DECLARATION and the spec's maintenance loop (R4) keys the
    walk's re-entry on it EXPIRING. But the landed tranche-1 values are FREE TEXT --
    "on producer assertion (solicitation outstanding)" -- with no date to compare against.

    So the expiry limb of the selection contract is NOT MACHINE-EVALUABLE against today's registry.
    That is reported as NOT_EVALUABLE, never silently treated as "not expired". A selection input
    that quietly evaluates false is a limb of the trigger that never fires, and nothing would say so.
    """
    if not value:
        return ("ABSENT", "no revalidate_by recorded")
    iso = re.match(r"^(\d{4}-\d{2}-\d{2})", value)
    if iso:
        try:
            due = datetime.strptime(iso.group(1), "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except ValueError:
            return ("NOT_EVALUABLE", "date-shaped but unparseable: %r" % value)
        return ("EXPIRED", value) if due <= utcnow() else ("CURRENT", value)
    return ("NOT_EVALUABLE", "free text, no comparable date: %r" % value)


def select(subject: str, rec: dict, enum: list) -> list:
    """THE SELECTION CONTRACT. Returns a list of REASONS this subject reaches the agenda.

    Empty list = does not surface. Every reason is a fact ABOUT THE RECORD -- never a judgement
    about what the subject IS, and never a proposed value.
    """
    reasons = []
    lc = (rec.get("lifecycle_class") or "").strip()

    if lc == "UNDECLARED":
        reasons.append({
            "code": "UNDECLARED",
            "why": "no producer has asserted a lifecycle. UNDECLARED AUTHORIZES NOTHING and is not "
                   "a value -- it records the absence of an assertion.",
        })
    elif lc and lc not in enum:
        reasons.append({
            "code": "UNRESOLVABLE_LIFECYCLE",
            "why": "lifecycle_class %r does not resolve against the rule bank enum resolved this "
                   "read. Surfaced as a RECORD defect, not a lifecycle judgement." % lc,
        })

    state, _detail = revalidate_state(rec.get("revalidate_by", ""))
    if state == "EXPIRED":
        reasons.append({"code": "REVALIDATE_EXPIRED",
                        "why": "revalidate_by matured -- the maintenance loop's re-entry (R4): the "
                               "assertion persists, marked stale, and returns to the walk."})
    if (rec.get("intent_source") or "").strip() == REJECTED:
        reasons.append({
            "code": "INTENT_SOURCE_REJECTED",
            "why": "intent_source was REJECTED at declaration: no governance level above was cited "
                   "and the registry correctly declined to MANUFACTURE one. Source-first cannot "
                   "resolve this (there is no authored intent to read) and measuring harder cannot "
                   "either -- ONLY A GOVERNANCE ACT CAN SUPPLY IT. This is the walk's canonical "
                   "case (spec s.2.3).",
        })

    # NOT_EVALUABLE / ABSENT are deliberately NOT surfacing reasons -- see record_defects().
    return reasons


def record_defects(rec: dict) -> list:
    """Defects in the RECORD, reported ALONGSIDE the agenda -- never as reasons to walk an item.

    >> WHY THIS IS SEPARATE, AND IT IS THE FIRST THING THIS TOOL GOT WRONG: <<
    The first build treated an un-evaluable `revalidate_by` as a surfacing reason. Every landed
    tranche-1 record carries free text there, so EVERY subject surfaced: 14 scanned, 14 surfaced,
    0 quiet. AC1's negative control fired on this tool's own first run.

    A REGISTRY DEFECT IS NOT A REASON TO WALK A SUBJECT. Conflating them produced a selector that
    passed everything through while looking selective -- and it would have passed every positive
    test in the TO, because each individual reason it printed was TRUE. The defect still gets
    reported; it just cannot make the agenda mean nothing.
    """
    out = []
    state, detail = revalidate_state(rec.get("revalidate_by", ""))
    if state in ("NOT_EVALUABLE", "ABSENT"):
        out.append({
            "code": "REVALIDATE_%s" % state,
            "why": "%s. THE EXPIRY LIMB OF THE SELECTION CONTRACT CANNOT FIRE FOR THIS SUBJECT -- "
                   "R4's maintenance re-entry is inert here. Reported, never assumed-current."
                   % detail,
        })
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="C3 walk agenda builder (C3L.3 steps 1-2)")
    ap.add_argument("--root", default=".", help="workspace root")
    ap.add_argument("--json", action="store_true", help="emit the agenda as JSON")
    ap.add_argument("--show-quiet", action="store_true",
                    help="ALSO list subjects that did NOT surface (the negative control, AC1)")
    args = ap.parse_args(argv)

    enum = resolve_lifecycle_enum(args.root)          # read-time, uncached, fail-loud
    files = sorted(glob.glob(os.path.join(args.root, REGISTRY_GLOB)))
    if not files:
        print("NO REGISTRY FILES under %s -- refusing to report an empty agenda as a complete one"
              % REGISTRY_GLOB, file=sys.stderr)
        return 2

    agenda, quiet, scanned = [], [], 0
    for path in files:
        meta, contracts = parse_registry(path)
        for subject, rec in contracts.items():
            scanned += 1
            reasons = select(subject, rec, enum)
            row = {
                "subject": subject,
                "source_file": os.path.relpath(path, args.root).replace("\\", "/"),
                "lifecycle_class": rec.get("lifecycle_class", ""),
                "intent_source": rec.get("intent_source", ""),
                "revalidate_by": rec.get("revalidate_by", ""),
                "revalidate_state": revalidate_state(rec.get("revalidate_by", ""))[0],
                "locality": rec.get("locality", ""),
                "describes": rec.get("describes", ""),
                "resolved_against": meta.get("resolved_against", ""),
                "resolved_version": meta.get("resolved_version", ""),
                "reasons": reasons,
                "record_defects": record_defects(rec),
                # NOTE: there is deliberately NO 'suggested_lifecycle' / 'likely' / 'proposed' key.
                # Its absence is the AC2 property, and it is checkable by reading this payload.
            }
            (agenda if reasons else quiet).append(row)

    if args.json:
        print(json.dumps({
            "generated_at": utcnow().isoformat(),
            "lifecycle_enum_resolved_this_read": enum,
            "denominator": {"subjects_scanned": scanned, "surfaced": len(agenda),
                            "did_not_surface": len(quiet), "registry_files": len(files)},
            "agenda": agenda,
            "did_not_surface": quiet if args.show_quiet else "(use --show-quiet)",
        }, indent=2))
        return 0

    print("=== C3 WALK AGENDA ===")
    print("  enum resolved THIS READ from %s: %s" % (RULE_BANK, ", ".join(enum)))
    print("  DENOMINATOR: %d subjects scanned across %d registry file(s) | %d surfaced | %d did not"
          % (scanned, len(files), len(agenda), len(quiet)))
    print("  LAYER 1 NEVER LABELS: this agenda proposes no lifecycle value for any subject.")
    print()
    for row in agenda:
        print("  %s" % row["subject"])
        print("     lifecycle_class=%s  revalidate=%s  locality=%s"
              % (row["lifecycle_class"] or "-", row["revalidate_state"], row["locality"] or "-"))
        if row["describes"]:
            print("     describes: %s" % row["describes"])
        for r in row["reasons"]:
            print("     [%s] %s" % (r["code"], r["why"]))
        for d in row["record_defects"]:
            print("     (defect) [%s] %s" % (d["code"], d["why"]))
        print()

    print("=== DID NOT SURFACE (AC1 NEGATIVE CONTROL) -- %d of %d ===" % (len(quiet), scanned))
    if not quiet:
        print("  *** ZERO. THE SELECTOR SURFACED EVERYTHING. ***")
        print("  A mechanism that surfaces the whole population is indistinguishable from one that")
        print("  works, and passes every positive test. TREAT THIS AS A FAILING RUN, not an agenda.")
    for row in quiet:
        print("  %s  (lifecycle=%s, revalidate=%s)"
              % (row["subject"], row["lifecycle_class"], row["revalidate_state"]))
        for d in row["record_defects"]:
            print("     (defect) [%s] %s" % (d["code"], d["why"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
