# The idempotency collision is fixed and a different refusal took its place — 0.7.0_AE_CloudOps~TV2

**archetype:** VALIDATE

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-RUN-R2-tr1.fwd1-thread-rerun-tv2 — AMENDMENT 2 @f0d4c2db95, third and last GO
**Status:** COMPLETE — outcome branch E; FWD-1 NOT REALIZED; no fourth run under this half

---

## Objective

Run the FWD-1 journey once more with the runner at `f4153fc637`, which mints a per-run idempotency
token, after run 2 ended at hop (d) on `CHANGED_INPUTS_SAME_REQUEST_ID`. Last run under the pair.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `...-run3-`, `open` + 4x `close-leg` + `close` | PASS | opened before any write; closed 4/4; row read back ABSENT against an 18-row control |
| fwd1_run.py @f4153fc637 | ONE invocation, backgrounded | PASS | rc 0, 145 lines, never interrupted; new pin, per-run token |
| r2_checks.py | `rn-safety`, `rn-token`, `rn-zero3` | PASS | 6/6, 4/4, 4/4 — `rn-token`/`rn-zero3` are new to this attempt |
| reread_27.py | once | PASS | `READ27 27/27` rc 0 |
| aws logs filter-log-events | full window read of `/aws/lambda/irpt-ycharts-generate`; `WE_` over `/aws/lambda/opal-ticket-api` | PARTIAL | the ticket read answered; the service read found **no reason for hop (d)** — row S32 |
| aws dynamodb get-item | `--consistent-read` filer row + control; journey ticket direct | PASS | no `Item` (ABSENT) against a control returning 1 item |
| safe-commit.sh | one commit per act, `-F` by a non-shell writer | PASS | `msg-verify MATCH`; surprise-row gate graded S32 |

**What worked:** the `rn-token` check plus the trace's `idempotency_token` field made the fix verifiable
rather than assumed — I could show run 3's token differs from run 2's rather than trust that it would.
The zero-call rule the CTO accepted off row S29 now returns a real verdict instead of VOID.

**What failed:** nothing of mine. The service log has no reason for hop (d)'s refusal, so branch E's
second instruction has nothing to read — row S32.

**Gap found:** one, S32.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Ledger first, then the union at `08:08:03Z` | **42 trees** (enumerated 42 == grepped 42), 47 rows, 17 distinct; only run3 open at my HEAD; runs 1 and 2 read closed-by `ad586be837` / `da19026e07` |
| 0b | CTO AMENDMENT 3 pre-GO condition | the 06:22:18 event PLACED **with its line** — one `MISSING_REQUEST_FIELD` carrying both it and `INVALID_INPUT`, matching run 2's `arms[71]`; the single `CHANGED_INPUTS_SAME_REQUEST_ID` 16.6 s later, same stream |
| 1 | New pin + three checks | `f8ef2b1f...2bb4` == required, worktree == blob at `f4153fc637`, 0 dirty; 6/6, 4/4, 4/4 |
| 2 | Prechecks, re-read live | `W03VREoM` · `6idtFvAm` · `TICKET_DL_MAP` 0 keys → PROCEED · `READ27 27/27` · new trace path absent |
| 3 | THE RUN | rc 0; row `08:12:32Z`, token exp `08:42:32Z` (30 min) |
| 3a | Hops | (a) MET on poll **2** (`RESOLVING` → `NORMALIZED`) · (b) `TCK-20261011-61631267` 201 · (c) 200 · **(d) REFUSED 200/`NOT_READY`** |
| 3b | Arms | both recorded `UNREACHABLE`, why `BRANCH_E_SUBMISSION_REFUSED` — explicit this time, not an empty object |
| 4 | Cleanup | both run tickets completed 200; `TCK-20261009-67ab7f27` untouched (no `--close-ticket`, per the amendment); row deleted `08:43:02Z` > exp `08:42:32Z` |
| 5 | After-reads | see Verification |
| 6 | Close, report once, stop | ledger CLOSED 4/4; one report; no fourth GO |

## Verification

```
hop d : POST /api/scoped/investor-reporting/analysis
        status=200  refused_reason=NOT_READY  request_id=null
        result=BRANCH_E_SUBMISSION_REFUSED
        idempotency_token=r2tr1run3-a5e6c43e3bbe069d00ef4894     <- per-run
        run 2 was        sar1b-bb079cbf53aaa2be7ce3fb6b          <- fixed by the input file
arms  : report_id_malformed_refused     UNREACHABLE (BRANCH_E_SUBMISSION_REFUSED)
        report_id_well_formed_stored    UNREACHABLE (BRANCH_E_SUBMISSION_REFUSED)

zero-calls (now PROVEN, S29's remedy):
        read_not_before 08:47:32Z | read_at 08:47:32Z | waited 269.83s   (= exp + 300s)
        streams 442 | active_in_window 0 | latest_event 2026-10-09T15:41:41Z
        -> ZERO_CALLS_PROVEN  proof=NO_INVOCATION_IN_WINDOW
        matches null BY DESIGN: the filter runs only if a stream was active; none was

mail (per run ticket, no recipient inferred):
        TCK-20261011-61631267  WE_DL_UNCONFIGURED 1  WE_CLIENT_SENT 1
        TCK-20261011-7731261a  WE_DL_UNCONFIGURED 1
        WE_DL_SENT 0  -> no BLOCKING row owed

service log /aws/lambda/irpt-ycharts-generate, 08:12:32-08:42:32Z, 41 events:
        tokens present: INIT_START LATEST UNEXPECTED NOT_AUTHORIZED REPORT
                        MISSING_REQUEST_FIELD INVALID_INPUT
        NOT_READY: absent
        the only 2 reason-bearing events are census arms, both BEFORE the
        journey ticket's created_at 08:14:27.233Z  -> no reason for hop (d)

filer row: no Item (ABSENT), control 1 item
```

---

## Decisions Made

1. **Measured the CTO's pre-GO placement instead of accepting it.** The issuer placed the 06:22:18
   refusal at run 2's `census.arms[71]`; that arm records only `INVALID_INPUT`, and the token
   `MISSING_REQUEST_FIELD` appears in no census arm, so the trace alone could not close it. The service
   log did: one such event, its line carrying **both** tokens — the internal reason served as that public
   code.
2. **Did not retry hop (d) or submit again with another token.** Branch E and the amendment both forbid
   it. One run means one submission.
3. **Reported that branch E's second instruction has nothing to read, rather than substituting the
   served code for a service reason.** The served `NOT_READY` is recorded as served; the absence of a
   service-side reason is recorded as an absence, with the argument made so it does not depend on
   identifying hop (d)'s invocation.
4. **Did not claim the collision fix as a success beyond what it is.** The per-run token demonstrably
   worked — the tokens differ between runs and `CHANGED_INPUTS_SAME_REQUEST_ID` is gone. A *different*
   refusal replaced it. Both halves of that are stated.

---

## Files Modified

| File | Commit |
|------|--------|
| run-3 ledger + its `.open_deploys` row | this commit |
| `deliverables/r2_tr1/r2_tr1_run3_trace.json` (68822 B) | this commit |
| `TCKT_VNEXT.TO-RUN-R2-tr1...proof_of_spec.json` (third revision) | this commit |
| surprise channel: S32 | this commit |

---

## Blockers

None owed by this seat, and **no fourth run exists** — CTO AMENDMENT 3: "If run 3 stops short of hop (g),
the next act is the round's slug, not another GO."

The open question is the same one, one layer deeper: **why the submission is refused.** Run 2 said
`INVALID_INPUT` off an idempotency collision; that is fixed. Run 3 says `NOT_READY`, and the service
logs no reason for it. Answering it needs the handler's source for that path or a reason on the log
line — neither in this order's `<paths>`.

---

## Current State

Three runs, three outcomes: D (precheck stop), E (collision), E (`NOT_READY`). What is proven across
them is substantial and not nothing: the identity arms correctly, the clamp holds under census with
**zero off-list admits across 82 armed routes**, upload/ticket/claim all work for a one-firm internal
filer, the mail path refuses as configured, zero data-refresh calls is now **proven**, and the identity
is always removed after `exp`. What is unproven is the same single link each time — the submission is
refused, so no report is ever made and hops (e)–(g) have never run.

**The R2-rr-2 report-id shape check has still never been exercised live** in either direction, across
all three runs. It is not implicated in any of them.

---

## Next Steps

1. The round's slug, with rows S32 (no service reason for hop (d)) and the closures of S29, S30, S31.
2. AC2 to `3.0.0_SA_CVO` at L9 on the run-3 trace. Not self-graded.
3. No further run under this pair. A new pair would be a new cell.
