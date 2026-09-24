# AMGT_RESAPP task order -- `AMGT-rn-1` -- THE SIZE-10 RESIDUE: FWD-29's own "no size below 11", closed at its two sites

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rn-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~146</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-38 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-rn-1` (round 39, decomposition s.47)

`FWD-29`'s DONE WHEN (PRD ADDENDUM B fence :729-735) says "no size below 11". The round-38 baseline reads `sizes FAIL [10]` on the
thesis and model states, attributed by rm-3 to ONE rendering: `PanelHeader.tsx:99` passes `className="text-[10px]"` to
`DataTimestamp`, whose own root carries `text-xs` (`DataTimestamp.tsx:38`). **Build:** the timestamp renders at 11px or larger in
every PanelHeader that passes one (the two callers are the thesis and model panels), with no `text-[10px]`/`text-[9px]` token in
either file. Prefer `text-[11px]` on the caller if 12px (`text-xs`) crowds the strip; say which in the report. Change nothing else
in either file: no weight, radius, colour, spacing or prop.

## 2. BOUNDS

1. **No server.** You run no vite; the render is graded by the issuer after the merge. Your criteria are the two files below.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-146-portal` at DEV `5e339ffd`.
3. Standing: no install, no push, no promote. REFUSE, do not rescue.

## 3. SURFACES

<paths>
portal/src/ui/components/panels/PanelHeader.tsx
portal/src/components/DataTimestamp.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~146/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rn-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-1.AC1.sh; echo "exit=$?"</invocation><expect>files with size=0: 2 of 2; text-[9px|10px] tokens across both: 0 -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rn-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/typecheck.sh; echo "exit=$?"</invocation><expect>tsc -b --noEmit exit=0 -- and exit=0 (the seam probe: every consumer of the two components still compiles)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~146/AMGT_RESAPP.TO-AMGT-rn-1.the-size-10-residue.proof_of_spec.json`.
Report names the token chosen, the two commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.7 item 1. Render grade: the issuer's `checks/drain.real-run.sh` on 5174 after the merge (sizes PASS 6 of 6).

<status>pending</status>
<round>39</round>
<slot>~146</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
