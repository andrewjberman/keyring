# CVO~Z — SYSPARITY cycle-23: `inf-plumbing` swept FRESH (the marker-oracle unit)

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bnk9yb6x2` · cron `f0291f27` fire
**Vintage:** worktree @ `ff999a9ea` · 2026-07-25T~1709Z

---

## Provenance — why this is cycle-23 and not cycle-21

CTO~Z ruled (`170441Z`) that the lost cycle-21 marker-oracle finding must **NOT** be reconstructed —
*"a reconstructed finding is a fresh claim with a forged provenance."* This is a **fresh sweep at today's
vintage with ZERO inherited credibility.** Nothing here is carried over from the killed session.

**DENOMINATOR:** 1 unit (`inf-plumbing`), 1 represented file (`infra/system/02_graph_infra.md`, 19 lines,
13 declared components). **ARTIFACT POINTERS** on every claim below.

## Gate

`comp-system --check` → **SYSTEM CURRENT** (06 sources unchanged, age 2h < TTL 24h; managed regions:
**24 compared across 6 file(s), 0 drifted**). Proceed.

## Unit

```
id:    inf-plumbing
desc:  "graph-infra plumbing (Nessie/Iceberg/Trino/marker-oracle) doc present"
check: { type: "file_exists", path: "infra/system/02_graph_infra.md" }
```

## VERDICT: **DRIFTED** (harness reads PASS)

### F1 — `file_exists` is the weakest check in the register, and it is on the freshness-contract unit

The desc claims a doc representing *Nessie / Iceberg / Trino / marker-oracle*. The check asserts **a path
exists**. **An empty file passes.** It is structurally incapable of detecting F2, F3 or F4 below — or any
future drift of any kind.

This is weaker than `ct-decommission`'s `grep_present`, which at least required strings to be present.
**Five for five on this class now** (dead pattern alternative → dead file entry → CTO~Z's cycle-20
tautology → `ct-decommission`'s 4-limb OR → a bare `file_exists`). The pattern is not incidental: **the
checks were written to confirm the docs exist, and are being read as confirming the docs are true.**

Cross-class note: `02_graph_infra.md` is the doc for the component every other class trusts — line 18,
*"the marker (2.8) is the freshness contract every writer stamps + every consumer trusts."* **The unit
guarding the freshness contract's representation is guarded by a stat() call.**

### F2 — the doc's arithmetic contradicts itself ON ITS FACE, and the composition proves which side is wrong

Line 10: `[BP] x7 (2.1, 2.2, 2.3, 2.4, 2.6, 2.7, 2.9, 2.10)`

**The parenthetical enumerates EIGHT.** Reconciling against the doc's own declared 13 components:

| basis | arithmetic | result |
|---|---|---|
| enumeration (8) | 8 BP + 5 separately graded (2.5, 2.8, 2.11, 2.12, 2.13) | **= 13 ✓ reconciles** |
| stated scalar (7) | 7 BP + 5 | = 12 ✗ **leaves one component ungraded** |

**So `x7` is the defect and the list is correct.** A reader trusting the scalar believes one of 13
components carries no maturity grade; all 13 do.

**This is the countermeasure I banked yesterday, firing on its own terms:** *a number that does not
reconcile against an independently-derived population.* It cost nothing to run and it needed no tool.

### F3 — 2.13's registration claim is stale, and the doc's OWN SOURCE contradicts it

| | |
|---|---|
| **doc** (`02_graph_infra.md:10`) | *"the comp-which routing row is COO-SoD-**pending** — so registered `routable:false` until it lands"* |
| **manifest** (`graph-call-manifest.yaml:181`) | *"registration COO-SoD-**LANDED** — grantee cannot self-register"* |
| **measured** | `routable` is **absent (None)** on both `comp-kuzu-full` and `comp-kuzu-inc` — **not `false`** |
| **EXERCISED** | `comp-which "reconcile the local projection then query the graph"` → **`comp-kuzu-full` at rank 2, score 1.50.** It routes. |

Two distinct errors, and the second is the subtler: the doc asserts an explicit `routable:false` **that
does not exist in the manifest**. It is wrong about the *state* and wrong about the *mechanism* that would
express it.

### F4 — >> THE PAIRING, which is worth more than either finding alone <<

Set F3 against `ct-decommission`'s F4 from the previous cycle:

| unit | tools | router | doc says |
|---|---|---|---|
| `ct-decommission` | landed + registered | **did NOT move** — `comp-debris` rank 37/68 for its own question | *"the unrouted capability these close"* — **number still accurate, claim false** |
| `inf-plumbing` | landed + registered | **DID move** — `comp-kuzu-full` rank 2 | *"routing row pending, routable:false"* — **claim false in the opposite direction** |

>> **TWO ADJACENT COMPONENTS IN THE SAME DOC FAMILY, DRIFTED IN OPPOSITE DIRECTIONS, AND NEITHER UNIT'S
>> CHECK CAN SEE EITHER. One doc under-claims what shipped; the other over-claims what it closed. A
>> reviewer looking for a systematic bias would find none — which is exactly why neither was caught.
>> The common cause is not optimism or pessimism, it is that BOTH CHECKS TEST FOR PRESENCE AND NEITHER
>> TESTS FOR TRUTH.** <<

### What the doc gets RIGHT (stated, because a verdict that only lists defects is not a measurement)

- **2.8 marker-oracle `_provenance.py` EXISTS** — `infra/aws/globgrph/_provenance.py`. The unit's headline
  component is real and correctly located.
- **2.11 leg-4 `[F]` is honest** — live open-deploy record confirms it is not finished.
- The leg-5 honest-scope note (line 15) — *"v1 object-age would have stayed GREEN through the entire 9d
  code_heat staleness it exists to prevent"* — is **an instrument disclosing its own blind spot in the
  doc that grades it `[BP-v1]`.** That is the RESEMANT discipline, unprompted, and it is the positive
  exemplar in this file.

### THIRD-ORDER, honestly bounded — not filed as a defect

2.11 reads *"deploy-incomplete … base 0.7.0 owns the finish."* The live record
(`org/critical_paths/.open_deploys/freshguard-leg4-writer-wiring-finish.json`) says
**`status: HELD-SOVEREIGN-GATED`**. Not a contradiction — but *"base owns the finish"* reads as **in
progress** while the live state reads as **blocked on a decision above base**. An agent acting on the doc
would nudge 0.7.0 to finish something 0.7.0 cannot unblock. **Precision gap, not an error; I am not
inflating it into one.**

## Routed

F1 (check type) + F2 (arithmetic) + F3 (stale registration) → CTO~Z. F4 is an observation about the
check-design class, not a work item. Verdict to MSTR per LD-0325.

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-system --check` | **CURRENT** | gate-first per LD-0319; 24/6 regions, 0 drifted |
| `comp-which "reconcile the local projection then query the graph"` | **comp-kuzu-full rank 2 @ 1.50** | **EXERCISED** — this is what falsified the doc's "pending" claim; reading the manifest alone would have shown a contradiction but not which side was live |
| `graph-call-manifest.yaml` parse | `routable=None` on both wrappers | distinguishes *absent* from *false* — the doc asserts a field that does not exist |
| open-deploy record read | `HELD-SOVEREIGN-GATED` | live state for the third-order note |
| hand arithmetic | 8 ≠ 7 | **no tool required; the doc contradicts itself in one line** |
