# Session Log — 0.2.0_DE_PortfolioAnalytics — /Peers Tab Missing Models (ST/LTC/LTA)
**archetype:** DIAGNOSE

**Date:** 2026-06-26
**Origin:** Andrew-direct — "/Peers tab Model toggle only offers UST and INT; missing ST, LTC, LTA."

## Investigation chain (symptom -> mechanism, source-grounded)

1. **FE not the cause.** `src/pages/ModelPortfolios/tabs/PeersTab.tsx:455` renders a Model
   toggle button per code present in the data: `MODEL_CODE_ORDER.filter(code =>
   transformedData.models[code])`. `MODEL_CODE_ORDER` already lists all 5. The transform
   (`transformPeerData`) iterates and preserves every model — it drops nothing. So the FE
   faithfully shows only what the data carries.

2. **Served artifact only has 2 models.** Pulled `s3://opal-data-portal-v2/json/peers/
   peer_performance.json` -> `MODEL KEYS: ['UST','INT']`, generated_at 2026-06-21,
   data_as_of 2026-06-18. The data itself is missing ST/LTC/LTA.

3. **Producer traced.** `pipescript --resource peer_performance` -> thread
   `model-portfolios / yang-peer-performance`. Source:
   `infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-generate-peer-performance/
   lambda_function.py`.

4. **Mechanism (the why, source+data-grounded — not inferred).**
   `parse_peer_excel()` hardcodes the model-section start columns: `for start_col in [0, 20]`
   (line 149). Ground truth from the two real Excels:
   - Old `Models Performance vs Peers 202512.xlsx`: 39 cols, 2nd block at col **20** ->
     parser run yields all 5.
   - Current source `Models Performance vs Peers 20260618.xlsx` (the one the served artifact
     used — confirmed via `json/latest/peer_excel.json` manifest s3_key + matching
     data_as_of 2026-06-18): **51 cols, 2nd block shifted to col 26.** "Return/Risk" headers
     physically at cols **0 and 26**. The hardcoded `[0,20]` never scans col 26, so the
     entire second block (ST at row0; Aggressive growth=LTA + Conservative growth=LTC at
     row16) is silently dropped. Running the actual Lambda parser on the live source returns
     `['UST','INT']` — reproduced the exact served defect.

   Andrew's "source should be 202605, not the old 202512" concern: source freshness is
   actually fine — the pipeline used the June file; `uploads/...202512.xlsx` is just a stale
   leftover. The missing models are purely the hardcoded-column bug, independent of month.

## Fix (written + validated; landed by DT)

Replace the hardcoded `[0, 20]` with a dynamic scan of every column containing a
"Return/Risk" header (`section_cols = sorted({...})`). Layout-agnostic.

Validation on the edited module against both live Excels:
- `20260618` (current source): `[UST, ST, INT, LTC, LTA]` — **PASS** (5/5). INT 1Y
  model=6.3888 bm=7.7631 p50=6.6365.
- `202512` (old): all 5 — **PASS** (backward-compatible).
- `py_compile` + `.tools/ds-commit-gate.sh`: clean.

**Lane handoff:** committing `infra/aws/lambda/` tripped the owned-paths gate (that path is
the AE/CLOUD_OPS_OR_ETL lane, not DE). Plus the fix needs a Terraform deploy + rerun (DT's
lane). Left the validated edit in the working tree + saved
`deliverables/peer_parser_fix.patch`; handed to **DT** (in-lane commit + TF deploy + rerun,
mirroring the benchmarks fast-track) and **DS** (pipeline owner). DT ACK'd and is deploying.

## Open

- **DT:** review + comp-blast + deploy ledger + in-lane commit (audited override on AE-lane
  source) + build/TF deploy + tag + rerun against the 06-18 source + CF-invalidate.
- **DE (me):** on DT's served-regen ping, re-pull `peer_performance.json` (expect 5 models)
  + confirm all five render in the /Peers toggle.

## Compiler Tools

| Tool | Result |
|---|---|
| `pipescript --resource peer_performance` | located producer thread `model-portfolios / yang-peer-performance` (PASS) |
| `comp-which "...peer_performance producer + 3 charts deps"` (earlier) | manifest backstop routing |
| Native Glob/Read/Bash(aws s3 cp) | grounded the served artifact + both source Excels + ran the actual parser (the decisive evidence) |

Note: the decisive grounding was running the real Lambda `parse_peer_excel()` against the
two live source workbooks — reproduced the 2-model defect and proved the 5-model fix. A raw
grep would have missed it entirely (the bug is a column-position vs data-layout mismatch, not
a text pattern).
