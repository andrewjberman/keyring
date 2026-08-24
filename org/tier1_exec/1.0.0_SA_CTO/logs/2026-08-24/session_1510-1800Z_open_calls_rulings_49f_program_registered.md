# 1.0.0_SA_CTO -- session 15:10-18:00Z: the six open-calls rulings; L1 order A4/A4.1; the three 49F-meeting findings recorded verbatim; the 49F program registered (INSURE / STITCH / PERFRP) with stage-2 PRDs on measured runs; CRO off the subject

**archetype:** COORDINATE
**secondary_archetypes:** SCRIBE, EXPLORE, VALIDATE

Continues `session_1422-1510Z_startup_map_49fsrc_d0brief.md` (@2f32fe15f8). Andrew at the terminal throughout.

## 1. The six /open-calls rulings (~15:2xZ) -- record @de481d0e06, broadcast 8 seats
49F sourcing HELD on Mike; ETF promote NOT YET (two conditions: full daily Bloomberg data structure for
all ETFs; DEV build with GICS -> sub-categories); TrueShares capture NOT deployed as wired -- constituents
accrue via the Bloomberg /terminal-upload pipeline structure (scoped additional script, same shape,
opal-data-etfs subfolder); history fork not relevant until Mike; gap-day backfill HOLD; constituent
layering Bloomberg-first / Pathfinder + TrueShares fill / Bloomberg enrich. Applied to
ETFS_POSITIONING (JSON + REGISTRY + PRD s.11 round-2 block), ADVI_49FSRC (HELD), the session-order map
(s.4a v0.2). Spawn order NOT inferred as ratified.

## 2. L1 order amendments (site Z) -- A4 @d27c047e70, A4.1 @2675189d2e; bus MessageId 7bc23652 (STORED, not delivered)
A4: the scoped additional script in the daily vehicle (three legs, bounds, L1-6..L1-8; retires TO-4's
laptop vehicle). A4.1 on site Z's measurement (MSTR 66223): TWO CLOCKS -- the derived layer (count,
sector/geo allocation, top-ten) needs no BQL, is CURRENT-DAY ONLY, accrues from the first run; the
constituent LIST is a BQL upgrade on his spend word only, filled by the issuer leg from day one. Plain
fact stated to Andrew: the derived layer loses a calendar day per day until the site-Z script lands.

## 3. The three 49F-meeting findings -- recorded VERBATIM, each its own file, broadcast (CRO EXCLUDED)
- Finding 1 @dbf4e493eb (+ conventions @0508a3be44, MSTR flag): ADVI for 49 on Schwab 08335338, limited
  history fine for now; Fidelity next; ADVI splits -- INSURANCE assets project (BD insurance endpoint
  snapshot; bronze/silver pattern; very light additive gold in opal-data-49financial; platinum; header
  subtext / account-level "Insurance" segment NOT Alternatives / Books-only aggregation; NEVER blended).
- DISTRIBUTION RESTRICTION @41c462cfa5 (~16:1xZ): nothing on this subject to 4.0.0_SA_CRO. Disclosed
  plainly: 66216 + 66227 reached CRO before the word; nothing after; MSTR's bridge checked clean.
- Finding 2 @a5f1acd3ad: BD history kept (backfill + SI stitching); untrusted across the 2024 Schwab
  migration; no clarified stable key; a future STITCHING project (migrated / stayed / dropped + what we
  cannot know); migrate opal-data-bd -> opal-data-assets by methodical design.
- Finding 3 @1cda24912a: the PURPOSE is per-client performance attribution + reporting on the spine;
  BD dashboard = inspiration (his screenshots + recording pending); Books tab + Book view only.

## 4. The 49F program registered + drafted -- @d9fff9a9c2 (stage 1) / @a6b91e8b78 (stage 2)
ADVI_INSURE, ADVI_STITCH, ADVI_PERFRP (dep_stage PRD; PRDs v0.1 DRAFT on runs I1-I10 / S1-S12 / P1-P8);
D2 PRD s.10 = the three-finding program shape (INSURE + STITCH as preconditions of PERFRP; MSTR 66255
observation adopted); ADVI_49FSRC narrowed per finding 1 (08335338 + Fidelity; the 08242234 union is
NOT in his words -- one question at him; history moved to STITCH). Rung-2 prior art measured before
minting: DATA_BDINSURANCE (source + auth resolved, HEAVY answered for 49F), ADVI_PERFORMANCE (method
contract, P-1..P-7 ruled -- REUSE THE ARTIFACT, DO NOT BRIEF ITS AUTHOR, in s.3), ADVI_HISTBF.
Load-bearing measurements (live parquet + s3api, denominators printed): the BD history is ours in THREE
planes (raw xlsx 2.47 + 5.24 GB; legacy silver 7,913 keys / 2.79 GB from 2020-03-06; legacy gold 73,526
keys / 32.83 GB, canonical/performance daily from 2020-01-02); dim_account_xref 6,201 rows -- 5,310 match
the current 08335338 book (7,336), 826 unresolved (all outside 0833, 808 open), 541 renumbered; legacy
universe 8,259, 6,107 in the xref, 2,152 absent; 1,817 of 2,026 Schwab-only accounts opened 2024-2026.
The account-level radial Andrew named: 0 hits / 52 files -- an open decomp cell.

## MCP traffic
Sent 13 (rulings + three findings broadcasts; restriction to MSTR/COO; ACKs; push pings). Received 4
significant (MSTR 66211 push-state; 66223 site-Z two-clock relay; 66237 restriction honored +
convention flag; 66255 the CRO-intersection constraint) -- all READ-acked and acted on.

## Compiler Tools
| tool | invocation | result |
|---|---|---|
| comp-find -i | insurance prior art (7,510 files); session/token + endpoints in data/black_diamond (176); frontend surfaces; radial/pie census (52) | PASS; two measured zeros stated with denominators |
| comp-find --name | PartnerAnalytics.tsx / AdvisorPublicProfile | PASS |
| raw s3api (rail-checked) | opal-data-bd backfill_v2 / forwardfill_v2 / bronze / silver / gold censuses by family + date; xref partitions | PASS -- materialised, IsTruncated=False |
| live parquet reads (boto3/pandas) | dim_account_xref 2026-08-21; 08335338 fact_acc date_opened | PASS |
| safe-commit -F | x8 this window | PASS (owned-paths + risk-reflex clean) |
| agentbus-sqs.sh | device + send sitez (A4/A4.1) | SENT, MessageId 7bc23652 -- not delivered until acked |

What failed: nothing. Gap: `check-inbox` CLI still not on PATH (MCP probe used); the bare `backfill/` and
`forwardfill/` prefixes are empty (the trees are `_v2`) -- named in the run so nobody censuses the wrong prefix.

## Blockers
**None at this seat.** At Andrew: the spawn order (revised Phase 2; the site-Z seat carries the derived-
layer clock); whether the 08242234 union stays in ADVI_49FSRC's scope; his screenshots + recording of the
BD Performance Reporting dashboard (PERFRP shape). Surfaced not chased: cottonwood/global served plane at
08-19 (DS cell); the ADVI_BDPARITY / ADVI_IDSPINE TO-without-JSON gap; no DAILY_SPRINT_2026-08-24.md.

## Current State -- for a reader with zero context
Fabric: MSTR, CRO, CTO live; every lane + COO + CVO closed-out; no spawn word yet. 49F: four projects under
D2 -- ADVI_49FSRC (HELD/narrowed), ADVI_INSURE, ADVI_STITCH, ADVI_PERFRP (all dep_stage PRD; packages =
PRD + run, ready for COO decomp on spawn). CRO is OFF the 49F subject by Andrew's word. ETF page: promote
NOT YET (two conditions); round-2 scope in ETFS PRD s.11; L1 order A4/A4.1 issued to site Z (unacked).
MDPF cottonwood + global served at 08-19 (DS cell). Push state: a6b91e8b78 LOCAL (1 ahead of c3ddf1a640).

## Next Steps
- **[Andrew]** spawn order; the 08242234 word; the screenshots + recording.
- **[0.0.0_AB_MSTR]** push a6b91e8b78 + this log; DIRECTIVES.yaml D2 member-set (four codes); spawns on
  his word (COO + CVO first; site Z for A4; DS; DE; AE; 0.8.0).
- **[2.0.0_SA_COO on spawn]** D1 TOs after CVO cert; ETFS round-2 decomp; ADVI_INSURE / ADVI_STITCH
  decomps (PERFRP non-shape cells); triage of the 0.8.0 inherited TOs. Carry the reuse-not-brief line.
- **[1.0.0_SA_CTO]** on his word: PRD amendments; PERFRP s.6 from the recording; the ADVI_49FSRC scope edit.
