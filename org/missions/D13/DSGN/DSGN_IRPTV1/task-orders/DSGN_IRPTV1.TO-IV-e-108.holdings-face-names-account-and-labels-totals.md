# TO DSGN_IRPTV1.TO-IV-e-108 -- the Holdings face names the picked account and labels each total with its base; the header's picker hands the tabs the picked account -- a product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-108</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~60</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-23 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_23_20261011.md` @b417e9ee3c, section 4 item 3, answering `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/remediations/REMEDIATION_v9.md` @d0092958d1 | **Rows:** DSGN_IRPTV1-D2-S14, DSGN_IRPTV1-D2-W53-S5 | **Decomp cell:** `IV-e-108` (decomposition v23) | **outcome_ref:** FWD-1 (the Holdings hop) | **depends_on:** none; slot B, beside IV-e-106.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-57` (the slot's worktree; branch `wk-dsgn-irptv1-r21-57`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~60/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-57/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` is a real local install that another worktree junctions to: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~60/`) is your base for `new_failing_ids`.

**What is wrong (rows D2-S14 and D2-W53-S5).** Opened on a picked account, the Holdings face shows two totals with no label between them
(the Identity band's household figure over all accounts, and Total Assets for the one account), and names the picked account nowhere. And
two things are called a picker: the header's Client search yields `HeaderSelection` (an ACCOUNT row narrows it), while the Account select
the walks used is the Performance tab's own (`AccountFilter`, `tabs/reporting/ReportingTab.tsx`, `focusedAccountId`), whose choice is
tab-local: nothing hands it to Holdings.

**The cell (`IV-e-108`).** Read both rows whole, and the ~53 worker's record and screenshots
(`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~53/`), before any edit. Read `portal/CLAUDE.md` (Color law) and
`portal/DESIGN.md`: a label is navy text on the canvas or on a white panel; no new band, no new colour.
1. **The picked account is named** on the Holdings face when one account is in scope: its masked label as the page already prints it
   elsewhere (the `****1111 / Trust` form), in a sentence or a caption a reader meets before the totals. With no account picked, the face
   says it covers all accounts and how many. `picked_account_named` {where {file, line}, text}.
2. **Each total says what it is a total of.** The Identity band's figure and the Holdings total each carry a short label of their base
   (for example "all 2 accounts" and "this account"), from data the page already holds; no new request. `totals_labelled`: [{total,
   label, file, line}].
3. **The header's picker hands the tabs the picked account.** When the header selection is an ACCOUNT row, Holdings (and any tab that
   scopes by account) opens on that account, and the Performance tab's own Account select starts from it instead of from nothing. Find
   the smallest change that does it through the existing `HeaderSelectionContext`. If the server answers with the whole set whatever
   the header picked, or the change needs a contract or route change, do NOT widen: `header_picker` {hands_tabs: false, how, reason, row}
   with a row, and parts 1 and 2 still land. Otherwise {hands_tabs: true, how}.
4. **A rendered test** under `__tests__/dsgn-irptv1/` (a two-account client: unpicked, and one account picked through the header) holding
   the account's name and both labels, with one temporary mutant. `test` {id, passes, mutant {what, failed}}.
5. **Screenshots, read by you** (Read tool): the face unpicked and with an account picked, from a build, by the corrected driver
   `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~58/holdings-face-driver.fixed.mjs` (copy it to your folder; it copies the
   nodes before rewriting them, which the earlier driver did not). Synthetic data only. `screenshots` (file names in your folder) and
   `screenshots_read` (the same names, each read). Say what each shows in a sentence.
6. `lint_errors`, `typecheck_errors`, `suite_after`, `product_files_changed`, `portal_commit`.

<criterion id="IV108-AC1" cell_refs="IV-e-108"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r23/p23_round23.py" . IV108-AC1</invocation><expect>IV108-AC1 PASS</expect></criterion>
`IV108-AC1` -- the Holdings face names the picked account and labels each total, the header's picker hands the tabs the account or the reason it cannot is a row, a rendered test holds it, and two screenshots were read. Base: FAIL.

<expected_criteria>IV108-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. The contract and the producer's fixtures (workspace files)
  are read, never edited. No file under `contracts/wire/` is hand-edited (generated; one command regenerates it:
  `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts`).
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no
  `bun install`, no package change, no dev server on any port.
- **Every portal commit is followed by `bun run lint` and `bun run typecheck`**; a lint ERROR is fixed before you report (the count goes in
  the record as `lint_errors`, and typecheck's as `typecheck_errors`).
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W60-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~60/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-108.holdings-face-names-account-and-labels-totals.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v23 (round 23), cell `IV-e-108`.
<owned_cells>IV-e-108</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV108-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~60/DSGN_IRPTV1.TO-IV-e-108.holdings-face-names-account-and-labels-totals.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV108-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; where the account is named and its text; each total and its label; whether the header's picker now hands the tabs the account, how, or why not; the test and its mutant; what each screenshot shows; `product_files_changed`; lint, typecheck and suite; the portal commit; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; labels and one selection hand-off on a client-facing page, with a rendered test; no request, route or contract change. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
