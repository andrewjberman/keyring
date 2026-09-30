# AMGT_RESAPP task order -- `AMGT-ac-4` -- THE ADAPTER'S DOCSTRING STATES HARVEST.STORE IS PACKAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ac-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~192</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- text only; no AWS call.
comp-adversary: RUN by the issuer at the cut -- AC1 reads the normalised text AND a dynamic import probe; base FAIL (1 stale clause).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AMGT-ac-4` (round 53, decomposition s.61)

A docstring in `lib/research/api/scoped_amgt.py` (near `:2175`, in the reader of the filing-attempt UNRESOLVED-SOURCE marker) says:
"-- never `lib.research.harvest.store` (module-scope `import pyarrow`) and never `lib.opal_naming` (packaged, but not imported by this
adapter itself): the first is unavailable in the deployed package." The last clause is false: `lib/research/harvest/store.py` IS packaged
(the build's content diff lists it) and the /thesis path imports it (`corpus.dossier` -> `harvest.store`). **Correct that clause, text
only:** say what is true -- this reader does not import harvest.store (why, if the reason still holds), and harvest.store is packaged and
imported on the /thesis path. No code line changes; no other docstring.

## 2. BOUNDS

1. That one docstring's wording in `scoped_amgt.py`; the diff must touch no non-docstring line. Standing: no install, no push, no deploy.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~192/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ac-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round53/checks/ac_4_store.py; echo "exit=$?"</invocation><expect>claims that store is unavailable in the deployed package: 0; dynamic: True; THE ADAPTER'S TEXT STATES HARVEST.STORE IS PACKAGED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~192/AMGT_RESAPP.TO-AMGT-ac-4.the-store-docstring.proof_of_spec.json`. Report once: the lines changed, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-52 analysis item 4 (row Z-S315). Base: AC1 FAIL (1 clause; dynamic True). Rides ac-3's build.

<status>pending</status>
<round>53</round>
<slot>~192</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
