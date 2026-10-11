# TO IRPT_BCKEND.TO-IB-pr-460 -- BUILD, nothing released: the draft store's persist answer carries `ticket_id` when the accepted record has one; and the release read for that one function

<to_id>IRPT_BCKEND.TO-IB-pr-460</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~316</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>156</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msgs 6024 and 6033 (PRD v0.45 @9de9ab8cf2, ratified-text half SIGNED @83e8664d75) | **Decomp cell:** `IB-pr-460` (decomposition section 148) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-316/` (bash `/c/dev/wk-irpt-bckend-316`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit`. Two parts, in order. **Part A edits ONE product file and adds tests. Part B is BUILD ONLY plus AWS
reads.** In neither: no upload, no apply, no deploy, no terraform, no edit of the real source map, NO invoke of any function, no
vendor call.

**The contract.** Read PRD ADDENDUM v0.45 whole (the last section of
`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`) and the read it was written from,
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~314/IB154-1_DRAFT_STORE_PERSIST_ANSWER_READ.md`:

> On a first persist that answers `status` OK, the answer carries a third member, `ticket_id`, equal to the accepted record's
> `ticket_id`, WHEN the record carries one. When the record carries none, the member is absent (not null, not empty): the answer
> is then exactly today's. A replay and a refusal are unchanged and carry no `ticket_id`.

The member is a pointer. The store reads no ticket and gains no grant. Its one consumer is the commentary drafter
(`data/transcripts/scripts/commentary/lambda_handler.py:114`, `:131-138`), which copies three keys and ignores any other; you
do NOT edit the drafter (another seat's cell, after this function's release).

### Part A -- build, in `infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py` only

- `resolve_request` (lines 112-124 today) already holds the accepted record at line 115 and returns `(tenant, owner)`. Carry the
  record's `ticket_id` out of that SAME read (no second read of anything) and put it on the answer `store` returns at line 171,
  the first-persist OK answer, when the record's `ticket_id` is a non-empty string; otherwise add nothing. `get_ref` (line 154),
  a replay (`ALREADY_WRITTEN`) and every refusal are unchanged. The crash-recovery branch (lines 161-166) returns through line
  171 and is a first persist that answers OK: it carries the member too; say so in your report, and if the addendum reads
  otherwise to you, stop and file a row.
- `resolve_request` is imported or called elsewhere? Find every caller with the native Grep tool BEFORE you change its return;
  a caller outside this file that unpacks two values is a row and a design choice you report (prefer a change that leaves the
  two-value return intact, e.g. a second small function over the same record, if any other caller exists).
- The value is copied as the record holds it. No format check is added here (the format is checked at submission), no ticket
  is read, no new import of a ticket module, no IAM or Terraform change.
- **Tests:** a NEW file `infra/aws/lambda/investor-reporting/reports/tests/test_commentary_draft_store_ticket_id.py`, using the
  existing test file's fakes (import them; do not copy-edit that file). **DO NOT EDIT
  `tests/test_commentary_draft_store.py`**: it pins the exact key set of every answer for records with no ticket id, and it
  passing unchanged IS the proof that such an answer equals today's (criterion AC3 hashes it). Your tests: a first persist for
  a record WITH a ticket id carries `ticket_id` equal to the record's; WITHOUT one the answer is exactly `{status,
  commentary_ref}`; `ticket_id` present but empty, `None` or not a string on the record adds nothing; a replay, each refusal
  and `get_ref` carry no `ticket_id` whether or not the record has one; the crash-recovery branch carries it; `requests.get` is
  called exactly once per persist (count it on the fake). The test also WRITES
  `tests/commentary_draft_store_answers.json` (sorted keys, `\\n` newlines, ASCII, byte-identical on re-run): exactly the keys
  `first_persist_with_ticket_id`, `first_persist_without_ticket_id`, `replay`, `refusal`, `get_ref` (each the answer object as
  returned) and `record_ticket_id` (the planted id, a synthetic `TCK-` id of the estate's shape; planted ids only, no firm name).

### Part B -- the release read for `irpt-commentary-draft-store-lambda` (model: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~312/`, its scripts, `candidate_repins.json`, `replay/` and packet; copy and adapt, leave it untouched)

After Part A is COMMITTED on your branch (the pin is that commit):
1. Live: `lambda get-function-configuration` and one `get-function` download of `irpt-commentary-draft-store-lambda` (through
   `.tools/aws`; the link used once, never written); `live_code_sha256`; the rollback version of its artifact key by content
   (`rollback_version_id`). Scratch OUTSIDE the worktree (`C:/dev/_scratch316/`), deleted file by file at the end; a package is
   data.
2. A MINIMAL candidate map (never the real map): in this function's entry, ONLY the row(s) that pin
   `commentary_draft_store.py` re-pinned to your Part A commit, sha256 recomputed from `git show`. Commit the re-pin DIFF and
   the generator, not a full copy of the map (the full map names firms).
3. Build twice with `BAU_SOURCE_MAP_OVERRIDE=<candidate> BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh
   investor-reporting irpt-commentary-draft-store-lambda` (`TMPDIR` in scratch; confirm in the script what `BUILD_ONLY=1`
   skips before running; `git status --short` after each build). Byte-identical, or say why.
4. `moved_members`: EVERY member whose bytes differ between live and built: `member`, `owning_commits` (every commit between
   the live blob and the built blob on that path), `class` (`served` / `inert`, unsure is `served`), `one_line`,
   `is_this_change` (true only if its owning commits are this cell's alone; a member that is this change's file but ALSO
   carries earlier unreleased commits is `is_this_change: true` with those commits listed and named in `one_line`), and
   `serves` (which contract or cell each owning commit belongs to, by its subject). `riders` = the moved members with
   `is_this_change` false. The CTO's note: this function was one of three NOT released for `commentary_requested`; say whether
   the minimal candidate leaves `acceptance.py` and `submission.py` at their live pins (it should, since only the store's row
   is re-pinned) and what would ride if they were not.
5. `replay.arms` (live zip against built zip, offline, in-memory fakes): a first persist for a record with NO ticket id is
   byte-identical on both (`record_has_ticket_id: false`, `identical`); for a record WITH one, live answers today's two
   members and built adds `ticket_id` (`record_has_ticket_id: true`, `expected-diff`); a replay and each refusal identical;
   `get_ref` identical; one or more `negative_control` arms.
6. `consumer`: `{name, code_line, on_the_new_member, read_the_pair_makes_through_it}`: the drafter, what it does with the new
   member today (ignores it: cite the line), and the ONE read that would show after a release that the drafter still persists
   and reads the ref (an existing path and what to look at, or an offline arm, said plainly). Also `who_may_invoke` (from
   Terraform: the invoke policy and the role it is attached to).
7. The packet `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-460.md` in IB-pr-456's form: digests, rollback version, every moved member with
   its commits and what each serves, riders, Branch A and Branch B, the after-read proposed (no draft is persisted to test a
   release unless a seat can say whose request it is: propose reads that persist nothing, and say what then stays
   unexercised), what is not exercised. Do NOT write which ratified outcome each change serves beyond `serves` as defined
   above, and recommend nothing on timing.

**Output of Part B:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~316/IB156-1_release_read.json` with
`{function: "irpt-commentary-draft-store-lambda", base_commit, pin, live_code_sha256, live_read_at_utc, rollback_version_id,
build:{outcome, built_sha256, built_twice_identical}, moved_members:[...], riders:[...], added_members, removed_members,
replay:{arms:[...]}, consumer:{...}, who_may_invoke, not_exercised:[...], uploads_made:0, applies_made:0,
real_source_map_edits:0, vendor_calls_made:0, functions_invoked:0}`.

<criterion id="IB156-1-AC1" cell_refs="IB-pr-460"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r156/p156_cells.py" . IB156-1-AC1</invocation><expect>IB156-1-AC1 PASS</expect></criterion>
<criterion id="IB156-1-AC2" cell_refs="IB-pr-460"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r156/p156_cells.py" . IB156-1-AC2</invocation><expect>IB156-1-AC2 PASS</expect></criterion>
<criterion id="IB156-1-AC3" cell_refs="IB-pr-460"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r156/p156_cells.py" . IB156-1-AC3</invocation><expect>IB156-1-AC3 PASS</expect></criterion>

<expected_criteria>IB156-1-AC1, IB156-1-AC2, IB156-1-AC3</expected_criteria>

AC1 is the built behaviour; AC2 is the seam against the live package; AC3 is the CONTROL and passes today: the existing test
file is byte-identical and passes. It must still pass, unchanged, when you finish.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else.
- **Refusal clause:** a second caller of `resolve_request` that your change would break, the addendum and this face
  disagreeing, a candidate that does not build, or a criterion that cannot be met as written: stop, file a row and report.
  Never weaken a check; do not edit `p156_cells.py`; do not edit the existing test file.
- **Client data:** counts, sha256 and reason codes only in committed files; no firm name, no account id.
- **Row ids** are `IRPT_BCKEND-D2-W316-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- Every `.py` passes `bash .tools/commit-gate.sh <file>` before the commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~316" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~316@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~316 <0.9.0_WK_IRPT_BCKEND~316@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py
infra/aws/lambda/investor-reporting/reports/tests/test_commentary_draft_store_ticket_id.py
infra/aws/lambda/investor-reporting/reports/tests/commentary_draft_store_answers.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~316/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-460.draft-store-persist-answer-carries-ticket-id.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 148 (round 156, workstream ~P), cell `IB-pr-460`.
<owned_cells>IB-pr-460</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB156-1-AC1, IB156-1-AC2, IB156-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~316/IRPT_BCKEND.TO-IB-pr-460.draft-store-persist-answer-carries-ticket-id.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base and the pin; the lines changed and how the two-value return was kept or changed,
with every caller of `resolve_request` found; whether the crash-recovery branch carries the member; the test count; the live
and built digests and the rollback version; every moved member with its owning commits and what each serves, and the riders;
whether `acceptance.py` and `submission.py` stayed at their live pins; the replay arms; the consumer and the read through it;
the after-read you propose and what stays unexercised; `git status --short` after the builds; each criterion's last line; the
commit gate's and the proof checker's results; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; Part A edits one source file and adds tests in the tree; Part B IS the blast-radius read of the release (every moved member of the one function, its one consumer); nothing is uploaded or applied.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the store reads no ticket and gains no grant (PRD v0.45); the invoke policy is read from Terraform.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; the function is invoked directly by one role.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p156_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~23:3xZ: AC1 FAIL as expected (no test file), AC2 FAIL as expected (no record), AC3 PASS as expected (control: the existing test file's sha256 b3c192b6... and 10 passed); commit-gate clean. The issuer read commentary_draft_store.py:100-181 at HEAD and v0.45's addendum; the sign-off was read as a COMMIT (83e8664d75). The existing test file names no ticket (native read: 0 lines), so it passing unchanged is the no-ticket equality the CTO asked to be shown. WORLD by the L6 floor (paths under infra/); nothing released; no apply order follows without a signed pair.
lane: the <paths> block IS the grant.
</preflight>
