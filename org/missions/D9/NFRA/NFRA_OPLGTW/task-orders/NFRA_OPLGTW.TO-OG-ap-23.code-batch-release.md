# NFRA_OPLGTW task order -- `OG-ap-23` -- APPLY: the code batch release -- the client tools, rival tools, silver etfs tools, the json-served family and the breakdown handlers, one deploy (FWD-22; PRD v3.12, v3.13)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-23</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-23</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; the applier still runs `comp-schedule --drift` at the act and records what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- this release changes NO IAM. The six vendor read roles are live from `OG-ap-24` (complete, `dcc3ac9174`); the json-served family reads `opal-data-portal-v2/json/*`, which the gateway role already holds (`infra/aws/terraform/opal-gateway/queryv0-iam.tf` line 34); the rival tools read the prefixes `OG-ap-20` granted. The applier re-reads each in Phase A.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is decomposition addenda R3-T.70 to R3-T.78 (PRD v3.7, v3.12, v3.13; CTO msgs 34552, 34690, 34699) and the CRO's G2/G3/G5 specs.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-23` (decomposition addendum R3-T.73, workstream CODE-BATCH, FWD-22)

APPLY: ONE release carrying every ready code cell of the gateway, on the live ref `OG-ap-21`/MX-r-12.. left (read it, do not assume it). It SUPERSEDES `OG-ap-22` (the rival tools ride here). Opal principals only on the Opal tools; each client tool admits and fences by firm before any read. The builds are merged to trunk (`box/sitez`): `OG-rv-1/2` (rival tools), `OG-cl-1..8` (the client core and the seven vendor adapters, firm names through `lookup()`), `OG-ch-1` (several adapters per vendor), `OG-gp-1` (`mdpf_get_model_composition`), `OG-gf-1` (three etfs silver tools), `OG-sv-1/2` (the json-served family), the issuer hookups (registrations, pins, roster copy), MCPINDEX's `etfs_get_positioning` extension (`a183b3cf85`, MX-c-22) and MC Portal's gateway-breakdown handlers (`8310672247`, `3317942ecc`, `54a75d46ba`). The GO message names `trunk_sha`, the one trunk commit you take from. The code is CODE ONLY: no Terraform, no apply, one deploy.

### PHASE A (only on the issuer's GO message, which names `trunk_sha`): re-cut, ask. NO deploy, NO apply IN ANY FORM

1. **Live ref.** Read `services.opal-gateway.deployed_commit` at HEAD and one SSM md5 read of the host against it over `app/`, `deploy/`, `dashboard/` and `lib/`. A mismatch is a STOP and a BLOCKING row. Re-read (IAM `get-role-policy`) the internal reader role's etfs/rivalfunds read grant and `gw_queryv0_portal_read` (`json/*`), and `get-role` for the six vendor read roles (`gateway-49f-blackdiamond-read-role`, `gateway-cot-blackdiamond-read-role`, `gateway-inf-orion-read-role`, `gateway-inf-eclipse-read-role`, `gateway-cot-commonwealth-read-role`, `gateway-smartx-read-role`); a missing one is a STOP.
2. **Re-cut** in `C:/tmp/og-rel-code`, branch `rel-nfra-oplgtw-code`, at the live ref, with `infra/logic/`, `org/missions/DIRECTIVES.yaml` AND `org/mcp/naming-gate.enforce` in the cone (the CTO's standing condition). **First enumerate the seams**: every app module the taken files import; print each as in-base or in-take-list; a missing seam is a STOP and a row. Files that differ between the live ref and `trunk_sha` and are NOT named below (for example `family_depth.py`, `refs/silver_families.json`, the yearinreview files, `admin_people_access.py`) are NOT part of this release; if a taken file imports one, that is a missing seam: STOP.
   Take WHOLE from `trunk_sha` (`git show <trunk_sha>:<path>`): the nine client modules `app/client_core.py`, `app/client_role.py`, `app/client_adapter_{schwab,bd49f,orion,eclipse,bdcottonwood,smartx,commonwealth}.py`; `app/etfs_rivals.py`, `app/etfs_rivals_flow.py`, `app/etfs_silver.py`, `app/portal_served.py`, `app/portal_json_served.py`; `app/admin_gateway_breakdown.py`, `app/admin_people.py`; `app/refs/partner_roster.json`; `lib/opal_naming.py`; every `tests/test_og_*.py` file of the cells above that exists at `trunk_sha` (`test_og_cl1..8`, `rv1`, `rv2`, `ch1`, `gp1`, `gf1`, `sv1`, `sv2`), `tests/test_admin_gateway_breakdown.py`, `tests/test_admin_people.py`, `tests/test_positioning_extension.py`. Write `app/refs/scopes.json` as a byte-equal copy of `infra/logic/registry/scopes.json` at `trunk_sha`.
   THE MCPORTAL BUNDLE (CTO round-2 ruling 2(b), `ROUND_ANALYSIS.pf-round2.md`; `NFRA_MCPORTAL` msg 34718): the release's `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway.mcportal_commit` is set to `mcportal_sha` named in the GO (the origin mcportal DEV commit `090b9cdc85ce3463e73915e68b44f4c21053a71c`, nine commits past the live `17dcbb28624eab147318052f58bcc39b8eb8029c`, descended from `421f8fbe8446650881a178fbac82a6432bb5d6ca`), and NOTHING else in the manifest changes in the release commit (`deployed_commit` and the checksums are written at the close). The deploy script bundles the dashboard from that manifest field. Verify with `git -C mcportal cat-file -e <mcportal_sha>` and `git -C mcportal merge-base --is-ancestor 421f8fbe8446650881a178fbac82a6432bb5d6ca <mcportal_sha>`; a failure is a STOP. Record `mcportal_sha` in `W/ap23_release.json`.
   Take BY HUNK (3-way against the base; never a whole file from trunk): `app/tools.py` (the import lines, every `@mcp.tool()` registration of the tools `trunk_sha` adds beyond the base, the re-pinned counts), `app/destructive_ops.py` and `app/data_entitlement.py` (the added names and pins), `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py` (pins re-derived against the base you cut on, plus the added tools), `app/integrations/portal_index/integration.py` (the MX-c-22 hunk of `a183b3cf85` only), and `deploy-to-ec2.sh` (ONE hunk: stage `lib/opal_naming.py` beside `lib/trading_calendar.py` where the script copies the calendar, around its line 271; nothing else). Nothing else.
   Commit with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the release commit only; the naming gate runs in ENFORCE on it (sentinel present) and must print NO REFUSE (the registry rows `OG-cl-8` and the issuer's hookup landed are in `infra/logic/registry/name_rulings.json` at `trunk_sha`; if the gate still refuses a string, STOP and file a BLOCKING row naming the (name, type)). Write `W/ap23_release.json` = `{"base_sha", "release_sha", "trunk_sha", "mcportal_sha"}` (FULL 40-character shas).
   Run in the release tree: every taken test file, the pinned-count tests, and the host-shaped import check (a 4-parent path with `lib/trading_calendar.py` AND `lib/opal_naming.py` beside it, `app/refs/scopes.json` present: every taken module and `app.tools` import in a fresh interpreter, and the client tools resolve their firms; then the same path WITHOUT `lib/opal_naming.py`: the client modules still import and answer `registry_unavailable` with zero reads).
3. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-23.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word: (1) the `diff` by file, including the one manifest field `mcportal_commit` (live `17dcbb286` to `mcportal_sha`, nine mcportal commits); (2) the `tools`: every tool added, its class (READ), its firm fence and its `refused` arm; (3) the `widening`, stated plainly: NO new IAM; the client tools turn the six live vendor read roles from unused to used, each through an assumed role scoped to its vendor and firm prefixes, and the gateway can now return client account-level data (holdings, transactions, fees, allocation) to named Opal principals; say which tool uses which role and fence; (4) the `order` of acts (one deploy, then the two CVO conditions); (5) `both branches` (refused: zero reads; admitted: capped, projected, fenced by firm); (6) the `rollback` (redeploy the base); (7) the `triggers`; (8) the CVO's two conditions from `OG-ap-24` (C1: one REAL AssumeRole of a vendor read role by the gateway role, because simulate cannot see a trust; C2: SmartX counts as firm-safe only after the two-firm negative arm) and where in Phase B each is met. Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

4. Ledger `nfra-oplgtw-gateway-release-code`, entry AND sentinel first. Deploy from `C:/tmp/og-rel-code` through `infra/aws/ec2/safe-ec2-deploy.sh` with `DEPLOY_BASE_REF=<base_sha>` under the A1 guard (HEAD = full `release_sha`, parent = live `deployed_commit`; no other release in flight). No `HALT_OVERRIDE`. Read back against the triggers; on any trigger redeploy the base and file an ARMED row naming `2.0.0_SA_COO~O`.
5. **The served read**, through the INSTALLED code on the host and the public endpoint (60 s ALB), writing `W/CODE_SERVED.json` = `{"body": {"registry_before": N, "registry_count": N+K, "per_tool": {"<tool>": {"opal_served": true, "non_opal_refused": true, "reads_on_refusal": 0}, ...}, "assume_role_real": true, "smartx_two_firm_arm": true}}` where K is the number of tools `trunk_sha` adds beyond the base (AC2 recomputes it). For every added tool: an Opal stand-in principal's real call returns an enveloped answer (`as_of`, `source_keys`, `denominator`, `absent_reason`; a client tool for a firm with live data returns rows, a firm with no catalog row answers `no_catalog_row`), and a non-Opal principal is refused with zero reads. `assume_role_real`: from the host, the gateway role performs one real `sts:AssumeRole` of `gateway-smartx-read-role` (record the call succeeded; print no credential). `smartx_two_firm_arm`: through the installed `client_*` tools, a SmartX read for firm A returns only firm A's rows and the same read naming the other SmartX firm returns a refusal or only that firm's rows, never A's (counts only; no account number, no name). No object content, account number or person's name is printed.
6. **Standing clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and `file_checksums` come from the release blobs. Close the ledger, commit, run AC2, and report once to `2.0.0_SA_COO~O`. Report once per phase. After the close, `2.0.0_SA_COO~O` tells `2.0.0_SA_COO~MI` and `~MP` the live commit.

## 2. BOUNDS

- The release's files only. No IAM or Terraform change, no catalog edit, no object or item written to any bucket or table.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply`; print an `.env` value, a credential, an account number, a person's name or email, or object content; override a gate other than the one audited lane escape in step 2 of Phase A.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-code.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-23"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap23.AC1.sh; echo "exit=$?"</invocation><expect>(?s)base [0-9a-f]+ is the live ref before this release: yes.*outside the batch set 0 \(want 0\); terraform files differing 0 \(want 0\).*registered in the release (\d+) of \1; extra tools in the release 0 \(want 0\); SAFE (\d+) of \2; NATIVE (\d+) of \3.*byte-equal to the registry yes.*mcportal bundle: manifest mcportal_commit equals the GO's, descends from 421f8fbe84, only that manifest field changed yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-23"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap23.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*landed=(?:current|superseded).*registry [0-9]+ -> [0-9]+ \(\+\d+\); per-tool (\d+) of \1; C1 real AssumeRole yes; C2 smartx two-firm arm yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-23" judgment="true"/>
</proof_of_spec>

- `AC1`: the re-cut carries exactly the tools and files trunk adds beyond the live ref, no Terraform, with the registry copy staged. `AC2`: the release landed and closed; the installed code serves every added tool to an Opal principal and refuses a non-Opal one; the CVO's C1 and C2 are met.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`): the first client and rival answers read as an analyst would want them (a firm's data date stated, figures with units, rows never merged across firms, Schwab masters never summed). Graded on a real call; never simulated here.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-23.code-batch-release.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream CODE-BATCH (decomposition addendum R3-T.73). Supersedes `OG-ap-22`. Queue on the gateway host: THIS, then `NFRA_MCPINDEX.TO-MX-r-15` (catalog-only, cut on this release's commit; I tell `~MI` the live commit at the ledger close).
- Staged: the GO for Phase A is the issuer's message citing this order and naming `trunk_sha`, sent after the hookup of the json-served tools and the `OG-cl-8` registry rows are on trunk.
- Finish-by: Fri 2026-10-16 ~22:00Z (CTO GO msg 34552, PRD v3.12).
- Pre-cut: ap23.AC1 and ap23.AC2 base FAIL as expected (ap23_release.json and CODE_SERVED.json absent).

<status>staged</status>
<round>37</round>
<workstream>CODE-BATCH</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
