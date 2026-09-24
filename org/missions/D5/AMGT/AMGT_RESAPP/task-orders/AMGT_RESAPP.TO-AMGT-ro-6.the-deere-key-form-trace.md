# AMGT_RESAPP task order -- `AMGT-ro-6` -- THE DEERE KEY-FORM TRACE: why Peers prices Deere and Posture calls it UNRESOLVED -- measured, not fixed

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ro-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~157</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-39 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-ro-6` (round 40, decomposition s.48)

Row `AMGT_RESAPP-Z-S267`: the Peers tab renders Deere & Company (DE) as member one with a full priced row, while Posture
says *"Comparable: Deere & Company -- identity UNRESOLVED: the form 'DE_US_Equity' matches no persisted or measured identifier
form in crosswalk/v1 (as_of 2026-09-24, 254 records)"*. **Measure, edit nothing:** write
`KEYFORM_TRACE.md` in your deliverables with four sections -- `## 1. PEERS` (which key form the peers engine uses for a
member and where it comes from: `lib/research/peers/engine.py`), `## 2. POSTURE` (which form posture resolves the comparable
with and through which call: `lib/research/api/scoped_amgt.py`, `lib/research/posture/packs.py`), `## 3. CROSSWALK` (whether
any DE form exists in the current pool crosswalk, read from the builder in memory, never an S3 write; and what universe/v1
carries for DE), `## 4. THE RULE PROPOSED` (one paragraph: the smallest rule that makes both surfaces agree without guessing an
identity -- the CTO rules on it). Cite `file:line` for every claim.

## 2. BOUNDS

1. **No server.** You start no vite, dev build or listener (Andrew-direct: portal dev builds use port 5174 only, and that
   run is the issuer's). Your criteria are the files named below, run from the worktree root exactly as written.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-157-portal` at DEV `46c0ae11`. Python from
   the repo root with `PYTHONPATH="$(pwd)"`.
3. Standing: no install, no push, no promote, no S3 write, no vendor call. REFUSE, do not rescue.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~157/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ro-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-6.AC1.sh; echo "exit=$?"</invocation><expect>sections present: 4 of 4 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~157/AMGT_RESAPP.TO-AMGT-ro-6.the-deere-key-form-trace.proof_of_spec.json`. Report once: what you changed and where, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.7 item 7, measure-first: an identity rule is the CTO's (C-ONE-IDENTITY).

**ISSUER CLOSE, 2.0.0_SA_COO~Z, 2026-09-24 ~21:1xZ, carried on the worker's branch so the chain-end merge carries it.**
Checker's match: proof-of-spec-check VALID rc=0 (1 of 1). KEYFORM_TRACE.md: Peers prices members off the scanner database keyed by
bare ticker root and attaches identity as a separate field that never gates the row (engine.py:886-900); Posture's route boundary
is a hard gate through crosswalk/v1 then a landed model block (scoped_amgt.py:1784-1886); Deere has NO record under any form in
crosswalk, registrations or the 89-name universe, and no model block -- so the form mismatch is not what breaks this case, the
absence is. Proposed rule for the CTO: Posture's comparable link carries the member's already-computed identity verdict, and a
member with identity UNRESOLVED is never presented as a resolved comparable. No rows.

<status>complete</status>
<round>40</round>
<slot>~157</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
