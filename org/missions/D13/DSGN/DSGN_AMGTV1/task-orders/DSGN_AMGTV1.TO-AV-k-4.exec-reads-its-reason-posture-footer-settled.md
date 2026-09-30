# DSGN_AMGTV1 task order -- `AV-k-4` -- EXEC READS ITS SERVED REASON, POSTURE'S FOOTER IS SETTLED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-k-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~52</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the check reads fixtures the issuer captured (read-only invokes, round 13).
comp-adversary: RUN by the issuer at the cut on portal DEV 118cd005 -- execfooter.cjs 0 of 3 (FAIL as expected: 6501's Exec prints the static "the company's 10-K had no officer section ..." and none of its served reason; BA's settled Posture footer states no comparable outcome and reads "the comparable bundles are still loading" on a failed-and-retrying read; the no-reason fallback names a 10-K and no in-flight marker exists); green arm (scratch r14-green-d @d7d29dd5, an issuer-spawned helper; ExecManagementTab.tsx + PostureTab.tsx, +48/-6) 3 of 3; bytes 3/3; portal tsc -b rc=0; all 16 page harnesses green; stacked OVER AV-k-1 in the issuer's scratch root, execfooter and reasonwords both 3 of 3. Blind spots: the Posture arms stub the react-query states (the render run and a person read the real timing); arm 1 matches the served reason's plain words of 4+ letters; the resolved comparable is WMB's /thesis relabelled as DE (no DE capture); the planted 10-K sentence tests the predicate; document types beyond 10-K / 10-Q / 20-F / "annual report" are not searched.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-k-4` (round 14, decomposition v14; serves FWD-11 and FWD-19)

The CTO's rulings 5 and 7 (round-13 analysis). This order follows AV-k-1 on the same worktree: keep its shared reason words whole
(both write ExecManagementTab.tsx and PostureTab.tsx). Build, under `portal/src/pages/SecurityAnalysis/`:
1. **Exec's empty-state sentence comes from the served reason** (`tabs/ExecManagementTab.tsx`, the PanelEmpty near `:247` that today
   asserts "the company's 10-K had no officer section this page could read" for every name). Where a management reason is served, the
   sentence reads it in words (through AV-k-1's shared mapping; the whole reason rides a `data-` attribute, e.g. `data-exec-reason`).
   Where none is served, the fallback claims NO document type. 6501 JP (a Japanese filer) must not read "10-K". The officer source
   line (near `:255`) names "the company's 10-K" only when the served record names its section; otherwise it says no filing section
   is named on the record. A name whose served record names its 10-K section still says so.
2. **Posture's settled footer states the comparable bundles' outcome** (`tabs/PostureTab.tsx`, near `:469`, today " -- the comparable
   bundles are still loading"): resolved / not served / failed. "Loading" appears only while a FIRST read is genuinely in flight; a
   read that failed once and is being retried is a failure, not loading. The read state may ride a `data-` attribute (e.g.
   `data-posture-comparable-read="resolved|not-served|failed|loading"`).

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing. **Design law (portal
`DESIGN.md`):** a code, field name or path may sit in a data attribute or in code, never in visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact, keep its
claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, no harness needs a change.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc or `python -c`; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~52/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/DESIGN.md`, `portal/src/pages/SecurityAnalysis/reasonWords.ts` (AV-k-1's) and the
issuer's checks and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-k-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/execfooter.cjs"; echo "exit=$?"</invocation><expect>EXEC READS ITS SERVED REASON, POSTURE'S FOOTER IS SETTLED: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-k-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bound.cjs" K4 posture.harness.cjs:32 posturePattern.harness.cjs:13 execPattern.harness.cjs:9 execFallback.harness.cjs execText.harness.cjs shell.harness.cjs:10; echo "exit=$?"</invocation><expect>K4 BOUND: 6 of 6 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-k-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-k-4" judgment="true"/>
</proof_of_spec>

AC1 renders 6501's Exec on its served bundle (its reason's words, no "10-K") beside INTU's (its served 10-K section still named), BA's
Posture at rest across the settled comparable reads (an outcome stated, no "loading"), and the negatives (a first read in flight MAY say
loading; the no-reason fallback names no document; a planted static 10-K sentence is caught). Also keep AV-k-1's check green:
`node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round14/checks/reasonwords.cjs"` must still read 3 of 3 (report its
line). AC2 is the bound on every harness that loads those tabs; AC3 no control byte. AC4 is JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9
on the issuer's walk and render PNGs (6501's Exec, BA's Posture), never self-graded: nothing asserted that the served record does not
say, nothing "still loading" at rest (FWD-11, FWD-19). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~52/DSGN_AMGTV1.TO-AV-k-4.exec-reads-its-reason-posture-footer-settled.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where (6501's Exec sentence and BA's footer as they now read), the output line of every criterion (and
reasonwords.cjs), the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 14 = the round-13 analysis @1e7d4bac11 s.4 item 4 with rulings 5 and 7. Chained after AV-k-1 on slot ~52 (both
write ExecManagementTab and PostureTab). The helper's green arm stripped one-letter interface codes ("M-1") locally; on the chain, the
worker words the reason through AV-k-1's shared mapping. Base 118cd005: execfooter.cjs 0 of 3; green r14-green-d @d7d29dd5 3 of 3;
stacked over k-1 3 of 3.

<status>pending</status>
<round>14</round>
<slot>~52</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
