# DS~C 2026-05-13 session 5 — Patrick NNA oscillation root-cause + Lambda forward-fill fix

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** ~17:00Z → ~17:15Z 2026-05-13 (~15 min)
**Trigger:** RD 0.4.2 URGENT brief (Andrew at console flagged): Patrick Scanlan Lifetime Activity (NNA mode, Max window, Quarter interval) shows alternating +/-$15M quarterly bars from Q3'24 onwards while AUA grows smoothly $0.5M → $20.9M. RD listed 3 hypotheses (re-attribution / double-count / walk-back drift) ranked by likelihood.

## TL;DR

**ROOT CAUSE LOCKED — none of RD's 3 hypotheses.** It's a **4th category**: sparse-day lookup miss in the Lambda's `_build_timeseries` cumsum emit. `canonical_nna` is sparse per advisor (Patrick has 696 activity days of ~2,170 total daily-series dates). Lambda computes cumsum on the sparse series + dict-lookup by date + falls back to $0 on lookup miss. Result: `timeseries.json#nna_canonical` flickers between cumulative-to-date (event days) and $0 (non-event days). FE chart computes Q-end deltas; whether each Q-end date happened to be an advisor activity day determines whether the bar shows $cum or $0. The "alternation pattern" is the deterministic pattern of quarter-end-date sparsity matching, not a flow signal.

**Fix shipped: `14c54aec2`** — replaces dict-lookup with reindex+forward-fill. Cross-advisor verified post-fix. AE brief `915910410` for the bundle (queue with v1.7.54 alongside orphan-bucket-drop `52478bb3a` + display_label inline `d12598087`).

## Per-quarter empirical proof

Patrick Scanlan canonical_nna RAW quarterly sums (ground truth — sum of `net_nna` across all 4 advisors' activity days, filtered to `patrick_scanlan`):

```
Q3'24: +$976,990    (FE showed +$15M)
Q4'24: +$1,741,728  (FE showed -$15M)
Q1'25:   -$345,487  (FE showed +$15M)
Q2'25:   -$299,948  (FE showed -$15M)
Q3'25:   -$213,573  (FE showed ~$0)
Q4'25:    -$62,853  (FE showed +$15M)
Q1'26:  +$208,692   (FE showed -$15M)
Q2'26:  +$272,275   (FE showed ~$0)
```

Per-account decomposition Q4'24: 34 distinct accounts, largest single-account inflow $640K (acct 727), no ±$15M anywhere. **The raw data is clean.**

## The bug (Lambda `inf-portal-advisor-publisher/lambda_function.py:767-815`)

L794: `adv_can['nna_canonical'] = adv_can['net_nna'].cumsum()` — produces cumulative-to-date for activity days only.

L797-799:
```python
can_lookup = ({pd.Timestamp(r['date']).strftime('%Y-%m-%d'): r
               for _, r in adv_can.iterrows()}
              if not adv_can.empty else {})
```
Dict only has entries for activity days. Non-activity days are missing.

L804: `can = can_lookup.get(date_str, {})` — returns `{}` for missing dates.

L811: `'nna_canonical': round(float(can.get('nna_canonical', 0.0)), 2)` — falls back to $0.

**Effect**: emitted `nna_canonical` flickers between $cum and $0 day-by-day. FE plots Q-end values, diffs adjacent quarters → +/-$15M alternation pattern.

## Quarter-end sparsity table for Patrick (current S3)

```
2024-09-30 (Mon) — in adv_can      → cum = $13,067,184      → chart shows $13M
2024-12-31 (Tue) — NOT in adv_can  → lookup miss → $0       → chart shows $0
2025-03-31 (Mon) — in adv_can      → cum = $14,463,425      → chart shows $14M
2025-06-30 (Mon) — NOT in adv_can  → lookup miss → $0       → chart shows $0
2025-09-30 (Tue) — NOT in adv_can  → $0
2025-12-31 (Wed) — in adv_can      → cum = $13,887,050      → $13M
```

Pattern of "in adv_can / NOT in adv_can" at quarter boundaries IS the alternation source. Not a flow signal.

## Why RD's 3 hypotheses don't apply

1. **Re-attribution artifact** — would show as paired +/− entries in canonical_nna. Doesn't exist; per-account decomp shows clean values.
2. **Double-counting by source_system** — would inflate canonical_nna totals. Doesn't exist; totals reasonable.
3. **Bronze-walk window drift** — would show as identical flow appearing +X / −X in adjacent canonical_nna periods. Doesn't exist; canonical_nna sums to correct quarterly totals.

All 3 are upstream-of-Lambda hypotheses. The bug is IN the Lambda's emit code, downstream of canonical_nna.

## Fix (commit `14c54aec2`)

Replaced `can_lookup` dict with `reindex(daily['date']).ffill().fillna(0.0)` so days without canonical_nna events retain the prior cumulative-to-date instead of returning $0.

```python
can_lookup: dict = {}
if not adv_can.empty:
    adv_can_ffilled = (
        adv_can.set_index('date')[['nna_canonical', 'inflows_canonical', 'outflows_canonical']]
        .reindex(daily['date'].values)
        .ffill()
        .fillna(0.0)
    )
    can_lookup = {
        pd.Timestamp(d).strftime('%Y-%m-%d'): r
        for d, r in adv_can_ffilled.iterrows()
    }
```

22 insertions / 3 deletions on one file. No schema change. Backward-compatible.

## Phase 3 sentinel (post-fix, replicated against live S3)

Patrick (all 25 quarters monotonic, deltas match canonical_nna raw EXACTLY):
- Q3'24 cum=$13,067,184 Q-delta=+$976,990
- Q4'24 cum=$14,808,912 Q-delta=+$1,741,728
- Q1'25 cum=$14,463,425 Q-delta=-$345,487
- ... (all 25 quarters verified)

Cross-advisor:
- Peter Lee: cum $92M (24Q3) → $107M (26Q2). Q-deltas $-1.3M to +$7.1M. Sensible.
- Joe Brandenburg: cum $8-10M range. Q-deltas $-248K to +$1.47M. Clean.
- IWM-catchall: cum -$719K to +$2.2M (negative during reorg). Sensible.

No advisor shows ±$15M alternation post-fix.

## Compiler Tools

| Tool | Runs | Result |
|---|---|---|
| `ds-commit-gate.sh inf-portal-advisor-publisher/lambda_function.py` | 1× | PASS — py_compile + ds-precommit + ruff py39 clean |
| `safe-commit.sh --author 0.4.0_DS_ClientPlatform~C` | 2× (Lambda fix + AE brief) | Both clean first-try |
| Live S3 5-source diagnostic — canonical_nna raw + timeseries.json + per-account decomp + Q-end sparsity check + replicate-Lambda-with-fix | 1× | Root cause locked in ~10 min; cross-firm sentinel verified before commit |

## Files Modified

| File | Change | Commit |
|---|---|---|
| `infra/aws/lambda/inf-portal-advisor-publisher/lambda_function.py` | `_build_timeseries` reindex+ffill replaces dict-lookup | `14c54aec2` (+22/-3) |
| `docs/briefs/ae-brief-inf-portal-advisor-publisher-nna-cumsum-ffill.md` | NEW AE brief for the bundle | `915910410` (+77) |

## Sequencing handoffs

| Recipient | Item |
|---|---|
| **RD 0.4.2_RD_AdvisorIntelligence** | RAVC2 sent 17:12Z with empirical root cause + per-advisor sentinel + commit hashes. Brief CLOSED my side modulo post-deploy visual smoke. |
| **AE 0.6.1_AE_PartnerETL** | FYI: 3rd commit added to inf-portal-advisor-publisher bundle queue. 3 commits non-overlapping in same file. Single build-and-upload + terraform apply. Fire Lambda invoke explicitly post-deploy (chain bypass per INFPUBLISHERDEDUP). |
| **COO 2.0.0_SA_COO** | No new MCP — bundle sequencing is your call with AE 0.6.1 (Path A vs B unchanged). |
| **Andrew (via RD)** | Root cause not in his/RD's hypothesis list; new category (sparse-day lookup miss). Visible fix awaits AE bundle ship. |
| **DS~C self** | Idle modulo bundle deploy. Cross-firm BD audit open as follow-up if greenlit (would check `bd-portal-advisor-publisher` for the same cumsum + dict-lookup pattern). |

## Decision notes (worth keeping)

1. **Layer-by-layer diagnostic beat hypothesis-list-walk.** RD listed 3 specific hypotheses; I could have spent 30 min checking each. Instead: pulled raw canonical_nna → checked totals → confirmed clean → traced upstream of Lambda → found the bug in the emit code. ~10 min total. The right cadence when you have a "downstream looks broken, upstream looks fine" mismatch.

2. **Sparse-series + dense-iteration is the bug pattern.** General lesson: when you've got a sparse dataset (events) and you're emitting daily values that depend on cumulative state, dict-lookup + fall-back-to-0 produces flickering output. Either reindex+ffill (this fix) or use merge_asof / merge with `direction='backward'`. Memory'able pattern beyond this incident.

3. **Pre-ship empirical verification, not just unit-test.** Re-ran the FIXED Lambda function against live S3 data for all 4 advisors. Matched canonical_nna raw sums exactly across 25 quarters for Patrick + sensible numbers for the other 3. Catches "fix that compiles but produces wrong numbers" before it reaches the chain.

4. **Bundle commits when you have non-overlapping function edits.** 3 commits to `inf-portal-advisor-publisher` in same file (orphan-bucket-drop in `_client_list`, display_label inline in `_build_top_holdings`, NNA ffill in `_build_timeseries`) → one terraform apply. Saves AE 2 apply cycles and 2 verification windows.

5. **The "4th category" beyond brief's hypotheses is worth flagging explicitly.** RD's 3 hypotheses were all upstream-of-Lambda. The actual bug was in the Lambda's emit. When confirming a bug, name the category that DIDN'T appear in the brief; helps RD calibrate their own diagnostic framing for future briefs.

## Pacing

15 min from URGENT brief receipt to RAVC2 sent + commit shipped + AE brief filed. Andrew-at-console + fast-turnaround pattern. Empirical-first diagnostic produced a definitive root cause and a verified-pre-ship fix in a single iteration.
