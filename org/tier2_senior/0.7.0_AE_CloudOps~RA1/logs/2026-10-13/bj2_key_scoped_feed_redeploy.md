# 0.7.0_AE_CloudOps~RA1 -- 2026-10-13 -- AMGT_RESAPP AMGT-bj-2: the key-scoped feed read applied, no served byte moved, first cold request 3,770 ms (target NOT MET)

**Date:** 2026-10-13 (GO 18:41Z, msg 5063; captures 18:48-18:53Z; apply 18:55:15Z; function LastModified 18:56:24Z; ledger closed after AC1-AC3)
**Task Order:** AMGT_RESAPP.TO-AMGT-bj-2.redeploy-the-scoped-api-carrying-the-key-scoped-feed-read-from-a-merged-pin-and-drive-its-first-cold-request
**Status:** APPLIED; AC1 and AC2 PASS, AC3 FAIL (R103 COLD TARGET: NOT MET); ledger CLOSED 11 of 11; the order is NOT flipped to complete

## Objective

One code leg of `opal-amgt-scoped-api` from the MERGED pin `c558bffbcc`, whose one change is `AMGT-bj-1`'s `lib/research/api/scoped_amgt.py`
(`02627c18a0ea` -> `84002d3fd559`): the overlay's news card and top band read the subject's `article_security_mention` rows by key and by column, not the whole table.
No served byte moves. The first request after the apply is driven alone, after the day's 12:30Z snapshot write, and graded against 3,000 ms of handler time.

## The act
**archetype:** DEPLOY

1. Read the order, both halves and the GO. Live read `bKCGUhXp..` first. Detached worktree at the pin; the corrected `r94_admission_table.py c558bffbcc --pin 6ecb5bc567`
   printed ONE member at the half's blobs.
2. Printed the rebuild rollback's blob table (`6ecb5bc567`), kept the live package as a hash-checked reference, re-hashed the wheels (6 of 6), read the source-map entry,
   swept 22 worktrees (315 entries).
3. Built offline: 408 files, CHANGED 1 (`scoped_amgt.py`), no registry member, zip member byte-equal to `git show c558bffbcc`.
4. Re-ran the CTO's replay on the built zip with a controlled import path (35 requests, 78 builder calls, 16 distinct, 0 differ). Printed the snapshot stamp: generated_at
   2026-10-13T12:30Z (today's write), so the request is graded.
5. Captured the 527-request timed baseline and the 95 thesis payloads; uploaded with read-back; graded the untargeted plan from its JSON (1 of 53); applied the saved plan.
6. **First act after the apply:** `r102_first_cold_request.py` for `ASML_NA_Equity`: handler 3,769.92 ms, Init 533.51 ms, feed 1,776 ms (47.1 percent), peers 1,001 ms.
7. As the only reader: timed replay (status moved 0, clocks only, 0 over 20 s), thesis capture and `ay4_compare` (95/95, growth 0), AC1, AC3 with `--handler-max-ms 3000`.
8. Hold released; record step; ledger closed.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L11, close | PASS | opened before the first live act |
| r94_admission_table.py / r94_naming_replay.py | at the pin; on the built zip | PASS | 1 member; 0 differ |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, 0 downloads, CHANGED 1 |
| bf1_capture.py, aw4_capture.py, ay4_compare.py | timed baseline/replay; thesis | PASS | clocks only; growth 0 |
| r102_first_cold_request.py | first request after apply | RECORDED | cold, Init 533.51 ms |
| r102_phase_table.py (fixed @50566b47c1) | --id-file ... --handler-max-ms 3000 | YES / NOT MET | sums within 2 ms; handler 3,770 ms |

**What worked:** reading the build's own content diff as the authority (one member, no registry member) after round 102's STOP; chaining the first cold request into
the apply's own call; pulling the request's `AMGT_SEGMENT` lines from its log stream between START and REPORT for round 104.
**What failed:** nothing in the act. Two shell calls aborted on a quoting error (nothing ran); the proofs were then passed from a script file.
**Gap found:** the target (3,000 ms) was missed by 770 ms: feed fell from 18,796 ms to 1,776 ms but peers (1,001 ms) and the fixed phases keep the handler near 3.8 s.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not flip the order to complete | the order: "Flip complete only if every criterion PASSES"; AC3 reads a failing criterion with numbers |
| Left the apply in place | the order's AMENDMENT 1 and the CTO half: a miss does not roll back; no served byte moved |
| Recorded AC3 as FAIL with status_reason in the instance | the numbers decide; the checker reads VALID with a stated reason |

## Files Modified

- `org/critical_paths/change_management/20261013T1842Z_amgt-resapp-r103-bj2-key-scoped-feed-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the first-cold-request file, the derived compare report, the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit 1aa6ce55fa)
- the order's `<status>` (applied; not complete)
- local only, uncommitted: `.scratch_bj2/thesis_pre.json`, `.scratch_bj2/thesis_post.json`

## Next Steps

1. `[2.0.0_SA_COO~R1]` Decide the order's status and route the miss to the CTO's round-104 analysis with the numbers above.
2. `[2.0.0_SA_COO~R1]` Remove the pin worktree `C:/tmp/bj2-build` and `C:/tmp/bj2-zip-root` (a recursive deletion is the user's).
3. `[box-sync / MSTR]` Integrate the local commits.
