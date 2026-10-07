# TO MDPF_SECCLASS.TO-SC-e51 -- round 9 SC-e-51: FWD-16: the Investor Reporting securities table shows Cash as its own group, like the same tab's treemap and class bar

<to_id>MDPF_SECCLASS.TO-SC-e51</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~37</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-51` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-16 | **depends_on:** none (slot ~37 queue: this order, then TO-SC-e52, then TO-SC-e53)

---

## WORKER FACE

### THE CELL

`SC-e-51`. FWD-16 (PRD v0.13): every screen that shows a mix by class reads the shared list's classes with one stated mapping.
Round-8 analysis 2.8: each of the three disagreements SC-e-24's census named (row W23-S2) is a FWD-16 cell; this is the first.

**The disagreement (measured, W23-S2):** on Investor Reporting > Holdings the securities table groups a Cash row under Fixed Income
while the same tab's treemap and class bar draw Cash as its own group. The fold is in the SHARED component
`portal/src/components/holdings/HoldingsBreakdownTable.tsx` (~:328-334: `holding.asset_class === 'Cash' ? 'Fixed Income'`, a fold
"moved from Positioning"), which `portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx` renders; the treemap side is
`HoldingsTreemap.tsx:613` `legendClassesFor(..., foldCash:false)`.

**Issuer ruling:** the Investor Reporting table matches its treemap: Cash shown alone. **Positioning keeps its fold** (its Holdings tab
folds Cash into Fixed Income by its own stated rule, `pages/Positioning/tabs/HoldingsTab.tsx`): so the fold becomes a prop of
`HoldingsBreakdownTable` (default the current behaviour, fold on) that `SecurityList.tsx` turns off. Read every importer of
`HoldingsBreakdownTable` before editing (portal DEV: `SecurityList.tsx`, `Positioning/tabs/HoldingsTab.tsx`, and the dsgn-irptv1 tests
iv-e-103, iv-e-134, iv-e-148, iv-e-152); none may change behaviour except the Investor Reporting table.

**Build:** the prop and its use; a new test `portal/src/pages/InvestorReporting/__tests__/mdpf-secclass/ir-securities-cash-alone.test.ts`
whose test names carry `cash_alone`: an Investor Reporting rendering with a Cash row groups it under Cash, not Fixed Income; a
Positioning rendering (fold on) still groups Cash under Fixed Income; the class order places Cash where the treemap's legend does.

### ACCEPTANCE

<criterion id="SC9-e51-AC1" cell_refs="SC-e-51"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/portal_named_tests.py src/pages/InvestorReporting/__tests__/mdpf-secclass/ir-securities-cash-alone.test.ts cash_alone</invocation><expect>PORTAL-TESTS ok=True</expect></criterion>
`SC9-e51-AC1` -- the Investor Reporting table shows Cash alone and Positioning still folds it.

<criterion id="SC9-e51-AC2" cell_refs="SC-e-51" judgment="true"/>
`SC9-e51-AC2` -- JUDGMENT (3.0.0_SA_CVO): the Investor Reporting > Holdings tab reads as one consistent grouping of Cash across its treemap, class bar and securities table.

<expected_criteria>SC9-e51-AC1,SC9-e51-AC2</expected_criteria>

Dry-run at the base (5d70aab6c9, 2026-10-07): SC9-e51-AC1 FAIL as expected (`PORTAL-TESTS ok=False ... reason=absent`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch, into any environment; row S49).
- **Portal.** Your worktree's `portal/` is a nested worktree at 91d29d17a0 (portal branch wk-MDPF_SECCLASS-22-portal: SC-e-23's held six-class candidate on top of origin/DEV 8ddfe409; this stack lands with it for one CTO review); commit there on your portal branch only. Never push, never touch portal DEV; the issuer lands the stack for a CTO review (product files).
- No deploy, no upload, no table write.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W37-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
portal/src/components/holdings/HoldingsBreakdownTable.tsx
portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx
portal/src/pages/InvestorReporting/__tests__/mdpf-secclass/ir-securities-cash-alone.test.ts
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-51`.
<owned_cells>SC-e-51</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e51-AC1, SC9-e51-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~37/MDPF_SECCLASS.TO-SC-e51.ir-securities-cash-alone.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e51-AC1,SC9-e51-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the prop's name and default, every importer read and its verdict (behaviour unchanged or changed), AC1's output, portal commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a portal display change schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no role, no table, no S3 address.
comp-adversary: RUN -- the screen census (M/SCREEN_GROUP_MAPPING_20261007.json, .md; row W23-S2); round-8 analysis ruling 2.8; BLIND: whether other screens import the edited component (the worker reads the importers named in the face before editing).
lane: the <paths> block IS the grant.
</preflight>

Source: round-8 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md` @1ca9e97fc9; PRD v0.13 @90f99888cd (ADMITTED); DECOMP_R9 @5d70aab6c9.
