# DSGN_AMGTV1 task order -- `AV-s-4` -- THE LEAD LISTS SHOW OPAL'S SERVED CLASSIFICATION AS COLUMNS; THE PASS BADGE LEAVES THE FACE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-s-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~27</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV fd4deb75 -- columns.cjs 0 of 3 (FAIL as expected: no column header, no data-row-asset-class / -sub-asset-class, no not-served note; 13 drafted sentences show a visible "PASS" badge); green arm 3 of 3; bound U4 5 of 5 at base and on the green arm (after the two re-anchors below); vv-5.AC1 YES on both. Served-column census at the cut: asset class and sub-asset class 30 of 32 on each price list and 2 of 2 on Trending x Chatter; sector 0 on every list; no places-moved field on any row; Breakout x Chatter 0 rows.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-s-4` (round 7, decomposition v7; serves FWD-2, FWD-11)

This is the SECOND order of your slot. The first (AV-s-2: the window footers) is already committed on your branches by this slot;
build on top of it and do not change what it built.

1. **FWD-2's columns from served fields (CTO ruling 5: measure, then build).** `components/RankedList.tsx` prints each row's name,
   ticker and figure, never its classification, though every served list row carries `classification`
   `{asset_class, sub_asset_class, sector}`. Build: the list gets a column header row (`data-list-columns`, one
   `data-list-column="<key>"` per column any row serves: "Asset class", "Sub-asset class", "Sector") and each row shows, aligned
   under those headers like the Positioning page's holdings breakdown, the SERVED value exactly as served -- on
   `data-row-asset-class` / `data-row-sub-asset-class` / `data-row-sector` and in visible text; a row that does not serve a column
   shows a plain placeholder ("--") and carries no attribute. A column NO row serves is not drawn; instead the list states ONCE
   which columns are not served (`data-list-unserved-columns="sector,places_moved"` -- `places_moved` always, because no served
   row carries a places-moved field) in words (e.g. "Not served for this list yet: sector, places moved since the last run. The
   research data team adds them."). Nothing is computed, looked up or joined.
2. **The PASS badge leaves the face (CTO ruling 6).** `components/ThesisCards.tsx` `SentenceBlock` draws `CheckFaceBadge` for every
   drafted sentence's `verbatim_check`, so each Recommendation line (and every other drafted line) ends in "PASS" -- a status word on
   the face. A PASS draws nothing visible; the sentence's element carries `data-verbatim-check="<served value>"`. A REFUSE /
   PROVISIONAL sentence keeps its badge.

**Two harness checks this change NECESSARILY moves (granted in `<paths>`; re-anchor exactly these, claims unchanged):**
1. `__harness__/drafting.harness.cjs` `verbatim_badge` (~line 236): it looks for a visible `>PASS</span>`. Re-anchor: a REFUSE
   sentence still needs `>REFUSED</span>`; any other served verdict reads `data-verbatim-check="<verdict>"` in the sentence region.
   Floor 8.
2. `__harness__/thesisLadder.harness.cjs` `pass_faces_kept` (~line 295): it counts `>PASS</span>` faces. Re-anchor: count
   `data-verbatim-check="PASS"` in place of `>PASS</span>`, keeping the REFUSED and PROVISIONAL face counts. Floor 10.

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
(old anchor -> new) in the instance.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/thesisLadder.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~27/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/` (never edit them; the fixtures are the served payloads the checks render).
Also read-only: `portal/src/pages/Positioning/tabs/HoldingsTab.tsx` and `portal/src/components/holdings/HoldingsBreakdownTable.tsx` (the layout reference).
Also read-only: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh` (the parity criterion).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-s-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/checks/columns.cjs"; echo "exit=$?"</invocation><expect>LEAD COLUMNS AND NO PASS BADGE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-s-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round7/checks/bound.cjs" U4 drafting.harness.cjs:8 thesisLadder.harness.cjs:10 leadPanelPattern.harness.cjs:15 tabs.harness.cjs:20 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>U4 BOUND: 5 of 5 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-s-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh"; echo "exit=$?"</invocation><expect>FWD-30 HARNESS READS THE REDESIGNED PAGE: YES -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-s-4" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on the four SERVED lead-panel lists (it prints the served-column census first) and the served VLO thesis, with two labelled variants (a served sector; a REFUSE sentence); AC2 the bound; AC3 the page/export parity (ThesisCards renders in it). AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (`lead-lists.json` and the list shots, a Recommendation window), never self-graded: every list row shows name, ticker, Opal's asset class and sub-asset class where served, laid out like the Positioning holdings breakdown, the unserved columns named once, and no PASS on the face (FWD-2, FWD-11). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~27/DSGN_AMGTV1.TO-AV-s-4.lead-columns-and-no-pass-badge.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 7 = the round-6 analysis s.4 item 4 with rulings 5 and 6. Base fd4deb75: columns.cjs 0 of 3.

<status>complete</status>
<round>7</round>
<slot>~27</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
