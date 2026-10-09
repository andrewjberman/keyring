# TO ADVI_COTBKF.TO-CB-ap-2.writer-registry-deploy -- round 42 CB-ap-2: deploy the cot price writer and its registry file, two keys, one pair

<to_id>ADVI_COTBKF.TO-CB-ap-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.7.0_AE_CloudOps~CB2</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>42</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ap-2` (`decompositions/ADVI_COTBKF_DECOMP.round42.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-ap-1, both pair halves

---

## WORKER FACE

### THE CELL

Round 42's `CB-ap-1` makes Cottonwood's price writer `data/cot/scripts/gold/build_canonical_prices_v2.py` resolve `source_firm` from
ONE registry file in its own directory, and removes a dead check. CB-ap-1's report (`writer_registry_local.md`) names that file, its
repo path, its blob id and its sha256.

The cot gold run syncs only `s3://opal-data-cot/code/gold/`. The deployed writer today is VersionId
`4M4XPMtc2JCbbWi22WuxrVIaicQqPzy6` (2026-06-12T20:07:45Z, 28,290 bytes), which predates `source_firm`.

**Your item. Do not start until this order's AMENDMENT names both pair halves and CB-ap-1's drained report.**
1. **Pair first.** The COO half by `2.0.0_SA_COO~C2` and the CTO half by `1.0.0_SA_CTO~DELL2`. Exactly TWO keys:
   - `code/gold/build_canonical_prices_v2.py` (a new version);
   - `code/gold/<registry file name>` (the registry blob pinned by CB-ap-1).
   Each names its prior VersionId (or `none` where it mints), its new sha256, and its rollback.
2. **Open the ledger** with `deploy_ledger.py open`.
3. **Census:** the deploy tool's key list printed FIRST holds exactly those two keys. Anything else means STOP.
4. **Writer:** `.tools/safe-deploy.sh data/cot/scripts/gold/build_canonical_prices_v2.py`.
5. **Registry file:** put the pinned blob at its `code/gold/` key by a single `put-object` of the exact bytes (`git cat-file -p
   <blob>`). Re-read each key's version just before its write.
6. **Read both back** and confirm the sha256 of each.
7. **Close the ledger.**
8. **The proof that closes D2-S62** is the next silver-prep census: `source_firm=cottonwood` on every row and `BREACH=0`. It is the
   issuer's post-deploy item, run on the next manual silver-prep under its own pair. It is not this order's act.

**AMENDMENT 1 (issuer, 2026-10-09 ~14:4xZ) -- the COO half is GIVEN. This order waits ONLY on the CTO half.**

- **COO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R42_WRITER_REGISTRY_DEPLOY_COO_HALF.md`.
- **CB-ap-1 drained** @7ae9de1d21. The registry file is `scopes.json`, git blob `261c0cf8adf46ade84fefd1144092c5665df7477`, and it
  goes to the key `code/gold/scopes.json`, which MINTS (head-object 404).
- **The writer's sha256 at HEAD** is `3ac0a502...7f6682`.
- **The registry bytes** are `git cat-file -p 261c0cf8adf46ade84fefd1144092c5665df7477`, sha256 `13947f7f...edeaade`.
- The order is released by AMENDMENT 2, citing the CTO half.

**AMENDMENT 2 (issuer, 2026-10-09 ~14:4xZ) -- RELEASED. Both halves exist; start now.**

- **CTO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R42_WRITER_REGISTRY_DEPLOY_CTO_HALF.md`
  @d92ed8390f (msg 3486). Its conditions REPLACE anything above that conflicts with them:
  1. **Rollback is the WRITER copy-back ONLY** (`?versionId=4M4XPMtc2JCbbWi22WuxrVIaicQqPzy6`).
     - `code/gold/scopes.json` is NEVER deleted, not even on refusal. Deleting it is Andrew's act.
     - The BOUNDS line "delete a key this act minted" is struck for this key.
  2. **The proof runs on the FETCHED SERVED files.**
     - Fetch both served keys and confirm each sha256: the writer `3ac0a502...7f6682`, `scopes.json` `13947f7f...edeaade`.
     - In a detached scratch worktree at HEAD, place the fetched writer at `data/cot/scripts/gold/build_canonical_prices_v2.py` and the
       fetched `scopes.json` where the test's fixture copies the registry from.
     - Run `python -m pytest data/cot/scripts/gold/tests/test_canonical_prices_source_firm.py -q` there. Record the line.
     - Remove the scratch worktree after.
- The issuer's post-drain items are not this order's acts:
  - the round-41 condition 4 becomes a `schwab/silver/rps/` reachability read (empty = unreachable) at this order's drain
    (ADDENDUM 15);
  - the stale-pin census line comes next issuance.

### ACCEPTANCE

<criterion id="CB42ap2-AC1" cell_refs="CB-ap-2"><invocation>python -m pytest data/cot/scripts/gold/tests/test_canonical_prices_source_firm.py -q</invocation><expect>passed</expect></criterion>
`CB42ap2-AC1` -- the source-firm tests pass on the bytes whose sha256 the two served keys were read back to equal. The ledger records
both read-back sha256 values beside this run.

<expected_criteria>CB42ap2-AC1</expected_criteria>

## BOUNDS

- **Grant.** Exactly the two `code/gold/` keys above (one new version each; prior versions kept), the ledger files, and this order's
  file.
- **Pair first.** No write before both halves exist and this order's amendment cites them.
- **Refusal clause.** If the key list holds anything else, or a version moved, or a read-back differs, stop. Restore any key written
  to its prior version (or delete a key this act minted), write the reason in the ledger, and file a NEW surprise row (id
  `ADVI_COTBKF-D2-WCB2-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your repo WRITE grant. The S3 grant is the two keys above.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round42.md</decomp_doc> (round 42), cell `CB-ap-2`.
<owned_cells>CB-ap-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB42ap2-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-ap-2.writer-registry-deploy.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB42ap2-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the pair files; the two-key census; the prior and new VersionIds; the read-back sha256 values; the pytest line; the ledger
entry.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- both keys are read by the cot gold run's code sync (gold_dispatch.sh:497-498); the writer runs only on a manual silver-prep (CB-aj-1 census: scheduled=0), so no scheduled output changes from this deploy.
comp-iam: RUN at apply time -- the dell2 identity's PutObject on two keys in opal-data-cot code/gold/; BLIND: none beyond them.
comp-adversary: RUN -- pair before write; a two-key census; version re-reads; sha256 read-backs; the registry put as exact blob bytes; BLIND: a manual silver-prep started mid-deploy (it would read one new and one old key; the ledger notes the window).
lane: SERVED write by the box applier via safe-deploy.sh plus one put-object; a lane refusal stops the order.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 14 @9a98e3b0a1 (msg 3442).
