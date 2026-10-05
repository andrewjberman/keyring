# AMGT_CORPUS -- L5 decomposition v38.0 -- ROUND 38 (counts and ratios carry no currency; the FWD-20 currency page read; the 10-06 fire read; today's recovery run)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-05 ~14:5xZ.

**Source:** `1.0.0_SA_CTO~Z` round-37 analysis `ledger/ROUND_ANALYSIS.round37.md` @`b12904724c` s.4 (msg 29603, READ-acked). The
rectangle is its four items, plus one instrument repair the page read needs. Round 37's decomposition is kept as
`AMGT_CORPUS_DECOMP.round37.md`. Base: CLOUD HEAD at the cut.

## 0. What this round IS

| # | item (analysis s.4) | cell | path | risk |
|---|---|---|---|---|
| 1a | Count and ratio fields carry NO currency: the producer (row Z-W1-S35) | `CRPS-an-1` | worker `0.9.0_WK_AMGT_CORPUS~1` (worker-light, direct act) | LOCAL |
| 1b | The served re-derive of the 96 + re-pin; census of count/ratio figures with a currency reads 0 | `CRPS-an-2` | the issuer's paired act (pair to `1.0.0_SA_CTO~Z`), after an-1 drains, an-3 reads and an-5 settles | SERVED |
| 3 | FWD-22's regression read on the 2026-10-06 13:00Z fire on pin `3ffe37a57a` | `CRPS-an-3` | the issuer's read | LOCAL (read) |
| 2 (repair) | The /ui-walk walker closes the timeline day it opened before pressing the tabs (the TSM walk of 10-05 was occluded) | `CRPS-an-4` | worker `0.9.0_WK_AMGT_CORPUS~2` (worker-light, direct act) | LOCAL |
| 4 | Today's recovery run of the refused 10-05 fire (row Z-S87), on MSTR~Z's line after OPAL_BBGTML re-runs OK | `CRPS-an-5` | the issuer's act: the same pinned task re-invoked | LOCAL (the daily pull, re-run once) |
| 2 | FWD-20's currency limb read on the page: a signed-in walk on TSM (TWD), SAP (EUR) and BA (USD, the positive control) | `CRPS-an-6` | the issuer's read, after an-2 and an-4 | LOCAL (read) |

**Chains:**
- `an-1 -> an-2 -> an-6`;
- `an-4 -> an-6`;
- `an-3` (the 10-06 fire's own clock);
- `an-5` (on MSTR~Z's signal; struck at the 10-06 fire if capacity does not return today).

`fanout: 2 of 2 worker chains, cap 8`. an-2's re-pin lands after an-3 has read the 10-06 fire on `3ffe37a57a`, and after an-5 has run
or been struck. Both use the old pin, so no new code goes under a fire being read.

**Write sets:**
- an-1: `integrations/bloomberg/research/model_block_pull.py` (the currency classification only) + one new test + the granted
  currency tests;
- an-4: `.claude/skills/ui-walk/walk.mjs` (the timeline step only).

COO~D maintains walk.mjs; DSGN's open round-38 cells write other files.

## 1. The cells

**CRPS-an-1.** Measured at the cut over the 96 served blocks: 34,894 count/ratio figures (unit containing "(share count)", or
beginning RATIO / PERCENT), of which **932 carry a currency, all `IS_SH_FOR_DILUTED_EPS`** (unit `MILLIONS (share count)`). It
sits in `_CURRENCY_SENSITIVE_FIELDS` (`model_block_pull.py:230`), so `_figure_currency` gives it the reporting currency. Money
stays as round 37 left it: 31,985 money figures, 0 unlabelled. Every other currency on a non-money unit is legitimate: `PX_LAST`
is a price, and money fields with an unresolved unit are still money.
- **Check** `checks/round38/count_ratio_currency.py --derive BA_US_Equity,SAP_GY_Equity,BABA_US_Equity,TSM_US_Equity` at the
  base: `crc derive build 0/1 control 2/2` (31 IS_SH figures with a currency; money unlabelled 0, values moved 0, money labels
  changed 0; 4 puts captured, none sent). As expected.

**CRPS-an-2.** Like round 37's am-2:
- (0) gate: the census dry run, and `-Plan -Commit <an-1 drain>`;
- (d) 96 re-derives;
- (r) re-pin;
- (v) `count_ratio_currency.py --served` reads `crc served build 1/1 control 1/1`, plus v35 and al5.

**CRPS-an-3.** The 2026-10-06 13:00Z fire's log (96 pulled, rc 0), v35 over its stamp (0 pointer units) and the served money
census (0 unlabelled). It is a regression read, not a re-grade.

**CRPS-an-4.** `walkTimeline` presses the newest day bar and waits for the day's state. It then leaves the day dialog open, and the
tab steps' shots are taken under it (10-05 TSM walk, `tmp/ui-walk/20261005T135401Z`, shots 012/013).
- **Check** `checks/round38/an4_check.cjs` at the base: `an4 build 0/1 control 1/1` (no close after the last day wait;
  `node --check` passes). As expected. Its real proof is an-6's walk.

**CRPS-an-5.** On MSTR~Z's line (msg 29607: OPAL_BBGTML re-run and read OK first), `schtasks /run amgt-induction-daily` once, on
its own pin `3ffe37a57a`. Read the log: pulled 96, rc 0. One NEVER-2 entry. If the capacity does not return before the 10-06
13:00Z fire, the cell is struck there (analysis ruling 3).

**CRPS-an-6.** Run only with a walker slot from MSTR~Z (ARM and DISARMED through it). Run only after verifying the local `:5174`
answers 200 before arming. Each money row on the Model tab names its currency: TSM TWD, SAP EUR, BA USD.

## 2. Found at the cut (rows, not cells)

None new. Row Z-W1-S34 is INERT (no cell, analysis ruling 4).

## 3. Coverage

| cell | order | slot |
|---|---|---|
| CRPS-an-1 | `AMGT_CORPUS.TO-CRPS-an-1.counts-and-ratios-carry-no-currency.md` | `~1` |
| CRPS-an-2 | the issuer's paired act (no order) | -- |
| CRPS-an-3 | the issuer's read (no order) | -- |
| CRPS-an-4 | `AMGT_CORPUS.TO-CRPS-an-4.walker-closes-the-timeline-day.md` | `~2` |
| CRPS-an-5 | the issuer's act (no order) | -- |
| CRPS-an-6 | the issuer's read (no order) | -- |
