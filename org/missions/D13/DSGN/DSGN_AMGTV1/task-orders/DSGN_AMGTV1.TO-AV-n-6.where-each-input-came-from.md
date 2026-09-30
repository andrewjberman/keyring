# DSGN_AMGTV1 task order -- `AV-n-6` -- THE MODEL TAB SHOWS WHERE EACH INPUT CAME FROM, WHEN IT LAST RAN AND WHETHER THAT RUN WORKED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-n-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~44</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call from the page build; the fixtures are the issuer's read-only captures at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV 2bb60cc3 -- ledger.cjs 0 of 3 (FAIL as expected: no ledger surface, no caller of /ledger); green arm 3 of 3 (6 inputs in the served order; market data from Bloomberg, run September 25th, 2026, "worked"; "1 of 6"; re-run said unavailable; no storage path); ALL 16 of 16 harnesses on the green arm with the two named harness lines; portal tsc -b rc=0; 0 control bytes. Blind spot: static markup; the layout is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-n-6` (round 11, decomposition v11; serves AMGT_RESAPP FWD-12)

AMGT_RESAPP FWD-12 (its PRD :520-528): "For each kind of input -- market data, filings, news, social, web -- the page shows where it
came from, when it last ran, and whether that run worked; and any one can be re-run on its own." AMGT_RESAPP's round-51 ruling 1
routes the page surface here. The deployed scoped API serves `GET /api/scoped/amgt/security/{key}/ledger` -> `{ security_key, classes:
{market_data|filings|news|social|web|sa: {source, stage_registered}}, outcomes: [OK, FAILED, SKIPPED], latest_by_class: {class:
{input_class, source, outcome, stamp, detail}}, entries_total, denominators: {classes, classes_with_a_stage, classes_with_a_run},
read: {status SERVED|ABSENT|READ_FAILED, reason, ...}, identity }`. NO served route re-runs one input on its own. This order follows
AV-n-5 on the same worktree: the versions surface, its hooks and its client calls are already on your branch -- keep them whole.
Build (C-PRESENTATION-ONLY -- from the served route only):
1. **Client + hook:** a client call for `/ledger` in `portal/src/api/endpoints/amgt-lead-panel.ts` (same convention as AV-n-5's), a
   query key in `constants.ts` (`AMGT_QUERY_KEYS`), the response type in `types.ts` (TYPES ONLY), and `useInputLedger(securityKey)`
   in `hooks/useLeadPanelApi.ts`.
2. **The surface, INLINE in `tabs/ModelTab.tsx`**, on `[data-input-ledger]`, headed e.g. "Where each input came from", with one
   `[data-ledger-class="<class>"]` per served class in the served order:
   - the class in words (Market data, Filings, News, Social, Web, Seeking Alpha -- no `market_data` / `sa` token);
   - its source in words (bloomberg -> Bloomberg, seekingalpha -> Seeking Alpha; null -> "no source set up yet");
   - its last run's date in the long form (the page's `dateWords.ts`) and its outcome in words ("worked" / "failed" / "skipped");
     or "has not run yet".
3. **The count and the re-run, honestly:** one line "<classes_with_a_run> of <classes> inputs have run" from the served
   denominators, and one sentence that re-running one input on its own is not available on this page yet (no served route does it).
4. **No storage path:** a run's `detail` holds storage paths ("pull landed at bloomberg/harvest/bronze/...json") -- never in
   visible text (a `data-` attribute is fine). A read that is not SERVED (ABSENT / READ_FAILED) reads one designed sentence that the
   input ledger is not there for this name yet -- no storage key, no status token.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing. **Design law (portal
`DESIGN.md`):** a code, field name, key or path may sit in a data attribute or in code, never in visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact, keep its
claim, never drop it; only a harness named in `<paths>` may be edited. Measured on the green arm, the new hook NECESSARILY breaks the
same two stubs AV-n-5 extended, each granted with its exact change:
- `modelPattern.harness.cjs` (the `useLeadPanelApi` loader stub): add `useInputLedger: () => ({ data: undefined, isLoading: false,
  isError: false })` beside the hooks already there.
- `tabs.harness.cjs` (`SOURCE_STUBS['src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts']`): add
  `useInputLedger: () => ({ data: undefined, isLoading: false }),` beside the hooks already there.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools, never through a shell heredoc; AC3 scans for control bytes.

## 3. SURFACES

<paths>
portal/src/api/endpoints/amgt-lead-panel.ts
portal/src/pages/SecurityAnalysis/constants.ts
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
portal/src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~44/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `lib/research/api/scoped_amgt.py` (the /ledger builder, :3883),
`lib/research/ledger/ledger.py` (the six classes, :46-53), `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` (FWD-12),
`portal/src/pages/SecurityAnalysis/dateWords.ts`, `portal/DESIGN.md`, and the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 180)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-n-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/ledger.cjs"; echo "exit=$?"</invocation><expect>WHERE EACH INPUT CAME FROM: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-n-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/bound.cjs" Q6 modelPattern.harness.cjs:12 tabs.harness.cjs:20 shell.harness.cjs:10 errorEmpty.harness.cjs:12; echo "exit=$?"</invocation><expect>Q6 BOUND: 4 of 4 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-n-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round11/checks/bytes.cjs"; echo "exit=$?"</invocation><expect>NO CONTROL BYTES, LABELS READ RIGHT: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AV-n-6" judgment="true"/>
</proof_of_spec>

AC1 is the built surface on the SERVED BA US /ledger plus labelled variants (a FAILED run; an ABSENT ledger); AC2 the bound on every
harness that loads the Model tab or the page around it; AC3 no control byte in the page's source. AC4 is JUDGMENT, graded by
`3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (BA's Model tab), never self-graded: for each kind of input a PM reads where it
came from, when it last ran and whether that worked, and reads honestly that re-running one alone is not yet available (RESAPP
FWD-12's re-run half has no served route). Portal typecheck, if you run one: `node_modules/.bin/tsc -b --noEmit` inside `portal/`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~44/DSGN_AMGTV1.TO-AV-n-6.where-each-input-came-from.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each harness change (old -> new), the output line of every criterion, the portal and outer
commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11 = the round-10 analysis s.4 item 6 (RESAPP round-51 ruling 1). Chained on ~44 after AV-n-5 (shared write
set). The re-run half of RESAPP FWD-12 has no served route: the page says so, and it is a round-12 input for AMGT_RESAPP (a per-input
re-run route). Base 2bb60cc3: ledger.cjs 0 of 3; the green arm 3 of 3; ALL 16 of 16 with the stub lines; tsc rc=0.

<status>pending</status>
<round>11</round>
<slot>~44</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
