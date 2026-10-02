# ETFS_RIVALS -- DECOMPOSITION, ROUND 6 (ENRICHMENT): the A1 tables follow their inputs, the AI accounts in production, the plausibility guard, dividend currency and exits, the census's three states, names, and the 33-item page walk

```json
{
 "project": "ETFS_RIVALS",
 "round": 6,
 "prd_ref": "org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md (v0.12 @afc2bed44f; ADMITTED -- ratified-text half 3.0.0_SA_CVO~RV current, brief half CRO-written)",
 "prd_version": "v0.12",
 "analysis_ref": "org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round5.md@56c99763bb (section 4) + PRD v0.12 ENRICHMENT BACKLOG (RFW-D01..D14, RFW-U01..U19)",
 "author": "2.0.0_SA_COO~RV",
 "cells": 14,
 "chains": 6,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "round5_decomposition": "org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.round5.md"
}
```

**Issuer:** `2.0.0_SA_COO~RV`, 2026-10-02 ~15:2xZ, FULL. Andrew-direct ~14:1xZ (relayed by CRO~RV, msg 28530): "/canonical-drive with
max parallelization on subagents"; confirmed at this terminal: "yes you can move to /canonical-drive for the remainder"
(record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261002_141xZ_CANONICAL_DRIVE_MAX_PARALLEL_RELAYED.md`).
**Source:**
- the round-5 analysis section 4 (cells 1-7; cell 6 done under FAST, addendum 12; cell 7's code exists, so it is issuer act
  I-3);
- PRD v0.12's 33-item walk (order: RFW-D01 first, data before UI, every acceptance graded on the SERVED page with a positive
  control);
- CRO~RV CALL 13 (C1 amended for rk-2; C2 = this round's L5 rule).

**Input state (15:1xZ):**
- Lambdas at CLOUD 722f0db291 + the publish-page bronze-read grant.
- The served 2026-10-02 page is rv-publish-1002g (RFW-D01 fixed on today's page by the refresh_a1 republish, pair
  @c1bf9ac157 / @6507370187); 13 of 13.

## Issuer rulings at this cut

1. **Cut by write set (C10); six chains, every one spawned at once.** `fanout: 6 of 6 chains, cap 8`. N is bounded by M; each
   chain serialises one write set.
   - `~1` st-1 -> ap-1 -> r-6: `publish_page.py`, `ai_accounts.py`, the new `ai_stage.py` and `ai_client.py`, `guardrails.py`,
     `gen_policies.py` and its outputs, `main.tf`.
   - `~2` rk-2 -> sx-1: `gold_holding_contribution.py`, `gold_buying_trend.py`, `guardrails_config.json`.
   - `~3` e-2 -> x-1: `enrichment_bloomberg.py`, `gold_trade_schedule.py`.
   - `~4` ic-2: `gold_input_census.py`.
   - `~5` nm-1: `collector_bloomberg.py`, `silver_bloomberg.py`, `gold_canonical_shape.py`, the new `names.py`.
   - `~6` ui-1 -> ui-2 -> ui-3 -> ui-4 -> ui-5: `render.py`.
2. **Hookups belong to no cell; the issuer adds them at the merge (C10).** They are named here so no worker reaches for them:
   - `publish_page.handler_entry` calls `ai_stage.run_for_day(sink_spec, day)` after `produce_a1`;
   - `ai_accounts.default_client` returns `ai_client.default_client()`;
   - the producers' name selection calls `names.display_name`.
3. **Workers never call a vendor, never write S3, never deploy** (rounds 1-5). Every deploy, S3 act, Bloomberg act and
   OpenAI act of the round is the issuer's, each under its own never-widen pair:
   - the Lambda deploy after the drain;
   - the dedicated secret's value;
   - the vehicle-run drains after a morning read (e-2, x-1 and nm-1 touch vehicle-run files);
   - I-1 to I-4 below.
4. **Every check is issuer-written and dry-run at the base before the cut**
   (`deliverables/2.0.0_SA_COO~RV/round6/checks/`). The issuance commit carries one base line per check.
5. **CALL 13 C2 binds:** every judgment criterion names its positive control.
6. **Carried from the CTO~Z D01 half (@6507370187):** "the AI section states the table vintage it was written against
   whenever that differs from the tables served" -> cell u-4.

## Rulings reaching every cell

Rounds 1-5's rulings stand (`ETFS_RIVALS_DECOMP.round{1..5}.md`, "Rulings reaching every cell"):
- builder-only addresses;
- markers;
- one revision contract;
- per-source floors through `guardrails.load_config()`;
- the Positioning pull read-only (Andrew-direct no-modify);
- column-optional readers;
- the A1 contracts of round-5 amendment A1;
- CALL 5 (one AI run per page day; a FAIL is shown, never re-rolled; the key read at runtime, never persisted);
- CALLs 8-13 as ruled.

## 3. THE CELLS

### `RIV-st-1` -- an A1 table follows its inputs (RFW-D01 lead, RFW-D02)
- `publish_page.a1_stale(s, day, table) -> bool` is True when the newest G1 `canonical_shape` or G4 `security_market` object
  in the table's input window carries a revision timestamp (the `YYYYMMDDTHHMMSSZ` in its name) strictly later than the
  table's newest object's.
- `produce_a1` rebuilds a stale table without `refresh_a1`. The manifest's `a1_produced[<table>]` records
  `stale_rebuilt: true` and `stale_input` (the newer input's uri).
- A rebuild leaves the table NOT stale: its newest object's revision time is no earlier than the newer input's, even when its
  content is identical (today `write_unique` writes nothing on identical content).
- With no newer input, the table SKIPS as today.
- Shared fixture: `round6/checks/_d1_page.py`.

### `RIV-ap-1` -- the AI accounts as a production stage (analysis cell 1; RFW-D08)
- New `rivalfunds/ai_stage.py`: `run_for_day(sink_spec, day)` runs `ai_accounts.run_day(day, sink_spec,
  client=ai_client.default_client(), provenance={"run_path": "scheduled", ...})` when `RIVALFUNDS_AI_ENABLE == "1"` and the
  page day holds no `research_hypotheses` object. It is a no-op on a second call for the day (CALL 5).
- New `rivalfunds/ai_client.py`: `RestClient(api_key).chat(messages, model)` POSTs with `requests` (already in the layer) to
  https://api.openai.com/v1/chat/completions with `Authorization: Bearer`, model, messages, `response_format` json_object and
  temperature 0.2, and returns choices[0].message.content. `default_client()` builds a RestClient from the secret named by
  `RIVALFUNDS_OPENAI_SECRET`, read at call time. Web search is unavailable in the Lambda (VEW-2: a fallback only).
- The dedicated secret is named by `name()` (add an LGIC registry row if the builder refuses).
- `gen_policies.py`: `secretsmanager:GetSecretValue` on that ONE ARN, to the daily role alone. Its generated `lambdas` map
  gives the daily Lambda an `environment` {RIVALFUNDS_AI_ENABLE: "1", RIVALFUNDS_OPENAI_SECRET: <name>}; `main.tf` passes it
  through.
- The secret's value is set by the issuer at the deploy. Tests stub the transport.

### `RIV-r-6` -- the AI grader and prompt repairs (remediations; RFW-D09 prompt half)
- `grounding_check/5`: a digit run inside a market reading's own name, quoted in the text (a trending-topic headline), is not a
  figure. The run-time grade gets the names from the readings; the publish recheck (`guardrails.analysis_grounding`) gets
  them from the row's `input_vintages` keys. A bare number outside the name still fails.
- Prompt a1-chain/5: a security is named by its name, not its Bloomberg ticker form (CALL 10 style); a figure is written in the
  facts' display form, never rounded into a new number (RFW-D09).

### `RIV-rk-2` -- the A1 plausibility guard (analysis cell 2; CRO~RV CALL 13 C1 as amended)
- `gold_holding_contribution.plausibility_guard(df, bounds=None) -> df`, applied in `handler_entry` before the write.
- Per fund x period, never the table, the rows give way to ONE row: axis "refused", bucket = the bound, contribution = the
  offending value.
  - (a) a total below -100% -> `total_below_minus_100pct` (hard), checked first;
  - (b) one holding with |c| above `contribution_single_holding_bound` (guardrails_config.json, value 0.25, status
    PROVISIONAL) -> `single_holding_above_bound`;
  - (c) NAV reconciliation where a NAV is on file, its tolerance from the residual distribution. It ships as a documented
    hook; no NAV is on file today.
- The page's refusal display is u-2's.

### `RIV-sx-1` -- the no-sector bucket is never ranked (RFW-U16 and RFW-D06, producer half)
- `gold_holding_contribution.build`: a sector-axis "Unclassified" row keeps its contribution with rank_best and rank_worst
  NULL; real sectors rank among themselves and `n_ranked` excludes it.
- `gold_buying_trend.build`: the sector-axis "Unclassified" row has rank NULL, either lean value, and keeps its notional.

### `RIV-e-2` -- dividend currency (analysis cell 5; W3-S11; W3-S12 waits on I-2's probe)
- `DVD_CRNCY` joins the dividend request: the OFFLINE plan's `fields` list it beside `DVD_HIST_ALL`.
- `rows_from_responses` fills G3 `currency` from a security's `DVD_CRNCY`, NULL when absent.
- `gold_trade_schedule.dividend_ccy(security_key, g3_currency) -> (ccy, source)`: the G3 currency wins ("g3"); otherwise the
  suffix table answers, labelled "suffix_table", with the LN/SJ/IT mixed-unit rule unchanged. G5's income conversion uses
  it.
- W3-S12's child identity is code only after I-2 names a field.

### `RIV-x-1` -- a full exit is priced (RFW-D10)
- Measured at the cut: an exit whose line is ABSENT from the later report is already priced and only lacks a label. The served
  "n/a" comes from a line KEPT AT QUANTITY 0 in the later report, which today reads `trim` with no price or notional (TXUE
  ATD_CN_Equity 138,182 -> 0).
- An exit is a line with prior quantity above 0 that is absent from the later report OR at quantity 0 there. It reads action
  `exit`, `est_price` = the prior market_value / the prior quantity, and `est_notional` = `est_notional_base` = minus the prior
  market_value. A new G5 column `est_price_source` (in `SCHEMA` and `COLUMNS`) reads "prior_valuation".
- A line with prior quantity 0 is never priced this way. A 0->0 row (CRO CALL 12) stays as today.
- A trim or an add keeps today's values exactly.

### `RIV-ic-2` -- the census reads three states (RFW-D14, RFW-U11 data half)
- `gold_input_census` status gains "covered_by_fallback" with a new column `fallback`: "holding_implied" for a price,
  "other_fund" for a GICS sector taken from another fund's file (CALL 9).
- "missing" is only for an input no fallback covers; `fallback` is NULL where none applies.
- "arrived" stays arrived. The page can count per state.

### `RIV-nm-1` -- names, not raw tickers or 30-character cuts (RFW-D05, RFW-D11; RFW-U14 data half)
- The rivalfunds BQL capture asks for the name: `get(id(), name()) for(holdings([...],dates=D))`. `collector_bloomberg`'s
  `request_plan` and `excel_fetch` build the SAME string; it is tested offline with fake COM modules, never a live session.
- silver stores the `name()` header as column `name`, and `gold_canonical_shape.build_bloomberg_rows` sets `security_name` to
  it exactly as captured. Display casing is the page's.
- New `rivalfunds/names.py` `display_name(candidates: list[str | None]) -> str | None`:
  - blanks are dropped;
  - a raw ticker is `<id> XX Equity` or `<id>_XX_Equity`;
  - the longest real name wins, but a name of exactly 30 characters ranks below any other real name;
  - with no real name the first ticker is returned; with no candidates, None;
  - an ALL-CAPS winner is re-cased per run of letters ("Mitsubishi Ufj Financial Group", "S&P Global Inc", "3M Co");
  - a name with any lower-case letter returns unchanged.
- Hazard, the issuer's to prove LIVE after the drain: the real BQL response shape for `name()` is unknown offline. A duplicate
  header makes silver refuse the capture, and `excel_fetch` reads columns A-P only.

### `RIV-ui-1` -- page header and chrome (RFW-U01, RFW-U17, RFW-U15; the absence sentences)
- The current-funds count appears once, and the sentence names only lagging funds (absent when none lag).
- A fund header reads "Latest report 30 Sep", a source chip and a separate current/late chip.
- No SVG bar has a negative width (clamped >= 0).
- An absence reason starts with a capital letter ("No AI account. The ...", "Input census not available. The ...").

### `RIV-ui-2` -- the ranking panels (RFW-U02, RFW-U03, RFW-U04, RFW-U16 render half; rk-2's refusal display)
- The default period is the shortest that ranks at least one holding for the fund; an empty period's switch shows its state.
- A fund-period with 0 ranked renders ONE empty-state line with its reason and the count without a price.
- Each block carries a one-line count chip; the method text appears once per page, behind an info element.
- "Unclassified" is never a ranked row: it is a footnote with its share.
- A refused fund-period (rk-2) shows "Rankings refused" with its bound, marked `data-refused`, and no table.

### `RIV-ui-3` -- the buying trend card (RFW-U05, RFW-U06, RFW-U07)
- The month trend is a small SVG bar/sparkline, not ASCII marks.
- Net notional reads in $ millions with one decimal; names wrap to at most two lines.
- The BET/TILT definition sits behind the pill's tooltip, not inline in every block.

### `RIV-ui-4` -- the AI account cards (RFW-U08, RFW-U09, RFW-U10, RFW-D09 render half, RFW-U18; the CTO's vintage line)
- The cited-rows dump and provenance fields sit behind a collapsed details element.
- A stored reading key in the text DISPLAYS as its label (`ai_accounts.reading_label` or a render map); the stored text is
  not rewritten.
- The grade is a badge at the top; a FAIL account is collapsed by default, its reason in the summary.
- An account opens to its first two sentences.
- The card states the table vintage it was written against when that differs from the tables served.

### `RIV-ui-5` -- the census and the audit trail (RFW-U11, RFW-U12, RFW-U13, RFW-U14 render half)
- Census lists are grouped by reason with a count.
- Consecutive empty trade windows collapse into one line; the G6 exclusions show once per fund as totals.
- Plain words replace system words in the trade log; bronze keys and sha256 sit behind details.
- One display name per security across the page.

## ISSUER ACTS (no worker; each under its own pair)

- **I-1 (analysis cell 3): W4-S9's disarm.** ONE deliberate marker batch above 45 dates against the deployed Lambda; the first
  backfill batch is the carrier.
- **I-2 (analysis cells 4-5; RFW-D12, RFW-D13).**
  - The backfills: IDVZ, PFOE, ACWI, IWM.
  - The v0.8 leg's gate, after the request-cost measurement and the ACWI/IWM G9 preview.
  - The G5/G6 replay under its own pair.
  - The W3-S12 Bloomberg field probe.
- **I-3 (analysis cell 7; RFW-D04, RFW-D06 coverage): the G4 universe and price history.** The existing market pull's daily
  universe scope and its historical path over the YTD window, within the Bloomberg budget, cost measured first.
- **I-4 (RFW-D07): the per-fund arrival read.** Why IDVZ (home producer), BIDD, CGIC and SCHY had no 10-01 report by the
  publish, and the act it names.
- **Andrew's act (RFW-U19, FWD-1): the signed-in walk of the gateway route.**
- **The Lambda deploy after the drain**, its pair measuring every cell through the handlers, and the one real run of each
  outcome at close.

## 4. DEPENDENCY EDGES AND CHAINS

| chain | cells (serial) | writes |
|---|---|---|
| `~1` | st-1 -> ap-1 -> r-6 | `publish_page.py` (st-1), `ai_stage.py`, `ai_client.py`, `infra/aws/terraform/etfs-rivalfunds/{gen_policies.py, policies/, generated.auto.tfvars.json, main.tf}` (ap-1), `ai_accounts.py`, `guardrails.py` (r-6) |
| `~2` | rk-2 -> sx-1 | `gold_holding_contribution.py`, `guardrails_config.json` (rk-2), `gold_holding_contribution.py`, `gold_buying_trend.py` (sx-1) |
| `~3` | e-2 -> x-1 | `enrichment_bloomberg.py`, `gold_trade_schedule.py` |
| `~4` | ic-2 | `gold_input_census.py` |
| `~5` | nm-1 | `collector_bloomberg.py`, `silver_bloomberg.py`, `gold_canonical_shape.py`, `names.py` |
| `~6` | ui-1 -> ui-2 -> ui-3 -> ui-4 -> ui-5 | `render.py` |

## 5. BATTERY

`deliverables/2.0.0_SA_COO~RV/round6/checks/`, dry-run at the base. Each order's face names its checks; the issuance commit
carries every base line.
