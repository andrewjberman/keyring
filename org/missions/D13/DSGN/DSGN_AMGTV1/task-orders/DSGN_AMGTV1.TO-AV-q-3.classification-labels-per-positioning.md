# DSGN_AMGTV1 task order -- `AV-q-3` -- THE LEAD LISTS NAME EACH CLASSIFICATION FIELD AS POSITIONING DOES, AND THE FINER FIELD BY ITS GRAIN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-q-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~31</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV ab7e1e49 -- labels.cjs 0 of 3 (FAIL as expected: headers "Asset class" / "Sub-asset class" against Positioning's "Asset Class" / "Sub Asset"; the finer field reads "Sector"; the note says "sector"); green arm 3 of 3; bound Q3 5 of 5 and round-7 columns.cjs 3 of 3 at base and on the green arm (no re-anchor needed); portal tsc -b rc=0 on the green arm. Blind spot: static markup with the estate chrome stubbed; the column widths are the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-q-3` (round 8, decomposition v8; serves FWD-2)

The CTO's ruling (round-7 analysis, ruling 5): the served rows carry `sub_asset_class` at the GICS-SECTOR grain for equities
("Industrials", "Financials") and a SEPARATE, finer `sector` field ("Banks" under "Financials"), so "Sub-asset class" showing sector
names while "sector" is listed unserved is a LABEL defect. The page names each field with the label the Positioning breakdown uses
for the same key; Positioning has no label for the finer field, so it is named by its grain -- never a second "Sector". The
Positioning breakdown (`portal/src/components/holdings/HoldingsBreakdownTable.tsx`, read-only) heads its columns "Asset Class"
(`asset_class`) and "Sub Asset" (`sub_asset_class`) and shows its finer field UNLABELLED under the Sub Asset value. Build, in
`portal/src/pages/SecurityAnalysis/components/RankedList.tsx` (the `COLUMNS` labels and the unserved note only):
1. `asset_class` is headed "Asset Class" and `sub_asset_class` "Sub Asset" -- exactly Positioning's header text.
2. `sector` is headed by its grain, with the words "Industry group" and "finer than Sub Asset" (e.g. "Industry group (finer than
   Sub Asset)"). No visible "Sector" / "sector" anywhere in the list. Let the header wrap rather than truncate, so the grain reads.
3. The unserved note uses the SAME labels (not lower-cased into a different word): e.g. "Not served for this list yet: Industry group
   (finer than Sub Asset), places moved since the last run. The research data team adds them." The attribute keys stay as they are
   (`data-list-unserved-columns="sector,places_moved"`, `data-list-column="<key>"`, `data-row-sector`).
No value, order, count or column set changes -- only the words that name them.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code, field name or path may sit in a data attribute or in code, never in visible text -- and text inside a
collapsed `<details>` is still visible text.

**If a bound harness check is anchored on the raw text this cell removes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Only a harness named in `<paths>` may be edited. Record each re-anchor
(old anchor -> new) in the instance. Measured on the green arm, no bound harness reads these labels, so none is granted and none
should need one -- a red bound means the change reached past the labels.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~31/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, `portal/src/components/holdings/HoldingsBreakdownTable.tsx`,
`lib/research/api/tests/test_list_rows_classification.py` (the two grains), and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round8/` and `round7/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-q-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round8/checks/labels.cjs"; echo "exit=$?"</invocation><expect>CLASSIFICATION LABELS PER POSITIONING: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-q-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round8/checks/bound.cjs" Q3 leadPanelPattern.harness.cjs:15 errorEmpty.harness.cjs:12 shell.harness.cjs:10 tabs.harness.cjs:20 posture.harness.cjs:32; echo "exit=$?"</invocation><expect>Q3 BOUND: 5 of 5 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-q-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/checks/columns.cjs"; echo "exit=$?"</invocation><expect>LEAD COLUMNS AND NO PASS BADGE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-q-3" judgment="true"/>
</proof_of_spec>

AC1 is the built labels on the four SERVED lead lists plus one labelled variant serving the finer field, with Positioning's labels
read from `HoldingsBreakdownTable.tsx` (never typed) and a census printing each key's page label beside Positioning's; AC2 the bound
on every harness that loads the lead list; AC3 round 7's served-column outcome stays whole. AC4 is JUDGMENT, graded by
`3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots (a lead list beside the Positioning breakdown), never self-graded:
the lead list's classification columns read like the Positioning breakdown, and the unserved finer field is not mistaken for the
column of sector names (FWD-2). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .`
lists no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~31/DSGN_AMGTV1.TO-AV-q-3.classification-labels-per-positioning.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 8 = the round-7 analysis s.4 item 3 with ruling 5. Base ab7e1e49: labels.cjs 0 of 3; green 3 of 3; Q3 5 of 5
and round-7 columns.cjs 3 of 3 at base and on the green arm (the green arm carried cells 2 and 3 together -- the drain state).

<status>pending</status>
<round>8</round>
<slot>~31</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
