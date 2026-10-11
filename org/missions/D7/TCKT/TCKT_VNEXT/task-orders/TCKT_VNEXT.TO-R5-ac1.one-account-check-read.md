# TO TCKT_VNEXT.TO-R5-ac1 -- a READ: where a one-account-per-file check can live

<to_id>TCKT_VNEXT.TO-R5-ac1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~20</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL; nothing is applied and nothing runs against AWS | **Decomp cell:**
`R5-ac-1` (`decompositions/TCKT_VNEXT_DECOMP_R5.md`) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~20`. Your worktree is `C:/tmp/tckt-r5-20` (cut from box/dell2 at the issuance commit). Work and
commit only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~20 <0.9.0_WK_TCKT_VNEXT~20@opal.agent>" -F <msgfile> -- <paths>`. Write
the message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or
stage it.

### WHY

An Analysis Request ticket carries one uploaded holdings file. The requirement (FWD-3) is that a file holding MORE THAN ONE
account is turned back to the person filing, at once, before anyone at Opal sees it. Nothing checks that today. The upload
goes through the investor-reporting upload door (`infra/aws/lambda/investor-reporting/intake/`); the ticket service
(`infra/aws/lambda/ticket_center/lambda_function.py`) receives only the door's `upload_id` and `input_id`, never the file; the
portal form (`portal/src/pages/TicketCenter/analysisRequest.ts` in the worktree's portal folder, READ ONLY) receives the door's
result with its `state` and `findings`. Before anyone builds the check, the issuer needs to know where it can live.

### THE CELL `R5-ac-1`

READ ONLY. Write no code and change no file but the one findings file. Read the upload door's code and answer, in
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~20/ONE_ACCOUNT_CHECK_READ.json`, a JSON object with EXACTLY
these keys:
- `question`: one sentence, the question above.
- `files_read`: a list of `path` or `path:line` strings, every file you opened that bears on the answer (paths relative to the
  worktree root; each must exist).
- `where_an_account_is_named_in_an_uploaded_file`: how the door's normalizer treats an account in a prospect upload: which
  column or field names it recognises as an account, if any, with the lines; and what the normalized input keeps of it.
  Note that `intake/uploads.py:209` sets `account_ids` to an empty list for a prospect input: say what that means for this.
- `can_the_door_count_accounts_today`: `yes`, `no` or `partly`, with the reason and the lines.
- `where_the_check_can_live`: a list of candidate homes (the door's normalizer; the door's result `findings`; the ticket
  service; the portal form), each with: what it would need that it does not have today, which file would change, and whether
  the person filing would learn at once (before a ticket exists).
- `what_was_not_read`: what you did not open or could not determine.
- `claim`: `measured` if every statement above is a line you read, `inferred` if any is reasoned from names.
Start with a named-file read of `infra/aws/lambda/investor-reporting/intake/` (list the folder, then read the normalizer and
`uploads.py`); use the Grep tool on that folder for `account`. Do not run a search over the whole repository. No client data:
column NAMES and code lines only, never a value from any holdings file.

### ACCEPTANCE

<criterion id="R5-ac1-AC1" cell_refs="R5-ac-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py ac-read</invocation><expect>AC-READ-OK</expect></criterion>
`R5-ac1-AC1`: the findings file exists, has exactly the seven keys, and every path in `files_read` exists.

<expected_criteria>R5-ac1-AC1</expected_criteria>

Dry-run at base: AC1 FAIL (absent findings file), as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run each invocation from the worktree root under `timeout 120`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W20-S<k>` with k from 1 upward, its own fenced block at the
  end of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~20/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files.

<paths>
# a read-only cell: its only write surface is its own deliverables folder
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~20/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R5.md</decomp_doc> (round 5), cell `R5-ac-1`.
<owned_cells>R5-ac-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R5-ac1-AC1. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~20/TCKT_VNEXT.TO-R5-ac1.one-account-check-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R5-ac1-AC1` before the flip.
</proof_of_spec>

**REPORT (once):** the check line verbatim, the commit, and the answer to `can_the_door_count_accounts_today` in one sentence with its lines.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (a read; nothing is built or applied).
</preflight>

Source: the CTO's round-5 analysis @d94b65958b section 3; decomposition `TCKT_VNEXT_DECOMP_R5.md`.
