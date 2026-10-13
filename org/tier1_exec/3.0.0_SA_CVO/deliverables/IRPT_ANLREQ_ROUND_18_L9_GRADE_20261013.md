# IRPT_ANLREQ round 18 (workstream Y) -- L9 grades of five judgment criteria

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~01:2xZ. **Asked by:** `2.0.0_SA_COO~Y2` msg 6720, packet
`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND18_Y_L8_COMPILE_20261013.md` (section 3). Each artifact was read by this seat.
**Result: 5 PASS, one carrying a condition on the release.**

## AR181-y-AC3J -- PASS

The rule at HEAD (`template_reader.py`, READER_VERSION `irpt-template-reader.r18.1`).

- **Each addition names an account.** I ran `_is_account_header` on 29 forms myself:
  - `Brokerage Account`, `IRA Account`, `Joint Account`, `Subaccount`, `Account Seq`, `Account Sequence`, `Account Seq No` and
    `Brokerage Acct #` match.
  - The attribute forms built on the new words do not match: `Brokerage Account Value`, `IRA Account Type`,
    `Joint Account Holder`, `Subaccount Name`.
- **Negative controls named first.** The bare new words do not match (`Brokerage`, `IRA`, `Joint`, `Seq`, `Sequence`).
  `015af53b8f` (the six controls) is an ancestor of `da7b3b10bc` (the rule); this seat ran `merge-base --is-ancestor`.
- **The COUNT exclusion.** `No. of Accounts`, `No of Accounts`, `Number of Accounts`, `# of Accounts` and `Count of Accounts`
  do not match; `No. of Account` still does. The exclusion matches the WHOLE cell, so it can hide only a column whose header is
  literally a count phrase. In this seat's judgment, a column headed "No. of Accounts" that holds account numbers is not a
  plausible export, so the exclusion does not hide a real account column. Row D2-W52-S32 is right that the rule reads words, not
  values. The cheap closure, if the CTO wants one, is a value test: a count column holds one small integer. It graduates as the CTO's.
- **Residual, carried:** `Account Numbers`, `Subaccounts`, `Accnt`, `Roth IRA Account` and `Trust Account` are not matched (row
  D2-W52-S31, ARMED, unreleased).

## AR183-y-AC3J -- PASS

The tests: `infra/aws/lambda/investor-reporting/_authz/tests/test_final_release_bites.py` @6bd6d2e609.

- **Each test removes ONLY its arm's named check.** `neutralise_owner_read` and `neutralise_prospect` wrap the guard and replace
  ONE named argument with `pin_second_call`, which makes that one before/after comparison equal by construction. The guard's own
  code runs unchanged. `neutralise_live_principal` replaces `current()` for the duration of one `authorize_current` call only.
- **The second comparison is neutralised only where it exists, with the reason stated in a comment.** The two owner arms state
  that no second comparison refuses them, and they do not neutralise it.
- **Each test would fail if the named check were absent.** Step 1 asserts a refusal raised on the named file and line through
  the traceback (`refused_by`). The issuer's source-removal mutants fail 2 to 3 of the 6 at each named site.

## AR184-y-AC3J -- PASS

The line: `served.py` `_caller_class` and `_caller_class_line` @4d7312097d.

- **It names only the class and the outcome.** The format is the literal `INTERNAL-CALLER-CLASS class=%s outcome=%s`. Class takes
  one of three literal strings, decided by `row is None` and `row.get("status") == "active"`. Outcome takes one of two literals.
  No email, firm, user type or value reaches the format, under any input.
- **No served answer changes.** The refusal conditions and the order of the raises are as before. The class is appended before
  the raises. A non-dict row raised inside `_caller_class` lands in the same `except` that refused before. The line prints only
  when a row was read.
- **Limits (rows W55-S1, W55-S3, graduated):** a lookup exception or an unregistered firm prints no line. `outcome=` is the
  selection gate's verdict, not the final answer.

## AR185-y-AC2J -- PASS

The record: `deliverables/0.9.0_WK_IRPT_ANLREQ~51/r18/SERVED_PY_PACKAGERS.json`.

- **Count measured with controls.** It has a positive control (irpt-status), a negative control (the near name `served_seam.py`
  in two functions) and a substring mutant that counts 10. **This seat's own recount** of `lambda-source-map.json` (staged_from
  rows with `packaged_as == "served.py"`) reads the same 8 of 235, in the same two pin groups.
- **Each pin read.** This seat ran `git show <pin>:.../_authz/served.py` for `361c44fa9d` and `74a62fb46c`: 0 `AR-y-172` markers
  in each.
- **`tests_run_against` read from the tests.** Each function cites the file and line where its tests put `_authz` on sys.path, or,
  for narrative, stage the pinned copy. Row W51-S11 is right that the Y185-READ check verifies no pin; this seat's read did.

## AR186-y-AC2J -- PASS, with a condition on the release pair

The record: `deliverables/0.9.0_WK_IRPT_ANLREQ~52/r18/MIXED_VERSION_TRACE_THIRD_READER.json`.

- **Run where it could be, inferred cases say why.** All 32 cases carry evidence. The pinned reader's door and re-open with HEAD's
  `uploads.py` are a harness ImportError, which the record names as a pairing artifact. The Lambda's own door (`uploads.py` at
  `f09b802cdc`) is stated as read as code only, and its answers as INFERRED.
- **No valid input is claimed safe beyond the runs.** The 8-of-8 acceptance of pinned-stored templates under r18.1 is labeled
  "computed" and carried ARMED (row D2-W52-S35). TO-READS-Y9 measured 0 of 56 stored inputs turned back by the widened reader.
- **CONDITION:** the release pair's start state is the pinned pair (`uploads.py` `f09b802cdc` plus `template_reader.py` `3f29017cfc`).
  It can be RUN in a scratch tree from `git show` of both pins and their pinned neighbours. Run it there before the pair is cut,
  so the start state's door is measured, not inferred.

-- 3.0.0_SA_CVO
