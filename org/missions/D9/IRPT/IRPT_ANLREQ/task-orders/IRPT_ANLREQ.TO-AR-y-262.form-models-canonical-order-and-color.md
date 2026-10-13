# TO IRPT_ANLREQ.TO-AR-y-262.form-models-canonical-order-and-color -- the Analysis Request form lists the Opal models in canonical order, each checkbox in its canonical color when checked

<to_id>IRPT_ANLREQ.TO-AR-y-262</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~87</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-262` (`decompositions/IRPT_ANLREQ_DECOMP_R22_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~87`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-87` (branch `wk-IRPT_ANLREQ-87`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~87 <0.9.0_WK_IRPT_ANLREQ~87@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W87-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-262`, inlined) -- CANONICAL ORDER AND COLOR FOR THE MODEL CHECKBOXES. A CANDIDATE on a portal branch; nothing is landed, pushed or deployed.

*Andrew (relayed by the CTO, msg 7151, filing on DEV after his smoke ~18:2xZ), verbatim: "we're missing the Opal Ultra Short-Term, also they should be arranged in canonical order with canonical color checkboxes that take that color when checked. Also the Advisory Fee doesn't need to be included ... These would largely be from prospects so we'd have no way of knowing their fees ... also add commentary checkbox doesnt do anything." Rows `IRPT_ANLREQ-D2-S79` to `-S82`. Item 2 of the CTO's ruling (msg 7151): canonical model order, and each checkbox in its canonical color when checked, both REUSED from the estate's model palette, not new values. The checkboxes today are plain browser checkboxes in the catalogue's order (portal/src/pages/TicketCenter/AnalysisRequestParts.tsx :112-121).*

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-87 -b wk-IRPT_ANLREQ-87-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Commit the way an earlier candidate branch was made (`git -C ... log` of `wk-IRPT_ANLREQ-63-portal`); if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text. Read the portal's own `CLAUDE.md` and `DESIGN.md` first: new text follows their clauses (navy ink on white panels, no light-on-light; cite the clause number in your record for each visual choice).
2. **Find the estate's canonical order and palette (reuse, never copy values).** The model palette is in the portal: read `src/lib/chartColors.ts` (`getModelColor`, `MODEL_PORTFOLIO_COLORS`, the extended colors), `src/pages/InvestorReporting/tabs/holdings/palette.ts`, `src/pages/ModelPortfolios.tsx`, and the tests `src/pages/InvestorReporting/__tests__/dsgn-irptv1/model-colors.test.ts` and `iv-e-11.model-color.test.ts` (the canonical names, e.g. `Ultra Short-Term`). Record `reuse` {`color_function` (file:line), `order_source` (file:line; if the estate has no single order constant, STOP before step 3, file a BLOCKING row and write the record without a candidate: the issuer asks the CTO), `name_matching` (how a catalogue entry's `label`/`key` maps to a canonical model name; entries that match no canonical name keep the catalogue's order after the matched ones and get NO color: say how you treat them)}. Import the existing function and constant; do not type any hex value or any model list of your own.
3. **The change.** In `src/pages/TicketCenter/AnalysisRequestParts.tsx` (the checkboxes :112-121): (a) the listed models are sorted by the canonical order (stable; unmatched entries last in their catalogue order); (b) each model checkbox shows its canonical color when CHECKED (an unchecked box keeps the form's current look): use the CSS `accent-color` property or the idiom the portal already uses for colored checkboxes (search `src/` for `accent-` and for a colored checkbox before inventing one), set from the color function; the label text stays legible on the form's band (white ink is legal there: `CLAUDE.md` color law, `DESIGN.md` C3; cite the clause for your choice). Keep every other behaviour: `comparison_keys`, the `MAX_COMPARISONS` limit, the labels, the other fields. Touch `src/` only (no `package.json`, lockfile, build or config file); do not edit the `Advisory fee` input or the `Add commentary` checkbox (other cells own them).
4. **The tests, before and after.** In the TicketCenter test folder, in the style of its neighbours (`src/pages/TicketCenter/__tests__/analysis-request.test.tsx`): (a) a catalogue given in a scrambled order lists in the canonical order; (b) a checked model's checkbox carries its canonical color (read the color through the same function in the test) and an unchecked one does not; (c) an entry matching no canonical name still lists, after the matched ones, uncolored; (d) checking and unchecking still updates `comparison_keys` and the limit still holds. `before_arm`: on `origin/DEV` WITHOUT the change (a) and (b) FAIL. With the change all pass; the whole TicketCenter test folder (counts) and `bun run typecheck` rc=0; the known `dsgn-irptv1` failures stated with counts both ways.
5. **Commit** in the portal worktree; record the full sha.
6. **Write `r22/PORTAL_FORM_ORDER_COLOR_CANDIDATE.json`:** `reuse`, `dev_tip`, `branch`, `commit`, `files_changed`, `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm` {`failed`, `output_tail`}, `what_a_person_sees` (the order as listed and the checked color per model, in words), `design_clauses`, `claim`, `not_read`.
7. **In your report:** the reused function and order source (file:line), the branch, the commit, the counts, what a person sees.

### ACCEPTANCE

<criterion id="AR262-y-AC1" cell_refs="AR-y-262"><invocation>python C:/dev/wk-irpt-anlreq-87/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y262-portal --root C:/dev/wk-irpt-anlreq-87</invocation><expect>Y262-PORTAL-OK</expect></criterion>
`AR262-y-AC1`: the record names the reused color function and order source, a portal commit under `src/` only, added tests that fail on the DEV tip without the change and pass with it, and no failing test of the folder beyond the known pre-existing ones.

<criterion id="AR262-y-AC2J" cell_refs="AR-y-262" judgment="true"/>
`AR262-y-AC2J` (judgment, graded at L9, never by you): the order and the colors come from the estate's own function and constant (no hex or model list was typed), a checked box shows its canonical color, an unchecked box is unchanged, unmatched entries still list, and nothing was landed or pushed.

<expected_criteria>AR262-y-AC1 AR262-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~87/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22_Y.md</decomp_doc>
<owned_cells>AR-y-262</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~87/IRPT_ANLREQ.TO-AR-y-262.form-models-canonical-order-and-color.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-262`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR262-y-AC1,AR262-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading Andrew's smoke words (rows D2-S79 to D2-S82) against the cell; the lens: a test that passes without the change, a color or order invented instead of reused, or a change that fixes the form the worker imagined and not the one Andrew filed on. The order requires the new test to FAIL on the DEV tip without the change, and the words a person sees to be stated as rendered. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on Andrew's smoke of the Analysis Request form (CTO msg 7151, rows `D2-S79` to `-S82`) as workstream `Y` round 22, the CTO's O1 issuance, ahead of anything else. Base: `AR262-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
