# The submission was accepted; the report never became ready — 0.7.0_AE_CloudOps~TV2

**archetype:** VALIDATE

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-RUN-R3-tr1.fwd1-fourth-run-tv2 (GO `2681fcca32`, AMENDMENT 1 `c3f18e39ac`)
**Status:** COMPLETE — branch C; `complete` means the act is finished, **not** that FWD-1 is realized

---

## Objective

Run the FWD-1 journey once more under a new round-3 pair with the runner at `83b4f0c597`, which reads an
accepted submission by state and identity, then finish the cleanup in two steps — the identity row lives
two hours after an accepted submission. Cell `R3-tr-1`.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open --window-hours 4` (4 legs), `close-leg` x4, `close` | PASS | L3 held OPEN across the two-hour wait, closed only on my own ABSENT read |
| fwd1_run.py @83b4f0c597 | ONE invocation, then ONE `--finish-cleanup` | PASS | **rc 3** then **rc 0**; never interrupted; no early cleanup, so no rc 4 in the record |
| r3_checks.py | `rn-row`, `rn-regress` | PASS | 6/6 and 56 (min 56) failed=0 |
| clamp_precheck.py | `--out …/r3_tr1/clamp_precheck_table.json` | PASS | `READ27 27/27` — AC1 |
| aws dynamodb get-item | the filer row 3x (`--consistent-read`), each with a control | PASS | ABSENT → PRESENT → ABSENT |
| aws logs filter-log-events | `WE_` over the ticket api across `iat..exp` | PASS | `WE_DL_SENT` 0 |
| background waiter | until-loop on `row_delete_not_before_unix` | PASS | fired 13:19:46Z — the act ran on its own signal, not a watcher tick |

**What worked:** arming a waiter on the trace's own `row_delete_not_before` instead of hoping a 30-minute
watcher tick landed on the right side of the boundary. The second step then ran 46s into its window.

**What failed:** nothing in execution. **My own omission:** I closed the ledger and reported but filed no
proof instance and no session log. The GO named no closing step and I didn't notice it was missing —
AMENDMENT 1 is the issuer catching it, and this log is part of the repair.

**Gap found:** none new. The run **resolves** my earlier row S32.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Ledger (4h window), then the union at `11:10:32Z` | **51 trees** (enumerated 51 == grepped 51) over **five** STOP names incl. the resident; 23 distinct, all closed but mine; `irpt-resident-st30` CLOSED, consistent with condition 1 |
| 1 | Pin + checks | `8f9e6ec5…59d6` on three reads (HEAD blob, working file, pin blob), 0 dirty — a **third** distinct runner for this journey; `rn-row` 6/6, `rn-regress` 56 |
| 2 | Prechecks, re-taken live | `READ27 27/27`; `irpt-status` `Iw3FADFr` (moved from run 3's `6idtFvAm`, as warned); ticket `t1EoiJRZ`; `DL_MAP` 0 keys; filer row ABSENT; st30 output read green at root `37210c771a-st30` |
| 3 | THE RUN | **rc 3**; row written 11:17:00Z, token exp 11:47:00Z (30 min) |
| 3a | Hops | (a) NORMALIZED on poll 2 · (b) `TCK-20261011-e1947e12` 201 · (c) 200 · **(d) ACCEPTED, `REQ-59aa6803901f371b27ffa176`, QUEUED** · (e) **NOT_READY at its 40-poll bound** · (f)(g) UNREACHABLE |
| 4 | After-reads | zero-call PROVEN; mail counts; row PRESENT by my own read |
| 5 | REPORT NOW | sent at 12:01Z without waiting the two hours, as step 5 directs |
| 6 | Second step | `--finish-cleanup` at **13:19:46Z**, rc 0; my own read ABSENT; ledger CLOSED 4/4 |
| — | AMENDMENT 1 | proof instance + this log + `complete` |

## Verification

```
hop (d) ACCEPTED -- the journey's first pass of the submission in four runs
  status 200  status_state QUEUED  status_public_reason_code NOT_READY
  data.identity.request_id  REQ-59aa6803901f371b27ffa176
  request_id_source submission_answer   accepted_state QUEUED
  submitted_at 2026-10-11T11:19:00Z
  key lists (CTO condition 4): answer_keys 6, data_keys [identity, stage], status_keys 5

hop (e) NOT_READY at its bound
  40 polls 30s apart, every one http 200, last_code NOT_FOUND, last 11:38:55Z
  job_last_read {NOT_READY, 40, 11:38:55Z}
  (f)(g) UNREACHABLE; report_route_arms {} -- the R2-rr-2 arms unexercised again

one firm only          82 armed | off_list_admits [] | 74 refused arms | 0 leaks | 0 UNKNOWN
row after its window   written 11:17:00Z | exp 11:47:00Z | deleted 13:19:46Z
                       ABSENT by two readers, each against a control of 1 item
zero-call              ZERO_CALLS_PROVEN NO_INVOCATION_IN_WINDOW, read at exp+300s
mail                   WE_DL_UNCONFIGURED 2, WE_CLIENT_SENT 1, WE_DL_SENT 0

the issued id against my own R2-rr-2 check:
  REQ-59aa6803901f371b27ffa176 fullmatches REQ-[0-9a-f]{24}
  the R2-rr-2 CTO half had this "inferred from the reader, not measured".
  One MEASURED instance now -- one instance, not a census, and obtained
  without calling the report route.
```

---

## Decisions Made

1. **Checked that a fourth run was legitimate before accepting it.** The round-2 CTO half said "No fourth
   run under this half." This order is cell `R3-tr-1` under its *own* signed pair, which states the
   round-2 pair is spent. The prohibition is respected, not worked around.
2. **Did not claim run 3's diagnosis as mine.** The issuer's corrected runner is what showed that run 3's
   `NOT_READY` was an accepted-and-queued *status*, not a refusal — which is why run 3's service log held
   no refusal reason, the anomaly I filed as **S32**. I flagged the right thing and passed the old
   runner's "refusal" framing through; the explanation is the issuer's.
3. **Armed a waiter rather than trusting the clock.** The two-hour boundary mattered: too early and the
   runner refuses, too late and the row narrows longer than signed for.
4. **Held the next order (`R3-rf-2`) for twelve minutes** rather than starting it before this ledger
   closed — its ordering condition is this cleanup.
5. **Wrote AC2 as `UNVERIFIABLE-BY-INSTRUMENT`, not a verdict.** The CVO graded it NOT MET at
   `5126c19d7a`; I cite that and write neither PASS nor FAIL myself.

---

## Files Modified

| File | Commit |
|------|--------|
| `deliverables/r3_tr1/r3_tr1_run4_trace.json`, `clamp_precheck_table.json`, ledger | `80c082777f` then `1060619ce4` |
| proof instance, this log, TO status | this commit |

---

## Blockers

None owed by this seat. For `2.0.0_SA_COO~G2`'s job-state read: from 13:19:46Z the trace's known limit
applies — a generation starting later than two hours finds no PROFILE row and ends ATTENTION
`ACTOR_NOT_FOUND`. Expected, not a new defect.

---

## Current State

Four runs, four outcomes: **D** (precheck stop), **E** (idempotency collision), **E** (`NOT_READY`
misread as a refusal), **C** (accepted, report never ready). Each cause was real and was fixed in turn,
which is why the branch moved each time.

What is proven across them: the identity arms and clamps, zero off-list admits across 82 armed routes,
upload/ticket/claim all work for a one-firm internal filer, the mail path refuses as configured, zero
data-refresh calls, the two-step row lifetime, and now **an accepted submission with a conforming issued
id**. What remains unproven is the last link only: no report has ever been generated, so hops (e)–(g)
have never completed and **FWD-1 is not realized**.

---

## Next Steps

1. `2.0.0_SA_COO~G2` reads the job state for `REQ-59aa6803901f371b27ffa176`.
2. The round's slug. A fifth run needs a new pair.
