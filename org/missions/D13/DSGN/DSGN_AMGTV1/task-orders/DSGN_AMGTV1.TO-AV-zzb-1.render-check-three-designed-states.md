# DSGN_AMGTV1 task order -- `AV-zzb-1` -- THE RENDER CHECK REQUIRES THE THREE DESIGNED STATES, NOT FOUR

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~112</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; one portal script, read as text by the check and run offline by the instrument.
comp-adversary: RUN by the issuer at the cut on portal b3440392 -- r50.cjs 2 of 4 (arm 1 FAIL: gradeFwd19 reads FAIL "no-permission (the standalone capture was not taken ...)" with three kinds on 6 of 6 panels; arm 2 FAIL: the run cell reads FAIL missing ["no-permission"]; KEEP and PLANTED pass). 4 of 4 on a scratch reference edit of the one file, with r47i.cjs still 4 of 4 and `node --check` clean (the tree restored after, 0 changes).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzb-1` (round 50, decomposition v50; one small edit to the render check)

The page's contract now names THREE designed panel states: empty, loading and error. The fourth, a "no permission" panel, was removed
from the product on the owner's word. The render check `portal/scripts/ui-contract-check.mjs` still REQUIRES the fourth in two places,
so it would fail a correct page the day the old capture stops being taken.

**The file uses CRLF line endings. Keep them.**

**Three edits in `portal/scripts/ui-contract-check.mjs`:**

1. **Declare the required kinds.** Directly under the line `const PANEL_KINDS = ['loading', 'error', 'empty', 'no-permission']` (about
   line 913), add: `const REQUIRED_PANEL_KINDS = ['loading', 'error', 'empty']`. Use exactly that name. Leave `PANEL_KINDS` as it is:
   the fourth kind is still COUNTED and reported, only no longer required.
2. **The run cell** (about line 959). Today: `const missingKinds = PANEL_KINDS.filter(k => combined[k] === 0)`. Make it filter
   `REQUIRED_PANEL_KINDS`. Change nothing else in that block. The cell keeps its name `fourStates` in `grades.json`, because other
   files read that key.
3. **`gradeFwd19`** (about line 991). Remove the line that pushes `'no-permission (the standalone capture was not taken inside the
   running application)'` into `missing`. Keep the `noPermission` object in the returned `value`, so the capture is still reported.

Then bring the comments that describe these two cells in line with the code: where a comment says PASS needs each of the FOUR kinds, or
that PanelNoPermission MUST be captured, say three kinds are required and the no-permission capture is reported and not required.
Do not remove the standalone capture itself, and do not rename `fourStates`, `PANEL_KINDS` or `gradeFwd19`.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the one file above changes (plus your deliverables and the surprise channel).
3. The portal file commits inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; keep the file's CRLF line endings (count carriage-return bytes before and after; the change must equal lines added
   minus lines removed).
5. Never run `bun install` or any command that reaches a package registry. The criteria use node and python only.
6. AC3 takes about 19 minutes (two full sweeps of the built page). Run it ONCE in the foreground with a long timeout; if the harness
   moves it to the background, wait for its last line before you report.

## 3. SURFACES

<paths>
portal/scripts/ui-contract-check.mjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~112/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzb-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round50/checks/r50/r50.cjs"; echo "exit=$?"</invocation><expect>THE RENDER CHECK REQUIRES THREE DESIGNED STATES, NOT FOUR: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzb-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round47/checks/r47i/r47i.cjs"; echo "exit=$?"</invocation><expect>THE RENDER CHECK READS ZERO PURPLE FILLS IN A SECURITY VIEW AND AT MOST ONE IN THE UNIVERSE VIEW: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzb-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PLANTS49_ONLY=designedStates node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round49/checks/plants49/plants49.cjs" | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>EVERY CLAUSE FAILS ITS PLANTED PAGE BESIDE A CLEAN CONTROL: 1 of 1 clauses (FILTERED run: designedStates; the full set is 9) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~112/DSGN_AMGTV1.TO-AV-zzb-1.render-check-three-designed-states.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W112-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** CTO msg 30918 ("the four-against-three count in the instrument is one script-only cell for the next issuance, whatever the
  grade"), on the finding in `round49/ROUND49_CLOSE.md` @5e36b6ca82. PRD v0.17 FWD-19 and FWD-20 DONE WHEN.
- **AC3 is the real run:** the designed-states pair of `plants49.cjs` on the edited instrument -- an untouched full sweep must still read
  PASS and the stripped-error page must still FAIL. It builds the product bytes of the worker's portal (b3440392 + its commit; the dist
  key is the HEAD sha) with vite from the linked node_modules; no registry is reached.
- **Base:** the worker's portal is at b3440392, so the candidate becomes b3440392 + 1 commit touching no product file.

<status>pending</status>
<round>50</round>
<slot>~112</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
