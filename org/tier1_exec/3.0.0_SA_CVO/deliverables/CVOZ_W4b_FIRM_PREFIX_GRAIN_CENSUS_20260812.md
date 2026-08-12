# FIRM-PREFIX GRAIN CENSUS — which "firm" artifacts descend below firm grain

**Author:** `3.0.0_SA_CVO~Z` · **Date:** 2026-08-12 · **Scope:** `s3://opal-data-bd/platinum/firm/`, firm `bd` only
**Method:** STRUCTURAL ONLY — key names and self-description fields. **No value enumeration; no client identifiers read.**
**Trigger:** the `advi.14` amendment (`0abd2e84fd`) found a firm-prefix artifact carrying per-client AUA. This asks whether it is alone.

---

## THE ANSWER

> **It is not alone. TWO of the thirteen firm-prefix artifacts descend to per-client grain, and both
> say so in their own `description` fields.** The other eleven do not.

| artifact | bytes | `adv_drill` share | self-description |
|---|---|---|---|
| **`advi.14` timeseries_chart** | 36,457,769 | **23.7%** | `"Per-client AUA for architect <name>"` · `"AUM by client vintage for <CITY>, <ST>"` |
| **`advi.10` cumulative_chart** | 4,709,304 | **27.0%** | `"Per-client AUA for architect <name>"` |

Both carry `adv_drill` keyed by **nine advisor names** — the same nine — each block self-described as
per-client. In `advi.10` that block is **27% of the artifact**; in `advi.14`, 23.7%.

**⛔ In neither case did I enumerate the `categories` lists.** On those descriptions they are very
likely client identifiers, and reading them is a client-data read this run holds no warrant for —
the same scope defence `0.1.0_DE_MarketIntelligence~Z` made on `tc.06.vintage_grain` and which I
upheld as certifier the same afternoon.

**⚠ NOT a security or authorization finding.** The routes are auth-enforcing per the author's
measured Plane-A cells; I have not assessed who can reach them; client-grain data behind an
authenticated route is not by itself a defect. **This is a SENSITIVITY CLASSIFICATION a catalog must
carry**, and it is invisible from the artifacts' names, their prefix, and their eleven siblings.

---

## MY INSTRUMENT OVER-FIRED, AND THE SPLIT IS THE USEFUL PART

The tell regex matched **seven** artifacts. **Two are real. Five are false, in two distinct ways** —
and a reader who took the raw count would conclude the whole firm prefix is client-grain.

**FALSE CLASS 1 — a COUNT of clients is not client data.** `client_count`, `new_clients`,
`fee_earning_client_count`, `existing_client_count` are firm-aggregate scalars. They matched a regex
containing `client`. Present in `dashboard` (575 B), `leaderboard`, `header_metrics`,
`clients-tab-slim`, `partner_analytics`, and the two undeclared keys. **All firm-aggregate; none
descend.**

**FALSE CLASS 2 — a ROLE NAMED after clients is not client data.** `advi.02
advisor_nna_canonical` matched on the key `"Centralized Client Ops"` — an advisor **role/bucket
name**, not a client record.

```
regex tells        7 artifacts
genuine            2  (advi.10, advi.14 -- both by SELF-DESCRIPTION, not by key name)
false, count-only  4+ (client_count and siblings)
false, role-name   1  (advi.02 "Centralized Client Ops")
```

> **The discriminator that worked was not the key name — it was the artifact's own `description`
> field.** Both genuine cases announce themselves in prose; neither is detectable from key names
> alone, and key names produced every false positive. **A grain classifier built on key-name
> patterns would have found the wrong five and missed the right two.**

---

## THE SHAPE, FOR W5

Both genuine cases share it: a **firm**-prefix artifact whose bulk is **drill-down**, and whose
deepest drill descends past the prefix's declared grain.

- `advi.14`: `nna_geo_drill` 28.9% · `adv_drill` 23.7% · `cla` 23.1% · `geo_drill` 11.8% — **87.5% in four drill keys**
- `advi.10`: `nna_geo_drill` 32.8% · `adv_drill` 27.0% · `geo_drill` 13.4% — **73.2% in three**

**Geo drills descend STATE → CITY** (`TX` → `AUSTIN`, +9 per state, 9 states), so **the per-key
expansion problem exists INSIDE single artifacts, not only across them.** A catalog keyed at the
artifact level records one row for `cumulative_chart` and thereby records nothing about the nine
advisors, nine states and ninety cities inside it.

---

## WHAT THIS DOES NOT ESTABLISH

- **Whether the other eleven descend below depth 4.** My walk bounded at depth 4. **A negative here is
  "no tell within four levels", not "firm-aggregate throughout."**
- **Anything about the other firms' trees.** bd only.
- **Any authorization claim.** Not assessed, deliberately.
- **What the `categories` lists contain.** Not read, deliberately, and that refusal is the evidence
  of the bound rather than a gap in it.

— `3.0.0_SA_CVO~Z`
