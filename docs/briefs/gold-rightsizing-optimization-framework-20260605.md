# Gold Right-Sizing — Two-Axis Optimization Framework (Andrew directive 2026-06-05)

**Context:** governs ADHC_GLDINC (gold incrementalization) + R3 (machine right-size). Andrew's framing of "true structural right-sizing" as a joint cost-optimization, not two separate efforts. Folds into the GLDINC build-PRD design.

**Core thesis:** the true structural right-size is the **joint (algorithm × machine) point that minimizes total cost = Σ(runtime_i × machine_rate)** — not "most incremental algorithm" and not "smallest machine" in isolation. The two axes interact, and the algorithm axis is the lever that unlocks the machine axis.

## Axis 1 — Script-level compute efficiency (the algorithm axis)

For each script: incremental vs full-aggregate (the Phase-0 3-bucket classification). **Key extension** — before concluding a script is FULL-RECOMPUTE-INHERENT, apply the **temporal-partition / freeze-baseline test:**

- **Pattern:** freeze the *closed* historical period into a materialized baseline (e.g., everything before June 2026 = frozen aggregate, computed once). Run **incremental dailies against only the OPEN current period** (June dailies touch only June). At the period boundary, do **ONE full run to roll the open period into the frozen baseline** (freeze June into history going into July) and begin light July dailies.
- **Effect:** converts "recompute the whole history every night" into "recompute only the open period nightly + rebaseline once per period." A firm aggregate / ranking / distribution that *looks* inherent is usually a **frozen-historical-baseline + incremental-current-period-delta + periodic-rebaseline** — i.e., INCREMENTAL-WITH-RECONCILE with a cheap reconcile.
- **Action:** re-examine the 7 Phase-0 FULL-RECOMPUTE-INHERENT scripts (D_00/D_00b/D_00c/D_01/C_05/C_07) through this lens — most are likely temporally-partitionable. Reclassify.
- **Correctness (0.4.0_DS rigor):** late-arriving / restated data for a *frozen* period invalidates the baseline → needs a **restatement trigger** (re-freeze the affected closed period). The periodic full rebaseline is the standing reconcile that catches drift. This is the subtle part — design it, don't hand-wave it.

## Axis 2 — Machine-sizing as a cost function (the economics axis)

The objective is **minimize total $ = Σ(runtime × machine_rate)**, NOT minimize machine size. Each (script, machine-size, algorithm) point has a runtime; model runtime as a function of machine + algorithm ("a series of optimizable regressions") and find the cost-minimizing point.

- A **bigger box** (more RAM, load-everything-in-memory) may run faster.
- A **smaller box** (memory-frugal: threaded / chunked / incremental) may run slower.
- A smaller box only WINS if its runtime penalty doesn't outweigh its cheaper rate.
- **Andrew's break-even example:** 1 hr on a $3/hr box = $3. A $2/hr box only beats that if it finishes in **< 1.5 hr** (1.5 × $2 = $3 break-even). Every minute past 1.5 hr is a worse deal than the bigger box.
- **Action:** fit per-script (+ whole-chain) runtime vs (machine, algorithm) from the **perf_history** archive we just started collecting (per-run runtime + memory). Find the cost-minimizing (machine, algorithm) per script and for the chain. Validate on scheduled nightlies (C1) — no ad-hoc runs.

## The synergy (why this unifies GLDINC + R3)

Incrementalization (axis 1) **shrinks the working set**, which *simultaneously*:
1. lowers the memory floor → enables a smaller box (axis-2 machine), AND
2. shortens runtime (axis-2 runtime).

Both factors of the cost product improve **together** — so axis-1 is what makes a smaller box a NET win rather than a runtime-penalty loss. **A_03.positions_cube is the canonical case:** dropping its 76GB working set (materializing the whole pair×day cross-product) enables both a smaller box AND a shorter run.

**Therefore:** R3 (tonight's right-size — cut wasted cores, same algorithm) is a **first-order point** on this frontier. The *true* structural right-size is the joint (algorithm, machine) cost-optimum that GLDINC + the cost-model finds. They are one effort, not two.

## Deliverable additions to the GLDINC build (CTO bakes into the PRD)
1. Temporal-freeze re-examination of the "inherent" scripts + the restatement/reconcile design (axis 1 extension).
2. The runtime-vs-(machine, algorithm) cost model per script + chain-level cost-minimization, fit on perf_history (axis 2).
3. Treat the right-size machine choice as the OUTPUT of the cost model, not a fixed target.
