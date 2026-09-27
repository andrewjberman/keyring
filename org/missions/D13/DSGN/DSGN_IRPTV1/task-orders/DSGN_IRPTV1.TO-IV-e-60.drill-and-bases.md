# TO DSGN_IRPTV1.TO-IV-e-60 -- The breadcrumb names the account; every percentage states its base; no one-slice pie (UIR-32/33/34/36/47/49)

<to_id>DSGN_IRPTV1.TO-IV-e-60</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~38</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<round>8</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 | **Round:** 8 (CTO analysis @36e18bf320, msg 101845) | **Decomp cell:** `IV-e-60` (decomp v8) | **outcome_ref:** FWD-14, FWD-6 | **depends_on:** IV-e-59 (same slot; DrillTree.tsx) | **slot:** ~38, queue position 2 of 3

---

## WORKER FACE

### THE CELL

`IV-e-60` -- Rows (verbatim, PRD v0.16): UIR-31 "Drilling into an account sets the account focus, and choosing an account opens its drill; the two always agree." UIR-32 "The breadcrumb names the account, the account and its strategy show the same tail, and one masking style is used." UIR-33 "Every percentage states its base (of this account / of the client), or both views use one base." UIR-34 "A level with one child shows no pie (or shows the next level down)." UIR-36 and UIR-47 "As UIR-33." UIR-49 "As UIR-31 and UIR-32."

Window 9: after drilling into the first account the breadcrumb reads "All holdings / Models". `tabs/holdings/DrillTree.tsx`
`Breadcrumbs` :439-486; at :568-571 it drops the root when there is one root, and in a one-account snapshot that root IS the account,
so the account disappears. Labels: `tabs/holdings/slices.ts` `maskedLabelFor` :402-405 and `initialDrillRef` :464-472. Percentages:
`renderInsideLabel` :121-145 prints `pctOfParent` with the base only in a `data-pct-base` attribute; `DonutHoverTooltip` :229-240;
`tabs/holdings/SliceTable.tsx` :207 ("% of total"), :224 (hover "% of parent"), :263. One-child levels: the table-only branch at
:602-608 checks `rows.length`, but the pie draws `donutRows`, which drops null amounts (:501), so one slice can still render.

**Build:** The breadcrumb always names the account (with the same masked tail the account and its strategy show, one masking style), even
when it is the only root. Every percentage on the pie label, tooltip and table says its base in words ("of this account" / "of the
client"), or both views use one base and say it once. A level whose DRAWN rows number one shows no pie (the table, or the next level
down). UIR-31's focus/drill agreement from IV-e-42 must still hold.

**Environment:** the portal worktree is based on your slot after IV-e-59. Other round-8 workers run in parallel in their own worktrees on disjoint files; edit only your `<paths>`. Do not start any server.

### ACCEPTANCE

<criterion id="IVE60-AC1" cell_refs="IV-e-60"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-38/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-60.drill-bases.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: DRILL-BASES-OK</expect></criterion>
<criterion id="IVE60-AC2" cell_refs="IV-e-60" judgment="true"/>
`IVE60-AC2` -- judgment: UIR-31/32/33/34/36/47/49 read on the running page (round-8 walk), graded by 3.0.0_SA_CVO at L9. Record it in your instance as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

Each mechanical criterion prints its expect string only when every arm holds. slices.ts: edit only maskedLabelFor / initialDrillRef and percentage-base helpers; HOLDINGS_FOOTER_SOURCE (:332) belongs to IV-e-63. If iv-e-42.drill-bases.test.tsx does not exist under that name, re-golden nothing and file no row for it.

<expected_criteria>IVE60-AC1, IVE60-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `src/lib/**`, `contracts/**` (unless named), other pages and every file not named are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/tabs/holdings/SliceTable.tsx
portal/src/pages/InvestorReporting/tabs/holdings/slices.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-60.drill-bases.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-42.drill-bases.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8, cell `IV-e-60`.
<owned_cells>IV-e-60</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE60-AC1, IVE60-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~38/DSGN_IRPTV1.TO-IV-e-60.drill-and-bases.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE60-AC1,IVE60-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W38-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3f76cdb2 (issuer, 2026-09-27 ~08:1xZ); file:line facts above are from that read.
lane: the <paths> block IS the grant; disjoint from every parallel round-8 chain (decomp v8 table).
</preflight>

Seating: slot ~38, queue position 2 of 3; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 38 --portal-ref <DEV at seating>` when C: allows (0.0.0_AB_MSTR 101618).
