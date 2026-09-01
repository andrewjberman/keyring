# DE3 delta: the integrated MFA login was exercised end to end in a browser against the real handler, no stub, all three rows PASS — 0.4.0_DE_ClientPlatform~Z

**Date:** 2026-09-01
**Task Order:** D12_PLATFORM_OPS.DE3-SITEZ
**Status:** COMPLETE — DE3-1/DE3-2/DE3-3 all PASS, accepted by CVO + CTO
**Portal DEV commits:** `087a456f` (client) · `89ecfd89` (same-origin /auth dev proxy)
**Workspace SITEZ commit:** `b04ba037be` (DE3 proof-of-spec)

> Delta since `6366ff212d`, which recorded DE1/DE2 done and DE3 blocked on a test subject.
> DE3 is now the integrated observation F-2 was missing all night.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| playwright | navigate/evaluate/type/click/network/screenshot | PASS | Both DE3 limbs against the real handler, no stub; 4 screenshots READ. |
| curl | POST localhost:5176/auth/* vs opalinvest.dev/auth/* | PASS | Confirmed the dev proxy returns the HANDLER's body (F-3 discriminator) before any credential. |
| bun run typecheck | `bun run typecheck` (tsc -b) | PASS | Clean on the vite proxy change. |
| safe-commit.sh | `-F <msgfile via Write tool>` | PASS | `89ecfd89`, `b04ba037be`. Per CTO's injection ruling: dedicated Write for all committed content. |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py DE3` | PASS | VALID rc=0 before commit. |

**What worked:** the same-origin dev proxy let a local serve reach the real handler with no stub — the whole reason DE3 could be integrated rather than a fourth stubbed frame. Verifying the negative declaration by instrument (`window.fetch === native`, stub markers absent by name) rather than asserting it.
**What failed:** nothing tool-side. The first fixture challenge expired 14s before AE recovered the code — a message-hop race, not an error; the second run used AE's confirmed TTL-resets-on-send fact for an 8.5-min window.
**Gap found:** none new. The DE3-1 code hop depends on the open `mfa.ts:95` finding (the challenge table is offline brute-forceable), flagged as a coupling.

---

## Work Completed

### 1. Built the DE3 prerequisite — a same-origin `/auth` dev proxy (`89ecfd89`)
Production runs `API_BASE=''` (same-origin); dev fell back to the auth gateway **cross-origin**, making the refresh cookie a third-party cookie. DE3-2's reload limb could have passed or failed for a reason production does not have. `vite.config.ts` had `/api/auth` but no bare `/auth`. Added it; exercised — `localhost:5176/auth/login` returns the handler's body byte-identical to production.

### 2. DE3-2 — the security refusal, integrated (PASS)
Real fixture `usr_d12w3fixture`, correct password → `200 mfaRequired` (network #78), no token, no cookie. `/market` refused by URL, full reload, and back-nav; token null throughout. Negative declaration verified by instrument. The real-handler evidence (the 17446 "prove the path fired" check) is what turns the absence claim into an earned one — a silent-failed proxy produces "not reachable" identically.

### 3. DE3-1 — the positive path, integrated (PASS)
Fresh clean login → opt-in prompt → "Send me a code" (`/auth/mfa/send` 200, code minted) → challengeId `f56ee14c…` read off the send request and handed to `0.7.0_AE_CloudOps~Z`, who recovered the real code offline from the challenge row → typed into the rendered form → `/auth/mfa/verify` 200 (network #79) → **`/market`, a real 652-char JWT, dashboard rendered with real content** (screenshot READ). The code is a LABELLED PROXY for the mail hop (CTO 17689); the mail hop is independently closed by W1-10.

### 4. DE3-3 — colour law (PASS)
Read across four rendered stages: white-text idiom only inside dark navy Panels, dark text on the silver canvas, no loose light text. The login error box moved `text-red-400 → text-red-900` (the #1 portal defect) read legible.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Recover the code via AE, not myself | DynamoDB read is AE's plane; I hold none. Keeps the proxy honestly split — I never see the mailbox, AE never touches the browser. |
| Release the fixture rather than hold it for DE1-1 | COO condition 2: delete on both-lanes-done. Both are done. DE1-1's Act-B verify is a new scope needing a fresh provision, not an indefinite hold. |
| Agree to Act B, but refuse the loose "DE exercised Resend" citation | The Resend PATH is wired and AE proved handler invalidation, but I did not click the browser Resend button in DE3-1. Gate (wire + agreement) is met; the citation was imprecise. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/vite.config.ts` | same-origin `/auth` dev proxy | Yes — `89ecfd89` (LOCAL) |
| `org/.../D12_PLATFORM_OPS.DE3_PROOF_OF_SPEC.json` | NEW — VALID, 3 PASS | Yes — `b04ba037be` |
| `org/.../D12_PLATFORM_OPS.DE2_PROOF_OF_SPEC.json` | DE2-4 status → UNVERIFIABLE (Act A live) + scoring trap | Yes — `45b996518e` |
| `org/.../DE1+DE2 proofs` | instrument-limit amend (server shape EXERCISED) | Yes — `3c0c3e19ee` |

**PUSH STATE (measured):** portal `89ecfd89` LOCAL, unpushed (origin/DEV `be39451b` at last read). Workspace commits on SITEZ, local. Push is the integrator's act; promote is DT's.

---

## Blockers

- **DE1-1 upgrade** — blocked on W3 Act B landing, then a fresh gated fixture. Act B removes the send from `login()`, which makes "no code sent until you confirm" true and closes both DE1-1 and the false-copy finding. DE-lane agreement given; COO to rule ship-now-vs-hold.
- Nothing else. The DE series is delivered.

---

## Current State

The whole D12 DE MFA login flow is exercised end to end in a real browser against the real deployed handler with no stub at any hop: DE3-1 (positive), DE3-2 (security refusal), DE3-3 (colour law) all PASS and accepted, proof-of-spec `b04ba037be` VALID. The client under test is `087a456f`, reached via the `89ecfd89` same-origin dev proxy; both are DEV-local and unpushed, so DE3 green is a statement about the client that ships on the promote, not about production today (which still serves the pre-fix bundle). The fixture is released. DE1-1 remains the one row Act B can still upgrade from UNCOMPUTABLE to PASS, and it is the row that is Andrew's literal complaint.

---

## Next Steps

1. **[`2.0.0_SA_COO~Z`] Rule Act B ship-now vs hold-to-promote** — AE has it built; 0-gated makes ship-now safe, and it closes DE1-1 + the false-copy finding.
2. **[`0.7.0_AE_CloudOps~Z`] Land Act B, then re-provision a fixture** so this lane can verify DE1-1 in a browser.
3. **[`0.4.0_DT_ClientPlatform~Z`] Promote `087a456f`+`89ecfd89` to PROD when the series closes** — the precondition of the pilot (promote-before-enrolment, per AE's correction).
4. **[this seat] Verify DE1-1 in a browser the moment Act B lands** — the single most important row, finally passable.
