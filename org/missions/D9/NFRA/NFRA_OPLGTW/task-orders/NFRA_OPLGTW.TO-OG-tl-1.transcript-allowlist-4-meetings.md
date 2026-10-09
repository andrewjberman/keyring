# NFRA_OPLGTW task order -- `OG-tl-1` -- env-only gateway release: the 4 NFRA_TRNSPT meetings onto TRANSCRIPT_MEETING_ALLOWLIST

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tl-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-tl-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~48</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- the gateway host queue is r29 (OG-ap-3, under way), then NFRA_MCPORTAL MP-x-4, then this cell's deploy (CTO~Z msg 32710, no veto). Window 11:00Z-23:00Z. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE -- one .env value on the gateway host; no role, policy, bearer or secret changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is `1.0.0_SA_CTO~Z`'s ruling org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~Z/CTO_RULING_HX_TRANSCRIPTS_HOST_ALLOWLIST_4_MEETINGS_20261009.md @261e2c42a0, on dell2 COO~T2's ask (row NFRA_TRNSPT-D2-S11).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM reads of the gateway host).
</preflight>

## 1. THE CELL -- `OG-tl-1` (decomposition addendum R3-T.35)

`/hx/transcripts` refuses every meeting today: `deploy-to-ec2.sh` writes `TRANSCRIPT_MEETING_ALLOWLIST=` EMPTY. The CTO
ruled that 4 meetings become readable: the `online_meeting_id` values in `data/transcripts/scripts/teams/meeting_allowlist.json`
(dell2's committed file, also on box/sitez; Morning Meeting, OCIO IC, Asset Management IC, Research Team Meeting). The
ids are READ from that file at deploy time, never typed. Nothing else changes: no code, bearer, route, IAM or other env.
Expect 3 of 4 readable: Research Team Meeting reads 403 from Graph's side until its organizer grants access (the
ruling's own note). That is NOT this cell's failure.

### PHASE A (now) -- build and ask; NO deploy

1. **Base = the host's LIVE ref, read now** (EC2_MANIFEST `services.opal-gateway.deployed_commit` at box/sitez HEAD,
   cross-read by host md5 with `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~43/r29_md5_host.py`
   through `r29_ssm_prog.py`). If r29 (`91811b648a`) is not yet live, build on `91811b648a` and say so; Phase B re-cuts
   on whatever is live then (MP-x-4 deploys between r29 and this cell).
2. Release worktree `C:/tmp/og-reltl1` on a new branch `rel-nfra-oplgtw-tl1` at that base. ONE commit: in
   `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, compute the allowlist from the json (comma-joined `online_meeting_id`
   values, in file order) and write it into the `.env` printf's `TRANSCRIPT_MEETING_ALLOWLIST=` (a `%s` and one argument).
   The deploy refuses (exit non-zero before any upload or `.env` write) if the json is unreadable or yields a count other
   than 4. Make sure the release tree carries `data/transcripts/scripts/teams/meeting_allowlist.json` byte-equal to
   box/sitez HEAD's. Then `W/tl1_release.json` = `{"base_sha": "...", "release_sha": "..."}`.
3. `W/NEVER_WIDEN_ASK_OG-tl-1.md`, in the form of `deliverables/0.9.0_WK_NFRA_OPLGTW~43/ANNOUNCE_OG-rl-15.md` sections 13
   and 14, short: the 4 ids BY NAME and value (they are meeting ids, not secrets), what a caller of `/hx/transcripts` can
   newly read (each meeting's transcript list and content, same bearer, same answer shape), the writers of the property
   (N printed: `deploy-to-ec2.sh` -> `.env`), both branches (the id admitted and Graph answers; the id admitted and Graph
   403s), the one restart, rollback = redeploy the base, triggers (`/health` off 200, tools off their count, any `.env`
   value hash changed other than this one). Halves owed: `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`.
4. Run AC1, commit, REPORT, STOP. The issuer cuts the applier's order after the halves and MP-x-4.

### PHASE C (after the applier's deploy report, named by the issuer's continuation)

5. One SSM read through the INSTALLED host: `W/TL1_READ.json` = `{"body": {...}, "ssm_command_id", "instance_id"}`, the
   host printing `TL1_DIGEST <sha256 of json.dumps(body, sort_keys=True)>`. Body exactly: `served_release`,
   `installed_code: true`, `allowlist_count`, `allowlist_sha256` (sha256 of the sorted ids joined by ","),
   `env_values_changed` (the `.env` keys whose value hash moved across the deploy, sorted). Then AC2.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~48/`.

## 2. BOUNDS

- You deploy, upload and restart nothing. The deploy is the applier's.
- One file changes in the release: `deploy-to-ec2.sh`. No other gateway file, no Terraform.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into a branch (row Z-W41-S5); override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~48/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W48-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root; AC1 after Phase A, AC2 after Phase C)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tl-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/tl1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)files differing 1 \(want 1\): infra/aws/ec2/opal-gateway/deploy-to-ec2\.sh.*ids typed literally: 0 \(want 0\); release json equals HEAD's: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-tl-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/tl1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)transcript allowlist served: fields=yes ssm=Success digest=yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-tl-1" judgment="true"/>
</proof_of_spec>

- `AC1`: the release changes one file and reads the ids from the committed json.
- `AC2`: the served host holds exactly those ids, and nothing else in `.env` moved.
- `AC3` (judgment, `3.0.0_SA_CVO~Z` at L9): dell2's own re-probe (one read per meeting, row NFRA_TRNSPT-D2-S11) reads 3
  of 4 meetings, the fourth a Graph-side 403 as the ruling predicts. Record it UNVERIFIABLE-BY-INSTRUMENT naming the CVO.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-tl-1.transcript-allowlist-4-meetings.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance>`, and flip the ONE `<status>` tag to `complete` only if AC1 and AC2
PASS. Report once per phase: literal outputs, commits, rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- CTO~Z ruling @261e2c42a0 (msg 32708): first OPLGTW release after r29; host order r29 -> MP-x-4 -> this cell (msg 32710,
  no veto) -> MX-r-9 -> E2 -> the metadata route.
- Pre-cut: tl1.AC1 base FAIL as expected (record absent); tl1.AC2 base FAIL as expected (record absent); the json reader
  reads 4 ids (sha256 prefix bd206c964417adfb). rl15_attest.py gains the TL1_DIGEST rule in the issuance commit.

- A1 (issuer, 2026-10-09 ~12:1xZ, on BLOCKING row Z-W48-S1): the one-file release commit on `rel-nfra-oplgtw-tl1` is
  refused by the owned-paths lane gate because the release tree (cut at the host's base) carries no copy of this
  order. RULED: that ONE commit (`infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` only) is made with the AUDITED escape
  `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL`, reason naming this amendment; no other commit, path or branch uses it,
  and no other gate is overridden. `tl1_release.json` records `base_sha` = the stage commit `4514246d65` (r29 +
  meeting_allowlist.json, row Z-W48-S2) so AC1 measures the one script change; the applier's `DEPLOY_BASE_REF` stays
  the host's live ref. Graded by no gate limb as a modification (placeholders NONE).

<status>complete</status>
<round>33</round>
<workstream>TRNSPT-ALLOWLIST</workstream>
<slot>~48</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
