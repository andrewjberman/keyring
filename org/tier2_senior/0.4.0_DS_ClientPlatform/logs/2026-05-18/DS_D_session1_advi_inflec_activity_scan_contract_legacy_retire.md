# DS~D Session — 2026-05-18 — ADVI_INFLEC activity_scan contract drift + legacy emit retire

**Agent:** `0.4.0_DS_ClientPlatform~D`
**Scope:** Message-driven pickup from `0.4.2_RD_AdvisorIntelligence` (Andrew brought DS~D online for it).
Two items surfaced by the FE BI Trade Activity window-wiring ship (portal commit 23e8ab14).
**Status:** CLOSED — RAVC validated + closed by RD 0.4.2 (2026-05-18). Both items done, nothing further.

---

## What shipped

| Item | Deliverable | Status |
|------|-------------|--------|
| ITEM 1 — `data_contract.xml` drift | Added `activity_scan_contract_notes` section: 4 per-window artifacts, `txn_count` (window-scoped, NOT `txn_count_12m`) row schema, legacy retirement note | COMPLETE |
| ITEM 2 — retire legacy emit | `INF_D_05.activity_scan.py` no longer emits `platinum/firm/activity_scan.json`; removed `LEGACY_OUTPUT_KEY`, legacy_rows build, legacy upload/log lines | COMPLETE — `d31efbe9e`, deployed |

Commit (author `0.4.0_DS_ClientPlatform~D`): `d31efbe9e`.

---

## Detail

**Context.** RD 0.4.2 shipped FE wiring (portal DEV 23e8ab14, parent CLOUD ca63fe2da) that
connects the Inflection BI panel's Trade Activity lens to the per-window activity_scan
artifacts — the Window toggle (QTD/YTD/1Y/Max) now path-keys to `activity_scan_{window}.json`
instead of being cosmetic. That surfaced two DS-lane loose ends.

**ITEM 1 — contract drift.** `data_contract.xml` had NO activity_scan entry at all — the
per-window emit (pre-existing, not new) was undocumented. Added an
`activity_scan_contract_notes` block modeled on the existing `fee_efficiency_contract_notes`
pattern: documents the 4 window artifacts, the row schema
`{household_id:int, aua:float, txn_count:int, activity_score:float, segment:'active'|'buy_and_hold'}`,
the window definitions (parity with INF_D_06.cash_drag / 49F C_08), and the legacy retirement.

**ITEM 2 — legacy emit retire.** `INF_D_05.activity_scan.py` header (lines 30-33) said the
legacy `activity_scan.json` (1y window, `txn_count_12m` field) was "preserved for FE
backward-compat; DE will retire in next FE PR once window-keyed paths are wired." That FE PR
is now shipped (23e8ab14) — the FE reads only `activity_scan_{window}.json`. Removed:
`LEGACY_OUTPUT_KEY` constant, the `legacy_rows`/`legacy_payload` build in `main()`, the legacy
summary log line, the legacy `put_object` upload block. Updated the module docstring + the
`build_window_rows` docstring (kept the generic `txn_count_field` param — it defaults
correctly and is harmless; only the "legacy artifact" wording was stale). Pure dead-code
simplification — the 4 window-keyed artifacts are byte-identical in shape.

**Deploy.** ds-commit-gate PASS -> commit `d31efbe9e` -> `git push origin CLOUD` -> pre-push
`safe-deploy.sh` hook auto-deployed `[inf]` and verified -> S3 confirmed:
`s3://opal-data-inf/code/gold/INF_D_05.activity_scan.py` 17408 bytes (matches local exactly).
Local `--dry-run` PASS: all 4 windows built (298 HH each, qtd/ytd/1y/max), no errors, no
legacy line in the per-window summary, `DONE: activity_scan 4-window emit complete`.

**No dedicated runner spin.** Pure dead-code removal; the window-keyed emit is unchanged.
INF_D_05 (`INF_D_05a`, group I, order 540) rides the next INF gold chain run for free.

**Stale legacy S3 object.** `platinum/firm/activity_scan.json` remains in S3 (now no longer
produced/refreshed). Left in place — S3 object deletion is a destructive op requiring explicit
sign-off and the RD confirmed it is "harmless dead weight." Flag for separate cleanup if wanted.

**No collision with the AE 0.6.1 runner sync defect.** That defect (orion-gold-dispatch.sh
flat-dir last-write-wins) only affects same-basename files across `code/{gold,manual_api,
silver,bronze}/`. Verified `INF_D_05.activity_scan.py` exists ONLY in `code/gold/` — no
collision.

---

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io INF_D_05.activity_scan.py` | READS 2 (accounts_dimension_latest, client_performance <- INF_C_02). WRITES none detected — template-string S3 writes (S3-DYNAMIC) not modelled. No COLUMN GAPS. |
| `comp-pipescript deployed INF_D_05.activity_scan.py` | BD-bucket-scoped (`opal-data-bd`) — no match; INF scripts live in `opal-data-inf`. Deploy verification done via the `safe-deploy.sh` pre-push hook ([inf] DEPLOYED + verified) + direct `aws s3 ls` size match. |
| `.tools/ds-commit-gate.sh` | PASS — py_compile + AST undefined-name scanner + ruff py39. |

---

## Files Modified

| File | Change |
|------|--------|
| data/orion/scripts/gold/INF_D_05.activity_scan.py | Retired legacy `activity_scan.json` emit — removed `LEGACY_OUTPUT_KEY`, legacy_rows build, legacy upload/log lines; docstring updates |
| org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/data_contract.xml | Added `activity_scan_contract_notes` section (4 per-window artifacts + row schema + legacy retirement) |

---

## RAVC closure

RD 0.4.2 validated `d31efbe9e` on origin/CLOUD (2 files: INF_D_05.activity_scan.py -22 lines,
data_contract.xml +29; gate PASS, S3 script match, dry-run 4-window clean) and **closed both
items**. RD ruled the stale `platinum/firm/activity_scan.json` S3 object stays in place —
unreferenced, harmless, not worth a destructive-op sign-off cycle; no separate cleanup item.
Both loose ends from the BI Trade Activity window fix are fully closed. Nothing further.

---

## Next Steps

| Recipient | Item |
|-----------|------|
| **RD 0.4.2** | DONE — RAVC closed. |
| **Whoever runs the next INF gold chain** | INF_D_05.activity_scan.py has a new version (`d31efbe9e`); no legacy `activity_scan.json` will be written on/after that run. No action needed — informational. |
| **DS~D (self)** | Idle — watchdog standby. No pending DSD-lane TOs. |
