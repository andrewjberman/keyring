# Session log — `2.0.0_SA_COO` — 2026-08-12 15:48–15:56Z — HOUSEHOLD CROSSWALK: SPEC NEEDED

**archetype:** SCRIBE · **secondary_archetypes:** COORDINATE
**Written at Andrew's instruction under a pending device reboot.** Reboot state: `@aa74f90069`.
**Purpose: a spec does not exist for the household crosswalk and one is needed. Everything a spec
author requires is below, so nobody re-derives it after the reboot.**

---

# ⛔ SPEC NEEDED: HOUSEHOLD-GRAIN CROSSWALK (49F canonical plane)

## THE ONE-LINE NEED
**The canonical plane has no household-grain identity, the served product has one, and the two do not
overlap at all — so no canonical publisher can reproduce a client-labeled served surface.**

## 1. THE TWO IDENTITY SYSTEMS — both real, neither wrong
| | BD / LEGACY plane | CANONICAL plane |
|---|---|---|
| artifact | `gold/dimensions/client_dimension.parquet` | `dim_relationship` |
| concept | **HOUSEHOLDS** — a *curated product concept* | **ACCOUNT-GROUPINGS** — *derived, structural* |
| population | **201 keys** in the `d13` artifact, **113 of them MULTI-PERSON** | **4,291 relationship_ids** over 7,239 account-rows (1.69 accounts each), `a01`-anchored on min `account_id` |
| key grammar | `z…` (e.g. `z08327149`) | `rel_…` (e.g. `rel_e9236546a41b7c`) |
| label examples | "Chan, William & Shelley" · "Waldrop, Mark and Dreama" · "Smith, Craig & Kimberly" | "WILLIAM CHAN" · "WALDROP INVESTMENTS LLC" · "CRAIG M SMITH" |

## 2. ⛔ THE MEASUREMENT — why this is a MISSING ARTIFACT and not a mapping bug
**Measured by `0.4.0_DS_ClientPlatform~B` on `d13_firm_partner_analytics`, all three granularities:**
- ⛔ **ZERO KEY OVERLAP: 0 of 201.** No served client key matches **any** id in the canonical dim —
  not `account_id`, not `relationship_id`, not `master_group_id`, and **not under z-prefix or
  leading-zero normalisation.** *The served client identity is a DIFFERENT SYSTEM, not a re-keying.*
- ⛔ **STRUCTURAL PROOF, not an illustration: 113 of 201 served labels are MULTI-PERSON household
  forms, and a per-account registration name CANNOT produce "Chan, William & Shelley" — the second
  is TWO PEOPLE.** No transform bridges them.
- ⛔ **AND IT IS NOT A PERSON-PAIRING RULE EITHER:** Waldrop is a **person-pair served** vs an
  **LLC canonical** — so "join the spouses" is not the missing operation.

**DOLLAR EVIDENCE — real, and DELIBERATELY CAVEATED:** the served household consistently aggregates
MORE than the canonical relationship:
| served | canonical |
|---|---|
| Chan, William & Shelley **$75,464,904.18** | WILLIAM CHAN **$61,723,413.86** |
| Lindsey, Jessica **$36,415,063.78** | JESSICA ABELN LINDSEY TTEE **$32,653,203.51** |
| Smith, Craig & Kimberly **$25,727,221.15** | CRAIG M SMITH **$25,186,727.37** |
| Waldrop, Mark and Dreama **$40,194,499.26** | WALDROP INVESTMENTS LLC **$23,817,167.64** |
> ⚠ **DO NOT QUOTE THIS TABLE AS A MEASURED GRAIN DELTA.** It is a **measured TOTAL delta with grain
> as ONE NAMED CANDIDATE.** Three mechanisms are live — **household grain, valuation basis,
> role-tagging** — and **Travis Penfield's own advisor total also differs ($446,677,579.87 served vs
> $361,133,185.60 canonical), which a grain story cannot explain.** *The IDENTITY gap is decisively
> isolated (0/201 + multi-person labels); the DOLLAR gap is not.*

## 3. SOURCE CHAIN — where the household identity comes from (source-confirmed)
```
D_01.partner_analytics.py:1023   name_map = client_dim.set_index('relationship_id')['relationship_name']
                     :1029-1031  client_day['relationship_name'] = …map(name_map).fillna(<the id>)
                     :330,344    client_dim  <- constant CLIENT_DIMENSION
lib/s3_layout.py:38              CLIENT_DIMENSION = 'gold/dimensions/client_dimension.parquet'
lib/s3_layout.py:18              gold/client_performance.parquet = "primary AUA source (daily x relationship)"
D_04:1878                        pass-through of D_01's output — adds nothing
```
⭐ **`D_01` COMPUTES NOTHING about household identity. It READS the dimension and MAPS it.** The `z…`
key AND the household name both **ARRIVE** from `client_dimension.parquet`; the household AUA arrives
from `client_performance.parquet` at daily×relationship grain.
⚡ **AND THE TELL THAT CLOSES IT — `:1030`'s `.fillna(relationship_id.astype(str))`: THE LEGACY
PRODUCER DEGRADES TO KEY-AS-LABEL EXACTLY AS THE CANONICAL EMITTER DID.** *The canonical family's
hash-labels were never an aberration — they are the same code shape without its input. The legacy
producer handles it by HAVING the dimension.*

## 4. THE GAP IS ALREADY DOCUMENTED IN THE ESTATE — twice
- **`d04_clients_tab.py:12`** — verbatim: ***"NO crosswalk exists at household grain."***
- **`d04_clients_tab.py:91`** — the consequence: curated display names are ***"unalignable per-row
  until a household crosswalk"*** exists.
⚡ **So the need was known and written down inside a producer's own docstring before anyone measured
it. The measurement corroborates the docstring independently.**

## 5. ⛔ THE ADJACENT ARTIFACT THAT IS **NOT** THE ANSWER — read this before wiring anything
**`a06_dim_identity_crosswalk`** (`runners_49f/` **and** a `runners_inf/` sibling — a two-instance
pattern) maps `smartx_allocation_uuid -> schwab_account_number -> account_id`:
**a VENDOR-INTEGRATION identity map at ALLOCATION grain. Commissioned by
`SPEC_49F_GROUP_A_DIMENSIONS_20260811.md:46` row A_06. Built to spec, LIVE INPUT
(`smartx/platform/silver/fact_allocation_account_map`), and ZERO READERS anywhere in the estate**
(`comp-find`: HEAD=7 = two implementations and nothing else; CONFIG=8 + DOC=4 are only things that
DESCRIBE it). **NEVER-LAUNCHED, not superseded — nothing else does its job.**
> ⛔ **DO NOT REPOINT A_06 AT THE HOUSEHOLD GAP.** *"A grain mismatch is not a wiring problem, and
> forcing it would be the worse defect"* (`0.4.0_DS_ClientPlatform`). **Allocation grain is not
> household grain.**
> ⚡ **AND THE TRAP IS NAMED: the estate holds a crosswalk NOBODY READS beside a crosswalk-shaped HOLE
> NOBODY FILLED, at DIFFERENT GRAINS — so a NAME-BASED audit would pair them and be wrong.** *A
> Rule-24(ii) live specimen: two artifacts, one noun, two grains.*

## 6. ⛔ THE FIRST QUESTION ANY SPEC MUST ANSWER — it decides ENGINEERING vs PROCUREMENT
**WHO PRODUCES `gold/dimensions/client_dimension.parquet`, and is the household grouping DERIVED
there, or does it ARRIVE from Black Diamond upstream of it?**
⚡ **DS~B traced TO the artifact, not PAST it, and said so.** **That last hop decides whether a
canonical household dimension is BUILDABLE FROM DATA WE HOLD or REQUIRES A VENDOR FEED — which is the
difference between an engineering task and a procurement one.** ⛔ **Nothing else in the spec can be
sized until this is read. It is one read.**

## 7. THE SOVEREIGN QUESTION THAT SITS ABOVE THE SPEC — ANDREW's
⛔ **The question is NOT "how do we map these." It is WHICH IDENTITY SYSTEM IS THE PRODUCT.**
- **HOUSEHOLDS are the product** -> the canonical plane needs a household dimension it does not have,
  and the spec below is the build.
- **RELATIONSHIPS are the product** -> **the served display changes for EVERY client-labeled family**,
  which is a visible product change requiring his word.
⚡ **This is Andrew's because the identity ARRIVES FROM UPSTREAM — it is a product-semantics call, not
an architecture one.** *Recorded, not asked under a reboot; it survives in `REBOOT_STATE_20260812T1548Z.md`.*

## 8. WHAT THE MISSING SPEC BLOCKS RIGHT NOW
- ⛔ **P4 LEG A** (`d13_firm_partner_analytics`, 3 served keys: `partner_analytics_{quarterly,monthly,annual}`)
  is **HELD** on this plus a 9-vs-15 population item.
- ⚠ **`d04` / `d05` / `d14` inherit the same gap — INFERRED BY CONSTRUCTION, only `d13` MEASURED.**
  *Label the inference; do not promote it to a measurement.*
- **It does NOT block P3** (complete, `@aa72ab5bc5`) **or the dim act** (`@4c1219fc34`/`@0205eef992`).

## 9. SUGGESTED SPEC SHAPE — a starting point, not a decision
1. **Read §6 first.** Derived-here vs vendor-supplied changes everything downstream.
2. **Define the grain explicitly and prove it MECE + same-grain** (Rule 24). ⚠ **Do NOT assume
   "relationship" and "household" are the same coarser-than-account concept — DS~B explicitly refused
   that identification, and their measurement does not show it.**
3. **State the direction of the bridge.** Household->relationship is many-to-one and derivable if the
   membership exists; relationship->household is not invertible.
4. **Name the ORACLE for correctness.** ⛔ Not a shape check — a `SHAPE-FROZEN` PASS is **blind to
   row-set identity and label semantics** (measured today: a shape-freeze passed a bidirectional
   entity-set replacement and a names-to-hashes regression). **The oracle is entity-set + label
   agreement against the served artifact.**
5. **One producer per key** (CTO's four-part P4 close bar), **canonical grammar**, **scheduled
   producer, no session-local input in the chain, and a declared consumer reading the serving path.**

---

## SESSION LOG — the window this reference was written in

**Dispatches: 6** (DS~B ×3, MSTR ×2, base ×1). **Commits: 2** — `@aa74f90069` reboot state,
this file. **Inbox: 0 unread.**

**WHAT HAPPENED:** Andrew ordered a device reboot (~1520Z, via MSTR). I persisted everything that
existed only in session context, drove my lanes' close-out, and corrected my own DONE report — it
covered **committed**, and his condition says **committed/pushed**, with **`CLOUD` 36 commits ahead of
`origin/CLOUD`.** The push is the integrator's and is the live gate.

**⚠ MY OWN OPEN ITEM, stated not buried:** I never placed the **comp-estate regen** execution after
CTO raised its priority (the codebase extractor is now refactor-gating; until regen, `comp-estate`
serves **snapshot names as fact**, and a large refactor leans hardest on names; contract approved
`@801e5e92a5`). **In the reboot state's clocked-items table, unassigned.**

**⚠ STILL OUTSTANDING AT REBOOT:** DT's **reachability determination** on a fourth `fee_earning_aua`
implementation that **inverted** — serving `$0.00` fee-earning with the entire book as non-fee beside
`avg_fee_bps_earned 114.5`. Base ground it further: **`:737` applies a silent `.get(…, 0.0)` to a
REQUIRED field** and `is_fee_earning` is **absent from today's billing partition after being present
every day 08-01..08-11** (denominator 1,598 partitions) — **while the DEPLOYED builder DOES derive the
column.** ⛔ **Root cause OPEN, four candidates unverified, reachability NOT claimed. My ruling
recorded not dispatched: the gate should REFUSE rather than let the default invent a zero. And DO NOT
back-fill the column — it erases the evidence of which producer dropped it.**

**COMPILER TOOLS:** `comp-find` (the A_06 reader census, 19 hits with bands printed) · `comp-freshness`
(the 05:26Z served-key age that exposed the live legacy producer) · raw `git log`/`status --porcelain`
as the **verify-by-hash** control on this file. ⛔ **Trap live during this sweep (AE-measured):
`safe-commit` does NOT stage a brand-new untracked file and fails at the TAIL of its output — both
commits in this window used explicit `git add` first and were verified by hash.**
