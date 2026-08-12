# SECURITY FINDING — `opal-ticket-api`: caller identity is STAMPED, never CHECKED. No per-caller or per-firm authorization on any of six routes.

**Raised by:** `0.1.0_DE_MarketIntelligence~Z` (OPAL_ANALYST W4c-1 `/ticket-center` decomposition, c1 @351719a4e3, 2026-08-12 ~1735Z)
**Routed by:** `1.0.0_SA_CTO~Z` → **ANDREW** (sovereign). **Status: SURFACED. NO REMEDY BUILT, NO GATE CREATED, NOTHING INVOKED.**
**Severity read (stated plainly, neither inflated nor softened):** missing tenant isolation among
**authenticated** users on a live client-facing surface. **Not** an unauthenticated door.
**Exploitability:** exploit**ABLE** by design absence, measured at source. **NO evidence of exploitation** —
that question is not answerable from this evidence and is not claimed.

## The measurement (deployed bytes, not source-of-record inference)

`opal-ticket-api` is **not in this repo** (0 hits / 25,673 files, positive control 2). Read via the
sanctioned code layer: `get-function` → `Code.Location` → download → read. **3,838-byte zip, one member,
273 lines.**

**The handler reads caller identity and never gates on it.** `_actor()` (`lambda_function.py:57-64`)
pulls `email` / `userType` / `firmId` from the authorizer context. **Every use is a STAMP, not a CHECK:**

| use | line | what it does |
|---|---|---|
| `created_by` / `requester.firm` | :106-109 | records who asked |
| `assignee` | :161 | records who claimed |
| audit rows | :76 | records what happened |

**The only `ConditionExpression`s are STATE-MACHINE guards, not AUTHORITY guards:**
- claim `:159` — `status.eq('open')`
- complete `:183` — `status.ne('completed')`

⛔ **No route compares the caller to the ticket's owner, assignee, or firm.**
- `list_tickets` `:123-141` — **no firm scoping at all**; scan/query then **in-memory** filters on
  status / assignee / ticket_type.
- `get_ticket` `:144-148` — a bare `get_item`.

**On routes namespaced `/api/scoped/`.** Plane A measured **zero** client-side guards.

**Consequence, as measured:** any **authenticated** portal user can list every firm's tickets and claim
or complete anyone's.

## Why this is being routed UP rather than into a remedy

It lands on top of an independent finding from `0.5.0_AE_OpalETL~Z` twenty minutes earlier
(PRD §9.10.3): **the portal serves TWO trees — `bd` and `inf` — behind a tenant branch**
(`TenantLayoutConfig` `static`/`lambda` + the `:569` firm gate), with client artifact sets sharing
exactly one leaf and **Jaccard overlap of 1 in 8** at client grain.

>> **Missing per-caller authorization + a genuinely multi-firm tenancy is the firm-separation harm
NEVER#2 exists to prevent — ARRIVING THROUGH THE SERVING LAYER RATHER THAN A PIPELINE.** NEVER#2's
enforcement (commit gate + IAM Deny) is pointed at pipeline trees crossing buckets. **Neither
mechanism observes an authenticated HTTP caller reading another firm's row out of one shared table.** <<

**The authorization model on a live client-facing surface is an architecture decision and it is Andrew's.**
CTO is not building a remedy, not proposing a gate, and not adjudicating scope.

## Disposition discipline held (and instructed)

- **No act, nothing built, nothing invoked** — the raiser's own posture, correct, and confirmed as standing.
- **No route was invoked to demonstrate it.** Measured from deployed bytes, which is both cheaper and
  **strictly safer** than probing a live ticket surface.
- **No cross-firm read was performed to prove absence of scoping.** The absence is proven at source; a
  live cross-firm read would **CREATE** the exposure being documented.
- **No monitor, alarm, SNS, or checker** (standing moratorium).

## The method finding underneath it — worth keeping independently

**Three documents recorded this cell as expected-UNMEASURED-FOREVER** (CTO's spec, the raiser's Plane B,
the raiser's own c0 `declared_limits`). The reasoning was sound and the conclusion was wrong:
**we were looking in the wrong COMPONENT.** The authorizer answers **authentication**
(`EnableSimpleResponses=true` → a bare boolean, source out of repo); **per-caller AUTHORIZATION lives in
the business handler**, whose deployed bytes are readable.

⛔ **BOUND: AN "UNMEASURABLE" CLAIM MUST NAME THE COMPONENT IT WAS UNMEASURABLE IN.** A component-free
unmeasurability claim is unfalsifiable — and **three seats signed one.**
**Corollary bound:** for an out-of-repo Lambda, `get-function` → `Code.Location` → read deployed bytes
**IS** the sanctioned code-layer instrument. It replaces the preflight-probe suggestion CTO had offered.

## What is NOT claimed here

- Not claimed: that anyone has exploited this. Unanswerable from this evidence.
- Not claimed: that the exposure is reachable unauthenticated. It is not — authentication holds.
- Not claimed: that `bd` and `inf` are separate **firms** in NEVER#2's sense. **That question is
  Andrew's** and is surfaced separately (PRD §9.10.3); this finding's severity depends on his answer and
  is stated without presuming it.
