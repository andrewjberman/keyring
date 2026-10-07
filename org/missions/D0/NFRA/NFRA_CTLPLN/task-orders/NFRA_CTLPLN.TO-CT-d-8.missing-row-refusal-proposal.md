# TO NFRA_CTLPLN.TO-CT-d-8 -- round 4 CT-d-8: the missing-row refusal -- measured today, and proposed to the gate's owning project

<to_id>NFRA_CTLPLN.TO-CT-d-8</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~11</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-d-8` (`decompositions/NFRA_CTLPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-d-8`, PRD v0.13 C-NAMING, next-issuance cell (b): "the missing-row refusal in the apply path, proposed to LGIC_ENFORCE as its owner,
since it is that project's gate." The PRD's own statement of today: "`.tools/naming-apply-gate.py` inside `safe-apply.sh` refuses a
badly named resource being ADDED (its plan mode). Clause (1) and clause (3) have no gate: ... no gate refuses an apply for a missing
registry row." You MEASURE what the apply path does today with a well-named resource that has no registry row, and you WRITE the
proposal. You do NOT edit the gate: it belongs to another project.

**Build:**

1. `.tools/tests/probe_missing_registry_row.py` -- the measurement, on stand-ins only (no AWS, no real plan against a backend). Read
   `.tools/naming-apply-gate.py` and how `.tools/safe-apply.sh` calls it (its input: a plan in which form; its modes; its exit codes).
   Then feed the gate, exactly as `safe-apply.sh` does, three synthetic plans that each ADD one resource:
   (A) a builder-conformant name that HAS a row in `infra/logic/registry/resources.json` (pick an existing row and re-use its name);
   (B) a builder-conformant name that has NO row (construct it with `lib/opal_naming.name()` from registry vocabulary so it is
       well-formed, and confirm by a text count that the registry does not hold it);
   (C) a badly formed name (the gate's known-bad case).
   Record each result (`admitted` / `refused` and the gate's line). LAST line
   `MISSING-ROW-PROBE registered_wellnamed=<admitted|refused> unregistered_wellnamed=<admitted|refused> badly_named=<admitted|refused> gate_mode=<m> ok=<True|False>`,
   `ok=True` when the three runs completed and (C) is refused (the positive control that the gate was really exercised).
2. `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~11/PROPOSAL_MISSING_ROW_REFUSAL_FOR_LGIC_ENFORCE.md` -- the
   proposal, in standard technical English, addressed to the owner of LGIC_ENFORCE. It carries: the probe's three results and the
   gate's lines; what the refusal should be (an ADDED resource whose name has no registry row is refused, naming the resource and the
   missing row; which resource kinds are out of scope because they have no name of their own; what a first-mint looks like, since
   C-NAMING clause 3 says the row lands in the same commit as the Terraform); where in the gate it would sit (file and function, by
   reading, with line numbers); the cost (one registry read per apply) and the non-application (a resource being changed or destroyed,
   an existing pipeline's legacy names covered by `legacy_addresses.json` or `exemptions.json` -- read those two files' `_about` and say
   how they bear on it); the mode it should start in, with the reason (the repo's naming gates distinguish WARN from ENFORCE: say which
   this gate is in today, by reading); and what it does NOT cover (a create outside Terraform, C-NAMING clause 1). It proposes; it does
   not instruct, and it changes no file of that project.

### ACCEPTANCE

<criterion id="CT4d8-AC1" cell_refs="CT-d-8"><invocation>python .tools/tests/probe_missing_registry_row.py</invocation><expect>badly_named=refused</expect></criterion>
`CT4d8-AC1` -- the gate was exercised (its known-bad case is refused), so the other two results are measurements. Record the whole
last line; `unregistered_wellnamed` is the finding, whichever value it takes.

<criterion id="CT4d8-AC2" cell_refs="CT-d-8" judgment="true"/>
`CT4d8-AC2` (judgment) -- the proposal is one the owning project can act on without asking a question: it states the measured
behaviour, the refusal, its place in the gate, its cost and its non-application.

<expected_criteria>CT4d8-AC1,CT4d8-AC2</expected_criteria>

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No edit to `.tools/naming-apply-gate.py`, `.tools/naming-gate.py`, `.tools/safe-apply.sh`, `lib/opal_naming.py` or any registry file.**
  No AWS call, no `terraform plan` against a backend, no apply.
- The judgment criterion gets its artifact path and NO verdict from you.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W11-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
.tools/tests/probe_missing_registry_row.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `.tools/naming-apply-gate.py`, `.tools/naming-gate.py`, `.tools/safe-apply.sh`,
`lib/opal_naming.py`, every file under `infra/logic/registry/`, `infra/logic/02_DOCTRINE.md`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round4.md</decomp_doc> (round 4), cell `CT-d-8`.
<owned_cells>CT-d-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT4d8-AC1, CT4d8-AC2 (judgment: recorded UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming `3.0.0_SA_CVO`). Instance at
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~11/NFRA_CTLPLN.TO-CT-d-8.missing-row-refusal-proposal.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT4d8-AC1,CT4d8-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the probe's last line and the gate's three result lines; the gate's mode today; the proposal's path and its one-paragraph
summary; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a probe that never reached the gate and reports admitted (the known-bad arm must be refused, AC1); a proposal that edits another project's gate by the back door (no gate or registry file in the grant); an approval gate implemented without Andrew's ask (this cell proposes and implements nothing: CLAUDE.md section 2, proposing is legal, implementing is not; his word here is the registration, and the gate is its owner's to build); BLIND: the gate's behaviour on a real plan on a Dell -- each Dell's fabric manager runs the known-bad name (PRD v0.13, UNMEASURED).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.13 @4cea56993a ADDENDUM v0.13 C-NAMING, cell (b); CTO msg 106067; decomposition round 4. Base dry-run at the cut:
CT4d8-AC1 base FAIL as expected (the probe does not exist); CT4d8-AC2 is judgment, graded by `3.0.0_SA_CVO` at L9.
