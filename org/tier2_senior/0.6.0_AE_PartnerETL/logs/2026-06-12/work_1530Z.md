# 0.6.0_AE_PartnerETL — work 2026-06-12 1530Z

**archetype:** IMPLEMENT (tooling-coverage)

## NFRA_COT_TOOLING — cot comp-validate + comp-pipescript coverage

Closed the cot tooling-coverage gap I surfaced in COT-FIX (cot was NO_CONFIG on comp-validate +
blind on comp-pipescript deployed). Commit **6bc1f1ce3** (code + config); manifest patch handed to COO.

### Changes
- **validate_cli.py**: `_COT_VALIDATE_CONFIG` + PATH-based cot routing (`_is_cot_path` / `_canonicalize_cot_script_id`).
  cot ids collide with bd (A_01, C_02, D_04 ...) so cot routes by PATH, never id-prefix, and loads in
  ISOLATION via `_load_raw_cot_configs()` — never merged into the bd+inf alias map (a merge would let cot
  D_00/D_04 shadow bd's). cmd_list grows a cot branch. Added `import re`.
- **pipeline_cli.py**: added `cot` to the path-canonicalize regex (both occurrences); cot-path→`cot-gold`
  auto-route in `cmd_deployed` (the cot bucket branch `S3_BUCKET=opal-data-cot` already existed —
  `--pipeline cot-gold` worked; the gap was bare-path auto-detection).
- **data/cot/scripts/gold/gold_validate_config.yaml**: FINDING — this file was a **stale forked copy of the
  bd config** (bd artifacts + bd incidents: timeseries_chart.json, employee_leaderboard.json, Travis
  Penfield, ADVI_STAUDT, cohort_a_summary ...) from the NFRA_DTAFLP bd→cot fork, **never wired into
  validate_cli** (dead — that's why comp-validate reported cot NO_CONFIG). Replaced with real cot content:
  A_01 + A_04 stanzas, verified PASS against the live served cot artifacts; cot header + fail-closed doc.
- **Firm separation held**: opal-data-cot only, no opal-data-bd refs in any cot tooling path.

### Compiler Tools section (acceptance-required)

**Phase-1:** read bd `gold_validate_config.yaml` (reference) + located both extension points —
`validate_cli` config-discovery (`_BD/_INF_VALIDATE_CONFIG`, prefix routing) + `pipeline_cli`
`cmd_deployed` bucket map (cot branch present; bare-path canonicalize regex excluded cot).

**Phase-2 verify (all green):**
- `python -m py_compile validate_cli.py pipeline_cli.py` → COMPILE OK.
- `comp-validate data/cot/scripts/gold/A_04.client_dimension.py --artifact <baseline>` → **2 PASS, exit 0**
  (Resolved A_04 → cot config; count_min relationship_id=201, key_present). NOT NO_CONFIG.
- `comp-validate data/cot/scripts/gold/A_01.advisor_assignments.py --artifact <baseline>` → **2 PASS, exit 0**
  (account_id=623, is_current present).
- `comp-pipescript deployed data/cot/scripts/gold/A_01.advisor_assignments.py` (BARE PATH) → auto-routed
  **[cot-gold] vs s3://opal-data-cot, A_01 MATCH** (blind-spot closed).
- REGRESSION: bd bare-path deployed → still opal-data-bd MATCH; `comp-validate --list` → still BD+INF (21);
  inf routing → reaches artifact check (config resolution intact). No bd/inf breakage.
- ruff: my edits added 0 new errors (validate_cli 0→0; pipeline_cli 11→11 pre-existing, not in scope/mine).
- YAML parse OK on all 3 edited yaml.

**Manifest (Rule 20 catalog completeness) — ANY_EXEC handoff to COO (uncommitted, this TO):**
- `graph-call-manifest.yaml` (1 line): deployed note updated (was "only checks opal-data-bd ... blind" —
  doubly stale; now bd/inf/mdpf/cot coverage + remaining-blind caveat).
- `comp-tools.yaml` (8 lines): comp-pipescript segment_scope_note + `deployed` subcommand + comp-validate
  segment_scope_note + `config` line — all add cot coverage.
- Both flagged in RAVC2 for COO to commit under COO/CTO/CVO author line (TO-F1 handoff pattern).

### Acceptance
- comp-validate cot spot-check → PASS (not NO_CONFIG). ✓
- comp-pipescript deployed cot → MATCH (not blind-skip). ✓
- Firm separation: opal-data-cot reads only. ✓
- Manifests updated (ANY_EXEC handoff). ✓

## Commits
- 6bc1f1ce3 — cot tooling code (validate_cli + pipeline_cli) + cot gold_validate_config.yaml
- (pending COO) graph-call-manifest.yaml + comp-tools.yaml cot-coverage notes
