# TO ADVI_COTBKF.TO-CB-ao-1.ff-worker-deploy -- round 41 CB-ao-1: deploy the cot gold carry-forward stamp under a never-widen pair

<to_id>ADVI_COTBKF.TO-CB-ao-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.7.0_AE_CloudOps~CB2</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>41</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ao-1` (`decompositions/ADVI_COTBKF_DECOMP.round41.md`) |
**outcome_ref:** FWD-3 | **depends_on:** both pair halves

---

## WORKER FACE

### THE CELL

Round 39 changed `_ff_worker` in `data/cot/scripts/gold/B_00.canonical_holdings.py` (+25/-1 lines, drained @88e7452955). Every
carried price now carries `price_basis`, `price_source_date` and `source_firm`, and a price whose `source_firm` is present and is not
Cottonwood is never carried. Its test is `data/cot/scripts/gold/tests/test_b00_ff_carry_claim.py`: 3 passed. The full suite is 31
passed.

The cot gold run syncs its scripts from `s3://opal-data-cot/code/gold/` (`gold_dispatch.sh`:497-498). The deployed
`code/gold/B_00.canonical_holdings.py`:
- is VersionId `BMqu7SNCbx2f3bQ_Tr56xMBCvtMe3van`, 65,249 bytes, sha256
  `6dbf6a86e734f514c92421e8e6ca9a9168bd8b6b90f742857f0f86d83c0d69a8`;
- is byte-identical to the repo file BEFORE round 39.

The file to deploy is the repo file at HEAD, sha256 `45fbbd921f026f9d4e30785e632c8f8e0feeb02730f033b96fd03b23da74c08d`.

**Your item (CTO ADDENDUM 13 @9326a48990).**
1. **Pair first.**
   - COO half: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R41_FF_WORKER_DEPLOY_COO_HALF.md`.
   - CTO half: signed by `1.0.0_SA_CTO~DELL2`, cited in this order's amendment.
   - Do not write before both exist.
2. **Open the ledger** with `deploy_ledger.py open`.
3. **Census the deploy.** Before the write, `diff` the deployed bytes (fetched at the prior VersionId) against the repo HEAD file, and
   print it. Every changed line must be inside `_ff_worker` (lines 1339-1395 at HEAD). Any other change means STOP. Print the diff's
   line counts.
4. **Write the file** with `.tools/safe-deploy.sh data/cot/scripts/gold/B_00.canonical_holdings.py`, which does cp, SHA verify and
   the pipescript confirm. Before the write, re-read the key's VersionId and STOP if it is not `BMqu7SNCbx2f3bQ_Tr56xMBCvtMe3van`.
   - If the tool refuses this lane (rule 13 names DS for `data/*/scripts/gold`), stop, write a row, and do not bypass.
5. **Proof.** Fetch the new served object. Its sha256 must equal `45fbbd92...d74c08d`. Then run
   `python -m pytest data/cot/scripts/gold/tests/test_b00_ff_carry_claim.py -q`, which drives the carry-forward on a synthetic day
   against those same bytes and reads the stamp.
6. **Close the ledger** with the prior and new VersionIds and the sha256 match.

**AMENDMENT 1 (issuer, 2026-10-09 ~14:1xZ) -- RELEASED. Both halves exist; start now.**

- **COO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R41_FF_WORKER_DEPLOY_COO_HALF.md` @3089cde892.
- **CTO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R41_FF_WORKER_DEPLOY_CTO_HALF.md` @9dd6703dd1
  (msg 3431). Its conditions are folded in:
  1. `safe-deploy.sh` prints its key list FIRST, and the list holds exactly one key (`code/gold/B_00.canonical_holdings.py`).
     Anything else means STOP.
  2. **The proof test imports the FETCHED SERVED file,** not the repo file.
     - Fetch the new served object to a scratch path, and confirm its sha256 equals `45fbbd92...d74c08d`.
     - In a detached scratch worktree at HEAD (`git worktree add --detach <scratch> HEAD`), place the fetched bytes at
       `data/cot/scripts/gold/B_00.canonical_holdings.py`.
     - Run `python -m pytest data/cot/scripts/gold/tests/test_b00_ff_carry_claim.py -q` THERE, and record the line in the ledger.
     - Remove the scratch worktree after. The shared tree is not edited.
  3. The next gold run's output fingerprint is read unchanged. That is the issuer's post-deploy watch item, not this order's act.

### ACCEPTANCE

<criterion id="CB41ao1-AC1" cell_refs="CB-ao-1"><invocation>python -m pytest data/cot/scripts/gold/tests/test_b00_ff_carry_claim.py -q</invocation><expect>passed</expect></criterion>
`CB41ao1-AC1` -- the stamp is proven on a synthetic day, on the bytes whose sha256 the served object was read back to equal. The ledger
records the read-back sha256 beside this run.

<expected_criteria>CB41ao1-AC1</expected_criteria>

## BOUNDS

- **Grant.** Exactly one S3 key, `opal-data-cot` `code/gold/B_00.canonical_holdings.py` (one new version; the prior is kept), plus the
  ledger files and this order's file. No other write.
- **Pair first.** No write before both halves exist and this order's amendment cites them.
- **Refusal clause.** If the census shows a change outside `_ff_worker`, or the version moved, or a read-back differs, stop. Restore
  the prior version by `copy-object` if anything was written, write the reason in the ledger, and file a NEW surprise row (id
  `ADVI_COTBKF-D2-WCB2-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your repo WRITE grant. The S3 grant is the one key above.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round41.md</decomp_doc> (round 41), cell `CB-ao-1`.
<owned_cells>CB-ao-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB41ao1-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-ao-1.ff-worker-deploy.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB41ao1-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the pair files; the census diff (line counts, all inside `_ff_worker`); the prior and new VersionIds; the read-back
sha256; the pytest line; the ledger entry.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the key is read by the cot gold run's code sync (gold_dispatch.sh:497-498); _ff_worker is reached only when schwab/silver/rps/ holds data (empty today, CTO-measured), so no scheduled fire changes output from this deploy.
comp-iam: RUN at apply time -- the dell2 identity's PutObject on one key in opal-data-cot code/gold/; BLIND: none beyond it.
comp-adversary: RUN -- pair before write; census limited to _ff_worker; version re-read; sha256 read-back; proof on the same bytes; BLIND: a gold run started between the write and the proof (it would run the stamped code, the intended state).
lane: SERVED write by the box applier via safe-deploy.sh; a lane refusal stops the order.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 13 @9326a48990 (msg 3423).
