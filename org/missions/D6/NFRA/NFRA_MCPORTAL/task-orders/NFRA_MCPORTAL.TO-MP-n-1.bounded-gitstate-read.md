# NFRA_MCPORTAL task order -- `MP-n-1` -- C17 ADDENDUM: the bounded git-state read, built and released

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-n-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-n-1</to_id>
<issued_to>0.7.0_AE_CloudOps~MP</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a handler change and its release; no cron, alarm, monitor or cadence is added.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the handler keeps MP-x-3's read grant and adds no store call kind (list_objects_v2 gains only the StartAfter parameter).
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1's 1x-vs-10x arm and AC2's two planted refusals are the adversary reads; the issuer dry-ran all three against HEAD (FAIL) and AC1/AC2 against a scratch C17 sketch (PASS).
EGRESS CLASS, declared: none beyond AWS control-plane calls in Opal's own account (SSM, the artifact bucket, the globgrph bucket read).
</preflight>

## 1. THE CELL -- `MP-n-1` (PRD v0.6 addendum C17; decomposition section "C17 ADDENDUM CELL")

**Why.** The served `GET /api/admin/fabric/gitstate` cold read takes 22.8 to 25.1 s against a 30 s bar, and it rises
every day. `_refused()` in `infra/aws/ec2/opal-gateway/app/admin_fabric_gitstate.py` scans each box's WHOLE history
newest-first and stops only at a refusal. With no refusal on record, every cold read fetches every body every box has
ever written: 2,771 fetches on the issuer's dry run. C17 bounds the read.

**Build (step 1), in a linked worktree you cut from `box/sitez` HEAD (NO-CONE pattern list if sparse).** Change
`app/admin_fabric_gitstate.py` so that a cold read fetches a number of bodies that does not grow with history length:
- **The listing** starts at the window. `_history_keys` passes `StartAfter` = the box's
  `fabric/activity/v1/gitstate/box=<box>/<cutoff stamp>.json` key, where cutoff = now minus `WINDOW_HOURS` (48) and the
  stamp is `%Y%m%dT%H%M%SZ`. So no key older than the window is listed.
- **`integration_refused`** is the newest refusal within the window that is NOT superseded. Scan newest-first and stop at
  the first record whose `pass.mode` is "integrate", whatever its outcome:
  - `rc != 0` gives that record as `{at, note}`;
  - `rc == 0` gives "not recorded";
  - reaching the window boundary with no integrate pass gives "not recorded".
  Beside the field, add `integration_refused_basis` per box. It is a fixed sentence saying the value is the newest
  integrate pass within the window, a later successful integrate supersedes a refusal, and older history is not read.
  This is the same pattern as `trunk.basis`.
- **`first_seen`** stops early per box. Scan newest-first within the window and stop at the first record whose
  `trunk_head` (12 characters) differs from the newest head. The earliest `at` among the records read before that stop
  is the box's contribution.
- **Unchanged:**
  - the response shape, except the one added basis field;
  - the 503 discipline;
  - the owner gate;
  - the body cache;
  - `FETCH_THREADS`;
  - every other module.
  The gateway still writes nothing.
- **Tests:** update `tests/test_admin_fabric_gitstate.py`. Its `FakeS3` paginator must accept `StartAfter`. Add one test
  per bullet above, then run every admin and fabric test file (`tests/test_admin*.py tests/test_entitlement_admin.py`),
  0 failed. Commit through the gate with no override.
- Run AC1 and AC2 (section 4) in that worktree. Both must PASS before step 2.

**Release (steps 2 to 5).** Follow MP-r-2's discipline, which you ran on 2026-10-10:
2. **Re-cut on the LIVE ref.** Read `services.opal-gateway.deployed_commit` from `infra/aws/ec2/EC2_MANIFEST.json` at the
   act, and confirm it on the HOST by md5 against that commit's tree (never `-latest`'s label; msg 33000).
   - Run `git worktree add -b rel-nfra-mcportal-c17 <path> <live>`, then `git checkout <your step-1 commit> --
     infra/aws/ec2/opal-gateway/app/admin_fabric_gitstate.py infra/aws/ec2/opal-gateway/tests/test_admin_fabric_gitstate.py`.
   - **Census:** `git diff --stat <live> HEAD -- infra/aws/ec2/opal-gateway` names ONLY those two files. Any other file:
     STOP with a BLOCKING row.
   - The mcportal bundle is the manifest's current `mcportal_commit`, unchanged. Run
     `ops/bun_cache_precheck.py bun.lock`; a miss STOPS.
   - **Load, before the cutover:** over SSM, the release's `admin_fabric_gitstate._compute()` from a temp directory with the
     host venv and the instance role. Take one cold sample in a fresh interpreter, and print its body-fetch count. Over
     10 s: STOP with a BLOCKING row naming the time and the count.
3. **Never-widen ASK.** Write `deliverables/0.7.0_AE_CloudOps~MP/NEVER_WIDEN_ASK_MP-n-1_<date>.md` before any ledger act.
   It names the BLAST RADIUS:
   - the one handler module and its test;
   - the served gateway restart;
   - the rollback per key: the versioned live artifact and the command that re-deploys it, proven by rebuilding the live
     base's artifact from a clean tree WITHOUT uploading, its app files equal to the host's by md5;
   - the expected outcome of BOTH branches (the release reads at or under 10 s; it does not, and rolls back).
   Commit it, and tell the issuer the commit. The deploy waits for BOTH halves, COO `2.0.0_SA_COO~MP` and CTO
   `1.0.0_SA_CTO~Z`, signed against that commit, and for the issuer's GO. The GO also confirms the gateway queue is free.
4. **NEVER-2 ledger and act, on your branch.**
   - Run `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-c17-gitstate-release`. The legs are: release
     build and upload, SSM pull and restart, served read-back, manifest record.
   - Put the census, the load sample, the rollback and this order's path in
     `deliverables/0.7.0_AE_CloudOps~MP/MP-n-1_PRE_ACT_RECORD.md`, with ONE pointer line in the entry.
   - Commit the entry AND its sentinel.
   - ACT from the release tree with ITS scripts: `bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway
     infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, with `DEPLOY_BASE_REF` = the live ref. The stale-base guard reads it
     unchanged at both reads.
   - Poll `/health` within 90 s. If it is not 200, run the named rollback AT ONCE, close the entry as rolled back, and stop.
   - Record the tool-surface counts before and after; their difference must be empty.
   - **Record the release:** `EC2_MANIFEST.json` `services.opal-gateway` gets `deployed_commit`,
     `previous_deployed_commit` (the base actually deployed over, not the release tree's vintage value) and a
     `release_note`, on your branch AND on `box/sitez` (the manifest is your lane; release branches are never merged).
   - Close every leg with its proof, and commit the close BEFORE the AC reads.
5. **Drain support.** Land the closed ledger entry and the manifest record on `box/sitez`. Leave the step-1 branch for the
   issuer's drain.

## 2. BOUNDS

1. Terraform, the ALB, the host, its role and its secrets are untouched. `safe-ec2-deploy.sh` is READ, never edited. No
   module other than `app/admin_fabric_gitstate.py` and its test is edited. The producer `.tools/fabric-gitstate.py` is
   not touched.
2. If step 2's load sample fails after the C17 change, STOP. Do not tune further in this cell.
3. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report. Never leave it
   half-landed.
4. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its measurement.
   Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_fabric_gitstate.py
infra/aws/ec2/opal-gateway/tests/test_admin_fabric_gitstate.py
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/*nfra-mcportal-c17-gitstate-release*
org/critical_paths/.open_deploys/nfra-mcportal-c17-gitstate-release.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/safe-ec2-deploy.sh`, the rest of `infra/aws/ec2/opal-gateway/`, `mcportal/`,
`.tools/fabric-gitstate.py`, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-S<k>` (the next free seat-row k, re-read at write time). `surfaced_at` = `date -u +%FT%TZ` at filing.
`disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`. Rows are append-only.

## 4. PROOF OF SPEC (literal; AC1 and AC2 from your step-1 worktree root; AC3 after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-n-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17/checks/n1.AC1.sh; echo "exit=$?"</invocation><expect>history 1x=240 10x=2400; get_object 1x=N 10x=N (equal, N>0); trunk head moved inside the window=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-n-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17/checks/n1.AC2.sh; echo "exit=$?"</invocation><expect>superseded refusal reads 'not recorded'; refusal newer than every integrate reads {'at': '2026-10-11T15:01:00Z', 'note': 'planted-live'} -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-n-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/c17/checks/n1.AC3.sh; echo "exit=$?"</invocation><expect>ssm status=Success; /health=200; no-identity gitstate 401 or 403; gitstate_s <= 10 with body_fetches printed and recorded >= 1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/NFRA_MCPORTAL.TO-MP-n-1.bounded-gitstate-read.proof_of_spec.json`.
Report once, to `2.0.0_SA_COO~MP`, with:
- the census;
- the load sample (time and body fetches);
- the tool-surface counts;
- the three check outputs;
- the ledger entry path and its CLOSED state;
- every commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut 2026-10-12 ~09:0xZ by the addendum path on PRD v0.6 C17 @fc09ade4ea (`1.0.0_SA_CTO~Z` msg 33458;
prd-signoff status ADMITTED, ENDPOINT unchanged). Decomposition section "C17 ADDENDUM CELL" @6e73fee848. One issuance:
`<workstream>C17</workstream>` round 1 keys it apart from CP2 round 1 (GATE (x)).
- **Checks dry-run by the issuer:**
  - n1.AC1 FAIL at HEAD (242 vs 2,402 get_object) and PASS on a scratch C17 sketch (98 vs 98);
  - n1.AC2 FAIL at HEAD (the superseded refusal is shown) and PASS on the sketch;
  - n1.AC3 FAIL on the served code 28ba9532b6 (22.8 s, 2,771 body fetches; ssm aeb096c6).
- **Known risk, not claimed away:** inside the 48 h window the producers write about 2,000 records across 4 boxes. Whether
  the early stops keep the cold read under 10 s depends on how often integrate passes and trunk moves occur. Step 2's load
  sample measures it before the cutover.
- **Assignee:** the applier seat holds the opal-gateway lane (`SHARED_CLOUD_OPS`), and one seat building and releasing
  follows MP-r-2's step-0 precedent (CP2.10). GO by message, the assignee being a seat.

**AMENDMENT 1 (issuer, 2026-10-12 ~10:1xZ, on row Z-S40 / msg 33462): ONE permitted load remedy, option (d).** Step 2
STOPPED: the release read 16.661 s with 1,346 body fetches against the 10 s bar. C17 works (AC1 98 vs 98, AC2 PASS, issuer
re-run in `C:/tmp/mp-n1` at @39ae93a10f). The new floor is the 48 h window's own 2,134 records, at about 12.4 ms per fetch,
eight at a time.
- In `app/admin_fabric_gitstate.py`, set `FETCH_THREADS = 32` (was 8). This matches `app/admin_fabric.FETCH_THREADS`, the
  pool size of the shared `_s3_client()` (`max_pool_connections=FETCH_THREADS`, AMENDMENT 5 of MP-r-2), so no client
  change is needed. Change nothing else. The section 1 line "`FETCH_THREADS` unchanged" is struck for this one constant.
- Commit it on `wk-mcportal-c17-n1` through the gate. Re-run every admin and fabric test file (0 failed), then AC1 and
  AC2 (both PASS).
- Re-take step 2's cold sample on the host, on the release bytes, with the cache asserted empty. At or under 10 s:
  continue to step 3. Over 10 s: STOP again with a row, and do not tune further. The window, the bar and the producer
  pointer (Z-S40's (a), (b), (c)) are contract or producer changes, so they go to `1.0.0_SA_CTO~Z`, not to this cell.
- BOUNDS 2 reads: "If step 2's load sample fails after the C17 change AND AMENDMENT 1, STOP."
Graded by: `.tools/to-pipeline-gate.py` at this commit (a MODIFIED order, so only GATE (viii) applies, and this order
declares `<placeholders>NONE</placeholders>`). No other limb grades a modification.

**DRAIN:** drained by 2.0.0_SA_COO~MP 2026-10-12 ~13:5xZ (build branch `wk-mcportal-c17-n1` @bf627dd9bb merged
@f555cd3a91; ledger entry @4497c5b1be; EC2_MANIFEST record @5f543a2363 by the applier). C17 + AMENDMENT 1 are LIVE on
185dc04888 over d9f2ebded9 (mcportal bc37107). Ledger nfra-mcportal-c17-gitstate-release CLOSED 20261012T130927Z, 4 of 4
legs. The trunk's two gateway files equal the deployed blobs, 2 of 2. Both never-widen halves were honoured:
- COO C-1: the payload was committed before the act, and the rollback key read back untouched;
- CTO-1: the first cut was discarded and the work re-cut on d9f2ebded9.
The issuer re-ran all three checks:
- AC1 PASS at HEAD (98 vs 98);
- AC2 PASS at HEAD (both arms);
- AC3 PASS on the host, ssm 2c8190a3: gitstate 7.6 s, 1,391 body fetches, 4 recorded, no-identity 401.
The CP2 regression r2.AC3 also PASSes (overlap 2.9 s, gitstate 7.1 s, calls 0.6 s).
Margin: about 1.2-1.3x and narrowing (fetches 1,346 -> 1,391 today). The structural fix is Z-S40 (c), the producer
pointer, and it is routed to 1.0.0_SA_CTO~Z's next analysis.
Was: pending

<status>complete</status>
<round>1</round>
<workstream>C17</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
