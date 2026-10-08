# MDPF_SECHIST decomposition -- ROUND 2, enrichment (issuer 2.0.0_SA_COO~H1, dell1; cut 2026-10-08 ~13:4xZ)

**Status: ISSUED** in one issuance. **Cut on:** the CTO's round-1 analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECHIST_ROUND_1_20261008.md` @0141533760 (msg 904), PRD v0.2. The
analysis's section 3 is this round's rectangle: three items, one cell each, item 3 held.

## The rectangle

| item | FWD | cell | status | placement | risk | chain / assignee |
|---|---|---|---|---|---|---|
| 1 | FWD-1 | `SH-t-3` acceptance read: on the first unassisted scheduled pull, the next-morning Positioning page shows a security that pull newly backfilled with class, sector, clean name and 8 of 8 windows | ISSUED, event-gated on the first `run_class: scheduled` manifest carrying the round-1 code (earliest as-of 2026-10-08, pull 2026-10-09 07:00 ET) | dell1, read only | SERVED | A, `0.9.0_WK_MDPF_SECHIST~4` (read only; spawned after the event) |
| 2 | FWD-7 | `SH-t-4` the run record prints the backfill draw beside the bbg_budget remainder: `history_backfill_budget` gains `spent_after` and `remainder`, and the log prints estimate (ticker-weekdays), drawn (returned records) and remainder | ISSUED | dell1 (code); runs at site Z after the drain and a never-widen pair | LOCAL (code); its site Z take is WORLD | B, `0.9.0_WK_MDPF_SECHIST~3` |
| 3 | FWD-2 | `SH-t-5` card-A backfill (1,319 securities) under the shared ledger, paced, with a per-day draw line | HELD, not cut: site Z ruling 31292 holds the draw until AMGT_CORPUS and ETFS_RIVALS record in bbg_budget | site Z | WORLD | cut on site Z's release |

Not in round 2 (analysis section 3): FWD-4, 5, 6, 8, 9. FWD-1's clean-name hop is MDPF_SECCLASS's cell (analysis 2.2, to
`2.0.0_SA_COO~M1`); `SH-t-3` grades whatever name that cell has landed on the acceptance morning.

## Rule 24

Domain: the analysis's enrichment list, three items. Subtraction: item 1 -> `SH-t-3`; item 2 -> `SH-t-4`; item 3 -> held with its
un-park condition. Remainder none. Same grain: each cell is one outcome on one surface (the served page; the run record). Intent: `SH-t-3`
reads and never writes; `SH-t-4` adds two fields and one log line. State coherence: `SH-t-4` does not move the refusal rule, the ledger
format, the production pull or the backfill plan.

## Write sets (disjoint)

- **SH-t-3:** none (read only). Check: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R2_CHECKS/sh_fwd1_acceptance.py`.
- **SH-t-4:** `integrations/bloomberg/pipeline/etf_daily_pull.py`, `integrations/bloomberg/pipeline/test_etf_daily_pull_history_plan.py`, the
  surprise channel. Check: `R2_CHECKS/sh_t4_budget_tests.py`.
- Both checks dry-run at the base 2026-10-08 ~13:4xZ, both FAIL as expected: `FWD1-ACCEPT-BAD newest-manifest-not-scheduled
  as_of=2026-10-07 run_class=adhoc`; `BUDGET-TESTS-BAD not-passed=test_run_record_prints_draw_and_remainder`.

## Edges and fan-out

No data edge between `SH-t-3` and `SH-t-4`. One ORDER edge at the deploy: site Z takes `SH-t-4`'s bytes only AFTER the `SH-t-3`
acceptance pull has run, because the acceptance grades the round-1 bytes unassisted; a new deploy in front of it would change the vehicle
under test. `fanout: 2 of 2 chains, cap 8`.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- no schedule change; both cells ride the existing site Z daily task.
- `comp-iam`: DECLARED-NOT-APPLICABLE -- no IAM change; the pull writes the same keys under the same site Z credentials; the read uses the
  dell1 read grants round 1 used.
- `comp-adversary`: `SH-t-4` touches the budget surface. Lens, applied at the cut: a field that reads a remainder from a ledger the pull
  cannot fully see (other legs write 0 lines today, ruling 31292) is labelled the ledger's remainder, never the day's Bloomberg
  remainder; the cell's worker face says so.

## The issuer's acts at the drain (not cells)

1. `SH-t-4` merged -> never-widen pair (COO half + `1.0.0_SA_CTO~Z` half; blast radius: two manifest fields and one log line, no change to
   rows drawn or written; rollback = revert at site Z), then site Z's take after the acceptance pull.
2. The one real run of FWD-7: the first site Z manifest carrying `remainder`, read against the ledger.
