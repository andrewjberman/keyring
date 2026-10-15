# /self-drive dell1 box open calls -- tick 23 (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~20:50Z, last log before the 21:00Z restart)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_DELL1_BOX_OPEN_CALLS.md` @bcd3be8ec3. Cron 4e032862 (:17) dies with this session.
**state: ARMED.** The successor re-arms off the arming record plus this log.
Covers the window since tick 22 (@37abf8ad4c).

## Measured (~20:49Z)

- **Box list:** two calls open.
  - `fbdf` (approval) is the J359 footnote deletion. It is client-facing and HELD for Andrew.
  - `df8f` (fork) is CROSS-BOX and was escalated as XA-20261014T204823Z-c7cd to the laptop.
- **MDPF_CANON PRD:** v2.21 @`3826492d9c` **ADMITTED**. The CVO signed it (review @635c0bea22).
- **Inbox:** 0 unread. Msgs 5857 to 5876 were acked and acted on.

## Andrew-direct this window (relayed records)

| word | record | applied |
|---|---|---|
| "only opal staff see global ... rec a, that is the easiest stitch"; satellite returns = models plus the commodity ticker at its weight | CRO `ANDREW_DIRECT_20261014_204xZ_MDPF_GLOBAL_TREND_VARIANT_1_AND_SATELLITE_GLD_RETURNS.md` @ab28358b88 | PRD v2.19 @02852d9d16. GLD is confirmed; 90/98 hold none (Black Diamond definitions), and J359's live formula matches |
| "put the SMA strategies in there"; "muni is just a custom model" | CRO spec amendment 1 @686f769e63 | PRD v2.21 @3826492d9c |
| "whatever CRO~DELL1 and I agreed on" (the ship-now-or-wait card) | `2.0.0_SA_COO` `ANDREW_DIRECT_20261014_204xZ_COO_D1_WHATEVER_CRO_DELL1_AND_I_AGREED.md` @21f20dc8ec | CN-i-3 WITHDRAWN. The approved edits ride the Variant 1 portal row |

## Verdicts and rulings

- **CVO 5865 REFUSED v2.19.** The demo tenant opens Global on PROD (`ModelPortfolios.tsx:271`, `:375-379`).
  - Ruled: the CVO's option 3, built as a read-side stitch. Single-firm Trend lines draw only for internal sessions, from the firm's own series. The Global leaves keep FWD-3's fold. Other sessions see Variant 2 plus exception (ii).
  - Result: v2.20 @038b2173f3, then v2.21 (SMA, Muni), which the CVO SIGNED.
- **Row `MDPF_CANON-D1-S27` (CVO, ARMED, disarm owner this seat):** per-firm MDPF leaves under `/api/general/mdpf/*` are not firm-gated at the edge.
  - Disarmed by routing: call `df8f` went to XA-c7cd at the laptop.
  - REC: measure live with a partner token as the negative control, then gate `auth-validator-edge` to the claim's firm.
  - It does not gate the Variant 1 round.
- **~D1:** cut the Variant 1 round now. The producer pieces are Client Supervised by difference, SMArtX SMA legs, `carried` rows and Muni to Custom, under a never-widen pair. The portal piece is the stitch plus the approved edits, on one client-facing row.

## Completion test

Box scope: **NOT DONE**. The stop is Andrew's stand-down. REACHABLE 0. HELD 1 (`fbdf`, his). CROSS-BOX 1 (`df8f`, at the laptop).

## ACTS ONLY ANDREW CAN DO (cited)

- **Approve `fbdf`.** It is a client-facing PROD push (CLAUDE.md Agent Autonomy). CVO grade @f1fda28056 holds J359 FAIL until it lands. If there is no word, the successor rules on the rollback to `6z8c7qDD`.
- **The Variant 1 /portfolios client-facing row**, when ~D1 registers it (same citation).
- **The 21:00Z restart at the console** (msg 5483).
- Carried from earlier ticks: the SECCLASS BD Mix PROD push; his gateway session; the ASTN FT hold; ADVI_BILLING's answers; G4 activation.

## For the successor (re-arm and pick up)

1. Re-arm `/self-drive 60m` off the arming record (`LIVE_ARMS` row), and `/watcher` once.
2. Read `fbdf` (Andrew's word, or the rollback ruling); XA-c7cd (laptop verdict, then `close --xadj`); ~D1's Variant 1 issuance and its never-widen pair; and FB-m-2 arm (a) on 10-15 by 14:00Z, then FB-l-5 act 3.
3. Owed by this seat: the Cottonwood Trend CRO ask, after the Global round; the AMGT_RESAPP round-107 analysis (G13/G14 first; G15, G1, G2-G5, G8); the MDPF_DEMQUE G9-G12 analysis; and the RIVALS r30 grades when its completion report lands.

## Compiler Tools

`open-calls.py list/add`; `xadj.py open`; `prd-signoff.py status`; `safe-commit.sh`.

-- 1.0.0_SA_CTO~DELL1
