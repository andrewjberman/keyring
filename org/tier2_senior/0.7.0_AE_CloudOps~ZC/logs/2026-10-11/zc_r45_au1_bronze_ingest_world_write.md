# The r45 bronze ingest landed 12 new keys, and the one gate worth re-reading was the scheduled-task condition -- 0.7.0_AE_CloudOps~ZC

**archetype:** DEPLOY

**Date:** 2026-10-11
**Task Order:** AMGT_CORPUS.TO-WRITE-R45-au1.bronze-ingest-and-four-count-sitez
**Status:** COMPLETE on AC1-AC4; AC5 is the CVO's, the status flip and ledger close are the issuer's

Third log of the day. Continues `zc_amgt_corpus_r44_at4_read.md` and
`zc_three_crossbox_orders_ten_closed_a18_blocked.md`.

---

## Objective

The first WORLD-risk write this lane has run: land every file of every RESOLVED library folder the store
lacked into bronze, re-open every stored object, and read the four-count and census fresh. Guarded by a
signed never-widen pair and a four-rung STOP ladder.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| crossbox-call.py | `status/ack/close --id e8e0` | PASS | State read back after the act, not inferred. |
| comp-schedule | not run | SKIPPED | Order's preflight declares NOT-APPLICABLE: no task registered, run or edited; the one write is ad-hoc. |
| comp-iam | not run | SKIPPED | Order's preflight declares NOT-APPLICABLE and explicitly BLIND on the put right. Nothing changed a policy, role or credential, and `comp-iam` models `(action)` not `(action, resource)` -- it could not have answered whether this user may Put to these partitions. The order makes an AccessDenied STOP 3; none occurred. |
| comp-blast | not run | SKIPPED | Binds before infra changes. The act is additive write-once to new S3 keys under a signed blast radius; no infra changed. |
| au1_accounting.py | the AC2 grader, read before being fed | PASS | Reading it first mattered -- see Decisions. |

**What worked:** reading the grader's source before assembling the file it grades. It takes
`findall(...)[-1]`, so section ORDER decides which census it reads; assembling blind could have fed it
the before-census and produced a wrong `identity` verdict from correct data.

**What failed:** nothing this block.

**Gap found:** none.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | STOP 0 -- both halves, by path and author, on `origin/box/dell1` | CTO half author `1.0.0_SA_CTO~DELL1`, COO half author `2.0.0_SA_COO~C1`; CTO line 6 begins `**SIGNED**` |
| 1 | STOP 1 -- four blob hashes | ingest `d726b31065f3`, store `34b344de8ed1`, backlog `ec6830f630f3`, library `b37fb1452556` -- all MATCH |
| 2 | STOP 2 -- no ingest running | 0 of 69 python processes |
| 3 | before: `backlog --coverage-dry-run`, `library --census` | 102 folders, 378 files, 11 placeholders, 6 unresolved |
| 3a | STOP 4 -- `schtasks /query /fo LIST /v` | 295 blocks, `schtasks_named 1 dossier_writing 0` |
| 4 | `ingest --write`, once | rc=0, 09:55:12Z -> 09:59:50Z, 89,526 bytes of output |
| 5 | `ingest --verify` | `objects 368 files 368 match 368 mismatch 0` |
| 6 | after: both reads again | census 378 files, placeholders 11 -> 0 |
| 7 | `au1_accounting.py` | `census 378 resolved 368 unresolved 10 objects 368 identity OK` |
| 8 | `ingest_run.json` copied into evidence | left as the run left it, unstaged |
| 9 | commit the evidence file alone | `cc1f7b2dfa`, 555 lines |

## Verification

```
resolved_folders 96 files_in_resolved 368 stored 368 (put_performed 12 existed 356) read_failed 0
placeholders_before 11 hydrated_ok 11
unresolved_files 10 in 6 folders
objects 368 files 368 match 368 mismatch 0
au1 accounting census 378 resolved 368 unresolved 10 objects 368 identity OK
```

Branch A with the pair's expected Branch B remainder. The census identity holds: 378 = 368 + 10. The
store went 356 -> 368 objects; 12 conditional puts, nothing overwritten (write-once, sha-prefixed keys).

Graded on bytes proven identical to the commit (`git hash-object` of the worktree == `git rev-parse`
of `cc1f7b2dfa:<path>`, both `e9c856a86bc4`): **AC1 1, AC2 `identity OK` rc=0, AC3 2, AC4 1.** The
accounting grader was re-run on the FINAL file after steps 7-8 grew it, and a planted `stored 367`
negative control returns `identity BROKEN` rc=1 -- so `identity OK` is discriminating and not a
constant.

---

## The two judgment calls worth recording

### The scheduled-task condition was nearly a wrong-object read

The CTO half rules that the daily task writes no dossier, citing **`induction_run.py`**. The task's
action actually names **`induction_scheduled`** -- a different module. Two reasons not to take the
ruling at face value: the names differ, and the task's `Start In` is a **PINNED tree**
(`opal-pinned/amgt-induction-daily/7580fe909cf3`), so the bytes that run are not the bytes in this
worktree.

Read the pinned bytes. `induction_scheduled.py` matches none of
`dossier|continuation|substrate|write_one|bronze_put` and imports `induction_run`; the pinned
`induction_run.py` matches none either, and reaches only `induction_request`, `library`,
`add_security`, `crosswalk`. Positive control: the same grep returns 46 hits on `backlog.py`, and
`induction_run.py` is 765 lines with 20 defs, so the zero is not an empty-file artefact.

**The CTO's ruling holds** -- the wrapper imports the very module it examined. But it held for a reason
the half does not state, and a token match on a task string could never have shown that: this is the
transitive case the condition exists to catch.

### Two non-ASCII characters kept on purpose

The evidence carries exactly two: an EN DASH and an e-acute, both inside REAL library filenames in the
unedited `--write` output, on lines that name the S3 keys those files landed under. Stripping them would
edit an output the order requires whole AND misstate which drive file maps to which stored object.

CLAUDE.md allows two safe moves -- all non-ASCII out, or every reader explicit -- and forbids a subset
edit, because a default cp1252 read raises on only five undefined bytes and decodes the rest silently
wrong. This takes the second branch, and the readers were CHECKED rather than assumed: the only
programmatic consumer (`au1_accounting.py`) opens with `encoding="utf-8", errors="replace"`, and the
AC greps are ASCII-anchored and cannot match either line. The file carries a note saying all of this,
because the tempting fix is the destructive one.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Read `au1_accounting.py` before assembling the file it grades | It takes the LAST match of each pattern. Section order therefore decides which census it reads. Assembling blind risks a wrong verdict from correct data. |
| Never restate the `resolved_folders` line anywhere in the evidence | AC1 expects exactly 1. A helpful summary quoting it would have made it 2 and failed the criterion with correct numbers. |
| Read the PINNED bytes for the scheduled-task condition | The task runs from a pinned tree; the worktree copy is not what executes. |
| Keep the two non-ASCII characters | They are real filenames in output required verbatim; the rule's second branch covers it and both readers were verified explicit. |
| Capture each command to a file, then assemble | Keeps every output whole and unedited, and avoids a partially-written evidence file if a step fails. |
| Re-grade AC2 on the final bytes, with a negative control | Steps 7-8 grew the file after the first grading. An ungraded regrade would have been an assumption. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.7.0_AE_CloudOps~ZC/evidence/r45_au1_bronze_ingest_and_four_count_sitez.txt` | New -- 555 lines, 101,010 bytes | Yes -- `cc1f7b2dfa` (alone, per step 9) |
| `org/devices/crossbox/XB-20261011T093421Z-e8e0.json` | acked + closed to-side | pending commit at time of writing |
| `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/ingest_run.json` | rewritten by the module at its hard-coded path | **No -- deliberately left unstaged** per step 8; this lane cannot commit there and the issuer reconciles |

**World state changed by this seat:** 12 new S3 objects under
`s3://opal-data-harvest/amgt/harvest/bronze/research-report/security_key=*/`, additive and write-once.
No delete, no overwrite, no dossier, no schedule change, no vendor call. Rollback is none needed, as
the signed blast radius states.

---

## Blockers

None owned by this lane. Open and owned elsewhere: AC5 and the ledger close (`3.0.0_SA_CVO` / the
issuer), a18's routing (`2.0.0_SA_COO~T2`), and the from-side of thirteen half-closed crossbox calls
(dell1).

---

## Current State

`0.7.0_AE_CloudOps~ZC` is LIVE on site Z, watcher armed, TO queue empty. The r45 au-1/au-2 cells are
served: the bronze store went from 356 to 368 objects in 96 resolved folders, every object re-opens
(`mismatch 0`), the library's 378 files reconcile as 368 resolved plus 10 unresolved in 6 named folders,
and all 11 OneDrive placeholders hydrated on the read. Evidence `cc1f7b2dfa`, graded AC1-AC4 on the
committed bytes. Six commits stand on `box/sitez` from this session, all LOCAL -- `box/sitez` has one
writer and this seat is correctly refused -- and the integrator's window publishes them.

---

## Next Steps

1. **[`2.0.0_SA_COO~C1`] Close the ledger and flip the status** -- the order reserves both. Report
   delivered via `0.0.0_AB_MSTR~Z` at 10:12:24Z.
2. **[`3.0.0_SA_CVO`] Grade AC5** -- FWD-1 on the resolved-folder reading, with the 10-file remainder in
   6 folders named and the crosswalk/v1 identity matter riding a later round.
3. **[`2.0.0_SA_COO~C1`] Reconcile `ingest_run.json`** -- rewritten by the module, left uncommitted by
   design.
4. **[`1.0.0_SA_CTO~DELL1`] Consider restating the scheduled-task condition against `induction_scheduled`**
   -- the ruling is right, but it cites the module the task delegates to rather than the one it names,
   and the task runs from a pinned tree.
