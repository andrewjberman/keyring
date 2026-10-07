# MDPF_SECHIST decomposition -- ROUND 1, the THREAD (issuer 2.0.0_SA_COO~H1, dell1; cut 2026-10-07 ~07:5xZ)

**Status: ISSUED** in one issuance. Seat: laptop MSTR award (bus d8db68fe; CTO msg 106023), seated by `0.0.0_AB_MSTR~DELL1`;
Andrew-direct ~07:15Z relayed in msg 3: "the COOs should be running /canonical-drive on their projects".

**Cut on:** PRD v0.1 @b4b995dc14 (L4-R ADMITTED: ratified-text half SIGNED by `3.0.0_SA_CVO` @6ed79bd1c9; brief half admitted because
the CRO wrote the brief). Brief `docs/briefs/securities-database-ingestion-maintenance-brief-20261006.md` @901edd46a2.

## The thread (PRD section 2, FWD-1) and its hops, measured at the base 2026-10-07

| hop | what | adapter today | cell |
|---|---|---|---|
| H1 detect | a new Opal ETF holding enters the pull's universe | `etf_daily_pull.py` derives the universe from the newest `silver/holdings` partition every run; MDPF_SECCLASS FWD-10 writes the table row (C-TABLE, not this project's) | none: works |
| H2 plan + pull | the pull asks Bloomberg for that security's one-year history | ONE window for every security (`etf_daily_pull.py:240-257`: prior manifest end + 1 to as-of); no per-security depth | `SH-t-1` (build) |
| H3 land | the series lands where gold reads it | `put(hist, "history_topup")` -> `s3://opal-data-etfs/bbg/<asof>/history_topup.parquet` | inside `SH-t-1`: rows ride the same artifact, so no new address (C-NAMES) |
| H4 gold | Positioning gold computes the windows | `load_history` (`etf_positioning_gold.py:731`) reads every `history_topup` partition in a 400-day lookback and does NOT filter a partition's rows by the partition date; `compute_returns` (`:855`) needs the series to START at or before the window start | `SH-t-2` (pin the read; repair only if the test shows a defect) |
| H5 page | the analyst reads it on the Positioning page | the publisher and page read gold; unchanged | none: the COO's one real run at close |

**Live negative case (read 2026-10-07):** CSCO and BX are in the universe since about 2026-09-18 with no backfill; `bbg-testpull/tickers/CSCO/` holds
nothing. Newest daily partition `bbg/2026-10-05/`.

## Rule 24

Domain: the FWD-1 thread, H1-H5. H1 and H5 work today (no cell). H2+H3 are one write set (the pull file and its test), one intent: depth per
security. H4 is one intent: the gold read of those rows. Two cells, no remainder. Same grain: each cell is one adapter. State coherence: neither cell moves
the interior-gap behaviour (enrichment 1), non-ticker keys (enrichment 3) or the budget ledger (enrichment 4).

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `SH-t-1` | Per-security history depth in the site Z ETF daily pull: a plan that gives every universe security whose stored history starts later than one year before the as-of a window back to `asof - 372` days (cap 50 securities per run), requested after the production pull, isolated so its failure never changes the leg's exit code, its rows appended into the same `history_topup` artifact, the windows recorded in the manifest; a read-only `plan_only()` entry | FWD-1 | NOT-EVALUATED | dell1 (code); runs at site Z after the drain | LOCAL | A, `0.9.0_WK_MDPF_SECHIST~1` |
| `SH-t-2` | Gold pin: a test that a `history_topup` partition carrying a year of one new security's rows yields all eight windows, with a one-row control that yields 1D only; repair `load_history`/`compute_returns` only if the test fails on the real code | FWD-1 | NOT-EVALUATED | dell1 | LOCAL | B, `0.9.0_WK_MDPF_SECHIST~2` |

## Write sets (disjoint)

- **SH-t-1:** `integrations/bloomberg/pipeline/etf_daily_pull.py`, `integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py`, the surprise channel.
- **SH-t-2:** `data/etfs/scripts/gold/test_etf_positioning_backfill_rows.py`; `data/etfs/scripts/gold/etf_positioning_gold.py` only on a measured defect; the surprise channel.
- Checks (issuer's, dry-run at the base, all FAIL as expected): `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R1_CHECKS/`.

## Edges and fan-out

No data edge: `SH-t-2` builds its own partition fixture, so it does not consume `SH-t-1`'s output. `fanout: 2 of 2 chains, cap 8`.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- thread round; no schedule changes (the leg runs in the existing site Z daily task).
- `comp-iam`: DECLARED-NOT-APPLICABLE -- the thread touches no IAM: the pull writes the same keys under the same site Z credentials.
- `comp-adversary`: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches its surface.

## The issuer's acts at the drain (not cells)

1. **SITE Z RUNS THE WORKING TREE** (`integrations/bloomberg/READ_HERE.md:104`): the merge of `SH-t-1` into CLOUD becomes a deploy the moment site Z's
   tree takes it. That act is WORLD: a change-management ledger entry, and a never-widen half naming the blast radius (`history_topup` gains rows for at most
   50 securities a run; Positioning windows that read null become populated; rollback = revert the commit at site Z), signed CTO + COO before the site Z
   tree takes it. Routed to site Z's owner through `0.0.0_AB_MSTR~DELL1`.
2. **The one real run of FWD-1:** the morning after the first site Z run, read CSCO, BX and a security an Opal ETF newly bought, on the Positioning page,
   classification and the eight windows (1D, WTD, MTD, 1M, QTD, 1Q, YTD, 1Y).
