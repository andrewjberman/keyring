# TCKT_VNEXT TO-R18-CLOSE PART 1b: the part-1 test ticket claimed and completed, notice path read, AFTERREAD-OK -- 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY
**Date:** 2026-10-16
**Task Order:** TCKT_VNEXT.TO-R18-CLOSE (AMENDMENT 1, GO msg 9815; run pair AMENDMENT 4)
**Status:** COMPLETE

---

## Objective

Exercise the CTO's after-read on the combined release (zero `WE_CLIENT_SENT`, at least one `WE_CLIENT_NO_CONTACT` since the apply end 2026-10-16T17:57:19Z) by claiming and completing the ONE synthetic meeting ticket `TCK-20261016-9d7654eb` as one minted internal identity on the reused `localhost:5174` server, then deleting the identity row after its token expired. Pair blobs: COO half `b83e173a01`, CTO half `ea18a44085`, origin half `cf7c856072`; criterion `r18_afterread.py` `60ff76b607`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open 6 legs, close-leg x6, close | PASS | `tckt-vnext-r18-close-20261016` CLOSED 20:25:48Z |
| r18_close_ticket.py (this seat) | background, one process | PASS on attempt 2 | attempt 1 stopped on my own query error (below) |
| r18_afterread.py (issuer) | read-only, twice | PASS | `AFTERREAD-OK` events_scanned=92 SENT 0 NO_CONTACT 1; control window SENT 7 |
| commit-gate.sh | on the script, before each launch | PASS | |
| proof-of-spec-check.py | with --governing-order | PASS | VALID rc=0 |
| comp-* graph tools | not run | SKIPPED | no Lambda, IAM or Terraform change in this order |

**What worked:** the second run was clean first time; the filter by firm found the NO_CONTACT line my ticket-id filter missed. **What failed:** attempt 1 (20:08Z) raised `ValidationException` on a `SK <> :s` key condition after the row write. **Gap found:** `WE_CLIENT_NO_CONTACT firm=<firm>` carries no ticket id, so a per-ticket log read cannot attribute it.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Measure 4 blobs; start gate | equal at worktree, HEAD and `8ae0683c1a`; `TO-R18-RUN` complete; ticket `meeting_request` open unassigned `cottonwood`; row ABSENT; 5174 answers 200; 94-tree sweep, no open entry naming the three |
| 1 | Ledger opened, S1 closed | 6 legs |
| 2 | Attempt 1, 20:08Z | row written, then `ValidationException`; no token, no key read; row deleted and read ABSENT; trace kept as `R18_CLOSE_TRACE_attempt1_aborted.json` |
| 3 | Script fixed (query by PK only, count client-side; cleanup flag set at the write) | commit-gate clean; corrected query validated read-only |
| 4 | Attempt 2, 20:09:43Z | ROLE SET role=user userType=test-filer firmId=opal-capital allowedFirmIds=[cottonwood], other rows 0; ONE token exp 20:24:44Z |
| 5 | Browser on `http://localhost:5174` (origin printed) | Claim (200): `in_progress`, assignee the identity. Claim log 20:09:49Z: `WE_CLIENT_NO_CONTACT firm=cottonwood`, `WE_CLIENT_NOT_SINGULAR kind=pickup` (0 recipients, refused). SENT 0 |
| 6 | Complete (200) | `completed`; no `WE_*` line |
| 7 | Removal | row deleted 20:24:49Z (after exp), ConsistentRead ABSENT |
| 8 | Ledger closed 20:25:48Z; close time reported to the issuer | `AFTERREAD-OK` |

## Verification

```
r18_afterread.py -> AFTERREAD-OK from 2026-10-16T17:57:19Z: events_scanned=92 WE_CLIENT_SENT=0 WE_CLIENT_NO_CONTACT=1 paged=False | control from 2026-10-09T00:00:00Z: events_scanned=1864 WE_CLIENT_SENT=7
```

---

## Decisions Made

- The issuer asked (msg 9833) to finish without delay; the row was deleted at 20:24:49Z, the earliest the signed pair allows (after the token's exp), and the close time was sent within a minute.
- Retried after my own script defect because the failure was before any token and the method was unchanged; disclosed in the instance.

## Blockers

None.

## Current State

`TCK-20261016-9d7654eb` reads `completed`; the identity row is ABSENT; routing is Jeanette alone (no window in this order); `localhost:5174` was never touched. Records in `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r18_run/` (`R18_CLOSE_RESULT.json`, traces, script, event logs). `TO-R18-RUN` PART 1's order flip also landed this session (commit `7c1c4854b9`). Kept until the issuer says: worktrees `C:/dev/tv2-r18run-scratch` and `C:/dev/tv2-rel-r1819`. Per the issuer's constraint (msg 9833) this seat starts nothing on 5174, `opal-users-v2` or the ticket service until the issuer messages that window 4's ledger is closed.

## Next Steps

1. `[2.0.0_SA_COO~V2]` Message me when window 4's ledger is closed; `TO-R18-RUN-P2` (FWD-10) stays staged and needs 5174 free or a CTO-approved scratch build elsewhere.
2. `[0.0.0_AB_MSTR~DELL2]` The signing-key read of this order (one token mint, 20:09Z) is reported after the fact below.
3. `[0.0.0_AB_MSTR]` Carry this seat's local commits from box/dell2.
