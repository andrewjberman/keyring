# Three items, an oracle of mine that could not work, and the provenance chain closing — `3.0.0_SA_CVO~Z`

**archetype:** VALIDATE
**Seat:** `3.0.0_SA_CVO~Z` (site Z) · **This entry:** ~02:20Z → ~04:10Z
**Predecessors:** `..._2340-0055Z_...` @`8bf081ef8f` · `..._0055-0220Z_...`

---

## Objective

Hold the channel through Andrew's *"just fix it now"* window, where five seats converged on one
field and four rulings were withdrawn in forty minutes.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `jsonschema` | VALID on every append, 11 this window | 39 items, ids contiguous 1..39 |
| **execution** | 6 predicates run rather than read | Again the highest-yield instrument — the marker test, the universe expression, the tier boundary |
| `aws s3api` | full-history censuses, token-walked | 41 bronze files · 73 silver partitions · every characteristics artifact |
| `safe-commit.sh` | 11 commits, `-F` | risk-reflex CLEAN each |

---

## Work Completed

### 1. Z-S37 — the semantic signal exists, and silver deletes it
Pathfinder's bronze carries **`MoneyMarketFlag`**; silver's 17 columns don't. **Rule 17 violation** —
*"NEVER drop bronze columns."* Four hours of substring reasoning over a property the issuer hands us.
⛔ **And the deciding asymmetry:** TrueShares' bronze has no such column, so a flag-keyed rule covers
FXFXX and **structurally cannot** cover SALXX. Two mechanisms, and any single-rule design silently
covers one fund family *while presenting as complete*.

### 2. Z-S39 — a holding enriched with a different company's data
`universe = [f"{t} US Equity" ...]` suffixes **every** ticker regardless of listing. `MER` returns
**MERRILL LYNCH & CO INC** (domicile US) for the issuer's **Manila Electric**; `ICT` returns nothing.
Both in **IDVZ, the international fund.**

> ICT fails loud-ish. **MER fails silent and positive** — and it is the worst of tonight's three
> fabricated-observation doors because **nothing in the artifact disagrees with itself.**

It also **retroactively corrected two of my own reads**: MER was in my no-GICS census and CTO~Z's six,
and we both called it an unmapped line. **It is the wrong line.**

### 3. The provenance chain closed
AE~Z pinned `:1375` — silver names the partition after `run_date` while the rows carry `data_as_of`.
Joined to Z-S29 (gold stamps the filename), the chain reads end to end:

> **The `data_as_of` on the page is the ingestion run date, and has never at any hop been a
> provider's assertion.** AE~Z found the upstream half; Z-S29 was the downstream half; **the same
> defect measured from opposite ends.**

Exercised proof: partition `2026-08-22.parquet` contains rows dated **2026-08-24**.

### 4. Testing designs before the keystroke
DS~Z published a design before typing it. **41-file census: 164 flagged rows, exactly two distinct
tickers ever, 82/82** — a standing structure of the feed, not a sample. And it endorsed their choice
of the *enumerated* sentinel set over CUSIP-validity for a reason they hadn't stated: **the two tests
agree on 164/164 today and fail in opposite directions.**

---

## ⛔ Errors of mine

**I published an oracle that cannot work.** I told five seats `alloc_cash` had two "numerically
disjoint" outcomes. **A third state — an empty book — produces the same reading, and it is the state
the system has been in all night.** A reader would have reported Z-S35 confirmed on two books
containing nothing. Corrected with a guard.

> **I built a discriminator, checked its two *named* outcomes differed, and never enumerated the
> state space** — the exact corollary I had applied correctly to `is_cash_inferred` *in the same
> message*.

**I over-claimed a blast radius by a tier.** `:671` exports to *gold parquet*, not to the served
JSON — COO~Z measured the boundary I'd called invisible.

**And my first attempt at that measurement failed:** I read an 833-byte manifest and got
`is_cash 0 · asset_class 0 · sub_asset_class 0` — **all four controls zero.** The failed output is
identical to the true one on the field alone.

**The third misattribution of the night was mine**, by a bare "your" eight lines below the serial —
the mechanism my own memory file names by title.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Declined the two-intents credit; filed Z-S38 under DS~Z | 821-message census; their msg predates the ratification by 84s. |
| Reported RTX as **my own false positive** | String similarity can't tell a rename from a mis-join; "3 mismatches" would over-count by 50%. |
| Trimmed only **my own** MEMORY.md lines, then stopped 54 B short | The file being over is not a reason to do the thing that made it dangerous. |
| Affirmed AE~Z's function-level limb against "strengthening" | The rule is layer-matching, not artifact-preference. |

---

## Current State

**39 items · ids contiguous · 0 ARMED without an owner.**
**BLOCKING+ARMED:** Z-S16, Z-S22, Z-S31, Z-S33, Z-S34, Z-S35, Z-S37, Z-S39.
⛔ **`bbg/2026-08-24/` still absent. DIVZ/IDVZ are shells — which is why Z-S35 is currently
UNMEASURABLE-BECAUSE-HIDDEN rather than open.**

---

## Next Steps

1. **~11:00Z** — did `bbg/2026-08-24/` land. One question; the ADR half is discharged.
2. **13:00Z** — TO-5 AC7, first scheduled gold fire. Invocation record, not a report.
3. **Z-S35 oracle, WITH ITS GUARD:** meaningful only if `DIVZ.holdings > 0 AND IDVZ.holdings > 0`.
   Then `alloc_cash ≈ 0.58 / 0.89` correct, `≈ 0.00` fired. **Guard fails → report the guard, not the
   number.** Reference: PFDE 0.36, PFOE 2.35. ⛔ **Never `is_cash_inferred` — 0 in both worlds.**
4. **Watch for the ordered pair:** the partition fix makes the books render *and* makes SALXX visible
   as equity in the same instant. **Partition-alone ships four full books with a wrong split,
   arriving looking like success.**
