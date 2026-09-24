# AMGT_RESAPP task order -- `AMGT-ro-2` -- THE P/E GUARD: a reciprocal column with no stated unit renders ABSENT, never the raw yield under a P/E label

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ro-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~153</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-39 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-ro-2` (round 40, decomposition s.48)

Round 39's rn-2 made `portal/src/pages/SecurityAnalysis/cscTable.ts` `valueOf` apply the map entry's `transform`/`units`,
and fall through to `return value` when the entry states none. Every served peers/v1 object was written before rn-2 and
states none, so the fixed page would render the raw earnings yield (DE 2.88) under "P/E (trailing)". And
`__harness__/peersCarry.harness.cjs` now exits 1: its own fixture's P/E entries carry no `transform`/`units` (fraction yields
0.05/0.04 read raw where 20/25 are asserted). **Build:** (1) in `valueOf`, a column whose map entry's `relation` begins
`RECIPROCAL` (the `reason` field on the built column) and which states no `transform`, or no `units` in {percent, fraction},
returns `null` -- ABSENT, never a number; every other column unchanged; (2) `peersCarry.harness.cjs`'s fixture entries for
`ey`/`ey_ntm` gain `transform: 'reciprocal'` and `units: 'fraction'` (its yields ARE fractions), and its assertions stand.

## 2. BOUNDS

1. **No server.** You start no vite, dev build or listener (Andrew-direct: portal dev builds use port 5174 only, and that
   run is the issuer's). Your criteria are the files named below, run from the worktree root exactly as written.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-153-portal` at DEV `46c0ae11`. Python from
   the repo root with `PYTHONPATH="$(pwd)"`.
3. Standing: no install, no push, no promote, no S3 write, no vendor call. REFUSE, do not rescue.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/cscTable.ts
portal/src/pages/SecurityAnalysis/__harness__/peersCarry.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~153/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ro-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-2.AC1.sh; echo "exit=$?"</invocation><expect>peersCarry exit=0 -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ro-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-2.AC2.cjs; echo "exit=$?"</invocation><expect>THE GUARD: entries stripped: 2; P/E cells with no stated unit: 24 absent, 0 numeric -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ro-2"><invocation>cd "$(git rev-parse --show-toplevel)/portal" &amp;&amp; node ../org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/pe-relation.cjs; echo "exit=$?"</invocation><expect>THE RELATION (bound): P/E x percent yield == 100 (+/-1): 24 of 24; off-relation 0; null 0 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~153/AMGT_RESAPP.TO-AMGT-ro-2.the-pe-guard.proof_of_spec.json`. Report once: what you changed and where, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Found at the cut (s.48b.1-2). The relation check replaces round 39's magnitude band, which a raw percent yield passes.

<status>pending</status>
<round>40</round>
<slot>~153</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
