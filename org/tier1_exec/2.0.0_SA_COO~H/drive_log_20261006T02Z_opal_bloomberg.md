# 2.0.0_SA_COO~H drive log -- 2026-10-05 23:46Z to 2026-10-06 02:16Z (AMGT_HARVST, /canonical-drive 30m)

Decisions: barrons transport stops resumed per ruling 2 (22:00Z, 23:54Z); Andrew-direct "yes do SA and try 200 page cap" -> sa as its own parallel leg (cap 200), launched 01:10Z; HARD BLOCK 01:12-01:41Z on every leg (sa 402, barrons/wsj/bbg bot_check) -> all stopped, no resume, row Z-S89 @d27bd12e34, carried to Andrew. ft held.

## tick 61 -- 2026-10-05 23:46Z
| AMGT_HARVST | L7 | 47 | at-5 live (234) | 2/2 + at-3, at-5 | none | NO-OP, alive (pids 46584/45668/53568): sa 9 (stopped), barrons 128 (last-25 empty_200 6; transport error 23:36Z -> cooldown, auto-resume 2 of 2 SPENT again: next stop resumes per ruling 2), bbg 90 (flat 30 min, one job running, event log fresh), wsj 153, ft 0 (held) of 191 pool keys |

## tick 62 -- 2026-10-06 00:16Z
| AMGT_HARVST | L7 | 47 | at-5 live (234) | 2/2 + at-3, at-5 | none | DRIVE FORWARD: barrons STOPPED ~23:54Z on a transport-class error (retries spent) -> resumed per ruling 2 from its own checkpoint --clear-stop barrons, pid 44328 (r47_sa_barrons_run3.out), 46 pairs left; sa stays stopped (Andrew asked about sa; options put to him: parallel sa leg on its own root, and/or lower the 200-page cap -- no act until his word). bbg 94, wsj 154 alive; barrons 129, sa 9, ft 0 (held) of 191 |

## tick 63 -- 2026-10-06 00:46Z
| AMGT_HARVST | L7 | 47 | at-5 live (234) | 2/2 + at-3, at-5 | none | NO-OP, alive (pids 44328/45668/53568, event logs <2 min): sa 9 (stopped; options with Andrew), barrons 130 (last-25 empty_200 7), bbg 97, wsj 154 (one long job), ft 0 (held) of 191 pool keys |
- 01:12Z ANDREW-DIRECT (verbatim): "yes do SA and try 200 page cap" -> sa runs as its OWN parallel leg, page cap kept at 200. Root .runtime/opal-data-harvest-sa (secrets/sa.dpapi copied; signed_in false, same as earlier sa jobs); checkpoint r47_sa_checkpoint.json seeded with the 13 sa pairs from r46_sa_barrons; dry-run plan sa 221, NETWORK 0; LAUNCHED pid 18932 (r47_sa_run1.out, stop file R47_STOP_SA, auto-resume 2). GUARD: never --clear-stop sa on r46_sa_barrons_checkpoint (that driver keeps SKIPping sa). NEXT TICKS watch pids 44328 (barrons) / 18932 (sa) / 45668 (bbg) / 53568 (wsj).

## tick 64 -- 2026-10-06 01:16Z
| AMGT_HARVST | L7 | 47 | at-5 live (234) | 2/2 + at-3, at-5 | none | RULE: the parallel sa leg (pid 18932) STOPPED on its first job 01:12:40Z: seekingalpha.com /api/v3/account/53673840/info -> HTTP 402 -> account_or_harvester_unavailable (stop class, not transport). Same token as the main root, whose account check read 200 x13 on 2026-10-05 (last 13:59Z); one prior 402 on 2026-09-29 cleared by 09-30. Ruling: ONE retry of the sa leg at the next tick (--clear-stop sa on r47_sa_checkpoint); a second 402 holds sa for Andrew (an account matter: subscription/session), no further attempts. barrons 130 (last-25 empty_200 10), bbg 101, wsj 154 alive; ft 0 (held) |

## tick 65 -- 2026-10-06 01:46Z
| AMGT_HARVST | L7 | 47 | at-5 live (234) | 2/2 + at-3, at-5 | none | RULE (hard block): ALL legs stopped 01:12-01:41Z -- sa 402, barrons/wsj/bbg bot_check (challenges failed). Row Z-S89. No resume; the planned sa retry CANCELLED; carried to Andrew. Concluded of 191: sa 9, barrons 130, bbg 104, wsj 154, ft 0 |

## tick 66 -- 2026-10-06 02:16Z
| AMGT_HARVST | L7 | 47 | at-5 (234) | 2/2 + at-3, at-5 | none | NO-OP (blocked on Andrew, row Z-S89 hard block): 0 backfill_driver processes; no event writes since 01:41Z; nothing resumed |
