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
