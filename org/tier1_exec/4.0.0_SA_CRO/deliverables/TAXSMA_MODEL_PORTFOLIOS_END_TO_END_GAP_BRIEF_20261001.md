# Tax-Managed SMA on the Model Portfolios page: end-to-end trace brief

Prepared by 4.0.0_SA_CRO on 2026-10-01 (01:16Z to 01:30Z). Read-only assessment plus proposed closure requirements;
no application change, vendor call, deployment or schedule activation by this trace. One read-only SSM command ran on
the Gateway host (checksums and line counts only; command id in the evidence file).

## Design finding

The Model Portfolios page should show a **Tax-Managed SMA** leaf under SMA > ALT Strategies with a dollar amount, and
the 49 Financial and Global totals should include it. The accounts come from Yang's SharePoint workbook (the RIA
column routes each row to a firm; Traded = Yes admits it). Opal reads that sheet through the Gateway under one named
identity, keeps a dated copy, and values each account from the firm's custodian master: Schwab 0833 for 49 Financial,
Black Diamond for Cottonwood. Where the master does not hold the account, the sheet's AUM (Mn) is used and labelled
as such. Opal never estimates a value and never backfills a day it did not observe.

The implementation is complete in source and proven offline on real data (49 Financial: 11 of 11 accounts,
$17,034,745.40 on 2026-09-28). **None of it is deployed.** The work worth keeping is everything from the Gateway
route module through the served fold and the page caption. What is unfinished is purely the connection to the live
plane: one secret, one Gateway release, one backend release, and the activation.

## Current measurement

Read from DEPLOYED bytes at 01:17Z to 01:27Z on 2026-10-01:

- **Gold function `mdpf-gold-lambda`**: downloaded; code digest `5aKNH5WB..` equals the configured digest; last
  modified 2026-09-22; 24 members; 0 files named taxsma; 0 files containing `run_taxsma_prelude`,
  `apply_taxsma_overlay` or `tax_additive_aum`. Environment: `MDPF_GOLD_COMMIT` only. Does NOT match source at
  workspace pin e8994f23af (39 modules, six Tax modules).
- **Publisher `opal-assets-mdpf-portal-publisher`**: downloaded; digest `7X50uR1H..`; last modified 2026-08-29;
  0 files containing `TAXSMA_ROLLOUT_SWITCH`, `taxsma_extend` or `read_taxsma_control`.
- **Gateway host `i-07dccb1615503ac99`**: service active; `app/taxsma_workbook.py` ABSENT; 0 lines naming the route
  in `server.py`; 0 Tax keys in `.env`. Deployed 2026-09-30T18:34Z by another project from a commit this box cannot
  resolve, so the host read is the measurement.
- **Capability secret** `gateway/global/taxsma-workbook-token`: does not exist.
- **Tax storage**: 0 objects under each of the 7 Tax prefixes (workbook Bronze and Silver, both firms' dispositions
  and `taxsma_assets`, the control key).
- **IAM**: the two scoped roles, the Gold role's Tax policy and the publisher's control-read policy EXIST (created
  2026-10-01T00:05Z and 00:17Z).
- **Served documents** (`opal-data-portal-v2/platinum/mdpf/`, written 2026-09-30T13:50Z, as of 2026-09-29): the
  category tree for 49 Financial and Global already carries a member `tax` / "Tax-Managed SMA" with `aum: null`;
  no coverage fields; aum-metrics totals 1,743,965,549.58 (49 Financial) and 2,066,937,285.42 (Global), both
  without Tax.
- **Portal**: branch heads read, not deployed bundles. The accessor and the caption are on origin/DEV (970d5c75) and
  NOT on origin/PROD (ba8e971f). The tree's presence rule (a member renders only when its served amount is above
  zero) is on both.

NOT invoked: the workbook route, Microsoft Graph, either Lambda, the publisher. A created role is not an exercised
role: the four IAM grants are verified by policy simulation only.

Machine-readable evidence: `org/tier1_exec/4.0.0_SA_CRO/deliverables/TAXSMA_MODEL_PORTFOLIOS_END_TO_END_GAP_EVIDENCE_20261001.json`

## Adapter map

| Surface / firm | Provider and intended endpoints | Existing work | Gap |
|---|---|---|---|
| 49 Financial Tax leaf and total | SharePoint workbook via Gateway `GET /ms/taxsma-workbook`; Schwab 0833 Silver (`fact_acc`, `fact_rps_s2`) | route module, snapshot, Silver, membership, reconcile, valuation, served fold, publisher extension, page caption; real offline run 11 of 11 | nothing deployed: no route on the host, no secret, no Tax code in either function |
| Global total | the 49 Financial Tax figure folded into Global | fold proven offline, reconciles to the cent | same as above; rides the same release |
| Cottonwood | workbook rows with RIA Cottonwood; Black Diamond `fact_holdings` | valued offline (2 of 2, $6,041,791.65); role live | Cottonwood's Tax is not added to Global (double-count question open) |

49 Financial working does not certify Cottonwood: different custodian, different role, different bucket.

## Start-to-finish walk

### 1. SharePoint workbook -> Gateway route -- MISSING

What exists: `infra/aws/ec2/opal-gateway/app/taxsma_workbook.py` (sha256 `6acc3e8c..`, contract 0.6.0, nine projected
columns), registered in `app/server.py`, configured by `TAXSMA_WORKBOOK_BEARER` and `TAXSMA_WORKBOOK_IDENTITY` in
`app/config.py`.

The exact mismatch: the host has no such module and no route line; `.env` has no Tax key; `deploy-to-ec2.sh` writes
neither key (0 lines, local and origin) and rewrites `.env` whole on each deploy; the identity
(`opalbloomberg@opalinvest.com`) has never been bound and its access to the sheet is unmeasured.

Close: one narrow Gateway release carrying the module, its route line and two `.env` lines in the deploy script;
proof is the host sha256 equal to source, the route refusing a call with no bearer, and one controlled read under the
bound identity returning `complete: true`.

### 2. Gateway -> Gold function (the capability bearer) -- MISSING

What exists: `taxsma_capability_bearer()` reads the secret named by `TAXSMA_CAPABILITY_SECRET_ID` under the 49
Financial scoped session; `infra/aws/terraform/opal-gateway/taxsma_workbook.tf` (written, uncommitted) declares the
secret and the Gateway role's read; the 49 Financial Tax role already holds the secret read by ARN pattern.

The exact mismatch: the secret does not exist. Its Terraform plan from the shared tree was refused because that tree
was 864 commits behind origin and the plan would have destroyed four live grants of other projects.

Close: apply the two-resource plan once the shared tree carries origin (plan must read exactly 2 to add), then set
the secret's value at activation; proof is the Gateway host and the Tax role each reading it, and another role
refused.

### 3. Gold function -> Tax prelude -- MISSING

What exists: `run_taxsma_prelude` and six Tax modules in the package built at e8994f23af (zip sha256 `ee12387e..`).

The exact mismatch: the deployed bundle has 24 members and no Tax module; the function's environment carries none of
the four values that turn Tax on.

Close: the backend release with Tax off (upload, plan, `safe-apply`); proof is the deployed digest equal to the built
zip and a deployed dry-run invoke recording Tax DISABLED with 16 of 16 objects built. Offline pre-proof done: the
deployed bundle and the new bundle differ only in process-time fields across 16 of 16 output bodies.

### 4. Prelude -> Tax storage under the scoped roles -- INCOMPLETE

What exists: `mdpf-49f-taxsma-role` and `mdpf-cot-taxsma-role` (live), stores for workbook Bronze and Silver, per-firm
dispositions and `taxsma_assets`.

The exact mismatch: no session of either role has run; all 7 prefixes hold 0 objects. Simulation says 30 of 30
grants behave as designed; the first-run read of a missing dispositions object under a prefix-conditioned list grant
is unexercised.

Close: the first enabled Gold run; proof is one object under each prefix and no AccessDenied in the run log.

### 5. Custodian Silver -> membership, reconcile, valuation -- INCOMPLETE

What exists: `taxsma_sources.py` loaders; inputs present (20 September partitions each for 0833 `fact_acc`,
`fact_rps_s2`, 0824 `fact_acc`, Black Diamond Cottonwood `fact_holdings`; latest 2026-09-29).

The exact mismatch: exercised offline only. By rule, an account counts only for valuation dates on or after its
first Gateway observation, so the first enabled run values nothing.

Close: the second scheduled run after activation; proof is a `taxsma_assets` partition marked COMPLETE whose total
equals the sum of its account rows. A one-time ruling from Andrew can make the first run count.

### 6. Tax value -> served fold (timeseries, aum-metrics, category tree) -- INCOMPLETE

What exists: `apply_taxsma_overlay`, the aum-metrics Tax total, the tree's own additive member.

The exact mismatch: built and proven offline (49 Financial 1,761,000,294.98 on all three documents for 2026-09-29);
the served documents carry the Tax member with a null amount and totals without Tax.

Close: rides hop 3's release plus activation; proof is the three served 49 Financial documents agreeing to the cent
and Global's components summing to its total.

### 7. Gold -> publisher -> served keys -- INCOMPLETE

What exists: the publisher's Tax extension behind `TAXSMA_ROLLOUT_SWITCH` (default OFF), its control-read grant
(live), the control writer in Gold.

The exact mismatch: the deployed publisher has no extension; the control object does not exist; the switch is not
set.

Close: the publisher package in the same backend release, the switch turned ON at activation under the never-widen
sign-off; proof is the served category document carrying `taxsma_coverage` and a control stamp.

### 8. Served documents -> portal fetch -> tree leaf -- WORKS

What exists: the page reads `/api/general/mdpf/{firmId}/category-views.json`; the served documents are fresh
(2026-09-30T13:50Z); `CategoryViewTree.tsx` renders a member when its served amount is above zero, on DEV and PROD.

The exact mismatch: none. The Tax member is hidden today only because its amount is null. This is why the page
shows no Tax SMA.

Close: nothing to build; proof is the leaf rendering on the first served non-null amount. Unverified: that PROD's
older reader tolerates the two new document fields.

### 9. Page caption and coverage accessor -- INCOMPLETE

What exists: `getTaxSmaCoverage` and the caption "Total includes Tax-Managed SMA ..." on origin/DEV (370d2fe8).

The exact mismatch: not on origin/PROD.

Close: Andrew's DEV to PROD promotion; proof is the caption under the totals on PROD.

## LGIC

Every address and name below is builder output already used by the code; none is hand-typed.

| Close: line (hop) | Builder call | Output | Registry row needed |
|---|---|---|---|
| 2 | `grade(path, "SECRET")` | `gateway/global/taxsma-workbook-token` CONFORMANT | none |
| 4 | `name("mdpf", firm, "taxsma", "role")` | `mdpf-49f-taxsma-role`, `mdpf-cot-taxsma-role` | none |
| 4 | `address("gateway", "global", tier, "taxsma_workbook", ...)` | `s3://opal-data-assets/gateway/global/{bronze,silver}/taxsma_workbook/...` | none |
| 4 | `address("mdpf", firm, ...)` | `s3://opal-data-{49financial,cottonwood}/mdpf/{firm}/{state/taxsma_membership,gold/taxsma_assets}/...` | none |
| 7 | `address("mdpf", "global", "state", "taxsma_control", "current.json")` | `s3://opal-data-mdpf/mdpf/global/state/taxsma_control/current.json` | none |

## Recommended completion sequence

1. **The live thread.** Andrew, signed in on the DEV portal, opens Model Portfolios for 49 Financial and sees the
   Tax-Managed SMA leaf with a dollar amount and a total that includes it. It crosses every hop above. The first hop
   (workbook to Gateway) is owned by this seat under the FAST lease and needs Andrew's sign-in of the named account.
   Steps, in order:
   a. the shared tree carries origin/CLOUD (`0.0.0_AB_MSTR`, in progress at 01:28Z);
   b. the capability secret and the Gateway role's read (hop 2);
   c. the two `.env` lines in the Gateway deploy script, then the narrow Gateway release (hop 1);
   d. the backend release with Tax off (hops 3 and 7), last check at the 13:50Z publisher run;
   e. activation: the named account signed in at the Gateway, the bearer value set, the identity recorded, one
      controlled read, the four Gold values set, the never-widen sign-off, the switch ON;
   f. the next trading day's scheduled run serves the first value (hop 5), unless Andrew rules the first run counts.
2. The caption on PROD (hop 9).
3. Cottonwood's Tax in Global, once the double-count question is answered.
4. The test and operations cells: expected cases re-cut to 0.6.0, the journey harness, the recovery runbook.

## Acceptance

One reconciled trace per case, from the workbook row through the Gateway response, the valued account, the served
document and the rendered leaf. Cases: 49 Financial and Global; a custodian-measured account and a workbook-stated
account; a complete day, a carried day and the day before first observation; failure cases: the named account's
session expired, the sheet's header changed, a custodian partition missing, the capability bearer wrong.

## Evidence anchors and limits

Source inspected at workspace e8994f23af (shared-tree HEAD c82ad88655, a merge in progress) and portal origin/DEV
970d5c75, origin/PROD ba8e971f. Verified fresh: both functions' deployed bytes, the Gateway host's files, the secret,
the roles, the storage prefixes, the served documents, the portal branch heads. Not verified: the deployed portal
bundles, a signed-in render, any live workbook read, any session of the new roles, PROD's tolerance of the new
document fields. The Gateway parity tool (`infra/aws/ec2/verify-ec2.sh --ssm`) returned a false "in sync" with
zero services checked and is not used here.

- `org/tier1_exec/4.0.0_SA_CRO/deliverables/TAXSMA_MODEL_PORTFOLIOS_END_TO_END_GAP_EVIDENCE_20261001.json`
- `org/missions/D8/MDPF/MDPF_TAXSMA/STATUS.md`
- `org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/4.0.0_SA_CRO/iam-applies.result.md`
- `org/missions/D8/MDPF/MDPF_TAXSMA/surprise-channel/investigations/INVESTIGATION_v1.md` (rows S7, S8, S9)

## Andrew-direct request -- verbatim record

Channel: the 4.0.0_SA_CRO terminal, 2026-10-01 ~01:1xZ.

> /closer trace MDPF_TAXSMA. What remains here?

Earlier the same session:

> i still am not seeing any Tax SMA appear in the Model Portfolios page
