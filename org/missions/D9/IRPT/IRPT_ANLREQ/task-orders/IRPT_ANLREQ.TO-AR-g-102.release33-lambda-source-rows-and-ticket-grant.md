# TO-AR-g-102 -- the SOURCE of release 33 (the irpt-ycharts-generate Lambda leg): re-pin six staged rows and one irpt-status row to HEAD's blobs, add the ticket_confirmation member, and declare the ticket-table variable and its one-statement GetItem policy

<to_id>IRPT_ANLREQ.TO-AR-g-102</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~201</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-102` (`decompositions/IRPT_ANLREQ_DECOMP_R24_G.md`) |
**outcome_ref:** FWD-1 run 3 / C-SWITCH / C-FILING-HINT / C-PRICES v0.16 | **depends_on:** `AR-g-67` (the accept stamps), `AR-g-85`, `AR-g-95` (merged `26d720a980`), `AR-g-96` (merged `78e28b386b`). Order: CTO msg 8658 (r33 = the `irpt-ycharts-generate` leg: the code, the staged row for `ticket_confirmation.py`, `IRPT_TICKETS_TABLE`, GetItem on that one table only, both priceDate branches) and 8693/8723 (r33 also carries the door tree).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~201`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-201` (branch `wk-IRPT_ANLREQ-201`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/`, `lib/`, `org/standards` and `org/missions/D9/IRPT` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~201 <0.9.0_WK_IRPT_ANLREQ~201@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W201-S<k>` (take the next free `<k>`; check the channel file for `W201` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- No live call, NO PUSH, no deploy, no AWS call, no terraform, no network, no install. Scratch outside the product tree. Edit `lambda-source-map.json` BYTE-PRESERVING: keep its indentation, key order and line endings, and change only the lines named below.

### Read first

- `infra/aws/lambda/ci/lambda-source-map.json`: the functions `irpt-ycharts-generate` (its `files` list and `staged_from` rows) and `irpt-status` (its `staged_from` rows). A row is `{"repo_path", "pin", "packaged_as", "sha256"}` on four lines (10 spaces); the builder (`release-census.py build_members`) packages `packaged_as` from `git show <pin>:<repo_path>` and refuses unless that blob's sha256 equals the row's.
- `infra/aws/terraform/investor-reporting/ycharts/generate.tf`: the module `irpt_ycharts_generate`'s `environment_variables` block and the inline policies above it (`generate_ownership_map`, `generate_directory_read`, the custody-factory one): your policy follows their shape.

### THE CELL (`AR-g-102`, inlined)

**1. The source map.** For each row below, set `pin` to the 40-hex sha of the LAST commit touching `repo_path` (`git log -1 --format=%H -- <repo_path>`; that commit's blob equals HEAD's) and `sha256` to the hex sha256 of that blob (`git show <pin>:<repo_path>`); change nothing else in the row.
- function `irpt-ycharts-generate`, `packaged_as` -> `repo_path`: `portfolio.py` -> `infra/aws/lambda/investor-reporting/intake/portfolio.py`; `uploads.py` -> `.../intake/uploads.py`; `acceptance.py` -> `.../ycharts/generate/acceptance.py`; `submission_service.py` -> `.../ycharts/generate/submission_service.py`; `generate_installed.py` -> `.../reports/generate_installed.py` (all under `infra/aws/lambda/investor-reporting/`).
- function `irpt-status`: `status.py` -> `infra/aws/lambda/investor-reporting/ops/status.py`.
- A NEW row for `irpt-ycharts-generate`, placed directly after its `submission_service.py` row, laid out exactly like its neighbours: `repo_path` `infra/aws/lambda/investor-reporting/ycharts/generate/ticket_confirmation.py`, `pin` and `sha256` as above for that path, `packaged_as` `ticket_confirmation.py`. And a new entry `"ticket_confirmation.py",` in that function's `files` list directly after `"submission_service.py",`.
- No other row, field, function or key of the map changes (not `last_deployed_*`, not `_staged_from_note`, not any other function). The two native members `normalized_input.py` and `prospect_submission.py` of `irpt-ycharts-generate` are packaged from the tree and need no edit.

**2. `infra/aws/terraform/investor-reporting/ycharts/generate.tf`.** Two additions and nothing else changes:
(a) in the module `irpt_ycharts_generate`'s `environment_variables` block, directly under the `IRPT_EVIDENCE_BUCKET` line and aligned with its neighbours: `    IRPT_TICKETS_TABLE             = "opal-tickets"`.
(b) immediately before the line `module "irpt_ycharts_generate" {`, after one blank line, and followed by one blank line, this block verbatim (comment lines, then the resource):
```
# PRD v0.9 C-SWITCH (AR-g-67): the accept step confirms the client's ticket_id with ONE consistent GetItem on the ticket table
# (ycharts/generate/ticket_confirmation.py) and stamps ticket_confirmed. ONE ACTION, ONE TABLE: no index, no Query, no write.
# The table has no customer key (AWS-owned encryption), so no kms statement. Its OWN inline policy so the rollback is one
# resource; the name is lib/opal_naming.py name("irpt", None, "ycharts-generate-ticket-read", "policy") output.
resource "aws_iam_role_policy" "generate_ticket_read" {
  name = "irpt-ycharts-generate-ticket-read-policy"
  role = aws_iam_role.generate.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid      = "ConfirmTheClientTicketOnly"
      Effect   = "Allow"
      Action   = ["dynamodb:GetItem"]
      Resource = ["arn:aws:dynamodb:${var.aws_region}:${data.aws_caller_identity.current.account_id}:table/opal-tickets"]
    }]
  })
}
```
DECLARED HERE, APPLIED BY THE R33 APPLIER under a signed never-widen pair: nothing in this cell plans, applies or deploys.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR102-g-AC1" cell_refs="AR-g-102"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g102_checks.py g102</invocation><expect>^AR-G102-OK</expect></criterion>

<criterion id="AR102-g-AC2" cell_refs="AR-g-102"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g102_checks.py scope</invocation><expect>^AR-G102-SCOPE-OK</expect></criterion>

<expected_criteria>AR102-g-AC1,AR102-g-AC2</expected_criteria>

- AC1 reads the map and generate.tf and asks 15 things: only the expected rows change in the whole map (compared by content with the base at the merge-base), every re-pinned or new row carries a full 40-hex pin that is an ancestor of HEAD with a blob equal to the file in the tree and to the row's sha256, the edit is byte-preserving (every changed line is one of the allowed forms, no CRLF), the two packages built from the old and the new map differ in exactly the six `irpt-ycharts-generate` members and in `status.py`, and `generate.tf` gains exactly the one environment variable and the one-statement GetItem-only policy named by the naming builder, the rest of the file byte for byte. At base it FAILs.
- AC2 checks (against the merge-base with `box/dell2`) that your branch changed only the map, `generate.tf`, your folder, your order and the channel file. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. No terraform command, no deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/ycharts/generate.tf
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~201/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-102.release33-lambda-source-rows-and-ticket-grant.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R24_G.md</decomp_doc> round 24, workstream ~G, cell `AR-g-102`.
<owned_cells>AR-g-102</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR102-g-AC1, AR102-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~201/IRPT_ANLREQ.TO-AR-g-102.release33-lambda-source-rows-and-ticket-grant.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-102`.
- Each acceptance entry's `invocation` is the criterion's text EXACTLY.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the two product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR102-g-AC1,AR102-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- for each of the seven re-pinned or new rows: the packaged_as, the new pin (first 10 hex) and sha256 (first 12 hex);
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the source map is read by `build-and-upload.sh`, `release-census.py`, `record-terraform-deploy.sh` and other lanes' builds; the two functions' rows and one files entry are the whole change, so a build of any OTHER function is unchanged (the check compares the whole map by content). The release delta this makes is exactly: `irpt-ycharts-generate` gains `ticket_confirmation.py` and changes `portfolio.py`, `uploads.py`, `acceptance.py`, `submission_service.py`, `generate_installed.py` (plus the two native members `normalized_input.py` and `prospect_submission.py` that already differ from the live zip), and `irpt-status` changes `status.py`. Hunk attribution since each row's old pin (git log, read by the issuer): portfolio.py three ANLREQ commits (AR-g-68 x2, AR-g-96); uploads.py three ANLREQ commits (AR-y-318, AR-g-95, AR-g-96); acceptance.py three commits, TWO ANLREQ (AR-g-67, AR-g-85) and ONE IRPT_BCKEND (IB-pr-478, `06557b6618`: the packager reads commentary_ref) that rides in; submission_service.py and generate_installed.py one ANLREQ commit each (AR-g-67); status.py one (AR-g-96). Nothing is deployed: the shipping is the r33 applier's.
comp-iam: RUN (by reading) -- DECLARES one inline policy on `irpt-ycharts-generate-role`: Allow `dynamodb:GetItem` on `table/opal-tickets` only (no index, no wildcard, no write). The table has no customer-managed key (read in `infra/aws/terraform/ticket-center/main.tf`). The role's aggregate inline size is the applier's plan to read (the custody-factory policy was split out for the same cap). NOT applied here; `safe-apply` and a simulate battery belong to the applier's order under the pair. NOT seen (blind): the live role's current inline policies and their aggregate size until the applier's plan; denominator: 1 policy, 1 statement, 1 action, 1 resource.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against CTO msg 8658 and the R42 lesson (other seats' merged work rides a shared zip): a pin that is not the last commit touching the file (so the package ships an older blob than HEAD's, or a newer one than reviewed); a sha256 that does not match its pin; a re-pin of an unrelated row (the check compares the whole map by content); a CRLF or re-indented map; the new member in the zip but not in `files` (or the reverse); an extra IAM action, an index or a wildcard on the table; a second statement; the environment variable on the wrong module; any other line of `generate.tf` changed. The checker feeds a green arm (a reference build passes the 15 cases) and 18 mutant arms, each of which fails the check.
</preflight>

- Cut on CTO msg 8658 and the issuer's reference build in a scratch tree. Risk WORLD: the floor of an infrastructure path (a Terraform file and the source map); source declarations only, nothing applied. Base: `AR102-g-AC1` FAILs (11 of 15 cases) and `AR102-g-AC2` PASSes, as expected.
- Release shape (for the r33 pair, not this cell): `release-census.py irpt-ycharts-generate --pin <the r33 pin>` against the live zip must print `changed_members=8` (the five re-pinned, the two natives, the one added) and `irpt-status` `changed_members=1`; anything else is a STOP at the applier. The IAM statement is shared-resource work: the CVO's single-executor-per-artifact ruling (@32f2f026ae) sequences it with any other apply on the generate role.
