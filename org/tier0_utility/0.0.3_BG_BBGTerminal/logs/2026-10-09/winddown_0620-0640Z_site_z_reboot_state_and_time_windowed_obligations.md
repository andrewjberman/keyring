# Wind-down 06:20-06:40Z: site Z reboot -- state committed, and one reboot hazard I do not own

**archetype:** SCRIBE
**secondary_archetypes:** DIAGNOSE (the etf_daily_pull working-tree hazard)

On Andrew-direct ~06:1xZ relayed as msg 32460, VERBATIM: *"we will roll that into a reboot, so
everyone on sitez should wind down preemptively and log as needed."* Started no new work after it.
Prior log this session: `relaunch_0106-0320Z_four_acceptance_reads_and_two_false_controls.md`
@396810359b.

## Current State

**Nothing of mine is uncommitted.** `git status --porcelain` over my seat dir and both channels I
touched returns empty. Four commits this session plus the rescue:

| commit | what |
|---|---|
| `550eac8853` | OPAL_ANALYST-Z-S1 -- the relaunch runbook's oid negative control reads 2 of 3, not 0 |
| `c086fcc096` | ETFS_RIVALS-Z-S79 + the 2026-10-08 vehicle-log transcription + `transcribe_vehicle_log.py` |
| `eaf6d69c9a` | ETFS_RIVALS-Z-S80 -- correction: S79's ARMED disarm_owner named a dead seat |
| `5fae4a8b04` | OPAL_ANALYST-Z-S2 -- correction: S1's second filter stopped applying within 3 h |
| `396810359b` | this session's main log |
| `11a393f55a` | THE RESCUE, 13 files / 1520 insertions -- see below |

**THE RESCUE, and it is the part worth reading.** The wind-down sweep of my own home folder found
the uncommitted set was mostly NOT this session's: two prior sessions' logs (`logs/2026-10-07/`,
all of `logs/2026-10-08/`) and seven thread dailies across five threads, including the records
carrying this seat's two standing OWED items. Site Z's shared tree loses uncommitted work on a
reboot, so they were one restart from gone.

Root cause of the accumulation, measured at the refusal: **this seat cannot commit its own thread
memory.** `owned-paths` refused 12 of 13 paths -- lane `TIER0_UTILITY` does not list
`0.0.3_BG_BBGTerminal` in `permitted_agents`, and its home-folder convention auto-enrolls only
`logs/` and `task_orders/`. That is why `396810359b` (a log) committed cleanly minutes earlier while
`threads/` and `deliverables/` under the SAME home folder refused. Landed under the audited lane
escape (`GIT_COMMIT_AUTHOR_OVERRIDE=TIER0_UTILITY`; audit lines 27385/27387 OVERRIDE, 27389
LANDED-2P). **Widening the lane enumeration is a GATE EDIT and was NOT taken** -- it is the lane
rule's owner's, and it is the real fix: thread memory is the serve loop's continuity mechanism
("THREAD MEMORY DECIDES WHAT IS OWED") living in a directory the seat may not commit.

## REBOOT HAZARD I DO NOT OWN -- surface, do not touch

`integrations/bloomberg/pipeline/etf_daily_pull.py` carries an **UNCOMMITTED 15-line deletion** in
the shared tree right now (`git diff --stat`: 1 file changed, 15 deletions), removing the SH-t-4
"Run record: print the draw beside the ledger remainder" block.

Three facts that combine badly across a reboot:
1. `READ_HERE.md:104-108` -- **SITE-Z SCHEDULED TASKS RUN THE WORKING TREE.**
2. `OPAL_BBGTML_daily_pull` nextRun 2026-10-09 07:00 local = **11:00Z**, state Ready.
3. `OPAL_restore_etf_daily_pull_20261009` nextRun 2026-10-09 08:00 local = **12:00Z** -- an hour
   AFTER the pull, which reads as someone deliberately staging that deletion to be live for the
   11:00Z run and restoring it afterwards.

**If the reboot discards the uncommitted deletion, the 11:00Z pull executes the COMMITTED version
instead -- a different code path than whoever staged it intended -- and the 12:00Z task then
"restores" a file that was never changed.** Both outcomes are silent: the pull does not know which
version it ran, and a restore of an unchanged file reports success.

NOT MINE on two counts: `integrations/bloomberg/` is under an Andrew-direct no-modify order (this
seat READS it, never edits), and I did not stage it. I neither committed nor reverted it. Surfaced
to `0.0.0_AB_MSTR~Z` in the WOUND DOWN reply for routing to whoever cut SH-t-4.

## Time-windowed obligations (none of them mine, named so the reboot does not drop them)

| when | what | owner |
|---|---|---|
| 10:45Z | Terminal sign-in pre-flight for the 11:00Z RIVALS/SECHIST and 13:00Z AMGT fires | `0.7.0_AE_CloudOps~ZV` (msg 32379). LOCALHOST-ONLY -- DAPI is 127.0.0.1:8194, so it must be a site-Z seat on this box |
| 11:15Z | commit the 2026-10-09 11:00Z vehicle-log lines verbatim | `0.7.0_AE_CloudOps~ZV`, dell1 order `TO-RELAY-tw1-vehicle-log-20261009`. My `transcribe_vehicle_log.py` is committed for it and makes it one command |
| 11:00Z | `OPAL_BBGTML_daily_pull` (OS task, survives the reboot) | the hazard above decides WHICH bytes it runs |

My own 04:2xZ pre-flight (credentials OK, `bloomberg_health` ok:true, draw already spent at 03:5xZ,
no sign-in needed) went to dell1 via `0.0.0_AB_MSTR~Z`, marked a 04:2xZ reading and NOT an 11:00Z
promise. It does not discharge the 10:45Z one.

## Next step for my successor

1. `/watcher`, then the four acceptance reads if relaunched under `--strict-mcp-config`.
2. **After EVERY Teams re-arm, make one gateway call and confirm the `re-selected after lapse`
   line.** Measured 3 of 3 arms this session came up blind: the pinned token's TTL is ~14 min
   (readings 784 s, 832 s) and the arm period is 29.5 min, so an arm is lapsed by construction and
   only a gateway call re-mints it. The arm banner alone is NOT evidence the seat can hear. This
   sharpens the already-owned gateway blocker (1) from intermittent to deterministic; it is not a
   new finding and was not re-filed.
3. **OWED, unchanged and all held on Andrew's word** (all three now committed in thread memory, so
   they survive this reboot): the PFDE reply, DRAFTED-HELD (answer `PX_LAST 28.4616`,
   `PX_CLOSE_DT 2026-10-08`, trading calendar resolved first); the Alyssa Tax SMA reply, drafted
   2026-10-08, not sent; Andrew's 2026-10-08T21:57Z dictated Tax SMA ask, ACK not sent, entitlement
   half routed to `0.0.0_AB_MSTR~Z`.
4. Gateway allowlist: **6 of 6** reads denied on this identity (`opal_discover`, `opal_describe`,
   `blackdiamond_list_fees`, `find_sharepoint_site`, `search_files`, `etfs_get_positioning`). It now
   has a measured service cost: the Bloomberg guardrails' PREFERRED path is the already-paid-for
   served artifact, and this seat cannot reach it, so every data question burns a live terminal read.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `git status --porcelain -- <my paths>` | the wind-down sweep | PASS -- found 12 uncommitted files, 10 of them prior sessions' |
| `safe-commit.sh` | 3 commits incl. the rescue | PASS; two BLOCKs then OVERRIDE, all three in the audit instrument |
| `grep` on `org/git-author-override-audit.log` | verify my own override was recorded | PASS -- lines 27385/27387 OVERRIDE, 27389 LANDED-2P `11a393f55a`, denominator 27396 |
| `Get-ScheduledTaskInfo` | the 11:00Z and 12:00Z task windows | PASS -- both Ready with nextRun read, which is what makes the hazard above concrete |
| `comp-read --for` | `READ_HERE.md` working-tree clause | PASS |

**What worked:** sweeping my own home folder by pathspec rather than trusting "I committed as I
went" -- it is the only reason two prior sessions' records exist now.

**What failed:** I spent an audited `surprise-row-override` earlier this session on a transient
(a concurrent-append race on a shared channel; the same bytes passed on retry minutes later) and
wrote an unsupported causal claim into its reason. Corrected to both seats I named in it (msg
32442/32443). The lesson is narrow and mechanical: on a corpus-wide gate, RETRY before overriding;
on a deterministic lane rule, the override is correct first time.

**Gap found:** lane `TIER0_UTILITY`'s enumeration covers `logs/` + `task_orders/` but not
`threads/` + `deliverables/`, so a UA seat cannot commit its own continuity record. Routed, not
taken.

## Blockers

None BLOCKED on evidence. Reserved at Andrew: the three OWED sends above and the allowlist
widening. One hazard surfaced and unowned-by-me: the `etf_daily_pull.py` working-tree deletion
across the reboot.
