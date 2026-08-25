# SPAWN BRIEF — THE ESTATE BUILD LANE (R-1, authorized 2026-08-24 ~22:0xZ)

**Authorized:** Andrew-direct, *"All recs approved"* over master /open-calls CALL 1.
**Prepared by:** `4.0.0_SA_CRO` (base). **Record:** `65c3977c66`.
**Lane:** estate / infra on `ajb_workspace`. **NOT a CRO research seat** — Rule 13 puts `infra/*` with
DT/AE. Suggested serial: an AE or DT `~lane` instance, one project only (Rule 27 seating).

> **This is the only item on the 41-call sheet that was BROKEN rather than UNDECIDED.**

---

## The work, in priority order. Do them in this sequence.

### 1. C2 REPAIR — `motif_family` is 0 of 45 resolved

**Measured:** composer artifact, graph vintage `7915165637360454576`, **45 of 45 UNRESOLVED**.

**Blast radius, three seats:** it degrades `~D`'s C4 suggestion seam to `BASIS_ABSENT` enrichment ·
it sits as an open cell in `~B`'s freeze (B plan §3.3) · D-9 rules it **fixed-in-sequence, not
dropped**, which makes it a predecessor to `~A`.

**`~B` §3.3 already specifies TWO remedy options and calls the work *"bounded, not deep semantic
work."*** **CHOOSE BETWEEN THEM AT THE LANE, NOT BEFORE** — that choice needs the code open.

⛔ **A POLICY CONSTRAINT BINDS THIS REPAIR (R-16, ruled the same night):** C2 equivalence is
**pinned identity or an explicit versioned mapping ONLY.** No heuristic motif-family substitution.
Every other resemblance stays `UNKNOWN`/`PROPOSED` and **cannot write canon.**
**`~B`'s reasoning, which is the load-bearing part: 45/45 unresolved is a MECHANISM defect, and a
mechanism defect is not evidence for an equivalence POLICY.** Repair the join; do not let the repair
quietly become semantics.

### 2. C3.i ANCHOR-NODE COVER PROMOTION

Deterministic cover = **1,255 structures in a CVO harness**; the production derive still emits
`FROZEN_CONTROL 4`. `~D`'s seam currently reads the harness artifact rather than production. Promote
the cover so the production path is the one consumers read.

### 3. THE SUBSTRATE MIGRATION — `node.layer` ONLY

Spec: `org/tier1_exec/4.0.0_SA_CRO/deliverables/SUBSTRATE_MIGRATION_SPEC_20260824.md`
(`30977ff0e5`, amended `69f3f82bb1`). `MIGRATION_GATES_B0` evaluated **TRUE on four clauses**.

⛔ **READ §6a BEFORE TOUCHING ANYTHING. THE SPEC WAS WRONG ON FIRST PUBLICATION AND I AMENDED IT.**

```
edge.layer :  aws 24,475 · ms 11,979 · semctl 5,049          41,503 edges, 3 values
node.layer :  portal 11,338 · ms 6,006 · aws 2,075 ·
              pipeline 1,337 · semctl 23                     20,779 nodes, 5 values
```

**Same field name. Same graph. DIFFERENT AXES.** `semctl` is 23 nodes and 5,049 edges; `portal` is
11,338 nodes and ZERO edges. `edge.layer` records **WHICH PRODUCER RAN**, not endpoint substrate.

- **IN SCOPE:** `node.layer` only. Every count in the spec's §2 value map is a NODE count.
- ⛔ **FORBIDDEN: applying the `layer` → `substrate` rename to `CloudEdge`.** A table-blind rename
  asserts substrate semantics on a producer-identity field — **strictly worse than today**, because
  afterwards the name positively misdescribes it and the reader has no tell.
- **The honest end state is two differently-named fields:** `CloudNode.substrate` and
  `CloudEdge.layer`. Naming the edge axis is a separate Rule-24 act with its own record.

**THE SHARPEST ITEM IN THE SPEC, do not skip it:** `derive_runner.py:1323` defaults a layer-less node
to `layer='aws'`. Under the new model that default **asserts a REAL value for an UNKNOWN one**, and
`aws` is real — so the mistake is **indistinguishable from a correct assignment downstream.** The
default must become an explicit `UNRESOLVED`, never a substrate value, and the `UNRESOLVED` count
gets **printed** and is a finding if non-zero.

**Also required:** `NODE_TYPE_LAYER` at `derive_runner.py:2052` is a **CVO-SIGNED FROZEN BASELINE.**
**CVO must re-sign.** Changing a signed baseline needs the signer, not whoever has write access.

### 4. THE MANIFEST-LEDGER DISARM — `~D`'s ARMED surprise item

**ARMED, and it has had no disarm owner all session. This spawn is that owner.**

The runner's unconditional manifest write is real but **UNHARMED TO DATE**. The defect is that
**the ledger cannot distinguish a reset-with-new-content (PENDING correct) from a reset-with-nothing-
new (PENDING = clobber)** — the discriminator lives in the `daily/` object's version list, which no
ledger reader consults.

**Disarm shape:** carry the superseded verdict forward in the new manifest so the oracle itself shows
a re-adjudication. **DISARMED ≠ REMEDIATED — two states, two owners, two clocks.**

---

## Acceptance — what a correct run must SHOW, not assert

1. **Denominators close.** Post-re-derive counts sum to the node total, with the `CLASS_GRAIN`
   population (19 `C2Motif` + 4 `C3System` = 23) reported as a NUMBER, not omitted.
2. **No node carries a defaulted substrate.** `UNRESOLVED` count printed; non-zero is a finding.
3. **The 1,360 frozen residue nodes have moved.** `pipeline` and `semctl` measured unchanged across
   08-19 → 08-24; **if they are still unchanged after the re-derive, the migration did not run.**
4. Column and contents agree — no half-migration state.
5. **A positive control:** at least one node of each new value verified BY QUERY, not by reading the map.
6. **CVO re-signs.**
7. C2: report resolved / unresolved **with the denominator**, not "fixed."

## Law that binds this lane

Rule 26 — **the apply runs on the device that owns the work; never ferry an apply across fabrics.**
Rule 1/NEVER#4 — Terraform only, via `safe-apply.sh`, never bare. Rule 4 — source map. NEVER#6 — a
begun deploy **finishes in-session or rolls back loud**; open a deploy-completion ledger entry at
`org/critical_paths/change_management/` at deploy-start. Rule 22a — verify on the **deployed
artifact's bytes**, resolved through the build input, never by filename.

**Report to `4.0.0_SA_CRO` (base). `~B` and `~D` are waiting on item 1 specifically.**
