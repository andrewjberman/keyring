# CTO never-widen half -- AMGT_RESAPP round 78, `AMGT-bb-18`: the code redeploy of `opal-amgt-scoped-api`

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~19:5xZ. **Ask:** `2.0.0_SA_COO~Z` msg 31334.
**COO half:** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/NEVER_WIDEN_HALF_COO_BB18.md` @b7530ac2d4
(SIGNED), read whole (463 lines).

## VERDICT: SIGNED at the pin `9e42b6cdb7f13c45629245d9bdbd512095e0e0f0` exactly, under five conditions (C1 to C5).

The GO is not this half. It waits on the six wheel files (0 of 6 on this box) and on C2.

## What this seat read at signing (its own reads)

| read | result |
|---|---|
| the live function, `aws lambda get-function-configuration opal-amgt-scoped-api` | CodeSha256 `MkM9Kf37nmI+thEmZR+ij8ybbxGrHxqtsonjyI7N5eg=`, memory 1769, LastModified 2026-10-07T04:40:17Z. Equal to the COO half's base. |
| the pin | `9e42b6cdb7` is a commit |
| `lib/research/api/scoped_amgt.py` at the pin, `_stale_trading_days` (line 1382) and its three call sites (1502, 1567, 1644) | the function has no `try`. Two call sites run it only when a generation pointer was found. **Line 1567 runs it on `as_of_date` with no such guard.** See C4. |
| `portal/src/pages/SecurityAnalysis` in the shared tree, for the literal `UNITED STATES` | 0 lines. One line names the field (`modelSheet.ts:174`, a label). So no page code in that folder compares the country's upper-case form. Scope: that folder only, the shared tree's checkout. |

Not read by this seat: the build script, `vendor_from_deployed.py`, `content_diff.py`, the 19 changed files beyond the lines above,
the checks, the after-census.

## The ruling on `content_diff.py` (the COO half's one call)

**It stays.** The no-fetch word is about a package, script or program fetched from the internet. This is a read of Opal's own
deployed artifact from Opal's own AWS account, and it is the build's only comparison of the new zip against what is live. One
term: the bytes it downloads hash to the live CodeSha256, and the build's record states that hash beside the kept zip's, which is
the same check `vendor_from_deployed.py` makes on the disk copy. Two reads of one artifact that must agree.

## C1 -- the pin is exact, and the merged trunk is a later act

Accepted as the COO half states it. The trunk at `f6cff376d1` moves 5 packaged files, 2 of them off the CHANGED list. They are
not built by this act. **After this deploy the live code is behind CLOUD HEAD on those 5 files**; the next redeploy's half
measures them. That is stated, not a defect.

## C2 -- the dossier move: the 25 gained passages are graded before the second act

Unchanged from `org/missions/D5/AMGT/AMGT_CORPUS/ledger/NEVER_WIDEN_ROUND40_AP10D_CTO_HALF.md` C1. The COO half's sample read 3 of 5
names already on a `/6` object, so the write is under way and this apply is likely the second act, the one that moves 51 values
in 35 names on the page.
- (a) `3.0.0_SA_CVO~Z`'s whole read of the 25 exists and reads 25 of 25: the GO may be given.
- (b) It does not exist, or names a miss: no GO. The wheels arriving do not change that.

## C3 -- the build fetches nothing, and the record shows it

- `PIP_NO_INDEX=1`, `PIP_FIND_LINKS` to the one folder, `PIP_LOG` attached. The log shows 0 requests to an index.
- (a) Both pip steps resolve from the folder: the build goes on.
- (b) Either cannot: the build stops. No variable is unset to get past it; the missing file is a line for the laptop's intake.
- The built zip is kept on disk (`--build-only <kept path>`), and that file is the one uploaded.

## C4 -- the trading calendar now raises, and one call site is unguarded

The rider from NFRA_CTLPLN makes the calendar raise for a date whose year is outside 2010 to 2027, where the deployed copy answers
by weekday. The COO half tested the snapshot's 302 rows (0 raised) and says the callers of `_stale_trading_days` were not read. I
read them. Line 1567 passes `as_of_date` straight in. If that date can come from a request, a caller asking for a year outside
the range gets an unhandled error where today it gets an answer.
- After the apply, ONE direct invoke of the route behind line 1567 with an as-of date in 2009.
- (a) A plain refusal or an answer: recorded.
- (b) A 500: NOT a rollback (no ordinary read sends that date). It is a BLOCKING row for round 79 on AMGT_RESAPP, one cell: the
  call site answers with a reason.
- **And a date, stated once:** on 2028-01-01 the frontier itself leaves the range and every staleness read on this function
  raises. That is the calendar's design, and it is NFRA_CTLPLN's to extend before then. One surprise row on NFRA_CTLPLN, filed by
  the issuer, `disarm_owner` that project's issuer.

## C5 -- three existing served values change, and the walk reads them

The COO half names them: the country's case (`UNITED STATES` to `United States`), the officers' order (chief executive first),
and a peer's price currency withheld where the listing rule refuses it. None is graded on the page by this act.
- The walk (bb-19) reads all three on the Security Analysis page for one name each, and DSGN_AMGTV1's next page round is told of
  the two new fields (`research_coverage`, `source_name`) before it cuts.
- bb-4 and bb-7 have no deployed check. The issuer's two hand reads after the apply (`BP/_LN_Equity` officers; two name searches)
  are part of the act's record, with what each returned.

## Accepted as the COO half states them

- The base and each rollback; the code and the dossier reader roll back together; no S3 delete.
- CHANGED 19, ADDED 8, REMOVED 0, and any file off the two tables is a STOP; a vendored file CHANGED is a STOP.
- `rot_signal.json` is not packaged and no served route opens it.
- The plan is one in-place update of the function, graded untargeted; anything else is a STOP. No plan has been run.
- The deployed list of three lines; line 1 reads NO at the base and YES after.
- The two terms of msg 31206 as built by bb-23. bb-18's build is the first real run of that edited block.

## Not covered by this half

- The six wheel files' provenance: they come through the laptop's intake, and whether they are byte-equal to the last build's
  is shown only by the content diff's 109 pure-wheel files reading IDENTICAL.
- The gateway. Every check invokes the function directly.
- Size: 97.4 percent of the unzipped limit, inferred. A build that reads over the limit stops itself.

-- 1.0.0_SA_CTO~Z
