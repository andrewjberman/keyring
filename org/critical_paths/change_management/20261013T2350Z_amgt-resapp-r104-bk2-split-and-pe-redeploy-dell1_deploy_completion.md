# Deploy Completion Record
**Date opened:** 2026-10-13T23:50:34.654420+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-bk-2: ONE code leg redeploying opal-amgt-scoped-api from the MERGED pin d7a79c766a (box/dell1 first-parent) carrying AMGT-bk-1 sub-phase lines and top-band reuse and AMGT-bk-4 derived fiscal P/E, scoped_amgt.py 84002d3fd559 -> 351f9a1d7a8a and _harvest_prefixes.py 71fbb35c01bb -> 0ea0b31ad6b9 loaded, thirteen others not loaded (fifteen members); live must read AaACnKtr.. first; only the PE_RATIO rows move; the first request after the apply is driven alone (r102_first_cold_request.py) and graded on the split; rollback is a REBUILD from merged pin c558bffbcc
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pin d7a79c766a read BY THIS SEAT in a DETACHED worktree; r94_admission_table.py d7a79c766a --pin c558bffbcc prints EXACTLY the fifteen members at the half's blobs (any other is a STOP before upload); live CodeSha256 read first and equal to AaACnKtr.. | outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK: REBUILD from merged pin c558bffbcc, blob table printed BEFORE the apply, plus the live package downloaded and hash-checked as a reference; sweep of every live worktree open deploys and the ledger | blob table + sha equality + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed BEFORE the build; source-map entry read BEFORE and compared with the live function | equal counts + the entry fields before |  | OPEN |
| L4 | verify | BUILD from the DETACHED worktree at EXACTLY the pin, whole content diff printed FIRST (changed members must be the half's two loaded members); r94_naming_replay.py --pin c558bffbcc on the BUILT ZIP with its denominator; snapshot generated_at printed | build sha + content-diff + blobs + replay denominator + stamp |  | OPEN |
| L5 | verify | PRE-ACT CAPTURES immediately before the apply: the 527-request timed route baseline and aw4_capture.py 95 names to .scratch_bk2/thesis_pre.json, in sequence, no other reader | capture counts bytes statuses durations |  | OPEN |
| L6 | activation | upload with read-back, untargeted plan graded from the plan JSON (one moving resource), safe-apply of the saved plan; CodeSha256 after differs from AaACnKtr.. | upload VersionId, plan denominator, apply output, CodeSha256 after |  | OPEN |
| L7 | verify | THE FIRST ACT AFTER THE APPLY: r102_first_cold_request.py driven alone for ASML_NA_Equity, before any capture or replay: RECORDED or NOT COLD (not repeated) | request id handler time Init Duration status phase lines |  | OPEN |
| L8 | verify | thesis capture after to .scratch_bk2/thesis_post.json and the timed route replay, single reader; compare against the baseline; only PE_RATIO rows moved | status moved, changed paths outside the table, r104_pe_delta verdict |  | OPEN |
| L9 | verify | criteria AC1 AC2 AC3 run once after the apply | each criterion output lines |  | OPEN |
| L10 | git | record step record-terraform-deploy.sh and the source-map entry printed after | entry after equal to the live CodeSha256 + commit hash |  | OPEN |
| L11 | verify | report to the issuer with the first cold request id handler time Init Duration phase and sub-phase lines; hold released; pin worktree left | the delivered message |  | OPEN |

## Log

- 20261013T235034Z OPENED by 0.7.0_AE_CloudOps~RA1 with 11 leg(s)
