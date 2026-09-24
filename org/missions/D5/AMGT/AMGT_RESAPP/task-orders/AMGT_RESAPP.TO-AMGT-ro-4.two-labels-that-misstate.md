# AMGT_RESAPP task order -- `AMGT-ro-4` -- TWO LABELS THAT MISSTATE: posture's 'still loading' and the header's 'BLOOMBERG: UNKNOWN'

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ro-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~155</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-39 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-ro-4` (round 40, decomposition s.48)

(a) `portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx:483` sets the comparable side's `loading` from
`comparableThesis.isLoading || comparablePeers.isLoading`; a query disabled because the comparable key does not resolve reports
`isLoading` true FOREVER in react-query, so the footer (`:403`) says *"the comparable bundles are still loading"* on a state that
never changes -- and in round 38 that transient's name made a grader decline to grade the evidence counts. Key it to a query
that is actually fetching (`fetchStatus === 'fetching'`, or `isFetching`), so a disabled or finished query never reads as
loading. (b) `portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx:63-67` labels the Bloomberg SESSION state
`BLOOMBERG: CONNECTED / SIGNED OUT / UNKNOWN` right beside the ticker, where "UNKNOWN" reads as an identity attribute. Relabel all
three so each names the session (e.g. `BLOOMBERG SESSION: CONNECTED`, `... SIGNED OUT`, `... NOT REPORTED`); icons and inks
unchanged.

## 2. BOUNDS

1. **No server.** You start no vite, dev build or listener (Andrew-direct: portal dev builds use port 5174 only, and that
   run is the issuer's). Your criteria are the files named below, run from the worktree root exactly as written.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-155-portal` at DEV `46c0ae11`. Python from
   the repo root with `PYTHONPATH="$(pwd)"`.
3. Standing: no install, no push, no promote, no S3 write, no vendor call. REFUSE, do not rescue.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~155/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ro-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-4.AC1.sh; echo "exit=$?"</invocation><expect>PostureTab comparable *.isLoading reads: 0; badge labels 'BLOOMBERG: ...': 0; labels naming the session: 3 or more -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ro-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/typecheck.sh; echo "exit=$?"</invocation><expect>tsc -b --noEmit exit=0 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~155/AMGT_RESAPP.TO-AMGT-ro-4.two-labels-that-misstate.proof_of_spec.json`. Report once: what you changed and where, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.7 items 4 and 6. Render grade: the issuer's real run on 5174.

<status>pending</status>
<round>40</round>
<slot>~155</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
