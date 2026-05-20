# SSCN_DIVDEF.009 — Factor Registry Category Regen + Scanner Lambda Redeploy + Re-fire

**Agent:** 0.5.0_AE_OpalETL
**Date:** 2026-05-20
**TO:** SSCN_DIVDEF.009.ae-registry-regen-and-lambda-redeploy
**PRD:** docs/architecture/SSCN_DIVDEF.md v0.6 (commit 2e9fe7f3a)
**Status:** COMPLETE + CLOSED — all AC1-AC7 PASS; RAVC2 sent to 2.0.0_SA_COO
CC 1.0.0_SA_CTO; **RAVC4 ACCEPT received from 2.0.0_SA_COO 2026-05-20** — all 7
ACs validated, no acceptance flex, `SSCN_DIVDEF.json` `.009` flipped complete.

---

## Summary

The bundled `factor_metadata_registry.json` used a wrong collapsed 11-category
taxonomy — 176/282 common factors (62%) mis-grouped. This TO regenerated the
registry `category` field from the canonical master `Signal Summary.xlsx`
(Andrew-supplied), redeployed `opal-security-scanner-processor` via Terraform
(`security-scanner-v1.1.3`), and re-fired the Lambda so `latest/` re-emitted
with the corrected 18-group taxonomy.

---

## Files Changed

| File | Change |
|------|--------|
| `infra/aws/lambda/opal_security_scanner_processor/factor_metadata_registry.json` | `category` field regenerated from master; 178 values changed; 5 factors appended; `_note` rewritten |
| `infra/aws/lambda/opal_security_scanner_processor/Signal_Summary.xlsx` | NEW — canonical master source-of-record (the file Andrew supplied) |
| `infra/aws/lambda/ci/lambda-source-map.json` | `artifact_sha256` + `last_deployed_commit`/`at` for opal-security-scanner-processor |
| `infra/aws/terraform/security-scanner-pipeline/CHANGELOG.json` | entry `security-scanner-v1.1.3` |

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Regen registry (probe script `.runtmp/sscn009/regen_registry_category.py`) | 178 category values changed; 5 appended; 18-group set |
| 2 | Commit source | `ec015ec27` feat(security-scanner): regenerate factor registry category from master taxonomy |
| 3 | build-and-upload.sh security-scanner-pipeline | SHA256 `sqEdjldeuQIUJEpFGhCYE1iEblHDTogiHerwH3pzph0=` (16K zip; xlsx NOT bundled) |
| 4 | Commit source map | `1b6ad2298` ci(security-scanner): upload artifact [skip ci] |
| 5 | terraform plan | 1 to change (sscn_processor s3_object_version + source_code_hash) |
| 6 | terraform apply | 0 added, 1 changed, 0 destroyed |
| 7 | 0-diff replan | No changes. Infrastructure matches the configuration. |
| 8 | record-terraform-deploy.sh | CHANGELOG.json entry written; own commit blocked by owned-paths hook (committer=Andrew); re-committed `2aa80bf25` under AE author |
| 9 | Tag + push | `security-scanner-v1.1.3` created + pushed `--follow-tags`; CLOUD pushed |
| 10 | Re-fire | delete-and-re-PUT 2026-05-18 source XLSX 15:42:32Z; Lambda re-processed; `latest/` regenerated 15:42:51-15:43:11Z |

**0-diff confirmed:** YES — post-apply replan reported "No changes."

---

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| security-scanner | `security-scanner-v1.1.3` | `c67cf33805` (deploy commits: `ec015ec27`, `1b6ad2298`, `2aa80bf25`) |

**Tag deviation:** TO/PRD v0.6 specified `security-scanner-v1.1.2`. That tag was
ALREADY consumed — DT 0.3.0 created it 2026-05-19 14:43Z for SSCN_DIVDEF.002 AC7
(sscn_processor manifest.json IAM grant). Per the MEMORY.md pipeline-tag rule
(`git tag -l` before tagging; never assume next version), `v1.1.3` is the
correct next-in-series. COO approved 2026-05-20 (ACK message); CTO CC'd.

---

## Acceptance Criteria — Evidence

**AC1 PASS** — every common factor `category` == master "Group". Field-scoped
check: 282/282 common factors match the master `Python_SN` Signal->Group; 0
mismatches.

**AC2 PASS** — 5 master signals missing from the registry appended:
`mkt_val`, `economy_conc`, `indgrp_conc`, `sector_conc`, `subsec_conc` — all
master Group `size`; records sourced from the master `Python_SN` sheet (the
only available canonical source — no prior registry record existed). 2
registry-only codes resolved: `downbeta_252d` and `upbeta_252d`,
`systematic` -> **`beta`**.
- *Resolution rationale:* the entire beta family in the master is group `beta`
  (`beta_21d`, `beta_63d`, `beta_252d`, `downbeta_63d`, `upbeta_63d`). The 2
  registry-only codes are the 252-day windows of `downbeta_63d`/`upbeta_63d`;
  the prior registry `_note` itself states they were "inferred from 63D
  counterparts." Nearest master group = `beta`. Unambiguous.

**AC3 PASS** — `category`-field-only diff. Field-scoped diff over the 284 prior
factors: `name`/`relationship`/`ic`/`coveragePct`/`autocorrelationPct`/
`assetClass`/`systematic` — 0 changes, byte-identical to the prior registry.
178 `category` values changed (176 common mis-grouped + `downbeta_252d` +
`upbeta_252d`).

**AC4 PASS** — post-redeploy + post-re-fire `latest/factor_metadata.json`:
289 factors, group set = exactly the 18 master groups, ZERO
`yield`/`systematic`/`sentiment`/`institutional`. asOf 2026-05-18.
Post-re-fire group counts: size 11, efficiency 22, growth 25, management 11,
profitability 21, quality 15, solvency 28, value 26, analyst 12, governance 11,
crowding 25, insider 10, short 10, liquidity 6, beta 7, momentum 15,
technical 22, volatility 12.

**AC5 PASS** — 13 DIVZ preset codes verified group-correct against master:
dy_ntm/shldr_yield/ey_ntm/fcfy=value; ret_mom_252d/velocity_63d/pcta52wl=
momentum; short_pct_chg_12m/days_to_cover=short; leverage=solvency;
eps_est_rev_45d=analyst; dps_gr_1yr=growth; accruals_bs=quality. 13/13 match.

**AC6 PASS** — post-apply terraform plan = 0-diff ("No changes");
`security-scanner-v1.1.3` tag created + pushed `--follow-tags`;
`lambda-source-map.json` updated (`artifact_sha256` +
`last_deployed_commit` `ec015ec27`).

**AC7 PASS** — regression guard. The 5 universes' `latest/universes/{u}/
scanner_data.json` are byte-identical pre vs post re-fire (sha256 match on all
5). A `category`-only registry change did not perturb the percentile compute.
Confirms `relationship` was untouched (percentile signs unchanged).

| Universe | scanner_data.json sha256 (pre == post) |
|----------|----------------------------------------|
| sp500 | `8d40c5143b26d423dcbad5a7ea9b88a9efbce73ff9f8d0dffe1790dfd1f0c64f` |
| r1000 | `eb5cd917e4a17e2e900ae3de5248c4251faadd5ad37858e87974fd671b70bbf3` |
| rmidcap | `7c37b71723ec1c802b5142a5cbe4b2d0adbf1efa2cbbed45644728aec0e45779` |
| sp400 | `9aad1c2118f0013dd9aaf8d8382023a639df92559b5b399562027685c4c3681c` |
| msciusa | `93ff915c75bc3b64ae994912f2237bcaafa7b270e6a246d223e7d5a9b4a5b3e2` |

*Structural note:* AC7 was structurally guaranteed and the empirical hash check
confirms it. `lambda_function.py` computes percentiles for `scoring_cols`
(XLSX-column-driven, not registry-driven) using only each factor's
`relationship`. The 5 appended factors are all in `NON_SCORING_COLS` (identity/
concentration columns) so they never enter the percentile compute; and the
regen left `relationship` byte-identical on all 284 prior factors.

---

## Verification

```
Lambda runtime (post-apply):
  CodeSha256:  sqEdjldeuQIUJEpFGhCYE1iEblHDTogiHerwH3pzph0=  (== build == TF == source map)
  LastModified: 2026-05-20T15:38:46Z
  Runtime: python3.12

Re-fire (delete-and-re-PUT 2026-05-18 source XLSX):
  re-fire start TS:  2026-05-20T15:42:32Z
  source XLSX:       s3://opal-data-portal-v2/security_scanner/uploads/2026-05-18/Screening_DIVZ_IDVZ_20260518.xlsx
  delete:            DeleteMarker created (bucket versioning ENABLED -- recoverable)
  re-PUT:            6929919 bytes, VersionId s.W38ZZK3_jAil0IpZBIHROknh5TnfQA, LastModified 15:42:36Z
  local safety copy verified pre-delete: 6929919 bytes, sha256 1556eb29...

latest/ regeneration (all > re-fire TS 15:42:32Z):
  factor_metadata.json          15:42:51Z   289 factors / 18 groups (was 284 / 11)
  universes/sp500/scanner_data  15:42:54Z
  universes/r1000/scanner_data  15:43:00Z
  universes/rmidcap/scanner_data 15:43:05Z
  universes/sp400/scanner_data  15:43:07Z
  universes/msciusa/scanner_data 15:43:11Z

  factor_metadata.json content delta (284/11 -> 289/18) is itself proof the
  v1.1.3 Lambda re-processed with the regenerated registry.
```

---

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `comp-iam service opal-security-scanner-processor` | 3 ops (s3:PutObject, s3:GetObject x2), all `[UNKNOWN]` | UNKNOWN != MISSING. This TO changed a bundled JSON asset only — `lambda_function.py` untouched, so the IAM surface is definitionally unchanged from v1.1.1/v1.1.2. No new boto3 call, no IAM delta. TO `<expect>` satisfied; `comp-iam gaps` not required. |
| `python -m py_compile` (regen script) | exit 0 | `.runtmp/sscn009/regen_registry_category.py` |
| `ruff check --target-version py39` (regen script) | All checks passed | regen script gated per CLAUDE.md Rule 14 |
| `terraform plan` (post-apply replan) | 0-diff | "No changes. Your infrastructure matches the configuration." — AC6 |

`lambda_function.py` was not edited, so `comp-pipescript`/`comp-iam gaps` were
not required. The regen script is retained under the probe path
`.runtmp/sscn009/` (not committed, not bundled into the Lambda zip).

---

## Anomalies / Notes

1. **Tag v1.1.2 already taken** — see Deployment Tags. Used `v1.1.3`, COO-approved.
2. **`_note` field updated** — the registry top-level `_note` described the old
   wrong 11-category taxonomy; left as-is it would be actively misleading
   post-regen. Rewritten to describe the v0.6 regen provenance. `_note` is file
   provenance, not per-factor data; AC3's byte-identical scope is the per-factor
   data fields. COO approved 2026-05-20.
   - OLD: "Factor metadata registry sourced from XLSM Tab 3 '3-Factor Data'...
     Categories mapped to V0 contracted taxonomy: efficiency, size, growth,
     management, profitability, quality, sentiment, systematic, value, yield,
     institutional. XLSM 18-category taxonomy collapsed..."
   - NEW: "Factor metadata registry. The `category` field was regenerated
     2026-05-20 from the canonical master 'Signal Summary.xlsx' (sheet
     Python_SN, Signal->Group, 18 groups) per SSCN_DIVDEF.009 / PRD v0.6..."
3. **Master sheet name** — TO/PRD reference sheet `Python_SN_New`; the actual
   `Signal Summary.xlsx` has sheet `Python_SN` (no `_New`). Verified the
   Signal->Group mapping is identical to `Signal_Summary_with_PPS.xlsx`
   (`Python_SN_with_PPS`) — 0 group differences — confirming CTO's "stable
   across old/new sheets, 0 group changes." Used `Python_SN` (the sheet the
   TO-named file actually contains).
4. **5 appended factors' non-category fields** — sourced from the master
   `Python_SN` sheet (name, relationship from Sign, ic/coveragePct/
   autocorrelationPct), since no prior registry record exists for them. This is
   not a stat-refresh of existing factors (out of scope) — it is populating new
   records from the only available canonical source.
5. **record-terraform-deploy.sh hook block** — known tooling issue: the script
   committed as committer `Andrew Berman`, blocked by the owned-paths hook
   (Andrew not in CLOUD_OPS_OR_ETL `permitted_agents`). The CHANGELOG.json +
   source-map.json content it wrote was correct; re-committed under AE author
   identity (`2aa80bf25`). No data lost.
6. **Master list placement** — committed `Signal_Summary.xlsx` (not a CSV) at
   `infra/aws/lambda/opal_security_scanner_processor/`. A CSV export was the
   first choice but `*.csv` is gitignored by `infra/.gitignore:74`; the `.xlsx`
   is not ignored and is the literal artifact Andrew supplied — better
   source-of-record fidelity. Verified `build-and-upload.sh` zips only
   source-map `files[]` (`lambda_function.py` + `factor_metadata_registry.json`)
   so the xlsx is NOT bundled into the Lambda artifact, and the
   ADHC_DRIFTD.002 parity check scans `*.py` only so the xlsx does not trip it.

---

## Current State

- `opal-security-scanner-processor` deployed at `security-scanner-v1.1.3`,
  CodeSha256 `sqEdjldeuQIUJEpFGhCYE1iEblHDTogiHerwH3pzph0=`.
- `s3://opal-data-portal-v2/json/security_scanner/latest/` fully regenerated
  with the corrected 18-group taxonomy (factor_metadata.json) and byte-stable
  scanner_data.json (AC7).
- All 7 ACs PASS. RAVC2 sent to 2.0.0_SA_COO CC 1.0.0_SA_CTO.
- **RAVC4 ACCEPT from 2.0.0_SA_COO 2026-05-20** — closed clean, no acceptance
  flex; `SSCN_DIVDEF.json` `.009` flipped complete by COO. Per COO: all
  SSCN_DIVDEF implementation TOs (.001-.005, .007-.010) are now done — only the
  `.006` bundled PROD push remains, gating on Andrew's DEV smoke.
- TO status -> complete. AE queue clear, no pending task orders.

## Next Steps

- `[2.0.0_SA_COO]` RAVC2 validation AC1-AC7. `SSCN_DIVDEF.json` ws=AE flip on accept.
- `[1.0.0_SA_CTO]` CC — v0.6 closeout: sync the docs/ reference-duplicate
  registry copy + correct `SSCN_GROUP_TAXONOMY.md` (CTO-lane per the TO do_not
  rule; out of .009 scope).
- `[SSCN_DIVDEF.010 — DE/RD]` portal `categoryOrder.ts` 18-group update runs
  parallel; both .009 + .010 gate the bundled `.006` PROD push.
