# DS Session Log -- inf served-AUM investigation + INF_B_00 short-position fix

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE
**serial:** 0.4.0_DS_ClientPlatform | **date:** 2026-06-29 | **window:** since log `71dd63d36` -> now (~20:10-22:15Z)

> SCOPE NOTE (Andrew-direct): this log covers the WORK PERFORMED only. It does NOT draw a
> conclusion about WHY the inf positions numbers differ between the morning-scheduled pull and a
> manual evening pull -- that question is OPEN/UNPROVEN and is deliberately not concluded here.

## Summary

Picked up the Inflection (inf) served-AUM defect rerouted from COO (originally dispatched to DS~B,
which had session-closed). Reported state: portal `platinum/firm/header_metrics.json` total_aua
showed $202.7M while Orion's dashboard showed $200.99M. Traced the inf positions pipeline layer by
layer against live S3, found + fixed a short-position drop in the INF_B_00 gold producer, ran a
manual full-chain rebuild, surfaced the pull schedule, and held a proposed schedule change pending
an Andrew decision.

## Work done (this window)

| # | Item | Detail | Outcome |
|---|---|---|---|
| 1 | Layer-by-layer grounding | boto3 reads of header_metrics.json, bronze/positions/, silver positions_mv, gold canonical_holdings, the perf tables | values documented per layer (Current State) |
| 2 | INF_B_00 short-position fix | `INF_B_00.canonical_holdings.py:282` filter `current_shares > 1e-9` -> `.abs() > 1e-9` (retains 8 negative-share/short rows summing -$129,678.45) | committed 07bc375d2 + deployed s3://opal-data-inf/code/gold/; ds-commit-gate PASS |
| 3 | Manual full-chain rebuild | forced positions pull (313 hh) -> silver positions_mv -> INF_B_00 -> INF_C_00 -> INF_C_03 -> INF_C_02 -> INF_D_00 | values landed (Current State); served header rebuilt |
| 4 | Schedule grounding | located inf positions pull EventBridge schedule | `inf-api-positions.tf:182` = `cron(50 12 * * ? *)` (12:50 UTC) |
| 5 | Coordination | RAVCs: COO, CTO, 0.6.0 (xref close-out), 0.7.0~A (timing HOLD), 0.8.0~B (freeze-monitor field provide) | see MCP |

## Grounded observations (facts only -- no causal conclusion)

- `bronze/positions/` daily sum(currentValue): 06-22 $204,391,897 | 06-23 $204,212,979 | 06-24
  $202,196,223 | 06-25 $202,319,889 | 06-26 $203,001,710 | 06-27 $202,582,216 | 06-28 $202,582,216 |
  06-29 $200,987,116 (the 06-29 value is from a manual forced pull I ran ~21:26Z; it overwrote that
  partition).
- The pre-fix INF_B_00 gold sum was $201,116,794.04; the raw pull + silver positions_mv sum was
  $200,987,116. The delta ($129,678.45) equals exactly the 8 negative-share rows that the `> 1e-9`
  filter excluded. After the `.abs()` fix, gold canonical_holdings_2026-06-29 = $200,987,115.59.
- $200,987,116 matches the Orion dashboard figure Andrew reported.
- I make NO claim about why the morning-scheduled vs evening-manual pulls returned different totals.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-which | "what produces inf positions_mv + the bronze pull" | routed | -> pipescript --resource / comp-pipescript io |
| comp-pipescript io | INF_B_00.canonical_holdings.py | PASS | reads bronze/orion-api + silver/api_dims/positions_mv |
| pipescript --resource | silver/api_dims/positions_mv | (no thread) | resource not in a named thread |
| ds-commit-gate | INF_B_00.canonical_holdings.py | PASS | py_compile+AST+ruff clean |
| safe-commit / aws s3 cp | 07bc375d2 + code/gold deploy | PASS | committed + staged to EC2 code prefix |
| boto3 (direct S3) | every layer read + the diff that located the 8 negative rows | PASS | the grounding spine |

**What worked:** boto3 layer-by-layer grounding located the exact $129,678 (the 8 short rows) and
confirmed the fix ties the gold to the reported Orion figure. **What failed:** n/a. **Gap found:**
`INF_D_00e.fresh_header_supplement.py` writes a SEPARATE `platinum/firm/header_metrics_fresh.json`
(in my run it read a stale 06-12 bronze assets.csv) -- flagged as a possible orphan for review.

Compiler-tools-log line appended.

## MCP traffic

~15 handled. Significant: COO (inf-AUM reroute + the 2-lane provide nudge), CTO (revert-direction then
REVERSED-hold after my ground-truth), 0.7.0~A (timing-change HOLD, ack'd), 0.8.0~B (freeze-monitor
served-field provide).

## Blockers

None open. The inf positions-pull schedule change is HELD pending an Andrew decision (a pending
decision, not a blocker).

## Current State (handoff)

- **INF_B_00.canonical_holdings.py** (07bc375d2, deployed s3://opal-data-inf/code/gold/): line 282
  now `pos[pos['current_shares'].fillna(0).astype(float).abs() > 1e-9]` (retains shorts).
- **gold/canonical/holdings_2026-06-29.parquet** = $200,987,115.59 (11,416 rows).
- **silver/api_dims/positions_mv/snapshot_date=2026-06-29** = $200,987,115.59 (from the manual ~21:26Z
  forced pull, which overwrote the partition).
- **served platinum/firm/header_metrics.json** total_aua = $202,582,215.84 after the manual chain
  rebuild (C_00->C_03->C_02->D_00).
- **inf positions pull schedule:** `inf-api-positions.tf:182` `cron(50 12 * * ? *)`. A proposed change
  to `cron(30 13 * * ? *)` was routed by COO to 0.7.0~A then HELD at my request, pending Andrew's
  decision (T-1 vs current-day) -- OPEN, unconcluded.
- **Flagged for review:** INF_D_00e.fresh_header_supplement.py (separate _fresh.json artifact, read
  stale 06-12 bronze in my run).

## Next Steps

- **[0.4.0_DS_ClientPlatform]** await Andrew's decision on the inf positions-pull schedule; send 0.7.0~A
  the exact cron once decided; verify the served number per the decision. Then: DATEMODE-B nightly
  verify + S10 emit-wire (still queued).
- **[0.7.0_AE_CloudOps~A]** holding the inf-api-positions.tf timing change (ack'd) until the cron is confirmed.
- **[0.8.0_AE_CloudComp~B]** freeze-monitor served-field provide delivered (value field = total_aua;
  flagged a market-calendar-gate requirement).
- **[2.0.0_SA_COO]** the CVO parity post-06-29 schwab canonical run -- flagged it needs a DS~B respawn (bandwidth).
