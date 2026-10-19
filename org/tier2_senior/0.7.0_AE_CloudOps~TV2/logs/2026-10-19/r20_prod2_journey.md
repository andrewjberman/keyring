# TCKT_VNEXT TO-R20-PROD2: the FWD-11 journey on the PROD site, RUN-OK (prodjourney), contrast 10.10:1 -- 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY
**Date:** 2026-10-19
**Task Order:** TCKT_VNEXT.TO-R20-PROD2 (AMENDMENT 1, GO msg 10800; hold lifted msg 10833, CTO ruling RUN msg 10829; run pair AMENDMENTS 8 and 9)
**Status:** COMPLETE (the judgment criterion R20PROD2-AC2J is the CVO's; FWD-11 is REALIZED only on that grade)

---

## Objective

On `https://opalinvest.dev`, one synthetic filer files one Meeting Request, one synthetic coordinator confirms it inside one routing window on `opal-ticket-api` `ROUTING_MATRIX` `meeting_request.primary`, the filer reads the confirmed line (contrast printed as a number), then the one synthetic `opal-tickets` item (record saved first) and both `opal-users-v2` rows are deleted by key. Pair blobs: COO `0b2978bfea`, CTO half `e7a33cf976`; check v2 `9ff30a5d38`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open 9 legs, close-leg x8, close | PASS | `tckt-vnext-r20-prod2-20261019` CLOSED 19:26Z |
| r20_prod2.py (this seat) | background, one process, attempt 3 | PASS | filed, confirmed, 3 shots, contrast, deletes |
| terraform plan / safe-apply | window open and window close, each plan 0 add 1 change 0 destroy | PASS | open applied 18:16:24Z, close applied 18:23:40Z |
| r20_prodjourney_check_v2.py | check and `--self-test` | PASS | `RUN-OK (prodjourney)`; `R20-PRODJOURNEY-SELFTEST-OK` |
| commit-gate.sh | on the script | PASS | |
| Pillow | WCAG contrast from own PNG | PASS | 10.10:1 |

**What worked:** `check-inbox` first; plan verified one-change before each apply; the gate files let the applier close the window while the script held the tokens. **What failed:** attempt 1 died on a network reset in preflight (before any write); attempt 2 was aborted at 18:00:55Z on timing (halt gate plus seat-gate delay), before any window or ticket existed. **Gap found:** the inbox watcher expired and missed the re-seated COO's msg 10912 (read 19:21Z by check-inbox).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Ledger opened FIRST, slug sent to the COO and Y2; blobs equal | S1 closed 17:52Z |
| 1 | Start gate | PROD head `8cd45f623bdf` (a news-sentiment promote landed after the GO, Ticket Center files byte-identical, COO confirmed msg 10845); site 200; fire windows answered (`r20_prod2/fire_windows_answer.txt`) |
| 2 | Attempt 3 run, 18:11:24Z | two rows written and PRESENT; one token each, iat 18:11:25Z exp 18:29:25Z (1080 s) |
| 3 | Window open | plan 1 change; safe-apply rc=0 18:16:24Z; read back: coordinator alone |
| 4 | File | `TCK-20261019-c50b4967` filed 18:16:31Z; shot `prod_filer_waiting` |
| 5 | Confirm | shot `prod_coordinator_controls` before the click; confirmed first proposed time 18:16:47Z |
| 6 | Window close | committed tree (main.tf blob `748e680fd7f8`) plan 1 change; safe-apply rc=0 18:23:40Z; read back: jeanette alone |
| 7 | Read | shot `prod_filer_confirmed`; contrast 10.10:1; PROD head unchanged at 4 checks |
| 8 | Delete | after exp: ticket record saved whole, deleted by key 18:29:30Z; both rows deleted 18:29:30Z; all ConsistentRead ABSENT |
| 9 | Check, ledger | `RUN-OK (prodjourney)` beside `R20-PRODJOURNEY-SELFTEST-OK`; ledger CLOSED 19:26Z |

## Verification

```
r20_prodjourney_check_v2.py -> RUN-OK (prodjourney) filed, confirmed and read on https://opalinvest.dev; the synthetic ticket and both rows ABSENT; routing restored; the two protected tickets present
r20_prodjourney_check_v2.py --self-test -> R20-PRODJOURNEY-SELFTEST-OK
contrast (own PNG, WCAG): 10.10:1 (rgb(209,212,217) on rgb(25,38,67))
```

---

## Decisions Made

- The New Ticket type list read: Trade Request, Service Request, Meeting Request, Other, Analysis Request. Trade Request IS listed on PROD (the 2a64d211 release no longer filters it). Per the CTO's binding condition this run RECORDED it and did not stop; Andrew's hold concerns the Trade Request action, which this run did not touch.
- Retried after two pre-write failures, disclosed to the COO; the same method, longer tokens (18 min) and later gate deadlines.
- Window closed by the applier through a plan from the committed tree, not the scratch copy.

## Blockers

None. R20PROD2-AC2J waits for the CVO at L9.

## Current State

Routing `meeting_request.primary` = `jeanette@opalinvest.com` alone (live read 18:24:27Z). Ticket `TCK-20261019-c50b4967` and both rows ABSENT. Protected tickets `TCK-20261017-da2a1987` and `TCK-20261017-5af976ff` present. Ledger `tckt-vnext-r20-prod2-20261019` CLOSED. Records and PNGs in `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_prod2/`. Scratch `C:/dev/tv2-r18run-scratch` main.tf restored to blob `748e680fd7f8`. Kept until a human confirms deletion: `C:/dev/tv2-r18run-scratch`, `C:/dev/tv2-rel-r1819`, `C:/dev/tv2-rel-r20-out`. Commits are LOCAL on box/dell2.

## Next Steps

1. `[2.0.0_SA_COO~V2]` Measure the contrast independently from `prod_filer_confirmed`, read the three shots, compile the L8 packet for `3.0.0_SA_CVO~DELL2` (R20PROD2-AC2J).
2. `[2.0.0_SA_COO~Y2]` The ledger is CLOSED; window 5 may lift per its own order.
3. `[0.0.0_AB_MSTR~DELL2]` Two signing-key reads and tokens this run (attempts 2 and 3 minted; attempt 3 used) are reported after the fact.
4. `[0.0.0_AB_MSTR]` Carry this seat's local commits; the inbox watcher keeps expiring and missing mail.
