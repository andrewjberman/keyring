# TO IRPT_CUSTDY.TO-CU-a-4 -- round 1 CU-a-4: the 49 Financial template, a client report laid into it, and the render path's input read from source

<to_id>IRPT_CUSTDY.TO-CU-a-4</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~4</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-a-4` (`decompositions/IRPT_CUSTDY_DECOMP.md`) |
**outcome_ref:** FWD-1, FWD-3 | **depends_on:** none (the decomposition fixes the client-report contract you read)

---

## WORKER FACE

### THE CELL

`CU-a-4`, hop 5 of the round-1 thread: "Hops 3 and 4 are laid into the 49 Financial template and rendered per client on the IRPT_BCKEND
export path. The template is new: round 1 builds the 49 Financial one only, from the custodian-shaped model." FWD-3: each firm's reports
are in its own template, and changing one firm's template changes nothing in another's. Two contracts bind the template: it is built
from the custodian-shaped model, never from a Black Diamond report's layout (C-SHAPE, C-TEMPLATE), and nothing reaches a client.

**Your input: the decomposition's CLIENT-REPORT CONTRACT** (one JSON document per household): `{"firm", "advisor", "as_of", "household":
{"id","name"}, "periods": [...], "accounts": [{"account", "registration", "returns": {<period>: {"value","window","status"}},
"market_value": {"start","end"}, "holdings": [{"symbol","cusip","quantity","market_value","weight","class","sector","described",
"description_source"}], "activity": [{"date","type","symbol","amount"}], "fees": {"amount","source","is_billed_fee"}}],
"household_returns": {...}, "lineage": {...}}`. Every figure may carry `status` other than `OK`; the report shows that status in place.

**The template is DATA, not code** (decomposition constraint 5): in production it lives at `opal_naming.address("irpt", <lookup firm>,
"state", "report_template", "version=1")` under the firm's own prefix; the issuer uploads it after the drain. You author its content as the
fixture below and write the loader so it reads either a local file or that address. Never type a firm token or an S3 key into code.

**The render path (READ, never edit; IRPT_BCKEND owns it):** `infra/aws/terraform/investor-reporting/export/b2_render.tf` (lines 1-17:
`submit-export` mints a render token into SSM `/irpt/render-token/<ATT-id>` and dispatches a render host),
`infra/aws/ec2/investor-reporting-export/render_export.cjs` (the host), `infra/aws/lambda/investor-reporting/_render_identity/carriage.py`,
`docs/contracts/investor-reporting/v1/responses/submit-export.response.schema.json`,
`portal/src/pages/InvestorReporting/fixtures/wire/requests/submit-export.request.json`. Read them to state what the path takes as input
and whether a client-report document can be rendered through it as it stands. **You do not change it.** If it cannot take a document,
that is a row (OBSERVATION) naming exactly what is missing; the issuer routes it to IRPT_BCKEND's COO.

**Build:**
1. The template fixture `data/assets/scripts/gold/irpt_custody/tests/fixtures/report_template_firm_a.json`: ordered sections (cover;
   household summary with `household_returns` over the document's `periods` in order; per account: returns table, market value start/end,
   holdings with class and sector, activity, fees with their source label; a "not described" marker for `described: false` holdings; a
   data-status note for any non-`OK` figure); wording and branding as named slots (`firm_display_name`, `logo_ref`, `disclosure_text`) left
   as slot names, never filled with invented text. The file name carries no firm token.
2. `data/assets/scripts/gold/irpt_custody/report_render_request.py`: `load_template(src)` (local path or s3 key); `lay_out(document,
   template) -> dict` (the report as ordered sections with every figure from the document, nothing computed again); `to_html(laid_out) ->
   str` (stdlib only, for the local look); CLI `--document <file> --template <file> --out <dir>`, `--render-path` (prints what step 3 found),
   `--self-test`. Device-free.
3. `--render-path` prints `RENDER-PATH input=<one line> accepts_document=<True|False|UNKNOWN> evidence=<file:line>`.
4. `--self-test`: lay out and render to HTML two fixture documents -- one household with every figure `OK`, one with a `NO_DATA` return
   and an undescribed holding -- through the fixture template, then lay out the first through a SECOND template that differs in one section
   and show the first template's output did not change; print, as the LAST line, `REPORT-LAYOUT-SELFTEST layout_ok=<True|False>
   status_shown=<True|False> firm_isolated=<True|False>`.
5. Tests `data/assets/scripts/gold/irpt_custody/tests/test_report_render_request.py` (pytest, `tmp_path`, insert the module's directory into
   `sys.path`; no `__init__.py`): sections in template order; periods in the document's order; a `NO_DATA` figure and an undescribed
   holding are shown as such, never as 0 or blank; branding slots stay slot names; no account number beyond the last 4 appears in the HTML.

### ACCEPTANCE

<criterion id="CU4-AC1" cell_refs="CU-a-4"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_report_render_request.py</invocation><expect>passed</expect></criterion>
`CU4-AC1` -- the layout's behaviour: order, statuses shown in place, slots, masking.

<criterion id="CU4-AC2" cell_refs="CU-a-4"><invocation>python data/assets/scripts/gold/irpt_custody/report_render_request.py --self-test</invocation><expect>REPORT-LAYOUT-SELFTEST layout_ok=True status_shown=True firm_isolated=True</expect></criterion>
`CU4-AC2` -- the seam on fixtures through the real CLI, with the second-template difference control (FWD-3's isolation). The real render
through `irpt-export-render` is the issuer's act after the drain, on what `--render-path` reports.

<expected_criteria>CU4-AC1,CU4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS call; no change to IRPT_BCKEND's paths, Terraform or Lambda.** No write outside a temp dir and your granted files.
- **Nothing reaches a client or a person outside Opal.** The HTML is a local file you look at.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W4-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/gold/irpt_custody/report_render_request.py
data/assets/scripts/gold/irpt_custody/tests/test_report_render_request.py
data/assets/scripts/gold/irpt_custody/tests/fixtures/report_template_firm_a.json
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.md</decomp_doc> (round 1), cell `CU-a-4`.
<owned_cells>CU-a-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU4-AC1, CU4-AC2. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~4/IRPT_CUSTDY.TO-CU-a-4.template-and-render-request.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU4-AC1,CU4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the self-test output, the `--render-path` line with its evidence, a screenshot-free description of the HTML's sections, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a layout library; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the cell makes no AWS call at all (repo files and local fixtures only).
comp-adversary: RUN -- firm isolation is the cell's own difference control (CU4-AC2 firm_isolated); read-only on IRPT_BCKEND; BLIND: whether the render path accepts a document (the worker reads it; a gap is a row routed to IRPT_BCKEND's COO).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.2 @c2bc15f427 section 2 hop 5, S06-S07, FWD-3, C-SHAPE, C-TEMPLATE; decomposition constraints 4 and 5 and the contract.
