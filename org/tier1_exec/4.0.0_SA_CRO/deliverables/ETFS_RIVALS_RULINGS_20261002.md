# ETFS_RIVALS open-call rulings -- 4.0.0_SA_CRO~RV, 2026-10-02

Authority: Andrew-direct ~04:57Z, "CRO~RV has adjudication ability for any open calls on the ETFS_RIVALS" (record
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261002_045xZ_RV_TEAM_ETFS_RIVALS_ADJUDICATION_AND_EGRESS_TONIGHT.md`).
One section per call, appended as calls arrive. Andrew may overrule any ruling.

## CALL 1 -- RIV-rk-1 price source (2.0.0_SA_COO~RV msg 28214, 05:13Z)

**Call.** G4 `security_market` holds one date (2026-09-29), so rk-1's MTD/QTD/YTD/R30 contribution reads almost all
`missing` and the rankings component is empty for the demo. COO recommendation: when G4 has no price, fall back per
(security, day) to the holding's own reported price, `market_value / quantity` from the fund's G1 report on d and d-1.

**Ruling: ACCEPTED, with five conditions.** The basis is sound for this measure. Contribution is to the FUND's return,
and the fund's own reported valuation is the price its NAV used, so within one fund the implied price is consistent.
G1 carries `quantity`, `market_value` and `position_type` per position (`gold_canonical_shape.py:133`, `:485`, `:584`).

1. **One source per daily return.** Source order per (security, day): `g4_tri`, then `g4_close`, then `holding_implied`,
   else `missing`. A day's return uses the SAME source at both endpoints (d-1 and d), never one source at each end.
2. **Only a priceable position gets an implied price:** a security holding (not cash, not a derivative, swap, future,
   option or forward), with `quantity > 0` and `market_value` non-null on both d-1 and d. Anything else is `missing` with
   its reason.
3. **Corporate-action guard (refused, never inferred; the RIV-h-5 doctrine).** When `quantity` changed between d-1 and d
   AND the implied price ratio departs from 1 by more than a PROVISIONAL band (`|p_d / p_(d-1) - 1| > 0.25`, kept in
   `guardrails_config.json`), the day is `missing` with reason `corporate_action_suspected`. A split's signature is
   quantity times k with price divided by k, and pricing it would give a false -50% contribution on a 2:1 split.
4. **No gap filling.** A return exists only where the fund has reports on both d-1 and d (trading-day adjacency,
   `lib/trading_calendar.py`). A missing report leaves that day unpriced; nothing is interpolated.
5. **Contract column, at row grain.** A contract row aggregates many days, so a single per-day source does not fit it.
   The `price_source` column takes the one source shared by every priced day of the row, else `mixed`, else `missing`
   (enum `g4_tri | g4_close | holding_implied | mixed | missing`). Add `n_days_holding_implied` beside `n_days_priced`.
   `claim` stays `INFERRED`. Readers stay column-optional (A1 ruling 3).

**Disclosure (demo-facing).** Implied returns are price-only. They exclude dividends and are measured at the report's
valuation date. Where `price_source` is present, the ranking tables state their basis in the caption (for example "priced
from the funds' own reports"), so the ranking is never read as a total-return figure.

**What this does not settle.** G4 history still lands in round 6. When it does, `g4_*` takes precedence automatically
and the rankings re-rank. The day-over-day shift from that re-rank is expected, not a defect.

**Carrier.** The issuer amends the rk-1 cell text and the `holding_contribution` contract in the decomposition, and the
order's text, in its own commit. That commit names the gate limb that graded the change (rule 27, L5/L6 issuer amendment).

## CALL 2 -- row ETFS_RIVALS-Z-S13, when to set the per-fund issuer floors (3.0.0_SA_CVO~RV msg 28225, relayed by 1.0.0_SA_CTO~Z msg 28226, 05:27Z)

**Call.** RIV-f-4 built per-fund issuer floors (`guardrails.py` `resolved_floor()`), but the shipped
`guardrails_config.json` still holds every issuer fund at 0.23, the value GQGU set. So a BASG regression down to 24%
resolved would still be served as updated. Nothing is served wrong today, because BASG reads 1.0
(`deliverables/0.9.0_WK_ETFS_RIVALS~4/evidence/floors_measured.json`). CVO recommendation: change no config today, and set
{BASG, GQGU} under the never-widen pair in the first round after FAST. The reason: the rounding rule puts BASG at 1.00, so
one new unmapped line would flip BASG to not-updated on demo day. Record: `surprise-channel/adjudications/ADJUDICATION_v5.Z.md`
@04a70a4241.

**Ruling: ACCEPTED. No config change today, plus one condition on the later setting.**

- **Today.** The shipped floors stay as they are. BASG is the FWD-1 demo fund, so a brittle 1.00 floor is the larger risk
  on demo day. S13 stays INERT and UNDER_INVESTIGATION through the demo and graduates in the round-5 slug as the CVO
  states.
- **Condition: the floor gets a line tolerance.** Deferring does not remove the brittleness the CVO named. Setting BASG
  at a bare round-down of 1.0 after the demo would ship the same false not-updated, one day later. So each per-fund issuer
  floor is set to `round_down_2dp(measured_fraction - 2 / n_noncash_lines)`, both terms read from that fund's newest
  report. That tolerates up to two new unmapped lines and still refuses a regression of the S13 size (to 24%). The
  tolerance is PROVISIONAL. Its measurement is written to the evidence file beside the floors, with `n_noncash_lines`
  printed per fund.
- **Not settled here.** The `bloomberg` source floor of 0.99 has the same arithmetic: a fund at 1.0 with fewer than 100
  non-cash lines flips on one unmapped line. That is an observation for the same post-FAST cell. This ruling neither
  moves it nor requires it.

**Carrier.** 2.0.0_SA_COO~RV cuts the config cell in the first post-FAST round, under the never-widen pair with
1.0.0_SA_CTO~Z. The pair's half names this formula and reads the expected per-fund floors from it, for both branches.

## CALL 3 -- RIV-rk-1 period anchor (2.0.0_SA_COO~RV msg 28236, 05:43Z)

**Call.** A real in-process run for page day 2026-10-01: MTD and QTD span one day (Oct 1), but the newest G1 report is
09-30, so MTD/QTD read 766 of 766 security rows `missing` (R30 3% missing, YTD 2%). COO recommendation: anchor the
periods on the data's as-of date, the newest G1 report date or G4 price date on or before the page day, with
`period_end` = as-of.

**Ruling: ACCEPTED in substance. The as-of date is fixed by the trading calendar, not read from the data.**

1. **One as-of date per page:** `asof = lib/trading_calendar.py prev_trading_day(page_day)` (the estate's T-1
   convention). Every fund's MTD/QTD/YTD/R30 runs through that same date, and `period_end = asof`. Today both rules give
   09-30, so the run's result does not change.
2. **Why not the newest data date.** A data-driven as-of moves with whichever source lands first. One fund that labels its
   report a day ahead, or one early G4 price, pushes the as-of date forward and makes the other twelve read partial. It
   also hides a universe-wide lag behind a quietly older window. A fixed T-1 as-of keeps the funds side by side on one
   window, and a fund whose data stops short shows `partial` coverage with its reason. That matches the "N of 13 funds
   current" headline (round-4 ruling 7).
3. **No per-fund windows.** Funds are compared on one page, so no fund gets its own period end.
4. **Label.** On the first trading days of a month or quarter, "MTD" names the PRIOR month (today: September). The caption
   already prints `period_start..period_end`; it also names the month or quarter, or prints the as-of date, so a reader
   never takes September's figures for October's.
5. **Fixture.** If rk-1 AC1's fixture assumed `asof` = the newest G4 date (10-02), the issuer re-derives its expectation
   under rule 1. That is the issuer's own criteria amendment.

## CALL 4 -- RIV-tb-1 bet test (2.0.0_SA_COO~RV msg 28241, 05:53Z)

**Call.** A real run (page 2026-10-01, BASG) reads Visa as a BET over 48 windows and Microsoft as a BET over 58. The A1 rule
tests the largest window against the line's absolute NET, and two-way churn shrinks the net (MSFT's gross is far above its
net of -11.6M). COO recommendation: `bet` when the largest window carries at least 0.5 (PROVISIONAL) of the line's GROSS,
the sum over windows of |window net|; else `tilt`. Net, lean and rank are unchanged.

**Ruling: ACCEPTED.** The A1 test is mis-specified. Net is the wrong denominator, because any heavily traded line
with a small net residue passes it. Gross measures what FWD-15 means by a bet: a lean concentrated in one move, rather than
spread over the year. The three fixtures read as the COO states (S1 100/300 tilt; S2 1.0 bet; S3 250/300 bet).

1. **Sector lines** apply the same test to the sector's per-window net, the sum of its securities' signed notional in that
   window. Gross is the sum of the absolute values of those per-window nets.
2. **The reading shows its basis.** Add `gross_notional_base` and `bet_share` (largest window / gross) to `buying_trend`
   (column-optional, A1 ruling 3). Where gross is far above |net|, the page can then show "net X of Y traded". A churned
   line is never presented as a steady lean.
3. **The threshold stays PROVISIONAL at 0.5, inclusive.** Two equal windows with nothing else read as a bet; that is
   accepted.

## CALL 5 -- live AI accounts for today's demo, run from the COO seat (2.0.0_SA_COO~RV msg 28246, 06:14Z)

**Call.** ai-2 is built: checks PASS on a stub client, and `default_client` refuses unless `RIVALFUNDS_AI_ENABLE=1`. A1 ruling
2 put the first live OpenAI run in round 6 (Lambda wiring, a new secret, IAM). COO recommendation: run today's accounts from
the COO seat on site Z, under the seat's own identity, with the existing Opal secret `opal/openai/news-trending`. One run per
page day: 12 non-benchmark funds x 2 prompts, gpt-5.4, web search only for a reading source with nothing fresh. Output is
append-only to `research_hypotheses date=<page day>`, every row graded by `grounding_check`, and FAILs shown as FAIL.
Lambda wiring and a dedicated secret stay in round 6. The COO asks whether "tonight" covers a vendor call after ~06:00 ET.

**Ruling: ACCEPTED, for today's seat run.**

1. **The vendor authority does not rest on "tonight" alone.** Andrew named this exact use twice:
   - C-VENDOR, "OpenAI writes the analyses" (PRD v0.10, confirmed);
   - ~02:2xZ, "Web search is ok" as the fallback, which CVO~Z read as the per-use authorization scoped to the rivalfunds AI
     (`L4R_REVIEW_ETFS_RIVALS_v0.10_RATIFIED_TEXT_20261002_Z.md`).

   The ~04:57Z egress word adds cover for running it tonight. A seat run for page day 2026-10-01 now is covered by all
   three. A seat run for page day 2026-10-02, after ~06:00 ET today, rests on C-VENDOR and the ~02:2xZ word, and this seat
   reads both as covering it. Andrew may overrule; nothing here is parked.
2. **The scope is the rivalfunds AI chain and nothing else:** at most one run per page day, plus at most ONE re-run per
   fund when the first run's call fails at transport. A grounding FAIL is shown, not re-rolled until it passes.
3. **The key.** It is read at run time from Secrets Manager and never written to disk, a log, a commit or a row. Using the
   news-trending key shares that pipeline's quota for about 24 chat calls plus the fallback reads. That is accepted for today
   only. The dedicated secret is round 6.
4. **The run's provenance travels with it.** Each row's `input_manifest` records `run_path: "seat-adhoc"`, the seat serial,
   the model and the run time. Per CLAUDE.md, an ad-hoc artifact is never production evidence. FWD-16/17 grade EXERCISED only
   on the scheduled round-6 run. Today's accounts are a QA-class demo read, and the audit material on the page says so.
5. **Benchmarks get no account** (A1 ruling 6). Web reads are labelled `[web]` and recorded in `web_reads` (A1 ruling 4).
6. **Served output.** The write to `research_hypotheses` is a literal key list the COO controls. Republishing the page is a
   move of served output and stays under the CLAUDE.md never-widen rule as it stands. This ruling adds no pair and removes
   none.

## CALL 6 -- rk-1 implausible-valuation band 0.5 (2.0.0_SA_COO~RV msg 28308 and 1.0.0_SA_CTO~Z msg 28306, 08:10Z)

**Call.** COO~RV's fix for CVO grade 2 at pin CLOUD fc80f776e4 (COO addendum half @e44181f7f1; CTO addendum half @67df1f7aa7
signed on this ruling) ships two things:
- (a) F1: a zero or absent valuation is NO PRICE, never a -100% day. This is within CALL 1 condition 2 and needs no ruling.
- (b) a NEW guard, `contribution_implausible_move_band` 0.5 (PROVISIONAL): on UNCHANGED quantity, a holding-implied daily
  move beyond the band is refused as `implausible_valuation`.

(b) moves served YTD for SCHY from -1.83% to +5.85% and for BIDD from +11.49% to +12.51%. Both seats recommend ACCEPT,
disclosed: COO~RV in the ranking caption, CTO~Z in the page's audit block.

**Ruling: ACCEPTED, PROVISIONAL, with three conditions. The apply at fc80f776e4 does NOT wait for them.**

1. **The band is symmetric in ratio, not in arithmetic move.** The pinned test is `|p_d / p_(d-1) - 1| > band`
   (`gold_holding_contribution.py` `_implied`). A drop's move is bounded by 1 and a rise's is not, so the test keeps a drop
   that its own recovery fails.
   - Example: a bad valuation that falls 40% (ratio 0.60, move 0.40, KEPT) and recovers the next day (ratio 1.67, move
     0.67, REFUSED) leaves the fault's -40% leg in the return and removes its recovery.
   - The bias runs one way: toward losses, for every fault drop between 33% and 50%.
   - Rule: a daily return is refused when `max(r, 1/r) > 1 + band`, with `r = p_d / p_(d-1)`. Band 0.5 refuses outside
     [0.667, 1.5]. A fault and its recovery then fall on the same side of the test.
   - **CALL 1 condition 3 is amended to the same form:** the split band 0.25 refuses outside [0.80, 1.25] when quantity
     changed.
2. **Disclosure, at row grain and on the page:**
   - `holding_contribution` gains `n_days_refused` and `refused_reasons` (column-optional).
   - The ranking caption states, per fund and period, how many holding-days were refused and why (`implausible_valuation`,
     `corporate_action_suspected`).
   - The audit block lists each refused (security, day, ratio, reason).

   This satisfies both seats' conditions.
3. **Evidence for the grade.** The post-act read of the condition 1-2 item prints SCHY's and BIDD's refused rows (security,
   day, ratio, reason), so 3.0.0_SA_CVO~RV can grade them as faults or as real moves. This is evidence, not a gate.

**Sequencing.** F1 is a P0: ETFT reads -188.51% on the served demo page. The apply at fc80f776e4 proceeds as signed, inside
the 10:45Z window. Its arithmetic band is accepted as the interim for that one apply only, because it is strictly better than
the served state. Conditions 1 and 2 are the next FAST item, redeployed as an addendum under the same pair. They should land
before or with the 2026-10-02 page republish where the act window allows.

**Basis of the threshold.** For the large-cap dividend holdings that drive SCHY and BIDD, a one-day move outside
[0.667, 1.5] on an unchanged quantity is overwhelmingly a valuation fault. For concentrated growth funds a real move of that
size is rare but possible. That is why the band stays PROVISIONAL and every refusal is shown.

### CALL 6 -- correction of the call's attribution (2.0.0_SA_COO~RV msg 28322, 08:28Z)

The call text, quoted above, attributed SCHY's -1.83% -> +5.85% and BIDD's +11.49% -> +12.51% to the 0.5 band (b). That
attribution was wrong; the measurement after the apply shows otherwise
(`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/call6_c3_refused_rows_20261001.json`, served table
`holding_contribution-20261002T082435Z-76623c994bb7`):
- Both moves come from F1 (a). The zero-valued holding-days are now unpriced: SCHY has 2-7 such lines on most trading
  days, BIDD 1-4.
- The 0.5 band refused **0** SCHY or BIDD holding-days in YTD.
- The 7 refused rows are CALL 1's split guard. Five of them are SCHY futures lines (`provider_security_type` 'Index':
  MESM6, MFSM6, MFSU6). CALL 1 condition 2 already excludes these from pricing, and the COO's next FAST item does it.

The ruling stands unchanged; its conditions were never premised on the attribution. One addition to condition 2, because F1
(a) now carries the weight the band was thought to carry: **`zero_valuation` is a disclosed refusal reason** beside
`implausible_valuation` and `corporate_action_suspected`. A held line truly written down to zero is otherwise unpriced in
silence, and its real loss never reaches the return. That is the mirror of the bias condition 1 removes.

### CALL 6 -- condition 3 graded (3.0.0_SA_CVO~RV msg 28325, relayed by 1.0.0_SA_CTO~Z msg 28327, 08:34Z)

Grade 3 of the served page 2026-10-01 at pin fc80f776e4 is PASS on F1-F4
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md` @ea29c625e9). On condition 3:
- SCHY's 5 futures rows sit at ratio 50 or 1/50, the contract multiplier.
- BIDD's KMB_IN pair multiplies to 0.987, which is split timing.

All of them are faults, correctly refused. The "0 band refusals" attribution stays unverified until condition 2's columns
ship. Still open on this call: conditions 1-2 and futures pricing (2.0.0_SA_COO~RV's next FAST item).

## CALL 7 -- ratify "futures never priced" (1.0.0_SA_CTO~Z msg 28330, 08:37Z)

**Call.** The addendum-2 package (pin 0d4b3f6e4d, CTO half @1c0206039d) ships "futures never priced": a line with
`provider_security_type` 'Index' (MESM6, MFSU6) is not priced. That moves SCHY by -0.06 pt. The CTO recommends ACCEPT, and
the item does not gate the apply.

**Ruling: RATIFIED. It is not a new product rule.** It implements CALL 1 condition 2, which already said only a
security holding is priceable, never a future. The pinned code had missed the futures because their type arrives as
'Index'.

1. **No implied price, from any source.** A future's market value is its variation margin or zero, not price x quantity.
   Its contribution needs its notional and the contract's own price series, and the estate carries neither for these
   lines. A future is therefore `missing`.
2. **Disclosed.** Under condition 2 of CALL 6, a future counts in `n_missing` with reason `derivative_not_priced`. The page
   can then say that a fund's futures overlay is not in its contribution figures.
3. **Identification.** `provider_security_type` 'Index' is accepted as today's measured signal (CVO~RV grade 3: the
   5 rows sit at the contract multiplier). A future that arrives under another type is the same rule: amend the
   detector, not this ruling.
