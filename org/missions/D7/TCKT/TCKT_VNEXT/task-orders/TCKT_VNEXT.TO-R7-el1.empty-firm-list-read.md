# TO TCKT_VNEXT.TO-R7-el1 -- a READ: what an empty or absent firm list on a users row means on each surface that reads it

<to_id>TCKT_VNEXT.TO-R7-el1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~26</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL; nothing is applied and nothing runs against AWS | **Decomp cell:**
`R7-el-1` (`decompositions/TCKT_VNEXT_DECOMP_R7.md`) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~26`. Your worktree is `C:/tmp/tckt-r7-26` (cut from box/dell2 at the issuance commit). Work and
commit only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~26 <0.9.0_WK_TCKT_VNEXT~26@opal.agent>" -F <msgfile> -- <paths>`. Write
the message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or
stage it.

### WHY

A users PROFILE row may carry `allowedFirmIds`: a list of firm ids, the literal `ALL`, an empty list, or no attribute at all.
Different services read it differently. In the ticket service (`infra/aws/lambda/ticket_center/lambda_function.py`,
`_profile_scope`, lines 360-391) NO attribute and an EMPTY list both mean "no scope", which reads every firm, and `ALL` inside
a list is "just an id that matches nothing". In the investor-reporting service
(`infra/aws/lambda/investor-reporting/_authz/served.py`, around lines 1110-1135) no row and no attribute both return an empty
list ("never unrestricted") and only the explicit `ALL` is unrestricted. The portal authorizer puts `allowedFirmIds` into every
caller's context. Before anyone rules what an empty list SHOULD mean, the issuer needs what it means TODAY on each surface.

### THE CELL `R7-el-1`

READ ONLY. Write no code and change no file but the one findings file. Answer, in
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~26/EMPTY_FIRM_LIST_READ.json`, a JSON object with EXACTLY
these keys:
- `question`: one sentence.
- `files_read`: a list of `path` or `path:line` strings, every file you opened that bears on the answer (relative to the
  worktree root; each must exist).
- `surfaces`: a list of AT LEAST THREE objects, one per reader of `allowedFirmIds` you find, each with: `surface` (its name),
  `where` (path and lines), and what it does for each of these six inputs, as six keys: `no_row`, `row_without_the_attribute`,
  `empty_list`, `list_of_firms`, `the_literal_ALL`, `malformed`. Each value is one of `EVERY_FIRM`, `NO_FIRM`, `THE_LISTED_FIRMS`,
  `REFUSED`, or `NOT_READ` with a short reason. Required surfaces: the ticket service's `_profile_scope`; the investor-reporting
  service's internal and service firm readers in `_authz/served.py`; the portal authorizer (find it under
  `infra/aws/lambda/` by its folder name; if you cannot find it, say so in `what_was_not_read`). Add any other reader you meet.
- `where_the_three_surfaces_disagree`: the inputs for which two surfaces give different answers, one line each.
- `what_was_not_read`: what you did not open or could not determine.
- `claim`: `measured` if every cell is a line you read, `inferred` if any is reasoned from names.
Use the Read and Grep tools on named folders (`infra/aws/lambda/ticket_center/`, `infra/aws/lambda/investor-reporting/_authz/`,
and the authorizer's folder). Do not run a recursive shell grep or `find` over the repository (a hook refuses it). No client
data and no person's email in the file: code lines and input classes only.

### ACCEPTANCE

<criterion id="R7-el1-AC1" cell_refs="R7-el-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R7_CHECKS/r7_checks.py el-read</invocation><expect>EL-READ-OK</expect></criterion>
`R7-el1-AC1`: the findings file exists, has exactly the six keys, lists at least three surfaces, and every path in `files_read` exists.

<expected_criteria>R7-el1-AC1</expected_criteria>

Dry-run at base: AC1 FAIL (absent findings file), as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run each invocation from the worktree root under `timeout 120`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W26-S<k>` with k from 1 upward, its own fenced block at the
  end of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~26/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files.

<paths>
# a read-only cell: its only write surface is its own deliverables folder
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~26/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R7_CHECKS/r7_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R7.md</decomp_doc> (round 7), cell `R7-el-1`.
<owned_cells>R7-el-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R7-el1-AC1. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~26/TCKT_VNEXT.TO-R7-el1.empty-firm-list-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R7-el1-AC1` before the flip.
</proof_of_spec>

**REPORT (once):** the check line verbatim, the commit, and `where_the_three_surfaces_disagree` as a short list.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (a read; nothing is built or applied).
</preflight>

Source: the CTO's round-7 analysis and PRD v0.4 ADDENDUM 3 @8bb81f8d6c (C-FENCE: an internal caller the users table does not know is refused), signed by 3.0.0_SA_CVO @b667a5fb11 (its own L4-R commit, naming v0.4); decomposition `TCKT_VNEXT_DECOMP_R7.md`.
