# OVP WS-1: Vendor As-Of Endpoint Census -- FULL EXECUTION, GO to denominator-complete

**archetype:** TRACE
**Serial:** 0.4.0_DS_ClientPlatform
**Session window:** 2026-08-03 ~20:20Z - 22:00Z
**TO:** OPAL_VENDORPROVENANCE.WS1.asof-endpoint-census (COO GO 201222Z; D-1/D-2/D-3 supplement 201447Z @e82271228b)

## What happened

The whole WS-1 census ran GO-to-complete in one session, four tranches, each committed +
tranche-reported to COO+CTO as landed (mandate phase 3):

| Tranche | Commit | Rows |
|---|---|---|
| T1 orion + eclipse | @f129fc1c80 | 15 (registry BORN at data/_contracts/vendor_asof_registry.yaml, D-1 canonical home) |
| U-1 probe resolution | @15d0326c80 | (CTO-authorized A/B probe; U-1 INFERRED -> EXERCISED) |
| T2 smartx + blackdiamond | @438a3c69b3 | +19 = 34 (MDPF_GLOBAL.T4A dependency set complete) |
| T3 schwab + U-5 ruling fold | @89d5de8a4a | +2 = 36 |
| T4 trueshares + pathfinder + completeness statement | @01ab614102 | +3 = **39 COMPLETE** |

Census doc (denominator method M1-M4, per-bucket inventory tables, findings 1-12, U-1
probe log s.6a, completeness statement s.6):
`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/OVP_WS1/CENSUS_asof_endpoint_denominator.md`.

## Rulings received + folded (same session)

- CTO 210542Z: vocabulary RATIFIED (current-state-no-date + event-dated) @dd62e07436 +
  SEAL-DECAY rule; U-1 probe AUTHORIZED in WS-1 scope; tool gap routed.
- CTO 211158Z: U-1 probe evidence ACCEPTED (RAVC-4).
- CTO 213057Z: U-5 RULED retired-by-supersession + 2 riders; recoverability class made
  PRD law s.3.2a; T3 file-vintage framing instruction.
- COO 213224Z: T2 verified; MDPF_GLOBAL.T4A authored to this seat @a9f8f06c55
  (staged, self-activating on WS-1 completion).
- COO 214357Z receipt-check: confirmed received + already-folded (reply 214534Z).

## The U-1 A/B probe (CTO-authorized, read-only, lifted Orion egress)

Three-way diff on the shared Assets endpoint: A = 09:32 ET production capture
(bronze/assets/2026-08-03.parquet, 35,219 rows) == B = fresh {today} pull 17:08 ET
post-close == C = fresh prior-trading-day (07-31) pull. 22/22 assets identical on
currentValue/currentPrice/currentShares; asOfDate echoed the request BOTH directions.
Post-shift -1 trading-day semantics EXERCISED at stated sample (1 day / 3 clients / 22
assets). _orion_vendor_asof.py NOT touched (premise refresh routes through COO to the
inf-tree lane per CTO).

## Findings worth the record (full list census doc s.4/s.4a)

1. The 2026-07-01 +47min pull shift (@b2f61bed83) crossed market open -- turned the
   Orion seal into an inference; probe re-exercised it same session.
2. Weekend-labeled partitions are live across daily pullers (Friday carries under
   Sat/Sun labels) -- the dedup canon must count NYSE trading days.
3. Recoverability distribution (now PRD law): BD = the ONLY date-addressed backfillable
   vendor; orion echo-normalized re-pullable; smartx/eclipse/trueshares/pathfinder
   current-state or fixed-URL = PERMANENT gaps; schwab file-vintage settled.
4. cot snapshot tables run LAG=0 -- the measured 0-row-shell exposure is LIVE (masked by
   the retry-net), now a named registry risk.
5. cot period-table filenames LEAD content by one ET day (UTC-run-date labels).
6. bd firm-bucket forwardfill_v2 RETIRED-BY-SUPERSESSION (U-5 ruled; zombie-writer +
   no-deletion-warrant riders recorded).
7. Dual-producer overlap on 6 inf dim feeds (Lambda crons + EC2 orchestrator) -- COO
   carrying to CTO with the MDPF twin-producer precedent.
8. Estate-census drift: pre-shift crons + a smartx vertical that does not contain the
   census-scoped monolith producer -- noted, grounded live instead.

## Compiler Tools (TO mandate reproduction -- every <run>, observed vs <expect>)

| Mandate run | Observed | Verdict vs expect |
|---|---|---|
| Phase 1 `comp-estate --list` then per-vertical | 29 verticals/138 chains; advi-inf read in full (14 chains, producer/cron/output detail); smartx read (3 chains -- monolith C5 producer NOT among them, an estate-census gap) | PASS -- seeded the inventory; census-vintage drift noted + grounded live exactly per if_mismatch |
| Phase 1 `comp-pipescript io <converter>` | REFUSED rc=2 on data/assets/scripts/silver/mirror_conversion.py (--pipeline required; script outside the tool's data/*/scripts map) | if_mismatch path taken: manual source-reads with file:line cites substituted (registry rows carry them); TOOL GAP reported to CTO (routed to COO as WS4-hardening candidate + CVO register, CTO 210542Z item 3) |
| Phase 2 `comp-blast <fn>` | N/A as expected: census is read-only, zero shared helpers touched, all committed files new (data/_contracts/ single-writer per TO, deliverables, this log) | PASS per expect ("expected: none") |
| Phase 3 `comp-validate` | N/A per expect (registry YAML has no validate config); MCP tranche reports sent at every tranche with registry path + commit + rows + UNKNOWN count + denominator coverage | PASS -- no tranche report omitted the denominator-coverage line |
| Supporting on-rails runs | comp-glob x3 (68 inf-pipeline + 81 assets-scripts + 6 bronze files), comp-grep x~15 (routes, schedules, as-of fields, producers -- each with printed scanned-N denominators), live aws s3 ls sweeps (all 4 buckets, vendor prefixes, partition tails), 1 CTO-authorized egress probe | All hits grounded to file:line @bc292d84cd or live-listing evidence in the registry |

## State / next

- WS-1 rows COMPLETE (39); CTO completeness gate = the one open acceptance step
  (his validation against the census doc s.6 statement).
- 4 open UNKNOWNs (U-2/U-3/U-4/U-6), each with resolution path; 2 resolved same-session.
- MDPF_GLOBAL.T4A @a9f8f06c55 self-activates now (WS-1 tranches done) -- it fills this
  registry's dedup_stable_key TODOs for the exemplar families; my 6 WS-1 findings are
  binding constraints in it.
- Committed, NOT pushed (LANES COMMIT, INTEGRATORS PUSH -- standing).

## Do NOT (for successors)

- Do not edit _orion_vendor_asof.py from this seat (inf-tree lane, via COO).
- Do not treat the U-1 probe as a full re-SEAL (1-day/3-client sample; seal-decay rule).
- Do not read a comp-estate freshness adjective as a live claim (census-vintage).
- Any write to opal-data-bd/forwardfill_v2 after 213057Z = zombie-writer signal; surface,
  never revive. RETIRED is not a deletion warrant.
