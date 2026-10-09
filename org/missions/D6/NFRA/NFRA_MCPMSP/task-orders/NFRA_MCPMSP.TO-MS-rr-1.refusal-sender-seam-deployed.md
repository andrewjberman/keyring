# NFRA_MCPMSP task order -- `MS-rr-1` -- ROUND 3, E2: whose identity a refusal entry's `user` holds, on the deployed bytes

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-rr-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPMSP.TO-MS-rr-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPMSP~9</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- local code against a fixture; no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1 asserts exact values; the script's absence at the base is its control.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-rr-1` (decomposition ROUND 3, R3.2; the CTO's round-2 analysis item E2, row NFRA_MCPMSP-Z-W4-S3)

The question: in an `asker_sender_refusal` audit entry, is `user` the Teams SENDER or the CALLING gateway identity, and
does the refusal list (`GET /api/admin/refusals`) show the sender's address? No real refusal entry exists on the live
host yet, so this cell answers it on the DEPLOYED code: the opal-gateway tree at commit
`aa75078e1b72a28219e6148d3ec8e9bf705ea111` (the deployed commit). The relevant code there:
- `app/asker_scope.py` (the asker query path): reads the chat's members through a `graph_call` function, takes the
  sender's address from the member whose `userId` is the sender's oid (`sender_gate.sender_address`), and on a refusal
  writes `audit_log(calling_email, SENDER_REFUSAL_TOOL, {tid, oid, display_name, chat_id, reason, sender_email,
  sender_domain}, "denied", <reason>)` -- `user` in the written record is `calling_email`;
- `app/audit.py`: `audit_log` writes one JSON line per call to `get_config().AUDIT_PATH` (env `AUDIT_PATH`), filtering
  `args` through `_ARGS_ALLOWLIST`; the lake ship is skipped when `AUDIT_S3_BUCKET` is unset;
- `app/admin_refusals.py`: `list_refusals(limit)` reads the `AUDIT_PATH` file and returns rows with `sender_email` /
  `sender_domain` taken from the entry's `args` only.
- The deployed test `tests/test_mcpmsp_sender_gate.py` already drives a domain refusal
  (`test_domain_not_allowed_refused_and_logged`: sender `pat@gmail.com`) with a fake `graph_call` and a fake tenant
  store; READ IT FIRST and reuse its harness shape (its fixtures, its calling identity, how it invokes the path).

Build ONE file, `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~9/rr1_seam.py`:
- `python rr1_seam.py --gateway <dir>` where `<dir>` is an extracted opal-gateway tree (the check extracts the deployed
  commit with `git archive`); it puts `<dir>` on `sys.path`, sets `AUDIT_PATH` to a NEW temp file and unsets
  `AUDIT_S3_BUCKET` BEFORE importing `app`, then drives exactly ONE domain refusal through `app/asker_scope.py` with
  calling identity `caller@opalinvest.com` and a Teams sender `pat@gmail.com` (a registered/Opal tenant so the refusal is
  the DOMAIN one, `asker_sender_domain`), using fakes for Graph and the tenant store only (never a network call);
- it then reads the temp file's `asker_sender_refusal` entry and calls `app.admin_refusals.list_refusals()` on the same
  file, and prints exactly one line:
  `SEAM user=<entry user> sender_email=<entry args.sender_email> listed_sender_email=<first listed row's sender_email>`
- it does not edit the gateway tree, and exits non-zero with a one-line reason if the refusal was not written.

## 2. BOUNDS

1. Write surface: exactly the `<paths>` below. Nothing under `infra/` is written.
2. No AWS, SSM, Graph or vendor call; no push. REFUSE a criterion you cannot meet as written.
3. If the printed `user` turns out to be the SENDER (not the calling identity), do not change any code: file a
   BLOCKING row stating it, and report.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~9/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/` (via `git show aa75078e1b:<path>` or the extract),
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round3/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W9-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-rr-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round3/checks/rr1.AC1.sh; echo "exit=$?"</invocation><expect>deployed=aa75078e1b72a28219e6148d3ec8e9bf705ea111; SEAM user=caller@opalinvest.com sender_email=pat@gmail.com listed_sender_email=pat@gmail.com -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~9/NFRA_MCPMSP.TO-MS-rr-1.refusal-sender-seam-deployed.proof_of_spec.json`.
Report once, with: the SEAM line; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E2 of `ledger/ROUND_ANALYSIS.round2.md` @8a9def3720 (CTO ruling 3). Issuer ruling at the cut
(decomposition R3.2): the analysis's "one real refusal record" does not exist -- host `audit.jsonl` 0 `asker_sender_refusal`
of 158,094 lines (SSM 4acf5205-763d-4f81-9748-7fbf6285c1dd), positive control 2 `opal_asker_query` entries (SSM
cad5ecd1-7df1-4e19-a060-849be67dc94d) -- and cannot be produced without a live sender to the pilot identity (G-MSPID,
Andrew's act). The deployed bytes already carry the remedy's "carry sender args" branch; this cell settles `user` on those
bytes; the real-record read is CARRIED to the round that re-cuts MS-sv-1. DIRECT ACT: one cell, under the size floor,
LOCAL; its close is the issuer's one real run of AC1 at the drain. Check dry-run at base: AC1 FAIL as expected (script
absent); extraction control: the deployed tree extracts (59 entries under app/, admin_refusals.py carries sender_email).

<status>complete</status>
<round>3</round>
<slot>~9</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
