# VUG Security-Naming Defect: Ground-Truth, Fix, Redeploy -- 1.0.0_SA_CTO~X

**Date:** 2026-08-18 (~1600-1740Z)
**Task Order:** ad-hoc, Andrew-direct at the CTO~X terminal (screenshot + instruction, mid-startup)
**Status:** COMPLETE
**Archetype:** defect-trace -> atom_decomp ground-truth -> code+data fix -> TF deploy -> served-artifact verify

---

## Objective

Portal Positioning page, Attribution Breakdown table: ticker VUG rendered NAME =
`1.61931034482759`. Andrew: investigate the security filtering/naming system (suspected a DynamoDB
classification list or Yang-pipeline Lambda code), identify the issue, rectify end-to-end incl.
redeployments, log step-by-step; begin with the atom_decomp workflow for rigorous SSOT ground truth
before work. Startup abbreviated per his word (no registration / no agent comms).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | "where does the Positioning page get security names" | PARTIAL | 3-way near-tie; routed me to comp-estate, which was right |
| comp-estate | positioning | PASS | full chain in one call: producers -> served keys -> frontend components; grounded the whole investigation |
| comp-find | --name / content, x8 calls | PASS | located producer source, both classifier-module copies, seeders, TF, SFN reference, atom_decomp package; DENOMINATOR lines quoted throughout |
| comp-pulse (via safe-commit) | diff, per commit | PASS | risk reflex clean on all 4 commits |

**What worked:** comp-estate positioning was the single highest-value call -- producers/served/frontend
in one read. comp-find's band separation (HEAD vs SURFACED) made the two-classifier-copies and
seeder discovery fast.
**What failed:** nothing silently; the comp-rail HUD correctly gated two greps until markers/comp-find.
**Gap found:** none new (comp-estate served-name caution already in law).

---

## Work Completed (step by step)

### 1. Symptom grounded on the served artifact (not the screenshot)
Downloaded `s3://opal-data-portal-v2/json/positioning/holdings_attribution_data.json`
(generated_at 2026-08-04T22:32:55Z, as_of 2026-07-31). VUG `name` = four distinct numerics, one per
period sheet ({1.61931034482759, 0.416312056737589, 4.1, 0.935458167330677}). Census over the whole
file: 56 held tickers, `name` NEVER a real security name -- numeric junk or `--`.

### 2. Chain mapped via comp-estate
`yang-generate-holdings-attribution` (Yang SFN, monthly `attribution_excel` upload) -> served JSON ->
`portal/src/pages/Attribution/tabs/SelectionTab.tsx`.

### 3. Producer read; root cause 1 found
`lambda_function.py:574` read the holding name from hardcoded Excel col idx 4 ("Column E"), a
pre-June-2026-format vestige. The June-2026 export shifted portfolio blocks left 3 cols; detection was
made scan-based then (in-file comment) but the name read stayed fixed. Parsed the actual 20260731
workbook: **it has NO name column at all** -- col 4 = first portfolio's Style Bench Average Weight.
Hence numeric names, different per period sheet.

### 4. Frontend read; the mask found
`SelectionTab.tsx:162 etc.`: `ETF_NAME_FALLBACKS[h.ticker]?.name || h.name` -- a hardcoded map masks
the junk for every held ticker EXCEPT VUG (0 occurrences in all 4 portal ticker maps). That is why
exactly one row leaked.

### 5. DynamoDB SSOT found and censused; root cause 2 found
`etf-classifications` (Andrew's remembered "classification list" -- confirmed real, TF-managed,
queried by the Lambda for asset classes but NEVER for `name`). Full scan: 116 rows, 60 ticker-as-name
seed placeholders. **VUG the only HELD ticker among them**, and the only held ticker absent from
`CANONICAL_SECURITIES` (seed_canonical_securities.py, last verified 2026-03-25) and from `_shared`
`ETF_NAME_OVERRIDES` -- it entered the models after the last canonical sweep, registered nowhere.
Canonical display name confirmed in-estate: served `positioning_data.json` already carries
`VUG -> "Vanguard Growth ETF"` (PKL metadata path).

### 6. atom_decomp SSOT rectangle written BEFORE any mutation
`org/tier1_exec/1.0.0_SA_CTO/deliverables/VUG_SECURITY_NAMING_ATOM_DECOMP_SSOT_20260818.md` --
focused single-seat run per SKILL.md Rule 14 with recorded boundaries; 16 PROVEN cells (incl. Rule-22a
deployed-bytes==repo baseline, sha256 both members), 1 owned UNKNOWN; fix design cites cells.
Guard cell 13: the seeder's `--yang` put_item DROPS `management_style`/`sector` (VTV measurably lost
both) -- so the data fix was a targeted attribute-preserving `update-item`, NOT a seeder run.

### 7. Fixes
- **Code** (78ae0b583e): `resolve_display_name(ticker, classification, excel_value)` -- DDB registry
  name -> Excel value only if an actual name (never numeric / `--` / ticker-equal) -> ticker; wired
  into the horizontal parser (classifier lookup already in the loop, zero added I/O, no IAM delta);
  stale docstrings corrected. Vertical (pre-2026) parser untouched.
- **Data:** targeted `update-item` on `etf-classifications` VUG: name -> 'Vanguard Growth ETF';
  ALL_NEW response confirms management_style/sector preserved; prior value recorded in the commit +
  updated_by field (reversible).
- **Registry parity** (617c434397, d6afb07089): VUG added to `_shared` ETF_NAME_OVERRIDES (a reseed
  would otherwise REGRESS the DDB name to the ticker) and to CANONICAL_SECURITIES (equity /
  US Large Cap). `_shared` also gained `from __future__ import annotations` (commit-gate fail-closed).

### 8. Pre-deploy exercise (build-time correctness, then port)
Ran the edited parser locally against the real 20260731 workbook + live registry: 5 models, 414 rows,
56 tickers, ZERO numeric/placeholder/ticker-equal names; VUG='Vanguard Growth ETF'; controls
VTV/QQQ/CASH_USD correct.

### 9. Deploy (TF-only), ledger-tracked
`org/critical_paths/change_management/20260818T1710Z_vug-naming-holdings-attribution_deploy_completion.md`
opened at start, CLOSED complete. build-and-upload (artifact sha256-verified) -> source map committed
(4ebc9e7f4f) -> plan (exactly 1 in-place change) -> safe-apply (serial stamped per LD-0290; 2 routine
msgs reviewed, no [STOP], HALT_ACK=1) -> 0-diff -> record-terraform-deploy -> tag yang-pipeline-v1.5.4.
Post-deploy package re-downloaded: deployed bytes == new repo bytes. Push: BLOCKED by LD-0367/0368
integrator-only gate, correctly -- commits + tag ride the integration window (lanes commit,
integrators push). Not a stranded leg: the AWS deploy is landed, 0-diffed, byte-verified.

### 10. Regenerate + verify at the consumed end
Invoked the redeployed function with the production-shaped 20260731 manifest event (rc 200,
model_count 5), then verified the SERVED artifact: generated_at 2026-08-18T16:46:50Z; VUG =
'Vanguard Growth ETF' in every period; zero numeric/`--` names file-wide; 414 rows / 56 tickers with
membership IDENTICAL to the prior vintage; **non-name payload byte-identical** to the 08-04 vintage
(names-only delta -- the regression control). Frontend needs no change: VUG is not in
ETF_NAME_FALLBACKS, so the fixed `h.name` flows to the render; edge route confirmed live
(auth-gated 401 as designed for anonymous reads; producer writes CacheControl no-cache).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Fix name at the PRODUCER via the DDB registry, not by adding VUG to the frontend map | The registry's own docstring declares it the SSOT replacing scattered hardcoded maps; a 5th map entry deepens the anti-pattern (Build Ladder rung 1) |
| Targeted update-item, not a seeder run | Seeder's --yang path drops management_style/sector on rows it touches (measured on VTV) |
| Registry-parity edits to BOTH repo name sources | Without them, the next seed run regresses the DDB row to the placeholder -- the exact mechanism that created it |
| Vertical (old-format) parser untouched | Its format carried real names in its name column; minimal-change discipline |
| Push left to the integration window | LD-0367/0368 integrator-only gate; deploy itself complete + verified |

## Surfaced, not chased (per no-inferred-remediation)

- 59 non-held `etf-classifications` rows still carry ticker-as-name placeholders -- harmless until such
  a ticker enters a model (exactly how VUG happened). A future canonical sweep closes the class; the
  seeder's attribute-dropping put_item (cell 13) should be fixed before any wholesale --yang run.
- `etf_classifications_dynamodb.py` exists as two byte-copies (holdings-attribution +
  generate-positioning) -- Rule 22a two-homes class.
- 4 overlapping hardcoded portal ticker->name maps remain; the DDB table exists to replace them.
- Two routine inbox items surfaced by HALTGT (CRO~A tightening spec for base-CTO ratify; COO
  DEPLOYCENSUS addendum) -- for the CTO seat's queue, untouched per Andrew's no-comms word.
