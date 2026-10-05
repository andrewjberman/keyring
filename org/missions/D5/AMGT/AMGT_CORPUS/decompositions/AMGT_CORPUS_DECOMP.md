# AMGT_CORPUS -- L5 decomposition v37.0 -- ROUND 37 (a currency on every money figure, in-row gap reasons, the `--pick` repair, the carried fire read)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-05 ~00:3xZ.

**Source:** `1.0.0_SA_CTO~Z` round-36 analysis `ledger/ROUND_ANALYSIS.round36.md` @`4c3e3755a7` s.4 (msg 29335, READ-acked). The
rectangle is its four items. Round 36's decomposition is kept as `AMGT_CORPUS_DECOMP.round36.md`. Base: CLOUD HEAD at the cut;
portal origin/DEV @`c66d08f346` (it carries round 36's `75efe9d6`).

## 0. What this round IS

| # | item (analysis s.4) | cell | path | risk |
|---|---|---|---|---|
| 1a | Every money figure carries its currency: the producer | `CRPS-am-1` | worker `0.9.0_WK_AMGT_CORPUS~1` | LOCAL |
| 1b | Re-derive all 96 blocks with it, and re-pin the daily task to the commit carrying it; control census reads 0 | `CRPS-am-2` | the issuer's paired act after am-1 drains (pair to `1.0.0_SA_CTO~Z`) | SERVED |
| 1c + 2 | The page names each money row's currency, and a gap inside a showing row says why | `CRPS-am-3` | worker `0.9.0_WK_AMGT_CORPUS~2` | LOCAL (portal candidate; DEV push on Andrew's word) |
| 3 | Row Z-W4-S4: `induction_request --pick` writes nothing | `CRPS-am-4` | worker `0.9.0_WK_AMGT_CORPUS~3` (worker-light) | LOCAL |
| 4 | al-4, carried: the 2026-10-05 13:00Z fire on pin `74e00624b0` | `CRPS-am-5` | the issuer's read (no order) | LOCAL (read) |

**Chains:** `am-1 -> am-2`; `am-3` (alone: it reads the served `currency` and `fiscal_unresolved` fields, both already in the
payload contract); `am-4` (alone); `am-5` (alone, on the fire's own clock). `fanout: 3 of 3 worker chains, cap 8`. Write sets are
disjoint:
- am-1: `integrations/bloomberg/research/model_block_pull.py` (the currency classification only) + one new test file;
- am-3: `portal/src/pages/SecurityAnalysis/{modelSheet.ts, tabs/ModelTab.tsx}`;
- am-4: `lib/research/corpus/induction_request.py` + one new test file;
- am-2: the served blocks, the Scheduled Task pin, its ledger entry.

**Sequencing with am-5.** am-2 re-pins the task the 10-05 13:00Z fire runs on. am-5 reads THAT fire on pin `74e00624b0`, so am-2's
re-pin lands only after the 13:00Z fire has been read (the round-35 ak-4 timing rule: never put new code under a fire being read).

## 1. The cells

**CRPS-am-1 (ruling 1, the producer).**
- **The defect, measured at the cut** (`checks/round37/money_currency_census.py` over the 96 served blocks): 32,176 money figures,
  of which 8,578 are labelled, 42 are null WITH a reason (round 25's UNMEASURED/UNSTATED census holds), and **23,556 are null with
  no reason** (basis "invariant"). TSM alone has 168. The cause is `_figure_currency`
  (`model_block_pull.py:1135-1167`), which labels only `_CURRENCY_SENSITIVE_FIELDS` / `_DENOMINATION_REPORTING_MNEMONICS` members
  and PX_LAST. Every other money field falls to "invariant".
- **The act:** every money figure gets its currency from the block's two header currencies: the REPORTING currency for a reported
  value, and the QUOTE currency for a market value. Which one applies is read from Bloomberg's definition and the landed values,
  never assumed. Round 25's held-out census figures keep their reasoned null.
- **Issuer ruling on the analysis's control "null-currency census reads 0":** a null that names why (UNMEASURED/UNSTATED, 42 at
  the cut) is a value carrying its claim, so it is not counted as unlabelled. The census reports it separately.
- **Check** `checks/round37/am1_check.py` at the base: `am1 build 0/1 control 2/2`. Build: 913 unlabelled money figures on
  TSM/1299 HK/SAP/BA, unchanged by an in-memory re-derive. Controls: 0 values moved, 0 labelled currencies changed. The 4 puts were
  captured and never sent. As expected.

**CRPS-am-2 (ruling 1, the served move; the issuer's paired act after am-1 drains AND after am-5's read).** One NEVER-2 entry,
like round 35's ak-4:
- (0) gate: the census dry run;
- (d) one `stage_derive(..., sa_fallback=False)` per registered name on its newest raw;
- (r) `schedule_induction.ps1 -Register -Commit <am-1 drain>`;
- (v) `money_currency_census.py` reads `null_unlabelled 0` over the 96, with 0 values moved against the prior blocks.

Without (r), the next scheduled fire would re-derive with the old pin and drop the labels again.

**CRPS-am-3 (rulings 1 and 2, the page).** `buildModelSheet` adds to every row:
- `cellReasons`: aligned with `cells`, a reason in PM words where a cell is empty and the served `fiscal_unresolved` names that
  mnemonic and year;
- `currency`: the one currency the row's money figures carry, or null.

`ModelTab.tsx` shows each gap reason (a hover or a footnote mark per gap year) and prints the currency beside the row's amounts.
Nothing is invented on the page.
- **Check** `checks/round37/am3_check.cjs` on portal DEV `c66d08f346`: `am3 build 0/2 control 2/2`. Build: b1 1299 HK has 92 gap
  cells with 0 reasoned; b2 TSM has 13 money rows and 0 expose a currency field. Controls: the 17 rows and the V3 row list are
  unchanged against `am3_base_snapshot.json`; round 36's `al2_check` still reads 3/3 + 1/1. The fixture `am3_fixture.json` was
  captured from the real read path (TSM: 400 fiscal figures, 0 fiscal reasons; 1299 HK: 543, 97). `modelPattern.harness.cjs`
  reads `CHECKS-OK 12 of 12` at the base. As expected.

**CRPS-am-4 (ruling 3, row Z-W4-S4).** `python -m lib.research.corpus.induction_request --pick` writes nothing. No module reads
the stored `induction_request.json`: `induction_run` rebuilds the request fresh (`induction_run.py:160-169`).
- **Check** `checks/round37/am4_check.sh` at the base: `am4 build 0/1 control 1/1` (the planted sentinel was rewritten; the run
  still decides, with rc 0 and `vendor_calls 0`). As expected. The check restores the file byte-exact.

**CRPS-am-5 (ruling 4, the carried read).** After the 2026-10-05 13:00Z fire: the run log's closing and refresh lines (96
pulled, rc 0), `checks/round35/v35.py` over the fire's stamp (0 pointer-unit figures), and `checks/round36/al5_served.py --where
deployed` (1/1 + 1/1). It is a Monday, so the content is Friday's close.

## 2. Found at the cut (rows, not cells)

None new. The 42 reasoned nulls are not defects (ruling above).

## 3. Coverage

| cell | order | slot |
|---|---|---|
| CRPS-am-1 | `AMGT_CORPUS.TO-CRPS-am-1.every-money-figure-carries-its-currency.md` | `~1` |
| CRPS-am-2 | the issuer's paired act (no order) | -- |
| CRPS-am-3 | `AMGT_CORPUS.TO-CRPS-am-3.model-sheet-gap-reasons-and-currency.md` | `~2` |
| CRPS-am-4 | `AMGT_CORPUS.TO-CRPS-am-4.pick-writes-nothing.md` | `~3` |
| CRPS-am-5 | the issuer's read (no order) | -- |

## 4. Acts for Andrew (cited from the analysis)

- The portal DEV push of am-3 after `1.0.0_SA_CTO~Z`'s review.
