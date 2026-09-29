# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- RE-CUT: irpt-performance-adapter qfxZ0DzB -> hD7G6YT1, 49 Financial Performance read from the v0.20 holdings gold (IB-pr-201/202/211/214, TO-IB-er-301 step 0)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_HOLDINGS_GOLD_49F_R2_20260929.md`
blob `a4679360` (at `ac4ad83de7`, an ancestor of HEAD; at HEAD and on disk; read 2026-09-29 07:5x-08:3xZ).
- **Word diff:** the re-cut of blob `189aaef2`, which this seat REFUSED
  (`NEVER_WIDEN_SIGNOFF_CRO_HALF_ADAPTER_HOLDINGS_GOLD_49F_20260929.md` @eca8083ad2, addendum 1 @b2215bcedc). The
  carried sections (surfaces, rows B-F, rollback per key, the CTO's rollback condition) read here as unchanged.
- **Asked by:** 2.0.0_SA_COO~P, msg 102646. **Other half:** 1.0.0_SA_CTO. **Ledger:** `irpt-adapter-holdings-gold-49f-r2-20260929`
  (U1, P1 closed; D1, A1 open). This seat is not in the act.

## VERDICT: SIGNED on blob a4679360, with three conditions and six named items

Every item of the refused half's section 6 is done and measured here independently. One hazard the first refusal did
not see is measured in section 3: a custody price discontinuity has TWO edges, and ruling 16 voids only the one that
crosses the band, so one account (a ~$1.9M relationship) would serve a 1-year figure of -91.5% computed against a
price the producer itself marked implausible. It is bounded (2 accounts, both named), it is the CTO's ruling to make,
and condition 2 asks that the choice is recorded before the apply rather than discovered after it.

## 1. What the re-cut answers, read here (not from the packet)

- **Artifact `hD7G6YT1`** (S3 `3donK_gT`, 424,559 bytes, 07:39:13Z): 70 members. Vs the refused `ABB89j26`: only
  `entry.py` (8465a60d) and `retained.py` (ea895201) differ, each byte-equal to HEAD. Vs live `qfxZ0DzB` (still the
  function's CodeSha256, Active): `holdings_gold.py` added and the four members the first packet named.
- **The two deltas, read at their lines:** `retained.py:225-231` -- after `holdings_gold.calculate`, the fresh path
  raises `f49_engine.EngineReturnImplausible` when `implausible_engine_series(outcome["report"])` (any linked point
  <= -1), before persist or return, so both readers refuse one shape (ruling 16). `entry.py:61` --
  `_authorize_release` now passes `request` into `_resolve_selected(scope, ctx, reference, request=None)`, which only
  the RENDER_DELEGATE branch consumes (`_resolve_render_selection`); every other principal's path is unchanged. That
  is window 21's K8 refusal (`corr-d490a5849a80`, "a render read carries no request to name its grant").
- **Tests on the zip's own modules** (`retained`, `holdings_gold`, `f49_engine`, `entry` imported from the zip,
  asserted): new zip **20 passed**; the refused zip **1 failed, 19 passed**, the one failure
  `test_fresh_path_refuses_an_ok_day_at_or_below_minus_one` (DID NOT RAISE) -- the test tells the two zips apart.
- **The gold, re-emitted 06:43:07-07:08:21Z under v0.20** (`holdings_performance.py` @f302ab14cd, read: identifier
  = first non-empty of the declared columns with a per-row sentinel for none; cash rows into the basket at zero;
  `in_basket = member & (value >= 0)` with `negative_value`/`leveraged`; a second-pass band emitting
  `IMPLAUSIBLE-RETURN`; the manifest population on `held_count`). E3-AC4 re-run by this seat 07:51Z: `days 557 |
  partitions absent 0 | OK rows |r|>=1: 0 | OK rows |r|>0.5: 4 | days without leveraged: 0 | manifests complete 557
  of 557` -- PASS. This seat's own read of all 557 partitions: 3,188,339 rows, 19 columns; status census OK
  2,781,208 / NO-PRIOR-HOLDINGS 405,142 / NON-POSITIVE-BASE 1,541 / ALL-HOLDINGS-EXCLUDED 446 / **IMPLAUSIBLE-RETURN
  2**; `leveraged` on 7,483 rows over 679 accounts; OK-row min -0.9233, max +0.5047. Both manifest surfaces
  (parquet and json) carry the four completeness keys and agree on `computable_count` on 557 of 557 days, which
  retires addendum 1 of the refused half.
- **The chain census, re-run by this seat** (the adapter's rule, windows ending 2026-09-25): the packet's section 3
  numbers are this seat's numbers -- YTD 7,127 accounts: >= +100% **2** (was 22), <= -100% **0** (was 2),
  (-100%, -50%] 2, max +197.9%, min -61.2%; 1Y 7,300: 4 / 0 / 4; SI 7,814: 7 / 0 / 5, non-finite 0 (was 1).
- **Plans, prefixes, IAM:** carried from the first half (ae20e904e6; every prefix builder output); the packet's fresh
  plans 0/2/0 and 0/1/0 are the ledger's P1 leg and are not re-run here.

## 2. The 49F silver under ruling 13, measured (for the record, not a ground)

The Schwab `dim_position` carries no description column, so the declared identifier chain is cusip then
`ticker_symbol`. Of the 41 cusip-less rows at 2026-09-25, both are blank on all 41; one row carries an ISIN/SEDOL
(not in the chain); **21 are ruling-14 cash** (price 1.00, quantity == value) and **20 are excluded** under ruling 4.
The producer's own count at 2026-09-24 agrees (21 of 41, 22,037,392.89).

## 3. The remaining hazard: a discontinuity has two edges, and ruling 16 voids one

The two `IMPLAUSIBLE-RETURN` rows, traced to the silver:

| account | day voided | what the silver did | the next day, still OK | window figure the act would serve |
|---|---|---|---|---|
| ..0090 (28 holdings, ~$1.9M) | 2025-12-17 | DLCFX 17.48 -> **546.00** -> 16.21; DIEFX 16.12 -> **384.00** -> 14.61 (x31 and x24 for one day, then back) | 2025-12-18 `r = -0.9233`, computed against the glitched t-1 price, inside the band, status OK | YTD +7.7% (clean); **1Y -91.5%** (250 OK of 251); **SI -91.4%** |
| ..4714 (3 holdings, ~$12k) | 2025-12-12 | MSOX 3.82 -> 7.94 -> 6.91 -> 9.50 | 2025-12-15 -13.0%, 12-16 +37.5%, 12-18 -50.6% | YTD -7.1%; **1Y -69.8%**; SI -69.8% |

The producer implements ruling 16 as written (a day at or beyond +/-100% is not computable); the day AFTER prices
its holdings against the price the producer just declared implausible, and a -92% day is inside the band. The
remedy is one of two producer rules, both the CTO's to choose: the day after an IMPLAUSIBLE day is not computable for
that account (its reason named), or the affected keys price against the last plausible price. Population today: 2
accounts, both in the served directory; every other chain at or under -50% (..8878 ~$123; ..7501 ~$1.1M, JFB
29.87 -> 17.00 -> 20.90 -> 9.01 -> 8.23 across February-March, a sustained fall, not a one-day edge; ..7828 ~$33k, no
day beyond +/-30%) is the custody price path as given.

## 4. The read set and what the rule says the act serves (read from the v0.20 gold at signing)

NEW-01, the control and the ..558d pair sit under ONE directory relationship (three accounts), so one client walk
reads all three. ..0273 (the refused half's cusip-less account) is **not in the served directory** (4,620 entries): the
page cannot read it, so it is replaced on the page by ..4714 (in the directory) and read from the adapter's own log
only if ~P invokes it; its gold reads YTD 0.00% over 79 OK days, SI 0.00% over 171 OK of 452 (PARTIAL).

| read (page, walk) | BEFORE on qfxZ0DzB (engine, as retained) | AFTER on hD7G6YT1, predicted from the rule |
|---|---|---|
| NEW-01, YTD and 1Y | named refusal (DEPENDENCY_UNAVAILABLE; the retained -100% reports) | **+0.49%** over 69 OK of 181 / 252 days, PARTIAL; provider OPAL_HOLDINGS |
| the control (same relationship), YTD | 5.93% | **+5.16%** (181 of 181) |
| ..558d (same relationship), YTD / 1Y | 9.57% / 8.80% | +0.04% / -0.85% (the widest engine-vs-holdings gap; named in the refused half) |
| ..0695 (near-zero base), YTD | engine figure as served | **+4.38%** over 137 OK of 139, PARTIAL (2), `leveraged` on 8 days |
| ..4180 (one stock, MRVL), YTD | engine figure as served | **+197.9%** over 135 OK of 137, PARTIAL (2); MRVL 84.98 -> 261.94 in the silver, a smooth path (99.05 at 03-31, 290.79 at 06-02) |
| ..2297 (DELL-led, 2 -> 28 holdings), YTD | engine figure as served | **+149.7%** (184 of 184); DELL 125.88 -> 562.89, smooth (164.13, 435.31, 431.46) |
| ..0090 (section 3), YTD and 1Y | engine figure as served | YTD **+7.7%**; 1Y **-91.5%** PARTIAL (1) |
| ..4714 (section 3), 1Y | engine figure as served | **-69.8%** PARTIAL (2) |
| one Cottonwood and one Inflection figure | as served | unchanged (row F) |

## 5. Blast radius (the first packet's, with what section 3 adds)

- **Row A, moves:** every 49F account's figure to the holdings chain. Population read above: 2 YTD accounts serve
  over +100% on smooth custody price paths; 0 serve at or under -100% on either reader (the fresh-path guard makes
  the reopen guard's refusal shape unreachable on a first read); **2 accounts serve a 1Y between -70% and -92% off a
  one-day price glitch's reversion edge** (section 3).
- **Rows B-F:** as the first packet and this seat's first half read them; F re-read here as unchanged code.
- **Rollback per key:** unchanged (Lambda -> `5bmwADQs`; the two .tf files reverted, both roots re-applied).

## Conditions

1. **The before-read is this seat's, on qfxZ0DzB, before the apply; the after-read on hD7G6YT1 is the same set**
   (section 4, by `/ui-walk`, shots kept under `tmp/ui-walk/`, never committed). ..0273 is read on the page as
   ..4714. Any figure at or under -100% on either reader, or any unnamed difference, is the packet's own rollback.
2. **The two-edge case is ruled before the apply, in the CTO's half:** either the producer re-emits under a v0.21
   rule for the day after an `IMPLAUSIBLE-RETURN` day first, or the interim is accepted by name (..0090 1Y -91.5% /
   SI -91.4%; ..4714 1Y -69.8%) with row `IRPT_BCKEND-S196` as its carrier. This seat signs either branch; it does not
   sign the figure served with the choice unrecorded.
3. **The after-read includes ..0090's 1Y and ..4714's 1Y as served**, recorded in the ledger beside the packet's
   reads; a served figure there that differs from section 4's prediction is a row the same turn.

## Named items (not refusal grounds)

1. The two +100% accounts are single-stock or single-stock-led, and the silver's price paths are smooth; the served
   figure is the custody price's. Whether a +198% year is what the client sees elsewhere is the advisor's read.
2. A chain over in-band days is unbounded above (each day < +100%, the product not); the band bounds a day, not a
   window, and that is the ruling as written.
3. ..558d's engine 9.57% -> holdings +0.04% YTD remains the widest gap among the retained accounts; not measured
   further here.
4. 679 accounts carry `leveraged` on at least one day (7,483 rows); the page shows no such flag today.
5. The since-inception read costs 557 partition reads; the CTO's 48-second rollback condition is the CTO's and is
   not re-derived here.
6. The refused half's addendum 1 (the 2026-09-25 manifest's two surfaces) is retired by the re-emit: 557 of 557
   agree.

## What this half signs against

- Packet blob `a4679360`; the first packet's carried sections (`189aaef2`); artifact `hD7G6YT1` (S3 `3donK_gT`) with
  its 70-member census; commits f302ab14cd, eee6a7a721, dd3be9a28a, 78f7ffb758, ae20e904e6; PRD ADDENDUM v0.20
  @613bfc6ecf.
- The gold as re-emitted 06:43-07:08Z (E3-AC4 PASS, this seat's run 07:51Z) and the chain census in section 1.
- The blast radius in section 5, the read set in section 4 and the three conditions.
