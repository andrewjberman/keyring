# DSGN_AMGTV1 task order -- `AV-o-3` -- THE RESEARCH TEAM'S UPSIDE AND DOWNSIDE ON THE MODEL TAB; OPAL'S RULE CASES LABELLED AS OPAL'S

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-o-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~37</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV b6634ba0 -- cases.cjs 0 of 3 (FAIL as expected: AZN's served team Upside and Downside are not rendered; the rule's lines read "Upside case: not in the pack yet -- the method is to be agreed." beside them); green arm 3 of 3 (AZN's team Base / Upside / Downside SERVED, 60 table cells as written; 9 rule-case lines over AZN / IMB / VLO all read "Opal's ..."); bound Q3 3 of 3 at base and on the green arm (no re-anchor needed); portal tsc -b rc=0 on the green arm. Blind spot: static markup with the estate chrome stubbed; the table layout is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-o-3` (round 10, decomposition v10; serves AMGT_CORPUS FWD-12)

The CTO's ruling (round-9 analysis, ruling 2): the team's Upside and Downside from `model.team_cases` are rendered; Opal's rule
cases are labelled as Opal's ("Opal's rule-based upside: the method is to be agreed"); a bare "Upside case: not in the pack yet"
never sits beside a served team Upside. `/thesis` serves `model.team_cases` = { base, upside, downside }, each `{ status: SERVED,
table: row -> period -> text, citation, currency, unit_as_written }` or `{ status: ABSENT, reason }` (typed in `types.ts` as
`TeamCases`), and `model_cases` (Opal's rule) = { base, upside, downside }, each with its own status, `label` and `reason`. Today
`portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` renders only the team's Base (`TeamBase`) and prints the rule's lines as
"<Name> case: not in the pack yet -- ..." (`ModelCaseLine`). On AZN the team's Upside and Downside ARE served. Build, in
`ModelTab.tsx` only:
1. **The team's three cases:** render the team's Base, Upside and Downside, each exactly as the team's Base renders today -- the
   table AS WRITTEN, headed "The research team's <Base|Upside|Downside> case", its report named in words -- on an element
   `data-model-team-case="<base|upside|downside>"` with `data-model-team-case-state` SERVED / ABSENT / NOT_SERVED. An absent side
   reads one plain sentence with no figure: "The research team's Upside case is not in this pack. The research team fills it in."
   (or "... is not served on this page yet ..." when the payload carries no `team_cases`, as today for the Base).
2. **Opal's rule cases labelled as Opal's:** every rule-case line (`data-model-case`) reads with "Opal's" at its head -- the
   served `label` when it already starts "Opal's" (e.g. "Opal's historical-multiple reference: ..."); a served label without it
   is prefixed ("Opal's historical-multiple reference" for "Historical-multiple reference"); no label reads "Opal's rule-based
   <upside|base|downside>". An absent rule case reads "<head>: <plain reason>", e.g. "Opal's rule-based upside: the method is to
   be agreed." -- no "not in the pack yet", and no bare "Upside case:" / "Downside case:" / "Base case:" anywhere on the tab. The
   served status, reason, value and currency keep riding the line's `data-model-case-*` attributes as today.
No value, table cell, order or currency changes -- only which team cases render and the words that head the rule's lines.

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
(old anchor -> new) in the instance. Measured on the green arm, no bound harness reads the case words, so none is granted and none
should need one -- a red bound means the change reached past the cases.

### AMENDMENT 1 (issuer, 2026-09-30 ~06:2xZ, after the close walk; row DSGN_AMGTV1-Z-S5) -- a repair, RE-OPENING this order

The issuer's walk found AZN's Model tab reading "Opal's opal's historical-multiple reference: ...". The cause: a literal BACKSPACE
byte (0x08) where the regex meant `\b` (word boundary), so the "already says Opal's" test never matches and the served label is
prefixed again. A byte scan of `portal/src/pages/SecurityAnalysis/` finds exactly three such bytes:
- `tabs/ModelTab.tsx` line 295: `/^Opal's<0x08>/i` -- must read `/^Opal's\b/i` (this order's own line);
- `components/HeaderBrief.tsx` line 48: `/^bloomberg<0x08>/i` -- must read `/^bloomberg\b/i`;
- `components/HeaderBrief.tsx` line 49: `/^D-1<0x08>/` -- must read `/^D-1\b/` (both since round 1: no description source has ever
  read "Company description from Bloomberg"; granted here because it is the same defect class, three bytes, one repair).
Build: replace each 0x08 byte with the two characters backslash + `b`, and change NOTHING else (no other byte, no reformatting, the
files' own line endings kept). **Do it at the byte level** (e.g. a Python script reading the file in binary mode and replacing
b'\x08' with bytes([92, 98])) -- a shell heredoc or an unescaped string is how these bytes got in. Re-read the three lines after
the edit (`cat -A` shows `\b`, not `^H`). Your portal branch still carries your earlier commit; bring it to the current portal DEV
first (`git -C portal merge --ff-only DEV` if it fast-forwards, else `git -C portal merge DEV`), so the repair sits on today's page.
Rewrite this order's proof instance with all four criteria below and flip `<status>` to `complete` again in the same commit.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~37/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts` (`TeamCases`, `ModelCases`),
`portal/DESIGN.md`, and the issuer's checks and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/`
(never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-o-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/checks/cases.cjs"; echo "exit=$?"</invocation><expect>TEAM CASES AND OPAL'S RULE CASES: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-o-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/checks/bound.cjs" Q3 modelPattern.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>Q3 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-o-3" judgment="true"/>
  <criterion id="AC4" cell_refs="AV-o-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 is the built Model tab on the SERVED /thesis of AZN (the team's three cases SERVED; the rule's upside and downside ABSENT), IMB
(team cases ABSENT; the rule base SERVED) and VLO (team cases ABSENT with reasons); AC2 the bound on every harness that loads the
Model tab. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (AZN's Model tab), never self-graded: a
PM reads the research team's Upside and Downside as the team's, reads Opal's rule cases as Opal's, and sees no "not in the pack"
line beside a case the team did write (CORPUS FWD-12). AC4 (AMENDMENT 1) is 0 control bytes over the page's source, AZN's rule
label read once (plus an unprefixed variant read "Opal's ..." once), and the description source read in words. Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside
`portal/` (`tsc -p .` lists no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~37/DSGN_AMGTV1.TO-AV-o-3.the-teams-cases-and-opals-rule-cases.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 10 = the round-9 analysis s.4 item 3 with ruling 2. Base b6634ba0: cases.cjs 0 of 3; green 3 of 3; Q3 3 of 3
at base and on the green arm (the green arm carried o-2, o-3 and o-4 together).
AMENDMENT 1 (row Z-S5): graded by no gate limb as a new order (LIMB 6 refuses a new order file in an issued round; a re-cut modifies
its orders), so the repair re-opens this order. Checked at DEV 5810586a: bytes.cjs 0 of 3; on a scratch copy with the three bytes
fixed, 3 of 3, cases.cjs 3 of 3, ALL 16 of 16 harnesses, tsc -b rc=0. cases.cjs arm 2 passed the doubled label (it asks only that a
line START with "Opal's") -- a check blind spot, closed by bytes.cjs arm 2 (AC4).

<status>pending</status>
<round>10</round>
<slot>~37</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
