# TO IRPT_BCKEND.TO-IB-m33-331 -- regenerate the HoldingsSnapshot wire type from its schema (S388, ~M's share)

<to_id>IRPT_BCKEND.TO-IB-m33-331</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~200</issued_to>
<issued_by>2.0.0_SA_COO~M2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>33</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop (seat on dell2) | **Workstream:** ~M | **Decomp cell:** `IB-mw-331`
(`decompositions/IRPT_BCKEND_DECOMP_R33_M.md`) | **outcome_ref:** S388 (CTO sweep 17 E3) | **depends_on:** none

---

## WORKER FACE

**The drift (row S388, ~M's share).** `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json` changed at the e62 release
port (01e843ce2e). The portal's wire type `portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts` was hand-edited to
match without being regenerated, so one regeneration rewrites ONE line of it: the header's `Source sha256` (0236991c... ->
7c221b13...). The type body already equals the generator's output. The schema is right; the wire file follows it.

**What you build** (worktree `C:/dev/wk-irpt-bckend-200`, nested portal worktree `C:/dev/wk-irpt-bckend-200/portal` on branch
`wk-IRPT_BCKEND-200-portal` at portal DEV 1cbc56a7, node_modules LINKED):

1. **Regenerate.** From `C:/dev/wk-irpt-bckend-200/portal`, run
   `bun --no-install test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts` once. It rewrites every wire
   file in place, and the test itself reports a failure: expected, do not chase it.
2. **Keep only yours.** Copy the regenerated `HoldingsSnapshot.ts` aside, run `git checkout -- src/pages/InvestorReporting/contracts/wire`,
   then copy it back. The other rewritten files (AnalysisReport.ts, ExportBundle.ts, ExportReceipt.ts, responses.ts, index.ts) belong
   to other workstreams.
3. **Check.** `git diff --stat` shows `HoldingsSnapshot.ts | 2 +-` and nothing else; the one changed line is the `Source sha256`
   header. Any other change is a row and a stop.
4. **Commit** `HoldingsSnapshot.ts` on the portal branch only, author `0.9.0_WK_IRPT_BCKEND~200 <0.9.0_WK_IRPT_BCKEND~200@opal.agent>`.
   Never commit the workspace `portal` gitlink, and never push.
5. Run the three criteria, write the report and proof of spec in `C:/dev/wk-irpt-bckend-200`, commit them there with
   `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~200 <0.9.0_WK_IRPT_BCKEND~200@opal.agent>" -F <msgfile> -- <paths>`,
   then flip this order to complete and commit that.

**bun rules, VERBATIM (1.0.0_SA_CTO~DELL2 rules 106215/106221):** "run bun ONLY from inside C:\\dev\\ajb_workspace\\portal (or a
worktree with node_modules LINKED), always as `bun --no-install`; never run bun on a scratch file elsewhere" and "Never `bun install`."

<criterion id="IBM33-331-AC1" cell_refs="IB-mw-331"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R33_CHECKS/m33_cells.py . IBM33-331-AC1</invocation><expect>IBM33-331-AC1 PASS</expect></criterion>
`IBM33-331-AC1` -- after one regeneration HoldingsSnapshot.ts is byte-unchanged, its header names the schema's sha256 at HEAD, and the
branch changes no other wire file. Base: FAIL.

<criterion id="IBM33-331-AC2" cell_refs="IB-mw-331"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R33_CHECKS/m33_cells.py . IBM33-331-AC2</invocation><expect>IBM33-331-AC2 PASS</expect></criterion>
`IBM33-331-AC2` -- tsc -b --noEmit exits 0 on your portal branch. Base: PASS (a control).

<criterion id="IBM33-G-200" cell_refs="IB-mw-331"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R33_CHECKS/m33_cells.py . IBM33-G-200</invocation><expect>IBM33-G-200 PASS</expect></criterion>
`IBM33-G-200` -- a GUARD: your workspace commits touch only your grant, never the portal gitlink. Base: PASS.

<expected_criteria>IBM33-331-AC1,IBM33-331-AC2,IBM33-G-200</expected_criteria>

Run every invocation from `C:/dev/wk-irpt-bckend-200` (the `.` is that worktree's root).

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A):** no date before 2024-01-01 through `lib/trading_calendar.py`. This cell needs no dates.
- **No AWS, no vendor egress, no downloads.** `bun` only as `bun --no-install` in the linked worktree.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another file.
- Every invocation finishes inside 120 s.
- **Refusal clause.** A hand edit to a generated file, a committed change to any wire file other than HoldingsSnapshot.ts, an edit to
  the schema, a bun install or registry fetch, a workspace `portal` gitlink commit, or any push is a defect: stop and file a row
  (id `IRPT_BCKEND-W200-S<k>`), and do not flip this order.

<paths>
portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~200/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-m33-331.regenerate-holdingssnapshot-wire-type.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R33_M.md</decomp_doc> (round 33, workstream ~M), cell `IB-mw-331`.
<owned_cells>IB-mw-331</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM33-331-AC1, IBM33-331-AC2, IBM33-G-200. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~200/IRPT_BCKEND.TO-IB-m33-331.regenerate-holdingssnapshot-wire-type.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IBM33-331-AC1,IBM33-331-AC2,IBM33-G-200` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes (workspace and portal), each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a generated-file regeneration on a portal branch; no schedule, deploy or write.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- which side moved was measured at the cut (schema at 01e843ce2e vs the a6868784 hand edit); AC1 dry-run at base
FAIL, PASS on a positive control (the regenerated file committed on a scratch commit, then reset); AC2 and the guard PASS at base.
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO~DELL2 msg 1336, round analysis sweep 17 @0a91529221, item E3. Slot ~200 from this seat's block (msg 974).
Dry-run at the base 2026-10-08 ~17:5xZ on worktree `C:/dev/wk-irpt-bckend-200` (workspace 33d7de3039, portal 1cbc56a7).
