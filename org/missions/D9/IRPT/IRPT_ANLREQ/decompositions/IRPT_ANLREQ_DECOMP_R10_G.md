# IRPT_ANLREQ round 10, workstream ~G (ENGINE) -- decomposition: the two existing-code cells the reads fully specify (the door's Keep, and the ticket-confirmation switch)

Issuer `2.0.0_SA_COO~G2`, 2026-10-15.

**Input:** the reads `AR-g-53` (C-SWITCH design, merged `286f7c048d`) and `AR-g-55` (the door's UNRESOLVED path, merged `e9c9bdf1f0`); round 9 (`IRPT_ANLREQ_DECOMP_R9_G.md`: `AR-g-63` merged `7ecc5acf18`,
`AR-g-70` merged `83980ff010`, `AR-g-69` in flight); CTO msg 8377 and PRD v0.15. Both cells below are found FREE: no unmet dependency (the empty-tick and WIDTH sequences), disjoint write sets.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-67` | C-SWITCH placement A in SOURCE: `ycharts/generate/ticket_confirmation.py` (NEW, one typed `GetItem` and a four-clause rule: the item exists, `ticket_type` is `analysis_request`, `source` starts `dashboard_form:`, the filer email equals the accepted principal), `accept(..., ticket_confirmed=False)` stamping a server-owned `ticket_confirmed` only when true, `SubmissionService(confirm_ticket=None)` calling it for a NEW acceptance and failing open to unstamped, the wiring from `IRPT_TICKETS_TABLE` (none typed), and `producer_for` also admitting `ticket_confirmed is True`; 12 direct cases and 8 named tests; NO Terraform, NO grant | `ticket_confirmation.py`, `acceptance.py`, `submission_service.py`, `prospect_submission.py`, `resident_worker.py`, `reports/generate_installed.py`, two new test files, the worker's folder | WORLD (the floor of an infrastructure path; source and tests only, nothing deployed or granted) |
| `AR-g-68` | the DOOR's Keep in SOURCE: `template_corrections` accepts the EXACT equal pair for `TICKER_NOT_FOUND` only; `freeze_template_portfolio` files the kept NOT_FOUND row as `UNRESOLVED` (no receipt, out of the vendor holdings block, no new finding code); `prepare_normalized_upload` refuses an UNRESOLVED row (and its bare-subscript TypeError becomes `RecipeRefused`, disarming armed row `W174-S3`); `read_holdings(..., allow_unresolved=False)` refuses by default and carries the marker when asked; 6 direct cases and 8 named tests | `intake/portfolio.py`, `ycharts/generate/normalized_input.py`, `ycharts/research/runner.py`, three new test files, the worker's folder | WORLD (same floor; source and tests only) |

## Edges and chains

- TWO independent chains with disjoint write sets (the first writes `resident_worker.py`, `acceptance.py`, `submission_service.py` and friends; the second `portfolio.py`, `normalized_input.py`, `runner.py`). Neither consumes the other's output.
- `AR-g-67` leaves the real switch off until a CloudOps cell grants the Lambda role one `GetItem` on the ticket table (after the role's identity is read: the design record's `generate.tf` line 120 reads as the generation job's statement list) and the environment names the table.
  Until then a ticket-filed staff request still takes the YCharts path, exactly as today. That grant is a NEW widening: a pair with the CTO's half.
- `AR-g-68` makes the equal pair acceptable to the server; `2.0.0_SA_COO~Y2` then posts it from the portal's Keep. The Opal path carries the marker only when the compose cell (a later round) calls `read_holdings(..., allow_unresolved=True)`.
- Still to cut (each with its own text and checks): the price adapters (on `AR-g-69`), the resident variant binding (`resident_installed.py`, `resident_worker.py` AFTER `AR-g-67`: same files), the map statistic fix, the compose into `opal_producer`,
  the IAM leg cell and the ONE resident release r32 (the only writer of `build_resident_package.py`).

## Four-postulate record

(i) Domain: C-SWITCH hop 8 and the door's Keep (FWD-1, FWD-7) only. (ii) One cell per file set. (iii) One intent per cell. (iv) What this cut does NOT move: any deployed byte, any grant, the Terraform, the portal, the YCharts or Yahoo accounts, the producer allow list (the synthetic address stays until after the FWD-1 run).

fanout: 2 of 2 chains for workers per cut (AR-g-67 worker slot 179, AR-g-68 worker slot 178), cap 8, reason: two source cells over disjoint files; the other open chains are the read at slot 176 and `2.0.0_SA_COO~Y2`'s workstreams.
