# WATER-TEST RECORD — aum-metrics end-to-end push (Andrew-direct 1408Z)

**Author:** 1.0.0_SA_CTO (Leg-2 owner + record keeper). **Closed:** 2026-08-04 ~15:55Z, INTERIM
vintage — the fresh supersede (GO'd 1550Z, in flight) is the named follow-on; this record closes
the operator-ordered interim end-to-end.
**Order:** Andrew-direct verbatim @`ANDREW_DIRECT_20260804_1408Z_AUMMETRICS_E2E_PUSH.md`
("push that generation end to end and water test it end to end" / "we cannot wait for a schedule").
**Serve ruling:** SERVE with 4 conditions (142446Z to COO) — all four held; per-scope vintages
below discharge condition 2.

## Verdict: PASS (interim) — 4/4 GENERATED, BRIDGED, SERVED, RENDERED, every leg observed

| Leg | Evidence (all observed, none inferred from a prior leg's rc) |
|---|---|
| 1 GENERATE | 49f: 0.4.0_DS 14:23:29Z, tie 5/5 per-model TO THE CENT @ spine idx 434, provenance-in-content. global 14:56:00Z + inflection 14:56:04Z: 0.2.0_DS, tie 7/7 each. CROSS-DERIVATION PARITY: both DS seats independently derived global+inflection via DIFFERENT paths (spine-side vs served-timeseries-side) and tied to the cent — legitimate two-leg evidence (derivations differ; shared-derivation law satisfied). |
| bridge | The accrual `--only` scope skip found + named (0.2.0's run bridged its own two scopes, skipped 49f by construction); 49f bridged 15:24:26Z, byte-identical ETag 9b9ef9b0… to the 14:23 source. |
| 2 ARTIFACT (CTO) | Full-paginated listings to file w/ rc+stderr controls (denominators 456→458→459). Per-scope served vintages: **cottonwood** 3,117B as-of **07-24** (stalest; pair+accrual path, pre-dates the push); **49f** 4,138B period **07-30**; **global** 5,908B period **07-30** (meta.source_spine/as_of_basis ABSENT — one-hunk asymmetry fix queued; `_provenance` carries vintage, serve condition 1 satisfied); **inflection** 4,306B period **07-30**. |
| 3 SERVE | Publisher fires 14:59:06Z (0.2.0_DS, attribution closed; resource policy = scheduler-only event source, so off-schedule = deliberate IAM invokes) + 15:44Z (0.7.0_AE, post-bridge). ETag-verified live. **Completeness-claim blindness EXERCISED live**: `all_present=True` printed at 11/11 and 13/13 while absent keys existed — derived-denominator, predicate-not-roster class → fix rides CI-R7R8. |
| 4 RENDER | 0.4.0_DE, deployed PROD bundle: cottonwood ($463M) · global ($1.96B) · inflection ($205M) · 49f ($1.70B, 15:49Z) — **4/4 VERIFIED-RENDERING.** Yang's ULT/LT names render canonically (rename ruled out as blank-cause). No FE changes (condition 4). |

## Root cause (source-confirmed, 0.7.0_AE)

Orion JWT TTL 10h (iat 08-03 21:01:02Z, exp 08-04 07:02:02Z); refresher UTC-fixed cron(0 13)Z
(CTO April anti-contention ruling) collides with the clock-v3 floor (09:00 ET = 13:00Z in EDT);
EC2 warm/cold decides the race — today cold, 66s, **lost by 12 seconds** → 401 ×9 at 13:01:15Z →
stage-1 death → stages 2-5 skipped → 6e never ran → 1-of-4 at 09:50 publish. **Standing window:
every morning 07:02Z-13:01Z the estate's only Orion token is expired.**
Fixes worded: **F-A GO** cron(15 12)Z (≥45min DST-safe lead, off hazard marks year-round; riders:
full TF law + the JWT chain added to the T2C clock-member table in the same commit) · **F-B**
stage-0 pre-pull exp gate (COO→DS, fail-LOUD named) · fresh supersede GO (full chain from the
floor, token exp 23:02Z).

## Forensics closed

08-03 no-cycle = pre-clock-v3 event-only-trigger class (the floor itself, which fired on its mark
today, is the closure). Publisher exonerated (correct-given-inputs at 09:50). Poisoned-prefix
mechanism CONFIRMED at the bronze listing (401-failed pull writes `_meta/`-only date prefix →
`resolve_bronze_date` counts the prefix as availability → roll-forward defeated exactly when
needed). Pre-6e-vs-6e-failed discriminator closed on 0.4.0_DS's log read (:16-24/:128/:244).

## Post-test queue (all authorized, reviewed path, NOT mid-test)

1. 0.4.0_DS roll-forward resolver one-hunk (model-bearing partitions only).
2. 0.2.0/0.4.0_DS global meta-asymmetry one-hunk.
3. Publisher completeness fix — rides CI-R7R8 (roster-derived expectations).
4. F-A apply + F-B gate (worded above). 3 stale-comment cleanups ride F-A.
5. **NEVER#4 acceptance stays OPEN** — a SCHEDULED run proving the chain is the acceptance event;
   today's direct invokes are operator-ordered interim, never acceptance evidence.

## CANRTE census additions (banked)

Cottonwood pair+accrual path ≠ 6e (another divergence) · two DS staging homes (gold/mdpf_revamp
vs portal/gold dated tree) · the accrual `--only` scope-skip class · cross-firm hardcoded read in
the 49f builder (scope SS6) · UTC-vs-ET run_date basis (cot retry-net, cross-pipeline) — five
same-class specimens in one day: convention divergence inside a chain is structural, not
MDPF-local.

## SUPERSEDE ADDENDUM (closed ~17:57Z) — the interim is RETIRED; fresh 4/4 at the T-1 frontier

Condition-3 executed across four rounds and CLOSED at the serve (AE 175723Z, live-verified
head-object + content, never the lambda summary): all four `aum-metrics` stamped 17:53:44-45Z —
**49f / inflection / global @ 2026-08-03** (the T-1 frontier), **cottonwood @ 2026-07-31** (its
roster-declared cadence frontier, up from 07-24). Cottonwood serves 5 canonical by_model rows,
NO moderate-income row, meta residual {$6,220,375.05 / 8 accts, G8 standing ruling cited} — the
ruled shape exactly. One cent-level staged-vs-served read flagged to 0.2.0's six-signal pass.

**The classification arc inside the supersede** (the record's second incident-as-evidence):
'Opal Moderate Income Portfolio' (new BD strategy, $5.0M/6 accts) → vocabulary gate refused
LOUD → three-way discriminator (CRO branches incl. the residual-conversion stop) → pre-refinement
mint landed → CRO sharpened to COMPOSITION-PRESENCE → DS proved ABSENT on the blend-table oracle
(30-row full read, 16 parents) → revert @54b15511c → round-4 green. **Controls that held: the
global composition gate refused the $5.0M misclassification TWICE (delta = the amount to the
dollar); AE's listing-derivation full hold kept disputed content off the serve.** Stale-beats-
misclassified ruled and vindicated.

**Two architecture findings banked to CANRTE from the supersede rounds:**
1. **Staged-input deadlock (AE):** stage 6a reads staging BEFORE 6d can rebuild it — a gate that
   refuses on poisoned staging also blocks the run that would FIX the staging; self-heal gap,
   design note for the canonical route's stage contract.
2. The mint-free re-stage by 0.2.0_DS was the deadlock break — cross-seat, correct, on the
   reviewed path.

Remaining open (unchanged): NEVER#4 acceptance (a SCHEDULED run proving the chain), the
post-test one-hunk queue, and the F-A first live exercise tomorrow 12:15Z.

## Compiler Tools

comp-routes trace/origins (pointer chain + real origin bucket) · comp-trigger (publisher schedule
forensics: live ENABLED cron(50 9) ET, NOT in TF — hygiene item) · comp-pipescript io (SS6
evidence) · full-paginated `aws s3 ls` to file ×4 with denominators + stderr controls ·
`aws scheduler get-schedule` / `logs filter-log-events` (the 09:50 run log, 17 events) · content
parses via s3 cp-to-stdout (4 artifacts).
