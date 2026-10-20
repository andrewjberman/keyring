# NFRA_OPLGTW task order -- `OG-ls-1` -- APPLY (grant narrowing): the gateway role's silver `s3:ListBucket` statement lists only under the eight sources of `local.family_depth_sources`, not under any first component (round 47; round-46 analysis "the `*/silver/*` ListBucket narrowing"; CVO condition of `OG-cd-3`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ls-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ls-1</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; you still run `comp-schedule --drift` at the act and record what it scanned.
comp-iam: RUN-BY-ISSUER at the cut: the change is ONE list inside ONE statement of the ONE file `infra/aws/terraform/opal-gateway/family_depth_read_iam.tf` (`aws_iam_role_policy.gw_family_depth_read`, name `gateway-family-depth-read-policy`): the statement `FamilyDepthSilverPrefixListOnly` limits `s3:ListBucket` on `opal-data-assets` by `s3:prefix` `StringLike` `["*/silver/", "*/silver/*"]`, and in IAM a `*` matches `/` too, so the grant lists ANY prefix that has a `/silver/` component under any first component. The narrowing replaces that list by the per-source forms `<source>/*/silver/` and `<source>/*/silver/*` for each of the eight sources of `local.family_depth_sources` (`schwab orion eclipse blackdiamond trueshares pathfinder msn smartx`). It is a NARROWING: the new set of listable prefixes is a strict subset of the old. No action, resource or other statement changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is item 2 of the owed list (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/ROUND47_ITEMS_OWED_DRAFT.md`) ruled in by the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429, "the `*/silver/*` ListBucket narrowing") on the `OG-cd-3` Phase B census (`FD_CT3_CENSUS.json`: four top-level prefixes beyond the eight sources hold a silver child: bloomberg, commonwealth, gateway, yahoo).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ls-1` (decomposition addendum R3-T.124, amendment A1, round 47, workstream ENRICH-R47-B)

You are the grants applier. `OG-ls-1` applies IAM only; it never deploys and no code changes. Nothing in the gateway needs the prefixes this order removes: `family_depth.py` lists `<source>/<scope>/silver/<table>/` for the eight sources only. METHOD = `OG-cd-3`'s (`org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cd-3.round-46-apply-the-family-depth-read-grant.md`, with its amendment A1), read first and followed step by step; this order states only what differs.

### PHASE A (no apply IN ANY FORM; a plan's output is KEPT)

1. **Read the live state first.** `get-role-policy` for `gateway-family-depth-read-policy` on `opal-gateway-role`; write `W/LS_BEFORE.json` = `{"read_at", "policy_sha256_16", "statements": 4, "silver_prefix_patterns": [...]}` (the live patterns, which must read `*/silver/` and `*/silver/*`; anything else is a STOP and a row) and print the denominator. With the simulator, record the BEFORE decision for `s3:ListBucket` on `opal-data-assets` with `s3:prefix` = `bloomberg/global/silver/`, `gateway/global/silver/` and `yahoo/g/silver/` (expected `allowed`: that is the defect) and for `schwab/x/silver/t/` (allowed).
2. **Edit the one file** `infra/aws/terraform/opal-gateway/family_depth_read_iam.tf`: in the statement `FamilyDepthSilverPrefixListOnly` replace `"s3:prefix" = ["*/silver/", "*/silver/*"]` by `"s3:prefix" = flatten([for s in local.family_depth_sources : ["${s}/*/silver/", "${s}/*/silver/*"]])`, and correct the file's header comment about statement (a) so it says the glob is per source (the comment that says "the glob admits ANY prefix that has a /silver/ component under any first component" is no longer true). NOTHING ELSE changes (the other three statements stay byte-equal; the file keeps FOUR statements, one resource, the three read actions). Commit it; say in the ask that this is the only edit and give the blob before and after.
3. **The plan**, targeted at `aws_iam_role_policy.gw_family_depth_read`, `-lock=false`, no `-out`, no apply: it must read `0 to add, 1 to change, 0 to destroy` and show the per-source prefixes (`/*/silver/`). Save it as `W/LS_PLAN.txt`. Any other change is a STOP.
4. **The simulation plan** `W/LS_SIMULATE_PLAN.json` = `{"all_as_expected": <bool>, "results": [{"name", "action", "decision", "expected"}]}`, run against a scratch copy of the policy document (the plan's `after` document attached through `simulate-custom-policy`, or an equivalent that does not touch the live role), with these cases (the case names carry these exact phrases, `check ls1.AC1` reads them): `ALLOWED: silver table list under a source` (`s3:ListBucket`, prefix `schwab/x/silver/t/`, expect `allowed`); `NEGATIVE: silver list under bloomberg` (prefix `bloomberg/global/silver/`, expect `implicitDeny`); `NEGATIVE: silver list under gateway` (prefix `gateway/global/silver/`, expect `implicitDeny`); `NEGATIVE: silver list under yahoo` (prefix `yahoo/g/silver/`, expect `implicitDeny`); `NEGATIVE: list a source root with NO delimiter` (prefix `schwab/`, delimiter absent, expect `implicitDeny`); `ALLOWED: list a source root WITH delimiter /` (prefix `schwab/`, delimiter `/`, expect `allowed`). Set `all_as_expected` from the results.
5. **The ask**, `W/NEVER_WIDEN_ASK_OG-ls-1.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word (CTO, COO, CVO), naming each seat by its full serial. It carries: (1) the `diff` (the one list in the one statement, blob before and after); (2) the `widening`: NONE, stated plainly: a strict narrowing; what stops being listable (silver prefixes under bloomberg, commonwealth, gateway, yahoo and any other first component outside the eight sources) and that nothing the gateway runs reads them through this policy; (3) the `order` of acts (one apply, read back from IAM); (4) `both branches` (the simulator's negative controls, as item 4); (5) the `rollback` (revert the one list to `["*/silver/", "*/silver/*"]` and apply again; the old policy hash is in `W/LS_BEFORE.json`); (6) the `triggers` (the `family_depth` read run once on the host after the apply fails or answers fewer families than before; the policy shape is not four statements; any decision in the simulation differs from the plan); (7) the line `process-wide state this change touches: none (IAM policy only; no process, logger, signal, environment or global config), read`. Commit, run AC1 (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/ls1.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at the `.tf` blob)

6. Ledger `nfra-oplgtw-grants-ls1`, entry AND sentinel first. Apply the one change through `safe-apply`, targeted, then read the policy back from IAM and simulate against the LIVE role: ALLOWED `s3:ListBucket` with prefix `schwab/x/silver/t/` (use a real source, scope and table from a `list-objects-v2 --delimiter / --max-keys 5` walk, and put that prefix in the record); NOT allowed with prefix `bloomberg/global/silver/`, `gateway/global/silver/`, `yahoo/g/silver/`; root list with delimiter `/` allowed and without it NOT allowed; and the unchanged statements still ALLOW `events:DescribeRule` on one real sweep-rule ARN and `s3:GetObject` on one real `backfill-status.json` key ARN while `events:PutRule` and `s3:PutObject` on the same ARNs are NOT allowed. THEN run the `family_depth` read once on the host from the deployed tree under the hard guard, as the instance role, and record `families` and `denominator`: they must equal the counts of `W/FWD20_DRIVEN_READ.json` (the round-46 driven read) or you say why not. On a trigger failing, revert the list, apply, and file an ARMED row naming `2.0.0_SA_COO~O`. Close the ledger, write `W/LS_APPLIED.json` = `{"policy_name", "sample_rule_arn", "sample_status_key_arn", "sample_silver_prefix", "sample_root_prefix": "schwab/", "policy_sha256_16", "applied_at", "families_after", "denominator_after"}`, commit, run AC2, report once, and send me the ledger CLOSED time.

## 2. BOUNDS

- IAM and Terraform of the one named policy only. No deploy, no release, no object read except the simulator, the describes and the one `family_depth` read above, no write to any store.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply` (use `safe-apply`); apply in Phase A in ANY form; print an account number.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/family_depth_read_iam.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
infra/logic/registry/legacy_addresses.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-grants-ls1.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ls-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/ls1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)narrowing: the broad globs \*/silver/ and \*/silver/\* left in the \.tf False \(want False\); the silver statement is built from family_depth_sources True \(want True\); plan names the per-source form True.*simulation all as expected True; .*terraform: role policies 1 \(want 1\); statements 4 \(want 4\); actions .*wildcard action or resource False \(want False\); other resource types 0 \(want 0\).*plan: 0 to add, 1 to change, 0 to destroy True; ask has the three halves True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ls-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/ls1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; policy \S+ shape ok; silver list under a source allowed; census prefixes outside the eight: bloomberg (?:implicitDeny|explicitDeny), gateway (?:implicitDeny|explicitDeny), yahoo (?:implicitDeny|explicitDeny); root list with delimiter allowed, root list with NO delimiter \(negative control\) (?:implicitDeny|explicitDeny); unchanged statements DescribeRule allowed, GetObject allowed; negative controls PutRule (?:implicitDeny|explicitDeny), PutObject (?:implicitDeny|explicitDeny).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me on my run before any GO to Phase B; `AC2` (Phase B) after the ledger closes, against the LIVE role. `AC1`: the one file lists silver only under the eight sources, keeps FOUR statements and the three read actions, the plan is `0/1/0`, the simulation holds the six cases, the ask has three halves. `AC2`: the narrowed policy is live and the simulator refuses the three census prefixes.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ls-1.round-47-narrow-the-silver-list-grant-to-the-eight-sources.proof_of_spec.json` after Phase B and validate it with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-B (the applier amendments of the round, disjoint write surface: Terraform and the ledger), amendment A1 of R3-T.124. Source: the CTO's round-46 analysis (msg 36165) "the `*/silver/*` ListBucket narrowing", from the CTO half of `OG-cd-3` ("narrow to `<source>/*/silver/*` if the count is non-zero": it is 4).
- READINGS DISCLOSED TO THE CTO: (1) the narrowing keeps the delimiter-bound source-root statement and the other two statements byte-equal; it removes listability under bloomberg, commonwealth, gateway, yahoo and any other first component. (2) The gateway's client tools read `commonwealth/cottonwood/silver` through other policies (the Schwab and client readers), not through this one: the Phase B host read of `family_depth` is the proof that nothing it needs was removed. (3) A strict narrowing is not a widening, so the ask's widening half says NONE; it is still signed by three halves because it is an IAM write through `safe-apply`.
- Pre-cut: `AC1` base FAIL as expected (plan, ask and simulation absent), `AC2` base FAIL as expected, READ AGAINST THE LIVE ROLE: shape `broad`; bloomberg, gateway and yahoo silver lists read `allowed` (the defect); PutRule and PutObject controls absent for want of a record. `AC1` arms fed with synthetic inputs: the narrowed `.tf` with a `0/1/0` plan, three halves and the six simulation cases PASSES; the ORIGINAL `.tf` with the same inputs FAILS (broad globs left, no per-source build).

<status>pending</status>
<status>complete</status>
<round>47</round>
<workstream>ENRICH-R47-B</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
