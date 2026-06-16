# Session close — YANG_SITTW.TO-1 (MDPF 1c/SMA collapse): delivered + accepted + released; /seams + /molecule

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, VALIDATE, DIAGNOSE, COORDINATE

Serial: 0.4.0_DS_ClientPlatform~A (lane A). Window: ~1808Z startup -> ~2150Z. Spawned for YANG_SITTW.TO-1 (Andrew "YANG up first"); ran it to full delivery + acceptance + COO release, then two Andrew-directed verification passes (/seams + /molecule). This close synthesizes the arc; per-phase detail lives in the 5 logs cited below.

## Summary (the session arc)

1. **Implemented + deployed the producer 1c/SMA collapse** (build_aggregate_aua_timeseries.py): fold sma_aua into non_model_aua (1b'=Schwab_total-1a) + drop the sma_aua field. Never-widen verified $0.0000 (TOTAL+model+combined band) across 413 dates x 3 slices, twice (local Phase-2 + Phase-3 on the DEPLOYED artifact). Commit 935d3ba79; deployed to runner code-prefix + served artifact. Detail: `yang_sittw_to1_mdpf_1c_sma_collapse_deploy.md`.
2. **CTO+COO joint never-widen co-sign granted; RAVC-ACCEPTED** (both independently verified the deployed object). Deploy finished in-session, deploy-completion ledger closed (4 legs); I added a DURABILITY leg (runner code upload) the GO steps omitted -> next nightly won't revert. Detail: `yang_to1_leg_a_ravc_close.md`.
3. **Leg(b) FE landed** (DE a447712b): Global SI extension to 2024-11-01 + estimate-tail demarcation + sma_aua type/fold cleanup. Producer<->FE seam mutually verified (value-preserving). Detail: `yang_to1_legb_seam_validation.md`.
4. **/seams** (Andrew-directed) on the producer->served->FE chain: SOUND for leg-a; surfaced a real semantic finding -- the SI extension EXPOSES a deep-tail Global-band overshoot (+$22.4M/2.9% @ 2024-11-01 floor; the band comes from non_model_assets.json, off-basis vs opal_aggregate in the estimate tail). Detail: `seams_1905Z_yang-to1-mdpf-1c-collapse-chain.md`.
5. **Finding closed end-to-end:** DE confirmed to the dollar -> COO surfaced accept-vs-refine to Andrew -> Andrew GO'd REFINE -> DE wired fbfdbe9d (deep-tail band = opal_aggregate_aua - model_aua, SMA-excluded per my molecule-WATCH) -> I independently verified 0 residual + boundary-continuous -> seam record updated (ae071e3f9).
6. **/molecule** (Andrew-directed) on _fold_sma_into_nonmodel: unit SOUND (deployed==committed, idempotent, never-widen). Recorded 1 WATCH -- the collapse makes SMA double-represented (by_model sleeves + folded non_model_aua), so sum(by_model all)+non_model_aua double-counts SMA; FE-safe (filters by_model sma); added a data_contract.xml CONSUMER WARNING. Detail: `molecule_2050Z_fold-sma-into-nonmodel.md`.
7. **COO RELEASED** the TO-1 data leg (delivered; project rides the PROD-promote auto-close trigger).
8. Infra aside: git push/ls-remote hung mid-session (fabric-wide GCM credential-helper issue, MSTR broadcast); resolved (Andrew refreshed GCM). All commits on origin + in sync.

## Current State (handoff)

- **YANG_SITTW.TO-1 DATA LEG: DELIVERED + ACCEPTED + RELEASED.** Producer `data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py` (commit 935d3ba79) deployed to BOTH `s3://opal-data-mdpf/code/scripts/backfill/` (runner code, durable) AND the served `s3://opal-data-portal-v2/json/mdpf/{global,49financial,inflection}/aggregate-aua-timeseries.json` (mtime 18:37:13Z, sma_aua absent, floor 2024-11-01, 413 dates). Never-widen $0 holds on the deployed object.
- **FE leg (b):** portal DEV a447712b (SI extension + demarcation) + fbfdbe9d (deep-tail reconcile REFINE). Both verified. On portal DEV; rides the DT DEV->PROD promote.
- **TO-1 closure:** auto-closes on the PROD promote (COO-released). No JSON flip owed by me (Tier-2).
- **Data-shape note for future consumers:** non_model_aua now = 1b' (includes SMA); by_model cohort_class='sma' sleeves retained. Correct identity: `sum(by_model class='model') + non_model_aua == opal_aggregate_aua`. Do NOT sum by_model-all + non_model (double-counts SMA). Documented in data_contract.xml `<mdpf_global_timeseries>`.
- **No open RAVC loops on my side.** IDLE/available, event-driven, persistent Monitor armed.

## Files Modified
See commit messages: 935d3ba79 (producer + data_contract), 697364866 (leg-a log + FE brief + ledger), 58d086ea3 / bc2b8c165 (closure logs), 8a1443806 + ae071e3f9 (seam report), f53fc5097 (molecule + data_contract warning), and this close. Producer + data_contract.xml are the only code/contract changes; the rest are logs/records.

## Compiler Tools

Session-spanning runs (full reproduction in the per-phase logs cited above; not re-run for this close):
| Tool | Result |
|---|---|
| comp-pipescript io build_aggregate_aua_timeseries | GAP -- mdpf unsupported (bd/inf-only); did consumer-enum via precise grep instead |
| comp-transform schema-check ModelPortfolios | TOOL-LIMIT -- no co-located types.ts; manual MdpfPerFirmTimeSeries reconcile |
| ds-commit-gate.sh (producer) | PASS (py_compile+AST+ruff) |
| Phase-2 + Phase-3 never-widen diffs (custom) | PASS -- $0 movement all 413d x3 slices, local + DEPLOYED |
| deploy_ledger.py (open->4 legs->close) | PASS -- no stranded leg |
| /seams (producer->served->FE) | PASS-with-finding (deep-tail overshoot, since RESOLVED+verified) |
| /molecule (_fold_sma_into_nonmodel) | SOUND-with-WATCH (double-count surface, data_contract warned) |
| REFINE re-verify (custom) | PASS -- 0 residual, boundary-continuous |

This close window itself ran no NEW compiler tools (synthesis + COO-release receipt only).

## Next Steps
- **[self, 6/17 morning]** Nightly durability review: confirm Stage-4 ran the new runner code (served mtime advanced + sma_aua stayed absent); flag COO loud if it reverted. Event-driven artifact review, not an overnight watcher.
- **[0.4.0_DT_ClientPlatform / Andrew]** Portal DEV->PROD promote carries the visual render smoke (Global renders from 2024-11-01, demarcation visible, deep-tail stack sums) + triggers TO-1 auto-close.
- Self: IDLE/event-driven; no open loops.
