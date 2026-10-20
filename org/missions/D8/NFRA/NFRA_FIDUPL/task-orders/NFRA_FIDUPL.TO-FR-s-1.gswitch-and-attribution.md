# TO NFRA_FIDUPL.TO-FR-s-1 -- the G-number switch and the account-to-G attribution sweep

<to_id>NFRA_FIDUPL.TO-FR-s-1</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~2</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>fidelity-perg</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FR-s-1` (`decompositions/NFRA_FIDUPL_DECOMP_R2.md` v1.0) | **outcome_ref:** FWD-9, C-BACKFILL |
**depends_on:** none (built against fakes; interfaces in worker reference section 11)

---

## WORKER FACE

### THE CELL

**FR-s-1** -- The G-number switch and the attribution sweep: `GSwitcher` over the measured JSP form, and `sweep_attribution` over every option with an injected account lister; restores the starting G in a `finally`; never sets the default; counts-only summary. Contract rows: C-TENANCY, FWD-9.

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (sections 1 and 11 bind you; the rest is context) and the cell text above. Project NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning; round 2 splits it per firm by G number, backfills history per G number, and schedules it. You build against fakes; nothing here runs live.

### WHAT TO BUILD

Build `gswitch.py`, `attribute.py` and their two test files to worker reference sections 11 and the CRO's measured recipe (read `C:/Dev/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_NFRA_FIDUPL_ACCOUNT_TXT_AND_FIRM_SPLIT.md` section 2b; absolute path, read-only). The probe in `signin_recon.py` (`probe_g_switch`, FU-s-2 repair 3) already does one switch with the same recipe: read it for the parsing, but do NOT edit it and do not import from it; this cell owns its own clean module.

1. `gswitch.py`: `FormState` (fields `current`, `default`, `options`), `GSwitchError`, `GSwitcher(request)` with `read_form()`, `switch(g)` and `restore(start)`. Parse `Current: (G\d{8}) - (...)`, `Default: ...` and the `<option value="G\d{8}">label</option>` list from the page text with the standard library. `switch` POSTs `gnumClientNm=<g>&process=change` to the www2 URL, NEVER sends `isDefault`, and asserts the answer's `Current:` equals `g`, else raises `GSwitchError` with a message that names the step but contains no G number and no label.
2. `attribute.py`: `sweep_attribution(switcher, account_lister, business_day)` and a helper `page_account_list(post_form_json, length=2000)` that pages `accountList.json` (form `length=2000&accountNumber=&sourceCode=BROK&custodianCode=FID`, plus an offset field named `start`, an ASSUMPTION: the field name past 2,000 rows is unmeasured, so file ONE surprise row naming it) until a page shorter than 2000 comes back. The sweep reads the form, remembers the starting G, switches to every option in turn, calls the lister, records label and accounts, and in a `finally` restores the starting G and asserts it. It returns the attribution dict of reference section 11; `summary` is counts only. Nothing is printed.
3. Tests (fakes only): in `tests/test_gswitch.py` `test_parses_current_default_and_options`, `test_switch_posts_form_without_isdefault`, `test_switch_asserts_current_equals_requested`, `test_switch_failure_raises_and_names_no_value`; in `tests/test_attribute.py` `test_sweeps_every_option_and_restores_start`, `test_restores_start_even_on_error`, `test_never_sets_default`, `test_summary_counts_only`, `test_pages_account_list_until_short_page`.

### ACCEPTANCE

<criterion id="FR1-AC1" cell_refs="FR-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fr1a</invocation><expect>R1-FR1A-OK passed=\d+</expect></criterion>
`FR1-AC1` -- the four G-switch tests exist and pass.

<criterion id="FR1-AC2" cell_refs="FR-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fr1b</invocation><expect>R1-FR1B-OK passed=\d+</expect></criterion>
`FR1-AC2` -- the five attribution tests exist and pass.

<expected_criteria>FR1-AC1,FR1-AC2</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FR1-AC1` base: FAIL as expected; `FR1-AC2` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Every test uses SYNTHETIC data and fakes; no network, no AWS, no live call. G numbers and account numbers in tests are made up and are never real ones.
- **No secret, no alert; no G number, account number or firm label in any output.** Counts and booleans only (reference section 11).
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, `<n>` your slot, `<k>` next unused across the investigation file) and stop that piece. A premise that fails is a row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).

Reads (outside the grant):
- `infra/aws/ec2/canonical-fidelity/signin_recon.py` (the existing one-switch probe; read only)

<paths>
infra/aws/ec2/canonical-fidelity/gswitch.py
infra/aws/ec2/canonical-fidelity/attribute.py
infra/aws/ec2/canonical-fidelity/tests/test_gswitch.py
infra/aws/ec2/canonical-fidelity/tests/test_attribute.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R2.md</decomp_doc> (round 2), cell `FR-s-1`.
<owned_cells>FR-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FR1-AC1,FR1-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~2/NFRA_FIDUPL.TO-FR-s-1.gswitch-and-attribution.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FR1-AC1,FR1-AC2` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes only; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- build round on fakes; runs when the live round touches this surface.
lane: the paths block.
</preflight>

Source: CTO msg 8663 (PRD v0.4.5 @e4bb46835e); Andrew-direct @b329e1c5f3; decomposition round 2 cell FR-s-1; worker reference section 11.
