# BRIEF — VINTAGE IS NOT ONE FIELD: four KINDS, four DURABILITIES, and why neither can be classified mechanically

**From:** `3.0.0_SA_CVO~Z` · **To:** Andrew, `1.0.0_SA_CTO~Z` (PRD owner) · **2026-08-12**
**Origin:** Andrew-direct request at the CVO~Z terminal, following the W4b semantic pass.
**Status:** FINDINGS + a design constraint for the W5 catalog. **No acts taken; nothing stripped.**

---

## 0. THE ONE-PARAGRAPH VERSION

Every artifact on a portal page answers *"when is this from?"* — and this session established that
**the question has four different answers that co-occur rather than compete**, and that **the dates
written into a catalog split into four durabilities that must not be treated alike.** The practical
consequence is a design constraint: **a catalog whose vintage field is a single dated string is lossy
by construction, and a lift that mechanically strips literal dates destroys durable content.**
**Three mechanical classifiers were built to sort these. All three failed**, which is itself the
finding — the discriminator is semantic, not lexical.

---

## 1. FOUR KINDS OF VINTAGE — the axis is not a partition

Found by authoring semantic cells across `/advisor-intelligence` and the earlier wave units.

| kind | measured example | answers |
|---|---|---|
| **BUSINESS AS-OF** | `data_as_of: 2026-08-06` | what date the *world* is described as of |
| **GENERATION TIME** | `generated_at: 2026-08-12T05:26:46Z` | when the *file* was built |
| **PERIOD BOUNDARY** | `y1: 2025-12-31`; quarter closes | what the *reporting frame* is cut at |
| **CONTRACT VERSION** | `partners-api-v1.15.6` | which *shape* the payload obeys |

**They CO-OCCUR.** `partner_analytics_annual` carries the first three simultaneously and they are
mutually irreducible: `data_as_of` 2026-08-06, `generated_at` 2026-08-12T05:04:19Z, and period
boundaries at 2026-08-06 / 2025-12-31 / 2024-12-31 / 2023-12-31.

**The fourth kind is the one that breaks a naive schema.** It surfaced on `clients-tab`, which is a
**Lambda-served route, not a stored object** — no `data_as_of`, no `generated_at`, because there is no
file. Its nearest vintage is an **API contract version** (`portal/src/pages/AdvisorIntelligence/_shared/types.ts:980`).
**A catalog whose vintage field admits only dates cannot hold it at all.**

### 1a. This retired a constraint I had authored

A prior lift constraint budgeted **"≥8 vintage variants."** That was wrong in the way counts usually
are: **it put a number on an axis that is not a partition.** Measured: 20 of 28 cells were
multi-valued across 14 combinations, with manifest-or-footer and artifact-field **co-occurring rather
than competing**. Eight slots is as wrong as three. The replacement is a property, not a bigger
number:

> **THE CATALOG'S VINTAGE FIELD IS MULTI-VALUED OR IT IS LOSSY BY CONSTRUCTION.**

### 1b. And it is multi-NAMED as well as multi-valued

`fee_efficiency` breaks the page convention three ways at once and is the only artifact of five that
does: its vintage key is **`as_of_date`**, not `data_as_of`; it carries **no `generated_at`** at all;
and it carries **no `firm_id`**, so the artifact does not say which firm it describes — only the S3
prefix does.

> **A catalog binding one key name silently loses that row's vintage — and a silently-lost vintage
> reads as NO FRESHNESS rather than as a spelling difference.** The failure mode is worse than the
> loss, because it presents as a finding about the data.

*Two timestamp FORMATS also coexist in one prefix: microsecond `+00:00` (`header_metrics`,
`timeseries_chart`) vs `Z`-suffixed (five others).*

---

## 2. FOUR DURABILITIES — and the near-miss that makes this brief worth writing

`1.0.0_SA_CTO~Z`'s review pass found that many semantic cells embed a **literal date**, and ruled that
the catalog lift should refuse literal dates: they are true at authoring vintage and go stale as the
data advances. **The diagnosis is correct.** The measurement underneath it is where it needs
refining.

**Census over the author's full corpus: 334 distinct MEASURED semantic cells · 73 embed a date · 123
date occurrences.**

| durability | n | example | fate under a blanket strip |
|---|---|---|---|
| **EPHEMERAL** — advances | 31 (25%) | `data_as_of = '2026-08-10'` (live reads `2026-08-11`) | **correctly removed** |
| **PERMANENT-EVENT** — a dated fact | 17 (14%) | `FROZEN 2026-04-07` | ⛔ **destroyed** |
| **PERMANENT-STRUCTURAL** — period close | 12 (10%) | `2020-03-31` | ⛔ **destroyed** |
| **PERMANENT-STRUCTURAL** — anchor | 5 (4%) | `as_of_first (2024-11-01) bounds the series` | ⛔ **destroyed** |
| **UNRESOLVED by the classifier** | 58 (47%) | — | unknown |

> ⛔ **THE NEAR-MISS: `FROZEN 2026-04-07` IS NOT A STALE VINTAGE — IT IS THE FINDING.** It is the date
> a 720-key news family stopped being written. A blanket literal-date strip deletes the single most
> load-bearing fact in that unit, in the name of freshness hygiene. Q1 2020 will always end
> 2020-03-31; a series' start bound never moves.

**The defect is CONFLATION, not staleness:** a cell mixes the vintage **MECHANISM** (which field, what
grain, what source — durable) with the vintage **VALUE** (the date that day — ephemeral by
construction). **The rule is not "no literal dates." It is "no literal CURRENT-VINTAGE values," and
the discriminator is whether the date describes FRESHNESS or an EVENT.**

---

## 3. ⚠ THREE MECHANICAL CLASSIFIERS WERE BUILT TO SORT THIS. ALL THREE FAILED.

**This is the part that determines the recommendation.**

| classifier | failure |
|---|---|
| durability classifier | **could not resolve 47%**, and tagged `cma_excel.data_as_of = '2026-12-31'` as a *permanent period close* purely because `12-31` matches a quarter-end pattern — **it is the ephemeral class exactly** |
| grain tell-regex (sibling census) | 7 matches, **2 real** — key names produced *every* false positive and detected *neither* true case; the discriminator was the artifact's own `description` field |
| accessor-name tell (sibling census) | **fails in both directions** — misses a row with no tell, over-fires on a row that carries one |

**And the author's own summary line was wrong before correction:** it reported *"75% are not
ephemeral"* by counting all 58 unresolved cases as durable. **Defensible claim: ≥28% confirmed
durable, 47% unresolved. Mechanism confirmed; magnitude not.**

> **Four over-broad predicates in one session, each returning a clean, well-formed, wrong answer.
> A date's durability is a semantic property. It is not recoverable from the string.**

---

## 4. THE DESIGN CONSTRAINT (what this brief is for)

1. **The vintage field is MULTI-VALUED and MULTI-NAMED.** One dated string per artifact is lossy
   before the catalog ships. It must hold at least: business as-of · generation time · period
   boundary · contract version — and tolerate a row that has none of the first three.
2. **CARRY EACH DATE WITH A DECLARED KIND. REFUSE LOUDLY ON AN UNDECLARED ONE.** Same posture as the
   verdict normalizer and the supersedes resolution: **raise on an unrecognised shape, never
   default.**
3. **DO NOT AUTOMATE THE STRIP.** No mechanical predicate resolved the durability question, and the
   one that tried mis-classified a `data_as_of` as a period close. **A lift that silently drops what
   it cannot classify loses the frozen date** — and the entire reason this program exists is that a
   pipeline stopped for three months and nobody noticed.
4. **A vintage claim inherits the depth of the check that produced it.** A cell reading *"there is no
   `generated_at`"* was FALSE — `metadata.generated_at` existed one level down. **Its own evidence
   field said "top-level keys," which was accurate; the claim generalised past its own stated
   bound.** Two seats made that identical error on the same cell an hour apart.

---

## 5. WHAT THIS BRIEF DOES NOT CLAIM

- **No cells were stripped or edited on the strength of this.** It is a measurement under an existing
  ruling, not a change to it.
- **The magnitudes are soft.** 47% of occurrences are unresolved by the instrument that produced the
  split; only the ≥28%-durable floor and the 25%-ephemeral figure are defensible.
- **It is scoped to firm `bd` and to this author's corpus.** No cross-firm reads.
- **The adjacent axis is someone else's:** `1.0.0_SA_CTO~Z` landed a vintage-**provenance** rule the
  same day — *a field read from a derived object carries the derivation's provenance, not the
  variable's name* (off `0.5.0_AE_OpalETL~Z` finding two vintage sources that were `useMemo`
  derivations). That is *where a vintage came from*, not *what kind it is*. The two compose; neither
  subsumes the other.

— `3.0.0_SA_CVO~Z`
