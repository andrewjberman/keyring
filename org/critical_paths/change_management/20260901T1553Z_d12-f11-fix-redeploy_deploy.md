# DEPLOY LEDGER -- auth-handler: F-11 fix + fail-open hardening (fix-forward)

| | |
|---|---|
| **Opened** | 2026-09-01T15:53Z |
| **State** | CLOSED -- COMPLETE 2026-09-01T15:57Z |
| **Seat** | `0.7.0_AE_CloudOps~Z` (site Z) |
| **Authority** | `1.0.0_SA_CTO~Z` 19201 -- *"14a88f66c9 stands as CVO~Z-cleared. Proceed... Condition (built + CVO-cleared) IS the authorization -- no separate go."* · `3.0.0_SA_CVO~Z` delta re-read CLEARED at `14a88f66c9` · `2.0.0_SA_COO~Z` 19173 (fix-forward, no rollback) |
| **Pipeline** | `infra/aws/terraform/portal-auth` |
| **Source** | `688e37909a` (F-11 fix) · `14a88f66c9` (hardening) · `cb17fc46af` (revert to the cleared form) |

## What this closes

**F-11**, live on the currently-deployed `gmJnyiaSC...`: `resendPhoneEnrolmentCode` refused a
cross-account caller only AFTER `sendChallengeCode` had charged the VICTIM's send budget.
Measured as E1w-c (`sends` 0 -> 1) by the wrong-session limb `3.0.0_SA_CVO~Z` insisted on.

Plus the hardening: the owner parameter is REQUIRED (discriminated union, no default), so a
future caller cannot silently omit the ownership check. Negative control run and recorded --
a caller omitting it gives `error TS2554`, `tsc rc=2`.

## ⛔ The tree deployed here is BYTE-IDENTICAL to the cleared commit

I had already applied a sentinel rename (`3b47766bd4`) when `1.0.0_SA_CTO~Z`'s ruling for it
crossed `3.0.0_SA_CVO~Z`'s withdrawal of the request. **Reverted at `cb17fc46af` rather than
kept**: the authorization is *built AND CVO-cleared*, the clearance is of `14a88f66c9`, and
shipping a renamed identifier nobody had read would be deploying uncleared code. `git diff
14a88f66c9 -- src/` is EMPTY -- verified, not assumed.

⭐ "It is only an identifier rename" is exactly the *it-is-only-a-small-change* reasoning this
leg exists to refuse.

## Verification order -- UNCHANGED, and email still goes first

1. positive sha match (deployed == built) **and** a deployed-BYTE census
2. ⛔ **EMAIL-NO-REGRESSION FIRST.** The login dispatch is shared; `sendChallengeCode`'s
   signature changed and the LOGIN resend is one of its two callers. **A signature change on a
   shared function is precisely when "the email path is untouched" stops being free.**
   Regression -> IMMEDIATE ROLLBACK.
3. then **E1w re-run in the AMENDED form.** ⛔ **The discriminator is the VICTIM'S `sends`
   UNCHANGED before/after, plus `attempts` unchanged and B's challenge still completable by B
   -- NOT the refusal. The broken build refuses too.**

## Rollback

Re-point `s3_object_version` at `gmJnyiaSCBIAnM3AOP3hzkY8AoGHH3/o18vxCAeg+e8=` and apply. Pure
code. That build carries F-11, which is inert and unreachable, so rollback is safe.

## Progress

- [x] build + upload -- `RIAv5cTFNKIH2X04tAuB7zen7gzDIrXgjdlN8ftN+7w=`
- [x] `terraform plan` -- `0 to add, 1 to change, 0 to destroy`, code attributes only
- [x] `safe-apply` -- `comp-tagauthz gate PASSED`, applied 15:54:25Z
- [x] 0-diff re-plan -- "No changes."
- [x] **deployed == built, POSITIVE match.** `LastUpdateStatus: Successful`
- [x] **EMAIL-NO-REGRESSION -- 12/12. NO ROLLBACK.**
- [x] **E1w re-run -- 9/9. E1w-c flipped 1 -> 0.**
- [x] pinged `2.0.0_SA_COO~Z`
- [x] fixtures deleted, census both ways, MFA table swept to 0
- [x] **CLOSED 15:57Z -- COMPLETE.**

## Close-out

### F-11 is CLOSED on the served plane

```
E1w-c   A's Bearer + B's challengeId -> enroll/resend
        BEFORE (gmJnyiaSC...)  B's sends 0 -> 1    FAIL
        AFTER  (RIAv5cTF...)   B's sends 0 -> 0    PASS
```

⭐ **THE COUNTER IS THE DISCRIMINATOR AND THE REFUSAL IS NOT.** Both builds refuse the
cross-account resend; only the victim's `sends` separates them. Scoring this on the refusal
would have passed the broken build.

Full run 9/9: the verify refusal still holds with `attempts` at 0, nothing was written to A's
record, and the positive control (B's own Bearer, same challenge, same code -> 200, then B's
record carrying the verified number) proves every refusal was about IDENTITY rather than a
dead challenge.

### EMAIL-NO-REGRESSION, run FIRST -- and it mattered more this time

12/12. **This deploy changed `sendChallengeCode`'s SIGNATURE, and the LOGIN resend is one of
its two callers** -- so "the email path is untouched" was NOT free here the way it is for a
pure addition. A shared-function signature change is exactly when that assumption stops
holding, which is why the check ran before anything SMS-side.

### ⚠ AN INSTRUMENT DEFECT IN MY OWN TEST, RECORDED

The E1w script prints `deployed gmJnyiaSCBIAnM3AOP3hzkY8AoGHH3/o18vxCAeg+e8=` in its banner.
**That is a HARDCODED LITERAL and it was STALE** -- the live sha at run time was
`RIAv5cTF...`, confirmed by a separate `get-function-configuration` read.

⛔ **A test that prints a stale build id in its own header invites a reader to conclude it ran
against the wrong build.** The result is still sound, and for a reason worth stating: the old
build produced `sends 0 -> 1` and this run produced `0 -> 0`, **so the flip itself proves which
bytes answered.** But the banner should read the sha rather than carry it -- the same
measured-not-asserted rule the test exists to enforce, applied to the test.

### Cleanup

`FIXTURE 1->0 = 2 of 48`, full scan both sides, condition-guarded delete, pilot pair untouched.
`opal-portal-auth-mfa` swept to 0 rows.

## Not established

⚠ No SMS sent or sendable (0 origination identities; SP-1 Andrew-gated).
⚠ Act C's transitional legacy-mint branch still unexercised.
⚠ SF-1 unflipped -- no client reaches the sms branch.
