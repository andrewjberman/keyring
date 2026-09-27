# TO DSGN_IRPTV1.TO-IV-e-67 -- A data-less QUEUED export answer starts the receipt poll (row S26, CTO 102138)

<to_id>DSGN_IRPTV1.TO-IV-e-67</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~41</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Decomp cell:** `IV-e-67` (decomp v8 addendum 4) | **outcome_ref:** FWD-9 (the export hop) | **depends_on:** IV-e-64 (merged) | **slot:** ~41, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-67` -- close row `DSGN_IRPTV1-S26`. On the running page (window 18, local DEV `3b98939b`) the served async export answered the
ONE `POST /api/scoped/investor-reporting/export?selected_tenant=...` with HTTP 200 in 3.1 s and a body with NO `data` member:
`{contract_version, operation: "submit-export", firm_id, unprojected_grant, status: {operation: {operation_id: "submit-export",
operation_kind: "write", revision: "exr_<24 hex>"}, state: "QUEUED", source_dates: {business_date, source_completion_date: null},
actions: [{action: "NONE", safe: true, description}], public_reason_code: "EXPORT_QUEUED"}}`. The contract's ruling R2 (CTO 102138,
backend @75156f2b18) makes `data` optional while `status.state` is QUEUED or RUNNING, with the export id in `status.operation.revision`.
The page instead went idle and never polled. At portal DEV `3b98939b` (IR = portal/src/pages/InvestorReporting):

- `IR/contracts/envelope.ts` `parseIrEnvelope` (:321) throws `EnvelopeMismatch('data')` whenever `data` is absent; the status must still
  pass `requirePublicStatus` (`contracts/public-status.ts:20-42`, checked at `envelope.ts:296`), which the served QUEUED status does.
- `src/api/endpoints/investor-reporting.ts` `submitExport` (:1212-1227; interface :826; fixture :1524) returns the adapted `data` as the
  receipt; `getExportReceipt` (:1229) is the receipt read (GET `/export/{exportId}`), already carrying `selected_tenant`.
- `IR/export/submit.ts` `interpretSubmitExportAnswer` (:363-382) already decodes both shapes (data present -> receipt; data absent with
  QUEUED/RUNNING -> `{exportId: status.operation.revision, receipt: null}`; anything else refuses by name) but nothing calls it;
  `SubmitOutcome` / `submitUnderGate` (:149-165) have no queued variant.
- `IR/export/ExportButton.tsx` `handleSubmit` (:213-232) stores the receipt the submit returned; `.catch` sends the flow back to idle.

**Build:** a submit answered with `data` absent and `status.state` QUEUED or RUNNING is accepted for `submit-export` (and a receipt read
answered the same way is accepted for `export-receipt`): the envelope parser lets that one shape through (public status still required;
any other state without `data` still refuses by name). `submitExport` yields `{exportId, receipt: null}` for it through
`interpretSubmitExportAnswer`. `ExportButton` then starts the existing receipt poll on that `exportId`
(`api.getExportReceipt({..., exportRef: exportId, selectedTenant})`), shows the queued/running state while it polls, and stops at READY
(download link, as today) or at a named FAILED/refused state. A submit that returns a receipt (`data` present) behaves exactly as
today. No backend change; no route added.

**Environment:** the portal worktree is based on local DEV `3b98939b` (round 8 drained). No other worker is running. Do not start any
server. Work ONLY in your own <WS>.

### ACCEPTANCE

<criterion id="IVE67-AC1" cell_refs="IV-e-67"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-41/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-67.queued-export-poll.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: QUEUED-EXPORT-POLL-OK</expect></criterion>
`IVE67-AC1` -- the built behaviour, with its control. Against a recording fake fetch / api: (a) a submit answered with the W18 data-less
QUEUED body (the shape above, synthetic ids) is accepted and yields the `exr_` id; (b) the flow then issues receipt reads for that id
carrying the selected tenant, and stops at READY with the download link when the fake answers READY; (c) a fake answering a named FAILED
stops the poll and shows that state; (d) control: a submit answered WITH `data` (a receipt) behaves as today, and a data-less answer
whose state is not QUEUED/RUNNING is still refused by name. Print `VERDICT: QUEUED-EXPORT-POLL-OK` only when every arm holds.

<expected_criteria>IVE67-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. In `envelope.ts` change only the `data`
  presence rule for `submit-export` / `export-receipt`; in `investor-reporting.ts` only `submitExport` (and its interface/fixture lines).
  `src/lib/**` and every other page are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on local DEV `3b98939b`). Commit through `.tools/safe-commit.sh`. Never
  push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** synthetic ids only; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/contracts/envelope.ts
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/InvestorReporting/export/submit.ts
portal/src/pages/InvestorReporting/export/ExportButton.tsx
portal/src/pages/InvestorReporting/export/ReceiptPanel.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-67.queued-export-poll.test.tsx
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8 addendum 4, cell `IV-e-67`.
<owned_cells>IV-e-67</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE67-AC1. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~41/DSGN_IRPTV1.TO-IV-e-67.queued-export-poll.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE67-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W41-S<k>`). The `__tests__/` grant is for re-goldening a pinned test that asserted `data` is always required, each naming S26.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read at portal DEV 3b98939b: envelope.ts:321 requires data; submit.ts:363-382 interpretSubmitExportAnswer decodes the data-less QUEUED shape but is unused; ExportButton.tsx:213-232 goes idle on the parse throw; window-18 HAR shows the data-less QUEUED body (row S26; CTO 102138 re-routed S26 here).
lane: the <paths> block IS the grant; no worker is running.
</preflight>

Seating: slot ~41, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 41 --path <abs> --portal-ref <DEV 3b98939b>`.
