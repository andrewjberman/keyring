# The silver header contract, the three-partition re-run, and the payload proof -- 0.4.0_DS_ClientPlatform~M

**Date:** 2026-08-25
**Task Order:** `MDPF_COTREMEDIATION.TO-R1-DS.silver-contract-rerun-and-payload-proof`
**Status:** COMPLETE (my leg). Project NOT complete -- `global` remains frozen and is seated elsewhere.

---

## Objective

Restore cottonwood and global MDPF served data to the correct T-1 frontier **through the real producer chain**, and prove the restoration at the **payload** layer rather than the object layer. Declare the two added Black Diamond columns as Rule-17 passthrough, re-run the three refused partitions, carry all payload verification, and hold the NEVER#6 completion obligation. Andrew-direct P0: *"That needs to get fixed immediately."*

 **NOT vendor drift.** We amended the BD holdings template ourselves (`@17c38a26f2`, under a CTO pin). The vendor changed nothing; the silver-contract step was never sequenced.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `"check whether a served platinum payload is frozen by reading its provenance source_keys"` | PASS | Routed to `comp-xray frozen` -- **discharged AC7 with NO new instrument** (build-ladder rung 2, moratorium never approached) |
| comp-which | `"does a specific silver date= partition exist in S3"` | PASS | Routed to `comp-keys` after the rail correctly gated a raw `s3api` listing |
| comp-which | `"what triggers this lambda -- schedule or event"` | PASS | Routed to `comp-trigger` at 1.50 -- how the Andrew-direct defect got measured rather than guessed |
| comp-find | `--name 'mirror_schemas.py'` ; `-i 'Holding Supervised'` | PASS | The `--name` call surfaced **FIVE homes** against the decomp's stated two; its SYSTEMS CONTEXT named all four lambda packages -- a raw grep gives the paths without the coupling |
| comp-keys | `partitions s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/` | PASS | The live-state verification of the re-run (55 -> 58, latest `2026-08-24`). Its own coverage line warned gaps are calendar-weekday not trading-calendar -- which sent me to resolve `2026-07-03` instead of filing a false gap |
| comp-xray | `frozen ... --fields as_of_last _provenance.source_keys --cadence-days 1.0` | PASS | AC7 on both arms, pre and post. The `written_at` re-point produced the demonstrated false green |
| comp-trigger | `mdpf-gold-lambda` ; `mdpf-scheduled-floor` ; `mdpf-feeder-trigger` | **FAIL** | **Measured defect, now an Andrew-direct record.** NO MATCH for `mdpf-gold-lambda` despite scanning the schedule targeting it by exact ARN |

---

## Work Completed

### 1. The silver header contract (`COTR-b-1`, `b-2`, `b-3` source half)

Declared `Account Supervised` (idx 8) and `Holding Supervised` (idx 20) as Rule-17 passthrough, dtype `string`. Commit `288807f747`, 1 file, +2 lines.

**Positions measured at the artifact, not taken on report.** I replicated the guard's *own* extraction (`_bd_frames:596-604` -- openpyxl Sheet1 row 1, `str(h)`, the `__N` dup-suffix) so my read and `assert_declared_header`'s are the same read. **Positive control:** `2026-08-19` = 19 cols matching the OLD declaration exactly -- that is what makes the replication sound rather than merely agreeable.

**Dtype deliberate, not defaulted:** 54,297 of 54,297 rows carry a Python `str`, zero nulls, two values. Declared `string` **not** `bool` -- coercing `'Supervised'`->`True` is a judgment about MEANING (gold-tier under Rule 17) and dies on a third value.

### 2. The three-partition re-run (`COTR-d-1..3`)

`run_id 20260825T172050Z-f26cf779` -- all three converted, `cols=21`, rows 18,088 / 18,102 / 18,107, **matching my pre-commit local exercise exactly**. Verified on live state (55 -> 58 partitions, latest `2026-08-24`), not the producer's self-report. Three partitions, not five; `08-22`/`08-23` are Sat/Sun.

### 3. Deployed-bytes confirmation (`COTR-c-2` -- AE's leg, my obligation)

Downloaded the deployed package, read the `mirror_schemas.py` member: 21 cols, idx 8 / idx 20, sha256(LF) `1ef7577547ae7af3` == repo source. Normalisation stated because a digest without it is not an identity.

### 4. Propagation and payload proof (`COTR-e-1..3`, `f-1..3`, `g-1..3`)

Gold -> platinum through the real chain. **cottonwood SERVED: `as_of_last` 2026-08-19 -> 2026-08-24, `n_dates` 458 -> 461 (+3, exactly the three restored partitions), `source_keys` advanced.**

**L1 and L2 relocated to the SAME field -- `count_as_of`, not `dates`.** AC5 explained at source: `point_class` 441 absent / 17 measured, `meta.absent_dates_emit` = *"null (absent is not zero)"*, `cottonwood_carry.law` *"counts NEVER carried"*. **Decisive control: gold and served are identical**, so the publisher is faithful and the sparsity predates the freeze by ~20 months.

---

## Decisions Made

- **Raised AC4 as BLOCKING rather than absorbing or deciding it.** `_provenance.written_at` made byte-identity unsatisfiable by *any* path including doing nothing. COO amended to the 111 data-bearing fields. The amendment proved load-bearing -- the publisher returned `published:14 unchanged:0`.
- **Did NOT weaken the cross-axis coherence gate**, and did not touch `2026-08-19`'s data. Manufacturing coherence to satisfy an instrument is weakening the gate in different clothes.
- **Did NOT drop the failing `COTR-b-3a` cell_ref to make the proof-of-spec go green** -- that would understate coverage of the very edge that broke this pipeline.
- **Fired one discriminating global run on COO's ruling** even though my own gate-history finding felt sufficient. It was not sufficient, and I said so unprompted.

---

## Files Modified

| File | Commit | Note |
|------|--------|------|
| `data/assets/scripts/silver/mirror_schemas.py` | `288807f747` | The contract: +2 lines, source home only (lane `ANY`) |
| `org/tier2_senior/0.4.0_DS_ClientPlatform~M/deliverables/ANDREW_DIRECT_20260825_COMP_TRIGGERS_GEARED_FOR_THIS.md` | `81e7373b8c` | Andrew-direct record + same-turn broadcast |
| `org/critical_paths/change_management/mdpf-cotremediation-ds-contract-rerun-propagation-20260825.md` | `9d60b310bc` | NEVER#6 ledger, CLOSED |
| `org/tier2_senior/0.4.0_DS_ClientPlatform~M/deliverables/MDPF_COTREMEDIATION.TO-R1-DS_PROOF_OF_SPEC.json` | `9d60b310bc` | 8 criteria, all PASS |

All **LOCAL on CLOUD, riding integration.** Not pushed by this seat.

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| Andrew-direct record (`comp-trigger`) | `org/tier2_senior/0.4.0_DS_ClientPlatform~M/deliverables/ANDREW_DIRECT_20260825_COMP_TRIGGERS_GEARED_FOR_THIS.md` | Andrew / CTO / COO / MSTR |
| Proof-of-spec instance | `org/tier2_senior/0.4.0_DS_ClientPlatform~M/deliverables/MDPF_COTREMEDIATION.TO-R1-DS_PROOF_OF_SPEC.json` | COO (issuer), CVO (cert) |

---

## Blockers

**None held by me.** One item was owed *to* me and it is now RESOLVED -- recorded here with its
correction because my original text in this section was WRONG.

**WHAT I ORIGINALLY WROTE (FALSE):** that `COTR-b-3a` was authored as a section heading rather than
a table row, and the checker's id space is table-derived. **I reasoned from the id-space COUNT and
the row FORMAT without reading the harvester.** `2.0.0_SA_COO` acted on it, converted the cell to a
table row @`3a08972df3` -- correct markdown -- and the violation did not move.

**TRUE CAUSE, source-confirmed at `.tools/proof-of-spec-check.py:179`:**
`CELL_ID_RE = re.compile(r"\b[A-Z][A-Z0-9]*-[a-z]{1,4}-[a-z]?\d+\b")` requires a cell id to END IN DIGITS.
A letter is allowed BEFORE the digits and none after, so `COTR-b-3a` and `COTR-b-5a` were
STRUCTURALLY UNHARVESTABLE in any formatting -- and `COTR-b-3-orig` SILENTLY HARVESTED AS
`COTR-b-3`, collapsing a distinct cell onto an existing one with nothing in the output saying so.

**RESOLVED:** COO renamed the cells to harvestable ids and removed the collapsing one
(@`6dcd789490`); the instance is now VALID (id space 42, 29/29 cell_refs resolve, 8/8 criteria).
**The rename is a WORKAROUND, not a fix -- the regex is unchanged and the class is still live.**
Routed to `1.0.0_SA_CTO`. Full account: `session_close_1800-1840Z.md`.

---

## Current State

**Cottonwood is restored and proven at the payload layer. Global is not, and global is not mine.**

`global` remains at `as_of_last=2026-08-19`; its cross-axis coherence gate refuses to emit on a `2026-08-19` foreign-day roster (7791 -> 8260 -> 7791, +469/-469, net 0). **Measured independent of this repair:** first fired `2026-08-24T13:31:04Z` (`retentionInDays=None`, so the 08-20..08-23 absence is real), and it refused again on a clean run started 21 minutes after fresh cottonwood gold existed. Matches a finding CTO filed 28 hours earlier. COO ruled it gets its own seat; my NEVER#6 discharged on cottonwood.

**AC6 is NOT closed by anything I ran.** The re-run, gold, publish and discriminating legs were ad-hoc -- a QA/repair instrument, never production evidence. AC6 closes on `mdpf-scheduled-floor` cron(30 13) -> `opal-assets-mdpf-portal-publisher-daily` cron(50 13), i.e. 2026-08-26.

---

## Next Steps

1. **[`2.0.0_SA_COO`]** One table row in the decomp for `COTR-b-3a`, which clears the single remaining proof-of-spec violation. Nothing I can write in the instance clears it.
2. **[`1.0.0_SA_CTO`]** The `comp-trigger` Scheduler-target defect (Andrew-direct ~17:4xZ). Root: the Scheduler plane is enumerated but its `Target` is never read, so a schedule is findable only by its own name and never by the lambda it fires. `list-schedules` already returns `Target.Arn`. Routed, not self-assigned.
3. **[the artifact, not a seat]** AC6 closes on the **2026-08-26 scheduled** floor + publish. No ad-hoc run substitutes.
4. **[unseated / `2.0.0_SA_COO` to seat]** `global`'s 2026-08-19 roster incoherence. Not mine, not carried by my ledger, and the gate stays untouched until it is diagnosed.
