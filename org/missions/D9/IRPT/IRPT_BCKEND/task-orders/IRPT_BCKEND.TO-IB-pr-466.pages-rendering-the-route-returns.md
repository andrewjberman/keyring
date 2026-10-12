# TO IRPT_BCKEND.TO-IB-pr-466 -- READ ONLY: the pages that render the performance route's returns, and what each shows of the claim, the absences and the excluded days

<to_id>IRPT_BCKEND.TO-IB-pr-466</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~321</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>160</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6245 (PRD v0.46 @3f577ef37f: "three reads before any cell, no build") | **Decomp cell:** `IB-pr-466` (decomposition section 152) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-321/` (bash `/c/dev/wk-irpt-bckend-321`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it). **A READ, NOT A BUILD.** You edit no product file and propose no build or fix.

**Why.** Read PRD ADDENDUM v0.46 (the last section of `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`), its closing bullet,
and the consumer list of `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~313/IB153-1_producer_design_read.json`
(`consumers`; its last entry says the portal pages that render the route's returns were NOT classified). The performance
route's reader returns, with each figure, a `claim`, a list of `absences` and `days_excluded`; over a window with a non-OK day
it still says `measured`. What a person SEES of that depends on the pages. This read lists them.

**HARD BOUNDS.** A CODE READ. The portal submodule is EMPTY in your worktree: read the portal READ ONLY at
`C:/dev/ajb_workspace/portal/` with the native Grep/Glob/Read tools, record `portal_checkout` (that path) and `portal_commit`
(`git -C C:/dev/ajb_workspace/portal rev-parse HEAD`), and say plainly it is another checkout at its own commit, which may be
ahead of or behind what is served. You edit nothing there or anywhere, run no dev server, open no page in a browser, sign in
nowhere, call no API.

**Read and state:**
1. The route and its payload: from `infra/aws/lambda/investor-reporting/performance/` (`holdings_gold.py` `calculate`, about
   lines 212-320, and the entry that serves it) and the contract under `docs/contracts/investor-reporting/v1/` (the
   performance report schema): the route's path, and the payload's members that carry the figure, the `claim`, the `absences`
   and `days_excluded` (their exact names and where each is declared: `payload_members`, each with file:line).
2. `files_naming_the_route_or_its_payload`: by subtraction over the portal checkout: every file that names the route's path,
   its client function, its wire type or one of those payload members (`searched_for`: the exact patterns); `total`, and each
   file placed as `render` (it puts a value on the screen), `fetch_or_adapt` (client, adapter, type, hook) or `neither`
   (tests, fixtures, stories, docs), summing to `total`.
3. `pages`: each page or component that renders the route's returns: `page_or_component`, `code_line`, `what_it_renders` (the
   figure, the period, a chart), `shows_claim` (how the claim reaches the screen, or `not shown`, with the line),
   `shows_absences` (likewise), `shows_days_excluded` (likewise), and `which_firms_can_open_it` if the code says (a route guard
   or a firm switch; else `not told`).
4. The adapter between wire and page (where the payload is reshaped): does it DROP `days_excluded`, the claim or the absences
   before the page sees them (`adapter_drops`: each member with kept or dropped and the line).
5. `not_searched` (anything you did not read: other front ends, the reporting PDF or export path if it also prints returns,
   generated files) and `not_established` (what is served today versus this checkout; what a signed-in firm user actually
   sees).

**Outputs** in `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~321/`: `IB160-3_pages_rendering_returns.json` with
the members named above plus `base_commit`, `portal_checkout`, `portal_commit`, `product_files_edited:0`, `sign_ins_made:0`,
`pages_opened_in_a_browser:0`; and a one-page `IB160-3_PAGES_RENDERING_RETURNS_READ.md`: one row per page, the three "shows"
columns first.

<criterion id="IB160-3-AC1" cell_refs="IB-pr-466"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r160/p160_cells.py" . IB160-3-AC1</invocation><expect>IB160-3-AC1 PASS</expect></criterion>
<criterion id="IB160-3-AC2" cell_refs="IB-pr-466"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r160/p160_cells.py" . IB160-3-AC2</invocation><expect>IB160-3-AC2 PASS</expect></criterion>

<expected_criteria>IB160-3-AC1, IB160-3-AC2</expected_criteria>

The checks grade the shape, the sums and the bounds. Every count and answer is UNMEASURED by the issuer; "none found" and
"cannot be told" pass where true.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No product file is edited.
- **Refusal clause:** an AWS read refused (record it as a reading; never retry another way; seek no grant) or a criterion that
  cannot be met as written: file a row and report. Never weaken a check; do not edit `p160_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W321-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Scratch** in `C:/dev/_scratch321/`, outside the worktree, removed at the very end by a short bounded python script; if the
  cleanup hangs or errors, stop cleaning, say so, and still report.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~321" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~321@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~321 <0.9.0_WK_IRPT_BCKEND~321@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~321/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-466.pages-rendering-the-route-returns.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 152 (round 160, workstream ~P), cell `IB-pr-466`.
<owned_cells>IB-pr-466</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB160-3-AC1, IB160-3-AC2. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~321/IRPT_BCKEND.TO-IB-pr-466.pages-rendering-the-route-returns.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base and the portal commit; the route and the payload members; the subtraction's counts; each page with what it shows of the claim, the absences and the excluded days; what the adapter drops; what was not searched and not established; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a read written to the worker's own deliverables folder; nothing is edited, built, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; reads only; a refused read is a reading.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; no deployed route is called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p160_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~01:4xZ: every criterion of this order FAIL (no file); commit-gate clean. The issuer read IB-pr-457's consumer list (the page entry reads NOT READ) and PRD v0.46's closing bullet; it read no portal file. The account-id text test is not in this check (three false failures of that pattern on 2026-10-11); the bounds keep values out.
lane: the <paths> block IS the grant. DIRECT-ACT (one read-only cell, LOCAL: records only).
</preflight>
