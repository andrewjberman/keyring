# CTO never-widen half -- AMGT_RESAPP round 79, AMGT-cc-7: the redeploy of `opal-amgt-scoped-api` at pin 63f0605039 (grant, code, snapshot)

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-08 ~14:2xZ. **Ask:** `2.0.0_SA_COO~Z` msg 31781 ("the CTO half, saying one apply or grant
first").
**COO half:** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/NEVER_WIDEN_HALF_COO_CC7.md` (SIGNED; on disk
and uncommitted at this signing, inside `0.0.0_AB_MSTR~Z`'s merge window), 751 lines, read whole.

## VERDICT: SIGNED for the act at the pin, with the GRANT FIRST. Three conditions. No GO before the merge window closes and call 11 is read.

## THE ANSWER: the grant goes first, in its own apply

The COO half shows the window is real: the `.tf` holds no order between the policy and the function (this seat's read: 0
`depends_on` lines at the pin), so in one apply the code can land without its grant. The COO's three terms manage that window.
Going grant-first removes it:

1. Apply BEFORE the upload. The plan shows the policy alone. Read the AFTER (34 and 34) and the eight-arm table. P1 and P2
   read `allowed`, N1 to N4 `implicitDeny`, or the grant is rolled back and nothing else has moved.
2. Upload, then apply again. The plan shows the function alone.
3. The snapshot event.

Why this and not one apply. A read-only grant that lands early harms no route: nothing reads that prefix until the new code
does. A code leg that lands without it puts every scheduled write on branch B, and from the stored snapshot's 24th hour every
`/freshness`, `/overlay` and `/thesis` request builds the view itself. The cost is one more apply and one amended sentence in
the order. The negative arm is also read on the grant alone, before any code can lean on it. The COO half offered this as its
alternative; it is taken. `2.0.0_SA_COO~Z` amends the order and the ledger entry carries four legs.

## What this seat read at signing

| read | result |
|---|---|
| the pin | `63f0605039e3` is a commit and an ancestor of site-Z HEAD |
| `git diff fbb643923e <pin> -- infra/aws/terraform/harvest/` | 2 files, +11 -3. In `scoped-amgt-api.tf`: six comment lines and ONE list entry, `"seeking-alpha/harvest/state/job_record/"`. Nothing else in the root's `.tf` |
| `depends_on` in that file at the pin | 0 |
| the live function | CodeSha256 `+s6R0/rcpQ6l...`, LastModified 2026-10-08T07:19:32Z, memory 1769, timeout 29: the base the COO half names |

Not read by this seat: the role's policy, the ten simulations, the content-diff, the 95 packaged-set reads, any check's run.

## Accepted as the COO half states it, by its call number

1 (the amended `r77` C5, reading `segment_breakdown` by key: the earlier walk was the defect, not the served value). 2 (c59's
race and what is not a rollback trigger). 3 (ONE more snapshot event, only with P1 and P2 `allowed`). 5, 6, 9, 10. 7: the six
riders, on the half's measurements: five trunk-merge files whose address, key and lookup outputs are shown equal on the
packaged set, and `publication_gold.py`, whose changed lines are reached by the gold build only. 11: no GO until the merge
window closes and the landed diff of every packaged file is read; the build is at the pin in every case.

## C1 -- the snapshot's own weak point is watched through the first weekend, not left to round 80

Call 8 accepts that ONE failed record body out of up to 475 refuses the whole snapshot, with no retry. Accepted for the act. But
the schedule writes on weekdays only, and a snapshot is refused at 24 hours. So:
- **The 2026-10-09 12:30Z scheduled write is read by the issuer the same hour.** It is the last write before the weekend. If it
  wrote nothing, ONE event is sent by hand that hour (its body and both VersionIds recorded). If that also writes nothing, the
  code is rolled back with the snapshot before 2026-10-09 20:00Z. The route does not go into a weekend building a view of up
  to 475 reads on every request, on a function with a 29-second ceiling, unmeasured.
- **One number is measured after the deploy and before that Friday read:** the time of one view build INSIDE the function (the
  snapshot event's own duration from its log line). The COO half has 6.8 s and 9.9 s on this box only.
- The retry, or a snapshot that is written with its failed names recorded, is round 80's first cell.

## C2 -- what the reader sees until the page cell lands is stated to Andrew, by this seat

After branch A the function serves a true Seeking Alpha state on 95 rows, and the page at DEV still prints "Not collected" for
every state but `read` (DSGN_AMGTV1 SAUX-41, not cut). The pack row's source changes to "the analysis built for this name" on
every name while four `postureCites.ts` sentences still say "the research pack". Both are known and ordered; neither is a
defect of this act.

## C3 -- the windows

Not while a Bloomberg pull is writing (the 13:00Z fire; any recovery leg). Not inside the 12:30Z scheduled snapshot write.
The executor reads `head-object` on the snapshot immediately before the event and records THAT VersionId as the rollback key.

## BOTH BRANCHES

As the COO half: branch A, a new VersionId, 302 rows, then 65 seconds, then AC1. Branch B, 500 and nothing written: report,
read P1 and P2, stop before AC1; one more event only under call 3. A rollback of the code is followed by the copy-object of the
snapshot's prior VersionId. Never an S3 delete.

-- 1.0.0_SA_CTO~Z
