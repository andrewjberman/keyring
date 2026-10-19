# TCKT_VNEXT TO-R20-PROD3: the Trade Request journey on PROD, two attempts, filed and cleaned up, the read-back UNPROVEN -- 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY
**Date:** 2026-10-19
**Task Order:** TCKT_VNEXT.TO-R20-PROD3 (GO msg 10941, CTO msg 10936; COO AMENDMENT 1 msg 11000, AMENDMENT 2 msg 11006 on the CTO's ruling 11005)
**Status:** NOT COMPLETE. Order stays `pending`; ledger `tckt-vnext-r20-prod3-20261019` OPEN (legs R1, V1). R20PROD3-AC1 would read RUN-BAD (no result file).

---

## Objective

One synthetic internal filer files ONE Trade Request with ONE synthetic .csv on https://opalinvest.dev through the form's three calls, reads the attachment back through the Open control (SHA-256 equal), then the ticket (record saved), the filer row and the uploaded object are removed.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open 6 legs; close-leg S1, M1, F1, D1 | PARTIAL | R1 and V1 open |
| r20_trade_prod.py (this seat) | two background runs | PARTIAL | filing and cleanup work; the read-back step stopped twice |
| commit-gate.sh | on the script, after each edit | PASS | |
| r20_tradejourney_check.py | not run | SKIPPED | no result file exists (both attempts stopped before it) |

**What worked:** `check-inbox` first; all four asks answered before the runs; door 200, PUT 200, ticket 201 in both attempts; create logged only WE_DL_UNCONFIGURED; PROD head `facddeb687b8` unchanged at every check; ticket and row deleted by key and read ABSENT in both attempts. **What failed:** (1) attempt 1: my `route.fetch` hung 40 s at the open read (STOP). (2) Attempt 1 cleanup: `delete-object` AccessDenied, an EXPLICIT deny in `cloudops-dell-agent-deploy-policy`; the script crashed before the row delete, the row was deleted by CLI 20:49:11Z. (3) Attempt 2: the Open route answered 200 and the browser's GET to the object went through, but my script read no `url` from the body and stopped (the body shape was not logged). **Gap found:** the Playwright error dump in attempt 1 printed one presigned URL into a scratch log; I scrubbed query strings from the committed logs and the script now redacts them.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Ledger opened FIRST 19:52Z, slug to V2 and Y2; asks to CTO, IB2, Y2 | Y2 backoff release live 20:15:44Z (msg 10993) |
| 1 | Start gate 20:35Z | head `facddeb687b8`, CI 39317468736 success 20:15:56Z, site 200, row ABSENT, prefix 0 objects, protected tickets present |
| 2 | Attempt 1 20:37Z | TCK-20261019-2d6d1a25 filed; open read STOP; ticket deleted 20:45:22Z; object delete DENIED; row deleted 20:49:11Z |
| 3 | Rulings | COO 11000 one rerun; CTO 11005: the deny stands, objects stay as RESIDUE (AMENDMENT 2) |
| 4 | Attempt 2 21:23:49Z (token 180 s) | TCK-20261019-b931d737 filed; open read STOP; ticket and row deleted 21:26:56Z |

## Verification

```
residue (head-object 21:28Z, 31 bytes each):
 portal/cottonwood/state/ticket_attachments/trade-form/8b46f05593e643f0bb229023841d2a4a/tckt-r20-trade-synthetic.csv  version U2wA9rMN_iqdUnci740XcsAfyvgsTK3h
 portal/cottonwood/state/ticket_attachments/trade-form/b35a21075c634b588e83a529a8a724c5/tckt-r20-trade-synthetic.csv  version 0pTf.3QXwPeHDLNgFTEKCnP32IE4IWuu
tickets TCK-20261019-2d6d1a25 and TCK-20261019-b931d737: ConsistentRead ABSENT; filer row: ABSENT; PROD head facddeb687b8
```

---

## Decisions Made

- Did not try another identity or a policy edit against the explicit deny; reported it (row S62) and followed the CTO's ruling.
- Used the one rerun the COO granted; did not start a third.
- Kept the ledger OPEN rather than closing 6 of 6 on an unproven read-back.

## Blockers

The read-back equality (R1) is unproven. A third attempt needs a new GO and a window; its first act should log the KEY SET (not values) of the Open route's body. Row S63 records this.

## Current State

Records and shots: `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_trade_prod/attempt1/` and `attempt2/` (ticket item, shots, trace, scrubbed run log); script `r20_trade_prod.py`; `promote_proof.txt`, `fire_windows_answer.txt`. Two 31-byte synthetic objects stay under the firm's trade-form prefix. Commits are LOCAL on box/dell2. Scratch left: `C:/dev/tv2-r18run-scratch`, `C:/dev/tv2-rel-r1819`, `C:/dev/tv2-rel-r20-out` (attempt stdout files, unscrubbed), awaiting a human's word to delete.

## Next Steps

1. `[2.0.0_SA_COO~V2]` Decide whether a third attempt is wanted; if so issue a GO and a window.
2. `[1.0.0_SA_CTO~DELL2]` The delete-by-version of the two residue keys is yours for Andrew (ruling 11005).
3. `[0.0.0_AB_MSTR~DELL2]` Two more signing-key reads and tokens (attempts 1 and 2 of PROD3) are reported after the fact.
4. `[0.0.0_AB_MSTR]` Carry this seat's local commits.
