# AMGT_RESAPP task order -- `AMGT-rr-1` -- THE FIVE NO-BLOCK NAMES: a Model block for AMD, GOOGL, LLY, PWR and UNH

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rr-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence moves; one scripted run.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant moves; the producer writes through the box's existing credentials.
comp-adversary: RUN by the issuer at the cut -- 2 of 2 acts carded in the COO half (2 served properties, 1 writer each); BLIND to the CTO half (not yet written) and to what the vendor returns, which the run prints per key.
EGRESS CLASS, declared: VENDOR -- Bloomberg reference/history/best calls through the Desktop API and the producer's own Seeking Alpha forecast fallback where it fires, under Andrew's STANDING grant R-21, SCRIPTED ONLY (model_block_pull.py makes every call; no agent composes one). S3: NEW stamps under the producer's raw and derived prefixes for five keys; nothing overwritten, nothing deleted.
</preflight>

## 1. THE CELL -- `AMGT-rr-1` (round 43, decomposition s.51)

**Begin only when both never-widen halves are committed:** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/NEVER_WIDEN_HALF_COO_RR1.md` and `1.0.0_SA_CTO~Z`'s.
**Land a Model block for each of the five names the LIVE research library holds beyond the 2026-09-10 snapshot** -- AMD, GOOGL, LLY,
PWR and UNH (`AMD US Equity`, `GOOGL US Equity`, `LLY US Equity`, `PWR US Equity`, `UNH US Equity`). Today none has a block, and
the print route refuses each (row `AMGT_RESAPP-Z-S280`). **The acts, in order, under ONE NEVER-2 entry opened AND COMMITTED before
the first pull:** (1) `bloomberg_health` reads `ok: true`, printed; (2) `PYTHONPATH="$(pwd)" python
integrations/bloomberg/research/model_block_pull.py pull --securities <up to three>` in two invocations (3 + 2), stopping at the
first non-zero rc; (3) `... model_block_pull.py derive --securities <the same>` in the same two batches, run at CLOUD HEAD at or after `025224c2cd` (the guarded base-case rule; the CTO half's condition) with `git rev-parse HEAD` printed beside each derived stamp; (4) verify with the two
criteria; close the entry. This is the SAME producer and the SAME invocation shape AMGT_CORPUS's round-4 pull used
(`org/critical_paths/change_management/20260925T0418Z_amgt-corpus-fwd12-round4-pull-derive-20260925_deploy_completion.md`).

## 2. BOUNDS

1. **Scripted only.** Every vendor call is made by `model_block_pull.py`; you compose none by hand (R-21's binding constraint).
   A key that comes back empty is printed and reported, never retried by hand.
2. The two acts and nothing else, under ONE NEVER-2 entry committed before the first pull and closed in the same session.
3. Standing: no S3 delete, no overwrite, no key hunting, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
org/critical_paths/change_management/**
org/critical_paths/.open_deploys/**
org/tier2_senior/0.7.0_AE_CloudOps~A/deliverables/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for a population sweep, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rr-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/checks/rr-1.AC1.py; echo "exit=$?"</invocation><expect>model blocks landed: 5 of 5 -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rr-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/checks/rr-1.AC2.py; echo "exit=$?"</invocation><expect>served pages with figures: 5 of 5 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-rr-1.the-five-no-block-names.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Amended at the CTO half's one condition (msg 25925, @c940964bea): act B binds a HEAD floor 025224c2cd; no criterion changed, so no gate limb grades this modification. s.7 item 1, first by the analysis's ruling. Seat order to the AE lane, which is live at the cut (process read) and holds only AMGT_RESAPP orders. Vendor authority: R-21 (standing, scripted), as ruled for AMGT_CORPUS's fire of 40.

<status>complete</status>
<round>43</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
