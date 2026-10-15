# NFRA_OPLGTW task order -- `OG-ap-20` -- APPLY: the five G5 wave A etfs tools and mdpf_get_category_views, their read grant and their gateway release (FWD-22)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-20</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-20</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; the applier still runs `comp-schedule --drift` at the act and records what it scanned.
comp-iam: RUN-BY-ISSUER at the cut: the grant is ONE `aws_iam_role_policy` on the gateway's internal reader role for `s3:GetObject` and a prefix-confined `s3:ListBucket` on named prefixes of `opal-data-etfs`, generated from the catalog rows of the tools' entities plus the rival-funds prefixes of PRD v3.7; nothing else changes in IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the G5 wave A plan of decomposition addendum R3-T.52 (PRD v3.7 and A1, FWD-22), the CTO's Friday set (msg 34198) and the CRO's G5 census and G5r spec.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-20` (decomposition addendum R3-T.62, workstream G5A-CV, FWD-22)

APPLY: release six READ tools and the one read grant they need on the live ref that `OG-ap-18` (and `OG-ap-19`, if it lands first) leave. Opal principals only; each tool admits before any read. The builds are merged: `OG-et-1` (`13979abd45`), `OG-et-2` (`9a16c77a6a`), `OG-pt-5` (`00e2b960ea`)
and the hookup `OG-gt-12` (pins +6). Every key and the bucket are read by the tools from their DATA_CATALOG table rows at call time (`NFRA_MCPINDEX` v0.5); the grant is generated from THE SAME ROWS.

The six: `etfs_get_partner_ownership`, `etfs_get_ownership_rollup`, `etfs_get_monthly_report`, `etfs_get_fund_nav_history`, `etfs_get_fund_holdings`, `mdpf_get_category_views`.

### PHASE A (only when the live ref is stable: `OG-ap-18`'s ledger `nfra-oplgtw-gateway-release-gt` is CLOSED): grant file, re-cut, ask. NO deploy, NO apply

1. **Live ref.** Read `services.opal-gateway.deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json` at HEAD, then one SSM md5 read of the host against it, walking `app/`, `deploy/`, `dashboard/` AND `lib/`. A mismatch is a STOP and a BLOCKING row.
2. **The G5 grant.** Write `infra/aws/terraform/opal-gateway/etfs_read_iam.tf`: ONE `aws_iam_role_policy` on `aws_iam_role.int_reader` (the identity that makes the S3 call), `s3:GetObject` on the prefixes of the catalog rows of these entities (read each row's `bucket` and `prefix`/`key_template`, keep the top-level prefix, no firm token):
   `opal_data_etfs_gold_daily_partner_ownership`, `opal_data_etfs_platinum_etf_ownership_dashboard`, `opal_data_etfs_platinum_monthly_ownership_report`, `opal_data_etfs_silver_netassets_daily`, `opal_data_etfs_gold_holding`, `opal_data_etfs_gold_book`, `opal_data_etfs_silver_holdings`;
   AND (PRD v3.7, CTO msg 34198: one ask, one grant, no second ask later) the rival-funds gold prefix `rivalfunds/etfs/gold/*` and the platinum page prefix `rivalfunds/etfs/platinum/page/*` of the same bucket, from the rows `opal_data_etfs_gold_*` (the rivalfunds ones) and `opal_data_etfs_platinum_rivalfunds_page`; plus `s3:ListBucket` on the bucket confined by an `s3:prefix` condition to the same prefixes
   (the tools list a partner's folder and the report months). No Put, no Delete, no bucket-wide object ARN, no `*` resource. A small generator script (committed beside the other grant generators in `W/`) reads the rows from the committed catalog, so the grant cannot drift from the tools' reads. `mdpf_get_category_views` reads `platinum/mdpf/` of the PORTAL bucket, which the existing
   internal-reader policy already grants (`platinum/*`): no grant for it.
   The policy name and the bucket come from `lib/opal_naming.py` (`name("gateway", "global", "etfs-read", "policy")`), written as literals the naming limb can grade. The legacy prefixes (`daily/`, `platinum/`, `gold/`, `silver/`, `rivalfunds/etfs/`) are LEGACY keys: per the CTO ruling (msg 34173) commit the
   `legacy_addresses.json` row(s) (reader `NFRA_OPLGTW`) FIRST, on their own, then the `.tf` together with ONE file under `org/missions/D9/NFRA/NFRA_OPLGTW/` (the generator).
3. Run the targeted plan for the one policy (`-target`, `-lock=false`, no `-out`, no apply); it must read `1 to add, 0 to change, 0 to destroy`. Save it as `W/G5A_PLAN.txt`. Any other change is a STOP.
4. **Re-cut** in a worktree `C:/tmp/og-rel-g5a`, new branch `rel-nfra-oplgtw-g5a`, at the live ref, with `infra/logic/` and `org/missions/DIRECTIVES.yaml` in the cone. Take WHOLE from `box/sitez` HEAD: `app/etfs_ownership.py`, `app/etfs_funds.py`, `app/portal_mdpf.py`, `tests/test_og_et1.py`, `tests/test_og_et2.py`, `tests/test_og_pt5.py`.
   Take BY HUNK (3-way where the base differs; never a whole file from trunk): the six registrations, the import line, the six names in `SAFE_TOOLS` and `NATIVE_TOOLS` and the two re-pinned counts of the hookup `OG-gt-12` (worker commit named in its merge) into `app/tools.py`, `app/destructive_ops.py`, `app/data_entitlement.py`, `tests/test_entitlement_admin.py`,
   `tests/test_data_entitlement_family.py` (the pins are the BASE'S plus six: re-derive them against the base you cut on). Add the grant file. Commit with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the release commit only. Write `W/g5a_release.json` = `{"base_sha", "release_sha"}` (FULL 40-character shas).
   Run in the release tree: the three tool suites, `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py`, and the host-shaped import check (a 4-parent path with `lib/trading_calendar.py` beside it; the three modules and `app.tools` in a fresh interpreter).
5. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-20.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`). Each under a heading containing its word: (1) the `diff` by file; (2) the six `tools`, their class and their `refused` arms; (3) the `widening`, stated plainly: the internal reader role gains `s3:GetObject`
   and a prefix-confined `s3:ListBucket` on the named prefixes of `opal-data-etfs`, including the partner folders `daily/<partner>/` (CLIENT-derived ownership by partner firm: the tools are Opal-principal-only and take ONE firm per call; no tool returns a total that adds firm slices) and the rival-funds prefixes that no tool of this release reads yet (granted now by the CTO's one-ask ruling); list every prefix;
   (4) the `order` of acts (the grant, then the deploy); (5) `both branches` of a call (refused: zero reads; admitted: capped, projected to 50 KB); (6) the `rollback` (the policy destroyed through `safe-apply` targeted; redeploy the base); (7) the `triggers` (`/health`, the registry count +6 on the host and on the repo pin, `.env` names unchanged, md5 = release, the policy present in IAM). Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

6. Ledger `nfra-oplgtw-gateway-release-g5a`, entry AND sentinel first. Apply the one policy through `safe-apply`, targeted, reading it back from IAM (`get-role-policy`). Deploy from `C:/tmp/og-rel-g5a` through `infra/aws/ec2/safe-ec2-deploy.sh` with `DEPLOY_BASE_REF=<base_sha>`; the deploy tree's `git rev-parse HEAD` must equal the signed `release_sha` in full and its parent must equal
   live `deployed_commit` at the act (a mismatch is a STOP; print both). No `HALT_OVERRIDE`. Read back against the triggers; on any trigger redeploy the base, destroy the grant this ask added, and file an ARMED row naming `2.0.0_SA_COO~O`.
7. **The served read**, through the INSTALLED code on the host, one SSM call writing `W/G5A_SERVED.json` = `{"body": {"registry_before": N, "registry_count": N+6, "policies_live": true, "per_tool": {"<tool>": {"opal_served": true, "non_opal_refused": true, "reads_on_refusal": 0}, ...}}}` for all six tools:
   an Opal stand-in principal's real call returns an enveloped answer (`as_of`, `source_keys`, `denominator`, `absent_reason`) with a numeric `trading_days_behind_t1`; a non-Opal principal is refused with zero reads. For `mdpf_get_category_views` also record the served arms the worker's probe could not (an Opal identity with its email in the request context reading `global` and one firm scope). No object content is printed.
8. **Standing release clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and `file_checksums` come from the release blobs. Close the ledger, commit, run AC2, and report once to `2.0.0_SA_COO~O`. Report once per phase.

## 2. BOUNDS

- The release's files and the one grant only. No other IAM or Terraform change, no catalog edit, no object or item written to any bucket or table.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply` (use `safe-apply`); print an `.env` value, a person's name or email, or object or item content; override a gate other than the one audited lane escape in step 4.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
infra/aws/terraform/opal-gateway/etfs_read_iam.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
infra/logic/registry/legacy_addresses.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-g5a.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-20"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap20.AC1.sh; echo "exit=$?"</invocation><expect>(?s)base [0-9a-f]+ is the live ref before this release: yes.*outside the G5A set 0 \(want 0\); tools registered 6 of 6; SAFE 6 of 6; NATIVE 6 of 6.*grant: etfs_read_iam\.tf policies 1 \(want 1\), wildcard resource 0 \(want 0\), only opal-data-etfs yes, rival-funds gold prefix yes, rival-funds page prefix yes, put or delete actions 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-20"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap20.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*landed=(?:current|superseded).*registry [0-9]+ -> [0-9]+ \(\+6\); per-tool 6 of 6; policy live in IAM yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-20" judgment="true"/>
</proof_of_spec>

- `AC1`: the re-cut carries exactly the G5 wave A and category-views build on the live ref with six registrations and the one grant (one policy, no wildcard, only `opal-data-etfs`, the rival-funds prefixes named, no Put or Delete).
- `AC2`: the release landed and closed, the policy is live, and the installed code serves all six tools to an Opal principal and refuses a non-Opal one.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`): the first ETF ownership and fund answers read as an analyst would want them (weights in percentage points with their unit, three dates in one row, coverage from each partner's own csv). Graded on a real call; never simulated here.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-20.g3-g6-tools-release.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G5A-CV (decomposition addendum R3-T.62; plan R3-T.52 and its A1, PRD v3.7). The issuer registers the tools and re-pins counts at the merge (OG-gt-12).
- Release queue: ap-18 (G1, three halves signed) -> ap-19 (G3 + G6) -> THIS -> ap-17 (bd-3 re-cut) -> ap-21 (G2 core); each close tells `2.0.0_SA_COO~MI` the live commit.
- Staged: Phase A waits on ap-18 closing; the GO for Phase A is the issuer's message citing this order.
- Pre-cut: ap20.AC1 and ap20.AC2 base FAIL as expected (g5a_release.json and G5A_SERVED.json absent).

- A1 (issuer, 2026-10-15 ~04:5xZ, msgs 34336 and 34325): `OG-ap-19` is LIVE at `ee23dd004c` (AC1+AC2 PASS re-run by the issuer, ledger CLOSED): PHASE A OPENS NOW on that live ref, EXCEPT the re-cut, which waits on the catalog: the three modules read their key templates and the bucket from `app/refs/DATA_CATALOG.yaml` at RUNTIME, and the live base carries catalog v0.4 while trunk carries v0.5 (the 216 table rows). Without v0.5 every tool answers `absent_reason` (no crash, no data). `NFRA_MCPINDEX.TO-MX-r-13` (`0.7.0_AE_CloudOps~MI`) releases the catalog; it goes FIRST. Steps 2-3 (the grant file, its plan) start now; step 4 (the re-cut) waits until `MX-r-13` is live and the base is re-read. The take-list must also ENUMERATE THE SEAMS the taken modules import from earlier cells (the CTO's ask after Z-S130 and Z-S137): before the cut, list every `from . import` / `from .x import` of `etfs_ownership.py`, `etfs_funds.py` and `portal_mdpf.py` that resolves to an app module, and prove each is in the live base or in the take-list (`app/typed_scope.py` and `app/harvest_typed.py` are in the base since ap-18 and ap-19; `app/integrations/portal_index/integration.py` and `app/graphql_plumbing/catalog_gate.py` are read by `portal_mdpf.py` and must be in the base too; the catalog `app/refs/DATA_CATALOG.yaml` is read at RUNTIME by all three modules and must be in the base at v0.5 or later, or in the take-list: check it). A missing seam is a STOP and a row, found at the cut and not at the deploy. The host-shaped import check covers the three modules and `app.tools`. Registry instrument: the host's own registry (live 69 -> 75) and the repo pin (88 -> 94 on the G1+G3+G6 base), named in `G5A_SERVED.json`. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>G5A-CV</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
