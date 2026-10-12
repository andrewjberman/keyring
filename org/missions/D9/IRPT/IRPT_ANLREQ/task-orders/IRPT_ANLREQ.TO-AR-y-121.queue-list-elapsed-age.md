# TO IRPT_ANLREQ.TO-AR-y-121 -- the Ticket Center queue list shows each open ticket's elapsed age

<to_id>IRPT_ANLREQ.TO-AR-y-121</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal change on a candidate branch; nothing is pushed, deployed or called live)
**Decomp cell:** `AR-y-121` (`decompositions/IRPT_ANLREQ_DECOMP_R12_Y.md`) | **outcome_ref:** FWD-1 (the page); TCKT_VNEXT FWD-5 by CTO msg 5682 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Workspace worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- **Portal worktree:** `C:/dev/wk-irpt-anlreq-51/portal`, branch `wk-IRPT_ANLREQ-51-portal-r12`, cut from portal DEV `a124694caf`
  (confirm with `git rev-parse --abbrev-ref HEAD` before you edit). Commit there with
  `git -c user.name=0.9.0_WK_IRPT_ANLREQ~51 -c user.email=0.9.0_WK_IRPT_ANLREQ~51@opal.agent commit -F <msgfile> -- <files>`. Never push.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W51-S<k>`. The workspace worktree shows ` M portal`: never commit it. Never run `bun install`.

### THE CELL (`AR-y-121`, inlined)

*In the Ticket Center queue list, each OPEN ticket shows how long it has waited.*

Why. The queue list (`src/pages/TicketCenter/TicketCenter.tsx`, the row at about line 579: `{fmtWhen(t.created_at)}`; `fmtWhen` at
about line 124) shows when a ticket was created. A person working the queue has to subtract to learn how long it has waited. The
ruling: "An elapsed age is owed, computed on the page from the created time already served; no service change."

1. **One pure helper in a NEW file** `src/pages/TicketCenter/elapsedAge.ts`, exported, taking the created time as the served ISO string
   (or null or undefined) and `now` as a number of milliseconds, returning a string:
   - the age says its UNIT IN WORDS, whole numbers, the largest unit that is at least one: for example `3 minutes`, `5 hours`,
     `2 days`; singular for one (`1 hour`); under one minute, the words `under a minute`. Your exact wording within that rule; no
     abbreviation such as `3m` or `5h`, no bare number.
   - **no created time** (null, undefined, empty, or a string that does not parse as a date) returns the EMPTY string. Never `0`,
     never `0 minutes`, never `NaN`, never `Invalid Date`.
   - **a created time AFTER now** (a clock that is behind) returns the EMPTY string. Never a negative age.
   - the helper never reads the clock itself: `now` is always passed in.
2. **The row.** In the queue list's created cell, an OPEN ticket shows the created time as today AND the age beside it (for example
   in the page's existing muted text style for secondary text in that table; read the row's neighbours and reuse a class already
   used there -- do not add a colour, a size or a new style). The page passes the viewer's clock (`Date.now()`) at render. When the
   helper returns the empty string the cell shows the created time alone, with no separator left dangling. A ticket whose status is
   the completed one shows the created time alone (it is no longer waiting): read the status values the page already uses
   (`STATUS_COLORS`, the tabs) and say in your report which statuses show an age.
3. No other change: no column added or removed (the table has 8 columns), no change to `fmtWhen`, to sorting, to the fetch, or to any
   file outside `src/pages/TicketCenter/`. No service change.
4. **One new test file**, `src/pages/TicketCenter/__tests__/queue-elapsed-age.test.tsx`, in the style of the folder's existing tests
   (typed; no `any`, no `// @ts-` comment), with tests named exactly:
   - `an age states its unit in words`
   - `a ticket with no created time prints nothing`
   - `a created time after now prints nothing`
   - `the age is computed against the given now and not the clock`
   - `the queue row shows the age beside the created time for an open ticket`
   **Every test fixes `now` as a literal number** (for example a constant built from a fixed ISO string): the file must not contain
   `Date.now()` or `new Date()` with no argument, so it cannot pass or fail by the hour it runs (the check refuses both strings).
   The fourth test calls the helper twice with the same created time and two different `now` values and asserts two different ages.
   The fifth renders the row (or the smallest component you can export for it WITHOUT restyling; if the row cannot be rendered in a
   test without a fetch, export a small pure function that returns the cell's text for a ticket and a `now`, use it in the row, and
   test that) and asserts the created time and the age are both present for an open ticket and that a completed ticket has no age.
5. In your report: `bun run typecheck` result; the eslint error-count line for the files you changed (`bun x eslint <files>`);
   `git diff --stat origin/DEV HEAD`; the exact words the helper prints for 30 seconds, 1 minute, 59 minutes, 1 hour, 23 hours,
   1 day and 40 days.

### ACCEPTANCE

<criterion id="AR121-y-AC1" cell_refs="AR-y-121"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r12/ar12_checks.py y121-age --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y121-AGE-OK</expect></criterion>
`AR121-y-AC1`: the new test file holds the five named tests, never reads the real clock, and passes.

<criterion id="AR121-y-AC2" cell_refs="AR-y-121"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r12/ar12_checks.py y121-keep --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y121-KEEP-OK</expect></criterion>
`AR121-y-AC2`: the difference control -- the whole TicketCenter test folder passes (53 at the base, plus yours).

<criterion id="AR121-y-AC3" cell_refs="AR-y-121" judgment="true"/>
`AR121-y-AC3` (judgment, graded at L9, never by you): a person reading the queue list learns how long each open ticket has waited
without subtracting, and nothing else about the list reads differently.

<expected_criteria>AR121-y-AC1 AR121-y-AC2 AR121-y-AC3</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only). In the portal: `src/pages/TicketCenter/` only.
- READ only: everything else. No live call, no push, no deploy. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R12_Y.md</decomp_doc>
<owned_cells>AR-y-121</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR121-y-AC1 AR121-y-AC2 AR121-y-AC3. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-121.queue-list-elapsed-age.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-121`. `AR121-y-AC3` is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason`
naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR121-y-AC1,AR121-y-AC2,AR121-y-AC3`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 25 lines of the list row at portal DEV a124694caf (lines 560-584) and 1 search for fmtWhen in the folder (2 hits: its definition at :124 and the row at :579); NOT seen: other pages that render a ticket's created time (none is in this cell's grant; the worker changes only this list). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called; created_at is already served on every list item (2.0.0_SA_COO~V2's read, msg 5683). comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change
comp-adversary: RUN -- by reading 1 ruling of 3 conditions (CTO msg 5690) against the face; the lens: an age of zero for a ticket with no created time, a negative age, or a test that passes by the hour it runs. The face forbids each and the check refuses a test file that reads the real clock. NOT seen: how the page behaves when the viewer's clock is far wrong (the age is against the viewer's clock by the ruling).
lane: the Ticket Center list row, one helper file, one test file, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on CTO msg 5690 as round 12's single cell. `AR121-y-AC1` base: FAIL as expected (no test file). `AR121-y-AC2` base: PASS as
  expected (53 pass at DEV a124694caf).
- After the drain: the issuer files eslint, typecheck and the suite on the candidate's head; the CTO reads the product-file change
  and confirms the page's class on PROD itself. `2.0.0_SA_COO~V2` is sent this order's id for its record of TCKT_VNEXT FWD-5.
- Seating: slot ~51 is reused; its earlier orders are terminal.
