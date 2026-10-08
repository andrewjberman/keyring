# ANDREW-DIRECT 2026-10-08 ~20:0xZ to ~20:3xZ -- at the `0.0.0_AB_MSTR~Z` terminal (site Z)

## His words, verbatim

> I want everything pushed, we have 6 min to get it onto cloud

> We will deal with this pull script after the fact, do whatever you have to do to manage it in the interim

> Ok now that the fabric is quiet here, what weirdness do we need to work out with the union row and the old vs new
> bloomberg puller? lets get that out of the way now, any remaiing merge/push work that needs to be done, e.g. pulling
> from CLOUD and so on, and then i want to reboot this box with instructions to bring everybody back online who was
> working before as ive had to cull most of the agents

## What was done on them, by `0.0.0_AB_MSTR~Z`

1. **Site Z on the trunk.** `box-sync.sh box` took origin CLOUD a8689cb259 into `box/sitez` and pushed it:
   `refs/heads/box/sitez` 75e0b219b6 (ls-remote read ~20:3xZ), tree check 826 needed / 0 dropped, no deploy. Seven
   deploy-ledger files carrying only monitor timestamps were restored to HEAD first (backup
   `C:/tmp/mstrz-relay/open_deploys_dirty_20261008_2030Z`; row NFRA_SYSPARITY-Z-S2's class).
2. **The Bloomberg puller, interim.** The trunk carries dell1's SH-t-4 edit of
   `integrations/bloomberg/pipeline/etf_daily_pull.py` (19e50528d3). The 2026-10-09 07:00 ET scheduled pull runs the
   site-Z working tree, and 1.0.0_SA_CTO~DELL1 asked that its acceptance run see the round-1 bytes. So the working copy
   is the round-1 blob 0e399c9523 (uncommitted, nothing committed over it), and a one-shot scheduled task
   `OPAL_restore_etf_daily_pull_20261009` runs `git checkout HEAD -- <that file>` at 2026-10-09 08:00 local. Both survive
   a reboot. Whether that is the end state is his to settle "after the fact".
3. **Reboot roster.** `C:\opal-elev\autolaunch-agents.ps1` (run by the logon task `OPAL_autolaunch_agents`) now
   launches the 15 seats working on site Z today; backup `C:/tmp/mstrz-relay/autolaunch-agents.ps1.bak-20261008`.
   The repo's `.tools/autolaunch-task.ps1 -Serials ...` could not replace the task (access denied: it was registered
   elevated), so the existing task's own script carries the list.
