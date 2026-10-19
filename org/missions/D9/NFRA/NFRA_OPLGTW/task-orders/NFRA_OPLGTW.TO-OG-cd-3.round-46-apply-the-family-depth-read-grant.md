# NFRA_OPLGTW task order -- `OG-cd-3` -- APPLY (grant): the gateway role reads the sweep rules' schedules and the silver status and listing objects the `family_depth` read needs (round 46; round-45 analysis A1 item 3, second half; PRD v2.6 FWD-20)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cd-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cd-3</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; you still run `comp-schedule --drift` at the act and record what it scanned.
comp-iam: RUN-BY-ISSUER at the cut: the grant is the ONE file `infra/aws/terraform/opal-gateway/family_depth_read_iam.tf` written by `OG-cd-1` (a worker) and already on trunk: ONE `aws_iam_role_policy` (`gw_family_depth_read`, name `gateway-family-depth-read-policy`) on the gateway role with three Allow statements: `events:DescribeRule` on the `opal-assets-silver-*-sweep-daily` rules; `s3:GetObject` on `opal-data-assets/*/meta/backfill-status.json`; `s3:ListBucket` on `opal-data-assets`, conditioned on `s3:prefix` to the silver prefixes and the one-level source prefixes. No `*` action or resource, no write action. The role today holds no `opal-data-assets` S3 and no events read (the file's own header and `OG-cd-1`'s measurement).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-45 analysis amendment A1, list item 3 (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round45.md` @6018fc83fd): "apply its read IAM (`family_depth_read_iam.tf`, through `safe-apply`)".
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-cd-3` (decomposition addendum R3-T.123, amendment A1, round 46, workstream ENRICH-R46-B)

You are the grants applier. `OG-cd-3` applies IAM only; it never deploys. The code that uses the grant is the route of `OG-cd-2`, released later by `OG-ap-50` (staged behind this order's close). The grant sits unused until that release. METHOD = `OG-ap-25`'s (`org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-ap-25.etf-classifications-read-grant.md`), read first and followed step by step; this order states only what differs (the file already exists; there is nothing to author).

### PHASE A (no apply IN ANY FORM; a negative check is a plan and its output is KEPT)

1. **Read the live state first.** `get-role` for `opal-gateway-role`, `list-role-policies` for it; confirm `gateway-family-depth-read-policy` is NOT already attached (a duplicate is a STOP). Write `W/FD_BEFORE.json` = `{"read_at": "<iso>", "role_policies": [...]}` and print the denominator.
2. **Read the file** `infra/aws/terraform/opal-gateway/family_depth_read_iam.tf` AT TRUNK HEAD (`git show HEAD:<path>`) and say in the ask whether you changed it. Change it only for a naming-gate or `terraform fmt` refusal, and then by the smallest edit, listed in the ask. Do not widen any statement.
3. **The plan**, targeted at `aws_iam_role_policy.gw_family_depth_read`, `-lock=false`, no `-out`, no apply: it must read `1 to add, 0 to change, 0 to destroy`. Save it as `W/FD_PLAN.txt`. Any other change is a STOP.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-cd-3.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word (CTO, COO, CVO). It carries: (1) the `diff` by file (none beyond the .tf, or the listed fix); (2) the `widening`, stated plainly: the gateway role may DESCRIBE the silver sweep rules (their schedule), GET the `backfill-status.json` objects, and LIST the silver and source prefixes of `opal-data-assets`, and nothing else (no data object, no bronze or gold prefix, no write); what a reader learns (each family's schedule, last sweep and earliest served date, no data value); (3) the `route` that uses it (`/api/admin/gateway/families`, owner only, released by `OG-ap-50`; until then nothing calls these actions); (4) the `order` of acts (the grant applied once and read back from IAM, BEFORE the route's release); (5) `both branches` (a call outside the three statements is refused: the simulator's negative controls); (6) the `rollback` (`aws iam delete-role-policy --role-name opal-gateway-role --policy-name gateway-family-depth-read-policy`, or a targeted destroy); (7) the `triggers`; (8) the line `process-wide state this change touches: none (IAM policy only; no process, logger, signal, environment or global config), read`. Commit, run AC1 (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/cd3.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at the `.tf` hash)

5. Ledger `nfra-oplgtw-grants-cd3`, entry AND sentinel first. Apply the one policy through `safe-apply`, targeted, then read it back from IAM (`get-role-policy`) and with `simulate-principal-policy`: ALLOWED `events:DescribeRule` on one real sweep-rule ARN (take `opal-assets-silver-<family>-sweep-daily` from `aws events list-rules --name-prefix opal-assets-silver-`) and `s3:GetObject` on `arn:aws:s3:::opal-data-assets/<source>/<scope>/meta/backfill-status.json` for a real source and scope; and, as negative controls, NOT allowed `events:PutRule` on the same rule ARN and `s3:PutObject` on the same key ARN. On a trigger failing, destroy what this ask added and file an ARMED row naming `2.0.0_SA_COO~O`. Close the ledger, write `W/FD_APPLIED.json` = `{"policy_name": "<name>", "sample_rule_arn": "<arn>", "sample_status_key_arn": "<arn>", "policy_sha256_16": "<sha>", "applied_at": "<iso>"}`, commit, run AC2, report once, and send me the ledger CLOSED time.

### AMENDMENT A1 (issuer, 2026-10-19 ~11:0xZ; the CVO's refusal @adba2df9a0 relayed by the CTO, msg 35935; the CTO's half @673a4582d9 lapses with the new blob): the source-root list was RECURSIVE; RE-CUT THE `.tf` AND THE ASK

The CVO's refusal (read it: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_OG-cd-3_20261019.md`) found that statement `FamilyDepthSilverPrefixListOnly` limits `s3:ListBucket` by `s3:prefix` alone, so a call with prefix `schwab/` (any of the eight source roots) and NO delimiter lists every key under that root at any depth (bronze, gold, every firm's folder names): the ask's "one level deep" holds only if the caller passes `Delimiter="/"`, which `family_depth.py` does but the grant does not require. **PHASE B DOES NOT RUN on the first blob.** This supersedes the order's step 2 ("change it only for a naming-gate or fmt refusal"): you make THIS ONE change, and no other, in `infra/aws/terraform/opal-gateway/family_depth_read_iam.tf`:
1. Split the `s3:ListBucket` statement in two: (a) the silver prefixes `["*/silver/", "*/silver/*"]` under `StringLike` on `s3:prefix` (unchanged); (b) the eight source roots (`"<source>/"`) under `StringLike` on `s3:prefix` AND `StringEquals` `"s3:delimiter" = "/"`. The policy then has FOUR Allow statements. Keep every other statement byte-equal. Correct the `.tf` header comment that says a list scoped to any bronze/gold/meta prefix is refused by the condition, so it states what the two list statements admit.
2. Re-run the targeted plan (`1 to add, 0 to change, 0 to destroy`; save as `W/FD_PLAN.txt`; the plan must print `"s3:delimiter"`) and extend `cd3_simulate.py` with two cases whose names carry these phrases: `NEGATIVE: list a source root with NO delimiter` (`s3:ListBucket`, prefix `schwab/`, delimiter absent, expect `implicitDeny`) and `list a source root WITH delimiter /` (prefix `schwab/`, delimiter `/`, expect `allowed`), via an `s3:delimiter` context entry; the other cases stay (the `schwab/x/silver/t/` list with no delimiter stays allowed because `family_depth.py:261` makes it); `W/FD_SIMULATE_PLAN.json` must read all as expected.
3. Re-cut the ask `W/NEVER_WIDEN_ASK_OG-cd-3.md` under its NEW sha256 and `.tf` blob, restating section 2 at the new bound (a reader learns the same things; a source-root list is one level deep BY THE GRANT, not by the caller's courtesy) and addressing the full serial of each seat (never "his"). Commit, run AC1 (amended: it now also requires the delimiter bound), REPORT, STOP. All three halves are signed again on the new bytes; the CTO's `CT3` census (real top-level prefixes beyond the eight roots that hold a `silver/` child) is a Phase B step, read-only.
Phase B, at the new bytes: the live read-back repeats the new negative control with `simulate-principal-policy` (prefix `schwab/`, delimiter absent: NOT allowed; delimiter `/`: allowed) and writes `sample_root_prefix` (`schwab/`) into `W/FD_APPLIED.json`; `AC2` reads it; the policy has exactly FOUR statements.

## 2. BOUNDS

- IAM and Terraform of the one named policy only. No deploy, no release, no object read except the simulator and the describes above, no write to any store.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply` (use `safe-apply`); apply in Phase A in ANY form; print an account number.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/family_depth_read_iam.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
infra/logic/registry/legacy_addresses.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-grants-cd3.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cd-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/cd3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)delimiter bound: the \.tf and the plan name s3:delimiter True; simulation all as expected True, root list with NO delimiter denied [1-9]\d* case\(s\), root list WITH delimiter allowed [1-9]\d* case\(s\): ok.*terraform: role policies 1 \(want 1\); actions \['events:DescribeRule', 's3:GetObject', 's3:ListBucket'\] \(want .*?\); wildcard action or resource False \(want False\); other resource types 0 \(want 0\).*plan: 1 to add, 0 to change, 0 to destroy True; ask has the three halves True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cd-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r46/checks/cd3.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; policy \S+ shape ok; simulate DescribeRule allowed, GetObject allowed; root list with delimiter allowed, root list with NO delimiter \(negative control\) (?:implicitDeny|explicitDeny); negative controls PutRule (?:implicitDeny|explicitDeny), PutObject (?:implicitDeny|explicitDeny).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me on my run before any GO to Phase B; `AC2` (Phase B) after the ledger closes. `AC1`: the one `.tf` grants exactly the three read actions, the plan adds one policy, the ask has three halves. `AC2`: the policy is live, allows the two reads, refuses both writes by the simulator, and the ledger is closed.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cd-3.round-46-apply-the-family-depth-read-grant.proof_of_spec.json` after Phase B and validate it with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 46, workstream ENRICH-R46-B. Source: the CTO's round-45 analysis amendment A1 (msg 35923), item 3. The CTO's `OG-cd-2` names the mount AND the IAM; they have different write sets and owners (a worker's code, the applier's `safe-apply`), so they are cut as `OG-cd-2` (mount, worker) and `OG-cd-3` (this, applier): READING DISCLOSED TO THE CTO.
- Independent of the code cell; it runs as soon as the applier has the three halves. `OG-ap-50` stages behind its close AND `OG-cd-2`'s drain.
- Pre-cut (amended at A1: `AC1` and `AC2` now also grade the delimiter bound; fixtures re-run): `cd3.AC1` and `cd3.AC2` base FAIL as expected (plan, ask, ledger and record absent). `AC1` arms fed to the check: the real `.tf` with a good plan and ask passes; a plan reading 2 to add, an ask with one half, `s3:*` in place of `s3:GetObject`, and an added `s3:PutObject` each fail. `AC2` needs the live policy and cannot be fed an arm before Phase B.

<status>pending</status>
<round>46</round>
<workstream>ENRICH-R46-B</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
