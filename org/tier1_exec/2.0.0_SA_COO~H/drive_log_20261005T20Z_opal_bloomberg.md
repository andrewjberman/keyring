# 2.0.0_SA_COO~H drive log -- 2026-10-05 17:27Z-20:16Z (AMGT_HARVST, /canonical-drive 30m)

Decisions: legs relaunched on 234 names 17:27Z; RESAPP au-3 gold url landed, HARVST gold-build hold lifted (COO~Z 29748); row Z-S88 barrons soft blocks @4c90da48d1 + CTO~Z ruling 29759 (pause at a majority of the last 25). ft held.

- 17:27Z RELAUNCHED on 234 (at-5 @1685d149fa), each from its own checkpoint: wsj pid 53568 (plan 127), sa_barrons pid 30680 (plan barrons 169; SKIP sa stopped upstream_unavailable), bbg pid 45668 (plan 180). Stop files removed. Outputs .runtime/harvest-backfill/r47_<leg>_run1.out. NEXT TICKS: watch pids 30680/45668/53568.

## tick 49 -- 2026-10-05 17:46Z
| AMGT_HARVST | L7 | 47 | at-5 landed @1685d149fa, legs relaunched 17:27Z on 234 | 2/2 + at-3, at-5 | none | NO-OP, alive (pids 30680/45668/53568): concluded of the 191 pool keys -- sa 9 (stopped), barrons 49 (empty_200 19; transport error 17:33Z -> cooldown, auto-resume 1 of 2), bbg 52, wsj 104, ft 0 (held); DECLARED SET EMPTY. The 43 added names sit later in each plan |
- 18:01Z COO~Z 29746: RESAPP au-3 (gold url column) landed @69c017d520; HARVST gold-build hold lifts when their test commit lands (no build due before the r47 drain). Replied: their Z-W233-S2 (reader holds 53 of 95 covered names) is the stale pool universe/v1 2026-09-16; the 56 approved resolutions are in registrations.json; the pool rebuild belongs to the build_universe.py owner.
- 18:11Z COO~Z 29748: test commit @a53eaf74c5 landed (harvest suite 353 passed) -> HARVST gold-build hold LIFTED (next build at the r47 drain carries url). Stale pool universe/v1 goes to RESAPP round-72 list with the build_universe.py owner. No reply owed.

## tick 50 -- 2026-10-05 18:16Z
| AMGT_HARVST | L7 | 47 | at-5 live since 17:27Z (234 names) | 2/2 + at-3, at-5 | none | NO-OP, alive (pids 30680/45668/53568, event logs <1 min): concluded of the 191 pool keys -- sa 9 (stopped), barrons 54 (empty_200 21), bbg 55, wsj 109, ft 0 (held); DECLARED SET EMPTY. Gold-build hold lifted (COO~Z 29748) |

## tick 51 -- 2026-10-05 18:46Z
| AMGT_HARVST | L7 | 47 | at-5 live (234) | 2/2 + at-3, at-5 | none | RULE: barrons listing_empty_200 12 of last 25 jobs (was ~26%), on large US names -> soft blocks; row Z-S88 @4c90da48d1; ruling: keep pacing, re-run empties in the leg-end --names pass, hard block -> stop + Andrew. Alive (pids 30680/45668/53568): sa 9 (stopped), barrons 64, bbg 59, wsj 114, ft 0 (held) of 191 pool keys |

## tick 52 -- 2026-10-05 19:16Z
| AMGT_HARVST | L7 | 47 | at-5 live (234) | 2/2 + at-3, at-5 | none | NO-OP, alive (pids 30680/45668/53568, event logs <1 min): sa 9 (stopped), barrons 72 (empty_200 3 of 12 since 18:46Z, eased from 12 of 25; Z-S88 ruling holds), bbg 62, wsj 118, ft 0 (held) of 191 pool keys; DECLARED SET EMPTY |
- 19:21Z CTO~Z 29759 RULING on Z-S88 (acked): (1) listing_empty_200 = soft-block status, never a conclusion (already so: not in SUCCESSFUL_RUN_STATUSES, verdict reader excludes it); (2) ONE re-run per such job in the leg-end --names pass = same run, no second pass; (3) if soft blocks reach a MAJORITY (>=13) of the last 25 barrons jobs -> pause the leg for one collector cooldown (stop file, relaunch from own checkpoint after it); (4) hard block -> stop, Andrew decides. EVERY TICK NOW: compute barrons empty_200 of last 25 jobs.

## tick 53 -- 2026-10-05 19:46Z
| AMGT_HARVST | L7 | 47 | at-5 live (234) | 2/2 + at-3, at-5 | none | NO-OP, alive: sa 9 (stopped), barrons 80 (last-25 empty_200 7, under the CTO pause line of 13; transport error 19:38Z -> cooldown, auto-resume 2 of 2 SPENT: a further transient stops the leg -> resume per ruling 2 with --clear-stop barrons), bbg 65, wsj 122, ft 0 (held) of 191 pool keys |

## tick 54 -- 2026-10-05 20:16Z
| AMGT_HARVST | L7 | 47 | at-5 live (234) | 2/2 + at-3, at-5 | none | NO-OP, alive (event logs <1 min): sa 9 (stopped), barrons 83 (last-25 empty_200 6), bbg 68, wsj 127, ft 0 (held) of 191 pool keys; DECLARED SET EMPTY |
