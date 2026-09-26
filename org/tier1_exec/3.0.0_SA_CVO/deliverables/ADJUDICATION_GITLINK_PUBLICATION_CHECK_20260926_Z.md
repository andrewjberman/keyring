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
