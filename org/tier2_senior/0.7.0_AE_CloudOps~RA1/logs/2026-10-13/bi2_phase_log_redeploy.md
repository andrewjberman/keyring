# 0.7.0_AE_CloudOps~RA1 -- 2026-10-13 -- AMGT_RESAPP AMGT-bi-2: the overlay's phase log lines applied, first cold request recorded, no served byte moved

**Date:** 2026-10-13 (GO 15:50Z, msg 4926; STOP 15:57Z-16:07Z; apply 16:15:54Z; function LastModified 16:17:06Z; ledger closed after AC1-AC3)
**Task Order:** AMGT_RESAPP.TO-AMGT-bi-2.redeploy-the-scoped-api-carrying-the-phase-log-lines-from-a-merged-pin-and-drive-its-first-cold-request
**Status:** COMPLETE (AC1, AC2, AC3 PASS; ledger CLOSED 11 of 11; one STOP before the apply, ruled)

## Objective

One code leg of `opal-amgt-scoped-api` from the MERGED pin `6ecb5bc567`, whose intended change is `AMGT-bi-1`'s `lib/research/api/scoped_amgt.py`
(`9f72b58aa87e` -> `02627c18a0ea`): fourteen `AMGT_PHASE route=overlay` log lines. Log lines only; no served byte moves. The first request after the apply is driven
alone, so it is cold by construction, and its phase table attributes the cold overlay's roughly 20 s.

## The act
**archetype:** DEPLOY

1. Read the order, both halves and the GO. Live read `j+j1k5r7..` first. Detached worktree at the pin; `r94_admission_table.py 6ecb5bc567 --pin 7da642c1ff` printed
   the pair's eleven at their blobs; the replay from the pin read YES (35/78/16, 0 differ).
2. Printed the rebuild rollback's blob table (`7da642c1ff`), kept the live package as a hash-checked reference, re-hashed the wheels (6 of 6), read the source-map
   entry, swept 33 worktrees (498 entries).
3. Built offline: 408 files, **CHANGED 5**, not the table's four runtime members: `exemptions.json` (`bc909dc105ff` -> `ccaf6c9f3481`) was a fifth. **STOPPED before any
   upload**, filed row D1-S27 and the evidence file, reported to the issuer and the CTO. The admission tool diffs only two registry files.
4. CTO ADDENDUM 1 and COO ADDENDUM 1 admitted it; I proceeded from L4. Re-ran the CTO's replay on the built zip with a controlled import path (0 differ).
5. Captured the 527-request timed baseline and the 95 thesis payloads. A first upload attempt ran without the script's `AWS` variable and wrote nothing (the plan read
   53 no-op); repeated with it set. Uploaded with read-back, graded the untargeted plan from its JSON (1 of 53), applied the saved plan.
6. **First act after the apply:** `r102_first_cold_request.py` for `ASML_NA_Equity`: handler 20.566 s, Init 744 ms, `feed` 18,796 ms.
7. As the only reader: timed replay (status moved 0, clocks only), thesis capture and `ay4_compare` (95/95, growth 0), AC1, AC3 from the issuer's fixed instrument.
8. Hold released; record step; ledger closed.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| deploy_ledger.py | open, close-leg L1-L11, close | PASS | opened before the first live act |
| r94_admission_table.py / r94_naming_replay.py | at the pin; on the built zip | PASS | 11 listed; the build found 12 |
| build-and-upload-scoped-amgt.sh | --build-only | PASS | offline, 0 downloads |
| bf1_capture.py, aw4_capture.py, ay4_compare.py | timed baseline/replay; thesis | PASS | clocks only; growth 0 |
| r102_first_cold_request.py | first request after apply | RECORDED | cold, Init 744 ms |
| r102_phase_table.py (fixed @50566b47c1) | --id-file | YES | sums within 3 ms |

**What worked:** stopping on the build's own content diff rather than the admission tool's list; chaining the first cold request into the apply's own call so no
reader could precede it; grading the plan from JSON as a gate before the apply.
**What failed:** the first upload attempt (my missing `AWS` variable, nothing written, caught by the script's read-back refusal and the 53 no-op plan); my first
phase-table run read NO because of the issuer's instrument defect (fixed @50566b47c1), not the request; my first replay import-path control used `python -c`, whose cwd
is first on the path, so it loaded the worktree's module (discarded, redone with a wrapper that printed the loaded file).
**Gap found:** `r94_admission_table.py` lists a fixed two registry files; the issuer fixed it in the addendum.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Stopped on a member the table did not name though the admission tool read 11 | GO condition 1 and bound 6: any other member is a STOP; the build's diff is the authority on what ships |
| Chained apply and the cold request in one call | GO condition 6: before any capture, replay or other reader |
| Re-ran AC3 from the fixed instrument and said so | the first run's NO was an instrument defect, recorded in the ledger and the instance |

## Files Modified

- `org/critical_paths/change_management/20261013T1553Z_amgt-resapp-r102-bi2-phase-log-redeploy-dell1_deploy_completion.md` (CLOSED)
- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/` the first-cold-request file, the derived compare report, the STOP evidence, the proof instance
- `infra/aws/lambda/ci/lambda-source-map.json`, `infra/aws/terraform/harvest/CHANGELOG.json` (record commit d369f9a90a)
- the order's `<status>` (complete); surprise row AMGT_RESAPP-D1-S27
- local only, uncommitted: `.scratch_bi2/thesis_pre.json`, `.scratch_bi2/thesis_post.json`

## Next Steps

1. `[2.0.0_SA_COO~R1]` Re-read the phase table from request `4737aa2a-fb3f-4092-84d8-42cfabfc8a8a`; feed is 18,796 ms of 20,338 ms.
2. `[2.0.0_SA_COO~R1]` Remove the pin worktree `C:/tmp/bi2-build` and `C:/tmp/bi2-zip-root` (a recursive deletion is the user's).
3. `[box-sync / MSTR]` Integrate the local commits.
