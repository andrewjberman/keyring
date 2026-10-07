# TO MDPF_SECCLASS.TO-SC-e24 -- round 8 SC-e-24: the census of every screen that shows a mix by class, and one stated mapping from the six classes to its groups, as data

<to_id>MDPF_SECCLASS.TO-SC-e24</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~23</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** placement DELL1 (the project row's `fabric` still reads laptop) | **Decomp cell:** `SC-e-24`
(`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) | **outcome_ref:** FWD-16 | **depends_on:** none. Slot `~23` queue: this order
first, then `MDPF_SECCLASS.TO-SC-e33` (no data edge; same slot).

---

## WORKER FACE

### THE CELL

`SC-e-24`. "The census of every screen that shows a mix by class: the groups it shows, and one stated mapping from the six
classes to them, as data; the geography list S26 placed" (R8).

FWD-16 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12): "Anyone looking at a mix by asset class on
any screen can say how the shared list's six classes became that screen's groups." ACCEPT: "each screen that shows fewer
groups than the shared list's six classes has one stated mapping that the person looking at it can read. Every security that
changes group when a screen switches to the shared list was named before the switch." This cell delivers the census and the
mapping as DATA. Showing the mapping on each screen is a later round (R8 coverage table). Naming the securities that change
group is the switch's own round.

**The six (Andrew-direct 2026-10-05 call 2, PRD addendum v0.10; and 2026-10-07):** `cash`, `fixed_income`, `equity`,
`structured`, `alternatives`, `commodities`. There is no seventh: `multi_asset` is retired (cell `SC-e-23` removes it from the
portal). Where a screen still shows "Multi-Asset" in your tree, record it as a group the screen shows today and note that
`SC-e-23` removes it.

**S26 (PRD addendum v0.7 manifest):** "the geography list in `yang-generate-positioning/lambda_function.py:95` ... no home in
the list is decided." Measured at this cut: `ETF_GEOGRAPHY_MAPPING` begins at line 96 of
`infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`. Record its source line,
its distinct values, and where it belongs: a new field on the shared list, or `OPEN` with the reason. Proposing is your job;
deciding is the CTO's.

**Build (read-only census; you edit no product file):**
1. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/screen_group_census.py`: a script that walks the
   portal source (`<WS>/portal/src`) and the producers that build each screen's mix. It prints
   `SCREEN-GROUP-CENSUS files_scanned=<n> screens=<n>`. It must finish within 120 s.
   - Start from the class lists and layouts: `src/lib/chartColors.ts` (`ASSET_CLASS`, `MIX_PIE`), the Advisor Intelligence
     partner layouts `src/pages/AdvisorIntelligence/_partners/*/layout.ts` and `_shared/lib/composition.ts`, the Investor
     Reporting Holdings class list `src/pages/InvestorReporting/tabs/holdings/assetClass.ts`, Positioning's
     `ASSET_CLASS_ORDER` (`src/components/holdings/HoldingsTreemapChart.tsx`), and the Attribution page's categories
     (`src/pages/Attribution/constants/etf-categories.ts`, surface S23).
   - Find any other screen by searching the source, and print the denominator.
2. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/SCREEN_GROUP_MAPPING_20261007.json`, in exactly the shape the
   AC1 check's docstring states (read it first: `R10_CHECKS/screen_group_mapping_check.py`).
   - One `screens` entry per screen a person sees: its files, its groups, and for any screen with fewer than six groups the
     mapping of each of the six to one of its groups.
   - Each mapping carries `basis`: `measured` where the code states it, `inferred` where you propose it.
   - A screen that shows the six one-to-one needs no mapping. Still list it.
3. `.../MDPF_SECCLASS_M/SCREEN_GROUP_MAPPING_20261007.md`: the same as a table a person can read, with every `inferred`
   mapping named as a proposal.

### ACCEPTANCE

<criterion id="SC8-e24-AC1" cell_refs="SC-e-24"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/screen_group_mapping_check.py</invocation><expect>SCREEN-GROUP-MAPPING ok=True</expect></criterion>
`SC8-e24-AC1` -- the mapping file exists in the stated shape: a printed denominator, the exact six, at least one screen, every screen with fewer than six groups mapped onto its own groups, every cited file present, the S26 geography list recorded.

<criterion id="SC8-e24-AC2" cell_refs="SC-e-24"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/screen_group_census.py</invocation><expect>SCREEN-GROUP-CENSUS files_scanned=</expect></criterion>
`SC8-e24-AC2` -- the census re-runs from the script and prints its denominator, so the file in AC1 can be reproduced.

<expected_criteria>SC8-e24-AC1,SC8-e24-AC2</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`file=ABSENT`); AC2 FAIL as expected (no script). The AC1 check is the
issuer's judge: you READ it and never edit it. Whether a proposed mapping is right is the CVO's to grade, not AC1's.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted. You edit NO portal file and no producer. The portal tree is your READ surface.
- **No AWS write, no deploy, no vendor or model call.**
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W23-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/screen_group_census.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/SCREEN_GROUP_MAPPING_20261007.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/SCREEN_GROUP_MAPPING_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-24`.
<owned_cells>SC-e-24</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e24-AC1, SC8-e24-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~23/MDPF_SECCLASS.TO-SC-e24.screen-group-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e24-AC1,SC8-e24-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the screens and their group counts; each `inferred` mapping; the S26 placement proposal; both outputs; commits.
Your next order, `MDPF_SECCLASS.TO-SC-e33`, follows in this same worktree once this one is terminal.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery 2026-10-07 ~07:3xZ: no gate names FWD-16.
comp-iam: RUN -- R8 battery: not applicable (a read-only source census).
comp-adversary: RUN -- R8 battery on the decomposition. Cell-specific read by the issuer: S26's list begins at line 96, not 95 (the PRD's line is held from the brief). BLIND: screens whose groups are computed by a producer at run time rather than declared in source (the census names the producer it reads).
lane: the <paths> block IS the grant.
portal_ref: 8ddfe409948cc79bb45e5ac27a8136264ce8c9d4 (portal origin/DEV at the cut). Provision with `--portal-ref 8ddfe409948cc79bb45e5ac27a8136264ce8c9d4 --node-modules none` (read only; no tests run).
</preflight>

Source: DECOMP_R8 @495efa3c32 (origin 1640a0e86e); PRD v0.12 @87ad6d2e4c.
