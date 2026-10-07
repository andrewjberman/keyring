# MDPF_HEALGAP -- L1 midstream brief: a source that recovers, an ingest that never re-runs

**Author:** `4.0.0_SA_CRO~DELL1`. **Mode:** `/brief-create --midstream`. **Directive:** D8.
**Authority:** Andrew-direct 2026-10-07 ~07:52Z, record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_075xZ_MDPF_HEALGAP_THROUGH_CANONICAL_FLOW_CRO_WITH_CTO.md`.
**Consumer:** `1.0.0_SA_CTO~DELL1`, `/endpoint --forward` (L2).

---

## PART 0 -- How the blind constraint was honoured, and where it bent

1. **Read on purpose (admissible):** the 2026-08-31 purpose brief `docs/architecture/MDPF_HEALGAP_BRIEF.md`; the
   live Terraform for the runner and the session schedule; a bronze census in S3 measured at this seat (Part VI);
   the header of the shipped module `data/mdpf/scripts/gold/mdpf_gold_catchup.py` (substrate, Part IV).
2. **Not read:** any task order of this project, the decomp run under `workflows/atom_decomposition/`, CTO rulings
   batches 69-75.
3. **WHERE IT BENT:** the project's `phase`, `blocking` and `leads` fields live in the same JSON as its purpose, and
   I read the whole file before this skill loaded. I therefore know: the decomp's cell list exists; a CTO ruling made
   the gold catch-up "cell 1"; a CVO grade found the served Cottonwood point absent on 11 of 28 trading days; the
   runner's fire time precedes its session's mint (lead L4b). A git log subject also told me cell 1 shipped.
4. **Containment:** no outcome below is cut from those fields. O1-O4 rest on the original purpose brief plus my own
   bronze measurement. O5 (ordering) rests on the two Terraform files I read myself, though lead L4b pointed me at
   them. The CVO's served-point finding is used only to bound the boundary in Part II, never as an outcome.
5. **Finding on direction: MOSTLY UNCHANGED, WIDER.** The endpoint the 2026-08-31 brief named still stands. Two
   things changed it: the hole is 11 days in one feed rather than 1 day in three (Part VI.2), and the one
   mechanism shipped under this project's name heals the gold layer and by its own design does not reach this
   hole (Part IV.3). That is a sign the problem lies in what the work was cut to target, not in the direction.

---

## PART I -- THE OUTCOME TERRITORY

**CANDIDATE THREAD (FWD-1):** a reader of the Cottonwood series in Model Portfolios, on a day when the morning
Rebalancer pull fails because the vendor session expired. Scope is one firm (Cottonwood), one runner
(`cot-rebalancer-runner`), its three bronze feeds and the default window. The thread runs end to end from failed
pull to session heal to re-pull to that day's served point, with nobody acting.

### O1 -- A reader sees a morning-failed day filled the same day, with nobody acting
When the morning pull fails and the vendor session heals later that day, the reader of the Cottonwood series sees
that day's point once the day's pipeline completes. No seat and no person has to notice the failure or start the
re-run.

### O2 -- An operator can trust that "the runner succeeded" means every feed landed
A run where one feed lands empty while its siblings land is a recovery case, never a success. An operator reading
the run's outcome learns which feed is missing for which date from the run itself. They do not need to list S3.

### O3 -- An operator can close an existing bronze hole with one act that names its own targets
For a date already holed at bronze, the operator runs one repair act. The act names the dates and feeds it will
fill before it calls the vendor, and it fills exactly those. It repairs. It does not notify (the moratorium and the
GLOBALALARM hold stay as they are). Each use stays under Andrew's per-use vendor word.

### O4 -- An auditor reading the runner's configuration learns the truth about its tolerance
An auditor reading the config sees the retry behaviour the function actually gets. Today the config states a
six-hour window that AWS cannot deliver to a function that raises (2026-08-31 brief section 3).

### O5 -- An operator reading the schedules sees each pull placed after the session it depends on
An operator reading the two schedules sees the runner fire after its session's daily mint, not before it. This is
a mitigation that makes O1 rarer. It does not replace O1.

### O6 -- The estate owner can say which other scheduled ingests share this shape, each answered
The estate owner can name every scheduled ingest whose success depends on a vendor session that heals outside the
ingest. Each one is answered "covered by O1's mechanism" or "not exposed, because ...". The 49F session chain is
the first candidate (2026-08-31 brief section 4). This brief makes no claim that 49F is exposed.

---

## PART II -- WHERE THE BOUNDARY SITS

1. **OWNS:** recovery at the INGEST layer for the Cottonwood Rebalancer bronze feeds (O1-O5), and the class answer
   (O6).
2. **RELIES ON, does not own:** the session chain `cot-bd-session-trigger` and its daily schedule (owner lane
   `0.6.2_AE_PartnerETL` per `cot-pipeline/lambdas.tf` header); the bronze-to-silver `on_success` destination on the
   runner (WSE_COTMDL WS-5); the gold catch-up `mdpf_gold_catchup.py`, which is already shipped.
3. **The gold catch-up is DOWNSTREAM of this project's hole, not a fix for it.** It re-values holdings dates at
   gold and by its own header never covers a date with no assignment partition. A bronze model_detail hole produces
   exactly such a date. Gold catch-up and ingest recovery are two layers. The PRD should say which layer each FWD
   grades at.
4. **SIBLINGS, named:** `MDPF_COTREMEDIATION` (Cottonwood served-point remediation, closed with rows placed here);
   `WSE_COTMDL` (built the runner and its `on_success` chain); `COT_CANON458`; `GLOBALALARM` (D10, all alarms held;
   no O here may become a notifier); `ADVI_COTBKF` (a Cottonwood backfill project live on dell2. Its scope relative
   to this one is UNREAD by this seat, and the CTO should settle the boundary at L2).
5. **OUT:** any monitor, alarm or freshness checker. Backfill of dates nobody has shown to be holed. Gold-layer
   valuation rules.

---

## PART III -- THE QUALITATIVE BAR

1. On a day the morning pull fails and the session heals the same day, nobody in the estate has to know it
   happened for the series to be whole by end of day. The alternative it displaces: a seat later notices a gap in a
   served chart and asks Andrew for a vendor re-pull.
2. A reader of a run's result would never call a run with an empty feed "succeeded". The alternative it displaces:
   listing S3 by date to find out.
3. An auditor who reads only the Terraform would predict the runner's real retry and timing behaviour correctly.
   The alternative it displaces: the 2026-08-31 config, which predicts the opposite of the truth.
4. The repair of an old hole is something an operator does once and finishes, not a standing comparison or a
   report.

No numbers are set here. The recovery window, the retry count and the fire time are L4 mechanics.

---

## PART IV -- THE SUBSTRATE

1. **FINDING, mechanism exists on this resource:** the runner already carries `destination_config { on_success }`
   to the silver converter (`infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf`, the `on_success` block after
   `maximum_event_age_in_seconds`). Any completion-keyed design is an edit to an existing mechanism (build-ladder
   rung 2), not a new one.
2. **FINDING, the heal has a declared TF-managed cadence:** `aws_scheduler_schedule.cot_bd_session_daily_et`,
   `cron(30 7 * * ? *)` America/New_York (`infra/aws/terraform/cot-pipeline/schedule-et.tf`), commented as an
   Andrew-direct placement with a 54-minute EST-worst-case margin to the 13:30Z floor. The runner fires at
   `cron(0 6 * * ? *)` UTC, still marked `PLACEHOLDER` in the file. Measured at this seat 2026-10-07: the file is
   unchanged since `27a3a98cdc` (2026-08-25).
3. **FINDING, the one shipped HEALGAP mechanism is gold-layer:** `data/mdpf/scripts/gold/mdpf_gold_catchup.py`
   (header lines 1-31) runs inside the daily consolidator, rebuilds unvalued holdings dates, "never calls a vendor",
   and leaves dates without an assignment partition absent (reason `NO-ASSIGNMENT-PARTITION`). It is canonical in
   shape (no schedule and no output path of its own) and is the right precedent for "a step of the one pipeline,
   not a second pipeline".
4. **FINDING, the declared tolerance is unreachable:** `maximum_retry_attempts = 2` beside
   `maximum_event_age_in_seconds = 21600` on the same resource (read at HEAD 2026-10-07). AWS caps async retries at
   2, so the six-hour window is never reached for a raising function (2026-08-31 brief section 3, unchanged).
5. **FINDING, prior art elsewhere:** `infra/aws/terraform/smartx-pipeline/assets-pull-onsuccess.tf` chains a daily
   pull with `on_success` (2026-08-31 brief section 5).

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

1. The runner's idempotency guard must work before any second attempt exists. On 2026-08-31 it read as dead
   (missing `s3:GetObject` on the complete stamp; 2026-08-31 brief section 6.1). Its state today is UNREAD at this
   seat.
2. A completeness test per feed must exist for O2 to be gradeable. "Landed" has to mean all three feeds for the
   date.
3. Any fire-time move (O5) re-derives the 13:30Z floor margin first, because the mint time is itself an
   Andrew-direct placement.
4. Every vendor call made by a repair (O3), and every new recurring vendor call (a second attempt), sits under
   Andrew's per-use vendor-egress word.
5. Any O1 mechanism must satisfy the moratorium line: it must fix, not notify.

---

## PART VI -- STATUS -- NOT OUTCOME-BEARING

Measured 2026-10-07 ~08:05Z at this seat via `.tools/aws s3api list-objects-v2`, bucket `opal-data-assets`, prefix
`blackdiamond/cottonwood/bronze/<feed>/`, window 2026-07-21..2026-10-07 = 79 calendar days.

1. `rebalancer_models` 79 of 79 dates present; `rebalancer_accounts` 79 of 79 present.
2. **`rebalancer_model_detail` 68 of 79 present; MISSING 11 consecutive dates, 2026-08-31 through 2026-09-10.**
3. 2026-08-31 for models (1 object) and accounts (5 objects) was written **2026-09-01T02:50Z**, which is the late
   one-shot re-run. model_detail for that date was not filled by it.
4. On 2026-09-05, models (1) and accounts (5) landed at 06:04Z, yet model_detail has no partition that day. So for
   ten days the runner landed two feeds and not the third. **That is not the session-death case.** Its cause is
   UNREAD here (Part VII). It is the evidence behind O2.
5. Controls: 2026-08-30 model_detail 83 objects at 06:00:45Z; 2026-09-11 81 objects; 2026-10-06 91 objects. The
   same command shape returns real counts on both sides of the gap.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

1. **Why model_detail stopped for 2026-09-01..09-10 while its siblings landed.** It could be a scope setting, a
   vendor-side change or a code path. It is not measured here. It may be a second cause class, separate from
   session death.
2. **The served-layer effect.** I did not read the served Cottonwood series. The 11-of-28 absent-point figure is
   another seat's grade, and I know it only through the leak in Part 0.
3. Whether the runner's idempotency guard (Part V.1) has since been repaired.
4. Whether 49F or any other firm is exposed (O6 asks; this brief does not answer).
5. The relation to `ADVI_COTBKF`.
6. Every S3 read here is one instrument (s3api, one plane). No second plane corroborates the census.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/mdpf-healgap-midstream-brief-20261007.md
  PROJECT           MDPF_HEALGAP (org/projects/MDPF_HEALGAP.json), directive D8
  EXISTING PRD      NONE (docs/architecture/MDPF_HEALGAP_BRIEF.md is a 2026-08-31 purpose brief, not a PRD;
                    D8 directive PRD docs/architecture/D8_MODEL_PORTFOLIOS_PIPELINE_FORTIFICATION_PRD.md)
  SIBLING PROJECTS  MDPF_COTREMEDIATION, WSE_COTMDL, COT_CANON458, GLOBALALARM (D10), ADVI_COTBKF (boundary unread)
  PRIOR ART         cot_rebalancer_runner.tf on_success block; cot-pipeline/schedule-et.tf session schedule;
                    data/mdpf/scripts/gold/mdpf_gold_catchup.py; smartx-pipeline/assets-pull-onsuccess.tf
  MEASURED AT       2026-10-07 ~08:05Z (S3 census, Part VI); Terraform read at HEAD a984cc37d2
```
