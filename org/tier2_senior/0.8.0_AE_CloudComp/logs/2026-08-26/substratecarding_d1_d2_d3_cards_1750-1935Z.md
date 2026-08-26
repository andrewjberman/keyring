# Session log -- `0.8.0_AE_CloudComp~Y` -- 2026-08-26 17:50Z - 19:35Z

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Serial:** `0.8.0_AE_CloudComp~Y` (lane instance; SINGLE-PROJECT -- holds NFRA_SUBSTRATECARDING and nothing else)
**TO:** `NFRA_SUBSTRATECARDING.TO-W1-CCY.d1-d2-d3-cards`
**Cells:** 21 -- `SC-e-1..7` (D1), `SC-f-1..7` (D2), `SC-g-1..7` (D3)
**Window:** session start (`/watcher` 17:31Z) -> proof-of-spec VALID 19:2xZ
**First log for this lane** -- `~Y` was spawned this session.

---

## 1. What this window was

Startup, then one TO end to end: three substrate cards for the D1/D2/D3 ontology rails,
their proof-of-spec instance, and the acceptance run. No prior work to continue.

## 2. Startup

`/watcher` armed a persistent inbox Monitor (task `b04l220iz`, `TaskOutput -> running`). Registration
was absent for the lane and was created. Two things worth recording because both are instrument
failures that would otherwise read as clean results:

- **`ps -ef` fails deterministically in this shell** (MSYS `cmalloc` fatal, 3 of 3 attempts). The
  orphan-watcher check depends on enumerating processes, and a `ps | grep` would have returned a
  clean empty -- indistinguishable from "no orphan". Switched to PowerShell/CIM: **48 bash/sh
  processes scanned, 0 matching this serial.** A `~X` lane watcher exists and is a live peer, not
  an orphan. The verdict rests on a working instrument.
- **`.tools/check-inbox` does not resolve** though `org/XXX.md` Step 1b-B mandates it. Surfaced as
  OBSERVATION to `3.0.0_SA_CVO` cc `2.0.0_SA_COO~X` (72817/72818), not chased.

Zero crons armed, confirmed two ways (`CronList` empty; no F-table row or live scoped arm names
`AE_CloudComp`). `/cloud-ops` loaded as the mandated one-shot.

## 3. The result, stated first

**All three rails card `QUALIFIED`. None `INCOMPLETE`. All 21 rows worked, basis `measured`.**

⛔ **THE TO'S STATED PRIOR ON D3 IS FALSIFIED.** TO s.2.2 and the PRD expected D3 to card
`persistence: none` / `location: null` and called that emptiness the deliverable. **D3 has a real
instance store**: `org/modules/graph/estate-contracts/`, **14 contract_records across 2 of 2 files**.

The count was **not** produced by my own grep -- I imported `contract_declare_lint.py` and ran **its**
`find_records` predicate, and it is independently corroborated by an `atom_layer0` run at a different
vintage by a different seat (`UNDECLARED 12, PERMANENT 2 of 14`), which my own re-measurement
reproduces exactly. `2.0.0_SA_COO~X` ruled the expectation retired rather than the card wrong (73049).

**Per-rail, one line each:**

- **D1** -- definition coherent, EdgeKind split reproduces exactly (337/142/482, sum 961). But 2 of 13
  embedded surfaces drifted and a third declared claim is now false: the block says "884/961 FLOWS_TO
  carry a non-null dstField"; live it is **961 of 961**.
- **D2** -- its three declared contributions are **not in the same state**, and that is the finding.
  DIRECTION sound, TRANSFORM sound, **TIME structurally unresolved**: cadence is D3-sourced and D3
  supplies a cadence value for **1 of 14** records, while **4** declare the `delivery_cadence`
  obligation. 9 of 15 embedded surfaces drifted.
- **D3** -- richest rail (13 keys), the only one with definition + store + validator. Four bounded
  defects: three carrier populations with no mapping between id spaces; **6 of 14** records carry zero
  obligations (UNDECLARED by the rail's own text) while passing the lint; **14 of 14** carry
  `revalidate_by: "on produce"`, a condition not a window, leaving the decay control nothing to
  evaluate; and the validator's REJECT and PASS **both return rc=0**.

## 4. The two measurements I did not trust on their own

**(a) The dstField zero.** My predicate was `props CONTAINS '"dstField": null'` and it returned 0 --
which would have meant every edge carries the field. Before reporting that as drift I ran a
**positive control on the identical predicate shape** against a field known to carry nulls:
`'"condition": null'` matched **938**. Two further arms ruled out alternate serialisations (key never
absent: 0; never empty-string: 0). Only then did I report 961 of 961. Without the control this reads
identically to a predicate that cannot match anything.

**(b) The rail-store absence.** Five `--name` sweeps returned 0 hits. A zero over a real denominator
is a measured absence -- but only if the sweep can find such a thing at all. Ran the **positive
control in the same call shape** on a store I already knew existed (`'*contracts*'` -> 21 hits /
28,790 scanned) **before** trusting any of the zeros.

⚠ And a name-collision trap worth carrying: `comp-find --name 'NFRA_ONTOLOGY_RULE_BANK*'` returns
**2** hits. The second, in this lane's own base deliverables, carries **zero** rail content
(0 occurrences of `dynamic_rails`, 0 of `rail`, against 31 in the canonical). It is a **different
artifact sharing a leaf name**, not a stale copy -- and a seat citing the bank unqualified would land
on it.

## 5. Two corrections against my own work

1. **I cited a line as `:~520`.** An approximate line number is not a citation -- the exact form is
   `file:line @ commit`. Pinned it to `:490` before commit.
2. **My first proof-of-spec instance was structurally INVALID** -- 20 violations. I invented six
   `method` names outside the ratified enum, added four forbidden properties, and omitted four
   required roots. Recorded rather than quietly fixed, because the checker **also warned** that its
   alignment figures "are identical to what a VALID instance prints -- they are NOT evidence of
   validity." Quoting 23/23 off an invalid instance is exactly the trap it names.

## 6. Inputs consumed, cited not re-derived

Per the TO's one-measures-one-cites rule:

- **`0.8.0_AE_CloudComp~X`'s SC-c-1 (73170)** -- "C2's motifs" resolves to **two unjoined
  vocabularies** (12 declared families vs 13 served class nodes, zero shared names, mapping null);
  and C2's instances are a **frozen composition inside a moving projection** (6,207 at one snapshot,
  0 at the serving snapshot, classes at a third). Since D2 is the rail that adds **TIME**, that lands
  directly on my subject. Folded into D2's `key` and `failure_mode` rows with attribution.
- **ANDREW-DIRECT ~1907Z** (relayed 73176, first-hand at `0.4.0_DT_ClientPlatform~X`'s terminal):
  the suspicion axis is **SEMANTIC, not vintage**. ⛔ **Every drift figure in my three cards is a
  vintage comparison, and no freshness instrument I hold can detect deprecated opinionation.** Added
  as an explicit limit to all three coverage rows: *a count that HOLDS is evidence of stability,
  never of correctness.*
- **`2.0.0_SA_COO~X` RULING 1 + RULING 2 (73211)** -- applied both before routing to CVO, so no edit
  lands mid-verification. Ruling 2's per-card semantic `UNMEASURED` is now a named entry in each
  card, stating plainly that no systematic semantic pass was run **and** what surfaced incidentally.

## 7. Compiler Tools

**Mandatory section. Every `<run>` from the TO's `<compiler_tools_mandate>`, observed result, and
pass/fail against `<expect>`.**

| phase | run | expect | observed | verdict |
|---|---|---|---|---|
| 0 | `comp-which "what generates and persists the D1 value rail / D2 path-flow rail / D3 contract rail"` | a named generator per rail OR a measured absence | declared near-tie (2 tools at 1.50) over 80, self-labelled "TOP SCORES ARE TIED -- NOT A RANKING". Named no generator = the documented `if_mismatch` branch | **PARTIAL -> widened deliberately** |
| 0 | read `NFRA_ONTOLOGY_RULE_BANK.yaml#dynamic_rails` -- D2 block AND siblings | the 7 declared keys; whether D1/D3 have comparable blocks | `yaml.safe_load` (a parse, not a grep): **D1 = 10 keys, D2 = 7, D3 = 13**. D2's 7 independently confirms the TO's "7 keys at 2026-08-20" | **PASS** |
| 1 | hunt the PERSISTED artifact per rail: `comp-find --name` over plausible outputs, then the live store | a home path, or a MEASURED absence with denominator printed | D1/D2: **0 hits / 28,789 scanned** across 5 patterns, positive control 21 / 28,790. D3: **found** -- `estate-contracts/`, 14 records / 2 of 2 files | **PASS** |
| 1 | EXERCISE each rail's failure path -- ask it something it cannot answer | an observed `returns_on_failure` | D1 row-grain probe -> **0** with positive control **4,969** (clean zero, indistinguishable). D3 linter mutant -> **REJECT, findings=2**, real file **PASS, findings=0** -- both arms, different truths | **PASS** |
| 2 | `jsonschema` validate all three cards | `3/3 VALID` | **3/3 VALID**, re-run after every amendment. Negative control (trust block deleted) -> **REJECTED**, so it is a live pass | **PASS** |
| 3 | `proof-of-spec-check.py <instance> CCY-AC1..AC7` | rc=0, VALID, alignment ENFORCE with denominators | first run **INVALID, 20 violations** (my error, s.5). After rewrite: **VALID, violations=0**, alignment ENFORCE, **7/7 criteria carry cell_refs, 23/23 resolve, 23/23 reachable** | **PASS (after correction)** |

**Additional tools, not mandated but load-bearing:**

- **`comp-kuzu`** -- provenance header read on every call (Rule 20); confirmed the **pinned** plane
  (snapshot `2902399899597701830`, 27,035/58,224, built 14:07:59Z), so every figure is at the wave
  vintage. Schema was **discovered, not assumed**: a first query on `e.type` failed
  (`Binder exception: Cannot find property type for e`) and `table_info` gave the real name
  `edge_type`. Recorded because guessing would have produced a confident wrong census.
- **`comp-icedrill`** -- one bounded attempt to count D3's Iceberg carrier. **Cannot answer**: its
  target grammar is `s3://... | ddb | graph`, no form for an arbitrary warehouse table. Recorded as
  the "where I looked" backing the UNMEASURED row rather than dropped.
- **`comp-to`** -- set the race-free per-session TO_ID.
- **`comp-find`** -- 12 calls, all audited against the invocation trap the moment it was broadcast:
  **12 of 12** used `--name` alone or a content pattern alone, every one with a non-zero `scanned`.

## 8. Surprise channel

Four OBSERVATIONs, none BLOCKING, none chased. The `check-inbox` gap (72818); the `comp-find` trap
audit (already fabric-wide, reported denominators rather than a self-assessment); the
`proof-of-spec-check` rc=0-on-INVALID shape, which is the **same** verdict-on-stdout-not-in-rc class
this lane independently exercised on `contract_declare_lint.py` -- **two distinct estate instruments
now measured with that property**, no causal story carried, neither tool touched; and the rule bank's
D3 `landing_state` asserting its own registry "does not exist" when it does, which is carded rather
than routed because a finding about a rail you are carding is the deliverable.

## 9. QUALIFY-DO-NOT-FIX

**Honoured and verified mechanically, not asserted.** This lane's entire committed file set is under
`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/**`. Per-surface check against all **6** carded
surfaces (rule bank, estate-contracts, the linter, SYSTEM_DEFINITIONS, the card schema,
keep-dormant): **0 touched**. The planted mutant was written to the session scratchpad **outside the
repository**. No schema amendment despite F-1/F-2/F-3 being live -- those route to the issuer and
`1.0.0_SA_CTO~X` (boundary `SC-bnd-4`).

## 10. Artifacts

| artifact | path |
|---|---|
| D1 card | `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/D11_CARDS/D1.json` |
| D2 card | `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/D11_CARDS/D2.json` |
| D3 card | `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/D11_CARDS/D3.json` |
| proof-of-spec | `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_SUBSTRATECARDING.TO-W1-CCY_PROOF_OF_SPEC.json` |
| this log | `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-08-26/substratecarding_d1_d2_d3_cards_1750-1935Z.md` |

Cards landed `@c43050e9bb`; amendments, instance and this log ride the follow-on commit.
Routed to `3.0.0_SA_CVO~X` at the completion flip, cc `2.0.0_SA_COO~X`.
