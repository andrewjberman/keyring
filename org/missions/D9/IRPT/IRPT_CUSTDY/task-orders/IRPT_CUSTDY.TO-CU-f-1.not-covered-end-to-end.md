# TO IRPT_CUSTDY.TO-CU-f-1 -- round 6 CU-f-1 (E1): not-covered accounts end to end -- validated with their reason, rendered by the template, never under another household

<to_id>IRPT_CUSTDY.TO-CU-f-1</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~14</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~K2</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-f-1` (`decompositions/IRPT_CUSTDY_DECOMP.round6.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (your queue's next order is CU-f-3)

---

## WORKER FACE

### THE CELL

`CU-f-1`, item E1 of the CTO's round-5 analysis. A granted account that Schwab holds under no identifier (NOT_HELD) is written by
`data/assets/scripts/gold/irpt_custody/hop3_real_run.py` as its own household document carrying `"not_covered": {"reason": "<text>"}` and no
figures. On real data (advisor `matthew_gooch`, as-of 2026-09-30) that is 4 of 18 accounts. Three gaps remain, ruled by the CTO (W13-S2):
- `client_report_figures.validate_document` would REJECT such a document; it must ADMIT a not-covered account carrying its reason, without
  the per-household blocks (`household_returns`, `lineage`), and REFUSE one whose reason is missing or empty.
- The portal template `ClientReportDocument` renders nothing for that state; it must render `not covered: <reason>` for the account.
- The producer must NEVER fold a not-held account into another household (that would put a client's account under someone else's
  household): one not-covered account, its own household id, always.

**The template lives on a portal branch, not DEV:** your worktree's nested `portal/` is on branch `wk-IRPT_CUSTDY-14-portal`, cut from
`99addd80` (`wk-IRPT_CUSTDY-12-portal`, the template as reviewed). Read `portal/src/pages/InvestorReporting/render/clientreport/` and the
existing test `portal/src/pages/InvestorReporting/__tests__/clientreport/client-report-document.test.tsx` before you change anything.

**Build:**
1. `client_report_figures.py`: `validate_document` admits an account document `{account (last 4), not_covered: {reason}}` with a non-empty
   reason and no figure keys, inside a household document with no `household_returns`/`lineage` when every account in it is not-covered;
   it raises on a missing or empty reason. Nothing else in its rules changes.
2. `hop3_real_run.py`: assert in code that a not-covered account's household id is its own (never another household's); run its documents
   through `validate_document` now that it admits them.
3. Tests in a NEW file `data/assets/scripts/gold/irpt_custody/tests/test_not_covered_validation.py`: the admit case, the missing-reason and
   empty-reason refusals, and a producer-level test that two not-held accounts and one covered household never share a household id.
4. Portal: `ClientReportDocument.tsx` (+ `types.ts`) renders a not-covered account as a block reading `not covered: <reason>` with the
   masked account and no figure tables; add one not-covered account to `render/fixtures/clientreport.firm-a.json` (synthetic); a NEW test
   `portal/src/pages/InvestorReporting/__tests__/clientreport/not-covered.test.tsx` (`bun:test`) asserting the text renders, no `0`/blank
   figure appears for it, and the masked account prints. The existing test must still pass.

**THE BUN RULE -- verbatim (`1.0.0_SA_CTO~DELL2` msgs 500 and 563, `0.0.0_AB_MSTR~DELL2` msg 508):** "run bun ONLY from inside
C:\dev\ajb_workspace\portal (or a worktree with node_modules LINKED), always as `bun --no-install`; never run bun on a scratch file
elsewhere." "Never `bun install`. Provision a worktree only with `wk-provision.sh --node-modules link` (it links
C:\dev\ajb_workspace\portal\node_modules, the kit tree) or `none`. The rest of 106215 stands: bun only inside a portal tree holding
node_modules, always --no-install, no registry-reaching probe." Conditions of msg 508: (1) before any bun call prove the link
(`ls portal/node_modules/react/package.json` resolves into the shared portal); (2) every bun call is `bun --no-install` from inside the
worktree's `portal/`; (3) an import of a package NOT already in node_modules is STOP: no run, file a row, return.

### ACCEPTANCE

<criterion id="CU16-AC1" cell_refs="CU-f-1"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_not_covered_validation.py</invocation><expect>passed</expect></criterion>
`CU16-AC1` -- the CTO's criteria (1) and (3): validate admits with a reason and refuses without; no not-held account under another household.

<criterion id="CU16-AC2" cell_refs="CU-f-1"><invocation>cd portal && bun --no-install test ./src/pages/InvestorReporting/__tests__/clientreport/not-covered.test.tsx</invocation><expect>0 fail</expect></criterion>
`CU16-AC2` -- the CTO's criterion (2): the template renders `not covered: <reason>`.

<expected_criteria>CU16-AC1,CU16-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Portal commits** on your nested branch `wk-IRPT_CUSTDY-14-portal` with `git -C portal commit`; never push. Workspace commits via
  `.tools/safe-commit.sh`.
- **Never commit a real-run output file. Never print a full account number.** Never edit another project's file.
- **A surprise row is committed in the same turn you write it** (an uncommitted row in a shared tree blocks other seats' commits).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a row (id `IRPT_CUSTDY-W14-S<k>`;
  `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do not weaken a test.

<paths>
data/assets/scripts/gold/irpt_custody/client_report_figures.py
data/assets/scripts/gold/irpt_custody/hop3_real_run.py
data/assets/scripts/gold/irpt_custody/tests/test_not_covered_validation.py
portal/src/pages/InvestorReporting/render/clientreport/ClientReportDocument.tsx
portal/src/pages/InvestorReporting/render/clientreport/types.ts
portal/src/pages/InvestorReporting/render/fixtures/clientreport.firm-a.json
portal/src/pages/InvestorReporting/__tests__/clientreport/not-covered.test.tsx
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round6.md</decomp_doc> (round 6), cell `CU-f-1`.
<owned_cells>CU-f-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU16-AC1, CU16-AC2. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~14/IRPT_CUSTDY.TO-CU-f-1.not-covered-end-to-end.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU16-AC1,CU16-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the link proof, the pytest and bun summaries, the portal commit hash, rows, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a validator, producer guard and template change; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the cell's checks make no AWS call (fixtures and bun tests only).
comp-adversary: RUN -- the household-folding guard is a test; synthetic portal fixture; bun rules verbatim; BLIND: none beyond the template's mounting (IRPT_BCKEND's).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: round-5 analysis @f6160117ce section 2 (W13-S2) and section 4 E1; CTO review msg 581; decomposition round 6 constraints 1-2.
