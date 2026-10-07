# DSGN_AMGTV1 task order -- `AV-zz-1` -- THE RENDER CHECK'S PURPLE-FILL CLAUSE READS THE AMENDED FWD-18: ZERO IN A SECURITY VIEW, AT MOST ONE IN THE UNIVERSE VIEW

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zz-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~110</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; one portal script, read as text by the check and run offline by the instrument.
comp-adversary: RUN by the issuer at the cut on portal ec9f9a0e -- r47i.cjs 1 of 4 (arm 1 FAIL: a Security state with 0 purple fills does not pass; arm 2 FAIL: gradeFwd18 says "want 1 in a Security state"; arm 3 FAIL: both retired failure texts survive; PLANTED passes). 4 of 4 on a scratch reference edit of the one file (the tree restored after, 0 changes). The instrument on ec9f9a0e reads 10 FAIL cells, all this clause.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zz-1` (round 48, decomposition v48; one small edit to the render check)

The page's rule changed and the check that grades it did not. The PRD's FWD-18 now reads: "the rendered state reads purpleFills <= 1 in
every view and == 0 in Security mode". The re-run button, which was the one purple control on each Security view, was removed. The
render check `portal/scripts/ui-contract-check.mjs` still demands exactly one purple fill on each Security view and that it be the
Refresh action, so it fails on five views that are now correct.

**The file uses CRLF line endings. Keep them.**

**Three edits in `portal/scripts/ui-contract-check.mjs`:**

1. **The `purpleFills` predicate** (about line 514). Today:
   `const expected = stateName === 'list' ? 0 : 1` then `pass: v === expected`.
   Make it: the Universe state (`stateName === 'list'`) passes when `v <= 1`; every other state passes when `v === 0`. Keep
   `value: String(v)`.
2. **`gradeFwd18`, the Security branch** (about lines 814-818, `if (state.name !== 'list') { ... }`). Today it fails unless
   `m.purpleFills === 1` and then unless `m.purpleRefresh === 1`.
   Make it one test: fail when `m.purpleFills !== 0`, with the text `` `purpleFills ${m.purpleFills}, want 0 in a Security state` ``.
   Remove the Refresh test and its text. Keep the `return fwdCell(...)` line as it is.
3. **`gradeFwd18`, the Universe branch** (about line 849). Today: `if (m.purpleFills !== 0) fails.push(... want 0 in the Universe state)`.
   Make it: fail when `m.purpleFills > 1`, with the text `` `purpleFills ${m.purpleFills}, want at most 1 in the Universe state` ``.

If the file's header comment describes the purple-fill rule in words, bring those words in line with the three edits. Change nothing else.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the one file above changes (plus your deliverables and the surprise channel).
3. The portal file commits inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY; keep the file's CRLF line endings (count `\r` bytes before and after: the count may change only by the lines you removed or added).
5. Do not edit `portal/scripts/ui-measure.mjs`: its own self-test line that expects one purple fill reads a planted positive page, not the product.
6. AC2 takes about 14 minutes (it builds the portal twice). Run it ONCE, in the foreground with a long timeout, and do not start AC3 before it ends: AC3 reads the folder AC2 writes.

## 3. SURFACES

<paths>
portal/scripts/ui-contract-check.mjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~110/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zz-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round47/checks/r47i/r47i.cjs"; echo "exit=$?"</invocation><expect>THE RENDER CHECK READS ZERO PURPLE FILLS IN A SECURITY VIEW AND AT MOST ONE IN THE UNIVERSE VIEW: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zz-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round35/checks/instrument/instrument35.cjs" | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>THE INSTRUMENT GRADES THE REDESIGN AND CAN FAIL: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zz-1"><invocation>python -c "import glob,json,io;p=sorted(glob.glob('C:/tmp/r35-scratch-c/out-*/candidate/grades.json'))[-1];d=json.load(io.open(p,encoding='utf-8'));print(p);print('CANDIDATE FAIL CELLS:',sum(1 for s in d['states'].values() for c in s.values() if isinstance(c,dict) and c.get('grade')=='FAIL'))"</invocation><expect>CANDIDATE FAIL CELLS: 0 -- on the out- folder AC2 just wrote (its path is the first printed line)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~110/DSGN_AMGTV1.TO-AV-zz-1.render-check-purple-fill-clause.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W110-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** CTO countersign `ledger/CTO_COUNTERSIGN_COMPLETION_GRADES_ROUND46.md` ruling 3 and ROUND 47 item 3; the go to cut is CTO msg 30831
  ("cut AV-zz-1 now, PRD v0.17 @8730d6c042 is ADMITTED"). PRD FWD-18 DONE WHEN at `prd/DSGN_AMGTV1_PRD.md` lines 281-286.
- **Base:** the worker's portal is at the round-47 candidate ec9f9a0e, so the instrument's Model size cell already passes and AC3 can reach 0.
- **AC3 reads a device-local scratch folder** that `instrument35.cjs` itself writes (`C:/tmp/r35-scratch-c`); the path is the instrument's, not a new one.
- **Round 48, not round 47:** the cell was held out of round 47 for the PRD addendum and the CTO's word; `.tools/to-pipeline-gate.py` admits one issuance per round, so it is its own round. The check stays at `round47/checks/r47i/`.

<status>complete</status>
<round>48</round>
<slot>~110</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
