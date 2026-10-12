# NFRA_OPSWKF PRD v0.10 -- ratified-text review (ENDPOINT: FWD-10, the trade functions have one door)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11. **PRD:** `org/missions/D9/NFRA/NFRA_OPSWKF/prd/NFRA_OPSWKF_PRD.md` @47d579b505.
**Asked by:** `1.0.0_SA_CTO~DELL2` (the v0.10 review delivery and its message). **Prior:** v0.9 SIGNED.
**Verdict: SIGNED, so the closing act is not held. One point the release's pair must settle before it relies on the proof.**

## The outcome is right, and it should not wait

A second public API fronts the trade functions, with a sign-in route that takes an email and a password from anyone and checks them
against the portal's own users table, with no rate limit, lockout or origin check (the applier's read of the deployed bytes; not
read by this seat). Closing it is a narrowing act, reversible, by one setting. Three things in the text are exactly right:

- **No seat tests the sign-in route, ever.** A request to it is a credential presented to a live password check.
- **Deleting the API, its functions and their key is a different act, unrecoverable, and Andrew's.** It is listed for him and kept out.
- **The traffic reading is given with its controls** (0 and 0 over 30 days beside 54,824 and 7), and the text does not turn "no
  traffic seen" into "never used": it says the window, and that access logging is off.

This seat's grade of FWD-8 and FWD-9 said "Opal staff only" was proven on the functions' own check and not on every path. This
outcome is that gap, taken up the same day.

## The point: the proof's two answers must be shown to DIFFER, and the setting read back

The DONE WHEN proves the closure by one request to a route the API does not have: "answered by the API itself BEFORE the act and
refused at the endpoint AFTER it".

That is a proof by change, and it works only if the two answers can be told apart. A request to a route that does not exist is
answered "not found" by an API that is open. Depending on which setting the pair picks, a closed endpoint may also answer "not
found", with the same status and the same body. This seat has not tested the platform and does not assert that it does; it is the
case to rule out before the act, not after. If the two answers are the same, the probe passes whether the setting landed or not,
which is the defect this seat refused v0.4 and v0.7 for.

The other two limbs do not cover it. The domain mappings are a read of something else. The invocation counts read 0 before the act
and will read 0 after it whether or not the door closed: flat proves nothing was called, not that nothing can be.

So the pair should carry two things:

1. **The setting read back from the API's own configuration after the act**, beside its value before. That is the direct
   evidence, it costs one read, and it is not in the DONE WHEN as written.
2. **Both probe answers written out, status and body, and shown different.** If the platform answers both alike, a better probe
   touches no function either: a route the API does have that needs a credential, asked with none. An open API refuses that at
   its own authorizer check without running the authorizer; a closed endpoint refuses earlier and differently. Never the sign-in
   route.

## Why this is signed and not refused

The text asks for the distinction in words ("by the API itself", "at the endpoint"), so an applier who gets two identical answers
cannot honestly claim it; the gap is that the text does not say what then. And a refusal here would withhold the PRD and hold a
closure that should happen today. The point goes to the pair, where both halves are read before the act.
