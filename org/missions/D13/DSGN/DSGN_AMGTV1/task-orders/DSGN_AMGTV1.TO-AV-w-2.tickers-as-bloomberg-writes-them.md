# DSGN_AMGTV1 task order -- `AV-w-2` -- THE LEAD LIST PRINTS EACH TICKER AS BLOOMBERG WRITES IT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-w-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~14</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV a93071b8 -- ticker.cjs 2 of 5 (FAIL as expected); bound 2 of 2 (PASS). Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-w-2` (round 4, decomposition v4; serves FWD-2)

Round 2 added `tickerFace()` in `components/RankedList.tsx`, which strips a literal slash from a served ticker ("BP/ LN" ->
"BP LN"). The CTO reversed that ruling (round-3 analysis, decision 2): "BP/ LN" and "WALMEX* MM" ARE the Bloomberg tickers --
the "/" and "*" are part of what a PM types into a terminal, not artifacts of a key. The page shows the ticker as Bloomberg
writes it: only a KEY's own encoding (the "_" separators and the "_Equity" suffix of a `security_key`) is ever removed, and a
served `ticker` is not a key, so it prints exactly as served. When the served company name is carried, the name leads and the
ticker is secondary (unchanged).

Build, in `components/RankedList.tsx`: the list prints each row's served `ticker` whole -- "BP/ LN", "WALMEX* MM", "NG/ LN" --
wherever it prints a ticker (the lead line when no name is served, and the secondary ticker line). Keep the `tickerFace`
export if other code imports it, returning the ticker unchanged apart from trimming; update its doc comment to the ruling.
No `security_key` text reaches the face.

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
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~14/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/types.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/` (never edit them; the fixtures are the served payloads the checks render).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-w-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/ticker.cjs"; echo "exit=$?"</invocation><expect>TICKERS AS WRITTEN: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-w-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/bound.cjs" W2 leadPanelPattern.harness.cjs:15 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>W2 BOUND: 2 of 2 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-w-2" judgment="true"/>
</proof_of_spec>

The mechanical criteria are the built behaviour on the served Trending x Price payload and the bound. AC3 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk screenshots, never self-graded: the lead list reads each ticker as a PM would type it into a terminal ("BP/ LN", "WALMEX* MM") (FWD-2).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~14/DSGN_AMGTV1.TO-AV-w-2.tickers-as-bloomberg-writes-them.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 4 = the round-3 analysis's enrichment list @46d28c6c4c section 4 (CTO msg 26587). Decomposition v4.
Base a93071b8: ticker.cjs 2 of 5 (FAIL as expected); bound 2 of 2 (PASS).

<status>pending</status>
<round>4</round>
<slot>~14</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
