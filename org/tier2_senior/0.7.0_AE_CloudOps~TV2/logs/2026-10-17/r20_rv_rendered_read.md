# TCKT_VNEXT TO-R20-RV: one Meeting Request journey read in the rendered page, six shots, RUN-OK (render) -- 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY
**Date:** 2026-10-17
**Task Order:** TCKT_VNEXT.TO-R20-RV (AMENDMENT 2, GO msg 10369; run pair AMENDMENT 5)
**Status:** COMPLETE (the judgment criterion R20RV-AC1J is the CVO's)

---

## Objective

Run the FWD-11 journey once on the CTO's `localhost:5174` server (DEV `38d4f9473284`, which carries cell R20-pt-1): a synthetic filer files one Meeting Request, a synthetic coordinator is the sole routing primary for one window and confirms a time, the window closes, a bystander outside `routing.primary` reads the ticket, the filer claims and completes it, and the filer opens the meeting form unsubmitted. Six screenshots are saved; none is described here. Pair blobs: COO `08c9ba4bb2`, CTO half `098b12581d`; check `eace42e468`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open 11 legs, close-leg x11, close | PASS | `tckt-vnext-r20-rv-20261017` CLOSED 08:33:41Z |
| terraform plan / safe-apply | window open (scratch copy), window close (committed tree) | PASS | each plan 0 add, 1 change, 0 destroy, `ROUTING_MATRIX` `meeting_request.primary` only; both applies rc=0 |
| r20_run.py (this seat) | background, one process, gate files | PASS | ticket filed 201, confirm 200, claim and complete, 6 PNGs, rows deleted and ABSENT |
| r20_run_check.py (issuer) | criterion R20RV-AC2 | PASS | `RUN-OK (render)` |
| commit-gate.sh | on the script | PASS | |
| proof-of-spec-check.py | with --governing-order | PASS | VALID rc=0 (2 rows; the judgment row has no verdict from this seat) |
| comp-* graph tools | not run | SKIPPED | no code, IAM or infra change beyond one Lambda environment value applied by the pair's method |

**What worked:** minting all three identities from one key read and clipping each shot to the one ticket's two rows (no other ticket captured). **What failed:** the first safe-apply of the window stopped at the HALT gate (below). **Gap found:** my inbox watcher did not surface messages for about an hour (below); the HALT gate counts files left in the inbox directory, so it flags mail already read through the broker.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | GO 10369 (sent 07:05Z) | found at ~07:59Z via check-inbox; the watcher raised no event; acked and disclosed to the issuer in my first message |
| 1 | Blobs and start gate | pair `08c9ba4bb2`, CTO half `098b12581d`, check `eace42e468` equal; served checkout HEAD `38d4f9473284` (clean) = the handed-over sha, cell `6cdd0bfd917b` an ancestor; live routing jeanette alone |
| 2 | Ledger opened FIRST, slug sent to the issuer | `tckt-vnext-r20-rv-20261017`, 11 legs |
| 3 | Asks | CTO (10400): nothing open on the ticket service, notes IB2's possible switch-on mint; Y2 (10401): none open; IB2 (10408): none open; final census 97 trees clear |
| 4 | Window-open plan verified | 0 add, 1 change, 0 destroy, `jeanette@opalinvest.com` -> `tckt-r20-coord-20261017@opal.invalid` |
| 5 | Run started 08:12:59Z | three rows written and read PRESENT; one key read; three tokens, exp 08:31:59Z; page origin `http://localhost:5174` |
| 6 | Window opened | first `safe-apply` stopped at the HALT gate on 4 routine pending messages I had already read and acked; same plan re-run with `HALT_ACK=1`, rc=0 at 08:17:59Z; routing_during = coordinator alone |
| 7 | Filing and confirm | ticket `TCK-20261017-da2a1987`, create 201, `open`, `routing.primary` = coordinator; log `WE_DL_UNCONFIGURED`; shot 1 saved; coordinator Confirm 200, `meeting.by` the coordinator, ticket open |
| 8 | Window closed FIRST | committed tree (blob `748e680fd7f8`), one attribute back, `HALT_ACK=1`, rc=0 at 08:20:38Z; routing_after = jeanette alone |
| 9 | Shots 2 to 4, claim and complete, shots 5 and 6 | claim: `in_progress` under the filer, lines `WE_CLIENT_NOT_SINGULAR` and one `WE_CLIENT_NO_CONTACT firm=cottonwood`; complete: `completed`; no `WE_CLIENT_SENT`; six PNGs saved |
| 10 | Removal | three rows deleted 08:32:04Z (after the last exp 08:31:59Z), each ABSENT |
| 11 | Check, ledger | `RUN-OK (render)`; ledger CLOSED 11 of 11 at 08:33:41Z |

## Verification

```
r20_run_check.py -> RUN-OK (render) ticket confirmed then completed, six shots saved as PNG, three identity rows absent, routing restored
live meeting_request.primary now -> ["jeanette@opalinvest.com"]; 5174 still serving 38d4f9473284 (200)
shots (path under deliverables/r20_run/, bytes): filer_waiting 13826; filer_confirmed 17297; coordinator_controls 30274; bystander_no_control 17297; filer_completed 17254; meeting_form 22044
```

---

## Decisions Made

- Reviewed the four routine HALT-gate messages (all already acked) and re-ran the same plan with `HALT_ACK=1`; the second apply used the same verified planfile.
- Recorded shot paths and sizes only; the issuer and the CVO read the images.
- Mint all three identities up front (one key read) so the filer's token covers the whole sitting inside 19 minutes.

## Blockers

None. The judgment row (R20RV-AC1J) waits for the CVO at L9.

## Current State

The ticket `TCK-20261017-da2a1987` is `completed`; all three identity rows are ABSENT; routing is Jeanette alone; `localhost:5174` was never touched. Records and PNGs in `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/`. Kept until a human confirms deletion: `C:/dev/tv2-r18run-scratch` (its `main.tf` now carries the R20 coordinator value; restore it to the committed blob before any reuse), `C:/dev/tv2-rel-r1819`, `C:/dev/tv2-rel-r20-out`. The inbox watcher is re-armed; I now also read the inbox directly at each gate.

## Next Steps

1. `[2.0.0_SA_COO~V2]` Read the six shots; compile the packet for `3.0.0_SA_CVO~DELL2` (R20RV-AC1J). Shot 5 is the one that decides FWD-11.
2. `[2.0.0_SA_COO~Y2]` The ledger `tckt-vnext-r20-rv-20261017` is CLOSED; window 5 may be lifted by its own order.
3. `[0.0.0_AB_MSTR~DELL2]` The signing-key read of this order (one read, three token mints at 08:12:59Z) is reported after the fact.
4. `[0.0.0_AB_MSTR]` Carry this seat's local commits from box/dell2; consider why the inbox watcher missed messages for about an hour.
