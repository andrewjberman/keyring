# NFRA_OPLGTW task order -- `OG-ap-3` -- APPLY: the r29 gateway release (OG-rl-15 Phase B), its commassist secret and one policy line

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-3</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- the gateway host has no scheduled consumer of the release; the 08403355 pull (10:45Z) and the other two daily pulls run on the SI2 box, not the gateway. Window: 11:00Z-23:00Z only (ANNOUNCE Half 2). No cron, alarm, monitor or notification is created.
comp-iam: RUN -- live `iam get-role-policy opal-gateway-role gateway-read-secrets-policy` at the cut: 1 statement, 4 resources; the act adds exactly one ARN (gateway/mail/commassist-bearer), Terraform line 98501422dc, plan expected 0 add / 1 change / 0 destroy.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the three signed never-widen halves over the ANNOUNCE org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~43/ANNOUNCE_OG-rl-15.md @368e48e533 (release sha 91811b648a): CTO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~O/NEVER_WIDEN_HALF_CTO_OG-rl-15_r29_20261009.md @d3f04813df, COO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-rl-15_r29_20261009.md @40b39ad88d, CVO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_OG-rl-15_r29_20261009.md @c348b51df9.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-3` (decomposition addendum R3-T.33; OG-rl-15 Phase B)

Deploy gateway release r29 (sha `91811b648ab119e73e22f8d401dd09f45b8ab19b`, worktree `C:/tmp/og-rel29`) over live r28
(`aa75078e1b72a28219e6148d3ec8e9bf705ea111`; rollback worktree `C:/tmp/og-rb29`, equal 97 of 97 to the live artifact).
READ the ANNOUNCE sections 10 and 13 (Half 2) and the three halves first. **The halves BIND**; Half 2's act list is the
procedure, in its order. Tooling is in `T` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~43/`
(`r29_ssm_prog.py`, `r29_md5_host.py`, `r29_verify.py`, `r29_bun_cache_size.py`, `r29_bun_cache_count.py`).

1. **The secret.** Create `gateway/mail/commassist-bearer` out-of-band, a random 32-byte hex value. The value never
   enters a file, a message, a log, TF state or a commit. Record ONLY its name and the version id the create returns.
2. **The policy line, its own ledger.** Open `nfra-oplgtw-r29-commassist-secret-grant` (`python .tools/deploy_ledger.py
   open ...`), entry AND sentinel committed. In `infra/aws/terraform/opal-gateway/`: `terraform plan -target` on
   `aws_iam_role_policy.gw_gateway_read_secrets` (and the new data source) -- expect 0 add, 1 change, 0 destroy, the
   policy only; any other row is a STOP. Apply the saved plan through `bash .tools/safe-apply.sh`. Read the policy back
   (5 resources). Close the ledger and commit.
3. **The deploy, its own ledger** `nfra-oplgtw-gateway-release-r29`, entry AND sentinel committed BEFORE the act. Then
   Half 2's steps (3)-(8) exactly: re-read live by host md5 (a live sha other than r28 = STOP, report); `r29_verify.py
   before`, `r29_bun_cache_size.py before`, record `deploy_started_utc`; dry-run the halt gate
   (`halt_gate_resolve_serial`, `halt_gate_validate_serial`, rc 0); from `C:/tmp/og-rel29`, `unset OPAL_AGENT_SERIAL`,
   `DEPLOY_BASE_REF=aa75078e1b72a28219e6148d3ec8e9bf705ea111 HALT_ACK=1 AGENT_NAME=0.7.0_AE_CloudOps~Z bash
   infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`; IMMEDIATELY
   `r29_verify.py after <state> --expect-changed MAIL_BEARER,MAIL_BEARER_LABELS`, `r29_bun_cache_size.py after`,
   `r29_bun_cache_count.py <deploy_started_utc> <out>` (the count must be **0**).
4. **Rollback triggers (Half 2):** bun-cache count above 0; tools off 66; consent off 9; `/health` off 200; md5 not
   98/98; a `.env` value hash changed that is not in `--expect-changed`. On any: redeploy `aa75078e1b` from
   `C:/tmp/og-rb29` with `DEPLOY_BASE_REF=91811b648ab119e73e22f8d401dd09f45b8ab19b`, file an ARMED row naming
   `2.0.0_SA_COO~O`, and report. A revoked concierge refresh family is NOT a rollback trigger: report it the same hour.
5. Record the deploy manifest entry by hand (the wrapper's own manifest commit is refused by the lane gate, expected;
   `release_note` holds r29's note alone). Close the ledger and commit, then run the criteria.
6. **Report once to `2.0.0_SA_COO~O`**: the secret's NAME and VERSION ID (never the value), both ledger closes, the
   verify after line, the bun-cache count, MainPID before/after. The issuer then continues the release worker for Phase
   C (the served read and the 13-month grant); you do not write any grant.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- The gateway host (one restart), one new secret, one policy line. No grant write, no other secret, role, Lambda or
  `.env` key value beyond `MAIL_BEARER`, `MAIL_BEARER_LABELS` and the new `MAIL_SENDER_DOMAIN_TABLE`.
- `gateway/mail/bearer` AWSCURRENT is never written.
- Window 11:00Z-23:00Z. Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-r29-commassist-secret-grant.json
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r29.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-AE-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from the repo root after both ledger closes are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ap3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)describe rc=0 arn_present=yes.*resources 5 \(want 5\); naming the new secret 1 \(want 1\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ap3.AC2.sh; echo "exit=$?"</invocation><expect>(?s)nfra-oplgtw-r29-commassist-secret-grant: entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*nfra-oplgtw-gateway-release-r29: entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the secret exists and the host role may read exactly one more secret.
- `AC2`: neither act is left half-landed. The served behaviour is graded by OG-rl-15's AC1-AC3 in Phase C.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-3.gateway-release-r29-apply.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance>`, and flip the ONE `<status>` tag to `complete` only if both PASS.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32, workstream APPLY-R29: OG-rl-15's Phase B, the deploy actor per msg 32057. Cut on the third half
  (CVO~Z @c348b51df9, 2026-10-09 ~07:5xZ); Phase A drained @76ff10095c.
- Owed onward: the secret's name + version id to laptop `2.0.0_SA_COO~R` via `0.0.0_AB_MSTR~Z` (COMM_ASSIST CA-m-1).
- CVO carried item (not a condition): PRD C7 `:694` "the bearer's one holder" -- the CTO's to addend.
- Pre-cut: ap3.AC1 base FAIL as expected (secret absent, rc 254; policy 4 resources); ap3.AC2 base FAIL as expected
  (0 entries per slug); AC2's ledger reader positive control on `nfra-oplgtw-og-bf-1-y-dispatcher-gate`: CLOSED=yes, PASS.

<status>pending</status>
<round>32</round>
<workstream>APPLY-R29</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
