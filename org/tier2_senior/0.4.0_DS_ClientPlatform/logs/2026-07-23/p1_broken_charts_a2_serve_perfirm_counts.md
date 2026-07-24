# P1 broken-charts joint review + A2 serve + W-7 per-firm counts (2105Z-2150Z)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, IMPLEMENT

## Window

Since 653df1a2f (~2105Z) -> ~2150Z. 1 commit (3efc9dc6d), 3 serve events (W-7 /global/
byte-copy, A2 one-key serve, 3x per-firm count publish), ~8 MCP messages handled (COO W-7
serve-fix + byte-confirm, CTO A2 GO, CTO P1 + addendum + acceptance).

## What happened

1. **W-7 SERVE FIX (COO 211752Z, P2 producer/consumer-parity class):** DE's parity gate found
   my W-7 count artifact published to the top-level json/mdpf/aggregate-aua-timeseries.json,
   which NO Global consumer reads -- the consumed key is the /global/ SIBLING. Pre-copy
   field-check (no /global/-only fields; strict superset), byte-copied 55a8b379 -> /global/,
   COO byte-confirmed independently (co-sign TRANSFERS). Class banked with COO acceptance:
   the publish set must be DERIVED from DE's read-surface enumeration (two same-night
   instances: this + W-6's bell legacy key).
2. **A2 SERVE (CTO 212002Z GO):** shape-compat pre-check FIRST at the bytes -- the revamp
   aum-timeseries carries the IDENTICAL field contract the FE reads (aum.ts:403-407 +
   ModelPortfolios.tsx:384 roll-forward); named density delta 547 weekend-filled -> 447
   trading rows (roll-forward handles by construction). VINTAGE FINDING: the consumed legacy
   copy's CONTENT frontier was 2026-05-29 (55-day-frozen, SmartX-only $1,404M). Refreshed the
   revamp producer (dim_mdpf_aum_timeseries.py, identity PASS, cottonwood-inclusive
   $1,637,144,180.01 @07-22), served json/portfolios/aum-timeseries.json ETag
   f96cfc4381d20ad1aae5927be1c73b4f, pre-A2 legacy bytes audited at
   gold/mdpf_revamp/_audit/legacy_aum-timeseries_pre-a2_20260723.json. 0.7.0's disable flag
   #3 rides this (HELD pending the P1 resolution per CTO).
3. **P1 JOINT REVIEW (Andrew-direct: Global Daily AUA Trend + Period End broken values AND
   counts) -- DS half grounded (213836Z):** read-paths pinned at portal DEV @af0867e9 (148).
   Global trend VALUE data DID NOT change tonight (the two /global/ publishes carry
   byte-identical value arrays) -> value break is RENDER/CACHE side: (i) 147/148 anchor
   total_aua = partner_custody_total, which the GLOBAL artifact omits BY DESIGN (shape
   parity), or (ii) CloudFront/staleTime serving the pre-count 8b6de1d5 to 148 code. A2
   rollback NOT indicated (the A2 key feeds only the :384 roll-forward cards on Global --
   a lawful 55-day unfreeze that reads "mismatched" beside the $1.95B trend = axis-label
   obligation). CTO accepted all dispositions (213931Z).
4. **THE ONE GENUINE DATA DEFECT, closed @3efc9dc6d:** 148's per-firm count reader (:746)
   consumed account_count_total/count_provenance, which existed ONLY on the global artifact.
   Added compose_count_total() (shared composer, same no-partial law, per-artifact build
   assertion; new honest class 'source_absent' for count-source-has-no-cell) to 49F + INF in
   the spine and inline to the COT band. Published byte-verified: 49F md5 501407448f...
   (408 valued/21 None, frontier 7,026 frontier_stamp), INF e3c8db35... (423/6, frontier 534),
   COT 194e5bb0... (2 valued/445 source_absent). Served global untouched (co-signed 55a8b379
   stands; rebuild differs by generated_at only).
5. **Addendum axes pinned to exact numbers:** Andrew's "7.03k vs 7,041" = 7,026 (49F roster-
   stamp at frontier, timeseries) vs 7,041 (49F funded-distribution, bell) -- fifteen accounts,
   two NAMED axes; label fix, not a defect. COT counts = distinct-294 law, blended-satellite
   folding carried in meta.cottonwood_fold. Disclaimer scope = per-quantity vintages
   (count_coverage_end 07-18 vs as_of_last 07-22, both already in meta) -- DE wording.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-grep | mdpf_revamp/portfolios/aum-timeseries | PASS | found the A2 producer (dim_mdpf_aum_timeseries.py) in one call |

Plus direct code pins in portal/ (scoped, returned to base) for the P1 read-paths -- the
comp-cache/graph route was not needed; DE co-owns the render half. No gaps found this window.

## Briefs Written (DS)

| Deliverable | Path |
|---|---|
| P1 DS-half grounding + A2 shape-compat + addendum axes | MCP 213836Z / 212706Z / 214834Z (fabric record) |

## Blockers

None BLOCKED. Held-on-others: DE's cache-clean render evidence decides (i)-vs-(ii) on the
Global values; flag #3 + 148's promote queue behind it (CTO order). The 13:00Z smartx-Lambda
clobber owner still open from the prior window (json/portfolios/account-distribution.json AND
now aum-timeseries.json + aum-metrics.json -- flag #3 covers all three once flipped).

## Current State (zero-context handoff)

- SERVED (opal-data-portal-v2): json/mdpf/global/aggregate-aua-timeseries.json = 55a8b379
  (co-signed, counts present); per-firm 49F/INF/COT keys = 501407/e3c8db35/194e5bb0 (counts
  present, first time); json/portfolios/aum-timeseries.json = f96cfc43 (A2, 07-22 frontier,
  cottonwood-inclusive); aum-metrics 9bae4b42; account-distribution 14d668ef both keys.
- AUDIT: pre-A2 + pre-W6 legacy bytes under gold/mdpf_revamp/_audit/.
- CODE: spine + band + verifier at HEAD 3efc9dc6d (pushed); mutants 8/8; verify battery all
  conditions PASS. Portal DEV @af0867e9 (148) is DE's lane.
- OPEN: DE render evidence -> CTO P1 close -> 0.7.0 flag #3 -> 148/149 promote. My clocks:
  07-24 ~0210Z 6d-wiring check; 1347Z INF chain clear.

## Next Steps

1. [0.4.0_DE_ClientPlatform] cache-clean render evidence on the Global elements; fallback fix
   if (i); axis/vintage/disclaimer labels (data + meta ready on every artifact).
2. [0.7.0_AE_CloudOps] flip disable flag #3 on CTO's P1 close (covers the three portfolios keys).
3. [0.4.0_DS] 07-24 clocks (0210Z 6d block, 1347Z INF chain); W-1/W-5 on COO's TOs; generation
   contracts on DE's enumeration.
