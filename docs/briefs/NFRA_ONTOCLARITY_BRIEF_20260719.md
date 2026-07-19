# NFRA_ONTOCLARITY — Brief: no semantic fog in the ontology (layering / nesting / definitions / processes), then correctly logged in system + sdk

**To:** 1.0.0_SA_CTO (REGISTER the project + render this brief into a PRD → issue to COO) · **From:** 0.0.0_AB_MSTR
**Date:** 2026-07-19 · **Charter:** LD-0320 · **Parent:** NFRA_SYSPARITY §8 / Part 2 · **Status:** brief issued to CTO

---

## 0. Origin (Andrew-direct, 2026-07-19, verbatim intent)

> "a pt 2 of this will be a separate audit that is devoted to establishing that there is no semantic
> fogginess in ontology, that there are clear rules on layering, nesting, definitions, processes, etc. and
> again, once established, that they are correctly logged and referenced in the system and sdk folders."

And (2026-07-19, promoting it to a live project): *"we should have CTO register NFRA_ONTOCLARITY on the other
subject once this is done if not already and have your brief on the subject rendered into a PRD and issued to
COO for decomposition and dispatch."*

## 1. What this is (and is NOT)

NFRA_ONTOCLARITY is the **DEFINITIONS/CLARITY audit** of Opal's ontology — establish that its rules on
**layering, nesting, definitions, and processes are unambiguous, non-contradictory, and single-sourced**, then
ensure the clarified rules are **correctly logged and referenced in `infra/system/` + `infra/system/sdk/`**.

- It is **NOT** NFRA_ONTOLOGY (which *builds* the 14/10/6 archetype layer) — it audits that layer's *clarity*.
- It is **NOT** NFRA_SYSPARITY (which measures *representation parity*) — it is Part 2, the *definitional* audit.
  The two compose: SYSPARITY WS-4 *represents* the ontology in system/sdk; ONTOCLARITY makes sure *what gets
  represented is itself unambiguous* first. **ONTOCLARITY's clarified definitions are the input WS-4 logs.**
- It is **NOT** NFRA_NESTEDABSTRACT (the forward SDK-incorporation loop) — it does not fold enhancements; it
  removes fog.

## 2. Method + evidence base

Seeded by the grounded ontology-parity analysis run this session (one of the four NFRA_SYSPARITY analysts,
citing `file:line` at HEAD). It surfaced **10 concrete semantic-fog spots**, all re-verifiable. CVO's
NFRA_SYSPARITY verification loop independently sharpened two of them (the name-vs-concept axis, §3), which is
the *method note* this whole project must adopt: **fog is a SEMANTIC property — a word-grep verifies clarity
in neither direction.**

## 3. The fog, organized by Andrew's four axes (10 spots → 4 classes)

### 3a. DEFINITIONS (the largest class — 5 spots)
1. **"Ontology" is one word for two layers, never disambiguated — the ROOT fog.** In `infra/system` it means
   the CSE C0-C3 algebra; in `org/modules/graph` "NFRA_ONTOLOGY" means the 14/10/6 archetype layer *above* it.
   No single doc states the relationship. Everything downstream inherits this ambiguity.
2. **The ratified vocabulary is split across ~5 files + a version-fogged pin.** CLOSED_SET.md (prose) +
   RULE_BANK.yaml (org/modules/graph) + a duplicate in deliverables + canon-patterns.yaml (v0.1, which
   *defers* to the ontology) + variance_dimensions.yaml. The SDK pins `v0.1-canon-patterns` — a version label
   naming a file that defers to the thing being versioned. No single canonical source-of-record + version scheme.
3. **DoR and rule-bank DISAGREE on whether Observer is settled** (`CLOSED_SET.md:48` "Open for CTO" vs
   `RULE_BANK.yaml:33` "CTO GRANTED") — a live internal record contradiction.
4. **`variance_dimensions` (the name) invites reading axis-names as the variance vocabulary** — but the real
   variance content is the 6 verdicts. The name is baked into a FROZEN v1 "additive-only" schema, so the fog
   is load-bearing.
5. **"Fork-Shadow = debt" is a recently-RETIRED definition whose old copies may linger** (LD-0315 replaced it
   with "advisory candidate"; it took 4+ sweeps to purge the prose synonym "divergence is debt"). Any consumer
   still reading the old equation is now wrong — definitional drift *inside* the ontology.

### 3b. LAYERING (1 spot, high-severity)
6. **"Layer/plane" carries FIVE incompatible numbering schemes with no crosswalk:** C0-C3 (compression axis) /
   the `layer` field (aws/portal/ms/pipeline substrate axis) / `semctl` (the "fifth layer exception") / the
   GLOBGRPH **L1-L7** design numbering / the recognizer **A-B-C-D** planes→"Territories." `01_substrate.md`
   itself flags "layer" as overloaded, then juxtaposes them with no reconciling map.

### 3c. NESTING (1 spot)
7. **The Relation-vs-Role composite is a stated "load-bearing subtlety" that nothing enforces.** Three edges
   (`routes-to` / `resolves-through` / `projects`) each yield a base Relation **plus** a Role (Router/Registry/
   Gateway) — dual-axis for exactly those three, single-axis for all others. A classifier must know the
   exception list; no artifact enforces it.

### 3d. PROCESSES (3 spots)
8. **Polymorphic-type Role resolution has no tie-breaker.** For a Lambda that both guards AND transforms, which
   Role wins is undefined — the derive-rules are prose heuristics with no priority ordering.
9. **The three incorporation "modes" are fog-prone.** The NESTEDABSTRACT PLAYBOOK spends most of its length on
   traps ("pin-advance is NOT the line," "vocabulary-vs-executable is NOT the line") — evidence the
   shared-version-slot / sdk-capability / per-tenant-template boundary is unclear in practice.
10. **C2→C3 emergence ownership overlaps NFRA_SYSTEM ↔ NFRA_ONTOLOGY.** The ontology "CONSUMES NFRA_SYSTEM's
    C3 detection, does not re-implement it" — yet both `RULE_BANK.yaml` and `01_substrate.md` author the same
    C2→C3 transition. "Consume, don't re-implement" is asserted but two artifacts describe it.

## 4. Recommended workstream shape (for CTO's PRD to refine)

- **WS-A — DEFINITIONS.** Disambiguate the two "ontology" layers in ONE authoritative place (the root fix);
  declare a single canonical source-of-record + version scheme for the ratified vocab (retire the split/pin
  fog); resolve the Observer DoR-vs-rulebank contradiction; purge the retired Fork-Shadow=debt copies to
  closure; rename/annotate `variance_dimensions` so axis-names aren't read as the verdict vocabulary.
- **WS-B — LAYERING + NESTING.** One crosswalk table reconciling the 5 layer/plane numbering schemes (the
  single highest-leverage clarity artifact); document + *enforce* the Relation-vs-Role dual-axis exception
  list (a lint, not prose).
- **WS-C — PROCESSES.** A deterministic tie-breaker (priority ordering) for polymorphic-type Role resolution;
  a decision-rule for which of the 3 incorporation modes applies; a pinned C2→C3 emergence ownership boundary.
- **WS-D — LOGGED + REFERENCED IN SYSTEM/SDK.** Once WS-A/B/C clarify the rules, ensure they are correctly
  logged + referenced in `infra/system/` + `infra/system/sdk/`. **This rides NFRA_SYSPARITY WS-4** (represent
  the ontology) — do not duplicate it; ONTOCLARITY supplies the *clarified definitions*, WS-4 logs them.

## 5. Sequencing + dependencies

- The **fog-resolution work (WS-A/B/C) can start NOW** — it audits the ontology's own clarity, independent of
  the SYSPARITY scope contract.
- **WS-D (logged in system/sdk) rides SYSPARITY WS-1 (scope contract) + WS-4 (represent the ontology)** — it
  needs the declared scope + the representation target. So ONTOCLARITY's *definitional* half runs in parallel
  now; its *logging* half sequences behind WS-1/WS-4. (Andrew's "once this is done" = the WS-D half.)
- **Method binding (CVO):** fog is semantic — verify clarity by the citational/semantic axis, NEVER a
  word-grep (a word-count mis-verifies in BOTH directions; CVO proved this on the "ontology absent" finding).

## 6. Verification regime

Same standing regime as its parent (LD-0318/LD-0319): **CVO verifies each ONTOCLARITY deliverable** — a fog
class is not "resolved" until CVO confirms, on the semantic axis, that the ambiguity/contradiction is actually
gone (not just reworded). Rolls into the CVO standing verification lane.

## 7. Ownership

- **CTO:** REGISTER NFRA_ONTOCLARITY (project JSON + REGISTRY row) + render this brief into a PRD, then issue
  the PRD to COO (Andrew-direct flow, same as NFRA_SYSPARITY).
- **COO:** decompose the PRD to TOs + dispatch (context-matched — ~C, the ontology lane, is the natural owner
  of the definitional workstreams).
- **MSTR:** charter (LD-0320) + governance; **CVO:** the standing verification.

---

**Ask of CTO:** register NFRA_ONTOCLARITY + PRD this brief → issue to COO for decomposition + dispatch. The
definitional half (WS-A/B/C) is startable now; the logging half (WS-D) rides SYSPARITY WS-1/WS-4. ~C (the
ontology lane) is the natural build owner.
