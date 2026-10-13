# Deploy Completion Record
**Date opened:** 2026-10-13T18:42:49.766340+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-bj-2: ONE code leg redeploying opal-amgt-scoped-api from the MERGED pin c558bffbcc (box/dell1 first-parent) carrying AMGT-bj-1's key-scoped feed and news-card read, lib/research/api/scoped_amgt.py 02627c18a0ea -> 84002d3fd559 (the only member); live must read bKCGUhXp.. first; no served byte moves; the first request after the apply is driven alone (r102_first_cold_request.py) and graded against 3,000 ms; rollback is a REBUILD from merged pin 6ecb5bc567
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the pin read BY THIS SEAT in a DETACHED worktree: c558bffbcc is a box/dell1 first-parent commit; r94_admission_table.py c558bffbcc --pin 6ecb5bc567 prints EXACTLY ONE member, scoped_amgt.py 02627c18a0ea -> 84002d3fd559 and no registry member (any other is a STOP before upload); the live CodeSha256 read first and equal to bKCGUhXp.. | the outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK: the function keeps only LATEST, so the rollback is a REBUILD from merged pin 6ecb5bc567 -- its blob table printed BEFORE the apply -- plus the live package downloaded and hash-checked as a reference; the pre-act sweep of every live worktree's open deploys and the change-management ledger | the blob table + base64 sha equality + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed BEFORE the build; the source-map entry read BEFORE this act and compared with the live function | equal counts + the entry's fields before |  | OPEN |
| L4 | verify | BUILD from the DETACHED worktree at EXACTLY the pin, whole content diff printed FIRST (ONE changed member, no registry member, any other is a STOP before upload); r94_naming_replay.py --pin 6ecb5bc567 re-run on the BUILT ZIP before the apply with its denominator, non-zero differ is a STOP; the snapshot's generated_at printed | build sha + content-diff summary + each blob + the replay's denominator and differ count + the stamp |  | OPEN |
| L5 | verify | PRE-ACT CAPTURES immediately before the apply: the timed route baseline and aw4_capture.py (95 names), in sequence, no other reader | capture counts, bytes per name, statuses, durations |  | OPEN |
| L6 | activation | upload with read-back, untargeted plan graded from the plan JSON (one moving resource), safe-apply of the saved plan; the CodeSha256 after differs from bKCGUhXp.. | upload VersionId, plan denominator, apply output, CodeSha256 after |  | OPEN |
| L7 | verify | THE FIRST ACT AFTER THE APPLY: r102_first_cold_request.py driven alone for ASML_NA_Equity, before any capture or replay: RECORDED or NOT COLD (not repeated); handler time against 3,000 ms | the request id, handler time, Init Duration, status, the fourteen phase lines, the AMGT_SEGMENT lines |  | OPEN |
| L8 | verify | the timed route replay and the thesis capture after, single reader; the compare against the baseline; no served byte moved | status moved, changed paths outside the generation clocks, thesis growth per name |  | OPEN |
| L9 | verify | the order's criteria AC1 AC2 AC3 run once after the apply | each criterion's output lines |  | OPEN |
| L10 | git | the record step (record-terraform-deploy.sh) and the source-map entry printed after | entry after equal to the live CodeSha256, commit hash |  | OPEN |
| L11 | verify | report to the issuer with the first cold request's id, handler time, Init Duration, phase lines and segment lines; hold released; pin worktree left | the delivered message |  | OPEN |

## Log

- 20261013T184249Z OPENED by 0.7.0_AE_CloudOps~RA1 with 11 leg(s)
