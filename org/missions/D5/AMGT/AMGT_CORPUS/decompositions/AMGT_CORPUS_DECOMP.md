# AMGT_CORPUS -- L5 decomposition v39.0 -- ROUND 39 (the skip key; FWD-20's three page defects; FWD-21's FY+3 fit; the FWD drive; the FWD-14 four-class census)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-06 ~18:5xZ.

**Source:** `1.0.0_SA_CTO~Z` round-38 analysis `ledger/ROUND_ANALYSIS.round38.md` @`9619211bcf` s.4 (msg 30195, READ-acked);
PRD v0.8 (ADDENDUM C), both L4-R halves SIGNED (`prd-signoff.py status` reads ADMITTED; CVO sign @`daa0645141`). The rectangle is
the analysis's five items. Item 1 splits into the code cell and the issuer's served act that proves it. Round 38's decomposition is
kept as `AMGT_CORPUS_DECOMP.round38.md`. Base: CLOUD HEAD at the cut; portal origin/DEV `e2130d42`.

## 0. What this round IS

| # | item (analysis s.4) | cell | path | risk |
|---|---|---|---|---|
| 1a | The daily refresh's same-day skip keys on the PULL date, not the derived stamp (ruling 6, row Z-S88) | `CRPS-ao-1` | worker `0.9.0_WK_AMGT_CORPUS~1` (worker-light, direct act) | LOCAL |
| 1b | Re-pin `amgt-induction-daily` to the ao-1 drain; one same-UTC-day re-derive PLANT on one name before 13:00Z; read the 2026-10-07 13:00Z scheduled fire: the plant name is pulled, 96 pulled, rc 0. Disarms Z-S88 | `CRPS-ao-2` | the issuer's paired act (pair to `1.0.0_SA_CTO~Z`), after ao-1 drains | SERVED |
| 2 | FWD-20's page cell: the header-fact line names its currency; every in-row "--" carries a cell mark; each `UNMEASURED:` basis reads in a PM's words, the bare raw figure suppressed (rulings 2-4) | `CRPS-ao-3` | worker `0.9.0_WK_AMGT_CORPUS~2` (worker) | LOCAL (portal DEV candidate, CTO render review) |
| 3 | FWD-21's fit: the Model sheet shows FY+3 (2028E) unclipped at 1440 px on TSM and ASML; history byte-unchanged (ruling 5) | `CRPS-ao-4` | worker `0.9.0_WK_AMGT_CORPUS~2`, queued after ao-3 (same write set) | LOCAL (portal DEV candidate, CTO render review) |
| 4 | The read-only drive of FWD-10/11/12/15/16/18, each named limb, plus the round's one real run of FWD-20/21 on the page (ruling 8) | `CRPS-ao-5` | the issuer's read, after ao-3 and ao-4 land on DEV; walker slot from `0.0.0_AB_MSTR~Z` | LOCAL (read) |
| 5 | The FWD-14 four-class census: resolved / ambiguous / empty-or-workbook-only / unresolved-with-reason, summing to the folder count (ruling 1, ADDENDUM C) | `CRPS-ao-6` | the issuer's read (v0.8 is signed, so it runs at the cut) | LOCAL (read) |

**Chains:**
- `ao-1 -> ao-2` (the 2026-10-07 13:00Z fire is the acceptance clock);
- `ao-3 -> ao-4 -> ao-5` (ao-3 and ao-4 write the same Model-tab files, so they are one worker's queue; ao-5 walks the landed page);
- `ao-6` (no edge).

`fanout: 2 of 2 worker chains, cap 8`. Slot `~1` runs ao-1; slot `~2` runs ao-3, then ao-4 by continuation. The issuer runs ao-2,
ao-5 and ao-6.

**Write sets (disjoint):**
- ao-1: `integrations/bloomberg/research/model_block_pull.py` (`cmd_refresh` and its stamp helper only) + one new test + the
  round-34 refresh test's planting (it plants "current" through derived keys);
- ao-3: `portal/src/pages/SecurityAnalysis/modelSheet.ts`, `tabs/ModelTab.tsx`, `components/StatTile.tsx`,
  `components/HeaderCards.tsx`, `components/model/WhatChangedPanel.tsx` (the callers that pass the basis);
- ao-4: `tabs/ModelTab.tsx` (the sheet table's layout only) and `modelSheet.ts` (value formatting only, if the fit needs it).

No non-terminal order on any project names these portal files in `<paths>` (census at the cut over every task-order folder).
DSGN_AMGTV1 (`2.0.0_SA_COO~D`) maintains the Model tab's design; told at the cut.

## 1. The cells

**CRPS-ao-1.** `cmd_refresh` (`model_block_pull.py:2227`) skips a name when `_model_block_latest_stamps(s3)` (the newest
DERIVED stamp) reads today's UTC date (`:2243`). Round 38's an-2 re-derived the 96 at 03:20Z, so the 10-06 13:00Z fire skipped
all 96 and pulled 0 (Z-S88). The skip must key on the name's last PULL: the newest stamp under the pull-log state prefix
(`_state_pull_log_prefix`) or the bronze refdata/histdata stamps (`_bronze_prefix`). A same-day re-derive no longer silences the
fire; a same-day pull still skips.
- **Check** `checks/round39/skip_key_check.py` at the base: `skip build 0/1 control 2/2` (the PLANT name, derived 03:00Z today and
  pulled yesterday, is skipped). As expected.

**CRPS-ao-2.** Like round 38's an-2 shape, paired:
- (0) the pair: COO half + CTO half, blast radius = the task's pin and ONE plant name's derived stamp (its values re-derive from
  the same raw stamp, so values move 0);
- (r) re-pin `amgt-induction-daily` to the ao-1 drain commit;
- (p) after 00:00Z 2026-10-07 and before 13:00Z, re-derive ONE name (`BA_US_Equity`) from its current raw stamp;
- (v) read the 13:00Z fire's log: the plant name is in the pulled set, `pulled 96`, rc 0. That read, then the CVO's, is FWD-22's
  acceptance. Z-S88 disarms on it.

**CRPS-ao-3.** Measured at the cut on portal origin/DEV `e2130d42` with `checks/round39/ao_fixture.json` (captured from the real
read path for TSM, BA and ASML):
- (currency) `buildModelSheet`'s `v3Facts` carry `{mnemonic, label, value, unit}` and never `currency`
  (`modelSheet.ts:431`). 6 of 6 header facts with a served currency drop it. **Check** `ao3_check.cjs currency`: `build 0/1
  control 1/1`.
- (marks) TSM shows 99 in-row "--" cells with no reason: EPS, DPS and P/E across 2016-2025 (30, no history served), and 23 lines
  across 2026E-2028E (69, no consensus served). TSM's `fiscal_unresolved` is empty, so `cellReasons` is null on all 99.
  **Check** `ao3_check.cjs marks`: `build 0/1 control 1/1`.
- (words) `formatStatValue` renders TSM enterprise value as "unit not resolved -- raw figure 77,689,148.37" and net debt as
  "-2.00T currency not stated"; both figures' `currency_basis` read `UNMEASURED: ...`. **Check** `ao3_check.cjs words`:
  `build 0/1 control 1/1` (BA's resolved EV and net debt unchanged: "USD 184B", "USD 26.96B").

**CRPS-ao-4.** At 1440 px the Model sheet clips 2028E on TSM and ASML (2027E too on ASML) at the card edge
(`ADJUDICATION_v44.md`). The table is `w-full` inside `overflow-x-auto` (`ModelTab.tsx:480-481`). **Check** `ao4_check.cjs` at the
base: `ao4 control 2/2` (history and full sheet values unchanged; a control, so PASS at the base). The fit itself is the judgment
criterion, graded on ao-5's 1440 px walk.

**CRPS-ao-5.** With a walker slot from MSTR~Z (ARM, DISARM through it), after `:5174` answers 200, on the DEV build carrying ao-3
and ao-4:
- FWD-20: TSM, SAP, BA Model tab -- header facts with currency, every "--" marked, EV and net debt in words;
- FWD-21: TSM and ASML Model tab at 1440 px -- 2028E unclipped;
- FWD-10: IMB LN, open one pillar to its report and passage;
- FWD-11: a name whose pack carries no management reads ABSENT; ASML's roster count unchanged against round 38's 7;
- FWD-12: one name's cases against the SharePoint template's rows, order and labels;
- FWD-15: the header posture line cited; the Posture tab byte-unchanged against the round-38 capture;
- FWD-16: the docx control's recovered count before (round-38 served object) and now;
- FWD-18: the feed filtered to one pillar term.
Each limb is a named capture or read in the drain packet.

**CRPS-ao-6.** `python -m lib.research.corpus.backlog --coverage-dry-run` (read-only, `written NONE`): the four counts and the
folder count, beside FWD-19's partition.

## 2. Found at the cut (rows, not cells)

None new. Z-S88 stays ARMED until ao-2's fire read. Z-S87 is carried (analysis ruling 9).

## 3. Coverage

| cell | order | slot |
|---|---|---|
| CRPS-ao-1 | `AMGT_CORPUS.TO-CRPS-ao-1.skip-keys-on-the-pull-date.md` | `~1` |
| CRPS-ao-2 | the issuer's paired act (no order) | -- |
| CRPS-ao-3 | `AMGT_CORPUS.TO-CRPS-ao-3.model-page-currency-marks-words.md` | `~2` |
| CRPS-ao-4 | `AMGT_CORPUS.TO-CRPS-ao-4.sheet-fits-fy3-at-1440.md` | `~2` (after ao-3) |
| CRPS-ao-5 | the issuer's read (no order) | -- |
| CRPS-ao-6 | the issuer's read (no order) | -- |
