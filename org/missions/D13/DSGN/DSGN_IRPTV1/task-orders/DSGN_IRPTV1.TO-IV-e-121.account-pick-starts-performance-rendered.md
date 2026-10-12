# TO DSGN_IRPTV1.TO-IV-e-121 -- an ACCOUNT row picked in the header starts Performance's Account select on that account and Holdings opens on it, proven on a RENDERED page; the record says which row kind the header yields -- a product change only if the rendered proof fails; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-121</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~69</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>31</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6625 (2026-10-12 ~22:03Z), section 1 row D2-S24: "A page cell, proven on a RENDERED page with an account row picked, never a test alone." | **Rows:** D2-S24 | **Decomp cell:** `IV-e-121` (decomposition v31) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** none (portal DEV 183860bac055 is the base).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-69` (branch `wk-dsgn-irptv1-r31-69`); run everything from its root unless a step says the
portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~69/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-69/portal` is a PORTAL worktree (its own git repo) at portal DEV `183860bac055`. Do not amend or revert anything
committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the
workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` here is a LINK to the
main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run,
then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file that has no uncommitted work of yours. ONE whole-scope
run before any edit (`bun test src/pages/InvestorReporting`, output to a file under
`C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~69/`) is your base for `new_failing_ids`; the issuer measured it at this base as
1203 pass, 27 skip, 1 fail (F14-AC3, a diff check against DEV 1f3ce9f0, a known base failure).

**What is claimed, and what is not shown.** IV-e-108 (portal cd744428) states that when the header's selection is an ACCOUNT row, Performance's Account
select starts from that account and Holdings opens on it. The mechanism, from its record
(`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~60/HOLDINGS_FACE.json`, key `header_picker`): Holdings opens on the header's ACCOUNT row
through `pickedAccountRef` (`tabs/holdings/HoldingsTab.tsx`); Performance's Account select starts from it through `headerPickedAccountId()` in
`tabs/reporting/accountFocus.ts`, used by `ReportingTab`'s preselect effect ahead of the largest account; an id the account list does not hold is not used.
It was held by a rendered unit test and a pure-rule arm only. A laptop walk (the issuer's row D2-S24 in
`org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md`, search the row id) typed an account's last four digits, picked the one
option offered, and saw Performance's Account select start on the client's OTHER, larger account; the walker's own earlier select loop may have caused it, so
the read is not clean. NOT established: whether the option the header offers for that search IS an account row or a client row labelled with an account.

**The cell (`IV-e-121`).**
1. **What the header yields.** Read `header/search.ts`, `header/ClientSearch.tsx`, `header/selectionRequest.ts` and `header/HeaderSelectionContext.ts`: for a
   search by an account's last four digits, does the option the header offers carry an ACCOUNT row or a CLIENT row, and what selection does a pick hand on?
   Record `header_yields` (`ACCOUNT_ROW` or `CLIENT_ROW`) and `header_basis` (the files and lines).
2. **The rendered proof.** Render the real page (the `Page` / `index.tsx` mount under the project's rendered-test harness or a dev server of YOUR worktree on a
   port other than 5174) with a synthetic client of TWO accounts, the second the larger, and the header's selection an ACCOUNT row naming the smaller one.
   Read, from the rendered DOM and one screenshot you read: the Performance tab's Account select value is the picked (smaller) account; the Holdings tab opens
   on that account. Record `rendered` {account_select_starts_on_picked, holdings_opens_on_picked, row_kind_rendered "ACCOUNT_ROW"}. The proof must NOT run a
   select loop that could leave the account selected: the page starts clean from the pick.
3. **If the proof fails,** the page is wrong: fix it inside the grant (`tabs/reporting/`, `header/`, `index.tsx`), re-run the proof, and record
   `product_change true` with `product_files_changed`. If Holdings is the one that fails, the cause is in `tabs/holdings/`, which is another cell's file this
   round (IV-e-120): do NOT edit it; file a BLOCKING row naming the file and the line and finish the rest. If the proof passes at the base, record
   `product_change false` and `product_files_changed []`; the only files you then add are the test and the record.
4. **The test and the suite.** One rendered test `__tests__/dsgn-irptv1/iv-e-121.account-pick-rendered.test.tsx` holding the case you proved, one temporary
   mutant (drop the preselect from the picked account) that the test catches, then reverted. `suite_base`, `suite_after` {pass, skip, fail, new_failing_ids},
   `lint_errors`, `typecheck_errors` (run `bun run lint` and `bun run typecheck` after your last portal commit), `portal_commit` (40 hex), `screenshots`,
   `screenshot_read`. Record everything in `ACCOUNT_PICK_RENDERED.json` with the keys named in the criterion below.

<criterion id="IV121-AC1" cell_refs="IV-e-121"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r31/p31_round31.py" . IV121-AC1</invocation><expect>IV121-AC1 PASS</expect></criterion>
`IV121-AC1` -- the record says what the header yields for an account search, a RENDERED page with an ACCOUNT row picked shows Performance's Account select on that account and Holdings on it, a rendered test and a mutant hold it, and a screenshot was read. Base: FAIL (no record).

<expected_criteria>IV121-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `tabs/holdings/` (IV-e-120's) and every file under `contracts/wire/`
  (generated). No file the other two cells of this round name is edited by you.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no secret read, no `bun install`, no package change.
  A dev server is allowed only for your own screenshot, on a port other than 5174, started from YOUR worktree and stopped when you finish.
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order
  did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W69-S<k>`, with the real current UTC time; append as BYTES, never re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~69/
portal/src/pages/InvestorReporting/tabs/reporting/
portal/src/pages/InvestorReporting/header/
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-121.*
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-121.account-pick-starts-performance-rendered.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v31 (round 31), cell `IV-e-121`.
<owned_cells>IV-e-121</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV121-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~69/DSGN_IRPTV1.TO-IV-e-121.account-pick-starts-performance-rendered.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV121-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; what the header yields for an account search and the lines that say so; what the rendered
page showed (the select's value, the Holdings account), whether a product change was needed and what; the test and its mutant; lint, typecheck, and the suite
before and after; what the screenshot shows; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; the cell proves a claim on a rendered page and changes the page only if the proof fails. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
