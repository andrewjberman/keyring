# SSCN_UNVREV.001 — Lambda universe-map revert (legacy 6-set) + data refresh

**Agent:** 0.5.0_AE_OpalETL (AWS Engineer, base lane)
**Date:** 2026-05-22
**TO:** `SSCN_UNVREV.001.ae-lambda-universe-revert-and-data-refresh.md` (from 0.3.0_DE_TradingOperations)
**Status:** COMPLETE — all 6 acceptance criteria PASS.

---

## Summary

Andrew ruled 2026-05-21 to revert the SSCN_DIVDEF v0.2 universe migration: Yang's
refreshed FactSet export `Screening_DIVZ_IDVZ_20260519.xlsx` empirically carries the
legacy 6-set weight columns, not the v0.2 5-set. SSCN_UNVREV.001 reverts the Lambda
`UNIVERSE_MAP` and refreshes the data.

**Execution note (honest framing):** Both Part A (Lambda revert + deploy) and Part B
(xlsx upload) were executed on **2026-05-21** by a prior session of this agent — the
agent was brought online by Andrew at 19:18Z, committed the revert at 19:19Z, deployed
v1.2.0 at 19:33Z, and uploaded the trigger file at 19:46Z. That session was interrupted
before writing a log or flipping the TO. **This session is the verification + closure
pass:** every AC was re-verified against live AWS/S3/git state (ship-attestation is
necessary-not-sufficient — deploy-attestation was confirmed independently). Nothing was
re-deployed; the work was already live and correct.

---

## Deployment Sequence (Part A — executed 2026-05-21, verified 2026-05-22)

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source | `ee442cd07` fix(security-scanner): SSCN_UNVREV.001 -- revert UNIVERSE_MAP to legacy 6-set |
| 2 | build-and-upload.sh | artifact SHA256 `AUDtMWNcR1vkr6CQQEQkFrhnd+LI5ZpzFXOM5NRXZME=` |
| 3 | Source map updated | `lambda-source-map.json` -> `last_deployed_commit ee442cd07`, sha256 match |
| 4 | terraform apply | 1 changed (sscn_processor function code) |
| 5 | 0-diff plan (this session) | `No changes. Your infrastructure matches the configuration.` |
| 6 | Core doc | `pipeline_inventory.xml` security-scanner `current_tag` -> `security-scanner-v1.2.0` (this session) |
| 7 | record-deploy + tag | CHANGELOG `security-scanner-v1.2.0` deployed_at 2026-05-21T19:42:00Z; tag pushed |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| security-scanner-pipeline | `security-scanner-v1.2.0` | `ee442cd07` (on origin/CLOUD; tag on origin) |

---

## Acceptance Criteria — all PASS

- **AC1 — UNIVERSE_MAP is the 6-entry legacy dict.** PASS. Deployed Lambda
  `CodeSha256 = AUDtMWNcR1vkr6CQQEQkFrhnd+LI5ZpzFXOM5NRXZME=` — byte-identical to the
  `security-scanner-v1.2.0` artifact (CHANGELOG + source-map). Source `UNIVERSE_MAP` =
  `{sp500:wt_ivv, r1000:wt_iwb, r1000v:wt_iwd, acwx:wt_acwx, eafe:wt_efa, eafev:wt_efv}`.
- **AC2 — 0-diff + tag + source map.** PASS. `terraform plan` (this session) =
  "No changes." `security-scanner-v1.2.0` tagged (`dc3fc2bb8`) and present on origin;
  `ee442cd07` on origin/CLOUD; `lambda-source-map.json` updated.
- **AC3 — xlsx uploaded.** PASS.
  `s3://opal-data-portal-v2/security_scanner/uploads/20260519/Screening_DIVZ_IDVZ_20260519.xlsx`
  — 8,624,622 bytes, uploaded 2026-05-21 19:46:04Z.
- **AC4 — all 6 universes fresh.** PASS. `universe_data.json` + `scanner_data.json` for
  each of `{sp500,r1000,r1000v,acwx,eafe,eafev}` + `latest/factor_metadata.json`, all
  timestamped 2026-05-21 19:46Z (the trigger run).
- **AC5 — spot-check.** PASS. `sp500` universe_data.json: 502 securities (matches the
  file's `wt_ivv` member count), `country` populated ("United States"). `acwx`:
  1,682 securities, **0** rows with empty `country` (sample: Taiwan, South Korea,
  Netherlands, Hong Kong, UK...).
- **AC6 — scanner values + pctls populated.** PASS. `sp500` scanner_data.json rows
  carry both `values` (284 factor keys) and `pctls` (284 keys); sample row 281/284
  non-null on each.

## Trigger run evidence (CloudWatch — stream 2026/05/21/[$LATEST]f5cc590a5e22...)

```
asOf=20260519 | Loaded 2707 rows x 335 columns
sp500  (wt_ivv):  502 securities after filter
r1000  (wt_iwb): 1002 securities after filter
r1000v (wt_iwd):  864 securities after filter
acwx   (wt_acwx):1682 securities after filter
eafe   (wt_efa):  677 securities after filter
eafev  (wt_efv):  405 securities after filter
Processing complete. asOf=20260519, universes processed=6
```
No ERROR, no "skipping universe" lines — clean 6-universe run.

---

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-iam service opal-security-scanner-processor` | 3 S3 ops (`get_object` x2, `put_object`) — all pre-existing; no new boto3 call in the revert (a `UNIVERSE_MAP` dict edit only). No MISSING flagged. Clean. |
| `comp-pipescript deployed` | N/A — this is a Lambda, not a gold runner. The 0-diff `terraform plan` is the deployed-state check (AC2). |
| `comp-iam gaps` | N/A — `iam.tf` was not touched by this TO. |

---

## Current State

- `security-scanner-v1.2.0` is the deployed + tagged state. Lambda `UNIVERSE_MAP` is the
  legacy 6-set. All 6 universes regenerated in S3 `latest/` from the 2026-05-19 export.
- TO `SSCN_UNVREV.001` self-flipped to `complete`.
- `pipeline_inventory.xml` security-scanner `current_tag` brought current to
  `security-scanner-v1.2.0` (was stale at v1.0.0 — drift predating this TO).

## Next Steps / flags

- `[0.3.0_DE_TradingOperations]` RAVC2 sent with AC1-AC6 evidence (CC `2.0.0_SA_COO`).
  PROD coupling: the portal-side universe revert must not promote before AC4 — AC4 is
  now satisfied (6 universes live in S3). DT bundles the portal PROD push after Andrew's
  DEV smoke.
- `[follow-up, non-blocking — needs Andrew/COO sign-off, S3 deletion]` `latest/universes/`
  retains 3 **stale** v0.2-only universe prefixes — `msciusa/`, `rmidcap/`, `sp400/` —
  timestamped 2026-05-20, no longer emitted by the reverted Lambda. Harmless leftovers
  (the reverted portal stops requesting them) but cosmetically stale. Deleting S3 objects
  requires explicit confirmation — flagged, not actioned. Out of this TO's scope.
