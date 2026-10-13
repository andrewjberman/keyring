# IRPT_ANLREQ round 20 (workstreams Y and YR) -- L9 grades

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~14:3xZ. **Asked by:** `2.0.0_SA_COO~Y2` msg 6974, packet
`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md` (section 3).
**Result: AR211-y-AC3J FAILS its first clause; the five AC2J criteria PASS on a sampled read; the AR212-y-AC1 and AR213-y-AC1 re-grades are
accepted.**

## This seat's live reads (14:21Z to 14:2xZ)

- **All eight packagers carry the signed values:** performance-adapter `NdwQsZ4Y`, narrative `vBzPCvn9`, status `vlGh380Q`, directory-search
  `tvrsQ+w8`, ycharts-generate `hpNfkhLt`, export-render `K74JEIjw`, holdings `d1HwIxeA`, 49f-reporting-read `WjnDxvu2`.
- **Errors since 12:30Z:** TypeError, Traceback and ImportError are 0 in all eight log groups. REPORT counts are 69 for directory-search and
  0 for the other seven, so the zero is vacuous for seven.
- **The irpt-holdings artifact key** (`opal-313476888478-lambda-artifacts`, `investor-reporting/irpt-holdings.zip`):
  - the three wrong versions are there (`T1NEd9G.` 07:42:43Z; `msFi8sD6` 10:52:50Z; `QCyspt0v` 10:53:08Z; each 294,243 B);
  - then the restore `hfQkgY1L` (11:24:26Z, 299,273 B);
  - then the release `YMQJgP4t` (12:45:08Z, latest).
  - irpt-holdings was last modified at 12:47:20Z, so no function ever ran a wrong version.

## AR211-y-AC3J -- FAIL on its first clause; clauses two and three hold

The rule: `template_reader.py` r19.2. **Clause 1, "the repair cannot turn back a one-account file the CVO's cases or their obvious
neighbours describe": FAIL.** I ran `_several_accounts` on one-account single-column sheets myself:
- The round-19 cases are closed: `Acct Market Value` with 25000000 and 31000000 returns `[]`, and so do `Acct CUSIP` and `Acct Lot`.
- **Their obvious neighbours are still turned back:** `Acct Cost Basis` (25000000, 31000000) and `Acct Gain` (12000000, 13000000) are the
  same money-integer class as `Acct Market Value`, and both return `('C', 'VALUES', 2)`. So do `Acct Weight`, `Acct Description`,
  `Acct Currency` and `Acct Custodian` with letter-and-digit values.

A 17-word attribute blocklist cannot list every attribute a custodian export names. The criterion's own words, "or their obvious
neighbours", are what fail.

- **Clause 2 (the changed identifier definition is stated and right): holds.** A run of 8 or more digits counts only when no value in its
  column carries a separator, and that is written at the constants.
- **Clause 3: holds.** `cabeb1ece6` precedes `77f804b5e2` (this seat's `merge-base --is-ancestor`).
- **The trade-off the issuer named is real, and it has a remedy that keeps both.** An allowlist alone (a root header enters the backstop
  only when its other words are identifier-tail words) would stop `Acct Alias` and `Primary Acct`, which today are read as account columns
  through the backstop. The remedy: the allowlist, with `alias` added to the tail words and `primary` to the modifiers. That closes every
  attribute neighbour, known or not, and keeps both identifier forms. The CTO chose the blocklist; this seat grades the criterion as worded.
- Built, not released, so the fail costs nothing live (row D2-S73).

## AR212, AR213, AR217, AR214, AR216 -y-AC2J -- PASS, on a sampled read

This seat read 2 of the 5 records:
- `~61/r20/STATUS_RULE_REBASE_GROUP_A.json` (AR-y-212): the live packages were read from AWS, each zip's sha256 equals its CodeSha256, and
  a holds-only build is the control.
- `~65/r20/RULE_EXPECTATIONS.json` (AR-y-216): before and after counts, a control that shows the 13 narrative failures are caused by the
  rule, and no test removed.

The live reads above agree with AR212 and AR213's claim that each release moves only `served.py` (`status.py` too for irpt-status): every
digest is the signed value. AR214's candidate is on portal DEV by MSTR on the CTO's approval, per the packet; this seat did not re-read the
portal diff this round.

## AR212-y-AC1 and AR213-y-AC1 (mechanical, re-graded by AMENDMENT @9405a1f285) -- accepted

The workers' FAIL rows stand. The amendment rests on AR-y-216's measured repair (narrative 56/13 to 69/0; directory-search 182/10/28 to
216/4/0; export-render 306/7 to 313/0). The 4 remaining `test_read_once` failures also fail with the original bytes. A re-grade that
names exactly the failures a measured later cell repaired, and the pre-existing ones, is right.

-- 3.0.0_SA_CVO
