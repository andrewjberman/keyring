# D12 PLATFORM_OPS_USERMGMT — Rule 27 STAGE 3: COO atom-decomposition

**Author:** `2.0.0_SA_COO~Z` · **Date:** 2026-08-31 ~22:5xZ · **Stage 2 PRD:**
`docs/architecture/D12_PLATFORM_OPS_PRD.md` @`2da36986f6` (`1.0.0_SA_CTO~Z`)
**Rule 27 chain:** register → purpose-level PRD (done) → **COO atom-decomp (this)** → execute ON SPEC
**Certifier:** CVO. ⚠ `3.0.0_SA_CVO~Z` is DEAD — see §5.

---

## 0. SCOPE OF THIS ARTIFACT

Decomposition, **not** a TO cut. Owners are **ROLE-CLASS** (AE / DE / DT / CTO / ANDREW), never
device-bound serials — D12 is minted **UNPLACED** and its placement is Andrew's whole-register call
after the comb. **An `issued_to` field is a placement**, so TOs are cut only once he rules.
**No alarm, SNS subscriber, page or monitor is designed, proposed or costed anywhere below.**

⛔ **PILOT COHORT IS GATED — see FINDING F-2 at the bottom of this file. NOBODY MAY BE ENABLED YET.**
On today's DEV bytes a CORRECT PASSWORD ALONE reaches `/market`; the MFA branch is not enforced
client-side. Unreachable today only because 0 of 48 accounts are gated.

⛔ **OPEN FINDING WITH NO OWNER — see FINDING F-1 at the bottom of this file.** An intended IAM
restriction on auth mail restricts NOTHING. It is not a cell, not assigned, and not closed by W1 or W2.

⚠ **SUPERSEDED IN PART BY AMENDMENT 1 (bottom of file) — READ IT BEFORE ACTING ON THIS SECTION.**
Andrew ruled ~23:15Z @`efcfa8cc5b`: **D12 IS PLACED ON SITE Z and TOs ARE CUTTABLE.** The
no-placement constraint above was correct when written and is now discharged **for D12 and D7 only**
— `issued_to` remains a placement everywhere else, and the whole-register call stays open for
D0–D6 and D8–D11. The alarm sentence STANDS: nothing here is licensed to build a monitor.

---

## 1. OPEN DECISION #5 — RESOLVED HERE, AS THE PRD ASSIGNED

The PRD leaves #5 to *"stage 3, resolved against the live table"*: **does "admin" mean an existing
partner-table role or a new one?**

> ### ANSWER: `firmRole=admin` ALREADY EXISTS. WS-5 NEEDS NO NEW ROLE.

Measured at `4a59576fbb`, four independent surfaces:

| Evidence | Says |
|---|---|
| `users/scripts/create_user_v2.py:214` | `--role` `choices=["user","admin"]` |
| `provision_{inflection,cottonwood,49financial}.py:36/26/32` | same enum, help text *"firmRole (default user)"* |
| `docs/reference/user-provisioning-firm-scope-profiles-20260528.md:86,112,138` | `opal-partner-{49financial,inflection,cottonwood}`: `firmRole=user\|admin` |
| `docs/architecture/ADVI_ROLGAT_PERMISSION_GROUPS.md:30` | *"`firmRole === 'admin'` always wins"* |

Andrew's *"if a client is an admin in their partner table"* maps **exactly** onto the live
`firmRole=admin`. **This removes a design cell from WS-5 and replaces it with an adoption cell.**

⭐ **AND IT CONFIRMS THE PRD'S SHARPEST BOUNDARY IS ALREADY THE LIVE SHAPE.** The partner table
already holds `firmRole` (authorization) while `opal-users-v2` holds the identity record
(`ADVI_PRVSYS_PRD.md:38,41`). Andrew's self-correction — *"**Well, not store anything there.** That's
really for effectively, if they're an admin in the partner table, then they have the ability to add
users"* — describes the architecture that exists. **WS-5 must not drift user attributes into the
partner table; it is an authorization lookup, and it already is one.**

---

## 2. ⚠ PRIOR ART EXISTS FOR WS-4 AND WS-5 — AND IT IS ONE OF THE 92

**`ADVI_PRVSYS` already specifies D12's WS-4 and WS-5.** `ADVI_PRVSYS_PRD.md:30` —
*"a SCOPED admin page where a partner firm's ADMIN (`firmRole=admin`) manages ONLY their firm's
users"* — with `:54` naming the tenant-isolation security as *"the load-bearing security work"* and
`:77` carrying the control WS-5 needs:

> *"`firmRole=admin` gates the page AND the API (both — never page-only; the API independently
> re-checks the JWT, **a hidden page is not a control**)."*

⛔ **`ADVI_PRVSYS` IS IN THE MEMBERSHIP-ONLY CLOSED SET FROM TONIGHT'S COMB.** Its face at close read
*"PHASE 0 — PRD AUTHORED 2026-06-29 … SEQUENCE: COO decomposes; P1 LEADS → P2 internal UI → P3
partner-admin self-service (the tenant-isolation security is the load-bearing CVO-ratified gate)."*
**Its P2 and P3 are D12's WS-4 and WS-5.**

**This is the third instance of the exact pattern `0.0.0_AB_MSTR~Z` named** — after `PORTAL_AUTHHARD`
(D12 needs its MFA/account-lifecycle work) and `OPAL_TICKET` (D7 needs it). It was found by doing
D12's stage 3, not by looking for it. **Routed as a finding to the comb's open call, not acted on:
reopening is Andrew's.** Nothing in D12 is blocked by the closure — the PRD is readable at its path
regardless of project status — but a decomp that ignored it would re-derive a design that already
exists, which is the build-ladder's first failure mode.

---

## 3. THE CELLS

`READY` · `DEP-BLOCKED` · `ANDREW-BLOCKED` · `GATE` (an arch decision, not a build).

### WS-1 — Identity record extension · everything depends on it

| Cell | Deliverable | Owner | Depends | Status |
|---|---|---|---|---|
| **1.1** | `opal-users-v2` carries phone number, MFA channel preference (`email\|sms\|none`), and whatever WS-3's design requires. | AE | **2.0 (gate)** | DEP-BLOCKED |
| **1.2** | Migration leaving existing users in a **defined** state, never null. | AE + DT | 1.1 | DEP-BLOCKED |

**Acceptance:** a pre-migration user logs in and reads a *defined* MFA preference; a new user
round-trips a phone number write→read. ⛔ **A schema dump is NOT acceptance.**

### WS-2 — MFA at login

| Cell | Deliverable | Owner | Depends | Status |
|---|---|---|---|---|
| **2.0** | ⛔ **ARCH-GATE, AND IT IS THE FIRST ACT OF THE WHOLE DIRECTIVE:** build in `auth-handler` vs adopt Cognito. | **CTO** | — | **GATE / READY** |
| **2.1** | OTP challenge between credential check and dashboard, user-selectable channel. **Email leg.** | AE | 2.0, 1.1 | DEP-BLOCKED |
| **2.2** | **SMS leg.** SES is wired; **SMS is not** — this introduces a new vendor delivery surface. | AE | 2.0, **#4 at Andrew** | ⛔ **ANDREW-BLOCKED** |

⛔ **WS-2 IS NOT COMPLETE — SEE AMENDMENT 3. A LOGIN-CHALLENGE UI DOES NOT EXIST, AND CELL 2.7 IS
MISSING FROM THIS TABLE.** W1 scored 10/10 against criteria that were narrower than this acceptance.

**Acceptance:** an MFA-enabled account **cannot reach the dashboard** without a live code, exercised
end to end; a wrong code fails; **a replayed code fails**; the OTP secret is never returned by any
endpoint.

⛔ **MFA IS ENTIRELY GREENFIELD — MEASURED, AND THE MEASUREMENT HAS A TRAP THE DECOMP MUST NOT REPEAT.**
`1.0.0_SA_CTO~Z` measured at `4a59576fbb`: a **loose** census returned 5 apparent `mfa`/`totp`/`otp`
hits in `auth-handler`, and **every one was a base64 substring inside a lockfile integrity hash**
(`sha512-...AmfAaJ...` matches `mfa`). **Word-boundary re-run over source: ZERO. Positive control
`password`: 157**, so the probe finds things. `PORTAL_AUTHHARD`'s WS-3 was **specified and never
built**.
⛔ **IF ANY CELL RE-DERIVES THIS, USE A WORD BOUNDARY AND EXCLUDE LOCKFILES**, or it reproduces the
near-miss that nearly recorded *"MFA partially exists"*. **There is no MFA to extend — 2.1 builds it.**
⚠ This warning is recorded here because it did NOT reach this decomp on the first pass: it lives in
msg 17168, which was EMITTED but unread when §3 was written, while the parallel D7 naked-zero warning
did reach it. **A decomp is only as complete as the messages its author actually opened** — found by
measuring the READ clock rather than recalling it.
⛔ **2.0 IS DECIDED BEFORE WS-1 SHIPS — the PRD's one hard ordering constraint.** A Cognito answer
changes where the identity record lives and would make the WS-1 migration wrong. **1.1 is therefore
DEP-BLOCKED on a gate, not merely sequenced after it.**
⛔ **2.2 IS SEPARATE FROM 2.1 DELIBERATELY.** Vendor egress needs Andrew's explicit per-use word —
availability is not authorization. Splitting the legs lets the email leg ship without waiting on him.

### WS-3 — Remembered device

| Cell | Deliverable | Owner | Depends | Status |
|---|---|---|---|---|
| **3.1** | TTL value. | **ANDREW** | — | ⛔ **ANDREW-BLOCKED** |
| **3.2** | Bounded trust window: explicit TTL, explicit revocation path, **per-device not per-account** scope. | AE | 3.1, 2.1 | DEP-BLOCKED |

**Acceptance:** a remembered device skips the challenge inside the window and is challenged after it;
logout-everywhere revokes it; **the window cannot be extended by a client-supplied value.**
⛔ **TTL IS ANDREW'S CALL AND MUST NOT BE DEFAULTED.** He said the cookie *"lasts"* without saying how
long. **An unmeasured exact constant fails closed looking principled** — a decomp that writes "30
days" has invented a requirement.
⚠ **PRIOR ART WITH A MEASURED NEGATIVE RESULT:** `ADVI_BDAPIMIG` established that a device-trust
cookie **did NOT durably skip daily MFA in production** (`ef75aaa21`, `3dbdcc73d`) — the system
re-verified every day. That is a *vendor's* MFA, not ours, so it does not transfer as a constraint —
but it is the estate's one live data point on this exact mechanism and 3.2 should read it before
designing.

### WS-4 — Front-end account creation

| Cell | Deliverable | Owner | Depends | Status |
|---|---|---|---|---|
| **4.1** | Admin UI over the **already-existing** `POST/GET /auth/admin/users`. | DE | — | **READY** |

**Acceptance:** an Opal admin creates a working account entirely in the browser — no console, no table
edit.
⭐ **SCOPE REDUCTION, load-bearing: the API EXISTS.** This is a front-end + authorization workstream
only. **4.1 is READY now** and gates nothing behind it except WS-5.

### WS-5 — Partner-admin delegated user-add

| Cell | Deliverable | Owner | Depends | Status |
|---|---|---|---|---|
| **5.1** | Adopt `firmRole=admin` (§1 — exists) as the WS-5 authorization predicate. **Adoption, not design.** | AE | 4.1 | DEP-BLOCKED |
| **5.2** | Firm admin adds users **within their own firm only**; identity record still written to `opal-users-v2`. | AE + DE | 5.1 | DEP-BLOCKED |
| **5.3** | ⛔ **THE REFUSAL EXERCISE** — the same admin is REFUSED adding a user to a *different* firm. | AE + **CVO** | 5.2 | DEP-BLOCKED |

**Acceptance — BOTH halves required.** Success alone tests nothing.
⛔ **THE GATE IS ON THE PAGE *AND* THE API.** `ADVI_PRVSYS_PRD.md:77`: *"never page-only; the API
independently re-checks the JWT, a hidden page is not a control."* A UI-only restriction is
decoration. **Name the input that makes the guard refuse, and run it.**
⚠ **NAMED HAZARD FOR 5.3, WITH ITS VINTAGE — VERIFY BEFORE RELYING ON IT.**
`docs/briefs/ADVI_PARTNER_AUTHZ_backend_enforcement_scope_20260629.md:48-53` records **G2, an
authorizer claim-parity gap**: `firmRole`/`advisorRole` were populated on **one entry path and not the
other**, so *"enforcement that keys on `firmRole`/`advisorRole` silently degrades to `'null'`"*
depending on how the request arrived. **If that is still live, WS-5's guard can read null on one path
and the refusal exercise passes or fails by entry route rather than by authorization.** ⛔ This is
**dated 2026-06-29 and may be fixed** — it is a hazard to MEASURE at 5.3, not a fact to carry forward.
Re-derive it with a positive control before designing around it.

### WS-6 — Onboarding + account-creation review

| Cell | Deliverable | Owner | Depends | Status |
|---|---|---|---|---|
| **6.1** | The current onboarding path written end to end, gaps named. **Output is a decision list, not a build.** | AE or DT | — | **READY** |

**Acceptance:** the review names, for each step, **what a new user actually receives and when.**
Feeds WS-4/WS-5; **does not gate them.**

---

## 4. SEQUENCING

```
2.0 [CTO GATE]  --> 1.1 --> 1.2 --> 2.1 --> 3.2 --> (WS-3 done)
                              ^        ^
                              |        +-- 3.1 [ANDREW: TTL]
                              +-- 2.2 [ANDREW: SMS vendor egress]
4.1 --> 5.1 --> 5.2 --> 5.3            (independent of the 2.0 gate)
6.1                                     (independent; feeds 4.x/5.x, gates nothing)
```

**READY now — three cells, and only one is a build:** `2.0` (the CTO arch-gate, and it is the
critical path for everything in WS-1/WS-2/WS-3), `4.1`, `6.1`.
**The whole MFA spine is behind one unmade architectural decision.** That is the single highest-value
act in D12 and it needs no staffing beyond the CTO seat.

---

## 5. PRECONDITIONS BEFORE ANY CELL EXECUTES

1. **Placement ruled** (open decision #1) — then TOs cut with real `issued_to` serials.
2. **Staffing** — no work-population seat is live on this device; I have seated none, because seating
   a lane to build an unplaced directive would place it.
3. **A CVO reader exists.** `3.0.0_SA_CVO~Z` is dead. **Cell 5.3 is a cross-firm refusal exercise
   whose entire value is independent certification** — a build seat scoring its own refusal is the
   author-verifies-author shape and voids the evidence. `ADVI_PRVSYS_PRD.md:54` already calls the
   tenant-isolation gate *"CVO-ratified"*.

---

## 6. WHAT IS EXPLICITLY NOT IN THIS DECOMP

- **No alarm, SNS subscriber, page or monitor.** Not open for discussion; GLOBALALARM is a
  consolidation plan, not a licence.
- **No Cognito presumption.** Cell 2.0 decides it. `PORTAL_AUTHHARD`'s note that *"a Cognito migration
  is a larger blast radius than the gap warrants"* is an **input to the gate, not a ruling**.
- **No `PORTAL_AUTHHARD` wave re-run.** Import its PRD as prior art; do not reopen its waves.
- **No user attributes in the partner table.** §1's boundary.
- **No placement, on any cell.**


---

# AMENDMENT 1 — 2026-08-31 ~23:2xZ: **ANDREW-DIRECT ~23:15Z @`efcfa8cc5b` — FOUR CELLS CLOSE, THREE OPEN**

Verbatim, entire: *"All recs approved. Make sure that on the email otp we should be properly set up
with SES now that its no longer sandboxed. The only thing we will want to clarify is the DNS/DKIM/DMARC
and health of that service so these things don't go to spam. Furthermore, we will want to do the
testing for 2FA on my account so we know it works before pushing anything to clients"*
Relayed by `1.0.0_SA_CTO~Z` (msg 17191) from its own `/open-calls` at the site-Z terminal.

## CELLS THAT CLOSE

| Cell | Was | Now |
|---|---|---|
| **placement** | ANDREW-BLOCKED | ⭐ **CLOSED — D12 IS PLACED ON SITE Z.** TOs are cuttable. |
| **2.0** arch-gate | GATE / READY | ⭐ **DECIDED — BUILD IN `auth-handler`**, by `1.0.0_SA_CTO~Z` under the PRD's own CTO gate. Grounds: the bespoke token is read by ~8 surfaces incl. 2 at the CDN edge; Cognito changes issuer and shape for all of them to add a challenge in front of a working session flow. Entra eliminated on POPULATION — portal users are partner-firm clients outside Opal's tenant. Decision record owed by that seat. |
| **1.1 / 1.2** | DEP-BLOCKED on 2.0 | **READY** — the gate that blocked them is decided. |
| **3.1** TTL | ANDREW-BLOCKED | ⭐ **CLOSED — 30 DAYS, revocable by sign-out-everywhere.** 3.2 is now DEP-BLOCKED on 2.1 only. |
| **2.2** SMS leg | ANDREW-BLOCKED | **DEFERRED, not retired.** Email OTP proceeds now; SMS still needs his explicit per-use word before any vendor egress. |

⛔ **CALL 4 IS SEQUENCING, NOT A SCOPE CUT.** He asked for user CHOICE of channel. Email-first removes
a vendor decision from the critical path; **it does not retire the SMS leg.**

## THREE NEW CELLS FROM HIS OWN WORDS

| Cell | Deliverable | Owner | Status |
|---|---|---|---|
| **2.3** | **SES readiness CONFIRMED** for this use. He states sandbox exit as FACT — ⛔ **a stated premise is still measured before it is built on**, and if the account is not actually out of sandbox that is a FINDING TO REPORT, not to quietly fix. | CTO (taken) | **READY** |
| **2.4** | **DNS / DKIM / DMARC + service health.** ⭐ **THIS IS AN ACCEPTANCE CONDITION OF WS-2, NOT A FOLLOW-UP: a one-time code that lands in spam is a BROKEN LOGIN, not a degraded one.** | CTO (taken) | **READY** |
| **2.5** | **PER-ACCOUNT MFA ENABLEMENT.** ⚠ **THIS IS `1.0.0_SA_CTO~Z`'s INFERENCE, EXPLICITLY NOT ANDREW'S WORDS**, and it is carried as such: B.3 names an ordering (his account before clients), which is unsatisfiable if the MFA switch is fabric-wide. **If the inference is wrong, this cell is void — it is not a requirement he stated.** | AE | **READY** |

⛔ **2.4 IS A DIAGNOSTIC, NOT A LICENCE TO BUILD A DELIVERABILITY MONITOR.** See the scope limit below.

## WS-2 ACCEPTANCE — AMENDED

Prior acceptance stands, **plus**: the OTP email must be confirmed to arrive in an inbox rather than a
spam folder (2.4), **and** — **B.3, A STAGED-ROLLOUT GATE NAMING AN ORDERING:** *"we will want to do
the testing for 2FA on my account so we know it works before pushing anything to clients."*
**No client account is exposed to MFA before his own account has been exercised end to end.** This
binds the workstream's acceptance; it is not a test case inside it.

## ⛔ WHAT THIS RULING DOES **NOT** DO — three limits, carried verbatim from `1.0.0_SA_CTO~Z`

1. **THE ALARM MORATORIUM STANDS.** Call 2 lifted ONE thing BY NAME (D7's reminder). **A hold lifted
   by name is lifted for that name.** No general licence to build alerts, monitors, SNS subscribers or
   freshness checkers follows — including a deliverability monitor off 2.4.
2. **TWO DIRECTIVES ARE PLACED, NOT THE REGISTER.** The ~21:1xZ whole-register call stays **OPEN** for
   D0–D6 and D8–D11. The approved rec explicitly proposed deferring them.
3. **`issued_to` IS STILL A PLACEMENT EVERYWHERE ELSE.** The discharge is for D12 and D7 only.


---

# FINDING F-1 — 2026-09-01 ~01:1xZ: **AN INTENDED IAM RESTRICTION THAT RESTRICTS NOTHING**

**OPEN. NO OWNER. Not a cell, not assigned, not closed by W1 or W2.** Recorded here because it was
found inside D12's work and would otherwise live only in a message thread.

Found by `1.0.0_SA_CTO~Z` on the live role `opalinvest-auth-lambda-role`:

| policy | grant | condition |
|---|---|---|
| `opalinvest-auth-permissions` | `ses:SendEmail` on `*` | `StringEquals ses:FromAddress = noreply@opalinvest.dev` |
| `ses-send-email` | `ses:SendEmail` on `identity/*` | ⛔ **NONE** |

**IAM is a union of Allows and there is no Deny**, so the second statement grants exactly what the
first one's condition excludes. **The narrow grant is decorative.** Someone wrote that condition
intending to constrain what this role may send as; it constrains nothing.

⛔ **W2 REPOINTED ALL AUTH MAIL TO `noreply@` AND DID NOT FIX THIS.** Andrew's basis was semantic —
*"there is nobody responding to these"* — not remedial. **Anyone reading "all auth mail now sends from
`noreply@`" as "sending is now restricted to `noreply@`" has drawn exactly the false conclusion this
workstream spent a night avoiding.** That reading is why the repoint was nearly shipped as a security
fix, and why `0.7.0_AE_CloudOps~Z` deleted its own retracted "DENIED by IAM" comment from `email.ts`.

## Why it is recorded and NOT acted on

**Nothing is failing.** The condition has never blocked a send; the finding is that it never could.
⛔ **Changing it is an IAM act with its own gate and its own owner** — it is not a side effect of a
sender repoint, and no lane was authorised to widen or narrow a policy. `0.7.0_AE_CloudOps~Z`
explicitly touched none.

## How it was found — worth keeping, because the route was backwards

A simulation said `support@` was **denied**; the world then delivered a `support@` email to Andrew.
The cause was `--resource-arns "*"`, which matches the *first* statement's `Resource` and **not**
`identity/*`, so the simulator only ever evaluated the conditioned grant. **A control run in a separate
invocation agreed — because both calls carried the same wrong ARN.**
> The false finding was "the mailer is broken." The true finding is its opposite: **the mailer works
> precisely because the restriction does not.** Chasing a wrong answer produced a real one.


---

# AMENDMENT 3 — 2026-09-01 ~01:2xZ: **WS-2 IS NOT COMPLETE. THE LOGIN-CHALLENGE UI DOES NOT EXIST.**

Andrew, ~01:2xZ, VERBATIM: *"I got an OTP just now, but that flow doesnt make sense if i am not
presented wit a page to sign in to input it. Furthermore, OTP should be opt in, like you have to say
'Yes' on some prompt that it will send you an email OTP or something, not just send silently without a
UI flow."*

**MEASURED** by `1.0.0_SA_CTO~Z`: `mfaRequired` / `mfa/verify` / `mfaToken` in `portal/src` = **ZERO**,
against a positive control of **10 auth files** including `LoginPage.tsx`. The probe works; the absence
is real. The backend correctly returns `mfaRequired: true` with no session token — **the browser has
nowhere to type the code.**

## NEW CELL 2.7 — the login challenge UI · DE-class · **NOT SEATED**

| | |
|---|---|
| **2.7** | Challenge screen (code entry, resend, error states) · an **OPT-IN PROMPT before any send** · the **email-or-text SELECTION at that moment** · one flow for everyone (the client-vs-Opal split does not arise here). Owner: **DE**. Status: **READY, NO LANE SEATED.** |

⛔ **POPULATION IS ANDREW'S CALL.** No DE lane is seated and I am not seating one on any seat's say-so,
including my own. D7 remains parked ahead of it.
⛔ **NOBODY ENABLES MFA ON ANY FURTHER ACCOUNT.** The pilot cohort cannot proceed until 2.7 exists —
enabling it for "a few people" today would lock out a few people. **His account is currently the only
one enabled, and he cannot complete a login.**

## ⭐ HIS "OPT-IN" IS NOT NEW SCOPE — IT IS THE HALF WE DROPPED

His original 2026-08-31 memo: *"the client has an opportunity to select email or text for an OTP
receipt."* **We built the preference FIELD (cell 1.1) and never built the SELECTION MOMENT.** "An
opportunity to select" was always a UI event at challenge time. Both his memos agree; we implemented
half of one.

## ⛔ HOW A 10/10 PRODUCED A FEATURE A HUMAN CANNOT USE — AND THE DEFECT IS IN THIS DOCUMENT'S CHILD

```
PRD @2da36986f6  "cannot reach the DASHBOARD ... exercised end to end"        <- a BROWSER outcome
this decomp      "cannot reach the DASHBOARD ... exercised"                    <- carried faithfully
the W1 TO, W1-3  "cannot reach the DASHBOARD -- exercised end to end AGAINST
                  THE DEPLOYED HANDLER, not a unit test."                      <- the narrowing
```
**The clause `against the deployed handler, not a unit test` was added by `2.0.0_SA_COO~Z` to RAISE
rigor** — to forbid a unit-test pass. It kept the word *dashboard* and named the instrument as the
handler, and an executor reading it tests the handler. **The word survived; the surface moved
underneath it.**

> ### A CLAUSE THAT NAMES THE INSTRUMENT CAN RELOCATE THE SUBJECT — AND IT READS AS TIGHTENING WHILE IT DOES.
> **When a PRD exercise names a USER-VISIBLE outcome, do not name the instrument in the criterion at
> all — name the OBSERVER.** *"A person cannot reach the dashboard"* survives translation;
> *"exercised against the deployed handler"* does not.

**W1's 10/10 stands and no seat mis-scored anything.** Every criterion was met as written.
`0.7.0_AE_CloudOps~Z` built and proved exactly what W1-3 asked for. **The ask was wrong, not the work
— and the ask was mine.**


---

# FINDING F-2 — 2026-09-01: ⛔ **A CORRECT PASSWORD ALONE POISONS THE AUTH STATE. THIS GATES THE PILOT COHORT.**

> ## ⚠ CORRECTED ~02:1xZ BY THE RED CAPTURE — READ THIS BEFORE QUOTING ANYTHING BELOW.
> **The headline was "a correct password alone REACHES `/market`". THE BROWSER FALSIFIED IT.** The
> capture's own pre-registered prediction was wrong in its headline and its author said so in those
> words before anyone built further on it.
>
> **WHAT ACTUALLY HAPPENS, measured in a browser at `be39451b`, tree pristine, fix NOT landed:**
> - The submit **does NOT navigate.** It stays on `/login` and renders
>   `Cannot read properties of undefined (reading 'email')` — on the `mfaRequired` branch `data.user`
>   is undefined, `OpalAnalytics.init` throws a **TypeError**, `LoginPage`'s catch renders it, and
>   `navigate()` is never reached. ⛔ **RUNG 5 IS WITHDRAWN: an unrelated crash, not the gate, stopped
>   the navigation.**
> - ⛔ **BUT THE GATE IS STILL DEFEATED, because setState runs BEFORE the throw.** `localStorage`
>   `accessToken` === the **STRING `"undefined"`** — only reachable if the provider's setState block
>   executed. **`isAuthenticated` is true while no token exists. The state IS poisoned; only the
>   automatic redirect was blocked.**
> - **THE ACTUAL RED, and it is exactly DE3-2's wording — REACHABLE BY URL:** in-session SPA navigation
>   to `/market` is **ADMITTED** — no redirect, no login form (`input[type=password]` = null).
>   Screenshot **READ**: a blank silver canvas.
> - ✅ **AND THE BOUND THAT MAKES IT PRECISE: a FULL RELOAD of `/market` BOUNCES to `/login`.**
>   `refreshToken()` runs on mount, there is no refresh cookie, `isAuthenticated` stays false, and
>   `ProtectedRoute` correctly redirects. **DE3-2 names three limbs — it FAILS the URL limb and PASSES
>   the refresh limb.**
> - ✅ **NO DATA WAS DISCLOSED, stated rather than left implied:** all five prefetch calls returned
>   **401** (cumulative_chart, dashboard, mix_summary, partner_analytics_quarterly,
>   timeseries_overview). **Server-side auth holds completely. The net effect today is a broken empty
>   page, NOT a data leak. This is NOT a breach and must not be relayed as one.**
>
> **CORRECTED SENTENCE, and this is the one to quote:** *a correct password alone POISONS THE AUTH
> STATE, and `/market` is then REACHABLE BY URL WITHIN THE SESSION.*
> ⚠ **INSTRUMENT:** `window.fetch` overridden to return the exact shape `index.ts:167` emits,
> `/auth/me` stubbed 401 (the real server's behaviour for a bad bearer), everything else passed through.
> **This exercises THE CLIENT from the fetch boundary inward.**
>
> ### ⭐⭐ THE RED IS **REPRODUCED ACROSS SEATS, PROCESSES AND VINTAGES — ON ONE INSTRUMENT** ~02:2xZ
> ⛔ **DO NOT SHORTEN THIS TO "DOUBLE-OBSERVED."** `1.0.0_SA_CTO~Z` added the axis my first wording did
> not name, and it was right to: **a compact phrase outruns its own qualifier once it is in a record.**
> ```
>   seat / author       INDEPENDENT   the certifier did not write the fix
>   process / server    INDEPENDENT   own vite, port 5199, own browser
>   vintage mechanism   INDEPENDENT   immutable worktree vs the DE lane's live tree
>   INSTRUMENT CLASS    ⛔ THE SAME   both frames are Playwright + a fetch-boundary stub
> ```
> **WHAT THE FOUR BUY:** seat-specific error, author bias, a poisoned local tree and a one-off
> environment fluke are all excluded. That is most of what independence is for and it is real.
> ⛔ **WHAT THE FIFTH CANNOT:** an error **inherent to stubbing at the fetch boundary** is invisible to
> both frames, *because both make it*. **Two runs of one instrument cannot find that instrument's own
> error.**
> `3.0.0_SA_CVO~Z`'s second frame is **VALID and SCOREABLE**, and it reproduces the DE frame limb for
> limb — **including the falsified rung 5**: submit does NOT navigate, identical error string,
> `localStorage.accessToken` the **STRING** `"undefined"` (len 9), `/market` admitted by in-session nav
> with no password input, blank silver canvas **READ not asserted**.
> ⭐ **PRE-FIX BYTES WITHOUT TOUCHING ANY TREE:** a detached `git worktree` of `portal` at `be39451b`,
> sparse-checkout, own vite on :5199. **The vintage cannot move under the run** — pinned to an immutable
> commit, immune to the DE lane's concurrent edits. Nothing read-modify-written, nothing reverted.
> ⚠ **AND AN INSTRUMENT TRAP WORTH CARRYING:** its own script first reported `VINTAGE_OK=false` from a
> raw SHA-1 over on-disk bytes — served 23,003 B vs git blob 22,344 B, **difference 659, and the file
> contains exactly 659 CRLFs.** `git hash-object` normalizes per the repo's line-ending config and is
> the instrument that *defines* blob identity. ⛔ **It did not settle that by swapping instruments until
> one said yes** — it ran an independent content check (`isAuthenticated: true` ×3 present,
> `mfaRequired` ×0, the post-fix marker ABSENT). **Two instruments, one conclusion.**
>
> ### ⭐ EVIDENTIARY STATUS UPGRADED ~02:1xZ — THE STUB'S LIMIT IS **DISCHARGED**, NOT MERELY ACKNOWLEDGED
> The capture was honestly bounded as *"it cannot prove the server emits that shape,"* and every seat
> repeated that bound — leaving the finding on **one exercise plus a source read.**
> **`0.7.0_AE_CloudOps~Z` CLOSED IT WITH AN EXERCISED ARTIFACT:** the live `/auth/login` response
> captured during tonight's actual W1-3 run, **including the absent `user` field that causes the
> TypeError.** Not a re-read of `index.ts:167`.
> >> **F-2 IS NO LONGER "CLIENT EXERCISED, SERVER SOURCE-READ." BOTH HALVES ARE EXERCISED, ON TWO
>    SURFACES** — and the stub is now CONFIRMED to match reality rather than assumed to. <<
> ⚠ **STILL OPEN, AND IT STAYS STATED: THE JOIN IS NOT EXERCISED.** Nobody has driven the REAL server
> end-to-end into a REAL browser — that needs a gated account, which this very gate forbids.
> **Correct status: BOTH HALVES EXERCISED SEPARATELY, THE JOIN NOT EXERCISED.**
> ⛔ **RECORDED BECAUSE THE DIRECTION IS UNUSUAL:** almost every correction tonight moved a claim
> DOWNWARD. This one moves it UP. **A finding recorded weaker than its evidence gets discounted by the
> next reader** — and this one is a gate on a cohort, so understating it is not the safe error.

⭐ **WHY THIS ENTRY IS BETTER THAN THE ONE IT REPLACES:** rungs 1–4 are confirmed and are what produce
the RED. **Rung 5 was wrong, and only a browser could have shown that** — three seats had read it at
source and agreed. **The capture was worth insisting on for the opposite of the expected reason: it did
not confirm the finding, it corrected it.**

Found by `0.4.0_DE_ClientPlatform~Z` (msg 17360) **by reading, hours before it could have exercised it**, and
**independently re-derived at source by `1.0.0_SA_CTO~Z` (17369) and `3.0.0_SA_CVO~Z`** — ⚠ which all
three correctly declined to call corroboration: **three seats on one rung is one instrument counted
three times.** It raises confidence in the READING and says nothing about the WORLD. **That is why the
browser capture exists.**
— which is the only reason it is known before anyone was gated.

## THE CHAIN — **SIX** rungs, each read at source (portal `be39451b`, workspace `c7dfddcdff`)

| # | file | what it does |
|---|---|---|
| 1 | `index.ts:166` | the MFA challenge returns **HTTP 200**, not 401 |
| 2 | `AuthContext.tsx` `login()` | throws only `if (!response.ok)` — **a 200 does not throw** |
| 2b | `AuthContext.tsx:349-354` | ⭐ **THE RUNG THE FIRST READING MISSED:** the `/auth/me` **401 is SILENTLY ABSORBED by the null-claims FALLBACK**, so no error surfaces even though the server correctly refuses. Added by `1.0.0_SA_CTO~Z`'s independent re-derivation. |
| 3 | same function | sets `isAuthenticated` **as a LITERAL**, never derived from whether a token exists; `accessToken` is `undefined` on this branch and `localStorage` stores the string `"undefined"` |
| 4 | `ProtectedRoute.tsx` | gates on `isAuthenticated` **only** — the token is never consulted |
| 5 | `LoginPage.tsx` | `login()` did not throw → `navigate('/market')` |

> ### THE SERVER IS CORRECT. THE CLIENT ADMITS ON A FLAG IT SETS ITSELF.
> `isAuthenticated` is an assertion, not a derivation — and step 3 is where a security property became
> a literal.

## ⭐ THE INTEGRATED OBSERVATION MAY ALREADY EXIST — ONE LINE IN ANDREW'S CONSOLE

`1.0.0_SA_CTO~Z`, and it is the highest-value single observation still available on this finding.

**Andrew attempted a REAL MFA login against the REAL server tonight and could not complete it.**
Reconstructed against the RED, his experience is **limb-for-limb the same shape**: submit password →
server returns the MFA response → client throws → he stays on `/login` and reads it as *"locked out."*

> **So the "lockout" and the "RED" may be ONE EVENT SEEN FROM TWO ANGLES** — the user-visible half
> (login fails) and the security half (auth state poisoned, `/market` reachable by URL in-session).
> **The second half is invisible to anyone who does not manually navigate**, which is why it was never
> reported as part of the lockout.

⛔ **UNMEASURED AND NOT CLAIMED: nobody read his `localStorage.accessToken`.** If it holds the **STRING**
`"undefined"`, **the RED is confirmed ON THE INTEGRATED SYSTEM — the one rung neither frame can reach**,
and it closes the stub bound rather than working around it.
⚠ **NOT AN ASK TONIGHT.** It is ~02:30Z, it blocks nothing, and the RED is already sufficient to justify
the fix. **Queued for when he is next at the terminal** — and worth asking *then*, because it is one
line in a console and it retires the only limb this finding cannot otherwise reach.

## ⛔ WHY THIS IS A COHORT GATE AND NOT A FIRE TONIGHT

**It is not a live exposure today, and that is measured, not assumed: 0 of 48 accounts are gated, so
the `mfaRequired` branch is unreachable in production.**
>> **IT GOES LIVE THE MOMENT THE FIRST ACCOUNT IS GATED — WHICH IS EXACTLY WHEN THE PILOT COHORT
   STARTS.** Enabling "a few people" before the client fix would hand each of them a login that a
   correct password alone completes. <<
⛔ **SO: NOBODY IS ENABLED — INCLUDING ANDREW'S OWN RE-ENABLE — UNTIL DE3-2 PASSES IN A BROWSER.** This
is now a **hard precondition on his cohort decision**, and it must travel with the cohort question
rather than sit in this file.

## BOUNDING — the finder's own, kept verbatim in substance

**SOURCE-CONFIRMED on the code path; UNEXERCISED at the browser rung.** It has not been observed in a
browser and currently **cannot** be — 0 accounts are gated and that lane is barred from enabling one.
**So: not "proof", not "exercised" — five rungs at `file:line`, no browser observation yet.**
⭐ That bound is what makes it usable. **DE3-2 is the row that will exercise it**, and it was written to
catch exactly this: *"with the correct password and NO code, the dashboard is not reachable — by URL,
by back-navigation, or by refresh."* The criterion found its defect before it ran.

## DISPOSITION

**The client fix is `0.4.0_DE_ClientPlatform~Z`'s and is squarely in its lane** — it is proceeding with
it now as DE-a (handle the `mfaRequired` 200 without authenticating; derive admission from a token, not
from a literal). **Not a new TO**; it is inside DE1/DE2's existing scope.
**No IAM, no backend, no account enablement follows from this finding.**
