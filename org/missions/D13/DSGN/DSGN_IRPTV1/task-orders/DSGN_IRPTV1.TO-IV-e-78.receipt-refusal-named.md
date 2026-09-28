# TO DSGN_IRPTV1.TO-IV-e-78 -- A refused or non-pending export-receipt read is shown by name, never a silent idle (row S27, CTO 102222)

<to_id>DSGN_IRPTV1.TO-IV-e-78</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~41</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Decomp cell:** `IV-e-78` (decomp v9 addendum 1) | **outcome_ref:** FWD-11 (a refusal reads by name), FWD-9 (the export hop) | **depends_on:** IV-e-67 (merged, local DEV 8808eeb6) | **slot:** first slot to free (net-zero reuse), queue position 1 of 1; runs before IV-e-75 (both write ExportButton.tsx / submit.ts)

---

## WORKER FACE

### THE CELL

`IV-e-78` -- close the page half of row `DSGN_IRPTV1-S27`. On the running page (window 19, local DEV `8808eeb6`) the ONE export submit
answered QUEUED (`exr_<24 hex>` in `status.operation.revision`) and the page, per IV-e-67, started the receipt poll. The FIRST
`GET /api/scoped/investor-reporting/export/{exportId}?selected_tenant=...` answered HTTP 200 with NO `data` member and
`status: {operation: {operation_id: "export-receipt", operation_kind: "read", revision: "v1"}, state: "UNAVAILABLE", source_dates: {...},
actions: [{action: "NONE", safe: true, description}], public_reason_code: "NOT_READY"}`, `ok: false`. The page refused that read, the
poll stopped, and the export panel returned to idle with NO reason shown. Ruling (CTO 102222): the backend will answer RUNNING while an
export is pending; the page must NOT treat UNAVAILABLE or any reason code as pending (no poll-on-UNAVAILABLE); it must show ANY refused or
non-pending receipt read BY NAME. At portal DEV `8808eeb6` (IR = portal/src/pages/InvestorReporting):

- `IR/export/ExportButton.tsx` `handleSubmit` (:214-249): the queued branch calls `pollExportReceipt(...)` and its `.catch(() =>
  setFlow((prev) => flowReceipt(prev, prev.receipt)))` returns the flow to its previous (empty) receipt and sets nothing else. The page
  already has a named-refusal slot: `refusal` state (:212) rendered as `<p data-slot="export-refusal" data-gate="refused-at-submit">`
  (:279-281).
- `IR/export/submit.ts` `pollExportReceipt` (:277-295) reads until a terminal `jobState` (ready/failed/expired) or `maxAttempts`; a read
  that throws rejects the whole poll.
- `src/api/endpoints/investor-reporting.ts` `getExportReceipt` (:1286) goes through `send(...)` and the envelope parser
  (`IR/contracts/envelope.ts` :315-343): a status whose `public_reason_code` is a refusal code is returned/raised as a refusal, and a
  data-less answer whose state is not QUEUED/RUNNING throws `EnvelopeMismatch('data', 'export-receipt')`.

**Build:** when the receipt poll ends WITHOUT a READY or FAILED/expired receipt -- a read rejected (refusal envelope, envelope mismatch,
HTTP error) or the attempt bound spent while still queued/running -- the export panel shows the reason BY NAME in the existing
`data-slot="export-refusal"` element (a new `data-gate` value, e.g. `refused-at-receipt`), carrying the public reason code where the
answer named one (e.g. `NOT_READY`) and a plain named reason otherwise (e.g. the envelope mismatch, or "still building after N reads").
The submit control returns to its usable state; the flow never goes silently idle. A READY receipt (download link) and a FAILED receipt
render exactly as today. Do NOT add UNAVAILABLE, NOT_READY or any reason code to the pending states; the poll's pending states stay
queued/running. No backend change; no route added; `envelope.ts` is not edited.

**Wire copy (amendment 1, CTO 102228 / 102238):** contract ruling R11 (ratified, CVO @ab453f59ed; wording @25f7581ded, both in your
base) makes `export-receipt`'s `data` optional while QUEUED or RUNNING, mirroring R2, and changed
`<workspace>/docs/contracts/investor-reporting/v1/responses/export-receipt.response.schema.json`. The portal's generated wire copy
`IR/contracts/wire/responses.ts` is now stale against it: at portal DEV the pinned regeneration test
`__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts` fails with "gen-wire.ts regeneration is not byte-identical to the committed files:
responses". Regenerate `responses.ts` with the existing generator `__tests__/fe-s-13/gen-wire.ts` against your worktree's schemas (never
hand-edit a generated file), check that the regenerated `export-receipt` type makes `data` optional as R11 says, and commit it. The
generator and the schemas are read, never edited.

**Environment:** base your portal worktree on local DEV `8808eeb6`. Do not start any server. Work ONLY in your own <WS>.

### ACCEPTANCE

<criterion id="IVE78-AC1" cell_refs="IV-e-78"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-78.receipt-refusal-named.test.tsx 2>&1 | tail -15</invocation><expect>VERDICT: RECEIPT-REFUSAL-NAMED-OK</expect></criterion>
`IVE78-AC1` -- the built behaviour, with its control. Against a recording fake api: (a) a submit answered QUEUED (synthetic `exr_` id),
then a receipt read answered with the window-19 body above (data-less, UNAVAILABLE, NOT_READY): the panel shows the `export-refusal`
element naming `NOT_READY`, the flow is not left submitting, and NO further receipt read is issued (no poll-on-UNAVAILABLE); (b) a
receipt read that throws a non-refusal error shows a named reason in the same element; (c) a fake that stays RUNNING past a small
`maxAttempts` shows a named "still building" reason; (d) control: QUEUED -> RUNNING -> READY shows the download link and NO
`export-refusal` element, and QUEUED -> FAILED shows the FAILED receipt as today. Print `VERDICT: RECEIPT-REFUSAL-NAMED-OK` only when
every arm holds.

<criterion id="IVE78-AC2" cell_refs="IV-e-78"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts 2>&1 | tail -8</invocation><expect>1 pass, 0 fail</expect></criterion>
`IVE78-AC2` -- the wire copy matches R11: the pinned regeneration test passes (byte-identical regeneration, data optional, content pin
17 of 17). It FAILS at the base (portal DEV) because `responses.ts` predates R11.

<expected_criteria>IVE78-AC1, IVE78-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `envelope.ts`, `src/lib/**` and every other
  page are read, never edited. In `investor-reporting.ts` read only.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on local DEV `8808eeb6`). Commit through `.tools/safe-commit.sh`. Never
  push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** synthetic ids only; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/export/ExportButton.tsx
portal/src/pages/InvestorReporting/export/submit.ts
portal/src/pages/InvestorReporting/export/ReceiptPanel.tsx
portal/src/pages/InvestorReporting/export/ExportModal.tsx
portal/src/pages/InvestorReporting/contracts/wire/responses.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-78.receipt-refusal-named.test.tsx
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v9 addendum 1, cell `IV-e-78`.
<owned_cells>IV-e-78</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE78-AC1, IVE78-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~41/DSGN_IRPTV1.TO-IV-e-78.receipt-refusal-named.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE78-AC1 IVE78-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W41-S<k>`). The `__tests__/` grant is for re-goldening a pinned test that asserted the silent-idle catch, each naming S27.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read at portal DEV 8808eeb6: ExportButton.tsx:214-249 queued branch, poll .catch returns flow to prev receipt with no refusal; refusal slot :212/:279-281; submit.ts pollExportReceipt :277-295; window-19 HAR (deliverables/2.0.0_SA_COO~D/w19-20260927.jsonl) GET export/exr_9f785460 23:20:58Z -> UNAVAILABLE NOT_READY, no later read (row S27; CTO 102222 ruled (b) plus the naming half).
lane: the <paths> block IS the grant; IV-e-75 (round 9, not yet seated) also writes ExportButton.tsx/submit.ts and is seated after this order drains.
</preflight>

Seating: slot ~41 re-provisioned by net-zero reuse of the first round-9 slot to free (MSTR 102173 disk budget);
`.tools/wk-provision.sh provision DSGN_IRPTV1 41 --path <abs> --portal-ref <DEV 8808eeb6>`.
