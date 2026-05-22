# DIRECTIVES — The Active Mandate for `0.0.0_AB_MSTR`

**Status:** v1.1 RATIFIED 2026-05-22 — format ratified; Active Directives still to be authored by Andrew
**Authority:** Andrew, and Andrew alone. MSTR may propose a directive and the CVO may review and recommend, but only Andrew adds, amends, or retires one — this is a Tier-0 law document, never CVO-ratifiable (Constitution Art. III, XIV). (owned-paths: `0.0.0_AB_MSTR` not in `permitted_agents`.)
**Version:** 1.1 · **Last updated:** 2026-05-22
**v1.1 amendment:** Directive format tightened to a full schema — `non_goals`, `allowed_stakes`, `stop_conditions`, `issued_by` and the ignition-validation rule added (external Phase-3 review).

---

## What this document is

The standing mandate. Under Constitution Article II, MSTR pursues **only** what is
written here and its *faithful extensions* — it may not originate goals outside
this file. This is Andrew's steering wheel: to redirect the fabric's autonomous
top layer, edit this document.

## How MSTR uses it

- Read in full at the start of every operating cycle (Constitution Art. XII); the
  cycle record attests the version read.
- Every Decision Ledger entry cites ≥1 `directive_ref` into this file and a
  `mandate_distance` (Stakes Matrix rule 6). An action that cannot cite an active
  Directive is a new goal — out of mandate — proposed back to Andrew.
- A Directive that conflicts with the Constitution is void to the extent of the
  conflict (Art. III); MSTR surfaces such a conflict rather than acting on it.

## Ignition validation

Before `/govern` will originate work under a Directive, it validates the
Directive is: **(a)** well-formed — every required field below present;
**(b)** `status: active`; **(c)** `issued_by: andrew`. A malformed or
accidentally-active Directive does **not** ignite autonomy — `/govern` flags it
and stays in scan-and-report-only mode. Ignition takes all three.

## Directive schema

Each Directive is one block. **Every field is required** (use `none` where a
field genuinely does not apply — never leave it blank).

```
### D-NNN — <short title>
- directive_id:           D-NNN
- status:                 active | paused | retired
- issued_by:              andrew
- issued_at:              <date>
- objective:              <the mandate, imperative — what MSTR is to pursue>
- scope:                  <what is explicitly IN>
- non_goals:              <what is explicitly OUT — the cheapest drift control>
- allowed_stakes:         S0-S2 | S0-S3 | S0-S4
                          <the ceiling on what MSTR may even PROPOSE under this
                           Directive. S0-S2 = pursue it but never propose a
                           gated action; S0-S4 = the full range is in play.>
- success_signals:        <how Andrew/MSTR knows the directive is being served>
- stop_conditions:        <conditions under which MSTR halts work on this Directive>
- review_cadence:         <how often this Directive itself should be revisited>
- expiry_or_review_date:  <date the Directive expires or must be re-confirmed>
```

The three load-bearing fields are **`non_goals`**, **`allowed_stakes`**, and
**`stop_conditions`** — they are the per-Directive leash. Keep `objective` broad
enough that MSTR has room to ideate; keep `non_goals` and `allowed_stakes` tight
enough that "faithful extension" stays legible.

---

## Active Directives

> _Andrew: author the standing directives here. Until at least one Directive
> exists that passes ignition validation, MSTR has no mandate — `/govern` will
> only scan, report, and surface the empty-mandate state; it originates nothing._

_(none yet)_

---

## Example — format reference only, NOT active

```
### D-000 — (EXAMPLE) Reduce single-vendor data dependence
- directive_id:           D-000
- status:                 retired   (example — never active)
- issued_by:              andrew
- issued_at:              2026-05-22
- objective:              Drive the portal's market-data surfaces toward
                          multi-source resilience so no single external vendor
                          is a point of failure.
- scope:                  Sourcing assessments; dual-source architecture;
                          charters handed to CTO/COO for execution.
- non_goals:              Signing vendor contracts or committing spend (S3,
                          Andrew-ratified). Changing WHAT data the product shows
                          (a product call, not a sourcing call).
- allowed_stakes:         S0-S2   (MSTR assesses and charters; it does not
                          propose the gated procurement itself)
- success_signals:        Every market-data surface has a documented primary +
                          fallback source; no surface single-vendor without an
                          explicit accepted risk.
- stop_conditions:        Andrew rules the single-vendor risk acceptable; or a
                          dedicated-seat procurement supersedes the work.
- review_cadence:         monthly
- expiry_or_review_date:  2026-08-22
```

---

## Retired Directives

_Retired Directives move here with their retirement date — kept for the audit
trail and so `/mstr_review` can resolve historical `directive_refs`._

_(none yet)_

---

## Versioning

Any edit by Andrew bumps **Version** and **Last updated** above. MSTR re-reads on
its next operating cycle and the cycle record attests the new version. A Directive
set is never silently changed — the version bump is the signal MSTR keys on.
