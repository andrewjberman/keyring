# Session Log — 2026-05-22 — SSCN_UNVREV Portal Revert

**Agent:** 0.3.0_DE_TradingOperations (Dashboard Engineer, Trading Operations PM)
**Date:** 2026-05-22
**Session type:** Resume — landed an in-flight portal revert left uncommitted by a prior session.

**Portal DEV commit:** `47330865`
**Workspace CLOUD commit:** (none — no workspace files in DE scope this session)

---

## Why this log exists

Session opened with three delivered messages in the `.unread-deliveries` sentinel
(AE_OpalETL ACK of SSCN_UNVREV.001; two COO routing notices). All three were
informational — the operative instruction across them was COO's "carry on with the
portal revert." The portal-side SSCN_UNVREV revert was found fully built but
**uncommitted** in the portal working tree (prior session ended before commit).
This session verified and landed it.

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
  running them requires a DEV dev-server bring-up and is recommended pre-PROD.

## Cross-domain coordination

- **AE SSCN_UNVREV.001** (0.5.0_AE_OpalETL) reverts the Lambda `UNIVERSE_MAP` +
  refreshes S3 data. PROD coupling: the portal must NOT reach PROD before the AE
  TO's AC4 (all 6 universe JSON artifacts exist in S3) or 4 universes render
  empty/404. AE will RAVC2 with evidence; validation pending.
- **MDPF_ASSETS.033** — another pod's uncommitted portal work shares the tree;
  flagged to the owning agent and to DT (see Next Steps).

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-transform schema-check UniverseScannerTab` | PASS — all rendered fields match response types |
| `comp-transform schema-check SecurityScanner` | PASS — all rendered fields match response types |

`comp-blast` not run — this is a revert to a prior-shipped universe set, no new
downstream nodes introduced; the `UniverseId` union returns to its pre-.005 shape.

## Current State

Portal SSCN_UNVREV revert committed to DEV `47330865`, statically verified clean.
DEV only — nothing in PROD. PROD promotion is gated on AE SSCN_UNVREV.001 AC4 +
Andrew's DEV smoke, bundled by DT.

## Next Steps

- `[0.3.0_DT_TradingOperations]` (1) Portal submodule is checked out on PROD —
  return it to DEV. (2) Bundle the PROD promotion of `47330865` after AE
  SSCN_UNVREV.001 AC4 + Andrew's DEV smoke. (3) Uncommitted MDPF_ASSETS.033 work
  sits in the portal tree (not pod-0.3 scope).
- `[0.4.0_DE_ClientPlatform]` Your MDPF_ASSETS.033 changes (`ModelPortfolios.tsx`,
  `aum.ts`, `portal-proxy.ts`) are uncommitted in the portal PROD working tree —
  commit them to DEV.
- `[0.5.0_AE_OpalETL]` SSCN_UNVREV.001 RAVC2 — DE validates AC1-AC6 evidence on
  receipt.
- `[Dashboard Engineer]` Recommend `/frontend-dev` smoke (Scenario 5 + 7) on DEV
  before the PROD bundle.
