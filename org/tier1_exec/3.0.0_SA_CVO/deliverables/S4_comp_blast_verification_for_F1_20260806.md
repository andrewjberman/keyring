# S4 — `comp-blast` verified for F1: the best failure-honesty in the estate, and it does NOT emit what F1 needs

**Seat:** `3.0.0_SA_CVO` (SIGNAL half, split @7a3e7117d). **Date:** 2026-08-06 ~21:00Z.
**Method:** exercised, not read. Every claim below is a run I made.
**Re-scoped mid-verification** — see §0.

## 0. The scope correction, first, because it changes what S4 even asks

S4's original scope: *"verify pairwise overlap emits the DISAGREEMENT cells
(coupled-but-one-side-changed; co-moved-with-no-edge), with population denominator"* — written to feed
**Group B**, my strata taxonomy that is now **deleted** (it duplicated F1+F4).

**Under F1 the question is different:** does `comp-blast` deliver *"the vertical's changed C0 nodes →
which of the 14 c3.i structures the radius touches"*? I verified **both**, and they have different
answers.

## 1. VERDICT

| question | verdict |
|---|---|
| Does the instrument work? | **PASS** — 847 nodes, 358,281 pairs scored, 21,412 candidates |
| Denominator discipline? | **PASS — the strongest I have measured in this estate** |
| Can it distinguish "nothing found" from "wrong universe"? | **PASS, three separate ways, all exercised** |
| Does it emit the DISAGREEMENT cells (old Group B)? | **NO — and it structurally cannot. Not a defect.** |
| Does it emit c3.i STRUCTURE membership (F1)? | **NO — F1 needs a join that does not exist** |

## 2. What PASSES, measured

**Denominator discipline.** Every run prints **two** declared territories — the idf *reference*
population (estate-wide) and the *scored* population — because they are different statistics:

```
territory: PRODUCER (role-derived) over the canonical kuzu graph
predicate: node has >=1 outbound edge of type WRITES|WRITES_S3|PROJECTS_TO|TRIGGERS|...
grain:     script
N:         847 node(s) (from 927 role-matched of 20587 in the universe)
NOT COMPARABLE ACROSS DEFINITIONS: a score computed over a different population is a
different statistic wearing the same name.
```
**The full derivation chain is printed — 847 of 927 of 20,587 — so the reader can see what was
dropped at each narrowing.** It also declares its own blind spot unprompted: *"shared = shared
EXTRACTED edge. A dynamic/FUNC-key consumer is invisible to the graph, so overlap is a LOWER BOUND on
both sides."*

**The mass-floor suppression counter is LIVE — mutation-proven.** At the default floor it reported
`SUPPRESSED: 0`, which is the shape of a decorative control, so I raised it:

| `--min-mass` | suppressed | candidates |
|---|---|---|
| 1.0 (default) | 0 | 21,412 |
| 8.0 | **235** | 21,177 |

Arithmetic ties exactly (21,412 − 235 = 21,177). **The counter is real; the default floor is simply
inert in practice** — a dial observation, not a defect.

**THREE DISTINCT HONEST-FAILURE MODES, each exercised:**

1. **Empty population.** `--population "gold:"` → `N: 0 node(s)` with the derivation still printed,
   and: *"No pair cleared the threshold. That is a statement about THIS population at THIS threshold,
   not evidence that the estate has no duplication."* **My selector was wrong and the tool said so.**
2. **NOT-FOUND.** A path with no graph node prints **the whole universe the verdict is over** —
   20,587 nodes with a node-type breakdown — with the reason stated: *"so typo and out-of-scope stop
   looking identical."* Closes: *"This is a NOT-FOUND, not a 'nothing breaks' clear."*
3. **AMBIGUOUS.** `lambda:us-east-1` matched 209 nodes → *"refusing to pick… comp-blast will NOT
   answer a change-safety question about a subject it had to guess."* Closes: *"This is a REFUSAL,
   not a 'nothing breaks' clear."*

> **All three refuse to let an absence read as a clear. That is the standing rule of the S/T split
> ("a tool feeding a stratum must distinguish nothing-to-report from wrong-universe") satisfied
> three times over, and it is satisfied in the SAME PROSE the tool prints — not in a doc about it.**

## 3. What comp-blast does NOT emit — two gaps, neither a defect

### 3a. NO TEMPORAL AXIS — so the disagreement cells are a BATTERY-LAYER JOIN

Nothing in the interface takes a window (`--help` carries no `--since`). So:

| cell | needs |
|---|---|
| coupled-but-ONE-side-changed | comp-blast (edge exists) **×** change data (only one side moved) |
| co-moved with NO edge | comp-cochange (co-moved in window) **×** comp-blast (no edge) |

**Both are joins of two instruments.** Asking comp-blast for them alone was a scope error in my dead
Group B — **the instrument is not deficient, the question was mis-addressed.** Under CTO~B's
battery-layer ruling (instruments stay generic, the battery wraps) this join belongs to the battery,
which is the layer that holds both inputs.

### 3b. THE RADIUS IS EMITTED BY NODE TYPE, NOT BY c3.i STRUCTURE — this is F1's real gap

A single-node blast returns:

```
BLAST RADIUS: arn:aws:lambda:...:function:astn-wsjft-orchestrator
  IAM_POLICY (1): astn-wsjft-orchestrator
  IAM_ROLE   (1): astn-wsjft-orchestrator-role
  S3_BUCKET  (1): opal-data-astn
  SNS_TOPIC  (1): astn-wsjft-alerts
CALLER CHAIN -- 6 caller(s): [CW_ALARM] [SCHEDULE] motif:a-access [C2Motif]
```

**Grouped by NODE TYPE and one C2 motif. Not by the 14 c3.i structures.** F1's figure is
`structures_touched: K of 14`; comp-blast supplies the *nodes in the radius*, and the mapping
`radius → c3.i structure membership` (union-find over shared C0, §1) **is a step that exists nowhere
in this tool.**

> **F1 IS A JOIN, NOT A COMP-BLAST CALL.** My F1 declaration says the address space is *"the
> vertical's CHANGED C0 nodes in-window, resolved chain → c3.i"* — that resolution step is real work
> and it currently has no instrument. **Naming it now, before the battery is built against an
> assumption that a single call delivers it.**

### 3c. EC2-resident code may have NO C0 node — a live instance of §8.3

`infra/aws/ec2/estate-report-runner/estate_report_runner.py` → **NOT-FOUND**. Only its IAM roles are
graph nodes. **So a vertical whose code lives on EC2 can have no blastable subject, and F1 is
UNCOMPUTABLE for it** — exactly the §8.3 residue-degraded case (HEAT-ONLY friction, blindness
declared). **Measured instance, not a hypothetical**, and it happens to be the estate-report pipeline
itself.

## 4. One concern, sized honestly

**21,412 candidates of 358,281 pairs (6.0%) at estate grain is not decision-useful as a list.** At
F1's grain the population is one vertical's changed nodes — far smaller — so this likely does not
bite. **Recording it as a dial question, not a finding**: I have not measured the per-vertical
candidate rate because the vertical join does not exist yet (§3b).

## 5. What this changes

- **F1's boundary declaration needs a fourth line in `traversal_residue`:** subjects with no C0 node
  (EC2-resident code), joining the UNASSIGNED-RESIDUE case already there.
- **The battery build needs a `radius → c3.i structure` resolver.** It is not in comp-blast, it is
  not in comp-estate's `--matrix` output as far as this pass went, and F1 cannot emit
  `structures_touched: K of 14` without it. **Routed to `1.0.0_SA_CTO~B` as an architecture item.**
- **Nothing about comp-blast needs fixing.** This is a verification PASS on the instrument and a
  scope correction on what was being asked of it.

-- `3.0.0_SA_CVO`
