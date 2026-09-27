# TO DSGN_IRPTV1.TO-IV-e-52 -- UIR-27 and UIR-29 in full (CTO 101768): one money format, one client total, Supervision/Advisory one click away; the pinned tests re-goldened to their intent

<to_id>DSGN_IRPTV1.TO-IV-e-52</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~29</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 (UIR-27, UIR-29) | **Decomp cell:** `IV-e-52` (decomp v7 addendum 7) | **outcome_ref:** FWD-2, FWD-11, FWD-15, FWD-16, FWD-18 | **depends_on:** IV-e-45 (merged, DEV 0a83fbc4) | **slot:** ~29, queue position 3 of 4 (before IV-e-50)

---

## WORKER FACE

### THE CELL

`IV-e-52` -- TO-IV-e-45 built the batch cell but met two rows only in part (rows `DSGN_IRPTV1-W29-S2`, `-W29-S3`), because older tests
pin the old markup. 1.0.0_SA_CTO ruled both (a) (101768), "read against the register's acceptance lines":

- **UIR-29 -- "One money format across the page; the client total appears once."** The identity card's `$1,234.56` format wins
  page-wide. "Once" means ONE authoritative total: the identity card's HOW MUCH (FWD-2). `tabs/holdings/HoldingsSummary.tsx` drops its
  own total. Should a non-USD position ever render, it shows its currency code. The page-local formatter is `tabs/holdings/format.ts`
  (IV-e-45's); every amount on the page goes through it.
- **UIR-27 -- "Supervision and Advisory are one click away (or hidden when withheld on every row)."** The parenthetical covers only the
  all-withheld case (IV-e-45 built it); in the ORDINARY case the two columns go one click away (a disclosure), off the face.
- **Re-golden, keeping each test's intent (the served values), in this cell:** the money sets and F39-AC7 the CTO names --
  `fe-s-39/adapter-plane.test.ts` (F39-AC7's byte-exact Advisory cell), `dsgn-irptv1/iv-e-18.census.test.ts`, `fe-s-7/slices.test.ts`,
  `dsgn-irptv1/iv-e-3.card-fed.test.ts`, `dsgn-irptv1/iv-e-33.client-words.test.tsx`, `dsgn-irptv1/iv-t-1.identity-card.test.ts` -- plus the two
  pinned tests IV-e-45 broke at the merge (DEV ad06e37f): `fe-s-30/predicate.test.ts` (F30-AC5, "ReportingTab imports the gate and mounts
  its body on it, with no partition of its own") and `fe-s-55/withheld-vs-unknown.test.ts` ("withheld vs an asserted unknown ... the
  words never cross"). For each: if the current ENDPOINT still requires the old behaviour, fix the CODE (class G); if it is retired by
  UIR-27/29, re-golden to the new markup with the intent kept (class R), and **each re-golden commit names the UIR row it serves**.

**Environment:** this slot's portal worktree, brought to local DEV 0a83fbc4 (every round-7 cell merged). Re-read every file; line numbers
in older records are stale. Run the eight pinned files first to measure your denominator. Do not start any server. The workspace
`portal` gitlink is NOT yours: never stage or commit it.

### ACCEPTANCE

<criterion id="IVE52-AC1" cell_refs="IV-e-52"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-29/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~29; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-52.money-and-disclosure.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: MONEY-AND-DISCLOSURE-OK</expect></criterion>
`IVE52-AC1` -- the built behaviour: a rendered page with a multi-account client shows every amount in one format, the client total exactly
once (the identity card's HOW MUCH; HoldingsSummary renders no total), a non-USD position with its currency code, and Supervision /
Advisory behind one disclosure in the ordinary case (and hidden when withheld on every row). Prints `VERDICT: MONEY-AND-DISCLOSURE-OK`
only when every arm holds.

<criterion id="IVE52-AC2" cell_refs="IV-e-52"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-29/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~29; timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-39/adapter-plane.test.ts src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-18.census.test.ts src/pages/InvestorReporting/__tests__/fe-s-7/slices.test.ts src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-3.card-fed.test.ts src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-33.client-words.test.tsx src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-1.identity-card.test.ts src/pages/InvestorReporting/__tests__/fe-s-30/predicate.test.ts src/pages/InvestorReporting/__tests__/fe-s-55/withheld-vs-unknown.test.ts 2>&1 | tail -20</invocation><expect>0 fail</expect></criterion>
`IVE52-AC2` -- the eight pinned files pass on the new behaviour, each keeping its intent.

<expected_criteria>IVE52-AC1, IVE52-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**`, `src/lib/**`, `src/ui/**`,
  `src/components/**` and every other page are READ, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** never type a firm token or a real client figure into a new file.
- **Portal law:** light canvas, white panels with a hairline, navy ink, one band per page (portal `CLAUDE.md`, `DESIGN.md`).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/format.ts
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsSummary.tsx
portal/src/pages/InvestorReporting/tabs/holdings/SliceTable.tsx
portal/src/pages/InvestorReporting/tabs/holdings/AllocationBars.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTreemap.tsx
portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-52.money-and-disclosure.test.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-39/adapter-plane.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-18.census.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-7/slices.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-3.card-fed.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-33.client-words.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-t-1.identity-card.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-30/predicate.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-55/withheld-vs-unknown.test.ts
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7 addendum 7, cell `IV-e-52`.
<owned_cells>IV-e-52</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE52-AC1, IVE52-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~29/DSGN_IRPTV1.TO-IV-e-52.money-and-disclosure.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE52-AC1,IVE52-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W29-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- measured at local DEV 0a83fbc4: rows W29-S2/S3 name the six pinned money/F39-AC7 files; the drain suite (ad06e37f) adds fe-s-30 F30-AC5 and fe-s-55 as new failures under IV-e-45.
lane: the <paths> block IS the grant; slot ~29, queued before IV-e-50 (which then measures the final DEV).
</preflight>

Seating: slot ~29, queue position 3 of 4, after IV-e-45; IV-e-50 (the harness) runs after this.

**Issuer close (2.0.0_SA_COO~D, 2026-09-27 ~05:1xZ; rows W29-S2/S3 closed, W29-S7 moved):** IVE52-AC1 PASS (MONEY-AND-DISCLOSURE-OK). IVE52-AC2 read 38 pass / 1 fail; the one failure is F30-AC4, which was already failing at the base (DEV ad06e37f, suite log) and is not one of the two tests this order named as IV-e-45's breakage -- an issuer cut defect (the criterion's file list carried a pre-existing residual). F30-AC4 moves to TO-IV-e-50 (amendment 1), whose bar is only Q rows fail. Merged at DEV 200d257a (tsc 0, lint 0, suite 898 / 17).
