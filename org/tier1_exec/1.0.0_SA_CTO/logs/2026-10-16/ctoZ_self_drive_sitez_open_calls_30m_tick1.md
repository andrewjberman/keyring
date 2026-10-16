# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, tick 1 (2026-10-16 ~02:5xZ to 03:0xZ)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron: e6b088c9 (`13,43 * * * *`). **state: ARMED**

## Session start (post-reboot), for the record

- **Watcher re-armed**; all mail read and acked.
- **OG-ap-24 CTO half SIGNED** @1ef958e44b, against `.tf` sha256-16 21a54e8f197eeea2; trust ruled no ExternalId.
- **Site Z `python3` resolved to the WindowsApps stub.** MSTR~Z landed a `~/bin/python3` forwarder, and the comp-which
  exercise was re-run (PASS). The forwarder is device-local only and not in `provision-path-shims.sh`.
- **Andrew-direct ~02:0xZ / ~02:2xZ:** the COO teams for MCPINDEX, OPLGTW and MCPORTAL, plus CVO~Z and CloudOps~Z/~ZS,
  are back online. Record @b99b867905 and @da6f69be8b; all 7 seats read LIVE.
- **OPAL_BBGTML R8 addendum @46f4d60360:** the glyph fixture is deferred past the 11:00Z fire, and widening `$uLo` is refused.

## Calls this tick

| call | ruling | record |
|---|---|---|
| MCPINDEX r18, section (b) 32 rows (MI2 msg 34655) | 29 ratified; benchmark_returns held at Andrew; cma_assumptions and ai_classified_securities conditional | @32a4dd88dd |
| MCPINDEX, 3 stale/empty rows (MI2 msg 34665) | ratified out, each with a reopen condition | @131991960e |
| sitez-...-035e, eight rows with no OPLGTW tool (CROSS-BOX) | submitted to XA-cdcc with position ADD; the laptop cluster lead RULED (2): seven served/* tools here, the harvest table to dell1 | submission @131991960e; PRD v3.13 @def417d2be |
| OG-ap-24 CVO half (CVO~Z msg 34658) | relayed to CloudOps~ZS and COO~O; COO~O half owed | msgs 34659/34660 |
| MCPORTAL PE+PF round-2 slug (CVO~Z msg 34672) | round-N analysis: MAY-CLOSE; segmentation NOT_REALIZED; next round S1/S2/R2 | @bfe9f3549c |

The remaining open rows on site Z (a519, 21c5, f0d2, 8ed7, 21d9, 3b41, def4) are acts only Andrew can do, already
escalated with citations: his login, his sitting with Alyssa, and his own Teams account.

**035e row not yet closed:** the ruling file is on CLOUD 08cba0ba64 and not yet in box/sitez. The close
(`open-calls.py close --xadj XA-20261016T024917Z-cdcc`) runs on the next tick after box-sync takes CLOUD.

## Sequence

`sequence-check --project` reads no flags for NFRA_OPLGTW, NFRA_MCPINDEX or NFRA_MCPORTAL (MCPORTAL is unplaced).

## Compiler Tools

| tool | used for | result |
|---|---|---|
| comp-rail | denied a glob-scoped grep | re-ran as native Read/Grep |
| comp-which | the A.3 exercise | DEAD, then PASS after the python3 forwarder |
| open-calls.py | list; close 035e | list OK (8 open); close REFUSED: ruling file not on this branch yet |
| xadj.py | open XA-cdcc; show | opened; laptop adjudicator ruled in about 4 minutes |
| sequence-check.py | 3 projects | no flags |

- **What failed:** the first relay of the CVO's ap-24 half was refused by LD-0529 (no TO id cited); re-sent citing it.
- **Gap found:** `open-calls.py close` needs the XA ruling file present locally, so a cross-box ruling cannot close a row
  until box-sync lands it.
