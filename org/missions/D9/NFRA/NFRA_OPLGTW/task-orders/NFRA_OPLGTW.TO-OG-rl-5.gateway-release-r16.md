# NFRA_OPLGTW task order -- `OG-rl-5` -- the gateway release carrying R9's grain on live af2d762970

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release is the CTO's round-15 analysis item 2 (R9).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, Secrets Manager reads) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-rl-5` (decomposition addendum R3-T.9, item 2)

Handed only after `OG-gr-3` is drained to CLOUD. Pattern: your `ANNOUNCE_OG-rl-4.md` for every step (release tree,
rollback tree, verify script, deploy). STANDING RULE (row Z-S32): never source `/opt/opal-gateway/.env`.

### PHASE A (pre-GO): read-only on the host; no upload

1. **Live ref.** Confirm `af2d7629702528c050860314a7867d8ea0cecfbf` by host md5 (a mismatch STOPS).
   - Release tree `/c/tmp/og-rel10`, branch `rel-nfra-oplgtw-r16`, at that commit. Take `OG-gr-3`'s three files from its
     drained head on CLOUD; the two app files were byte-equal on CLOUD and live at the cut.
   - Census against live: exactly those three files. The template is untouched.
2. **Tests** on the release tree: `test_schwab_grain_r9.py`, `test_schwab_semantics.py`, `test_schwab_query.py`,
   `test_entitlement_admin.py::test_ogz2_ac08`.
3. **Rollback** `/c/tmp/og-rb10` at `af2d762970`, equal file by file to the live S3 artifact.
4. **The paging measurement, BEFORE** (it is the control). On the host, through the installed engine and its venv, run
   one rows-mode page of `dim_position` and one of `dim_asset` on ONE qualified snapshot, the newest the measured basis
   covers:
   - Use a SYNTHETIC principal and a SYNTHETIC grant, the OG-r-4 / `onhost_bench.py` mechanism. NEVER an existing
     person's identity, NEVER a grant written to the state store.
   - Record each outcome (`OK` with row count, or `REFUSED <code>`).
   - Expected today: `dim_position` REFUSED (grain collision).
   - Remove every host scratch copy.
5. **Verify script** written now: host `/health` 200; shipped md5 = release bytes; tool list unchanged; `.env` 50 key
   names unchanged; then the paging AFTER run (step 4 again), `rl4.AC1.sh` and `ht.AC2.sh`.
6. `ANNOUNCE_OG-rl-5.md`; commit; report. Do NOT upload.

### PHASE B (GO): only after the issuer says GO (CTO + COO + CVO halves SIGNED: paging becomes available where it refused)

7. Re-read live; if it moved, re-cut. Open NEVER-2 ledger `nfra-oplgtw-gateway-release-r16` (legs: upload, install +
   verify, manifest, rollback-proven), with entry AND sentinel committed before the act.
8. Deploy from `/c/tmp/og-rel10` with `DEPLOY_BASE_REF=<live full sha> HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~15`
   through `infra/aws/ec2/safe-ec2-deploy.sh`. The template reads the Tax identity host-side since OG-rl-4, so nothing is
   exported.
9. Run the verify script IMMEDIATELY. Write `RL5_PAGING.json` with these keys:
   - `served_release`;
   - `before {dim_position, dim_asset}` and `after {dim_position, dim_asset}`;
   - `synthetic_principal: true`, `grants_written: 0`, `state_store_written: false`.
   Any failure: roll back, re-verify, close ROLLED BACK.
10. Record `EC2_MANIFEST.json` by hand. Close every leg with proof. Run section 4. Write the proof. Edit this order's ONE
    `<status>` tag IN PLACE to `complete`. Commit.

## 2. BOUNDS

- No grant is created or changed (CTO G1, B2; CVO W1).
- The served read by the REAL grant holder is not exercised here. It is her act, at her next use.
- Terraform, IAM, the ALB and the template are untouched. `safe-ec2-deploy.sh` is READ only.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r16.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W15-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r16/checks/rl5.AC1.sh; echo "exit=$?"</invocation><expect>(?s)host query.py \+ datasets.json equal the release bytes: yes.*dim_position after ok: True.*dim_asset after ok: True.*dim_position before refused: True.*synthetic principal: True.*grants_written 0: True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r16/checks/rl5.AC2.sh; echo "exit=$?"</invocation><expect>(?s)sentinel at HEAD=no;.*descends from af2d762970=yes;.*outside the release set 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-rl-5.gateway-release-r16.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 16 (addendum R3-T.9, item 2), after `OG-gr-3`. Halves: CTO + COO + CVO.
- **Deviation from the CTO's acceptance wording, named:** "a rows-mode page ... for an EXISTING grant holder" cannot be
  measured by an agent.
  - The holder's read is her act, and no agent reads as another person.
  - Andrew's own session holds no Schwab grant: his gateway lists no `schwab_*` tool.
  - AC1 therefore measures the same served engine with a SYNTHETIC principal and grant, as OG-r-4 was accepted. The real
    holder's read is UNEXERCISED until her next use, as the /hx/teams POST verbs were until Andrew's EOD post.
- Pre-cut 22:1xZ: `rl5.AC1` FAIL (record absent; host bytes equal live); `rl5.AC2` FAIL (no ledger); floor rl4.AC1 and
  ht.AC2 PASS today.

<status>pending</status>
<round>16</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
