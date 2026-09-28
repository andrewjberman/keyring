# ANDREW-DIRECT 2026-09-28 ~19:5xZ -- SITE-Z AMGT ONLINE, ONE COO PER PROJECT (seating record)

**Recorded by:** `1.0.0_SA_CTO~Z`, same turn as receipt.
**Channel:** relayed by `0.0.0_AB_MSTR~Z` as this seat's first message after the site-Z reboot (spawn audit
`2026-09-28T19:49:29Z SPAWN 1.0.0_SA_CTO~Z by 0.0.0_AB_MSTR~Z`).

## The word (verbatim as relayed)

> "bring the site Z AMGT fabric online with one COO per project on a relevant tilde. Read
> org/tier1_exec/1.0.0_SA_CTO/deliverables/SITEZ_AMGT_REBOOT_STATE_20260928.md first, then your inbox. Python PATH
> fixed at be2d74b007."

## Seating (this seat's L3 choice of tilde; the spawn is `0.0.0_AB_MSTR~Z`'s act -- a CTO does not hold /mstr-spawn)

| Project | COO lane | Why this tilde | Resume from |
|---|---|---|---|
| AMGT_HARVST | `2.0.0_SA_COO~H` | NEW lane. The previous seat `~Y` is LIVE on the laptop for IRPT_BCKEND workstream ~Y (commit 89f619e28b, 2026-09-28 14:47 local); re-seating HARVST at `~Y` would put one serial on two devices and two projects. `~H` = HARVST, no prior author (git census, origin/CLOUD). | `org/tier1_exec/2.0.0_SA_COO~Y/logs/2026-09-28/session_close_0104-1440Z.md`; `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round10.md` |
| AMGT_CORPUS | `2.0.0_SA_COO~X` | Its seat through 2026-09-26 (last commit d8cbad9590). No other device authored as `~X` since. | `org/tier1_exec/2.0.0_SA_COO~X/deliverables/CHECKPOINT_AMGT_CORPUS_20260926.md` |
| AMGT_RESAPP | `2.0.0_SA_COO~Z` | Its seat from round 12 (last commit e55bcd9e54). Site-Z native. | `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/CHECKPOINT_20260926_COO_Z.md` |

Carrier: `project.json` `seats.coo` for AMGT_HARVST moves to `~H` in the same commit as this record.

## Every COO's first read

1. `SITEZ_AMGT_REBOOT_STATE_20260928.md` section 2 (its project) and sections 5a / 5b.
2. **S19 constraint:** origin/CLOUD was rewritten. Never merge a pre-rewrite branch; land content by cherry-pick only.
   Cut every worker worktree fresh from the current trunk. HARVST round 11 re-spawns on fresh worktrees; z-2's two
   uncommitted AC scripts cross by file copy from `C:/Users/Opal Bloomberg/Desktop/wk-hvst-z2-r11`.
3. Zero crons at launch (`org/XXX.md` Step 1b-F); `/watcher` once. No `org/ref/LIVE_ARMS.md` row exists for these lanes.

## Not in this word

- `3.0.0_SA_CVO~Z` (restart map item 5). Not seated by this record. Until it is, AMGT_HARVST's L8-L10 route to
  `3.0.0_SA_CVO~O` stands, and RESAPP round 45 / CORPUS round 7 L8 have no site-Z compiler.
