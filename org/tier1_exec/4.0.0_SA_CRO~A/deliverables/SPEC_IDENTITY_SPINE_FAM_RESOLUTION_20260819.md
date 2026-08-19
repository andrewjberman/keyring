# SPEC: THE IDENTITY SPINE -- resolving the fam dependency via portfolio-group strategy + the BD table (v1.0 DRAFT for COO decomposition)

**Commissioned:** Andrew-direct at the CRO~A terminal 2026-08-19 ~2030Z: *"we need to figure out a
solution for this 'fam' thing because COO wants a game plan. It kind of seems like this can either
be managed through portfolio_group strategy we discussed earlier, or through some amalgamation of
that and the existing BD table. I need you to draft a spec on how this could be done and issue to
COO."*
**Author:** 4.0.0_SA_CRO~A (recon -> specs). **Route:** 2.0.0_SA_COO (decompose) · 1.0.0_SA_CTO
(architecture ratify -- the a01 source change is a P2/P3-class act through their gate).
**Grounding:** every number herein was measured 2026-08-19 at this seat (deliverable citations
inline); the four Andrew parity rulings (@3c8c3f1035/@1e0ec3b079 via CTO 202318Z) are folded as law.

---

## 0. THE PROBLEM, ONE PARAGRAPH

`dim_relationship` -- the identity spine of Advisor Intelligence (who owns what account, whose book,
which household) -- is built from ONE input: Schwab's `fact_fam` file (a01_dim_relationship.py),
which Schwab stopped publishing after AsOf 2026-08-07 (endpoint-confirmed under Andrew's egress;
sole path to resumption = Schwab contact). The carry ruling ("use the most recent data") keeps us
honest but frozen: new accounts (~5/business day) enter the book invisible to the identity plane.
Meanwhile a RICHER identity source already lands DAILY and kept landing through the entire outage:
the BD allocation export (06:30Z + 08:30Z retry, `blackdiamond/49f/bronze/allocation_390224/`).
Tonight Andrew ruled the served book definition GROUP-BASED -- which makes the BD export not merely
a fallback but the SOURCE OF RECORD for the ruled definition. This spec turns that into a build.

## 1. DECISION FRAME -- pure portfolio-group vs amalgamation

**REC: the AMALGAMATION (Option B), with the probe deciding how far layer 2 retires.** Measured
basis: the BD export covers 5,277 of fam's 7,202 accounts (73.3%); the 1,925 fam-only accounts are
the Schwab-custodial tail (dominated by closed/ungrouped -- the export filters to open+grouped:
30,567 of 30,577 rows open) but NOT empty of live assets. A pure portfolio-group strategy (Option A)
silently narrows the identity universe to what BD groups -- the exact scope-is-not-the-universe
class this program keeps catching. The amalgamation costs one extra layer and loses nothing.

## 2. THE DESIGN -- a three-layer identity spine, one join key, provenance per row

```
                       JOIN SPINE (exists today, silver):
        dim_account_xref  bd_account_id <-> schwab_account_id (zfill-10)
        blackdiamond/49f/silver/dim_account_xref/ -- 6,201 rows, daily
                                  |
   LAYER 1 -- THE BOOK (BD allocation export, DAILY -- the ruled definition)
   ---------------------------------------------------------------------------
   NEW dim_portfolio_group        group grain: group_name, group_class
                                  (advisor-book | local-ops-view | division |
                                  firm-wide), derived per the transcript ruling
   NEW bridge_group_account       membership grain (account x group; 90.6% of
                                  accounts are multi-member BY DESIGN) +
                                  is_primary flag from "Primary Portfolio
                                  Group" (dim id 436) -- THE partition key
   NEW dim_account_identity_bd    account grain: Relationship ID (z-key),
                                  relationship name/SEC type, client name,
                                  registration type (36 vals), account type
                                  (15), roles x splits (Architect/Consultant/
                                  Implementor/LocalOps/Additional), open/closed,
                                  inception -- the fam superset, refreshed daily
   ---------------------------------------------------------------------------
   LAYER 2 -- THE CUSTODIAL TAIL + HOUSEHOLD SUB-GRAIN (Schwab fam, carried)
   ---------------------------------------------------------------------------
   dim_relationship (a01) v3      keeps its job at the PER-TAXPAYER household
                                  grain (fam col_6 nests INSIDE BD relationships
                                  at 96.8% -- consistent hierarchy, finer grain)
                                  + covers the 1,925-account custodial tail.
                                  Source: fam carried-as-of-2026-08-07 (honest
                                  label, the ruled carry), auto-heals on Schwab
                                  resumption (R-WATCH already reads the frontier)
   ---------------------------------------------------------------------------
   LAYER 3 -- CONDITIONAL (the THU-FRI householding probe decides)
   ---------------------------------------------------------------------------
   BD Firm Householding /         pre-registered decision table (already ruled):
   Client Account Assignment      >=90% gap coverage -> BD becomes the tail's
                                  source too; fam retires to CROSS-CHECK.
                                  30-90% -> this hybrid stands PERMANENTLY.
                                  <30% -> fam stays REQUIRED for the tail.
```

**Laws that bind the build (each already ruled or measured -- cite, don't relitigate):**
- **Book = GROUP-BASED** (Andrew 2026-08-19): served figures partition on PRIMARY group; roles are
  an attribute view. `bridge_group_account.is_primary` carries the partition; the full membership
  carries visibility.
- ⛔ **Never sum across groups** (90.6% multi-membership; measured $10.2B phantom on a ~$1.77B
  book). The bridge table makes this structural: aggregations join through `is_primary=true` unless
  a view EXPLICITLY wants membership scope.
- **Denominator subclasses printed** (Andrew ruling 2): every consumer of the spine prints
  BD-covered / fam-only / held-away / non-8-digit counts -- the Travis enumeration is the template.
- **Rule 24 grain discipline:** three new tables at three declared grains (group / account x group /
  account). No table mixes grains; dim_relationship keeps its household grain -- we ADD tables, we
  do not overload one.
- **Provenance per row** (atom 9 + one addition): each identity attribute block carries
  `identity_source` (bd-allocation | fam-carried | fam-live | bd-householding) + `source_as_of` --
  a consumer can always see which layer answered.
- **Conflict law: fields have ONE source of record each; disagreements SURFACE, never merge
  silently.** Holder name: BD Client Name is display SoR where BD covers; fam col_5 is SoR on the
  tail (92.1% token agreement measured -- disagreements beyond formatting land in a small
  reconciliation listing, not a guess). Household: fam col_6-anchor for per-taxpayer grain, BD
  Relationship ID for the client super-grouping -- BOTH kept, they nest, they are different grains.
- **PII law carried:** fam col_6 is TIN-shaped -- grouping-only, hashed anchor emitted (a01's
  existing law). BD's z-keys are synthetic and safe -- one more reason BD is the preferred display/
  join surface.
- **Bronze/silver untouched:** the export already lands raw; the new dims are GOLD builds under
  `opal-data-49financial/gold/advi/dimensions/` (the ruled home), parquet + manifests, scheduled
  in the canonical runner chain (P2's floor covers them -- NO new trigger machinery, no monitors).

## 3. WHAT THIS FIXES IMMEDIATELY (before the probe even fires)

1. **The new-account hole closes.** The carry's only real cost was accounts opened after 08-07
   being invisible. They appear in the BD export the NEXT MORNING (verified: export current to
   T-1 through the whole outage). Layer 1 makes FAM resumption a NICE-TO-HAVE for freshness rather
   than the identity plane's clock -- R stays a heal event, exactly as re-ruled.
2. **The ruled book definition gets its data.** Group-based serving cannot ship without
   dim_portfolio_group + the bridge; this spec IS the T2 build the fence-lift cleared, formalized.
3. **The rep-layer vocabulary gap closes from the BD side.** Roles x splits at account grain replace
   the unmappable fam rep-name layer (measured: no baseline-beating alignment exists).
4. **The T1 tie-out oracle gets its keys:** group-grain qt6 reads tie to our group-partitioned
   figures BY CONSTRUCTION once both use the same group definition.

## 4. SEQUENCED WORK PACKAGES (for COO's decomposition -- suggested cuts, dates R-independent)

| WP | what | owner class | depends on | acceptance-that-fails-if-wrong |
|---|---|---|---|---|
| WP-1 | silver `fact_bd_allocation` parse (dedup+dtype ONLY per Rule 17) of the daily export | DS lane | nothing (bronze lands today) | row/col counts tie to the xlsx dimension ref; re-run idempotent; Decimal dtypes per SILVER-DTYPE law |
| WP-2 | gold `dim_portfolio_group` + `bridge_group_account` (+ is_primary from dim 436) | DS lane | WP-1 | Travis reproduction: primary-partition sums NEVER double-count (his $456.8M membership view + a primary-only view both derivable; cross-group sum test FAILS LOUD); group_class enum MECE |
| WP-3 | gold `dim_account_identity_bd` (the fam-superset attributes) | DS lane | WP-1 | field census vs the 92-col header; roles+splits sum to 100% or declare; provenance cols present |
| WP-4 | a01/dim_relationship v3: consume the carry EXPLICITLY (label carried-as-of), add the tail-scope declaration, keep auto-heal on resumption | DS lane | none (independent) | build succeeds on the carried partition WITHOUT a fresh fam; label present; on a synthetic fresh partition, auto-heals |
| WP-5 | consumer re-point: ADVI book figures partition on primary-group (P4-class, CTO gate; per-key never-widen where served keys move) | DS~B/DE + CTO | WP-2/3 + CTO ratify | served leaderboard reproduces the vendor-native book number for the Travis specimen within the pre-registered bands; subclass denominators printed on every served figure |
| WP-6 | CONDITIONAL (probe result): tail source per the decision table -- BD-householding pulls productionized (new scheduled feed = new egress + P2-class acts) OR hybrid declared permanent | CTO frame -> Andrew word | AE's THU-FRI probe + my measurement | per the pre-registered table verbatim |

Nothing here gates the 49F push rows; WP-5 lands as part of P4's own machinery (pins/oracles/certs
already pre-registered). Build ladder honest: WP-1..4 are rung-2 (the export lands, the xref
exists, a01's pattern exists); zero new vendor calls; zero new triggers (the P2 floor covers the
new runners); zero monitors.

## 5. NON-GOALS / GUARDS

- Does NOT delete or stop consuming fam (dormancy is never a deletion warrant; the carry is ruled).
- Does NOT productionize the householding templates ahead of the probe + Andrew's word (per-use
  grants are not standing lifts).
- Does NOT touch cot/bd firm planes (49f-scoped throughout; NEVER#2).
- Does NOT decide the Schwab-contact question -- identity freshness stops depending on it, which is
  the point, but the contact-ready line stands for data-completeness reasons (custodial tail).
- The 868 BD-only + held-away accounts stay OUT of Schwab-derived AUA and IN the printed
  subclasses (Andrew's denominator ruling) -- this spec does not widen any served universe.

## 6. THE ONE-PARAGRAPH GAME PLAN (for COO's card)

Stand up the BD allocation export as the identity plane's daily source of record (it already lands,
it survived the outage, and Andrew ruled its group model the served book definition): three new
gold dims at clean grains, joined on the existing xref, with fam retained at its own household
grain + the custodial tail under the ruled carry. New accounts stop being invisible immediately;
the book definition ships on real data; the THU-FRI probe then decides whether BD's native
householding templates retire the fam tail too, per the already-ruled decision table. R becomes
a heal event on every axis, and no work package waits on Schwab.
