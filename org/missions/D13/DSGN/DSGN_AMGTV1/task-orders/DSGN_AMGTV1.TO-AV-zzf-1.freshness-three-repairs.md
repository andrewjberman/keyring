# DSGN_AMGTV1 task order -- `AV-zzf-1` -- DIRECT ACT: THE FRESHNESS PAGE'S THREE REPAIRS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~118</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; two page files and their test, rendered offline by the check against a body the issuer captured.
comp-adversary: RUN by the issuer at the cut on the round-53 candidate portal 84e13d0f -- r54.cjs 1 of 4 (arm 1 FAIL: 94 of 95 Seeking Alpha cells carry data-state "collected"; arm 2 FAIL: the head reads "Research pack"; arm 3 FAIL: 285 of 285 day cells without nowrap; arm 4 PLANTED passes). On a scratch reference edit loaded through CHECK_SRC_OVERRIDE, 4 of 4, and r53a.cjs still 3 of 3. The tree was not edited.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzf-1` (round 54, decomposition v54; three repairs on one page, batched)

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
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~118/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzf-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round54/checks/r54.cjs"; echo "exit=$?"</invocation><expect>THE FRESHNESS PAGE: SERVED STATE ON THE CELL, THE BUILT ANALYSIS NAMED, DAYS ON ONE LINE: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzf-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round53/checks/r53a.cjs"; echo "exit=$?"</invocation><expect>THE SEEKING ALPHA COLUMN DRAWS THE THREE SERVED STATES APART: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzf-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~118/DSGN_AMGTV1.TO-AV-zzf-1.freshness-three-repairs.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY), and only
when every criterion passes.
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W118-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** the CTO's round-53 verdict, msg 32088: "One finding for round 54, beside S25 and S26 ... Rows: ... S25 and S26 to the next
  DSGN round." `round53/ROUND53_CLOSE.md` @4a5b10aaf3 lists the three as the round-54 list.
- **Base:** the round-53 candidate 84e13d0f. The CTO approved it for DEV, and the push waits on Andrew's word. This round stacks on it.
- **The issuer's ruling (S26):** the built thing's column head is "Built analysis". It is the short head form of "the analysis built for
  this name" (decomposition v52/v53). The stale words follow the label.
- **Batched:** all three are repairs (instrument, record, style). Per obligation 1 they go into ONE cell. It is under the size floor with
  `<risk>LOCAL</risk>`, so it takes the direct-act path.
- **Three criteria:** AC2 (r53a) is the round-53 outcome's control, because this cell edits the same cell markup.

<status>cancelled</status>
<status_reason>Cancelled by the issuer before any spawn. Andrew-direct ~22:5xZ/~23:0xZ 2026-10-08 moves DSGN_AMGTV1 to DELL1 after the CURRENT round closes (record org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_225xZ_AMGT_DSGN_RIVALS_TO_DELL1_AFTER_ROUND_CLOSE_AND_BBG_CENSUS.md @b7361ceb2a; relay 1.0.0_SA_CTO~Z msg 32100: "finish the round in flight, start no new round"). Round 53 was the round in flight and is closed; this round-54 cell was issued @a07147a87c at 23:01:02Z, after his first message, and no worker took it. Its three repairs (the CTO finding of msg 32088, rows Z-S25 and Z-S26) and the check round54/checks/r54.cjs carry forward as the next DSGN_AMGTV1 round's list on DELL1.</status_reason>
<round>54</round>
<to_id>DSGN_AMGTV1.TO-AV-zzf-1</to_id>
<slot>~118</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
