# Deploy Completion Record
**Date opened:** 2026-10-13T23:47:40.647365+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-bz-10: site Z cycle runner re-registered from pin 3d88eccbc3 with -Windowless -RefreshOnce
**Authored by:** 0.7.0_AE_CloudOps~ZW
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PIN | git | worktree at 3d88eccbc3 added and rev-parse reads it, with a positive control on the old pin 995adcaeaa | bz10_pin.out |  | OPEN |
| LOCK | git | every harvest pin carries a locked line in git worktree list --porcelain | bz10_lock.out |  | OPEN |
| STOP | activation | the live cycle ended by the runner's OWN stop file (never a kill), its .cycle.json read, and the stop file DELETED before Start-ScheduledTask | bz10_stopped.out |  | OPEN |
| ARM | activation | installer -Plan read then registered once, bz10_t0.txt written, Start-ScheduledTask once | bz10_plan.out + bz10_register.out + bz10_t0.txt |  | OPEN |
| WINDOW | verify | the four reads R1-R4 at +3 and +15 minutes, each with its control | bz10_reads.out |  | OPEN |

## Log

- 20261013T234740Z OPENED by 0.7.0_AE_CloudOps~ZW with 5 leg(s)
