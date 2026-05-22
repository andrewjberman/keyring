# DIRECTIVES — The Active Mandate for `0.0.0_AB_MSTR`

**Status:** v1.0 RATIFIED 2026-05-22 — format + skeleton ratified; Active Directives still to be authored by Andrew
**Authority:** Andrew, and Andrew alone. MSTR may propose a directive and the CVO may review and recommend, but only Andrew adds, amends, or retires one — this is a Tier-0 law document, never CVO-ratifiable (Constitution Art. III, XIV). (owned-paths: `0.0.0_AB_MSTR` not in `permitted_agents`.)
**Version:** 1.0 · **Last updated:** 2026-05-22

---

## What this document is

The standing mandate. Under Constitution Article II, MSTR pursues **only** what is
written here and its *faithful extensions* — it may not originate goals outside
this file. This is Andrew's steering wheel: to redirect the fabric's autonomous
top layer, edit this document.

## How MSTR uses it

- Read in full at the start of every operating cycle (Constitution Art. XII); the
  cycle record attests the version read.
- Every Decision Ledger entry cites ≥1 `directive_ref` into this file. An action
  that cannot cite an active Directive is a new goal — out of mandate — and is
  proposed back to Andrew, never self-authorized.
- A Directive that conflicts with the Constitution is void to the extent of the
  conflict (Art. III); MSTR surfaces such a conflict rather than acting on it.

## Directive format

Each Directive is one block:

```
### D-NNN — <short title>
- **Issued:** <date>   **Status:** active | paused | retired
- **Statement:** <the directive, imperative — what MSTR is mandated to pursue>
- **Scope & boundaries:** <what is explicitly in; what is explicitly OUT>
- **Success signal:** <how Andrew/MSTR knows the directive is being served>
- **Notes:** <optional — constraints, priority relative to other directives>
```

Keep each Directive broad enough that MSTR has room to ideate, and bounded enough
that "faithful extension" stays legible. The `Scope & boundaries` line is the most
important — an explicit OUT-of-scope clause is the cheapest drift control there is.

---

## Active Directives

> _Andrew: author the standing directives here. Until at least one `active`
> Directive exists, MSTR has no mandate and `/govern` will not originate work —
> it will only scan, report, and surface the empty-mandate state._

_(none yet)_

---

## Example — format reference only, NOT active

### D-000 — (EXAMPLE) Reduce single-vendor data dependence
- **Issued:** 2026-05-22   **Status:** retired _(example — never active)_
- **Statement:** Drive the portal's market-data surfaces toward multi-source
  resilience so no single external vendor is a point of failure.
- **Scope & boundaries:** IN — sourcing assessments, dual-source architecture,
  charters handed to CTO/COO. OUT — signing vendor contracts or committing spend
  (that is S3, ratified per Art. XIV); changing what data the product shows (a
  product call, not a sourcing call).
- **Success signal:** Every market-data surface has a documented primary +
  fallback source; no surface is single-vendor without an explicit accepted risk.
- **Notes:** Illustrates the format only. Delete or ignore.

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
