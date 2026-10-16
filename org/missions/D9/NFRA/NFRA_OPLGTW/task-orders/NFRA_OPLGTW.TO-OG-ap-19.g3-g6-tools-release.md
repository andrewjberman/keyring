# NFRA_OPLGTW task order -- `OG-ap-19` -- APPLY: the eight G3 portal tools and the five G6 news tools, their two read grants and their gateway release (FWD-22)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-19</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-19</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; the applier still runs `comp-schedule --drift` at the act and records what it scanned.
comp-iam: RUN-BY-ISSUER at the cut: the G6 grant is the worker's `infra/aws/terraform/opal-gateway/news_read_iam.tf` (merged `21073a6055`): ONE `aws_iam_role_policy` `gateway-global-news-read-policy` on the gateway instance role, `dynamodb:Query` and `dynamodb:GetItem` only, on the tables `opal-news-articles`, `opal-news-trending-daily`, `opal-keyword-intelligence` and the index `date-index`; the G3 grant is yours to write in Phase A (one policy on `aws_iam_role.int_reader`, `s3:GetObject` on `json-tiered/market-overview/` of the portal bucket). Nothing else changes in IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the G3 and G6 plan of decomposition addendum R3-T.52 (PRD v3.7 and v3.8, FWD-22), the CTO's Friday set (msg 34198) and the CRO's G3/G6 census.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-19` (decomposition addendum R3-T.57, workstream G3G6-RELEASE, FWD-22)

APPLY: release thirteen READ tools and the two grants they need on the live ref that `OG-ap-18` and `OG-yr-1` leave. Opal principals only; each tool admits before any read. The builds are merged: `OG-pt-1` (`4a153a46e1`), `OG-pt-2` (`6bf3636c5d`), `OG-nw-1` (`21073a6055`),
the fix `OG-gt-10` (`d7aec6640c`: the portal modules find the staged calendar by search) and the hookup `OG-pt-4` (merge `d91f1363c7`, worker commit `4500d443a0`; pins +13). `OG-pt-3` is SUPERSEDED: `mdpf_get_category_views` rides `NFRA_MCPINDEX`.

The thirteen: `portal_get_model_positioning`, `portal_get_model_attribution`, `portal_get_market_returns`, `portal_get_market_regime`, `portal_get_macro`, `portal_get_valuation`, `portal_get_security_scan`, `portal_get_pipeline_freshness`,
`news_search_articles`, `news_trending_topics`, `news_keyword_intelligence`, `news_market_mood`, `news_for_security`.

### PHASE A (only when `OG-ap-18`'s ledger `nfra-oplgtw-gateway-release-gt` and `OG-yr-1`'s `nfra-oplgtw-gateway-release-yr` are CLOSED): grant file, re-cut, ask. NO deploy, NO apply

1. **Live ref.** Read `services.opal-gateway.deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json` at HEAD, then one SSM md5 read of the host against it, walking `app/`, `deploy/`, `dashboard/` AND `lib/`. A mismatch is a STOP and a BLOCKING row.
2. **The G3 grant.** Write `infra/aws/terraform/opal-gateway/portal_tiered_read_iam.tf`: ONE `aws_iam_role_policy` on `aws_iam_role.int_reader` (the identity that makes the S3 call; `mcpmsp_internal_reader.tf` already grants `json/*` and `platinum/*` of the portal bucket and nothing under `json-tiered/`),
   `s3:GetObject` on `arn:aws:s3:::<portal bucket>/json-tiered/market-overview/*` and nothing else; no `*` resource, no Put, no Delete. Generate the prefix list by AST from `portal_models.SERVED_PREFIXES` and the key constants of `portal_macro.py`, keeping ONLY what the existing grant does not cover,
   so the grant cannot drift from the code (as `hv2_grant_gen.py` did for the harvest grant). The policy name and the bucket come from `lib/opal_naming.py` (`name("gateway", "global", "portal-tiered-read", "policy")`), written as literals the naming limb can grade.
   The grant prefix is a LEGACY key: per the CTO ruling (msg 34173) commit the `legacy_addresses.json` row(s) (reader `NFRA_OPLGTW`) FIRST, on their own, then the `.tf` together with ONE file under `org/missions/D9/NFRA/NFRA_OPLGTW/` (the generator). No firm token in a grant prefix.
3. **The G6 grant** is the merged `news_read_iam.tf`, unchanged. Run the targeted plan for BOTH policies (`-target` each, `-lock=false`, no `-out`, no apply); the plan must read `2 to add, 0 to change, 0 to destroy`. Save it as `W/G36_PLAN.txt`. Any other change is a STOP.
4. **Re-cut** in a worktree `C:/tmp/og-rel-g36`, new branch `rel-nfra-oplgtw-g36`, at the live ref. Take WHOLE from `box/sitez` HEAD: `app/portal_models.py`, `app/portal_macro.py`, `app/news_typed.py`, `tests/test_og_pt1.py`, `tests/test_og_pt2.py`, `tests/test_og_nw1.py`, `tests/test_og_gt10.py`. Take BY HUNK
   (3-way where the base differs; never a whole file from trunk): the thirteen registrations, the import line, the thirteen names in `SAFE_TOOLS` and `NATIVE_TOOLS` and the two re-pinned counts of the hookup `4500d443a0` into `app/tools.py`, `app/destructive_ops.py`, `app/data_entitlement.py`,
   `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py` (the pins are the BASE'S plus thirteen: re-derive them against the base you cut on; the trunk's 88 and 79 assume the G1 set is in the base); and the three `NEWS_*` `.env` keys of `deploy-to-ec2.sh` from `c1f02c8f63`.
   Add the two grant files. Commit with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the release commit only. Write `W/g36_release.json` = `{"base_sha", "release_sha"}` (FULL 40-character shas). Run in the release tree: `tests/test_og_pt1.py`, `test_og_pt2.py`, `test_og_nw1.py`, `test_og_gt10.py`,
   `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py`, and the host-shaped import check: copy the release tree's `app/` to a 4-parent path with `lib/trading_calendar.py` beside it and import the three modules and `app.tools` in a fresh interpreter.
5. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-19.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`). Each under a heading containing its word: (1) the `diff` by file; (2) the thirteen `tools`, their class and their `refused` arms; (3) the `widening`, stated plainly:
   the gateway instance role gains `dynamodb:Query` and `dynamodb:GetItem` on three named tables and one index (news articles, trending, keyword intelligence), the internal reader role gains `s3:GetObject` under `json-tiered/market-overview/` of the portal bucket, and thirteen tools make that data easy to read for Opal principals only,
   with the data named (market and macro series, model positioning and attribution, news article text and sentiment); (4) the `order` of acts (both grants, then the deploy); (5) `both branches` of a call (refused: zero reads; admitted: capped, projected to 50 KB); (6) the `rollback` (each policy destroyed through `safe-apply` targeted; redeploy the base);
   (7) the `triggers` (`/health`, the registry count +13, the three `NEWS_*` key names present, md5 = release, both policies present in IAM). Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

6. Ledger `nfra-oplgtw-gateway-release-g36`, entry AND sentinel first. Apply the two policies through `safe-apply`, targeted, ONE at a time, reading each back from IAM (`get-role-policy`) before the next. Deploy from `C:/tmp/og-rel-g36` through `infra/aws/ec2/safe-ec2-deploy.sh` with `DEPLOY_BASE_REF=<base_sha>`; the deploy tree's
   `git rev-parse HEAD` must equal the signed `release_sha` in full and its parent must equal live `deployed_commit` at the act (a mismatch is a STOP; print both). No `HALT_OVERRIDE`. Read back against the triggers; on any trigger redeploy the base, destroy the grants this ask added, and file an ARMED row naming `2.0.0_SA_COO~O`.
7. **The served read**, through the INSTALLED code on the host, one SSM call writing `W/G36_SERVED.json` = `{"body": {"registry_before": N, "registry_count": N+13, "policies_live": true, "env_key_names_present": true, "per_tool": {"<tool>": {"opal_served": true, "non_opal_refused": true, "reads_on_refusal": 0}, ...}}}` for all thirteen tools:
   an Opal stand-in principal's real call returns an enveloped answer (`as_of`, `source_keys`, `denominator`, `absent_reason`) and carries a numeric `trading_days_behind_t1` where the tool states freshness; a non-Opal principal is refused with zero reads. No object content is printed.
8. **Standing release clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and `file_checksums` come from the release blobs. Close the ledger, commit, run AC2, and report once to `2.0.0_SA_COO~O`. Report once per phase.

## 2. BOUNDS

- The release's files and the two grants only. No other IAM or Terraform change, no catalog edit, no object or item written to any bucket or table.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply` (use `safe-apply`); print an `.env` value, a person's name or email, or object or item content; override a gate other than the one audited lane escape in step 4.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
infra/aws/terraform/opal-gateway/portal_tiered_read_iam.tf
infra/aws/terraform/opal-gateway/news_read_iam.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
infra/logic/registry/legacy_addresses.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-g36.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-19"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap19.AC1.sh; echo "exit=$?"</invocation><expect>(?s)base [0-9a-f]+ is the live ref before this release: yes.*outside the G3-G6 set 0 \(want 0\); tools registered 13 of 13; SAFE 13 of 13; NATIVE 13 of 13.*grants: news_read_iam\.tf policies 1 \(want 1\), wildcard resource 0 \(want 0\); portal_tiered_read_iam\.tf policies 1 \(want 1\), wildcard resource 0 \(want 0\), only the json-tiered/market-overview prefix yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-19"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap19.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*landed=(?:current|superseded).*registry [0-9]+ -> [0-9]+ \(\+13\); per-tool 13 of 13; policies live in IAM yes; NEWS_\* key names present yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-19" judgment="true"/>
</proof_of_spec>

- `AC1`: the re-cut carries exactly the G3 and G6 build on the live ref with thirteen registrations and the two grants as one policy each, no wildcard, the G3 one confined to its prefix.
- `AC2`: the release landed and closed, both policies are live, and the installed code serves all thirteen tools to an Opal principal and refuses a non-Opal one.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`): the first portal and news answers read as an analyst would want them (freshness in trading days, a quiet day answered as an empty window with its as-of and not as an error, the 14-day news cap stated by `news_search_articles`). Graded on a real call; never simulated here. (Reworded by A3: the portal and news tools carry no `data_status` field.)

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-19.g3-g6-tools-release.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G3G6-RELEASE (decomposition addendum R3-T.57; plan R3-T.52, PRD v3.7). The issuer registered the tools and re-pinned counts at the merge (CUT BY WRITE SET: hookups belong to no cell).
- Release queue: ap-18 (G1, re-cut) -> yr-1 -> THIS -> ap-20 (G5 wave A) -> ap-17 (bd-3, re-cut) -> ap-21 (G2 core). MX-r-13 (`~MI`) takes its slot when `~MI` asks; each release closes with the live commit told to `2.0.0_SA_COO~MI`.
- Staged: Phase A waits on ap-18 and yr-1 closing; the GO for Phase A is the issuer's message citing this order.
- Pre-cut: ap19.AC1 and ap19.AC2 base FAIL as expected (g36_release.json and G36_SERVED.json absent).

- A1 (issuer, 2026-10-15 ~00:1xZ, row Z-S132): the release worktree carries `infra/logic/` in its cone (its registry feeds `lib/opal_naming.py address()`, which `deploy-to-ec2.sh` calls for the `.env` S3 roots); prove it with a no-upload dry read of the script's naming step before Phase B. Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A2 (issuer, 2026-10-15 ~03:5xZ, msg 34323, row Z-S137): `app/typed_scope.py` (OG-gt-6, merged `d8b0b28c32`) is the seam the portal and news modules import, and ap-18 deliberately left it out; it is in neither the base nor the take-list, and `portal_models.py` imports it, so without it the service would not start. Ruled route (a): take `app/typed_scope.py` WHOLE and its test `tests/test_og_gt6.py` WHOLE from `box/sitez` HEAD into this release (code only: no IAM, no grant, no tool of its own; it is what makes the thirteen tools' admission uniform). The ask names the two files under `diff`. ap19.AC1's allow-list gains both. Add the host-shaped import check of `app.typed_scope` itself. `app/harvest_published.py` stays out (its own ask). Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A3 (issuer, 2026-10-16 ~10:5xZ, row Z-S168 and Z-S170 of `0.7.0_AE_CloudOps~Z` in `OG-ev-1`): the AC3 text named `data_status` on a quiet day, a field only the harvest answers carry (ap-18 shows it); the portal and news tools express a quiet day as an empty window with its as-of. The AC3 marker is reworded to that, a wording change of a judgment line (no mechanical criterion moves; the CVO still grades on the real answers). The 14-day cap is the `news_search_articles` tool's (PRD v3.x G6 (c)); `news_for_security` applies a 30-day window by its own contract, so the marker's body comes from `news_search_articles` (`OG-ev-1` A1). Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>complete</status>
<round>37</round>
<workstream>G3G6-RELEASE</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
