# MDPF_TAXSMA closer-drive: Tax SMA built to 0.6.0, IAM live, Tax-off backend release applied -- 4.0.0_SA_CRO

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, TRACE

**Date:** 2026-10-01 (window 2026-09-30 ~13:0xZ to 2026-10-01 02:45Z)
**Task Order:** MDPF_TAXSMA under `/closer-drive` (FAST lease, seat 4.0.0_SA_CRO); ad-hoc Andrew-directs before it
**Status:** IN PROGRESS -- paused at a checkpoint for the two-device reboot
**Workspace CLOUD commit:** checkpoint `b240405088`, on origin/CLOUD `4053e6c255` (ls-remote read 02:40Z); this log's commit follows
**Portal DEV commits:** `4235e77c`, `370d2fe8` (both in origin/DEV `970d5c75`; not in origin/PROD `ba8e971f`)

---

## Objective

Andrew, 2026-09-30: get the Tax SMA total for the Alongside scorecard, then "run it to completion" on MDPF_TAXSMA
under `/closer-drive`, and later "what our priority is here is getting the tax sma getting sent through mdpf so it
appears in all the relevant places" (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_202xZ_TAXSMA_PRIORITY_THROUGH_MDPF_ALONGSIDE_DROPPED.md` @733b28e890).
This window took the project from "offline engine, nothing wired" to "all IAM live, Tax code deployed in both
functions with Tax off, one scheduled check and two external dependencies short of activation".

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find 'opal-data-49financial\|opal-data-cottonwood' infra/aws/terraform --files` | PASS | found the generated scope-to-bucket map in `modules/opal_name` |
| comp-find | `comp-find 'scope_long\\[\|scope_bucket\\[' infra/aws/terraform` | PASS | found the one accepted derivation pattern (`investor-reporting/directory/principal_49f.tf`) |
| comp-find | `comp-find 'tax_additive_aum' data/mdpf/tests portal/src` | PASS | 6 hits of 1246 files: the one test and the portal's optional type |
| comp-find | `comp-find 'ROUTE_BINDINGS_SHA256\|...' infra/aws/terraform/opal-assets` | PASS | proved the publisher's pin is a typed literal, not a remote-state read |
| comp-find | `comp-find 'portal/gold/mdpf/_code' --files` | FAIL | did not return inside 120 s; replaced by reading the last deploy ledger |
| comp-iam | `comp-iam service mdpf-gold-lambda` (after the iam.tf changes) | PARTIAL | lists the role's 13 statements incl. the new `sts:AssumeRole` and control RW; it models the function role, not the assumed Tax sessions |
| comp-iam | `comp-iam gaps` | SKIPPED | not run; the new grants were verified on the live primitive instead (40 simulation rows, one host exercise), which cloud-ops requires for new resources because comp-iam fails green |
| verify-ec2 | `infra/aws/ec2/verify-ec2.sh --ssm opal-gateway` | FAIL | "in sync", rc 0, with 0 checked (jq off PATH) and with the instance "unreachable" while SSM read Online; row MDPF_TAXSMA-S12 |

**What worked:** comp-find for locating the accepted naming patterns; the handler's own `qa_local` mode as a zero-write A/B instrument.
**What failed:** verify-ec2's false green; one comp-find timeout.
**Gap found:** no instrument reads deployed Gateway bytes reliably; a direct read-only SSM checksum was used.

---

## Work Completed

### 1. Ad-hoc Andrew-directs (2026-09-30)

A Windows Desktop shortcut into the home Mac over Tailscale/VNC. The Tax SMA total from Yang's workbook plus Schwab
0833 for the Alongside scorecard, then the Alongside restatement; Andrew later dropped Alongside as irrelevant.

### 2. MDPF_TAXSMA engine to contract 0.6.0 (E1, E2a, E2b)

- RIA column routes each workbook row to a firm; custodian per firm (0833 `fact_rps_s2` for 49 Financial, Black
  Diamond `fact_holdings` for Cottonwood); workbook AUM (Mn) fallback for an account its master does not hold.
- Production wiring: global workbook Bronze/Silver, per-firm dispositions and `taxsma_assets` Gold, live loaders.
- Served fold: Tax into the 49 Financial and Global totals, carry the last complete figure, no backfill
  (Andrew-direct 18:3xZ). Real run 2026-09-28: 49 Financial 11 of 11 accounts = 17,034,745.40; served spines
  09-29: 49 Financial 1,761,000,294.98, Global 2,083,972,030.82, reconciled to the cent.
- Portal: coverage accessor and page caption on DEV.
- Tests: `data/mdpf/tests/taxsma` 216 of 216; Gold suite 94 passed, 3 failed (pre-existing, baseline row S1).

### 3. Lease-tool regression and repair

My fix to `.tools/drive-mode.py` @05f0a0b5af read 435 of 1473 orders open (was 106); repaired @7acc39ca65 (103
open; self-test ALL HOLD). 1.0.0_SA_CTO told the sequencing ask was withdrawn.

### 4. Deployment sequence (all through `safe-apply`, vendored terraform 1.9.8)

| Step | Action | Result |
|------|--------|--------|
| 1 | TX-i-1, `mdpf-pipeline`: two scoped Tax roles + policies + `mdpf-gold-taxsma-policy` | 00:03:55Z, 5 added; re-plan No changes; ledger closed @14670cf66c |
| 2 | TX-i-2, `opal-assets`: `mdpf-publisher-taxsma-control-read-policy` | 00:16:59Z, 1 added; re-plan No changes; closed @73ef80ab94 |
| 3 | TX-i-3, moved to `mdpf-pipeline`: secret `gateway/global/taxsma-workbook-token` (no value) + `gateway-taxsma-workbook-bearer-read-policy` on `opal-gateway-role` | 01:52:55Z, 2 added; re-plan No changes; closed @c3d2237872 |
| 4 | Build both packages at e8994f23af | gold zip sha256 `ee12387e..` (39 modules), publisher `a63f896a..`; sidecars @75a4076b90 |
| 5 | Upload both artifacts with `content-sha256` | gold version `U4JsC9gYCgaK..`, publisher `Deg26fXt..`; downloaded back, hashes equal |
| 6 | TX-r-1 Gold, `mdpf-pipeline` | 02:15:52Z, 1 changed; deployed CodeSha256 `7hI4flW5..` = built; re-plan No changes |
| 7 | TX-r-1 publisher, `opal-assets` | 02:20:56Z, 1 changed; deployed CodeSha256 `pj+Jat96..` = built; `TAXSMA_ROLLOUT_SWITCH = OFF`; re-plan No changes |

### 5. Verification (actual output)

```
SIMULATION TX-i-1: rows as expected: 30 of 30        SIMULATION TX-i-2: rows as expected: 10 of 10
Gateway host, caller assumed-role/opal-gateway-role, 01:56:15Z:
  NEW_SECRET ResourceNotFoundException | CONTROL_NOT_HELD AccessDeniedException | CONTROL_HELD opal/mcp/ms-ingest-token
Deployed qa_local BEFORE (code 5aKNH5WB.., 02:12Z): status green, errors [], a4_objects_built 16
Deployed qa_local AFTER  (code 7hI4flW5.., 02:17Z): status green, errors [], a4_objects_built 16
SUMMARY: 16 compared -- byte-identical 0, process-time only 16, business-different 0
Served probe self-compare: documents as expected: 16 of 16; negative control (2 planted): 14 of 16, rc 1
```

### 6. Defects found and fixed before release

- The control write passed a full `s3://` address as a key into the assets bucket and would have been refused on
  every later run (row S8, fixed @338665c1b1).
- N+1 category Gold copies: no reader, wrong bucket, a duplicate output path; no longer written (row S9).
- With Tax off the new bundle added a null `total.tax_additive_aum` on three scopes; now emitted only when Tax is
  additive (@3f03d42024), found by diffing the deployed bundle against the new one.

### 7. `/closer trace` (01:16Z to 01:30Z)

`org/tier1_exec/4.0.0_SA_CRO/deliverables/TAXSMA_MODEL_PORTFOLIOS_END_TO_END_GAP_BRIEF_20261001.md` with its evidence
JSON: 9 hops, 3 MISSING, 5 INCOMPLETE, 1 WORKS at the time of the read. The page hides the Tax member because its
served amount is null; the tree renders it once an amount is served.

### 8. MCP traffic

About 14 messages, all with 0.0.0_AB_MSTR. Significant: rows S7/S10 (the `opal-gateway` root has appliers whose
commits are not on origin); two merge windows (origin pulls 68e15a70df and 8ac17decf6); three checkpoints
(1422c121ef, withdrawn; b240405088; this log).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Two scoped prelude roles, not one | each firm bucket's live `DenyForeignFirmPrincipals` admits only its own short token |
| The operational control lives at the global scope in `opal-data-mdpf` | it spans both firms and the publisher's role is outside the 49 Financial fence |
| TX-i-3's secret and Gateway grant declared in `mdpf-pipeline`, not `opal-gateway` | two plans of `opal-gateway` each carried destroys of other projects' live grants; Andrew then ruled that root is applied from site Z only |
| Value a STRATEGY_CONFLICT account and keep its reason | a label conflict is not a value conflict; reversible by one tuple |
| Did not invoke the publisher after its deploy | it has no dry-run mode and a hand-run writes the served plane; the scheduled 13:50Z run is the check |

---

## Files Modified

See commit messages: 338665c1b1, 3f03d42024 (engine and publisher code), 8baf85002e, bb9a291faa, bf643a0530,
9db0981bd6, 853c67b719 (Terraform), 75a4076b90 (package sidecars), eabe4b79cd, 294c511782 (surprise rows S7-S9,
S11-S13), c2f48b5000 (trace), 1422c121ef, b240405088 (STATUS, site Z request, served baseline and probe).

| File | Change | Committed |
|------|--------|-----------|
| `org/critical_paths/.open_deploys/mdpf_taxsma-tx-r-1.json` | OPEN sentinel, 5 of 6 legs closed, window 14 h | Yes -- `b240405088` |
| `infra/aws/lambda/layers/mcportal-grant-writer-deps/.build/`, `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/.build/` | gitignored build leftovers from planning `opal-gateway`; harmless | No -- ignored |

---

## Blockers

- BLOCKED on site Z NFRA_OPLGTW (`1.0.0_SA_CTO~O` / `2.0.0_SA_COO~O`): the Gateway release carrying the Tax workbook
  route with its capability off, including the two `.env` lines `deploy-to-ec2.sh` lacks. Evidence: host read
  01:25:43Z, `app/taxsma_workbook.py` ABSENT. Request:
  `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/SITEZ_GATEWAY_RELEASE_REQUEST_TX-r-2.md`.
- BLOCKED on Andrew: the `opalbloomberg@opalinvest.com` sign-in at the Gateway (TX-r-3 AC2, AC5, AC6) and the
  never-widen sign-off (the CTO seat died 2026-09-30 ~23:2xZ; relaunch pending).

---

## Current State

Nothing serves Tax SMA. Lambda `mdpf-gold-lambda` runs code `7hI4flW5..` (built at e8994f23af, six Tax modules)
with only `MDPF_GOLD_COMMIT` in its environment, so `taxsma_capability_configured()` is False and Tax is DISABLED;
Lambda `opal-assets-mdpf-portal-publisher` runs code `pj+Jat96..` with `TAXSMA_ROLLOUT_SWITCH = OFF`. Roles
`mdpf-49f-taxsma-role` and `mdpf-cot-taxsma-role`, policies `mdpf-gold-taxsma-policy`,
`mdpf-publisher-taxsma-control-read-policy`, `gateway-taxsma-workbook-bearer-read-policy` and secret
`gateway/global/taxsma-workbook-token` (0 versions) exist; all seven Tax S3 prefixes hold 0 objects. One ledger is
OPEN by design, `mdpf_taxsma-tx-r-1`, on leg V2 (the 13:50Z publisher run). Rollback: Gold artifact S3 version
`8eu2ppmBW1z1j2MOwTQc3G27uo9SbDXD`, publisher `ZLaQC2nGuQ2hP72JpdTA4RWfciYhFoql`. The resume list is
`org/missions/D8/MDPF/MDPF_TAXSMA/STATUS.md`; the lease runs to 05:06Z and needs re-arming after the reboot
(Gateway surfaces dropped).

---

## Next Steps

1. **Run leg V2 after the 13:50Z publisher run** -- `py -3.12 org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/probes/tx_r_1_served_delta.py compare org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/tx_r_1_served_baseline.json`; 16 of 16 closes the ledger, a FAIL is a rollback.
2. **[0.0.0_AB_MSTR] relay site Z's reply on the Gateway release** -- release commit, host sha256 of `app/taxsma_workbook.py` (expected `6acc3e8c..`), four acceptance results.
3. **[1.0.0_SA_CTO] and a `2.0.0_SA_COO` seat: the never-widen halves for TX-r-3** -- both served keys, writer count, rollback per key.
4. **Activation (TX-r-3)** -- bearer value into the secret, the identity record, four Gold values, one controlled read, switch ON; Tax first serves one trading day later by the current rule (Andrew's decision parked in STATUS).
5. **Unblocked meanwhile** -- the Cottonwood double-count read (bd-rebalancer model assignments for the two accounts); the 0.6.0 re-cut of the 102 expected cases (TX-v-1) and the journey harness (TX-v-2).
