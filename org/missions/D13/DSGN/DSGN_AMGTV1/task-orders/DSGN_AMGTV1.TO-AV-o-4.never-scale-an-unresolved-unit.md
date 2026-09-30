# DSGN_AMGTV1 task order -- `AV-o-4` -- NEVER SCALE AN UNRESOLVED UNIT: SHOW IT RAW, LABELLED, WITH NO K / M / B / T

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-o-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~38</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV b6634ba0 -- units.cjs 0 of 3 (FAIL as expected: 6501's enterprise value 24154022.78 under an UNRESOLVED unit prints scaled; no display helper exported); green arm 3 of 3 (6 unresolved figures over the six names unscaled and labelled; 50 measured figures format exactly as before, IMB "GBP 30.13B" and AZN "USD 281B" keep their scale); bound Q4 3 of 3 at base and on the green arm (no re-anchor needed); portal tsc -b rc=0 on the green arm. Blind spot: static markup with the estate chrome stubbed; the card window opens lazily, so the window rows are graded through the exported display helper and the walk.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-o-4` (round 10, decomposition v10; serves AMGT_RESAPP FWD-30)

The CTO's ruling (round-9 analysis, ruling 3; AMGT_RESAPP round-50 addendum): a figure whose served unit is UNRESOLVED shows raw,
with its UNRESOLVED label, and never carries a K / M / B / T. The header figures carry `unit`. On six names (6501, 9433, 8316,
8035, 8766 JP and TSM US) the enterprise value -- and 8316's net debt -- is served with a unit reading "UNRESOLVED-ON-<name>:
sampled magnitude ... does not discriminate absolute vs millions". The page's one formatter,
`portal/src/pages/SecurityAnalysis/components/StatTile.tsx` `formatStatValue`, scales every money figure by magnitude, so 6501's
24154022.78 prints "JPY 24.15M" -- a magnitude the unit never claimed. Build, in `StatTile.tsx` and `HeaderCards.tsx` only:
1. `formatStatValue(value, format, currency?, unit?)` takes the figure's served `unit` as an optional fourth argument. When that
   unit starts with "UNRESOLVED", the number shows unscaled -- grouped (e.g. `toLocaleString('en-US', { maximumFractionDigits: 2
   })`), its currency code first for a money format exactly as today -- followed by " (unit not resolved)": "JPY 24,154,022.78
   (unit not resolved)". No K / M / B / T, and the raw unit string ("UNRESOLVED-ON-...", "field_map") never reaches the face.
2. Every other figure formats exactly as it does today (a MEASURED unit keeps its scale).
3. `HeaderCards.tsx` passes `figure.unit` into `formatStatValue` where it resolves a card figure, and exports
   `headerCardFigureDisplay(bundle, mnemonic): string | null` -- the display string of the header card figure with that mnemonic,
   by the SAME path the cards and windows print (the first `HEADER_CARD_DEFS` figure def carrying that mnemonic).

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
(old anchor -> new) in the instance. Measured on the green arm, no bound harness reads an unresolved figure's display, so none is
granted and none should need one -- a red bound means the change reached past unresolved units.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~38/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/constants.ts` (`HEADER_CARD_DEFS`),
`portal/src/pages/SecurityAnalysis/types.ts` (`ModelFigure.unit`), `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/` (never edit them; the fixtures are the served payloads the
checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-o-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/checks/units.cjs"; echo "exit=$?"</invocation><expect>NO SCALE ON AN UNRESOLVED UNIT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-o-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/checks/bound.cjs" Q4 shell.harness.cjs:10 tabs.harness.cjs:20 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>Q4 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-o-4" judgment="true"/>
</proof_of_spec>

AC1 is the built display on the SERVED /overlay of the six planted names (every unresolved-unit card figure unscaled, labelled in
words; each header face's enterprise value) and the control (every measured-unit card figure over eight names formats exactly as
the base formatter did; IMB's and AZN's enterprise value keep their scale); AC2 the bound on every harness that loads the header.
AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (a planted name's header beside a measured name's),
never self-graded: an unresolved figure reads as a number whose unit is not known, and no reader could take it for a scaled
amount (RESAPP FWD-30). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists
no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~38/DSGN_AMGTV1.TO-AV-o-4.never-scale-an-unresolved-unit.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 10 = the round-9 analysis s.4 item 4 with ruling 3. Base b6634ba0: units.cjs 0 of 3; green 3 of 3; Q4 3 of 3
at base and on the green arm (the green arm carried o-2, o-3 and o-4 together).

<status>pending</status>
<round>10</round>
<slot>~38</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
