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
  <criterion id="AC1" cell_refs="AMGT-am-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c2 --where deployed; echo "exit=$?"</invocation><expect>C2 PASS for 6501_JP and 2317_TT (officers, or a stated reason); C1 (ASML_NA) is HELD on Andrew's per-use vendor word (row AMGT_RESAPP-Z-W205-S1) and reads FAIL ABSENT until a pull lands, so R63 C2 SERVED: NO and exit=1 come from C1 alone</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-am-7.the-management-objects-write.proof_of_spec.json`.
Report once: each key written (existed or new, new VersionId) and AC1's output lines. Stamp any row's `surfaced_at` with `date -u`.

## 6. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~15:5xZ) -- also the two rebuilt peers objects (am-8, Z-W4-S6)

In the same act, under the same entry and pair (re-signed to include them), PUT each entry of the FROZEN plan
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~209/peers_slash_plan.json` (at the sha256 the halves name) from
`.../0.9.0_WK_AMGT_RESAPP~209/peers_pool/<store_key>` to `s3://opal-data-harvest/<store_key>`. These are new keys, with the same
per-key sha256 check and record. Grade them with
`r63_served.py --cell c6 --where deployed --plan <that plan>` (C1: every planned served field reads its `after`). It runs beside AC1
and is reported; the issuer re-reads it.

## 7. AMENDMENT 2 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~16:1xZ) -- the management write is two keys, not three

Of `m1_fwd7_plan.json` (sha256 `598950e3150bae6f975a5f47c56bb38657c354418f07706842a60b3d54a3a595`), PUT the entries for `6501_JP_Equity` and `2317_TT_Equity` only. The `ASML_NA_Equity` entry
is NOT written: no officer pull exists for it (row AMGT_RESAPP-Z-W205-S1, held on Andrew's per-use vendor word), so its planned
object would swap one ABSENT read for another. AC1's expectation is amended to match (C2 PASS, C1 HELD). The peers plan
(AMENDMENT 1) is unchanged at sha256 `ccb09b8ab20a7caff35bdf19970444b423da5d5b9dbe302a17002a8b969fec22`. Gate limb that graded this modification: none (LIMB 6 fires only on a newly-added order;
GATE (viii) does not apply).

## 8. AMENDMENT 3 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~19:2xZ) -- the three officer objects from the Bloomberg pull

am-2 AMENDMENT 2 (drained `af6184d5b0`) made the ONE Bloomberg pull on Andrew's per-use word and rebuilt the plan:
`.../0.9.0_WK_AMGT_RESAPP~205/m1_fwd7_plan_a2.json`, sha256 `ca25158b678666379b862074eb173e8b05e7c5ecea3e95641de9a27bcb908557`.
Under ONE NEVER-2 entry and the pair named in its GO (`deliverables/2.0.0_SA_COO~Z/round63/NEVER_WIDEN_HALF_COO_AM7_A3.md` plus
`ledger/NEVER_WIDEN_ROUND63_AM7_A3_CTO_HALF.md`), PUT each of its 3 entries from `.../0.9.0_WK_AMGT_RESAPP~205/m1_pool_a2/<store_key>` to
`s3://opal-data-harvest/<store_key>`. The keys are `management/v1/{ASML_NA,6501_JP,2317_TT}_Equity/2026-10-02T1840Z.json`, all NEW.
Check sha256 before each PUT and run head-object after. AC1's expectation for this amendment is the original one: C1 PASS (ASML_NA
SERVED, BLOOMBERG_FALLBACK, officers > 0), C2 PASS for both; R63 C2 SERVED: YES; exit=0. Gate limb that graded this modification:
none (LIMB 6 fires only on a newly-added order; GATE (viii) does not apply).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-62 final addendum cell 2 (DSGN COMPLETION_GRADES.round26, FWD-7). Staged until am-2 drains, its plan
freezes and the pair is signed.

<status>staged</status>
<round>63</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<status>complete</status>

**ISSUER GRADE (2.0.0_SA_COO~Z, 2026-10-02 ~18:3xZ):** ACCEPTED as amended. AE~A `eb079d1e36`, 4 new keys, 0 overwrites
(VersionIds: 6501_JP `IhgGo4SLO2eh.LLG7COpr_XiSUBHvapU`, 2317_TT `3M7mBXYbQskxBUsVouH1NWU2PzCCnj5F`, BP `JnY3RSuWrNJPpP1Fkpzw0Ve9LQnxNyMo`,
NG `M.lsmArE9oWTLmtf_KRJxNP44XwZWLUG`). Re-read by the issuer on deployed: c2 C2 PASS for 6501_JP and 2317_TT (each its own reason), C1
(ASML_NA) HELD; c6 YES 52 of 52 (base 0 of 52). am-2 AMENDMENT 2 (the Bloomberg pull on Andrew's word) is in flight; its rebuilt plan
reopens this order under AMENDMENT 3 and a re-signed pair.

**ISSUER REOPEN (2.0.0_SA_COO~Z, 2026-10-02 ~19:2xZ):** AMENDMENT 3.

<status>staged</status>
