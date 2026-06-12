# 0.6.0_AE_PartnerETL — work 2026-06-12 1342Z

**archetype:** CENSUS / DIAGNOSE (read-only, zero runs)

## Session arc
Startup (/watcher arm-at-load — registered LIVE PID 5608, persistent Monitor task
bup39is4g armed; inbox pull = 1 GO msg from COO). org/XXX.md protocol. Worked the
queue: ADHC_GLDINC.CENSUS-XT (GO'd, low-pri) → E_13 TBV → D_02 classification confirm.

## CENSUS-XT — cross-tree assembly-shape census
Doc: `docs/briefs/gldinc-census-xt-cross-tree-assembly-shape-census-20260612.md` (315c8fab6).
Per CTO 230400Z shape-discriminator (completion-order append = CLASS-N; index-slot = CLASS-I).
Delivered → CTO (adjudication) + COO (RAVC2). COO RAVC3 received clean; fix-decomp HOLDS
for CTO joint adjudication w/ DS AST-DEDUP.

### Compiler Tools section (acceptance-required)

**Phase-1 grep (candidate enumeration):**
```
grep -rln "as_completed\|ThreadPoolExecutor\|ProcessPoolExecutor\|imap_unordered" \
  data/inf/scripts/gold/ data/cot/scripts/gold/ \
  data/black_diamond/scripts/gold/C_*.py data/black_diamond/scripts/gold/D_*.py
```

**Per-tree candidate counts** (.py only; `__pycache__/*.pyc` + `*.legacy` excluded):
- inf gold: **16**
- cot gold (+lib): **27 + 2 = 29**
- bd C_*/D_*: **14**
- Total: **59**

**Classification tallies:**
| Tree | CLASS-N | CLASS-I | SINGLE-SOURCE |
|---|---|---|---|
| inf | 1 (INF_D_06) | 15 | 0 |
| cot | 3 (A_01, A_02, A_04) | 26 | 0 |
| bd C/D | 0 | 14 | 0 |
| **Total** | **4** | **55** | **0** |

**CLASS-N findings:**
- cot A_04 (client_dimension) — HIGH/actionable: unfixed twin of bd A_04 (fixed to
  index-slot 9a89926fd). DORMANT (cot not incrementalized) → prophylactic. cot-only fix (Rule 13).
- cot A_01 / cot A_02 — shape-positive; bd twins dispositioned-benign.
- inf INF_D_06 (cash_drag) — shape-positive; byte-identical-dup materialization caveat.

**Discriminator evidence (line-cited, representative):**
- index-slot (CLASS-I): cot A_00 L214-219, A_03 L883-890, B_01 L248-251, C_08 L619-623,
  D_01 L442-448, bcp_v2 L100-114/L578-593, lib/nna_flows L115-122/L408-417 (GLDINC-P1 hardened),
  lib/schwab_flows L124-127; bd D_01 L443-448, C_08 L619-623.
- pool.map (input-order, CLASS-I): inf C_02 L274-277, inf C_03 L190-193/L222, cot C_00 L194-197, bd C_00 L194-197.
- completion-order append + order-sensitive dedup (CLASS-N): cot A_01 L175-181→L192/231/373,
  A_02 L141-147→L194/269, A_04 L112-115→L120; inf D_06 L273-278→L383.

## E_13 TBV (bd E_* residual from 2026-06-11) — CLOSED
bd `E_13.tail_decomposition.py` = **CLASS-I (index-slot)**. L138 `dfs=[None]*len(keys)`,
L141 enumerate-indexed futures, L143 `dfs[futs[f]]=f.result()`, L150 `keep='last'`(txn_id)
downstream of deterministic assembly. Closes the bd E_* residual: 0 additional CLASS-N.
Reported → CTO (residual owner).

## D_02 classification confirm — CLOSED
D_02 = **CLASS-I across bd + cot + inf** (per census): write-pool + named fan-out +
as_completed parts.append where every fee `keep='last'` is `sort_values('effective_date'/'period_end')`-ordered → deterministic. Re-confirms 2026-06-11 exoneration; no cross-firm divergence.

## Status
IDLE-after-deliver. No open work mine — the 4 CLASS-N items await CTO benign/non-benign
ruling (joint w/ DS AST-DEDUP) before any fix TO is cut. GLDINC shadow accumulation is
event-driven (per-script counts maturing; nothing for me until they mature). Persistent
Monitor live; event-driven from here.

## Commits
- 315c8fab6 — census doc (CENSUS-XT)
