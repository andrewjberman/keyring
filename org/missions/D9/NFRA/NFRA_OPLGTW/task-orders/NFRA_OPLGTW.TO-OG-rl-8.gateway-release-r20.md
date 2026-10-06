# NFRA_OPLGTW task order -- `OG-rl-8` -- the r20 release: OG-lg-1's /login tier admit and audit record on live cf4b036e62

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release is the CTO's round-19 analysis item 2 (R24).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, audit-bucket and access-state reads) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-rl-8` (decomposition addendum R3-T.13, item 2; CTO R24)

Handed only after `OG-lg-1` is drained to CLOUD. FOLLOW
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md` IN FULL: Phase A steps 1-8 with 7
and 7a, Phase B 9-12, and Phase D 13 (DRAIN-BACK).

- **Live:** `cf4b036e62b5074600086e1d670dc3c6bdab004f`.
- **Ledger:** `nfra-oplgtw-gateway-release-r20`.
- **The release set:** OG-lg-1's files, so that after the drain-back CLOUD equals live for the gateway tree.

**R24's release condition: THE ADMIT SET, read in Phase A.**
- Using OG-lg-1's `LG1_ADMIT_SET.md` method and the access state READ-ONLY, compute the `/login` admit set BEFORE
  (live: any non-blocked tenant identity) and AFTER (server-held plus Graph-tool tiers) over the CURRENT principal
  population.
- List, by digest, every principal admitted before and refused after.
- Any such principal that is NOT restricted BLOCKS: file a BLOCKING row and STOP before GO.

Write `RL8_LOGIN.json`:
- `{served_release, files_shipped:[...], admit_before:[...], admit_after:[...], lost_nonrestricted:[...]}`;
- `after: {nonrestricted, restricted, server_held, requests, audit_records}`, from synthetic principals through the
  deployed code, host-local;
- `grants_written: 0`.

## 2. BOUNDS

- No grant is created or changed. Never source `/opt/opal-gateway/.env`.
- Terraform, IAM, the ALB and the template are untouched. `safe-ec2-deploy.sh` is READ only.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; call a vendor. R13 (a) applies on the release branch only.
- PHASE B only on the issuer's GO, with CTO + COO + CVO halves SIGNED on the release sha.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r20.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W15-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the drain-back and ledger close are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r20/checks/rl8.AC1.sh; echo "exit=$?"</invocation><expect>(?s)host shipped files equal the release bytes: \d+ of \d+.*lost non-restricted 0: True.*non-restricted admitted: True.*restricted refused: True.*server-held admitted: True.*one audit record per request: True.*grants_written 0: True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-8"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r20/checks/rl8.AC2.sh; echo "exit=$?"</invocation><expect>(?s)sentinel at HEAD=no; deployed=\w+ descends from cf4b036e62=yes; gateway files differing live\.\.CLOUD after drain-back 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-rl-8.gateway-release-r20.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 20 (R3-T.13, item 2), after `OG-lg-1`. Halves: CTO + COO + CVO. Served output moves: `/login`'s admit set
  changes to the tier rule, and `/login` gains an audit record.
- Pre-cut: see the issuance commit.

<status>pending</status>
<round>20</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
