# DSGN_AMGTV1 task order -- `AV-zzg-1` -- DIRECT ACT: THE FRESHNESS PAGE'S THREE REPAIRS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzg-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~119</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; two page files and their test, rendered offline by the check against a body the issuer captured.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) at the cut on DELL1, on the round-53 candidate portal 84e13d0f in a worker-shaped nested worktree -- r54.cjs 1 of 4 (arm 1 FAIL: 94 fault(s), Seeking Alpha cells carry data-state "collected"; arm 2 FAIL: the head reads "Research pack"; arm 3 FAIL: 285 of 285 day cells without nowrap; arm 4 PLANTED passes); r53a.cjs 3 of 3; battery29 ALL PASS (0 skipped). Site Z measured the same 1 of 4 and the reference edit 4 of 4 (issuance @a07147a87c).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzg-1` (round 55, decomposition v55; three repairs on one page, batched)

Paths are under `portal/src/pages/Freshness/`. The Seeking Alpha cell already prints the served sentence and carries `data-sa-state`
(round 53). Make three repairs. Change nothing else.

1. **The cell carries the served state** (the CTO's round-53 finding). In `Freshness.tsx`, the input cell's `data-state` is today
   `input?.collected ? (input.stale ? 'stale' : 'collected') : 'not_collected'`. A Seeking Alpha cell whose served state is `no_record`
   therefore reads `collected`. Make it: when the input carries `saState`, `data-state` is `'stale'` if `input.stale`, otherwise the
   served `saState` (`read`, `checked` or `no_record`). Every other cell keeps today's rule.
2. **A day reads on one line** (row DSGN_AMGTV1-Z-S25). Add `whitespace-nowrap` to the class of the "Oldest input" cell
   (`data-slot="keyed-date"`). Add it also to every input cell that prints a day, which is every input cell that does NOT carry
   served `words`. The Seeking Alpha sentence cell keeps wrapping.
3. **The built analysis is named "Built analysis"** (row DSGN_AMGTV1-Z-S26; the issuer's ruling). In `freshnessRows.ts`, the `pack`
   input's `label` reads `'Built analysis'`, not `'Research pack'`. The column head and the stale words then read "Built analysis" and
   "Built analysis last read <day>". Update any comment in the two files that calls this input "the research pack" or "Research pack".
4. `Freshness.test.tsx`: update only the assertions this changes and name each in your report:
   - the assertion that reads `Research pack last read 2026-08-01` becomes `Built analysis last read 2026-08-01`;
   - any assertion whose expected markup changes with the new class or `data-state`.
   Add one test: a `no_record` row's Seeking Alpha cell carries `data-state="no_record"`.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the three files in section 3 change (plus your deliverables and the surprise channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY. Keep each file's line endings exactly as you find them; read them first, for example with
   `python -c "print(open(p,'rb').read().count(b'\r\n'))"`.
5. You may run `bun test src/pages/Freshness/Freshness.test.tsx` from `portal/`. It is not a criterion.

## 3. SURFACES

<paths>
portal/src/pages/Freshness/Freshness.tsx
portal/src/pages/Freshness/freshnessRows.ts
portal/src/pages/Freshness/Freshness.test.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~119/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzg-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round54/checks/r54.cjs"; echo "exit=$?"</invocation><expect>THE FRESHNESS PAGE: SERVED STATE ON THE CELL, THE BUILT ANALYSIS NAMED, DAYS ON ONE LINE: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzg-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round53/checks/r53a.cjs"; echo "exit=$?"</invocation><expect>THE SEEKING ALPHA COLUMN DRAWS THE THREE SERVED STATES APART: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzg-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~119/DSGN_AMGTV1.TO-AV-zzg-1.freshness-three-repairs.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY), and only
when every criterion passes.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W119-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** round 54's list, carried to DELL1. Site Z issued it as `AV-zzf-1` @a07147a87c and cancelled it before any spawn
  (@e4852820af) on Andrew-direct ~22:5xZ 2026-10-08 (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_225xZ_AMGT_DSGN_RIVALS_TO_DELL1_AFTER_ROUND_CLOSE_AND_BBG_CENSUS.md`
  @b7361ceb2a). The hand-over (`deliverables/1.0.0_SA_CTO~Z/HANDOVER_TO_DELL1_20261009.md`, box/sitez @70c5bd38d1) names it this round's input.
  The list: the CTO's round-53 verdict (msg 32088) finding, plus rows DSGN_AMGTV1-Z-S25 and Z-S26.
- **The face is AV-zzf-1's, unchanged except identity:** cell id, slot ~119, issuer, round 55, the dell1 row infix and the preflight
  re-run on DELL1. The S26 ruling ("Built analysis") is site Z's issuer ruling, kept.
- **Base:** portal 84e13d0f, which is origin DEV HEAD at the cut (round 53, CTO-approved and on DEV).
- **Producer rule (1.0.0_SA_CTO~DELL1 msg 1267):** the three files are portal presentation. They are not a site-Z producer path.

<status>pending</status>
<round>55</round>
<to_id>DSGN_AMGTV1.TO-AV-zzg-1</to_id>
<slot>~119</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
