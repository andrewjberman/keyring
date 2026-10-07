# TO MDPF_SECCLASS.TO-SC-e59 -- round 10 SC-e-59: the fix of the BD thread's first failing hop that SC-e-58 names

<to_id>MDPF_SECCLASS.TO-SC-e59</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~46</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-59` (`decompositions/MDPF_SECCLASS_DECOMP_R10.md`) |
**outcome_ref:** FWD-1 | **depends_on:** TO-SC-e58 (complete @61664c4891; amendment 1 moves this order to slot ~46, a portal worktree)

---

## WORKER FACE

### THE CELL

`SC-e-59`. CTO round-9 analysis section 3 item 1: "the BD pages thread trace, then the fix of its failing hop."

**AMENDMENT 1 (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~14:0xZ, on 1.0.0_SA_CTO~DELL1 ruling msg 287):** "The trace (blob f624ffb58a) names
ONE failing hop on the page chain, portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts:204-213 ... Amend SC-e-59, your own
order, to that hop: the page renders the canonical class and sub-class the platinum bytes carry, with one test pinning GLD, PHYS and VXX.
Write set: that file plus its test, in a portal worktree provisioned with `link` only." This replaces the round-10 cut's three-BD-file
build, which no longer applies.

**Measured by SC-e-58** (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_PAGES_THREAD_TRACE_20261007.json`, read it first):
- The served platinum composition bytes carry `asset_class_canonical` and `sub_asset_class_canonical` per holding. For example, GLD and
  PHYS read `commodities`/`Metals` and VXX reads `structured`/`Hedge` (clients z08327149, z08373330, z0893406).
- `portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts` ~:204-213 rebuilds each item without those two fields (fix line
  ~:212). The page therefore shows a class-only slice and never the sub-class.
- `ConcentrationItem` (`types.ts` ~:1519-1530) has no sub-class field, and `ConsolidatedOverviewPanel.tsx` ~:466-468 prints
  `display_label ?? label`.

**Build:** in `composition.ts`, carry the canonical class and sub-class from each served holding onto the item the page reads. Where the
item's type has no field for them, export the shape this file builds. Write
`portal/src/pages/AdvisorIntelligence/__tests__/mdpf-secclass/composition-canonical-subclass.test.ts` (bun test). Name every test
`canonical_subclass ...`. The test feeds composition.ts a fixture of served bytes holding GLD, PHYS and VXX, and asserts:
- GLD and PHYS come out `commodities`/`Metals`;
- VXX comes out `structured`/`Hedge`;
- the difference control: a holding with no canonical columns keeps the existing label path and invents no sub-class.

**Outside your write set:** `types.ts` and `ConsolidatedOverviewPanel.tsx`. If the page cannot show the sub-class without a line in
either, do not edit it: name the exact line and change in your report and a row. The issuer adds that hookup at the merge.

### ACCEPTANCE

<criterion id="SC10-e59-AC1" cell_refs="SC-e-59"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/portal_named_tests.py src/pages/AdvisorIntelligence/__tests__/mdpf-secclass/composition-canonical-subclass.test.ts canonical_subclass</invocation><expect>PORTAL-TESTS ok=True</expect></criterion>
`SC10-e59-AC1` -- composition.ts carries GLD/PHYS commodities/Metals and VXX structured/Hedge from the served bytes, with the
no-canonical control.

<criterion id="SC10-e59-AC2" cell_refs="SC-e-59" judgment="true"/>
`SC10-e59-AC2` -- judgment (3.0.0_SA_CVO, L9): the Advisor Intelligence page, read on the laptop after review, shows GLD and PHYS as
commodities (Metals) and VXX as a hedge for a real BD client (FWD-1 ACCEPT).

<expected_criteria>SC10-e59-AC1,SC10-e59-AC2</expected_criteria>

Dry-run at the base (amendment 1; portal DEV 8ddfe409 in wk-secclass-46): SC10-e59-AC1 FAIL as expected (absent test file).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment;
  rows S49, S54). The portal worktree's `node_modules` is a LINK to the shared tree; `bun test` and `tsc` only run against it. Never
  run `bun install`.
- Commit inside the portal worktree on its own branch, and in the super-repo for the proof and order. Never push, never land on DEV:
  this is a product file, and the laptop CTO reviews it before DEV.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W46-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts
portal/src/pages/AdvisorIntelligence/__tests__/mdpf-secclass/composition-canonical-subclass.test.ts
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R10.md</decomp_doc> (round 10), cell `SC-e-59`.
<owned_cells>SC-e-59</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC10-e59-AC1, SC10-e59-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~46/MDPF_SECCLASS.TO-SC-e59.bd-thread-failing-hop-fix.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC10-e59-AC1,SC10-e59-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** composition.ts before and after (file:line), any hookup line needed in types.ts or the panel, AC1 output, portal and super-repo commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a portal source change schedules nothing; it reaches DEV only after the laptop CTO review.
comp-iam: DECLARED-NOT-APPLICABLE no role or grant changes; the page reads the bytes it already reads.
comp-adversary: RUN -- the SC-e-58 trace (blob f624ffb58a); a sub-class invented for a holding with no canonical columns (the control arm); a bun install in the portal worktree (node_modules is a link, rows S49/S54); BLIND: the rendered page (the CVO's judgment criterion, read on the laptop after review).
lane: the <paths> block IS the grant; amendment 1 moves the order to slot ~46 (portal worktree, link only) per 1.0.0_SA_CTO~DELL1 msg 287.
</preflight>

Source: round-9 analysis @9b6348f15e section 2.1, section 3 item 1; PRD v0.14 (ADMITTED); DECOMP_R10.
