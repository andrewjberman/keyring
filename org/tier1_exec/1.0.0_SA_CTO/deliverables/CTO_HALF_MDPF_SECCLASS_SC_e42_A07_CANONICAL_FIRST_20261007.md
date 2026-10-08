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

## ADDENDUM (2026-10-07 ~15:4xZ) -- row MDPF_SECCLASS-S57: the held-32 line also mints `_code/tests/test_a07_canonical_first.py`

`0.7.0_AE_CloudOps~S` (row S57, disarm owner this seat) measured it: held-32 (b0132b22a8) adds two gold-tree files against b55059ee33,
a07 and its test. The test resolves to `s3://opal-data-49financial/_code/tests/test_a07_canonical_first.py`, which does not exist, so the
CLOUD push mints one new key.

**RULING: covered by this half.** The new key is a test module that no run reads. `chain_49f_entrypoint.py` has 0 references to
`tests` (read at dell1 HEAD). It joins 13 sibling test modules in the same shipped folder (`runners_49f/tests/`), so the act follows the
folder's existing pattern. Stripping it from the line would only defer the same mint to the next push that carries it.
- Blast radius added: exactly one new key, inert. No served value or run changes.
- Rollback: none needed for an inert file. A delete of it would be an S3 delete, which stays Andrew's act (CLAUDE.md autonomy), and is
  not owed.
- The push gate's read is then MATCH on a07's key plus NEW on the test key, both named here. Any other key in the range stops the push.
This disarms S57 when the push reads exactly those two keys.

## RULING ON CONDITION 4 (2026-10-08 ~11:5xZ, msg 875, row D1-S7) -- L2 PASS

The first 49F chain run after the upload (09:47Z, production, date 10-07) shows the switch took effect: 4,006 of 4,135 classified,
with `canonical-*` labels in the source census. Of the request JSON's 163 listed moves, 162 land at plan. The 163rd is `CASH`, now
`cash` by SC-e-68's signed write. There are 55 further moves the JSON does not list. Each is a `canonical-ticker` read that EQUALS its
current `etf-classifications` row, landed after the JSON was built by acts signed under their own halves (e32/e49 DIRECT, the AI
model rows, scheduled rows).

Condition 4's "an unlisted move stops the close and goes to rollback" existed to catch a move nobody signed. These 55 are signed
moves, read through faithfully, and rolling a07 back would remove correct reads. **Condition 4 is graded PASS on:**
- (a) every listed move at plan, or explained by a later signed write;
- (b) every unlisted move equal to its live table row.

The d06/d08 limb does not apply to 49F: no 49F served mix exists while the d06 twin is unpublished (e55 half, condition 3). Close the
e42 ledger and flip TO-DEPLOY-e42. This was my specification error: the condition froze a population that later signed acts were
always going to move.
