# DSGN_AMGTV1 task order -- `AV-n-1` -- AN UNRESOLVED FIGURE LEADS WITH ITS QUALIFIER, AND ITS DIGITS ARE LABELLED A RAW FIGURE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-n-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~40</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cuts (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV 2bb60cc3 -- unitlead.cjs 1 of 3 (FAIL as expected: every unresolved figure reads "TWD 71,993,494.73 (unit not resolved)"-style, amount first; the measured-unit control passes at base by design); green arm 3 of 3; ALL 16 of 16 harnesses and Q1 3 of 3 at base and on the green arm (no re-anchor needed); portal tsc -b rc=0; 0 control bytes. Blind spot: the card window opens lazily, so window rows are graded through the exported display helper and the walk.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-n-1` (round 11, decomposition v11; serves AMGT_RESAPP FWD-30, FWD-11)

The CTO's ruling (round-10 analysis, ruling 1): round 10 showed TSM's enterprise value as "TWD 71,993,494.73 (unit not resolved)",
which reads as about TWD 72 million when the served number is very likely in millions (TWD 72 trillion). The qualifier must LEAD
and the digits be labelled raw, so a reader who stops early reads "unit not resolved", never an amount. Build, in
`portal/src/pages/SecurityAnalysis/components/StatTile.tsx` `formatStatValue` only (its unresolved-unit branch, added in round 10):
1. A figure whose served `unit` starts "UNRESOLVED" displays as `unit not resolved -- raw figure <digits>` followed, for a money
   format with a served currency, by ` (<CURRENCY>)`: e.g. "unit not resolved -- raw figure 71,993,494.73 (TWD)". The digits stay
   the served number, grouped and unscaled (no K / M / B / T); with no currency served there are no brackets.
2. Every other figure formats exactly as it does today. `HeaderCards.tsx` (`headerCardFigureDisplay`, which passes the unit) is
   unchanged; the card face then reads "Enterprise value unit not resolved -- raw figure ... (TWD)".

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed. **Design law (portal `DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never
in visible text -- the raw unit string ("UNRESOLVED-ON-...", "field_map") never reaches the face.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact as the
page now states it, keep its claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, no
harness needs a change, so none is granted.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc (they can turn a backslash sequence into a control byte);
   AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~40/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `components/HeaderCards.tsx`, `constants.ts` (`HEADER_CARD_DEFS`), `portal/DESIGN.md`,
and the issuer's checks and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-n-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/unitlead.cjs"; echo "exit=$?"</invocation><expect>UNRESOLVED FIGURE LEADS WITH ITS QUALIFIER: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-n-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/bound.cjs" Q1 shell.harness.cjs:10 tabs.harness.cjs:20 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>Q1 BOUND: 3 of 3 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-n-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-n-1" judgment="true"/>
</proof_of_spec>

AC1 is the built display on the SERVED /overlay of the six planted names (the qualifier first, the digits labelled raw, the
currency after them; each header face putting "unit not resolved" before the digits) and the control (every measured-unit card
figure over eight names formats exactly as before); AC2 the bound on every harness that loads the header; AC3 no control byte in
the page's source. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (TSM's header), never
self-graded: a reader who stops early reads that the unit is not resolved, never an amount (RESAPP FWD-30, FWD-11). Portal
typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~40/DSGN_AMGTV1.TO-AV-n-1.the-qualifier-leads-an-unresolved-figure.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11 = the round-10 analysis s.4 item 1 with ruling 1. Base 2bb60cc3: unitlead.cjs 1 of 3; the green arm (issuer
scratch r11-green-a by an issuer-spawned helper agent) 3 of 3; ALL 16 of 16; tsc rc=0; round-10 units.cjs is superseded on its
display form by ruling 1.

<status>pending</status>
<round>11</round>
<slot>~40</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
