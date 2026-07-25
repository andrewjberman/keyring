# CVO~Z — SYSPARITY cycle-29: `inf-sdk-exercised-label` — CLEAN, and it BOUNDS my own III-d.22

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · cron `f0291f27` · vintage @ HEAD

---

## Gate

`comp-system --check` → **SYSTEM CURRENT** (24 regions / 6 files, 0 drifted).

## VERDICT: **CLEAN** — the caveat is TRUE, self-reality-matching, and well-built

I picked this unit to test III-d.22 (*a stale caveat under-bounds its own subject*) on a fresh instance
rather than the one it was derived from. **It refutes the doctrine's applicability here, and that is the
finding.**

### The caveat holds — verified on its OWN offered reality-match

> *"the parameterized Terraform module (P1) is **FAITHFUL-BY-CONSTRUCTION but CLOUD-UNEXERCISED — DESIRED,
> never `terraform apply`'d to a real tenant on AWS** … This deferral is **deliberate** … not an oversight."*

| test | result |
|---|---|
| `tenants/acme/verify-report.json` → `tier` | **`local`** |
| `tenants/demo/verify-report.json` → `tier` | **`local`** |
| evidence of a real cloud apply | **none** — only the README's own mentions |

**The caveat offers its own falsifier** (*"reality-matched: `tenants/*/verify-report.json` reports
`"tier": "local"`"*) **and it survives being checked against it.** It also states the accepted future
proof (a one-tenant `terraform apply` smoke), gates it (`safe-apply` + CTO), and explicitly warns *"do NOT
read the SDK's local PASS as cloud-exercised."*

### >> WHY III-d.22 DOES NOT APPLY — the boundary my own doctrine needs <<

III-d.22's mechanism is a **number** written once at maximum knowledge and never re-derived. **This caveat
states no count.** It is bounded by a **binary event**: *has any tenant been provisioned to cloud?*

>> **A CAVEAT BOUNDED BY A COUNT AGES; A CAVEAT BOUNDED BY A BINARY EVENT DOES NOT. The staleness
>> mechanism requires a QUANTITY that drifts. A qualitative caveat is re-derivable by one question with
>> one answer, and it FLIPS LOUDLY when the event occurs rather than eroding silently — the exercise
>> either happened or it did not, and the person who runs it knows.** <<

**The SDK's TF surface HAS grown** (22 on disk / 16 tracked, unchanged from cycle-18's measurement) —
**and that growth does not erode this caveat at all**, because "never applied to a real tenant" is equally
true of 16 files or 60. **That is precisely the property `~61` lacked**: a counted bound decays with the
population; an event bound does not.

**This is III-d.22's second acquittal-shaped result in two cycles** (III-d.20 acquitted in cycle-25).
**Both boundaries have now cleared something, which is the only evidence that either discriminates.**

## Residuals — named, neither active, neither warranting a DRIFTED

1. **A LATENTLY generic limb.** The pattern's `DESIRED` limb is compiled `re.IGNORECASE`, so it would
   match the ordinary English *"desired"*. **Measured: zero ordinary-prose occurrences in this file** — so
   it is not currently degrading the check. **Latent, not active**, and I am recording it that way rather
   than inflating it: III-d.20 is about a generic limb *carrying* the predicate, and here two specific
   limbs (`unexercised`, `Rule 22a`) carry it.
2. **A DEAD limb that is a NEAR-MISS.** `apply-smoke` matches **zero** — while the doc says
   `` `terraform apply` smoke``. The concept is present; the token is one character-class away.
   **The pattern author was PRECISELY WRONG rather than accurately absent** — the near-miss class from the
   address-space vocabulary, landing on a check pattern instead of a term vocabulary.

## Routed

Both residuals → CTO~Z as low-priority pattern hygiene. **No estate change; no verdict change.** The unit
is doing its job.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-system --check` | CURRENT | gate-first |
| per-limb sensitivity measurement | 1 / 1 / 2 / **0** / 2 | the 0 is the dead near-miss limb |
| ordinary-prose probe for `desired` | **0** | **refuted my own generic-limb hypothesis before I filed it** |
| `verify-report.json` tier read (both tenants) | `local` | the caveat's own offered falsifier, applied |
| SDK `.tf` surface | 22 disk / 16 tracked | unchanged vs cycle-18 — and irrelevant to an event-bounded caveat |

**No instrument error this cycle.** The one hypothesis I formed — that `DESIRED` was acting as a generic
limb — **I measured and refuted before writing it up**, and recorded it as latent rather than dropping it
entirely, because the risk is real even though it has not fired.
