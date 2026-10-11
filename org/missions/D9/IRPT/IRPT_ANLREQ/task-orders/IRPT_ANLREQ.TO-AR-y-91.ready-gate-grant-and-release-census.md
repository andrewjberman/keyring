# TO IRPT_ANLREQ.TO-AR-y-91 -- the READY gate's role grant written in Terraform, and the release census of the composition-read function

<to_id>IRPT_ANLREQ.TO-AR-y-91</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~53</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (Terraform text, and one live single-resource read of a function's package). NOTHING is applied, uploaded, planned against live state or invoked by this order.
**Decomp cell:** `AR-y-91` (`decompositions/IRPT_ANLREQ_DECOMP_R9_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~53`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-53` (branch `wk-IRPT_ANLREQ-53`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~53 <0.9.0_WK_IRPT_ANLREQ~53@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing. The worktree shows ` M portal`:
  never commit it.
- **A HOLD binds you and every seat:** nobody builds-and-uploads `irpt-commentary-composition-read-lambda` until this round's pair is
  signed and its apply order is cut. Every build here is `BUILD_ONLY=1`. Without `BUILD_ONLY=1` the build script UPLOADS: never run it so.

### THE CELL (`AR-y-91`, inlined)

*(a) The role grant WRITTEN in Terraform, not applied. (b) The release CENSUS of the composition-read function.*

Why. A gate was merged into `infra/aws/lambda/investor-reporting/reports/commentary_composition.py` (commit `d6824da73a`): before it
answers, the composition read now reads the request's JOB row and refuses unless the job reads READY. The function's role can read
only the requests table, so a rebuilt function would refuse every read. The release therefore applies the GRANT FIRST and the code
second, in one pair. This cell prepares both halves' evidence. It applies nothing.

**Part (a) -- the grant, in `infra/aws/terraform/investor-reporting/export/commentary_composition.tf` (statements at about lines 62-71).**
- `S1...` (the `dynamodb:GetItem` statement): add the JOBS table's ARN to `Resource`, built exactly as the requests table's ARN is
  (the same expression with `tables.jobs`; confirm the `core` remote state exports `tables.jobs` by reading
  `infra/aws/terraform/investor-reporting/core/` -- the file that declares the `tables` output -- and cite the line). The Action stays
  exactly `dynamodb:GetItem`. The `LeadingKeys` condition stays as it is and now covers both tables: read the jobs table's key schema
  (`core/dynamodb.tf`) and say whether its partition key is the tenant, as the condition assumes; if it is not, STOP part (a), file a
  row, and say what the condition would have to be.
- `S2...` (the `kms:Decrypt` statement): its condition on `kms:EncryptionContext:aws:dynamodb:tableName` names the requests table.
  Make it name BOTH tables (a list value under the same `StringEquals` key). Confirm the jobs table uses the same KMS key the
  statement's `Resource` names (cite the line); if it uses another key, say so and add nothing you cannot justify from the files.
- Change nothing else in the file: no other statement, no other resource. Run `terraform fmt -check` on the file if `terraform` is on
  the path (report its result or that it is not available). Do NOT run `terraform init`, `plan` or `apply`.

**Part (b) -- the census, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r9/COMPOSITION_READ_RELEASE_CENSUS.json`.**
1. **The live package.** `.tools/aws lambda get-function --function-name irpt-commentary-composition-read-lambda` returns a
   `Code.Location` link. Use it ONCE, in the same command, to download the zip into a temp folder OUTSIDE the worktree; NEVER print,
   log, write or report the link. Record `Configuration.CodeSha256` and `LastModified`, and check the downloaded file's base64 sha256
   equals that `CodeSha256` (if not, STOP and say so). Hash every member (sha256 hex). Delete the zip when you are done.
2. **The live blob of the gated file.** For the live zip's `commentary_composition.py`: find the commit whose blob has exactly those
   bytes -- `git log --format=%H -- infra/aws/lambda/investor-reporting/reports/commentary_composition.py`, then for each commit
   compare `git show <c>:<path>` bytes' sha256 with the live member's. Record the first (oldest) and last (newest) commit that match,
   or `found: false` with how many commits you compared. Compare the bytes, never the file name or a commit message.
3. **Every other live member** against (i) the blob at its pin in the function's source-map entry
   (`infra/aws/lambda/ci/lambda-source-map.json`, `functions["irpt-commentary-composition-read-lambda"]`: `files` and `staged_from`)
   and (ii) the blob at this branch's HEAD: say which it equals.
4. **The trunk build.** This function builds only with the parity skip (a known defect, not yours): `BUILD_ONLY=1 BAU_PARITY_SKIP=1`
   and `TMPDIR` outside the worktree, `bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-commentary-composition-read-lambda`,
   TWICE; the two digests must be equal. Diff its members against the live zip.
5. **Write the census:**
   `{"read_at": "<UTC>", "tree_head": "<short hash>", "live": {"code_sha256": "...", "last_modified": "...", "member_count": <n>,
   "members": {"<name>": "<sha256 hex>", ...}}, "gated_file_live_blob": {"found": true|false, "sha256": "...", "commit": "<newest
   matching>", "oldest_matching_commit": "...", "searched": "<what, how many commits>"}, "members_vs_pins": [{"packaged_as": "...",
   "equals_pin": true|false|null, "equals_head": true|false, "pin": "<hash or null>"}, ...], "build": {"sha256_first": "...",
   "sha256_second": "...", "members": <n>, "changed_members_vs_live": ["..."], "added": [...], "removed": [...], "parity_skip": true},
   "moved_members": [{"packaged_as": "...", "owning_commits": ["<short hash> <author>", ...], "served_effect": "CHANGES_ANSWER"|"INERT",
   "why": "<two sentences with file and line>", "claim": "measured"|"inferred"}, ...], "map_corrections_needed": ["<field: has ->
   should read, at the release>", ...]}`. `moved_members` has ONE row for EACH name in `changed_members_vs_live`.
   `map_corrections_needed` lists what the entry records wrongly about the LIVE function today (for example a missing
   `last_deployed_commit`); you do NOT edit the map.
6. Commit the Terraform file and the census (one commit or two).

### ACCEPTANCE

<criterion id="AR91-y-AC1" cell_refs="AR-y-91"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r9/ar9_checks.py y91-grant --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y91-GRANT-OK</expect></criterion>
`AR91-y-AC1`: S1 and S2 each name the requests table AND the jobs table; S1's Action list is exactly GetItem; both conditions remain.
It reads Terraform text: it shows the grant is written, never that it is applied.

<criterion id="AR91-y-AC2" cell_refs="AR-y-91"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r9/ar9_checks.py y91-census --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y91-CENSUS-OK</expect></criterion>
`AR91-y-AC2`: the census holds the live members, the gated file's live blob (found, or not found with what was searched), two equal
build digests, and one complete row per changed member.

<expected_criteria>AR91-y-AC1 AR91-y-AC2</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/` and this order's
  file (status flip only).
- READ only: everything else, `infra/aws/lambda/ci/` included (do NOT edit the source map).
- Live: exactly ONE `get-function` on that one function and the one download it enables. No list call, no invoke, no upload, no
  plan, no apply. The signed link is never printed, logged, written or reported. No non-ASCII in what you add.

<paths>
infra/aws/terraform/investor-reporting/export/commentary_composition.tf
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R9_Y.md</decomp_doc>
<owned_cells>AR-y-91</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR91-y-AC1 AR91-y-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/IRPT_ANLREQ.TO-AR-y-91.ready-gate-grant-and-release-census.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-91`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR91-y-AC1,AR91-y-AC2`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading: 1 policy document of 5 statements (read by the issuer, lines 55-85) and the function's source-map entry (6 files[] members shown, 12 pinned rows counted); NOT seen: the core remote state's outputs and the jobs table's key schema and key (the worker reads and cites them; a mismatch stops part (a)). comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: RUN -- by reading 1 role policy: the edit ADDS one table to a GetItem statement under an unchanged LeadingKeys condition and one table to a kms context list; no new action, no new principal. It is written and NOT applied here; the apply is the release pair's first step.
comp-adversary: RUN -- by reading 1 statement pair; the lens: a grant wider than the gate needs (a second action, a dropped condition), or a census that names a commit by file name instead of bytes. The check refuses the first; the face orders the second compared by sha256. NOT seen: whether LeadingKeys fits the jobs table's partition key.
lane: one Terraform file, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on CTO msg 5208 (row `IRPT_ANLREQ-D2-S53`, ARMED). `AR91-y-AC1` base: FAIL as expected (neither statement names the jobs table).
  `AR91-y-AC2` base: FAIL as expected (no census).
- The pair and the apply order are the issuer's, written on this census.
- Seating: slot ~53 is reused; its earlier order is terminal.
