# TO MDPF_SECCLASS.TO-SC-e53 -- round 9 SC-e-53: FWD-16: Attribution's static etf-categories list follows the producer's two-group funnel

<to_id>MDPF_SECCLASS.TO-SC-e53</to_id>
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

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-53` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-16 | **depends_on:** none (slot ~37 queue: after TO-SC-e52)

---

## WORKER FACE

### THE CELL

`SC-e-53`. FWD-16; round-8 analysis 2.8, the third W23-S2 disagreement.

**Measured (W23-S2, SC-e-24 census screens 7-9):** Attribution > Holdings, Asset Allocation Summary and Style vs Policy show TWO groups
(Fixed Income, Equity) by the producer's funnel (Andrew-direct 2026-10-06;
`infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/lambda_function.py` ~:594-603: cash and fixed
income to Fixed Income, every other class to Equity). `portal/src/pages/Attribution/constants/etf-categories.ts` still carries a static
four-way `assetClass` type (`'Fixed Income' | 'Equity' | 'Cash' | 'Hedge'`), `ASSET_CLASS_ORDER` = Cash, Fixed Income, Equity (~:107-111),
and `SEGMENT_ORDER` with Cash and Hedge keys. Its reader is `portal/src/pages/Attribution/constants/holdings-shared.tsx`
(`getETFCategory`, ~:157-170).

**Build:** the static list's class axis is the funnel's two groups: `ASSET_CLASS_ORDER` = Fixed Income, Equity; a `CASH_USD`-type entry
sits under Fixed Income with segment Cash (the funnel's own fold); no `Hedge` class. Segment names are unchanged. Read
`holdings-shared.tsx`'s use first: what it renders must not change for any ticker except where the class axis named Cash or Hedge. A
new test `portal/src/pages/Attribution/__tests__/mdpf-secclass/etf-categories-two-group.test.ts`, names carrying `two_group`: the
order is two groups; every `ETF_CATEGORIZATION` entry's class is one of the two; CASH_USD reads Fixed Income / Cash.

### ACCEPTANCE

<criterion id="SC9-e53-AC1" cell_refs="SC-e-53"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/portal_named_tests.py src/pages/Attribution/__tests__/mdpf-secclass/etf-categories-two-group.test.ts two_group</invocation><expect>PORTAL-TESTS ok=True</expect></criterion>
`SC9-e53-AC1` -- the static list carries the funnel's two groups.

<expected_criteria>SC9-e53-AC1</expected_criteria>

Dry-run at the base (5d70aab6c9, 2026-10-07): SC9-e53-AC1 FAIL as expected (`reason=absent`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch, into any environment; row S49).
- **Portal.** Your worktree's `portal/` is a nested worktree at 91d29d17a0 (portal branch wk-MDPF_SECCLASS-22-portal: SC-e-23's held six-class candidate on top of origin/DEV 8ddfe409; this stack lands with it for one CTO review); commit there on your portal branch only. Never push, never touch portal DEV; the issuer lands the stack for a CTO review (product files).
- No deploy, no upload, no table write.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W37-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
portal/src/pages/Attribution/constants/etf-categories.ts
portal/src/pages/Attribution/__tests__/mdpf-secclass/etf-categories-two-group.test.ts
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-53`.
<owned_cells>SC-e-53</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e53-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~37/MDPF_SECCLASS.TO-SC-e53.attribution-etf-categories-two-group.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e53-AC1` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** every ticker whose class changed, the reader's use as read, AC1's output, portal commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a portal display change schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no role, no table, no S3 address.
comp-adversary: RUN -- the screen census (M/SCREEN_GROUP_MAPPING_20261007.json, .md; row W23-S2); round-8 analysis ruling 2.8; BLIND: whether other screens import the edited component (the worker reads the importers named in the face before editing).
lane: the <paths> block IS the grant.
</preflight>

Source: round-8 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md` @1ca9e97fc9; PRD v0.13 @90f99888cd (ADMITTED); DECOMP_R9 @5d70aab6c9.
