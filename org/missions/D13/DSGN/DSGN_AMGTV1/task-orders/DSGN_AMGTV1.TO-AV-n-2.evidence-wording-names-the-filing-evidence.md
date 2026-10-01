# DSGN_AMGTV1 task order -- `AV-n-2` -- THE POSTURE TAB'S EVIDENCE WORDING NAMES WHICH EVIDENCE IT MEANS AND WHICH IS ABSENT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-n-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~41</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cuts (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV 2bb60cc3 -- evidence.cjs 1 of 3 (FAIL as expected: the evidence section says "pack" / "the research team's pack" / "research pack"; 992 HK and IMB read "no pack for <KEY> is carried in packs on this object"; the control passes at base by design); green arm 3 of 3; ALL 16 of 16 harnesses and Q2 4 of 4 at base and on the green arm (no re-anchor needed); portal tsc -b rc=0; 0 control bytes. Blind spot: static markup; the layout is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-n-2` (round 11, decomposition v11; serves FWD-11)

The CTO's ruling (round-10 analysis, ruling 3): IMB's Posture tab put two "packs" side by side. The evidence-coverage lines refer to
AMGT_RESAPP's FILING-EVIDENCE object; the position line above them refers to the research team's pack (the dossier). Each is named
by what it is, and "no pack is carried in packs on this object" becomes a sentence a PM can read, naming which evidence is absent.
Build, in `portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx` and `portal/src/pages/SecurityAnalysis/postureCites.ts`:
1. The evidence-coverage section and its citation footer name the FILING EVIDENCE and never say "pack" / "packs" / "research pack" /
   "the research team's pack". For example:
   - the heading "Filing evidence, each side";
   - an absent side: "IMB LN (subject): no filing evidence is carried for this name yet.";
   - an absent source (the sentence comes from `postureCites.ts` `absentSourceSentence`; its trailing clause is the `FILLED_BY`
     constant): "No executive management record for VLO US yet -- the filing evidence does not include one";
   - the footer: "20 of the 20 citations can be shown on this page; 20 of 20 were checked against their filings".
2. No machine words anywhere on the Posture tab:
   - "on this object" goes ("No basis claim on this object." -> e.g. "No reason with a basis is drafted for this name yet.";
     "Comparable: none named on this object." -> "Comparable: none named yet.");
   - no raw security key (`IMB_LN_Equity`) is printed -- use the page's identity label or plain words; the key may ride its data-
     attribute.
3. Nothing else moves: every served count, value and citation stays as it is, and the research team's position line ("Fund of
   record: ...; last stated position: ...", with "Source: <report>") is left exactly as it is -- that IS the research team's pack.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state naming,
in plain words, what is missing and which team fills it -- never a project code, serial or storage path. **Design law (portal
`DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never in visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact as the page
now states it, keep its claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, no harness
needs a change, so none is granted.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/postureCites.ts
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~41/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md` and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-n-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/evidence.cjs"; echo "exit=$?"</invocation><expect>EVIDENCE WORDING NAMES THE FILING EVIDENCE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-n-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/bound.cjs" Q2 posture.harness.cjs:32 posturePattern.harness.cjs:13 tabs.harness.cjs:20 shell.harness.cjs:10; echo "exit=$?"</invocation><expect>Q2 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-n-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-n-2" judgment="true"/>
</proof_of_spec>

AC1 is the built Posture tab on the SERVED /thesis of seven names (the evidence section and footer name the filing evidence; no
"pack", "on this object" or raw key; an absent side says no filing evidence is carried; served counts and the research team's
position line unchanged); AC2 the bound on every harness that loads the Posture tab; AC3 no control byte in the page's source. AC4 is
JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (IMB's Posture tab), never self-graded: a PM can tell the
filing evidence from the research team's pack and reads which evidence is absent (FWD-11). Portal typecheck, if you run one:
`node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~41/DSGN_AMGTV1.TO-AV-n-2.evidence-wording-names-the-filing-evidence.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11 = the round-10 analysis s.4 item 2 with ruling 3. `postureCites.ts` is granted because the absent-source
sentence's clause is its `FILLED_BY` constant (found by the green arm; its only caller is PostureTab.tsx). Base 2bb60cc3: evidence.cjs
1 of 3; green 3 of 3; ALL 16 of 16; tsc rc=0.

<status>complete</status>
<round>11</round>
<slot>~41</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
