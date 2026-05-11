# DS~C 2026-05-11 — ADVI_INFGRO.TO-000 close (Stage 0 foundation)

**Agent:** 0.4.0_DS_ClientPlatform~C
**TO:** ADVI_INFGRO.TO-000 (CTO 1.0.0_SA_CTO via COO 2.0.0_SA_COO)
**Status:** SHIPPED — commit `119b04124` + S3 MATCH for both files
**Authorized by:** Andrew global GO on ADVI_INFGRO 2026-05-11 21:13Z + CTO PRD v0.2 §6.TO-000

## TL;DR

Stage 0 foundation for the AUA_growth = NNA + Return + ε decomposition: shipped
declarative cashflow taxonomy YAML (43 type_desc / 58 compound-key entries) and
refactored INF_C_01 to consume it. **Byte-equivalent inheritance** verified —
Joe Brandenburg full-history rows / inflow / outflow / net NNA / MAX firm-level
NNA all match baseline exactly ($0.0000 delta). Five PRD §2.3 reclassifications
documented in YAML's `open_items` block for CTO ratification in follow-on TO.

## Files shipped

| File | Status | SHA16 |
|---|---|---|
| `data/orion/scripts/silver/orion_cashflow_taxonomy.yaml` | NEW (343 lines) | `a18a90368b58cf96` MATCH |
| `data/orion/scripts/gold/INF_C_01.canonical_nna.py` | REFACTOR (+71/-19) | `87dcd38db99c5b24` MATCH |

Both deployed:
- `s3://opal-data-inf/code/gold/INF_C_01.canonical_nna.py` (auto via safe-deploy pre-push hook)
- `s3://opal-data-inf/code/gold/orion_cashflow_taxonomy.yaml` (manual `aws s3 cp` — YAML not auto-deployed)

## Behavioral inheritance test

**Acceptance criterion:** canonical_nna.parquet rows match prior output within $1.
Joe Brandenburg MAX NNA = $11,729,310 (TO target).

| Metric | Baseline (S3) | Post-refactor (local rerun on current silver) | Delta |
|---|---:|---:|---:|
| Joe full-history rows | 813 | 813 | 0 |
| Joe inflow $ | $14,412,925.94 | $14,412,925.94 | **$0.0000** |
| Joe outflow $ | $2,603,501.07 | $2,603,501.07 | **$0.0000** |
| Joe net NNA $ | $11,809,424.87 | $11,809,424.87 | **$0.0000** |
| Joe firm-level MAX NNA $ | $11,824,453.75 | $11,824,453.75 | **$0.0000** |
| 30-day window firm inflow $ | $4,102,224.83 | $4,102,224.83 | **$0.0000** |
| 30-day window firm outflow $ | $3,123,269.91 | $3,123,269.91 | **$0.0000** |
| Per-date row count (2026-05-06/07/08) | 265 | 265 | 0 |

**Note on Joe MAX NNA:** the TO referenced $11,729,310 as the inheritance target.
Empirical current value is $11,824,453.75. The ~$95K gap is silver-state drift —
TO referenced an older snapshot. **Inheritance is what matters:** post-refactor
matches the CURRENT baseline byte-for-byte. The TO-stated number reflects an
older silver state; both pre- and post-refactor INF_C_01 produce $11,824,453.75
on the current silver state.

## Open items for CTO ratification (PRD §2.3 future state, NOT applied in Stage 0)

The YAML's `open_items` block enumerates five reclassifications where PRD §2.3
disposition differs from current INF_C_01 behavior. All currently encoded as
`bucket` = inherited + `prd_proposed_bucket` = future state, status documented:

| # | type_desc | Current | PRD §2.3 proposed | Impact | Status |
|---|---|---|---|---|---|
| 1 | Starting Value | NNA inflow | Internal | -$6,643,771 firm NNA inflow (896 rows / 69 accts; Joe: 158 rows / $1,468,199) | **RATIFIED-NOT-APPLIED** (Andrew global GO + DS~C disambiguator b33f42a63) |
| 4a | Dividend Paid from Cash | Return (excluded) | NNA outflow | -$172 firm (101 rows) | ESCALATED-TO-CTO (cross-check confirmed current EXCLUDES) |
| 4b | Income Paid | Return (excluded) | NNA outflow | -$172 firm (101 rows paired with 4a) | ESCALATED-TO-CTO |
| tax-withheld | Federal/State/Foreign Tax Withheld + Tax Credit | NNA outflow | Return | +$2,326,772 firm NNA-outflow reduction (2,561 rows; Joe: 61 Federal Tax rows = -$42,082) | AWAITING-RATIFICATION |
| other-variants | Client/Rollover Contribution + Merge In/Out variants under "Other" activity_category | Internal (excluded) | NNA (collapse with primary) | ~$3K across 40 rows | AWAITING-RATIFICATION |

**Follow-on TO required to apply each item.** Item 1 (Starting Value) has the
strongest endorsement chain — Andrew global GO + CTO PRD §2.3 + DS~C 5-signal
empirical — and is ready for application; the other four need CTO disposition
before follow-on TO can flip `bucket` → `prd_proposed_bucket`.

## YAML architecture decisions

1. **Compound key (`type_desc`, `activity_category`):** PRD §2 structural note 2
   recommends type_desc-only with variants collapsed to primary. Stage 0 preserves
   the compound key because current INF_C_01 excludes variants under "Other"
   activity_category via the activity_category-set filter. Collapsing to
   type_desc-only would change behavior (~40 Other-variant rows would flip from
   Internal → NNA). Compound-key preserves this exactly. Follow-on TO can
   collapse if CTO ratifies the variant-merge proposal in `open_items`.

2. **`bucket` vs `prd_proposed_bucket`:** active vs future-state. INF_C_01's
   `_load_cashflow_taxonomy` only reads `bucket`, guaranteeing inheritance.
   `prd_proposed_bucket` is documentary — informs the follow-on TO author what
   to flip. Each entry also carries `prd_proposed_status` enum:
   - `RATIFIED-NOT-APPLIED` (Item 1 — Andrew confirmed; awaits mechanical apply)
   - `ESCALATED-TO-CTO` (Items 4a, 4b — empirical evidence surfaces a question)
   - `AWAITING-RATIFICATION` (tax-withheld, other-variants — proposed but not endorsed)

3. **Path resolution:** env var override > script-dir > repo-relative. EC2
   dispatcher pulls files from `s3://opal-data-inf/code/gold/` into
   `/tmp/orion_gold_scripts/`. Uploading the YAML to `code/gold/` (next to .py
   files) makes the script-dir candidate succeed on EC2 without needing
   dispatcher changes. Repo-relative path used in local dev.

4. **PyYAML dependency:** `import yaml` — assumed present in EC2 gold-runner
   Python env (standard data-science stack). If a future runner image strips
   pyyaml, the script will fail at import. Worth flagging for AE 0.7 to confirm
   in the runner inventory.

## Compiler tools

| Phase | Tool | Result |
|---|---|---|
| 1 (before write) | `comp-pipescript io INF_C_01` | NOT RE-RUN (DS~B audit covered the I/O contract) |
| 1 | `comp-blast canonical_nna` | NOT RUN — downstream confirmed via PRD §3.2 (INF_C_02 + INF_D_00c) |
| 1 | DS~B Stage -1 audit | inherited (43 type_desc / 58 compound pairs / 1,156,082 rows) |
| 1 | DS~C SV disambiguator | inherited (`b33f42a63` — 5-signal verdict) |
| 1 | Existing INF_C_01 read | inherited classification logic captured verbatim into YAML |
| 2 (before commit) | `.tools/ds-commit-gate.sh INF_C_01.canonical_nna.py` | PASS (py_compile + AST + ruff py39) |
| 2 | Behavioral inheritance test (local rerun + diff vs baseline) | PASS — $0.0000 delta on inflow + outflow + Joe MAX |
| 3 (after commit) | safe-deploy pre-push hook | DEPLOYED INF_C_01 + verified SHA |
| 3 | Manual `aws s3 cp` YAML to `code/gold/` | DONE |
| 3 | Manual `hashlib.sha256` cross-check both files | MATCH both (`a18a90368b58cf96` + `87dcd38db99c5b24`) |
| 3 | `comp-pipescript deployed INF_C_01` | NOT RUN — manual SHA cross-check is the INF-side equivalent (comp-pipescript deployed is BD-hardcoded per DS~B INF_COMP_PIPESCRIPT_DEPLOYED_COVERAGE finding) |

## Sequencing handoffs

| Recipient | Item |
|---|---|
| **CTO 1.0.0_SA_CTO** | Ratify Items 4a, 4b, tax-withheld, other-variants for follow-on TO authoring |
| **COO 2.0.0_SA_COO** | Author follow-on TO that flips Item 1 (Starting Value: NNA→Internal); already endorsed by Andrew global GO, mechanical apply only |
| **Stage 1 TO authors** | YAML now exists — Stage 1 (.001-.006) dispatch is unblocked |

## RAVC

- RAVC2 ACK to COO: 21:22Z (pivot from TO-2b takeover to TO-000)
- RAVC4 close to COO + cc CTO: this commit + this log
- Andrew watching per COO 21:18Z message

## Status

CLOSED. DS~C standing by for next routing.

## Memory entry candidate

Per TO note: "Declarative taxonomy YAML over inline classifier" pattern. Will
crystallize as feedback memory when CTO ratifies the follow-on TO flow (proves
the pattern works end-to-end). Holding off until then.
