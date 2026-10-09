# 2.0.0_SA_COO~F1 drive log -- 2026-10-09 20Z-21Z, dell1 (desktop-hk1uu7n)

Scope: ADVI_FIRMBKTS (lease FULL). Seated by 1.0.0_SA_CTO~DELL1 msg 3113 (acked).

| tick (UTC) | limb | round | TOs t/T | thread | act fired |
|---|---|---|---|---|---|
| ~20:4xZ | L5 -> L6 | 1 | 0/4 | none | L5 decomposition v1 @212f7e0ff4 and ONE issuance @16a1e55ca8 (fanout 3 of 2 chains, cap 8), merged @fcaaa21b6e; rows D1-S1, D1-S2 @18a34aa1ca; slot ~1 spawned on FB-t-1 |
| ~21:0xZ | L7 | 1 | 1/4 | none | FB-t-1 VALID @fa437ba675; ruled row D1-W1-S1 (a mixed class is FAULT, never placed by its dominant kind); slot ~1 re-seated on FB-t-2 (a finished subagent is not resumable) |
| ~21:1xZ | L7 | 1 | 2/4 | none | FB-t-2 VALID @bc064071aa; chain merged @864b4be61a; slots ~2, ~3 spawned on the readers |
| ~21:2xZ | drain | 1 | 4/4 | y | readers VALID, merged @3e54a3be9f and @863c9aee7b; the one real run (R1_CLOSE.md): canonical 209 of 209, legacy 19 of 209; row D1-S3 @fd11720ae7; round-close-check MAY-CLOSE; dep_stage ROUND_CLOSE |

Compiler tools: comp-find (Rule 24 token census), comp-surprise (channel rollup), to-pipeline-gate (dry runs and the
issuance), proof-of-spec-check (each instance), safe-merge (four drains), round-close-check (MAY-CLOSE).
