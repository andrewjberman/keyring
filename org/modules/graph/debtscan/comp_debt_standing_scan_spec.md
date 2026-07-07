# NFRA_DEBTSCAN -- comp-debt standing-scan SPEC (DS-authored -> AE-build)

**Author:** 0.4.0_DS_ClientPlatform~A | **2026-07-07** | **Status:** SPEC -> RAVC COO -> AE-build (0.8.0)
**Purpose (TO item 3):** turn the debtscan from one-shot per-family CENSUSES into a STANDING scan --
the design-stage keystone becomes a running, self-alarming scan. DS authors this spec + the per-family
query-logic; AE builds `comp-debt`, wires the schedule + hook, commits to the canonical home
(infra/aws/globgrph, AE lane).

## What comp-debt IS
A thin standing-scan ORCHESTRATOR over the existing per-family scan surfaces (query-don't-rebuild, Rule
20). It does NOT re-derive; it dispatches each family to its right source, applies the shared gates
SEPARATELY, emits a dated ledger, and ALARMS only on a NEW finding (not in the last CVO-adjudicated
baseline). One scan, many families, no silent suppression (CTO cond-1: every suppressed finding logged).

## Family registry (each scores off the RIGHT surface)
| Family | Source | Scorer | Gates |
|---|---|---|---|
| REACHABILITY (D1) | comp-kuzu (kuzu_nessie + stitch) | isolated 0-edge sweep by type | suppression_v1 (FP_* classes) |
| CANON-MOTIF (D3) | canon_motif_scorer (kuzu/deploy-ledger/pipescript) | dominant-motif + outlier tail | twin_shadow_guard + suppression_v1 |
| DUPS | comp-dups v2 | lexical-twin pairs | DUP_BENIGN_* predicates (pending CVO per-class) |
| COMPOSITION (D2) | comp-kuzu | field/schema drift | suppression_v1 |
| DEPLOY (D4/D5) | deploy-ledger cross-ref | orphan code-prefix / portal sweep | suppression_v1 |
| IAM | comp-iam gaps | effect==Allow public/missing-perm | FP_CROSS_FIRM_DENY_GUARDRAIL (Deny=guardrail) |

## Standing-scan mechanism (the AE-build target)
1. **Schedule:** a daily EventBridge -> a small Lambda (or fold into an existing daily monitor), same
   shape as the NFRA_SILVERFRESH alarm. (Or ride the existing nightly graph-derive cadence.)
2. **Per run:** `comp-kuzu` FRESHNESS-ASSERT first (header current / pin==marker; refuse-or-warn on
   BEHIND/UNKNOWN-VINTAGE -- the marker-oracle discipline; a stale surface poisons the scan, cf. the D1
   stitch 592h-stale finding). Then dispatch each family -> score -> apply gates SEPARATELY (twin-shadow
   THEN suppression, each logged) -> residual = ADVISORY candidates.
3. **Ledger:** emit `org/modules/graph/debtscan/comp_debt/{date}.json` -- per-family {census_count,
   suppressed_count, twin_cleared_count, residual_candidates[], provenance-header}. The scorecard md is
   the human view; the json is the diff surface.
4. **ALARM (the standing value):** diff residual_candidates vs the LAST run's CVO-ADJUDICATED baseline.
   A NEW candidate (not previously adjudicated) -> alarm (Namespace Debt/Scan, dim=Family) -> routes to
   CVO. A RETIRED candidate (a fixed one) -> log the close. No re-alarm on an already-adjudicated finding.
5. **Baseline:** the CVO-adjudicated set is the alarm baseline; CVO rulings update it. This is what makes
   the scan STANDING (not re-flagging known debt) rather than a noisy re-census.

## Freshness is a first-class gate (banked from D1)
Every kuzu-family run asserts surface freshness BEFORE scoring, and the ledger records the provenance
header. The D1 drive proved WHY: a scan over a 592h-stale stitch (or a grain-regressed snapshot) silently
mis-scores (0-edge = "orphan" when the edge just wasn't rebuilt). comp-debt refuses-or-warns on a stale
surface rather than emit a freshness-poisoned scorecard -- the grain-sentinel discipline, scan-level.

## Interfaces DS hands to the AE-build
- Per-family query-logic: REACHABILITY sweep (kuzu Cypher, authored); CANON-MOTIF (the D3 scorer design +
  queries); DUPS predicates (in suppression_v1 already). AE wires them into the `comp-debt` runner.
- The gate application order + the no-silent-suppression logging contract (above).
- The ledger json schema + the alarm-diff-vs-baseline logic (above).
AE owns: the runner skeleton, the kuzu-lib read (post-freshness-assert, NO Python->comp-* subprocess on
Windows -- banked), the EventBridge/Lambda schedule, the CloudWatch alarm, comp-manifest-check register,
and the canonical commit.

## Sequence
1. RAVC this spec + the D3 scorer design -> COO -> AE-build assignment (0.8.0).
2. AE builds comp-debt (REACHABILITY + CANON-MOTIF families first -- census-validated) + the schedule +
   alarm; DS pairs on the query-logic + validates the ledger reproduces the census numbers.
3. Register + go standing. CVO baseline seeded from the current adjudicated sets.
