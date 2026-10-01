# MDPF_SECCLASS -- round 6 remediations

<sweep_watermark>2026-09-30T23:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-01. Graduated at round 6's L9 (ADJUDICATION_v4.md): 10 rows. Closed at this compile on this seat's own reads: W10-S1, W10-S5, W12-S1. S4 is closed IN PLACE in REMEDIATION_v3.md, clocks only. Carried unchanged: W6-S2 (REMEDIATION_v2, ARMED), W5-S2 (REMEDIATION_v2, OPEN), S2 (REMEDIATION_v1, OPEN). Rounds read v7: the project is FAST since 2026-10-01T05:39Z and its round-7 list is built directly (STATUS.md).

```json
[
  {
    "id": "MDPF_SECCLASS-S5",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The BD thread library reached the shared classifier client through a repo-relative hop; the gold runner executes a flat copy of code/gold/ with no infra/ tree, so C_06 crashed at import on the runner (2026-09-30 17:47Z) and the five code objects were rolled back. Every in-repo test had passed because the repo tree supplies the ancestors the runner lacks.",
    "evidence": [
      "investigation row MDPF_SECCLASS-S5 (2.0.0_SA_COO~M): the runner log line, the rollback at 18:16:09Z, served keys unchanged 0 of 4",
      "r6_deployed_layout_import.py at CLOUD HEAD (this seat, 06:3xZ): DEPLOYED-LAYOUT-IMPORT modules=5 of 5 files=8, each module resolving the client from <extract>/lib/_shared, sys.path entries inside the repo = 0",
      "comp-pipescript deployed --firm bd (this seat, 06:2xZ): C_06, D_03, D_04 and build_bd_assets_dim.py read MATCH; 41 MATCH, 0 STALE, 0 MISSING; the report's overall state NOT-DECIDABLE (1 head-object deferred)",
      "s3api head-object, three keys under opal-data-bd code/gold/lib/_shared/ (this seat): present, LastModified 06:11:37Z to 06:11:46Z, ETag of etf_classifications_dynamodb.py 181e1902667beb928a9ea993bd17d349; absent-key control 404",
      "ledger secclass-bd-thread-r3-m-20261001: legs P, S1, L0 CLOSED 06:16Z; legs X, A1, A2, B4 OPEN",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "The fix-forward is built (SC-e-13) and its bytes are on the code prefix. It is REMEDIATED only when ledger leg X reads C_06, D_03 and D_04 rc=0 on the real runner with no IndexError and no BLOCKED line: the first failure was exactly a pass everywhere except the runner.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": "2026-09-30T18:16Z"
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W10-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The silver runner's bootstrap document staged the gold lib with no copy of code/gold/lib/_shared/*, so build_bd_assets_dim.py would refuse on its runner once the gold redeploy made the library depend on the shared client.",
    "evidence": [
      "aws ssm describe-document --name opal-bd-asset-dim-download (this seat, 06:2xZ): DefaultVersion 5, LatestVersion 5, Hash d3a38c7b1a92b3d92030c241ab6502245c5a25d3b40930dcef67548943d3f407, equal to sha256 of git show HEAD:infra/aws/ssm/opal-bd-asset-dim-download.json; get-document at $LATEST carries 5 lines naming _shared",
      "s3api head-object: the three _shared keys the document copies exist (06:11:37Z to 06:11:46Z), absent-key control 404",
      "r6_deployed_layout_import.py at HEAD: SILVER-LAYOUT-AS-STAGED-TODAY files_staged=10, document keys with no repo source 0",
      "investigation rows MDPF_SECCLASS-W10-S1 and -W10-S4 (0.9.0_WK_MDPF_SECCLASS~10)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Done: the document stages the three shared modules and the keys exist. The served acceptance is ledger leg A2 (the first 22:10Z silver fire advances bd_assets_dim.parquet); that leg is graded at the ledger close, not on this row.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": "2026-10-01T06:15Z"
    },
    "closed": true
  },
  {
    "id": "MDPF_SECCLASS-W10-S5",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The silver trigger reads the SSM document at $LATEST, so a document published before its three new copy sources exist fails the next 22:10Z fire at the first missing key, before shutdown is armed, and strands the runner; and restoring the default version does not roll a $LATEST reader back.",
    "evidence": [
      "infra/aws/lambda/bd-pipeline/bd-asset-dim-trigger/lambda_function.py:58 at HEAD: DocumentVersion='$LATEST' (this seat's read; the live Lambda bytes were not read)",
      "order of the act, from this seat's own reads: the three _shared keys LastModified 06:11:37Z to 06:11:46Z; document version 5 created 06:14:59Z; so the sources existed before the document changed, and the next silver fire is 22:10Z",
      "ledger secclass-bd-thread-r3-m-20261001 leg L0: 'After S1 completed (order: step 1 first, CTO condition 1)'",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Done for this act: sources first, then the document, in one gap. The rollback form (republish the version-4 bytes as a new $LATEST, not restore-default alone) stays in the signed half. The same reading applies to four sibling triggers; see the review, Q1.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": "2026-10-01T06:15Z"
    },
    "closed": true
  },
  {
    "id": "MDPF_SECCLASS-W10-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "gold_dispatch.sh carries no E_ id in its catalog or chains, so no scheduled fire runs E_18.detect_new_securities.py. FWD-7's 'first scheduled fire' and the open ledger secclass-e18-iam-and-deploy-m-20260930's acceptance have no event that can produce them.",
    "evidence": [
      "data/black_diamond/scripts/gold/gold_dispatch.sh at HEAD (this seat): 0 lines matching E_<digits>; control, 57 lines matching C_<digits>",
      "org/critical_paths/.open_deploys/secclass-e18-iam-and-deploy-m-20260930.json present (an open entry whose acceptance cannot fire)",
      "investigation row MDPF_SECCLASS-W10-S2 (0.9.0_WK_MDPF_SECCLASS~10)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "P1: E_18 gains a scheduled trigger (a catalog entry and a chain position in gold_dispatch.sh, under both halves: it is a deploy), and the E18 ledger's acceptance is re-worded to that fire. STATUS.md next-list item 4 holds it; the lease surface names both files.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W10-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": ".tools/test_safe_deploy.py fails 7 of 14 at CLOUD HEAD, before and after SC-e-13's edit of .tools/safe_deploy_core.py, so the deploy tool's own test file is not a regression guard for a change to it.",
    "evidence": [
      "python -m pytest .tools/test_safe_deploy.py at CLOUD HEAD (this seat, 06:3xZ): 7 failed, 7 passed",
      "investigation row MDPF_SECCLASS-W10-S3 (0.9.0_WK_MDPF_SECCLASS~10): the same count against HEAD's unmodified tool",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "P2: the owner of .tools/safe_deploy_core.py repairs or retires the seven failing cases (four INDEX_MISSING, three 'Strings must be encoded before hashing'). Outside this project's paths; placement is the CTO's.",
    "owner": "1.0.0_SA_CTO",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W11-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Issuer amendment 1 of TO-SC-e14 repaired the four condition-string assertions and turned the two contract assertions into a version floor (at or past 0.2.0) and a superset check, where the order said no assertion is weakened. The contract reads 0.3.0; a regression to 0.2.0 or a removed fifth value would pass both tests.",
    "evidence": [
      "infra/aws/lambda/v2_portal/_shared/tests/test_classified_by_v2.py:57-70 at HEAD (this seat): test_contract_version_is_at_or_past_0_2_0 asserts version >= (0, 2, 0); the values test asserts the original four are a subset",
      "org/standards/MDPF_SECCLASS_CONTRACT.json at HEAD: contract_version 0.3.0",
      "the two v2_portal test directories in one process at HEAD (this seat): 1 failed, 93 passed (the one failure is row W11-S2's)",
      "drain-end packet DRAIN_END_R6_20260930.md @2744a9fc57, deviation 1",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "P2: pin the contract version and the five classified_by values exactly, read from the contract file at the commit that changes them. STATUS.md next-list item 6.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W11-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "test_seed_etf_constituents.py::test_positioning_universe_plan_unchanged fails on CLOUD's unmodified script: the test expects batched writes and the script writes conditional puts. The guard that the positioning-universe plan is unchanged is red, so a real change to that plan would not be seen.",
    "evidence": [
      "python -m pytest infra/aws/lambda/v2_portal/yang_pipeline/tests/test_seed_etf_constituents.py at CLOUD HEAD (this seat, 06:3xZ): 1 failed, 7 passed, the named test",
      "git log -- seed-etf-constituents.py: ebf23aa8fe (0.9.0_WK_MDPF_SECCLASS~5, TO-SC-e2, the instrument_kind-only conditional update) and 63fa135384 (the site-Z union merge) are the two changes before the failure was first recorded; which one turned the test red was not bisected",
      "investigation row MDPF_SECCLASS-W11-S2 (0.9.0_WK_MDPF_SECCLASS~11)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "P2: the issuer names which behaviour is intended (conditional puts or batched writes) and the test is brought to it; the script is this project's own (SC-e-2 changed it).",
    "owner": "2.0.0_SA_COO~M",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W12-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "seed-etf-classifications.py merge_item() carried classification_confidence and low_confidence onto a row it rewrote as classified_by = seed, against contract 0.3.0 (a seed correction drops both).",
    "evidence": [
      "commit 9053ffba73 (2.0.0_SA_COO~M, FAST, 2026-10-01T05:52Z), an ancestor of CLOUD HEAD",
      "MDPF_SECCLASS_M/R7_CHECKS/test_seed_model_correction.py at HEAD (this seat, 06:3xZ): 4 passed",
      "r6_model_reader_census.py at HEAD (this seat): MODEL-READER-CENSUS readers=34 tolerates=23 read_only=8 crashes=3 refuses=0 fails_contract=0 (the packet's census read fails_contract=1)",
      "investigation row MDPF_SECCLASS-W12-S1 (0.9.0_WK_MDPF_SECCLASS~12): 0 model rows live and 0 overlap with the seed source, so no live row carried the defect",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "Done: merge_item drops the two model-only fields on a seed correction. The script runs from the repo, so HEAD's bytes are the running bytes.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": "2026-10-01T05:52Z"
    },
    "closed": true
  },
  {
    "id": "MDPF_SECCLASS-W12-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "ETFClassifier.classify_holdings raises KeyError on an asset_class outside fixed_income / equity / hedge / unknown, in the client and its two byte-identical Lambda copies; it has no caller, and it crashes the same way on 17 rows already live. The MODEL_ROWS half refuses its act while the reader census prints a crash.",
    "evidence": [
      "r6_model_reader_census.py at HEAD (this seat, 06:3xZ): 3 READER CRASHES lines, the client and the two positioning copies; crashes=3",
      "NEVER_WIDEN_HALF_REQUEST_SECCLASS_MODEL_ROWS_20260930.md:201: the act is refused unless a fresh census prints MODEL-READER-TOLERATED",
      "investigation row MDPF_SECCLASS-W12-S2 (0.9.0_WK_MDPF_SECCLASS~12)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "P1: seed the result from the ratified class list in all three copies (a Lambda bundle change, so a deploy act), or the CTO rules that a zero-caller method is not a reader and the method is removed. After BD_THREAD_R3 closes: the client's bytes are inside that act's signed candidate. STATUS.md next-list item 2.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W12-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The reader census covers the tracked tree at its pin. The bound has now been met: at CLOUD HEAD the census prints UNCENSUSED for a file that arrived after the cut, and IRPT_BCKEND landed a new reader of etf-classifications (the comparison catalogue's classifications_reader) that the census set does not name.",
    "evidence": [
      "r6_model_reader_census.py at HEAD (this seat, 06:3xZ): 'UNCENSUSED infra/aws/lambda/investor-reporting/reports/generate_installed.py'",
      "IRPT_BCKEND commits 0ad0e6867d and efde229443 (2.0.0_SA_COO~Y, 2026-10-01): comparison_catalogue.py gains a paginated Scan of etf-classifications projecting ticker, name and identifier_namespace; wired by 4f43b48050 (source only)",
      "investigation row MDPF_SECCLASS-W12-S3 (0.9.0_WK_MDPF_SECCLASS~12)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md (co-committed)"
    ],
    "remedy": "P1: the fresh census before the MODEL_ROWS act classifies every UNCENSUSED file and the catalogue reader, on the integrated tree. STATUS.md next-list item 3.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v7"
    },
    "closed": false
  }
]
```
