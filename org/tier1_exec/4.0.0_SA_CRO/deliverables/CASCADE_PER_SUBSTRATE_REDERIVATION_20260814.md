# Cascade budget — per-substrate re-derivation on the RULED denominator (C0-node grain)

**Ruling:** Andrew-direct 2026-08-14 via /open-calls at the CTO terminal, VERBATIM "REC APPROVED"
on (a) NODE GRAIN + per-substrate re-derivation + 90/9/1 as MATURITY TARGET not today-gate.
Record @71d9f06eba (`ANDREW_DIRECT_20260814_CASCADE_BINDING_GRAIN_NODE.md`) — the anchor.
**Executed by:** 4.0.0_SA_CRO (CTO 201137Z: "YOURS TO EXECUTE").
**Figures:** MEASURED-NOW on the 2026-08-12 graph build (18:25:51Z; 20,616 nodes) per F02
(`KIMI_ESTATE_FANOUT_20260812/02_COVERAGE_CENSUS.md` §6a). **This is a VINTAGE-PINNED derivation
with a mechanical re-derivation formula (§3) — recompute on any newer graph build; do not hand-roll
the digits forward.**

## §1 The ruled semantics, stated once

- **Denominator = the graph's nodes, per substrate — INDEPENDENT of the instrument.** Coverage is
  "of the estate, how much is deterministically covered," never "of what the detectors found, how
  much anchored."
- **90/9/1 (deterministic >= 90% -> inferential <= 9% -> user_described <= 1%) is the MATURITY
  TARGET each substrate matures toward — not a gate any substrate must pass today.** Floors-of-
  honesty unchanged: a node classifies by what it IS.
- **Instance-grain figures remain quotable ONLY with their frame** (ruling rider, from my
  condition): "82.0% — of backend motif instances the detectors found; portal/ms structurally
  absent from the denominator."

## §2 The re-derivation (vintage 2026-08-12)

Per substrate: today-state, ceiling (nodes any detector can currently reach), and the ruled
decomposition of the gap into its TWO different work-kinds — coverage-to-ceiling (detector work
inside the current catalog) vs ceiling-to-target (CATALOG EXTENSION; no tuning reaches it).

| substrate | nodes | covered today | today % | ceiling % | to-ceiling gap (detector work) | ceiling-to-90% gap (catalog extension) | maturity read |
|---|---|---|---|---|---|---|---|
| pipeline | 1,337 | 1,291 | 96.6% | 100.0% | 46 | 0 | **AT TARGET** (only substrate) |
| aws | 2,055 | 1,398 | 68.0% | 77.7% | 199 | 253 (the 458 out-of-scope types' census) | maturing — extension is the binding constraint |
| portal | 11,338 | 1,495 | 13.2% | 46.3% | 3,750 | 4,959 (5,286 role-mapped-undetected + 807 TypeDecl declared-out) | early — extension dominates |
| ms | 5,886 | 0 | 0.0% | 0.0% | 0 | 5,297 (anchor + extractor from zero) | pre-coverage — extension is ALL of it |
| **ESTATE** | **20,616** | **4,184** | **20.3%** | **39.7%** | **3,995** | **10,375** | the honest today-state the ruling binds |

Readings the table carries:
- The estate-wide gap is 72% catalog-extension, 28% detector-work — the ruled grain makes the WORK
  PROGRAM legible (instance grain read the same estate as "487 instances short").
- The inferential/user_described budgets (<=9/<=1) bind per-substrate over the SAME node
  denominator; today every covered node is deterministic-class, so both budgets are trivially met
  where coverage exists and undefined where it does not (ms) — recorded, not glossed.
- Per the ruling's no-self-dispatch boundary (CTO 201137Z): the catalog-extension program (portal
  motif family · ms anchor+extractor · aws type census) is now SIZEABLE against a ruled
  denominator; **COO staffs it when Andrew prioritizes** — this deliverable sizes, it does not
  dispatch.

## §3 The mechanical re-derivation formula (any future graph build)

For each substrate S at graph vintage V:
1. `nodes(S)` = COUNT of graph nodes with substrate S (the FULL node set — never a detector's
   output set).
2. `covered(S)` = COUNT of nodes carrying deterministic-class coverage (anchored / detector-
   covered per the census's covered-now measure).
3. `ceiling(S)` = COUNT of nodes belonging to any type referenced by any detector constituent list
   or anchor catalog entry.
4. today% = covered/nodes · ceiling% = ceiling/nodes · to-ceiling gap = ceiling − covered ·
   ceiling-to-target gap = max(0, 0.9·nodes − ceiling).
5. Print ALL FOUR per substrate + estate. **A quoted percentage without its `nodes(S)` beside it
   is a frame violation of the ruling's own rider.**

## Labeling
MEASURED-NOW (2026-08-12 build): every table figure. INFERRED: nothing. The ruling anchor and the
census file:lines are the citations; this document adds arithmetic and the ruled frame only.
