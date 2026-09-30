# DSGN_AMGTV1 task order -- `AV-l-3` -- THE THREE C14 BLOCKS ARE ONE PLAIN SENTENCE OR FOLDED, AND THE RAW TOKENS ARE GONE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-l-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~49</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV ba62e945 -- c14.cjs 0 of 3 (FAIL as expected: an ABSENT description reads "Description: ABSENT -- no description header scalar ['CIE_DES', ...]"; BA's Exec reads "CEO public profile (Robert K. Ortberg): unreadable object -- status=ABSENT query=set absence_class=None"; Peers shows a raw ISO stamp, "R-1" and "CSC"; the Thesis driver chart shows "PASSAGE P0278"-style ids; Posture shows "N drafted sentences, N evidence records ..." at rest); green arm (scratch r13-green-a @3f79ec94 over AV-l-1, an issuer-spawned helper; 6 files, +48/-21) 3 of 3, dossier.cjs still 3 of 3; bytes 3/3; portal tsc -b rc=0; posture, posturePattern, peersPattern, execPattern, shell and drafting green. Blind spot: c14's long-form as-of test also matches the identity line's date, so the raw-ISO clause is what grades the Peers as-of; static markup (the folded block's affordance is the walk's).
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-l-3` (round 13, decomposition v13; serves FWD-11 and FWD-20's person-read rejections)

The CTO's ruling 3 (round-12 analysis), on the CVO's three C14 rejections of round 12's render PNGs: each is cut to one plain
sentence or folded, never a count block at rest; and FWD-11's raw tokens go with them. This order follows AV-l-1 on the same
worktree: keep its dossier readers whole (they share PostureTab.tsx and ExecManagementTab.tsx). Build, under
`portal/src/pages/SecurityAnalysis/`:
1. **An ABSENT description** (`components/HeaderBrief.tsx` `DescriptionLine`, and the description block in `components/ThesisCards.tsx`)
   reads one plain sentence -- "No company description is on file yet." -- or nothing; never "Description: ABSENT --" plus the raw
   reason. The reason may ride a `data-` attribute. A served description is unchanged.
2. **Exec's CEO public profile line** (`tabs/ExecManagementTab.tsx`): one plain sentence (e.g. "CEO public profile (Robert K.
   Ortberg): no public profile is on file yet."), no "unreadable object", "status=", "query=" or "absence_class" in visible text (they
   may ride `data-` attributes).
3. **Posture's "Filing evidence, each side" count block** (`tabs/PostureTab.tsx`): folds behind a closed affordance (e.g. a
   `<details>` whose summary is the heading) -- never "N drafted sentences, N evidence records ..." at rest; the verdict card, the
   comparable sentence and the numbered reasons stay visible.
4. **Peers** (`tabs/PeersTab.tsx`): the as-of reads as a long-form date (the served `as_of` looks like "2026-09-24T2252Z", which the
   page's `longStamp` does not parse); no "R-1" and no "CSC" in visible text (e.g. "5 present / 12 absent of 17 declared column(s) in
   the comparison map; 5 column(s) carry a per-member value.").
5. **The Thesis driver chart** (`components/ThesisDriverChart.tsx`): no passage id ("PASSAGE P0278", "P0278") in visible text -- e.g.
   "2023: 528 -- show the filing passage"; the id may ride a `data-` attribute.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing. **Design law (portal
`DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never in visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact, keep its
claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, no harness needs a change (the Peers
counts line keeps the substrings `peersPattern` anchors on).

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx
portal/src/pages/SecurityAnalysis/components/ThesisDriverChart.tsx
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~49/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md`, `portal/src/pages/SecurityAnalysis/dateWords.ts`, and the issuer's
checks and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-l-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/c14.cjs"; echo "exit=$?"</invocation><expect>C14 BLOCKS CUT, RAW TOKENS GONE: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-l-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/bound.cjs" Q3 posture.harness.cjs:32 posturePattern.harness.cjs:13 peersPattern.harness.cjs:13 execPattern.harness.cjs:9 shell.harness.cjs:10 drafting.harness.cjs:8; echo "exit=$?"</invocation><expect>Q3 BOUND: 6 of 6 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-l-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-l-3" judgment="true"/>
</proof_of_spec>

AC1 is the built header, Thesis, Exec, Peers and Posture surfaces on the SERVED BA /thesis, /overlay and /peers, plus labelled planted
ABSENT descriptions: each C14 block one plain sentence or folded, each raw token gone, the served description and the verdict card
unchanged. AC2 is the bound on every harness that loads those surfaces; AC3 no control byte. Also keep AV-l-1's check green: `node
"org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round13/checks/dossier.cjs"` must still read 3 of 3 (report its line).
AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk and render PNGs (BA's header, Exec, Peers, Posture and
Thesis), never self-graded: no count block at rest and no machine token on the face (FWD-11, FWD-20's C14 rejections). Portal
typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~49/DSGN_AMGTV1.TO-AV-l-3.c14-blocks-cut-raw-tokens-gone.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where (the visible wording of each fixed line), the output line of every criterion (and dossier.cjs), the
portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 13 = the round-12 analysis s.4 item 3 with ruling 3, minus the Model tab's "C-MODEL" token (AV-l-2 owns
ModelTab.tsx), plus the issuer's same-class Peers words "R-1" / "CSC" (walk L). Chained after AV-l-1 on slot ~49 (both write PostureTab
and ExecManagementTab). Base ba62e945: c14.cjs 0 of 3; green r13-green-a @3f79ec94 3 of 3.

<status>complete</status>
<round>13</round>
<slot>~49</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
