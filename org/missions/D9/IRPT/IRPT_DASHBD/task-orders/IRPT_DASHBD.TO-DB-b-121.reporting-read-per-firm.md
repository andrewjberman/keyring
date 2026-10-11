# TO IRPT_DASHBD.TO-DB-b-121 -- one read-only cell before any build: what the reporting read needs per firm and whether Cottonwood has it; whether the page's year-to-date needs the reporting summary once performance answers; what DB-b-86's hop3 reads of the Cottonwood returns gold

<to_id>IRPT_DASHBD.TO-DB-b-121</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~96</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>65</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ruling msg 4459 (FWD-11 is unbuilt for the reporting read; one read-only cell before any build), on DSGN_IRPTV1's record `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~51/FIRM_BINDING_PLACED.json` | **Decomp cell:** `DB-b-121` (decomposition section 67) | **outcome_ref:** FWD-11 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-96`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~96/`. Portal code is read by content at the DEV tip:
`git -C C:/dev/ajb_workspace/portal show 733986d7c6989c8be26a964344e663e7f372a213:<path>` (the `portal/` directory in your worktree is empty).

**The cell (`DB-b-121`).** A real signed-in walk of the Investor Reporting page for a Cottonwood client broke at the Performance tab. One of its two
refusals is this project's: the reporting summary and manifest answered `FIRM_BINDING`, emitted at
`infra/aws/lambda/investor-reporting/_authz/served.py:1214`, because the reporting-read function's firm-to-bucket map holds ONE firm by design
(`infra/aws/terraform/investor-reporting/reporting-read/locals.tf:57-59`). The CTO ruled (msg 4459): that is the route doing what it was built to
do; FWD-11 (every client firm) is not built for the reporting read. Before any build it asks two lines, and the build's shape (one function per
firm, or one map) is ruled on them. The issuer adds a third, for this project's one open order.

1. **What the reporting read needs per firm, and whether Cottonwood has it.** Read the reporting-read function end to end: its Terraform root
   (`infra/aws/terraform/investor-reporting/reporting-read/`: locals, role, environment, the source rows it declares) and its handler
   (`infra/aws/lambda/investor-reporting/reporting/` and the `_authz` loaders it uses). List EVERYTHING a firm must have for a summary, a manifest
   and a series read to answer: the platinum table(s) and prefix(es), each built by `lib/opal_naming.py address()` (print the builder call and its
   output for 49financial and for cottonwood; never type an address), the registry rows, the role's reach, the directory map entry, any
   environment variable. `per_firm_needs`: [{need, source: {file, line}}], with the denominator of what you read.
   Then, for Cottonwood, `cottonwood_has`: one entry per need, state `PRESENT`, `ABSENT`, `ACCESS_DENIED` or `NOT_ESTABLISHED`, with evidence.
   - Registry and Terraform needs are read from the tree.
   - Published data: what PRODUCES the platinum reporting files (the publisher, its schedule, its firm scope), with file and line, and whether that
     producer runs for Cottonwood at all. For whether the files exist you may make S3 LIST reads through `.tools/aws` on the builder-output
     prefixes, with the same list on 49financial as the positive control. dell2 seats are denied on some Cottonwood prefixes: an AccessDenied is
     recorded as `ACCESS_DENIED` with its text, NEVER as absence; a list that returns 0 keys beside a control that returns keys is `ABSENT`.
   - The Cottonwood returns gold was minted on 2026-10-11 (ADVI_COTBKF): read its record
     `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_MINT_ARD_COTTONWOOD_DRAIN_END_20261011.md` and
     `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json` (its caveats matter: how many rows are
     measured, that no bond day is measured, what `holdings_price_return_reason` reads). State what the reporting publisher would make of that
     table as it stands: which of the page's figures it could serve and which it could not, from the publisher's own code.
2. **Does the page's year-to-date need the reporting summary at all once performance answers?** The other refusal (`OBJECT_NOT_COVERED` on the
   performance route) is being removed by IRPT_BCKEND (its cell IB-pr-421). Read the Performance tab's loader at the DEV tip
   (`src/pages/InvestorReporting/tabs/ReportingTab.tsx` and the reporting client it calls, `reportingRead.ts`, and what feeds the header's YTD
   label): when `/performance` answers and the reporting summary and manifest still refuse, does the tab show the year-to-date return and its
   spread, a partial state, or a refusal? `ytd_needs_summary`: `YES`, `NO` or `NOT_ESTABLISHED`, with `because` in plain words and `basis`
   [{file, line, repo: "portal"}] citing the branch that decides it.
3. **DB-b-86's hop3.** This project's one open order waits on a run of `data/assets/scripts/gold/irpt_custody/hop3_real_run.py` on the laptop
   (order `org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-86.e2a-real-statement-apply.md`, AMENDMENT 3). Read the script and its
   test: `hop3` {reads: [{what, source: {file, line}}] (every table and prefix it reads, by builder call), reads_cottonwood_returns_gold (bool),
   existing_readers (the count of readers of that Cottonwood table the tree shows today, with how you counted), writes: [...]}. ADVI_COTBKF's
   ADDENDUM 11.1 makes a reader of that table its own never-widen pair; say what the pair would have to name (the keys read, nothing more).
Write `REPORTING_READ_PER_FIRM.json` and a one-page `.md` whose first lines are the two answers the CTO asked for, each in two sentences.

<criterion id="DB65-1-AC1" cell_refs="DB-b-121"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r65/p65_round65.py" . DB65-1-AC1</invocation><expect>DB65-1-AC1 PASS</expect></criterion>
`DB65-1-AC1` -- every per-firm need of the reporting read is listed with its source and graded for Cottonwood, the year-to-date question is answered from the page's own branch, and hop3's reads are listed. Base: FAIL.

<expected_criteria>DB65-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** S3 LIST reads on builder-output prefixes, each beside its positive control. No object body is downloaded.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant or a filled figure is a defect: stop and
  file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~96/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~96/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-121.reporting-read-per-firm.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 67 (round 65), cell `DB-b-121`.
<owned_cells>DB-b-121</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB65-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~96/IRPT_DASHBD.TO-DB-b-121.reporting-read-per-firm.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB65-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, the criterion's last line, the two answers the CTO asked for, the per-firm needs with Cottonwood's state for each, the hop3 reads, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only cell; no producer, contract or infra edit.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 list reads inside the seat's existing reach; a deny is recorded, never worked around.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the worker reads the reporting routes and their function as source.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the worker reads the publisher's schedule and firm scope as source.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: RUN -- DB65-1-AC1 FAIL at base (no record). CTO ruling msg 4459.
lane: the <paths> block IS the grant.
</preflight>
