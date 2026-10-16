# NFRA_OPLGTW task order -- `OG-ap-25` -- APPLY (grant): the gateway role reads the DynamoDB etf-classifications table by key (the named next increment; CTO ruling @d97ea3ae82 section 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-25</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-25</to_id>
<issued_to>0.7.0_AE_CloudOps~ZS</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; the applier still runs `comp-schedule --drift` at the act and records what it scanned.
comp-iam: RUN-BY-ISSUER at the cut: the grant is ONE statement, Effect Allow, Action `dynamodb:GetItem`, Resource the table ARN of `etf-classifications` (us-east-1); the census (`W0/ETF_CLASS_CENSUS.json`) measured the table and its key schema (`ticker` hash, no range key); no `*` resource, no Scan, Query, write or batch action. The gateway role today reads the table with `implicitDeny` (the CRO's G4 spec section 3.3).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling @d97ea3ae82 section 2 (the table is the NAMED NEXT INCREMENT of NFRA_OPLGTW, owner `2.0.0_SA_COO~O`; it needs a DynamoDB read grant, a never-widen ask, and a census) built on the OG-ac-1 spec.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-25` (decomposition addendum R3-T.83, workstream CLASS-INCREMENT-2, FWD-22)

`W0` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/`. The tool `mdpf_get_security_classification` (built by `OG-ac-2`, module `app/mdpf_classification.py`) reads ONE item by its hash key `ticker` from the DynamoDB table `etf-classifications`. The census and the spec are `W0/ETF_CLASS_CENSUS.json` and `W0/ETF_CLASS_SPEC.md` (section `## Grant` is the statement you write; read both). You are the grants applier (`~ZS`): IAM and Terraform here; this order never deploys, and the code that uses the grant is a later release by `0.7.0_AE_CloudOps~Z`.

### PHASE A (files, plan, ask; NO apply IN ANY FORM, a negative check is a plan and its output is KEPT)

1. **Read the live state first.** `describe-table` for `etf-classifications` (ARN, key schema, item count: print the denominator), `get-role` for `opal-gateway-role`, and `list-role-policies` for it; confirm no policy of the role already names `etf-classifications` (a duplicate is a STOP). Write `W/CLS_BEFORE.json` = `{"read_at": "<iso>", "table_arn": "<arn>", "role_policies": [...]}`.
2. **Write the Terraform** `infra/aws/terraform/opal-gateway/etf_classification_read_iam.tf`: ONE `aws_iam_role_policy` on the gateway role (`aws_iam_role.gw`, the existing resource in this module; read how `queryv0-iam.tf` and `client_vendor_roles_iam.tf` attach theirs and copy the form), the policy name from `lib/opal_naming.py name()` written as a literal the naming limb can grade (a builder refusal is a missing registry row to add under `infra/logic/registry/` through the route the OG-ap-24 roles used, never a hand-typed workaround), one statement: Allow, Action `["dynamodb:GetItem"]`, Resource the table ARN (built from the table's own ARN with `data.aws_caller_identity`/`data.aws_region` or the literal ARN the census measured, as the sibling files do). No other resource in the file, no `*`.
3. **The plan**, targeted at that one policy, `-lock=false`, no `-out`, no apply: it must read `1 to add, 0 to change, 0 to destroy`. Save it as `W/CLS_PLAN.txt` and keep the output of every negative check. Any other change is a STOP.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-25.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word (CTO, COO, CVO): (1) the `diff` by file; (2) the `widening`, stated plainly: the gateway role may read ONE item at a time from the classifications table by ticker, and nothing else (no other table, no index, no write, no scan); what an Opal analyst learns (a security's asset class, sub-asset class, who classified it and the model's confidence), that the rows are Opal-internal market data and hold no client data; (3) the `tool` that uses it (`mdpf_get_security_classification`, Opal principals only, refuses before any read); (4) the `order` of acts (the grant applied once, read back from IAM, BEFORE the code release that serves the tool); (5) `both branches` (a refused call reads zero items; an admitted call reads one); (6) the `rollback` (destroy the one policy, targeted); (7) the `triggers`. Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at the `.tf` hash)

5. Ledger `nfra-oplgtw-grants-ap25`, entry AND sentinel first. Apply the one policy through `safe-apply`, targeted, then read it back from IAM (`get-role-policy`; `simulate-principal-policy` allows `dynamodb:GetItem` on the ARN and, as the negative control, does NOT allow `dynamodb:Scan` on it). On a trigger failing, destroy what this ask added and file an ARMED row naming `2.0.0_SA_COO~O`. Close the ledger, write `W/CLS_APPLIED.json` = `{"policy_name": "<name>", "table_arn": "<arn>", "policy_sha256_16": "<sha>", "applied_at": "<iso>"}`, commit, run AC2, report once.

## 2. BOUNDS

- IAM and Terraform of the one named policy only. No item written to or deleted from any table; no deploy; no catalog edit; no other table read.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply` (use `safe-apply`); apply in Phase A in ANY form; print an account number or a table item.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/etf_classification_read_iam.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
infra/logic/registry/legacy_addresses.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-grants-ap25.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free; a correction is a NEW row citing the old id), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-25"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap25.AC1.sh; echo "exit=$?"</invocation><expect>(?s)terraform: policies 1 \(want 1\); dynamodb actions \['dynamodb:GetItem'\] \(want \['dynamodb:GetItem'\]\); table arn ends table/etf-classifications True; wildcard action or resource False \(want False\); other resources 0 \(want 0\).*plan: 1 to add, 0 to change, 0 to destroy True; ask has the three halves True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-25"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap25.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; policy \S+ shape ok; simulate GetItem allowed, Scan \(negative control\) (?:implicitDeny|explicitDeny).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the one `.tf` file grants exactly `dynamodb:GetItem` on the table ARN, the plan adds exactly one policy, the ask has three halves. `AC2`: the policy is live on the gateway role, allows GetItem, denies Scan by the simulator, and the ledger is closed.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-25.etf-classifications-read-grant.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream CLASS-INCREMENT-2 (decomposition addendum R3-T.83). Outside the 22:00Z line (CTO ruling @d97ea3ae82 section 2). Parallel with `OG-ap-23`; disjoint (IAM here, code there). The Phase A GO is the issuer's message citing this order; `~ZS` is the grants applier.
- Census facts: 11,362 items, hash key `ticker`, `last_updated`; the CRO's G4 spec says the gateway read is implicitDeny. The tool is `OG-ac-2` (a worker building now).
- Pre-cut: ap25.AC1 and ap25.AC2 base FAIL as expected (tf, plan, ask and ledger absent).

<status>staged</status>
<round>37</round>
<workstream>CLASS-INCREMENT-2</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
