# DSGN_AMGTV1 task order -- `AV-zk-1` -- DEV CI GREEN AGAIN: THE WHAT-CHANGED PANEL'S PROPS TYPE PASSES ESLINT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zk-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~91</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; local lint, type check and static checks only.
comp-adversary: RUN by the issuer at the cut on portal DEV 49c6e94a0f -- battery29.sh (as amended) FAILS: eslint rc=1, 1 error at WhatChangedPanel.tsx:395. Green arm: the one-line fix below, piped to eslint --stdin, reads rc=0.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zk-1` (round 33, decomposition v33; DIRECT ACT; DEV CI green)

Portal DEV fails CI at "Run ESLint" with one error:
```
src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
  395:18  error  An interface declaring no members is equivalent to its supertype  @typescript-eslint/no-empty-object-type
```
The line is `export interface WhatChangedPanelProps extends PairContext {}`.

Build, in `portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx` only:
1. Replace that one line with `export type WhatChangedPanelProps = PairContext`.
2. Nothing else changes: no behaviour, no other line, no import.
3. If `tsc` refuses the alias, export the `PairContext` interface (add `export` to its declaration at line 186) and keep the alias.
   Report which you did.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. Keep the file's
   existing line endings.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~91/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular the issuer's checks under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/`.

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zk-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zk-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/model/whatchanged.cjs" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/model/etwords.cjs"; echo "exit=$?"</invocation><expect>THE MODEL TAB READS IN ET AND IN READER WORDS: 4 of 4 arms -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 now includes the CI's ESLint step, errors only, and needs it to read `eslint ... rc=0`. AC2 runs whatchanged.cjs first; it must
also exit 0.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~91/DSGN_AMGTV1.TO-AV-zk-1.eslint-green-whatchanged-props.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W91-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: the change, the output line of every criterion, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Source:** MSTR~Z msg 29015 (CI 37152260084 RED at "Run ESLint"); CTO msg 29017 (review the fix the same turn); MSTR~Z msg 29018 (gate
  suggestion, adopted as battery29 AMENDMENT 1).
- **Direct act:** one line, LOCAL; the close is the issuer's run of battery29 + the CI lint step on the candidate; the CTO reviews the
  product file and MSTR~Z pushes DEV.

<status>complete</status>
<round>33</round>
<slot>~91</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker-light</worker_class>
