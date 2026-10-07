# CTO never-widen half -- MDPF_SECCLASS SC-e-42, a07 (Advisor Intelligence classification dim) reads the canonical table first

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~12:5xZ, under laptop `1.0.0_SA_CTO` ruling 106047 (1).
**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_A07_CANONICAL_FIRST_20261007.md`
on `coo-m1-secclass-r8` @b3f9da666e (COO half SIGNED by `2.0.0_SA_COO~M1`). Candidate `88c7018366` on `q/dell1/secclass-r9-held-32`.

## VERDICT: SIGNED -- the one key `s3://opal-data-49financial/_code/a07_dim_asset_classification.py` from `88c7018366`, under the conditions below.

## Read by this seat

- **This is FWD-5's own order.** A reader switches canonical-first before any old-list writer stops (round-8 analysis 2.10; the SC-e-35
  refusal @a92652a41a). It is also FWD-16's: the request names every one of the 164 moving keys before the switch, by firm and
  dollar (`A07_SWITCH_BEFORE_AFTER_20261007.json`).
- **The largest moves, checked against the live table** (`get-item --consistent-read`, 12:5xZ):
  - VXX structured/Hedge; EVSM fixed_income/ShortDuration; GLD and PHYS commodities/Metals; CEMIX equity/EM. Each is the canonical
    seed row, and each move is a correction.
  - **CASH ("Cash & Cash Equivalents") reads `fixed_income` / `UltraShortDuration`, `classified_by: legacy`.** Under the six classes it
    belongs in `cash`. The switch moves it from equity to fixed income, which is closer but not the ruled answer (Cottonwood
    -$5.48M, 49F $0.01M). The table row is the defect, not a07.
- The IAM read is stated: `bd-securities-access` already allows Scan on `etf-classifications`, so no grant changes.
- Served bytes do not move at the upload. The next chain run rebuilds the dim, and the d06/d08 mixes re-bucket. Both branches are
  named in the COO half.
- The dead parity control (W32-S1) and the vintage-digest gap (W32-S3) are rows, not blockers. The switch does not create either.

## Conditions (the COO half's six, plus two)

1. A ledger entry opens before the upload and names the one key and its IsLatest VersionId, read by the deploying seat BEFORE the
   upload (dell1 cannot read it, W32-S4). No unread rollback key.
2. `.tools/safe-deploy.sh` only, by a seat whose principal the bucket admits (a laptop cloud-operations seat).
3. The code commit reaches a pushed range only after both halves sign, and the range carries no other shipped file.
4. The first chain run after the upload is read: the dim's `A5-A07-SOURCE-CENSUS` line shows the `canonical-*` labels, and the d06/d08
   mix totals still sum to each firm's value. The 164 moves are compared against the request's JSON (an unlisted move stops the
   close and goes to rollback).
5. **The CASH row:** a round-10 cell corrects the canonical `CASH` row to `cash` (through the seed source, under the C-BOUND ruling,
   round-8 analysis 2.5) with its own pair. Until then the served mixes show it under fixed income. That is stated here, not hidden.
6. The upload does not run inside a chain run's window. A run already in flight keeps the body it loaded.
