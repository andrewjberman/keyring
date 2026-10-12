# NFRA_OPLGTW task order -- `OG-ap-7` -- APPLY: the NFRA_CTLPLN CT-i-11 gateway release (`/hx/teams/*` channel-read routes), re-cut on the live ref

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-7</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-7</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- host queue: MX-r-10 CLOSED 14:22Z (COO~MI msg 33305), live ref c3af8687e4; THIS release is next and the only one in flight. B2 window 11:00Z-23:00Z. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE -- code only; no role, policy, bearer or secret changes. The Graph scopes the routes' token is requested with are LISTED in the ask (CHANNEL_READ_SCOPES_MEASURED.md); no consent is changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the laptop CTO's ruling on XB-20261011T030021Z-b98e, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_XB_B98E_CTLPLN_CT_I_11_RELEASE_BY_SITEZ_GATEWAY_ISSUER_20261011.md @de13ed0e00 + Addendum 1 @4f285abe22, and 1.0.0_SA_CTO~Z msgs 33138/33141/33147.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-7` (decomposition addendum R3-T.42)

NFRA_CTLPLN's CT-i-11 adds the gateway's channel-read routes `GET /hx/teams/teams`, `/hx/teams/teams/{id}/channels` and
the channel messages route. It is built as two commits, `863e37d1f9` and AMENDMENT 1 `4d722ff458`, touching
`app/teams_route.py`, `app/server.py` and `tests/test_teams_route.py`. It is on trunk, but the live gateway answers 404
(COMM_ASSIST row Z-S11). Read the ruling and its Addendum 1 first; they BIND. The code ships exactly as built.

### PHASE B1 (now): re-cut, prove, ask. NO deploy

1. **Live ref.** Read the host md5s through one SSM read (your `ap6_md5_host.py`, widened to `dashboard/`) and compare
   them with `c3af8687e44a1e641259b37f992033ae02cdce3d`'s shipped files. The host is a superset: name every extra. Any
   mismatch is a STOP.
2. **Re-cut.** Create a worktree `C:/tmp/og-rel-cti11` on a new branch `rel-nfra-oplgtw-cti11`, at `c3af8687e4`. Apply
   ONLY CT-i-11's gateway hunks: `git diff 863e37d1f9~1 4d722ff458 -- infra/aws/ec2/opal-gateway/ | git apply`; the
   issuer's dry-apply lands it clean, 3 files. Commit it with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL`,
   on this one commit only. Write `W/ap7_release.json` = `{"base_sha", "release_sha"}` (full shas), and run AC1.
   The release worktree's deploy wrapper needs `lib/` and `.tools/`. Row NFRA_MCPINDEX-Z-S99 records sparse-cone import
   failures in MX-r-10, so use a cone that carries them.
3. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-7.md`, for `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~O`. It carries:
   - the diff by file;
   - the blast radius: `/hx/teams/*` routes only;
   - the Graph scopes the token is requested with and which the new paths need
     (`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~39/CHANNEL_READ_SCOPES_MEASURED.md`). No
     consent change: a missing scope answers 403, not a widening;
   - both branches of a call;
   - triggers relative to the live base (tools unchanged, routes +3, `.env` names unchanged, md5 = release);
   - the rollback: redeploy `c3af8687e4`.

   Commit, REPORT, STOP.

### PHASE B2 (only on the issuer's GO, which names both halves signed at `release_sha`)

4. Ledger `nfra-oplgtw-gateway-release-cti11`: entry AND sentinel committed first. Deploy from `C:/tmp/og-rel-cti11`
   through `infra/aws/ec2/safe-ec2-deploy.sh`, with `DEPLOY_BASE_REF=c3af8687e44a1e641259b37f992033ae02cdce3d`. The
   halt gate's premise holds as in OG-ap-6. No `HALT_OVERRIDE`.
5. **Read back immediately.** If any trigger fires: redeploy the base, then file an ARMED row naming `2.0.0_SA_COO~O`.
6. **The served grade.** `GET /hx/teams/teams` on the served gateway answers 200 where it answered 404. Measure it the
   way the route is really called, and record the method: the COMM_ASSIST assistant's channel_poll, or a host-side call
   through the installed app with the same identity. Write `W/AP7_SERVED.json` = `{"status_before", "status_after",
   "method", "ssm_command_id" | "log_ref"}`.
7. **Standing release clauses** (CTO round-33 analysis):
   - update `infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md` section 7.2 to name the new live release;
   - record EC2_MANIFEST `deployed_commit` = `release_sha`, and its `file_checksums` from the release's blobs.

   Close the ledger, commit, run AC2, and report once to `2.0.0_SA_COO~O`.

## 2. BOUNDS

- CT-i-11's three files and nothing else; the bytes as built. A change to them is a call to the laptop CTO.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare
  `terraform`; override a gate other than the one audited lane escape in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-cti11.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The release commit lives on `rel-nfra-oplgtw-cti11`, never on box/sitez. `W` =
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free),
fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after B1, AC2 after B2's ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/ap7.AC1.sh; echo "exit=$?"</invocation><expect>(?s)is the live ref c3af8687e4: yes.*equal=yes.*outside CT-i-11's paths 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/ap7.AC2.sh; echo "exit=$?"</invocation><expect>(?s)entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*equal=yes; rb\.AC2 PASS; GET /hx/teams/teams after: 200.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the re-cut carries exactly CT-i-11 as built, on the live ref. `AC2`: landed, closed, recorded, and served 200.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-7.cti11-teams-routes-release.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip the ONE `<status>`
tag to `complete` only if both PASS. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 34. The gateway queue after MX-r-10 is ordered by CTO~Z msg 33141. Consent covers both commits (laptop
  Addendum 1 @4f285abe22).
- The never-widen pair is COO ~O + CTO~Z; the laptop ruling says no laptop half is owed.
- B2's runbook edit is sequenced after OG-br-1's merge: both edit runbook 7.2. The B2 GO is given only after that merge.
- On close, the issuer writes the pointer row in the NFRA_CTLPLN channel (ruling term 4).
- A1 (issuer, 2026-10-11 ~17:5xZ): **B2 GO, effective now, inside the 11:00Z-23:00Z window.** The GO names:
  - **both halves, signed at release `28ba9532b6`:** COO @bd6be1a027 and CTO @4f49f40bd0. Their conditions bind: a 403
    or 409 at the served grade is a finding, not a rollback; the release cone carries `data/transcripts/scripts/teams/`,
    `lib/`, `.tools/` and `org/modules/graph/`; the record clauses apply;
  - **OG-br-1 merged @625b54f616**, so runbook 7.2 now names live c3af8687e4, and B2 moves it to the release.
  Before step 4, confirm one release in flight: no other gateway ledger open in any worktree, with the per-tree
  denominator printed. The CTO's observation (row Z-S92, the teams bearer's group holders) is known and is not a
  trigger. Gate limb: GATE (viii) on the modified order (placeholders NONE).
- Pre-cut: ap7.AC1 and ap7.AC2 base FAIL as expected. Positive control: a synthetic re-cut on c3af8687e4 read AC1 PASS
  (patch-id 37fa4995232e, 3 files). Negative control: a trunk commit read FAIL. The control record was removed.

<status>complete</status>
<round>34</round>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
