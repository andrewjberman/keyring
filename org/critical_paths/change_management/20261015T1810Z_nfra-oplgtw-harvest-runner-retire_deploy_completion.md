# Deploy Completion Record
**Date opened:** 2026-10-15T18:10:00.130183+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-eg-3: the site Z harvest runner RETIRES -- STOP at a job boundary then Disable, unregister nothing, pins stay locked; and the two open runner ledgers close SUPERSEDED (PRD v3.11, CTO msg 34500, Andrew moved all harvest operations to dell1). Reassigned to 0.7.0_AE_CloudOps~Z in A1 167a5e9ecb because 0.7.0_AE_CloudOps~ZW is stopped at a weekly usage limit until Oct 18.
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| stop | activation | write the runner's STOP file and wait for it to exit at a JOB BOUNDARY; never kill the process or the task | proof: a Win32_Process census showing 0 cycle_runner processes with the denominator printed, and the exit time |  | OPEN |
| disable | activation | Disable-ScheduledTask on 'Opal Data Harvest - Continuous Cycle', unregister nothing, leave the STOP file in place | proof: Get-ScheduledTask reads State Disabled, plus a second census at 0 |  | OPEN |
| pins-locked | verify | the five pin worktrees stay LOCKED -- they are the rollback source until dell1 reports a productive cycle per publisher | proof: git worktree list --porcelain read WHOLE, each of the five pins printed with its locked line |  | OPEN |
| ledgers-superseded | verify | close nfra-oplgtw-harvest-runner-silver-cache (OG-eg-2, FIRSTREC NOT-EXERCISED) and nfra-oplgtw-harvest-runner-sa (OG-sa-1, WINDOW NOT-EXERCISED) SUPERSEDED by this order | proof: both entries read Status CLOSED at HEAD with SUPERSEDED named in the close line, and both sentinels gone |  | OPEN |

## Log

- 20261015T181000Z OPENED by 0.7.0_AE_CloudOps~Z with 4 leg(s)
