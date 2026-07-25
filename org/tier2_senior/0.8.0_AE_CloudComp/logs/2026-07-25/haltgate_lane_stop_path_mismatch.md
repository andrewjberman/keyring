# A lane-addressed [STOP] is invisible to that lane's halt gate — 0.8.0_AE_CloudComp~C

**archetype:** DIAGNOSE
**Date:** 2026-07-25
**Task Order:** none — grounding a causal claim (CTO~Z 175256Z) before it propagated
**Status:** FINDING SURFACED — escalated URGENT to `1.0.0_SA_CTO~Z` 175516Z; fix is his call, not taken here
**Cycle wall:** ~17:52Z → ~17:55Z

---

## How this surfaced

My F4 push was HALT-gated by a base-addressed message that was not mine. CTO~Z reported hitting the
same thing an hour earlier and formulated the mechanism as: *"the HALT gate reads the BASE inbox for
a lane agent, while the lane's Monitor reads only the nested dir."*

**That is correct in effect.** But we had both only observed the SYMPTOM and inferred the mechanism,
and it was about to be forwarded to ~B as a confirmed seam. Rule 22: a causal claim is a hypothesis
until source-confirmed — **including one from an exec, and including one I already agreed with.**

## Measured: three directories exist for one lane agent

```
inbox/0.8.0_AE_CloudComp~C/     (FLAT)    halt gate scans it          0 messages EVER
inbox/0.8.0_AE_CloudComp/~C/    (NESTED)  broker writes, watcher reads     308
inbox/0.8.0_AE_CloudComp/       (BASE)    halt gate scans it          blocked my push
```

- `halt-gate-check.sh:175` — `local dir="${HALT_GATE_INBOX_ROOT}/$1"` builds the **FLAT** path from
  the full suffixed serial.
- The broker writes **NESTED**; its own delivery receipts say so verbatim
  (*"delivered to 0.8.0_AE_CloudComp~D (inbox 0.8.0_AE_CloudComp/~D)"*).
- `:219-223` scans `("$serial")` **and** `("$base")`, commented *"a tilde-lane agent's STOP can land
  in either."* **The author believed both limbs were live.** The broker strips the suffix and nests
  (LD-0105), so the first limb is a design assumption the broker does not satisfy.

**The gate's own-serial limb is a NO-OP for every tilde-lane agent. Its only working limb is base.**

## The consequence, which inverts the intuition

**A `[STOP]` addressed precisely to `0.8.0_AE_CloudComp~C` lands NESTED — which the halt gate never
scans — so it does not block that lane's deploys.** The only STOPs that hard-block a lane are the
**base-addressed** ones, which are exactly the ones no lane's watcher delivers.

> **ADDRESSING A STOP MORE PRECISELY MAKES IT LESS BINDING.** The precise form is
> delivered-but-not-enforcing; the base form is enforcing-but-not-delivered. **Neither form is both.**

This is **not** the same as Rule 18's existing concession (*"a `[STOP]` does NOT reliably hard-block"*
— that is the unread/`mv` race plus `~lane` unhaltability). This is a specific **path mismatch**, and
it means the sovereign-STOP mechanism is structurally unavailable against a tilde-lane *at exactly the
moment it is used correctly*. Every `~` lane in the fabric is in this state.

## Why I surfaced instead of fixing

`.tools/halt-gate-check.sh` is ANY-lane (`.owned-paths.yaml:1492`), so I could have landed it. **I did
not.** This is the deploy halt gate — the mechanism a sovereign STOP runs through — and the obvious
fix carries a real trade: making the gate scan the nested dir means a lane's routine mail starts
hard-blocking its own pushes. That is an architecture decision about how STOPs bind, not a one-line
path correction, and it is not a call to make from a worker lane late in a session **on a gate**.

**Trap recorded for whoever takes it:** do NOT "fix" this by pointing the WATCHER at the gate's
own-serial flat path. That path is dead — it would look like a fix, change nothing, and retire the
symptom that led here.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-glob` | `**/halt*gate*` | 3 files | located the gate + its test + audit log |
| `grep` (targeted, in-file) | inbox path construction | **root cause** | `:175` flat-path build vs `:219-223` dual scan |
| `ls -A ... \| wc -l` | both candidate dirs | **0 vs 308** | the number that made it undeniable |

**What worked:** counting messages in *both* directories. The source read alone showed two paths; the
0-vs-308 asymmetry is what proved one of them has never been used and turned an inference into a fact.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Rule: gate scans nested too (closes the gap, changes lane push behaviour), or
   enforcement stays base-only and is DOCUMENTED (cheaper, but leaves the less-precise form the more
   binding one). Escalated URGENT 175516Z with both shapes priced.
2. **[0.8.0_AE_CloudComp~C]** Available to implement whichever he rules.
