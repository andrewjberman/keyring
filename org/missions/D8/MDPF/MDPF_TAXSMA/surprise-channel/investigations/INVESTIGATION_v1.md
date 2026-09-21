# MDPF_TAXSMA -- surprise channel, INVESTIGATION v1

**Opened by:** `2.0.0_SA_COO~T` at L6, 2026-09-15. **Home:** the project tree's channel. Lane `ANY`; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project). **Append-only.**
Worker rows carry their slot's coordinate, `MDPF_TAXSMA-W<n>-S<k>`; a seat's row carries none.

**Why this file is opened at the issuance.** Two facts found while grounding the round's test criteria change what a
"the suite passes" criterion can honestly say, so every criterion that runs a suite names them instead of inheriting them.

**Denominator at this write: 2 rows** -- `MDPF_TAXSMA-S1`, `MDPF_TAXSMA-S2`, 2.0.0_SA_COO~T at L6.

```json
[
  {
    "id": "MDPF_TAXSMA-S1",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "surfaced_at": "2026-09-15T16:52Z",
    "one_line": "The MDPF Gold suite already fails 3 tests at the cut base, all in test_global_fold_flag2.py on the Global fold carry path that TX-a-1 and TX-a-2 edit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: Python 3.12.10, 'python -m pytest data/mdpf/scripts/gold/tests -q -p no:cacheprovider' at HEAD bd2fa195c0, 2026-09-15 16:5xZ: 92 collected, '3 failed, 89 passed'.",
        "FAILED: data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_within_window_carries_and_labels (assert 'carried' == 'measured'); ::test_carry_beyond_window_absent_for_real (assert 128.0 == 120.0); ::test_carry_source_is_measured_never_interpolated (assert 'carried' == 'measured').",
        "DECOMP: org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md s.7 and bound 17 record this baseline; TX-p-1 re-measures it at its own HEAD."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A cell that edits the Gold aggregation or consolidator would naturally be graded on 'the MDPF Gold suite passes', which assumes the suite is green at the base the workers branch from.",
    "world_is": "The suite is red at the base on 3 tests that predate this project. Every Gold-suite criterion in this issuance therefore reads 'fails only on the 3 pre-existing test_global_fold_flag2.py ids', and a new failure is the defect.",
    "notes": "INERT: it blocks nothing in this round because the criteria name it. OBSERVATION: whether the tests or the fold code is the one to change belongs to the Global fold's owner, not to any MDPF_TAXSMA cell."
  },
  {
    "id": "MDPF_TAXSMA-S2",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "surfaced_at": "2026-09-15T16:52Z",
    "one_line": "moto is not installed in this box's Python, so two Gateway test modules fail collection; TAXSMA's Gateway tests must not depend on it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: 'python -m pytest infra/aws/ec2/opal-gateway/tests -q --co -p no:cacheprovider' at HEAD bd2fa195c0: '90 tests collected, 2 errors'.",
        "ERRORS: tests/test_access_state.py and tests/test_oauth_durable.py, each 'ModuleNotFoundError: No module named moto'; both modules belong to NFRA_OPLGTW.",
        "PROBE: 'python' and 'py -3.12' both resolve Python 3.12.10 with pandas, pyarrow, boto3, yaml, pytest, fastapi, starlette and httpx importable; moto and msal are not."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A Gateway code cell would naturally be graded on 'the Gateway suite passes', which assumes every module collects on this box.",
    "world_is": "Two modules cannot collect here without an install no order grants. TX-g-1's criterion counts the modules that collected and passed before its edit, names the two moto modules as NOT-EVALUATED on this box, and forbids a new dependency.",
    "notes": "INERT for this project. OBSERVATION: whether moto belongs in the box's Python is NFRA_OPLGTW's and the box owner's question, not this project's."
  },
  {
    "id": "MDPF_TAXSMA-S3",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~T",
    "surfaced_at": "2026-09-15T20:57Z",
    "one_line": "TX-g-1's issued grant omitted tests/test_principal_cutover.py, whose ROUTE_CLASS completeness assertion requires one entry for every served route; amended before spawn.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TEST: infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py:487 defines ROUTE_CLASS; :542 asserts set(ROUTE_CLASS) == set(routes) over every route app.server serves; :35 imports moto (read at HEAD 91b11ff0c9).",
        "MESSAGE: 2.0.0_SA_COO~O 97236 (20:50Z), answering notice N-1: the new route is not in ROUTE_CLASS, so whichever drain lands it goes red without the entry; NFRA_OPLGTW cells take an entries-only grant under 1.0.0_SA_CTO ruling 97203 rule C, scoped to that project.",
        "ORDER: MDPF_TAXSMA.TO-TX-g-1 as issued @955b8c6cbe granted four Gateway paths and not this test file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TX-g-1's <paths> named taxsma_workbook.py, server.py, config.py and test_taxsma_workbook.py as the whole Gateway write surface for adding GET /ms/taxsma-workbook.",
    "world_is": "Adding a served route also requires one ROUTE_CLASS entry in test_principal_cutover.py. The order was amended before its spawn to grant exactly that file for one entry, with no criterion changed; the module needs moto, absent on this box, so it is NOT-EVALUATED here.",
    "notes": "INERT after the amendment. Found by 2.0.0_SA_COO~O's reply to N-1, before any TAXSMA worker spawned; the drain merges TX-g-1's entry after NFRA_OPLGTW's own ROUTE_CLASS lines."
  },
  {
    "id": "MDPF_TAXSMA-W5-S1",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~5",
    "surfaced_at": "2026-09-15T21:20Z",
    "one_line": "PRD s.3.4 classifies additional Tax-labelled custodian candidates 'UNCONFIRMED', but no status axis or reason code in the data contract carries that value, so the expected-case manifest cannot name the candidates' status in contract vocabulary.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md@671925aecc line 205: 'Discover additional Tax-labeled custodian candidates by the complete dated source population and classify them UNCONFIRMED; no automatic workbook edit or membership promotion follows.'",
        "CONTRACT org/standards/MDPF_TAXSMA_DATA_CONTRACT.json@91b11ff0c9 status_axes (business_status 7, identity_status 7, membership_date_status 3, technical_enrollment 5, value_status 4, freshness 5, run_result 6 members) and reason_codes (36 members): the token UNCONFIRMED occurs only inside REMOVED_UNCONFIRMED (lines 245 and 650), a different state (a removed prior traded row).",
        "TASK ORDER org/missions/D8/MDPF/MDPF_TAXSMA/task-orders/MDPF_TAXSMA.TO-TX-v-1.expected-cases.md@91b11ff0c9 line 22: 'the contract's enumerations are the only vocabulary'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order makes the contract's enumerations the only vocabulary, and PRD s.3.4 names the additional-candidate classification UNCONFIRMED.",
    "world_is": "The contract has no UNCONFIRMED member on any axis. TX-v-1's arm A02-09 therefore states the candidate's observable without a status label: not counted live, not in the dated expected population, listed once in protected candidate evidence, no workbook write. The label that S04 (TX-m-2) emits for a candidate is unfixed by the contract.",
    "notes": "INERT: the manifest's candidate expectation does not depend on the label. OBSERVATION: whether the contract gains a candidate value or the PRD word is dropped belongs to the contract owner (the PRD author), not to any worker cell."
  },
  {
    "id": "MDPF_TAXSMA-W6-S1",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~6",
    "surfaced_at": "2026-09-15T21:39:18Z",
    "one_line": "TX-p-1's AC7 (a read-only SSM census of the Gateway host) needs ssm:SendCommand, a Send verb, so AC10 (every AWS call is Describe/Get/List/Head) cannot pass in the same cell as written.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D8/MDPF/MDPF_TAXSMA/task-orders/MDPF_TAXSMA.TO-TX-p-1.baseline.md@91b11ff0c9 :49 (TXP1-AC7, 'a read-only SSM census of the Gateway host's app source') and :58 (TXP1-AC10, 'every AWS call in the cell's command log is a read verb (Describe, Get, List, Head)'); decomposition org/missions/D8/MDPF/MDPF_TAXSMA/decompositions/MDPF_TAXSMA_DECOMP.md@7f65001ab3 s.3 :179 and :182 carry the same two lines.",
        "RUN 2026-09-15T21:35:44Z, probe deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_p_1.py AC7: ssm describe-instance-information (i-07dccb1615503ac99 Online), ssm send-command CommandId 686530ff-12ce-46ab-b5b2-d07ef6985eaa (AWS-RunShellScript, a 20-line script of find, grep, wc, md5sum and stat that writes nothing), ssm get-command-invocation Status=Success; VERDICT: PASS-TXP1-AC7.",
        "RUN 2026-09-15T21:39:18Z, same probe AC10 over deliverables/0.9.0_WK_MDPF_TAXSMA~6/command_log.jsonl: 'READ-VERB CALLS: 42 of 43; NON-READ: 1 of 43', the one being 'ssm send-command (criterion TXP1-AC7)'; VERDICT: FAIL-TXP1-AC10.",
        "The worker found no read-verb SSM route to host file content: DescribeInstanceInformation, GetCommandInvocation and ListCommandInvocations read only a command that SendCommand created, and inventory lists files without their content."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TX-p-1 is read only; AC7 asks for a read-only SSM census of the Gateway host's app source, and AC10 requires every AWS call in the cell's command log to be a Describe, Get, List or Head verb.",
    "world_is": "The only SSM call that runs a census on the host is SendCommand, whose verb is Send. The command it ran was read-only and AC7 passed, but the log then carries 1 non-read call and AC10 prints FAIL, so the two criteria cannot both pass as written. The worker ran AC7 as named and left AC10 FAIL, so TO-TX-p-1 stays open; no criterion was reworded.",
    "notes": "BLOCKING on TXP1-AC10 only: it holds this order's complete flip. INERT: nothing in normal operation is harmed if it is left alone. SendCommand also leaves an SSM command-history record and the SSM agent's own orchestration files on the host; the script itself wrote nothing. Whether AC10 is reworded or AC7 re-routed is the issuer's call, not the worker's."
  },
  {
    "id": "MDPF_TAXSMA-W6-S2",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~6",
    "surfaced_at": "2026-09-15T21:41:00Z",
    "one_line": "EC2_MANIFEST.json's opal-gateway file_checksums do not describe its own deployed_commit: app/server.py records a101f27e..., while the host file and the git blob at 7bd89b5d71 are both 370d5568....",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MANIFEST infra/aws/ec2/EC2_MANIFEST.json@91b11ff0c9: :505 deployed_commit 7bd89b5d71b8d488d9e8c4168513193c9d6a9ec2, :506 deployed_at 2026-09-09T19:08:11Z, :509 app/server.py a101f27ea37009d73cb19b247eef26e7, :511 app/config.py 20836f8aa54ee27ffb7209686fa27df7, :512 app/audit.py 5f8342859f23ad773b059c4030d4c402.",
        "HOST (probe AC7, SSM CommandId 686530ff-12ce-46ab-b5b2-d07ef6985eaa, 2026-09-15T21:36Z): /opt/opal-gateway/app/server.py md5 370d55689b57c33221317271f10d7bd3, mtime 2026-09-09 18:43:58 +0000.",
        "REPO: 'git show 7bd89b5d71:infra/aws/ec2/opal-gateway/app/server.py | md5sum' gives 370d55689b57c33221317271f10d7bd3, equal to the host; the CRLF rendering of the same blob gives 68b3b073721be878f5cf825af293e072; the blob at HEAD 91b11ff0c9 gives 552335bcbc6fdc45a0f2013a2296c4da. The recorded a101f27e... equals none of the three (positive control: 'git cat-file -t 7bd89b5d71' is commit).",
        "DENOMINATOR: 6 of the 10 recorded app/*.py checksums compared with the blob at 7bd89b5d71. tools.py, tier.py and guard.py match; server.py, config.py (blob 881be540ca15f2cbeaa566bbee6e3ece) and audit.py (blob 7858f05f4b4d2fde48a88fa1866f5bc8) do not. The other 4 were not compared."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "infra/aws/ec2/EC2_MANIFEST.json, a read file named by TO-TX-p-1, records for opal-gateway a deployed_commit (7bd89b5d71) and per-file md5 checksums, which a reader takes as the fingerprint of the code on the host at that commit.",
    "world_is": "The host's app/server.py is byte-identical to the git blob at 7bd89b5d71 (md5 370d5568...), but the manifest's recorded checksum for it (a101f27e...) matches neither that blob, its CRLF rendering nor HEAD. config.py and audit.py also differ from their blobs, while tools.py, tier.py and guard.py match. For three files the checksum field is not a measurement of what the host runs.",
    "notes": "OBSERVATION found while grounding TXP1-AC7; TX-p-1 did not ask for it and relies on nothing in it. INERT as far as this cell can see. Whether infra/aws/ec2/safe-ec2-deploy.sh or TX-r-2 reads file_checksums is a question for the manifest's writer (the 7bd89b5d71 deploy is recorded as 0.7.0_AE_CloudOps~Z's). Separately, HEAD's server.py differs from the host's because NFRA_OPLGTW's OG-a-1..3 commits of 2026-09-15 are not deployed; that state belongs to gate G-O."
  },
  {
    "id": "MDPF_TAXSMA-W6-S3",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~6",
    "surfaced_at": "2026-09-15T21:47:53Z",
    "one_line": "The live opal-assets-mdpf-portal-publisher's MDPF_PUBLISHER_COMMIT stamp (c0902245b0, 2026-08-06) is not the pin its deployed code was built from (dc14d649bb, 2026-08-28).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DECLARED: infra/aws/terraform/opal-assets/mdpf_portal_publisher.tf@91b11ff0c9 :155-156, 'The deploy pin, stamped into every D7 manifest (updated per deploy).' MDPF_PUBLISHER_COMMIT = 'c0902245b07438eb0be65cf5e28241d4be56aa38'.",
        "LIVE (probe AC2, lambda get-function, 2026-09-15T21:47:53Z): env MDPF_PUBLISHER_COMMIT=c0902245b07438eb0be65cf5e28241d4be56aa38, LastModified 2026-08-29T01:01:04Z, CodeSha256 7X50uR1HrGyeEHZ4FWyHBNwTxt/XXJq5GNmR/eFfWE0=. The downloaded code's in-zip BUILD_MANIFEST source_vintage is pin and commit dc14d649bb3e8e7853ed9f648b08f7ca7017b7c8.",
        "CONTROL: the existing builder run at --pin dc14d649bb3e8e7853ed9f648b08f7ca7017b7c8 reproduces the live CodeSha256 exactly (MATCH), so the deployed bytes are the dc14d649bb build.",
        "REPO: 'git cat-file -t' is commit for both. c0902245b0 is 2026-08-06 ('TO(MDPF_CANPLAT cutover leg 3): P3-1 publisher rebuilt ...'); dc14d649bb is 2026-08-28 ('ledger(CATVP-c publisher): OPEN before the act ...')."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "mdpf_portal_publisher.tf, a read file named by TO-TX-p-1, declares MDPF_PUBLISHER_COMMIT as 'the deploy pin, stamped into every D7 manifest (updated per deploy)'.",
    "world_is": "The live function carries the declared value c0902245b0 (2026-08-06), but the code it runs is the build at dc14d649bb (2026-08-28): its own BUILD_MANIFEST says so, and a rebuild at that pin matches CodeSha256. The stamp was not updated at the 2026-08-29 deploy, so by the file's own description each D7 manifest names a commit that is not the running code.",
    "notes": "OBSERVATION found while grounding TXP1-AC2. It bears on TX-u-2 and TX-r-1, which re-package and release this function. The gold Lambda's MDPF_GOLD_COMMIT does equal its zip's commit (48b8671569). INERT as far as this cell can see; whether any served body carries the stamp was not read here."
  },
  {
    "id": "MDPF_TAXSMA-W6-S4",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~6",
    "surfaced_at": "2026-09-15T23:08:00Z",
    "one_line": "AC7's census script sends one redirect to /dev/null, and amended TXP1-AC10 condition (2) says 'no redirect or write to any path outside the SSM agent's own working directory'; the probe grades /dev/null as the null device, which is a reading of the frozen text.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D8/MDPF/MDPF_TAXSMA/task-orders/MDPF_TAXSMA.TO-TX-p-1.baseline.md@6be05d277f, TXP1-AC10 as amended by 1.0.0_SA_CTO ruling 97255 option A: condition (2) 'it ONLY reads: no redirect or write to any path outside the SSM agent's own working directory, no sudo write, no package or service action, and no network call'.",
        "SCRIPT: org/missions/D8/MDPF/MDPF_TAXSMA/deliverables/0.9.0_WK_MDPF_TAXSMA~6/probes/tx_p_1.py@b9a15838d7 :485 (CENSUS_TMPL), the GREP_ERRORS line '... xargs -0 -r grep -l -F 'taxsma-workbook' -- 2>&1 >/dev/null | wc -l'. It sends grep's stdout to /dev/null so that only error lines are counted. The script has 2 redirects: '2>&1' (a file-descriptor duplication, no path) and '>/dev/null'; 0 to any other path.",
        "BYTES: the regenerated script's sha256 0892538431cbf66b9bc9ca8486745cce62ea6dce353e84c9288e7bde69ecfaad begins with the run-time value 'census script sha256=0892538431cbf66b' recorded in runs/AC7.txt@b9a15838d7 :5, and equals the untracked request file .scratch/tx_p_1/ssm_census_request.json that send-command read.",
        "GRADE: the probe's AC10 (runs/AC10.txt, this commit) prints '1 to /dev/null (the null device: bytes discarded, no file created or modified), 0 to any other path' and a READING line saying that a literal reading of 'any path' would FAIL condition (2) on this 1 redirect; conditions (1), (3) and (4) are MET without it."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Amended TXP1-AC10 admits AC7's one send-command only if its script makes 'no redirect or write to any path outside the SSM agent's own working directory'.",
    "world_is": "The script's only redirect to a path is '>/dev/null', which discards bytes and creates or modifies no file. /dev/null is still a path outside the agent's working directory, so the clause read literally is not met; read as 'the script only reads', it is. The worker's probe graded it as the null device, printed that reading in the evidence and filed this row rather than choosing silently. TXP1-AC10 prints PASS under that reading.",
    "notes": "OBSERVATION: whether the literal or the purposive reading binds belongs to the L9 adjudicator (3.0.0_SA_CVO) and the ruling's author (1.0.0_SA_CTO, 97255), not to the worker. If the literal reading is ruled, TXP1-AC10 is FAIL and TO-TX-p-1's complete flip is withdrawn; no new AWS act would change the recorded script. INERT: the redirect wrote nothing on the Gateway host."
  },
  {
   "id": "MDPF_TAXSMA-S4",
   "project": "MDPF_TAXSMA",
   "fabric": "laptop",
   "surfaced_by": "0.0.0_AB_MSTR",
   "surfaced_at": "2026-09-20T19:25:00Z",
   "one_line": "TX-g-1 was completed by its worker on 2026-09-15 and never drained: the order reads pending on origin/CLOUD and complete at f2cac74c60, whose three commits exist only in the worktree /c/tmp/wk-taxsma-1.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "disposition": "UNDER_INVESTIGATION",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "GIT: `git rev-list f2cac74c60 --not origin/CLOUD origin/SITEZ` = 3 (6abf60e5d5, 8dce9aeb0b, f2cac74c60), run by 0.0.0_AB_MSTR from the shared checkout after a fetch of both branches, 2026-09-20 ~19:0xZ; origin/CLOUD @8c6f223092, origin/SITEZ @047aee5478.",
     "BYTES: org/missions/D8/MDPF/MDPF_TAXSMA/task-orders/MDPF_TAXSMA.TO-TX-g-1.workbook-capability.md reads <status>pending on origin/CLOUD and <status>complete at f2cac74c60 -- 1.0.0_SA_CTO msg 98700, a second seat on a different read.",
     "PACKET: org/tier0_exec/0.0.0_AB_MSTR/deliverables/CVO_REVIEW_PACKET_UNMERGED_WORKTREES_20260920.md@423d855bf7."
    ]
   },
   "spec_asserts": "Spine L7-L8: a worker's completed cell reaches the shared branch by the issuer's drain, and the order's <status> on CLOUD is what every census reads as the project's open work.",
   "world_is": "git rev-list f2cac74c60 --not origin/CLOUD origin/SITEZ returns 3: 6abf60e5d5 feat (GET /ms/taxsma-workbook capability, route, config keys, tests), 8dce9aeb0b fix, f2cac74c60 complete -- all 0.9.0_WK_MDPF_TAXSMA~1, 2026-09-15. The same order file reads <status>pending on origin/CLOUD and <status>complete at f2cac74c60 (1.0.0_SA_CTO msg 98700, read at the bytes). The worktree also holds 2 dirty paths, unread here. So the open-order census over-counts this project by one and the only copy of the cell is one directory on one disk that reached 0 bytes free on 2026-09-20.",
   "notes": "PARKED with an owner and a condition because 2.0.0_SA_COO~T is not seated and mail to it would be a silent hole: OWNER the MDPF_TAXSMA issuer; UN-PARKS when that lane is next seated. Drain, re-cut or supersede is the issuer's call and is not decided here. The worktree is in 3.0.0_SA_CVO's review packet @423d855bf7 (LD-0595) and is NOT to be removed on any verdict short of the issuer's own word. Found by 0.0.0_AB_MSTR's /cleanup sweep; confirmed by 1.0.0_SA_CTO."
  },
  {
    "id": "MDPF_TAXSMA-W1-S1",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~1",
    "surfaced_at": "2026-09-15T21:37Z",
    "one_line": "TXG1-AC22 names two moto-dependent Gateway test modules as NOT-EVALUATED; at the cut base fd2f1e4b31 four fail collection on moto, and two collected modules already fail or error.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: 'py -3.12 -m pytest infra/aws/ec2/opal-gateway/tests -q -p no:cacheprovider' at HEAD fd2f1e4b31, 2026-09-15T21:20:52Z, Gateway tree untouched: 'Interrupted: 4 errors during collection', each 'ModuleNotFoundError: No module named moto': tests/test_access_state.py, tests/test_browser_oidc.py, tests/test_oauth_durable.py, tests/test_principal_cutover.py.",
        "RUN: the same 14 modules one process each at fd2f1e4b31: tests/test_identity_scope.py '1 failed, 5 passed' (test_scoped_deny_by_default, AssertionError: opal_data_refresh_upload); tests/test_jwt_cve_lock.py '5 passed, 1 error' (test_control_valid_token_accepted, No module named moto at :43); tests/test_schwab_audit.py '1 skipped' (could not import moto); the other 7 modules pass.",
        "ORDER: org/missions/D8/MDPF/MDPF_TAXSMA/task-orders/MDPF_TAXSMA.TO-TX-g-1.workbook-capability.md@50b8910af4 TXG1-AC22, '(the two moto-dependent modules named as NOT-EVALUATED on this box)'; row MDPF_TAXSMA-S2 measured '90 tests collected, 2 errors' at bd2fa195c0."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TXG1-AC22 compares the Gateway modules that collected and passed before the edit with after, naming the two moto-dependent modules (row MDPF_TAXSMA-S2: test_access_state.py, test_oauth_durable.py) as NOT-EVALUATED on this box.",
    "world_is": "At fd2f1e4b31 four modules fail collection on moto, because test_principal_cutover.py and test_browser_oidc.py landed with NFRA_OPLGTW after S2's measurement, and all four are named NOT-EVALUATED. The comparison runs per TEST, not per module: test_identity_scope.py carries 1 pre-existing failure and test_jwt_cve_lock.py 1 pre-existing moto fixture error. Both are shown before and after and are not graded, and every test that passed before must still pass.",
    "notes": "INERT: the criterion is graded on the population as measured, with the before arm recorded at fd2f1e4b31 in deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/ac22_before.json before any Gateway edit. OBSERVATION: the identity_scope failure and the missing moto belong to NFRA_OPLGTW and the box owner, not to this cell."
  },
  {
    "id": "MDPF_TAXSMA-W1-S2",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~1",
    "surfaced_at": "2026-09-15T22:02Z",
    "one_line": "Running the Gateway test modules from the Gateway directory, as TXG1-AC22 requires, appends to the TRACKED file infra/aws/ec2/opal-gateway/audit.jsonl, which is outside this order's grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: the pre-edit per-module baseline at fd2f1e4b31 (cwd infra/aws/ec2/opal-gateway) left 'M infra/aws/ec2/opal-gateway/audit.jsonl', '3 insertions(+)', 0 deletions: three '_ratelimit_control' alarm records ('per-IP-AUTH', 'per-IP-global' and 'per-identity limiter error ... induced'), written by tests/test_ratelimit.py through the default AUDIT_PATH './audit.jsonl' (app/config.py:279 @fd2f1e4b31).",
        "RESTORE: the file was rewritten with its own HEAD blob's bytes (git show HEAD:<path>): git hash-object = git rev-parse HEAD:<path> = 3c69355bcda895e2e0fbd9fef0d18284534d6dd0, 'git diff --quiet HEAD -- infra/aws/ec2/opal-gateway' rc=0, 0 untracked; porcelain status still reads ' M' from a stale stat entry on this core.autocrlf=true box, so the probe tests content equality instead.",
        "PROBE: deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/tx_g_1.py now points every pytest it starts at a scratch AUDIT_PATH, so neither AC22 arm writes the tracked file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TX-g-1's write grant is its <paths> block plus its deliverables folder, and TXG1-AC22 runs the Gateway test modules before and after the edit.",
    "world_is": "One of those modules (test_ratelimit.py) writes three records into the tracked Gateway audit.jsonl whenever it runs from the Gateway directory, so running the criterion as written touched a file outside the grant. The worker restored the file's bytes to HEAD (blob 3c69355bcd), commits nothing under that path, and runs its own measurements with AUDIT_PATH redirected to scratch.",
    "notes": "INERT for this cell once the file is back at its HEAD blob and every later run redirects AUDIT_PATH. OBSERVATION: whether test_ratelimit.py should patch AUDIT_PATH, and whether audit.jsonl should be tracked at all, belongs to NFRA_OPLGTW."
  },
  {
    "id": "MDPF_TAXSMA-W1-S3",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~1",
    "surfaced_at": "2026-09-15T22:35Z",
    "one_line": "The TXG1-AC22 before-record at fd2f1e4b31 reads tests/test_schwab_engine.py::test_ogq1_ac02 FAILED in both probe records (bar 0.25 s) though the first shell run passed it, so row W1-S1's 'the other 7 modules pass' holds for 6.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: shell loop, one process per module, finished 2026-09-15T21:36Z at fd2f1e4b31: tests/test_schwab_engine.py '13 passed in 41.02s'.",
        "RUN: probes/tx_g_1.py AC22 --record-before at fd2f1e4b31, Gateway tree content-equal to HEAD: first record (the module beside the others) 'assert 1.005868499991484 < 0.25'; second record (the module alone, first) 'assert 0.48001869998755864 < 0.25', recorded_at 2026-09-15T22:35:23Z in deliverables/0.9.0_WK_MDPF_TAXSMA~1/probes/ac22_before.json.",
        "TEST: tests/test_schwab_engine.py:259 @fd2f1e4b31 'assert child_lag < 0.25'; row NFRA_OPLGTW-W3-S12 records that module's lag bar as load-sensitive."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TXG1-AC22 grades that the Gateway tests which passed before the edit still pass after it; row MDPF_TAXSMA-W1-S1 states that at fd2f1e4b31 every module other than the four moto modules, test_identity_scope.py, test_jwt_cve_lock.py and test_schwab_audit.py passes.",
    "world_is": "test_ogq1_ac02's lag bar failed in 2 of 2 probe records and passed in 1 shell run. The committed before arm therefore counts it as failing BEFORE the edit: it is shown before and after and is not graded, and the passed-before population is 12 of that module's 13 tests.",
    "notes": "INERT: AC22's grading is deterministic whichever way the timing lands, because a test failing before is never a regression and a test passing before must still pass. OBSERVATION: the bar's load sensitivity belongs to NFRA_OPLGTW (W3-S12), not to this cell."
  },
  {
    "id": "MDPF_TAXSMA-W1-S4",
    "project": "MDPF_TAXSMA",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_MDPF_TAXSMA~1",
    "surfaced_at": "2026-09-21T03:15:00Z",
    "one_line": "TX-g-2's TXG2-AC1 build (mirroring the registered deploy-to-ec2.sh tar step) bundles a TRACKED runtime telemetry file, app/org/mcp/agent_telemetry/0.7.0_AE_CloudOps.jsonl (9 lines, 1863 bytes), into every Gateway deploy artifact through the same `app` whole-directory member that carries taxsma_workbook.py.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TAR: infra/aws/ec2/opal-gateway/deploy-to-ec2.sh @2aa1e26cbf lines 69-72, `tar -czf \"$TMP/$ART\" -C \"$SRC\" --exclude=... app deploy requirements.txt identity_tool_allowlist.txt` -- `app` is archived whole, no exclude names it.",
        "MEMBER LIST: TXG2-AC1 probe run, 2026-09-21T03:08:37Z, member list (84 of 84 printed) includes `app/org/mcp/agent_telemetry/0.7.0_AE_CloudOps.jsonl` alongside `app/taxsma_workbook.py`.",
        "TRACKED: `git ls-files infra/aws/ec2/opal-gateway/app/org/mcp/agent_telemetry/` returns the one file; `git log -1 -- <path>` shows commit 2781aac326 (2026-08-14), pre-existing and unrelated to this project; `wc -l`/`wc -c` on the worktree copy: 9 lines, 1863 bytes."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Rule 2 (`No private data in the repository`) and the order's bound of the same name: masked labels and aggregate counts only enter code, fixtures, deliverables or logs; a secret's path is one `grade(<path>, \"SECRET\")` returns CONFORMANT for.",
    "world_is": "A pre-existing tracked file under the Gateway's own app/ tree, an agent telemetry JSONL, ships in the deploy artifact by virtue of being inside the whole-directory `app` tar member -- not added, moved or graded by this cell, and not read for content here (no private-data claim is made about its bytes, only about its inclusion path).",
    "notes": "OBSERVATION found while grounding TXG2-AC1's member list. INERT: this cell added no file and the bundling behavior predates it (commit 2781aac326, 2026-08-14, NFRA_OPLGTW/the box owner's surface). Whether app/org/mcp/agent_telemetry/ belongs in the deployed artifact, in the tar excludes, or is fine as-is is a question for the Gateway's owner, not this cell."
  }
]
```
