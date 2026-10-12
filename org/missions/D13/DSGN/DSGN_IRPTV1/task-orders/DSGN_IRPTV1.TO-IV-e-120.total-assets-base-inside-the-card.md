# TO DSGN_IRPTV1.TO-IV-e-120 -- the Total Assets base sits inside the card the shared CategoryViewTree draws, and every page that mounts the tree reads the same before and after -- a product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-120</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~68</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>31</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6625 (2026-10-12 ~22:03Z), section 1 row D2-W60-S1: "Grant ONE cell on that file [CategoryViewTree.tsx], the same two conditions, because moving the base inside the card changes every page that mounts the tree. A page the census finds that a partner-firm login opens is listed in the cell's record; its PROD rides Andrew's held promote." The two conditions: no other live order's `<paths>` names the file (read by the issuer: none does), and every page that mounts the component (a census from the build's module graph, denominator printed) is rendered before and after with no visible change but the one asked for. | **Rows:** D2-W60-S1 | **Decomp cell:** `IV-e-120` (decomposition v31) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** none (portal DEV 183860bac055 is the base).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-68` (branch `wk-dsgn-irptv1-r31-68`); run everything from its root unless a step says the
portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~68/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-68/portal` is a PORTAL worktree (its own git repo) at portal DEV `183860bac055`. Do not amend or revert anything
committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the
workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` here is a LINK to the
main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run,
then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file that has no uncommitted work of yours. ONE whole-scope
run before any edit (`bun test src/pages/InvestorReporting`, output to a file under
`C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~68/`) is your base for `new_failing_ids`; the issuer measured it at this base as
1203 pass, 27 skip, 1 fail (F14-AC3, a diff check against DEV 1f3ce9f0, a known base failure).

**What is wrong.** The Holdings tab's "Total Assets" hero is drawn by the SHARED `portal/src/components/CategoryViewTree.tsx` (the heading `<p>` near
line 1317, in the card's `body`). Its base (which accounts the figure covers: "all 2 accounts", "this account") is a caption ABOVE the card:
`portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx` near line 436, `<p data-slot="holdings-total-base">Total Assets below: {scopeWords.base}</p>`.
The reader sees the base outside the thing it describes. Row D2-W60-S1 (`org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md`,
search the row id) holds the worker's own account of it.

**The cell (`IV-e-120`).**
1. **The change.** `CategoryViewTree` gains ONE optional prop that carries the base words (name it for what it is, for example `totalBase`); when set, the
   hero card prints the base on a line inside the card under the "Total Assets" heading, in the card's own ink and type scale (read the file's existing
   `subText` / `headline` classes; invent no new colour). When the prop is absent the component renders EXACTLY as before. The Holdings tab passes the
   words it printed above the card (`scopeWords.base`, the same words, no rewording) and the caption above the card, `holdings-total-base`, goes.
   Keep the data-slot name `holdings-total-base` on the new line inside the card so the existing queries still find it. Record `prop` {file, name}.
2. **The census (the CTO's second condition).** From the BUILD'S MODULE GRAPH, not from memory, list every page or component that imports
   `CategoryViewTree` (production code, not tests): the issuer's own search found `ModelPortfolios.tsx`, `Positioning/tabs/HoldingsTab.tsx`,
   `InvestorReporting/tabs/holdings/DrillTree.tsx` and `InvestorReporting/tabs/analysis/VariantCards.tsx` and `api/endpoints/aum.ts` and `lib/chartColors.ts`
   name it in some way; you decide which of those MOUNT the tree, and you print the denominator (how many importers, how many mount it) and how you
   derived it (`census.denominator_source`). For each page that mounts it, render it BEFORE your edit and AFTER it with the same synthetic fixture
   and compare: no visible change, except the Holdings tab's base moving inside the card. Say per page what you compared and how (a DOM snapshot of the
   card subtree, plus one screenshot you read). `census` {mounts_found, pages_rendered_before_after (equal to mounts_found), unchanged_outside_holdings
   true, partner_login_pages [the pages the census finds that a partner-firm login can open, from the route table / route guards; say how you read it],
   denominator_source}.
3. **The test and the suite.** One rendered test `__tests__/dsgn-irptv1/iv-e-120.total-base-in-the-card.test.tsx` (the base words appear inside the card
   element, not above it; a mount without the prop renders byte-for-byte as before), one temporary mutant (print the base outside the card again) that the test
   catches, then reverted. Re-golden `__tests__/dsgn-irptv1/iv-e-108.holdings-names-account-labels-totals.test.tsx` only where it asserts the caption's
   position, and say which assertions moved. `suite_base` {pass, skip, fail}, `suite_after` {pass, skip, fail, new_failing_ids}, `lint_errors`,
   `typecheck_errors` (run `bun run lint` and `bun run typecheck` after your last portal commit), `product_files_changed`, `portal_commit` (40 hex).
4. **A screenshot** of the Holdings tab (synthetic fixture, a two-account client) from a build of your worktree, showing the base inside the card; read it.
   Record everything in `TOTAL_BASE_IN_CARD.json` with the keys named in the criterion below.

<criterion id="IV120-AC1" cell_refs="IV-e-120"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r31/p31_round31.py" . IV120-AC1</invocation><expect>IV120-AC1 PASS</expect></criterion>
`IV120-AC1` -- the base is inside the card and the caption above it is gone, a prop-less mount renders as before, the census names every mounting page with its denominator and renders each before and after with no visible change outside the Holdings tab, a rendered test and a mutant hold it, and a screenshot was read. Base: FAIL (no record).

<expected_criteria>IV120-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. No file under `contracts/wire/` is hand-edited (generated). The shared file
  `portal/src/components/CategoryViewTree.tsx` is granted for THIS change only: no other edit in it (no restyle, no refactor, no colour change).
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no secret read, no `bun install`, no package change.
  A dev server on a port is allowed only for your own screenshot, on a port other than 5174, started from YOUR worktree and stopped when you finish.
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order
  did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row. If the census finds a mounting
  page whose render changes in any way you cannot attribute to the base line, STOP that page and file a BLOCKING row; do not edit the shared file further.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W68-S<k>`, with the real current UTC time; append as BYTES, never re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~68/
portal/src/components/CategoryViewTree.tsx
portal/src/pages/InvestorReporting/tabs/holdings/
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-120.*
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-108.holdings-names-account-labels-totals.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-120.total-assets-base-inside-the-card.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v31 (round 31), cell `IV-e-120`.
<owned_cells>IV-e-120</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV120-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~68/DSGN_IRPTV1.TO-IV-e-120.total-assets-base-inside-the-card.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV120-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the prop and where the base now prints; the census (denominator, which pages mount the tree, each
before and after result, the partner-login pages and how you read them); the test and its mutant; lint, typecheck, and the suite before and after; what the
screenshot shows; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one optional prop on a shared presentation component and one caption moves inside the card. The census inside the order is the blast read. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
