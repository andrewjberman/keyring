# NFRA_OPLGTW task order -- `OG-tb-1` -- READ: who reads `gateway/teams/bearer` (CloudTrail 90 days), then the narrowing ask (round-35 E3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tb-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-tb-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~59</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- CloudTrail and IAM reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- this order changes no identity, role or policy; reading the secret's resource policy and the group's grant is the cell's own work (step 2), and the narrowing is a later applier order under a signed pair.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-34 analysis @026a983b34 row Z-S92 ruling (cell E3), on its own observation at OG-ap-7's CTO half (msg 33350).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (read APIs).
</preflight>

## 1. THE CELL -- `OG-tb-1` (decomposition addendum R3-T.44, E3)

The Teams bearer secret `gateway/teams/bearer` is readable by the gateway, COMM_ASSIST's Lambda,
`cloudops-dell-agents-group` and admin (row Z-S92). OG-ap-7 added three channel-read routes, so every holder of that
bearer can now read Teams channels. The group has no named consumer.

1. **CloudTrail**, management events for the full 90-day window: every `GetSecretValue` whose request names
   `gateway/teams/bearer` (by name or ARN). For each, record the principal ARN and its count. The positive control:
   the gateway's own role (`opal-gateway-role`) must appear as a reader. If it does not, the read is broken; say so and
   STOP.
2. **The grant path:** read how `cloudops-dell-agents-group` gets read (the secret's resource policy and the group's IAM
   policies) and name the exact statement. Then decide which principals in step 1 are the group's members:
   `dell_group_verdict` = "none" (no group member read it in 90 days) or "found" (name them).
3. Write `W/TB1_READ.json` = `{"window_days", "events_read", "principals": [{"arn", "count"}], "positive_control":
   {"gateway_role_seen"}, "dell_group_verdict", "grant_statement"}`. Use ARNs only, no person's name.
4. **The never-widen ask**, `W/NEVER_WIDEN_ASK_OG-tb-1.md`, for `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~O`, following the
   CTO's ruling:
   - **"none":** remove the group's read of this one secret (the exact statement change), with rollback;
   - **"found":** give that consumer its own bearer (the commassist pattern: a separate secret, its own grant), and then
     remove the group's read.

   Record each remaining holder's reason.
5. Run AC1, commit, REPORT, STOP.

## 2. BOUNDS

- READ ONLY. No secret value is read or printed, no policy is changed, no secret is created.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret or a person's name; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~59/`. Rows: id `NFRA_OPLGTW-Z-W59-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`. AWS goes through `bash .tools/aws`; paginate
every lookup and count client-side.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tb-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r35/checks/tb1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)GetSecretValue events read [1-9]\d*; .*gateway role seen True; dell group verdict (none|found).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the 90-day reader census is complete, positively controlled, and states the group verdict.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-tb-1.teams-bearer-holders-read.proof_of_spec.json`. Validate it AFTER
your LAST commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`; artifact
rows pin to the commit that carried them. The order stays `pending` (the narrowing is a later apply). Report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 35, E3. Pre-cut: tb1.AC1 base FAIL as expected (TB1_READ.json absent).

<status>pending</status>
<round>35</round>
<slot>~59</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
