# AMGT_RESAPP task order -- `AMGT-am-7` -- THE STORED WRITE OF am-2's FROZEN MANAGEMENT OBJECTS (FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-am-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one stored write by hand.
comp-iam: RUN by the issuer at the cut -- 0 new function actions: the PUTs are made by the executor's own credentials on `opal-data-harvest` `management/v1/` keys, and the function's existing read of that prefix serves them.
BLIND: no IAM simulation was run for this act; AC1 reads the served management through the deployed function, so a denied read or a missed write shows as a FAIL there.
comp-adversary: RUN by the issuer at the cut -- r63_served c2 FAILS at the base on the deployed function (ASML_NA ABSENT/ZERO_OFFICERS; 6501_JP and 2317_TT NO_OBJECT).
EGRESS CLASS, declared: NONE. No vendor call.
</preflight>

## 1. THE ACT -- `AMGT-am-7` (round 63, decomposition s.71)

ONE act under ONE NEVER-2 entry and ONE never-widen pair. For each entry of the FROZEN plan
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~205/m1_fwd7_plan.json` (at the sha256 the halves name), PUT the
planned object file `.../0.9.0_WK_AMGT_RESAPP~205/m1_pool/<store_key>` to `s3://opal-data-harvest/<store_key>` (the bucket is versioned).
Before each PUT, confirm the local file's sha256 equals the plan entry's, and record whether the key existed. Write
`am7_store_writes.json` (key, existed, new VersionId) to your deliverables dir.

**Begin only when** the GO names the plan's sha256 and both halves are committed
(`deliverables/2.0.0_SA_COO~Z/round63/NEVER_WIDEN_HALF_COO_AM7.md`, `ledger/NEVER_WIDEN_ROUND63_AM7_CTO_HALF.md`).

ROLLBACK, per key: a key that did NOT exist before is removed only by Andrew's word (an S3 delete is a hard stop), so the
rollback for a NEW key is to PUT a superseding object the halves name. A key that existed is restored by copying its prior VersionId
back.

## 2. BOUNDS

1. The plan's keys only. No S3 delete, no vendor call, no push of shared branches.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-am-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c2 --where deployed; echo "exit=$?"</invocation><expect>C1 PASS (ASML_NA SERVED, BLOOMBERG_FALLBACK, officers > 0); C2 PASS for 6501_JP and 2317_TT (officers, or a stated reason); R63 C2 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-am-7.the-management-objects-write.proof_of_spec.json`.
Report once: each key written (existed or new, new VersionId) and AC1's output lines. Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-62 final addendum cell 2 (DSGN COMPLETION_GRADES.round26, FWD-7). Staged until am-2 drains, its plan
freezes and the pair is signed.

<status>staged</status>
<round>63</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
