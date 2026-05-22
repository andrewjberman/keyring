# Session Log — 2026-05-22 — SSCN_UNVREV Portal Revert

**Agent:** 0.3.0_DE_TradingOperations (Dashboard Engineer, Trading Operations PM)
**Date:** 2026-05-22
**Session type:** Resume — landed an in-flight portal revert left uncommitted by a prior session; closed the AE-side RAVC loop.

**Portal DEV commit:** `47330865`
**Workspace CLOUD commit:** `aca762ae9` (this session log)

---

## Why this log exists

Session opened with three delivered messages in the `.unread-deliveries` sentinel
(AE_OpalETL ACK of SSCN_UNVREV.001; two COO routing notices). All three were
informational — the operative instruction across them was COO's "carry on with the
portal revert." The portal-side SSCN_UNVREV revert was found fully built but
**uncommitted** in the portal working tree (prior session ended before commit).
This session verified and landed it, then closed the AE-side RAVC loop when AE's
SSCN_UNVREV.001 completed mid-session.

## Startup reconciliation

- Portal submodule was checked out on the **PROD** branch (a leftover from the DT
  SSCN_DIVDEF .006/.007/.008/.010 PROD promotion). DE development belongs on DEV.
- The portal working tree carried **two disjoint workstreams**: my SSCN_UNVREV
  revert (7 files) and another agent's uncommitted MDPF_ASSETS.033 work
  (`ModelPortfolios.tsx`, `aum.ts`, `portal-proxy.ts` — ClientPlatform pod). The
  MDPF files were left untouched per commit-scope discipline.

## Work Completed — SSCN_UNVREV portal revert

Three Yang-feedback items on the live Security Scanner page, all SSCN_UNVREV
(Andrew-direct 2026-05-21), committed as one cohesive batch:

1. **Universe-set revert 5 -> 6.** The v0.2 migration (SSCN_DIVDEF .005) assumed the
   FactSet feed had shifted permanently to a US-only-equity 5-set
   (rmidcap/sp400/msciusa). The ongoing feed (`Screening_DIVZ_IDVZ_20260519.xlsx`)
   empirically carries the legacy mixed columns. `UNIVERSE_IDS` / `UniverseId` /
   `US_ONLY_UNIVERSES` reverted to the legacy 6-set
   (sp500/r1000/r1000v/acwx/eafe/eafev). Paired with the AE Lambda `UNIVERSE_MAP`
   revert (SSCN_UNVREV.001, security-scanner-v1.2.0).
2. **Composite column = 0-100 percentile rank.** A plain weighted average of factor
   percentiles clusters mid-range and never used the full 0-100 range; the displayed
   `compositeScore` is now the rank position rescaled to 0-100. The weighted average
   is retained as the intermediate ordering score, and now divides by the weight
   actually used so partially-null rows are not deflated.
3. **Raw-value toggle interleave.** The "Percentiles + Raw" toggle appended raw
   columns far off-screen (Yang: "not working"). Each factor's raw column is now
   interleaved immediately after its percentile column.

| File | Change | Committed |
|------|--------|-----------|
| portal/src/api/endpoints/security-scanner.ts | `UNIVERSE_IDS` 5->6 revert | Yes — DEV `47330865` |
| portal/src/pages/SecurityScanner/types.ts | `UniverseId` union 5->6; `compositeScore` semantic doc | Yes — DEV `47330865` |
| portal/src/pages/SecurityScanner/constants.ts | `US_ONLY_UNIVERSES` 6-set form | Yes — DEV `47330865` |
| portal/src/pages/SecurityScanner/SecurityScanner.tsx | "5 universes" -> "6 universes" copy | Yes — DEV `47330865` |
| portal/src/pages/SecurityScanner/tabs/UniverseScannerTab.tsx | Percentile-rank composite + raw-column interleave | Yes — DEV `47330865` |
| portal/.frontend-dev/testing/sscn_divdef_001_smoke.json | Scenario 5 -> 6-set dropdown assertions | Yes — DEV `47330865` |
| portal/.frontend-dev/runners/sscn_divdef_001_runner.mjs | Scenario 7 added — raw-toggle wiring | Yes — DEV `47330865` |
| org/tier2_senior/0.3.0_DE_TradingOperations/logs/2026-05-22/SSCN_UNVREV_portal_revert.md | This session log | Yes — CLOUD `aca762ae9` |

## How it was landed (branch handling)

The portal was on PROD; DE work must land on DEV. To avoid (a) committing dev work
onto PROD and (b) disturbing the other agent's uncommitted MDPF_ASSETS.033 work in
the shared tree, the 7 SSCN files were captured as a patch, applied in a temporary
`DEV` worktree, committed there (`47330865`), and the worktree removed. The 7 files
were then restored to PROD-HEAD state in the main tree — leaving the main tree
carrying only the MDPF agent's work, untouched. Verified: my 7 files are
byte-identical between DEV HEAD and PROD HEAD, so the patch applied cleanly.

## Verification

- `bun run typecheck` (`tsc -b --noEmit`) — exit 0.
- `bun x eslint` on the 5 SSCN source files — exit 0.
- `comp-transform schema-check UniverseScannerTab` — "All rendered fields match
  their response types"; `comp-transform schema-check SecurityScanner` — same.
- `/frontend-dev` smoke NOT run this session — see Next Steps. The runner +
  constitution were updated (Scenario 5 6-set dropdown, Scenario 7 raw toggle);
  running them requires a DEV dev-server bring-up and is recommended pre-PROD. DT
  has agreed to fold the smoke into the PROD-promotion TO.

## RAVC — SSCN_UNVREV.001 (AE lane) closed

0.5.0_AE_OpalETL completed SSCN_UNVREV.001 mid-session (closure commit `e0286ec3b`,
`security-scanner-v1.2.0`) and sent the RAVC2 evidence. Validated all six ACs and
sent **RAVC4 ACCEPT** — loop closed:

- AC1 — `UNIVERSE_MAP` 6-set; deployed Lambda CodeSha256 byte-identical to the
  v1.2.0 artifact. PASS.
- AC2 — `terraform plan` 0-diff; tag `security-scanner-v1.2.0` (`dc3fc2bb8`);
  commit `ee442cd07`; source-map updated. PASS.
- AC3 — xlsx at `s3://opal-data-portal-v2/security_scanner/uploads/20260519/`. PASS.
- AC4 — 6 universe JSON artifacts + `factor_metadata.json` regenerated (trigger run
  2026-05-21 19:46Z). PASS — the 5/21 stamp is the trigger-run output, not a
  freshness defect.
- AC5 — sp500 502 securities / country populated; acwx 1682 / 0 empty country. PASS.
- AC6 — sp500 `scanner_data.json` rows carry both `values` and `pctls` (284 keys
  each). PASS.

Per-universe counts: sp500 502 / r1000 1002 / r1000v 864 / acwx 1682 / eafe 677 /
eafev 405. **AC4 satisfied means the PROD coupling is cleared** — the 6 universes
are live in S3, so the portal revert is safe to promote.

Non-blocking flag from AE: 3 stale v0.2-only S3 prefixes (`msciusa/`, `rmidcap/`,
`sp400/` under `latest/universes/`) remain — harmless to the portal (the reverted
`UniverseId` union references only the 6-set, nothing reads those prefixes); S3
deletion needs explicit sign-off, so AE left them.

## Coordination / handoffs

Four MCP messages sent:
- `0.5.0_AE_OpalETL` — RAVC4 ACCEPT (above).
- `0.3.0_DT_TradingOperations` — handoff: `47330865` PROD-ready; portal-on-PROD
  branch needs return to DEV; MDPF WIP in tree. **DT ACK received:** item 1 staged
  pending Andrew's DEV smoke + a GO (DT will run the SSCN-commit-set cherry-pick
  promotion, same mechanism as SSCN_DIVDEF.006, and fold the `/frontend-dev` smoke
  into that TO); item 2 (branch return) correctly **blocked** — `git checkout DEV`
  would be refused because aum.ts/portal-proxy.ts differ across the branch boundary
  while the MDPF WIP is uncommitted; DT will switch once 0.4.0_DE_ClientPlatform
  clears their tree. "Nothing for you to do."
- `2.0.0_SA_COO` — status for the SSCN exec lane (COO~B not live).
- `0.4.0_DE_ClientPlatform` — flagged their uncommitted MDPF_ASSETS.033 work.

## Watcher health

Ran `/watcher` per CTO `[ACTION]` directive (Andrew 2026-05-22, every active agent).
`watcher-status.sh` VERDICT ORPHAN — killed prior-session orphan watcher PID 61403
(PPID=1), relaunched exactly one tracked watcher. Registration LIVE throughout.

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-transform schema-check UniverseScannerTab` | PASS — all rendered fields match response types |
| `comp-transform schema-check SecurityScanner` | PASS — all rendered fields match response types |

`comp-blast` not run — this is a revert to a prior-shipped universe set, no new
downstream nodes introduced; the `UniverseId` union returns to its pre-.005 shape.

## Current State

Portal SSCN_UNVREV revert committed to DEV `47330865`, statically verified clean.
AE-side SSCN_UNVREV.001 closed (`e0286ec3b`) and RAVC4-accepted — 6 universe
artifacts live in S3, PROD coupling cleared. DEV only — nothing in PROD. No pending
task orders. Watcher tracked + healthy; idle, standing by.

## Next Steps

- `[0.3.0_DT_TradingOperations]` On Andrew's DEV smoke + a COO/CTO GO: run the
  PROD-promotion TO bundling `47330865` (cherry-pick set, `/frontend-dev` smoke
  folded in). Return the portal submodule to DEV once the MDPF WIP clears.
- `[0.4.0_DE_ClientPlatform]` Commit the MDPF_ASSETS.033 WIP to DEV — it currently
  blocks the portal branch return.
- `[Andrew]` DEV smoke of the Security Scanner before the PROD bundle.
- `[Dashboard Engineer]` Idle — no pending TOs; watcher healthy; standing by for
  dispatch.
