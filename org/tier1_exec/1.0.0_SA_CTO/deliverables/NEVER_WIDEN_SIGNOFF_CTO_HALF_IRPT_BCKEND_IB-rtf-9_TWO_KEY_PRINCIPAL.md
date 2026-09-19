# NEVER-WIDEN SIGN-OFF -- **CTO HALF** -- `IRPT_BCKEND.TO-IB-rtf-9`: the two-key bounded test principal

**Signed by:** `1.0.0_SA_CTO`. **Date:** 2026-09-19 ~09:5xZ.
**BOUND BY CONTENT TO PACKET BLOB `a1f36b95b26c8fefd6ff0d47489f9884f87dd2c4`** -- resolved on this seat's own
instrument, matching the value `2.0.0_SA_COO~B` cited in `98215`.
**Pairs with:** the COO half @`3c0bad02ee` (blob `ee4bb9c7a6`), which correctly states that the `rte-2` half
@`a0f05dda0c` no longer covers this act -- **a re-cut packet is a re-signature, and saying so unprompted is the
behaviour this mechanism depends on.**
**Authority for the act:** Andrew-direct @`af794c77e3` (a bounded test principal, deleted at round close), read
as my `98209` s.2 rules it: **boundedness is carried by the delete, not by the absence of an advisor claim.**

---

## 1. ⛔ THE ONE CONDITION THIS HALF ADDS: **THE LONGEST-LIVED CREDENTIAL IS THE ONLY ONE WHOSE DEATH IS NOT EXERCISED**

The packet creates **two** durable credentials and treats them very differently:

| credential | TTL | how its death is established |
|---|---|---|
| access token | **15 minutes** (`jwt.ts:17 @b95c935160`) | ⭐ **EXERCISED** -- step 8: after the last `exp`, one request is refused 401, `n of n` |
| **refresh token** | **7 DAYS** (`jwt.ts:18 @b95c935160`) | ⚠ **DESCRIBED ONLY** -- *"a refresh re-reads the row (`auth.ts:483-537`), so it dies with K1"* |

⛔ **THE CARE IS INVERTED RELATIVE TO THE RISK.** The 15-minute artifact gets a live refusal; **the SEVEN-DAY
artifact gets a code read.** And the packet's own interval -- `max(K1 delete verified, K1b delete verified, last
access-token exp)` -- **names only the ACCESS token's `exp`**, so if the refresh path does not in fact die with
`K1`, the formula closes the interval while a credential with **six days and twenty-three hours left** is still
live, and nothing in the plan would notice.

⭐ **This is Rule 22's STATE axis at the one place the packet did not apply its own standard: DESIRED != APPLIED
!= EXERCISED.** The packet is rigorous everywhere else precisely *because* it exercises; here it took the code's
word. The failure modes a read cannot see are ordinary ones -- a cache, a second refresh handler, a path that
validates the signature without re-reading the row.

**BINDING, AND IT COSTS ONE REQUEST IN A STEP THAT ALREADY RUNS: step 7, immediately after `K1`'s delete is
verified, ATTEMPT A REFRESH with the issued refresh token and REQUIRE A REFUSAL, recorded `1 of 1` like every
other control in this packet. A success is a STOP and a same-turn escalation, not a branch.** The interval in
step 8 then reads `max(K1 delete verified, K1b delete verified, last access-token exp, refresh refused)`.
**NON-APPLICATION:** none -- the refresh token is minted by the same login that mints `K2`, so it always exists.

## 2. THE PACKET IS ACCEPTED AS WRITTEN, AND FIVE THINGS EARN IT

1. ⭐ **MINIMISATION BY OMISSION, WITH THE REASON STATED.** `K1b` carries **only** `{email, advisorKey}` --
   `firmRole`/`advisorRole`/`advisorName` deliberately **ABSENT**, because *"admin in either bypasses the edge
   check, the backend tier and the L1 scope."* **The packet names the escalation it is declining to create.**
2. **The `FIRM#/MEMBER#` item is NOT written**, so the principal does not appear in firm-member listings --
   **narrower than the tooling's default**, and named as such rather than left implicit.
3. **`create_user_v2.py` is NOT used**, with its three disqualifiers cited (refuses a non-`@49financial.com`
   address, writes an unread item, sends SES unless suppressed). **A tool declined for stated reasons.**
4. ⭐ **THE CENSUS CAN FAIL: the packet's lines EQUAL the re-derived counts 3 of 3 and DIFFERED 3 of 3 on the
   pre-packet run.** That is a discriminating control, not a restatement -- and it is the arm I would have asked
   for had it been absent. 263 principals simulated, **0 UNKNOWN**, 112 settled by reading their statements.
5. ⭐ **IT CORRECTS ITS OWN FACE.** Row `S88`: the order's face and row `S86` cite `lib/partner/index.ts:39-47`
   (`canAccessFirm`) as the firm-admission mechanism, and **that function has 0 callers in production.** The real
   mechanism is the L0 tier (`tier_policy.mjs:9`) plus `opal-partners-data:1673-1680` on L1/L2 only. **A graded
   party correcting the citation its own order rests on, against itself, is why this packet is signable quickly.**

**MY `98209` CONDITION (a) IS MET:** the round-close deletion is **VERIFIED by a failing consistent read, `2 of
2`, `K1b` FIRST** -- the binding dies before the login can use it.

## 3. THE FIRM-MEMBERSHIP EXPOSURE: **IN RADIUS, NOT WIDENED, AND IT IS MINE**

A 49financial login with no book sees **L0 firm aggregates** on the advisor-intelligence routes. The packet names
it **inside the radius and expressly neither widened, narrowed nor fixed** -- which is the correct handling of a
pre-existing exposure inside a bounded act. ⚠ **It is my finding and it stays mine** (`98209` s.4); whether any
such login EXISTS is an unscoped `opal-users-v2` x `opal-partner-*` census with a per-firm denominator that
**nobody has run**, and `R66-AC2`'s statement of what that census would take is the hand-off I will act on.
**This act does not enlarge it: `K1b` exists for the shortest possible window and dies first.**

## 4. WHAT THIS HALF DOES **NOT** SIGN

- **Any widening of the principal** beyond `K1`, `K1b`, `K2` as the packet's three keys describe them.
- **The `FIRM#/MEMBER#` item**, any `firmRole`/`advisorRole`/`advisorName` attribute, or `create_user_v2.py`.
- **Any second login, any second principal, any other firm**, and any re-use of this principal after round close.
- **A failed-login throttle counter** beyond the packet's own terms: if one is created it is **named in the
  ledger**, and it is not a licence to probe.
- ⚠ **The FIX for the firm-membership exposure** -- naming is not remediating, and remediation is not authorized
  by this half.
- **`IB-rtf-8`**, which has its own halves @`d81cccbfe3` / @`6b35db034a`.

---

## VERDICT

**CTO HALF: SIGNED**, bound by content to packet blob `a1f36b95b26c8fefd6ff0d47489f9884f87dd2c4`, subject to
s.1 (the refresh-token refusal exercised at step 7, a STOP on success) and the s.4 exclusions.

With the COO half @`3c0bad02ee`, **both halves are on file for `IB-rtf-9` and `IB-rtf-3` may be re-handed.**
⭐ **And the reason s.1 is the whole of my contribution: this packet exercises everything it claims except the
one credential that outlives the round by a week.**

**PUSH STATE at write time:** LOCAL; `origin/CLOUD` `9b5a99d29f` (`ls-remote` read this tick).
