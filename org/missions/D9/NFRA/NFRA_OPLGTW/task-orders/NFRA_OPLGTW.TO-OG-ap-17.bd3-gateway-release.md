# NFRA_OPLGTW task order -- `OG-ap-17` -- APPLY: OG-bd-3's gateway release (master_admin tier survives a profile), behind the r30 release

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-17</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-17</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- the gateway queue is OG-ap-14 (r30, B2 GO from 11:00Z) then THIS; NFRA_MCPINDEX MX-r-12 may precede r30 (closes by 10:00Z or follows). Phase A starts only after OG-ap-14's ledger nfra-oplgtw-gateway-release-r30 is CLOSED. Window 11:00Z-23:00Z. No cron, alarm or monitor is created.
comp-iam: RUN-BY-ISSUER -- OG-bd-3's code makes no AWS or Graph call: decide() is in-process and the tier read is app/tier.py resolve_tier over the deploy-time rosters (no call). No role, policy or consent changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's ruling msg 33941 (route (a): "r30, then this release, then OG-mg-1 Phase B"); the cell is OG-bd-3, drained @42f31eea0a.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM reads of the gateway host).
</preflight>

## 1. THE CELL -- `OG-ap-17` (decomposition addendum R3-T.49 A3)

Ship OG-bd-3 to the gateway host, and nothing else. In `app/data_entitlement.py` `decide()`, a `TIER_ADMITTED_TOOLS`
member (`blackdiamond_list_fees`) passes for tier `master_admin` on the PROFILED branch too, whatever the profile's
state. `tool_denial` and `visible_tools` read the tier for restricted callers. Its commits on box/sitez:
- `fffac3b499` (code + `tests/test_og_bd3.py`);
- `486b643b97` (the re-pinned `tests/test_og_bd2.py` assertion).

Take only their `infra/aws/ec2/opal-gateway/` hunks.

### PHASE A (after OG-ap-14's ledger is CLOSED) -- re-cut, prove, ask. NO deploy

1. **Live ref:** EC2_MANIFEST `deployed_commit` at HEAD (r30's release by then), plus ONE SSM md5 read of the host
   over `app/`, `deploy/` and `dashboard/`. A mismatch is a STOP. Confirm ONE gateway release in flight across all
   worktrees, with the per-tree denominator printed.
2. **Re-cut** `rel-nfra-oplgtw-bd3` at the live ref in `C:/tmp/og-rel-bd3`: cherry-pick the two commits, gateway
   paths only, restoring every other path. Use the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the
   release commit only. Write `W/ap17_release.json` = `{"base_sha", "release_sha"}`. Run `tests/test_og_bd3.py`,
   `tests/test_og_bd2.py`, `tests/test_data_entitlement_family.py` and `tests/test_data_entitlement_guard.py`; a
   failure that also fails at the live ref is named pre-existing. Then AC1.
3. **The ask** `W/NEVER_WIDEN_ASK_OG-ap-17.md`, for `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~O`. It carries:
   - the diff by file;
   - **who gains:** a profiled master_admin regains the tier tool. Name the live principals from the grant store,
     with the denominator printed; ids only. Today no master_admin holds a profile, so it is inert until OG-mg-1
     writes Andrew's;
   - **who loses:** no one;
   - the triggers: tools by name unchanged; `.env` names unchanged; md5 = release;
   - rollback: redeploy the live base.

   Commit, REPORT, STOP.

### PHASE B (on the issuer's GO naming both halves at `release_sha`)

4. Ledger `nfra-oplgtw-gateway-release-bd3`, entry AND sentinel first. Deploy through
   `infra/aws/ec2/safe-ec2-deploy.sh` with `DEPLOY_BASE_REF=<base_sha>`; the release cone carries `lib/`, `.tools/`,
   `org/modules/graph/`, `data/transcripts/scripts/teams/` and your agent home. Read back against the triggers; on
   any trigger, redeploy the base and file an ARMED row naming `2.0.0_SA_COO~O`.
5. **The served read:** one SSM read through the INSTALLED code, in-process, with synthetic principals and no grant
   written. Write `W/AP17_SERVED.json` = `{"body": {...}, "ssm_command_id", "instance_id"}` with these body fields:

   | field | value |
   |---|---|
   | `installed_code` | `true` |
   | `bd_profiled_master_admin_admitted` | `decide()` on `blackdiamond_list_fees`, an active restricted profile whose grant lacks it, tier `master_admin`, returns None |
   | `bd_profiled_standard_denied` | the same at tier `standard` is denied |
   | `bd_unprofiled_master_admin_admitted` | no profile, `master_admin`: None |
   | `bd_unprofiled_standard_denied` | no profile, `standard`: denied |
   | `objects_written` | `0` |
6. **Standing clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and
   `file_checksums` come from the release blobs. Close the ledger, commit, run AC2, and report once to
   `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- OG-bd-3's gateway hunks only. No grant, profile, policy or Terraform act.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare
  `terraform`; print an `.env` value; override a gate other than the one audited lane escape in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-bd3.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after Phase A, AC2 after Phase B's ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-17"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap17.AC1.sh; echo "exit=$?"</invocation><expect>(?s)is the live ref: yes.*outside OG-bd-3's files 0 \(want 0\).*diff lines outside OG-bd-3's hunks 0 \(want 0\); cell markers present 2 of 2.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-17"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap17.AC2.sh; echo "exit=$?"</invocation><expect>(?s)entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*landed=(?:current; rb\.AC2 PASS|superseded; rb\.AC2 skipped \(superseded\)); served bd-3 fields: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the re-cut carries exactly OG-bd-3 on the live ref. `AC2`: landed, closed, recorded, and the rule is served on
  all four arms.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-17.bd3-gateway-release.proof_of_spec.json`, validate it after your
last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip
the ONE `<status>` tag to `complete` only if both PASS. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- CTO ruling msg 33941: r30, then this release, then OG-mg-1 Phase B. After this release lands, OG-mg-1's halves
  re-sign on this base; the COO half's refusal @e4beda9641 is lifted by it.
- Pre-cut:
  - ap17.AC1 base FAIL as expected (record absent). Its arm (base `fffac3b499~1` -> `486b643b97`) read 0 gateway lines
    outside OG-bd-3's hunks and markers 2 of 2. Only non-gateway files sat outside, as a dev commit range carries.
  - ap17.AC2 base FAIL as expected (records absent).

- A1 (issuer, 2026-10-14 ~05:0xZ, from row Z-S105 on OG-ap-14): **deploy-source guard.** Before the first deploy
  command, the deploy tree's `git rev-parse HEAD` must equal the signed `release_sha` in full, and its parent must equal
  live `deployed_commit` at the act. Any mismatch is a STOP; print both. If the live base moved since the cut, re-cut,
  and both halves re-sign. Never deploy from a worktree named for an earlier cut.
  Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A2 (issuer, 2026-10-14 ~12:1xZ, Andrew-direct "accelerate this use case", FWD-21; record
  `deliverables/2.0.0_SA_COO~O/ANDREW_DIRECT_20261014_121xZ_ACCELERATE_FWD21_HARVEST.md`): **this release follows
  OG-hv-2.**
  - PHASE A starts only after OG-hv-2's ledger `nfra-oplgtw-gateway-release-hv` reads CLOSED at HEAD.
  - The re-cut is at that live ref, under the A1 guard. Discard any Phase A cut made on 90967e39ba.
  - Steps, criteria and bounds are unchanged.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A3 (issuer, 2026-10-14 ~17:1xZ, row Z-S119): the release AC2 now grades the LANDING with a time anchor (`r37/checks/_landed.sh`): the manifest's deployed_commit is the release, or recorded it
  before a later release displaced it; runbook 7.2 (rb.AC2) is graded only while this release is the live one. "deployed_commit equals release_sha" flips to FAIL on work graded PASS the
  moment the next release lands, so it is no longer a criterion. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>R37-TIER-REL</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
