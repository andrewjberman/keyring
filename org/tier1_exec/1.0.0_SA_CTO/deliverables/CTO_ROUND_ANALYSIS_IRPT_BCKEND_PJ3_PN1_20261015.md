# CTO ROUND ANALYSES -- IRPT_BCKEND (~P2): ~PJ round 3 (the holdings overlay) and ~PN round 1 (the Scope feed and household lift) (2026-10-15 ~18:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` msg 8531 (v127 @ca16619ae9) and msg 8532 (v128 @8e7748750d), both MAY-CLOSE, on the shared packet
@9ac52f5198.
**No PRD addendum.** Folded into `~P2`'s ONE issuance with the ~PL1/~PJ2 analysis @b8810197f6.

## ~PJ round 3: the holdings release pair is NOT signed on this blast radius

`holdings_snapshot.py` at the overlay pin and at HEAD carries two things the release must not ship:
- the unreleased IB-pr-536 one-date bypass (`allow_older_date` 10, against 0 at both minting pins);
- a reversal of 49F's CUSIP port (12 CUSIP lines at b1d354cfc9, 2 at the overlay).

The HEAD build would also move the 6 drifted members. That is wider than my analysis @57266eeb77 scoped, and I agree with the CVO.

**RULED:**
1. **The CTO half for the IB-pr-580/582/583 pair is withheld until the transplant (IB-pr-595) shows, per firm, a member diff against that
   firm's LIVE bundle equal to the exemption alone.** That means:
   - `allow_older_date` reads 0, as at the minting pins;
   - 49F's 12 CUSIP lines are present;
   - none of the 6 drifted members moves.
   A COO half bound to a wider diff is refused, not signed with a condition.
2. **The bypass and the CUSIP reversal are each a finding of their own** (row S206, `~P2`).
   - The bypass ships only under its own pair and its own ruling.
   - The CUSIP reversal is read for its cause: which commit dropped the 10 lines, and whether HEAD is wrong for 49F today. That is a READ in
     this issuance. If HEAD is wrong, the fix is a build cell before any holdings release.

## ~PN round 1: the Scope feed is repository-only; two apply checks are added

Nothing is deployed: the feed script is 404 on the runner, and the runner's dispatch object is unchanged since 08-30. The performance
adapter still runs the pre-merge account mapping, whose release is its own cell.

3. **W429-S4, imports from outside the synced prefixes, is a STOP check in the addendum-1 apply order.**
   - Before the catalog edit, the apply runs the feed once on the runner in dry-run mode (no write).
   - An import failure is a STOP, and the fix is packaging the dependency into the feed's code object, never a sync rider.
4. **W429-S5, a partial key after a 429 stop, is ruled at the build, not the apply: a day's key is written only when the day is
   COMPLETE.**
   - Complete means every household for that day either returned or was recorded with a reason class.
   - A run that stops on a 429 writes no key for an incomplete day, so the absent-first rule can never freeze a partial day.
   - The cell is a build criterion with a test: stop after N of M households, and the day's key reads ABSENT.
   - This also binds the backfill (my addendum-2 half, condition 2, which assumed whole days).
5. **W430-S2 (the RECORD FACE reached a worker) is a process finding for the issuer.** `~P2` states in its next issuance commit how the
   worker face is cut. It is not a gate. W430-S3 (a stale comment) is hygiene at the drain.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (~18:3xZ): IB-pr-596 STOP gate (f), the feed bucket against the runner role; and the CUSIP read (`~P2` msg 8549)

**The feed's home is canon-correct, so the remedy is (a), an IAM pair, NOT (b), a registry change.**
- `address()` places the feed in `opal-data-assets/orion/inflection/{bronze,silver}/scope_account_returns/`. That is
  `infra/logic/registry/tiers.json` FIRM bronze and silver, shared home `opal-data-assets`, doctrine R4: "bronze and silver have one home".
- Pointing the registry at `opal-data-inf` would be a deliberate departure from R4. Under CLAUDE.md rule 30 that is an R20 register entry
  Andrew acknowledges, not a fix.
- The existing Orion Inflection prefixes in `opal-data-inf` are legacy, and each reaches conformance through its own migration (R19).

**RULED (a): a never-widen IAM pair for `inf-gold-layer-ec2-role`, scoped to exactly the feed's two prefixes:**
1. The actions are `s3:PutObject` and `s3:GetObject` on `arn:aws:s3:::opal-data-assets/orion/inflection/bronze/scope_account_returns/*`
   and `.../silver/scope_account_returns/*`, plus `s3:ListBucket` on `opal-data-assets` with an `s3:prefix` condition naming those two
   prefixes only (the read-ABSENT-first needs it).
2. No wildcard above `scope_account_returns/`, no Delete, and no other firm's prefix. Under the cross-firm law, the shared bucket's fence
   is the key prefix plus the IAM condition.
3. It goes through Terraform and `safe-apply` under its own ledger. The plan reads 1 policy change. The pair's Branch A runs a `simulate`
   of PutObject that is allowed on the feed key and implicitly denied on a sibling `orion/inflection/` key; that negative control is
   required. Branch B reverts the statement.
4. IB-pr-596 resumes after this pair applies, with gate (f) re-read live.

**The CUSIP read (item 2 of msg 8536) is closed:**
- The port 01e843ce2e was undone on pin 2 by 5fad7eaaa8, per my round-197 ruling ("ship the cash rule WITHOUT the CUSIP port; the port gets
  its own release"). It was merged at de08782c38.
- Pin 1 (b1d354cfc9), which the live 49F bundle runs, keeps it. So the port is LIVE for 49F today, and HEAD lacks it.
- My ~PJ3 ruling stands: a release must leave 49F's live CUSIP lines unchanged.
- HEAD's lack of the port is a hazard for any future HEAD build, carried in row S206 (`~P2`). It is closed only when the port's own
  release lands on HEAD (its owner is MDPF_SECCLASS's issuer), not by this release.
