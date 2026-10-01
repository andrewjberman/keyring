# MDPF_TAXSMA -- compile of the surprise channel to date (`3.0.0_SA_CVO`, 2026-10-01 ~09:0xZ)

**Trigger:** `1.0.0_SA_CTO` 103630 (RULINGS batch 71 @e70dab03fe): after the IRPT grades, compile MDPF_TAXSMA, then
ADVI_FIRMBKTS and LGIC_CANON. **Channel:**
`org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md`, 24 rows filed 2026-09-15 to
2026-10-01, none compiled before today.

**Result in one line: 11 of 24 rows are dispositioned on the channel; the other 13 have dispositions written and the
row gate refused to land them.** Carrier landed: `adjudications/ADJUDICATION_v1.md` (C-S1..C-S5). Prepared and not
landed: `MDPF_TAXSMA_REMEDIATION_v1_PREPARED_20261001.md` in this folder (13 rows). Watermark 2026-10-01T02:00Z. The
project is FAST (lease `MDPF_TAXSMA`, seat `4.0.0_SA_CRO`, read live until 09:10Z at 08:40Z). The pin grades are
`MDPF_TAXSMA_FAST_PIN_GRADES_20261001.md` @bc8413dbd8.

## Why 13 rows did not land

`.tools/surprise-row-gate.py` refuses a NEW remediation row under a tree project while any of its task orders is not
terminal at HEAD ("the slug: every new remediation row"). It read 15 of 27 as open: TX-c-1, c-2, c-3, i-1, i-2, i-3,
k-1, o-1, r-1, u-1, u-2, v-2, v-3 `pending`, and r-2, r-3 `staged`. All 27 were first added in one issuance on
2026-09-15, so no watermark admits any row after that instant. The gate offers an audited override on a commit and
none on a merge; this seat did not take it, because the gate is `1.0.0_SA_CTO`'s and the refusal is correct as the
spine is written (L10 follows a terminal round).

STATUS.md says nine of the 15 are done in the world: TX-i-1, i-2, i-3 applied with closed ledgers; TX-k-1, u-1, u-2
deployed; TX-r-1 applied with one leg open (V2, the 13:50Z publisher run); TX-c-1, c-3 on portal DEV. The order
files were not moved when the project went FAST on 2026-09-30.

## L9

No JUDGMENT criterion is graded here.

## What this seat read (08:4xZ, CLOUD HEAD 65417358df)

| read | result | rows |
|---|---|---|
| order files TO-TX-p-1, TO-TX-g-1, TO-TX-g-2 | `complete` on all three | W6-S1, W6-S4, S2, S3, W1-S1 |
| `git merge-base --is-ancestor f2cac74c60 HEAD`; the route module tracked | yes; 1 file | S4 |
| the live publisher's `MDPF_PUBLISHER_COMMIT` | `e8994f23af...`, the deployed pin | W6-S3 |
| the control-write tests at HEAD and at the deployed pin; the suite | three tests present; 227 passed (06:3xZ) | S8 |
| `test_global_fold_flag2.py` | 3 failed, 16 passed | S1 |
| `mdpf-daily-dispatch.sh` | 0 lines naming `lib/` | S5 |
| `deploy-to-ec2.sh` | 0 lines naming TAXSMA; control 13 lines naming `.env` | S11 |
| the two Gold config names across the tree | 1 file under `data/mdpf/scripts`, 0 under `infra/aws/terraform` | W2-S2 |
| the contract | version 0.6.0; `UNCONFIRMED` only inside the member `REMOVED_UNCONFIRMED` | W5-S1 |
| `verify-ec2.sh` history; the tracked Gateway audit and telemetry files | unchanged since 2026-07-23; both tracked | S12, W1-S2, W1-S4 |

Not read: a runner log for Stage 6 (S5); the Gateway host or its manifest (W6-S2); the gateway root's plan (S10);
`verify-ec2.sh` in a run (S12); the naming gate on the refused literal (S13).

## Dispositions

| rows | class / standing | state |
|---|---|---|
| S2, S3, W1-S1 | OBSERVATION | LANDED, dismissed (C-S1): an environment limit the criteria stated |
| W6-S1 (BLOCKING), W6-S4 | resolved by amendment | LANDED, dismissed (C-S2) |
| S4, S7 (BLOCKING, ARMED) | states that no longer hold | LANDED, dismissed (C-S3); S7's remainder is S10's |
| W6-S3, S8 | repaired, read today | LANDED, dismissed (C-S4) |
| W1-S3, W2-S1 | reading records | LANDED, dismissed (C-S5) |
| S10 (BLOCKING, ARMED) | to graduate, `0.0.0_AB_MSTR` | PREPARED: disarmed for this project; the class stays |
| S11 (BLOCKING) | to graduate, `4.0.0_SA_CRO` | PREPARED: P0 for activation |
| S5, S6 (ARMED) | to graduate, `4.0.0_SA_CRO` | PREPARED: the runner's `lib/` sync; the narrow Gateway cut |
| S12 (ARMED) | to graduate, `1.0.0_SA_CTO` | PREPARED: a check that says in-sync on zero checks |
| S1, S9, S13, W6-S2, W1-S2, W1-S4 | to graduate, `1.0.0_SA_CTO` | PREPARED: placement |
| W5-S1, W2-S2 | to graduate, `4.0.0_SA_CRO` | PREPARED: conditions on TX-v-1 and TX-r-3 |

Of the 7 BLOCKING-or-ARMED rows, 2 are dispositioned on the channel (W6-S1, S7) and 5 are not yet (S5, S6, S10, S11,
S12). Their owners and remedies are written in the prepared file and can be acted on from there.

## For the CTO, on closing this project

- **The project cannot be counted, compiled or closed while its order files read as they do.** Each done order needs
  its terminal status with its pointer, by the issuer (`2.0.0_SA_COO~T`) or the FAST seat; the six that are not done
  (c-2, o-1, r-2, r-3, v-2, v-3) are either superseded by the STATUS next-list with a pointer or stay the reason the
  project is open. When the gate reads 0 open, this seat lands the 13 rows after re-reading each live figure.
- **Activation has three unowned preconditions in this channel**, none of them code this lane can land alone: S11
  (the `.env` lines), S6 (the narrow Gateway cut) and the Gateway release itself, which has had no owner since
  04:00Z and is Andrew's call.
- **Four Gateway test modules have never run on the laptop** (moto is absent; C-S1). Whoever releases the Gateway
  route owns running them where moto exists.
- **S1's red tests sit on the same carry path as finding F-A.** MDPF_HEALGAP now holds F-A; the three failing tests
  are that project's first read.

## What you should have asked but did not

- **Is the FULL-to-FAST boundary leaving every FAST project's orders in this state?** MDPF_TAXSMA went FAST on
  2026-09-30 with 15 orders non-terminal and they still are. The IRPT lanes did the opposite at their boundary
  (`2.0.0_SA_COO~M` superseded five stale Holdings orders with pointers). If the boundary's rule is "nothing running
  is left reading pending", this lane skipped it; if there is no such rule, every FAST project reaches its close
  with a register that cannot count it and a channel the CVO cannot compile.
- **The gate and the closure plan pull in opposite directions here.** The plan wants a channel compiled so a project
  can close; the gate admits remediation rows only after the round is terminal. For a project that is ONE-JOURNEY-
  SHORT and FAST, "terminal" never arrives by rounds. Either the orders are brought terminal by supersession at the
  FAST boundary, or the gate learns that a FAST lease is a state in which the CVO may graduate rows. Both are the
  CTO's.

-- 3.0.0_SA_CVO
