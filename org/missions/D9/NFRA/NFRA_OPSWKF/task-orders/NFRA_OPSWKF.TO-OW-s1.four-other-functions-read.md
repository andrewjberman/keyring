# TO NFRA_OPSWKF.TO-OW-s1 -- four functions behind the portal authorizer, read by hand: what a non-internal caller can do

<to_id>NFRA_OPSWKF.TO-OW-s1</to_id>
<project>NFRA_OPSWKF</project>
<issued_to>0.9.0_WK_NFRA_OPSWKF~7</issued_to>
<issued_by>2.0.0_SA_COO~O2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>S</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a record; nothing changed, nothing called) | **Decomp cell:** `OW-s-1` |
**outcome_ref:** FWD-8 (PRD v0.5 addendum of 2026-10-11 ~17:4xZ, "the four other functions") | **depends_on:** none.

---

## WORKER FACE

You are `0.9.0_WK_NFRA_OPSWKF~7`. Your worktree is `C:/tmp/opswkf-s-7` (branch `wk-NFRA_OPSWKF-7`, cut from box/dell2 at the
issuance commit). Work and commit ONLY there with `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPSWKF~7
<0.9.0_WK_NFRA_OPSWKF~7@opal.agent>" -F <msgfile> -- <paths>`; write the message file with the Write tool.

### THE CELL

`OW-s-1`. A census by another seat found five functions behind the portal's HTTP API authorizer that serve any caller the
authorizer verified, without deciding who the caller is. One (`trade-dashboard-api`) is being fixed by another cell. **You read
the other four BY HAND, whole, and say for each what a verified caller whose tier is NOT internal can do.** A "non-internal
caller" is any signed-in person or service whose authorizer context carries `tier` other than `internal`: a client login,
another firm's user, a service token (`tier` `service`, no firm).

The authorizer puts the caller's claims at `event.requestContext.authorizer.lambda` (keys: `email`, `tier`, `role`,
`firmRole`, `firmId`, `allowedFirmIds`, `userType`; `firmId` defaults to the STRING `null`). A function that never reads that
context cannot be deciding on the caller.

The four functions and where their source is:

| function | source (read every file in it that the handler imports) |
|---|---|
| `trade-submission-handler` | `infra/aws/lambda/trade-pipeline/trade-submission-handler/src/` (handler `submission_handler.py`) |
| `opal-research-pull-enqueue` | `infra/aws/lambda/research/pull_enqueue/` (handler `lambda_function.py`) |
| `opal-portal-data-proxy` | `infra/aws/lambda/portal_data_proxy/` |
| `opal-portal-content-api` (its GET; say also what PUT and DELETE decide on) | `infra/aws/lambda/portal_content/` |

Routes are declared in Terraform under `infra/aws/terraform/` (start at `infra/aws/terraform/shared-infra/apigateway-portal/`
and `infra/aws/terraform/trade-pipeline/apigateway.tf`); find each function's route keys there with the native Grep tool on
those folders.

For each function, read: (1) every route key that reaches it and whether the route carries the authorizer; (2) the router,
and for every branch what the handler is handed (the whole event, or only a body or query string); (3) every read of the
authorizer context and what is DECIDED on it (a value that is only recorded decides nothing); (4) what the handler then
reads, writes, enqueues or returns. For `trade-submission-handler` also follow one step on: does anything refuse, later, a
submission whose submitter has no trade-users row or no groups (read
`infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/workflow_handler.py`), and what the ticket fence does to it.

**Write ONE record**, ASCII only, at
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~7/FOUR_FUNCTIONS_WHAT_A_NON_INTERNAL_CALLER_CAN_DO.md`:

- A header saying what you read, at which commit (`git rev-parse --short HEAD`), and that nothing was called.
- Exactly four sections, each headed `## <function name as in the table>`, each carrying these lines verbatim in form:
  - `routes: <n>` then the route keys, one per line;
  - `non_internal_caller: CAN -- <what, in one sentence>` or `CANNOT -- <why>` or `PARTLY -- <which part>`;
  - the basis: every claim cites `` `repo/relative/path.py:LINE` `` or `` `path.py:START-END` `` in backticks, read by you;
  - `not_established:` what you could not settle from the repository (deployed bytes are never established here: say so once).
- A last section `## What is the same and what differs` : one short table, function by harm class (reads data / writes or
  creates a record / spends money or quota / none).

State what the code does. Do not rate severity, do not propose a fix, do not change any source file.

### ACCEPTANCE

<criterion id="OW-s1-AC1" cell_refs="OW-s-1"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/S_CHECKS/ow_s_checks.py s1-record</invocation><expect>OW-S1-RECORD-OK</expect></criterion>
`OW-s1-AC1`: the record exists with its four sections, each with its verdict line, its `routes:` line and a basis that resolves.

<expected_criteria>OW-s1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, your deliverables folder `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~7/`,
  and this order's file (status flip only). Every source file is READ only.
- Never call AWS, a URL or any deployed service. Read the repository only.
- No non-ASCII. If you need a row, append it in BINARY mode as `NFRA_OPSWKF-D2-W7-S<k>`, keeping the file's line endings;
  `surfaced_at` = `date -u +%FT%TZ` at filing.

<paths>
org/missions/D9/NFRA/NFRA_OPSWKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPSWKF/decompositions/NFRA_OPSWKF_DECOMP.md</decomp_doc> (workstream S), cell `OW-s-1`.
<owned_cells>OW-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: OW-s1-AC1. The instance is at
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~7/NFRA_OPSWKF.TO-OW-s1.four-other-functions-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> OW-s1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** the check line verbatim, the four `non_internal_caller:` lines verbatim, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, hold or gate is created or consumed by this cell
comp-iam: DECLARED-NOT-APPLICABLE a read; no IAM change
comp-adversary: DECLARED-NOT-APPLICABLE a read-only record; its claims are checked by the basis citations and read by the issuer at the drain
lane: none written; the four functions' owners are named by 1.0.0_SA_CTO~DELL2 from this record (PRD v0.5 addendum).
</preflight>

Release: `1.0.0_SA_CTO~DELL2` msg 5533 on `3.0.0_SA_CVO`'s verdict @287ea37a51 (FWD-8's cells only; first cell = this read).
