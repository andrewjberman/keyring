# NFRA_OPLGTW task order -- `OG-ap-26` -- APPLY (grant move): the etf-classifications read leaves the gateway instance role and lands on the internal reader role (OG-ap-23 Phase A, gap 2, `~Z` msg 34753)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-26</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-26</to_id>
<issued_to>0.7.0_AE_CloudOps~ZS</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; the applier still runs `comp-schedule --drift` at the act and records what it scanned.
comp-iam: RUN-BY-ISSUER at the cut (`comp-iam stats` 2026-10-16 ~06:3xZ: 222 IAM roles parsed, 197 services, 1175 operations, 345 permission gaps estate-wide; it is a DESIRED-plane lens over Terraform and cannot see a live-only policy, so the live roles are read by the applier in Phase A step 1): ONE policy changes role, same statement (Allow, `dynamodb:GetItem`, the table ARN of `etf-classifications`). It leaves `opal-gateway-role` (the instance role) and lands on `gateway-global-internal-reader-role`. Net: the instance role LOSES a grant, the internal reader gains one; nothing else on either role moves.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act corrects my own placement in OG-ap-25 under the standing direction that Opal-internal data reads through the internal reader role (OG-ap-21 moved those statements OFF the instance role): the module `app/mdpf_classification.py` takes its DynamoDB client from `internal_role.dynamodb_client()` when `INTERNAL_READER_ROLE_ARN` is set, and an assumed-role session holds only the assumed role's policies (the `OG-ap-23` applier measured the policy absent on the internal reader, ask section 0 gap 2).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-26` (decomposition addendum R3-T.86, workstream CLASS-INCREMENT-3, FWD-22)

`OG-ap-25` (complete, applied at `3ba4af364d`) put `gateway-global-etf-classification-read-policy` on the instance role. The tool that uses it reads as the internal reader role. Move the policy: same name, same statement, other role.

### PHASE A (files, plan, ask; NO apply IN ANY FORM)

1. **Read the live state first.** `get-role-policy` for the policy on `opal-gateway-role` (its document hash, so the rollback is exact), `list-role-policies` for `gateway-global-internal-reader-role` (the policy must be absent there), `describe-table` for `etf-classifications`. Write `W/CLS2_BEFORE.json`.
2. **Edit the Terraform** `infra/aws/terraform/opal-gateway/etf_classification_read_iam.tf` (the file `OG-ap-25` wrote): the `aws_iam_role_policy` `role` becomes the internal reader role resource (read how `queryv0-iam.tf`'s siblings and the OG-ap-21 files address `gateway-global-internal-reader-role`, for example `aws_iam_role.int_reader`; copy the form). Keep the policy name, the Sid, the single statement and the table ARN byte for byte; change nothing else. Update the file's header comment to say the grant is on the internal reader role and why (one line).
3. **The plan**, targeted at that one resource, `-lock=false`, no `-out`, no apply: it must read `1 to add, 0 to change, 1 to destroy` (a replacement: the role is a force-new attribute). Save it as `W/CLS2_PLAN.txt`. Any other change is a STOP.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-26.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word (CTO, COO, CVO): (1) the `diff` (the one file, the role line); (2) the `widening`, stated plainly: the internal reader role gains `dynamodb:GetItem` on ONE table; the instance role LOSES it; the data is Opal-internal market data; (3) the `tool` (`mdpf_get_security_classification`, Opal principals only, refuses before any read); (4) the `order` of acts (one targeted apply that replaces the policy; both ends read back from IAM; BEFORE the code release `OG-ap-23`); (5) `both branches`; (6) the `rollback` (re-point the `role` line back to `aws_iam_role.gw` and replace; the prior document hash is in `CLS2_BEFORE.json`); (7) the `triggers`. Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at the `.tf` hash)

5. Ledger `nfra-oplgtw-grants-ap26`, entry AND sentinel first. Apply the replacement through `safe-apply`, targeted. Read back: the policy is on `gateway-global-internal-reader-role` (one statement, `dynamodb:GetItem` only, the table ARN) and ABSENT on `opal-gateway-role`; `simulate-principal-policy`, ONE resource per call: internal reader GetItem allowed, internal reader Scan not allowed (negative control), instance role GetItem not allowed; a `*`-principal positive control beside any deny read; `describe-table` of the exact table. Re-plan the target: `No changes`. On a trigger failing, restore the prior state and file an ARMED row naming `2.0.0_SA_COO~O`. Close the ledger, write `W/CLS2_APPLIED.json` = `{"policy_name": "<name>", "table_arn": "<arn>", "policy_sha256_16": "<sha>", "applied_at": "<iso>"}`, commit, run AC2, report once.

## 2. BOUNDS

- IAM and Terraform of the one named policy only. No item read or written; no deploy; no other role or policy touched.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply` (use `safe-apply`); apply in Phase A in ANY form; print an account number or a table item.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/etf_classification_read_iam.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-grants-ap26.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free; a correction is a NEW row citing the old id), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-26"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap26.AC1.sh; echo "exit=$?"</invocation><expect>(?s)terraform: policies 1 \(want 1\); role is the internal reader True \(role expr \S+\); dynamodb actions \['dynamodb:GetItem'\]; table arn ok True; wildcard False \(want False\).*plan: 1 to add, 0 to change, 1 to destroy True; ask has the three halves True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-26"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap26.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; internal reader holds policy \S+ shape ok; instance role still holds it 0 \(want 0\); simulate internal reader GetItem allowed, Scan (?:implicitDeny|explicitDeny) \(negative control\); instance role GetItem (?:implicitDeny|explicitDeny).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the one `.tf` file puts the policy on the internal reader role, GetItem only on the table ARN, and the plan is a one-for-one replacement. `AC2`: the policy is live on the internal reader role, gone from the instance role, GetItem allowed and Scan not allowed by the simulator, and the ledger is closed.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-26.etf-classifications-grant-to-internal-reader.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream CLASS-INCREMENT-3 (decomposition addendum R3-T.86). The placement error is mine: my OG-ac-2 order told the worker to prefer the internal reader role's client, and my OG-ap-25 order named the instance role. The direction (OG-ap-21) is Opal-internal data through the internal reader role, so the grant moves; the alternative (point the module at the instance role) would widen the instance role's standing surface.
- The Phase A GO is the issuer's message. OG-ap-23's Phase B waits on this cell closing (its precondition becomes `ap26.AC2` PASS).
- Pre-cut: ap26.AC1 and ap26.AC2 base FAIL as expected (plan, ask and CLS2_APPLIED.json absent).

<status>pending</status>
<round>37</round>
<workstream>CLASS-INCREMENT-3</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
