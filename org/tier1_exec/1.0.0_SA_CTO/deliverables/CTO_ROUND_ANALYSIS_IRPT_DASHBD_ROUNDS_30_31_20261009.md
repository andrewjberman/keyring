# CTO ROUND ANALYSIS -- IRPT_DASHBD rounds 30-31 (on the CVO's joint compile)

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~00:5xZ | **Input:** the CVO's L10 slug msg 2006,
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v16.md` @c33fea078b. Both rounds MAY-CLOSE, ARMED 0.
**This supersedes** the provisional `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_30_20261009.md` (@4cfe197b0c, ADDENDUM 1 @b88cc62432).

## Measured (from the compile and the drains)

- **Within 0.35 pp:**
  - round 18 (additive add-back): 5,416;
  - DB-b-53 (compounded): 7,459;
  - **DB-b-57 and DB-b-58, independently (daily-mean fee base): 8,088 of 9,078.**
  - 762 segments moved OUT to IN, and 133 moved IN to OUT.
- **The 990 still outside are all named by class:**
  - LARGE_FLOW_DAY 170;
  - NEAR_ZERO_BALANCE 153;
  - FLOW_TIMING_AFTER_FEE_BASE 116;
  - smaller classes.
- **FLOW_TIMING (370):** 337 tie at flow-start and 0 at flow-end. Flow-end is the reader's current convention, so 0 there is by construction.
  Flow-start is closer on 356.

## Decision 1: ONE daily-mean fee-base module as the reader of record (W35-S1)

**RULING: `tieout_compound_v2.py`** (worker ~35, DB-b-57, drain @605c4cd4ac) is the reader of record.
- **Why:** it is the tie-out reader's own line (`tieout_compound.py`, then v2). ~36's `unexplained_classes.py` is a classifier that reached
  the same base independently.
- The two agree (8,088 each). That agreement is the evidence, and two homes for one rule is the defect.
- Round 32 moves v2 out of the worker deliverables folder into the project's code path. The classifier then imports its fee base from v2
  instead of computing it again.

## Decision 2: the FLOW_TIMING convention

**RULING: the tie-out reader adopts flow-START for a flow day's fee base.**
- **Why:** 337 of 370 tie at flow-start against 0 at flow-end, and start is closer on 356. The measured reference behaves as flow-start.
- **This is the reconciliation reader's convention only.** The served dashboard values do not change under this ruling.
- If a later cell finds that the served producer itself must change, that change moves served output and needs a never-widen pair
  (CLAUDE.md NEVER-1). This ruling does not authorize it.

## Enrichment list (round 32)

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | `tieout_compound_v2.py` becomes the reader of record in the project code path; the classifier imports its fee base | one module computes the daily-mean fee base (writer count printed = 1); the re-grade still reads 8,088 |
| E2 | Flow-start adopted in the reader; full re-grade | within count printed, expected at least 8,088 plus most of the 337; every segment that moves IN to OUT is named |
| E3 | LARGE_FLOW_DAY (170) | a traced cause per sub-class with counts; fixed or carried as a named class |

Drain-ends go to `3.0.0_SA_CVO` (ruling of 00:3xZ).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (2026-10-09 ~01:2xZ) -- round 32 (CVO slug msg 2029, `ADJUDICATION_v17.md` @e87c35ec88)

**Measured:**
- MAY-CLOSE, ARMED 0.
- Flow-start lands at **8,315 of 9,078**, not the "8,088 plus most of 337" this seat projected: 430 segments moved OUT to IN and 203 moved
  IN to OUT. This seat's projection was optimistic, and 8,315 is the honest figure.
- The guard threshold does not matter (8,310 to 8,319 across 1 to 5%).
- W35-S1 (one reader of record) is REMEDIATED.

**Decision 1: the two small reader fixes (W39-S1). RULED: ADOPT BOTH.**
- BD_FEE_FIELD_IS_FLOW: 23 of 26 tie.
- FIRST_DAY_FLOW_AT_START: 4 of 4 tie.

Both are in the reconciliation reader only, and served values do not change.

**Decision 2: the served pandas 2.2.3 measurement holding the activity-and-lot release (W27-S2, W31-S2).**
**RULED: neither "3.0.6 and 2.3.3 suffice" nor a new kit.** Measure on the SERVED runtime itself:
- One ad-hoc QA invoke of the deployed function, pinned to its own layer (pandas 2.2.3). It is permitted for QA and is not production
  evidence of a schedule.
- It runs the same fixture the 3.0.6 and 2.3.3 measures ran, and prints its result beside theirs.

**Why:**
- Two other versions agreeing is a bracket, not a measurement of 2.2.3. A value read from them would carry `inferred`, not `measured`.
- The served function is the object the release changes. Reading it there settles the claim without a laptop kit.

If the function cannot run the fixture as served, the cell says so with the measured refusal. Only then does a 2.2.3 kit request go to
the laptop through MSTR~DELL2.

**Round 33 enrichment:**

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | Adopt BD_FEE_FIELD_IS_FLOW and FIRST_DAY_FLOW_AT_START in the reader of record | within count printed, at least 8,315 plus the tying cases; every IN-to-OUT segment named |
| E2 | The served pandas 2.2.3 measurement, by one QA invoke | the result printed beside 3.0.6 and 2.3.3, equal or with the difference named; the activity-and-lot release proceeds or stays withheld on that read |
| E3 | NEAR_ZERO_BALANCE (153) | a traced cause per sub-class with counts; fixed or carried as a named class |

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 2 (2026-10-09 ~01:5xZ) -- round 33 (CVO slug msg 2114, `ADJUDICATION_v18.md` @73fda8626e)

**Measured:** MAY-CLOSE, ARMED 0. **8,385 of 9,078** within 0.35 pp, up from 8,315.

**RULED:**
1. **The round-34 repair cell for the two broken callers (W40-S1, W42-S1) also re-runs DB-b-65 WITHOUT its shim** (row S36).
   - Round 33's near-zero "79 fixed" was computed with `daily_mean_value` substituted under the name `mean_daily_value`, and W38-S1
     measured those as different means.
   - Until the re-run, the 79 is not counted. 8,385 is reported as "8,385, of which 79 are pending the shim-free re-run".
2. **DB-b-64's refusal is the right outcome.** The served function cannot run the lots fixture, because it packages no lots producer. That is
   the measured refusal this seat's round-32 ruling named, so the 2.2.3 kit request (ETA ~02:1xZ) stands. The activity-and-lot release stays
   withheld until the kit measure.

**Round 34 enrichment:**

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | Repair the two broken callers (W40-S1, W42-S1), and re-run DB-b-65 without the shim | each caller passes its own test; the near-zero count is recomputed on the reader of record's own mean, with the within total printed |
| E2 | The pandas 2.2.3 peak, measured on the laptop kit when it lands | the release's peak printed beside 3.0.6 and 2.3.3; the activity-and-lot release proceeds or stays withheld on that read |
| E3 | The next largest unexplained class after NEAR_ZERO | traced per sub-class with counts |

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 3 (2026-10-09 ~02:4xZ) -- round 34 (CVO slug msg 2216, `ADJUDICATION_v19.md` @d1cf2ba48f)

**Measured:**
- MAY-CLOSE, ARMED 0, 5 rows closed. Tie-out **8,433 of 9,078**.
- S36: the shim-free re-run keeps 79 of 79.
- The served-runtime measure on the pandas 2.2.3 kit: lots peak **1,500.7 MB of 2,048**, batch 1000, **7,604 accounts, total 447 s**.

**The withheld activity-and-lot release's gates, RULED:**
- **S31** (the lots stage at the 7,597-account population inside 900 s and 2,048 MB): **MET.** 7,604 accounts, 447 s, 1,500.7 MB, all on
  the served pandas.
- **S33** (the lots stage refused and crossed 2,048 MB at population scale): **MET.** The run completed at population scale under the
  memory limit. The packet must print the run's refusal count as 0, or the gate reopens.
- **S32** (the account_return_daily re-pin ships `classify_and_sum` to pandas 2.2.3): **MET only on one read the release packet must carry.**
  That read is `classify_and_sum` output on 2.2.3, equal to its tested-version output on the same fixture, or the differences named.
  This seat does not infer equality from the memory run.
- **The two halves:** the release now proceeds to its never-widen pair. The COO half goes first, then this seat's half on the packet.

**FLOW_TIMING_AFTER_FEE_BASE:** 114 of 116 within. The 2 left are named, and one needs BD's flow date. That one is carried as a named data
gap, not a fix.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 4 (2026-10-09 ~03:4xZ) -- round 35 (CVO slug msg 2299, `ADJUDICATION_v20.md` @e9d4ac3755) and FWD-11

**Measured:**
- MAY-CLOSE, 3 rows dismissed, ARMED 0.
- The R35 activity-and-lot packet was re-cut. Served-pandas peak is 1,500.7 / 1,672.3 MB of 2,048, and duration is 375 to 447 s of 900.
- The blast radius equals round 26's.
- Both halves are GIVEN: COO @cbad72eb7b, CTO @75acbfcb50. The pre-apply rollback anchor is @3285eae1a5.

**Andrew-direct ~03:3xZ (msg 2318):** "You should be doing this not just for 49 Financial, but for all clients, inflection and cottonwood
too." The PRD is amended to v0.8 with **FWD-11** @e8b44a8379. The CVO's re-sign of the ratified-text half is asked.

**Round 36 enrichment (ONE issuance):**

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | The 49 Financial R35 release APPLY under both halves | preconditions 1 to 3 in order (pins, plan exactly 0/3/0, a dry_run under 85% of both limits); A1 to A6 read on the first fire; A4 DELTA=0 before any second fire |
| E2 | FWD-11, Cottonwood: its adapter's gold `account_return_daily` from Black Diamond (C-ADAPTERS), on a sample, tied out against BD's own return (C-TIEOUT) | the sample's within-tolerance count printed with its denominator; every miss classed; no write to served gold (offline) |
| E3 | FWD-11, Inflection: the same from Orion, with lots `NO_LOTS` until Eclipse tax lots are shown populated | the same criteria, plus the lots status named per account |

Each firm's served release later goes under its own pair.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 5 (2026-10-09 ~05:2xZ) -- round 36 (CVO slug msg 2545, `ADJUDICATION_v21.md` @37daf4f637)

**Measured:**
- MAY-CLOSE, ARMED 0.
- The R35 rollback was measured live: the code is at the anchor, and the role policy is returns-only.
- 7 rows are OPEN for round 37.

**RULED, W48-S1 (Cottonwood's tie-out is 0 of 61 by structure):**
- No Commonwealth window overlaps Black Diamond's value coverage, and Black Diamond is Cottonwood's own registered master, so a BD tie-out would
  be circular. Today there is NO independent overlap source.
- FWD-11's Cottonwood tie-out clause is graded **NOT MEASURABLE**, carried as a named gap. It is not passed and it is not waited on.
  - Owner: ADVI_COTBKF (`~C2`), whose Commonwealth rebuild extends the history.
  - Un-park condition: any window where a Commonwealth-sourced value series and Opal's series both exist.
- Cottonwood's other FWD-11 clauses (the page, the gold tables, the stated gaps) proceed now.
- No cross-firm data is used to manufacture an overlap (the cross-firm rule).

**RULED, W49-S3 (two Inflection flow classes depart from the ratified `orion_cashflow_taxonomy.yaml` by measurement):**
- The ratified taxonomy governs until it is amended. A measurement does not overrule it inside a worker cell.
- `~D2` cuts ONE cell to write the amendment proposal under the taxonomy law (rule 24): the four-postulate record, a word-boundary token census,
  and the two classes' measured effect on the returns.
- Until then the adapter maps by the ratified taxonomy, and the output flags those two classes with their counts. This seat rules on the
  proposal when it lands.

**Round 37:** `~D2`'s re-cut as listed (the lots key, HEAD pins, the Orion registry row, a like-for-like compounded fee tie-out for Inflection),
plus the W49-S3 proposal cell.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 6 (2026-10-09 ~06:5xZ) -- round 37 (CVO slug msg 2703, `ADJUDICATION_v22.md` and `REMEDIATION_v18.md` @153e101791)

Round 37 MAY-CLOSE: 5 orders, 0 judgment criteria, ARMED 0, 4 rows OPEN.

### Decision 1: W49-S3, the Orion flow taxonomy -- the proposal is ADOPTED (option 4, additive keys)

Read: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~54/ORION_TAXONOMY_AMENDMENT_PROPOSAL.md`, the rule-24 record. It covers:
- MECE by subtraction from 48 entries, after a falsified domain read over 64,024 files;
- SAME GRAIN;
- INTENT COHERENCE;
- STATE COHERENCE, naming each value that does not move.

1. **The four entries gain `account_boundary`:** Internal Account Journal In (`in`), Out (`out`), and Federal and State Tax Withheld (`out`).
   - The two tax entries also gain `account_boundary_when: before_tax_return`.
   - No `bucket` and no `nna_direction` moves. Served NNA does not move, and the 2026-05-11 ratification Items 1 and 2 stand.
2. **The tax pair is IN scope.**
   - **Why:** it is a property of the return BASIS (the vendor figure is before-tax), which the qualifier states.
   - A consumer on an after-tax basis ignores the key, so it is not a fit dressed as a rule.
3. **The three declared-unmeasured members** (Foreign Tax Withheld, Foreign Dividend Tax, Tax Credit) **stay inside the value,** untagged.
   - They are measured first when a sample carries them. This is an enrichment item, not a guess.
4. **The return adapter reads the keys from the ratified file** and drops `orion_sources.json`'s `inter_account_comment` and
   `tax_withheld_comment` departure. One source of truth; this was W49-S3's defect.
5. **Measured effect, one sample (562 account-windows, 0.35 pp):**
   - like-for-like gross (Orion's gross figure): 291 to 418;
   - net: 293 to 421.
   This is a fit at one snapshot. The scheduled tie-out re-reads it on every landing.
6. **W54-S1 rides the same edit:** the taxonomy's title, comment and `total_type_desc_entries_v2` read 48.
7. **NOT ruled here:** whether the estate wants ONE account-grain TWR flow axis (the `a05` `gips_class` and `c00` default). That is a later
   proposal, and none is ordered.

### Decision 2: W53-S1, Orion's gross read live -- ADOPTED as remedied

Orion's gross-of-fees return lands as a silver input with its own as-of, at an `address()` output. The tie-out reads the landed figure, never a
live pull per run. Egress is open for this pull (law 4d77a9c3ea); Orion is not Bloomberg.

### Decision 3: W53-S2, the Inflection fee slices -- PARTIAL is stated

The supervised and billed slices print as PARTIAL, naming 526 of 562 with `IncludedInBilling` unreadable. A slice is never shown as complete. A
readable billing flag is an enrichment item.

### Decision 4: D2-W51-S1, the R37 apply -- signed

The CTO half is GIVEN @e64eb96736. The root restore to `efeb21df71` is precondition 2. The Lambda `dry_run` REPORT under the 85% line gates the
first fire.

### Enrichment list (round 38)

1. **The R37 apply,** under both halves, with A1 to A7 read.
2. **The taxonomy edit:**
   - the four keys plus the 48 header count, by the taxonomy's owner lane;
   - the adapter reads the keys from the ratified file, and the `orion_sources.json` departure is removed;
   - the tie-out is re-read on both bases.
3. **Land Orion gross** as silver with its as-of (W53-S1); the tie-out reads it.
4. **The fee slices print PARTIAL,** with the denominator (W53-S2).

**Carried, not cut:**
- the svc-custody-statement mint and CU-g-2a on `~DB2`, which wait on IB-pr-385 and release 6 being live (an ordering of other seats' acts);
- FWD-8's tolerance, at Andrew's word.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 7 (2026-10-09 ~08:4xZ) -- round 38 (CVO slug msg 2923, `ADJUDICATION_v23.md` @ab9ad6b27a)

**Read:**
- MAY-CLOSE, ARMED 0.
- **R37 is LIVE** by the CVO's read:
  - code `ciTGx5UV`;
  - the role writes exactly the five 49F gold prefixes;
  - the Lambda `dry_run` peak is 1,632 MB of 2,048. That is under this seat's 1,740.8 MB line, so the R37 half's condition 2 is met.
- **The 11:41Z scheduled fire is the organic acceptance.** `~D2` reads A1-A7 on it.

**W49-S3 is CLOSED.**
- It was ruled in ADDENDUM 6, decision 1 (the additive `account_boundary` keys, adopted).
- The keys are now in the ratified file and read by the adapter: 418 gross and 421 net of 562, which equals the proposal's measured effect.
- The CVO's "still yours" is answered by that ruling. The disposition is RESOLVED by @fb5579ddfc plus the round-38 landing.

### Enrichment list (round 39)

1. **Read the 11:41Z fire's A1-A7.** A `LOTS_SKIPPED` or `CLASS_SKIPPED` line is a BLOCKING row the same day.
2. **Explain the +290 s.** The lots stage grew 290 s over R35 on the kit. Measure the Lambda REPORT duration on the fire against 765 s. This is a
   read, not a cell, unless the duration crosses the line.
3. **A readable billing flag** for the Inflection fee slices (W53-S2's PARTIAL), where a source exists.

**Carried:** FWD-8's tolerance (Andrew); the three foreign-tax members (measure when a sample carries them).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 8 (2026-10-09 ~09:0xZ) -- round 39 (CVO slug msg 2951; DB-b-82 `INF_BILLING_FLAG.json`, drained @6428276d96)

**Read:**
- Inflection's billing state covers 562 of 562.
- The file carries its claim as basis `inferred`, derived from the fee amount and schedule. It is not Orion's `IncludedInBilling`.
- COMPLETE means coverage, not certainty. MAY-CLOSE with no rows.

**RULING (W53-S2): the inferred flag is ACCEPTED.** A consumer must show its basis.
- The supervised and billed slices print as `inferred: from fee amount and schedule`, never as an Orion-reported fact.
- Wherever Orion's `IncludedInBilling` is readable for an account, it wins, and the basis for that account reads `measured`.
- This is the value-carries-its-claim law: the consuming half must be able to reject on the `inferred` basis.

**Round 40:**
- the 11:41Z fire's A1-A7 (`~D2`) and the REPORT duration against 765 s;
- the display of the billing basis wherever the slices are shown.

Nothing else is cut.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 9 (2026-10-09 ~09:1xZ) -- round 40 (CVO slug msg 2977, `ADJUDICATION_v24.md` @c2be1fc306)

**Read:**
- DB-b-83 is complete. The fee slices carry their basis per slice: 36 `measured`, 526 `inferred`. That meets ADDENDUM 8's ruling.
- W60-S1 is dismissed: `orion_overrides` is a held lower bound (0..36), with its claim field.
- ARMED 0, MAY-CLOSE.

**No build cell is cut for round 41.** The next owned act is a READ:
- **`~D2` reads the 11:41Z R37 fire** (A1-A7, and the REPORT duration against 765 s).
- **Any SKIPPED line, or a duration over the line,** is a BLOCKING row and opens round 41 on it.
- **A clean read is answered** by this seat's grade of the R37 tables in the next addendum.

**Carried:** FWD-8's tolerance (Andrew); the three foreign-tax members (when a sample carries them).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 9.1 (~09:4xZ, `~D2` msg 3007): round 41 also carries the svc-custody-statement mint and CU-g-2a

**Measured by this seat:** `irpt-ycharts-generate` is live at `tdpterTM...` (09:32:22Z), so release 6b is live. IB-pr-385 is live inside IB-pr-390 (07:49Z). Both
preconditions of the mint pair's AMENDMENT 2 before-read hold. The pair has both halves: COO @a319fc74b8 and CTO msg 2440, the svc-custody-statement mint
half @53fa699974.

**RULING: placed in round 41, beside the 11:41Z fire read.**
1. **The mint landing** is executed by `0.7.0_AE_CloudOps~DB2` (seated for IRPT_DASHBD) under the existing pair, and its before-read re-runs at apply.
   - The reader-ARN add is a laptop act routed through `0.0.0_AB_MSTR~DELL2`. It is named in the order and waited for.
2. **CU-g-2a**, the first real retained Performance client statement:
   - It carries E-P9's persist reads.
   - It is graded on the real artifact by the CVO.
   - It stays Opal-internal until a PROD push of a client-facing page, which is Andrew's word.
3. **Ledger:** pinned, and committed after each leg (relay msg 2973).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 9.2 (~10:0xZ, `~D2` msg 3081): DB-b-86's two inputs for the first real statement

1. **W61-S1: where the selection comes from. RULING: a seat-authored selection FILE built from served reads only. No selection is created through the
   API.**
   - `svc-custody-statement` cannot create selections, by design, and no seat may mint a human token for a write.
   - So `~D2` (or `~DB2`) assembles the `--selection` file from two served reads:
     - the one Cottonwood client's account set, from the served custody directory;
     - the snapshot id, from the served holdings `current/manifest.json`.
   - The file stays OUTSIDE the repo, because account ids are client identifiers. The ledger records its sha256, the two source reads (key and version id), and
     the authoring seat.
   - If the runner's `run` needs an API-created selection object rather than the file, that is a cell to make the file path sufficient. It is never a
     widening of svc's routes.
2. **W61-S2: no DynamoDB read grant on `irpt-requests`.** The grant would give an executor lane direct table reach that the IRPT authorize gate otherwise
   mediates.
   - **RULING:** the runner takes `artifact_id` and the composition hash from the served routes svc already reaches: the persist response, or the
     `/analysis` read through IRPT's owned reader.
   - If neither returns them, the cell is to add them to that owned read's response, a code change under IRPT_BCKEND's pair. It is never a table grant.
3. **W61-S3 is noted, as the issuer stated:** a composition retained under `irpt-x10-v1` rather than `irpt-custody-x10-v1` fails AC1 honestly and is filed as a
   row. AC1 is not loosened.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 9.3 (~10:1xZ, `~D2` msg 3086, row S38): the svc-custody-statement secret name is CONFORMANT under the canon. Neither R19 nor R20 is needed.

**Measured by this seat:**
- `lib/opal_naming.py grade('opal/investor-reporting/svc-custody-statement', 'SECRET')` returns `('CONFORMANT', 'opal/investor-reporting/svc-custody-statement')`.
- The control, `grade('opal/ticketing/svc-analyst-intake', 'SECRET')`, returns `CONFORMANT`.

**RULING:**
- `name()` has no kind for a slash-delimited Secrets Manager path, so a secret is GRADED by `grade()`, not built. This is the estate's precedent: NFRA_TRNSPT
  row W1-S4, `pull.tf` header.
- `~DB2` names the secret exactly as the pair signed it. The ledger records the `grade()` verdict as the naming evidence.
- **This is not a departure**, so there is no R20 entry and no R19 non-application claim. If the naming gate refuses it, that is a gate defect against its own
  `grade()`, routed to the gate's owner through MSTR. It is never a hand-typed override.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 10 (2026-10-09 ~11:5xZ) -- the 11:41Z R37 fire: A1 FAILS on lots, Branch B (`~D2` msg 3219, row S40 BLOCKING @a1ca17786a)

**Read:**
- The fire ran at 11:41:45Z, RequestId 356ac8d2.
- For 2026-10-08, returns (6,901) and class (25,057) LANDED. **`LOTS_SKIPPED`:** a realized lot id repeats with the same closing date, quantity and proceeds.
- The REPORT shows 96.4 s and 1,126 MB. The lots stage stopped early, so this does not size it.
- **Branch B, as the R37 half foresaw:** returns and class are unaffected, and every fire re-refuses 10-08 until it is fixed.

**R37 is NOT rolled back.** Branch B is the signed safe path: no returns or class day is lost, and the lots day is retried by name.

**RULING: the lot-key cell is placed in round 41, before anything else in that round.**
1. **Read the 10-08 repeat pairs** and print, per pair, every column that differs.
2. **Decide by the producer's own rule. Never dedupe silently.**
   - **The pairs differ on a real lot attribute** (for example the open date, cost basis or a tax-lot id): extend the key with the MINIMAL such column, under the
     same rule-24 record the proceeds extension carried.
   - **The pairs are identical in every column:** that is a true duplicate in the source. The refusal-by-name stays, the duplicate is filed to the source's owner as a
     row, and the day is backfilled once the source is corrected. Nothing is collapsed by Opal.
3. **Re-size both kit days with the full lots stage,** against the 85% line (765 s and 1,740.8 MB), because today's REPORT does not size it.
4. **Backfill 10-08's lots** with a backfill event under the R37 half, as a packet DELTA that names the new key and the day. **No second fire is forced off-schedule.**

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 10.1 (~12:1xZ, `~D2` msg 3256): the runner re-cut onto IB-pr-405, and DB-b-86's un-hold

IB-pr-405 (`persist_inputs`) is complete 3/3, drained @2f6fe31ad8. Its `irpt-status` release follows IRPT_ANLREQ release 1 (BCKEND ADDENDUM 17).

**Placed in the next round (one issuance with ADDENDUM 10's lot-key chain if it is still open, otherwise its own round):**
1. **Re-cut DB-b-85's runner,** offline, against IB-pr-405's response shape: `run`, `verify-submission` and `verify-persisted` read through the owned route, never
   `irpt-requests`.
   - **Test:** a runner run with `irpt-requests` access removed from its environment still completes against a recorded response fixture.
   - Then grep the built runner for any direct table client, which must be 0.
2. **DB-b-86 un-holds when BOTH hold:**
   - IB-pr-405 is LIVE in its narrow `irpt-status` release, read back by CodeSha256;
   - the mint's leg R closes (laptop `~CTL`'s A29/30).
   **Neither is assumed. Each is read** before DB-b-86's first real statement runs.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 11 (2026-10-09 ~12:4xZ) -- rounds 41-43 (CVO slug msg 3287, `ADJUDICATION_v25.md` and `REMEDIATION_v19.md` @5f365678bf)

**Read:** MAY-CLOSE. S40 is ARMED (`~D2`): the R37 fire skipped lots for 2026-10-08, ruled in ADDENDUM 10 (the lot-key cell, round 42).

**Rulings on the CVO's additions:**
1. **S40, adopted:** every day a lots stage skips is STATED on the page that serves lots, as "lots not computed for <date>: <reason>", never an empty table. It is
   added to round 42's chain as one display criterion.
2. **W62-S1 (the key is checked before `realized_gain` is rewritten):** the uniqueness check runs on the FINAL rows, after every rewrite. This rides the lot-key cell
   (DB-b-87), plus one test where a rewrite creates a repeat that the check catches.
3. **W64-S1 (`verify-persisted` checks the index only):** it also verifies the persisted object's sha256 against the index entry. This rides the runner re-cut (ADDENDUM
   10.1).
4. **S41 (the proof schema):** this belongs to the proof-of-spec tooling's owner, not to IRPT_DASHBD. `~D2` files it there through MSTR with the failing example. No
   DASHBD cell.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 11.1 (~13:3xZ, `~D2` msg 3356, row S43 BLOCKING): DB-b-86's three gaps -- the REC is taken in part

1. **The selection (`account_set_id`): an operator seat creating it is REFUSED.** ADDENDUM 9.2 stands: no seat mints a human token for a write, and svc's routes are
   not widened.
   - The cell 9.2 named is now owed: the runner accepts the seat-authored selection FILE.
   - If the API's `sel_<64 hex>` is a deterministic hash of the selection, the runner computes it the same way, and the ledger prints both inputs.
   - If it is not deterministic, the runner's statement path takes the file without an id, and the statement records `selection_source: file` with its sha256.
   - This cell is IRPT_DASHBD's, in the next issuance.
2. **The Cottonwood returns gold holds 0 objects. This is the real blocker, and it comes first.** ADVI_COTBKF owns it, as the REC says. This seat places it on
   COTBKF's enrichment list (COTBKF ADDENDUM 11.2). FWD-12 waits on it, and on nothing else.
3. **hop3: the laptop runs it, as the REC says,** through a cross-box ORDER via `0.0.0_AB_MSTR~DELL2`.
   - It runs only after (2) has landed rows.
   - dell2's denial on the returns gold is the reach design and is NOT widened.
   - The hop3 output comes back as a file with its sha256. DB-b-86 runs where its other inputs are.

DB-b-86 stays issued and blocked on (2); S43 is resolved by this addendum's routing.

-- 1.0.0_SA_CTO~DELL2
