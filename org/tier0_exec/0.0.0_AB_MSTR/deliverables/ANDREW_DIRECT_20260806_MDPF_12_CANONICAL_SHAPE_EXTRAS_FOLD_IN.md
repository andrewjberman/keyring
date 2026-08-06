# ANDREW-DIRECT — 2026-08-06 ~2215Z, site-Z MSTR terminal: the 12-vs-14 boundary RESOLVED — the extras FOLD IN; canonical shape law; gold irons out vendor divergence

**Recorded by:** `0.0.0_AB_MSTR~Z`, same turn, per the record+broadcast law
**Resolves:** the 12-vs-14 clarification (CTO~Z surfaced @0caf2e907; COO~Z/CVO~Z live-measured the extras)
**Supplements:** the 12-file daily contract ruling @0caf2e907 (3 types x 4 scopes, every day)

## VERBATIM

> "they should be produced in a manner where the account-units.json information (count) is included
> within the account-distribution.json, as that is the file that feeds the bell curve, which is the
> component that serves the count. Regarding non-model assets, that should be included in the
> generation of aum-metrics.json and in aggregate-aua-timeseries.json, as their respective components
> in the portal both feature non-model assets. I want these things to be identical in shape by the
> time they're in platinum. That means being canonical and working our way back layer by layer to have
> a canonical process and shape. Because the data source is different in bronze (different vendors),
> inherently bronze/silver will be differnet per scope, however in the gold layer the scripts that
> produce these files need to iron out these changes."

## WHAT THIS SETTLES

1. **THE DAILY CONTRACT IS EXACTLY 12 — and neither prior reading was right.** Not (a) 14-with-extras,
   not (b) 12-with-served-data-dropped. The two extras' INFORMATION survives; their standalone FILES do
   not:
   - `cottonwood/account-units.json` → the count folds INTO `account-distribution.json` (the file that
     feeds the bell-curve component, which is what serves the count).
   - `global/non-model-assets.json` → folds INTO the generation of BOTH `aum-metrics.json` AND
     `aggregate-aua-timeseries.json` (their portal components both feature non-model assets).
   No served information is lost; the file count converges to the 12.

2. **THE SHAPE LAW: the 12 are IDENTICAL IN SHAPE across scopes by the time they are in platinum.**
   `{scope}/account-distribution.json` has ONE schema whether scope is 49financial, inflection,
   cottonwood, or global — which means the folded fields (count; non-model) are part of the canonical
   schema FOR EVERY SCOPE, not cottonwood-only or global-only appendages. A scope without data for a
   canonical field carries the field with honest absence (per the standing null-not-zero guards), never
   a scope-specific schema.

3. **THE LAYER LAW: divergence is legitimate in bronze/silver and DIES IN GOLD.** Different vendors
   make per-scope bronze/silver inherently different; the GOLD scripts are where those differences get
   ironed out. This is Rule 17b's each-layer-has-one-job extended with a new explicit assignment:
   CROSS-VENDOR NORMALIZATION IS GOLD'S JOB. Platinum projects an already-canonical gold; it never
   patches shape.

4. **"Working our way back layer by layer"** — the canonicalization direction is serve-side-first:
   pin the platinum shape (the 12), then make gold produce it canonically, then let bronze/silver stay
   vendor-shaped. The port (one firm-parameterized `mdpf-gold-lambda` path) is the execution vehicle —
   this ruling and the consolidation are one build, not two.

## CONSEQUENCES FOR THE LIVE BUILD (routed, not adjudicated)

- **DS~Z (P1 port spec):** the firm-parameterized spine now carries a CANONICAL OUTPUT SCHEMA
  requirement per artifact type — one schema, four scopes. The account-units count and non-model
  fields enter the canonical schemas. The 02 audit's "AUM metrics soft-fail posture not acceptable"
  row composes with this: per-scope status is part of the manifest, and shape is invariant.
- **Portal note (NOT in this project's scope; flag to the wave):** the bell-curve component reads
  `account-distribution.json` today per Andrew's own words; the non-model components read their two
  files. When the folded fields land, any component still fetching the standalone extras re-points.
  Serving-tier reads are DT/portal work under its own lane — surfaced, not started.
- **The two standalone extras retire only AFTER their information is folded and verified** in the
  canonical 12 — sequence, not simultaneity. Until then they continue (they were written today by the
  live cycle; nothing stops before its replacement is proven).
- **H6 (schema pin) note:** the do-not-touch pin on `as_of_first`/`as_of_last`/`firm_id` held for the
  INFRASTRUCTURE cutover. This ruling authorizes a DELIBERATE, TESTED schema convergence as its own
  scoped act — exactly the "separately tested schema migration" doc 04 H6 anticipated. The pin is not
  violated by it; it is discharged through it.
