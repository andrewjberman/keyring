# 0.7.0_AE_CloudOps~RA1 -- 2026-10-13 -- AMGT_RESAPP AMGT-ar-3: the scoped API carries the AI-fill serve; `ai_fill` served for three names, cold request 2,986 ms

**Date:** 2026-10-13 ET (GO 01:15Z, msg 5334; pre-capture 01:22Z; apply 01:23:38Z-01:24:54Z; function LastModified 01:24:49Z)
**Task Order:** AMGT_RESAPP.TO-AMGT-ar-3.the-scoped-api-carries-the-ai-fill-serve-and-its-first-cold-request-is-driven-alone
**Status:** APPLIED AND VERIFIED; AC1 (YES 8 of 8) and AC2 PASS; ledger CLOSED 11 of 11

## Objective

One code leg of `opal-amgt-scoped-api` from the MERGED pin `0447f2df38`: `scoped_amgt.py` `351f9a1d7a8a` -> `1f5de89912e5` (the `/thesis` body gains the key `ai_fill`, served from
the stored document by one S3 GET); seven `lib/research/aifill` modules differ in the tree and are not packaged. The grant (`AMGT-ar-1`) is live; 95 documents stored.

## The act
**archetype:** DEPLOY

1. Read the order and the GO. Live `Wkt48Y6v..` first. Detached worktree `C:/tmp/ar3-build` at the pin; `r94_admission_table.py 0447f2df38 --pin d7a79c766a` printed EIGHT members at the
   half's blobs; `check_ar1_grant.py` YES; the stored AMD document exists (12,673 bytes). Opened the 11-leg ledger entry. Rollback blob table (`d7a79c766a`), live package kept as a
   hash-checked reference, wheels 6 of 6, source-map entry current, 25 worktrees swept.
2. Built offline: 408 files, CHANGED 1 (`scoped_amgt.py`, blob recomputed from the zip), ADDED 0, no aifill module in the package. Naming replay on the built zip: 35/68/16, 0 differ.
3. Captured the three names before the apply; uploaded with read-back; graded the untargeted plan (1 of 53); applied the saved plan through `safe-apply`.
4. **First act after the apply:** `r102_first_cold_request.py` for `ASML_NA_Equity`: handler 2,985.71 ms, Init 654.45 ms, request `8d3bfc93-9a13-4d66-916a-716d962a9181`.
5. As the only reader: AC1 (`AIFILL AR-3 SERVED: YES (8 of 8)`), AC2 (R97, R95, R94 YES). Hold released at 01:29Z. Record step `809521d220`.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L11, close | PASS | opened before the first live act; no early close this time |
| r94_admission_table.py / r94_naming_replay.py | at the pin; on the built zip | PASS | 8 members; 35/68/16, 0 differ |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, CHANGED 1 of 408 |
| check_ar3_aifill_served.py | capture (pre), verify (AC1) | PASS | 3 names; 8 of 8 arms |
| r102_first_cold_request.py | first request after apply | RECORDED | cold, Init 654.45 ms |
| r97 / r95 / r94 checks | AC2 | PASS | exit=0 |

**What worked:** applying the bk-2 lessons (extract only lib/ and infra/ for the replay; create output directories first; capture well clear of 00:00Z).
**What failed:** nothing.
**Gap found:** the cold handler read 2,985.71 ms against bk-2's 2,910.88 ms (+75 ms); no overlay read was added, so I read it as one container's variance and filed no row.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| No row for the +75 ms | the order asks for a row only if the request shows a worsening of the split; feed fell 11 ms and fixed phases moved under 40 ms |
| Did not push | commits stay LOCAL |

## Files Modified

- `org/critical_paths/change_management/20261014T0118Z_amgt-resapp-r104-ar3-aifill-serve-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the first-cold-request file and the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit `809521d220`)
- the order's `<status>` (complete)
- local only, uncommitted: `.scratch_ar3/thesis_pre.json`

## Next Steps

1. `[2.0.0_SA_COO~R2]` Read the read-back and route it onward; remove the pin worktree `C:/tmp/ar3-build` and `C:/tmp/ar3-zip-root` (a recursive deletion is the user's).
2. `[box-sync / MSTR]` Integrate the local commits.
