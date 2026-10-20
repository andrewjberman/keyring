# RESEARCH 2026-10-20 -- NFRA_FIDUPL: ATT is a PERSISTED cross-session cookie, not login-minted

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 1.0.0_SA_CTO~DELL1 msg 8770 ("which response sets ATT in HAR 5?").
**Source:** Andrew's working sign-in `wealthcentral.advisorchannel.com5.har` (off git). Names, methods, statuses, order only.

## Direct answer: no login-step response sets ATT

- **ATT is already present on the FIRST request of the capture** -- entry #5, `POST wealthcentral.advisorchannel.com/X3eR/.../EeAoW`
  (an Akamai sensor POST), at the very start, before any login step. So Andrew's browser carried ATT in **from a prior session**; it was
  not issued during this login.
- **The only responses that `Set-Cookie: ATT`** are the post-login virtual-assistant / cognitive calls, which fire AFTER the home page
  (#92):
  - `#273 POST digital.advisorchannel.com/ftgw/digital/cognitive/web/ws/adv/v2/initialization/initializationData` -> 201, Set-Cookie
    `ATC, ATT`. Preceded by the chat-assistant remote loader (`#193 .../chat-assistant/appcontent/remote-loader/...`).
  - `#282 POST digital.advisorchannel.com/ftgw/digital/cognitive/web/ws/adv/v2/transcript/` -> 200, Set-Cookie `ATC, ATT`.
- **The login steps set `ATC, ET, FC, LC, MC, RC, SC`** (the session tokens), never ATT: the password POST (#47), session/login (#49,
  #88), otp/state (#55), identity/attributes (#58), otp/sms (#67, #86).

## What this means

1. **ATT cannot be "earned" by replaying login pre-flow calls.** It is a longer-lived **device-trust cookie, persisted in the browser
   profile across sessions**. It is refreshed by the `digital.advisorchannel.com` cognitive calls AFTER a completed, authenticated
   session reaches home.
2. **A fresh browser profile has no ATT, so the password POST 403s.** That is the box: a clean profile, no prior session, no ATT. Real
   Chrome headful does not change that -- the discriminator is the **absence of the persisted ATT**, not headless vs headful.
3. **The box's replayed pre-flow answering 400 (CTO 8770) is consistent:** those calls do not mint ATT anyway.

## REC

1. **Seed ATT once by a completed authenticated session IN THE BOX'S PERSISTENT PROFILE, then reuse it.** This is exactly the hand
   sign-in the CTO is arranging. After a hand sign-in reaches home on the box's profile, the `digital.advisorchannel.com` cognitive
   calls set ATT; the persistent profile keeps it; the next automated run sends it on the password POST and should pass.
2. **Do NOT block `digital.advisorchannel.com`** (the virtual-assistant/cognitive calls). Those are what `Set-Cookie: ATT`. If the box's
   automation suppresses third-party or chatbot calls, ATT is never set even after a successful login. Allow them alongside
   `cfa.fidelity.com`.
3. **The one open bootstrap question:** how does a profile get its FIRST ATT? HAR 5 does not show it -- Andrew's profile already had one.
   Two possibilities to settle at the hand-seed:
   - the first interactive login reaches home (human-paced, trusted), the cognitive calls set ATT, and it persists -- then we are done; or
   - a fresh profile's password POST itself 403s even by hand, in which case the first ATT comes from a device-enrollment path (the
     "Certified Browser" link on the login page), which we would need to capture.
   **So the hand-seed is also the test:** if Andrew's hand sign-in on the box's fresh profile reaches home, ATT persists and automation
   works; if it 403s, we capture the Certified-Browser enrollment.

## Not measured

- The first-ever ATT issuance (no fresh-profile capture exists).
- Whether ATT is HttpOnly / its TTL (value never read).
