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

## ADDENDUM 12 (2026-10-09 ~13:3xZ) -- rounds 42 and 44 (CVO slug msg 3367, `ADJUDICATION_v26.md` @fbc76ab42d): MAY-CLOSE

The CVO read the live gold Lambda as `yIAQjspL`. 10-08 is backfilled with 0 skipped. **S40 is CLOSED**, and 0 rows are ARMED.

1. **The status key under the activity prefix meets the intent, not the letter: ACCEPTED.** `~D2` amends the order's criterion text to the key as built, in its own
   amendment commit (the issuer amends its own criteria, Andrew-direct 2026-09-24). The commit names which gate limb, if any, graded it.
2. **The double check (uniqueness on the final rows) is sound.** No act.
3. **The verify-persisted sha256 limb is DORMANT** until IRPT_BCKEND serves `report_index.sha256` (W64-S1 OPEN). It stays in the runner, dormant, with no stub value.
   **IRPT_BCKEND carries it as an enrichment item:** the persist and read responses return the stored object's sha256. That is a code change under IRPT_BCKEND's own
   pair; `~P2` places it.
4. **S43 is ruled at ADDENDUM 11.1** (@43bbe32935). The selection stays file-based; the Cottonwood returns gold comes first, owned by COTBKF; hop3 runs on the laptop.
5. **DB-b-90 and DB-b-91 are released TOGETHER as ONE gold Lambda release** after `yIAQjspL`, under one never-widen pair.
   - Both are gold-builder changes: the uniqueness check on final rows, and the lots-not-computed statement.
   - The packet's member census against live `yIAQjspL` must show exactly the members those two orders own. Anything else means STOP.
   - Branch B is the `yIAQjspL` version.
   - DB-b-92 (the runner's sha256 check) rides the runner, not this release.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 13 (2026-10-09 ~14:0xZ) -- round 45 (CVO slug msg 3402, `ADJUDICATION_v27.md` @11b79674b2): MAY-CLOSE

1. **D2-S3 is disarmed.** The schema break (e7c10e5b4b) was fixed by this seat @1f256cfc64. The CVO read the fix on HEAD, and `check_schema` passes.
2. **The CVO's suggestion: a `check_schema` step on schema edits.** It is a mechanical validity check, not an approval gate, and it is ROUTED to its owner.
   - The owner is laptop `1.0.0_SA_CTO`, who owns proof-of-spec tooling (the S41 route, ADDENDUM 11 item 4). It travels via `0.0.0_AB_MSTR~DELL2`.
   - The proposed shape: `.tools/commit-gate.sh` runs `jsonschema.Draft202012Validator.check_schema` on any staged `org/standards/*.schema.json`.
   - Cost: one call per schema commit. Non-application: every other file.
   - This seat does not edit the commit gate.
3. **W68-S1 (does live POST /analysis admit a file-only selection?) stays OPEN, and DB-b-86's first run proves it,** as the CVO says.
   - Both branches are pre-ruled at ADDENDUM 11.1 item 1: the file path is accepted, or the runner takes the file without an id and records `selection_source: file`.
   - A refusal on the first run is recorded with its code, and that branch is cut. No widening of svc.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 13.1 (~14:0xZ, `~C2` msg 3408, W66-S1 / S63): the Cottonwood returns method -- the sources entry, as STRUCTURED fields, never a new return_basis value

**The call:** CB-al-1 built 3,325 Cottonwood days through `account_return_daily.py`. Its `return_basis` has no value for "positions x as-traded close, after fees",
so the field reads NULL. `emit_day(upload=True)` then writes a manifest claiming the custodian method.

**RULING: (b), a Cottonwood sources entry, but as STRUCTURED fields, not manifest text.**
- **`return_basis` is "which arithmetic produced total_return_daily"** (`account_return_daily.py`:132). Positions times the as-traded close, chained daily with flows,
  is TWR arithmetic.
  - If CB-al-1's arithmetic is TWR, the row says `TWR`.
  - If it is not, the row says `NOT_MEASURABLE` with its reason.
  - **A new enum value would put the valuation source on the arithmetic axis.** That breaks rule 24 (iii), one axis per intent, so no enum edit is made.
- **What differs for Cottonwood is the VALUATION SOURCE and the FEE TREATMENT.** Those are per-firm source facts, so the firm's sources entry carries them as fields:
  - `valuation_source: positions_x_as_traded_close`;
  - `fee_treatment: net_of_fees`;
  - `price_basis: as_traded` (COTBKF ADDENDUM 8).
- **The manifest writer reads those fields, and never defaults to the custodian method.** A firm with no entry writes `valuation_source: absent`. A consumer
  can reject on the field (A VALUE MUST CARRY ITS CLAIM). The existing custodian firms' entries carry `custodian_reported` explicitly.

**Placement:** ONE IRPT_DASHBD cell in `~D2`'s next issuance:
- the sources entry fields;
- the manifest writer reading them;
- no default;
- a negative arm: a firm with no entry writes `absent`.

**The CB-al-2 mint stays HELD until that cell drains.** It then re-runs through the producer as built, under its own pair (COTBKF ADDENDUM 11.2).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 14 (2026-10-09 ~14:0xZ) -- round 46 (CVO slug msg 3410, `ADJUDICATION_v28.md` @eae4b4d6e3) and FWD-8 (`~D2` msg 3411)

1. **Round 46 MAY-CLOSE, ARMED 0.** The CVO's W69-S2 point (drop a stale lots-not-computed record on any successful landing) is already placed as a next-round cell.
   That is in the R44 CTO half @fa8d2c2961.
2. **FWD-8: YES to the cell.** `~D2`'s next issuance carries ONE LOCAL cell:
   - it classifies each of the 510 UNEXPLAINED outside segments in `TIEOUT_COMPOUND_V2.json` (990 outside) by a named reason from a declared set, or files it as a
     defect row;
   - the reason set arrives with its rule-24 record;
   - it reads the existing tie-out inputs only, with no vendor call;
   - the result prints the denominator (990) and the per-reason counts, which sum to it.
3. **The tolerance itself is NOT this seat's to rule.** PRD FWD-8 reads "a tolerance Andrew accepts" (`IRPT_DASHBD_PRD.md`:236, :587), an L2 line he confirmed.
   - His word is the act, and open call 2f53 carries it with REC 0.35pp.
   - The cell above runs regardless of the number he picks.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 15 (2026-10-09 ~14:4xZ) -- round 48 (CVO slug msg 3490, `ADJUDICATION_v29.md` @9e4cefbb3a): MAY-CLOSE; FWD-8 NOT REALIZED

Of 990 outside segments, 793 are reasoned and **197 are DEFECT** (W73-S1: 74; W73-S2: 123). FWD-8 stays NOT REALIZED while any DEFECT stands. The tolerance is
0.35pp (laptop CTO ruling @ea01eb1e34; Andrew's word supersedes it) and is never widened.

**Round 49 enrichment (`~D2`):**
1. **Sensitivity on the classifier's thresholds, LOCAL.** Counts per reason at 0.5% and 2% of peak, beside the 1% cut, and at the $1/0.1% tie's neighbours.
   - The 156 segments resting on the 1% cut are printed at each setting.
   - If a reason's count moves by more than half across the band, the reason is NOT robust. Those segments are re-graded UNEXPLAINED, not reasoned.
2. **Pre-registration from now on.** Any changed threshold is committed BEFORE the run that grades it: rule commit, then output commit, checked by order. A threshold
   tuned after seeing results is refused.
3. **Every reason carries its claim** in a field: `inferred` (from our data) or `confirmed` (Black Diamond's own record). All 793 read `inferred` today. FWD-8 may be
   REALIZED on `inferred` reasons only where the reason is mechanical: flow timing or an income date read from both sides' transaction dates. A reason without a
   two-sided read stays NOT-REALIZED until confirmed.
4. **The 197 DEFECTs: ONE cell per class.** W73-S1 (74) and W73-S2 (123) each get a fix of our producer's defect, or a two-sided read showing it is Black Diamond's.
   - Fixes ride their own pairs.
   - FWD-8 re-grades on the next tie-out after both land.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 13.2 (~14:4xZ, `~C2` msg 3495, row W70-S1): `method_version` is a default claim -- the producer change comes FIRST

CB-aq-1 drained @9a7eaa849a: 3,325 days, with all three method fields present (0 of 9,975 absent). But `build_manifest()` writes `method_version: 2`, the custodian-equity
method row, into every manifest whatever the source entry says. The rows carry NULL.

**RULING: NOT minted as is.**
- A manifest that names the custodian method beside positions-based fields is the exact default claim ADDENDUM 13.1 forbids. A consumer reading `method_version` would
  be told something false.
- **IRPT_DASHBD owes ONE LOCAL producer cell first:** `build_manifest()` takes `method_version` from the firm's sources entry.
  - A positions-based entry names its own method row (a new row in the method table, with its rule-24 record). It never reuses row 2.
  - A firm with no method declared writes `method_version: absent`.
  - Negative arm: a positions-based firm's manifest never reads 2.
  - The existing custodian firms keep 2 explicitly from their entries.
- **CB-al-2's mint waits on that cell's drain.** Then it re-runs through the producer as built, under its own pair.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 16 (2026-10-09 ~15:0xZ) -- round 47 (CVO slug msg 3538, `ADJUDICATION_v30.md` @84387e2a60): MAY-CLOSE

1. **R44 is LIVE** at `oNgy4rnr` (14:34Z) by the CVO's read. W62-S1 is closed.
2. **DB-b-97 (a backfill clears the lots-not-computed record) is NOT in R44,** so W69-S2 stays open on live code.
   - It ships in the NEXT gold Lambda release, under its own pair, as the R44 half placed it.
   - The census against live `oNgy4rnr` shows only DB-b-97's members.
   - Until then, a backfilled day can still read "not computed" on the page. That is a stale statement, never a wrong figure.
3. **Ledger S1 (first-fire sizing at 85%) is the R44 half's condition 4,** and it is read at the first scheduled fire after 14:34Z.
   - `~D2` prints duration and max memory against 85% of the timeout and the configured memory.
   - Either one over: Branch B to `yIAQjspL`.
4. **The drain's line-union merge produced two malformed channel rows.** The row gate refused them, so nothing landed.
   - `~D2` re-appends the two rows cleanly on the shared index, as CLAUDE.md 14b says for append-only files: take the shared index's race; do not isolate.
   - The merge-driver behaviour is a tooling note for the safe-merge owner, via MSTR, and is not this project's cell.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 17 (2026-10-09 ~15:4xZ) -- rounds 49-51 (CVO slug msg 3581, `REMEDIATION_v24.md` @832337d37c): MAY-CLOSE, ARMED 0

1. **DB-b-104's status key is `address()` output with its bytes unchanged.** It ships with DB-b-97 in the next gold Lambda release, under ONE pair. The census
   against live `oNgy4rnr` shows only those two orders' members.
2. **RULING on W74-S1: FLOW_TIMING and INCOME_DATE are relabelled `inferred`.** ADDENDUM 15 item 3 admits a reason as mechanical only on a TWO-SIDED read. The
   test re-links Opal's own series, and no Black Diamond date is read, so the `mechanical` label is a claim the evidence does not carry.
   - **ONE LOCAL cell:** read Black Diamond's OWN transaction or posting dates for every segment carrying either reason.
     - The source is the firm's own Black Diamond input already in the 49F tree, read by its served address. No vendor call, and no cross-firm read.
     - It compares them with Opal's dates.
     - A segment whose two dates agree with the stated reason becomes `confirmed`. One that disagrees is re-graded UNEXPLAINED.
   - **Until that cell drains, FWD-8 stays NOT REALIZED on these reasons,** on top of the 197 DEFECTs.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 18 (2026-10-09 ~15:5xZ) -- round 50 (CVO slug msg 3593, `ADJUDICATION_v31.md` @e6298fbcf4): MAY-CLOSE, ARMED 0

1. **R44's dry-run sizing reads UNDER both lines:** 377 s of 765, and 1,661 MB of 1,740.8 MB. Memory sits at 95.4% of its line. The ledger closes, per the R44
   half's AMENDMENT 1.
   - **One sample is not a margin. That gets measured now, not waited for:** ONE more ad-hoc dry run (no writes) on the HEAVIEST lots day in the last 90 days,
     chosen by the largest lot-row count, printed with its denominator. Month-end 2026-09-30 is a candidate.
   - Over the 85% line on that day: a pair for EITHER a producer fix (preferred) or a memory-configuration change, the latter with its own measured before/after.
     Monday 07:41 ET's fire stays the acceptance row.
2. **W73-S2 (123 segments):**
   - **98 are BD-side by a two-sided read: `confirmed`.**
   - **25 are BD-side only by exclusion: `inferred`, and they do NOT count toward FWD-8** (ADDENDUM 15 item 3, ADDENDUM 17).
   - The ADDENDUM 17 two-sided date cell reads them too. Any that stay exclusion-only are graded UNEXPLAINED.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 19 (2026-10-09 ~16:0xZ) -- round 49 (CVO slug msg 3625, `REMEDIATION_v25.md` @3fdfddae0c): MAY-CLOSE

1. **D2-S5 (client data in git) is contained.** W73_S1 and W73_S2 were removed from the tree @20e0b6408b, pushed, and box-sync was re-enabled (MSTR msg 3618).
   - The history purge on origin box/dell2 and CLOUD is Andrew's act.
   - The same class was found in ADVI_COTBKF's ARD manifest and removed @cb16f8b2f9.
   - **Fabric rule (msg 3628-3632):** no account ids or client figures in any tracked file. Each COO runs a census.
   - The disarm owner stays MSTR~DELL2, and the row disarms on its push read.
2. **RULING on W75-S1, the FWD-8 comparator: compare on ONE COMMON convention, never across two.**
   - 73 of 74 segments turn on our own declared conventions: fees inside the return, and income on receipt.
   - The comparator RESTATES Black Diamond's return to Opal's declared conventions, then grades against 0.35pp. The restatement rule is pre-registered:
     committed before the run that uses it (ADDENDUM 15 item 2).
   - **A segment within 0.35pp AFTER restatement carries reason `CONVENTION` (`confirmed`: it is arithmetic on both sides' own figures).**
   - **A segment still outside after restatement is NOT explained by convention.** Per W75-S2 that is 60 of 74, since only 14 fall within. They stay
     UNEXPLAINED, or DEFECT where a cause is found.
   - The tolerance is not widened to absorb them.
3. **`ZERO_GAIN_VENDOR_TWR` failed the robustness band** (ADDENDUM 15 item 1). Its 45 segments are re-graded UNEXPLAINED, as the CVO did.
4. **FWD-8 stays NOT REALIZED.** The next tie-out re-grades on the restated comparator.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 20 (2026-10-09 ~16:4xZ) -- round 53 (CVO slug msg 3715, `ADJUDICATION_v32.md` @5465479292): MAY-CLOSE; the memory remedy placed before Monday

- D2-W82-S1 is dismissed (the denominator is 2 days).
- **The heaviest-day dry run reads 1,685 MB against the 1,740.8 MB line:** UNDER, at 96.8% of the line. That leaves no margin for a heavier month-end.
- **RULING: BOTH remedies, in this order.**
  1. **Before Monday's 07:41 ET fire: ONE pair raising the gold Lambda's configured memory one step**, under its own pair.
     - The step is the next size up, which also raises CPU.
     - The census is the memory setting only, with no code change.
     - Proof: the same heaviest-day dry run re-read under the new setting, printed before and after against 85% of each.
     - Rollback: the prior setting.
     - It is a configuration change and does not hide the growth: the before/after numbers and the producer cell below keep it visible.
  2. **The producer fix stays owed (preferred, ADDENDUM 18):** ONE cell measuring peak memory per stage on the heaviest day, then cutting the largest stage's peak.
     It ships in the gold release with DB-b-97/104, under that pair.
- Monday's fire remains the acceptance row. Over the line under the new setting means Branch B to the prior release.
- **Containment AMENDMENT 2 is done for the CVO's files** (@751d0de81a): the DASHBD 6 and BCKEND 10 tokens are in the `49financial:` form, with 0 bare-form tokens
  left.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 21 (2026-10-09 ~17:0xZ) -- rounds 52 and 54 (CVO slug msg 3755, `REMEDIATION_v26.md` @5740a5fdc9): MAY-CLOSE

1. **RULING on W81-S1: matching dates REFUTE `FLOW_TIMING`; they do not confirm it.** On 156 segments Opal's and Black Diamond's flow dates agree, so timing
   cannot explain the gap. Those 156 are re-graded UNEXPLAINED unless another reason holds on a two-sided read. A reason is `confirmed` only when the two-sided
   read SHOWS the mechanism (dates differ in the stated direction), never when the read merely exists.
2. **The 319 segments after 2026-08-20 (Black Diamond's record ends there): `NOT_COMPARABLE`, reason `BD_RECORD_ENDS_2026-08-20`, with the count printed.** They
   are not "unexplained", because no comparator exists. **FWD-8's comparison window is stated as ending 2026-08-20.** A refreshed Black Diamond record extends it.
   The refresh runs through the existing Black Diamond pipeline, with no new vendor leg. The window is printed on every tie-out, never silently truncated.
3. **R45's CTO half is GIVEN** (`deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R45_RELEASE_CTO_HALF.md`). The memory step goes first, plus the live-call arm.
4. DB-b-108 is checked: 0 ids, and its tokens are in the firm form. W80-S1 is dismissed.

-- 1.0.0_SA_CTO~DELL2
