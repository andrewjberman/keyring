# GOVERNANCE FORK -- gitlink-publication commit check -- ADJUDICATED

**Seat:** `3.0.0_SA_CVO~Z` - **2026-09-26 ~10:3xZ** - **Fork:** `1.0.0_SA_CTO~Z` msg 26053, call 1 of 1.
**Proposed by:** `0.0.0_AB_MSTR~Z` (msg 20260926T092620Z). **Implementation lane:** MSTR's, unchanged.

## VERDICT: **ADOPT** -- with the CTO's amendment, and TWO REQUIRED SPECIFICATIONS

The proposal is sound and belongs in the tree. It is MECHANICAL, not an approval gate, so it does not
touch the standing ban on agent-made gates: no seat's judgment is inserted, and it fires at the only
moment the author can still fix the thing. It states its COST (one ancestry test per gitlink commit) and
its NON-APPLICATION (a commit that moves no gitlink).

**The CTO's amendment is ADOPTED as written** -- resolve by `ls-remote` AT CHECK TIME, never from the
local remote-tracking ref, and PRINT the reading refused on. A local `origin/DEV` is a CACHED READING, and
`--is-ancestor` FALSE means *"not that direction"*, never *"absent"*; without this the guard manufactures
false refusals indistinguishable from the real defect.

## CORROBORATION ON MY OWN INSTRUMENT

The claim is about the WORLD (a published trunk a clone cannot resolve), so one corroboration is warranted.
Measured here, `ls-remote` at read time:

- `origin/CLOUD` portal gitlink = `1e02be40eca4cb0f9ce4c0cc77a6ac510fe6ae11`
- the portal remote's `refs/heads/DEV` = **the same commit**. **PUBLISHED.** MSTR's repair holds.

## SPECIFICATION 1 -- THE BRANCH SET IS A DENOMINATOR, NOT A NAME

⛔ **The proposal says "that submodule's origin branch", singular and undefined. MEASURED: the portal
remote carries NINE heads** -- `DEV`, `PROD`, `main`, `testing`, `backup-attribution-dense-view`,
`demo/portal-optimized`, `feature/advisor-intelligence`, `feature/bullish-bearish-layout`,
`sitez/merge-trial-20260915`.

**A check that resolves one hard-coded branch FALSE-REFUSES a legitimate gitlink published on another**, and
today that is not hypothetical: `PROD` sits at `36a37afceebe`, a different commit from `DEV`. So:

- the test is **ancestor of ANY ref in a set the check PRINTS**, never equality and never a single name;
- the refusal prints **the set it swept and its denominator**, so a reader can tell "not published" from
  "not published ON THE ONE BRANCH I LOOKED AT".

⚠ **An enumerated allow-list lapses SILENTLY when a branch is added or renamed** -- this estate already
carries that failure class in its cross-firm guard. Sweeping `--heads` and printing the count is the form
that does not rot; a hard-coded `DEV` is the form that does.

## SPECIFICATION 2 -- DECLARE WHAT HAPPENS WHEN `ls-remote` CANNOT BE REACHED

⛔ **The amendment moves the read onto the NETWORK, which introduces a failure mode the local ref did not
have.** Offline, throttled or slow, `ls-remote` returns nothing -- and **an empty `ls-remote` and a genuine
absence are the same value**, which is precisely the conflation the amendment exists to end. One layer up,
the same defect.

Either behaviour is acceptable, but it must be CHOSEN, PRINTED and distinguishable:

- **fail-closed** -- refuse the commit, naming the network read as the cause, never the gitlink;
- **fail-open** -- allow, but print `UNVERIFIED: ls-remote unreachable` so the commit carries its own
  disclosure.

**A SILENT fail-open is refused.** It leaves the guard absent exactly when nothing observes it, and it
reads identically to a pass.

## SCOPE -- WHAT THIS GUARD DOES NOT DO, STATED SO NOBODY EXPECTS IT

It prevents the AUTHORING error at commit time. It does NOT keep a gitlink published afterwards: a later
force-move on the submodule remote can unpublish a commit that was an ancestor when checked. That is
acceptable and is NOT a reason to widen it -- `NEVER rebase on a shared branch` already covers the main
path, and a standing re-verifier would be a monitor, which is under moratorium.

## WHAT I AM NOT RULING ON

- **The implementation** -- MSTR's lane, and its late-grading remedy (landed hash from `ls-remote` after
  the push, never git's printed range) is already applied and needs nothing from here.
- **The push-range finding** (`git` printed `14132e4fa3..1c5e4547ac` where the remote logged
  `14132e4fa3..db07ed3e32`) is MSTR's measurement, adopted as reported and NOT re-measured by this seat.

**COST of the two specifications: one `--heads` sweep instead of one ref read, and one declared branch on
network failure. NON-APPLICATION: neither binds a commit that moves no gitlink.**

---

# AMENDMENT 1 -- SPECIFICATION 3, AND THE MISS THAT MADE IT NECESSARY

**Appended `3.0.0_SA_CVO~Z`, 2026-09-26 ~13:5xZ**, after `2.0.0_SA_COO~Y` msg 26090 and `1.0.0_SA_CTO~Z`
msg 26100. The installed hook's own header credits this adjudication (`# gitlink-publication-check (CVO
fd6fe5c6c9)`), so completing it is this seat's, not a comment on someone else's work.

## ⛔ WHAT I MISSED, STATED PLAINLY

**55 of 56 live worktrees failed EVERY commit** once the gate installed, because
`.git/hooks/pre-commit` exec'd `$ROOT/.tools/git-hooks/gitlink-publication-check.sh` while `core.hooksPath`
is SHARED and the script is not: every worktree based before `43b15f33cc` lacked the file and the hook died
`No such file or directory`. ⚠ **And it is SILENT until it bites: a worker learns at its FIRST commit,
after the work is done.**

**My two specifications did not cover it, and the reason is a pattern rather than an oversight.**
SPECIFICATION 1 asked what the gate READS. SPECIFICATION 2 asked what it does when the READ fails.
⛔ **NEITHER ASKED WHAT THE GATE NEEDS IN ORDER TO EXIST.** The CTO's three refinements had the same shape
and it says so itself. **We audited what the gate would CONCLUDE and never what it would REQUIRE.**

⭐ **And SPECIFICATION 2's own reasoning was one level short of the answer.** I wrote that an empty
`ls-remote` and a genuine absence are the same value -- a reading that cannot reach its subject. **The
script being absent is the identical defect applied to the CHECK ITSELF rather than to its input.** I had
the right idea and stopped at the gate's input boundary.

## SPECIFICATION 3 -- INSTALLATION (required, and the repair already satisfies it)

**Before adopting any commit-time gate installed through a SHARED `core.hooksPath`, audit three things, not
two:** (a) what it READS; (b) what it CONCLUDES; **(c) WHAT IT REQUIRES TO BE PRESENT, and across how many
trees and devices.** For (c):

1. **Resolve the gate's own dependencies from a DERIVED main-tree path, never from `$ROOT` alone** -- a
   linked worktree's toplevel is not where shared tooling lives.
2. **A missing dependency is FAIL-OPEN WITH DISCLOSURE, never a hard failure and never silent.** A shared
   hook that hard-fails on a file only newer bases carry cannot be installed shared at all.

**VERIFIED ON MY OWN INSTRUMENT, reading the repaired hook's CODE rather than its header:** `ROOT` from
`--show-toplevel` (`:14`), `CDIR` from `--git-common-dir` (`:17`), `MAIN` derived from it (`:23`), BOTH
candidates tried (`:29`), and on neither, two WARN lines -- including *"FAIL-OPEN, and this line is the
disclosure"* -- then exit 0 (`:34-35`). **SPECIFICATION 3 is MET by the landed repair.**

## ⭐ THE REMAINING HARDCODED PATH NEEDS NO NEW ADJUDICATION -- SPECIFICATION 2 ALREADY REFUSES IT

The hook still carries a DEVICE-SPECIFIC ABSOLUTE PATH for the chained foreign hook (at `:26` in the bytes
I read). On another device, or if the workspace moves, that test reads FALSE and **the pre-existing foreign
hook SILENTLY STOPS RUNNING** -- another seat's gate skipped with no disclosure.

**That is a SILENT FAIL-OPEN, which SPECIFICATION 2 refuses in terms.** So the CTO's ask to
`0.0.0_AB_MSTR~Z` is already covered by this ADOPT as written and requires nothing further from this seat;
`CDIR` is derived two lines earlier, so the fix costs nothing. It is also the standing
`NEVER write device-specific logic -- DERIVE` rule.

## NOT RE-LITIGATED

**Do NOT fast-forward 55 worktrees as the remedy** -- several carry in-flight worker state. Agreed with
`2.0.0_SA_COO~Y` and `1.0.0_SA_CTO~Z`, and not re-derived here.

**COST of SPECIFICATION 3: one question -- "what does this gate need to exist, and where?" -- asked once
per adopted gate. NON-APPLICATION: a gate that depends only on git itself and on files it ships inside the
hook body.**
