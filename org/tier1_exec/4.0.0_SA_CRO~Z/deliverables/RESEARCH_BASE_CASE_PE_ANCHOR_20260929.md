# RESEARCH: the Base-case P/E anchor -- which multiple the team applies, what window, and whether to lead with the team

**Author** `4.0.0_SA_CRO~Z` -- **Date** 2026-09-29 (census ~04:4xZ-05:0xZ) -- **Asked by** `1.0.0_SA_CTO~Z`, broker
message `20260929T042544Z` ("Research ask (design fork): the Base-case P/E anchor"), ruled at the CTO's /self-drive tick.
**Frame:** Andrew ruled the Base-case BASIS on 2026-09-28 ~21:3xZ: adjusted EPS x adjusted P/E
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_213xZ_BASE_CASE_ADJUSTED_BASIS_AND_AMGT_UI_WALK_TO_D13_DESIGN.md`).
He did not rule the WINDOW or the multiple's kind. That is the open fork, and the served reason on the Upside and Downside cases still routes
"methodology to be discussed with Andrew" (`lib/research/api/case_rule.py:59`).

## REC

**Lead with the team's Base case wherever the team wrote one, labelled as the team's, with its multiple and pack citation. Keep the rule as
a secondary "historical-multiple reference" for every name. Do not change the window: no trailing window reproduces the team, and a
shorter one is noisier, not closer.** If Andrew wants the rule itself to move toward the team, the principled change is a different KIND of
multiple, not a different length: forward EPS x the stock's own history of FORWARD P/E. That needs a history the block does not carry
(Bloomberg `BEST_PE_RATIO` by date), so it is a pull and his call, not a CTO ruling.

## What was measured

**Instrument.** A read-only census (`pe_window_census.py`, session scratchpad). For each of the 70 served rule Bases in
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~167/BASE_CASE_BASIS.json` it reads the newest model block through
`scoped_amgt.read_model_block` (with the corrected overlay, as served). It rebuilds the adjusted P/E window with `case_rule.adjusted_pe_window`
(the served rule's own function) and joins `dossier.read_dossier`'s Base-case table.

**Positive control.** The recomputed all-years median equals the served `trailing_median_pe` on 70 of 70 names. The served
`ratio_to_px_last` equals (trailing median / current forward P/E) on 70 of 70, with 0 mismatches.

**Denominator.** 20 of the 70 carry a readable team Base table. This is the same 20 that ADJUDICATION_v56 joined; the other 50 carry no
case table (6 unreadable per CORPUS `Z-W1-S12`).

**Q1. Which multiple do the team's packs apply?** A single round P/E per case, held FLAT across every projected year: 20 of 20 tables carry
one multiple value across 2026E-2030E, and Price = EPS x Multiple. The multiples are judgment numbers (10x, 12x, 16x, 22x, 30x, 36x), not a
formula output. The EPS they multiply matches the served one: team EPS in the first year / BEST_EPS FY1 has a median of 1.00, and 14 of 19
are within +/-10%. Outliers are MNST at 1.95 (likely a share-count basis) and ORA, whose team EPS did not parse. **So the gap to the team
is the multiple, not the EPS.**

**Q2. Window: 10y vs 5y vs 3y, and forward.** Each anchor's multiple divided by the team's multiple, over the 20:

| Anchor | median anchor/team | within [0.8, 1.25] | above 1.5 |
|---|---|---|---|
| trailing median, all closed years (served; 3-10 yrs, 10 on most) | 1.53 | 6 | 11 |
| trailing median, last 5 closed years | 1.52 | 3 | 11 |
| trailing median, last 3 closed years | 1.56 | 3 | 12 |
| last closed year's P/E | 1.58 | 5 | 11 |
| current forward P/E (px / BEST_EPS FY1) | 1.08 | 12 | 4 |

- **Shortening the window does not close the gap.** On the growth names the recent years carry the highest multiples: NOW is 76x on all
  years and 66x on the last 5 against the team's 22x, and CDNS is 39x on all years and 50x on the last 5 against 36x.
- **The mechanism is the kind of multiple, not its length.** A trailing P/E (price over realized EPS) paired with a FORWARD EPS counts a
  growth name's growth twice. The served ratio to price is exactly (trailing median / current forward P/E). Over all 70 names its median
  is 1.13, 27 names are above 1.25 and 11 are below 0.8.
- **The current forward P/E sits closest to the team (median 1.08) but cannot be the anchor.** Forward P/E x forward EPS = today's price,
  so the Base would equal PX_LAST by construction and say nothing. What it does show: **the team's multiple is usually a modest haircut to
  the stock's current forward multiple.** Examples: WDAY 10x against 17x, NOW 22x against 34x, UBER 16x against 21x, MELI 30x against 46x.
  The exceptions run the other way, e.g. INTU 16x against 12x and CPA 10x against 8x.
- **Estate precedent.** The one valuation surface in the estate, the Valuation page (`json/valuation/valuation_data.json`,
  `docs/reference/yang-pipeline-lineage-map.md:364-382`), reads FORWARD (NTM) and trailing P/E as a percentile within each index's own
  history since 1990 (p10-p90 bands). It is a "where is the multiple versus its history" view. The estate has no precedent for a
  historical median used as a target multiple.
- **Industry practice, not checked externally (no egress was taken; this seat's prior, INFERRED).** A target price is usually forward EPS
  times an analyst-chosen forward multiple, anchored on the stock's own historical FORWARD P/E average (often 5y) or on peers and adjusted
  for growth. A trailing median applied to forward EPS is not the usual construction.

**Q3. Is leading with the team's case the cleaner answer?** Yes, where one exists (20 of 70 today). It is the team's own number, cited to
their pack (CORPUS serves the table with its page citation). No rule has to imitate a judgment multiple held flat for five years, and the
DSGN_AMGTV1 brief independently asks for the team's view to lead (`docs/briefs/dsgn-amgtv1-security-analysis-frontend-brief-20260928.md`,
O6 and finding AMV-21 there). For the other 50 names the rule stays the only Base. Labelled as a historical-multiple reference, it is honest about
what it is. Labelled "Base case", it reads as a view nobody holds, and for growth names it runs well above one.

## Per name (the 20 with a team table, sorted by served/team)

| Name | Team multiple (flat, 5 yrs) | Team EPS y0 / BEST FY1 | Trailing median, all yrs (served) | last 5 | last 3 | Current fwd P/E | Years |
|---|---|---|---|---|---|---|---|
| WDAY_US | 10x | 0.97 | 46.0x | 46.0x | 35.3x | 17.2x | 5 |
| NOW_US | 22x | 1.02 | 76.2x | 65.5x | 65.5x | 33.9x | 7 |
| ORA_FP | 6x | -- | 16.3x | 12.1x | 12.1x | 11.1x | 10 |
| MELI_US | 30x | 1.02 | 80.8x | 80.8x | 51.1x | 46.0x | 7 |
| ZTS_US | 12x | 1.12 | 30.0x | 30.0x | 27.5x | 11.3x | 10 |
| NFLX_US | 25x | 0.90 | 60.8x | 38.1x | 38.1x | 20.4x | 10 |
| UBER_US | 16x | 0.99 | 37.9x | 37.9x | 37.9x | 20.8x | 3 |
| INTU_US | 16x | 1.01 | 32.2x | 31.2x | 31.2x | 12.1x | 10 |
| NKE_US | 22x | 0.89 | 35.6x | 36.2x | 35.0x | 21.4x | 10 |
| IDXX_US | 34x | 0.99 | 52.5x | 51.7x | 51.7x | 34.7x | 10 |
| ISRG_US | 38x | 0.96 | 57.9x | 63.4x | 63.4x | 37.1x | 10 |
| MSCI_US | 30x | 1.00 | 39.8x | 40.6x | 39.5x | 28.2x | 10 |
| MA_US | 26x | 0.98 | 34.2x | 34.8x | 34.8x | 28.4x | 10 |
| RMS_FP | 36x | 1.04 | 46.2x | 49.3x | 49.3x | 30.5x | 10 |
| MNST_US | 30x | 1.95 | 37.3x | 37.4x | 37.2x | 36.9x | 10 |
| CPA_US | 10x | 1.06 | 12.1x | 7.4x | 6.3x | 8.2x | 9 |
| ASML_NA | 30x | 0.83 | 35.5x | 35.7x | 35.3x | 39.5x | 10 |
| SAP_GY | 20x | 1.01 | 22.4x | 27.8x | 33.9x | 25.9x | 10 |
| CDNS_US | 36x | 0.97 | 39.3x | 50.3x | 50.3x | 39.5x | 9 |
| ML_FP | 12x | 1.02 | 12.0x | 12.1x | 12.1x | 12.7x | 10 |

## Not claimed

- The team comparison covers 20 names, the join's whole population today, not a sample. Growth names dominate the high end.
- The team year-0 column is 2026E on 19 names and 2025E on NKE; the rule's EPS is FY1. The two share a horizon for most names, not all.
- The forward-P/E-history anchor was NOT computed. Its inputs are not on the block, so whether it lands near the team is untested. It is
  named as the principled option, not as a measured one.
- Whether the Upside and Downside cases should follow the team's tables is outside this ask. Andrew's ruled ABSENT stands.
- No vendor call and no write. The census read S3 under this seat's credentials only.
