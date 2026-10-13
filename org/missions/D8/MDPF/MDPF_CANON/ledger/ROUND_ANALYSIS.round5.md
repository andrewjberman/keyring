# MDPF_CANON -- ROUND 5, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~17:5xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4525, compiled @602bd2ad10 (LOCAL; origin at 79bbe02f05 by the CVO's ls-remote read). All orders are terminal, the nine ARMED rows are
dispositioned, and the round reads MAY-CLOSE. Issuer evidence: `deliverables/2.0.0_SA_COO~D1/round5/READ_20261012_MONDAY_FIRE_GRADED.md` @6c49fa41d0.

## 1. Graded

- **CN-d-1 deploy (D1/D2): MET, WORLD.**
  - The package equals `0d39789fdf` (3 of 3), and the manifest has no errors.
  - The account-distribution change is exactly the two `cottonwood_fold` keys, and the served object is otherwise unchanged.
  - **The served-key read is OWED** at the first SCHEDULED fire after the deploy, 2026-10-13 13:30Z, owner `2.0.0_SA_COO~D1`. W8-S4 closes on it. This is a scheduled producer's
    own run, and an on-demand run is not production evidence, so the wait is the rule, not a choice.
- **CN-e-1 AC4: MET.** Nothing calls the instrument, and the verifier is not repointed.
- **CN-a-2 AC3: MET** on the Monday fire. D1-S9/S10 are REMEDIATED: the weekend refusal was the value leg's Thursday clock.

| FWD | Verdict | Read |
|---|---|---|
| FWD-1 | **REALIZED** | The Monday 13:30Z fire: 16 of 16 series at the frontier 2026-10-09, 547 of 547 snapshot keys unchanged, parity 12 of 12, cross-axis and composition gates PASS, cycle 16/16, no errors. |
| FWD-7 | **REALIZED** | The first new-home bronze feed, on the CVO's grade. The next routine delivery is confirmation only (PRD M8 row). |
| FWD-3 | NOT REALIZED | `fe9b` RULED (A) by the cluster lead. The fold is round 6's cell (record `RECORD_FE9B_RULED_BY_CLUSTER_LEAD_20261012.md`, ADDENDA 1-5). |
| FWD-5 | in progress | Two M4 readers repointed. |
| FWD-2, 4, 6, 8 | UNBLOCKED, not started | `ADVI_FIRMBKTS` act 4 flipped (edge applied 15:15:10Z); M9/M10 may begin once FIRMBKTS's flip receipt passes ownership (v2.11 R2). |

## 2. Rows

- **C-S65 (mine): ACCEPTED as written.** An on-demand gold run writes `mdpf/global/state/taxsma_control/current.json`, which the CN-d-1 pair did not name; only `process_time`
  moved. From now on, every pair that authorizes an on-demand gold run names that key, and every other routine state write of the gold run, with its prior VersionId as the
  rollback. The fold cell's pair is the first, and C-S65 closes on it.
- **D1-S18, the gold commit stamp lags the deployed code (COO~D1):** round 6, item 3.
- **W8-S4:** closes on the 10-13 served-key read.

## 3. ENRICHMENT LIST (round 6, ONE issuance by `2.0.0_SA_COO~D1`)

1. **The fe9b Global fold** under its own pair, per the record's ADDENDA 1-5:
   - every emitted line held at 2 or more firms per date, the fold line included;
   - the residual differential to the cent;
   - SMA lines untouched;
   - the trend and quarter-cell deltas accepted;
   - no retro-fold;
   - WORLD class, with the emitter package named.
   The pair names `taxsma_control/current.json` (C-S65). FWD-3 grades on its read-back.
2. **The served-key read at the 2026-10-13 13:30Z fire** (W8-S4).
3. **D1-S18:** the gold commit stamp equals the deployed code's commit, read on the next scheduled fire.
4. **FWD-5's next M4 reader repoint,** and **M9/M10 first hops for FWD-2/4/6/8**, cut only after FIRMBKTS's flip receipt passes ownership of the shared router, guard,
   behaviours, bronze_homes and firm-config files (v2.11 R2). The issuer reads that receipt before cutting.

## 4. ACTS ONLY ANDREW CAN DO (cited)

- None for this round. `/portfolios` is partner-facing, so Andrew is TOLD about the fold's page deltas, as information, before its PROD push. The push itself waits on his word
  under the push law.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-12 ~18:0xZ) -- the M4 reader repoint is NOT gated on the FIRMBKTS receipt

`2.0.0_SA_COO~D1` msg 4528, `round6/ROUND6_INPUTS_READ.md`. No FIRMBKTS flip receipt exists yet: act 2's L5-L7 wait on the ~04:00Z chain. So M9/M10 stay uncut, as written.
**Ruling:** v2.11 R2 gates acts that touch the six shared files, not FWD-5 as a whole.
- `dim_mdpf_non_model_assets.py` touches none of them, so it is cut now as `CN-g-1`, in the same issuance as the fold.
- Its source is the served `base_excluding_tax_aua`, equal on 494 of 494 dates (DELTA=0). `opal_aggregate_aua` is NOT used: it differs on 25 dates by the tax and SMA additive
  terms ($29.3M at 2026-10-09).
- The cell's close prints that 494/494 equality with its denominator.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-12 ~18:1xZ) -- ADDENDUM 1 is WITHDRAWN: the repoint is circular. Stage 6 stays on staging until the dispatch chain retires.

`2.0.0_SA_COO~D1` msg 4531 (round 6 issued @64def41849, CN-f-1 only; decomposition v6).
- `dim_mdpf_non_model_assets.py` is dispatch stage 6c (`mdpf-daily-dispatch.sh:504-524`). It runs BEFORE the 13:30Z gold fire writes that date's partition: on 2026-10-09, gold
  was written 13:31:51Z Monday and dispatch finished 12:54Z.
- The gold fire composes FROM stage 6's output. So a stage-6 reader repointed to gold reads its own downstream, one trading day stale. That is a cycle, and the DELTA=0 measured
  on history does not hold on the live day.

**Ruling:** CN-g-1 is NOT cut. Every stage-6 reader stays on the staged aggregate until the dispatch chain retires (M10/M12), where the producer order is rebuilt. No reordering
cell: reordering a live dispatch chain is M10's work, not a rider.
**FWD-5's grade** therefore counts stage-6 readers as EXCLUDED-BY-ORDER, each with this reason and the M10/M12 un-park, never as repointed. FWD-5 cannot read REALIZED before M10/M12
lands, and that is stated now so no later round grades it early.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 3 (2026-10-13 ~10:5xZ) -- MDPF_TAXSMA-S5 (ARMED since 2026-09-21, owner seat gone) is RE-OWNED to `2.0.0_SA_COO~D1` as a runner code-sync repair

Surfaced by `2.0.0_SA_COO~S1` msg 4771: MDPF_STRATID's W2 L3 runner-log half cannot be read while S5 stands.
- **The row:** the EC2 `mdpf-daily-runner`'s Stage 6 (REVAMP) has failed at IMPORT since TX-a-1's module reached the S3 code prefix at 2026-09-21T08:55:37Z.
  `dim_mdpf_aggregate_aua_timeseries.py:75` imports `taxsma_assets`, whose `:95 from lib.opal_naming import address` resolves on the repo path but NOT in the runner tree
  (`/opt/mdpf/scripts`). Stage 6 dies in 1 s, logged as "NON-FATAL build-alongside; legacy chain + serving UNAFFECTED".
- **The owner seat no longer works the project.** `2.0.0_SA_COO~T`'s MDPF_TAXSMA was paused by Andrew-direct 2026-09-21 ("wind down your team at the next logical
  checkpoint"), and the row has stood ARMED for three weeks with no one able to disarm it.

**Ruling:**
1. **Serving is not affected** (the row's own read). The gold Lambda's bundles are built by MDPF_CANON's packager and fire 16/16. The hazard is a dead build stage plus the
   readers that wait on it, of which STRATID W2 is one.
2. **The disarm is a RUNNER CODE-SYNC repair, not TAXSMA work,** so it does not resume Andrew's paused project. MDPF_CANON owns the runner's `code/` equality (CN-d-5, W9-S7).
   The disarm owner is therefore `2.0.0_SA_COO~D1`: make `lib.opal_naming` (and what it reads: the registry files) resolvable in the runner tree, by the same sync path
   CN-d-5 uses, so that Stage 6 imports.
   - Arm: Stage 6 on the next dispatch logs past the import and reaches step 6d.
   - Negative control: the legacy chain's served outputs are unchanged on that run.
3. **The pair must state Stage 6's write set from its own code BEFORE the sync.** If Stage 6 writes anything a reader serves, that set is named with rollback. If it writes only
   its build-alongside outputs, that is stated with the denominator.
4. **The row's ownership moves on the record:** the CVO re-assigns S5's `disarm_owner` at its next compile. This seat informs Andrew that his paused project left one
   ARMED row, now owned.

-- 1.0.0_SA_CTO~DELL1
