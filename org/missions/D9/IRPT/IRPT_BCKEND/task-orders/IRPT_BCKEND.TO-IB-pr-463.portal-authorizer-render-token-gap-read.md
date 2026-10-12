# TO IRPT_BCKEND.TO-IB-pr-463 -- READ ONLY: the portal authorizer's source is ahead of its recorded build input (a render-token path): what is live, what is unreleased, and whether anything served depends on it

<to_id>IRPT_BCKEND.TO-IB-pr-463</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~318</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>159</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6237 ("row TCKT_VNEXT-D2-S52 reads as yours") | **Decomp cell:** `IB-pr-463` (decomposition section 151) | **outcome_ref:** FWD-7

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-318/` (bash `/c/dev/wk-irpt-bckend-318`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it).

**HARD BOUNDS.** READ ONLY. The function is the PORTAL AUTHORIZER: every scoped portal API call passes through it. You do
NOT invoke it, do not call any route through it, do not sign in, do not build or upload anything, do not run terraform (not
even a plan), do not edit any product file or the source map, and you PROPOSE NO RELEASE: you describe what is live and what
is not. AWS reads allowed, through `.tools/aws`: `lambda get-function-configuration` (with `--query`; never print or record an
environment variable's VALUE: key names only) and ONE `lambda get-function` download of the authorizer's package (the link
used once, never written anywhere), plus the same two reads on ONE other function if a sender you find needs its live digest
compared. The downloaded package goes in a NEW EMPTY folder OUTSIDE the worktree (`C:/dev/_scratch318/pkg/`), your scripts
in a different folder; it is data: never run or import anything from it; read members with `zipfile` under `python -I`.
Delete the scratch file by file at the end with a short bounded script; if cleaning hangs or errors, stop cleaning, say so
and still report.

**What is known** (row `TCKT_VNEXT-D2-S52`; read it in
`org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md`): the source map's entry
`opal-portal-authorizer` (`infra/aws/lambda/ci/lambda-source-map.json`) records `last_deployed_commit` 26ffa22b79 and
`last_deployed_at` 2026-09-09; an applier measured the live CodeSha256 EQUAL to the map's `artifact_sha256`; the function's
LastModified is 2026-10-03, later than the map's date; and `infra/aws/users/lambda/portal-authorizer/index.mjs` is 450 lines at
HEAD against 262 at 26ffa22b79. Read by the issuer with `git log` on that file: four commits follow 26ffa22b79 on it:
`4bca50737e` (IB-rtq-2, 2026-09-22), `18971693ad` (IB-rtr-2, 2026-09-22), `972976ebca` (export section A, 2026-09-25),
`ee822c425f` (IB-pr-307, 2026-10-03: "the portal authorizer (V2) admits a render token on the 49F reporting ..."). Nobody has
read the DEPLOYED BYTES. The date of the last of them equals the function's LastModified date.

**Read and state:**
1. **`live`:** CodeSha256, LastModified, the downloaded bytes' base64 sha256 EQUAL to CodeSha256 (if not, stop and file a
   row), the member list; and the environment's KEY NAMES only (does a key that names a render public key or a render
   audience exist: `env_keys_naming_render`).
2. **`live_source_matches`:** compare the live `index.mjs` (and any other source member) BY CONTENT to the file's blob at
   every commit that touched it from 26ffa22b79 to HEAD (`git log --format=%H -- <path>`, then `git show <c>:<path>`,
   compared after normalising line endings, and say so): `revisions_compared`, `matched` and at which `commit`, or matched
   none (then the nearest by line diff, with the count of differing lines). `has_render_token_path`: do the functions the
   row names (`authorizeRenderToken` and its helpers) appear in the LIVE member.
3. **`commits_after_the_live_blob`:** each commit on the file after the matched one: `commit`, `date`, `order_or_cell`,
   `adds_in_words` (read the hunk with `git show <c> -- <path>`; one sentence).
4. **`map_entry`:** the source map's recorded fields for the function, and whether `build-and-upload.sh` is what deploys it
   (read `infra/aws/terraform/portal-auth/lambdas.tf` around lines 50-80: how the function's code is packaged and applied; a
   function built by terraform's own archive is not recorded by the map's recorder; say which it is, with the lines).
5. **`render_token_senders`** and **`routes_a_render_token_is_meant_to_pass`:** who MINTS or SENDS a render token (search
   the native Grep tool for `render` token minting and audience under `infra/aws/lambda/investor-reporting/` and
   `infra/aws/users/`; the export / PDF render path; the orders `IRPT_BCKEND.TO-IB-rtq-*`, `IB-rtr-*`, `IB-pr-307` under
   `org/missions/D9/IRPT/IRPT_BCKEND/task-orders/` say what the path is for); for each sender: `code_line`, whether the
   sender is LIVE today (its function's map entry and, if needed, one configuration read), and
   `what_it_gets_from_the_live_authorizer` today (by reading the LIVE authorizer member's code path for such a token:
   admitted, refused with which answer, or never sent). The routes the token is meant to pass, each with where it is
   declared (`declared_at`).
6. **`orders_that_built_the_unreleased_commits`:** each order (`order`, `status` from its file, `ledger_entry` = the path of
   a deploy ledger entry under `org/critical_paths/change_management/` that names the authorizer for it, or null; search by
   the function's name and by the order ids), and what each order's own face said about RELEASING the authorizer.
7. **`verdict`**, one of: `RELEASE_OWED_SOMETHING_SERVED_DEPENDS_ON_IT` (a live sender sends a token the live authorizer
   refuses or mishandles), `UNRELEASED_AND_NOTHING_SERVED_DEPENDS_ON_IT` (the path is in the tree only and no live sender
   needs it), `RELEASED_THE_RECORD_IS_BEHIND` (the live bytes carry the path and the map is stale), `CANNOT_BE_TOLD` (with
   `what_would_tell`); with its `claim` and `reason`. And `not_established`.

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~318/`: `IB159-1_authorizer_render_token_gap.json`
with the members named above plus `base_commit`, `searched_for`, `not_searched`, `functions_invoked: 0`, `aws_writes_made: 0`,
`sign_ins_made: 0`, `product_files_edited: 0`, `releases_proposed_as_orders: 0`; and a one-page
`IB159-1_AUTHORIZER_RENDER_TOKEN_GAP_READ.md` leading with the verdict.

<criterion id="IB159-1-AC1" cell_refs="IB-pr-463"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r159/p159_cells.py" . IB159-1-AC1</invocation><expect>IB159-1-AC1 PASS</expect></criterion>
<criterion id="IB159-1-AC2" cell_refs="IB-pr-463"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r159/p159_cells.py" . IB159-1-AC2</invocation><expect>IB159-1-AC2 PASS</expect></criterion>
<criterion id="IB159-1-AC3" cell_refs="IB-pr-463"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r159/p159_cells.py" . IB159-1-AC3</invocation><expect>IB159-1-AC3 PASS</expect></criterion>

<expected_criteria>IB159-1-AC1, IB159-1-AC2, IB159-1-AC3</expected_criteria>

The checks grade the shape: the live bytes read, the content match, the lists, one verdict of four, the five zeros. Which
verdict holds is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** an AWS read refused, the downloaded bytes not equal to CodeSha256, or a criterion that cannot be met as
  written: file a row and report. Never weaken a check; do not edit `p159_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W318-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~318" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~318@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~318 <0.9.0_WK_IRPT_BCKEND~318@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~318/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-463.portal-authorizer-render-token-gap-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 151 (round 159, workstream ~P), cell `IB-pr-463`.
<owned_cells>IB-pr-463</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB159-1-AC1, IB159-1-AC2, IB159-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~318/IRPT_BCKEND.TO-IB-pr-463.portal-authorizer-render-token-gap-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the live digest and that the bytes equal it; which commit's blob the live source
matches, and whether it carries the render-token path; each commit after it with its order and what it adds; how the function
is packaged and whether the map's recorder sees it; the senders and routes, what each gets from the live authorizer today;
the orders behind the unreleased commits, their status and ledger entries; the verdict with its claim and reason; what is not
established; each criterion's last line; the proof checker's result; commit hashes; row ids; whether the scratch was cleaned.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read written to the worker's own deliverables folder; the authorizer is not invoked, built, planned or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; get-function and get-function-configuration are reads.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; route declarations are read.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p159_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~01:2xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. Read by the issuer before the cut: row TCKT_VNEXT-D2-S52 whole; `git log` on the authorizer's file (four commits after 26ffa22b79, the last IB-pr-307 on 2026-10-03, the function's LastModified date); the map entry's recorded fields. The account-id test of earlier checks is NOT in this check (three defects of that pattern today); the face keeps values out by its bounds. The face forbids invoking the authorizer and proposing a release.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
