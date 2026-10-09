# TO TCKT_VNEXT.TO-F10-p2 -- the Ticket Center page shows an Analysis Request's draft commentary and its package

<to_id>TCKT_VNEXT.TO-F10-p2</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~4</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>F10</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL (DEV portal; a product file, landed by the portal review route) | **Decomp cell:**
`F10-p-2` (`decompositions/TCKT_VNEXT_DECOMP_F10.md`) | **outcome_ref:** FWD-6, FWD-9 | **depends_on:** none (builds against the
served shape below)

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~4`. Your PORTAL worktree is `C:/tmp/tckt-f10-p2` (a worktree of the `portal` repository, branch
`wk-tckt_vnext-f10-p2`, cut from portal `origin/DEV`). Your WORKSPACE worktree, which holds this order and the checks, is
`C:/tmp/tckt-f10-r4`. Commit portal code in the portal worktree with plain `git -C C:/tmp/tckt-f10-p2 commit -F <msgfile>` (author
`0.9.0_WK_TCKT_VNEXT~4 <0.9.0_WK_TCKT_VNEXT~4@opal.agent>`; message file written with the Write tool). Commit this order's status flip
and your proof in the workspace worktree with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~4 <0.9.0_WK_TCKT_VNEXT~4@opal.agent>" -F <msgfile> -- <paths>`.

### THE CELL

`F10-p-2`. The ticket service now serves two more fields on an `analysis_request` ticket (deployed 2026-10-09 01:01Z, source
`infra/aws/lambda/ticket_center/lambda_function.py` at box/dell2 `3b04c040fc`). The Ticket Center page shows neither today. Make an Opal
person see both on the ticket.

**The served shape (READ it from the handler source to confirm; do not invent fields):**
- `draft_commentary`: `{text, model, generated_at, status}` with `status` always `"DRAFT"`. It is written once, at create, by the
  commentary drafter.
- `package`: `{report_ref, pdf_ref, original_ref, commentary_ref, attached_at, attached_by}`. It is written by the package route.

**Build:**
1. `src/api/endpoints/tickets.ts`: add both optional fields to `Ticket`, typed exactly as above.
2. `src/pages/TicketCenter/AnalysisRequestParts.tsx`, plus the ticket row/detail in `TicketCenter.tsx` that already renders the
   analysis parts:
   - an `analysis_request` ticket with `draft_commentary` shows a block labelled **Draft commentary (DRAFT)**, containing the text
     (preserved line breaks), the model and the generated time;
   - a ticket with `package` shows a block **Report package** listing the four refs by name (Report, Branded PDF, Commentary,
     Original file) with `attached_at` and `attached_by`.
   - Each ref is displayed as its handle text. Opening the files is NOT this cell: IRPT's signed-link reader is bound by IRPT_ANLREQ's
     L5. Add no link and no new API call.
3. A ticket with neither field renders exactly as today.
4. Follow the page's existing panel classes, which are already used in `AnalysisRequestParts.tsx` (the portal colour law: light
   canvas, white hairline panels, navy ink). Add no new colours.

**Tests** in the new file `src/pages/TicketCenter/__tests__/commentary-package.test.tsx`, named EXACTLY:
- `shows the draft commentary labelled DRAFT on an analysis ticket`
- `lists the four package refs with attached time and attacher`
- `shows nothing for a ticket without draft or package`

Before you report, also run `bunx tsc -b` and the existing `src/pages/TicketCenter/__tests__/analysis-request.test.tsx`.

### ACCEPTANCE

<criterion id="F10-p2-AC1" cell_refs="F10-p-2"><invocation>python C:/tmp/tckt-f10-r4/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-p2 --portal C:/tmp/tckt-f10-p2</invocation><expect>F10-P2-OK</expect></criterion>
`F10-p2-AC1`: the three named tests exist and pass under bun.

<expected_criteria>F10-p2-AC1</expected_criteria>

## BOUNDS

- **Grant.** In the portal worktree: `src/pages/TicketCenter/` (all files) and `src/api/endpoints/tickets.ts`. In the workspace worktree:
  your deliverables folder `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~4/` and this order's file (status flip
  only).
- LOCAL: never push, never run a dev server on any port but 5174, and never call AWS or the live API.
- No non-ASCII. If you need a surprise row, append it in BINARY mode to the channel as `TCKT_VNEXT-D2-W4-S<k>`, keeping its line endings.

<paths>
portal/src/pages/TicketCenter/AnalysisRequestParts.tsx
portal/src/pages/TicketCenter/TicketCenter.tsx
portal/src/pages/TicketCenter/__tests__/commentary-package.test.tsx
portal/src/api/endpoints/tickets.ts
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_F10.md</decomp_doc> (workstream F10, round 4), cell `F10-p-2`.
<owned_cells>F10-p-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: F10-p2-AC1. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~4/TCKT_VNEXT.TO-F10-p2.ticket-page-draft-and-package.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> F10-p2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** the check line verbatim, the portal commit(s), the tsc result, the workspace commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE -- portal display only; no new API call.
comp-adversary: DECLARED-NOT-APPLICABLE -- display of already-served fields.
lane: product file; lands on portal DEV by the CTO review route (CLAUDE.md Portal), never by the worker.
</preflight>

Sources: FWD-6 and FWD-9 ACCEPT ("an Opal person ... finds ... there"); the F10 deploy of 01:01Z; the /next-calls --drive assessment
of ~02:0xZ (OPTION 1).

# pipeline-override: the portal landing on DEV is the issuer's route (CTO review), not a worker cell; this issuance covers round 4's two worker cells (F10-p-2, F10-l-4).
