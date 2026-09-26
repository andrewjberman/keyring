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
