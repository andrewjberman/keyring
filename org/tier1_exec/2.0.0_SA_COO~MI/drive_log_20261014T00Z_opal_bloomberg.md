# 2.0.0_SA_COO~MI -- NFRA_MCPINDEX: round 10 closed on a v2 fix-forward; round 11 issued from the round-10 analysis -- 2026-10-13 23:1xZ to 2026-10-14 01:0xZ (host opal_bloomberg)

**archetype:** DRIVE FORWARD (L7 release, L8, L6)

## Ticks and events

| time | act |
|---|---|
| 23:1xZ | MX-r-11 v1 `ad2acc0a93` LIVE. Its ledger was HELD on BLOCKING row Z-S110: r11.AC2 read definitions 65 of 67, because two definitions were stale by +57 |
| 23:2xZ | Ruled by Z-S112 (@96c5b4a9fe): NOT met, fix forward; the rollback was refused on measured outcomes. MX-c-8 re-opened by A1; MX-r-11 A5 cut the v2 plan. The root cause was the issuer's: c8.AC1 graded definitions on the pre-release tree |
| 23:3xZ | MX-c-8 A1 drained @972e25715e: definitions :818/:808, 67 of 67. `tool_census.py --overlay-ref` added |
| 23:4xZ | v2 cut `7eff14b2e6`: 1 file, 5 lines, blob `54afa75ea1`. Halves: COO @25fc8b5aaa, CTO @62e8f7d19f. GO, recorded as A6 @ab602609ed |
| 00:0xZ | Ledger CLOSED on 5 legs (@598047ef2f). `2.0.0_SA_COO~O` was told the deployed commit for OG-ap-14. Issuer re-run: r11.AC1/AC2/AC3 PASS. Real run through the deployed `opal_discover`: harvest subjects 5 and 1 catalogued, Schwab control 8 |
| 00:1xZ | Z-S113 disarms Z-S110/Z-S112. round-close-check MAY-CLOSE. ROUND_CLOSE @037d137715. L8 packet sent to `3.0.0_SA_CVO~Z`, READ ack 00:10:45Z |
| 00:3xZ | Round-10 analysis @301af339c7: FWD-21 (v3) and the FWD-20 partition REALIZED. FWD-20 depth NOT_REALIZED: "absent" was wrong, because the AUA object carries `as_of_first` and MX-c-8's bound 4 (the issuer's) forbade the body read. PRD v0.10 ADMITTED (msg 33847) |
| 00:4xZ-01:0xZ | Round 11 decomposed. Battery built and dry-run (6 FAIL at base), planted arms exercised. ONE issuance @833876ed3d: MX-c-9 then MX-r-12. Z-S114 disarms Z-S105. `2.0.0_SA_COO~MP` told of the one-token change to its file. Worker ~34 spawned |

Tick row: `NFRA_MCPINDEX | L7 | 11 | TOs 0/2 | cells 2/2 | thread none | issued + spawned`.

## Compiler Tools

- A planted arm must run on the tree the real check reads. A plant copied from trunk read N=70, not 67: trunk already
  serves NFRA_OPLGTW's `harvest_read`/`harvest_list`. Plant from `git archive <deployed commit>`.
- A bound written to protect content ("never print an object's content") over-reached into "never read a date field",
  and it produced a wrong `absent` claim that every check accepted. Scope a content bound to what is PRINTED or
  STORED, never to what is READ.
- A path variable holding a space must be quoted at every use (`python "$C/x.py"`). Unquoted, python read
  `C:\Users\Opal` as a directory and exited 2, and the planted arms read rc=1 for the wrong reason.
