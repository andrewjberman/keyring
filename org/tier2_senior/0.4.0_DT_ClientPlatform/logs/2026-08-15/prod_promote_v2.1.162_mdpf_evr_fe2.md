# Portal DEV -> PROD promote v2.1.162 -- MDPF_EVR.FE-2 reconstructed-as-ordinary + OPAL_INVPHL pillar-copy follow-on -- 0.4.0_DT_ClientPlatform

**Date:** 2026-08-15 (session ~2105Z-~2145Z)
**Task Order:** MDPF_EVR.FE-2.PROMOTE (`org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/MDPF_EVR.FE-2.PROMOTE.prod-promote-reconstructed-ordinary.md` @13ed79bc40, issued 2.0.0_SA_COO 2112Z, GO 210723Z)
**Status:** COMPLETE -- PROD live at `portal-v2.1.162` (449a6a0e); all 7 legs landed; ledger closed; proof-of-spec VALID rc=0
**Authority:** Andrew-direct at the MSTR terminal 2026-08-15 ~2100Z, VERBATIM *"yes, do both"* (MSTR 210435Z) -- (b) spawn DT for the PROD promote; shipping *"yes they should render as ordinary points"* (LD-0417). Relayed by MSTR/COO; recorded here verbatim as relayed.
**Archetype:** deploy-promote, spec-proven

---

## Objective

Promote portal DEV -> PROD via `/prod-deploy` exactly, shipping EXACTLY 3 commits (`684e67de` OPAL_INVPHL pillar copy; `778ea780` FE-2 Implementation B; `e8b1fb07` FE-2 AC-8), main tree never leaving DEV, CI verified by `gh run view --json`, acceptance = a RENDERED read of PROD.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-routes | `comp-routes behaviors` | PASS | 25 CF behaviors (DESIRED plane); `/portfolios` SPA via `/*` -> S3-opalinvest-portal; MDPF data `/api/general/*` -> opal-data-portal-v2 via public-data-router. TO BEFORE-mandate. |
| comp-find | `comp-find 'getMdpfAggregateAUATimeSeriesByFirm' portal/src` | PASS | 3 files; fetch URL `/api/general/mdpf/{firmId}/aggregate-aua-timeseries.json` (`portal-proxy.ts:532`) -- used to key the render fixtures |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py .../MDPF_EVR.FE-2.PROMOTE_PROOF_OF_SPEC.json AC-P1,AC-P2,AC-P3,AC-P4,AC-P5` | PASS | `structural=jsonschema \| acceptance rows=5 \| violations=0` VALID **rc=0** (positional id form) |
| /frontend-dev (ui-smoke) | `node scripts/ui-smoke.mjs portfolios <png> --origin https://opalinvest.dev --fixtures <served Global artifacts>` x3 (REAL/MUTANT/ASMEASURED) + console-capture variant x2 (REAL/unknownstr, each twice) | PASS | LOC /portfolios, REFAREAS 0 x3 every run; PNG read; PIL diffs 60 px (status dot) only; console oracle discriminates 0 vs 1 |
| /watcher | armed once at load | PASS | Monitor bl95v52vi; delivered COO GO/ACK + MSTR leg-5 signal |
| comp-pipescript io | not run | -- | no gold script deployed (frontend-only promote); the DT minimum row does not apply |

**What worked:** `ui-smoke --origin` + `--fixtures` = the DEPLOYED bundle rendering the SERVED data, no credentials; a mutant fixture set + PIL diff turned the "read the PNG" step into a measured instrument with a stated blind spot; console capture (a 1-line variant of ui-smoke) gave the behavioral oracle the pixels could not.
**What failed:** the first served-bytes check grepped the entry chunk (`index-*.js`) for the FE-2 marker AND the positive control -- both 0; the page is a lazy chunk (`ModelPortfolios-gqyfc1FQ.js`). The positive control failing is what caught it. Also: `git rev-parse --show-toplevel` from inside the ephemeral worktree resolves to the WORKTREE, not the workspace -- one `git -C portal` call died `No such file or directory` before I switched to absolute paths.
**Gap found:** none new; the estate's `ui-smoke` has no console-capture flag -- the variant lives at `portal/.frontend-dev/testing/ui-smoke-ppr-console.mjs` (untracked, session convention).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Gate + freeze | DT serial OK; GO current, no `[STOP]`; freeze announced (ACK 210743Z to COO, FYI 210751Z to MSTR); TO BEFORE-mandate `comp-routes behaviors` + `rev-list --count` = **3** (AC-P1) |
| 1 | DEV tree | branch DEV; 0 ahead / 0 behind origin/DEV; payload `origin/PROD..origin/DEV` = exactly `e8b1fb07 778ea780 684e67de`; PROD `fbbb9b39` = `portal-v2.1.161` exact-match; 13 `??` untracked items surfaced (not payload) |
| 2 | typecheck | `bun run typecheck` (`tsc -b --noEmit`) rc=0 |
| 3 | re-assert local PROD | `update-ref` no-op, local PROD == origin/PROD `fbbb9b39` |
| 4 | worktree + install + merge | `.runtmp/portal-promote-20260815T211038Z`; `bun install` FOREGROUND 420 pkgs rc=0; `merge --no-ff origin/DEV -F <msg>` -> **`449a6a0e`** (parents fbbb9b39 + e8b1fb07); **parity `git diff origin/DEV HEAD` = 0 lines**; message carries `Base fbbb9b39... Rollback: fbbb9b39...` (AC-P5) |
| 4d | `git push origin PROD` | **DENIED** by never-rules-gate GATE 5 (LD-0367/0368 integrator-only, shared branch PROD) -- override NOT used; ledger opened @0f264f59de; **handed to MSTR 211559Z** with the exact command + re-verify data; **MSTR pushed 2118Z** after re-deriving parity/payload/base; remote read-back `origin/PROD = 449a6a0e` |
| 5 | CI + tag | `Deploy to Production` run **31909060242** `conclusion: success` (**1 of 1** workflows on headSha 449a6a0e, enumerated by sha, not the badge; polled via `gh run view --json`, never `watch`); tag `portal-v2.1.162` OBJECT e9822640 peels to **449a6a0e** == PROD head (AC-P2). Served bytes: `ModelPortfolios-gqyfc1FQ.js` carries `reconstructed(` x1 (absent at v2.1.161 source) with control `interpolated_estimate` x13 |
| 5b | AC-P3 rendered read | see Verification |
| 6 | workspace gitlink | gitlink already `e8b1fb07` (MSTR @04d25a3533) == DEV HEAD == promoted payload head; `git diff HEAD -- portal` 0 lines -> NO empty bump commit; traceability carried by ledger + proof-of-spec (this commit); MSTR pushes CLOUD as integrator |
| 7 | teardown | `worktree remove` "Filename too long" (documented class; dir persists gitignored+inert); `worktree prune` OK; `worktree list` clean; main tree **DEV** @e8b1fb07; cwd workspace root |
| 8 | report + freeze release | RAVC completion report to COO cc MSTR (this session); TO status -> `complete`; ledger CLOSED |

## Verification

**AC-P3 (the acceptance).** PNG `portal/.frontend-dev/screenshots/mdpf_evr_fe2_PROD_v2.1.162_global_REAL.png` (1440x2346): deployed PROD bundle (`--origin https://opalinvest.dev`) + SERVED Global platinum artifacts as fixtures (`s3://opal-data-portal-v2/platinum/mdpf/global/{aggregate-aua-timeseries,aum-metrics,account-distribution}.json`, point_class census measured 403 / interpolated_estimate 35 / absent 9 / carried 5 / **reconstructed 2 = 2026-05-20, 2026-08-05**, n_dates 454). READ: `Select Partner: Global (All)`; period-end bars + Daily AUA stacked area with NO band, NO dashed overlay, NO "Interpolated" legend entry (legend = 5 tiers + Non-Model AUA); REFAREAS 0 x3; color law clean. **The 2 dates render ordinary.**

**Premise correction, source-confirmed (surfaced to COO, not adjudicated):** the pixel read is NON-DISCRIMINATING at Global. MUTANT (both dates relabelled `interpolated_estimate`) and ASMEASURED (relabelled `measured`) are each pixel-identical to REAL: 60 of 3,378,240 px differ, all in bbox (105,2223)-(113,2231) = the animated "SmartX Connected" status dot (the same 60-px bbox DE measured on DEV). Mechanism: `portal/src/pages/ModelPortfolios.tsx:884-889 @449a6a0e` empties `trendInterpolatedDates` at Global (Andrew-direct 2026-07-23 materiality ruling -- band, dash, legend, bar outlines all derive from it); the same gate exists at `fbbb9b39 :882`. **Global never pixel-rendered estimate-class on either build; the TO's "still renders 2 dates estimate-class -- visually distinct, live" premise is false at source.** What FE-2 changes at Global is the derived class (`reconstructed`, a known member, instead of warn + `interpolated_estimate`) and the console warn.

**The discriminating exercise on the deployed bundle (behavioral):** console capture (`portal/.frontend-dev/testing/ui-smoke-ppr-console.mjs`, same fixtures, each run twice): REAL -> **0** console lines mentioning `reconstructed` (3179/3179 PPR lines both runs); unknown-string mutant `reconstructed_zzz` -> **1** warn `[pairedProvenanceRead] invalid Global point_class 'reconstructed_zzz' at index 386 -- treating as interpolated_estimate (never silently measured)` (3180/3180). The instrument fires on the mutant and is silent on the real data -- Implementation B is RUNNING on PROD, not merely shipped.

---

## Decisions Made

- **Did NOT use the audited `# never-override:` on the GATE-5 PROD-push deny** -- same grounds as 08-11 (a non-integrator push republishes every seat's local commits; I cannot enumerate them from here). MSTR concurred and put it on the record ("the reasoning generalizes").
- **No empty gitlink-bump commit** -- the pointer already paired the workspace with the payload head; traceability lives in the ledger + proof-of-spec instead of an empty commit dressed as a record.
- **Reported AC-P3 as PASS with the premise correction inside the row**, rather than either (a) quietly declaring the pixel pass or (b) failing it -- the criterion as written is met; what is false is the TO's premise about the before-state, and that is COO's to adjudicate.

## Files Modified

- `org/critical_paths/change_management/20260815T211100Z_portal_prod_promote_MDPF_EVR_FE2.md` -- opened @0f264f59de, CLOSED this commit
- `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/MDPF_EVR.FE-2.PROMOTE_PROOF_OF_SPEC.json` -- VALID rc=0
- `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/MDPF_EVR.FE-2.PROMOTE.prod-promote-reconstructed-ordinary.md` -- `<status>` pending -> complete
- this log
- portal: `refs/heads/PROD` -> `449a6a0e` (merge, pushed by MSTR); tag `portal-v2.1.162` (CI-minted). Untracked, session-convention: `portal/.frontend-dev/screenshots/mdpf_evr_fe2_PROD_v2.1.162_global_{REAL,MUTANT,ASMEASURED}.png`, `portal/.frontend-dev/testing/ui-smoke-ppr-console.mjs`

## Blockers

None. (The GATE-5 deny was routed and resolved in 3 minutes: handoff 211559Z, push 2118Z.)

## Surprise channel (one line each, no action)

1. Portal main tree: 13 untracked `??` items (stray telemetry dirs / screenshots / .runtmp probes, June-Aug) -- surfaced to COO 211613Z, logged at their desk as hygiene.
2. Deployed Global page load emits ~3,178 `[pairedProvenanceRead] invalid point_class 'undefined' at <date>.model` warns -- served Global `cohort_provenance` carries partner slots and no `model` slot; PRE-EXISTING (same template at `fbbb9b39 pairedProvenanceRead.ts:273`).
3. TO premise about the Global before-state is false at source (above).

## Current State

PROD = `portal-v2.1.162` @449a6a0e, live and served (chunk verified). Main portal tree on DEV @e8b1fb07. Ledger CLOSED. TO complete. Freeze released with the COO report. Seat IDLE after the report; awaiting COO validate/close.

## Next Steps

1. `[2.0.0_SA_COO]` -- validate + close MDPF_EVR.FE-2.PROMOTE on this report; adjudicate the AC-P3 premise correction (met-as-written vs the TO's before-state claim).
2. `[0.0.0_AB_MSTR]` -- push CLOUD (this commit) as integrator.
3. `[nobody, surfaced only]` -- the 3,178-warn Global cohort_provenance/model-slot mismatch is a pre-existing DE-lane observation, not routed by me.
