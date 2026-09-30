# DSGN_AMGTV1 task order -- `AV-k-1` -- SERVED REASONS READ AS WORDS ON EVERY FACE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-k-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~52</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check reads fixtures the issuer captured (read-only invokes, round 13).
comp-adversary: RUN by the issuer at the cut on portal DEV 118cd005 -- reasonwords.cjs 1 of 3 (FAIL as expected: BA's header reads "No fund of record: no report's RECOMMENDATION line names a fund token (IDVZ|PFOE|DIVZ)."; Exec "... no MANAGEMENT section in class A missing or class B missing."; 4 faults over 4 faces; a planted new family "OUTLOOK_SUMMARY ... (ABCD|EFGH)" shows verbatim; arm 3 is the control and passes at base by design); green arm (scratch r14-green-a @f2258ff0, an issuer-spawned helper; 8 files, +66/-28) 3 of 3; bytes 3/3; portal tsc -b rc=0; all 16 page harnesses green with three granted loader lines; stacked with AV-k-4 and AV-k-2 in the issuer's scratch root, every check 3 of 3. Blind spots: the token detector is a pattern set (a lower-case machine word or a 2-3 letter code is not caught); only the four dossier-line elements, on BA, 6501 and planted bundles; the wording of each sentence is the L9 read.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-k-1` (round 14, decomposition v14; serves FWD-11)

The CTO's ruling 1 (round-13 analysis): machine tokens in served dossier reasons are fixed at the PAGE, by the page's own existing
pattern. The page shows the producer's per-field reasons verbatim, and for every name with a dossier they carry machine tokens: "(IDVZ|PFOE|DIVZ)", "RECOMMENDATION line", "class A missing or class B missing", "no class A report", "MANAGEMENT section". Build, under `portal/src/pages/SecurityAnalysis/`:
1. **One shared word mapping** (e.g. a new `reasonWords.ts`), following the Model tab's pattern (`tabs/ModelTab.tsx` `dropContractCodes`,
   `formulaInWords`, `caseAbsenceWords`): a served reason is turned into plain words and the WHOLE served reason rides a `data-`
   attribute. It is a pattern, not string replaces: a new token family of the same kinds (a code list in parentheses such as
   "(ABCD|EFGH)", an ALL-CAPS field or section name) is worded or dropped too. Class A reads "research pack" and class B "earnings
   update" (the producer's own docstring, `lib/research/corpus/dossier.py:14`).
2. **Every face that prints a served dossier reason uses it**: the header's fund line (`components/SecurityOverlay.tsx`), Exec's management
   line (`tabs/ExecManagementTab.tsx`), Posture's fund and last-stated-position line (`tabs/PostureTab.tsx`) and Thesis's pillars line
   (`tabs/ThesisTab.tsx`). Each face drops its own local copy of the reason-words helper.
3. **A served reason with no token reads as served** (e.g. 6501's "no research dossier exists for this name").
Do not move or change `ModelTab.tsx` (another cell owns it); import nothing from it.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing. **Design law (portal
`DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never in visible text. Producer wording is NOT
re-opened (the reasons also serve machine readers).

**Granted harness changes (exact, tested on the green arm):** `drafting.harness.cjs`, `execFallback.harness.cjs` and `execText.harness.cjs`
load only the modules they name, so each needs ONE line naming the new module: the diffs are
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/grants/{drafting,execFallback,execText}.harness.cjs.reasonwords.diff`
(apply them as written, adjusted only for your module's file name). No other harness may change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/reasonWords.ts
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execText.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~52/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md`, `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` (the pattern)
and the issuer's checks, fixtures and grants under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-k-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/reasonwords.cjs"; echo "exit=$?"</invocation><expect>SERVED REASONS READ AS WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-k-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bound.cjs" K1 posture.harness.cjs:32 posturePattern.harness.cjs:13 execPattern.harness.cjs:9 execFallback.harness.cjs execText.harness.cjs drafting.harness.cjs:8 shell.harness.cjs:10 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>K1 BOUND: 8 of 8 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-k-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-k-1" judgment="true"/>
</proof_of_spec>

AC1 renders BA's header, Exec, Posture and Thesis on the SERVED bundle (no token family in visible text, a sentence present, each
face's served reason whole in its data attribute), a planted new token family on the same faces, and 6501's token-free reason unchanged;
arm 3 is a negative control on the detector. AC2 is the bound on every harness that loads those faces; AC3 no control byte. AC4 is
JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on the issuer's walk and render PNGs (BA's header, Exec, Posture, Thesis), never self-graded:
no machine token on the face (FWD-11, ruling 1). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~52/DSGN_AMGTV1.TO-AV-k-1.served-reasons-read-as-words.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where (the visible wording of each fixed line on BA), the output line of every criterion, the portal
and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 14 = the round-13 analysis @1e7d4bac11 s.4 item 1 with ruling 1. Leads chain ~52 (k-1 -> k-4 -> k-2: all three
write ExecManagementTab and PostureTab). Round 13's frozen `dossier.cjs` arm 2 reads BA's verbatim "no class A report" and will read FAIL
after this cell (inferred by the helper; a round-13 check, not a round-14 bound). Base 118cd005: reasonwords.cjs 1 of 3; green
r14-green-a @f2258ff0 3 of 3.

<status>pending</status>
<round>14</round>
<slot>~52</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
