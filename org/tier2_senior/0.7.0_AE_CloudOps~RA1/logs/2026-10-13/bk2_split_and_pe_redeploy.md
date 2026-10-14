# 0.7.0_AE_CloudOps~RA1 -- 2026-10-13 -- AMGT_RESAPP AMGT-bk-2: the sub-phase lines, the top band's reuse and the derived fiscal P/E applied; split YES, cold request 2,911 ms; AC2 FAIL on its instrument

**Date:** 2026-10-13 ET (GO 23:43Z, msg 5282; captures 23:58-00:03Z; apply 00:06:02Z-00:07:13Z; function LastModified 00:07:07Z; replay 00:08-00:12Z)
**Task Order:** AMGT_RESAPP.TO-AMGT-bk-2.redeploy-the-scoped-api-carrying-bk-1-and-bk-4-from-a-merged-pin-and-drive-its-first-cold-request
**Status:** APPLIED; AC1 and AC3 PASS, AC2 FAIL (r104_pe_delta.py prints NO); ledger CLOSED 11 of 11; the order is NOT flipped to complete

## Objective

One code leg of `opal-amgt-scoped-api` from the MERGED pin `d7a79c766a`: `AMGT-bk-1` (sub-phase log lines, top band reusing the feed's rows) and `AMGT-bk-4` (the served fiscal
P/E is `PX_LAST / IS_EPS` of the same year), fifteen members differing, two loaded (`scoped_amgt.py` `84002d3fd559` -> `351f9a1d7a8a`, `_harvest_prefixes.py`
`71fbb35c01bb` -> `0ea0b31ad6b9`). The first request after the apply is driven alone and graded on the split (T6, T7).

## The act
**archetype:** DEPLOY

1. Read the order, both halves and the GO. Live `AaACnKtr..` read first. Detached worktree `C:/tmp/bk2-build` at the pin; `r94_admission_table.py d7a79c766a --pin c558bffbcc` printed
   FIFTEEN members at the half's blobs. Opened the 11-leg ledger entry. Rollback blob table (`c558bffbcc`) printed, live package kept as a hash-checked reference, wheels 6 of 6,
   source-map entry read, 26 worktrees swept.
2. Built offline: 408 files, CHANGED 2 (the two loaded members, blobs recomputed from the zip), 0 downloads. Naming replay on the built zip's lib/ and infra/: 35 requests, 68 builder
   calls, 16 distinct, 0 differ. Snapshot stamp 2026-10-13T12:30Z (today's write).
3. Captured the timed baseline (528 requests, 23:58:35Z-00:02:49Z) and the 95 thesis payloads; uploaded with read-back; graded the untargeted plan from its JSON (1 of 53); applied the
   saved plan through `safe-apply`.
4. **First act after the apply:** `r102_first_cold_request.py` for `ASML_NA_Equity`: handler 2,910.88 ms, Init 675.26 ms, request `26780d80-43c1-4c36-8827-693d9e4ae6b7`.
5. As the only reader: timed replay, thesis capture, AC1, AC2, AC3; the hold was released at 00:26Z. Record step `4f6b15aef0`.

## Findings (rows D1-S28, D1-S29)

- **AC2 cannot read YES on its own captures.** `r104_pe_delta.py` compares `check_face` whole and counts served/withheld from `model.fiscal_year_figures`, which `aw4_capture.py` does not
  keep: it printed 69 per-name DIFF lines, `served 0 withheld 0`, `NO`. The half's own normalization on the same captures: P/E rows 618 -> 464 (154 withheld), 154 `fiscal_unresolved`
  entries added, row count consistent on 29 names, 0 other differing paths over 95 names.
- **My baseline straddled 00:00Z.** I started it 85 s before the UTC date change. 2,596 overlay paths differ for that reason (date-driven); the old pin's handler run locally against the
  live pool differs from the live function on 0 non-noise paths over all 174 pre-midnight name requests. The 354 post-midnight requests: 0 name-class paths. I mistakenly closed ledger
  leg L6 with the text `PENDING` before the apply; its proof was replaced after the apply and says so.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L11, close | PASS | opened before the first live act; L6 closed early by mistake, corrected in the text |
| r94_admission_table.py / r94_naming_replay.py | at the pin; on the built zip | PASS | 15 members; 35/68/16, 0 differ |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, 0 downloads, CHANGED 2 of 408 |
| bf1_capture.py, aw4_capture.py | timed baseline/replay; thesis | PASS | 528 requests; 95/95 |
| r102_first_cold_request.py | first request after apply | RECORDED | cold, Init 675.26 ms |
| r104_split_table.py | --id-file ... --handler-max-ms 3000 | YES | T1-T7 PASS; target line MET (2,911 ms) |
| r104_pe_delta.py | thesis_pre.json thesis_post.json | NO | instrument mismatch, row D1-S28 |

**What worked:** the build's own content diff as the authority (two members, both named); chaining the first cold request into the apply's call; a control against the old pin's
handler to separate the date change from the code.
**What failed:** the AC2 instrument against its own captures; my capture start time near midnight UTC; the `PENDING` probe closing L6.
**Gap found:** the 3.6 s the issuer and CTO expected was 2.9 s on this request (one request, one container; not a trend).

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did not roll back | Branch 2 names a changed served value outside the P/E; the supplement reads 0 other paths and the date-driven paths read 0 against the old code |
| Did not flip the order to complete | the order: complete only if every criterion PASSES; AC2 prints NO |
| Did not amend AC2 | the criteria are the issuer's; the supplement sits beside the literal result |
| Did not push | commits stay LOCAL; origin `box/dell1` read by ls-remote |

## Files Modified

- `org/critical_paths/change_management/20261013T2350Z_amgt-resapp-r104-bk2-split-and-pe-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the first-cold-request file, the derived compare report, the proof instance
- `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md` (rows D1-S28, D1-S29)
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit `4f6b15aef0`)
- local only, uncommitted: `.scratch_bk2/thesis_pre.json`, `.scratch_bk2/thesis_post.json`

## Next Steps

1. `[2.0.0_SA_COO~R1]` Decide AC2 (amend the instrument or rule on the supplement), disposition rows D1-S28 and D1-S29, and the order's status.
2. `[1.0.0_SA_CTO~DELL1]` Read the split: feed.imports 782 ms and feed.snapshot 593 ms (feed 1,376 ms), peers.numeric_tickers 502 ms (peers 735 ms).
3. `[2.0.0_SA_COO~R1]` Remove the pin worktree `C:/tmp/bk2-build` and `C:/tmp/bk2-zip-root` (a recursive deletion is the user's).
4. `[box-sync / MSTR]` Integrate the local commits.
