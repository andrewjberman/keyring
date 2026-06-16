# MOLECULE: _fold_sma_into_nonmodel() + its build()/slice_per_firm integration (build_aggregate_aua_timeseries.py) (scale: MICRO)
**archetype:** EXPLORE
**secondary_archetypes:** VALIDATE

Andrew-directed deep-dive on the unit I authored for YANG_SITTW.TO-1. Grounded against the DEPLOYED runner code (s3://opal-data-mdpf/code/scripts/backfill/) + the served artifact (json/mdpf/global), not the repo/memory.

## Unit + expected role
A pure in-place dict mutator: fold the 1c/SMA columnar series into the 1b non-model plug (`non_model_aua' = non_model_aua + sma_aua`), then drop `sma_aua`. Called once on the aggregate dict + once per partner. Expected role: make the never-widen-safe collapse at rollup time without re-running the partition builders.

## 1. Composition — what it actually is (vs declared)
Deployed fn (line 222) is byte-identical to committed HEAD (verified). Logic: `sma=series.get("sma_aua"); if sma is None: return; nm=series.get("non_model_aua") or []; folded[i] = None if both-None else (nm[i]||0)+(sma[i]||0); series["non_model_aua"]=folded; del series["sma_aua"]`. Integration (lines 419-421): runs AFTER apply_count_backfill, BEFORE the `out={}` assembly, on `aggregate` + every `partners.values()`. slice_per_firm then reads the already-folded artifact (global spreads `**aggregate`; per-firm reads `non_model_aua`, sma_aua line removed). **No declared-vs-actual drift** — docstring, name, and behavior all agree.

## 2. State — live snapshot
Served global (mtime 18:37:13Z): n_dates=413; len(non_model_aua)=len(model_aua)=len(opal_aggregate_aua)=413 (LENGTH INVARIANT HOLDS); `sma_aua` key ABSENT; `meta` carries `sma_collapsed_into_1b=True`. Fresh, in-family, distinct content. PASS.

## 3. Position in the chain
- **Upstream:** 413 `platinum/mdpf/aggregate_aua/{date}.json` partitions (each carries aggregate{opal_aggregate_aua,model_aua,sma_aua,non_model_aua} + partners + by_model), mdpf_model_registry.json (F5 names), aggregate_aua_count_backfill_pre0518.json. The fold consumes the partition-read `sma_aua` + `non_model_aua` columnar arrays.
- **Downstream:** served json/mdpf/{global,49financial,inflection}/aggregate-aua-timeseries.json -> FE getMdpfAggregateAUATimeSeriesByFirm -> ModelPortfolios.tsx. Per-firm band reads `non_model_aua` (folded). Global band reads a SEPARATE artifact (non_model_assets.json), not this field.
- **Deps/reach:** pure dict op, no new IAM. Runs in the daily-chain Stage-4 (RUNBOOK) + on-demand.
- **Seams (already run via /seams):** S1 producer->served SOUND; S3 served->FE SOUND+finding (deep-tail Global band overshoot, routed to COO/DE).

## 4. Behavior — exercised
The deployed code ran (--upload 18:37Z) producing the folded served artifact. Idempotent + re-derived-from-source: each nightly re-reads the partitions (which RETAIN their internal sma_aua) and re-folds fresh -> the fold is never persisted to partitions, only the rollup output drops sma_aua. Unhappy paths: sma_aua key absent -> no-op early-return (idempotency on a re-run of folded data); both-None date -> None preserved (honest empty); post-launch REAL sma (>=~2026-05-20) -> folded into 1b' to its real extent (per TO). All correct.

## Smell findings
| Smell | Rating | Evidence | Why it caught my eye |
|---|---|---|---|
| **Data-shape invariant changed: `sum(by_model all-classes) + non_model_aua` now DOUBLE-COUNTS SMA** | **WATCH** | served @2026-06-16: sum(by_model ALL)=1,556,827,318 (incl 24.2M sma sleeves) + non_model_aua=355,046,446 (now ALSO incl 24.2M sma) => sma counted twice. Before the fold this sum == total (non_model excluded sma); after, it = total + sma. | SMA is now represented in TWO places (by_model cohort_class='sma' sleeves + folded into non_model_aua). SAFE for every LIVE consumer (FE filters by_model sma out of the model stack + reads non_model_aua alone), but a future naive consumer summing all by_model + non_model would double-count $24.2M. The invariant flipped TRUE->FALSE. Mitigation: data_contract note (added this session). |
| Fold bound uses `len(nm)`; drops sma tail if `len(sma) > len(nm)` | WATCH | fn line: `for i in range(len(nm)): b = sma[i] if i < len(sma) else None` | Holds by construction (build pads both to n_dates; verified 413==413), but the length-equality invariant is NOT asserted. A future build-loop change that desyncs the two would silently truncate the sma tail rather than error. Cheap assert would harden it. |
| Re-fold-from-partitions each run (partitions keep sma_aua; rollup drops it) | NOTE | partitions unchanged; rollup folds fresh each Stage-4 | Correct + idempotent, but means the fabricated pre-launch sma_aua STILL lives in the 413 platinum partitions (just never served). Not wrong (the rollup is the served authority), but a partition-level reader would still see the fabricated 1c. |
| Rollup carries only 3 agg fields (dropped partner_aua_subtotal/cohort_2b_audit at read) | NOTE | agg_metrics reads 4 -> fold -> 3 served | Pre-existing (the rollup never carried subtotal/2b_audit); the /seams Global-band overshoot traces to opal_aggregate (which nets out cohort_2b_audit) vs the separate non_model_assets basis. Cross-ref the seam finding. |

## Assessment
The unit is **sound and correctly deployed** — pure, idempotent, never-widen-safe, byte-identical committed==deployed==served-producing. It does exactly what it claims. The one notable thing the deep look surfaced is the **WATCH double-count surface**: by folding sma into non_model_aua while retaining the by_model sma sleeves, the data now represents SMA twice, and the `by_model-all + non_model == total` invariant (true pre-change) is now false. No live consumer trips it (all filter by_model sma), so it is **not a defect** — but it is exactly the benign-but-surprising property worth recording before a future consumer rediscovers it as an incident. Routed: strengthened the data_contract.xml consumer note (declarative repair, my core doc); no code change needed. The length-invariant WATCH is a cheap-assert hardening opportunity (optional, not urgent).

## Knowledge-parity delta + residual
- BELIEVED (implicit, pre-change): "sum(by_model all-classes) + non_model_aua reconciles to the enterprise total." Now FALSE (double-counts SMA). Corrected in data_contract.xml `<mdpf_global_timeseries>` with an explicit "do NOT sum by_model-all with non_model_aua" consumer warning.
- Residual: the length-equality assert is unwritten (WATCH, optional). The 6/17 nightly will exercise the durable re-fold (Stage-4 on the new runner code) — standing review owned by me.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| aws s3 cp deployed runner code + served global | yes | deployed fold == committed HEAD; served sma_aua-free, length-invariant 413 holds |
| custom by_model double-count probe (python) | yes | sum(by_model ALL)+non_model double-counts sma $24.2M (the WATCH); FE-safe (filters by_model sma) |
| comp-* | no | unit is a pure dict-op + served-shape read; comp-pipescript io is mdpf-unsupported (leg-a GAP). Ground-truthed via deployed-code + served-artifact reads per molecule discipline. |
