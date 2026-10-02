# ETFS_RIVALS closer trace, Andrew's three calls, and the two rivalfunds briefs -- 4.0.0_SA_CRO~RV

**archetype:** MIXED
**secondary_archetypes:** TRACE, SCRIBE

**Date:** 2026-10-01 15:51Z to 2026-10-02 ~04:00Z
**Task Order:** none. Andrew-direct work in the terminal; no task order held (to-check: 0 of 3947).
**Status:** COMPLETE. Wound down on Andrew-direct ~03:4xZ via `0.0.0_AB_MSTR~Z` msg 28186 (disk at 100%).
**Workspace CLOUD commits (this seat):** b7622c0b5a, 4add024498, b1e877a1c6, 381bec5549, 19c5277a57, 52eb8a5dc7, and this
log's commit. All LOCAL at the last read (origin/CLOUD 0abf99fcd4, ls-remote read ~18:0xZ); push state not re-read since.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find 'CRO~RV' <spawn log, liveness, LIVE_ARMS>` | PASS | 2 hits / 3 files: the lane had only my own registration |
| comp-find | `comp-find -i 'openai\|...\|outcome_rollup' data/etfs/scripts/rivalfunds infra/aws/lambda/etfs-pipeline` | PASS | 0 hits / 71 files: G7-G13 and the AI step have no code |
| comp-find | inception regex for IDVZ/PFOE | PASS | 64 hits; gave PFOE launch 2025-12-31; IDVZ launch not found |
| comp-find | `--name '*fear*greed*'`, `'*news_scanner*'`, `'*harvest*'` | PASS | located the fetcher config, the news scanner deep dive, AMGT_HARVST |
| opal_discover | three subjects | PASS | sentiment catalogued (news.03); rival funds NOT catalogued |
| to-check | `--all --assignee 4.0.0_SA_CRO~RV` | PASS | 0 active |
| rail hook | raw grep / `aws s3 ls` on served prefixes | REFUSED | rerouted to comp-find, or marked `# rail-checked` for single known files |

**What worked:** boto3 read-only censuses over the served gold (502 G2 objects, 501 G5/G6) gave every method and coverage
figure with a printed denominator. opal_discover gave the catalog's own caveats on the sentiment stores.
**What failed:**
- A signed-out probe of `mcp.opalinvest.dev/rivalfunds` returns 302 for every path, including a nonexistent one, so it
  is undiscriminating.
- A whole-corpus comp-find timed out at 120 s and finished in the background.
**Gap:** no instrument reads a signed-in MCP page; the live thread remains Andrew's own read.

---

## Work Completed

1. **Startup:** `/watcher` (the lane registered, the Monitor re-armed on every 30-minute expiry), `org/XXX.md` A-F. Zero
   crons.
2. **`/closer trace ETFS_RIVALS`** (Andrew-direct @b7622c0b5a): 13 hops from ingestion to the MCP page. Brief
   `deliverables/ETFS_RIVALS_END_TO_END_GAP_BRIEF_20261001.md` and evidence JSON @b1e877a1c6. Findings:
   - equal-value swaps erased as ID-CHANGE (PFOE Universal Music -> Quanta; IDVZ UBS -> Lenovo);
   - an unbounded flow factor (INEQ f=0, 102 false trades on each of two windows);
   - the enrichment step a no-op that logs "landed": surprise row ETFS_RIVALS-Z-S10 @4add024498, BLOCKING/ARMED, fixed
     by COO~RV in RIV-v-2 amendment 3;
   - IDVZ/PFOE at 22 reports against rivals' 91-501;
   - GICS sector fill 0% on six funds;
   - G7-G13 absent.

   The CTO ruled hop 9 (a), (b) and (d) into round 5 (@4baf852611); all three are now complete.
3. **Correction @381bec5549:** my first call-1 source (Black Diamond/COT custodial cubes) was wrong. Those cubes hold
   client accounts' PFOE units, and cot is a separate firm. The CTO caught it (msg 28012); the correction is written out
   in the brief.
4. **Andrew's three answers recorded** @19c5277a57: IDVZ/PFOE into the Bloomberg queue; ACWI and IWM as the controls;
   no peer criteria. They landed as PRD v0.8.
5. **Two midstream L1 briefs** @52eb8a5dc7, with the verbatim record of both transcripts:
   - `docs/briefs/rivalfunds-backend-data-ai-synthesis-20261001.md`;
   - `docs/briefs/rivalfunds-frontend-mcp-page-20261001.md`.

   The CTO cut FWD-13..20 from them (v0.9). Andrew confirmed them ~02:2xZ (v0.10 @ed31270000), CVO-signed @807ca60066.
6. **`/open-calls`:** zero open calls at this lane. All three calls were answered in the CTO terminal at ~02:2xZ.

## MCP traffic

| Msg | Peer | Content |
|---|---|---|
| 28010 out | 2.0.0_SA_COO~RV | row Z-S10, disarm ask |
| 28011 out | 1.0.0_SA_CTO~Z | rule on hop 9 (a), (b), (d) |
| 28012 in | 1.0.0_SA_CTO~Z | ruled; the call-1 source hazard |
| 28015 in | 2.0.0_SA_COO~RV | Z-S10 ruled into v-2 amendment 3 |
| out | 1.0.0_SA_CTO~Z | two record pointers |
| 28186 in | 0.0.0_AB_MSTR~Z | wind down |

Every inbound message was acked.

## Blockers

None at this seat.

## Current State

- ETFS_RIVALS is executing round 5 (h-4, h-5, h-6, b-2 and f-4 complete; m-2, s-6 and l-1 open at the last read). Round
  6 carries the backfills and Addendum B.
- The served page of 2026-10-01 reads 12 of 13 funds current (GQGU behind on freshness).
- G3 and G4 each hold one date until the fixed enrichment's first scheduled run.

## Next Steps

1. **[4.0.0_SA_CRO~RV, next session]** Nothing is owed. On request, re-read the round-4/5 hops of the trace after round
   5's live join.
2. **[2.0.0_SA_COO~RV]** Tomorrow's three-leg morning read (round-4 analysis section 3), the first scheduled enrichment
   pull included.
