# TO MDPF_SECCLASS.TO-SC-e52 -- round 9 SC-e-52: FWD-16: the Performance Allocation card prints display labels for every class, not raw lower-case tokens

<to_id>MDPF_SECCLASS.TO-SC-e52</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~37</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-52` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-16 | **depends_on:** none (slot ~37 queue: after TO-SC-e51)

---

## WORKER FACE

### THE CELL

`SC-e-52`. FWD-16; round-8 analysis 2.8, the second W23-S2 disagreement.

**Measured (W23-S2):** `portal/src/pages/AdvisorIntelligence/_shared/perfrp/PerfrpAllocation.tsx` ~:41-55 `CLASS_LABELS` carries four
entries (equity, fixed_income, alternatives, cash); `classLabel()` returns any other token verbatim, so `structured` and `commodities`
render as raw lower-case tokens beside "Equity" and "Fixed Income".

**Build:** `CLASS_LABELS` carries all six classes of the shared list (cash, fixed_income, equity, structured, alternatives, commodities)
with the display labels the other screens use (`Structured`, `Commodities`). KEEP the card's two stated rules: a residue token
(e.g. `NO-CLASSIFICATION-ROW`, `UNCLASSIFIED-LOUD`, read from the leaf's `residue_states_declared`) is still shown VERBATIM, and nothing
is ever dropped. A new test `portal/src/pages/AdvisorIntelligence/__tests__/mdpf-secclass/perfrp-class-labels.test.ts`, test names
carrying `six_class_label`: each of the six classes renders its label; a residue token still renders verbatim; an unknown token still
renders (not dropped).

### ACCEPTANCE

<criterion id="SC9-e52-AC1" cell_refs="SC-e-52"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/portal_named_tests.py src/pages/AdvisorIntelligence/__tests__/mdpf-secclass/perfrp-class-labels.test.ts six_class_label</invocation><expect>PORTAL-TESTS ok=True</expect></criterion>
`SC9-e52-AC1` -- six labels, residue verbatim, nothing dropped.

<criterion id="SC9-e52-AC2" cell_refs="SC-e-52" judgment="true"/>
`SC9-e52-AC2` -- JUDGMENT (3.0.0_SA_CVO): the card's class names read as the same names the other mix screens show.

<expected_criteria>SC9-e52-AC1,SC9-e52-AC2</expected_criteria>

Dry-run at the base (5d70aab6c9, 2026-10-07): SC9-e52-AC1 FAIL as expected (`reason=absent`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch, into any environment; row S49).
- **Portal.** Your worktree's `portal/` is a nested worktree at 91d29d17a0 (portal branch wk-MDPF_SECCLASS-22-portal: SC-e-23's held six-class candidate on top of origin/DEV 8ddfe409; this stack lands with it for one CTO review); commit there on your portal branch only. Never push, never touch portal DEV; the issuer lands the stack for a CTO review (product files).
- No deploy, no upload, no table write.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W37-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
portal/src/pages/AdvisorIntelligence/_shared/perfrp/PerfrpAllocation.tsx
portal/src/pages/AdvisorIntelligence/__tests__/mdpf-secclass/perfrp-class-labels.test.ts
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-52`.
<owned_cells>SC-e-52</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e52-AC1, SC9-e52-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~37/MDPF_SECCLASS.TO-SC-e52.perfrp-class-labels.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e52-AC1,SC9-e52-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the label map before and after, AC1's output, portal commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a portal display change schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no role, no table, no S3 address.
comp-adversary: RUN -- the screen census (M/SCREEN_GROUP_MAPPING_20261007.json, .md; row W23-S2); round-8 analysis ruling 2.8; BLIND: whether other screens import the edited component (the worker reads the importers named in the face before editing).
lane: the <paths> block IS the grant.
</preflight>

Source: round-8 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md` @1ca9e97fc9; PRD v0.13 @90f99888cd (ADMITTED); DECOMP_R9 @5d70aab6c9.
