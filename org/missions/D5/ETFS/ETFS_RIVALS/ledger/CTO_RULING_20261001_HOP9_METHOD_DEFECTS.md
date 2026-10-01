# ETFS_RIVALS -- CTO RULING: hop-9 method defects (a), (b), (d)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~18:1xZ.
**Answers:** `4.0.0_SA_CRO~RV` msg 28011.
**Grounding:** brief `org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_END_TO_END_GAP_BRIEF_20261001.md` @b1e877a1c6, hop 9, under
Andrew-direct @b7622c0b5a. The code was read at `data/etfs/scripts/rivalfunds/gold_trade_schedule.py`: `_id_changes` at :315 is a
greedy market-value pairing within `ID_CHANGE_TOL` with no identifier test, and the flow factor at :426-428 is an unbounded median.

**Routing:**
- Mid-round the spec is frozen. Round 4 (d-5 in flight) completes as cut.
- These rulings become **round-5 cells**, which `2.0.0_SA_COO~RV` cuts from the round-4 analysis.
- The G5/G6 replay that serves them runs under a new never-widen pair.

## (a) An ID-CHANGE needs an identifier relation, never equal value alone -- ADOPTED

- **What qualifies:** an exit and an entry pair as `ID-CHANGE` only when one of these holds:
  - a G3 or issuer-published identifier event names both;
  - a crosswalk hit (ISIN, SEDOL or FIGI) maps one to the other;
  - the two CUSIPs are equal after normalization.
- **Equal value alone stays an exit plus an entry, with real share counts.**
- **Normalization lands at silver**, not in the pairing. CUSIPs are zero-padded to 9 characters, so BP `55622104` ->
  `055622104` is the SAME security and never reaches the pairing.
- **A shared CUSIP-6 issuer root is NOT enough by itself.** Two share classes of one issuer are two securities, so a CUSIP-6
  match qualifies only alongside a G3 event.
- **Acceptance:**
  - PFOE 2026-09-28 serves an exit of Universal Music Group (`91377B109`) and an entry of Quanta Services (`74762E102`).
  - IDVZ 2026-09-23 serves an exit of UBS and an entry of Lenovo.
  - BP serves no row at all (one normalized security).
  - The served ID-CHANGE count falls from 3 to 0 at the replay. It is printed with its denominator.

## (b) A window whose flow factor is implausible is REFUSED, never inferred -- ADOPTED

- **Refusal rule:** refuse a fund-window when either condition holds:
  - f lies outside `[0.5, 1.5]`;
  - the share of the window's non-cash lines with quantity 0 on either side exceeds 0.20.
- **The thresholds are PROVISIONAL.** They come from the measured distribution: 7 of 3,656 windows fall outside the band.
  They live in `guardrails_config.json` beside the other floors, never as literals in code.
- **What a refused window serves:** a G6 row with `status: REFUSED` and its reason (`flow_factor_out_of_band` or
  `zero_quantity_share`), and **zero inferred trades**. The page shows the window as not inferred. It never shows an empty
  window as "no trades".
- **The guardrails run on the replay.** The backfill and replay path runs the same guardrails the page uses, so a refused
  window cannot reach served trades by any path.
- **Acceptance:**
  - INEQ 2025-08-29 and 2025-11-28, TXUE 2025-04-14 and TSEL 2025-01-16 each serve REFUSED with 0 trades.
  - The other 3,649 windows' trade counts are unchanged except where (a) moves them.
  - Both counts are printed.
- **Both branches** for a genuinely large flow (f > 1.5 on a real creation): the window is refused and recorded, never
  silently lost. Widening the band is an enrichment that waits for a measured true case.

## (d) Key resolution is its own column, out of the confidence precedence -- ADOPTED

- **A new G5 field, `key_resolution`, records the key's resolution state:** `RESOLVED`, `ALIAS` or `UNRESOLVED`.
- **The `confidence` label stops being overridden by `UNRESOLVED`.** It grades the trade inference only, meaning the flow
  factor, the event cleaning and the price band.
- **The contract changes additively.** The page reads `key_resolution` where it showed `UNRESOLVED`. No existing consumer loses
  a value.
- **Acceptance:** BASG, CGIC and SCHY serve a confidence distribution that is no longer dominated by one label. The before and
  after counts per fund are printed.

## Not ruled here (with Andrew in his live CRO~RV session)

The brief's three "Andrew calls" (the Opal history source, the PFOE-group passive control, the peer-set criterion) are in front
of him through `4.0.0_SA_CRO~RV`, whose closer run he started himself. His record says the BUILD phase needs his word.

**One hazard is named for that call.** Recommendation 1 reads PFOE history from "Black Diamond / COT data". CLAUDE.md forbids a
pipeline tree to reference another firm's data (`ds-precommit-check.py` `_CROSS_FIRM_FOREIGN_*`), and cot is a separate firm.
The source's firm must be confirmed before that call is put to him.
