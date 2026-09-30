# AMGT_RESAPP task order -- `AMGT-ab-2` -- EVERY NAME SERVES ITS DOSSIER BLOCK, EACH FIELD WITH ITS REASON, AND `pack_shape` PASSES THROUGH

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ab-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~188</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change and no new read surface: the dossier read this order extends already runs on /thesis (read_dossier).
comp-adversary: RUN by the issuer at the cut -- AC1/AC2 go through the route handler in process (never a component with a handed input); base FAIL on both.
EGRESS CLASS, declared: NONE. Opal's own S3, read-only.
</preflight>

## 1. THE CELL -- `AMGT-ab-2` (round 52, decomposition s.60)

`/thesis` serves `dossier_fields`, built by `lib/research/api/scoped_amgt.py` `_dossier_fields(dossier_read)` from
`lib.research.corpus.dossier.read_dossier(key)["document"]["fields"]`. Two gaps (AMGT_CORPUS round-20 rulings 2-3, row Z-W2-S15):

1. **A name with no dossier** (6501_JP_Equity: `read_dossier` raises LookupError, "no research_dossier object under
   s3://opal-data-harvest/amgt/harvest/gold/research_dossier/security_key=6501_JP_Equity/") serves only
   `{"status": "READ_FAILED", "reason": ...}`, so the page cannot say why each field is empty. **Build:** when the dossier does not
   exist, serve the SAME block shape as for a name with a dossier: `thesis_pillars: []`, `thesis_pillars_absent` {status ABSENT,
   reason}, and each of `management`, `fund_of_record`, `last_stated_position`, `pack_shape` as {status: "ABSENT", value: null,
   reason: <why -- e.g. no research dossier exists for this name>}. A read that FAILS for another reason (S3 error, bad JSON) stays
   `READ_FAILED` -- a missing dossier and a broken read are different things and must stay distinguishable.
2. **`pack_shape` is not passed through.** The `/5` dossiers hold `fields.pack_shape` as {value: "pdf"|"docx"|"mixed", basis: [bronze
   keys]} or {value: null, absent: <reason>, basis: []} (measured: AZN_LN_Equity pdf, ADBE_US_Equity pdf, AMD_US_Equity absent).
   **Build:** serve it like the other scalars -- {status: "SERVED", value, basis} or {status: "ABSENT", value: null, reason: <the
   dossier's absent text>}; a dossier without the field (an older method version) reads ABSENT with a reason saying so.

Nothing else in /thesis moves. Tests for each branch.

## 2. BOUNDS

1. `scoped_amgt.py` and the api tests only. No route added (payload fields only). Standing: no install, no push, no promote, no deploy,
   no vendor call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~188/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ab-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round52/checks/ab_2_dossier.py --plane local --what absent; echo "exit=$?"</invocation><expect>plane local: A NAME WITH NO DOSSIER SERVES EVERY FIELD ABSENT WITH ITS REASON: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ab-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round52/checks/ab_2_dossier.py --plane local --what shape; echo "exit=$?"</invocation><expect>AZN/ADBE pack_shape SERVED pdf with basis, AMD ABSENT with the dossier's reason; plane local: PACK_SHAPE PASSES THROUGH FROM THE DOSSIER: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ab-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/api-suite.sh; echo "exit=$?"</invocation><expect>pytest reports N passed and 0 failed (plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~188/AMGT_RESAPP.TO-AMGT-ab-2.every-name-serves-its-dossier-block.proof_of_spec.json`. Report once: what 6501's block reads now, the pack_shape shapes served, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-51 analysis item 2 (CORPUS r20 rulings 2-3). Base: AC1 FAIL (READ_FAILED), AC2 FAIL (no pack_shape), AC3 PASS.
Served in ab-6. The read preference to `/5` rides ab-6's closure (dossier.py METHOD_VERSION `/5` at HEAD, `/4` deployed).

<status>complete</status>
<round>52</round>
<slot>~188</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
