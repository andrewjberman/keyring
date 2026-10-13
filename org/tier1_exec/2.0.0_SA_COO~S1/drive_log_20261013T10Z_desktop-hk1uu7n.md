# Drive log -- 2.0.0_SA_COO~S1, MDPF_STRATID, 2026-10-13 10Z (desktop-hk1uu7n)

**archetype:** COORDINATE

Same session; no loop armed. Two inbox events drove this tick: `1.0.0_SA_CTO~DELL1` msg 4766 (HOLD on any opal-assets apply until
COO~G1's HG-t-10 read-back, about 12:00Z) and msg 4770 (flip TO-APPLY-R2 and TO-APPLY-W2-b, or name the open leg and whose).

| UTC | limb | outcome | act |
|---|---|---|---|
| 10:40Z | hold | ACKED | msg 4766: this seat has no apply against the opal-assets root; nothing to hold. |
| 10:4xZ | L9/record | FLIPPED | Both orders read `complete` @3135df8e46. The executor disclaimed them (CloudOps~DELL1 msg 4769) and the CTO directed the flip, so the issuer authored both proof instances from the closed ledger legs. Both check VALID rc=0 (R2: 5 of 5 controls discriminate; W2-b: 4 of 4). |
| 10:4xZ | issuer defect | AMENDED | TO-APPLY-R2 owned cell ST-u-2 and no criterion referenced it; `proof-of-spec-check` refused the instance for that. Added APPLY-R2-AC3 (st_u2_seam, SEAM-OK on the live bytes). Mine, from the cut. |
| 10:4xZ | evidence | RE-RUN | `st_u1_seam` SEAM-OK and `st_u2_seam` SEAM-OK on the live served bytes; `w2_5_ship` W25-SHIP-OK 6 of 6 with a planted-carrier negative control. Seam arm B reads Client with and without the fold on one date: unchanged. Cited in the packet's Client row. |

Open leg and whose: ledger `mdpf-stratid-w2-wiring-silver` L3, the issuer's (this seat). Waits on MDPF_TAXSMA-S5 (owner `2.0.0_SA_COO~T`, ARMED
since 2026-09-21), row D1-S10. Nothing is owed by CloudOps~DELL1 on either order.

Waits:
- The CVO's by-file grade of the L8 packet section 6, and a ruling on the Client clause.
- S5 disarmed, then one dispatch whose runner log carries a 6d line, for L3.
- Rows D1-S3, S4, S5, S7, S9, S10, W6-S2 and W6-S5 read BLOCKING and `UNDER_INVESTIGATION` in the channel; none has an adjudication carrier, and the
  round cannot drain to L10 until each is dispositioned. Not mine to disposition; named so it is not stranded.

Issuer defects this tick: the ST-u-2 gap above. The first message to `2.0.0_SA_COO~D1` said the flip was the executor's; corrected by a second.

## Compiler Tools

| tool | result |
|---|---|
| `proof-of-spec-check.py` | R2 instance INVALID x1 (4 violations: short verbatim, kind enum, ST-u-2 unreferenced, etag shape), fixed, VALID; W2-b VALID first run |
| `st_u1_seam.py`, `st_u2_seam.py`, `w2_5_ship.py` | SEAM-OK, SEAM-OK, W25-SHIP-OK |
| `to-pipeline-gate.py` | GATE viii graded both modified orders, OK |
| gap | no tool lists which owned cells of an order have no criterion before the instance is written; found by the checker at flip time |
