# DSGN_AMGTV1 task order -- `AV-w-3` -- NO STATUS WORD ON THE MODEL FACE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-w-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~15</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV a93071b8 -- status.cjs 1 of 3 (29 hits per surface; FAIL as expected); bound 2 of 2 (PASS); vv-5.AC1 YES, 4 of 4 sets exact (PASS). Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-w-3` (round 4, decomposition v4; serves FWD-11)

The Model tab (`tabs/ModelTab.tsx`) still prints status words as labels on the face. On SAP GY and on Valero (served
fixtures) it reads: "Revenue per share REFUSED -- The number is in the pack, but this page cannot show it yet because its
unit convention is not built." eighteen times; "y/y growth rows: ABSENT -- the block carries none and this page computes
none."; "2026E, 2027E, 2028E: ABSENT -- the block carries fiscal years 2016 to 2025 only."; "Upside case: ABSENT --
methodology to be discussed with Andrew"; "Historical-multiple reference: SERVED -- 159.61 EUR (...)"; and three score tiles
"Robustness not read", "Peers V not read", "Divergence D not read".

Build: each becomes a plain sentence a PM reads without a legend -- e.g. "Revenue per share: in the research pack, but this
page cannot show it yet because its unit is not set up here.", "No year-on-year growth rows: the pack carries none and this
page computes none.", "Historical-multiple reference: 159.61 EUR (...)", "Upside case: not in the pack yet -- the method is to
be agreed." -- and the score tiles name the score in words and say it has not been measured yet rather than "not read" (the
letter-coded labels "Peers V" / "Divergence D" read as the score's name in words). No upper-case status word (REFUSED,
ABSENT, SERVED, NOT_SERVED, UNRESOLVED, PRESENT), no "not read", no "Peers V" / "Divergence D" on the face. The served state
stays on the element: every refused line keeps its `data-model-line-refusal` attribute, and a case's or row's status may ride
a data attribute. The numbers, the served figures, the case values and the order of lines are unchanged.

The page/export parity harness (`__harness__/exportCompare.harness.cjs`, graded by AC3) compares the page's absences, cases
and figures with the export's; it keys on the data attributes, but some of its checks still anchor on the page's "REFUSED --"
/ "ABSENT --" / "SERVED --" text. If AC3 goes red, re-anchor those checks onto the data attributes (the same fact), never
weaken a set comparison.

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
2. Only the files in `<paths>` under `portal/` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/assembled.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~15/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/` (never edit them; the fixtures are the served payloads the checks render).
Also read-only: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh` (AC3's check).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-w-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/status.cjs"; echo "exit=$?"</invocation><expect>MODEL STATUS WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-w-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/bound.cjs" W3 modelPattern.harness.cjs:12 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>W3 BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-w-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh"; echo "exit=$?"</invocation><expect>FWD-30 HARNESS READS THE REDESIGNED PAGE: YES -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-w-3" judgment="true"/>
</proof_of_spec>

AC1 is the built behaviour on two served payloads; AC2 the bound; AC3 (the one further criterion this cell needs) the page/export parity, which reads the same lines this cell rewords. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: the Model tab reads every missing, refused and unmeasured line as a plain sentence, with no status label on the face (FWD-11).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~15/DSGN_AMGTV1.TO-AV-w-3.status-words-off-the-model-face.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 4 = the round-3 analysis's enrichment list @46d28c6c4c section 4 (CTO msg 26587). Decomposition v4.
Base a93071b8: status.cjs 1 of 3 (29 hits per surface; FAIL as expected); bound 2 of 2 (PASS); vv-5.AC1 YES, 4 of 4 sets exact (PASS).

<status>pending</status>
<round>4</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
