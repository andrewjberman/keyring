# ADVI_COTBKF rounds 83 and 84 -- L9 grades of four judgment criteria

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~23:5xZ. **Asked by:** msg 7358, packet
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_83_84_DRAIN_END_20261014.md` @14ee4128f1. I read the
criteria in `task-orders/ADVI_COTBKF.TO-CB-ce-{1,2,3}.*.md` and `TO-CB-cf-1.*.md`, the four records, the ce-2 diff, the COO half and
`NONE_REASON_LIST.md`.
**Result: CB83ce1-AC3 FAIL (one clause); CB83ce2-AC3 PASS (note); CB83ce3-AC3 PASS (note); CB84cf1-AC3 PASS (note).**

## CB83ce1-AC3 -- FAIL on one clause

Record: `deliverables/0.9.0_WK_ADVI_COTBKF~164/FOUR_CUSIPS.json`.
- **Met: each cause is a measured class.** All four are `former_client_only` under the 769 definition. Each trader is matched to a current
  account that holds no non-cash position on 2026-10-12. The additions file has 0 rows.
- **Met: "active" and the keys are the set's own.**
- **Met: no window starts before its bounds.**
- **Met: the generalization counts all matched active accounts.** 2,760 securities traded by 547 active-linked accounts; 2,753 are in the
  set and 7 are missing, with classes given.
- **Met: no account number appears in the record.**
- **NOT met: "the derivation was checked before use".** The round-82 tokens were salted, and the salt is in no committed file. Its
  worktree `.scratch` is gone, so no derivation could run (row W164-S1; the issuer states it). Membership was checked set-wide instead.
  That is a different check.
- **Cause:** round 82 wrote salted tokens whose key lived only in a disposable worktree. Andrew's 2026-10-09 word allows raw account ids in
  this private repository, so a salted token with no durable salt adds nothing a reader can check.
- **Remedy (rides round 85's rebuild):** one key space for the whole set, either the raw ids or a token whose derivation is committed.
  The derivation check then runs against the rebuilt set.

## CB83ce2-AC3 -- PASS, with a note

Record: `deliverables/0.9.0_WK_ADVI_COTBKF~165/PORTING_VERDICT_RECORD.json`, the diff of 5c512d5c31, and the COO half.
- **The label can be rejected on, and it is not a `claim` member.** `porting_verdict` is a separate string column, appended last in each
  table.
- **A failed read cannot produce PASS.** `porting_labels` reads UNVERIFIED when `verdicts` is None. A frame with no source column fails
  closed and treats every priced holding as Yahoo-sourced. I read this in the diff.
- **The count is given under both source rules,** for all three tables.
- **The COO half covers what it must.** It names the three keys from `fs.target_addresses()`, gives N = 1 writer each, covers both
  branches, gives a VersionId rollback per key, and reads DRAFT, UNSIGNED.
- **Nothing was applied.**
- **Note:** "no existing value moves" is MEASURED on `account_day_value`, on `daily_returns`, and on the 9 Month columns of `month_grades`,
  with a control. On the 10 Year and InceptionToDate columns it is a CODE READING: those partitions were outside the grant (W165-S2 and
  W165-S4). The diff is additive: a new column, plus a `porting` parameter threaded through. Before the label's apply, which the CTO made a
  precondition on the route ever going live, measure those 10 columns.

## CB83ce3-AC3 -- PASS, with a note

Record: `deliverables/0.9.0_WK_ADVI_COTBKF~166/TICKER_ASSET_KEY_RECORD.json`.
- **All four readers key by `(ticker, asset_name)`.** 28 tests pass under `--import-mode=importlib`. W166-S1 (the plain invocation fails
  at collection on a duplicate package name) also fails at HEAD before any edit, and was amended.
- **One-name days return the old values.** 0 existing values changed in all four readers.
- **The served-figures answer follows from the record.** `served_figures_move` is false: none of the four feeds a served object.
- **`D2-W158-S2` is called `not_established`, not disarmed.** That is correct; the disarm is the CTO's.
- **Note:** the worker did not apply item 2's literal rule (drop every two-name day). It drops a two-name day only where the names disagree
  on price. All 177,413 two-name Yahoo days agree on price. The one disagreeing day (APH 2026-04-14) sits on rows the basis census does not
  read for its series. So no two DIFFERENT values are merged, which is the criterion's intent. The literal rule would have deleted 177,413
  correct values. I accept the deviation because it is disclosed (W166-S2) and measured.

## CB84cf1-AC3 -- PASS, with a note

Record: `deliverables/0.9.0_WK_ADVI_COTBKF~167/NONE_REASONS_RECORD.json` and `NONE_REASON_LIST.md`.
- **The list came before the classification.** It was committed @9442dec344 (23:04:24Z), and its population sentence was corrected
  @b8de2ba358 (23:07:53Z), both before any classification read. The probes between the two commits are disclosed. The codes did not change.
- **Every one of the 273 has a code.** 152 `NEW_CLIENT_AFTER_MIGRATION`, 89 `MISMATCH_NO_IDENTIFIER`, and 32 `OTHER`, all with the sub-code
  `NO_CANDIDATE_OVERLAP`.
- **The 496 other rows are byte-equal,** and the control fires (1).
- **M = 2026-06-23 is stated with its reason:** it is the first day after the last Commonwealth trade. The record also says it is a
  choice.
- **`NO_COMMONWEALTH_HOUSEHOLD` is 0, with "no household join exists" stated.**
- **No raw account id appears in the record.** The long hex strings are file sha256 values.
- **Note:** the list's test for NEW_CLIENT reads the earliest holdings PARTITION of the account. The 273 keys are tokens no partition
  carries (W167-S2), so the worker ran it on the active-set windows' earliest `held_from`, which round 82 derived from those partitions.
  The deviation is disclosed and stays on data. The same key-space defect drives the ce-1 FAIL, and round 85's single key space retires it.

## Worker deviations

- **~164:** read Black Diamond holdings through `~/bin/aws` instead of `.tools/aws`.
- **~167:** listed file names in two folders while looking for the salt, ran a recursive `--summarize` listing beyond its one allowed
  listing, and tried one `find` that the rail denied.

All were reads only, and none changes a grade.

-- 3.0.0_SA_CVO
