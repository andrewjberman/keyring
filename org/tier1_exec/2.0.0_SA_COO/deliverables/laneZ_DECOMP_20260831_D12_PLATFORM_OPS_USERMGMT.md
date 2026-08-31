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

**Acceptance:** an MFA-enabled account **cannot reach the dashboard** without a live code, exercised
end to end; a wrong code fails; **a replayed code fails**; the OTP secret is never returned by any
endpoint.
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
