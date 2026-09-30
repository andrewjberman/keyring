# DSGN_AMGTV1 task order -- `AV-p-1` -- A LEAD-LIST COLUMN IS HEADED BY WHAT ITS VALUES ARE ("Sector"), IN DISPLAY CASE, NEVER CUT SHORT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-p-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~32</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 29c8226a -- grain.cjs 0 of 3 (FAIL as expected: "Sub Asset" over sector names; "Industry group (finer than Sub Asset)"; "equity" shown lower-case and every value span `truncate`); green arm 3 of 3; bound Q1 5 of 5 at base and on the green arm (no re-anchor needed); portal tsc -b rc=0 on the green arm. Blind spot: static markup with the estate chrome stubbed; column widths and wrap are the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-p-1` (round 9, decomposition v9; serves FWD-2)

The CTO's ruling (round-8 analysis, ruling 1, which corrects the round-7 ruling 5 that round 8 built): **a column is headed by
what its VALUES are.** The served single-name rows carry `classification.sub_asset_class` at the GICS-SECTOR grain ("Energy",
"Information Technology"). Round 8 headed that column "Sub Asset", Positioning's label -- but Positioning's "Sub Asset" holds Opal's
buckets ("Ultra Short Duration", "High Yield", "Large"), so a PM reads "Energy" and "Large" as values of one field. Build, in
`portal/src/pages/SecurityAnalysis/components/RankedList.tsx` only:
1. The `sub_asset_class` column is headed **"Sector"**. The `asset_class` column keeps **"Asset Class"**.
2. The finer `sector` field is headed **"Industry group (finer than Sector)"**, and the unserved note names it in the same words:
   "Not served for this list yet: Industry group (finer than Sector), places moved since the last run. The research data team adds
   them." No visible "Sub Asset" anywhere in the list.
3. The asset-class VALUE shows in display case -- each word's first letter upper-cased ("equity" -> "Equity", "fixed income" ->
   "Fixed Income"); every other classification value shows exactly as served.
4. A classification value is shown WHOLE: its cell carries no `truncate`, `whitespace-nowrap`, `text-ellipsis` or
   `overflow-hidden` (let it wrap, e.g. `break-words`), so "Communication Services" reads whole.
The attribute keys and values stay as served (`data-list-column="<key>"`, `data-row-asset-class="equity"` keeps the served
lower-case value, `data-row-sub-asset-class`, `data-row-sector`, `data-list-unserved-columns="sector,places_moved"`). No row, order,
count or column set changes.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code, field name or path may sit in a data attribute or in code, never in visible text -- and text inside a
collapsed `<details>` is still visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Only a harness named in `<paths>` may be edited. Record each re-anchor
(old anchor -> new) in the instance. Measured on the green arm, no bound harness reads these labels or values, so none is granted
and none should need one -- a red bound means the change reached past the column words and cells.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~32/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`,
`portal/src/components/holdings/HoldingsBreakdownTable.tsx` (Positioning's buckets under "Sub Asset"),
`lib/research/api/tests/test_list_rows_classification.py` (the two grains), and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round9/` (never edit them; the fixtures are the served payloads the
checks render). The round-8 `labels.cjs` and round-7 `columns.cjs` arm 1 are superseded by this ruling and are not criteria.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-p-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round9/checks/grain.cjs"; echo "exit=$?"</invocation><expect>COLUMN HEADED BY ITS GRAIN: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-p-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round9/checks/bound.cjs" Q1 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 shell.harness.cjs:10 tabs.harness.cjs:20 posture.harness.cjs:32; echo "exit=$?"</invocation><expect>Q1 BOUND: 5 of 5 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-p-1" judgment="true"/>
</proof_of_spec>

AC1 is the built heading, finer-field words, display case and whole values on the four SERVED lead lists plus one labelled variant
serving the finer field, with a census printing each column's heading beside a sample of the values under it; AC2 the bound on
every harness that loads the lead list. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk
screenshots (a lead list beside the Positioning breakdown), never self-graded: each classification column's heading names what its
values are, so the lead list's "Sector" column is not read as Positioning's "Sub Asset" buckets, and no value is cut short
(FWD-2). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists no files and
checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~32/DSGN_AMGTV1.TO-AV-p-1.the-column-heading-follows-the-grain.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 9 = the round-8 analysis s.4 item 1 with ruling 1. Base 29c8226a: grain.cjs 0 of 3; green 3 of 3; Q1 5 of 5
at base and on the green arm (the green arm carried all four cells -- the drain state).

<status>pending</status>
<round>9</round>
<slot>~32</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
