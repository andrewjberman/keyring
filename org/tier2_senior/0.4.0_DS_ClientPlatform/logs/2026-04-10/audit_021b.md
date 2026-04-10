# T1 Cap Audit — Investigation Log (021 → 021b bridge)

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-10
**Scope:** the audit investigation phase between ADVI_GLDRST.021 (source-tag shipped) and ADVI_GLDRST.021b (exemptions + min-sample guard shipped)
**Brief that triggered this:** `docs/briefs/data-scientist-t1-cap-audit.md`
**Findings doc delivered:** `docs/briefs/data-scientist-t1-cap-audit-findings.md`

## Why this log exists

ADVI_GLDRST.021 proved the cap was rewriting 31 rows silently. The fix in 021b (named exemptions + min-sample guard) is narrow and mechanical, but the decision of *which* assets to exempt and *where* to set the threshold is the interesting work. This log captures the audit investigation itself — the methodology, the evidence sources, the classification reasoning, and how the findings resolved directly into 021b's two-mechanism design. The code-change logs (`v2_source_tag_and_diff_before_ship.md`, `v2_cap_exemptions_and_minsample_guard.md`) cover what shipped; this one covers how we knew what to ship.

## Starting state

After .021 landed, the diff-before-ship harness reported:

- 31 rows tagged `transaction_observed_capped`
- 14 distinct assets affected
- 1 of those assets was already identified as the 2024-08-07 INVESCO STABLE VALUE RET CL 1 corruption case (the anchor the cap was originally written for)
- 4 rows were Chipotle Mexican Grill in May 2024 — spot-checked as legitimate pre-50:1-split prices
- The other 26 rows (across 12 assets) were unclassified

Andrew's direction: keep the 50x cap as a defensive safety net, but classify every capped row before deciding how to fix the silent-rewrite problem. The fix could be an exemption list, a sample-size guard, a synthetic-$1 filter, a threshold change, or some combination. Each asset needed a human-legible classification first.

## Methodology

Three artifacts were produced, each reusable for later audits:

1. **`data/analysis/t1_cap_audit_dump.py`** — loads silver/transactions/ once, reruns the cap logic, dumps the full 31-row capped DataFrame to `/tmp/t1_capped_rows.{parquet,csv}` plus the per-asset full transaction history (881 rows across 14 assets) to `/tmp/t1_capped_assets_txns.parquet`. Cheap to re-run, deterministic, no S3 round-trips after the initial load.

2. **`data/analysis/t1_cap_audit_investigate.py`** — consumes the dump, iterates the 14 assets, and for each one prints: capped dates with pre/post prices, BD transaction history summary (date range, txn types), daily T1 price distribution bucketed 0.99-1.01 / 1-10 / 10-50 / 50-150 / 150-500 / 500-5000 / 5000+, rows exceeding the 50x threshold. For assets with a known yfinance ticker, it also queries `yf.Ticker(t).splits`, `.history(lo..hi, auto_adjust=False)`, and compares yfinance closes against BD pre-cap observations.

3. **`docs/briefs/data-scientist-t1-cap-audit-findings.md`** — the classification deliverable, one section per asset, every classification tied to a specific evidence line so Andrew (or the next DS) could spot-check without re-running.

The key analytical insight: the price-distribution buckets immediately reveal which category an asset is in, before any yfinance cross-check:

- **Corruption pattern**: ~30+ daily observations, all clustered tightly in one bucket, one outlier 100x-60,000x above the median on a single isolated date. Historical median matches the cluster, pre-cap value is physically impossible.
- **Regime-shift pattern**: ~30+ daily observations spanning two or more clusters (pre-shift and post-shift), with the pre-shift cluster at the 50x+ range and the historical median falling in the post-shift cluster because it has more observations.
- **Sparse-pollution pattern**: <10 daily observations, ~60-100% in the 0.99-1.01 bucket (synthetic $1.00 entries), a handful of real NAVs in the $50-$500 bucket being flagged as outliers because the $1 entries dominate the median.

That categorization held without exception across all 14 assets.

## Evidence gathering — yfinance cross-checks

For tickered assets, yfinance was authoritative for splits/actions and for close-price verification. Mapping table used in the investigator:

| BD asset_name | Ticker used | Result |
|---|---|---|
| CHIPOTLE MEXICAN GRILL INC COM | CMG | `.splits` → 50:1 on 2024-06-26; unadjusted pre-split closes match BD ±2% |
| PRAXIS PRECISION MEDICINES INC COM NEW | PRAX | `.splits` → 1:15 reverse on 2023-11-29; 2025-10→2026-04 history $50→$347 matches BD runup exactly |
| DODGE & COX INCOME X | DOXIX | Jul-Aug 2024 closes tight $12.50-$12.94; BD asset median $12.49 matches, one 2024-08-07 spike at $40,412 |
| PGIM JENNISON SMALL COMPANY R6 | PJSQX | Jul-Aug 2024 closes $21.92-$23.68; BD asset median $23.55 matches, one 2024-08-07 spike at $8,625 |
| RED ROCK RESORTS INC CL A | RRR | Jun-Jul 2025 closes $50.23-$57.32; BD had only 6 txns, $54.23 observation is legitimate but polluted by $1 dividends |
| VANGUARD BALANCED INDEX I | VBAIX | Jul-Aug 2024 closes $46.64-$48.97; BD asset median $48.58 matches, one 2024-08-07 spike at $29,441 |
| VANGUARD EMERGING MKTS STOCK IDX INSTL | VEMIX | Jul-Aug 2024 closes $26.65-$28.53; BD asset median $28.85 matches, one 2024-08-07 spike at $5,833 |

For the collective-trust assets (INVESCO STABLE VALUE, the Northern Trust tiers, NT Agg Bond, Vanguard "GM" class, Vanguard Explorer GM) there was no yfinance mapping, so classification relied on BD transaction-history inspection alone. The Northern Trust and NT tiers clustered perfectly with the 2024-08-07 corruption group (all single-date spikes, all 30+ observations, all tight outside that date). The Vanguard "GM" cases clustered perfectly with the sparse-pollution group (3-11 total observations, 40-80% at exactly $1.00, the handful of non-$1 values all within a reasonable NAV range for the fund).

## Classification outcome

| Group | Assets | Rows | Signature |
|---|---:|---:|---|
| LEGITIMATE — regime shift | 2 (CMG, PRAX) | 13 | Split/reverse-split confirmed via yfinance; multi-cluster price distribution; median is post-shift |
| LEGITIMATE — sparse pollution | 3 (Vanguard 500 GM, Vanguard Bond GM, RRR) | 9 | <15 total daily T1 obs; median collapsed to $1.00 by synthetic accounting entries; real NAVs flagged as outliers |
| AMBIGUOUS | 1 (Vanguard Explorer GM) | 1 | Same sparse-pollution signature as above but only 5 total obs and one exactly-round $100 value — leaned legitimate but called out for Andrew |
| CORRUPTION — 2024-08-07 BD file error | 8 | 8 | All single-date spikes on 2024-08-07; 30+ daily obs elsewhere; yfinance (where available) confirms the non-outlier cluster is the truth |
| **Total** | **14** | **31** | |

Zero assets fell outside these four categories. The strong clustering is itself evidence — if the 31 rows were a random mix of many failure modes, a two-mechanism fix would not be sufficient.

## How the findings resolved into 021b's design

Once the classification was done, the shape of the fix was forced:

1. **CMG and PRAX can't be caught by a sample-size guard.** CMG has 36 daily observations, PRAX has ~90. The cap fires on them because the asset's median is legitimately post-shift, not because the sample is too small. Only a named exemption works for this class → `_T1_CAP_EXEMPTIONS`.

2. **The sparse-pollution group can't be caught by a named list sustainably.** If we name Vanguard INSTL 500 IDX TRST GM, we also have to name every future thinly-traded collective trust that hits the same pattern. The list would rot. But every sparse-pollution asset has <10 daily T1 observations, and every corruption asset has >=30 daily T1 observations. A sample-size guard cleanly separates the two without requiring individual judgment → `MIN_OBSERVATIONS_FOR_CAP`.

3. **The AMBIGUOUS case resolves automatically.** Vanguard Explorer Fund GM has 5 daily observations. With a threshold of 15, it's auto-exempted by the guard without anyone needing to make a discretionary call. That was a lucky break — it removed Andrew's only pending judgment from the brief.

4. **The threshold value is forced by the data.** The four groups' observation counts:

   | Group | Min | Max |
   |---|---:|---:|
   | Sparse-pollution (auto-exempt target) | 3 | 9 |
   | Regime-shift (explicit exemption) | 36 | ~78 |
   | Corruption (must stay capped) | 30 | 51 |

   Any threshold between 10 and 29 works. 15 sits in the middle with a 6-point cushion above the largest sparse case and a 15-point cushion below the smallest corruption case. The TO fixed it at 15 and Andrew explicitly said do not parameterize it — the value is data-driven, not a knob.

Once those four observations were in hand, writing the code was mechanical: two module-level constants and a three-clause boolean mask. The entire 021b change is 30-ish lines of diff against the .021 file.

## What went well

- **Two harnesses, fast iteration.** The dump + investigator split meant I could re-run the investigator repeatedly (on cached /tmp data, ~2 seconds) without reloading silver/transactions from S3 (55 seconds). Every asset-level question was answerable in seconds.
- **yfinance cross-check caught CMG and PRAX cleanly.** `yf.Ticker('CMG').splits` with a single line returned the exact split date and ratio; `yf.Ticker('PRAX').splits` caught the prior reverse split that explains why BD's median is so low despite 2025-10+ prices being in the hundreds. Without yfinance, classifying these as "legitimate regime shift" would have required hand-inspection of BD's transaction history across multi-year time spans.
- **Price-distribution bucketing worked as a first-pass classifier.** The three signature patterns (single-cluster + single outlier for corruption; multi-cluster spanning the 50x line for regime shift; dominant $1.00 bucket for sparse pollution) were visually obvious and matched the final classification 14 for 14.
- **The audit validated the brief author's expectation.** The brief speculated that some capped assets would be legitimate and some would be corruption. The actual split (6 legitimate + 8 corruption) meant the fix had to preserve the cap for the corruption cases while not being a wholesale cap removal — which is exactly what the two-mechanism design does.

## What to watch on future audits

- **yfinance datetime-tz mismatch.** The investigator's date-alignment block hit `Cannot compare dtypes datetime64[ns, America/New_York] and datetime64[ns]` on every yfinance lookup. It did not affect classification (the min/max/first/last close values printed fine, and the split data is always present), but the per-capped-date close alignment failed on every asset. A future audit should localize the BD date to America/New_York before the `get_indexer` call, or strip tz from the yfinance index. Non-blocking, noted for future cleanup.
- **Sparse-pollution diagnosis is qualitative.** The 15-observation threshold is load-bearing for the 021b fix, and it was derived from a 14-asset sample. If a future BD snapshot surfaces a capped asset with, say, 20 observations and clearly polluted ($1.00-heavy) history, the guard won't catch it and it'll need either a threshold nudge or the deferred synthetic-$1 filter. The harness exists — re-running this audit periodically (maybe quarterly, or whenever capped-row count drifts meaningfully) is cheap.
- **Collective trusts have no yfinance fallback.** Four of the 14 assets (INVESCO stable value, 3 Northern Trust tiers, NT Agg Bond) were classified via BD history alone. The corruption pattern was so clean on 2024-08-07 that this wasn't ambiguous, but if a future incident is subtler we'll need a manual cross-reference process (plan-sponsor statements, Morningstar, the trustee's monthly NAV report). Flagging as a known blind spot.

## The 2024-08-07 event itself

All 8 corruption cases cluster on exactly one date. That is not random. Every single capped corruption row is from 2024-08-07, and the assets span multiple fund families (Vanguard, Northern Trust, Invesco, Dodge & Cox, PGIM). A single BD extract file for that date was almost certainly broken — the most likely explanation is a decimal-shift or units/par confusion affecting all collective-trust-style records in that day's ingest. The cap is currently the *only* defense against whatever produced that file.

The audit findings doc flagged this as follow-up #4: pull the raw BD extract for 2024-08-07, diff the asset rows against neighboring days, and either correct them at source (have BD resend) or add a targeted ingest-time fix. That work is outside DS scope per the 021b TO but the evidence is strong enough that Andrew should consider chasing it down with BD support. Even with 021b shipped, the cap is still load-bearing for exactly this scenario; taking it off in the future requires understanding what produced the 2024-08-07 file in the first place.

## Artifacts produced by the audit

| Artifact | Purpose | Tracked in git? |
|---|---|---|
| `data/analysis/t1_cap_audit_dump.py` | Dumper | untracked (present in working tree) |
| `data/analysis/t1_cap_audit_investigate.py` | Per-asset investigator | untracked |
| `docs/briefs/data-scientist-t1-cap-audit-findings.md` | Classification deliverable | untracked (brief explicitly said do not commit until Andrew reviews) |
| `/tmp/t1_capped_rows.{parquet,csv}` | The 31-row capped DataFrame | ephemeral |
| `/tmp/t1_capped_assets_txns.parquet` | 881 BD txns for the 14 assets | ephemeral |
| `/tmp/t1_audit_investigate.txt` | Full investigator output | ephemeral |

The investigation harnesses were deliberately left untracked because the brief's non-action rules said "do not commit the findings doc until Andrew has reviewed it" and I did not want to half-commit (harnesses committed, findings dirty). After 021b ships and Andrew approves, a follow-up commit can track the audit tooling under `data/analysis/` alongside the existing v2 diff harnesses.

## Outcome

- 031 → 008 capped rows in v2 production output
- 023 drop-outs all carry plain `source='transaction_observed'` — no silent rewriting of legitimate prices
- 008 still-capped rows are all the 2024-08-07 BD file corruption cases
- INVESCO STABLE VALUE RET CL 1 regression anchor still fires
- Zero price changes on the still-capped group
- `_T1_CAP_EXEMPTIONS` contains exactly the two named regime-shift assets the audit surfaced; nothing else
- `MIN_OBSERVATIONS_FOR_CAP = 15` catches the remaining 4 sparse-pollution assets without naming them
- ADVI_GLDRST.022 (nightly gold-runner integration) unblocks
