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
  }
]
```
