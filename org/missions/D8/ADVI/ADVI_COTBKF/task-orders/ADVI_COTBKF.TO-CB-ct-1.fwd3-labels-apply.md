# TO ADVI_COTBKF.TO-CB-ct-1.fwd3-labels-apply -- round 98 CB-ct-1: apply the relabelled FWD-3 tables to the three served keys under the signed never-widen pair, verify, and close the ledger

<to_id>ADVI_COTBKF.TO-CB-ct-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.7.0_AE_CloudOps~CB1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>98</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-ct-1` (`decompositions/ADVI_COTBKF_DECOMP.round98.md`) |
**outcome_ref:** FWD-3 | **depends_on:** the signed pair (both halves)

---

## WORKER FACE

### THE CELL

The three served FWD-3 tables of ADVI_COTBKF live at three keys. They are to gain two appended label columns, `use_class` and `porting_verdict`, with no pre-existing value moved:

`s3://opal-data-assets/commonwealth/cottonwood/silver/{daily_returns,account_day_value,month_grades}/date=2026-06-23/part-00000.parquet`

You apply the issuer's local build, AS BUILT, under a signed never-widen pair. There are no served readers (the gateway catalog entities carry `read_tool: null`), and the reader gate stays closed: you grant nothing.

**Read first (the pair; both exist and are signed):**
1. COO half: `org/missions/D8/ADVI/ADVI_COTBKF/ledger/NEVER_WIDEN_R97_FWD3_LABELS_COO_HALF.md` GIVEN @814c6cc826.
2. CTO half: `org/missions/D8/ADVI/ADVI_COTBKF/ledger/NEVER_WIDEN_R97_FWD3_LABELS_CTO_HALF.md` SIGNED @eceab5b4b0 (CTO msg 6563). Read its conditions; they bind you as the COO half's section 5 does.

**The build to apply (READ-ONLY input; absolute paths; off git, gitignored):** `C:/Dev/ajb_workspace/.scratch/cotbkf_r97/build/` (three tables and `fwd3_manifest.json`), made at `run_commit=14793ce1882921b8da023c99e9512879d0d451c1` from the regrade at `C:/Dev/ajb_workspace/.scratch/cotbkf_r97/regrade`. **Do NOT run `--build`.** The builder script is `data/assets/scripts/silver/commonwealth_fwd3_serve.py` at the current trunk (the run_commit above names the code that made the build; you run only `--dry-run`, `--apply` and `--verify`, which read the build as it is).

**Your items, in this order. Stop at the first that fails and restore nothing you have not yet written.**

0. **Step 0 -- your own open round-88 deploy, before any round-97 act (CTO msg 6567).** The worktree `C:/dev/wk-cb1-r88` holds an OPEN deploy-ledger commit by `0.7.0_AE_CloudOps~CB1` (slug `advi-cotbkf-r88-crm-match-grant`, 2026-10-15 ~15:26Z) and a dirty `infra/logic/registry/exemptions.json`. (a) Measure the round-88 artifact per NEVER-2: read the world (the CRM role the entry created and later removed on 2026-10-15, and the cottonwood bucket policy) with read-only IAM/S3 gets; the CTO's own read found the role gone and the policy clean. If the world reads done, close the entry SUPERSEDED with `deploy_ledger.py` and never re-execute the round-88 act; if it does not read done, STOP and report before any round-97 act. (b) Name the `exemptions.json` edit (file, line count, which exemption: no value that names a client) in the ledger, and revert it in that worktree (`git -C C:/dev/wk-cb1-r88 restore infra/logic/registry/exemptions.json`, no commit) unless an order of the round-88 project covers it. Record both in your report. This step touches no served key.

1. **Before any write.** The pair is signed (items 1 and 2 above; confirm the COO half's sha256 begins `4ab6b4b15433758c` with `git show 814c6cc826:<path> | sha256sum`). Open the change-management ledger entry with `deploy_ledger.py open` (it commits its own files). Record the blast radius: exactly the three keys, overwritten; the rollback per key is the prior VersionId in the COO half's section 1.
2. **Re-read the three prior versions immediately before the first put** (head-object on each key) and STOP if any differs from the COO half's section 1: `daily_returns` `w9j5YeV1LnNIakNlRTBX6jW1.SDHqmJR` (ETag `26ad8293e2ba2e561dbde60b1aa7eb95`, 1,651,055 bytes); `account_day_value` `qIWjLLwCIh_Gx6IblSgyaint2tfJ37pr` (ETag `ca1ac0f48971f6cc0d11a147dcda086e-7`, 54,246,028 bytes); `month_grades` `QI5Ks8vQwGTwnc9ekyh.DOsyN8PKN3PB` (ETag `7269e2607b1e5806058b1136b8c4e36b`, 421,751 bytes). Record ETag and VersionId per key in the ledger.
3. **Dry run.** `python data/assets/scripts/silver/commonwealth_fwd3_serve.py --dry-run --data-dir C:/Dev/ajb_workspace/.scratch/cotbkf_r97/regrade --out C:/Dev/ajb_workspace/.scratch/cotbkf_r97/build`. The three addresses (from the builder), row counts and content hashes it prints MUST equal the COO half's section 3: `daily_returns` 1,691,729 rows `b558693deb2975198b36c1a23a5905f7eb9b19daf2a387a6924276bf1508427c`; `account_day_value` 21,102,041 rows `7792443dc3e61d6f0766e7eda4af83a78a89b2e849ad888f09b7a48949e4199b`; `month_grades` 82,593 rows `eca458ac82800c658d9ebcf8c986362cc53652a4924997b3d6e019c547e1aa0a`; it must also print `absent_months=5`. Otherwise STOP and report; write nothing.
4. **Apply.** `python data/assets/scripts/silver/commonwealth_fwd3_serve.py --apply --overwrite --data-dir C:/Dev/ajb_workspace/.scratch/cotbkf_r97/regrade --out C:/Dev/ajb_workspace/.scratch/cotbkf_r97/build`, printing the hashes. Then `--verify` (acceptance AC1). Never `--yahoo-active-policy blank` (the builder refuses it under `--apply`).
5. **Read back and close.** Record the new ETag and VersionId per key; run AC2; close the ledger with the read-back. If any criterion fails after a write, restore each key to its recorded prior VersionId (`s3api copy-object --copy-source opal-data-assets/<key>?versionId=<prior>`), read the three objects back against the prior size and ETag, write the reason in the ledger and file a surprise row.

### ACCEPTANCE

<criterion id="CB98ct1-AC1" cell_refs="CB-ct-1"><invocation>python data/assets/scripts/silver/commonwealth_fwd3_serve.py --verify --out C:/Dev/ajb_workspace/.scratch/cotbkf_r97/build</invocation><expect>FWD3-VERIFY tables=3 match=True</expect></criterion>
`CB98ct1-AC1` -- the three served tables read back equal (row counts and content hashes) to the applied local build.

<criterion id="CB98ct1-AC2" cell_refs="CB-ct-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/ct1_ac2_versions_check.py</invocation><expect>^SERVED-WRITE keys=3 moved=3 prior_readable=3 sizes_grew=3$</expect></criterion>
`CB98ct1-AC2` -- each of the three keys moved to a new version, each prior version is still readable (the rollback exists), and each object grew (two columns appended). The issuer's script reads object metadata only; read it, do not edit it.

<expected_criteria>CB98ct1-AC1,CB98ct1-AC2</expected_criteria>

## BOUNDS

- **Grant.** S3: exactly the three keys above (put, overwrite) and head/get of them and of their prior versions; no other write. Repo: the ledger files for this deploy, the surprise channel row, and this order's file.
- **Pair first.** No served write before items 0 to 3 pass. Read-only IAM and S3 gets are allowed for step 0.
- **No account number, name or dollar value** in a ledger entry, a record, a row or a message: counts, hashes, VersionIds and ETags only. The build directory holds per-account values: read it only through the builder and never copy it.
- **NEVER** `--build`, `blank` policy, a delete of any object or version, a grant, a push, or a change to any module.
- **Refusal clause.** If a criterion cannot be met as written, stop. Restore each written key to its recorded prior version, write the reason in the ledger, and file a NEW surprise row (id `ADVI_COTBKF-D1-WCB1-S<k>`, `"fabric": "dell1"`). Do not weaken the test.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your repo WRITE grant. The S3 grant is the three keys above.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round98.md</decomp_doc> (round 98), cell `CB-ct-1`.
<owned_cells>CB-ct-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB98ct1-AC1, CB98ct1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB1/ADVI_COTBKF.TO-CB-ct-1.fwd3-labels-apply.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB98ct1-AC1,CB98ct1-AC2` BEFORE the flip. Both are mechanical.
</proof_of_spec>

**REPORT:** the pair files and the COO half's hash read; the prior versions (ETag and VersionId per key); the ledger entry; the dry-run hash lines; the apply and verify lines; the new ETags and VersionIds; the two criterion lines; every refusal and denial verbatim. No account number or value.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time overwrite of three keys; no schedule is created or changed.
comp-iam: RUN at apply time -- the dell1 identity's write on the three keys under opal-data-assets and read of their versions; BLIND: none beyond the three keys.
comp-adversary: RUN -- pair before write; prior versions re-read and recorded for rollback; dry-run addresses, rows and hashes equal to the pair's; read-back equality (AC1) and version movement (AC2); BLIND: a downstream reader outside the gateway catalog (the catalog carries none; the reader gate stays closed), and the build directory is checked by the dry-run hash read only.
lane: SERVED write by the box applier; the issuer signed the COO half on CB-cs-1's build; the CTO signed his.
</preflight>

**ISSUER NOTES:** Source: CTO msg 6563 (CTO half signed, applier named; seat registration asked of `0.0.0_AB_MSTR~DELL1`). Mechanical checks dry-run at the base: AC1 reads the served tables, which differ from the local build before the write (`match=False`, FAIL as expected); AC2 reads `moved=0` (FAIL as expected).
