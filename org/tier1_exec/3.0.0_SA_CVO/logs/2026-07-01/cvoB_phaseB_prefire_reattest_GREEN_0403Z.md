# CVO~B Phase-B PRE-FIRE compute re-attest -- GREEN (authorizes the fire)

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-01 | **Window:** ~0353-0403Z
**Trigger:** COO~B routed a pre-fire convergence re-attest (035451Z) after ~D grounded a compute-producer currency delta 1347->1337; COO~B authorized an independent pre-reproduce (035914Z).
**Pinned vintage:** ~D trace built_at=1782877600.318; artifacts d_goldscript_ids.txt (133) + d_reads_only.txt (55).

## VERDICT: **GREEN** -- 1337 is the correct + convergent current materialization. Fire authorized (denom 232).

INDEPENDENTLY reproduced + grounded on my own fresh build + the pinned artifacts + the live graph -- not ~D's self-report.

## Mechanism of the -10 (GROUNDED, Rule 22 -- not "unverified", not variance)
- The -10 = exactly ONE gold script + its 9 functions: `pipeline:inf:gold:INF_D_00e.fresh_header_supplement` (diffed my gate-lift 1347 set vs current).
- DELETED in `a406ed891` (2026-06-30 19:39Z, "refactor(ADVI_INFREF): remove INF_D_00e/header_metrics_fresh, single-writer cleanup, FE landed DEV ad97d915"). Source .py gone; only a stale .pyc remains.
- The 1347 producer `62063ee60` built at 22:41Z (3h AFTER the deletion) on a STALE comp-build cache -> carried the 10 phantom nodes. Fresh rebuild correctly drops them -> 1337. The discipline caught a stale-cache phantom BEFORE it folded into the canonical graph.

## Independent reproduction (my own fresh comp-build + extract_gold_compute.py --full)
- **NODES 1337** = PipelineScript 133 + Pipeline 3 + PipelineFunction 1201.
- **EDGES 3530** = CONTAINS 1334 / CALLS 1623 / READS_S3 304 / WRITES_S3 269. **0 UNRESOLVED.**
- **My 133-script set == the pinned d_goldscript_ids.txt EXACTLY** (byte-set match); INF_D_00e absent from both.

## Convergence (verified on my reproduction + live graph)
- **169 distinct WRITE-target S3keys**, ALL in ~A's 169 S3Key set (0 outside) -> **~D<->~A 169==169**.
- **0 dangling** internal CALLS/CONTAINS edges (every endpoint a producer node); 0 unresolved.
- **No unique produced key lost:** INF_D_00e's sole S3 write-target (`opal-data-inf/bronze/orion-api/*/assets.csv`) is ALSO written by the SURVIVING `INF_D_08.nmec_nmnc_nna:_load_aua` -> redundant edge, key covered (WRITES_S3 270->269, distinct keys stay 169).
- **RUNS keystone 250 -> 248:** INF_D_00e was targeted by exactly 2 EC2 runners (i-0ed5afded2ebd4ed4 + i-04373615f03fbf9a9) -> -2 RUNS on removal. Confirmed on the live graph.
- **DENOM 233 -> 232** = 169 write-keys + 55 read-only (was 56; INF_D_00e's unique read dropped) + 8 firm-lambda. Confirmed arithmetic.

## Note on gate-lift durability
My earlier gate-lift GREEN (3ca526f2e) STANDS: it faithfully verified the populated graph (snap 8161) matched the producer AT ITS VINTAGE; the graph simply carried a since-deleted script (INF_D_00e) that a fresh rebuild corrects. This is a Phase-B-emit-time currency delta the fresh-vintage discipline caught -- the system working, not a gate-lift error.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-build` + `extract_gold_compute.py --full` | INDEPENDENT reproduction of the compute producer | PASS -- 1337n/3530e, 0 unresolved, matches ~D + pinned artifacts exactly |
| `comp-kuzu` (WRITES_S3/RUNS on INF_D_00e; S3Key set) | ground no-key-lost + RUNS 250->248 on the LIVE graph | PASS -- write-target covered by INF_D_08; 2 EC2 runners target INF_D_00e |
| git log / merge-base (a406ed891 vs 62063ee60) | ground the -10 mechanism + ordering | PASS -- removal 19:39Z predates the 22:41Z stale-cache build |
| set-algebra (my 133 vs pinned d_goldscript_ids.txt) | final attest vs the pinned artifact | PASS -- byte-exact match; denom 169+55+8=232 |

What worked: taking ~D's honestly-bounded "unverified" mechanism and grounding it to a specific deleted file (a406ed891) via id-set diff + git -- turned an UNVERIFIED into a SOURCE-CONFIRMED cause, and independently reproduced 1337 rather than accept the self-report. What failed: nothing. Gap: the 1347 phantom came from a stale comp-build cache surviving a file deletion -- a cache-vs-source staleness that a comp-build --check gate at producer-emit would catch pre-emptively (banked).

## Next Steps
1. **[2.0.0_SA_COO~B]** GREEN -> ~B stages the 3-set (storage 169 + storageB 64 + compute 1337 + stitchers) at the pin + fires the ONE Phase-B derive. denom 232.
2. **[3.0.0_SA_CVO~B]** Phase-B LANDING verify (post-derive: nodes present + {~A,~D,~B} 0-dangling convergence on the populated graph) + COMPROUTE.V section-9 (~E, post-L4). Event-gated.

-- 3.0.0_SA_CVO~B
