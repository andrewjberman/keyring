# DSGN_AMGTV1 task order -- `AV-v-1` -- THE POSTURE CITES READ AS WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-v-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~18</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 09bd04b1 -- posturecite.cjs 0 of 3 (FAIL as expected: SAP GY 7 passage ids, 3 preset codes, 2 status words; Valero 4 preset codes, 11 status words); green arm fed 3 of 3; bound 2 of 2 (PASS). Blind spot: static markup with the estate chrome stubbed; the drawer's layout is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-v-1` (round 5, decomposition v5; serves FWD-10, FWD-11)

The Posture tab (`tabs/PostureTab.tsx`) resolves every cite on a reason through `postureCites.ts` `resolveCite` and prints it in
the reason's "cites N" drawer (`<li data-posture-cite="<raw cite>">`). On SAP GY (served fixture) 10 of its 18 cite lines still
print machine form:
- 6 unresolved evidence cites: "cite not resolved -- no served drafted sentence on this name's thesis carries passage P0102; the
  thesis carries only the passages its sentences cite" (P0102, P0118, P0094, P0106, P0091, P0108);
- 1 resolved evidence cite: "filing passage P0201 (accession 000110465926020058): "<quote>"";
- 2 fit-score cites: "fit score PFOE: no score (status ABSENT; 0 of 16 factors present (16 code(s) named by the preset))";
- 1 membership cite: "membership: held in PFDE at snapshot 2026-09-15".
On Valero the drafted-sentence misses also print "(drafting SERVED; 5 sentence(s) in that section)".

Build, in `postureCites.ts` (and `PostureTab.tsx` only where a cite line's rendering must change):
1. No passage id (`P` + 4 digits) in a cite line's visible text. An evidence cite the thesis bundle CARRIES reads its document
   and section in words from the record's own served `source` fields (e.g. "the company's filing, ITEM 5. OPERATING AND
   FINANCIAL REVIEW AND PROSPECTS / paragraph 81: "<quote>""); one it does not carry says so in words (e.g. "a filing passage the
   research pack cites, which no drafted sentence on this name's thesis quotes, so this page does not carry its text"). The
   bundle serves NO document or section for an uncarried passage: never look one up, and never guess one.
2. A fit-score cite is one sentence with no preset code and no status word (e.g. "No fit score for this name on one of the model
   portfolios' screens yet: none of its 16 factors has a value." / a served score as a sentence with its value).
3. A membership cite is one sentence with no book code (e.g. "Held in 1 of the model portfolios at the 2026-09-15 snapshot.").
4. No upper-case status word (ABSENT, SERVED, PRESENT, REFUSED, UNRESOLVED) in any cite line (the drafted-sentence misses drop
   "drafting SERVED;").
The raw cite, every code and every status stay free on the element's attributes (`data-posture-cite` already carries the raw
cite; add attributes if a harness needs one). Every cite still renders -- one line per cite, none dropped -- and an unresolved
cite still says it is not resolved, beside its warning icon.

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
portal/src/pages/SecurityAnalysis/postureCites.ts
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/posturePattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~18/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-v-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/posturecite.cjs"; echo "exit=$?"</invocation><expect>POSTURE CITES IN WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-v-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round5/checks/bound.cjs" V1 posture.harness.cjs:32 posturePattern.harness.cjs:13; echo "exit=$?"</invocation><expect>V1 BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-v-1" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on two served payloads (SAP GY, Valero) and the bound. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: every Posture cite reads as words a PM follows -- no passage id, preset code or status word -- and an uncarried passage says so rather than naming a document it cannot show (FWD-10, FWD-11).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~18/DSGN_AMGTV1.TO-AV-v-1.posture-cites-read-as-words.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 5 = the round-4 analysis's enrichment list @177c576c80 section 4 item 1 (CTO msg 26684). Decomposition v5.
Base 09bd04b1: posturecite.cjs 0 of 3; green arm (scratch postureCites.ts: E-hit reads source.location, E-miss in words, FIT and
membership as sentences, "drafting SERVED;" dropped) 3 of 3; posture 32/32, posturePattern 13/13. The analysis says "7 passage ids
become the document and section in words (from the served citation fields)": 6 of the 7 are passages the bundle does NOT carry
(no served citation field exists for them), so the order admits a words sentence for those and names document + section only
where `source` is served (P0201) -- C-PRESENTATION-ONLY forbids the lookup.

<status>complete</status>
<round>5</round>
<slot>~18</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
