# FILLED-VIA-HISTORY Executed: the Hole's Event History Landed as Vendor Bytes — 0.4.0_DS_ClientPlatform~B

**archetype:** IMPLEMENT
**Date:** 2026-07-16 (18:26Z–18:50Z)
**Task Order:** ad-hoc (CTO GO 164833Z on the WP1 census recommendation; queued behind the D_04 P0 per CTO, unblocked at his 182432Z gate-close)
**Status:** COMPLETE — conditions 1-3+5 discharged, 4 handed to 0.7.0

---

## Objective

Execute the FILLED-VIA-HISTORY-ARTIFACTS window pull per the prior ~B session's census recommendation:
land the 07-13..07-15 eclipse hole's event history as the vendor's own shapes, additively, under
`bronze/eclipse/_history/`, with the call census + landed-key listing as the acceptance artifact.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| (none applicable) | — | SKIPPED | one-shot vendor-API window pull + S3 landing: no comp-tool models the Eclipse vendor surface or the _history landing; every raw boto3 inspection carried `# rail-checked:` markers (pre/post listings, overlap measurement, re-run verification) |

**What worked:** the run-time denominator gate (script-internal, comp-style discipline) aborted on the 21-vs-18 mismatch before any vendor call.
**What failed:** n/a.
**Gap found:** none new (the io-manifest gap was logged in the P0 session log).

Appended one line to org/compiler-tools-log.md.

---

## Work Completed

### 1. Proposal recovered + arithmetic corrected BEFORE pulling
Recovered the exact proposal from `ECLIPSE_ENDPOINT_CENSUS_WP1_CLOSE_20260716.md`. The run-time
denominator derivation (from the same held discriminator source, `bronze/eclipse/2026-07-16/
portfolios_simple.json`) returned 18 changed portfolios vs the proposed 21 — gate ABORTED pre-call.
Measured: |edited|=18, |created|=3, created ⊂ edited (1419/1420/1421 carry both stamps in-window);
"21" summed overlapping sets; the true set byte-matches the census's own printed ID list. Gate
re-anchored to that list; pull proceeded.

### 2. The window pull (18:36–18:45Z)
55 vendor calls, 55/55 HTTP 200, 55 keys landed as RAW response bytes (17a-strict — no
re-serialization) under the four proposed types:
18 portfolio auditlogs (ALL non-empty; created trio carries Insert+Update rows) · 18 model auditlogs
(ALL honest-zero → "models static across the hole" upgraded to roster-wide exercised) ·
closed_trades 11.74MB (2,937-row ledger w/ at-trade values) · 18 trade_instances (3 non-empty:
portfolios 165/468/1381). Pre-listing proved `_history/` EMPTY (additive); ListObjectsV2
key+ETag+size acceptance listing printed; gold/meta held keys untouched. Egress count logged: 56
(55 window + 1 SMOKE), standing JWT via SM, ORION standing lift.

### 3. Conditions
(1) vendor shapes only ✓ (2) census+listing acceptance ✓ (3) additive-only ✓ — incl. one accidental
script re-invocation that the additive gate aborted pre-call (verified zero effect: 55 keys, newest
mtime 18:44:43Z) (4) manifest amendment → 0.7.0's authorship, handoff message 184940Z with the
union-correction carried (manifest should record 18, not 21) (5) doc catalog-pointers landed
in-window @ b06048dd5.

### 4. Artifacts
`ECLIPSE_HISTORY_WINDOW_PULL_ACCEPTANCE_20260716.md` + `eclipse_history_census_2026-07-13_2026-07-15.json`
(lane deliverables) @ `4d085af8d`, pushed. Closure messages: CTO 184927Z, 0.7.0 184940Z.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Abort-and-measure on the 21-vs-18 mismatch instead of pulling the printed IDs | the denominator disagreement had to be MECHANISM'd (union-vs-sum) before any egress; 30-second measurement settled it decisively |
| Per-id raw files rather than one aggregate per type | aggregating 21 responses wraps vendor bytes in our envelope — 17a-strict is per-response bytes |
| Gate re-anchored to the census's printed ID list, not a count | a list-equality gate cannot be satisfied by a coincidence of counts — the exact failure class 0.6.2 corrected today |

---

## Blockers

None.

## Next Steps

- **[0.7.0_AE_CloudOps]** holes-manifest amendment on the landed evidence (GO condition 4); carries 18-not-21.
- **[1.0.0_SA_CTO]** D3 arch-spec catalog pointer (routed separately by 0.7.0, his lane).
- **[me]** none open on this package; silver leg stays today-forward per the proposal.
