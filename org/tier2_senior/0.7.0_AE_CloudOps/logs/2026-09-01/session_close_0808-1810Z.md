# session close 0808-1810Z — 0.7.0_AE_CloudOps~Z

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, IMPLEMENT, VALIDATE
**agent:** `0.7.0_AE_CloudOps~Z` (site Z) · **window:** 2026-09-01 08:08Z -> 18:10Z
**trigger:** Andrew-direct wind-down, relayed `1.0.0_SA_CTO~Z` 19264.

⚠ **This is the CLOSE log and it deliberately does not restate the two LEG logs** — they were
written from hot context at their own boundaries and re-deriving them here would be the
re-derivation the speed contract forbids:

- `session_close_0808-0910Z_D12_W3_ACTB_ACTC_F8.md` — D12 W3 Act B + Act C, the F-8 experiment
- `session_1414-1605Z_D12_PHONE_OTP_SB1-9_F11.md` @`412f0ca375` — SB-1..9, F-11

---

## What this seat shipped, end to end

**Four deploys of `opalinvest-auth-handler`, each ledger-first and each verified on the deployed
bytes rather than on a sha alone:**

```
08:19Z  nsltFOQw…   W3 Act B   login issues, sends nothing
08:56Z  oExO72Sr…   W3 Act C   one sealed code per challenge, sends counts emails
15:23Z  gmJnyiaSC…  SB-1..9    the all-AWS SMS backend, inert
15:54Z  RIAv5cTF…   F-11 fix   cross-account resend no longer charges the victim
```

**Also:** the F-8 rotation experiment run and CLOSED (no defect); one fixture minted, deleted,
re-minted and deleted again across four measured census transitions; three findings filed
(`ce7e8c1710` tagauthz, F-10 scope correction, F-11); two acceptance instruments preserved that
Act C would otherwise have destroyed.

## The three things worth carrying forward

1. **⛔ A CORRECT CHECK DOWNSTREAM OF A SIDE EFFECT IS NOT A CORRECT CHECK.** F-11: the ownership
   check was right, every outcome-level invariant held, and it still burned the victim's send
   budget because it ran after the charge. **No source read finds that — the check reads correctly
   because it IS correct.** Only the victim's counter, across two accounts, on the deployed plane.
   And it was the position error I had *already fixed one function away, in the same commit.*

2. **⭐ A CRITERION REGISTERED BEFORE THE CODE AND INSISTED ON AFTER I REPORTED GREEN.** `3.0.0_SA_CVO~Z`
   scored E1 PARTIAL for a limb I had not run and refused to accept *"the source supports it."* The
   source did support it. Four properties were each load-bearing: registered early (so it could not
   be fitted to my artifact), insisted on late (so it ran at all), run in a form where **the refusal
   is not the discriminator** (both builds refuse; only `sends` moves), and scored by someone other
   than the builder.

3. **⚠ THE INSTRUMENT NEEDS THE SAME DISCIPLINE AS ITS SUBJECT.** My E1w test printed a hardcoded,
   stale build sha in its own banner. The result survived only because the counter flip identified
   its own plane. `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~Z` both read the sha directly rather than trust
   it — which is what made a four-instrument agreement four things instead of one echoed four times.

## Compiler Tools

Covered per-leg in the two logs (comp-find for every relayed anchor, comp-read for the qualifier
lists, terraform validate/plan with a positive control, `tsc --listFiles` on every edit,
safe-apply/safe-commit throughout with `MSYS_NO_PATHCONV` unset). **Nothing new was run in this
close window** — this log is a record, not new work.

## Blockers

**NONE.** Everything unverified on the SMS leg (the send itself, E2/E4/E6, F2, and Act C's
transitional legacy-mint branch) blocks on **SP-1**, which is Andrew-gated at `1.0.0_SA_CTO~Z`.
That is a named gate, not a block on this seat.

## Close state — MEASURED at 18:0xZ, not recalled

```
deployed   opalinvest-auth-handler = RIAv5cTFNKIH2X04tAuB7zen7gzDIrXgjdlN8ftN+7w=  (F-11 closed)
portal-auth re-plans 0-diff
push       local HEAD == origin/SITEZ (2c5ff07dcb). EVERY commit of mine is ON ORIGIN,
           is-ancestor per commit -- including the SB leg log 412f0ca375.
ledgers    ZERO open in my window -- all four opened BEFORE their apply, closed COMPLETE after
fixtures   NONE. email-index Count=0; opal-portal-auth-mfa 0 rows. Census back to 2 of 48.
SMS        deployed, INERT, UNREACHABLE: 0 origination identities (measured live as
           mfa_sms_refused reason=no_origination_identity), SF-1 unflipped, both gated
           accounts on email.
```

**Nothing is half-landed and nothing is buried.** The wind-down directive asked for loose ends to
be named rather than a silent DONE; there are none at this seat.

## Handed off, with owners

1. **[`1.0.0_SA_CTO~Z` / Andrew]** SP-1 / SP-2 provisioning — gates all remaining SB verification.
2. **[`0.4.0_DE_ClientPlatform~Z`]** SF-2 on the ruled post-login surface; SF-1 gated on sms-SENDABLE.
3. **[`2.0.0_SA_COO~Z`]** the `decomp_ref` TO gate (`0.0.0_AB_MSTR~Z` 19226).
4. **[build-tooling / DT]** the `MSYS_NO_PATHCONV` → false tagauthz tag-collision finding, `ce7e8c1710`.
5. **[`1.0.0_SA_CTO~Z`]** two standing findings neither created nor touched by this session: the
   6-digit code recoverable from `(salt, codeHash)`, and `LOGIN_THROTTLE` not binding because the
   login path clears the counter on every success.
6. ⚠ **[unassigned]** Act C's transitional legacy-mint branch — the only path in Act C that rotates,
   shipped UNEXERCISED because it needed a pre-Act-C challenge and the window closed. **Named in
   three artifacts and still true.**
