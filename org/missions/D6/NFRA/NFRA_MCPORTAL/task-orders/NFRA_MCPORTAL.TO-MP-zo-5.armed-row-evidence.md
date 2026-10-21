# NFRA_MCPORTAL task order -- `MP-zo-5` -- WORKSTREAM OGW ROUND 2: evidence for the four 26-day ARMED rows (W2-S8, W3-S2, C-S3, C-S8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-zo-5</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-zo-5</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~45</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time evidence read.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only, with the caller's own identity; no role is assumed and no policy touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- each finding is one command and its output, re-runnable by the issuer.
EGRESS CLASS, declared: AWS READ on Opal's own plane (`lambda get-function-configuration`, `lambda invoke` with NO owner header), and local reads of the repository. No write, no deploy, no vendor call.
</preflight>

## 1. THE CELL -- `MP-zo-5` (workstream OGW round 2, decomposition section OGW2.2)

Four surprise rows have been ARMED for 26 days. For each, bring evidence that it can be disarmed, or name an owner and a date. You change nothing in the world; you measure and write one file.

You work in your own worktree `C:/tmp/mp-ogw-45` (branch `wk-NFRA_MCPORTAL-45`); begin each shell call with `cd C:/tmp/mp-ogw-45 &&`. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~45 <0.9.0_WK_NFRA_MCPORTAL~45@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push. No network call other than the two AWS reads named below.

The four rows, each in `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/` (the two `Z-W` rows in `investigations/INVESTIGATION_v1.Z.md`, the two `Z-C` rows in `adjudications/ADJUDICATION_v1.Z.md`; find a row by its `"id"` line and read that one JSON block only):

1. `NFRA_MCPORTAL-Z-W3-S2` -- no record named Andrew's Entra object id, so the writer could not be given its owner key. **Measure:** the deployed function carries its owner configuration. Run `bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zo5.AC2.sh` (a no-header invoke of the writer; it answers `REFUSED NO-OWNER-HEADER` only when the owner configuration is set, because the writer checks that first). Also run `.tools/aws lambda get-function-configuration --function-name mcportal-grant-writer-lambda --query "Environment.Variables.keys(@)" --output json` and record the NAMES only. Never print, record or commit a value.
2. `NFRA_MCPORTAL-Z-C-S8` -- the writer's `parents[5]` and gateway imports could not resolve inside the zip its Terraform builds. **Measure:** the writer now runs from its built package. The same `zo5.AC2.sh` run proves the handler imported and answered from `/var/task`. Also download the deployed zip (the presigned URL `.tools/aws lambda get-function --function-name mcportal-grant-writer-lambda --query Code.Location --output text` returns, on Opal's own plane) into a new empty directory under `C:/tmp/mp-ogw-45/zipcheck/` and record whether `lambda_function.py` and the gateway `app/` members the handler imports are inside it (list the member names; do not run the code).
3. `NFRA_MCPORTAL-Z-C-S3` -- `.tools/owned-paths-validate.py` refuses a task-ordered NEW top-level path as `UNDEFINED`. **Measure:** read `.tools/owned-paths-validate.py` and say whether the `UNDEFINED` branch still refuses a path the order names (quote the lines with their numbers and the file's last commit from `git log -1 --format=%h%x20%ci -- .tools/owned-paths-validate.py`). The fix is a fabric-tool edit outside your surface: propose `OWNER_DATE`.
4. `NFRA_MCPORTAL-Z-W2-S8` -- the 90-second rollback trigger cannot be met by `safe-ec2-deploy.sh`'s rollback, because its HALT-GATE scans a message backlog for about 12 minutes first. **Measure:** read `infra/aws/ec2/safe-ec2-deploy.sh` and quote the halt-gate lines that scan messages (line numbers, and the file's last commit). Do not run the script. If you cannot tell from the source whether the scan still precedes the host step, say so. The fix is `2.0.0_SA_COO~O`'s: propose `OWNER_DATE`.

Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~45/row_evidence.json`:
`{"rows": [{"id": "<row id>", "proposal": "DISARM" | "OWNER_DATE", "owner": "<serial>", "date": "YYYY-MM-DD", "evidence": [{"claim": "MEASURED" | "RECORDED" | "ABSENT", "command": "<the command>", "output": "<its output, trimmed to what matters, no value of any variable>"}]}, ... exactly four ...]}`.
A `DISARM` proposal needs at least one `MEASURED` item with a non-empty command and output. An `OWNER_DATE` proposal needs the owner serial and a date that is a calendar date at least 3 days after today (`date -u`); you do not decide it, you propose it. Rows 1 and 2 are expected to be `DISARM`; rows 3 and 4 are expected to be `OWNER_DATE`; if your evidence says otherwise, write what the evidence says and say why in `output`.
Commit the file, then run AC1 and AC2.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No edit of `.tools/`, `infra/`, the Lambda, the gateway or any task order.
2. No credential, token, account number, or environment-variable value appears in any file you write or any output you print.
3. If a criterion cannot be met as written, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check scripts and the proof line are the issuer's.
4. Do NOT flip this order's `<status>`.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~45/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `.tools/owned-paths-validate.py`, `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/lambda/mcportal/`, the surprise-channel rows named above, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_MCPORTAL-Z-W45-S<k>` (k from 1). APPEND ONLY: add your row after the last one and leave every earlier byte untouched. `surfaced_at` = `date -u +%FT%TZ`. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-zo-5"><invocation>cd C:/tmp/mp-ogw-45 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zo5.AC1.sh; echo "exit=$?"</invocation><expect>(?s)evidence=read rows=4 ids_match=yes rows_with_valid_proposal=4 of 4.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-zo-5"><invocation>cd C:/tmp/mp-ogw-45 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zo5.AC2.sh; echo "exit=$?"</invocation><expect>(?s)invoke status=200 verdict_reason=\[REFUSED NO-OWNER-HEADER\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~45/NFRA_MCPORTAL.TO-MP-zo-5.armed-row-evidence.proof_of_spec.json`, run `proof-of-spec-check.py` on it as the worker rules say, and report once, with: the output of AC1 and AC2; the commit hash; for each of the four rows its proposal, owner and date; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut in the OGW round-2 issuance (decomposition OGW2.2) from the CTO's `ledger/ROUND_ANALYSIS.ogw-round1.md` item 3 ("each one is disarmed with its evidence, or ruled to an owner with a date; none is carried silently"). Rows W3-S2 and C-S8 are the issuer's own reading of the writer deploy (MP-pd-7, closed 2026-10-20T20:23:42Z: the deployed function answers REFUSED NO-OWNER-HEADER before and after, so it imports and carries its owner key); the worker re-measures. Rows C-S3 (fabric tool, `1.0.0_SA_CTO`) and W2-S8 (the gateway release script, `2.0.0_SA_COO~O`) are not this project's product: the worker documents the state and the issuer asks the owner for a date. Only a CVO `adjudicates` row or a remediation row moves a worker row's clock; the issuer sends the worker's file to the CVO as an L8 packet. AC2 passes at base by design (it is an independent probe of the world the evidence describes, not a build check); AC1 FAILS at base (the file is absent) and its green and red arms were exercised with synthetic files.

<status>complete -- drained f89f7afb6f8 (worker 0.9.0_WK_NFRA_MCPORTAL~45); AC1 PASS (4 of 4 rows) and AC2 PASS (issuer re-ran both); proof instance VALID; DISARM proposals W3-S2, C-S8, C-S3; W2-S8 OWNER_DATE 2.0.0_SA_COO~O 2026-10-21. Issuer row Z-S78.</status>
<round>2</round>
<workstream>OGW</workstream>
<slot>~45</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
