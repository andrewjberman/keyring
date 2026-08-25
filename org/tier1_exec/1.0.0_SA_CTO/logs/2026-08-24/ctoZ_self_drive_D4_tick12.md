# /self-drive D4 -- ticks 11-12 log (2026-08-24 23:45Z - 2026-08-25 00:10Z) -- state: ARMED

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE
**Driver:** `1.0.0_SA_CTO~Z` · cron `71ae484c` (verified live via CronList this window) · carrier: `org/XXX.md:408` · continues `ctoZ_self_drive_D4_tick10.md`.

## SCOPE + COMPLETION

```
D4 -> 2 project(s) [ETFS_INGEST, ETFS_POSITIONING]   device: sitez
  claim scan 324 project JSONs · denominator 1 of 9 live directives
  COMPLETION TEST: NOT DONE -- 0 of 2 complete.  REACHABLE 2 / UNREACHABLE 0.
  open calls at Andrew: ZERO (his economy-code word closed the last one)
```

## ANDREW-DIRECT THIS WINDOW

**~23:44Z, item 5 answered, VERBATIM:** *"If you have access to economy code for these securities we
can order based on that instead of GICS, i really dont care if its official gics or some general
economy/sector thing, whatever we can get."* -> **we do, at zero cost: all 10 of our sectors map to
`ECONOMY_ORDER` positions via `GICS_SECTOR_NAME` -> GICS code, a field we already pull.** Record
`ctoZ_ANDREW_DIRECT_20260824_ECONOMY_CODE_ORDERING_WHATEVER_WE_CAN_GET.md`. Item 6 unblocked.

**~23:5xZ, the DIVZ/IDVZ requirement, VERBATIM:** *"We should be able to display data for all 4 ETFs
every day."* -> **the current design structurally cannot**: `resolve_as_of` returns ONE global as-of
and every fund renders at it, so any fund whose history starts later is empty by construction.
**RULED: per-fund as-of.** Measured underneath it: **TrueShares has ZERO rows on 08-19..08-23 and has
NEVER had any** -- bronze holds `20260824/` only, and the source is a point-in-time export, so it is
not retroactively capturable.

## ⛔ THREE CORRECTIONS AGAINST MY OWN RULINGS, ALL FROM OTHER SEATS, ALL ACCEPTED

1. **`Z-S29` (CVO~Z) FALSIFIED MY SEQUENCING RULING.** Gold stamps `data_as_of` from the **PARTITION
   NAME** (`:649`, one occurrence, a WRITE) and reads silver's row-level column **ZERO** times --
   with a positive control that makes it a finding: **gold reads EIGHT other silver columns by
   name.** So *"more visible AND still wrong"* -- the scenario my *"land the re-derive, not the
   per-fund as-of"* rested on -- **cannot occur on either branch.** Retracted inside a minute because
   DS~Z was building against it. **The re-derive came OFF the 13:00Z critical path; the blocking item
   MOVED TO GOLD** (read the row, do not stamp the run), which is where Andrew's provenance ruling is
   actually unimplemented.
2. **`:1183 run_date` (AE~Z) -- MY OWN REFUSAL WAS CARRIED NOWHERE.** I refused the fabricating
   re-fetch at 23:5xZ and **left the refusal in a message**, on a mechanism live on a deployed
   function one `{"run_date": "..."}` away. **A refusal that exists only in message traffic is not a
   control -- it is a hope about who reads their mail.** Disarm ruled as a CODE guard (`run_date` !=
   today AND a fetch about to happen -> REFUSE), which is mechanical correctness at the act and not
   an approval gate.
3. **MY `ETFS-TO5-AC7` WAS NOT ON THE TO FACE AND ITS 11:00Z PREREQUISITE WAS IN NOBODY'S DURABLE
   RECORD** -- and the face carried a DIFFERENT `AC7` (`ETFS-TO2-AC7`, an ADVI fetch), so the search
   a successor would run returned a **confidently wrong hit** rather than nothing. I routed it at
   22:22Z and never verified it landed. **Adoption is not implementation** -- my own banked rule,
   broken on the criterion that closes the round.

⭐ **COO~Z's fix was better than my ask: they wired AC7 into `<expected_criteria>` (`:164`), so
`proof-of-spec-check` REFUSES to close without it.** Mine depended on a successor reading a
paragraph; theirs makes the gate enforce it. Verified on the artifact (165 -> 186 lines), not on the
report -- which was the whole lesson of the ten minutes preceding it.

## AND ONE RISK I DID **NOT** RAISE, BECAUSE I MEASURED IT FIRST

I had drafted an amendment against my own re-derive ruling: the rewrite emits the **26-column
superset** where the partition has **17**, putting an untested shape on the 13:00Z run.
**`etf_positioning_gold.py:351` has no `columns=` pin and `:582` addresses by NAME** -- the wide
shape is a superset and the extras are ignored. **The objection dissolved.** Told DS~Z explicitly not
to build a defence: the likely defence (narrow silver on write) would have **discarded the very
provenance columns the re-derive exists to add.** **A plausible risk raised before it is measured
costs more than one measured and dropped.**

## STATE OF THE WORK

**Bronze, silver, gold, platinum all EXERCISED tonight** -- the chain ran end to end for the first
time. **Schedule closed** (136 -> 137 rules), verified three rungs deep: rule exists · targets the
function · resource policy permits that rule, SourceArn pinned.
**Open:** the gold row-level as-of cell (new, blocking) · per-fund as-of · period returns (1D 109/114,
every other period 0/114) · the yield display convention (producer-emitted, `(a)` only) · items 4/5/6
frontend · the 11:00Z pre-check and 13:00Z AC7, both now durable and machine-enforced.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| CronList | verify the loop is armed | `71ae484c` live, session-only |
| directives-check / to-check | scope + open TOs | 2 projects, NOT DONE 0 of 2 |
| comp-find (`-i`) | as-of surface · `run_date` · `AC7` on the TO face · gold column handling | the AC7 collision; the 0-hit durability gap; no `columns=` pin |
| raw aws (rail-checked) | silver partitions 08-19..08-24, bbg characteristics, deployed bytes | TrueShares 0 rows on five partitions; 109-row characteristics |
| safe-commit | 2 commits ticks 11-12 | PASS |

## Blockers

None at this seat. **Zero cards at Andrew.** 2 commits ahead of `origin/SITEZ`, ride the next window.
