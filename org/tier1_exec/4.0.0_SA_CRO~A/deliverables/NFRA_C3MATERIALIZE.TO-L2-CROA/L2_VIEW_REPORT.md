# NFRA_C3MATERIALIZE L2 — independent STRUCTURE and BEHAVIOR views

**Task:** `NFRA_C3MATERIALIZE.TO-L2-CROA`
**Executor:** `4.0.0_SA_CRO~X` (historical path retained by the task face)
**Anchor:** `bb01a202721f9c3a719a3a662319cebc194a1720`
**Artifact digest:** `61f12d72056daa25d6ff300bccec640e9c1004446258006dae191eff6449904d`
**File SHA-256:** `1c45ba56622048f7ba66209550dc4b385dd1f9a84ff7e162a91f6307377526d6`

## Outcome

Both required views are delivered independently. BEHAVIOR is measured and passes its discrimination gate. STRUCTURE is delivered as a failed view: its topology population is measured, but its consensus affinity is explicitly `ABSENT-NOT-ZERO` because no repository-local or installed graph-tool-class SBM producer exists. No substitute community algorithm is represented as SBM.

This is a task-complete delivery with one failed view, exactly as the face requires: a failed discrimination gate is carried, not withheld. Nothing here claims fusion, a common entity set, or a cross-view affinity.

## Measured view frame

| View | Entity denominator | Signal coverage | Matrix | Gate |
|---|---:|---|---|---|
| STRUCTURE | 19,482 edge-incident, non-`semctl` Kuzu nodes | topology 19,482/19,482; consensus 0/19,482 | `ABSENT-NOT-ZERO` | **FAIL** |
| BEHAVIOR | 3,726 file paths in at least one repeated co-change pair | co-change 3,726/3,726; Git-recency heat 3,726/3,726; propagation drift 0/3,726 | 6,841 nonzero / 6,939,675 possible pairs; all unlisted pairs are measured zero | **PASS** |

STRUCTURE scanned 20,805 non-`semctl` nodes and excluded 1,323 isolated nodes that carry no topology signal. Its 19,482 signal-bearing denominator exactly reconciles the historical prose figure; the current edge count is 36,549 versus the historical 36,513, a 36-edge vintage difference. That explains the prior count without pretending the vanished historical producer or output has been recovered.

BEHAVIOR parsed 29,301 non-merge commits at the anchor. After the declared machine-generated exclusions and the swept historical cap of 25 paths per commit, 28,963 commits were accepted. Repeated co-change means at least two shared accepted commits, yielding 3,726 paths and 6,841 positive pairs. The prior prose-only run reported 3,532 paths and 6,393 pairs at an earlier vintage; those values are historical references, not copied evidence.

## The 14 owned cells

| Cell | Field | Delivered value / evidence |
|---|---|---|
| `L2-adkg-1` | STRUCTURE.entity_set | 19,482 edge-incident non-`semctl` Kuzu node ids; denominator printed and every id serialized. |
| `L2-adkg-2` | STRUCTURE.coverage | topology 19,482/19,482 MEASURED; consensus 0/19,482 ABSENT. |
| `L2-adkg-3` | STRUCTURE.missing_flag | Every entity carries `topology_signal=MEASURED`, `consensus_affinity=ABSENT`; no absent affinity is encoded as zero. |
| `L2-adkg-4` | STRUCTURE.computation | Requested degree-corrected SBM plus consensus; refused before run 1 because the conforming producer/dependency is absent. Input digest `a323f598...`. |
| `L2-adkg-5` | STRUCTURE.reproducibility | N requested 25, N executed 0; all 25 anchor-derived seeds and the required per-run record shape are carried. |
| `L2-adkg-6` | STRUCTURE.discrimination_gate | **FAIL**: no measured affinities, therefore zero bits admitted downstream. |
| `L2-adkg-7` | STRUCTURE.failure_mode | Dependency absence is distinguishable from genuine low affinity by `ABSENT-NOT-ZERO`, N=0, and no measured matrix. |
| `L2-kedi-1` | BEHAVIOR.entity_set | 3,726 repository-relative paths participating in a repeated co-change pair. |
| `L2-kedi-2` | BEHAVIOR.coverage | co-change 3,726/3,726; heat 3,726/3,726; drift 0/3,726; 6,841/6,939,675 nonzero pairs. |
| `L2-kedi-3` | BEHAVIOR.missing_flag | Per entity: co-change and path-resolving heat MEASURED; propagation drift ABSENT. Unlisted matrix pairs are explicitly MEASURED-ZERO. |
| `L2-kedi-4` | BEHAVIOR.computation | Cosine affinity on pinned commit incidence: shared commits / sqrt(commits_i × commits_j), cap 25, repeated-pair floor 2, declared machine exclusions. |
| `L2-kedi-5` | BEHAVIOR.reproducibility | Deterministic N=1, no seed, exact Git anchor and input digest `9e89a868...`; two same-anchor runs were byte-identical. |
| `L2-kedi-6` | BEHAVIOR.discrimination_gate | **PASS**: 877 distinct positive affinities, density 0.000985781; executed all-1 constant mutant **FAIL**. |
| `L2-kedi-7` | BEHAVIOR.failure_mode | Retrieval/vacuity/constant-matrix failures are hard failures; genuine low affinity remains a measured zero inside a non-empty frame. |

## Named hazards answered

1. `graph_tool` is absent. NumPy, SciPy, and NetworkX are present, but presence of different algorithms is not evidence of an equivalent degree-corrected SBM. The STRUCTURE affinity is therefore **BLOCKING**, delivered failed, and represented as absent rather than zero.
2. `comp-heat score` is **not used** because it does not resolve its id. Heat metadata is calculated only after Git resolves each file path. `comp-drift` is a propagation-target orchestrator at another grain, so drift is explicitly ABSENT for every BEHAVIOR entity and contributes nothing to affinity.

## Reproduction

```powershell
python org\tier1_exec\4.0.0_SA_CRO~A\deliverables\NFRA_C3MATERIALIZE.TO-L2-CROA\build_views.py --anchor bb01a202721f9c3a719a3a662319cebc194a1720
python org\tier1_exec\4.0.0_SA_CRO~A\deliverables\NFRA_C3MATERIALIZE.TO-L2-CROA\run_acceptance.py
```

The producer was run twice against that exact anchor. Both generated `L2_VIEW_ARTIFACTS.json` with SHA-256 `1c45ba56622048f7ba66209550dc4b385dd1f9a84ff7e162a91f6307377526d6`. Acceptance returned 7/7.

## Declared exclusions

- FLOW and SEMANTIC are not in this task order.
- No common spine, bridge, fusion, or cross-view affinity is asserted; those are downstream L3 work.
- No historical 2026-08-26 SBM result is promoted to current evidence; its producer and output are absent.
- No deployment or external write occurred.
