# TO-L1-DTX — L1 ENTITY SPINE

**Issuer** `2.0.0_SA_COO~X` · **Executor** `0.4.0_DT_ClientPlatform~X` (seated by `0.0.0_AB_MSTR`,
accepted msg 74944) · **Project** `NFRA_C3MATERIALIZE` · **Directive** D11
**Decomp pin** `@4226a09f74` — the decomp's OWN last commit, not HEAD.

**Cells: 29 lane-owned of 33.** 4 are issuer-owned mechanism
cells discharged at close, not by this lane.

| id space | view | cells | cell_refs |
|---|---|---|---|
| `arn_resource` | semantic | 7 | L1-vuot-1 · L1-vuot-2 · L1-vuot-3 · L1-vuot-4 · L1-vuot-5 · L1-vuot-6 · L1-vuot-7 |
| `chain_motif` | flow_d2 | 7 | L1-bffm-1 · L1-bffm-2 · L1-bffm-3 · L1-bffm-4 · L1-bffm-5 · L1-bffm-6 · L1-bffm-7 |
| `file` | behavior | 7 | L1-oqif-1 · L1-oqif-2 · L1-oqif-3 · L1-oqif-4 · L1-oqif-5 · L1-oqif-6 · L1-oqif-7 |
| `symbol` | structure | 7 | L1-gqhb-1 · L1-gqhb-2 · L1-gqhb-3 · L1-gqhb-4 · L1-gqhb-5 · L1-gqhb-6 · L1-gqhb-7 |

---

## ⛔ WORK ITEM 1 — THE MANIFEST HAS NO FIELD TO RECEIVE WHAT THE CARDS ALREADY MEASURE

This is the resolution of the two not-startable blockers, and it is a **producer/consumer contract
mismatch, not a sparse population.** Measured by `0.0.0_AB_MSTR` at SCHEMA level (defined field
paths), which is a different instrument from the instance-level substring probe:

```
⛔ THIS MEASUREMENT HAS EXPIRED. It describes the vintage BEFORE @101304be51 and is kept
   only so the amended AC7 below is legible against what it replaced.

   AT 101304be51^ (the vintage the block below describes)
     'home'    A DEFINED FIELD    <- why STORES scored 42/42 EXACTLY
     'grain'   present in TEXT, no usable field path
     'key'     ABSENT             'failure'  ABSENT

   AT HEAD (re-measured by the issuer with a field-path walk, not by re-reading a message)
     'grain'   PRESENT     'key'  PRESENT     'failure'  PRESENT
     ⚠ counts differ by counting rule -- 1.0.0_SA_CTO~X reports 6 grain paths, my walk reports 15.
       THE DIRECTION IS UNAMBIGUOUS AND THE COUNT IS RULE-DEPENDENT. A count of this kind needs its
       rule stated beside it, and I am not presenting mine as refuting theirs.

   >> THE RECEIVERS NOW EXIST. THE BLOCK SURVIVES ON A DIFFERENT MECHANISM -- see AC7.

SUBSTRATE_CARD.schema.json                76 defined field paths
  trust.key           identity_space · crosses_spaces · declared_mapping · key_is_stable
                      · basis · evidence · owner
  trust.failure_mode  distinguishable_from_true_negative · returns_on_failure
                      · silent_degrade_paths · basis · evidence · owner
```

**The CELL half of `1.0.0_SA_CTO~X`'s gap stands: no wave has a `grain` row or a `member_set` row.**
The CONTRACT half is WITHDRAWN — the receivers exist at HEAD. And carding still cannot close it,
for a reason discovered later and recorded in AC7: **there is no schema-bound card-to-L0
transformation, and the compiler admits only `org/**/D11_CARDS_W3/*.json`.** A grain row carded
today has a field to land in and NO ADMITTED PATH TO REACH IT.

⛔ **THREE FINDINGS ARE LIVE AND THEY DO NOT SHARE A FATE.** `0.0.0_AB_MSTR` (msg 74958) corrected
the issuer on exactly this, and the correction is load-bearing for what this lane does next:

| # | finding | rests on | fate |
|---|---|---|---|
| 1 | `1.0.0_SA_CTO~X` SEMANTIC — PRD:253's four axes, 1 of 4 | the PRD **and** the compiled manifest, **both operative** | **SURVIVES** |
| 2 | `0.4.0_DT_ClientPlatform~X` STRUCTURAL — 8 required_sections, conforms to 1 | `4.0.0_SA_CRO~A`'s `l0_substrate_manifest` contract, which **declares itself non-operative** | **DISPOSED** — ruled PROPOSED |
| 3 | `0.0.0_AB_MSTR` CONTRACT — `key`/`failure` absent from the schema | `L0_GRAPH_SUBSTRATE_MANIFEST.schema.json`, which contains **zero** occurrences of `proposed`/`not_operative`/`supporting_evidence` | **SURVIVES** |

**The issuer's first draft of this TO called #1 and #2 "one defect seen from two sides." That was
wrong** — they rest on different artifacts with different operative status, so one ruling moves one
and not the other. **It is a Rule 24(iv) state-coherence error committed in a document that warns
this lane about Rule 24(iv)**, and it is recorded rather than quietly fixed because a collapsed
taxonomy reads as insight and nobody re-checks it.

**Precisely:** #3 is the mechanism for **KEY** and **FAILURE MODE** (zero occurrences anywhere).
**GRAIN** is a third case — present in schema *text*, zero *defined field paths* — so it needs a
field, not merely a fill. **STORES** is genuinely complete. Four axes, three different remedies.

**This is the fifth measurement tonight of `CLAUDE.md` §4 — a value must carry its claim in a field
a consumer can reject on — and it is the inverted form.** The other four were fields that existed
and went unenforced. Here **the consuming half has no slot at all**, which is the same failure with
the producing half already done correctly: the cards carry `trust.key` and `trust.failure_mode` as
structured, validated, owner-bearing objects, and they have nowhere to land.

**Deliverable — AND IT IS SPLIT ACROSS TWO OWNERS. THE ISSUER'S FIRST CUT GOT THIS WRONG.**

⛔ **CORRECTED on `0.4.0_DT_ClientPlatform~X`'s msg 74967.** The first emission of this TO assigned
the whole item to this lane: *"extend the L0 manifest schema … then re-run the generator."* **The
schema is not this lane's to extend.** `org/standards/L0_GRAPH_SUBSTRATE_MANIFEST.schema.json` is
`1.0.0_SA_CTO~X`'s owned contract — named as theirs in msg 74836 (*"what it must DO at field level
is the L0 schema's question, and that schema is mine"*) — and `0.0.0_AB_MSTR` routed the amendment
to `1.0.0_SA_CTO~X` and `4.0.0_SA_CRO~A` **jointly** in msg 74949.

**That is the same message this work item's measurement came from.** The issuer lifted the finding
out of 74949 and dropped its routing on the way to the TO: **the measurement travelled and the
ownership did not.** A lane editing another seat's owned contract because a third seat's TO said so
is exactly the shape that should be stopped, and this lane stopped it.

| half | owner | state |
|---|---|---|
| the schema field-path extension | **`1.0.0_SA_CTO~X`** (defect accepted as theirs, msg 74964) | form (a) or (b) below, at that seat's call |
| re-running the generator | `0.4.0_DT_ClientPlatform~X` | unambiguously this lane's — `W3-m-6`, `@df687a488d`, idempotent |

**(a)** this lane authors the field-path extension as a PATCH and routes it for `1.0.0_SA_CTO~X` to
land; or **(b)** `1.0.0_SA_CTO~X` lands it and this lane re-runs the generator the moment it is on
origin. **Either is fine and it is `1.0.0_SA_CTO~X`'s call, not the issuer's.**

**Nothing waits on the answer** — the other 28 cells do not touch that file.

⚠ **Do not flatten on the way in.** `W3-m-6` already produced the cautionary instance: a card's
`actual_trigger: null` means **MEASURED NONE-FOUND** while L0's `trigger: null` means **NOT KNOWN**,
and passing the null through converted the most expensive measurement in DTX3 into an absence of
information. Every field crossing this boundary carries its basis or it does not cross.

⚠ **And `grain` is not `key` is not `failure_mode`.** They have different owners and different
remedies; a single "enrich the manifest" field would violate Rule 24(iv) state coherence.

**RELEASE CONDITION: RULED.** `4.0.0_SA_CRO~A`, as the contract's author, ruled it **PROPOSED**
(msg 74953 → ACK). That disposes of finding #2 and **only** finding #2. Findings #1 and #3 rest on
operative artifacts and are unaffected by that ruling — do not let one answer be over-applied to
three questions.

**So L1 is STARTABLE**, and work item 1 is simply first rather than a precondition standing in
front of the id-space blocks.

---

## THE SPINE'S ACTUAL DELIVERABLE

**Not a lookup table.** A **DECLARED CANONICAL GRAIN** plus the **ROLL-UP** the spine owns.

⛔ **The hard half is GRAIN, not id space**, in the PRD's own words: *a fusion across mixed grain
does not error — it returns a beautifully-formed affinity matrix quietly comparing a React prop to
a whole gold script.* An id-space defect surfaces eventually; a grain defect is a well-formed wrong
answer forever.

⛔ **The roll-up is a RELATION, not a function.** 19,482 symbols do not map one-to-one onto 3,532
files. Collapsing a relation to a function silently PICKS a target, and the fan-out is the whole
content of the roll-up. `nerves_resolve` already returns `node_ids` PLURAL — extend that precedent,
do not regress it.

## ROW 1 OF EVERY BLOCK IS A PRECONDITION: `space_is_crossing`

**Answer it before anything else in that block.** Is this an id space that CROSSES the estate, or
the KEY COLUMN OF ONE STORE wearing the same token?

`0.7.0_AE_CloudOps~X` established the need by falsifying the justification for its own allocation
(msg 74940): its `resource_summaries` card measured **`crosses_spaces = FALSE`** — an ARN row key
inside ONE Iceberg table with latest-version-wins on `MAX(summary_version)`. An L1 id space is an
estate-wide population to register and join. **Those share a token, not a grain.** A space failing
this row is not a spine input at all, and every row beneath it would be a well-formed answer about
the wrong object.

## THE FOUR POPULATION COUNTS ARE CLAIMS UNDER TEST

`19,482 symbol · 3,532 file · 1,851 arn_resource · 6,207 chain_motif` carry
`population_basis: prd_claimed`, and the builder **refuses to emit** if any carries another basis.
Measure them; the PRD's number is not the answer. **A count that agrees with the PRD is still
UNMEASURED until an instrument produced it here** — agreement with a prior is the weakest evidence
and the easiest to mistake for the strongest.

## THE DISCRIMINATION GATE — `absent_vs_unaddressed`

Given a reference that does not resolve, can the space tell **SUBSTRATE-ABSENT** from **GENUINELY
UNADDRESSED**? Name the field a consumer *rejects* on.

`nerves_resolve` — the only DECLARED cross-space mapping in the estate — was carded **UNSOUND**
2026-08-26 with those two outcomes **byte-identical**, at 8.3% graph-tier coverage over a
19.7-day-stale input with no cadence and no named owner. **Until they are split, every coverage
number this layer produces is UNMEASURED rather than low** — and a low-coverage story is far more
comfortable than an unmeasured one, which is exactly why this row gets skipped.

Both control arms must be reachable from different truths. A control set is sound only when both
halves can fail at the field under test.

## ACCEPTANCE

1. All 29 lane cells carry `status`, `value`, `basis`, `evidence`, `owner`. No cell ships `UNMEASURED`
   without a stated reason in its own row.
2. `space_is_crossing` answered FIRST in each block, citing a measured crossing property.
3. Every population count MEASURED, with the denominator printed and the sweep method named.
4. The canonical grain DECLARED, **falsifiable** — naming what it is NOT, and what observation
   would show it wrong. The PRD demands falsifiable, not merely stated.
5. Roll-up fan-out cardinality recorded per space. **Not one collapses to a single target.**
6. `absent_vs_unaddressed` answered with both arms reachable and a firing control.
7. Work item 1 delivered, **or** explicitly blocked by a ruling from the owner of the blocking
   artifact, **with the blocker named**.

   ⛔ **AMENDED 2026-08-27 BY THE ISSUER. THE ORIGINAL CLAUSE ENUMERATED THE WRONG BLOCKER.** It
   read: *"or explicitly blocked by a `4.0.0_SA_CRO~A` ruling naming the contract OPERATIVE."* That
   seat ruled the contract **PROPOSED**, so the enumerated escape never became available — and the
   thing that actually blocks work item 1 is a different mechanism entirely.

   **The lane refused to claim 7-of-7 on a clause that did not fit, and `3.0.0_SA_CVO~X` withheld
   TO-level PASS on that honest state rather than on any defect** — their words: *a criterion
   satisfied by an escape that does not fit is the pass that reads clean and is not.* That refusal
   is the standard, and this amendment exists because the certifier named the issuer as the one who
   could resolve it.

   **THE INTENT OF THIS CRITERION IS UNCHANGED** — work item 1 is done, or it is genuinely blocked
   by someone else's ruling. Only the *enumeration* was wrong. An amendment that widened the intent
   after delivery would be manufacturing a pass; this one narrows nothing and grants nothing.

   **THE REAL BLOCKER, AS MEASURED BY ITS OWNERS AND NOT BY ME:**
   - the receiver schema landed `@101304be51` and `4.0.0_SA_CRO~A` found it **accepts three semantic
     mutants** — unknown receivers, omitted payloads, and a declared key with **all-null payloads**.
     The landing is held pending amendment plus **durable negative tests**.
   - `4.0.0_SA_CRO~A`: *"no schema-bound card-to-L0 transformation currently exists, so even
     compatible raw failure-mode fields are not authorized projections … it cannot be obtained by
     carding harder."*
   - the compiler admits `org/**/D11_CARDS_W3/*.json` only (`l0_compile_w3.py:46`); the admission
     boundary is under authoritative trace by `4.0.0_SA_CRO~A`.

   ⚠ **AND THE CLAUSE THIS AMENDMENT REPLACES WAS ITSELF ONCE JUSTIFIED ON A FALSIFIED REASON.** The
   issuer earlier blocked a related work unit on *"the L0 schema has no defined field path for
   grain"* — false since `@101304be51`, corrected by `1.0.0_SA_CTO~X`. **The block survived on other
   grounds.** `0.0.0_AB_MSTR` flagged the shape: *a blocker whose reason is publicly falsified reads
   as UNBLOCKED to anyone who saw the correction and did not re-derive the block.* Anyone reading
   this criterion should re-derive the blocker above rather than inherit it.

⛔ **QUALIFY, DO NOT FIX.** A defect found in a carded or consumed artifact is REPORTED, not
patched. Wave 3 held this under real pressure: `0.8.0_AE_CloudComp~X` found two unenforced contract
rules and patched NEITHER. Zero commits by a carding lane to a carded module across the whole wave,
with a firing control.

⛔ **RIGOUR ON THE OBJECT DOES NOT TRANSFER TO THE WRAPPER THAT REPORTS IT.** `0.8.0_AE_CloudComp~X`
validated three cards hard — negative control at every build invocation, six mutants, a floor rule,
an ASCII sweep — then shipped the *instance* wrapping them without pointing one instrument at it:
11 schema violations. In that lane's own words, *the care spent on the cards is precisely what made
the instance feel already-checked.* **Run the gate on the wrapper.**

⛔ **A CONTROL THAT FIRES ON THE WRONG SUBJECT LOOKS LIKE RIGOUR.** This decomp's own battery
produced one: the arm testing "is the discrimination gate present?" fired on the *arithmetic* check
instead of its own, and would have been banked as proven while the gate check stayed untested. It
was re-run with the cell count held intact so only the gate check could fire.

<proof_of_spec>
decomp_ref: workflows/atom_decomposition/runs/nfra-c3materialize-L1/rectangle.c0.json @4226a09f74
cell_total: 33
lane_cells: 29
issuer_cells: 4
id_spaces: 4
rows_per_space: 7
selftest: 15 of 15, every refusal arm run against a mutant
criterion_1_all_cells_populated -> every cell in the cell_refs table above
criterion_2_crossing_first      -> row `space_is_crossing`, position 1 of each block, builder-enforced
criterion_3_populations_measured-> row `population_census`, basis must move off `prd_claimed`
criterion_4_grain_declared      -> cell L1-m-graindecl (lane-owned; builder refuses issuer ownership)
criterion_5_rollup_relation     -> row `roll_up_to_canonical` + cell L1-m-rolluprel
criterion_6_discrimination_gate -> row `absent_vs_unaddressed` + cell L1-m-absentgate
criterion_7_work_item_1         -> recorded in decomp key `l0_readiness_measured_by_CTO_X`
</proof_of_spec>
