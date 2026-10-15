# NFRA_OPLGTW task order -- `OG-ap-22` -- APPLY: the ten rival-funds tools (G5r) and their gateway release, no new grant (FWD-22)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-22</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-22</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; the applier still runs `comp-schedule --drift` at the act and records what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- this release changes NO IAM: the read grant for `rivalfunds/etfs/gold/*` and `rivalfunds/etfs/platinum/page/*` on the internal reader role is live since `OG-ap-20` (`06cfb6db64`, the one G5 ask under the CTO's ruling msg 34198); the ten tools read only those prefixes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is decomposition addendum R3-T.70 (PRD v3.7, FWD-22; CTO msgs 34190, 34198) and the CRO's G5r spec (e1b9937129).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-22` (decomposition addendum R3-T.70, workstream RIVAL-REL, FWD-22)

APPLY: release ten READ tools on the live ref that `OG-ap-21` (and the catalog tags release `NFRA_MCPINDEX.TO-MX-r-14` if it lands first) leave. Opal principals only; each tool admits before any read. The builds are merged: `OG-rv-1` (`be90fc548d`, `app/etfs_rivals.py`), `OG-rv-2` (`a1bd060467`, `app/etfs_rivals_flow.py`) and the hookup `OG-rv-3` (pins +10, the registry 95 -> 105 on trunk). Every key and the bucket are read by the tools from their DATA_CATALOG table rows at call time (v0.5 live); the read grant already exists (`OG-ap-20`), so this release is CODE ONLY: no Terraform, no apply, one deploy.

The ten: `etfs_get_peer_group_members`, `etfs_get_rival_fund_holdings`, `etfs_who_holds`, `etfs_get_security_reference`, `etfs_get_coverage` (module `etfs_rivals`), `etfs_get_fund_trades`, `etfs_get_fund_flows`, `etfs_compare_peers`, `etfs_get_research_notes`, `etfs_get_rival_page_status` (module `etfs_rivals_flow`). The CRO's `etfs_get_peer_group` was renamed because the naming gate types a `_group` ending as an IAM group; `etfs_get_fund_holdings` is already the four Opal funds' tool, so the rival one is `etfs_get_rival_fund_holdings`.

### PHASE A (only when the live ref is stable: `OG-ap-21`'s ledger `nfra-oplgtw-gateway-release-p21` is CLOSED, or the issuer's message names the live ref): re-cut, ask. NO deploy, NO apply IN ANY FORM

1. **Live ref.** Read `services.opal-gateway.deployed_commit` at HEAD and one SSM md5 read of the host against it over `app/`, `deploy/`, `dashboard/` and `lib/`. A mismatch is a STOP and a BLOCKING row. Re-read `get-role-policy` for `gateway-global-etfs-read-policy` on the internal reader role: it must still hold the rival prefixes (`rivalfunds/etfs/gold/*` GetObject and the two rival `s3:prefix` ListBucket conditions); if not, STOP.
2. **Re-cut** in `C:/tmp/og-rel-rv`, branch `rel-nfra-oplgtw-rv`, at the live ref, with `infra/logic/`, `org/missions/DIRECTIVES.yaml` AND `org/mcp/naming-gate.enforce` in the cone (the CTO's standing condition after Z-S142). **First enumerate the seams**: every app module the taken files import (`app/typed_scope.py`, `app/harvest_typed.py`, `app/internal_role.py` and the catalog loader are in the base; check the rest) and print each as in-base or in-take-list; a missing seam is a STOP and a row.
   Take WHOLE from `box/sitez` HEAD: `app/etfs_rivals.py`, `app/etfs_rivals_flow.py`, `tests/test_og_rv1.py`, `tests/test_og_rv2.py`. Take BY HUNK (3-way against the base; never a whole file from trunk): the one import line, the ten `@mcp.tool()` registrations, the ten names in `SAFE_TOOLS` and `NATIVE_TOOLS` and the two re-pinned counts of the hookup `OG-rv-3` into `app/tools.py`, `app/destructive_ops.py`, `app/data_entitlement.py`, `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py`
   (the pins are the BASE'S plus ten: re-derive them against the base you cut on, as the person-roles release does). Nothing else. Commit with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the release commit only; the naming gate runs in ENFORCE on it (sentinel present) and must print no REFUSE. Write `W/rv_release.json` = `{"base_sha", "release_sha"}` (FULL 40-character shas).
   Run in the release tree: `tests/test_og_rv1.py`, `tests/test_og_rv2.py`, `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py`, and the host-shaped import check (a 4-parent path with `lib/trading_calendar.py` beside it; the two modules and `app.tools` in a fresh interpreter).
3. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-22.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word: (1) the `diff` by file; (2) the ten `tools`, class and `refused` arms; (3) the `widening`, stated plainly: NO new permission (the read grant of `OG-ap-20` already covers the prefixes these tools read; list them and say which tool reads which); ten READ tools make Opal's research on the rival funds easy to read for Opal principals only; the rival fund data is public-fund research, not client data;
   (4) the `order` of acts (one deploy); (5) `both branches` (refused: zero reads; admitted: capped, projected to 50 KB); (6) the `rollback` (redeploy the base); (7) the `triggers`. Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

4. Ledger `nfra-oplgtw-gateway-release-rv`, entry AND sentinel first. Deploy from `C:/tmp/og-rel-rv` through `infra/aws/ec2/safe-ec2-deploy.sh` with `DEPLOY_BASE_REF=<base_sha>` under the A1 guard (HEAD = full `release_sha`, parent = live `deployed_commit`; no other release in flight). No `HALT_OVERRIDE`. Read back against the triggers; on any trigger redeploy the base and file an ARMED row naming `2.0.0_SA_COO~O`.
5. **The served read**, through the INSTALLED code on the host and through the public endpoint (60 s ALB), writing `W/RV_SERVED.json` = `{"body": {"registry_before": N, "registry_count": N+10, "policies_live": true, "page_status_manifest_read": true, "trades_rows_returned": K, "per_tool": {"<tool>": {"opal_served": true, "non_opal_refused": true, "reads_on_refusal": 0}, ...}}}` for all ten tools: an Opal stand-in principal's real call returns an enveloped answer (`as_of`, `source_keys`, `denominator`, `absent_reason`) with a numeric `trading_days_behind_t1` where the tool states freshness; a non-Opal principal is refused with zero reads. `policies_live` is the IAM read-back of the existing grant. `etfs_get_rival_page_status` must read the platinum manifest (`page_status_manifest_read`) and `etfs_get_fund_trades` for the fund with the most trades must return K greater than 0 rows whole (not truncated). No object content is printed.
6. **Standing release clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and `file_checksums` come from the release blobs. Close the ledger, commit, run AC2, and report once to `2.0.0_SA_COO~O`. Report once per phase.

## 2. BOUNDS

- The release's files only. No IAM or Terraform change, no catalog edit, no object or item written to any bucket or table.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply`; print an `.env` value, a person's name or email, or object content; override a gate other than the one audited lane escape in step 2 of Phase A.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-rv.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-22"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap22.AC1.sh; echo "exit=$?"</invocation><expect>(?s)base [0-9a-f]+ is the live ref before this release: yes.*outside the rival-funds set 0 \(want 0\); terraform files differing 0 \(want 0\); tools registered 10 of 10; SAFE 10 of 10; NATIVE 10 of 10.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-22"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap22.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*landed=(?:current|superseded).*registry [0-9]+ -> [0-9]+ \(\+10\); per-tool 10 of 10; grant live in IAM yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-22" judgment="true"/>
</proof_of_spec>

- `AC1`: the re-cut carries exactly the ten rival tools and their hookups on the live ref, with no Terraform. `AC2`: the release landed and closed, the existing grant is live, the page manifest is read, the top-trade fund's trades return whole, and the installed code serves all ten tools to an Opal principal and refuses a non-Opal one.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`): the first rival-funds answers read as an analyst would want them (a fund's report date and lag stated, weights with their unit, INFERRED trades labelled, the published page beside the holdings value, never merged). Graded on a real call; never simulated here.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-22.rival-funds-release.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream RIVAL-REL (decomposition addendum R3-T.70). Release queue: ap-20 (live) -> MX-r-14 (`~MI`) -> ap-21 (person roles) -> THIS -> ap-17 re-cut -> G2. Each close tells `2.0.0_SA_COO~MI` the live commit.
- Staged: Phase A waits on `OG-ap-21` closing; the GO for Phase A is the issuer's message citing this order. The hookup `OG-rv-3` must be merged first (it is the source of the registrations and the pins).
- Pre-cut: ap22.AC1 and ap22.AC2 base FAIL as expected (rv_release.json and RV_SERVED.json absent).

<status>pending</status>
<round>37</round>
<workstream>RIVAL-REL</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
