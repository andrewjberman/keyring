# ANDREW-DIRECT 2026-08-12 (CRO terminal) — CRO into ALL EXEC-coded groups + the ontology ruling set

**Recorded by:** `4.0.0_SA_CRO` · **Channel:** CRO terminal, direct · **Date:** 2026-08-12
**Status:** RECORDED + BROADCAST same turn (org/XXX.md Andrew-direct law). **The grant itself is NOT
self-landed — SoD; routed to a grantor.**

---

## 1. THE LANE RULING — VERBATIM

> **"furthermore CRO needs to be added to any and all EXEC-coded groups."**

Preceded in the same message by: **"Agreed with all of these recs"** (the ontology rec set, §3 below).

### ⛔ SoD — why this record exists instead of a commit to `.owned-paths.yaml`

The CRO is the **GRANTEE**. Standing Andrew rule, carried on `.owned-paths.yaml`'s own lane:
*"grantor — grantee does not commit its own grant."* Charter §"Hard boundaries": **"Do not
self-grant."**

**AND THE MECHANISM DOES NOT STOP ME — ONLY THE RULE DOES.** Exercised this session with a
discriminating negative control (`.tools/owned-paths-validate.py` `check_agent`, config loaded from
`.owned-paths.yaml`):

| serial | path | result |
|---|---|---|
| `4.0.0_SA_CRO` | `.owned-paths.yaml` | **True** — I can mechanically write my own grant |
| `4.0.0_SA_CRO` | `infra/system/ontology/SYSTEM_DEFINITIONS.yaml` | **True** |
| `4.0.0_SA_CRO` | `org/projects/REGISTRY.md` | True (the declared-scope surface) |
| `4.0.0_SA_CRO` | `org/tier0/ledger/LD-9999.md` | **False** ← negative control FIRES |

The negative control reproducing a real refusal is what makes the True values evidence rather than an
undiscriminating harness. **A grant I can land is exactly the one I must not land.**

## 2. MEASURED SCOPE — 9 groups missing, 3 already held

Enumerated from `.owned-paths.yaml` by parsing group blocks (57 lanes, 241 paths). **This is an
enumeration for the grantor, NOT an adjudication of what "EXEC-coded" means** — where the boundary is
ambiguous it is named as ambiguous, per surface-don't-adjudicate.

**ALREADY HELD (3):** `BASE_EXEC` · `ANY_EXEC` · `ANY_EXEC_OR_AE`

**MISSING — CRO absent (9):**

| group | line | members |
|---|---|---|
| `TIER0_EXEC` | 441 | 3 (MSTR, CTO, COO) |
| `POD1_OR_EXEC` | 493 | 12 |
| `POD2_OR_EXEC` | 509 | 8 |
| `POD3_OR_EXEC` | 521 | 7 |
| `POD4_OR_EXEC` | 532 | 24 |
| `SHARED_OPAL_ETL_OR_EXEC` | 560 | 6 |
| `ANY_POD_OR_EXEC` | 570 | 36 |
| `SHARED_PARTNER_ETL_OR_EXEC` | 611 | 10 |
| `SHARED_CLOUD_OPS_OR_EXEC` | 625 | 9 |

**Selection rule used:** group name contains `EXEC`. Stated so the grantor can widen or narrow it
against Andrew's words rather than inheriting my filter silently.

⚠ **NAMED AMBIGUITY, not resolved here:** `TIER0_EXEC` is a **Tier-0** group (MSTR/CTO/COO). It
matches "EXEC-coded" on its name, and Andrew said *any and all*. It is listed because his words cover
it; whether Tier-0 membership was intended is **his call or the grantor's, not mine.** Adjacent
governance groups that are exec-ish but NOT `EXEC`-named — `ANY_CTO`, `TIER0_LAW`, `TIER0_RATIFY`,
`GOVERNANCE_AUDIT`, `WS_CONTRACT_AUTHORS` — are **deliberately excluded from this list** and flagged
for a ruling rather than swept in.

## 3. ⛔ A PROSE SCOPE THIS RULING SUPERSEDES — and it must be edited in the same act

`.owned-paths.yaml:670` carries, on the CRO's `ANY_EXEC_OR_AE` line:

> `# Andrew-direct 2026-07-22 "You can register projects yes." -> SCOPED TO PROJECT REGISTRATION
> (org/projects/REGISTRY.md + org/projects/*.json). The CRO explicitly did NOT claim the lane's other
> surfaces (hook-config etc.) and its membership must NOT be read as blanket. LD-0331.`

**That is a scope declared in PROSE over a mechanism that does not enforce it** — the gate is
enumeration-based, so the comment narrows nothing and `check_agent` returns True across the whole
lane (measured above). Andrew's 2026-08-12 ruling **supersedes that narrowing**. The grantor must
update or strike that comment in the same commit; leaving it standing preserves a record that
contradicts both the mechanism and the live ruling.

*(The sibling comment two lines up — the `1.0.0_SA_CTO~C` entry — records this identical trap from the
other direction and is emphatic about it: "**DO NOT CITE IT AS EVIDENCE THAT ENUMERATION WAS
REQUIRED** … I landed it on the inference '~C is not enumerated, therefore BLOCKED' and **NEVER
EXERCISED THE GATE**." That is why this record exercises rather than infers.)*

## 4. CORRECTION OF MY OWN PRIOR STATEMENT — stated, not quietly fixed

Earlier this same session I told Andrew that CRO was **excluded** from `ANY_EXEC_OR_AE` and therefore
**could not** land `infra/system/**`, and proposed routing the registry rewrite to CTO/COO/CVO.
**That was WRONG.** My check was an `awk` range that began matching at a *description mention* of
`ANY_EXEC_OR_AE` inside the `BASE_EXEC` block and concluded "not in group" before ever reaching the
real group definition at line 664. The stale LD-0331 note in that description made the wrong answer
read as corroborated.

**A retrieval whose frame is wrong returns a confident, well-formed, wrong answer** — the class the
estate has hit five times today across three seats. The fix that caught it was not care: it was
running the gate with a negative control.

## 5. THE ONTOLOGY RULINGS — "Agreed with all of these recs"

Ratified in the same message, for execution:

1. **`Substrate` is the real "estate"; `Estate` is just the collective substrate.** Resolves the
   capital-E/lowercase-e collision: substrate = the unit, Estate = the set of them. The 2026-07-20
   `estate`-as-partition-axis name is retired by this; `Estate`-as-totality is untouched.
2. **`Territory` RETIRED** — covered by `Substrate`. (It was `substrate × deploy-state` flattened onto
   one axis — a Rule 24(ii) two-grains violation, and the evidence the deploy axis existed unnamed.)
3. **`Substrate_Side` DEMOTED** from an axis to a reporting rule: estate-wide denominators are
   reported per-substrate, never pooled.
4. **`Deployed`/`Undeployed` to be minted as a generalized axis** covering local vs remote
   codebase/portal work — Andrew-direct: *"desired/applied is specific language for terraform, i think
   there needs to be a generalized undeployed/deployed language."* Bindings: codebase → local vs
   **CLOUD**; portal → local vs **PROD**. It is a **sibling** to the ratified `Plane`, not a re-coin:
   `Plane` types an **assertion** (is this claim about config or live state — it is the type_tuple
   slot the registration invariant validates tool declarations against), whereas this types a **code
   artifact**. Different subjects, no collision.
5. **`Layer` MINTED** as the tracking-grain axis — **`resource | contents`**, plus `null` for C2/C3
   aggregates (same precedent as `semctl`'s drop, where aggregates take a null and that null is a
   declared prohibition, not a gap).
   ⛔ **SEQUENCING IS LOAD-BEARING:** `layer` is TODAY the live Iceberg column holding *substrate*
   values (80 occurrences in `infra/aws/globgrph/derive_runner.py`, incl. `"layer": "semctl"` at
   `:1761` — a value Andrew's own 07-20 ruling ordered DROPPED). Minting `Layer = resource|contents`
   before that column is renamed puts two meanings on one field name, one of them materialized.
   **The `layer` → `substrate` rename lands FIRST**, which also discharges the half-landed 07-20
   migration (80 `layer` vs 27 `estate` in the producer, against a spec that said "must land
   together / do not half-land").
6. **Registry naming convention — `Capitalized_Snake_Case`**, standing rule for all definitions.
   48 of 65 keys are straight renames. Agreed sub-rules: **rung/rail ids EXEMPT** (`C0`–`C4`, `C3.i`,
   `C3.ii`, `D1`–`D3` — strict snake would mangle `C3.i`); **materialized enum values renamed as TERM
   KEYS ONLY** with an explicit line that the on-disk form (`api-serving`, `ui-dataflow`) is
   unchanged; **`UNDECLARED` left as-is** (it is a written value, not a concept).

### Consumers that move with the rename (blast radius, measured)

- `rcg/bin/lexicon.py` — generates a **dashed variant of every term key**; must land in the same act.
- `org/modules/graph/opal_estate_infrastructure.py` — fuzzy term lookup; tolerant.
- ⚠ `org/tier1_exec/3.0.0_SA_CVO/deliverables/kimi_subdivision_harness/stage1_sides.py` — hardcodes
  `substrate_side` **pinned at v1.8 with the stale pre-1.9 membership** (`BACKEND = {aws, pipeline}`).
  It sits in the **Kimi harness**, the next work front, and needs re-pointing regardless of the rename.

## 6. GROUND TRUTH BANKED THIS SESSION (for whoever builds the Layer axis)

- **The live graph carries ONE node label: `CloudNode`, 20,639 nodes / 41,253 edges** (comp-kuzu,
  rebuilt 2026-08-12T18:25Z, Nessie HEAD current). Every distinction lives in properties, none in
  structure. So `Layer` is not adding a facet to a typed graph — it is the **first structural answer
  to "what kind of thing is this node."**
- **`derive_runner.py:336,372` default an unlabeled node to `aws`** (`str(n.get("layer","aws"))`).
  Mechanism SOURCE-CONFIRMED; **magnitude UNMEASURED** — I have not counted how many nodes take the
  default. Direction of the bias is toward backend, which is the same direction as the coverage split
  `Substrate_Side` was invented to report around. Worth measuring before anyone quotes a per-substrate
  denominator.
- **`Substrate_Side`'s origin numbers, still in the registry:** BACKEND 2693/3396 (79.3%) vs FRONTEND
  1495/11338 (13.2%), average 38.4% "describes neither" — i.e. it was always a *presentation rule*
  that got promoted to a ratified axis. That is why it read as a mess.

## 7. ROUTING

- **Grant → a grantor exec** (CTO / COO / MSTR). CRO does not self-land. This record is the ask.
- **Ontology execution → CRO (me)**, now that the lane question is measured rather than assumed:
  the `Capitalized_Snake_Case` v2.0 rewrite, `Territory` retirement, `Substrate_Side` demotion, and
  the `Layer` mint — sequenced behind the `layer`→`substrate` column rename.
- **Broadcast:** MSTR + CTO + COO, same turn.

## 8. W-04 / W-05 CLOSED (appended 2026-08-14 ~20:18Z — Andrew-direct via /open-calls at the MSTR terminal, MSTR relay 201712Z, VERBATIM "RECS APPROVED")

The two items this record held open are RULED:

- **W-04 — TIER0_EXEC membership = YES (IN the EXEC-coded classification).** The approved rec's
  rationale, on the record: TIER0_EXEC IS the exec tier by name and mapping (`org/tier0_exec/**`);
  excluding the literal exec tier from "EXEC-coded" would be an MECE break. It routed to Andrew
  because MSTR was an interested party on its own tree — his word settles it. **The 9th grant (CRO
  into TIER0_EXEC) LANDS AT A GRANTOR SEAT per SoD (§7 above: "CRO does not self-land") — flagged
  back to MSTR as the grantor of the other 8 @97eabc3ebc; this append applies the CLASSIFICATION,
  not the grant.**
- **W-05 — the non-EXEC-named governance groups (ANY_CTO, TIER0_LAW, TIER0_RATIFY,
  GOVERNANCE_AUDIT, WS_CONTRACT_AUTHORS) = OUT of the EXEC-coded classification.** Rationale:
  governance FUNCTIONS, not exec seats — intent coherence (Rule 24) preserved. **Scope note carried
  verbatim from the relay: this word rules them OUT of EXEC-coded ONLY; whether they warrant their
  own governance-function axis is a SEPARATE schema decision routed via MSTR if it ever surfaces —
  not inferred from this ruling.** Applying the OUT surfaced no such need (an OUT records itself).

With these, the 2026-08-12 walk-list's section A holds only W-02 (`build` fifth Function value —
deliberately event-gated on the W-24 placement pass). W-01 closed earlier today @71d9f06eba.
