# The MFA login UI shipped, and building it surfaced a client-side gate bypass whose RED was captured before the fix could hide it — 0.4.0_DE_ClientPlatform~Z

**Date:** 2026-09-01
**Task Order:** D12_PLATFORM_OPS.DE1-SITEZ + .DE2-SITEZ (DE3-SITEZ blocked, see Blockers)
**Status:** COMPLETE for DE1+DE2 to the extent they can be; BLOCKED on DE3
**Portal DEV commits:** `be39451b` → `087a456f`
**Workspace SITEZ commit:** `527058ca05`

---

## Objective

Build the MFA login flow Andrew said was missing — an opt-in prompt before any code is sent,
and a page to type the code into. Every acceptance row is BROWSER-observed by the TOs' own
construction, because this workstream already scored an honest 10/10 on a feature no human
could use.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find -i 'mfaRequired\|mfa/verify\|mfaToken\|mfaChannel' portal/src` | PASS | 0 hits / 431 files. The frontend genuinely did not exist. |
| comp-find | `comp-find -i 'LoginPage' portal/src` | PASS | POSITIVE CONTROL for the zero above — 7 hits, so the zero was absence, not an out-of-corpus read. |
| comp-find | `comp-find --name '*rotected*' portal/src` | WARN | Run from INSIDE `portal/` it returned `0 hits across 0 files` — OUT-OF-CORPUS, not absence. comp-find is bounded to the workspace worktree. Re-ran from the root and it resolved. |
| comp-find | `comp-find -i 'mfaRequired' .` | PASS | Located `infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts:95` — the origin of the blocking finding. |
| to-check | `python .tools/to-check.py --all --project PLATFORM_OPS_USERMGMT` | PASS | 5 TOs, 3 ACTIVE to this lane. `--project` filtered correctly; I read the ROWS, never the count. |
| bun run typecheck | `bun run typecheck` (`tsc -b --noEmit`), mutant planted FIRST | PASS | Mutant produced 4 errors, so the clean pass is meaningful rather than the empty-file-set artifact portal/CLAUDE.md warns about. |
| bun run lint | `bun run lint` | PASS | 0 errors, 11 pre-existing warnings, none in the five touched files. |
| playwright | navigate / fetch-stub / submit / screenshot / evaluate, 5 scripted runs | PASS | The instrument the whole TO series turns on. RED and GREEN captured on the identical stub; 4 screenshots READ. |
| curl | `curl https://opalinvest.dev/assets/index-D9vMtGZu.js` | PASS | Read the SERVED PROD bundle to establish its vintage — not a local tree, not a deploy record. |
| safe-commit.sh | `--author '0.4.0_DE_ClientPlatform~Z <...>' -F <msgfile>` | PASS | Two commits, both msg-verify MATCH. |
| commit-gate | (invoked by safe-commit) | SKIPPED | Printed `checked 0 of 5 files — NOTHING WAS CHECKED`. It reads only .py/.sh/.tf/json. NOT cited as validation for a frontend artifact. |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <both>` | PASS | VALID rc=0 — after rejecting my first draft on 11 real violations. |

**What worked:** `comp-find` with a positive control settled "does the frontend exist" in two calls.
Playwright with a fetch-boundary stub made the whole TO scorable without an account. The typecheck
mutant and the leak-detector positive control both did real work.
**What failed:** Nothing tool-side. The failures were mine — see Postmortem.
**Gap found:** `proof-of-spec-check.py` has no `BLOCKED-BY-BACKEND` status. I mapped those rows to
`UNCOMPUTABLE-BY-CONSTRUCTION`, which is defensible but is not the same claim: it reads as "cannot be
computed" when the truth is "cannot be computed *until another lane ships an endpoint*". The
`status_reason` carries the distinction; the enum does not. Surfaced, not chased.

---

## Work Completed

### 1. Measured the surface before building

`mfaRequired`/`mfa/verify`/`mfaToken`/`mfaChannel` in `portal/src`: **0 hits across 431 files**,
positive control 7 hits. Independently confirmed the TO's claim rather than inheriting it.

### 2. Found the blocking backend dependency

`auth.ts:93-95` calls `issueChallenge()` then `sendMfaCodeEmail()` **inside `login()`**, before the
response returns. All 16 routes of `index.ts` read; `mfa.ts` exports exactly two operations;
`issueChallenge` has exactly ONE call site. **There is no endpoint that sends a challenge
independently of `/auth/login`** — so DE1-1's "no code sent until the user confirms" and DE2-4's
resend are unsatisfiable frontend-only. Routed as msg 17360 with `0.7.0_AE_CloudOps~Z` proposed as
owner. I did not touch that tree.

### 3. Found a client-side gate bypass — the more serious finding, and in my own lane

The MFA challenge is HTTP **200**. `AuthContext.login()` checked only `response.ok`, so it fell
through to the session block and set `isAuthenticated: true` with `accessToken` undefined;
`ProtectedRoute` gates on `isAuthenticated` alone.

### 4. Captured the RED before fixing it

`3.0.0_SA_CVO~Z` (17378) observed that landing the fix first would make the bypass permanently
unobservable — a later DE3-2 PASS could not then show it discriminates. Predictions pre-registered in
17390 **before** the act. Same stub, before and after:

| | RED `be39451b` | GREEN `087a456f` |
|---|---|---|
| `localStorage.accessToken` | `"undefined"` (string) | `null` |
| calls after login | login + `/auth/me` + 5 prefetches | login **only** |
| `/market` by in-session URL | **ADMITTED**, blank silver canvas | bounces to `/login` |
| `/market` after full reload | bounces to `/login` | bounces to `/login` |

All 5 data calls 401'd in the RED — **no data disclosed**. The harm is a broken half-authenticated
state, not a breach.

### 5. Built DE1 + DE2

`MfaOptInPrompt.tsx` (channel selection; `sms` visibly UNAVAILABLE because it fails closed 503),
`MfaChallengeForm.tsx` (6-digit entry, resend, honest errors, never auto-retries because a consumed
challenge is DELETED not flagged), `LoginPage.tsx` (credentials → optin → challenge on one route,
challenge in component state only), and `AuthContext` with `establishSession()` shared by `login()`
and `verifyMfa()` so the two session paths cannot drift.

### 6. Ran the unassigned PROD-vintage step

`1.0.0_SA_CTO~Z` (17469) named a step 1 that had to precede any console read and left it unowned. It
was unblocked, in my project and on my surface. The served bundle `index-D9vMtGZu.js` carries **zero**
MFA tokens (positive control: `"Welcome back"` 1, `auth/login` 1, `isAuthenticated` 12) and I read the
minified `login` callback out of the bytes — ok-only check, no `mfaRequired` branch, `/auth/me` with
`Bearer undefined`. **PROD serves the pre-fix client with the bypass mechanism present.** Accepted by
CTO in 17510, which ruled the consequence: gating an account against today's PROD bundle would ARM the
bypass for that account.

---

## Postmortem — three errors of mine, all caught in-session

**Root cause pattern: I stated conclusions at a confidence my evidence did not carry, and each time
the correction was cheaper than the propagation would have been.**

| Error | Shape | Resolution |
|---|---|---|
| Told four seats "a correct password alone NAVIGATES to /market" | The navigate half was WRONG — a `TypeError` in `OpalAnalytics.init` threw first. The state was poisoned anyway and `/market` was reachable BY URL. | Rung 5 withdrawn, rungs 1-4 stand. Corrected in 17420 before anyone built on it. |
| Concluded a `send_message` refusal was caused by SUBJECT LENGTH | It was not. My `body` parameter was failing to transmit; the refusal message was accurate and I misread it. I said the wrong cause on the wire. | Corrected in 17360's opening paragraph rather than left standing. |
| Wrote both proof-of-spec files against a SIBLING deliverable instead of the schema | 11 real violations. "Modelled on an existing example" is not "validated against the contract". | Read `org/standards/PROOF_OF_SPEC.schema.json` and rewrote. Both VALID rc=0. |

A fourth, smaller: my first `AuthContext.context.ts` patch wrote LF into a 100%-CRLF file, producing
36 mixed-ending lines. Caught by checking the endings rather than the diffstat, and the patch script
was rewritten to preserve the file's own ending.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Score DE1-1 as UNCOMPUTABLE rather than PASS on its rendered half | The row is a CONJUNCTION. Passing it on the prompt alone satisfies the letter while shipping the exact thing Andrew objected to. |
| Record DE2-1 UNVERIFIABLE rather than stub a token | I could have made a stub return a token and watched the browser reach `/market`. That is the substitution this TO series exists to prevent. |
| Wire `requestMfaCode()` to an endpoint that does not exist yet | So the flow becomes correct with NO further frontend change when AE lands the split. A 404 is SHOWN, never swallowed as "code sent". |
| Fix the pre-existing `text-red-400` error box | Beyond the literal ask, disclosed as such. It is the documented #1 portal defect AND the box DE2-2/DE2-3 must be READ in — my own criteria would have failed in it. |
| Run CTO's unassigned step 1 without asking | Unblocked, in-project, on my surface, needed nobody's terminal. CTO confirmed in 17510 this was the correct disposition of an unowned step. |
| Do NOT write a partial DE3 proof-of-spec | DE3 exists to be the INTEGRATED browser exercise. Scoring it off stubs would repeat the defect it was created to correct. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `portal/src/contexts/AuthContext.context.ts` | `MfaChannel`/`MfaChallenge`/`LoginOutcome`; `login()` returns a discriminated union | Yes — `087a456f` (LOCAL) |
| `portal/src/contexts/AuthContext.tsx` | `establishSession()` extracted; MFA gate; `requestMfaCode()`; `verifyMfa()` | Yes — `087a456f` (LOCAL) |
| `portal/src/pages/auth/MfaOptInPrompt.tsx` | NEW — DE1 opt-in prompt + channel selection | Yes — `087a456f` (LOCAL) |
| `portal/src/pages/auth/MfaChallengeForm.tsx` | NEW — DE2 challenge screen | Yes — `087a456f` (LOCAL) |
| `portal/src/pages/auth/LoginPage.tsx` | 3-step flow; error box `text-red-400` → `text-red-900` | Yes — `087a456f` (LOCAL) |
| `org/.../D12_PLATFORM_OPS.DE1_PROOF_OF_SPEC.json` | NEW — VALID rc=0 | Yes — `527058ca05` |
| `org/.../D12_PLATFORM_OPS.DE2_PROOF_OF_SPEC.json` | NEW — VALID rc=0 | Yes — `527058ca05` |

**PUSH STATE, measured not defaulted:** portal `087a456f` is **LOCAL** — `git ls-remote origin DEV`
reads `be39451b`, `rev-list --left-right --count HEAD...origin/DEV` = `1 0`. Workspace `527058ca05` is
**LOCAL** — `origin/SITEZ` reads `4e136d8311`; confirmed an ancestor of HEAD by `merge-base
--is-ancestor`. Push is the integrator's act; portal promotion is DT's.

---

## Blockers

- **BLOCKED on `2.0.0_SA_COO~Z`:** `D12_PLATFORM_OPS.DE3-SITEZ` — DE3-1 needs an MFA-enabled test
  account on a mailbox that is not a live human address. DE3 §4 instructs this lane to STOP AND ASK
  rather than provision one. Asked in msg 17475. I enabled nothing and created no account.
- **BLOCKED on `0.7.0_AE_CloudOps~Z`** (proposed owner, not yet assigned by COO): `POST /auth/mfa/send`
  — the issuance split. Until it exists, DE1-1 and DE2-4 cannot pass. Frontend call site is wired and
  exercised against its absence.

---

## Current State

The MFA login UI exists and works: `portal` `087a456f` on DEV (LOCAL, unpushed) adds
`MfaOptInPrompt.tsx` and `MfaChallengeForm.tsx` and rebuilds `AuthContext.login()` to return a
`LoginOutcome` union that establishes no session on the `mfaRequired` branch — closing a bypass where
`ProtectedRoute`, which gates on `isAuthenticated` alone, admitted `/market` to anyone with just a
correct password. Six of nine acceptance rows PASS browser-observed with screenshots read; DE1-1 and
DE2-4 are blocked on an auth-handler endpoint that does not exist (`POST /auth/mfa/send`), and DE2-1
is unverifiable without a gated account. The served PROD bundle `index-D9vMtGZu.js` was measured to
carry the pre-fix client with the bypass mechanism intact, which CTO ruled (17510) means gating any
account before this promote would arm the bypass for that account. Zero of 48 accounts are gated, so
nothing is exposed today.

---

## Next Steps

1. **[`2.0.0_SA_COO~Z`] Provision an MFA test subject** — an enabled account on a non-human mailbox.
   It is the only thing standing between here and DE3-1, and DE3 §4 reserves the act to that seat.
2. **[`0.7.0_AE_CloudOps~Z`] Split issuance out of `login()` into `POST /auth/mfa/send`** — unblocks
   DE1-1 and DE2-4 with no further frontend change. Needs COO to name the owner first.
3. **[`0.4.0_DT_ClientPlatform~Z`] Promote `087a456f` to PROD when the series closes** — measured
   consequence: until it lands, the PROD client cannot enforce MFA and cannot render a code page.
4. **[`0.0.0_AB_MSTR~Z`] Ask Andrew which host he was on, paired with the `localStorage.accessToken`
   console read** — CTO assigned this in 17510. Not mine and explicitly not tonight.
5. **[this seat] Nothing outstanding.** Available on measurement; DE3 resumes the moment a subject
   exists.
