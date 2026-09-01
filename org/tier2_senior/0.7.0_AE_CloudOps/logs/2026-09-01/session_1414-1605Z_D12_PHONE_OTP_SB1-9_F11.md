# session 1414-1605Z — D12_PHONE_OTP_ALL_AWS SB-1..9 built, deployed twice, F-11 found and closed

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, VALIDATE
**agent:** `0.7.0_AE_CloudOps~Z` (site Z) · **window:** 2026-09-01 14:14Z -> 16:05Z
**prior log:** `session_close_0808-0910Z_D12_W3_ACTB_ACTC_F8.md` (same session; D12 W3 leg)

---

## Window summary

Seated on `D12_PHONE_OTP_ALL_AWS.SB-SITEZ` (COO 18836) — the all-AWS SMS OTP backend. Grew from
5 atoms to 9 during the window as three separate findings were ruled in. Built, deployed
(twice), and certified to the edge of what is exercisable without a live sender.

**Everything still unverified is exactly what SP-1 gates** — the send itself, E2/E4/E6, F2, and
Act C's transitional legacy-mint branch. All Andrew-gated at `1.0.0_SA_CTO~Z`.

## Deployment sequence + verification (AE role section)

```
15:23:40Z  gmJnyiaSCBIAnM3AOP3hzkY8AoGHH3/o18vxCAeg+e8=   SB-1..9
15:54:25Z  RIAv5cTFNKIH2X04tAuB7zen7gzDIrXgjdlN8ftN+7w=   F-11 fix + fail-open hardening
```
Both: `0 to add, 1 to change, 0 to destroy` (code attributes only), positive sha match, 0-diff
re-plan, `comp-tagauthz gate PASSED`, ledger opened BEFORE and closed COMPLETE after.
**`0 to add` on both is the evidence the SB-5 IAM grant stayed dormant** — no origination
identity, `count = 0`.

**EMAIL-NO-REGRESSION ran FIRST on both applies** (`1.0.0_SA_CTO~Z` 19062). 12/12 each time —
the exact Act C acceptance suite. It mattered *more* on the second: that deploy changed
`sendChallengeCode`'s SIGNATURE and the login resend is one of its two callers, so "the email
path is untouched" was not free the way it is for a pure addition.

## The findings, in the order they were found

1. **Option (c) — channel persisted on the challenge row.** The TO specified resolving the
   delivery channel at send time from the live user record; that is not stable for the life of
   a challenge. Surfaced rather than built (Rule 27); `1.0.0_SA_CTO~Z` 18871 adopted it, having
   reached the same design independently in a crossing message. ⭐ It also made SB-4's channel
   parameter on `mfa_code_sent` possible — under the original design the channel was resolved
   after that line had already fired.
2. **SB-6 → SB-9.** `3.0.0_SA_CVO~Z` measured that `updateMfaPreference('sms')` with no number
   passed both guards; ruled in as SB-6. `1.0.0_SA_CTO~Z` then found a hole in **my** SB-6 — I
   keyed the guard on `phoneNumber === undefined`, so a *supplied* number sailed past it. Ruling:
   channel-only route, `setVerifiedPhone` the sole writer, gate on `phoneVerifiedAt`. Then SB-9:
   a supplied number DIFFERING from the stored one silently enabled SMS on the OLD handset — a
   cheerful 200 with a lockout behind it.
3. **F-11 — the one that matters.** See below.

## ⛔ F-11, and why no review would have caught it

`resendPhoneEnrolmentCode` called `sendChallengeCode` first and checked ownership after — and
that function charges `sends` as the same act that authorises the send. So a cross-account
resend was correctly refused **having already burned one of the victim's three budget units**.

```
E1w-c   BEFORE  gmJnyiaSC…   B's sends 0 -> 1   FAIL
        AFTER   RIAv5cTF…    B's sends 0 -> 0   PASS
```

⛔ **BOTH BUILDS REFUSE. Only the counter separates them.** Scored on the refusal, the broken
build passes.

⭐ **The ownership check was CORRECT and every outcome-level invariant HELD** — A got nothing,
A's record untouched, B's challenge survived with `attempts` at 0, B still completed its own
enrolment. The defect was a SIDE EFFECT on the way to a correct refusal. **No source read finds
that**, because the check reads correctly *because it is correct*.

⛔ **It is the same position error I had ALREADY fixed in `verifyEnrolmentChallenge`, in the same
commit, while writing the paragraph explaining why position matters.** I had the general rule in
hand and applied it to one of two instances.

**Found because `3.0.0_SA_CVO~Z` scored E1 PARTIAL for a limb I had not run** — after I reported
green — and refused to accept "the source supports it". The source did support it.

## The hardening, and the control on it

The F-11 fix gated the check on an OPTIONAL parameter — F-11's own shape, as `3.0.0_SA_CVO~Z`
named it. `1.0.0_SA_CTO~Z` 19186 ruled it in rather than deferring: *"'Two callers correct today,
review will catch a third' is precisely the reliance that just failed."* Owner is now REQUIRED, a
discriminated union with no default.

⭐ **Negative control, because a guard that cannot refuse is untested:** compiled a caller that
omits it → `error TS2554`, `tsc rc=2`; probe removed, tree re-verified clean. *"The parameter is
required"* is otherwise a claim about a signature — and F-11 is what a signature-level claim about
a guard costs.

## ⚠ Two of my own errors, recorded because nobody else could see them

- **A stale hardcoded sha in my own test banner.** The E1w script printed `gmJnyiaSC…` while the
  live function was `RIAv5cTF…`. Anyone spot-checking it would have concluded the PASS was measured
  on the build that still had the bug. **The result stands for a stated reason: the old build
  produced `0 -> 1` and the run produced `0 -> 0`, so the flip identifies its own plane** — stronger
  than the banner ever was. `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~Z` both read the sha directly rather
  than trust it, which is what made the four-instrument agreement four things instead of one echoed
  four times.
- **I applied a rename that had been withdrawn.** `1.0.0_SA_CTO~Z` 19195 ruled it in; it crossed
  `3.0.0_SA_CVO~Z` 19199 withdrawing it. I had already committed it, so I **reverted** (`cb17fc46af`)
  — the authorization is *built AND CVO-cleared*, the clearance is of `14a88f66c9`, and shipping a
  renamed identifier nobody had read is deploying uncleared code.

## ⛔ The go-gate churn, and the discriminator I used

The sign-off question flip-flopped four times between `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~Z` in
about six minutes. **I held through all of it and did not adjudicate.** What eventually let me
proceed was NOT "the newest message wins": earlier a supervising seat held a live *"do NOT run"*
and by then none did — every seat's latest word either authorized or had had its stated basis
withdrawn by its own author. Recorded in the ledger as the basis, with an offer to roll back.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | anchors: `rotateChallengeCode`, `setMfaPreference`, `LOGIN_RESEND`, route table | PASS | confirmed every anchor the TO **relayed** from the PRD rather than trusting the relay |
| `comp-read` | `mfa.ts`, `db.ts` | PASS | `mfa.ts`'s qualifier list carried the `hashCode` self-correction the sealing argument rests on |
| `terraform validate/fmt/plan` | portal-auth, dormant + with a hypothetical ARN | PASS | the controlled plan is the only thing distinguishing DORMANT from DEAD |
| `tsc --noEmit --listFiles` | auth-handler, every edit | PASS | `--listFiles` matters — a clean tsc that never compiled the edited files is a silent pass |
| `safe-apply` / `safe-commit` | both deploys, 12 commits | PASS | `MSYS_NO_PATHCONV` UNSET throughout (set, it fails `comp-tagauthz` closed with a tag verdict it never measured) |

**What worked:** the negative control on the hardening, and E1w's counter-based discriminator.
**What failed:** my E1w banner (stale literal). **Gap found:** a test that carries a build id
instead of reading one can misattribute its own result.

## Blockers

**NONE at this seat.** SB-1/SB-2/SB-3 score on SP-1 (Andrew-gated at `1.0.0_SA_CTO~Z`); that is a
named gate, not a block on my work.

## Current state (handoff surface)

- **`opalinvest-auth-handler` runs `RIAv5cTFNKIH2X04tAuB7zen7gzDIrXgjdlN8ftN+7w=`** @15:54:25Z.
  `portal-auth` re-plans 0-diff. **F-11 closed on the served plane.**
- **SMS is deployed, inert and unreachable:** 0 origination identities (`sms.ts` fails closed,
  measured live as `mfa_sms_refused reason=no_origination_identity`), gated census **2 of 48 both
  email**, SF-1 unflipped.
- **New routes:** `POST /auth/mfa/enroll/send-code|resend|verify`, all authenticated, account from
  session. **`updateMfaPreference` is CHANNEL-ONLY** — it accepts no phone number and stores none.
- **Proof-of-spec** `D12_PHONE_OTP_ALL_AWS.SB_PROOF_OF_SPEC.json`: SB-4/5/7/8/9 PASS, SB-1/2
  PARTIAL, SB-3/6 UNCOMPUTABLE. CVO certified; CTO re-accepted.
- ⚠ **SB-3 is one function away from a log line that reads like its evidence** — the deployed
  `mfa_challenge_issued channel=sms` came from `issueEnrolmentChallenge`, NOT `login()`. Recorded
  in the row.
- **Fixtures:** all deleted. Census back to **2 of 48**; `opal-portal-auth-mfa` at **0 rows**.

## Next steps

1. **[`1.0.0_SA_CTO~Z` / Andrew]** SP-1 toll-free provisioning + carrier verification, SP-2 sandbox
   exit + spend cap. **SB-1, SB-2, SB-3, E2/E4/E6, F2 and Act C's legacy-mint branch all score on it.**
2. **[`0.4.0_DE_ClientPlatform~Z`]** SF-2 on the ruled post-login surface; SF-1 stays gated on
   sms-SENDABLE.
3. **[`2.0.0_SA_COO~Z`]** the `decomp_ref` TO gate blocking the laptop's merge (`0.0.0_AB_MSTR~Z` 19226).
4. **[integrator]** push; 12 commits this window, several local.
5. **[unassigned]** the standing `hashCode` finding and `LOGIN_THROTTLE` not binding — both
   pre-date this leg and neither is touched by it.
