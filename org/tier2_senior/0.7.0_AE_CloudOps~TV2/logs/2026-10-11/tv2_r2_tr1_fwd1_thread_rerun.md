# The FWD-1 journey reached the submission and the submission refused it — 0.7.0_AE_CloudOps~TV2

**archetype:** VALIDATE

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-RUN-R2-tr1.fwd1-thread-rerun-tv2 (first GO @ec3d0fd6c1, second GO @bc3a095fd2)
**Status:** COMPLETE — outcome branch C; FWD-1 NOT REALIZED

---

## Objective

Run the FWD-1 journey once end to end on DEV as the synthetic one-firm filer: upload, file the
Analysis Request ticket, claim, submit, read the finished report for the issued id, record it on the
ticket, open it from the ticket. Then clean up in the signed order. Cell `R2-tr-1`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | two entries (attempt 1, then `...-run2-`), `open` + 4x `close-leg` + `close` each | PASS | both opened BEFORE any write and closed with every leg proven or dispositioned; each `.open_deploys` row read back ABSENT against a printed control |
| fwd1_run.py @2d2b309be9 | ONE invocation, backgrounded | PASS | rc 0, 160 lines, never interrupted, waited 2621 s for `exp` and exited on its own |
| r2_checks.py | `rn-safety`, `rn-zero`, `rn-arms` — both attempts | PASS | 6/6, 4/4, 4/4 each time |
| reread_27.py | once per attempt | FAIL then PASS | `21/27` rc 1 (branch D, row S28), then `27/27` rc 0 after the issuer's AMENDMENT 1 |
| comp-find | `'NOT-RELEASED\|CLAMPED\|RELEASED'` over reread_27.py | PASS | 1 hit / 1 file scanned — localised the verdict line at `:62` in a 71-line script |
| aws logs filter-log-events | `WE_` over `/aws/lambda/opal-ticket-api` across `iat..exp` | PARTIAL | 3 events; proves AMENDMENT 1's limb, exposes condition 3's missing field |
| aws dynamodb get-item | `--consistent-read` on the filer row + a control scan; journey ticket direct | PASS | no `Item` (ABSENT) against a control returning 1 item |
| proof-of-spec-check.py | on the instance | PASS | INVALID twice (schema enum, then pre-commit artifact resolution), then VALID rc 0 |
| safe-commit.sh | one commit per act, `-F` files written by a non-shell writer | PASS | `msg-verify MATCH` each time; surprise-row gate graded every new row |
| comp-schedule / comp-iam | not run | SKIPPED | DECLARED-NOT-APPLICABLE by the order's preflight |

**What worked:** `comp-find` turned the AC1 diagnosis from a guess into a one-line citation. Backgrounding
the runner was the right call and not a convenience — the token-expiry wait exceeds a foreground
ceiling, and the order warns an interrupt leaves the identity row in place.

**What failed:** nothing in my own tooling this order. Two of the pair's own instruments could not produce
the evidence their conditions require — the zero-call control and the `WE_CLIENT_SENT` line — and both
are rows rather than workarounds.

**Gap found:** three, all filed: S29, S30, S31.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Ledger first, then the open-deploys union | attempt 1: 29 trees, 32 rows, 13 distinct, all closed but mine. Attempt 2 re-taken at `06:17:08Z`: same verdict, 14 distinct, and the first attempt's own entry now reads closed-by `ad586be837` |
| 1 | Runner pin + `rn-*` | `10f1abb9...9557` == required, 0 dirty; 6/6, 4/4, 4/4 |
| 2 | Prechecks | `opal-ticket-api` W03VREoM · `irpt-status` 6idtFvAm · `TICKET_DL_MAP` 0 keys → PROCEED · **attempt 1: `READ27 21/27` → BRANCH D** |
| — | AMENDMENT 1 @bc3a095fd2 | the issuer admitted `ca3be343` to `TICKET_OK` on its own reads and issued a **second GO** |
| 2' | Prechecks again | all four PASS; `READ27 27/27`, `opal-ticket-api` now CLAMPED at the same bytes |
| 3 | THE RUN | rc 0; row written `06:20:46Z`, read back present, `allowedFirmIds` = `['49financial']`; token 45 min |
| 3a | Census, before any hop | 119 live vs 117 source (printed as a finding); 82 of 91 armed, 9 data-refresh skipped; `off_list_admits` EMPTY; 16 selector-ignored cleared, 0 leak, 0 UNKNOWN; `STOP=None` |
| 3b | Hops | (a)(b)(c) MET · **(d) REFUSED 200/`INVALID_INPUT`, `request_id` null** · (e)(f)(g) UNREACHABLE · `report_route_arms` EMPTY |
| 4 | Cleanup | both tickets completed 200; `TCK-20261009-67ab7f27` FOUND_LEFT_ALONE; row deleted `07:06:17Z` > exp `07:05:46Z`; absent |
| 5 | After-reads | see Verification |
| 6 | Close, report, key-read report | ledger CLOSED 4/4; one report to the COO; key read reported via `0.0.0_AB_MSTR~DELL2` |

## Verification

```
hop d_analysis : POST /api/scoped/investor-reporting/analysis
                 status=200  refused_reason=INVALID_INPUT  request_id=null
named_failures : e_ready / f_report / g_open -> UNREACHABLE
                 "depends on (d), which produced no service request id"
report_route_arms : {}            <- neither arm ran; NOT branch B

one firm       : armed 82 | off_list_admits [] | behaves-as-ALL 16 (0 leak, 0 UNKNOWN)
                 GET /api/scoped/tickets -> n=14 firms=['49financial']
row after exp  : token_exp 07:05:46Z | row_deleted_at 07:06:17Z | waited 2621.24s
                 read-back absent: runner True, and my own --consistent-read (control: 1 item)

zero-calls     : target /aws/lambda/opal-data-refresh-api  442 streams, 0 active, 0 matches
                 CONTROL /aws/lambda/opal-ticket-api       167 streams, 1 active, 0 matches
                 -> ZERO_CALL_VOID (CONTROL_FOUND_NO_FILER)   <- no zero-call claim made

mail           : WE_DL_UNCONFIGURED x2   WE_DL_SENT 0   WE_CLIENT_SENT x1
                 "WE_CLIENT_SENT kind=pickup ticket=... firm=49financial
                  message_id=... from=<local>@opalinvest.dev"   <- sender only, no recipient
                 journey ticket requester.email domain = opal.invalid (the filer's own)
```

---

## Decisions Made

1. **I did not edit the AC1 instrument to clear my own criterion.** `reread_27.py` reads
   `opal-ticket-api` against a hand-kept two-hash set, and the build I had deployed hours earlier under
   a signed pair was a third hash. Editing it would have been wrong whoever owned the file; it also sits
   outside this order's `<paths>`. I measured that the clamp was intact (4 added / 0 removed against R13,
   with a control proving numstat reports removals on that file), filed S28, and reported.
2. **I did not restart on a file edit.** When `TICKET_OK` changed, I first checked whether the change was
   **committed** — an uncommitted edit to an acceptance instrument is not authority — and only proceeded
   on finding `bc3a095fd2`, whose own text carries the words "SECOND GO". One trap worth recording: the
   log rendered that commit as `10-11 02:14` in **local** time, i.e. `06:14Z`, minutes *after* my Branch D
   close. Read as UTC it would have looked like a pre-existing edit.
3. **Reported branch C, and said the branch set does not name this case.** C's consequences fit exactly —
   a RESULT, record the code, no re-run, no widening. But C is written about hop (e), and hop (e) never
   started. I placed it at C rather than widening C's text or inventing a branch E, and filed S31.
4. **Withheld two claims the run could not support.** The zero-call verdict is VOID because its own
   control failed, and CTO condition 3 is neither violated nor confirmed because the line it is written
   against carries no recipient. Neither got a BLOCKING row (nothing evidences harm) and neither got a
   clean bill (nothing evidences compliance).

---

## Files Modified

| File | Commit |
|------|--------|
| ledger (attempt 1) + its `.open_deploys` row | `ad586be837` |
| ledger (attempt 2, run2) + its row | `da19026e07` |
| `deliverables/r2_tr1/r2_tr1_trace.json` (68459 B) | `da19026e07` |
| `TCKT_VNEXT.TO-RUN-R2-tr1...proof_of_spec.json` | `ad586be837`, rewritten `da19026e07` |
| surprise channel: S28 · S29, S30, S31 | `ad586be837` · `da19026e07` |

---

## Blockers

None owed by this seat. FWD-1 stays NOT REALIZED and the next cell is the issuer's to cut. The open
question is upstream of everything here: **why `POST /api/scoped/investor-reporting/analysis` answers
`200 INVALID_INPUT` for this submission.** That is a read of the submission envelope against the
published contract, not a re-run of this order.

---

## Current State

The journey is live and proven as far as the claim: upload, ticket, claim all work for a one-firm
internal filer, with zero off-list admits across 82 armed routes. The submission refuses. Nothing is
stranded: no open deploy entry, the identity row removed after `exp` and read absent twice, and the only
retained artifacts are one upload and two completed `[TEST TCKT_VNEXT FWD-1]` tickets under
`49financial`.

**What this run did NOT establish:** both live arms of the R2-rr-2 report-id shape check. The report
route was never called, so my own earlier deploy is neither exercised nor implicated — and specifically
this is **not** branch B, so no rollback is triggered.

---

## Next Steps

1. The issuer cuts the next cell from hop (d)'s code. Three rows await disposition: S29 (the zero-call
   control keys on something the handler does not log), S30 (log the recipient, or restate condition 3
   against the ticket's `requester` field, which is readable), S31 (the branch set).
2. AC2 goes to `3.0.0_SA_CVO` at L9 on the trace. Not self-graded.
3. A third run needs a new GO. This order consumed its one run.
