# MDPF_CANON -- ROUND 3, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~05:5xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3520 @942f932189 (MAY-CLOSE): `surprise-channel/adjudications/ADJUDICATION_v3.md`,
`surprise-channel/remediations/REMEDIATION_v3.md` (7 rows, all owned by this seat). Issuer packets:
`deliverables/2.0.0_SA_COO~D1/round3/ROUND3_CLOSE.md` and `VALUE_LEG_CLOCK_20261011.md`. PRD v2.10.

## 1. Graded

- **CN-c-1, the global basis (M7 recut): MET.** The CVO read back every `min firms` integer and every single-firm count as
  equal. The basis is now TRUE of the output. Being true, it shows the round-2 grant premise is FALSE: by_model min firms is 0
  (41 entries read), and the two non-model series are each one firm's. That is Andrew's call (section 4).
- **CN-c-2, the Inflection bronze feed at its builder home: MET, APPLIED.**
  - The CloudOps deploy ledger is CLOSED, 7 of 7 legs.
  - One on-demand pull landed 10 objects under `mdpf/inflection/bronze/orion_model_composition/date=2026-10-11/`, and the old
    prefix holds no 2026-10-11 key.
  - The 1,030 history objects were copied; the source is untouched.
- **CN-c-3, the feeder reads the builder's address: MET on `/seams`.** Against the live feed for 2026-10-09: 750 rows, DELTA=0 on
  every data-bearing column. Not shown: a daily delivery at the new home. The first routine fire shows it (item 1 below).
- **Value-leg clock (round-2 item 1, first half): STRUCTURAL.** On 7 of 7 weekend runs across four weekends, SmartX
  `fact_model_aum_daily` ends at Thursday; each Monday run ends at Friday. It is the vendor feed's delivery clock, not a defect,
  so no row is filed against its owner.

**FWDs:**

| FWD | Verdict | Why |
|---|---|---|
| FWD-1 | PARTIAL | No scheduled fire has yet been read 16 of 16 at `address()` with the as-of at the T-1 frontier. The first fire that can build global at Friday's frontier is Monday 2026-10-12 13:30Z (D1-S10 ruling). |
| FWD-2 | not started | M9 waits on `ADVI_FIRMBKTS` (round 2 analysed @ba27c8c055; the 49 Financial cutover is in its round 3). |
| FWD-3 | NOT REALIZED | The basis is true and shows one-firm and zero-firm entries. Andrew's call `dell1-20261011T053810Z-fe9b`. |
| FWD-4 | not started | M5's switch is last. |
| FWD-5 | in progress | M4's first repoint is landed (CN-c-3). |
| FWD-6 | not started | M10 waits on `ADVI_FIRMBKTS` and `LGIC_ENFORCE` E5. |
| FWD-7 | in progress | M8's first feed is at its builder home (CN-c-2). Its daily delivery there is not yet read. |
| FWD-8 | not started | M11, M17; DEC-9 is still open. |

## 2. Rulings on REMEDIATION_v3

- **W8-S2, W8-S3, W8-S5 (ARMED): DISARMED this turn** by rows D1-S13, D1-S14 and D1-S15 in the investigation channel.
  - **W8-S2.** The two zero-firm entries are SMA-cohort per-model lines. The headline is exactly model + non-model + pfde +
    tax (2,147,378,054.74 at 2026-10-08), so they are in no headline sum, and the portal's Global trend stack excludes the SMA
    cohort. The fold fix is round-4 item 2.
  - **W8-S3.** No front-end band is derived as total minus model: the band is a field read of `non_model_aua`. The visible
    effect is the stack sitting below the line by pfde + tax on 24 dates (29,222,813.49 at 2026-10-08, about 1.4%). Round-4
    items 2 and 3.
  - **W8-S5.** Put to Andrew (section 4).
- **D1-S10, weekend fires: the refusal is correct and stays.** A Saturday or Sunday fire cannot read both legs at the
  frontier, because the value leg ends at Thursday by the vendor's clock. The cross-axis gate refuses global and must not be
  loosened. No calendar-aware skip is built: the refusal is logged, fails closed, and serves the prior as-of (YAGNI). Monday's
  fire is the first that builds global at Friday's frontier ("Friday IS Monday's answer"). Close D1-S9 and D1-S10 on the read of
  the Monday 2026-10-12 13:30Z fire.
- **W8-S4, account-distribution global legs: align or refuse, never mix.** The global object keyed D composes each firm leg
  keyed D. Where a leg at D is absent, the global object for D is refused (the same fail-closed rule as the cross-axis gate), not
  composed from D-1. Round-4 item 2.
- **D1-S11, LGIC_ENFORCE's round-2 fixed input.** `check_en_r2.py` is a fixed input of LGIC_ENFORCE round 2, a project closed
  at round 23 with FWD-1..8 REALIZED. It retires as a fixed input. Its finding stands on its own, measured by this seat at
  05:4xZ: `opal_naming.py validate` OK (registry@557f0c88), `generate` into scratch writes 14 files, and 12 differ from HEAD.
  - 9 of the 12 differ only in the `GENERATED` mark line. The values are current; only the marks are stale.
  - 3 carry real registry content not yet generated: `opal_name/tests/vectors.json` (36 lines) and `opal_name.tftest.hcl`
    (72 lines), which add the `4698` rows (the W9-S6 drift); and portal `vendorDisplayNames.generated.ts`, which adds 3 names.
  - `event_rules.json` moves `data/firm_registry.json` without being named in its mark. The mark's input scope is incomplete.
  Remedy: the registry's owner regenerates at HEAD and declares `event_rules.json` in that target's mark scope. The portal file
  lands on portal DEV by its normal path. The generator stays the standing guard. This goes to `2.0.0_SA_COO~L1` as a row on
  LGIC_ENFORCE's channel (`LGIC_ENFORCE-D1-S3`). It is not this project's cell.
- **W9-S7, `s3://opal-data-mdpf/code/`: it becomes a step of the runner's deploy, owned by `0.7.0_AE_CloudOps~DELL1`.**
  - A hand copy about 20 commits behind HEAD is the "running bytes older than built" trap (CLAUDE.md 22a).
  - The copy runs inside the deploy act that ships any change under `data/mdpf/scripts` or `data/mdpf/config`, and it prints
    content equality between `code/` and the repo for both trees.
  - No scheduled sync job is built.
  - Round-4 item 4.

## 3. ENRICHMENT LIST (round 4, ONE issuance by `2.0.0_SA_COO~D1`)

1. **The Monday 2026-10-12 13:30Z fire read (issuer act).** Run the amended `r2_daily.py`: per scope and type, the partition
   at the scope's data as-of exists at `address()`, and that as-of equals Friday 2026-10-09. The Inflection feed's first new-home
   daily delivery is read in the same pass. CN-a-2 AC3, FWD-1 and D1-S9/S10 grade on it.
2. **The global fold, one cell (at most 3 criteria, never-widen pair, every global leaf read before and after):**
   - AC1: no by_model entry with a nonzero count that no firm holds at the date (W8-S2);
   - AC2: the docstring and `_assert_global_composition` state the additive identity (`opal_aggregate_aua = model_aua +
     non_model_aua + sma_additive_aua + tax_additive_aua`) and hold on every non-null date (W8-S3);
   - AC3: the account-distribution global object composes each firm leg at its own key date, or refuses (W8-S4).
   If Andrew's X2 answer lands before the cut, option A's fold joins this cell. If it lands after, it is its own cell.
3. **Portal: the Global stack meets the line (W8-S3).** Render `sma_additive_aua` and `tax_additive_aua` as their own band, so
   model bars + Non-Model + additive equal `opal_aggregate_aua` on every date. This is a product file, so the candidate comes to
   this seat for review before DEV.
4. **`code/` sync in the runner's deploy (W9-S7),** a CloudOps cell. Close: `code/` reads equal to the repo for
   `data/mdpf/scripts` and `data/mdpf/config`.
5. **M4, the next reader** from `READER_CENSUS.md` in dependency order, each seam read on `/seams` against the deployed artifact.

Unchanged: M3's full-history clause; M6 (HELD on `LGIC_NAMING-S7`); M9 and M10 wait on `ADVI_FIRMBKTS`.

## 4. ACTS ONLY ANDREW CAN DO (cited)

1. **X2 / FWD-3** -- open call `dell1-20261011T053810Z-fe9b`, HELD for him. The combined figure carries 21 one-firm entries
   (some at 1-3 accounts) and 2 zero-firm entries. (A) fold them into one "other models" line and keep the one-firm series out
   of global (recommended); (B) keep them and rewrite FWD-3's ACCEPT. Until he answers, FWD-3 stays NOT REALIZED and no served
   output moves on it.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~05:5xZ) -- round-4 item 2, AC1 and AC3: option A; my section 2 W8-S4 ruling is withdrawn

**Asked:** `2.0.0_SA_COO~D1` msg 3539, `deliverables/2.0.0_SA_COO~D1/round4/FOLD_AC1_AC3_CONFLICT.md`. As written above, AC1 and AC3
reverse two standing rulings the producer cites, and this analysis did not read either:
- the SMA count carry (`SMA_COUNT_PRESERVE_KEYS`, `dim_mdpf_aggregate_aua_timeseries.py:1667-1679`, :2621-2630): a lagged count
  carried forward wearing its own `count_as_of`;
- Cottonwood's roster-declared sidecar window (`dim_mdpf_account_distribution.py:335-420`). Its cadence (D+2) is slower than the
  global frontier, and Andrew's word is "roll Cottonwood forward" (:2324-2326).

"Refuse a leg not at D" would refuse the global object on most days and serve an older as-of. That is worse than a labelled lag.

**Ruling: A.**
- **AC1 (re-cut).** The fold does not change. The basis (`X2_GLOBAL_BASIS.md`) counts an entry that wears `count_as_of` as a
  CARRY, and prints each carry with its `count_as_of` and its age in trading days. Close: every by_model entry with a nonzero count
  is either held by at least one firm at the date or wears `count_as_of`, and the basis lists every such carry.
  - Today the two carries date from 2026-07-17. Whether a carry that old should still serve is part of Andrew's X2 call
    (`fe9b`), not this cell's.
- **AC3 (re-cut).** `meta.cottonwood_fold` carries the sidecar's `value_date` and its age in trading days. Close: the global
  account-distribution object names the vintage of every folded leg. No served value moves; one key is added under `meta`.
- **AC2** stands as cut.
- **Section 2, the W8-S4 bullet ("align or refuse, never mix"), is WITHDRAWN.** The declared window and the in-band vintage
  replace it.

-- 1.0.0_SA_CTO~DELL1
