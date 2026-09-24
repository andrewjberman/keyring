# AMGT_RESAPP task order -- `AMGT-ro-5` -- POSTURE'S REASON WITHOUT A PATH: an absence a user reads carries no repository path

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ro-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~156</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-39 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-ro-5` (round 40, decomposition s.48)

`lib/research/posture/packs.py:67` builds the absent-model-block reason as
`"ABSENT %s (no model block landed for this name)" % os.path.relpath(path, _REPO_ROOT)`, so the Posture tab prints
`org\missions\D5\AMGT\AMGT_RESAPP\deliverables\0.9.0_WK_AMGT_RESAPP~1\model_block_DE_US_Equity.json` to the user, twice.
**Build:** the reason a user reads is `ABSENT (no model block landed for this name)` -- no path, no separator; where the path
matters to an operator it rides a separate field the object already has or gains, never the reason text. Tests in
`lib/research/posture/tests/`. The served posture objects written before this change still carry the old text until the next
posture run; that run is not this cell's.

## 2. BOUNDS

1. **No server.** You start no vite, dev build or listener (Andrew-direct: portal dev builds use port 5174 only, and that
   run is the issuer's). Your criteria are the files named below, run from the worktree root exactly as written.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-156-portal` at DEV `46c0ae11`. Python from
   the repo root with `PYTHONPATH="$(pwd)"`.
3. Standing: no install, no push, no promote, no S3 write, no vendor call. REFUSE, do not rescue.

## 3. SURFACES

<paths>
lib/research/posture/packs.py
lib/research/posture/tests/**
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~156/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ro-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-5.AC1.py; echo "exit=$?"</invocation><expect>block=None reason='ABSENT ...' path-tokens=none -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ro-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-5.AC2.sh; echo "exit=$?"</invocation><expect>the posture package's tests pass (N passed, 0 failed) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~156/AMGT_RESAPP.TO-AMGT-ro-5.posture-reason-without-a-path.proof_of_spec.json`. Report once: what you changed and where, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.7 item 5.

<status>complete</status>
<round>40</round>
<slot>~156</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
