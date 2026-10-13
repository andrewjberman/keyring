# IRPT_ANLREQ round 19 (workstreams Y and YR) -- L9 grades

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~07:1xZ. **Asked by:** `2.0.0_SA_COO~Y2` msg 6836, packet
`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND19_Y_L8_COMPILE_20261013.md` (section 3).
**Result: the 13 AC2J criteria PASS on a sampled read; AR194-y-AC4J FAILS its first clause; AR200-y-AC1's re-grade is accepted.**

## This seat's live read of the release (07:06Z)

`irpt-ycharts-generate` reads CodeSha256 `bNPCG2Oe1oQM/ztjggmrdDbdl83CAmUEcPnBFxlj2Rk=` (LastModified 06:27:22Z, Successful): the digest the
packet names. Since 06:27Z: Traceback 0, ImportError 0, TypeError 0, 1 invocation. The resident leg's read-back is the issuer's and its
applier's (0 of 297 not OK). This seat made no host call.

## AR191 to AR203 -y-AC2J (13 criteria) -- PASS, on a sampled read

Each asks the same: the run was real and not inferred, the compared artifact was read, a host-origin member is named and not fabricated,
and the readers were the portal's own functions at the named commits. This seat read 4 of the 13 records itself:
- `~52/r19/START_STATE_SCRATCH_RUN.json` (AR-y-191): "RUN, not inferred"; its one inferred item (the deployed code equals the map's pins)
  is labeled with its reason.
- `~56/r19/LAMBDA_LEG_LIVE_REBASE.json` (AR-y-201): the live package was read from AWS, and a holds-only control reproduces `NeAB50...`.
- `~58/r19/PORTAL_DEFER_SHAPE_READERS.json` (AR-y-203): RUN, 36 cases, through the moved folder's own functions at the named commits.
- `~55/r19/RESIDENT_RECIPE_AND_DELTA.json` (AR-y-199): the host pydeps names are recorded as MISSING, not invented.

Each carries a `not_read` list. The other nine rest on the issuer's re-run and their proofs (VALID). The sample found no claim beyond
its run.

## AR194-y-AC4J -- FAIL on its first clause; clauses two and three hold

The rule: `template_reader.py` r19.1 (`_has_account_root`, `_identifier_like`, `_several_accounts`).

- **Clause 1, "the backstop cannot turn back a one-account file": FAIL.** I ran `_several_accounts` on single-column one-account sheets myself:
  - `Acct Market Value` holding `25000000` and `31000000` (whole-dollar values with no separator, as an xlsx numeric cell reads) returns
    `('C', 'VALUES', 2)`: turned back as two accounts.
  - `Acct CUSIP` holding `912828ZT6` and `38141G104` (security ids, one account) is turned back.
  - `Acct Lot` holding lot ids is turned back; that is the worker's stated residual (row W59-S1).
  - Not turned back: decimals (`1250000.50`) and the full word `Account ...` (it is not a root).

  The cause: an account ROOT followed by an ATTRIBUTE word (market value, cusip, lot) still enters the backstop. A run of 8 or more digits
  reads as an identifier even when the column is money.
- **Clause 2 (the identifier-like definition is stated and right): holds as stated.** The definition is written at the constants and on
  the record; its 8-digit rule is what admits the money case above.
- **Clause 3 (negative controls named before the rule): holds.** `8170278635` is an ancestor of `920cdf69ca` (this seat ran
  `merge-base --is-ancestor`).
- **Repair (the cut is the issuer's):** a root header enters the backstop only when its other words are identifier tail words (the same
  test the header rule already uses), and a digits-only run is admitted only when no other value in the column carries a decimal point or
  separator. Built, not released: the fail costs nothing live, and it rides before the r19.1 release.

## AR200-y-AC1 (mechanical, re-graded by AMENDMENT 1) -- the re-grade is accepted

The worker's proof records FAIL, and that row stands. The amendment accepts exactly the two failures the CTO accepted as named limits
(msg 6778: S25, the held status.py's 24 correction words; S26, the nine fixtures not packaged). It does not widen to any other failure:
the issuer's run prints `Y200-TWO-OK`. Re-grading after a CTO acceptance is right when the acceptance names the failures and the
amendment names nothing more. The issuer's first statement that no gate limb graded it was wrong (GATE (viii) did, with no finding), and
the issuer said so.

-- 3.0.0_SA_CVO
