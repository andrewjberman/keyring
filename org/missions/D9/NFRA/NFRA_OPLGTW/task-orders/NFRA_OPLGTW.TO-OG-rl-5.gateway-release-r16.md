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
   - Release tree `/c/tmp/og-rel10`, branch `rel-nfra-oplgtw-r16`, at that commit. From `OG-gr-3`'s drained head on CLOUD
     take `query.py`, `datasets.json` and the `tests/test_schwab_*.py` files it changed WHOLE (byte-equal on CLOUD and
     live before gr-3).
   - **`integration.py` (A2, R9a): merge ONLY gr-3's hunks onto the LIVE bytes.** CLOUD's copy differs from live by one
     line, the live `aws_roles.environ_with_external_ids(...)` call, which MUST stay. Prove it:
     `git diff af2d762970 -- integration.py` on the release equals gr-3's own diff of that file.
   - Census against live: those files only. The template is untouched.
2. **Tests** on the release tree: `test_schwab_grain_r9.py` (5 named), `test_schwab_semantics.py`, `test_schwab_query.py` (incl. `test_ogq2_ac20` restated), `test_schwab_transactions.py`,
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
4b. **Grain-column census (A1, issuer, before the cut is handed).** Run this read-only. For EVERY snapshot the gateway can
    serve for `dim_position` and `dim_asset` (every closure-marker-qualified date, both masters; print the
    denominator), confirm the R9 grain columns exist and are never blank:
    - `dim_position`: `quantity_settled_unsettled` and `quantity_cash_settled`;
    - `dim_asset`: `security_description_line_1`.
    A servable snapshot that lacks a column would REFUSE paging after the release where it may have served before. So
    any such snapshot STOPS the order with a BLOCKING row naming it.
4c. **AMENDMENT A3 (CTO ruling R12, `ledger/ROUND_ANALYSIS.round15.md` section 8 @261571c07e; rows Z-W15-S33, S34).**
    Steps 1-4 stand as measured @18a741f858 (PAGING BEFORE: `dim_position` REFUSED `INCOMPLETE_SNAPSHOT
    snapshot_incomplete`, `dim_asset` REFUSED `UNAVAILABLE asset_policy_selection_unavailable`; record those as the
    `before` values). The release widens to three changes, and nothing else:
    - **Contract, whole.** The release tree's `infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json` AND its
      `org/standards/NFRA_OPLGTW_CONTRACT.json` become byte copies of CLOUD's
      `org/standards/NFRA_OPLGTW_CONTRACT.json` at 261571c07e (live plus the two `silver/dim_transaction/` prefixes).
      Prove: `git diff af2d762970 -- <both paths>` shows exactly those two added strings.
    - **S34, in YOUR worktree first (CLOUD source):** delete `integration.py` lines 569-570 only (the query path's
      `if q.dataset == "dim_asset" and self._asset_policy is None: raise ServiceError(UNAVAILABLE, ...)`). The lines at
      ~818-819 (`prepare_download`) and ~895-896 (`export_query`), `build_default_service()` and the `asset_policy`
      parameter stay byte-identical. Add `tests/test_schwab_rl5_asset_query.py`, built through `build_default_service()`'s
      construction (no `asset_policy` seam): (i) a `dim_asset` rows query on a qualified snapshot returns only CUSIPs
      held by the grant's accounts, and a planted UNHELD CUSIP is absent; (ii) `dim_asset` `prepare_download` still
      refuses `asset_policy_selection_unavailable`. Run the full `tests/test_schwab_*.py` set: no failure beyond those
      already failing at CLOUD HEAD (print both lists). Commit in your worktree.
    - **Release tree:** carry the same two-line deletion and the new test onto `/c/tmp/og-rel10` (live bytes + gr-3
      hunks + this deletion); re-run step 2's tests plus the new file there.
    - **Census, step 4b re-run** with the RELEASE contract (in-memory on the host, as SSM 02bc6129 did): print the
      denominator per master; it must read servable snapshots at both masters with 0 lacking or blank. A zero denominator
      STOPS again.
    - **Paging BEFORE for the asset check:** none further; the after run (step 5) also runs a `dim_asset` rows page by the
      synthetic principal, compares each returned CUSIP to the CUSIPs of that grant's accounts in `dim_position` for the
      same master/date (`dim_asset_held_check {returned, unheld_returned}`), and a `dim_asset` `prepare_download`
      (`after_dim_asset_download`, expected REFUSED `asset_policy_selection_unavailable`).
5. **Verify script** written now: host `/health` 200; shipped md5 = release bytes (incl. the deploy contract); tool list
   unchanged; `.env` 50 key names unchanged; then the AFTER run: the paging page of step 4, the served census
   (`census_after {servable_by_master, lacking_or_blank}`), the asset held-check and the download control of 4c; then
   `rl4.AC1.sh` and `ht.AC2.sh`.
6. `ANNOUNCE_OG-rl-5.md`; commit; report. Do NOT upload.

### PHASE B (GO): only after the issuer says GO (CTO + COO + CVO halves SIGNED: paging becomes available where it refused)

7. Re-read live; if it moved, re-cut. **A4 (CTO half C1 @75d651b7f4):** print the count of live grants naming
   `dim_transaction` and the count naming `dim_balance` (state-store READ only). Open NEVER-2 ledger `nfra-oplgtw-gateway-release-r16` (legs: upload, install +
   verify, manifest, rollback-proven), with entry AND sentinel committed before the act.
8. Deploy from `/c/tmp/og-rel10` with `DEPLOY_BASE_REF=<live full sha> HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~15`
   through `infra/aws/ec2/safe-ec2-deploy.sh`. The template reads the Tax identity host-side since OG-rl-4, so nothing is
   exported.
9. Run the verify script IMMEDIATELY. Write `RL5_PAGING.json` with these keys:
   - `served_release`;
   - `before {dim_position, dim_asset}` and `after {dim_position, dim_asset}`;
   - `census_after {servable_by_master, lacking_or_blank}`, `dim_asset_held_check {returned, unheld_returned}`,
     `after_dim_asset_download` (A3);
   - `dim_asset_held_check` also carries `held_cusips_in_dim_position` and `asset_universe_cusips` (the distinct
     `dim_asset` CUSIPs of the same snapshot) (A5, CVO guard Q2 @d370d16fe3). `unheld_returned = 0` counts only when
     `returned > 0` AND `held_cusips_in_dim_position < asset_universe_cusips`; otherwise the held check is UNGRADED:
     re-run it with a principal whose grant names fewer accounts before closing;
   - `census_after_other {dim_balance, dim_transaction}` servable per master (A4, C1). Expected 14 each per master.
     ABOVE 14, or any read by a principal without a grant for that dataset: roll back at once. BELOW 14: a surprise
     row, not a rollback;
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
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/tests/test_schwab_rl5_asset_query.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r16.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W15-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r16/checks/rl5.AC1.sh; echo "exit=$?"</invocation><expect>(?s)host query.py \+ datasets.json \+ contract equal the release bytes: yes.*dim_position after ok: True.*dim_asset after ok: True.*dim_position before refused: True.*synthetic principal: True.*grants_written 0: True.*RESULT: PASS.*exit=0</expect></criterion>
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
- **A3 (2026-10-04 ~21:0xZ, issuer, on CTO R12 @261571c07e, msg 29230):** Phase A STOPPED at 4b @18a741f858 (drained
  68cb0083f2): the live contract lacked the `dim_transaction` data prefixes (S33) and the query path refused every
  `dim_asset` read (S34). Ruled (a): one widened release -- contract whole, the two-line `:569-570` deletion and its
  test, gr-3's hunks. `rl5.AC1` gains the contract md5, the served census after, the asset held-only check and the
  download control; `rl5.AC2`'s shipped set admits `deploy/NFRA_OPLGTW_CONTRACT.json`. Never-widen: the release moves
  served output (0 -> servable snapshots; `dim_asset` queries servable under the C3 holdings restriction); the CTO's
  Phase B half names that blast radius. No grant changes. S33 and S34 disarm on the post-act read.
- **A6 (2026-10-04 ~23:4xZ, issuer; row Z-W15-S38):** A3 changed `rl5.AC1.sh`'s first line to name the contract but
  left AC1's `<expect>` unamended, so the PASS output could not match. The issuer's defect: the expect now reads
  `... + contract equal ...`. Issuer re-grade at CLOUD b91a1a44cf against the served host: 11 of 11 arms, RESULT: PASS,
  exit=0. Release 4b6b823fae LIVE 23:12:32Z; ledger CLOSED; AC2 PASS (worker).
- Pre-cut 22:1xZ: `rl5.AC1` FAIL (record absent; host bytes equal live); `rl5.AC2` FAIL (no ledger); floor rl4.AC1 and
  ht.AC2 PASS today.

<status>complete</status>
<round>16</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
