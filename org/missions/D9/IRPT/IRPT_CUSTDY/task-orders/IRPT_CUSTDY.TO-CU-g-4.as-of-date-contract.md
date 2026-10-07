# TO IRPT_CUSTDY.TO-CU-g-4 -- round 7 CU-g-4 (break 3): the custody document carries `as_of_date`, the export contract's name, read by one name everywhere

<to_id>IRPT_CUSTDY.TO-CU-g-4</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~16</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~K2-B3</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-g-4` (`decompositions/IRPT_CUSTDY_DECOMP.round7.addendum1.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CU-g-4`. The client-report household document produced by hop 3 must carry its date under the key the export contract reads:
`as_of_date` (YYYY-MM-DD). The CTO's ruling, verbatim: "The custody document carries `as_of_date` as the export contract names it. Its
first producer is this project, so the contract's name wins; no consumer is asked to read two names."

The contract is `infra/aws/lambda/investor-reporting/export/narrative_submit.py`, function `custody_report_as_of(report)`: it reads
`report["as_of_date"]` and refuses by name without it. READ that file; never edit it (it is another project's).

Today the household document carries `as_of`. It is read by two consumers, both in your grant: `client_report_figures.validate_document`
and the portal template `ClientReportDocument` (+ `types.ts`). Only the DOCUMENT KEY changes: function arguments, CLI flags
(`--as-of`), partition dates and local variables named `as_of` stay exactly as they are.

**Your worktree's nested `portal/` is on branch `wk-IRPT_CUSTDY-16-portal`, cut from `4c10b488`** (the template as passed by the CTO).

**Build:**
1. `data/assets/scripts/gold/irpt_custody/client_report_figures.py` and `hop3_real_run.py`: the household document's date key is
   `as_of_date`; no household document carries `as_of`. `validate_document` requires `as_of_date` (YYYY-MM-DD) and refuses a document
   that carries `as_of` instead. Update the fixtures and tests that build documents with the old key (listed in `<paths>`).
2. A NEW test `data/assets/scripts/gold/irpt_custody/tests/test_as_of_date_contract.py`: (a) a produced document (built through the
   producer's own code on fixtures, no AWS) carries `as_of_date` and no `as_of`; (b) the export's REAL `custody_report_as_of`, imported
   from `infra/aws/lambda/investor-reporting/export/narrative_submit.py` by path, returns the date for that document; (c)
   `validate_document` refuses a document carrying `as_of` without `as_of_date`.
3. Portal: `types.ts`, `ClientReportDocument.tsx` and `render/fixtures/clientreport.firm-a.json` read and carry `as_of_date`; update the
   three existing clientreport tests that build documents; a NEW test
   `portal/src/pages/InvestorReporting/__tests__/clientreport/as-of-date.test.tsx` (`bun:test`) asserting the rendered date comes from
   `as_of_date` and that a document carrying only `as_of` does not render a date silently (refuse by name, or render the missing-date
   state the template already has -- say which in your report). Commit on your portal branch with `git -C portal commit`; never push.
4. Re-run every existing clientreport bun test and the `irpt_custody` pytest files you changed: all pass.

**THE BUN RULE -- verbatim (`1.0.0_SA_CTO~DELL2` msgs 500 and 563, `0.0.0_AB_MSTR~DELL2` msg 508):** "run bun ONLY from inside
C:\dev\ajb_workspace\portal (or a worktree with node_modules LINKED), always as `bun --no-install`; never run bun on a scratch file
elsewhere." "Never `bun install`. Provision a worktree only with `wk-provision.sh --node-modules link` (it links
C:\dev\ajb_workspace\portal\node_modules, the kit tree) or `none`. The rest of 106215 stands: bun only inside a portal tree holding
node_modules, always --no-install, no registry-reaching probe." Conditions of msg 508: (1) before any bun call prove the link
(`ls portal/node_modules/react/package.json` resolves into the shared portal); (2) every bun call is `bun --no-install` from inside the
worktree's `portal/`; (3) an import of a package NOT already in node_modules is STOP: no run, file a row, return.

**WEB (Andrew-direct, verbatim):** "I do not mind webbrowsing if necessary for research purposes, however we do not do downloads." No
package, script or program is fetched from the internet on any box.

### ACCEPTANCE

<criterion id="CU19-AC1" cell_refs="CU-g-4"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_as_of_date_contract.py</invocation><expect>passed</expect></criterion>
`CU19-AC1` -- the produced document carries `as_of_date`, the export's own `custody_report_as_of` accepts it, and `validate_document`
refuses the old key.

<criterion id="CU19-AC2" cell_refs="CU-g-4"><invocation>cd portal && bun --no-install test ./src/pages/InvestorReporting/__tests__/clientreport/as-of-date.test.tsx</invocation><expect>0 fail</expect></criterion>
`CU19-AC2` -- the template reads its date from `as_of_date`. (Re-run the whole clientreport directory too: every test passes.)

<expected_criteria>CU19-AC1,CU19-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Portal commits** on your nested branch `wk-IRPT_CUSTDY-16-portal` with `git -C portal commit`; never push. Workspace commits via
  `.tools/safe-commit.sh`. Do not commit the workspace's `portal` submodule pointer.
- **No AWS call.** Never edit another project's file (`infra/aws/lambda/...` is read only).
- **A surprise row is committed in the same turn you write it.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a row (id `IRPT_CUSTDY-W16-S<k>`;
  `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do not weaken a test.

<paths>
data/assets/scripts/gold/irpt_custody/client_report_figures.py
data/assets/scripts/gold/irpt_custody/hop3_real_run.py
data/assets/scripts/gold/irpt_custody/report_render_request.py
data/assets/scripts/gold/irpt_custody/tests/test_as_of_date_contract.py
data/assets/scripts/gold/irpt_custody/tests/test_client_report_figures.py
data/assets/scripts/gold/irpt_custody/tests/test_not_covered_validation.py
data/assets/scripts/gold/irpt_custody/tests/test_hop3_real_run.py
data/assets/scripts/gold/irpt_custody/tests/fixtures/report_template_firm_a.json
portal/src/pages/InvestorReporting/render/clientreport/ClientReportDocument.tsx
portal/src/pages/InvestorReporting/render/clientreport/types.ts
portal/src/pages/InvestorReporting/render/fixtures/clientreport.firm-a.json
portal/src/pages/InvestorReporting/__tests__/clientreport/client-report-document.test.tsx
portal/src/pages/InvestorReporting/__tests__/clientreport/not-covered.test.tsx
portal/src/pages/InvestorReporting/__tests__/clientreport/mixed-document-refused.test.tsx
portal/src/pages/InvestorReporting/__tests__/clientreport/as-of-date.test.tsx
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round7.addendum1.md</decomp_doc> (round 7, addendum 1), cell `CU-g-4`.
<owned_cells>CU-g-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU19-AC1, CU19-AC2. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~16/IRPT_CUSTDY.TO-CU-g-4.as-of-date-contract.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU19-AC1,CU19-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the link proof, the pytest and bun summaries (the new files and the full clientreport directory), what an `as_of`-only
document does in the template, the portal commit hash, rows, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a document-key rename; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the cell makes no AWS call (fixtures, pytest and bun only).
comp-adversary: RUN -- the contract is read from the export's own code, not restated; the old key is refused, not tolerated; bun rules verbatim; BLIND: none.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-6 ADDENDUM 1 @c3addc6f25 Ruling 1 (msg 914); row S14 break 3; decomposition round 7 addendum 1.
