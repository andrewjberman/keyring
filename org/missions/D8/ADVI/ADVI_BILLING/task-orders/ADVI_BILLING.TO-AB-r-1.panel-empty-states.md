# TO ADVI_BILLING.TO-AB-r-1 -- FWD-3: the fee panel states its empty flow and exclusion lists instead of omitting them

<to_id>ADVI_BILLING.TO-AB-r-1</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.9.0_WK_ADVI_BILLING~6</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f | **Decomp cell:** `AB-r-1` (decomposition section 4, round 3) | **outcome_ref:** FWD-3 | **depends_on:** none. **Authority:** CTO ADDENDUM 3 @7f414eb19e (msg 3004).

---

## WORKER FACE

Your worktree is `C:/dev/wk-advi-billing-6`; its portal is `C:/dev/wk-advi-billing-6/portal` (portal DEV, which carries the panel).
Run `bun` from `portal/`. Your folder is `org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~6/`.

**The cell.** `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookFeePanel.tsx` renders one household's billed-quarter fee. Per account it
shows the flow adjustment and the exclusions only when they are non-zero, so an advisor cannot tell "none" from "not shown". FWD-3's ACCEPT
asks that an advisor sees "any adjustment for money moved in or out during the quarter, and anything left out".

1. In each account block, when `flows_in_period` is empty (or absent) show the line **"No money moved in or out this quarter"**; when
   `excluded_value` is 0 or null show **"Nothing excluded"**. Keep the existing rendering when they are non-zero. Use the panel's existing
   row style (navy ink on white; the portal's colour law: no light text on light fills).
2. In `portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookFeePanel.test.tsx` add a test whose name contains `empty`, rendering an
   account with no flows and nothing excluded and asserting both phrases appear; keep every existing test passing. Edit the fixture
   `__fixtures__/adviBillingFeeQuarter.json` only if the test needs it (invented values only).
3. Commit on your portal worktree branch and on your workspace branch (the workspace commit carries the proof instance).

<criterion id="AB3-1-AC1" cell_refs="AB-r-1"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB3-1-AC1</invocation><expect>AB3-1-AC1 PASS</expect></criterion>
`AB3-1-AC1` -- the panel and its test carry both phrases, a test named *empty* exists, and the bun test passes. Base: FAIL.

<expected_criteria>AB3-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- No new dependency, no push, no AWS call, no edit outside the three portal files.
- **Refusal clause.** An edit outside the grant, a write or deploy the face does not name, a vendor call, or an account number, name
  or dollar figure in a committed file is a defect: stop and file a row.

<paths>
portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookFeePanel.tsx
portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookFeePanel.test.tsx
portal/src/pages/AdvisorIntelligence/_shared/__fixtures__/adviBillingFeeQuarter.json
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~6/
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-r-1.panel-empty-states.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 4 (round 3), cell `AB-r-1`.
<owned_cells>AB-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB3-1-AC1. The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~6/ADVI_BILLING.TO-AB-r-1.panel-empty-states.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB3-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what the cell measured, and every row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one served-on-DEV component; no route or key moves.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role is created or changed in this cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: enrichment cell; no served claim is graded here.
checks dry-run at base: AB3-1-AC1 FAIL as expected.
lane: the <paths> block IS the grant.
</preflight>
