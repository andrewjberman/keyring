# 49F — BLACK-DIAMOND-EXCLUSIVE DEPENDENCY MAP (measured)

**Author:** 2.0.0_SA_COO · 2026-08-21 · **Status:** MEASURED-BUT-UNCERTIFIED. Characterize-not-fix,
read-only. **This is a MAP, not a plan, not a trace, and not a build authorization.**
**Commissioned by:** Andrew-direct 2026-08-21 ~17:3xZ, verbatim: *"we should map out what these tables
actually are, get light tables sorted out in the same pattern as the roles/fees table frameowrk, and
mark what these dependencies are so we can make a clean switch later"* — with the strategic why stated
in the same instruction: ***"if 49 gets off Black Diamond (which is the goal, we are trying to replace
this function for them), then these 'custom' dim tables that provide these non-schwab data points, are
going to need to be hosted by them direct."***

## 1. THE EXISTING PATTERN — and it is better than a precedent, it is a generalized framework

`a00_runner.py` already treats external-source tables as **JOIN DIMS**: read by date partition (latest
`<= asof`), vintage-stamped, and **ABSENT-NOT-SILENT**.

| | source | prefix | supplies |
|---|---|---|---|
| **JD2** | **Black Diamond** | `blackdiamond/49f/silver/dim_advisor_fee_role/` | advisor ROLES + fee splits |
| **JD1** | SmartX | `smartx/platform/silver/fact_allocation_account_map/` | model membership (date-effective) |

**THE FRAMEWORK IS ALREADY MULTI-VENDOR.** JD1 is SmartX-scoped and read CROSS-SOURCE by construction
(CTO prefix ruling 234434Z: *"absent at the schwab scope root is correct-not-defective"*). So hosting a
custom dim at a **new** source is a **SOURCE SWAP INSIDE AN EXISTING PATTERN**, not a new mechanism —
which is the single most useful fact in this document for the migration.

**ABSENCE BEHAVIOUR, verbatim** (`a00_runner.py:129`):
`WARN: join dim 2 absent <= asof -- roles will be None, unbridged=-1 (stated)`
**ROLE PROVENANCE LAW** (`a00_dim_account.py:18`): advisor roles come from JD2 facts —
*"NEVER txn-derived; unbridged accounts REPORTED, never defaulted."*

## 2. THE THREE BD-EXCLUSIVE TABLES

| # | table | read by | supplies |
|---|---|---|---|
| 1 | `blackdiamond/49f/silver/dim_advisor_fee_role/` | `a00_runner.py:51` (JD2), `d_publisher_port.py:72` | advisor roles + fee splits |
| 2 | `blackdiamond/49f/silver/dim_account_xref/` | `a01_dim_relationship.py:50` (`BD_XREF_PREFIX`) | account crosswalk / custodial tail |
| 3 | `blackdiamond/49f/silver/fact_bd_allocation/` | `bd49f_dim_portfolio_group.py:79` | BD allocation → portfolio group |

*(Also measured, OUT OF SCOPE here: the `blackdiamond/cottonwood/**` tree feeds the Cottonwood MDPF
slice builders — a different firm and a different product. Named so a later reader does not conflate
them.)*

## 3. PRESENCE + FRESHNESS, measured 2026-08-21 ~17:4xZ (s3api, UTC)

| table | newest partition | written | read |
|---|---|---|---|
| `dim_advisor_fee_role` | `date=2026-08-20` | 2026-08-21T07:06:44Z | **FRESH, daily** |
| `dim_account_xref` | `date=2026-08-20` | 2026-08-21T07:06:44Z | **FRESH, daily** |
| `fact_bd_allocation` | `date=2026-08-18` | 2026-08-19T22:46:03Z | **BEHIND — see §5** |

⛔ **THE ROLES TABLE IS PRESENT AND FRESH. THE 49F TWIN REGRESSIONS ARE THEREFORE *NOT* A MISSING
SOURCE TABLE**, and nobody should carry that inference forward. Why the twins lose roles anyway is
UNMEASURED and is exactly the field-level trace Andrew commissioned — §6.

## 4. THE DERIVED-VIEW FAN-OUT — why this map explains 2026-08-21's regressions

The `ROLES` vocabulary (`architect / implementor / consultant / additional_advisor / local_ops`)
is consumed by:

`d03_firm_fee_efficiency` · `d05_client_detail` · `d07_firm_leaderboard` · `d08_firm_ownership_map` ·
`d09_firm_timeseries_overview` · `d10_firm_cumulative_chart` · `d14_advisor_nna_canonical`

**THAT IS ESSENTIALLY THE ENTIRE SET OF KEYS THAT REGRESSED AT THE PRODUCT PLANE TODAY** (DE's
complete pass: material regressions on 9 of 10 certified keys — AUA-by-Office 100% `other`,
AUA-by-State 100% unassigned, leaderboard 163 → 146 with twenty named advisors absent, mix_periods
5 → 1). **The 9-of-10 finding and this dependency map are the same fact seen from two ends.**
Restating the readiness question in these terms: it is not "is canonical ready" in the abstract — it is
**"do the BD-sourced join dims and their derived views survive into the canonical product?"**

⚠ **NOT A CAUSAL CLAIM (Rule 22).** The fan-out is source-measured; the *mechanism* by which the twins
lose roles is a HYPOTHESIS until traced. Two candidates, neither adjudicated: the twin/publisher path
does not carry the JD2-derived fields, or the derived views are computed somewhere the join does not
reach. **This document does not choose between them.**

## 5. ONE DEPENDENCY ALREADY DEGRADED, BEFORE ANY MIGRATION

`fact_bd_allocation` sits at `date=2026-08-18`. That matches the **FRIDAY-ONLY BD snapshot cadence**
`0.6.0_AE_PartnerETL` measured independently this morning (their BDAPIMIG re-ground: allocations +
unrealized full-size landings **only on Friday as-ofs, six straight weeks**, enumerated over the full
dated history; weekday pulls return header-only 0-data-row exports that the FIX-1 guard correctly
refuses). **So one of the three custom dims already runs up to four trading days stale by Thursday**,
and that is a vendor-side condition, not a defect in our chain. Whether it matters depends on the
migration: if 49F leaves BD, the table's cadence is moot; if not, it is a live dependency.

## 6. WHAT IS NOT ESTABLISHED — the honest boundary

1. **WHY the twins lose roles** with JD2 present and fresh. Field-level trace. **The next act.**
2. **Whether these three are ALL of it.** This census keyed on the literal `blackdiamond` token. Per
   `0.7.0_AE_CloudOps`'s measurement today, **only ~11% of in-scope S3 key call sites NAME their key**
   — the rest build keys generatively — so **a token census is a FLOOR, not a denominator.** A
   constructed-key reader of a BD prefix would be invisible to this map, exactly as the platinum
   publisher was invisible to my PROVCANON enumeration.
3. **What the light tables must contain.** Field-level requirements per table — a trace output, not
   assumable from prefixes.
4. **Office.** `fact_acc.schwab_br_cd` is 100% populated with **285 distinct branch codes** against the
   legacy product's **NINE offices** — a GRAIN MISMATCH, so office is a CANDIDATE, not an answer.
   *(Contrast STATE, which IS measured available: `fact_acc.ac_st` 100% populated, 48 distinct, top
   values matching the legacy chart's own state set — so state is an UNBUILT DIM over data we already
   hold, NOT a BD-exclusive attribute. The two must not be carded together.)*

## 7. ONE DESIGN NOTE FOR THE SWITCH ITSELF

JD2's absence path warns and sets roles `None` / `unbridged=-1` — **loud in a log, and the DOWNSTREAM
consequence is what was watched all afternoon: views collapsing to `other`/`unassigned` while the
pipeline reported itself healthy.** If 49F self-hosts these tables, that absence path becomes THEIR
operational responsibility, and the failure would present as *"the warning fired in a log nobody read."*
**Design the handoff so a missing custom dim fails where a person sees it** — noting the standing
monitoring moratorium means this is a ROUTE-AND-OWNERSHIP question, not an alerting build.
