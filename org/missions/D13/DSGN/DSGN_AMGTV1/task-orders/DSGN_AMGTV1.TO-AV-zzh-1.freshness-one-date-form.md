# DSGN_AMGTV1 task order -- `AV-zzh-1` -- DIRECT ACT: THE FRESHNESS PAGE READS ONE DATE FORM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zzh-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~120</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; two page files and their test, rendered offline by the check against a body the issuer captured.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) at the cut on DELL1, on portal DEV 8d2a08a9 in a worker-shaped nested worktree -- r56.cjs 2 of 5 (arm 1 FAIL: 285 of 285 day cells print ISO without data-day; arm 2 FAIL: page-composed ISO in the cells; arm 3 FAIL: no cell prints the long form; CONTROLS and PLANTED pass). On a scratch reference edit (longDate on the cells and the stale words, data-day added), 5 of 5. The filtered bun test matches 0 tests at the base (exit=1). The tree was not edited.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zzh-1` (round 56, decomposition v56; serves FWD-27)

The page prints days two ways: ISO in the table ("2026-09-22") and the house long form in the page end ("Data as of October 8th, 2026,
5:00p ET", from `portal/src/ui/components/PageEnd.tsx` through `formatPanelTimestamp`). The house form is the long date. One page, one
date form. Paths are under `portal/src/pages/Freshness/`. Change nothing else.

1. **Use the estate's helper; write no formatter.** `longDate` in `portal/src/pages/SecurityAnalysis/dateWords.ts` turns a `YYYY-MM-DD`
   day into the long form ("2026-10-08" -> "October 8th, 2026"). Import it (`import { longDate } from '@/pages/SecurityAnalysis/dateWords'`).
   Do not edit `dateWords.ts`.
2. **The table's days** (`Freshness.tsx`):
   - the "Oldest input" cell (`data-slot="keyed-date"`) prints `longDate(line.keyedDate)` and carries `data-day={line.keyedDate}`;
     when there is no keyed date it still prints "Nothing collected" and carries no `data-day`;
   - every input cell WITHOUT served `words` that prints a day prints `longDate(input.day)` and carries `data-day={input.day}`;
     "Never" and "Not collected" are unchanged and carry no `data-day`;
   - keep `whitespace-nowrap` on these cells, and keep every other attribute (`data-input`, `data-state`, `data-sa-state`) as it is.
3. **The stale words** (`freshnessRows.ts`): a stale input reads `` `${label} last read ${longDate(day)}` `` (for example "Built analysis
   last read August 1st, 2026"). Update the doc comment's example the same way.
4. **Served words print as served.** The Seeking Alpha sentence (`words`) and the lists lines (`owner_line`, `out_of_date`) are the
   producer's text. Do not reformat a date inside them.
5. `Freshness.test.tsx`: update only the assertions this changes and name each in your report (for example `Built analysis last read
   2026-08-01` becomes `Built analysis last read August 1st, 2026`). Add ONE test whose name contains `one date form`. It renders a row
   with a day and the page end (`PageEnd` with `pageName="Freshness"` and the same day as `dataAsOf`), and asserts:
   - the cell's day and the page end's day read the same long form;
   - the ISO day appears only in `data-day`.

## 2. BOUNDS

1. No server, no fetch, no network, no install (`bun install`, `bun add`, `npm`, `npx` are refused here), no push, no deploy.
   REFUSE, do not rescue.
2. Only the three files in section 3 change (plus your deliverables and the surprise channel).
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Edit tool ONLY. Keep each file's line endings exactly as you find them; read them first, for example with
   `python -c "print(open(p,'rb').read().count(b'\r\n'))"`.
5. The older checks `round53/checks/r53a.cjs` and `round54/checks/r54.cjs` are anchored on the ISO text this cell removes. They are not
   criteria here. Do not run or edit them.

## 3. SURFACES

<paths>
portal/src/pages/Freshness/Freshness.tsx
portal/src/pages/Freshness/freshnessRows.ts
portal/src/pages/Freshness/Freshness.test.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~120/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/dateWords.ts`, `portal/src/ui/components/PageEnd.tsx`,
`portal/src/lib/dateUtils.ts`, and the issuer's check `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round56/checks/r56.cjs`
(never edit it).

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zzh-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D1/round56/checks/r56.cjs"; echo "exit=$?"</invocation><expect>THE FRESHNESS PAGE READS ONE DATE FORM: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zzh-1"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; bun test src/pages/Freshness/Freshness.test.tsx -t "one date form"; echo "exit=$?"</invocation><expect>at least 1 pass and 0 fail -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zzh-1"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; bun test src/pages/Freshness/Freshness.test.tsx; echo "exit=$?"</invocation><expect>0 fail -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~120/DSGN_AMGTV1.TO-AV-zzh-1.freshness-one-date-form.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY), and only
when every criterion passes.
A row id on this project carries the dell1 infix: `DSGN_AMGTV1-D1-W120-S<k>`, with `surfaced_at` from `date -u +%FT%TZ` at filing.
Report once: the exact diff, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** `ledger/ROUND_ANALYSIS.round55.md` (1.0.0_SA_CTO~DELL1, msg 1391), enrichment list item 1 / ruling R1 (walker finding
  UIW-20261009T015010Z-001). The house form is cited from `PageEnd.tsx` (formatPanelTimestamp) and Security Analysis round-9 ruling 1
  (`dateWords.ts`, decomposition AV-o-1).
- **Residual, not this cell's:** the served sentences hold ISO days. The page prints them verbatim (C-PRESENTATION-ONLY). Row
  `AMGT_RESAPP-D1-S1` @76a7a2fc8a carries the producer ask.
- **Superseded anchors:** r53a's old-body arm and r54 arms 2-3 read ISO text. r56 arm 4 (CONTROLS) keeps their served-state, verbatim
  sentence and head facts. On the scratch reference edit r53a read 2 of 3 (the old-body arm, ISO-anchored).
- **Base:** portal 8d2a08a9 (origin DEV HEAD at the cut).

<status>in_progress</status>
<status_reason>REOPENED by the issuer at the drain (2.0.0_SA_COO~D1): AC1-AC3 pass, but the drain hygiene `tsc -b --noEmit` fails at Freshness.test.tsx(183,67) TS2339 -- toMatch is not on the typed Matchers (tsc passed at the base). RULING: replace `expect(...).not.toMatch(/\d{4}-\d{2}-\d{2}/)` with `expect(/\d{4}-\d{2}-\d{2}/.test(...)).toBe(false)` -- the same fact, a typed matcher. Then re-run AC1-AC3 and `node node_modules/typescript/bin/tsc -b --noEmit` from portal/ (rc=0), update the instance, flip complete.</status_reason>
<round>56</round>
<to_id>DSGN_AMGTV1.TO-AV-zzh-1</to_id>
<slot>~120</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
