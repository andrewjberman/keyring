# TO DSGN_IRPTV1.TO-IV-e-46 -- Advisor Intelligence's composition admits the ETF Classifier's structured and commodities classes, each labelled and coloured (CTO 101579)

<to_id>DSGN_IRPTV1.TO-IV-e-46</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~30</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.15 @f12fcbb16e (UIR-50, FWD-23) | **Decomp cell:** `IV-e-46` (decomp v7 addendum 1; workstream AI-TAGS, outside the rounds) | **outcome_ref:** FWD-23 (UIR-50, the Advisor Intelligence readers) | **depends_on:** -- | **slot:** ~30, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-46` -- Andrew's rule (UIR-50, ruled (a) by the CTO): a security the ETF Classifier tags keeps that class; the class list gains
`structured` and `commodities`. The data producer (2.0.0_SA_COO~M) writes those values only after every reader admits them. Its reader
census (`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/ETF_TAGS_READER_CENSUS_20260926.md`, Part 3) names the Advisor
Intelligence readers that drop them today:

- `_shared/lib/composition.ts` `normalizeMixTo4Class` (:32 `CANONICAL_CLASSES`, :43 the with-cash list, :90-93) keeps only the listed
  classes, SKIPS any other (:108 `if (!classes.includes(item.asset_class)) continue`), then re-percents over the kept ones (:119, :125),
  so the other slices inflate with no visible gap.
- The partner layouts' `assetClasses.ordered` lists are fixed keys: `_partners/49financial/layout.ts:89`, `_partners/cottonwood/layout.ts:125`,
  `_partners/inflection/layout.ts:126`, `_partners/demo/layout.ts:75`.
- Labels: `_shared/components/PartnerAnalytics.tsx` `MIX_CLASS_LABELS` (:74-80) and the class colour resolver below it (tenant
  `colorPalette` override, else the global `MIX_PIE` palette in `src/lib/chartColors.ts`).

**Build:** every reader above admits `structured` and `commodities`: kept in the mix (never skipped, never folded into another class),
counted in the total they are percented over, placed in each partner's `ordered` list, labelled "Structured" and "Commodities", and
coloured. Each colour is distinct from every existing mix colour and from every model colour (`src/lib/modelPortfolioColors.ts`, read
only). Add the two colours to `MIX_PIE` in `src/lib/chartColors.ts` as NEW keys only; no existing key's value changes. A client with
neither class renders exactly as today. Each firm's layout file is edited on its own; nothing is copied from one firm's file to another.

**Environment:** the portal worktree is based on DEV `6757223a`. Both test files do not exist at the base; write them against synthetic
in-memory mix payloads (no real client figure, no firm token in the test file). Do not start any server.

### ACCEPTANCE

<criterion id="IVE46-AC1" cell_refs="IV-e-46"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-30/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~30; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/iv-e-46.composition-tags.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: COMPOSITION-TAGS-OK</expect></criterion>
`IVE46-AC1` -- the built behaviour with its control. A mix payload carrying equity, fixed_income, alternatives, structured and
commodities, run through `normalizeMixTo4Class` for each partner's options, keeps all five classes, their percentages sum to 1 over the
full total, and each new class carries its label and a colour distinct from every other mix colour and every model colour. Control arm:
a payload with neither new class yields the same output as the base code for the same input. Prints `VERDICT: COMPOSITION-TAGS-OK`
only when every arm holds.

<criterion id="IVE46-AC2" cell_refs="IV-e-46"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-30/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~30; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: CLASS-READERS-OK</expect></criterion>
`IVE46-AC2` -- the reader census. Every source file under `src/pages/AdvisorIntelligence/` (tests excluded) that names an asset-class key
list (`'alternatives'` beside `'equity'`/`'fixed_income'`) is enumerated with its count printed, and each one either admits `structured`
and `commodities` or is listed by file:line in the test as a named non-mix reader with the reason it cannot drop them. Prints
`VERDICT: CLASS-READERS-OK` only when every enumerated file is one or the other.

<expected_criteria>IVE46-AC1, IVE46-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every other file, including every other
  `src/lib/**` file and the Investor Reporting page, is READ, never edited. A needed edit outside the grant is a surprise row, not an edit.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Firms:** each firm's layout is its own file and is edited on its own; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts
portal/src/pages/AdvisorIntelligence/_shared/components/PartnerAnalytics.tsx
portal/src/pages/AdvisorIntelligence/_partners/49financial/layout.ts
portal/src/pages/AdvisorIntelligence/_partners/cottonwood/layout.ts
portal/src/pages/AdvisorIntelligence/_partners/inflection/layout.ts
portal/src/pages/AdvisorIntelligence/_partners/demo/layout.ts
portal/src/lib/chartColors.ts
portal/src/pages/AdvisorIntelligence/__tests__/iv-e-46.composition-tags.test.ts
portal/src/pages/AdvisorIntelligence/__tests__/iv-e-46.class-readers.test.ts
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7 addendum 1, cell `IV-e-46`.
<owned_cells>IV-e-46</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE46-AC1, IVE46-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~30/DSGN_IRPTV1.TO-IV-e-46.composition-tags.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE46-AC1,IVE46-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W30-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- the reader lines are 2.0.0_SA_COO~M's census (ETF_TAGS_READER_CENSUS_20260926.md Part 3), read at portal DEV 6757223a: composition.ts :32/:108, the four partner ordered lists (:89, :125, :126, :75).
lane: the <paths> block IS the grant; disjoint from every round-7 chain (no InvestorReporting file). src/lib/chartColors.ts gains new keys only.
</preflight>

Seating: slot ~30, queue position 1 of 1; `.tools/wk-provision.sh provision DSGN_IRPTV1 30 --portal-ref 6757223ad648f015276a33b5ff8aab47b91e62f1`.
Drain: a product-file candidate outside DSGN_IRPTV1's page -- 1.0.0_SA_CTO reviews it before it lands on DEV (CTO 101579).
