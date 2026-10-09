# TO ADVI_COTBKF.TO-CB-aj-2.cot-price-rewrite-apply -- round 36 CB-aj-2: write the 38 rewritten cot price files as new versions, under a never-widen pair

<to_id>ADVI_COTBKF.TO-CB-aj-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.7.0_AE_CloudOps~CB2</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>36</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-aj-2` (`decompositions/ADVI_COTBKF_DECOMP.round36.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-aj-1, both pair halves

---

## WORKER FACE

### THE CELL

Round 36's `CB-aj-1` builds 38 rewritten Cottonwood price files locally under `.scratch/advi_cotbkf/cot_price_rewrite/`, with a manifest
`cot_price_rewrite_manifest.json` (per key: version_before, sha256_after, rows, removed, repriced). The 49 Financial rows are removed and
the three bonds are re-priced from Yahoo or left unpriced.

The live keys are in `opal-data-cot` under `silver/prices/`. The bucket is versioned. CTO ADDENDUM 10 rules that the rewrite lands as
new versions under a never-widen pair, and that the old versions are NOT deleted. Deleting them is Andrew's act.

**Your item. Do not start until this order's AMENDMENT names both pair halves and CB-aj-1's drained manifest.**

1. **Pair first.** The COO half is signed by `2.0.0_SA_COO~C2` and the CTO half by `1.0.0_SA_CTO~DELL2`, naming:
   - exactly the 38 keys;
   - each key's prior VersionId;
   - each key's new sha256;
   - the rollback per key: `copy-object` of the prior VersionId.
2. **Open the ledger** with `deploy_ledger.py open`; it commits its own files.
3. **For each of the 38 keys:**
   - re-read the current VersionId, and stop if it differs from the pair's;
   - `put-object` the local file;
   - record the new VersionId;
   - read the object back and confirm its sha256 equals the manifest's.
4. **Close the ledger** with the per-key table: prior VersionId, new VersionId, sha256 match.

### ACCEPTANCE

<criterion id="CB36aj2-AC1" cell_refs="CB-aj-2"><invocation>python data/assets/scripts/silver/commonwealth_cot_price_rewrite.py --verify-served --out .scratch/advi_cotbkf/cot_price_rewrite_verify</invocation><expect>COT-PRICE-REWRITE-VERIFY keys=38</expect></criterion>
`CB36aj2-AC1` -- every one of the 38 served keys reads back equal to its rewritten local file. The `--verify-served` mode is added by
CB-aj-1, or by the amendment that releases this order.

<expected_criteria>CB36aj2-AC1</expected_criteria>

## BOUNDS

- **Grant.** Exactly the 38 keys (one new version each), the ledger files for this deploy, and this order's file. No delete of any
  version.
- **Pair first.** No write before both halves exist and this order's amendment cites them.
- **Refusal clause.** If a key's version moved, or a read-back differs, stop. Restore every key written so far to its prior version by
  `copy-object`, write the reason in the ledger, and file a NEW surprise row (id `ADVI_COTBKF-D2-WCB2-S<k>`, `"fabric": "dell2"`). Do
  not weaken the test.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your repo WRITE grant. The S3 grant is the 38 keys above.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round36.md</decomp_doc> (round 36), cell `CB-aj-2`.
<owned_cells>CB-aj-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB36aj2-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-aj-2.cot-price-rewrite-apply.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB36aj2-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the pair files; the ledger entry; the per-key prior and new VersionIds with sha256 matches; the verify line.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at apply time -- re-read CB-aj-1's writer census; a scheduled writer enabled since then stops the apply.
comp-iam: RUN at apply time -- the dell2 identity's PutObject on the 38 keys in opal-data-cot; BLIND: none beyond the 38 keys.
comp-adversary: RUN -- pair before write; per-key version re-read; sha256 read-back; old versions kept (no delete); BLIND: a reader pinned to an old VersionId (none known).
lane: SERVED write by the box applier; the issuer signs the COO half on CB-aj-1's manifest.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 10 (msg 3266); row D2-S52.
