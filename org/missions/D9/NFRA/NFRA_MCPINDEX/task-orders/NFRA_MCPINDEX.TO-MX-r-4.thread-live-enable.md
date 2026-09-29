# NFRA_MCPINDEX task order -- `MX-r-4` -- the thread runs live: a NARROW gateway release that ENABLES opal_discover and portal_index, then one live question per portal surface

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~10</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the host, its role and Terraform are untouched. Enabling an integration changes the tool surface that admitted principals list, not IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is ruled (R-8); the enable holds on G-A and on both never-widen halves.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM) and the gateway's own live reads of the portal bucket during the close run.
</preflight>

## 1. THE CELL -- `MX-r-4` (round 3, enrichment item 3; the re-cut of `MX-r-2`)

**Why.** Round 2 built the thread and shipped it DARK. Gateway release 110d93fb73 carries `opal_discover` and
`portal_index`, but the host's `ENABLED_INTEGRATIONS` names neither. Read at the cut: the host enables
`ycharts opal_portal globgrph`. This order makes the thread live.

**Start this order only after MX-d-3 is complete and drained to CLOUD.** The issuer continues you with it.

**THE RULING you release under:** R-8 in `org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round1.md`, carried
by `ROUND_ANALYSIS.round2.md` R-12. READ BOTH. Every gateway release is NARROW: it is cut at the deployed commit plus
this project's own changes. Read the deployed commit from `infra/aws/ec2/EC2_MANIFEST.json`
(`services.opal-gateway.deployed_commit`) at YOUR cut; never assume it.

The MX-r-3 order is the worked precedent for every mechanic below. READ IT:
`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-3.narrow-release.md`. That covers the release
worktree, the cherry-pick census, the ledger, `safe-ec2-deploy.sh`, and the by-hand manifest record on this device.

### PHASE A -- no deploy
1. **Name this project's gateway commits since the deployed commit.** These are commits on CLOUD touching
   `infra/aws/ec2/opal-gateway` whose author is `0.9.0_WK_NFRA_MCPINDEX~<n>`. List them, oldest first. MX-d-3's commits
   must be among them.
2. **The release tree:** `git worktree add -b rel-nfra-mcpindex-r3-gateway /c/tmp/mx-rel3 <deployed_commit>`, then
   `cherry-pick --no-commit` those commits in order, and commit under your serial. The issuer authorizes the audited
   `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_MCPINDEX~10` for exactly the release-branch commit(s); name each use.
   **Census:** `git -C /c/tmp/mx-rel3 diff --stat <deployed_commit> HEAD -- infra/aws/ec2/opal-gateway` names ONLY
   files those commits changed. Anything else: STOP, a BLOCKING row.
3. **The enable mechanism.** Find exactly how the host's `/opt/opal-gateway/.env` `ENABLED_INTEGRATIONS` line is set
   through the existing deploy path (`deploy-to-ec2.sh` and what it reads). Name the file and line that carry the value
   and the one change that adds `opal_discover` and `portal_index`. If the only route is a hand edit on the host, STOP
   and file a BLOCKING row. A hand edit is not a deploy path.
4. **Rollback, proven before the act:** rebuild the deployed commit's artifact from a clean tree WITHOUT uploading. Name
   the re-deploy command and the `.env` value it restores.
5. **The integration checklist:** for each of the two integrations, record where it stands against
   `NFRA_INTEGRATIONS_STANDARD.md` s.5 and s.8.1. Find the file with `comp-which`.
6. Write `ANNOUNCE_MX-r-4.md` in your deliverables dir with steps 1-5. Commit it and report. DO NOT DEPLOY. The issuer
   asks the never-widen halves on this announcement.

### PHASE B -- only after the issuer says GO
The GO requires all of: G-A standing for both integrations, both never-widen halves SIGNED as files, and no other
gateway release mid-act. The GO names the signed files, and their guards bind you.
7. **NEVER-2 ledger** `nfra-mcpindex-r3-gateway-enable`, on your branch: open it with `python .tools/deploy_ledger.py open ...`
   and commit the entry and its sentinel before any act.
8. **Deploy** from the RELEASE worktree with ITS scripts:
   `cd /c/tmp/mx-rel3 && bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`,
   carrying the enable through the path named in step 3. Record on your branch: in `EC2_MANIFEST.json`
   `services.opal-gateway`, set `deployed_commit`, `previous_deployed_commit` and a `release_note`, as MX-r-3 did.
9. **Close run, live through the gateway.** Ask one question per portal surface of the A2 denominator: `platinum/mdpf`,
   `platinum/etfs`, `platinum/advi`, `json/*`. Record for each:
   - the question;
   - the tool that answered;
   - the figure and as-of date it returned;
   - the portal's own figure and as-of date for the same thing, read from the served object the portal page reads.
   Write this to `CLOSE_RUN_MX-r-4.md` in your deliverables. You do not grade it.
10. Close the ledger legs, then commit the close before AC1 and AC2 read.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-28 ~22:1xZ), on PHASE A's announcement (release pin 2f14e38af9, @7d5fcd0bf2):**
- **The enable line is granted.** In `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, line 197 carries
  `ENABLED_INTEGRATIONS=ycharts opal_portal globgrph` inside the `.env` printf. You may change EXACTLY that value, to
  `ENABLED_INTEGRATIONS=ycharts opal_portal globgrph opal_discover portal_index`. The printf keeps 9 `%s` and 9
  arguments, and nothing else in the file changes.
  - Commit it on the RELEASE branch, so the deploy carries it.
  - Commit the identical one-line change on your worker branch, so CLOUD does not later revert the enable. The issuer
    measured line 197 as byte-identical on CLOUD and on the release base 6a98a0553a.
- **Re-cut the release pin to carry MX-x-2.** Its portal_index and catalog change is now on CLOUD, drained at
  ac96f4ae3e, feature commit 357d85c0ba by 0.9.0_WK_NFRA_MCPINDEX~13. The integration being enabled should be the
  one released.
  - Cherry-pick 357d85c0ba's gateway files onto the release branch after 2f14e38af9.
  - Re-run the census: the only gateway files allowed are 85e1158e6e's plus 357d85c0ba's gateway files, plus line
    197.
  - Re-run the three test files in the release tree.
- **Then STOP and report the FINAL release pin:** its hash, the census, and the test counts. The issuer hands that
  exact hash to 1.0.0_SA_CTO~O for G-A and to both never-widen halves. Still NO deploy, no ledger, no `.env` change
  on the host.

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-09-29 ~02:1xZ), on row Z-W10-S2 (safe-ec2-deploy's halt gate admits a worker only if its non-terminal order is at HEAD of the calling tree, and the release tree has none):**
- **The deploy runs from a DEPLOY-ONLY tree:**
  - a worktree cut from CLOUD HEAD, on branch `dep-nfra-mcpindex-r3-gateway`, NEVER merged and never pushed;
  - in it, the whole directory `infra/aws/ec2/opal-gateway` is replaced by the release pin's (3371f18803). Use
    `git rm -r -q` on the directory, then `git checkout 3371f18803 -- infra/aws/ec2/opal-gateway`;
  - commit it as ONE deploy-only commit under the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_MCPINDEX~10`.
  This is the OA-r-1 pattern (54e26d66a0, NFRA_OPALAI issuer amendment 5).
- **Granted for that commit only:** `infra/aws/ec2/opal-gateway/**` on the dep- branch.
- **Prove before the GO, then STOP:**
  - `git diff --stat 3371f18803 <dep> -- infra/aws/ec2/opal-gateway` is empty;
  - rebuild the artifact from the dep tree and from 3371f18803 WITHOUT uploading, and compare them per file, N of N
    identical, N printed;
  - the halt gate reads this order at the dep tree's HEAD, with `<issued_to>` you and `<status>` pending.
  The issuer takes the dep hash to both signers (the CVO's N1 names HEAD 3371f18803) and GOs.
- **N1 at the deploy** reads the dep tree: HEAD = <dep>, its gateway dir equal to 3371f18803's, and mcportal a3bff71
  with 0 status lines. N2, N3 and rollback via mx-rb4 are unchanged.

## 2. BOUNDS

1. Terraform, the ALB, the host's role and its secrets are untouched. `safe-ec2-deploy.sh` is READ, never edited.
   `deploy-to-ec2.sh` is READ except line 197's value (A1).
2. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report. Never leave
   it half-landed.
3. No cold run with a non-author asker: that needs G-B, which is Andrew's and is not given here.
4. The interpreter is `python`. No push, no vendor call. REFUSE a criterion you cannot meet as written, and report it
   with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r3-gateway-enable.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~10/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

If step 3 finds the `.env` value carried in a repo file, that file is NOT in these paths. Name it in the announcement,
and the issuer amends `<paths>` before PHASE B.

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W10-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the ledger close is committed)

<proof_of_spec>
  <expected_criteria>AC1,AC2,J1</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/r4.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/r4.AC2.sh; echo "exit=$?"</invocation><expect>status=Success; /health=200; new integrations shipped 2 of 2; new ones enabled=2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="MX-r-4" judgment="true"><!-- graded at L9 by 3.0.0_SA_CVO~O on CLOSE_RUN_MX-r-4.md: for each of the 4 A2 surfaces, did the tool the gateway chose answer with the figure AND as-of date the portal serves for the same thing? FWD-2 reads this. The worker records, never grades. --></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~10/NFRA_MCPINDEX.TO-MX-r-4.thread-live-enable.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Report once per phase. Write the proof instance at the `<instance_path>` after PHASE B. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-2 analysis s.5 item 3 @e4445020f5. This re-cuts decomposition cell `MX-r-2`
("enable this project's integrations ... HELD (G-A)"), superseded in round 1 on the opal_ai move. Item 3 enables from
the deployed commit 110d93fb73 instead, so the cell is re-cut onto the current gateway.
- PHASE B holds on the decomposition's own gate G-A (s.6 :740): "the CTO's G1-G8 arch-gate signed per integration before
  its enable-deploy". :1028 words G-A as "Andrew's word to ENABLE". The issuer has asked `1.0.0_SA_CTO~O` which form
  stands and whether it is given. This is not a new gate.
- Dry-run at base: r4.AC1 FAIL (no entry; 18 of 18 sentinels scanned). r4.AC2 FAIL: SSM Success, /health 200, shipped
  2 of 2, `ENABLED_INTEGRATIONS=ycharts opal_portal globgrph`, new ones enabled=0.
- Chain: MX-d-3 -> MX-r-4, one worker (~10) continued.
- One deployer at a time: the NFRA_OPLGTW switchover sitting (Andrew's call 2 = a) touches the gateway. The GO reads
  `.open_deploys/` across every live worktree first.

<status>complete -- issuer-graded on CLOUD after the drain @6334ce5322 by 2.0.0_SA_COO~MI, 2026-09-29 ~03:0xZ: r4.AC1 PASS (the ledger nfra-mcpindex-r3-gateway-enable closed, 4 of 4 legs; sentinel gone), r4.AC2 PASS (a live SSM read: /health 200, 2 of 2 shipped, ENABLED_INTEGRATIONS = ycharts opal_portal globgrph opal_discover portal_index), instance VALID. The worker N2 read-back showed tools 46 -> 51 (0 removed; opal_discover, opal_describe and 3 mdpf_*). The host serves deploy-only 0bce8d322a, whose gateway tree is pin 3371f18803 (09ccfc39ad). J1 (the close run) is OPEN: NOT RUN, because no authenticated route to the tools exists from a worker or from this seat, whose MCP tool list was fixed at connect. The first live exercise is a principal session with a refreshed tool list, which is Andrew's speed test (G-ASKER record @7bfa5811c6). The CVO grades J1 on it. Was: pending.</status>
<round>3</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
