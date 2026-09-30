# AMGT_HARVST task order -- `HVST-ab-3` -- ROUND 29 chain 1 (after `ab-1`): BACKFILL BATCH 1, 10 NAMES x {bbg, wsj}, MEASURED-FIRST UNDER A PAIR -- ITS MEASURED PAGES RE-BASE THE 180-NAME CEILING (FWD-9, FWD-7, FWD-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ab-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~83</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector task is Disabled; ONE manual collection and its upload. It enables nothing.
comp-iam: RUN at L5 -- vendor egress to bbg and wsj by the collector script only (R-21 @b390c36444); S3 PUTs: the persisted run record, the upload's bbg/wsj bronze and silver. NO DELETE, NO ft/barrons/sa call, NO gold write, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a run that spends pages past its printed plan, or a "measured" page count read from the plan instead of the run. AC1 caps the requests at the pre-run print; AC2 reads the pages spent per (name, publisher) from the persisted run record and the listing bronze.
</preflight>

## 0. BEGIN ONLY WHEN ALL FOUR HOLD

1. `HVST-ab-1` is `complete` and merged on CLOUD. The dispatch names its merge.
2. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round29/NEVER_WIDEN_HALF_COO_AB3.md`;
   - `1.0.0_SA_CTO~Z`'s half.

   **Act only inside them.**
3. No other WORLD act of this project is in flight (`HVST-ab-2` does not overlap).
4. The issuer's checks exist at `.../round29/checks/`, and the act-start gate there prints OK.

## 1. THE ACT (each command that reaches a put is named in the halves)

**The 10 names** are the first 10 rows of `aa-5`'s `aa5_plan_190.json`, in file order: `2317_TT`, `2602335D_US`, `9433_JP`,
`AAPL_US`, `ABBV_US`, `ABT_US`, `ADM_US`, `AEP_US`, `AIG_US`, `AIZ_US` (each `_Equity`).

1. **The pre-run page print, first, with no request:** the collector's `plan` over the 10 names x {bbg, wsj}, floor
   `2026-01-01`, with the watermark. Print a ceiling per (name, publisher), each with its basis (MEASURED or DEFAULT).
2. **Collection, ONCE:** `run --harvest-grammar --retrieval-mode backfill --floor 2026-01-01 --new-only` over the 10 names,
   `--publishers bbg wsj`, and `--max-jobs` equal to the job count the halves name. It makes 1 S3 put, the persisted run record.
   Articles and listings queue locally.
3. **Upload, ONCE:** `upload-harvest` with the `--max-objects` the halves name.
4. **Run AC1 and AC2.**

The exact argv, the 10-name security file and the object caps are in the halves. A refusal is recorded and never retried.
A publisher's refusal ends that publisher's jobs, not the other's. Rollback is forward only.

## 2. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~83/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ab-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round29/checks/ab-3.AC1.py</invocation><expect>AC1 RESULT: PASS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-ab-3"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round29/checks/ab-3.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round28.md` @`c907537920` section 4 item 3, ruling 3. Andrew's quota word stands: brief @`6f1a72e4be`
  `:129-130`, `TO-HVST-h-10:70`.
- **The checks and halves are issuer-written after `ab-1` merges** (the `aa-2` pattern). The pre-run print is measured on
  `ab-1`'s code, whose wsj backfill bound-stops at the floor.
- **AC1:**
  - no pre-existing object moved;
  - no write on the barrons, ft or sa roots;
  - exactly one new run record, whose jobs are exactly the 10 names x {bbg, wsj};
  - listing requests per (name, publisher) do not exceed the pre-run print;
  - the outbox holds no pending bbg/wsj row after the upload.
- **AC2:** the MEASURED pages per (name, publisher), read from the run record and the listing bronze. It also prints the
  re-based ceiling for the other 180 names, with its basis per pair (measured vs default), the input to batch 2's pair.
- **NOT in this cell:**
  - the gold rebuilds that read batch 1 (they ride a later paired rebuild);
  - batches 2+ (they wait on this measurement).

**AMENDMENT 1 (issuer, 2026-09-30 ~14:0xZ) -- the round-29 re-cut (decomp section 42): PRD v0.9 `C-HV-TRUST-TOKEN`, the barrons and ft Lenovo jobs, and the schedule re-arm as phase B.**
- **The source:** Andrew-direct 2026-09-30 ~12:5xZ (CTO msg 27155): "use existing trust tokens ... not confuse rate limit for trust
  token expiry ... retry backoff"; card 4, barrons B1 yes; card 3, re-arm the schedule after batch 1, daily, for the names batch 1
  reached.
- **Section 0 item 1** now reads: `HVST-ab-1` is `complete`, with BOTH its amendments (A1: pre-floor hits are not fetched; A2:
  `C-HV-TRUST-TOKEN`), and merged on CLOUD.
- **PHASE A, the collection, ONE run:**
  - It covers the 10 names x {bbg, wsj} AND Lenovo (`992_HK_Equity`) x {barrons, ft}.
  - It runs token-first. The halves name each publisher's token source: the Secrets session for bbg and ft, and the
    saved-session file for wsj and barrons (per the CVO's 13:13Z note).
  - **Before the run, with no request:** read and classify ft's kept 403 body (`q-6` F1).
  - The pre-run print covers every (name, publisher) pair.
  - A barrons or ft refusal is recorded (token source, attempts, and class), never retried outside the bounded backoff, and it
    does not stop the other jobs.
  - AC1 counts the jobs as the 20 plus the 2. AC2 prints each job's token source, sign-in count and attempts.
- **PHASE B, the schedule, after phase A's AC1 and AC2 pass, under a RE-SIGNED pair:**
  - Give the existing harvest collection Scheduled Task ONE daily trigger. Its action runs the collector over EXACTLY the names
    phase A reached (at least one concluded job), in the mode, publishers and caps the re-signed halves name. Enable it.
  - Fire no run by hand.
  - Rollback is disabling the task.
  - Scheduled Tasks run the working tree on this device; the halves name what that checkout is.
  - The phase-B check reads the task's trigger, action argv and name file back from Task Scheduler and diffs them against
    the halves. It is named in the re-sign.
  - The first scheduled fire is graded at the next round, never waited on.
- **`<paths>`:** unchanged. **Criteria:** the same two invocations. The issuer's checks cover both phases; phase B's check is
  added at its re-sign.
- **Gate limb:** `to-pipeline-gate` grades a modified order's `<placeholders>` only (NONE).

**AMENDMENT 2 (issuer, 2026-09-30 ~14:5xZ) -- Seeking Alpha joins batch 1; the run shape follows the CLI.**
- **sa is in scope** (CTO msg 27212, @`7db0a2f4d3`): Andrew confirms the sa account is active and its credentials are unchanged.
  "sa waits on the renewal" came from one unmeasured 402 (`Z-W37-S4`, 2026-09-29 02:49Z) and is struck.
- **Batch 1 is now** the 10 names x {bbg, wsj, sa}, AND Lenovo x {barrons, ft}.
- **sa, before any sa job:** ONE account-check probe on the stored Secrets session. On a 402 or 401, retry ONCE with a fresh
  session and KEEP the response body.
  - Only a 402 that persists is a finding. It is recorded, with its kept body, and the sa jobs do not run.
  - `Z-W37-S4`'s standing follows the probe (the CVO's).
- **The run shape, measured at the CLI** (`__main__.py` ~:138): `--security-json` carries ONE security per invocation. So
  phase A's collection is ONE invocation per name:
  - 10 invocations with `--publishers bbg wsj sa`;
  - 1 Lenovo invocation with `--publishers barrons ft`;
  - each persists its own run record (11 in all);
  - then ONE `upload-harvest`.

  The halves name every argv and the per-name security files (built from `~46/securities.universe.json`). AC1 counts 11 new
  run records and 32 jobs (30 + 2).
- **`<paths>`:** unchanged. **Criteria:** the same two invocations.
- **Gate limb:** `to-pipeline-gate` grades a modified order's `<placeholders>` only (NONE).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>29</round>
<slot>~83</slot>
<fabric>site-z</fabric>
