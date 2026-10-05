# COO half -- IRPT_BCKEND release r54 (reduced set: the holdings-performance functions)

**Signer:** 2.0.0_SA_COO~P. **Signed on:**
- the plan `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/RELEASE_R54_PLAN_20261005.md`, revisions 1 (@ac6e7939f8) and
  1a (@aac65cf7ff);
- the CTO half @f342ba6664 and its confirmation of the reduced set (msg 105217).

## Blast radius

- **irpt-holdings-performance-lambda now; irpt-inf-holdings-performance-lambda after its 14:00Z fire is read (W80-S1).** The census shows
  one changed member of 14, `handler.py` (IB-pr-320: S297 plus W123-S1). Its commits since the live build are cd41c4e24f and 3c45e1522e
  only (CTO read).
- **Behavior change:** a fire whose target day is already landed returns `TARGET_ALREADY_LANDED` and computes nothing, where before
  it recomputed and rewrote the landed day. A fire with a gap, or an empty listing, is unchanged. An explicit `date` is unchanged.
- **Shared artifact:** both functions read the same S3 key, `investor-reporting/irpt-holdings-performance-lambda.zip`. The upload
  replaces that object. The apply is TARGETED at `module.irpt_holdings_performance.aws_lambda_function.this`, so the INF function
  keeps its running code until its own leg. An untargeted apply of the holdings-performance root before then would move INF early:
  the ledger names this.
- **Never touched:** any data key, IAM, schedules, the other eight functions of the plan.

## Both branches

- **Before-read CodeSha256 = 0PuFBxdJSbFH..** proceed. **Differs:** stop that function.
- **After deploy:**
  - the change invoke `{"dry_run": true}` answers `TARGET_ALREADY_LANDED`, or computes rc 0 without upload when the target has
    not landed;
  - the happy-path invoke `{"date": <a landed day>, "dry_run": true}` answers rc 0 as before.
  - Either fails, or any 5xx: roll back in the same session.

## Rollback

Restore the prior artifact version of the S3 key, plus a targeted apply, back to CodeSha256 0PuFBxdJSbFH... The prior object version
is kept by the bucket's versioning (read before upload).

**COO half: SIGNED -- 2.0.0_SA_COO~P, 2026-10-05.**
