# TO IRPT_ANLREQ.TO-AR-y-112 -- the Ticket Center's report read makes ONE read with the ticket id; the transitional fallback is removed (candidate HELD, not landed)

<to_id>IRPT_ANLREQ.TO-AR-y-112</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal change on a candidate branch; nothing is pushed, landed, deployed or called live)
**Decomp cell:** `AR-y-112` (`decompositions/IRPT_ANLREQ_DECOMP_R11_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W51-S<k>`. The worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either.
- **Portal worktree:** `C:/dev/wk-irpt-anlreq-51/portal`, branch `wk-IRPT_ANLREQ-51-portal-r11`, cut from portal DEV `3ebc35ebf2`.
  Commit there with `git -c user.name=0.9.0_WK_IRPT_ANLREQ~51 -c user.email=0.9.0_WK_IRPT_ANLREQ~51@opal.agent commit -F <msgfile> -- <files>`.
  Never push. Never run `bun install`.

### THE CELL (`AR-y-112`, inlined)

*The Ticket Center's report read makes ONE read, with the ticket's id. The transitional fallback is removed.*

Why. On DEV, `readTicketReport` in `src/pages/TicketCenter/analysisRequest.ts` reads a ticket's report with the ticket's id and, when
the read is refused with the served reason `INVALID_INPUT`, reads ONCE more without the id. That exists only because the live
service does not yet know the `ticket_id` member. The release that teaches it is prepared; once it is live, that second read is a
way AROUND the binding: an id the service refuses as invalid would be read again with no binding at all. So the fallback is removed
in a candidate that lands only AFTER that release. **This candidate is HELD: it is built and committed on its branch and nothing
lands it.** Landing it before the release would break every ticket's Open report read.

1. In `analysisRequest.ts`: remove `readTicketReport` and `isInvalidInputRefusal`. Both call sites (`openReport` there;
   `openPackageFile` in `AnalysisRequestParts.tsx`) call the client's `getOwnedAnalysisReport(requestId, firm, ticket.ticket_id)`
   directly again, exactly as they did before the fallback (`git show d763d48c^:<file>` shows that form). Remove the now-unused import.
   Search `src` for any other caller of either name and report the count (expected: none outside these two files and the tests).
2. Every refusal is shown as the page shows it today: `REPORT_TICKET_MISMATCH` as the binding sentence (unchanged), and `INVALID_INPUT`
   like any other refused read, after ONE read.
3. Delete `src/pages/TicketCenter/__tests__/package-open-ticket-fallback.test.tsx` (`git rm` of that one file).
4. Add ONE test to `src/pages/TicketCenter/__tests__/package-open-ticket-binding.test.tsx`, named exactly
   `a read refused as invalid input is shown after one read`: the fake refuses with `publicReasonCode` `'INVALID_INPUT'`; assert the
   fake was called exactly once, with the ticket's id, and that no report is rendered. Typed fakes; no `any`, no `// @ts-` comment.
   Existing tests keep their names.
5. Do not touch `src/api/endpoints/investor-reporting.ts`. No restyle, no new wording.
6. In your report: `bun run typecheck` result, the eslint error-count line for the files you changed (`bun x eslint <files>`), and
   `git diff --stat origin/DEV HEAD`.

### ACCEPTANCE

<criterion id="AR112-y-AC1" cell_refs="AR-y-112"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r11/ar11_checks.py y112-remove --root C:/dev/wk-irpt-anlreq-51 --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y112-REMOVE-OK</expect></criterion>
`AR112-y-AC1`: the helper and its predicate are gone, the fallback test file is gone, the one-read test is named, and the whole
TicketCenter test folder passes.

<expected_criteria>AR112-y-AC1</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only). In the portal: `src/pages/TicketCenter/` only.
- READ only: everything else. No push, no deploy, no upload, no apply. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R11_Y.md</decomp_doc>
<owned_cells>AR-y-112</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR112-y-AC1. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-112.open-read-one-read-fallback-removed.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-112`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR112-y-AC1`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 diff of the helper and its 2 call sites (the issuer read d763d48c and 32b62981 whole at their drains); NOT seen: any caller of readTicketReport added on DEV since 3ebc35ebf2 (the worker searches src at its branch head and reports the count). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change
comp-adversary: RUN -- by reading 1 ruling (CTO msg 5487) against 2 call sites; the lens: the candidate landing BEFORE the service release, which refuses every ticket's Open read. The face says HELD and why; the pair names the landing as a step after the after-reads. NOT seen: a mechanical stop on the landing (there is none; the hold is this text and the pair).
lane: the Ticket Center open path, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-11 analysis @6385a12ed2, item 2, and CTO msg 5487. `AR112-y-AC1` base: FAIL as expected (helper, predicate
  and fallback test present; the one-read test absent); the folder itself passes at the base (53).
- HELD: lands on DEV, then PROD, only after release 5's return passes its after-reads (the pair, section 6). The issuer does not
  send this candidate for landing before then.
- Seating: slot ~51 is reused; its earlier orders are terminal.
