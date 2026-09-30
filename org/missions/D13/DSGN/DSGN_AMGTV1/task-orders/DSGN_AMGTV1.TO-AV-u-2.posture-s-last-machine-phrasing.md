# DSGN_AMGTV1 task order -- `AV-u-2` -- POSTURE'S LAST MACHINE PHRASING

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-u-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~23</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 4f927ad0 -- posturewords.cjs 1 of 3 (FAIL as expected: SAP GY 14 phrase hits, Valero 11 -- "the object", "comparable selection", "rung", "on this name's peer set", "cite(s)", "validated 18 of 18 against its packs"; the nothing-dropped control passes); green arm 3 of 3; bound 2 of 2 (PASS). Blind spot: static markup with the estate chrome stubbed.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-u-2` (round 6, decomposition v6; serves FWD-10)

Round 5 took every code off the Posture cites (0 of 18 carry one). What remains is machine PHRASING (round-5 analysis ruling 5),
built in `postureCites.ts` and the footer in `tabs/PostureTab.tsx`. On SAP GY (served fixture):
- "comparability log cap distance: 0.1047 (the object's comparable selection)"
- "cite not resolved -- no rung name for the comparable on this name's peer set or on the object's comparable selection"
- "cite not resolved -- no industry group for the comparable on this name's peer set or on the object's comparable selection"
- the footer: "10 of 18 cite(s) resolved on the bundles this page reads (the object validated 18 of 18 against its packs)"

Build: each reads as words a PM follows. A comparability measure is named from a FIXED, NAMED display map in `postureCites.ts`
(e.g. `log_cap_distance` -> "Size difference between the two companies (log of market value)", `rung_name` -> "How closely the
comparable was matched", `industry_group` -> "Industry group"; an unmapped field reads "a comparison measure the research pack
names <field in words>") -- a label, never a derivation; the value prints as served. Where it came from reads in words ("from how
the comparable was chosen", "from this company's list of comparable companies"). A miss says what the research pack does not
state ("the research pack does not say the comparable's industry group"). The footer states both served counts in words (e.g.
"10 of the 18 citations can be shown on this page; the research pack checked 18 of 18 against its sources"). None of these
words may remain in a cite line or the footer: "the object", "comparable selection", "rung", "log cap", "cite(s)", "bundles this
page reads", "on this name's peer set", "validated N of N against its packs". Every cite still renders (one line per cite), and
an unresolved cite still says it is not resolved beside its warning icon.

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
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged. This slot's NEXT order (AV-u-5) edits
   `PostureTab.tsx` too: change only the cite and footer words.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/postureCites.ts
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/posturePattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~23/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-u-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/checks/posturewords.cjs"; echo "exit=$?"</invocation><expect>POSTURE PHRASING IN WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-u-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round6/checks/bound.cjs" U2 posture.harness.cjs:32 posturePattern.harness.cjs:13; echo "exit=$?"</invocation><expect>U2 BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-u-2" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on two served payloads (SAP GY, Valero) and AC2 the bound. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: every Posture cite and the footer read as words a PM follows (FWD-10).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~23/DSGN_AMGTV1.TO-AV-u-2.posture-s-last-machine-phrasing.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 6 = round-5 analysis s.4 item 2, ruling 5. The next order of this slot (AV-u-5, the data attributes) also edits PostureTab.tsx. Base 4f927ad0: posturewords 1 of 3; green 3 of 3; U2 bound 2 of 2.

<status>complete</status>
<round>6</round>
<slot>~23</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
