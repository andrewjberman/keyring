# DSGN_AMGTV1 task order -- `AV-w-5` -- POSTURE EVIDENCE IN WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-w-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~17</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV a93071b8 -- posture.cjs 1 of 3 (FAIL as expected); bound 2 of 2 (PASS). Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-w-5` (round 4, decomposition v4; serves FWD-10)

On the Posture tab (`tabs/PostureTab.tsx`, cites via `postureCites.ts`), SAP GY (comparable ANET US):
1. The comparable's missing sources are said twice: once as three bullets ("No drafted thesis for ANET US yet -- the
   research team's pack does not include one", "No executive management record for ANET US yet -- ...", "No financial model
   block for ANET US yet -- ...") and again in a run-on line ("The comparable's evidence is incomplete: the pack for ANET US
   is missing 3 source(s) -- No drafted thesis ... -- No executive ..."). Say them ONCE: keep one lead sentence (e.g. "The
   comparable's evidence is incomplete: 3 sources are missing from ANET US's pack.") followed by the three bullets, each
   still in the shape "No <what> for ANET US yet ..." (the check counts that shape).
2. The reasons' cites print raw figure codes and unit words: "figure OPER_MARGIN FY2025: 26.1332 PERCENT", "figure
   CF_FREE_CASH_FLOW FY2025: 8264 MILLIONS", "NET_DEBT ... MILLIONS". Each reads in words: e.g. "Operating margin, FY2025:
   26.1332%", "Free cash flow, FY2025: 8,264 million". The figure's name comes from a served label if the cite carries one;
   otherwise from a fixed, named display map in `postureCites.ts` from the mnemonic to its plain name (a label, not a
   derivation), with an unmapped mnemonic reading as "a figure the research pack names <mnemonic in lower case words>" --
   never the raw code. The VALUE is printed exactly as served (no rounding, no scaling); only the unit word becomes its
   symbol or word (PERCENT -> %, MILLIONS -> million, BILLIONS -> billion, THOUSANDS -> thousand). The raw code may ride a data
   attribute.

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
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/postureCites.ts
portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/posturePattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~17/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-w-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/posture.cjs"; echo "exit=$?"</invocation><expect>POSTURE EVIDENCE IN WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-w-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/bound.cjs" W5 posture.harness.cjs:32 posturePattern.harness.cjs:13; echo "exit=$?"</invocation><expect>W5 BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-w-5" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on two served payloads (SAP GY, Valero) and the bound. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: the Posture evidence says the comparable's gaps once and every cite reads as words (FWD-10).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~17/DSGN_AMGTV1.TO-AV-w-5.posture-evidence-in-words.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 4 = the round-3 analysis's enrichment list @46d28c6c4c section 4 (CTO msg 26587). Decomposition v4.
Base a93071b8: posture.cjs 1 of 3 (FAIL as expected); bound 2 of 2 (PASS).

<status>pending</status>
<round>4</round>
<slot>~17</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
