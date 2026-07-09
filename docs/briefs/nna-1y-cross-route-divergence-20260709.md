# BRIEF: advisor-NNA 1Y cross-route divergence (leaderboard vs canonical)

**Date:** 2026-07-09
**From:** 0.7.0_AE_CloudOps (surfaced during the NFRA_GCONTR advisor-intelligence-nna sign-off verify)
**To / owner:** 0.4.0_DS_ClientPlatform (bd/ADVI gold lane — D_00c / D_00f / C_07)
**CC-relevant:** 3.0.0_SA_CVO (owns the advisor-intelligence-nna GCONTR value-limb F-1 that catches this)
**Class:** grounded finding + hand-off (read-only investigation; the fix is DS/bd-lane per Rule 13)

## The finding

The advisor-NNA cross-route identity invariant (GCONTR F-1: per-advisor NNA identical across the
canonical + leaderboard routes for a given window) **passes on 4 of 5 windows but FAILS on 1Y.**

Live sweep, both served artifacts fresh today (leaderboard `platinum/firm/leaderboard.json`
regenerated 10:18Z; canonical `platinum/firm/advisor_nna_canonical.json` 10:32Z):

```
QTD : 154 matched, 0 divergent
YTD : 158 matched, 0 divergent
MAX : 158 matched, 0 divergent
3Y  : 158 matched, 0 divergent
1Y  : 158 matched, 65 divergent   <-- worst -$1,566,083 (hunter lloyd)
```

## Why this is NOT the over-crediting you already fixed

The C_07 Layer-3 placeholder->individual inference removal (D_00c:821, C_07 `architect_no_infer`,
Andrew-decided 06-17) **is working** — that's why QTD/YTD/MAX/3Y now converge 0/158 (they used to
diverge firm-wide via the $357.6M house-book + Unassigned over-credit). This 1Y gap is a **separate,
window-specific bug**:

- If it were the attribution over-credit, it would appear in EVERY window (uniform, leaderboard>canonical).
  It doesn't — it's isolated to 1Y.
- The 65 divergences are **MIXED direction** (27 leaderboard>canonical, 38 leaderboard<canonical),
  ~3% magnitude — the signature of a **window-bound or rolling-aggregation difference**, not a
  mis-attributed advisor set.
- Canonical publishes a clean 1Y bound `{start: 2025-07-07, end: 2026-07-07}` (trailing 365d off the
  07-07 as_of). The **leaderboard artifact does not publish its 1Y window_bounds at all** (only
  `entry_count` + `summary`), so the two routes' 1Y windows can't be reconciled from the served
  artifacts — a strong hint they compute the 1Y start/end (or the flow-inclusion at the window edges)
  differently.

## The ask (DS/bd lane)

1. Trace the **1Y** net-flow computation in `D_00c.portal_leaderboard.py` (leaderboard) vs
   `D_00f.advisor_nna_canonical.py` (canonical) — pin the exact difference: window-bound start/end,
   boundary-day inclusion, or the rolling-aggregation basis (weekly/monthly/quarterly series roll-up).
   The other 4 windows converging says the shared attribution source is fine; the delta is in the 1Y
   window definition/aggregation only.
2. Align them so F-1 holds on 1Y (single-sourced window vocabulary, same as QTD/YTD/etc.).
3. Secondary hygiene: publish the leaderboard's per-window `window_bounds` in its artifact (canonical
   already does) so cross-route bounds are auditable, not inferred.

## Why it matters now

This surface is being **canonicalized** — the `advisor-intelligence-nna` GCONTR contract (SEV1,
`ratified_at: PENDING-ANDREW-SIGNOFF`) declares F-1 cross-route identity as a value-limb invariant.
Its value_check text still describes the *06-17* QTD divergence (now resolved) and does not mention
this 1Y gap. So: (a) advisor-nna's F-1 would correctly read RED today on 1Y; (b) CVO should refresh
the value_check text before ratification (drop the resolved QTD example, add/track the 1Y gap). This
brief is the grounded starting point; DS owns the trace + fix, CVO owns the contract-text refresh.

## Grounding / reproduce

- Served artifacts: `s3://opal-data-bd/platinum/firm/{leaderboard,advisor_nna_canonical}.json` (gzipped).
- Producers: `data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py`,
  `D_00f.advisor_nna_canonical.py`, shared `lib/advisor_nna_attribution.py`, upstream
  `C_07.advisor_attribution.py` (emits `architect_no_infer`, the no-inference source both now share).
- The sweep: decompress both, compare per-advisor NNA by name across each window (QTD/YTD/MAX/1Y/3Y).
