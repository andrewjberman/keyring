# DSGN_AMGTV1 task order -- `AV-m-5` -- THE POSTURE TAB READS AS SENTENCES WHEN THERE IS NO COMPARABLE AND NO CITATION

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-m-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~48</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cuts (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV 846ecc6c -- zerowords.cjs 1 of 3 (FAIL as expected: IMB's comparable line reads "a comparable the research team has not identified (comparable): no filing evidence is carried for this name yet."; its footer "0 of the 0 citations can be shown on this page; 0 of 0 were checked against their filings"; the VLO control passes at base by design); green arm (scratch r12-green-d @244593b7, an issuer-spawned helper) 3 of 3; posture 32/32, posturePattern 13/13, tabs 20/20, shell 10/10 (issuer re-run with lib/research present); bytes 3/3; portal tsc -b rc=0. Blind spot: static markup; the layout is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-m-5` (round 12, decomposition v12; serves FWD-11)

The CTO's item (round-11 analysis s.4 item 5): on IMB LN's Posture tab, the "Filing evidence, each side" section reads "a
comparable the research team has not identified (comparable): no filing evidence is carried for this name yet." -- a noun phrase
standing in for a name, then "this name" for the comparable's side -- and the footer reads "0 of the 0 citations can be shown on
this page; 0 of 0 were checked against their filings". Build, in `portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx` (and
`postureCites.ts` only if you need it):
1. With no comparable identified, the comparable's line of the evidence section is ONE sentence saying the research team has not
   identified a comparable (keep the words "research team has not identified"), e.g. "The research team has not identified a
   comparable yet, so there is no comparable filing evidence to show." -- never "... (comparable)" and never "this name" on that
   line. The subject's line ("IMB LN (subject): ...") is unchanged.
2. The footer at 0 citations reads in words that no citation is drafted yet (e.g. "No citation is drafted for this call yet") --
   no "0 of the 0" / "0 of 0" -- and keeps its `data-posture-cites-resolved` / `data-posture-cites-total` attributes.
3. Nothing else moves: a footer with citations reads as today ("<N> of the 20 citations can be shown on this page; 20 of 20 were
   checked against their filings"), a name with a comparable names it, the verdict card and the research team's position line are
   unchanged.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: the counts stay the
served counts. **Design law (portal `DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never in
visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact, keep its
claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, no harness needs a change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/postureCites.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~48/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md` and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-m-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/zerowords.cjs"; echo "exit=$?"</invocation><expect>POSTURE READS AS SENTENCES AT ZERO: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-m-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/bound.cjs" Q4 posture.harness.cjs:32 posturePattern.harness.cjs:13 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>Q4 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-m-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round12/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-m-5" judgment="true"/>
</proof_of_spec>

AC1 is the built Posture tab on the SERVED IMB LN /thesis (no comparable, 0 citations) and VLO US /thesis (a comparable, 20
citations -- the control): the comparable's side reads as a sentence, never "this name"; the zero footer in words with its data-
attributes; VLO unchanged. AC2 is the bound on every harness that loads the Posture tab; AC3 no control byte. AC4 is JUDGMENT, graded
by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (IMB's Posture tab), never self-graded: a PM reads the empty evidence and
the empty footer as plain sentences (FWD-11). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~48/DSGN_AMGTV1.TO-AV-m-5.posture-reads-as-sentences-at-zero.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 12 = the round-11 analysis s.4 item 5 (the Posture half; the never-collected timeline sentence rides AV-m-4,
which owns TimelinePanel.tsx). Base 846ecc6c: zerowords.cjs 1 of 3 (control by design); green r12-green-d @244593b7 3 of 3 (7+/3-,
PostureTab.tsx only).

<status>pending</status>
<round>12</round>
<slot>~48</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
