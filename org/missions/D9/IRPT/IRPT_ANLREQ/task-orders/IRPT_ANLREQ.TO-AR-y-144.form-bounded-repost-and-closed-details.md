# TO IRPT_ANLREQ.TO-AR-y-144 -- the form shows a first-answer finding at once, re-posts a RESOLVING answer a bounded number of times, and shows a raw code only inside a closed Details

<to_id>IRPT_ANLREQ.TO-AR-y-144</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal change on a candidate branch; nothing is pushed, deployed or called live)
**Decomp cell:** `AR-y-144` (`decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md`) | **outcome_ref:** FWD-1 (hop 2, the upload door); TCKT_VNEXT FWD-3 by CTO msgs 5737 and 5849 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W51-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you change passes `bash .tools/commit-gate.sh <file>` before its commit.
- **The background for every cell of this round** is one record, read it first:
  `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r13/ONE_ACCOUNT_CHECK_READ.json` (what the upload door does today, run in process on four synthetic sheets), and the CTO's rulings in
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_14_20261011.md` section 2. Any sheet you build is SYNTHETIC: made-up tickers (`AAA`, `BBB`), made-up numbers, nothing that looks
  like a real account number or a person. No real uploaded file is ever read.
- **Portal worktree:** `C:/dev/wk-irpt-anlreq-51/portal`, branch `wk-IRPT_ANLREQ-51-portal-r14`, cut from portal DEV `d3ef4a5d88`
  (confirm with `git rev-parse --abbrev-ref HEAD` before you edit). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~51 -c user.email=0.9.0_WK_IRPT_ANLREQ~51@opal.agent commit -F <msgfile> -- <files>`.
  Never push. Never run `bun install`.

### THE CELL (`AR-y-144`, inlined)

*The form shows a first-answer finding with no second press; re-posts a RESOLVING answer a bounded number of times; and shows a raw
code only inside a closed Details.*

The form's side is `src/pages/TicketCenter/analysisRequest.ts` (`fileAnalysisRequest`, `findingLines`, `FileOutcome`) and where
`TicketCenter.tsx` shows a `FileOutcome`. Today: a NEEDS_CORRECTION answer shows "Review required: ..." with one line per finding;
any other non-accepted answer says "The file is still being checked. Nothing was filed; submit again in a moment." and the person
must press again. The service is being changed (not released yet) so that findings it can decide at once arrive on the FIRST
answer; only pricing stays later. The form must work against BOTH the service of today and the changed one.

1. **First answer:** a NEEDS_CORRECTION on the first answer is shown at once, as today. No change needed there beyond item 3;
   a test proves it.
2. **Bounded re-post (CTO ruling 4):** when the answer is RESOLVING, the form does NOT ask the person to press again. It re-posts
   the SAME upload itself, a bounded number of times with a stated wait between tries (use at most 5 tries and a 3 second wait
   unless the code already defines such constants for this page -- read first; export the two numbers as named constants), and
   shows while it waits that the file is being checked. It stops at the first answer that is not RESOLVING and shows it (filed, or
   the findings). If every try answers RESOLVING it says plainly that the file is STILL being checked, that nothing was filed, and
   that the person can submit again later -- your wording, one sentence, no code. It never files a ticket on a RESOLVING answer.
   READ how the upload request is keyed (does a second POST of the same file create a second upload, or answer for the first?
   `src/api/endpoints/investor-reporting.ts` `uploadAnalysisInput` and the request's idempotency or token member): re-post in the
   way that answers for the SAME upload; if you cannot tell from the portal code, say so in your report and file a row -- do not guess.
   The wait must be injectable (a `wait` function in `deps`, defaulting to a real timer) so tests never sleep.
3. **A raw code only inside a closed Details (CTO item 3):** a finding with words shows its words. A finding with NO words shows a
   plain line ("One row could not be read; see details" in your wording) and its raw code and row ONLY inside a closed
   `<details>` element (or the page's existing disclosure component if the Ticket Center already uses one -- read first). No raw
   code is visible until a person opens it.
4. No restyle: reuse classes the form's result area already uses. No file outside `src/pages/TicketCenter/`.
5. **One new test file**, `src/pages/TicketCenter/__tests__/analysis-request-repost.test.tsx`, typed fakes, no `any`, no `// @ts-`
   comment, no real timer, with tests named exactly:
   - `a finding on the first answer is shown without a second press`
   - `a resolving answer is re-posted a bounded number of times`
   - `after the bound the form says it is still working and files nothing`
   - `a raw code is shown only inside closed details`
   Existing tests keep their names; change an expectation only where items 2 or 3 force it, and say which.
6. In your report: the two constants; how the re-post addresses the same upload; `bun run typecheck`; the eslint error-count line
   (`bun x eslint <changed files>`); `git diff --stat origin/DEV HEAD`.

### ACCEPTANCE

<criterion id="AR144-y-AC1" cell_refs="AR-y-144"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r14/ar14_checks.py y144-form --root C:/dev/wk-irpt-anlreq-51 --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y144-FORM-OK</expect></criterion>
`AR144-y-AC1`: the four named tests are in the new file, no test waits on a real timer, and the whole TicketCenter folder passes
(62 at the base, plus the four).

<criterion id="AR144-y-AC2J" cell_refs="AR-y-144" judgment="true"/>
`AR144-y-AC2J` (judgment, graded at L9, never by you): a person who attaches a bad sheet learns what to fix without pressing twice
and without reading a code; a person whose sheet is still being priced is told so plainly and nothing is filed.

<expected_criteria>AR144-y-AC1 AR144-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only). In the portal: `src/pages/TicketCenter/` only.
- READ only: everything else. No push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md</decomp_doc>
<owned_cells>AR-y-144</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR144-y-AC1 AR144-y-AC2J. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-144.form-bounded-repost-and-closed-details.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-144`. `AR144-y-AC2J` is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with `method`, `invocation`, `denominator` and a `status_reason`
naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR144-y-AC1,AR144-y-AC2J`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 45 lines of analysisRequest.ts at portal DEV d3ef4a5d88 (lines 72-116: findingLines, FileOutcome, fileAnalysisRequest); NOT seen: where TicketCenter.tsx renders a FileOutcome and how the upload request is keyed (the worker reads both before changing anything). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers of what this cell writes. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change
comp-adversary: RUN -- by reading 2 rulings (ruling 4; item 3) against the face; the lens: a re-post that creates a SECOND upload each try, an unbounded loop, or a ticket filed on a RESOLVING answer. The face orders the keying read first, a bound of 5, and forbids the third. NOT seen: the service's behaviour on a repeated POST of the same file (not run live).
lane: the Ticket Center form's result path, one test file, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-14 analysis @1edb90ada7, items 3 and 4 (form half). `AR144-y-AC1` base: FAIL as expected (no test file;
  the folder itself passes, 62).
- The candidate works against today's service and the changed one, so it does not wait on the service release; it goes to the
  CTO as a portal candidate after the drain.
- Seating: slot ~51 is reused; its earlier orders are terminal.
