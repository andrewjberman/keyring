# MDPF_CANON -- DECOMPOSITION (L5) -- ROUND 1, THE THREAD (PRD v2.9)

```json
{
 "project": "MDPF_CANON",
 "directive": "D8",
 "macro": "MDPF",
 "fabric": "dell1",
 "decomp_version": "v1",
 "step": 5,
 "prd_ref": "org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md@12adb87963 (v2.9, ADMITTED: ratified-text re-signed by 3.0.0_SA_CVO @d8ef27e783 / @435cf1dbbd; brief current by ENDPOINT hash)",
 "order_ref": "0.0.0_AB_MSTR~DELL1 msg 2979 (seated on 1.0.0_SA_CTO~DELL1 msg 2978); CTO msgs 2995 (ruling (a)) and 3000 (the CVO's L6 condition)",
 "author": "2.0.0_SA_COO~D1",
 "round": 1,
 "rectangle": "THE THREAD (FWD-1): the per-firm gold writers (CN-a-1), the one parquet writer wired into the gold Lambda (CN-a-2), the backfill of the dated history (CN-a-3); the reader hop is the issuer's real run at close",
 "cells": 3,
 "chains": 2,
 "join_cells": 0,
 "ground_truth": "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round1/L5_FACTS.md (read-only measurement 2026-10-09 ~18:2xZ-18:4xZ)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~D1` (dell1), seated by `0.0.0_AB_MSTR~DELL1` msg 2979. **Input:**
- PRD v2.9 (ENDPOINT, CONTRACTS, DEC-1..15, CELL CANDIDATES M1-M17, PATHS, SURFACE MANIFEST);
- the L5 fact sheet;
- the CTO's L5 ruling (a), the per-firm gold writer (msg 2995);
- the CVO's L6 condition (msg 3000).

## Round 1 -- THE THREAD (FWD-1)

FWD-1's journey has four hops:
1. A figure is computed (the existing gold Lambda).
2. It is written as dated parquet where the naming rule puts it: the firm bucket for a firm, the product bucket for the composite.
3. Its history is there, one partition per date.
4. Someone answers "what did 49 Financial's total assets read on a day last month" from the stored file's name alone.

Hop 1 is served and has no cell. Hop 4 is the issuer's real run at close: list `address()`'s partitions and answer from the key's date.

| cell | hop | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|---|
| `CN-a-1` the per-firm gold writers (WORLD) | 2 (who may write) | FWD-1 (and FWD-6's fence-untouched clause) | PRD v2.9 "the firm gold writer" | `infra/aws/terraform/mdpf-pipeline/iam.tf`, `gold-lambda.tf` | -- | ~1 (worker) |
| `CN-a-2` the one parquet writer (WORLD) | 2 (what is written, where) | FWD-1 | M2, M16 | `mdpf_gold_parquet.py` (new), `mdpf_gold_consolidator.py`, its test, `build_package.py` | -- | ~2 (worker) |
| `CN-a-3` the backfill (WORLD) | 3 (the history) | FWD-1 | M3 | `mdpf_gold_backfill.py` (new), `mdpf_gold_consolidator.py`, its test, `build_package.py` | `CN-a-2` | ~3 (worker) |

**Chains:**
- Chain 1 is `CN-a-1`.
- Chain 2 is `CN-a-2` -> `CN-a-3`; they share the consolidator and the package list, so they run in sequence.

**Fan-out:** 2 of 2 chains, cap 8; `CN-a-3` is cut in the same issuance and spawned when `CN-a-2` completes.

**Deploy order at the drain** (CloudOps, `safe-apply`, never by a worker):
1. `CN-a-1`'s IAM.
2. The gold Lambda package with `CN-a-2` and `CN-a-3`.
3. One ad-hoc QA invocation of the daily path.
4. One `run_class=backfill` invocation.

The scheduled 13:30Z floor is the confirmation, never the proof.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round1/checks/`:

| check | at base | against the reference tree |
|---|---|---|
| `r1_iam.py` | 2 of 6 (ADMITTED passes live) | -- |
| `r1_emit.py` | 0 of 7 | 7 of 7 |
| `r1_backfill.py` | 0 of 7 | 7 of 7 |

**Not in round 1:**
- M1 (the census) and M7 (the basis) wait on nothing and open round 2.
- M4-M6, M8 and M11-M17 follow the PRD's arc.
- M9 and M10 wait per firm on ADVI_FIRMBKTS (at PRD).
- The publisher (M5) cannot read parquet as deployed (python3.12, no pyarrow layer; L5_FACTS section 4). That is a packaging decision for its round.
- `demo` has no writer and no object anywhere (L5_FACTS section 1), so no cell writes it.

**Known red at base, not this project's:** three `test_global_fold_flag2.py` cases fail at box/dell1 (filed as row MDPF_CANON-D1-S1);
the regression criterion deselects exactly those three by node id.


## v2 -- ROUND 2 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-09 ~21:5xZ)

**Rectangle:** `ledger/ROUND_ANALYSIS.round1.md` @409182ae5a section 3.
- Item 1 (the 2026-10-10 13:30Z daily-write read: CN-a-2 AC3, FWD-1 REALIZED) is the issuer's act, not a cell.
- Item 5 (the first account_units partitions forward) is the same read.
- Items 2-4 are four cells, independent of one another:

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-b-1` the reader census (LOCAL) | FWD-5, FWD-8 | M1 | `deliverables/READER_CENSUS.md` | -- | ~4 (worker) |
| `CN-b-2` the combined slice's basis (WORLD: a ledger row under infra/) | FWD-3 | M7 | `deliverables/X2_GLOBAL_BASIS.md`, `infra/logic/06_CONFORMANCE_LEDGER.md` (X2 row citation) | -- | ~5 (worker-light) |
| `CN-b-3` the publisher can read parquet (WORLD; no switch) | FWD-4 | M5 (capability) | `infra/aws/terraform/opal-assets/mdpf_portal_publisher.tf` | -- | ~6 (worker-light) |
| `CN-b-4` the composite grant from the builder (WORLD) | FWD-1, FWD-6 | W1-S1 ruling | `infra/aws/terraform/mdpf-pipeline/iam.tf` (+ registry row and regenerated locals if needed) | -- | ~7 (worker-light) |

**Fan-out:** 4 of 4 chains, cap 8.

**Deploy at the drain** (CloudOps, `safe-apply`):
- CN-b-3's runtime and layer change, then one publisher run whose served data-bearing leaves are byte-identical;
- CN-b-4's re-pointed grant, whose rendered policy is identical.
CN-b-1 and CN-b-2 are documents.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round2/checks/r2_checks.py` with one subcommand per cell. At base: census 2/4, basis 0/3,
publisher 1/3, builder 0/3.


## v3 -- ROUND 3 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-11 ~03:1xZ)

**Rectangle:** `ledger/ROUND_ANALYSIS.round2.md` @71e85b7191 section 3 (the CTO's enrichment list), issued after Andrew lifted the dell1
hold (CTO msg 3378, record commit cbcfdc0c1c).
- Item 1 (D1-S9: the value leg's clock, then the Monday 2026-10-12 13:30Z fire) is the issuer's act, not a cell. The clock is read:
  `deliverables/2.0.0_SA_COO~D1/round3/VALUE_LEG_CLOCK_20261011.md`, row D1-S10. The fire is read by the amended `r2_daily.py`.
- Items 2-4 are three cells in two chains:

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-c-1` the basis made true (WORLD: a ledger citation under infra/) | FWD-3 | M7 recut | `deliverables/0.9.0_WK_MDPF_CANON~8/X2_GLOBAL_BASIS.md`, `infra/logic/06_CONFORMANCE_LEDGER.md` (X2 row citation) | -- | ~8 (worker-light) |
| `CN-c-2` the bronze pull lands at the builder's address (WORLD) | FWD-7 | M8 | `data/mdpf/scripts/bronze/pull_orion_model_composition.py`, `infra/aws/terraform/mdpf-pipeline/iam.tf` (+ registry row and regenerated locals if needed) | -- | ~9 (worker-light) |
| `CN-c-3` the inflection feeder reads the bronze at the builder's address (WORLD) | FWD-5 | M4 first slice | `data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py` | `CN-c-2` (one destination, two files) | ~9 (worker-light), after `CN-c-2` |

**Why this reader first (M4):** the census (`READER_CENSUS.md`, note 3) finds one writer and one reader of `mdpf/bronze/`. The slice closes
a whole surface, moves no served output, and its seam has a real neighbour to read against. Every other reader sits behind a served
key and takes a never-widen sign-off with a before-and-after of each leaf; those are later slices.

**Fan-out:** 2 of 2 chains, cap 8; `CN-c-3` is cut in the same issuance and queued behind `CN-c-2` in slot ~9.

**Deploy order at the drain** (CloudOps, `safe-apply`, never a worker):
1. `CN-c-2`'s IAM statements.
2. The two scripts into `code/scripts/bronze/` and `code/scripts/gold/`.
3. The existing bronze objects copied to the builder's keys (DEC-8; no delete).
4. ONE on-demand run of the pull, its output listed where it landed; then ONE feeder run for the as-of, value-equal to the old home's.

**M8's gate (the CTO's):** "only if `LGIC_ENFORCE` E3 reads applied at the cut." Read: LGIC_ENFORCE is CLOSED 7 of 7 REALIZED
(`ROUND_ANALYSIS.round21.md` @55b3104426) and the builder answers the call above, so M8 is cut.

**Not in round 3:** M3's full-history clause, M6 (HELD on `LGIC_NAMING-S7`), M9 and M10 (`ADVI_FIRMBKTS`), M11-M17 follow the arc. FWD-3's
disclosure call is at Andrew (round-2 analysis section 4); `CN-c-1` is needed under either option.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round3/checks/r3_checks.py`, one subcommand per cell. At base: basis 0/3, writer 0/3, reader 0/3;
a reference tree reads 3/3, 3/3, 3/3.

### v3 AMENDMENT 1 (issuer 2.0.0_SA_COO~D1, 2026-10-11 ~03:2xZ; row MDPF_CANON-D1-W9-S1, CTO ruling msg 3417 = B)

The daily runner syncs only `code/scripts/` and `code/config/`, so neither bronze script can import `lib/opal_naming`. `CN-c-2` now also owns
a generator (`.tools/gen_mdpf_bronze_homes.py`), its output (`data/mdpf/config/bronze_homes.json`, builder output with the generator's
path, its commit and the registry hash) and the repo test that asserts each entry equals `address()` at HEAD, with an altered-entry
negative arm. Both scripts read the JSON from `../../config/`. Cells and chains are unchanged. Checks: `r3_checks.py` gains `homes`; at
base basis 0/3, writer 0/3, homes 0/3, reader 0/3; a reference tree reads 3/3 on all four.

### v3 AMENDMENT 2 (issuer 2.0.0_SA_COO~D1, 2026-10-11 ~03:5xZ; rows MDPF_CANON-D1-W9-S2, W9-S3, CTO ruling msg 3431)

The commit-time naming limb refuses a hand-written generator and its JSON as new carriers, and `opal_name` exposes no tier-bucket
output. `CN-c-2` now carries a whole-file generate target in `lib/opal_naming.py` (the `VENDOR_DISPLAY_NAMES` pattern: `VIEWS`,
`WHOLE_FILE_TARGETS`, `TARGET_REGISTRY_KEYS`, a `BLOCKS` renderer, the EN-r-6 mark) that emits `data/mdpf/config/bronze_homes.json`, and the
same feed map as a `bronze_homes` Terraform local and module output that the runner grant reads. The `.tools/` generator is withdrawn.
`.tools/naming-gate.py` is not touched. Cells and chains unchanged. Checks: `r3_checks.py homes` re-cut (the mark, builder equality,
regeneration reproduces the bytes) and `libs` added (opal_naming's tests, r6-declared-moves, r6-delta0-ordered). At base: homes 0/3, libs
3/3 (a control that must stay green), basis 0/3, writer 0/3, reader 0/3. Row D1-S11 records that three other r6 arms read FAIL at HEAD.

### v3 AMENDMENT 3 (issuer 2.0.0_SA_COO~D1, 2026-10-11 ~04:0xZ; rows MDPF_CANON-D1-W9-S4, W9-S5, CTO ruling msg 3457)

`CN-c-2`'s generate target met two more refusals. S4: the feed is declared as a registry row the renderer reads (a new registry file,
read by this target only, so no other generated view re-marks), with no firm or scope literal in `lib/opal_naming.py`; the edit carries
its own `validate` run. S5: `data/mdpf/config/` and `data/mdpf/scripts/` are classified as a `runner-code` plane measured from the
runner's real sync list (`mdpf-daily-dispatch.sh` :125, :130); where the hand sync differs from the plane the cell files a row and does
not widen the plane. Cells and chains unchanged. `r3_checks.py libs` is now 5 arms (opal_naming's tests, `validate` rc 0, `targets` rc
0, r6-declared-moves, r6-delta0-ordered); 5 of 5 at base, a guard that must stay green.


## v4 -- ROUND 4 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-11 ~06:3xZ)

**Rectangle:** `ledger/ROUND_ANALYSIS.round3.md` @ae094ea51d section 3 (the CTO's enrichment list, msg 3530) as re-cut by its ADDENDUM 1
@187b53dbe6 (msg 3542, on the issuer's evidence `deliverables/2.0.0_SA_COO~D1/round4/FOLD_AC1_AC3_CONFLICT.md`).
- Item 1 (the Monday 2026-10-12 13:30Z fire read: grades FWD-1, CN-a-2 AC3, rows D1-S9 and D1-S10) is the issuer's act, not a cell. The
  gold fire is read by `r2_daily.py read --fire 2026-10-12T13:30:00Z` after a snapshot taken before it. The Inflection feed's first
  new-home daily delivery is the runner dispatch's, not the fire's, and is read by `round4/checks/r4_daily_bronze.py` after the dispatch.
- Item 2 (the fold) is two cells, because the addendum split it: `CN-d-1` the code half (AC2 the served identity, AC3 the cottonwood leg's
  vintage in-band; AC1's fold change is withdrawn, the fold does not change) and `CN-d-2` the document half (AC1 the basis counts a
  `count_as_of` entry as a carry and lists each with its age). They share no file.
- Items 3, 5 and the repo half of 4 are `CN-d-3`, `CN-d-4`, `CN-d-5`. The WORLD half of item 4 is a CloudOps order cut at the drain.

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-d-1` served identity stated and asserted; cottonwood vintage in-band (WORLD: scripts shipped by a deploy) | FWD-3 | M7 / fold | `data/mdpf/scripts/gold/{mdpf_gold_consolidator,dim_mdpf_aggregate_aua_timeseries,dim_mdpf_account_distribution}.py`, `data/mdpf/tests/canon/` | -- | ~10 (worker-light) |
| `CN-d-2` the X2 basis counts carries (WORLD: a ledger citation under infra/) | FWD-3 | M7 recut | `deliverables/0.9.0_WK_MDPF_CANON~11/X2_GLOBAL_BASIS.md`, `infra/logic/06_CONFORMANCE_LEDGER.md` (citation only) | -- | ~11 (worker-light) |
| `CN-d-3` the Global stack meets the line (portal candidate, LOCAL) | FWD-3 | M7 / W8-S3 | `portal/src/lib/pairedProvenanceRead.ts`, `portal/src/pages/ModelPortfolios.tsx` | -- | ~12 (worker-light) |
| `CN-d-4` the count-source audit reads the gold artifact (LOCAL) | FWD-5 | M4 second slice | `data/mdpf/scripts/gold/mdpf_revamp_count_source_audit.py` | -- | ~13 (worker-light) |
| `CN-d-5` the runner `code/` equality step (LOCAL, repo half) | FWD-7 | W9-S7 | `.tools/mdpf-code-equality.py`, `docs/deployment/MDPF_RUNNER_CODE_SYNC.md` (both new) | -- | ~14 (worker-light) |

**Fan-out:** 5 of 5 chains, cap 8. Every pair of cells has disjoint write sets and no data edge. The one shared file is the append-only
surprise channel `INVESTIGATION_v1.md`, which is read-only to every cell except for a row.

**Why this reader (M4, `CN-d-4`):** every other remaining producer reader sits behind a served key or on a tree whose writer moves with it
(`READER_CENSUS.md` note 1), and each of those takes a never-widen sign-off with a before and after of every leaf. The audit writes nothing it
serves, and the artifact it audits already exists at the builder's address (CN-a-2, CN-a-3).

**Deploy at the drain** (CloudOps ~DELL1, a WORLD order the issuer cuts after the drain; never a worker):
1. `CN-d-1`'s three scripts, AFTER `MDPF_STRATID.TO-APPLY-R2.global-fold-deploy` reads CLOSED (it names `mdpf_gold_consolidator.py` too; two
   acts never copy one key in one window). The added `meta` keys change the served account-distribution bytes, so the order carries a
   never-widen pair (CTO + COO) naming that blast radius and the per-key rollback (the prior object's VersionId).
2. `CN-d-5`'s tool run whole, every non-EQUAL name classified, then ONLY the files the dispatch chain executes or reads, named, through the
   step the document writes down; read back with `--files`.
3. `CN-d-3` is a portal candidate: it goes to `1.0.0_SA_CTO~DELL1` for review before DEV, with the issuer's render beside it.
4. `CN-d-2` and `CN-d-4` ship nothing.

**The item-4 close, restated (carried to the CTO in the L10 message):** the analysis closes "`code/` reads equal to the repo for
`data/mdpf/scripts` and `data/mdpf/config`". Measured 2026-10-11 ~05:3xZ (md5 against ETag, tests directories excluded locally): scripts gold
35 local / 23 equal / 4 differ / 8 missing, backfill 11/6/2/3, feeders 5/3/1/1, bronze 2/2/0/0, config 4/2/0/2. Most non-equal names are not
runner members (QA tools, a bundle-shipped file, a non-.py data file), so whole-tree equality is not a goal. The close this decomposition
holds: every file the dispatch chain executes or reads is EQUAL, and every other non-EQUAL name is listed with its reason.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round4/checks/`. At base: `r4_cn_d_1.py` 0/5, `r4_cn_d_1_vintage.py` 0/3, `r4_cn_d_2.py` 1/4 (B2 is
a control), `r4_cn_d_3.py reader` 1/4 and `page` 1/5 (controls), `r4_cn_d_4.py reader` 0/3 and `seam` 0/1, `r4_cn_d_5.py tool` 0/5 and
`live` 0/2. A reference tree reads 5/5, 3/3, 4/4, 4/4, 5/5, 3/3, 2/2, 5/5 and 2/2.

**Not in round 4:** M3's full-history clause; M6 (HELD on `LGIC_NAMING-S7`); M9 and M10 (wait on `ADVI_FIRMBKTS`); M11-M17 follow the arc.
FWD-3 stays NOT REALIZED at Andrew's X2 call (open call fe9b), whatever `CN-d-1` and `CN-d-2` read. The CTO's "align or refuse" ruling on
the global account-distribution is withdrawn (ADDENDUM 1); the declared window and the in-band vintage replace it.


## v5 -- ROUND 5 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-11 ~07:5xZ)

**Rectangle:** `ledger/ROUND_ANALYSIS.round4.md` @c902dcb1b5 section 3 (the CTO's enrichment list, msg 3597). Round 4 closed 5 of 5 MET and the issuer's
restated `code/` close was accepted ("every file the dispatch chain executes or reads is EQUAL; every other non-EQUAL name is listed with its reason").
- Item 1 (the CN-d-1 deploy, acts D1 and D2, closing W8-S4) and item 2 (the `code/` sync, WORLD half, its own window, never beside D1) are CloudOps
  orders, not worker cells. Item 1 is `ADHOC.canon-r4-code-deploy` @359072576e, already issued and WAITING on `MDPF_STRATID.TO-APPLY-R2`; its leg e
  prints and classifies the `code/` tree and deploys nothing. Item 2's order is cut after that classification exists and after item 1's ledger
  CLOSED, so the two never share a window.
- Item 3 (the gold fire reads: Sunday 2026-10-11 13:30Z read-only, Monday 2026-10-12 13:30Z graded; FWD-1, CN-a-2 AC3, D1-S9, D1-S10) and item 4
  (the first new-home bronze delivery, FWD-7) are the issuer's acts: `round4/checks/r4_daily.py` and `r4_daily_bronze.py`, pre-fire snapshot taken.
- Item 5 (the next M4 reader) is the one cell, `CN-e-1`.

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-e-1` the aum-timeseries instrument reads the gold artifact (LOCAL) | FWD-5 | M4 third slice | `data/mdpf/scripts/gold/dim_mdpf_aum_timeseries.py`, `deliverables/0.9.0_WK_MDPF_CANON~4/READER_CENSUS.md` (two rows) | -- | ~15 (worker-light) |

**Fan-out:** 1 of 1 chains, cap 8.

**Why this reader, and why not the one the analysis expected:** `verify_mdpf_revamp_conditions.py` reads four cells that are not columns of the
wide parquet at the builder's address (`cohort_provenance`, `meta.latest_cross_section.partner_custody_total`, `by_model.<sma>.count_as_of`,
`meta.count_coverage_end`); a repoint needs a logic change or a change to the one gold writer, which is the CTO's ruling, not a cell
(`deliverables/2.0.0_SA_COO~D1/round5/CN_E_1_CANDIDATE_READ.md`). Every other remaining reader feeds a served key and takes a never-widen pair.
`dim_mdpf_aum_timeseries.py` is a read-only instrument whose staging write is retired; measured DELTA=0 on 2958 of 2958 cells.

**Open fork carried to the CTO (not decided here):** repoint a never-canonical, uncalled instrument at all, or retire it (build ladder step 1);
and whether the verifier's missing cells go into the gold writer.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round5/checks/`. At base: `r5_cn_e_1.py reader` 0/5 and `seam` 0/1, `r5_cn_e_1_census.py` 1/4 (C4 is a
control). A reference implementation reads 5/5, 1/1 and 4/4.

**Not in round 5:** M3's full-history clause; M6 (HELD on `LGIC_NAMING-S7`); M9 and M10 (`ADVI_FIRMBKTS`); M11-M17; FWD-3 at Andrew's X2 call
(open call fe9b).


## v6 -- ROUND 6 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-12 ~18:3xZ)

**Rectangle:** `ledger/ROUND_ANALYSIS.round5.md` @7cbc4492c0 section 3 (the CTO's enrichment list, msg 4526) and, for the fold cell, the CTO's record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/RECORD_FE9B_RULED_BY_CLUSTER_LEAD_20261012.md` ADDENDA 1-5 (cluster lead ruling (A) on open call
`dell1-20261011T053810Z-fe9b`; msgs 4393, 4398, 4414, 4418, 4422, 4439), read with the issuer's design `deliverables/2.0.0_SA_COO~D1/round6/FOLD_DESIGN.md`
@2f702bb7ff (with its CORRECTION notes) and `FOLD_ADDENDUM2_READ.md` @01b9e95401. Round 5 closed: FWD-1 and FWD-7 REALIZED (the CTO, 17:5xZ).
- Item 1, the fe9b fold, is ONE cell, `CN-f-1`. It serves FWD-3 (the X2 grant's basis, "aggregate counts only"); row `D1-W8-S5` disarms on its
  read-back and the open call closes on it. Its pair names `mdpf/global/state/taxsma_control/current.json` (C-S65).
- Item 2, the served-key read of the global account-distribution on the 2026-10-13 13:30Z scheduled fire (W8-S4), is the issuer's act, read by
  `round4/checks/r4_daily.py` and the object itself; not a cell.
- Item 3, D1-S18 (the gold commit stamp lags the deployed code), is a leg of the fold's CloudOps deploy plan: the function's `MDPF_GOLD_COMMIT` is set
  from the pin actually built, and the stamp is read on the first scheduled fire after it. Not a cell.
- Item 4, FWD-5's next M4 reader and the M9/M10 first hops: M9/M10 are NOT cut, because no FIRMBKTS flip receipt exists at this issuance (act 2's L5-L7
  wait on ~04:00Z; `fb-f-19` L6 NOT EXERCISED; `OWNERSHIP-PASS` is a step of the round-4 window runbook, not yet written; PRD v2.11 R2). The next M4
  reader is NOT cut as a cell either, on a measured fact: see below.

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-f-1` the Global min-firms fold: per date, a model-class line is shown only where >= 2 firms hold it; the rest fold into `other_models`, itself shown only where >= 2 firms hold it; the differential identity asserted fail-closed (WORLD: scripts shipped by a deploy; an `infra/` file) | FWD-3 | M7 / fold (fe9b) | `data/mdpf/scripts/gold/{mdpf_gold_consolidator,dim_mdpf_account_distribution,dim_mdpf_aum_metrics,mdpf_revamp_model_crosswalk}.py`, `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/mdpf_revamp_model_crosswalk.py` (second home, byte-equal), `data/mdpf/tests/canon/test_global_min_firms_fold.py` (new) | -- (a deploy-order edge, not a data edge) | ~16 (worker) |

**Fan-out:** 1 of 1 chains, cap 8. Reason: one behaviour with a cross-file contract (`fold_keys` / `fold_emit` between the consolidator and the
distribution builder); splitting would put that contract between two workers who share the consolidator.

**The next M4 reader, measured and not cut (`dim_mdpf_non_model_assets.py`, round 6 item 4).** The repoint is a one-file reading change and was drafted
to DELTA=0 (`base_excluding_tax_aua` equals the staged enterprise total on 494 of 494 dates; `opal_aggregate_aua` differs on 25 dates by exactly the tax
and SMA additive terms, $29,345,854.15 at 2026-10-09). It is not a one-cell hop, because of ordering: the dispatch runs it as stage 6c
(`mdpf-daily-dispatch.sh:504-524`), the same dispatch whose stage 6a writes the staged aggregate, and the gold partition for a date is written
by the gold lambda's 13:30Z fire AFTER the dispatch (partition 2026-10-09: 2026-10-12 13:31:51Z; the dispatch finished 12:54Z). At dispatch time the
newest gold partition is the PREVIOUS trading day, so a repoint builds one day stale, and the gold fire then composes from that staged output.
The same holds for every stage-6 reader. Drafts: `round6/draft/TO-CN-g-1.DRAFT.md` and its checks. The question is put to the CTO (leave stage 6 on the
staged aggregate until the dispatch chain retires, or cut a reordering cell). No cell is cut for it in this round.

**What the cell is, in one paragraph:** `apply_global_min_firms_fold(arts, firm_scopes, min_firms=2) -> (arts_out, report)` in the consolidator,
called through `guard_global_min_firms_fold(arts, _isolated)` directly after `guard_global_served_identity`, so a refusal refuses Global alone.
The held predicate is the firm's own `model_value > 0` on that date; the as-of fold set is computed from the objects on every run; per date, a
line held by fewer than two firms goes to the pool; the pool is emitted as `other_models` only where two firms hold it; the dollars that leave
are suppressed, never redistributed; the differential identity `model_aua - sum(by_model)` moves by exactly the suppressed dollars on every
valued date or the build refuses. SMA-class lines and `tax` are untouched (the SMA tree already serves `by_firm` by Andrew-direct ruling).

**Deploy at the drain** (CloudOps ~DELL1, a WORLD order the issuer cuts after the drain; never a worker): by the CN-d-1 order's own shape, in its OWN
window, clear of the FIRMBKTS window acts and of the router, guard, behaviours, `bronze_homes.json`, `firm-config.mjs` and WAF rider before its flip
receipt (R2). It carries a never-widen pair (CTO + COO): blast radius the four global aggregate objects and the global gold parquet partitions FROM
THE FIRST NEW-DATE FIRE ONWARD (no firm scope, no staged object, no dated key already served; no retro-fold), N = 8 writers across 7 leaf classes, the
three branches, the per-key rollback, the C-S65 state-write clause, and the client-visible deltas the CTO accepted (Total Holdings -185, archetype
cards -$43.16M, per-model trend and the ten core quarter cells beginning 2026-05-15).

**The close, restated (carried to the CTO in the L10 message):** FWD-3 reads REALIZED when (a) the first scheduled run after the deploy serves a
global aggregate-aua-timeseries on which no model-class line is held by fewer than two firms on any date it carries a value, (b) the identity
differential read-back holds on every valued date and the pre-existing residual is printed with its denominator, (c) the in-band statement is
present and names no model, and (d) the round-5 close stands (every file the dispatch chain executes or reads is EQUAL; every other non-EQUAL name is
listed with its reason).

**Checks:** `deliverables/2.0.0_SA_COO~D1/round6/checks/`. At base (HEAD of box/dell1): `r6_cn_f_1.py contract` 0/10, `seams` 0/6,
`r6_cn_f_1_comparator.py` 1/11 (K0 is a control). A reference tree (`checks/ref/make_reference_tree.py`, never committed to product paths) reads
10/10, 6/6 and 11/11; on the real 2026-10-09 objects it reads fold set 11, other_models emitted on 47 dates and not shown on 438, per-model detail
beginning 2026-05-15, identity checked on 485 dates with 0 gaps. Three planted defects turn it red.

**Not in round 6:** M9 and M10 (FIRMBKTS flip receipt not written); the next M4 reader (measured circular, above); M3's full-history clause; M6
(HELD on `LGIC_NAMING-S7`); M11-M17; the `code/` sync of the 8 runner members (its own WORLD window after the fold's deploy ledger closes, never beside it).


## v7 -- ROUND 7 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-14 ~14:2xZ)

**Rectangle:** `ledger/ROUND_ANALYSIS.round6.md` @65bf603a7a section 4 (the CTO's enrichment list, msg 5589), read with section 3 (the three ARMED-row rulings). Round 6 closed MAY-CLOSE
(`round-close-check.py`, AC4 MET, D1-C-S67). FWD-3 REALIZED. One cell per list item; the CTO's item 1 is four cells (CN-h-1, CN-i-1, CN-j-1, the repair CN-k-1), item 2 is two
(CN-l-1 served, CN-l-2 portal), items 3 and 4 are one each (CN-m-1, CN-n-1), item 5 (D1-S24) rides the repair cell with D1-S23 (repairs batched into ONE cell).

**Rulings the issuer took inside its own decomposition (recorded here, graded by `to-pipeline-gate.py`):**
- *The refusal-arm run has no QA prefix.* The CTO's "writing to a QA prefix only" is met as "writes nowhere": the gold lambda documents qa_local as zero S3 writes (the shadow-prefix veto), and
  `lib/opal_naming.py` has no QA, scratch or ephemeral address kind, so no builder call can name one. CN-n-1's instrument refuses any AWS call that is not a read; the before/after
  listing of the served prefix is the evidence. If the dry run cannot complete in the worker's shell, the cell falls back to its guard arm plus a finding row.
- *The Other Models card text is a second cell.* CN-l-1 serves the `as_of`; CN-l-2 draws it. CN-l-2 edits `portal/src/pages/ModelPortfolios.tsx`, which CN-i-1 owns, so it is the SECOND
  order on CN-i-1's worker queue and starts from that branch's committed result; it is client-facing and lands only through `portal-merge-forward.sh` with Andrew as approver
  (CLAUDE.md Portal, fcdfc34843).
- *The census is a cell, with the issuer's pre-read stated.* CN-m-1's face carries the issuer's pre-read (28 of 8,831 files name the key; four readers; the accrual bridge a candidate) labelled as the issuer's, not the worker's result.
- *One gold-package deploy for CN-h-1 and CN-l-1,* if both are VALID at the drain, under ONE never-widen pair covering both blast radii; CN-l-1's pair is drafted at the drain with the CTO's half. Not a cell.
- *Correction to the round-6 drain-end packet (row D1-S24):* its `/portfolios` line "Total Holdings 8,607 -> 8,607" was my wrong-date read (the account-distribution is keyed by the RUN date, 2026-10-14; I passed the frontier date).
  The CTO's -177 (8,607 -> 8,430) stands; CN-k-1 makes the tool default to the newest distribution key and print the date it read.

**Fan-out:** 7 of 7 chains, cap 8. Chains: `CN-h-1`; `CN-i-1` -> `CN-l-2`; `CN-j-1`; `CN-k-1`; `CN-l-1`; `CN-m-1`; `CN-n-1`. Reason: disjoint write sets (the one shared file, `ModelPortfolios.tsx`, puts CN-l-2 on CN-i-1's queue).
Slots: ~17 CN-h-1, ~18 CN-i-1 then CN-l-2, ~19 CN-l-1, ~20 CN-m-1, ~21 CN-n-1, ~22 CN-k-1, ~23 CN-j-1.

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-h-1` the frontier account counts read the newest A4 account-distribution at or before the axis date, never the staged runner object; no A4 -> the loader returns absent, never a fallback (S5 disarm; WORLD: a script shipped by a deploy) | FWD-5 (the lambda's inputs leave the runner-only objects); FWD-1 (the served counts are the day's roster) | M4 / S5 (MDPF_TAXSMA-S5) | `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`, `data/mdpf/scripts/gold/tests/test_canplat_p1_1.py` and `test_global_fold_flag2.py` (one stub lambda each), `data/mdpf/tests/canon/test_frontier_counts_a4.py` (new) | -- (a deploy-order edge: after the fold's first scheduled fire is read; one change per fire) | ~17 (worker-light) |
| `CN-i-1` the AUA Trend groups its custom models into ONE 'Custom Models' series (the fold's `other_models` replaced, every scope), draws the strategy groups in the Total Assets colours through one exported palette (ETF Strategies = pfde + the two carve-out SMA lines carved out of `non_model_aua`; ALT Strategies = `tax_additive_aua`, vermilion500 on the Trend; Client Supervised / Unsupervised chips AS-OF ONLY from the page's existing category-views object; Other AUA the true remainder), no served-object change, no new key (LOCAL: a portal DEV candidate; client-facing at the PROD push) | FWD-9 | portal / AUA Trend | `portal/src/components/CategoryViewTree.tsx` (two exports), `portal/src/lib/trendGrouping.ts` (new, pure), `portal/src/pages/ModelPortfolios.tsx` | -- (the Client chips' dated history waits on its own route cell) | ~18 (worker) |
| `CN-j-1` the history leaf: one read-only served series per scope (`platinum/mdpf/{scope}/category-views-history.json`: `dates[]` plus the two Client aum arrays) assembled by the publisher from the dated category-views objects it already lists; absent is null, a malformed dated object is omitted and named (WORLD: a publisher package deployed by CloudOps; four new served keys) | FWD-9 | M7 / FWD-9 Client chips (history route; CTO msgs 5086-5088) | `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py`, `.../tests/test_completeness.py` (three serve-write filters only), `.../tests/test_history_leaf.py` (new) | -- (a deploy-order edge to `CN-i-1`: its Client chips draw the history from this leaf once served; `CN-i-1` ships as-of first without it) | ~23 (worker) |
| `CN-k-1` the two read-side repairs batched in one cell: the code-equality tool compares the git blob (the bytes `safe-deploy` serves), not the working tree, and prints each EQUAL name's basis and CR count (row D1-S23); `portfolios_card.py after` defaults to the newest account-distribution key's run date and prints, as its first line, the date and the exact key read for each of the three types, with a WARN when a newer distribution key exists (row D1-S24) (LOCAL, direct-act: two operator tools, no served byte) | FWD-7 (the runner's `code/` equality read is the instrument of the round-4 close (d)); FWD-3 (the `/portfolios` before/after is the card to Andrew) | M7 / instruments (D1-S23, D1-S24) | `.tools/mdpf-code-equality.py`, `.tools/tests/test_mdpf_code_equality_blob.py` (new), `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/portfolios_card.py` | -- (no data edge; no shared file with `CN-h-1`, `CN-i-1`, `CN-j-1`) | ~22 (worker-light) |
| `CN-l-1` the Global aum-metrics `Other Models` row carries its date or is blank: pool present on the as-of -> current, no stamp; no pool but a pooled date within 4 calendar days -> that date's value with `as_of` = that date; none within 4 days -> the row is absent; every other model key keeps its fallback; the carried row's count is the count at its carried date (rows D1-W16-S2, D1-W16-S4; WORLD: a script shipped by a gold-package deploy; the served half only) | FWD-3 (a combined line never shows stale dollars as current); FWD-1 (the served figures are the day's) | M7 / fold (fe9b) follow-on | `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py`, `data/mdpf/tests/canon/test_aum_metrics_dated_carry.py` (new) | -- (a deploy-order edge only: one change per fire with `CN-h-1`; the portal half `CN-l-2` waits on this cell's served `as_of` and on `CN-i-1`) | ~19 (worker-light) |
| `CN-l-2` the Model Portfolios card draws `as of <date>` under the Other Models value when the served row's `as_of` is present and differs from the page's own as-of date, and nothing extra otherwise; an absent row stays absent; the label text lives in one pure helper (LOCAL: a portal DEV candidate; client-facing at the PROD push) | FWD-3 (a combined line never shows stale dollars as current) | portal / aum-metrics card (rows D1-W16-S2, D1-W16-S4, the portal half) | `portal/src/lib/otherModelsAsOf.ts` (new, pure), `portal/src/pages/ModelPortfolios.tsx` (three lines of wiring and one guarded span), `portal/src/api/endpoints/aum.ts` (one optional field) | `CN-i-1` (the same page file: ONE queue, `CN-i-1` first; no data edge); the served stamp it reads is `CN-l-1`'s contract, tolerated absent, so no build-order edge to it | ~18 (worker, continuing `CN-i-1`) |
| `CN-m-1` the staged-copy READER CENSUS: who reads `s3://opal-data-assets/gold/mdpf_revamp/global/aggregate_aua_timeseries.json` (the unfolded staged global aggregate, row D1-W16-S5), in five classes -- code consumers, scheduled consumers, static IAM grants, live IAM decisions, and the S3 read-evidence coverage of the bucket -- every count printed with its denominator, every reader classed by whether its output reaches a partner-facing prefix, the zero case recorded as a zero with its denominator and never as an absence (LOCAL: a record under the worker's deliverables folder; AWS get/describe/simulate reads only, no write) | FWD-3 (a combined figure held by fewer than two firms must not survive on a reachable surface); FWD-5 (the lambda's inputs leave the runner-only objects) | M7 / S5-adjacent (D1-W16-S5) | none in the product tree; the record `deliverables/0.9.0_WK_MDPF_CANON~20/CN-m-1_READER_CENSUS.json` (+ `.md`) | -- (reads the consolidator, the dim_* scripts and the accrual script at its own base; `CN-h-1` and the dated-carry cell change other files in `data/mdpf/scripts/gold/`, so a census read of those files names the base it read) | ~20 (worker) |
| `CN-n-1` the refusal arm DRIVEN: one QA run of the gold consolidator's `build_all` in `dry_run` mode in which the run's own in-memory firm builds are edited so the Global fold's pool is held by ONE firm on the as-of; Global is refused WHOLE with the guard's refusal text, the siblings are not touched, the refusal is logged, and the served prefix is identical before and after (a botocore write guard blocks and records any non-read call). QA, never production evidence (LOCAL: no S3 write is possible in the run; AWS reads only; no product file changes) | FWD-3 (the third arm of CN-f-1's close: a one-firm as-of publishes no Global object and the prior one stays served) | M7 / fold (D1-W16-S1) | none in product paths. Record files only: `deliverables/0.9.0_WK_MDPF_CANON~21/run/{qa_run.json,qa_run.log,served_before.json,served_after.json,s3_ops.json}` | -- (no data edge; read-only beside `CN-h-1` and `CN-j-1`, whose merges change other files than the consolidator path the run exercises) | ~21 (worker) |

### CN-h-1




**Why this and not the nine-key sync / Stage 6:** the CTO's ADDENDA 4-5 ruled out a Stage 6 revival and moved the S5 disarm to the lambda's input. The
read `round6/TAXSMA_S5_STAGE6_READ.md` @7de2c1aa99 shows Stage 6 has been dead since 2026-08-14 for three stacked reasons; this cell removes the
lambda's dependence on its output instead.

**Close (carried to the CTO):** S5 reads DISARMED when, on the first scheduled fire after the deploy that mints a new date, every overridden key's
served frontier `account_count` equals the selected A4 map's value, the stamp's as-of is the A4's period, no staged object was requested, and the
per-scope moves equal the pair's table within the stated A4 key date.

**Not in this cell:** Stage 6 and everything that revives it; the nine `lib` keys; the IAM change on the runner role; `dim_mdpf_account_distribution.py`;
the staged object's retirement (M12); W2 L3's runner-log half (parked at M10 by the CTO).

**Checks:** `deliverables/2.0.0_SA_COO~D1/round7/checks/` (drafts at `round7/draft/checks/`). At base: `r6_cn_h_1.py reader` 1/8 (H0 a control), `seams`
1/4 (S4 a control), `comparator` 1/5 (K0 a control). A scratch reference tree (`checks/ref/make_reference_tree_h1.py`, never committed to product
paths) reads 8/8, 4/4, 5/5.

### CN-i-1



independent chains if both are issued in one round. `portal_ref:` the portal `DEV` HEAD at the cut.

**What it is not (the CTO's rulings, msgs 5086-5088):** the dated category-views history route (its own cell and pair, read-only over the existing dated
objects; FWD-9 grades with it live); any change to the ALT colour (vermilion500 stays, the pin test stands); any back-cast or interpolation; any firm-scope
carve-out or Client arithmetic (measured at Global only; firm scopes get the Custom Models grouping and the relabelled bands).

**Close (carried to the CTO):** FWD-9 reads MET for the series set and the sums when the rendered Global trend, from the folded object, shows the five canonical
series unchanged, ONE 'Custom Models' in the Total Assets Custom colour and no 'Other Models', 'ETF Strategies' (pfde + carve-outs) in the Total Assets colour,
'ALT Strategies' (`tax_additive_aua`) in vermilion500, on the as-of date the Client chips and a true-remainder Other AUA, on the other dates one Other AUA and no
Client segment, no '-$0', and a stack that adds to `opal_aggregate_aua` to the cent (the fold's suppressed dates excepted, read from the fold's record); and
PARTIAL (named) for the Client chips until the history route cell lands: the draw arms B (2026-08-27) and the dated middle of the axis wait for it.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round7/checks/` (drafts at `round7/draft/checks/`). At base: `r7_cn_i_1.py module` 0/1 (the module is absent), `page`
2/8 (P6 and P8 are controls that hold), `data` 5/5 (it grades the SERVED inputs: the stack to the cent on 486 valued dates, the Client gap equal to the carve-outs
on 21 of 21 same-date objects; a control, not a build test). A scratch reference patch reads module 9/9 and page 8/8; four mutants (null coalesced to 0; a hex
literal beside a group label; the grouping gated on Global; ALT recoloured from Total Assets) turn M2, P5, P4 and P6 red (`r7_cn_i_1.py selftest` prints
`ROUND 7 SELFTEST: OK`).

### CN-j-1



independent chains if the three are issued in one round, cap 8.

**What it is not:** the portal fetch and the chips (`CN-i-1`); any consolidator, gold-lambda or edge change; a change to the artifact-type axis or `a4_expected` (the leaf is not a gold
type); a repair of the publisher's unreadable pointer (a separate finding, its own pair).

**Close (carried to the CTO):** FWD-9's Client-chip history reads exercised when the four leaves are served and equal the dated Client nodes, every existing served leaf is unchanged
apart from `_provenance.written_at`, and the Trend (`CN-i-1`) draws the chips on the leaf's dates and absent elsewhere on `bun run dev:live` at a stated portal commit.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round7/checks/` (drafts at `round7/draft/checks/`). At base: `r7_cn_j_1.py unit` 0/6, `seam` 3/8 (S2 pairs unchanged, S7 no served-plane read
beyond the pointer, S8 the publisher's own 12 tests are controls that hold), `real` 2/6 (R0, R2 controls: the 91 dated objects read; both Client nodes on every one). A scratch reference
(`checks/ref/make_reference_publisher_j1.py`, never committed to product paths) reads 6/6, 8/8 and 6/6; `selftest` prints OK with two planted mutants RED (a missing node read as 0.0 -> U3;
a leaf that ignores the pointer -> S3).

**Not in this cell:** the portal side; the readback script `round7/checks/r7_history_readback.py` (owed before issuance); the CloudOps deploy order and the pair's CTO half.

### CN-k-1

small read-side repairs the CTO batched into one cell; about 110 product lines; direct-act path.

**Close (carried to the CTO):** D1-S23 reads closed when the tool's NAMED line for `mdpf_model_registry.json` reads `EQUAL (blob)` with its CR count on a CRLF checkout and the true
`bronze_homes.json` difference still reads DIFFER; D1-S24 reads closed when `portfolios_card.py after` with no date reads the newest run-date key and its first line names it.

**Not in this cell:** any change to a deploy path (`safe_deploy_core.py` is correct), the `code/` sync itself, `bronze_homes.json` (FIRMBKTS-owned), any served object, the pinned
`portfolios_card_before.snapshot.json`.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round7/checks/` (drafts at `round7/draft/checks/`, scratch references under `.../ref/`, never committed to product paths). At base:
`r7_cn_k_1.py tool` 3 of 6 (T2, T3, T6 are controls), `card` 1 of 5 (C4 a control); the scratch references read 6 of 6 and 5 of 5; the existing `r4_cn_d_5.py tool` reads 5 of 5 at base
and on the reference (the regression guard).

### CN-l-1

chain (portal files). No shared file with any of them. Reason: one behaviour, one file, about 35 product lines.

**One cell or two:** two. The served half is `CN-l-1`. The portal half, `CN-l-2` (the card draws "as of <date>" when the row's `as_of` differs from the page's), edits
`portal/src/pages/ModelPortfolios.tsx`, which `CN-i-1` owns, and `portal/src/api/endpoints/aum.ts`; it is sequenced AFTER `CN-i-1` on the portal chain (same file, no
parallel write), is a client-facing portal rung (DEV by `portal-merge-forward.sh`; PROD on Andrew's word), and is NOT a one-line hookup (a type field, a mapping, card
text). It is cut in this issuance as `CN-l-2`. `CN-l-1` does not wait on it: an unread extra row key is inert.

**Close (carried to the CTO):** D1-W16-S2 and D1-W16-S4 read DISARMED when, on the first scheduled fire after the deploy, the Global `aum-metrics` `Other Models` row
equals the rule's reading of that day's served time series (current and unstamped where the pool exists on the as-of; stamped with the last pooled date where it does not
and that date is within 4 days; absent otherwise), no other by_model row differs from the prior day's rule, and `total`/`meta` key sets are unchanged. The refusal-arm QA run
(the CTO's item 3) is a separate cell.

**Not in this cell:** the card text and any portal file; `dim_mdpf_aggregate_aua_timeseries.py` (`CN-h-1`); the consolidator fold; per-firm aum-metrics (the fold line is Global-only);
retro-stamping dated objects; a `meta` key.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_l_1.py` (drafts at `round7/draft/checks/`). At base: `unit` 3/8 (U1, U5, U6 controls), `seams` 3/5 (S1, S2, S5
controls), `real` 3/6 (R1, R5, R6 controls). A scratch reference tree (`checks/ref/make_reference_tree_l1.py`, never committed to product paths) reads 8/8, 5/5, 6/6; the four
planted defects turn `nocap` U4+R4, `noasof` U2+U3+U7+U8+R2+R3, `allkeys` U6, `frontiercount` U7 red.

### CN-l-2

(`CN-l-2` adds no chain). Reason: both orders edit `portal/src/pages/ModelPortfolios.tsx`; a second parallel writer on one file is a merge conflict by construction, and the
hand-on is the same subagent continued with its context intact (`/dispatch` Step 5).

**What it is not:** any change to the served object (that is `CN-l-1`); a card for an absent row; a date computed from the clock or from another series; a friendlier date
format; a second print site; the Trend, the colours, or anything `CN-i-1` owns.

**Close (carried to the CTO):** D1-W16-S2 and D1-W16-S4 read DISARMED on the portal side when the rendered Other Models card, at a stated portal commit, shows no extra line
where the pool is present, `as of <date>` where the value is carried, and no card where the row is absent (the CVO reads it at L9; AC3 is judgment). Landing is
`.tools/portal-merge-forward.sh cand/dell1/<slug>` on a row whose approver is Andrew (client-facing); the PROD push of the page is his word.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_l_2.py` (drafts at `round7/draft/checks/`). At base: `helper` 0/1 (the module is absent), `page` 3/8 (P6, P7, P8
are controls). The reference helper reads 7/7 and the reference page patch 8/8, alone and on top of CN-i-1's reference patch (the two cells' anchors do not overlap);
four page mutants and one helper mutant turn the named arms red; `selftest` prints OK. The reference lives inside the check file's `selftest` (never written to product paths).

### CN-m-1



surprise channel). Reason: one record, one reader, five instruments.

**What it is not:** the re-point of any reader that reaches a partner-facing surface (the CTO's rule: a re-point of such a reader to the folded object is its own cell under a
pair, cut only if the census finds one); moving the staging write behind the fold guard; retiring the staged key; any AWS write; enabling CloudTrail data events or S3 server access
logging on `opal-data-assets` (a billed infrastructure change, Andrew's moratorium on new monitors applies); the other staged keys (`49financial`, `inflection`, `cottonwood`),
which share the shape and are named in the record only where a reader's pattern covers them.

**Close (carried to the CTO):** D1-W16-S5 reads DISARMED when the record (a) lists every reader of the key in the five classes with its denominator, (b) classes each reader's
output as NONE / INTERNAL / PARTNER-FACING-CANDIDATE / PARTNER-FACING with the output key named for the last two, and (c) carries a verdict the evidence permits: a ZERO-READERS
verdict is PROVEN only where runtime reads are observable. On this bucket they are NOT (the issuer's pre-read: no data-event selector and no server access logging cover
`opal-data-assets`), so a zero static count reads ZERO-STATIC-READERS-RUNTIME-UNOBSERVED and does not disarm the row alone. Any PARTNER-FACING or PARTNER-FACING-CANDIDATE reader is
re-pointed to the folded object under a never-widen pair (a later cell).

**Checks:** `deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_m_1.py` (draft at `round7/draft/checks/`). At base (no record): `record` 0/1 (M0 record not found), `verify` 1/5
(V1 key-exists is a control that holds), `selftest` 6/6 (a good record passes; five planted defects each turn a named arm red). A scratch reference record (built from the real
repo scan, never committed) reads `record` 7/7 and `verify` 5/5.

### CN-n-1

the issuance HEAD, so the run exercises the consolidator and loader code AS ISSUED, before any round-7 merge.

**Why no QA S3 prefix (a finding, not a gap).** `mdpf_gold_consolidator.lambda_handler` documents it: QA-LOCAL MODE runs the FULL build with `dry_run` semantics and local A4 bodies, "ZERO S3 writes
anywhere ... no scratch S3 prefix -- the shadow-prefix veto" (CLAUDE.md: no shadow or build-alongside output path). `lib/opal_naming.py` has no QA, scratch or ephemeral address kind (a case-insensitive
search for `qa`, `scratch`, `ephemeral`, `sandbox` returns nothing), so a QA prefix would be a hand-typed name that Rule 30 refuses. The CTO's "writing to a QA prefix ONLY" is therefore met as
"writing nowhere": the instrument installs a botocore guard that raises on every operation not named Get, Head, List, Describe, Lookup or Simulate and records the call kinds.

**The plant.** In the run, `spine.build_global_artifact` is wrapped; before it calls the real function the wrapper edits the three firm artifacts IN MEMORY: on the last date, every model-class line held
by fewer than two firms keeps its value at ONE firm and is set to None at the others. The real function then builds Global from those, `guard_global_served_identity` passes (the headline arrays are
untouched), and `guard_global_min_firms_fold` finds the pool held by one firm on the as-of and refuses (CN-f-1 AMENDMENT 1). No served object is read into the plant as a write source; no served object is edited.

**Risk class, who acts, pair.** LOCAL: the cell changes no product file, deploys nothing, and cannot write to S3 (the guard blocks it). It is a worker's act (the issuer authored the instrument; the worker runs it
once outside the 13:30Z fire window and files the record). No CloudOps seat, no ledger entry, NO never-widen pair: the blast radius is empty by construction and is MEASURED by three independent reads
(served snapshots equal, no write-kind call, a live head of the prior Global ts by key and VersionId).

**Close (carried to the CTO):** the refusal arm reads DRIVEN when `r7_cn_n_1.py grade` reads 6 of 6 and `served` reads 4 of 4 on the committed record. The ORGANIC one-firm as-of day stays the negative
arm and is read when it occurs; this QA is never production evidence.

**Not in this cell:** any change to the guard, the fold or the consolidator (read-only); any deploy; any QA key, prefix, table or bucket; reading the deployed lambda (the run is the repo code at the cut, which equals the
deployed package `51cfc93ea8` by the 13:30Z fire's R9).

**Checks:** `deliverables/2.0.0_SA_COO~D1/round7/checks/` (drafts at `round7/draft/checks/r7_cn_n_1.py`). At base: `grade` 0/6 and `served` 0/4 (no run record: FAIL as expected); `guard` 5/5 (a CONTROL: it grades
the guard code already merged, over the served unfolded objects of 2026-10-09, GETs only). `selftest`: a synthetic good record passes and five planted defects turn it red.


## v7 AMENDMENT 1 -- CN-i-2, the repair of the AUA Trend candidate (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-14 ~19:5xZ)

**Why a cell is added to a drained round:** the CVO graded CN-i-1 AC4 NOT MET (`surprise-channel/adjudications/ADJUDICATION_v10.md`, D1-C-S73) and the CTO directed the repair (msgs 5705, 5719); PRD v2.18 @0736ed5c23 (ADMITTED, ratified-text half signed by the CVO) rules the stack clause: exception (ii) of FWD-9 (2) covers the 383 dates before the per-model detail begins, NO band. The cut is the CTO's direction; the order file is added under the audited pipeline-override line (the round-7 issuance is closed to new order files). `fanout: 1 of 1 chains, cap 8`, worker slot ~24, base = the approved candidate branch `cand/dell1/mdpf-canon-aua-trend-groups-and-as-of` (34cd12d2d0), `portal_ref:` that branch. My REC of an exception (iii) band was refused by the CTO (FWD-3: never drawn); the measurement is `round7/STACK_SUM_MEASURE_20261014.md`.

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-i-2` the repair of the AUA Trend candidate: `Client Unsupervised` leaves the locked Ultra-Short Term orange (lime500, at least 10 CIEDE2000 from every other Trend colour), the tooltip draws no row for a series that is absent on the hovered date, and the page states "per-model detail begins <date>; earlier model assets are in the Total and are not broken out" where it draws dates before the served boundary, with NO band for them (v2.18); the readback classifies the stack against the Total so it can fail (LOCAL: a portal candidate repair; client-facing at the landing) | FWD-9 (the Trend, DONE WHEN (2) as ruled in v2.18, (3) and (4)) | portal / AUA Trend repair (CVO D1-C-S73) | `portal/src/components/CategoryViewTree.tsx` (one L1_COLOR entry), `portal/src/lib/trendGrouping.ts` (two pure exports), `portal/src/api/portal-proxy.ts` (one optional type field), `portal/src/pages/ModelPortfolios.tsx` (three edits) | CN-i-1's candidate branch `cand/dell1/mdpf-canon-aua-trend-groups-and-as-of` @34cd12d2 (the worker's base is that branch, not DEV); the CVO's signature of v2.18's ratified-text half (LIMB 6) | ~24 (worker) |

**What the cell is, in one paragraph.** On the candidate branch the Trend's Client Unsupervised resolves through the shared `L1_COLOR` to orange500, the locked Ultra-Short Term hex (CIEDE2000 0.0). The cell moves that one entry to lime500 (minimum 20.59 from the Trend colours, 19.94 from the Total Assets table), so the Total Assets breakdown's Client Unsupervised
bar and dot repaint with it (named in the approval row). It adds `presentTrendEntries` so `renderTrendTooltip` lists a series only where it holds a value (a measured zero stays), and `trendDetailNote` so the Global Trend states where per-model detail begins, read from the served `meta.by_model_fold.per_model_detail_begins`
(the type gains the optional field; no fetch). It draws nothing for the suppressed model assets: the stack is below the Total by the whole model AUA on the 383 earlier dates, which exception (ii) of FWD-9 (2) covers by the CTO's ruling.

**Close (carried to the CTO and the CVO):** CN-i-1 AC4 stays NOT MET until the repaired head is read. The repaired head reads MET when, at a STATED portal commit on `bun run dev:live --port 5174`, at Global: Client Unsupervised is not in the Ultra-Short Term hex and no pair of Trend colours is under 10 CIEDE2000; a hover on dates C and D prints no Client row and no `$0`
row; the note is on the face; no band is drawn; and the readback prints BEFORE-DETAIL 383, EXACT 49, FOLD-OR-OTHER 55 with FAIL 0 (the counts of the served 2026-10-13 object; they move with the object). The new candidate gets a FRESH client-facing approval row naming the four changes from head 34cd12d2.

**Not in this cell:** a band, series or number for the suppressed dates; a Trend-local colour override; any change to `STACK_SERIES`, the locked model colours, Custom, ETF, Client Supervised or ALT (vermilion500, pinned); any served-object change; per-firm boundaries (the per-firm objects carry no fold meta); the history-leaf failure surfacing (CN-j-2); the Other Models "as of" text (CN-l-2).

**Checks:** `deliverables/2.0.0_SA_COO~D1/round7/checks/r8_cn_i_2.py` (drafts at `round7/draft/checks/`). At base (the candidate branch): `build` 3 of 13 (C1, C4, N4 controls), `data` 3 of 3 by design (served inputs), `regress` 2 of 2 (the CN-i-1 arms stay green). A scratch reference
patch (`checks/ref/make_reference_tree_i2.py`, never committed to product paths) reads `build` 13 of 13 and `regress` 2 of 2; six mutants turn C2/C3, T2, N2, N4, N3 and N1 red; the classifier fails three planted defects that CN-i-1's D1 accepted. `selftest` prints OK.


## v7 AMENDMENT 2 -- CN-i-3, the Global AUA Trend returns to PROD's text (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-14 ~20:3xZ)

**Why:** Andrew declined the Trend as built by CN-i-1 and CN-i-2 (approval row 19ae CLOSED declined; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_201xZ_PORTFOLIOS_SMOKE_TREND_FULL_HISTORY_COTTONWOOD_SPEC.md` @caf5dc7d73) and approved every other edit, the lime repaint and the 49 Financial view. The CTO directed (msg 5831): one candidate branch, the feature's changes with the Global AUA Trend byte-equal to PROD's, the 49F view unchanged, held. `fanout: 1 of 1 chains, cap 8`, worker slot ~25, `portal_ref:` `scratch/canon-i3-base` (PROD 5ab67a65 plus the three feature commits). The cell is a per-scope choice between two texts that already exist; it writes no new Trend behaviour. The order that carries it is the CN-i-2 order file, MODIFIED and reopened (the TO issuance gate's one-issuer-per-round limb: a re-cut into the first issuance modifies its orders and adds no file); it owns CN-i-2 and CN-i-3.

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-i-3` the Global AUA Trend draws PROD's text (the five models, Non-Model, Additive SMA sleeves, Tax-Managed SMA, no custom grouping, no Client chips, no boundary note) while every other scope keeps the feature's text; the lime colour, the Other Models "as of" and the type fields stay (LOCAL: a portal candidate; client-facing at the landing, held) | FWD-9 (the Trend, held at PROD's layout pending the full-history spec) | portal / Global Trend revert by scope | `portal/src/pages/ModelPortfolios.tsx` | -- (CN-i-1, CN-i-2 and CN-l-2 merged) | ~25 (worker) |

**Not in this cell:** the full-history Trend (the CRO's spec), any change to Inflection or Cottonwood beyond what the feature already does (put to the CTO), fixing DEV (`9e637fe51e` carries the declined Trend; the CTO's), the Cottonwood Trend upgrade.
**Checks:** `round7/checks/r8_cn_i_3.py` (`sites`: P1 PROD's removed lines present, P2 the feature's added lines present; `scope`: S1 only ModelPortfolios.tsx changed, S2 the protected files byte-equal). At base: `sites` 1 of 2, `scope` 1 of 2; selftest OK. They are source-level; the issuer's real run (a render of the Global Trend against PROD's) is what proves which text each scope draws.


## v9 -- ROUND 9 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-14 ~21:5xZ)

**Rectangle:** the Variant 1 Global AUA Trend (PRD v2.19 @02852d9d16, v2.20 @038b2173f3, v2.21 @3826492d9c; the CRO spec `org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_CANON_GLOBAL_AUA_TREND_FULL_HISTORY_SPEC_20261014.md` @686f769e63; Andrew-direct ~20:4xZ, "What I want is whatever CRO~DELL1 and I agreed on", record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261014_204xZ_COO_D1_WHATEVER_CRO_DELL1_AND_I_AGREED.md`), cut on the CTO's msgs 5868, 5873, 5877, 5886 (the dell1 restart HELD), plus the edge firm gate the laptop CTO ruled LIVE on XA-c7cd (CTO msg 5913, "cut FIRST in this round"). Three cells: `CN-q-1` the edge gate (first), `CN-p-1` the producer, `CN-p-2` the portal. Rounds 7 and 8 are drained and their orders stay as delivered; CN-i-3 is WITHDRAWN (CTO msg 5877).

**Rulings the issuer took inside its own decomposition:**
- *The served contract is fixed here so the producer and the portal cut in parallel:* on the Global `aggregate-aua-timeseries` object, top-level `client_supervised_aua[]`, `etf_strategies_aua[]`, `alt_strategies_aua[]` (number or null, aligned to `dates[]`; null before the group's first value, rolled FORWARD only) and `carried_dates[]` (ISO strings). `point_class[]` is not touched. CN-p-2's build reads this contract on fixtures; only its real run waits on CN-p-1's deploy.
- *The new keys go on EVERY scope* (all-None / `[]` off Global), because `assert_keyset_identity` has no ruled extra and a Global-only key refuses the whole run; the alternative, an `R2_RULED_EXTRAS` entry, is a contract amendment for the CTO. The four-scope gold parquet therefore gains three series columns (new partitions only); the never-widen pair names it. Put to the CTO as a cut decision, not an open question.
- *The SMArtX read goes through the CRO's two registry rows* (`legacy_addresses.json` @ff00e3e265: `smartx-platform-silver-fact-model-aum-daily`, `...-allocation-roster`, params `date`, reader MDPF_CANON); the code types no key. CN-p-1's base must contain that commit (it does: the worktree's base is past it).
- *CN-q-1 is WORLD by the gate floor* (`infra/` paths floor at WORLD), though the worker writes code and tests only; the deploy is a separate crossbox ORDER to the laptop CloudOps seat (`DEPLOY_ORDER_CNQ1_DRAFT.md`), on the issuer's written GO naming the pin. No never-widen pair is owed for it (the CTO's word, msg 5913: no served output moves). Three places the code departs from the CTO's measure or ask are resolved in the order's record face: the stale "403 swallowed" comment (the distribution has no custom error response), the legacy `json/mdpf` prefix also gated, and the firm-less claim reading `global` (as ruled; the CTO may strike it).
- *CN-p-2 carries the approved edits unchanged* (lime Client Unsupervised, the Other Models "as of", the 49 Financial view, Inflection and Cottonwood as built): ONE client-facing row, ONE smoke (CTO msg 5877). It also carries a one-line composition footnote (Inflection from 05-15, Cottonwood from 05-28, estimated to 07-20) that the drafter added and I kept; it shows to internal sessions only and the CTO may strike it. The portal base is `scratch/canon-i3-base` (f8c7d310); portal PROD moved to 5d64641891 meanwhile, in four files none of which this cell touches, so the approval-row candidate is re-cut from PROD by cherry-pick as before.
- *CN-j-2 is WITHDRAWN* (the CTO's condition: no page reads the category-views history route after CN-p-2). READER CENSUS, printed: `git grep -l -i -e views-history -e ViewsHistory -e views_history` over every tracked file of the portal ref: `scratch/canon-i3-base` 0 of 2,172 files, `DEV` 0 of 2,173, `PROD` 0 of 2,170; the positive control `category-views` matches on all three. CN-p-2 adds no reader (it reads the Global aggregate series). The census covers the portal repo only; a lambda, script or other-repo reader is outside it. CN-j-2 was never a cut cell; the record is this paragraph.

**Fan-out:** 3 of 3 chains, cap 8. Chains: `CN-q-1`; `CN-p-1`; `CN-p-2`. Reason: disjoint write sets; the one data edge (CN-p-2's real run reads CN-p-1's deployed arrays) is mine, not a worker queue edge, since CN-p-2's build is graded on contract-shaped fixtures. Slots: ~28 CN-q-1, ~26 CN-p-1, ~27 CN-p-2.

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-q-1` the edge admits a per-firm MDPF leaf only to the claim's own firm: `auth-validator-edge` refuses (403) a non-internal claim on any `/api/general/mdpf/<folder>/` (and the frozen `/api/general/json/mdpf/`) whose folder is not the claim's own; `opal-capital` and `Dev` pass all; `demo` and a firm-less claim read `global` only; any other firm reads nothing; no role, `firmRole` or `tier` widens it (the BUILD is LOCAL code and tests; the WORLD act is a separate CloudOps deploy order) | cross-firm containment of the MDPF serve (XA-c7cd; row MDPF_CANON-D1-S27; PRD FWD-2 scoped route `/api/general/mdpf/{firm}/`, DEC-5); no FWD is served by it, it is a CTO-directed remediation of a live gap | edge / viewer-request firm gate | `infra/aws/lambda-edge/auth-validator-edge/mdpf_gate.mjs` (new, pure, no imports), `infra/aws/lambda-edge/auth-validator-edge/index.mjs` (one import line, one marked block), `infra/aws/lambda-edge/auth-validator-edge/tests/mdpf_gate.spec.mjs` (new) | -- (none; it touches no served object and is independent of CN-p-1 and CN-p-2) | ~28 (worker); the deploy: `0.7.0_AE_CloudOps~U7` (laptop) by crossbox order |
| `CN-p-1` the Global aggregate-aua-timeseries serves the Trend groups: `client_supervised_aua[]` (= `non_model_aua` - Dividend - Growth - Opal Global All Equity Total Return; SMArtX before 2026-05-18, Global's carve-outs from it), `etf_strategies_aua[]` (= Dividend + Growth + `sma_additive_aua`), `alt_strategies_aua[]` (= `tax_additive_aua`, Tax-Managed only), each aligned to `dates[]`, null before the group's first value, rolled FORWARD from the last known value on a row with no value, and `carried_dates[]` (the dates a group was rolled forward; the 9 no-total dates today); every other scope gains the same keys all-None / `[]`; ONE SMArtX partition read through the two registry rows (`legacy_address`), never a typed key; the category tree drops "Muni SMA" from `SMA > ALT Strategies` (WORLD: a script shipped by a gold-package deploy; new keys on four scopes, one tree member removed) | FWD-9 (the Trend groups are READ from the served series, never recomposed; the amended oracle holds to the cent); FWD-3 (no pre-2026-05-15 per-model value enters any Global leaf: v2.20) | M7 / FWD-9 Variant 1 (PRD v2.19-v2.21; CRO spec @686f769e63) | `data/mdpf/scripts/gold/mdpf_gold_consolidator.py`, `data/mdpf/scripts/gold/mdpf_category_registry.py` (one tuple), `data/mdpf/tests/stratid/test_stratid_round2_inside_model.py` (one assertion), `data/mdpf/tests/canon/test_global_trend_groups.py` (new) | -- (a data edge OUT: `CN-p-2`'s real run reads the deployed fields; its build reads the contract in this row and waits on nothing); the registry rows `smartx-platform-silver-fact-model-aum-daily` and `...-allocation-roster` (landed, `ff00e3e265`); a deploy-order edge: one change per fire, after CN-h-1/CN-l-1's fire is read | ~26 (worker) |
| `CN-p-2` the Global AUA Trend draws the whole history, 2024-11-01 to the as-of: Client Supervised, ETF Strategies and ALT Strategies are FIELD READS of the Global series' new top-level arrays `client_supervised_aua[]`, `etf_strategies_aua[]`, `alt_strategies_aua[]` (aligned to `dates[]`) with `carried_dates[]` naming the dates on which values were carried forward; Client Unsupervised, the as-of Client chips and Other AUA are retired at Global; Custom Models is the served difference `model_aua` - the five lines once the fold's pooled line is served, and for an INTERNAL session only Inflection's own series inside the single-firm window; the five model lines before 2026-05-15 are 49 Financial's own series, stitched read-side for an INTERNAL session only (Variant 1); every other session (the demo tenant opens Global) draws Variant 2 -- one `Models` band before 2026-05-15, Custom suppressed inside the window with the footnote "models held at one firm are in the total and not broken out", the "Per-model detail begins" note kept; carried points draw with their class and a tooltip/legend marking; the logic lives in exported pure functions of `trendGrouping.ts` (LOCAL: a portal candidate; client-facing at the landing; carries the approved edits -- lime Client Unsupervised, the Other Models "as of", the 49 Financial view -- unchanged: ONE row, ONE smoke) | FWD-9 (the Trend, DONE WHEN as amended by v2.19, v2.20, v2.21); FWD-3 (the read-side stitch: a non-internal session cannot reach a single-firm value through the page) | portal / AUA Trend, Variant 1 | `portal/src/lib/trendGrouping.ts` (pure exports), `portal/src/pages/ModelPortfolios.tsx` (the wiring), `portal/src/api/portal-proxy.ts` (four optional type fields) | `CN-p-1` for the REAL RUN only (the served arrays and `carried_dates` must be deployed before the render on 5174); the BUILD does not wait: it is graded on contract-shaped fixtures against the CRO spec's amended period-end oracle | ~27 (worker) |

**Why a cell is cut for a gap that no FWD names:** the laptop CTO ruled on XA-c7cd (msg 109249, relayed by MSTR 5912 and the box CTO 5913) that the gap is LIVE and that MDPF_CANON builds the gate, cut first in this round. Evidence: the box CTO's measure `MEASURE_XA_C7CD_MDPF_CROSS_FIRM_EDGE_20261014.md` @b4d483cac4 (the deployed `auth-validator-edge:23` has no `mdpf` string; `public-data-router:7` rewrites the prefix with no firm check; no-token 401, but a foreign-firm read was never run for want of a login).

**What the cell is, in one paragraph.** The page resolves one id per session (`effectiveFirmId`: the internal selector, `global` for the demo tenant, otherwise `claims.firmId`) and interpolates it into the path, so the folder a claim may read is a function of the claim alone:
`49financial`, `inflection` and `cottonwood` read their own folder, `demo` and a firm-less claim read `global`, `opal-capital` and `Dev` read everything (the predicate `aggregate_gate.mjs` already uses for the Opal-only aggregate), and any other `firmId` reads nothing. The check runs after the JWT verify and the aggregate gate, on the path the origin will resolve (the query dropped, ONE percent-decode, dot segments and slash runs
considered): a non-internal request is refused unless its raw URI begins with the prefix, every segment is plain, and the folder equals an admitted one exactly. It is a pure module (`mdpf_gate.mjs`, no imports, so it bundles into the one-file function) called from one marked block in `index.mjs`. The denial is a 403 (the distribution has no custom error response; a 401 would trigger the portal's token refresh) with a body that names nothing, one `mdpf_scope_denied` log event and no token in any log.

**Not in this cell:** the deploy (a crossbox order to the laptop CloudOps seat with a NEVER-2 ledger); CloudFront standard logging (Andrew's separate ask); the tracked plaintext password in `portal/.frontend-dev/auth/login-constitution.json` (for Andrew); the S3 bucket policy and the `public-data-router` rewrite; any served-object change (so no never-widen pair).

**Checks:** `round9/checks/r9_cn_q_1.py` (+ `q1_harness.mjs`, `ref/`). At base (box/dell1 @3a6a8d98e0): `handler` 6 of 14 (A1, A2, A4, A11, A13, A14 are controls), `seam` 4 of 5 (S2-S5 controls), `control` 2 of 5 (K1, K3 controls). A scratch reference (`ref/make_reference_cn_q_1.py build`) reads 14 of 14, 5 of 5, 5 of 5; the nineteen planted defects (thirteen gate mutants M1-M13, six handler defects I1-I6) each turn the arms they name red (`make_reference_cn_q_1.py mutants` prints `MUTANTS: ALL CAUGHT`); `selftest` prints OK.
The harness drives the REAL handler with the JWT verify replaced in-process (a `node:module` resolve hook), so it needs no `node_modules`, no AWS and no network.

**Close (carried to the CTO and the CVO):** the build is graded by AC1-AC3. The outcome is graded after the deploy: a live no-token read of a per-firm leaf is 401, the live association version is the newly published one on every behavior that carried `:23`, and the deployed bundle's code answers the synthetic claim matrix as AC1 does (see `DEPLOY_ORDER_CNQ1_DRAFT.md`). A live 403 for a real partner login is NOT provable (no partner or demo login exists); the bundle replay is the stated substitute.

### CN-p-1
**One cell, one chain.** Three functions in the consolidator (`compute_trend_groups` pure, `load_smartx_sma_legs`, `apply_global_trend_groups`), one wiring call pair in `build_all` after the fold, one registry tuple removed, one assertion edited, one new test file. About 130 product lines; two behaviours (the groups; the Muni removal). Independent of `CN-p-2` for the build.

**Contract fixed here for `CN-p-2` (served on Global):** `client_supervised_aua[]`, `etf_strategies_aua[]`, `alt_strategies_aua[]` (number or null, aligned to `dates[]`), `carried_dates[]` (ISO strings). `point_class[]` is unchanged (the headline stays byte-equal); a carried point is marked from `carried_dates`. Custom Models is not served: the portal takes `model_aua` minus the five primary lines from 2026-05-15, and the internal-session stitch supplies the earlier dates.

**Measured (read-only, served 2026-10-13 Global object and SMArtX partition 2026-10-14):** the rule reproduces the amended oracle at the 9 period ends (max diff 0.00M); the partition (`model_aua` + groups + the pre-05-15 Global All Equity TR leg) equals the total on all 487 dated rows; SMArtX equals Global's carve-outs on 103 overlap dates ($0.00); SMArtX covers all 384 pre-05-18 dated rows; `tax_additive_aua` is null on all 486 earlier rows; the gold lambda role is ALLOWED `s3:GetObject` on both keys (APPLIED plane).

**What it is not:** any pre-2026-05-15 per-model value in a Global leaf (PRD v2.20); Custom Models; a change to `point_class`, `opal_aggregate_aua`, `by_model` or any existing `meta` key; a `R2_RULED_EXTRAS` entry (the keys go on every scope instead); the portal; the deploy; the pair.

**Close (carried to the CTO):** FWD-9's producer half reads MET when, on the first scheduled fire after the deploy that mints a new date, the served Global object carries the four keys aligned to `dates[]` and equal to the rule's reading of that day's own fields and SMArtX partition (the amended oracle at the nine period ends; the partition identity on every dated row; `carried_dates` equal to the dated rows with no total), the other scopes carry them all-None / `[]`, every pre-existing key of every scope is equal to the prior day's rule, and no scope's `category-views` lists "Muni SMA".

**Not an open question, decisions the drafter took:** (1) keys on every scope (key-set identity, `assert_keyset_identity`, has no ruled extra); (2) the four-scope gold parquet gains three series columns (new partitions only); (3) SMArtX absent on every candidate day -> the pre-05-18 groups stay None and the run stays green, a denied or failed read raises `C2-SIBLING FAIL-LOUD` and Global is refused alone; (4) `TREND_SMARTX_UNTIL` = 2026-05-18 is a constant from the CRO spec.

**Never-widen pair (COO half, drafted after the cell builds):** count the writers of each moved leaf (N printed), both branches (SMArtX present; SMArtX absent for every candidate day), a rollback per key, prior VersionIds, the headline sums byte-equal, `category-views` Muni member removed on the scopes that listed it.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round9/checks/` (scratch reference under `.../ref/`, never committed to a product path). At base: `r9_cn_p_1.py pure` 2 of 7 (M0, P0 controls), `seams` 2 of 6 (S0, T2 controls), `oracle` 2 of 7 (O0, Om controls). A scratch reference tree (`checks/ref/make_reference_tree_p1.py <dest>`) reads 7 of 7, 6 of 6, 7 of 7. Six planted defects (`--mutant typed-literal | no-gaetr | no-test-edit | keep-muni | no-allscope | mutates-input`) each turn at least one arm red.

### CN-p-2
**What the cell is, in one paragraph.** The page asks the pure module for one row per served date: `buildGlobalTrendRows(served, stitch, trendModeFor(internal), meta.by_model_fold.per_model_detail_begins)`. The module reads the Total and the three group arrays as served (no arithmetic, no rounding), takes the five model lines from the Global series on and after the boundary and, for Variant 1 only, from 49 Financial's own series before it, takes Custom Models by the served difference once the fold's pooled line (`other_models`) is served and, for Variant 1 only, from Inflection's own Custom series before that, and rolls a null FORWARD only on a date listed in `carried_dates` and only after the series' first value. Variant 2 (every non-internal session) never receives the single-firm series: the builder ignores the stitch, and the page does not even fetch it (the two single-firm reads are enabled only when `internal`). The same row feeds the period-end bars and the daily area, so both charts agree.

**Reader census, printed for the CTO's CN-j-2 call (read at 2026-10-14 ~21:0xZ, portal repo, `git grep -l -i -e views-history -e ViewsHistory -e views_history` over every tracked file of the ref):** `scratch/canon-i3-base` 0 of 2,172 files; `DEV` 0 of 2,173; `PROD` 0 of 2,170; positive control `category-views` in `src/` matches on all three. So no portal file reads the history leaf `category-views-history.json` at base, on DEV or on PROD, and this cell adds none (it reads only the Global aggregate series, which is where the spec puts Client Supervised). CN-j-2 (surface a history-row error) has no portal reader to serve in this tree; the leaf's other possible readers (a lambda, a script, a non-portal repo) are outside this census.

**Not in this cell:** the producer's arrays, `carried` rows, the SMArtX read and the category tree's "Muni SMA" removal (`CN-p-1`); the Custom pre-2026-05-15 sliver (Opal Global All Equity Total Return, about $0.05M, 2024-08-30 .. 2025-03-26: no served array carries it, so the stack misses it by at most $0.05M while Client Supervised already excludes it -- put to the issuer); any per-firm Trend change; the Cottonwood Trend; fixing DEV `9e637fe51e`.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round9/checks/r9_cn_p_2.py` . `oracle` 7 arms (C1 a control), `variants` 10, `wiring` 9 (C2 and W8 controls). At the base (`scratch/canon-i3-base` f8c7d310): `oracle` 1 of 7, `variants` 0 of 10, `wiring` 2 of 9. A scratch reference (`checks/ref/make_reference_cn_p_2.py` + `cn_p_2_helpers.ts`, never committed to a product path) reads 26 of 26; eighteen planted mutants each turn the arm(s) that name them red; `selftest` prints OK. The pure arms run `bun` on the module (not source-line matching); the page arms read CRLF-folded, whitespace-collapsed text, so a rewrapped expression passes. The reference module typechecks under `tsc --strict`; the page wiring is NOT compile-checked (the issuer runs the type check at the drain). They are source and fixture checks: which pixels the two sessions draw is the issuer's real run (AC4, judgment).


## v10 -- ROUND 10 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-15 ~16:0xZ)

**Rectangle:** `ledger/ROUND_ANALYSIS.round9.md` @ff1e47f079 section 4 (the CTO's enrichment list, msg 6037), read with the CTO's generalisation of item 1 (msg 6047) and PRD v2.22 @9d4dab1941 (ADMITTED: the CVO re-signed the ratified-text half). Round 9 graded: CN-p-1 AC4 MET (C-S81), CN-p-2 AC4 MET (C-S89), CN-h-1 AC4 MET (C-S82), CN-j-1 AC4 NOT MET and closed by v2.22 (C-S83), CN-l-2 AC3 held on a render (item 6). Items to cells: 1 to CN-r-1 (a producer cell under a never-widen pair); 2 to CN-r-2 (the publisher's read grant); 3 DONE by the issuer (the readback prints every restated cell, `48c40b2375`); 4 to CN-r-3 (E4, a CloudOps measurement, no worker); 5 ALREADY BUILT (CN-p-2 AMENDMENT 1: the footnote renders at Global only, on PROD `c3b21a40e2`; measured by the Inflection per-firm walk of 2026-10-15 01:31Z); 6 the issuer's two renders (no cell, nothing ships: the Other Models card under a planted no-pool state, and a non-internal Variant 2 session under a synthetic claim on 5174); 7 the CVO's clock; 8 not a cell (the Cottonwood Trend upgrade waits on the CRO's spec).

**Rulings the issuer took inside its own decomposition (recorded here, graded by `to-pipeline-gate.py`):**
- *Item 1 is ONE rule (the CTO, msg 6047):* on a total-bearing row a missing Dividend, Growth or `sma_additive_aua` carries its last known value ONLY IF the carried row still partitions the served Total (override (d); the Total is read, never recomposed); where the Total itself excludes the leg (`sma_additive_aua` on 2026-08-31..09-09, measured: missing on 7 total-bearing dates, ETF dips 0.41M there) the leg stays absent. The CN-p-1 oracle arms O3-O5 stay green; on today's data the cell moves no cell.
- *CN-r-2 grants the served prefix, not `latest.json` alone:* the publisher also reads the served keys to re-hash them (`_publish_one`), and a denied read there republishes the pair, so a `latest.json`-only grant would not end the 18-of-18 republish. It is still ONE added read-only inline policy on `opal-assets-mdpf-egress-publisher-role`, `s3:GetObject` on `opal-data-portal-v2/platinum/mdpf/*` (the prefix the role already writes); the CTO reads this contradiction at the round-N analysis.
- *Never-widen:* CN-r-1 takes a pair (it moves a served leaf's rule; COO half drafted after the cell builds). CN-r-2 moves no served byte and widens a ROLE by one read; it deploys under a NEVER-2 ledger and a before and after policy read, with no pair (the CTO may ask for one). CN-r-3 writes no object and removes what it creates.
- *CN-r-3 is a CloudOps order, not a worker cell, and is STAGED:* its precondition is the CTO's GO and the filter set (`draft/ADHOC.canon-r10-e4-reader-measure.md`); request metrics name hours, bytes and prefix and do NOT name the principal (`round10/E4_MEASURE.md`: no instrument covers the bucket today).

**Fan-out:** 2 of 2 worker chains, cap 8 (CN-r-1, CN-r-2; no edge between them, disjoint write sets). CN-r-3 has no worker. Slots: ~29 CN-r-1, ~30 CN-r-2.

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-r-1` the Global aggregate-aua-timeseries carries a missing Dividend, Growth or `sma_additive_aua` leg: in `compute_trend_groups`, on a TOTAL-BEARING row a missing leg takes its last known value ONLY IF the carried row still partitions the served Total (`total - model_aua - (Client Supervised + ETF + ALT) - the Global All Equity TR allowance` within 0.011; the Total is read, never recomposed), decided per leg; forward only, never before the leg's first value; one memory per leg across 2026-05-18; the Global All Equity TR leg never carried; the date joins `carried_dates[]` ONLY when a leg actually carried; where the Total excludes the leg (the sleeve on 2026-08-31..09-09) it stays absent as today; no key is added and no existing key moves (WORLD: a script shipped by a gold-package deploy; on today's data no served cell moves) | FWD-9 (the Trend groups are READ from the served series; PRD v2.22 override (c) a gap carries its last known value, bounded by override (d) the groups partition the Total) | M7 / FWD-9 Variant 1 (PRD v2.22; the CTO's round-9 analysis section 4 item 1 and ruling msg 6047) | `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` (two constants, three helpers, the statements of `compute_trend_groups`), `data/mdpf/tests/canon/test_global_trend_groups.py` (five tests added) | `CN-p-1` (built and deployed; this cell edits its function); a deploy-order edge: one change per fire, after the round's other gold changes; the first-fire readback `r9_trend_groups_readback.py` (amended R11) | ~29 (worker) |
| `CN-r-2` the publisher role may READ what it serves: one added inline policy on `opal-assets-mdpf-egress-publisher-role` grants `s3:GetObject` on `arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/*` (the prefix the role already writes, and the prefix its NEVER#3 scoping record names), builder-named (`opal_name`: system `mdpf`, function `publisher-live-serve-read`, kind `policy`), ungated, a SEPARATE resource so the plan reads "1 to add" and the existing write, list, Gold and Tax-control grants stay byte-equal. With it the `latest.json` pointer is readable (prior rows return, `prior_pointer_note` is null) and the served keys are readable (the unchanged branch's re-hash of the served object passes), so a pair whose gold and Tax control have not moved reports `unchanged` and the 18-of-18 republish ends. The grant covers the served keys as well as the pointer because `_publish_one` reads both: a pointer-only grant leaves every Tax-extended pair on the REPAIR path (the served-sha read raises, `served_ok` is false, the pair republishes). The build is LOCAL Terraform source; the WORLD act is a separate CloudOps deploy order (targeted `safe-apply`, one publisher hand-run, NEVER-2 ledger) | FWD-2 (the publish is idempotent: an unchanged pair writes nothing); CTO round-9 analysis section 4 item 2 and section 3 (b) (`ROUND_ANALYSIS.round9.md`); no served byte moves when the proof holds | publisher / IAM read of the served prefix | `infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf` (one module block and one resource block appended after the Tax-control policy; nothing else in the file changes) | -- (none: a build edge to no other cell; touches no served object. A deploy-order edge: after the round-10 gold-side cells' fires are read, so the first idempotent publisher run is not confused with a data change; and the proof holds only while no gold or Tax-control change lands between the last publish and the proof run) | ~30 (worker); the deploy: `0.7.0_AE_CloudOps~DELL1` by ADHOC order `ADHOC.canon-r10-publisher-latest-read-deploy` |
| `CN-r-3` E4: one day of S3 request metrics on `opal-data-assets` (one `EntireBucket` filter plus a short named prefix list, 24 hours, read by hour and by prefix, then removed), a MEASUREMENT RECORD that names the hours, the prefix and the bytes of the 53 GB egress reader and states plainly that it does NOT name the principal (WORLD: a bucket configuration created and deleted; no object write or delete; no alarm, dashboard or standing metric) | none of FWD-1..FWD-9: a CTO-placed remediation of an unattributed cost (laptop CTO @06ffa2a6e8, dell1 CTO @e65d1fed56; round-9 analysis section 4 item 4) | S3 egress / E4 (placement; MDPF_CANON owner) | no product file. The order's own files: `org/tier2_senior/0.7.0_AE_CloudOps~DELL1/task_orders/ADHOC.canon-r10-e4-reader-measure.md` (the carrier), the CloudOps deliverable `.../deliverables/canon_r10_e4/E4_READER_MEASURE.md`, the NEVER-2 ledger and sentinel `mdpf-canon-r10-e4-reader-measure` | -- (no data edge; it touches no MDPF object). A precondition edge to the CTO's written word on the filter set and the cost estimate, and a stop condition: any existing metrics configuration on the bucket | 0.7.0_AE_CloudOps~DELL1 (no worker; WORLD) |

### CN-r-1` block below are this cell's.

Table row (columns as in the v9 table: cell | serves (cell_refs) | candidate | owned files | depends on | actor):

| `CN-r-1` the Global aggregate-aua-timeseries carries a missing Dividend, Growth or `sma_additive_aua` leg: in `compute_trend_groups`, on a TOTAL-BEARING row a missing leg takes its last known value ONLY IF the carried row still partitions the served Total (`total - model_aua - (Client Supervised + ETF + ALT) - the Global All Equity TR allowance` within 0.011; the Total is read, never recomposed), decided per leg; forward only, never before the leg's first value; one memory per leg across 2026-05-18; the Global All Equity TR leg never carried; the date joins `carried_dates[]` ONLY when a leg actually carried; where the Total excludes the leg (the sleeve on 2026-08-31..09-09) it stays absent as today; no key is added and no existing key moves (WORLD: a script shipped by a gold-package deploy; on today's data no served cell moves) | FWD-9 (the Trend groups are READ from the served series; PRD v2.22 override (c) a gap carries its last known value, bounded by override (d) the groups partition the Total) | M7 / FWD-9 Variant 1 (PRD v2.22; the CTO's round-9 analysis section 4 item 1 and ruling msg 6047) | `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` (two constants, three helpers, the statements of `compute_trend_groups`), `data/mdpf/tests/canon/test_global_trend_groups.py` (five tests added) | `CN-p-1` (built and deployed; this cell edits its function); a deploy-order edge: one change per fire, after the round's other gold changes; the first-fire readback `r9_trend_groups_readback.py` (amended R11) | ~29 (worker) |

### CN-r-1
**One cell, one chain.** Two module constants, three small helpers (`_leg_present`, `_partitions`, `_leg_carry`) and about fifteen statements inside one pure function; five tests added to the CN-p-1 test file. About 45 product lines; one behaviour. Independent of the other round-10 cells for the build.

**Rule fixed here (the CTO's, msg 6047):** a leg value is PRESENT when it is a number (0.0 is a value; None and NaN are absence). On a total-bearing row an absent Dividend, Growth or `sma_additive_aua` carries the leg's last known value only if the carried row partitions the served Total within 0.011; otherwise it reads 0.0 as today. Each leg is decided alone. A leg that has never had a value is not carried. `gaetr` is never carried. A row with no `model_aua` carries nothing. The date joins `carried_dates` only when a leg actually carried.

**Measured (read-only, served 2026-10-14 Global object, SMArtX partition 2026-10-15):** `sma_additive_aua` has its first value 2026-08-26 and is missing on 7 total-bearing dates (2026-08-31..09-09) where the Total excludes the sleeve; under the rule the sleeve stays absent there, the three arrays equal today's on all 497 dates, `carried_dates` stays the 9 no-total dates, the nine period ends equal the amended oracle (max diff 0.00M), the identity holds on all 488 dated rows. Dividend and Growth have no gaps today.

**Limit of the rule, stated:** Dividend and Growth cancel in the identity, so the partition test is a no-op guard for them; for the sleeve it passes only when the carried value is within 0.011 of the true value on that row, so a gap on a day the sleeve moved is refused, not carried.

**What it is not:** the publisher IAM (CN-r-2); the readback print (done, 48c40b2375); a change to `apply_global_trend_groups`, `load_smartx_sma_legs`, `build_all`, `point_class`, `model_aua` or any existing key; the Cottonwood Trend; the deploy; the pair.

**Close (carried to the CTO):** FWD-9's gap rule reads MET when, on the first scheduled fire after the deploy that mints a new date, the served Global object's `carried_dates` equals the no-total dates plus the dates on which a leg actually carried, the first-fire readback (11 of 11, R3 oracle, R4 identity, R11 CARRIED or no leg lost) passes, and every other key is equal to the prior day's rule. On today's data the fire moves no cell.

**Never-widen pair (COO half, drafted after the cell builds):** count the writers of each moved leaf (N printed; the Global `aggregate-aua-timeseries` object and its parquet partition), both branches (Total contains the gap leg -> carried; Total excludes it -> absent) and the SMArtX-absent branch, a rollback per key, the prior VersionId, the headline `opal_aggregate_aua`, `by_model` and `model_aua` byte-equal; DELTA=0 on today's data needs no hold.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round10/checks/r10_cn_r_1.py` (+ `r9_trend_groups_readback.py` amended for R11, `ref/make_reference_tree_r1.py`, `ref/ref_compute_r1.txt`, never committed to a product path). At base (box/dell1): `pure` 6 of 11 (M0, P0 controls; R2, R5, R7, R9 guards the base already meets), `seams` 2 of 4 (S0, S3 controls), `oracle` 10 of 11 (only O9, the planted Dividend gap on a real row, is red). A scratch reference tree reads 11 of 11, 4 of 4, 11 of 11 (14 tests pass; CN-p-1's `r9_cn_p_1.py oracle` reads 7 of 7 on it). Ten planted defects (`--mutant no-carry | carry-before-first | carry-gaetr | no-carried-date | reset-at-cut | mutates-input | carry-unconditional | date-when-refused | fail-open-no-model | row-level`) each turn their named arm red; `selftest` prints `CN-R-1 SELFTEST: OK`. The pure arms run `compute_trend_groups` on fixtures, so a rewrapped or differently-written body passes; the oracle arms read the served object and the SMArtX partition read-only and derive the groups independently (the identity in its algebraic form).

### CN-r-2
Notes (the drafter's, read by the issuer):
- Risk: WORLD by the `.tools/to-pipeline-gate.py` GATE (xii) floor (a `<paths>` entry under `infra/` floors at WORLD). What the worker does is LOCAL (source text, `terraform fmt`, no AWS).
- Never-widen: the served-output rule governs "moving served output". The apply moves no served byte if the proof holds, and the one publisher run is expected to write nothing; but it widens the ROLE (a new read). Whether a CTO+COO pair names the read grant and the one run is the issuer's call (stated in the TO record face, not decided here).
- Fan-out: one cell, one chain, slot ~30, base box/dell1.

### CN-r-3
**What the cell is, in one paragraph.** The CRO's findings and both CTO rulings leave one measurement owed: the 53.1 GB (10-11..10-14; 240.7 GB since 10-01) that left `opal-data-assets`, whose reader is unnamed because no instrument covers the bucket (`E4_MEASURE.md`, section 3: no request-metrics configuration, no access logging, no CloudTrail data events). The cell enables ONE `EntireBucket` request-metrics filter and a short prefix list on the dell1 seat's own allowed path, reads `BytesDownloaded` and the request counts by hour for 24 hours (a second day only if the CUR for the first day reads under 2 GB), writes the record, and deletes exactly the configurations it created. It cannot name the principal (the trail change is explicitly denied to the dell1 agent identity and the access-log target bucket admits only two security buckets); it hands the prefix, hours and share to the CTO, who routes the next step to the surface's owner.

**Not in this cell:** a trail data-event selector, server access logging, a bucket-policy edit, a CloudWatch alarm or dashboard, any standing metric (the moratorium); the E3 `opal-data-bd` pulls (ADVI_FIRMBKTS' enrichment); the harvest runner's re-read (site Z).

**Checks:** none are worker checks (no worker). The criteria are the CloudOps seat's own prints: C1 the list empty before and exactly the named ids after, C2 the 24-hour by-prefix table and the CUR cross-check, C3 the configurations removed and the ledger closed. The issuer's pre-measurement (`E4_MEASURE.md`) is the baseline the day is compared with: the CUR hourly series for the bucket.

**Close (carried to the CTO):** E4 is REALIZED as a measurement when `E4_READER_MEASURE.md` states which prefix and hours carried the egress (or that none dominated) and the bucket's configuration list is empty again; the principal is a separate, owner-routed step.


## v11 -- ROUND 11 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-16 ~14:3xZ)

**Rectangle:** `ledger/ROUND_ANALYSIS.round10.md` (the CTO, msg 6731, on ADJUDICATION_v19 @dec32ed773: round 10 closes, CN-r-1 AC4 MET on the first fire), PRD v2.23 @1fb9ac96ab (FWD-9 heads a, f, g), the CRO spec `org/tier1_exec/4.0.0_SA_CRO/deliverables/MDPF_CANON_COTTONWOOD_AUM_TREND_UPGRADE_SPEC_20261015.md` @21caa664be, Andrew's records (Muni `ANDREW_DIRECT_20261015_152xZ_*` and `_184xZ_*`; demo and the next promote `ANDREW_DIRECT_20261015_162xZ_DEMO_GLOBAL_TREND_USES_VARIANT1_NEXT_PROMOTE.md`). Items to cells: 1 to `CN-s-4`; 2 to `CN-s-5` (the CTO's 4a/4b split, which I put to it @ba8dca3ec2 and msg 6731 accepted); 3 head (g) to `CN-s-1`; 3 head (f) to `CN-s-3`, with the carried legs folded into it (ruling 1).

**Rulings the issuer took inside its own decomposition (recorded here, graded by `to-pipeline-gate.py`):**
- *1. The Cottonwood carried legs are NOT a producer cell (the draft's CN-s-2 is dissolved into CN-s-3).* The draft recommended a producer emission to match Global. Read at HEAD: `apply_global_trend_groups` (`mdpf_gold_consolidator.py` L2447-2464) resets `carried_dates` to `[]` on EVERY scope before it computes Global, so a Cottonwood emission from `build_cottonwood_mdpf_slice.py` would be overwritten, and the alternative is an edit to the function CN-p-1 and CN-r-1 own. The served Cottonwood object already lists its own absent-leg dates (`meta.channel_participation.exceptions`: 2026-07-28, 07-29, 07-30, 08-04, 08-12, 08-31, 09-01..09-04, 09-08, 09-09, each `no_measured_value`). So the carry rolls READ-SIDE, in CN-s-3's pure module, keyed on that served list and marked `carried`; the Total stays measured. The PRD allows either (issuer decision 2 of the round-11 draft); this one needs no consolidator edit, no deploy and no never-widen pair.
- *2. The CTO's CN-s-4a and CN-s-4b are cut as `CN-s-4` and `CN-s-5` (the L6 gate's cell-id grammar takes no letter suffix), one chain.* `CN-s-4` (the Variant 2 Models-band repair, one condition in `trendGrouping.ts`) is independent of any edge decision and can ship alone; `CN-s-5` (the demo session on Variant 1) shares `trendGrouping.ts` and `ModelPortfolios.tsx` with `CN-s-4`, so it queues behind it on the same worker and lands as a SEPARATE portal commit. CN-s-3 also edits `ModelPortfolios.tsx`, so it is third in the same queue.
- *3. CN-s-5 is HELD from any portal promote until its edge question is ruled.* The two single-firm reads the Variant 1 stitch needs (49 Financial, Inflection `aggregate-aua-timeseries`) are refused by the live edge gate (CN-q-1, `mdpf_gate.mjs`: a `demo` or firm-less claim reads `global` only). The cell wires the page and REPORTS the edge result; it never widens the gate (PRD v2.23 line). Widening it is a cross-firm containment decision (and a WORLD deploy), not mine: it is queued as an open call for the box CTO (`open-calls.py`, source this section). Without it a demo session on PROD would draw Variant 1 with an empty pre-2026-05-15 stitch. 4a promotes without it.
- *4. CN-s-1 moves ONE account, not the residual.* On 2026-10-14 `income_non_model_residual` holds $64,990,553.26 for 2 accounts: `Opal_Muni_Income` $63,241,218.96 and `Opal Hewitt Moderate Income` $1,749,334.30. Andrew named only Muni ("Nothing wider is ruled", record 184xZ item 3), so the registered custom model is keyed on the EXACT vendor name `Opal_Muni_Income` (key `opal_muni_income`, display "Opal Municipal Bonds") and the Hewitt account stays in Other. It is a SEPARATE key from the existing `opal_muni_sleeve` ("Opal Muni Sleeve", $554,036.75 on 2026-10-14). The registration is three files plus a test, and the crosswalk has a byte-identical Lambda copy that must change with it.
- *5. The Happyland identity check is a precondition of the never-widen pair, not a worker act.* It needs a silver read (AWS), which the worker does not have. The pair (COO half after the cell builds, CTO half) carries it as a printed match flag with no name; a mismatch stops the deploy. The deploy is a CloudOps ADHOC order naming BOTH the gold package and the daily-emitter Lambda package, no earlier than the 2026-10-17 13:30Z fire (one gold change per fire; round 10's fire of 2026-10-16 13:30Z is read, 11 of 11).
- *6. CN-s-3's build waits on nothing; its real run does.* The served Cottonwood object before CN-s-1 still has Muni in Other; after CN-s-1's fire Custom rises and Other falls by that account on every date it holds a value. The rule does not change; the oracle's month-end numbers do. CN-s-3's criterion is graded on the object as served 2026-10-15 (fixture in `round11/checks/ref/`); the issuer re-bases the oracle at the real run after CN-s-1's deploy.

**Fan-out:** 2 of 2 chains, cap 8. Chains: `CN-s-4` -> `CN-s-5` -> `CN-s-3` (shared `trendGrouping.ts` and `ModelPortfolios.tsx`: one worker's queue, slot ~31, portal base DEV); `CN-s-1` (producer, crosswalk and Lambda copy: no shared file with the portal chain, slot ~32).

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-s-4` the Variant 2 Models band is never carried forward on or after `per_model_detail_begins`: a non-internal Global session draws the band only before the boundary, and on the 9 carried dates after it no row draws the band together with the model stack, so the drawn stack never exceeds the served Total (one condition in the roll-forward loop of `buildGlobalTrendRows`; LOCAL: a portal candidate; client-facing at the landing) | FWD-9 head (a) (PRD v2.23: the Models band never carries on or after per_model_detail_begins; 0 rows with both band and stack, no row above the Total); row MDPF_CANON-D1-S29 disarms on this cell's PROD read | portal / AUA Trend, Variant 2 | `portal/src/lib/trendGrouping.ts` | -- (none; ships alone on the next portal promote on Andrew's 2026-10-15 word) | ~31 (worker) |
| `CN-s-5` the demo-tenant session draws Variant 1 (the same code as the internal session): `trendModeFor(internal, demo)` gains the second parameter and the page defines `demoTenant` and `variant1Session = internal OR demoTenant`, which replace bare `internal` in the two single-firm stitch reads and the stitch memo; everything else on the page keeps `internal` (LOCAL: a portal candidate; client-facing at the landing; HELD from promote on the edge call) | FWD-9 (Andrew-direct 2026-10-15 ~16:2xZ: the demo Global Trend uses Variant 1); row D1-S29 | portal / AUA Trend, demo wiring | `portal/src/lib/trendGrouping.ts` (`trendModeFor` only), `portal/src/pages/ModelPortfolios.tsx` | `CN-s-4` (same chain, shared file); an external edge: the call on the demo session's read of two single-firm leaves, before any promote | ~31 (worker) |
| `CN-s-3` the Cottonwood AUM Trend upgrade (CRO spec): a new pure module `cottonwoodTrend.ts` builds one row per total-bearing served date from the first one (2026-06-09) to the as-of: Total = `partner_custody_total`, the five primary lines = the models' `model_value`, Custom = `model_aua` minus the five, Other AUM = `partner_custody_total` minus `model_aua` on EVERY row with a total (today drawn only from 2026-07-20), the 12 absent-model-leg dates listed in `meta.channel_participation.exceptions` take the last measured model leg and are marked carried with their measured Total, the sanctioned backfill window keeps its interpolated marking; the page's Cottonwood Trend draws from it, no 2026-04-22 extension (LOCAL: a portal candidate; client-facing at the landing) | FWD-9 head (f) (PRD v2.23; CRO spec @21caa664be; Andrew-direct 2026-10-14 ~20:1xZ: upgrade this, find/fill/roll-forward the asset taxonomy groups) | portal / Cottonwood AUM Trend | `portal/src/lib/cottonwoodTrend.ts` (new, pure), `portal/src/pages/ModelPortfolios.tsx` (the Cottonwood Trend wiring) | `CN-s-5` (same chain, shared page file); the real run after CN-s-1's deploy re-bases the oracle (ruling 6), the build does not wait | ~31 (worker) |
| `CN-s-1` Muni becomes a registered custom model (head g): the vendor account named exactly `Opal_Muni_Income` routes to the new key `opal_muni_income`, display "Opal Municipal Bonds", leaving `income_non_model_residual` and entering `by_model` / `model_aua` on Cottonwood and, through `GLOBAL_MODEL_KEYS`, the Custom sum of Global; `Opal Hewitt Moderate Income` stays in Other and `opal_muni_sleeve` is untouched; registered in the producer (`CUSTOM_KEY`, `CUSTOM_DISPLAY_NAME`), the crosswalk and its byte-identical Lambda copy (`ModelEntry`, `COTTONWOOD_CUSTOM_MODEL_KEYS`, `GLOBAL_ACCOUNT_DIST_DISPLAY`; `GLOBAL_MODEL_KEYS` reads that tuple, so the dim file is read-only), and the existing custom-model test (WORLD: a gold-package deploy AND a daily-emitter Lambda package; moves the served history of two objects from the account's first date) | FWD-9 head (g) (PRD v2.23; Andrew-direct 2026-10-15 ~15:2xZ and ~18:4xZ: Muni is in Custom Models, only Muni) | producer / Cottonwood and Global custom-model routing | `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py`, `data/assets/scripts/gold/tests/test_cottonwood_custom_and_sma.py`, `data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py`, `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/mdpf_revamp_model_crosswalk.py` | -- (a build edge to no other cell); a deploy-order edge: one change per fire, no earlier than the 2026-10-17 13:30Z fire; the never-widen pair with the Happyland identity flag (ruling 5) | ~32 (worker); the deploy: `0.7.0_AE_CloudOps~DELL1` by ADHOC order |

**Not cut this round, and what is missing (the CTO's "otherwise state what is missing"):** (a) *CN-s-2, the producer emission of Cottonwood carried legs* -- dissolved by ruling 1; if the CTO prefers a producer emission, the input missing is a ruling on how `apply_global_trend_groups` may preserve a scope's own `carried_dates` (it resets every scope), which edits CN-p-1's and CN-r-1's function. (b) *The edge decision for CN-s-5* -- queued, not mine (ruling 3). (c) *The optional extension in the CRO spec* ("Andrew's call; not in the base") -- not cut. Nothing for head (f) or (g) waits on a spec input: both are on file.

**Checks:** `deliverables/2.0.0_SA_COO~D1/round11/checks/` (`r11_cn_s_4.py` modes `pure`, `real`, `wiring`; `r11_cn_s_3.py` mode `pure`; `r11_cn_s_1.py` modes `pure`, `seams`; `ref/` holds the two served-object fixtures, 2026-10-15; every script has a `selftest` with a scratch reference and planted mutants). Base results are in each order's preflight.


## v11 AMENDMENT 1 -- the demo tenant's Trend: (C) final, (B) struck, `CN-s-5` superseded (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-16 ~15:3xZ)

**Rests on:** the laptop CTO's ruling `XA-20261016T143752Z-6cad` (ruled 14:43:09Z; box CTO msg 6758: (C) now, (B) next, (A) refused), the issuer's read and measurement `deliverables/2.0.0_SA_COO~D1/round11/CN_S_5_RULING_READ_20261016.md` @ac7b8e71ef, and the CTO's final ruling on that read (box CTO msg 6762, 14:54Z: "(C) is final ... (B) struck as empty under the ruling's own condition; CN-s-4 ships alone").

- *`CN-s-5` is SUPERSEDED.* Its build (portal `e206e06e`, wiring 10 of 10) is not cherry-picked into any landing candidate. As built it would give the demo `mode = variant1` with the stitch reads refused at the edge, which draws no Models band before 2026-05-15; the demo's own form is Variant 2, which `CN-s-4` repairs.
- *Cell (B) is not cut.* The one-firm suppression condition empties it: all 1,865 pre-2026-05-15 per-model points (383 dates, five primary models) rest on exactly one firm (49 Financial), MEASURED on the served per-firm objects.
- *`CN-s-4` ships alone* on the next portal promote (client-facing: Andrew's word). The demo's open call `dell1-20261016T143036Z-c7de` closes on the ruling.
- **Round record, as the CTO asked:** before 2026-05-15 the demo tenant's Global Trend differs from the internal global view, because the per-model lines there are single-firm values (49 Financial's own series) and a non-internal session may not read them (FWD-3). The demo draws Variant 2's one Models band for that span.
- *Chain 1 now reads:* `CN-s-4` (done, merged), `CN-s-5` (superseded), `CN-s-3` (done, merged). `CN-s-1` is merged. Remaining for the round: the typecheck and the one real run on 5174 of `CN-s-4` and `CN-s-3` (judgment criteria for the CVO), the CN-s-1 never-widen pair and the CloudOps deploy (no earlier than the 2026-10-17 13:30Z fire).


## v11 AMENDMENT 2 -- `CN-s-6`, Global's axis drops the enumerated date 2026-10-16 (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-17 ~14:5xZ)

**Rests on:** the scheduled fire of 2026-10-17 13:30Z (manifest `20261017T133145Z`, read `deliverables/2.0.0_SA_COO~D1/round11/real_run/FIRE_READ_20261017.md` @882da2f5f8; row `MDPF_CANON-D1-S33`), PRD v2.29 @11ea6ef573, and the CTO's rulings: msg 7594 (exempt 2026-10-16, built on the deployed pin, the 10-18 fire's one gold change) and msg 7600 (ruling (B): drop the date from Global's axis as an ENUMERATED set, never a general filter, never also in the exempt list; the pair names Cottonwood's own axis as untouched; the D4 no-write dry run must show Global `as_of` = the frontier, a non-None headline and no None `model_value` inside the covered range, else the change does not ride the fire).

- *Ruling taken inside this decomposition (issuer):* the repair is a NEW cell, `CN-s-6`, not a reopening of `CN-s-1`: it changes a different function (`build_global_artifact`'s axis, `dim_mdpf_aggregate_aua_timeseries.py` L2368) and a different outcome (the fire emits Global at all), it builds on the deployed pin `d2f734fbac` and not on the issuance base, and it rides the next fire alone. CN-s-1 stays `complete`; its WORLD grade is read on the first scheduled fire after CN-s-6 deploys (CTO msg 7600: "CN-s-1's Global grade reads that fire").
- *Measured at the pin, read-only:* the Global refusal reproduces offline over the fire's three staged legs ("5 across 1 date(s)"); with the one-set change Global emits 498 dates, `as_of_last` 2026-10-15; with the date in the exempt list instead, gate (v) passes and the composition gate then refuses ("1 band/total violation(s) across 499 dates"), which is why (B) and not (A).

**Gate keying (Rule 27, `to-pipeline-gate.py` GATE (x)):** round 11 already has its issuance at HEAD, and a new order file in it is refused; the order therefore carries the line-anchored `<workstream>GLOBAXIS</workstream>` beside `<round>11</round>`, which keys it as (GLOBAXIS, 11), a scope with its own write surface (the Global axis line in `dim_mdpf_aggregate_aua_timeseries.py`, which no other round-11 order owns). It is still round 11's amendment 2: the round closes only when this workstream is terminal too.

**Fan-out:** 1 of 1 chain, cap 8. Slot ~33, base the deployed pin `d2f734fbac`.

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-s-6` Global's axis drops the enumerated date 2026-10-16: `GLOBAL_AXIS_DROP_DATES = frozenset({"2026-10-16"})` subtracted from the union of the three legs' dates in `build_global_artifact`, so Global's series, `as_of_last` and coherence gates never see it; the date is not in the exempt list; Cottonwood's axis keeps it (WORLD: a gold-package deploy; the 2026-10-18 13:30Z fire's one gold change) | FWD-9 head (g) as served (CN-s-1's outcome at Global; PRD v2.29); row MDPF_CANON-D1-S33 | producer / Global axis | `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`, `data/mdpf/scripts/gold/tests/test_global_fold_flag2.py` | -- (no build edge); a deploy edge: one gold change per fire, no earlier than a never-widen pair signed by both halves, finished before the 2026-10-18 13:30Z fire | ~33 (worker) |

**Checks:** `deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_6.py` (mode `real`, arms S0 to S4; legs read from `C:/dev/_deploy_artifacts/canon_s6/`, outside the repo). Base 2 of 5, reference 5 of 5, three planted mutants each red on their named arms (order preflight).


## v11 AMENDMENT 3 -- `CN-s-7`, Global's axis keeps 2026-10-16: the drop set is emptied (issuer 2.0.0_SA_COO~D1 on DELL1, 2026-10-19 ~14:5xZ)

**Rests on:** the scheduled fire of 2026-10-19 13:30Z (manifest `20261019T133153Z`, read `deliverables/2.0.0_SA_COO~D1/round11/real_run/FIRE_READ_20261019.md` @4d30e30e8a; row `MDPF_CANON-D1-S36`), and the CTO's ruling `ledger/CTO_RULING_S36_EMPTY_GLOBAL_AXIS_DROP_20261019.md` @176378e74d: msg 6986's premise ("no catch-up fills 2026-10-16") failed, because the feeder wrote 2026-10-16 for 49financial and inflection (all three staged legs end 2026-10-16 with values); the drop of CN-s-6 holds Global at as_of 2026-10-15; RULED yes, empty `GLOBAL_AXIS_DROP_DATES` under a new never-widen pair, landed before the 2026-10-20 13:30Z fire. The pair's gate is the D4 bodies of a build without the drop over the live legs; both branches are read from the code's own rule; Cottonwood's 2026-10-16 write-once conflicts are named as a fact, not a gate; the computed-drop idea is a round-12 row, not a cell.

- *Ruling taken inside this decomposition (issuer):* a NEW cell, `CN-s-7`, under workstream `GLOBAXIS2` (gate (x) keys by (workstream, round): `(GLOBAXIS, 11)` already holds `CN-s-6`); one constant and one test change, built on the deployed pin `128fce3524`.
- *Measured offline at HEAD, read-only:* over the 2026-10-19 legs the build as deployed EMITS 498 dates, as_of_last 2026-10-15; with the set emptied it EMITS 499 dates, as_of_last 2026-10-16, headline present, no refusal; over the 2026-10-17 legs (2026-10-16 only at Cottonwood) the emptied-set build is REFUSED by gate (v), the code's own protection for the branch where a leg loses the date.

**Fan-out:** 1 of 1 chain, cap 8. Slot ~34, base the deployed pin `128fce3524`.

| cell | serves (cell_refs) | candidate | owned files | depends on | actor |
|---|---|---|---|---|---|
| `CN-s-7` Global's axis keeps 2026-10-16: `GLOBAL_AXIS_DROP_DATES` becomes an empty frozenset (the mechanism and the constant stay; the date is no longer dropped), so Global's series, its `as_of_last` and its gates see 2026-10-16 again; the CN-s-6 test is replaced by one that asserts the date stays on the axis when all three legs carry it (WORLD: a gold-package deploy; the 2026-10-20 13:30Z fire's one gold change) | FWD-9 head (g) as served (CN-s-1's outcome at Global; PRD v2.29); row MDPF_CANON-D1-S36 | producer / Global axis | `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`, `data/mdpf/scripts/gold/tests/test_global_fold_flag2.py` | `CN-s-6` (done, live); a deploy edge: a never-widen pair signed by both halves and D4 on the no-drop build, finished before the 2026-10-20 13:30Z fire | ~34 (worker) |

**Checks:** `deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_7.py` (mode `real`, arms S0 to S4; legs `C:/dev/_deploy_artifacts/canon_s6/fire_20261019/` and, for the control arm, `C:/dev/_deploy_artifacts/canon_s6/`, outside the repo). Base 2 of 5, reference 5 of 5, three planted mutants each red on their named arms (wrong date in the set: S0; empty set but the date added to the exempt list: S0 and S4; a computed drop: S4).
