# The ticket's creator can now record its own report id, once — 0.7.0_AE_CloudOps~TV2

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** TCKT_VNEXT.TO-APPLY-R3-rf2.creator-records-report-code-dell2 (read at `19b02b2971`)
**Status:** COMPLETE — branch A, 6 of 6 legs, deploy recorded, AC1 `READ27 27/27` on the new build

---

## Objective

Deploy `opal-ticket-api` at `8ef21584f8` so `POST /api/scoped/tickets/{ticketId}/report` admits the
ticket's **creator** — once, on its own non-completed analysis-request ticket that carries an attachment
and has no report recorded — then record the deploy. Cell `R3-rf-2`.

**This apply widens a writer.** Both halves say so in those words, and so does this log.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | `open` (6 legs) + 6x `close-leg` + `close` | PASS | opened before any AWS read; row read back ABSENT against a 22-row control |
| safe-apply.sh | `-chdir=… apply <planfile>` | PASS | **no `MSYS_NO_PATHCONV=1`** — every gate limb evaluated |
| terraform plan / replan | `-out=<planfile>`, then plan | PASS | branch A; replan `No changes.` |
| build-and-upload.sh | `BUILD_ONLY=1` then the real run | PASS | identical content hash both times |
| record-terraform-deploy.sh | `ticket-center --function opal-ticket-api --author …` | PASS | **both halves in one commit** → STOP 3 did not fire |
| clamp_precheck.py | `--out …/r3_rf2/clamp_precheck_table.json` | PASS | `READ27 27/27`, ticket host CLAMPED on `dc0cd973` |
| aws lambda get-function + download | live package before and after | PASS | `cf10e19e` → `dc0cd973`, both by content |

**What worked:** the order's own joint test. AC1 can only pass if *both* the apply and the record landed,
so one command proves the pair. That is row S28's remedy doing real work for the second time today.

**What failed:** nothing. Four recorder gates WARNed that they checked nothing or could not decide; those
are recorded as WARNs, not cited as validation.

**Gap found:** none new. Row S40 (another seat's) stays open — see Blockers.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| — | **Ordering condition** | the fourth run's entry reads `closed-by 1060619ce4` (my own close) and its row was deleted 13:19:46Z, absent by two readers. The order arrived 13:07Z; I read both halves during the wait and **started no AWS call** until the gate lifted |
| 0 | Ledger, then the union at `13:25:39Z` | **57 trees** (enumerated 57 == grepped 57), 36 ticket rows, 9 distinct; only this entry open, and the eight closed ones are all mine from today |
| 1 | STOP 1 | 0 changed paths vs a **179** control; 0 dirty; shipping file `dc0cd973…` |
| 2 | STOP 2 | live package: 1 member `cf10e19e…`, package b64 == live `CodeSha256` → the object read IS the running artifact (my own R2-pk-2 build) |
| 3 | BEFORE | `t1EoiJRZ…`, 8 env keys, ItemCount 25, control ticket 23 attrs / open / NULL / svc-commentary |
| 4 | Build + upload | version `rWw.Gz93epEfpyXC__5Sbn1EdLMkRMY4`, 29696 B; downloaded back: 1 member `dc0cd973…`, no `tests/` |
| 5 | Plan, then ONE safe-apply | `0 to add, 1 to change, 0 to destroy`; `Apply complete! 0 added, 1 changed, 0 destroyed` |
| 6 | Five after-reads | all pass — see Verification |
| 7 | **RECORD** + STOP 3 | `40a13c5638`: map entry **and** reconcile line in the SAME commit → both halves landed |
| 8 | AC1 on the new build | `READ27 27/27`, `opal-ticket-api 6 2026-10-11T13:34:27 dc0cd973 CLAMPED` |
| 9 | Close, report once | ledger CLOSED 6/6; deployed hash reported first |

## Verification

```
(a) CodeSha256 20v0+vfeQjbJfs4kuCwA7IzjYm95aZg8vv3Lzv9GkWQ=  == uploaded zip
    deployed package re-downloaded from Code.Location:
      members: 1 ['lambda_function.py']
      deployed member : dc0cd973c61f4b037e7181f4675ec8ffe2ec68414cfd9e036c01f4096f386a15
      required (pin)  : dc0cd973c61f4b037e7181f4675ec8ffe2ec68414cfd9e036c01f4096f386a15
    LastModified 2026-10-11T13:34:27Z | runtime/timeout/memory unchanged

(b) env  8 / 8 | key names identical: True | VALUES identical: True

(c) POST .../tickets/TCK-20261009-a1052909/report (no auth) -> HTTP 401
    control GET /api/scoped/tickets -> 401 (proves reachability, and ONLY that --
    the authorizer fronts the whole /api/scoped prefix, so this says nothing
    about the creator branch, which sits behind it)

(d) ItemCount 25, TableSizeBytes 31538 -- unchanged
    control ticket 23/23 attributes, WHOLE ITEM identical -> no ticket written

(e) No changes. Your infrastructure matches the configuration.

STOP 3 -- both halves of the record, in ONE commit 40a13c5638:
    half 1  map entry artifact_sha256 20v0+vfe... == live CodeSha256
            last_deployed_commit 8446fdfa05  last_deployed_at 13:38:16Z
    half 2  reconcile line appended (deployed_commit 010d40d7..., ts 13:38:25Z)
    + CHANGELOG 36 lines. Exactly three files: the recorder's declared pathspec.
    map entries 235 before / 235 after, 0 added, 0 removed, 1 CHANGED (counted)

the mis-stamp check this order did NOT ask for, run anyway:
    stamped 8446fdfa05 is the R3-rf-1 worker build commit (+46/-10 handler,
    +180 test file); ITS lambda_function.py == dc0cd973... == the deployed file.
    I deployed from the drain merge 8ef21584f8 -- a different commit, same
    handler bytes. Agreement BY CONTENT, not by luck of naming.
```

---

## Decisions Made

1. **Held the apply for twelve minutes rather than starting early.** The order landed at 13:07Z with an
   ordering condition pointing at my own unfinished cleanup. I read both halves during the wait — that is
   free — but opened no ledger and made no AWS call until the fourth run's entry read closed. Starting
   early is precisely the overlap on one function the condition exists to prevent.
2. **Proved the ordering condition instead of asserting it from memory of my own work.** The STOP-0 union
   reads the fourth run's entry `closed-by 1060619ce4`, my own commit. My having done it is not evidence;
   the record is.
3. **Recorded that this widens a writer, in the log and the ledger.** "Code only" describes the plan's
   shape, not the act's effect. An apply that adds a writer to a route deserves the sentence.
4. **Ran the mis-stamp content read the order didn't ask for.** `TO-RECORD-R3-sm1` made it step 5(b); here
   it is unasked. It is the one failure a green recorder can still produce, and it costs one `git show`.
5. **Did not ride `MSYS_NO_PATHCONV=1`.** Fourth ticket apply in a row under that ban, which started as my
   own lapse on R2-rr-2.
6. **Carried the binding gap rather than closing or burying it.** See Blockers.

---

## Files Modified

| File | Commit |
|------|--------|
| source map, reconcile audit log, `ticket-center/CHANGELOG.json` | `40a13c5638` (by the recorder) |
| rf2 ledger + its `.open_deploys` row, proof_of_spec, this log, AC1 table, TO status | this commit |

---

## Blockers

None owed by this seat. **One gap carried, and it is another seat's:** the creator's write is **unbound**.
Every reader of these tickets is internal and may already open any request
(`interactive_access.py:115-116`), so a creator recording another person's request id widens no *access* —
but it can make its own ticket show a report that is not that ticket's. The binding (the report read
refused when the request's stored `ticket_id` differs) is `2.0.0_SA_COO~Y2`'s cell, and row
**TCKT_VNEXT-D2-S40** stays open against it. The CTO signed on that basis in words.

Also carried, per CTO condition 3: two creator refusals carry no `code` yet; the next cell touching the
route adds them, and the half says that is not a hold.

---

## Current State

The creator branch is live and verified by content against the pinned build input, the source map
describes it, and the clamp precheck reads the new build CLAMPED. Env, table and control ticket all
untouched; rollback retained as a non-latest S3 version.

**The branch has no live exerciser today.** No product path calls the route as a creator — the CTO's
pre-apply read placed `recordTicketReport` in one call site, the assignee's path. So the widening is real
in the bytes and dormant in practice until `2.0.0_SA_COO~Y2`'s portal cell lands.

---

## Next Steps

1. `2.0.0_SA_COO~Y2`'s binding cell, which closes row S40 and is the gate on this widening being safe to
   exercise.
2. AC2 — this order has none; AC1 is its only criterion and it passes. The CVO grades the round.
