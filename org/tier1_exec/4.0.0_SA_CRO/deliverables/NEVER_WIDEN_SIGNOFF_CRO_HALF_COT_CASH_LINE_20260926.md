# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- COT: Black Diamond's cash line is `cash`, not the ticker CASH's equity

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_COT_CASH_LINE_20260926.md`
blob `0bf09da4344eef0a75c2fa0f4784948a640c4650` @`a746f2f9a1`. The code is branch `irpt-m-cot-cash-line` @`f28c0d89f2`
(`8a52e2c352` + `f28c0d89f2`), not merged.
**First half:** 1.0.0_SA_CTO, SIGNED (`SIGNOFF_COT_CASH_LINE_20260926.md`, msg 101570).
**Asked by:** 2.0.0_SA_COO~M msg 101563. This seat is not in the act.

## VERDICT: REFUSED on blob 0bf09da4 -- the C_06 guard is not on C_06's served path. Signed on sight on a re-cut that changes only that

The request names C_06's delta: 853 rows, net $59,253,165.31, largest z09305653 +$63,196,106.53. It also makes C_06 the
read-back ("read back z09305653's cash slice"). **C_06's own code does not produce that delta.** Read from branch
`irpt-m-cot-cash-line` @`f28c0d89f2`, `data/cot/scripts/gold/C_06.client_mix_timeseries.py`:

| Line | What it is |
|---|---|
| `:176` | `is_bd_cash_line`, the new predicate |
| `:184-186` | `classify_holding`, which carries the guard |
| `:199` | `classify_series` |
| `:215` | `classifier.classify(ticker, name)`: **no guard** |
| `:469` | `pos['asset_class'] = classify_series(pos['ticker'], pos['asset_name'])`: the one served classify, feeding the mix `groupby('asset_class')` |

- **`classify_holding` has no caller.** A search for `classify_holding|classify_series` over `data/` on CLOUD found 13
  hits in 6 files; INF's two are `_classify_holdings`, a substring match. `classify_holding` appears only at its two
  definitions (COT C_06 `:176` on CLOUD, BD C_06 `:182`) and, on the branch, in the new test. Nothing after `:469`
  re-classes the rows.
- **So after the deploy, D_03 and D_04 move BD's cash line to `cash` while C_06, the client mix, keeps it as equity.**
  Their guards sit on the served paths (branch line numbers): D_03 `_classify` inside `classify_series` `:130`, called
  at `:686`; D_04
  `_classify` `:1343` and `_classify_ticker` `:2913`. The served COT composition and portal summary would disagree
  with the client mix by about $59M, and z09305653's read-back would read no move.
- **The test cannot see this.** `test_the_bd_cash_line_is_cash_not_the_pathward_ticker` asserts the predicate and
  `c06.classify_holding`, never `c06.classify_series`. The D_03 test in the same file already calls `classify_series`
  (`test_other_admission.py:39`).

This half signs a blast radius and the outcome the producer's own rule gives (CLAUDE.md section 5). The request's
expected outcome for C_06 is not that rule's outcome.

**The re-cut, signed on sight if the diff is only this:**
1. The guard in C_06 `classify_series`: `if is_bd_cash_line(ticker, name): unique_pairs.at[idx, 'asset_class'] = 'cash'; continue` before `:215`.
2. Either delete `classify_holding` or leave it; it has no caller.
3. The test calls `c06.classify_series(pd.Series(["CASH", "CASH"]), pd.Series(["CASH", "PATHWARD FINANCIAL INC COM"]))`
   and asserts `["cash", "equity"]`.
4. One request line naming the correction.

## What stands as read (carried to the re-cut unchanged)

- **The rule itself.** Ticker `CASH` AND the asset name exactly `CASH`, with whitespace and case normalized. It never
  fires on the ticker alone (the test covers `FCASH`/`CASH` and Pathward's name). A row it does not match falls to
  today's behaviour, so the rule cannot widen.
- **The Holdings part** (`f28c0d89f2`). It keys on the row's own `display.description`, never the label. The 49F
  Pathward node (no description) stays equity, which is tested. It rides the R4 enable publication as its own class in
  the pinned diff, as the request says.
- **Order and rollback.** Merge and deploy only after Monday's ledger cot-cash-admission-m-20260925 R1 read-back,
  under its own ledger. Rollback per key is the prior S3 object version of each script and the prior Holdings
  revision. Pass: z09305653's cash slice rises by +$63,196,106.53 in C_06 AND D_04. A move in one without the other
  is a rollback.

## Named items (not refusal grounds)

1. **Negative cash.** The request says some moved rows are negative. Today they net inside equity. After the move, a
   relationship whose only cash is a negative BD cash line shows a NEGATIVE cash slice. The re-cut prints:
   - how many of the 29 relationships, and how many accounts, net negative in `cash`;
   - for each person-facing reader (C_06 mix, D_04 portal summary, the AI Cottonwood views), whether it renders a
     negative slice, or clamps or drops it.

   Zero relationships closes this item.
2. **a07 / d08.** The COT mix summary d08 keeps the line as equity until a07 takes the same rule. The owner question is
   with 0.0.0_AB_MSTR (CTO 101570). At the read-back, print d08's COT cash for z09305653 beside C_06's, so the gap is
   measured and dated, not assumed.

Not measured by this seat: the per-firm delta figures themselves (the request's), and the served Holdings node count.

## Addendum 1 (2026-09-26 ~23:0xZ) -- SIGNED on the re-cut

- **Request:** blob `f702d9d6db880dbccf6e78259e9b93a1420fd516` @`11b9e27d52`, the same at HEAD and on disk.
- **Code:** branch `irpt-m-cot-cash-line` @`9e3f568d42`, still unmerged. Asked by 2.0.0_SA_COO~M msg 101592.
- **The diff read here is only what the refusal asked for.**
  - `9e3f568d42` touches 2 files, +11/-4.
  - C_06 `classify_series` gains the guard before the classifier call (`unique_pairs.at[idx, 'asset_class'] = 'cash'; continue`), and it leaves `classify_holding`.
  - The test replaces the `classify_holding` assert. It calls `c06.classify_series` with a ticker-first fake classifier, the real loader's shape, and asserts `["cash", "equity"]` for CASH/CASH and CASH/Pathward.
- **From the request's addendum 1, not re-run here:**
  - `classify_series` over COT canonical 2026-09-22 classes all 853 CASH/CASH rows as cash, $59,253,165.31;
  - a census finds 5 classifier calls, and the 4 on served paths are guarded;
  - the one unguarded call is `classify_holding`, which has 0 callers.
- **Everything under "What stands as read" carries unchanged:** the order (after Monday's R1), rollback per key, and
  the pass rule (z09305653's cash rises by +$63,196,106.53 in C_06 AND D_04; one without the other is a rollback).
- **Named items 1 and 2 carry.** The addendum does not address them.
  - Item 1, the negative-cash census and the readers' rendering of a negative slice, is owed before the merge.
  - Item 2, d08 printed beside C_06 at the read-back, is owed at the read-back.

  Neither stops the signature.

## Addendum 2 (2026-09-26 ~23:3xZ) -- named item 1 answered; the D_03 part re-signs on its own diff

- **Request:** blob `8aca3995c3290a0e3dcb1fd93106bcc858003f90` @`eaca6a30de`, addendum 2. 2.0.0_SA_COO~M msg 101612.
- **CTO ruling (a):** msg 101617.
- **Named item 1 is answered, and it changed the act.**
  - No reader renders a negative slice.
  - But D_03 drops a class at 0 or below (`:407`) while its total keeps the negative. So 13 of 29 compositions would
    sum to 100.5%-128.0% under the re-cut as signed.
  - C_06's true delta is **+$66,055,897.80** (the 45 positive rows, 15 relationships; C_06:462 drops rows at 0 or
    below), not the net $59.25M. The pass rule on z09305653 (+$63,196,106.53 in C_06 and D_04) is unchanged: that row
    is positive, and D_04's firm mix takes C_06's values (`:565-583`).
- **This half stands on `9e3f568d42` for C_06, D_04 and Holdings.** The D_03 part does not deploy on `9e3f568d42`.
  Under ruling (a) it is new code (C_06's positive-rows rule in D_03), so it re-signs on that diff.
- **Condition for the D_03 re-sign, beyond the CTO's (1)-(3).** The rule drops more than the 3 personal-liability
  rows: it drops **all 26 negative cash-line rows (-$6,802,732.49)**. Before, those netted inside equity. After, they
  appear in no COT total. So D_03's relationship totals rise, and its percentages shift, for every relationship
  carrying such a row, which is at least the 17 that net negative on the cash line.
  - The pre-deploy measurement lists **every relationship whose D_03 total or composition changes** under (a): the
    cash-line debits and the 3 liabilities. Each row shows total before and after and composition before and after,
    with the count printed.
  - The half signs that list at its real size, not the 3 liability rows alone.
- **Named, not a condition (state coherence):** after (a), no COT mix shows a debit or a liability anywhere. That
  matches C_06's long-standing rule. Whether a viewer should see a net-of-debit value is not this act's question.

## Addendum 3 (2026-09-26 ~23:4xZ) -- D_03 SIGNED on 0deac23f1e; a correction of this seat's addendum 2

- **Request:** blob `7a6cd9abc354cf2f98d881ac7ef07d16bb60e811` @`625e331ded`, addendum 3. Measurement
  `D03_POSITIVE_ROWS_DIFF_20260926.json` beside it.
- **Code:** branch `irpt-m-cot-cash-line` @`0deac23f1e`, unmerged. 2.0.0_SA_COO~M msg 101627.
- **The diff read here** (2 files, +27):
  - `positive_rows()` keeps `market_value > 0`;
  - it is called once at `:671` in `main`, after the open filter (`:670`) and before ghost exclusion (`:681`) and
    classification (`:696`), and both input branches (`:650`, `:667`) pass through it, so it is on the served path;
  - one test asserts that the kept rows sum to 100% and that the raw rows exceed it.
- **CORRECTION to addendum 2.** It said D_03's relationship totals would rise in at least 17 relationships. **That was
  an inference, and it is wrong.**
  - `_build_composition` scales each composition to the canonical AUA when one is given (`:390-392`, printed here). So
    dropping negative rows moves the mix, never the total.
  - The request measured 0 totals moving across 223 scopes.
  - The ask it carried (list every moved scope) is met anyway, in the JSON's `material_moves`: the firm and 27
    relationships, plus 22 moving by under $1, listed.
- **As measured by the request (not re-run here):**
  - 0 of 223 compositions exceed 100.0% after (0 before);
  - all 17 cash-line net-negative relationships are in the moved set;
  - the largest move is z09305653, cash 0.4% -> 82.5% (its $63.2M cash line);
  - the firm's cash share goes 3.50% -> 15.33%;
  - the 3 liabilities, all in z09305672, leave a total of $8,838,093.55 unchanged, with the mix moving under 1pp per
    class.
- **The whole act now stands on `9e3f568d42` + `0deac23f1e`:** C_06, D_03, D_04 and Holdings. The order, rollback
  and z09305653 pass rule carry. After the deploy, the check re-reads 0 of 223 over 100.0% (tolerance 0.05pp), per the
  CTO's condition (2).
- **The liabilities classed `equity`,** dropped here only because they are negative, are ~M's own `other` half under
  R5, as the request routes it.

## Addendum 4 (2026-09-27 ~02:0xZ) -- S152 (COT mix_views) rides this act; ~X's B1 commits do not

- **Request:** blob `d5f8302da9ffab6a58f6295e925736b46107e0ba` @`dda9a80465`, addenda 4 and 5. 2.0.0_SA_COO~M msg
  101684.
- **This half's claim "No reader crashes or drops it" was wrong for COT `lib/mix_views`.** Its period rows built only
  from a list without `cash` and `other`, so every cash dollar landed in the `unclassified` residual (S152). The fix is
  `41115a70aa`, read here: the list gains `cash` and `other`, the residual comment is corrected, and a test is added.
  The portal's `FirmMixPeriodPoint` already expects `cash`.
- **YES: `41115a70aa` merges and deploys with this act, after Monday's R1, under its ledger.**
  - Pass, at the read-back, for the firm's period rows: before/after of `unclassified`, `cash` and `other` per
    period.
  - `unclassified` must fall by exactly the `cash` + `other` that now appear, and the latest period's `cash` must
    equal C_06's published cash for the same date. Any other change is a rollback of mix_views to its prior S3
    version.
- **NOT the branch as a unit.** `CLOUD..irpt-m-s152` is 6 commits in 17 files. Besides `41115a70aa` and the registry
  entry `9135feae97` (`comp-constants.config.yaml`, not executed), it carries 0.4.0_DS_ClientPlatform~X's four
  commits:
  - `2c23591d48`: 49F a07 cash-line rule; d06 admits structured, commodities and other;
  - `6e2864bd3e`: BD C_06, D_03, D_04 and mix_views admit structured and commodities;
  - `88bf469ebf`: COT d08 and mix_views;
  - `146876e75a`: measurement.

  Those are the ETF Part B **B1** step, signed as its own sequence (`NEVER_WIDEN_SIGNOFF_CRO_HALF_ETF_TAGS_WIN_20260926.md`).
  They deploy under B1's own ledger, with their own served read: admitting a class with no values moves nothing, and
  any `other` admission that does move a served value is traced to its signed half. So this act carries the S152
  change alone, or it waits for B1 to land first and then merges on top of it.
  - `41115a70aa` does not cherry-pick cleanly: its "before" line already holds ~X's `structured` and `commodities`,
    while CLOUD's list (printed here, `mix_views.py:19`) is `['equity', 'fixed_income', 'alternatives']`.
  - Standing alone, the S152 change on CLOUD is that list plus `cash` and `other`, re-cut as one commit and read by
    both halves before it merges.
- **d08** is QA-only and serves nothing, so its fold and its frozen shape are parked, as the request says. The
  read-back still prints its figure beside C_06's.

## Addendum 5 (2026-09-27 ~02:2xZ) -- the S152 re-cut SIGNED on ff63895521; a one-cent tolerance

- **Request:** blob `90bdb9784b56678b63fc6477f15b223833be8958` @`9926d14a9d`, addendum 6. 2.0.0_SA_COO~M msg 101697.
- **Code:** branch `irpt-m-s152-cloud` @`ff63895521`, one commit on CLOUD. It supersedes `41115a70aa`.
- **The diff read here** (2 files, +35/-1):
  - `MIX_ASSET_CLASSES` becomes CLOUD's `['equity', 'fixed_income', 'alternatives']` plus `'cash', 'other'`;
  - a new test;
  - `from __future__ import annotations`, forced by the commit gate, with no runtime effect.

  That is exactly what addendum 4 asked for, so it rides this act after Monday's R1.
- **The request's measurement** (660 period rows on 2026-09-22, not re-run here):
  - totals are unchanged in 660 of 660;
  - the identity `cash + other + unclassified_after == unclassified_before` is exact in 639 and off by $0.01 in 21,
    because `round(total * pct, 2)` rounds each class separately;
  - today's firm quarterly row already gains cash **$19,230,791.02** (sweeps now sitting in `unclassified`), before the
    BD cash line adds C_06's +$66,055,897.80.

  So the period views move on their own, not only through the BD line; the request names this, and this half signs it.
- **Ruling on the tolerance: YES.** At the read-back, "exactly" means:
  - per row, `|cash + other + unclassified_after - unclassified_before|` is at most $0.01 for each added class present;
  - total_aua is exactly unchanged.

  Anything beyond that is the rollback in the request's term 4: the prior S3 versions of C_06, D_03, D_04 and
  mix_views plus the Holdings revision, then a D_04 re-run.
