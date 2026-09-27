# TO DSGN_IRPTV1.TO-IV-e-58 -- Each account picker entry shows the account value AND its YTD (UIR-15, FWD-20)

<to_id>DSGN_IRPTV1.TO-IV-e-58</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~36</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<round>8</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 | **Round:** 8 (CTO analysis @36e18bf320, msg 101845) | **Decomp cell:** `IV-e-58` (decomp v8) | **outcome_ref:** FWD-19, FWD-20 | **depends_on:** none | **slot:** ~36, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-58` -- Rows (verbatim, PRD v0.16): UIR-15 "Each picker entry shows a distinct label and the account's value." CTO 101845 E3: FWD-20's YTD is added BESIDE the value, not in place of it; the identical-label half of UIR-15 stays 2.0.0_SA_COO~M's (UIR-26).

The Performance chooser lists `****9079 / IRA -- 5.93%`: the YTD REPLACES the account value (window 9). The label is built at
`tabs/holdings/AccountFilter.tsx:220-227` (line 225) -- YTD replaces the value when `accountYtd` is supplied; helpers `formatAccountYtd`
:103-107 and `formatAccountFilterValue` :170-177. The account label comes from `header/IdentityCard.tsx` `accountListFromSnapshot`
:174-184 (read only). Mounted at `tabs/reporting/ReportingTab.tsx:570-577`. One account read `-100.00%` YTD in the walk: a YTD that is
not a finite answer (PARTIAL with no figure, UNAVAILABLE, or a -100% produced by a missing value) shows its state, not a number.

**Build:** Each entry reads label, value, then YTD (for example `****9079 / IRA -- $123,456.78 -- YTD 5.93%`), with the page's money format
(the card's `$1,234.56`, CTO 101768). While the YTD is pending or refused, the entry shows the value and the YTD state word
("YTD pending", "YTD unavailable"), and a PARTIAL answer that carries a figure shows the figure (round-7 candidate 2). The Holdings
account filter, which shows value only, is unchanged.

**Environment:** the portal worktree is based on local DEV `3f76cdb2` (round 7 drained). Other round-8 workers run in parallel in their own worktrees on disjoint files; edit only your `<paths>`. Do not start any server.

### ACCEPTANCE

<criterion id="IVE58-AC1" cell_refs="IV-e-58"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-36/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-58.picker-entries.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: PICKER-ENTRIES-OK</expect></criterion>
<criterion id="IVE58-AC2" cell_refs="IV-e-58" judgment="true"/>
`IVE58-AC2` -- judgment: UIR-15 read on the running page (round-8 walk), graded by 3.0.0_SA_CVO at L9. Record it in your instance as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

Each mechanical criterion prints its expect string only when every arm holds. AC1 arms: value and YTD both present; YTD pending; YTD refused; PARTIAL with a figure; the Holdings filter unchanged (control). IV-e-40's test may be re-goldened where it asserted YTD in place of the value, naming UIR-15.

<expected_criteria>IVE58-AC1, IVE58-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `src/lib/**`, `contracts/**` (unless named), other pages and every file not named are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/AccountFilter.tsx
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-58.picker-entries.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-40.account-ytd.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8, cell `IV-e-58`.
<owned_cells>IV-e-58</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE58-AC1, IVE58-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~36/DSGN_IRPTV1.TO-IV-e-58.picker-value-and-ytd.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE58-AC1,IVE58-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W36-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3f76cdb2 (issuer, 2026-09-27 ~08:1xZ); file:line facts above are from that read.
lane: the <paths> block IS the grant; disjoint from every parallel round-8 chain (decomp v8 table).
</preflight>

Seating: slot ~36, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 36 --portal-ref <DEV at seating>` when C: allows (0.0.0_AB_MSTR 101618).
