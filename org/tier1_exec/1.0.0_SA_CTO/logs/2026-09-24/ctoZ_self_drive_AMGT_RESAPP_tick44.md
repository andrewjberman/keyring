# /self-drive AMGT_RESAPP -- tick 44 (covers ticks 39-44)

**Arming record:** `ANDREW_DIRECT_20260923_193xZ_SELF_DRIVE_AMGT_ALL_THREE_CLOSER_LOOPS.md` @`a8a62f4f5c`
**state: ARMED** | watcher re-arm 40 (`bxsseueb6`) | last log `31c2e03c0e`, author time 2026-09-24T10:09:48-04:00
(cursor read from the COMMIT, never the filename) | 8 commits by this seat since

## Scope state -- BOTH populations, labelled (R-73)

| | |
|---|---|
| **close test** | **0 of 49 outcomes graded** (RESAPP 30 + CORPUS 19; addendums verified INSIDE -- `FWD-10..19` all ten, `FWD-30` present) |
| **macro** | **0 of 3 projects `status: complete`** (HARVST contributes to the backfill clause; its close status is Andrew's reading) |
| RESAPP | 208 orders, **3 pending** -- `rk-49` (Andrew), `rm-2`, `rm-7` |
| CORPUS | 17 orders, **0 pending** -- round 2 CLOSED, packet FINAL; L8 with `3.0.0_SA_CVO~Z` |
| HARVST | 18 orders, **0 pending**, `ROUND_CLOSE` |
| sequence | `AMGT_RESAPP` UNPLACED (TRACK) -- its own directive governs |

## The goal's last clause finally has a number -- and it is not the printed one

`CRPS-d-4` closed (drain `809a89d8ff`, packet FINAL `918ca7abe0`). Printed tri-state, MECE and summing:
`93 = 53 dossier-served + 0 resolved-no-prose + 40 unresolved-with-reason`.

⛔ **`dossier-served` IS A PIPELINE STATE AND THE GOAL ASKS A CONTENT QUESTION** (R-75 @`791aa3e4af`). Row
`W1-S4`: nine of the 53 resolved folders are workbook-only and all nine read `dossier-served`, because
`dossier.build()` has **no report-count floor** and stored an all-fields-absent dossier for each. Content
re-cut over the same denominator: **44 substantive + 9 empty-shell + 40 unresolved-at-identity = 93.**

**Reachability, with the unmeasured part left unmeasured:** UNMEASURED 40 (count AND direction unknown);
UNREACHABLE-BY-SOURCE 10 (workbook-only -- no pipeline makes prose from a source that has none);
UNREACHABLE 1 (empty folder). **At least 11 of 93 are not satisfiable by pipeline work at all**, which is
the card now with Andrew.

## Acts this block

| act | commit |
|---|---|
| C13 L4-R **RATIFIED**, 3 amendments | `b26449defe` |
| `Z-S248` fixed + ledger CLOSED (`PY_AWS` hoist, a DEPLOY) | `e7fbcf4f7c` open / `2e38c030f4` close |
| `Z-S251` filed (the 13-site concealment class) | `1c17c4d516` |
| R-73 (addendums covered; the 0-of-3 / 0-of-49 unit error) | `1c558b5` |
| R-74 (`POD_DE_ANY` on `portal/**` is UNENFORCED) | `c0e33bd6fc` |
| R-75 (53 is a pipeline state; content reads 44) | `791aa3e4af` |
| R-76 + amend R-75 | `4f93bbf428` |
| R-76a (the normalised plane fails too) | this commit |

## ⛔ FIVE OF THIS SEAT'S OWN CLAIMS WERE CORRECTED THIS BLOCK, FOUR BY OTHER SEATS

1. **R-71/R-72** -- this seat was ONE TOOL CALL from broadcasting a fabric-wide "identity breach" on a
   peer's report, having measured NOTHING. **Andrew stopped it, not any control here.**
2. **R-74** -- corrected a RIGHT answer into a WRONG one: `ls | head -10` (right, unsound), then
   `grep -v "\.sample$"` on classified output (**wrong, confident, and a retraction gets believed**).
3. **R-75** -- carried `2.0.0_SA_COO~Y`'s TRUE "13 of 13" into a population it never measured. That seat
   brought the correction itself: **UNRESOLVED entries carrying a cik, 0 of 59.** The EDGAR arm is strictly
   downstream of identity and can never CREATE it.
4. **R-57 -> R-76** -- a `DELTA=0` cited to skip a never-widen pair, with **no plane named.**
5. **R-76 -> R-76a** -- the plane was then named and was **still wrong**: the pin REMOVES `/CreationDate`
   and shifts every xref offset, so the normalised sha moves too. Comparand is now the CONTENT-STREAM
   digest.

⭐ **THE PATTERN WORTH THE ENTRY: every one of the four peer corrections came from the seat about to
EXECUTE the thing this seat had ruled on.** `0.7.0_AE_CloudOps~A` found two defects in the issuer's cut
before any world act; `2.0.0_SA_COO~Y` corrected its own evidence being over-carried; `2.0.0_SA_COO~Z`
relayed both and named its own scope gap. **The lane that has to run the rule is the one that finds it
false** -- which is an argument for stating rules in a form an executor can falsify, not for ruling less.

## Completion test

**NOT DONE.** No project reads `complete`. RESAPP's round 38 has `rm-2` building and `rm-7` deploying under
an amended face; CORPUS awaits its L8/L9 then this seat's L10; HARVST's cutover is mechanically blocked on
a card at Andrew.

## Still at Andrew (5)

Publisher access (heads *access -> collection -> cutover -> schedule*); `rk-49`'s Lusha key-rotation fact;
the call-4 client notification; the sidebar's wider treatment; **NEW -- the 11 source-blocked folders and
whether "every single security" can mean anything else.**

## Compiler Tools

`git log/show/ls-remote`, `safe-commit.sh` (verdict by token), `sequence-check.py`, `comp-find` (native
flags, never a pipe), `Get-ScheduledTask`/`Info`, `cmd.exe` two-arm control, `send_message`,
`ack_messages`, `check_inbox`, `get_live_agents`, `set_summary`, Monitor, Artifact, curl, Glob.
