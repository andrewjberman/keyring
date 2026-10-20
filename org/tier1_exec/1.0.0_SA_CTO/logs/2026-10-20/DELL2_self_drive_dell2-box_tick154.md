# /self-drive dell2-box -- ticks 153-154 (2026-10-20 ~03:57Z-04:57Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** ticks 153 and 154, since the tick 152 log (@baf8a812f2). state: ARMED.

## Delta

- **TCKT_VNEXT FWD-11** (Meeting Request) is graded REALIZED on DEV and PROD by `3.0.0_SA_CVO~DELL2` (msg 11204,
  ADJUDICATION_v14 @76c1694cb7).
  - R20PROD2 and R20LM7 are MET.
  - Round 20 reads 9 of 9 graded, MAY-CLOSE (TO-R20-PROMOTE-FIX not yet complete).
  - Trade PROD3 is not graded.
- **Run 5C** (IB2 msg 11208, `A_E2E5C.txt` @c48e4eb972):
  - U passed without a Keep; T and S were ok (REQ-948597d1).
  - It STOPPED at P1: the composition step now passes, but the resident retained the request three times with `RecipeRefused`.
  - Leftovers: rows S221 and S222.
- **The cause** (`~Y2` msg 11205, measured): a Ticket Center staff request takes the VENDOR producer, which refuses kept-by-history rows.
  - `producer_for()` picks OPAL only for the 2-name allow list or a `ticket_confirmed` record.
  - `confirm_ticket` needs ticket source `dashboard_form:` (set only by `/tickets/submit`); the Ticket Center creates tickets by `/tickets`
    with source `portal`.
  - So no staff filing from the Ticket Center is ever stamped for the Opal producer.

## Rulings

| item | ruling |
|---|---|
| Run 5D (Andrew's fresh-report verify) | APPROVED: on r34l, the allow-listed synthetic principal `fwd1-staff-r41b@opal.invalid`, the field omitted, the same pair, no new identity. PASS is R2 sections. Before 05:45Z, or 07:00Z-11:30Z. Not started at 04:56Z. |
| The routing defect | A MUST cell in the v0.24 round: `confirm_ticket` also stamps an `analysis_request` created through `/tickets` when `created_by` equals the request principal, so every Ticket Center filing takes the Opal producer. Grounding: PRD FWD-1 item (3), "the Opal-generated report (the Opal producer, not YCharts)". It ships with or before r34m v2. |

## Acts only Andrew can do

- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git, ... S3 deletes"):
  - `C:\dev\wk-irpt-dashbd-503`;
  - row 544d;
  - row 65a1;
  - row a392.
- **S3 deletes:**
  - row 6e7c;
  - row 128f;
  - the leftovers of runs 5, 5B and 5C (rows S218-S222).

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED
