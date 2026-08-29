# 1.0.0_SA_CTO -- session pause @ ~1920Z (PFMG_TAXSMA rename MID-STREAM)

**archetype:** COORDINATE
**secondary_archetypes:** SCRIBE, IMPLEMENT

Andrew-direct: "we'll pick up from here on next run -- take a /log of exact position and mid-stream work." This log is the handoff. **Window:** since last log `scty_prds_gate_sweep.md` (@ 8492715c8) -> ~1920Z 2026-06-26.

---

## CRITICAL -- EXACT MID-STREAM STATE (resume here)

**There is an UNCOMMITTED, HALF-DONE rename in the working tree. Resolve it FIRST next run.**

- `docs/architecture/ADVI_TAXSMA_PRD.md` was `git mv`'d -> `docs/architecture/PFMG_TAXSMA_PRD.md` (staged, NOT committed).
- The renamed file's **CONTENT is still stale** -- title line + project-code line still say `ADVI_TAXSMA` / macro `ADVI`. The content edit (title/code -> `PFMG_TAXSMA`, macro -> `PFMG`, UI=Hybrid-confirmed) was **REJECTED/interrupted before applying** -- NOT done.
- **Why this matters:** COO already committed the registry JSON rename `ADVI_TAXSMA.json -> PFMG_TAXSMA.json` (`6906a0b25`, pushed) and its JSON **points at `PFMG_TAXSMA_PRD.md`**. So right now the committed registry references a doc that (a) isn't committed at its new path and (b) has stale internal content = a **dangling reference**. Finishing the rename is the clean fix; reverting would orphan COO's registry pointer.

**RESUME ACTION (was about to do, had Andrew's go-question pending):** apply the content edits to `PFMG_TAXSMA_PRD.md` (title, project-code line, macro PFMG, drop the "macro-fit is a COO call" hedge since Andrew ruled, mark UI=Hybrid Andrew-confirmed), also fix the `tools/tax_sma/canonical/README.md` ADVI_TAXSMA -> PFMG_TAXSMA refs, then `safe-commit` both + push. COO confirmed (191741Z) the doc rename is MY lane; the registry JSON + COTMVP.json narrative refs are COO's lane (leave them).

---

## Work COMPLETED this window (committed + pushed)

1. **PRD PFMG_TAXSMA (Tax SMA Rebalancing Automation)** -- authored as `ADVI_TAXSMA` @ **90e4d889c**. Yang Liu reqs via 0.0.1_UA_mstools (Andrew-sovereign). Discovery-gated: S0.1 = the step-2 Schwab-lot cost-basis LEVER (does opal-data-schwab/49-schwab-conv already land lot-level cost-basis for the 3 Tax SMA accounts -> lookup vs fresh Schwab pull), S0.2 = Yang's converter scripts, S0.3 = FIS email first/second rule. HARD GUARDRAIL: system GENERATES trade file, human EXECUTES -- never auto-trade; no creds in code. UI = Andrew's call (3 options, CTO lean hybrid).
2. **PRD addendum (step-3 verbatim)** + **canonical script landed** @ **86b87d06d** -- Andrew-direct: step-3 uses Yang's `convert_cost_basis.py` VERBATIM. Provenance-locked the (previously untracked, in `C:\Users\AndrewBerman\Downloads\`) source to `tools/tax_sma/canonical/convert_cost_basis.py` + README. ONE documented deviation: 3 box-drawing comment separators (U+2500) -> ASCII `--` per CLAUDE.md no-non-ASCII rule; conversion BODY byte-for-byte Yang's. Pinned the exact I/O contract in the PRD (note "Initial Holding" SINGULAR, line-8 CSV offset, utf-8-sig, cols [0]/[2]/[3]/[4]/[6], CASH_USD substitution, "/"->"." rewrite). Build leg parameterizes {BASE}+{date} by injection only.
3. **ADVI_COTMVP D1 arch-gate ruling** @ **05f72c2f6** -- Option A (GO). 0.4.0_DS grounded+FALSIFIED my PRD's D1 producer premise BEFORE coding (exemplary Rule-22): COT NMNC uses IDENTICAL shared code as 49F (D_00b._build_static_aua_periods + D_04 pass-through); COT $401M year=quarter / NMEC=0 is FAITHFUL young-firm output (100% onboarded 2026-Q2), not a bug -- a "fix" would no-op or silently regress 49F. STOOD DOWN the producer leg; NMNC display concern folds into D3 (pod4 DE); DS gold lane freed. Rejected B (redefine NMNC fabric-wide = Andrew's separate call) + C (invent cot-only semantic). Updated the COTMVP PRD accordingly.

Dispatches sent: D1 GO-ruling -> 0.4.0_DS (ACK'd, leg stood down); decomp handoff -> COO (ABSORBED: PFMG registry rename 6906a0b25, S0 dispatched S0.1->CVO / S0.2->DS / S0.3->0.8.0 [S0.3 ALREADY GROUNDED 8fb5af90b: FIRST=PRELIM/SECOND=final by sent-time]); ACK -> UA/Andrew.

## QUEUED, UNACTIONED (work these next run, after the rename)

1. **0.4.0_DE RAVC -- ADVI_COTMVP S0 browser-repro grounded Symptom-1** (`20260626T185700Z...`) -- the BLOCKING gate I set on the Symptom-1 code leg. READ IT, issue arch-gate (was the exact blank GEO-donut / fetch-failure / single-bar perception?). NOT yet read.
2. **0.4.0_DE arch-gate request -- ADVI_COTMVP D2** (.quarters schema-guard hardening, `20260626T190703Z...`). NOT yet read.
3. **CVO NFRA_MSGRAPH re-scope arch-gate ruling** (`20260626T184120Z`, deliverable fc27980c8) -- CVO verdict: SOUND + 2 conditions. COND A = require 0-diff on CERTIFIED AWS graph_nodes/graph_edges after heat materialization (new tables only). **COND B (load-bearing, ADOPT)** = node-health is ONE surface, heat is a DEBTSCAN DIMENSION not a parallel surface -- unify SUBSTRATE (one materialization; migrate file-ledger debtscan onto it OR heat emits to same home) + DATA MODEL (one per-node health record {reachable,duplicated,heat_band,cold_since,cost}; comp-dups/comp-heat/comp-debtscan = LENSES) + TOOL FAMILY (comp-heat/comp-ms-find/comp-debtscan in comp-* + manifest). Make COND B a 6th arch-gate decision GATING decision #2 (estate-wide heat generalization). My ruling: adopt both conditions, forward 0.8.0's re-scope to GO under them. NOT yet issued.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-grep | scope ADVI_TAXSMA refs for the rename | PASS -- 5 files; PRD+README mine, project JSONs are COO lane |
| (Grep native) | pin PRD lines for edit | PASS |

What worked: comp-grep cleanly scoped the rename surface + lane-split (my docs vs COO's registry). What failed: two `git`/`date` Bash calls hung (exit 143 timeout / interrupted) at session end -- avoided further git per Andrew. Gap: none new.

## Current State (zero-context handoff)

- **Branch CLOUD.** My pushed commits this window: 90e4d889c, 86b87d06d, 05f72c2f6 (all on origin/CLOUD as of last successful push to 86b87d06d; the COTMVP ruling 05f72c2f6 + COO's 6af49d71c/6906a0b25/b51716b72 also on remote).
- **Working tree:** the half-done PFMG rename (above) is the only intentional uncommitted change of mine. (Plus pre-existing untracked/modified noise from gitStatus baseline -- not mine.)
- **PFMG_TAXSMA project:** REGISTERED by COO, macro PFMG (PortfolioManagement, owner 0.3.1_RD, sibling PFMG_VISPOL), UI=Hybrid, S0 dispatched + moving (S0.3 already grounded). S0 verdicts -> RAVC me, then build legs + UI specifics. Separately: UA driving an Andrew-authorized Schwab-cloud-delivery Path-B spike (headless REST, SI2 ValidateUserCredential auth) that feeds step 2 -- distinct from PFMG_TAXSMA, may firm into its own PRD.
- **ADVI_COTMVP:** pod4-DE-only now (D1 stood down). S0 grounded Symptom-1 (RAVC waiting on me), D2 arch-gate waiting, B/D3 follow, D3 carries the NMNC display concern.

## Next Steps

1. **[1.0.0_SA_CTO]** FINISH the PFMG_TAXSMA doc rename (content edits + README + commit + push) -- resolves the dangling registry reference. FIRST action.
2. **[1.0.0_SA_CTO]** Read + arch-gate the 0.4.0_DE ADVI_COTMVP S0 Symptom-1 RAVC + the D2 request.
3. **[1.0.0_SA_CTO]** Issue the NFRA_MSGRAPH arch-gate ruling to 0.8.0_AE (cc CVO): GO under COND A + COND B (B = 6th decision, heat lands AS a debtscan dimension, gating decision #2).
4. **[3.0.0_SA_CVO / 0.4.0_DS / 0.8.0_AE]** PFMG_TAXSMA S0 verdicts -> RAVC me, then I scope build legs + the hybrid UI specifics with Andrew.
