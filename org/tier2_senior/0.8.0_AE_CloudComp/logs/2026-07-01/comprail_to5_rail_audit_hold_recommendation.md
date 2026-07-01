# NFRA_COMPRAIL.TO-5 -- post-enforce telemetry + broad-grep-tier FP/TP -> HOLD (the COMPRAIL close TO)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE
**Serial:** 0.8.0_AE_CloudComp~E
**Date:** 2026-07-01
**Window:** COMPRAIL.TO-5 GO ~0455Z -> ~0503Z
**TO:** NFRA_COMPRAIL.TO-5 (COO~B GO; the COMPRAIL close TO; I own the rail-log via COMPLEARN's tool_activity)

## Current State

Batch-GO'd COMPRAIL.TO-5 (the close TO) after COMPLEARN closed + the affinity track parked at shadow.
**TO-5 DELIVERED:** the post-enforce telemetry + the broad-grep-tier FP/TP audit + a grounded HOLD
recommendation. comp-rail-audit committed `3b87a05a1`, pushed. The COMPRAIL CLOSE finalizes on COO~B +
CVO~B's disposition of the HOLD (their friction-sensitive gate; I recommend, they decide).

## What was built

`org/modules/graph/comp_rail_audit.py` -- the post-enforce telemetry tool COMPRAIL lacked. Re-parses
the raw comp-which-rail.log (recovering the `class=` + `q=` fields that tool_activity's parse_rail drops
for DENY/OVERRIDE -- the intent-level signal the audit needs). Answers the two close questions:
- **Telemetry:** route/on-rails-run/deny/override distribution + coverage gaps by class.
- **Broad-grep FP/TP:** scoped to GOVERNED repo-grep (grep/find invocations only), classified legit-raw
  (FP) vs should-route (TP) -> a GO/HOLD/NO-GO recommendation (advisory; no settings change).

## Findings (reproduce: `python org/modules/graph/comp_rail_audit.py`)

**Telemetry (enforce window 2026-06-22 -> 2026-07-01, 2256 events):**
- rail-found 89% (ROUTE 55% + on-rails comp-grep/comp-glob 34%); DENY 9%; OVERRIDE 2%. Agents ARE
  finding the rail.
- Coverage-gap classes (repeat DENY/OVERRIDE = a build-next/routing candidate -> COMPLEARN):
  aws_freshness 95, infra_grep 89, aws_iam_inspect 31, aws_deploy_verify 12, comp_which 11, aws_dynamodb 6.

**Broad-grep-tier FP/TP:** 27 of 249 deny/override blocks are GOVERNED repo-grep (the rest are aws-
inspection = tier-1 already live, or pipe-consumers = free). grep-FP rate 4% (26 should-route, 1
legit-raw) -- but several of the 27 are dryrun/test fixtures (__comprail_gate_dryrun__.tf, repeated
identical greps), thinning the real signal. NUDGE adoption: 769 comp-grep/comp-glob on-rails runs.

**RECOMMENDATION: HOLD** (advisory; the settings-matcher change is COO+CVO's gate). Grounded on:
1. DATA-SUFFICIENCY: only 27 governed-grep events, all from the narrow .tf tier (broad repo-grep is
   NUDGED, not denied -> ZERO direct broad-tier FP evidence). A fabric-wide hard-DENY off <30 points
   (some dryrun) is flying blind. The low 4% FP is on data too thin/narrow to trust for a friction gate.
2. The NUDGE already works: 769 comp-grep adoptions achieve most of the tier's goal WITHOUT hard-deny
   friction. Keep the tier STAGED-BY-DESIGN; gap classes -> COMPLEARN. Per the TO, a grounded HOLD IS a
   valid close.

## Compiler Tools

| Tool | Command | Result |
|---|---|---|
| comp-to | set TO_ID = NFRA_COMPRAIL.TO-5 | PASS |
| tool_activity parse_rail (reuse) | rail-log action distribution + RUN-OVERRIDE inspection | PASS (found overrides opaque -> re-parsed raw) |
| comp-rail-audit (built) | full telemetry + FP/TP + recommendation | PASS (89% rail-found; grep-FP 4% on 27 thin events -> HOLD) |
| ds-commit-gate.sh | comp_rail_audit.py | PASS |
| safe-commit.sh | 3b87a05a1 (~E author) | PASS (surface-check clean) |

**What worked:** re-parsing the raw log to recover class=/q= (parse_rail drops them for DENY/OVERRIDE)
gave the intent-level signal. **What failed / self-caught:** my FIRST-cut FP/TP lumped aws-inspection
(tier-1) into the broad-grep population + counted compound `echo && aws` commands as over-matches -> an
inflated 82% FP. Corrected by SCOPING to governed repo-grep only (grep/find invocations, not aws, not
pipe-consumers) -> the honest 4%-on-thin-data picture. Same grounding discipline as the P2 DENY-blob
catch: scope + ground before trusting a rate. **Gap found:** the rail-log does NOT capture the DENY
command / OVERRIDE reason in a parsed field (parse_rail drops class=/q=); a `class` dim in tool_activity
would make the class-level coverage-gap analysis first-class (a COMPLEARN P3 candidate).

## Blockers

None. The COMPRAIL close finalizes on COO~B + CVO~B's disposition of the HOLD (their friction-sensitive
gate -- a real external decision, not a blocker). My TO-5 deliverable (telemetry + FP/TP + recommendation)
is complete.

## MCP traffic

~5 messages. ACK COMPRAIL.TO-5 GO -> COO~B; RAVC2 TO-5 (telemetry + HOLD recommendation) -> COO~B + CC
CVO~B (co-gate) + CC CTO (coverage-audit).

## Next Steps

1. **[2.0.0_SA_COO~B + 3.0.0_SA_CVO~B]** dispose the broad-grep-tier HOLD recommendation (their gate) ->
   CLOSES COMPRAIL. If they concur HOLD: the tier stays staged-by-design, no settings change.
2. **[0.8.0_AE_CloudComp~E / self]** the coverage-gap classes feed COMPLEARN's value-scorer (already
   wired -- comp_learns_score reads the rail-log); a `class` dim in tool_activity = a COMPLEARN P3
   candidate (makes class-level coverage-gaps first-class).
3. **[me]** Phase-B co-sign priority-interrupt STILL ARMED; COMPROUTE step-3 outcome-capture data-gated.
