# TO IRPT_CUSTDY.TO-CU-c-3 -- round 3 CU-c-3 (E3): the 49 Financial ClientReportDocument -- the client-report template as a portal print document

<to_id>IRPT_CUSTDY.TO-CU-c-3</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~12</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~K2-E3</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-c-3` (`decompositions/IRPT_CUSTDY_DECOMP.round3.md`, E3 section) |
**outcome_ref:** FWD-1, FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CU-c-3`, item E3: "the 49 Financial template". FWD-1: one advisor's quarter-end client reports, built by Opal from Schwab's records, that the
advisor would send as they are. FWD-3: each firm's reports are in its own template; changing one firm's changes nothing in another's.
Contracts: the template is built from the CUSTODIAN-SHAPED model, never from a Black Diamond report's layout or field names (C-SHAPE,
C-TEMPLATE); nothing reaches a client.

**How the portal renders (READ, never edit):** `portal/src/pages/InvestorReporting/render/` -- a template is a React print document chosen by
`reportKind` (`manifest.ts` `templateFor`, `PrintEntry.tsx`); `render/performance/PerformanceDocument.tsx` is the pattern to follow (pages,
`Page.tsx`, `values.tsx` formatting, `brand.ts` tokens, `print.css`). Adding the client-report KIND to `manifest.ts`, the print route and the
render host is ANOTHER project's work (IRPT_BCKEND a1-a4): **you do not edit `manifest.ts`, `PrintEntry.tsx` or any existing file.** You build
the template and export it.

**The input shape (this project's client-report contract, one document per household):** `{firm, advisor, as_of, household: {id, name},
periods: [..], accounts: [{account (last 4 only), registration, name_source, returns: {<period>: {value, window: [start, end], status,
source: {table, partition, rows}}}, si_anchor: {date, rule, label, status}, market_value: {start, end}, holdings: [{symbol, cusip, quantity,
market_value, weight, class, sector, described, description_source}], activity: [{date, type, symbol, amount}], fees: {amount, source:
{label, table, partition, rows}, is_billed_fee}}], household_returns: {<period>: {...}}, lineage: {...}}`. Statuses: `OK | NO_DATA |
WINDOW_NOT_RULED | NOT_AVAILABLE`. The SI row prints the anchor's `label` verbatim (e.g. `since inception (first funded 2025-03-14)` or
`since 2024-07-08, the first date Opal holds`).

**Build (all NEW files):**
1. `portal/src/pages/InvestorReporting/render/clientreport/types.ts` -- the TypeScript type of that shape (field names exactly as above).
2. `portal/src/pages/InvestorReporting/render/fixtures/clientreport.firm-a.json` -- ONE document of that exact shape with SYNTHETIC values
   (invented numbers, accounts masked `****1234`): two accounts, one with a `NO_DATA` figure and one holding `described: false`, one SI under
   each label kind. Never a real client's figures.
3. `portal/src/pages/InvestorReporting/render/clientreport/ClientReportDocument.tsx` -- the print document, following
   `PerformanceDocument.tsx`'s page structure: cover (firm display name and logo as SLOTS, never invented text; household; advisor; as-of);
   household summary over the document's own `periods` in order; per account: returns table with the SI anchor label, market value start /
   end, holdings with class and sector or "not described", activity, fees with their source label; a data-status note listing every non-OK
   figure; a disclosure SLOT. Every printed value is a field of the document: it computes no financial quantity, reads no clock, touches no
   network. A non-OK figure prints its status in place, never 0 or blank.
4. `portal/src/pages/InvestorReporting/__tests__/clientreport/client-report-document.test.tsx` (`bun:test`, the pattern of
   `__tests__/dsgn-irptv1/*.test.tsx`): renders the fixture; asserts the periods' order, the two SI labels verbatim, `NO_DATA` printed in place,
   "not described" printed, the fee source label printed, no full account number, and that no prop or rendered label uses a Black Diamond
   field name (assert against the contract's key list above).

**THE BUN RULE -- verbatim, binding (`1.0.0_SA_CTO~DELL2` msg 500, `0.0.0_AB_MSTR~DELL2` msg 508):** "run bun ONLY from inside
C:\dev\ajb_workspace\portal (or a worktree with node_modules LINKED), always as `bun --no-install`; never run bun on a scratch file elsewhere."
And the three conditions of msg 508: (1) before any bun call, prove the link: `ls portal/node_modules/react/package.json` exists in your
worktree and resolves into the shared portal; (2) every bun call is `bun --no-install`, run from inside the worktree's `portal/` root, never on a
scratch file outside it; (3) an import of a package NOT already in node_modules is STOP: no run, file a row, return -- a new dependency comes
by the kit, never by bun. Never `npm install` or `bun install`.

### ACCEPTANCE

<criterion id="CU13-AC1" cell_refs="CU-c-3"><invocation>cd portal && bun --no-install test ./src/pages/InvestorReporting/__tests__/clientreport/client-report-document.test.tsx</invocation><expect>0 fail</expect></criterion>
`CU13-AC1` -- the template on the synthetic fixture: periods, SI labels, statuses in place, not-described, fee source, masking, no BD field names.

<criterion id="CU13-AC2" cell_refs="CU-c-3"><invocation>cd portal && bun --no-install run typecheck && echo TYPECHECK-OK</invocation><expect>TYPECHECK-OK</expect></criterion>
`CU13-AC2` -- the page lane's typecheck over the whole portal with your files in it (a control that passes at the base; it must still pass).

<criterion id="CU13-AC3" cell_refs="CU-c-3" judgment="true"/>
`CU13-AC3` (JUDGMENT, graded by `3.0.0_SA_CVO` at L9, never self-graded) -- C-SHAPE: the document is built from the custodian-shaped model
and names no field after a Black Diamond field; record it in your instance as UNVERIFIABLE-BY-INSTRUMENT with that status_reason.

<expected_criteria>CU13-AC1,CU13-AC2,CU13-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Portal commits** go on your worktree's nested portal branch (`wk-IRPT_CUSTDY-12-portal`) with `git -C portal commit` -- the issuer lands
  them on DEV after review; never push. Your workspace-side commits (proof, order flip, any row) go through `.tools/safe-commit.sh`.
- **No AWS call. No egress: the bun rule above.** Never edit an existing portal file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `IRPT_CUSTDY-W12-S<k>`; `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do
  not weaken a test.

<paths>
portal/src/pages/InvestorReporting/render/clientreport/ClientReportDocument.tsx
portal/src/pages/InvestorReporting/render/clientreport/types.ts
portal/src/pages/InvestorReporting/render/fixtures/clientreport.firm-a.json
portal/src/pages/InvestorReporting/__tests__/clientreport/client-report-document.test.tsx
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round3.md</decomp_doc> (round 3, E3 section), cell `CU-c-3`.
<owned_cells>CU-c-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU13-AC1, CU13-AC2, CU13-AC3. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~12/IRPT_CUSTDY.TO-CU-c-3.client-report-template.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU13-AC1,CU13-AC2,CU13-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the link proof, the bun test summary, the typecheck line, the portal commit hash on your nested branch, rows, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a portal template; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the cell makes no AWS call at all (portal source, a synthetic fixture and bun tests only).
comp-adversary: RUN -- synthetic fixture only (no client data in the portal repo); bun egress rule verbatim with msg 508's three conditions; BLIND: how IRPT_BCKEND's a4 print kind will mount the document (another project's cell).
lane: the <paths> block IS the grant (worker RULING 1); the portal landing is CTO-reviewed (product file).
</preflight>

Source: round-2 analysis @10e64fe9df gate 3 -> E3 (round 1 E3's criteria); CTO ruling (a) @822468e309 (a5 is this project's); msgs 467, 471, 492, 500, 508.
