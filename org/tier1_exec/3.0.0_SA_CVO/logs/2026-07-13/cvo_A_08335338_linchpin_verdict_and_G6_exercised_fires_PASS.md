# CVO~A -- OPAL_ASSETS validation tail: the 08335338 LINCHPIN verdict (PIT snapshots CONFIRMED, 2021 NOT reachable) + the G6 exercised-fires PASS (per-cohort alarms live + discriminating)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

**Window:** 2026-07-13T00:24Z (last log b4f1643b8) -> ~00:40Z. 0 commits (verdict work -- evidence in scratch responses + alarm history + the MCP record). Both verdicts delivered + triple-accepted.

## 1. The 08335338 linchpin verdict (FP-R1-classed; gates CTO~B's G2/G3 PRD)

0.7.0's live SDD REST enumeration (6932 file-detail rows, read-only): **LINCHPIN CONFIRMED [OBSERVED]** -- master
08335338 is fully enrolled and serves DIRECT daily PIT position products ("Cost Basis Daily UGL Open Positions"
taxable+non-taxable, "UGL Open Lots", "Core Reconciliation Position"), DISTINCT file types from the transaction
products -- positions-as-of, NOT TRN-reconstruction. Suite + date range IDENTICAL to 08242234 => **G2 collapses to
"the proven ingest pointed at a second master."** Andrew's canonical-Schwab-derived thesis has its empirical
foundation. **LOOK-BACK [OBSERVED]: 2023-07-12 floor (~3yr), NOT 2021** -- flagged to Andrew (deeper = a
vendor/human channel decision); silver lining: the REST floor is ~6mo earlier than our held 08242234 depth
(2024-01), so G3 extends the existing master too. **One claim capped INFERRED per my own FP-R0** (the file's
column content -- a what-the-artifact-contains dynamic question): closing via 0.7.0's ONE bounded content-confirm
download (triple-endorsed: me 002542Z / COO w/ a structure-not-extract sovereign-care boundary / MSTR "squarely
within Andrew's GO; don't expand"). **D1 rides the same read** (does 08335338 carry DIVZ/IDVZ/PFOE/PFDE -> the 49F
ETF custody attribution). Format corrected for the record: {master}.CRS{yyyymmdd}.{CODE}.zip; and the two-channels
precision held (2024-01 = held delivery-channel depth; 2023-07-12 = live-REST reach -- different questions, both right).

## 2. G6 exercised-fires verdict: PASS all 6 (triple-closed: COO 003855Z, CTO~B 003829Z, AE~A 003837Z)

AE~A built (46d8be80d + TF alarms, mdpf-pipeline-v1.5.0); I exercised per my protocol (80bc2d51c) + fixtures (0b715fc9f):
- **A1 fires-on-stale:** LIVE -- 12 of 14 mdpf-cohort-freshness-stale-* alarms in ALARM on PROD truth (8x49F
  rolled_forward/5, cohort-8 incomplete/99, DIVZ-IDVZ/3, inflection/1) + the INSUFFICIENT_DATA->ALARM history;
  FIXTURE -- one-stale moved ONLY etf_divz (3 >= ETF threshold 3).
- **A2 silent-on-fresh:** fresh-all -> ALL 14 = 0/fresh, nothing fires.
- **A3 discrimination:** LIVE -- PFOE/PFDE (staleness 2 < 3) stay OK while 12 fire, running in prod NOW; FIXTURE --
  mixed: 49F cohorts stale, inflection 0, ETFs 0.
- **A4 rolled_forward ages** on the OLD as_of (state in the response/log per the no-State-dimension design).
- **A5 missing = explicit 99** (never no-datapoint; treat_missing_data=breaching reserved for dead-checker):
  inflection missing/99; cohort-8 incomplete/99 with the self-describing detail "expected sub-source(s) not
  represented: 08335338 (G2 wires this)" -- the standing silent-gap alarm, live from day one as predicted.
- **A6 never-blocks:** exercised historically -- the chain GENERATED the 07-10 partition at 14:53Z while the global
  alarm had been ALARM since ~07-09; the checker is a separate monitor Lambda.
- **Integrity:** every fixture response echoed its exact _g6_fixture partition_key (seam proven); final no-override
  invoke re-emitted prod truth; PFOE/PFDE verified OK after (nothing corrupted). Sovereign-clean (served artifact +
  taxonomy constant only).
- **HONEST DISCLOSURE (mine):** 1 of 11 fixture assertions was MIS-AUTHORED -- I expected cohort-8=0 in mixed, but
  partner_multi_master rides as_of_by_partner[49financial] -> correctly rolled_forward/3 (99 reserved for
  master-ABSENT). Tool right, expectation wrong, corrected after re-grounding the spec (fixture-fidelity again).
- **Cleanup correctly gated:** my `aws s3 rm` of the 4 fixtures was DENIED by the S3-deletion human-confirmation
  gate -- did NOT retry/force; flagged; AE~A is leaving them as the re-exercise pack (inert, _g6_fixture:true);
  COO routes the delete-confirmation low-pri.

**Net: G6 = the OPAL_ASSETS P0.1 observability floor, LIVE.** The 14 per-cohort alarms double as the OPAL_ASSETS
progress dashboard (CTO~B is writing the PRD acceptance section around it: each G-item's DONE = its cohort alarm
clearing on prod truth -- G1 clears the 8 49F alarms; G2 clears cohort-8's).

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| aws lambda invoke (the REAL deployed checker, 4 fixture + 1 prod-restore) | exercised | PASS -- StatusCode 200 x5, per-cohort states asserted |
| aws cloudwatch describe-alarms/-history | live alarm grounding | PASS -- 12/14 ALARM + transitions + PFOE/PFDE OK integrity |
| g6_fixture_generator (mine, 0b715fc9f) | regenerated time-consistent fixtures | PASS |
| safe-commit/commit-gate | n/a this window (no commits) | -- |

- What worked: the live-prod state exercised A1/A3 more strongly than fixtures could (real transitions, real
  discrimination); fixtures covered the semantics prod couldn't (fresh-silence, missing-99).
- What failed: my cohort-8 mixed expectation (corrected, disclosed); the CLI v1 --cli-binary-format flag (v2-only, retried v1 syntax).
- Gap found: none in the tool under test; the S3-delete confirmation gate worked exactly as designed on ME.

## 3. VERDICT FINALIZED same window (0.7.0's exercised sample landed 003926Z; my finalize 004051Z)

- **CONTENT: INFERRED -> OBSERVED.** The 08335338 UGL Open Positions file IS a genuine PIT snapshot: pipe-delimited
  CBUGL (codes UPT taxable / UPN non-taxable; internal CBUGLPTX/CBUGLPNT), one row per (account, security) as-of
  Business_Date, columns Account ID + Ticker + CUSIP + ISIN + Quantity + market-value/UGL; ~93K position rows. NOT
  TRN-derived. Andrew's thesis proven END-TO-END for the BD master.
- **D1 RESOLVED = SPLIT:** all four Opal ETFs are IN 08335338 (~22K position rows; CUSIPs verified) AND the held
  08242234 RPS carries ~$153M DIVZ -> 49F Opal-ETF custody SPANS BOTH masters; both-masters-dedup is the CONFIRMED
  composite design (Andrew's map attribution half-right, the estate's half-right, the truth is both).
- **G2 honestly refined** from my "collapses" framing: the PULL generalizes (proven), but the position PARSER is NEW
  (CBUGL != the SmartX RPS layout) -> G2 = proven pull + new CBUGL converter + cohort wiring.
- **Depth final: 2023-07-12 (~3yr) both masters; 2021 = Andrew's vendor-channel call.**
- COO's structure-not-extract sovereign boundary HELD (transient inspect, summarized, not landed, box cleaned).

## Blockers

None. The OPAL_ASSETS DISCOVERY phase is COMPLETE end-to-end.

## Current State (handoff)

- G6 CLOSED all sides (AE~A: deployed mdpf-pipeline-v1.5.0, ledger 4/4; me: verdict PASS; COO captured; CTO~B: DONE
  in PRD -- and writing the acceptance section around the alarm-dashboard).
- 08335338: verdict FINAL + fully OBSERVED (capability + content + D1-split + depth) -- delivered to MSTR/COO/CTO~B.
- 4 inert fixture JSONs at s3://opal-data-portal-v2/platinum/mdpf/_g6_fixture/ = the re-exercise pack (AE~A keeping;
  delete-confirmation routed low-pri by COO).
- OPAL_ASSETS PRD (CTO~B): discovery set COMPLETE + fully OBSERVED; synthesis after the AoR go-live.

## Next Steps

- **[me]** available for CTO~B's PRD scoping + any exercise gates the PRD defines. Validation lane clear.
- **[1.0.0_SA_CTO~B]** the OPAL_ASSETS PRD synthesis (all inputs in).
- **[Andrew]** the build gos: G1 (49F feed freshness) + G2 (08335338 ingest w/ the new CBUGL parser) + the 2021
  vendor-channel decision.
