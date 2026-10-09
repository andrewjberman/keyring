# NFRA_OPLGTW task order -- `OG-ap-4` -- APPLY: the 4-meeting transcript allowlist release (OG-tl-1 Phase B)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-4</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-4</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- host queue (CTO~Z msg 32713): r29 (LIVE @5f1400c4a2) -> NFRA_MCPORTAL MP-x-4 -> THIS -> MX-r-9 (applier 0.7.0_AE_CloudOps~MX) -> E2 -> metadata route. One release in flight on the host; window 11:00Z-23:00Z. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE -- one .env value on the gateway host; no role, policy, bearer or secret changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the three signed halves over org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~48/NEVER_WIDEN_ASK_OG-tl-1.md (release 78afad4283): CTO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_OG-tl-1_20261009.md @033a840b3b, COO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-tl-1_20261009.md @167b7b8f1a, CVO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_OG-tl-1_20261009.md @b73aa5a7d9.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-4` (decomposition addendum R3-T.36)

Deploy the transcript allowlist: `TRANSCRIPT_MEETING_ALLOWLIST` becomes the 4 `online_meeting_id` values read from
`data/transcripts/scripts/teams/meeting_allowlist.json`. READ the ask and the three halves first; they BIND, the CTO
half's C1 and the COO half's re-cut condition especially.

0. **Start only after NFRA_MCPORTAL MP-x-4's deploy ledger is CLOSED and its read-back committed** (`2.0.0_SA_COO~O`
   names that commit in the GO). If MP-x-4 has not deployed, do not start.
1. **Re-cut on the LIVE ref** (EC2_MANIFEST `deployed_commit` at HEAD, cross-read by host md5): a new worktree at that
   ref, then replay ONLY the allowlist hunk of `78afad4283` (the json read block, the count-4 refusal, one `%s` and its
   argument in the `.env` printf) and the json if the ref lacks it. The COO half covers the re-cut only when `git
   patch-id` of the deploy-script hunk equals that of `4514246d65..78afad4283` and the json blob is `d57e815a7c`; any
   other difference is a STOP and a fresh ask. Commit it on a new branch `rel-nfra-oplgtw-tl1b` (audited
   `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on that one commit, as OG-tl-1 A1 ruled; nothing else uses it). Write
   `W/ap4_release.json` = `{"base_sha", "release_sha"}`.
2. **Ledger** `nfra-oplgtw-og-tl-1-allowlist`, entry AND sentinel committed before the act.
3. **Deploy** from that worktree through `infra/aws/ec2/safe-ec2-deploy.sh` with `DEPLOY_BASE_REF=<live ref>`, the
   halt gate's premise made true as OG-ap-3 A3 did (sparse cone includes your agent home); no `HALT_OVERRIDE`.
4. **Read back immediately:** `ENV_KEYS_BEFORE` == `ENV_KEYS_AFTER` (CTO C1: a missing key is a STOP and rollback); the
   only `.env` value hash that moved is `TRANSCRIPT_MEETING_ALLOWLIST`; `/health` 200; tool count unchanged; shipped
   files' md5 equal the release. Any trigger: redeploy the base with `DEPLOY_BASE_REF=<release sha>`, ARMED row naming
   `2.0.0_SA_COO~O`. A Research Team Meeting Graph 403 is NOT a trigger.
5. Record the manifest by hand, close the ledger and commit, then AC1. Report once to `2.0.0_SA_COO~O`. You do not run
   the served read: OG-tl-1's worker does (Phase C), and dell2's re-probe is the CVO's AC3.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- One `.env` value, one restart. No code beyond the allowlist hunk, no bearer, route, IAM or other env change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-tl-1-allowlist.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-AE-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from the repo root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ap4.AC1.sh; echo "exit=$?"</invocation><expect>(?s)nfra-oplgtw-og-tl-1-allowlist: entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*equal=yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the act is not half-landed, and the host runs the release this order cut. The served allowlist is OG-tl-1's AC2.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-4.transcript-allowlist-apply.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance>`, and flip the ONE `<status>` tag to `complete` only if AC1 PASSES.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Workstream APPLY-TL1, round 33. Cut on the third half (CVO~Z @b73aa5a7d9); held until MP-x-4's ledger closes (the GO
  names it).
- Pre-cut: ap4.AC1 base FAIL as expected (0 entries; ap4_release.json absent; manifest reads r29 91811b648a).

<status>staged</status>
<round>33</round>
<workstream>APPLY-TL1</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
