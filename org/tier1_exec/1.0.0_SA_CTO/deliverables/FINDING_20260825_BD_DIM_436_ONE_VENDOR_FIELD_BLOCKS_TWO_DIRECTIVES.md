# FINDING -- one BD template field blocks the advisor level of D3 AND the advisor spine leg of ADVI_INSURE

**Author:** `1.0.0_SA_CTO`. **2026-08-25 ~13:05Z.** **Class:** upstream vendor gap, source-confirmed.
**Routed to CTO by:** `2.0.0_SA_COO` @70463, who explicitly declined to propose the remedy
("it touches a partner integration and is your ground").
**Status:** RESERVED card at Andrew -- a vendor ask is his, not an exec act.

## THE CONVERGENCE IS THE FINDING

Two freshly-seated lanes hit the same wall from two different projects **within twenty minutes of
each other, and neither knew the other had**:

| lane | project | what they hit |
|---|---|---|
| `0.4.0_DS_ClientPlatform~K` | `D3_MODELOVERLAY` | `is_primary` NULL for **29,907 of 29,907** rows (100.00%), one partition, denominator 1 |
| `0.4.0_DS_ClientPlatform~J` | `ADVI_INSURE` | **no advisor id column anywhere** -- 0 of 95 across `dim_account` / `dim_relationship` / JD2 |

**One root: `BD dim 436 (Primary Portfolio Group) is not selected by template 390224`.**

## SOURCE-CONFIRMED -- the runner declares its own gap

`data/assets/scripts/gold/runners_49f/bd49f_dim_portfolio_group.py` @HEAD:

```
:21  The ruled basis names `Primary Portfolio Group` (BD dimension id 436) as THE partition key.
:22  IT IS NOT IN THE DATA. Measured on the landed 2026-08-18 export, all 92 vendor columns:
:23      columns containing "primary"   : 0
:24      columns containing "group"     : 2   (Portfolio Group, Portfolio Group Market Value)
:25      POSITIVE CONTROL "portfolio"   : 8   -> the matcher discriminates; the zero is a true absence.
:26  Persisted BD template 390224 does not select dim 436 (its own sidecar level census reads
:27  "Portfolio Group": 2). Silver is NOT at fault -- Rule 17 preserved everything the vendor sent;
:28  preservation is not provision. The gap is UPSTREAM at the template's dimension selection and is
:29  fixable only vendor-side (add dim 436, re-pull).
:191 bridge["is_primary_status"] = "ABSENT-UPSTREAM: BD dim 436 not selected by template 390224"
:224 dim["partition_key_status"] = "MEMBERSHIP-ONLY: is_primary absent upstream (BD dim 436)"
:248 "BD dim 436 -- cannot-answer, never answers-wrongly."
```

**The code carries its own positive control** (`"portfolio"` = 8 while `"primary"` = 0), so the
zero is a measured absence and not a silent matcher failure. **This is not a new discovery; it is
a previously-recorded gap whose BLAST RADIUS was not known until today.**

## ⛔ WHY THE ABSENT LEVEL IS THE SAFE STATE

COO's ruling, and it is the half that must not be lost:

> **DO NOT SUM TO ADVISOR LEVEL WITHOUT `is_primary`.** 5,579 of 6,155 accounts (**90.6%**) sit in
> 2+ portfolio groups -- mean **4.86**, max **13**. **An advisor sum counts each account ~5 times.**

**That is the $10.2B-vs-$1B hazard, and it produces a NUMBER, not an error.** A plausible wrong
total is worse than a missing level. **The absent level is the SAFE state; a built one would be
the incident.** `~K`'s 90.6% reproduces the PRD's own run #13 figure exactly -- an independent
confirmation of the PRD's measurement.

**Both dims publish their own limitation in a status field.** That behaviour is why two lanes
found this in minutes rather than at a reconciliation. **It is to be preserved, never routed around.**

## THE FALSIFICATION ATTEMPT THAT FAILED (and so strengthens it)

COO tried to break `~J`'s half rather than accept it. `~J`'s census matched `*advisor*_id` -- a
name pattern, which is the supplied-frame class. COO re-ran it over **all 44 JD2 columns** with a
deliberately wider net (`advis|rep|producer|_fa|agent|role|person|emp|owner|id$`). Result: the
only advisor-ish columns are `additional_advisor` (a **STRING**), its split pct, and its source.
**There is no advisor identifier under any name. The finding survives a wider frame than its
author used.**

**And the ruled consequence:** the advisor leg is declared `NOT-DERIVABLE-UPSTREAM` and is **NOT
joined on a name string** -- a name-string join across a 160,091-row dim is a silent-collision
generator. **An honest missing leg beats a leg that is right most of the time.**

## WHAT IS BLOCKED, PRECISELY

| blocked | not blocked |
|---|---|
| D3 R1 advisor level (**1 of 4** levels) | account · relationship-household-client · firm -- **3 of 4 DELIVER** |
| ADVI_INSURE advisor spine leg | account · relationship · firm legs -- **3 of 4 DELIVER** |

**Neither lane is blocked overall. One level and one leg are.** Both proceed on the rest.

## THE ASK (RESERVED -- Andrew's, not an exec act)

**Add BD dimension 436 (Primary Portfolio Group) to template 390224 and re-pull.**

It is a vendor-side template configuration change at Black Diamond, **fixable by no code in this
estate and by neither lane.** I am not proposing an internal workaround, because every candidate
workaround is a heuristic partition key (bare-advisor-name vs "- Local Ops" vs division) which
would be **our reading of vendor intent presented as vendor fact** -- exactly what the runner
already refuses at `:31`.

**Why it is worth raising as a vendor item rather than absorbing twice:** two independent
directives are now blocked on one upstream selection. Absorbed separately, each looks like a
scope trim; named together, it is a single request with a single owner.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find -i 'dim 436'` | estate-wide, case-insensitive per Rule 21 | 71 hits / 26,531 files; HEAD band names the runner |
| `comp-find -i 'is_primary absent upstream'` | the declared string | 2 hits -- 1 SURFACED (source), 1 DOC (CVO investigation) |
| `sed` at `bd49f_dim_portfolio_group.py:20-32,186-196,244-250` | the declaration read at source | the vendor-side attribution, in the producer's own words |
| positive control `comp-find -i 'MEMBERSHIP-ONLY'` | the matcher | fires across unrelated files -- the 2-hit result above is discrimination, not a dead pattern |

**What failed:** nothing at this seat on this item. **Gap found:** the blast radius of a
*known, well-declared* upstream gap was invisible until two projects collided on it -- **a
declared limitation is discoverable per-project and nothing aggregates it across directives.**
