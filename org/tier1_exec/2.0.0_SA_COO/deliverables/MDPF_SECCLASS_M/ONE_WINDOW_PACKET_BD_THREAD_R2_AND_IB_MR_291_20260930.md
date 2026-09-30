# ONE-WINDOW PACKET -- MDPF_SECCLASS BD_THREAD_R2 with IRPT_BCKEND IB-mr-291 (2.0.0_SA_COO~M, 2026-09-30 ~14:3xZ)

For 1.0.0_SA_CTO, per the rounds 2-3 analysis @0a8deabc8e section 2 (row S3) and 103245: "land BD_THREAD_R2 with
IRPT_BCKEND IB-mr-291 in ONE window under one ledger entry; I sign the BD_THREAD_R2 half only on a packet naming
IB-mr-291's commit as its precondition."

## The precondition: IB-mr-291's commit

- Built and proven on `wk-IRPT_BCKEND-93`: `c5f8b8ddd5` (build) and `df71fb818c` (complete; proof VALID rc=0; the
  order's `<status>` complete). Worker report (final message, 14:0xZ): AC1 `SUITE-WHOLE 319 passed`; AC2
  `NARROWED-CENSUS 49financial=6503/1171/120944 inflection=569/9370/34347 cottonwood=1061/3121/15355`
  (moved/fallback/denominator; `to_unclassified` 0 at all three); AC3 `HALF-READY`.
- Drain to CLOUD: `9fef6a7e9c` (filled at the drain; the shared index carried 2.0.0_SA_COO~Y's staged issuance from
  ~13:5xZ, and safe-merge refuses on a foreign staged set).
- Why it is the precondition: `holdings_snapshot.py` at CLOUD 571d032b98..1554e7c8c8 imports the BD library's private
  maps that SC-t-1 removed, so the investor_reporting suite reads SUITE-BROKEN there and a Holdings re-mint from CLOUD
  would fail (row MDPF_SECCLASS-S3, ARMED). IB-mr-291 removes the import (closure: the fallback module plus the one
  client replace the BD library, `.tools/safe_deploy_core.py` `_IRPT_HOLDINGS_CLOSURE`), so after its drain the BD
  thread deploy can change the BD library on the served code prefix without any IRPT consumer reading it.

## The two halves this window executes

1. `NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_R2_20260930.md` (WK~4, SC-e-3): deploy five BD files to `opal-data-bd`
   (gold `lib/etf_classifier.py`, `D_03`, `D_04`, `C_06`; silver `build_bd_assets_dim.py`), the chain's run, the COO's
   live FWD-1 run to the page for z08327149 (VXX structured/Hedge).
2. `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_NARROWED_RELEASE_20260930.md`
   (WK~93, IB-mr-291): the IAM statement `CanonicalClassifierLookup` (GetItem/Query on `etf-classifications` and its two
   GSIs for each firm's Holdings principal), the re-mint of the three Holdings bundles from the drained CLOUD, the QA
   fire, then the served publication.

## Corrections the packet makes to the halves (measured today, not predicted)

- **BD_THREAD_R2 step 2 (IAM) is ALREADY SATISFIED live and is NOT applied as written.** The half measured
  `bd-pipeline/iam.tf` alone and read "no DynamoDB statement on `bd-exporter-ec2-role`". Live read 14:3xZ
  (`list-attached-role-policies` + `get-policy-version`): the role carries the managed policy `bd-securities-access`
  (shared-infra `aws_iam_policy.bd_securities_access`) granting Scan/GetItem/PutItem/UpdateItem/BatchWriteItem on
  BOTH `bd-securities` and `etf-classifications`. GetItem on `etf-classifications` exists today. Adding the half's
  candidate `etf-classifications-read` inline policy would be a second, redundant grant; the surviving least-privilege
  read grant is decided by SC-e-12 (W6-S2, the shared-infra narrowing, AE lane, parked). So step 2 is a READ, not an
  apply: the ledger leg records the live grant and its source.
- **HOLDINGS_NARROWED: the fallback module is not byte-for-byte the pre-SC-t-1 library at two lines.** Row
  IRPT_BCKEND-W93-S2: the LGIC naming limb refused the hand-typed `'bd-securities'` defaults
  (`bd_securities_fallback.py:72`, `:77`) and the served label `"bd-securities-fallback"`
  (`holdings_snapshot.py:834`); they are now read from the naming registry (the 49financial scope's `serving-route`
  alias) and resolve to the identical strings. Logic, basis order, mirror refusal and the cash rule are unchanged; the
  whole suite (319) and the census were re-measured after the change and are identical.
- **A canonical hit is served with basis `TABLE`, not `CANONICAL`** (row IRPT_BCKEND-W93-S1): the published contract
  is `additionalProperties:false` with no `CANONICAL` enum member, and the contract file is outside the cell's grant.
  The class source is tracked in the producer's census only. Widening the contract is a PRD addendum if the CTO wants
  the source on the wire.

## The ONE ledger entry: `secclass-bd-thread-r2-and-irpt-narrowed-m-20260930` (opened at the first act, window 24 h)

Order inside the window (IRPT first, because its re-mint is what removes the BD-library dependency from the served
bundles; then BD):

| leg | kind | act | proof required |
|---|---|---|---|
| H1 | verify | `terraform plan` on `infra/aws/terraform/investor-reporting/directory` from the drained CLOUD | in-place policy updates for the Holdings principals only (the new statement), 0 add, 0 destroy; every changed resource named |
| H2 | activation | `safe-apply` that root (HALT_ACK) | apply rc 0; re-plan 0-diff; per-firm `get-role-policy` read-back names Sid `CanonicalClassifierLookup` |
| H3 | s3-prefix x3 | `safe-deploy --mint-bundle irpt_holdings_{49f,inf,cot}` from CLOUD `9fef6a7e9c` | BUNDLE MINTED lines + head-object members-sha256 + member-count (the closure now carries `bd_securities_fallback.py` + `etf_classifications_dynamodb.py`, not the BD library) |
| H4 | verify | QA fire `irpt-holdings-refresh-lambda {"qa": true}` | 3 of 3 Success; `holdings_qa` read per firm: PHYS/GLD commodities/Metals, VXX structured/Hedge, `to_unclassified` 0 against the census; served `holdings/current/manifest.json` VersionId unchanged at all three firms |
| H5 | verify | the served Holdings publication (the next scheduled fire; an ad-hoc served publication only under the halves' own word) | served manifest advances at each firm; PHYS reads commodities/Metals on the Investor Reporting Holdings page (Andrew's ~05:0xZ complaint), read on the page |
| B1 | s3-prefix x5 | `safe-deploy` the five BD files to `opal-data-bd/code/{gold,silver}` | DEPLOYED + VERIFY OK per file (SHA), bytes = CLOUD `9fef6a7e9c` (unchanged since @ae7aa281b0 for these five) |
| B2 | verify | the live IAM read for `bd-exporter-ec2-role` | `bd-securities-access` attached; GetItem on `etf-classifications` present (the read above); NO new inline policy added |
| B3 | activation | the BD chain's run: the ordinary gold-layer trigger, ad-hoc QA fire permitted as the exercise, the scheduled fire the acceptance | `build_bd_assets_dim` then `C_06 --upload`, `D_03 --upload`, `D_04`; served `gold/views/firm_composition.json` and `platinum/clients/z08327149/summary.json` advance; new VersionIds recorded beside the prior ones the half names |
| B4 | verify | the COO's one live FWD-1 run to the page | for z08327149, VXX reads structured/Hedge and GLD/PHYS commodities/Metals on the real page; `class_source` in the census reads `etf-classifications`; `bd_securities_reads` 0 |

**Blast radius:** exactly the union of the two halves' named keys (Holdings gold/platinum artifacts at the three IRPT
firms; BD `gold/views/*`, `gold/advisors/*`, `gold/entities/clients/*`, `platinum/accounts/*`, `platinum/clients/*`,
`platinum/firm/mix_summary.json`, `gold/client_timeseries/*`, `silver/bd_assets_dim.parquet`). Both branches are the
halves' own. **Rollback per key:** as each half states (S3 prior VersionId per key; code by revert + re-deploy of the
prior bytes; the Holdings IAM statement by re-apply without it; no IAM change on the BD side to roll back).

**Writers counted:** Holdings `asset_class_basis` 1 (holdings_snapshot.py); BD served classes 3 scripts + 1 library,
all in this window; `etf-classifications` is READ only by every act here (no table write in this window).

## What the CTO is asked

One decision: sign the BD_THREAD_R2 CTO half on this packet (the COO half is appended to that file). The HOLDINGS_NARROWED
half carries CTO 103169's four conditions; its COO half is appended after the drain lands the file on CLOUD, and the CTO
half is asked in the same message. Nothing in this window runs before both CTO halves are at HEAD.
