# TO ADVI_COTBKF.TO-CB-ah-3.fwd3-as-traded-remint -- round 34 CB-ah-3: re-mint the three FWD-3 tables at the as-traded build, under a never-widen pair

<to_id>ADVI_COTBKF.TO-CB-ah-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.7.0_AE_CloudOps~CB2</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>34</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ah-3` (`decompositions/ADVI_COTBKF_DECOMP.round34.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-ah-1, CB-ah-2, both halves of the pair

---

## WORKER FACE

### THE CELL

ADVI_COTBKF's FWD-3 tables are served at three keys, minted @476f970245 (round 29, your CB-ac-1). There are 0 readers, and the CTO's
reader gate stands: no grant until this rebuild is graded.

`s3://opal-data-assets/commonwealth/cottonwood/silver/{daily_returns,account_day_value,month_grades}/date=2026-06-23/part-00000.parquet`

They were built on a price store that is dividend-adjusted for 2,079 tickers. CTO ADDENDUM 8 rules valuation at the AS-TRADED close,
and ADDENDUM 9 cuts this rebuild. Round 34's `CB-ah-2` adds the as-traded basis to the chain and builds the tables locally at
`.scratch/advi_cotbkf/fwd3_serve_r34` with `commonwealth_fwd3_serve.py` (`--build`, `--dry-run`, `--apply`, `--verify`).

**Your item. Do not start until this order's AMENDMENT names both pair halves and the build to apply.**

1. **Before any write:** the never-widen pair is signed.
   - The COO half is signed by `2.0.0_SA_COO~C2` and the CTO half by `1.0.0_SA_CTO~DELL2`.
   - Each names the blast radius: exactly the three keys above, overwritten.
   - Each names the rollback per key: the current object versions, which you record by ETag and VersionId before the write.
2. **Open the change-management ledger** with `deploy_ledger.py open`. The fix @00d3393ff3 is in dell2 HEAD, so `open` commits its own
   files.
3. **From the drained trunk,** re-run the build exactly as the amendment states, then `--dry-run`.
   - The three addresses, row counts and hashes must equal the pair's, or stop.
   - The `--hold-cusips` list is the one the amendment states, which comes from `CB-ah-1`'s class.
4. **Run `--apply`, then `--verify`,** and close the ledger with the read-back.

**AMENDMENT 1 (issuer, 2026-10-09 ~12:3xZ) -- RELEASED. Both halves exist; start now.**

- **COO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R34_FWD3_ASTRADED_REMINT_COO_HALF.md`,
  GIVEN @e075588a6c.
- **CTO half:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R34_FWD3_ASTRADED_REMINT_CTO_HALF.md`, GIVEN
  (msg 3271).
- **The build to apply is the issuer's local build `.scratch/advi_cotbkf/fwd3_serve_r34_hold/`, AS BUILT.**
  - It was built at `run_commit=6f70d5cc01bb`, with `--hold-cusips 05613L3H2,95000U2D4,651639AX4`.
  - Do NOT run `--build`. Step 3 above is replaced by
    `commonwealth_fwd3_serve.py --dry-run --data-dir .scratch/advi_cotbkf/r34 --out .scratch/advi_cotbkf/fwd3_serve_r34_hold`.
  - The three printed hashes must equal the COO half's:
    - `fa1c1303fd969ec59de423f63d5d84d2d9b7b0d2a5d1514f206ff1df02a8dede` (daily_returns);
    - `a94d3acce066e98d8d3fdad69c8e16f19d874df9192010ddf844b3c43103b6e8` (account_day_value);
    - `66ea11a4434ae63d47246f980b216df2759edc4766427b31d8a2bfcc7a1d4ec0` (month_grades);
  - It must also print `absent_months=5`. Otherwise stop.
  - Then run `--apply` and `--verify` with the same `--data-dir` and `--out`.
- **The CTO half's conditions:**
  - Re-read the 3 prior VersionIds immediately before the write, and STOP if any changed. They are:
    - `rIUTpGUAPNG.rsDWrxpRbnJCmu6NFaXJ`
    - `PcSspTWz8xsreGMTF_coYhbqifk4preA`
    - `Y15sJCiA1KM.CksHSitFlsnqkI56N_34`
  - Apply as built, with the hashes printed.
  - The reader gate stays closed. Grant nothing.
  - The 5 ABSENT months are rows D2-S53..S57, already filed.
  - The ledger is pinned and opened with `deploy_ledger.py open`, which commits its own files.
- **The acceptance invocation becomes** the `--verify` with `--out .scratch/advi_cotbkf/fwd3_serve_r34_hold` (below). The bar is
  unchanged.

### ACCEPTANCE

<criterion id="CB34ah3-AC1" cell_refs="CB-ah-3"><invocation>python data/assets/scripts/silver/commonwealth_fwd3_serve.py --verify --data-dir .scratch/advi_cotbkf/r34 --out .scratch/advi_cotbkf/fwd3_serve_r34_hold</invocation><expect>match=True</expect></criterion>
`CB34ah3-AC1` -- the three served tables read back equal to the as-traded local build.

<expected_criteria>CB34ah3-AC1</expected_criteria>

## BOUNDS

- **Grant.** Exactly the three S3 keys above (overwrite), the ledger files for this deploy, and this order's file. No other write.
- **Pair first.** No write before both halves exist and this order's amendment cites them.
- **Refusal clause.** If a criterion cannot be met as written, stop. Restore each key to its recorded prior version, write the reason in
  the ledger, and file a NEW surprise row (id `ADVI_COTBKF-D2-WCB2-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your repo WRITE grant. The S3 grant is the three keys above.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round34.md</decomp_doc> (round 34), cell `CB-ah-3`.
<owned_cells>CB-ah-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB34ah3-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-ah-3.fwd3-as-traded-remint.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB34ah3-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the pair files; the prior versions (ETag and VersionId per key); the ledger entry; the dry-run and verify lines; the new
ETags.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time re-mint of three keys.
comp-iam: RUN at apply time -- the dell2 identity's write on the three keys under opal-data-assets; BLIND: none beyond the three keys.
comp-adversary: RUN -- pair before write; prior versions recorded for rollback; dry-run addresses, rows and hashes equal to the pair's; read-back equality; BLIND: a downstream reader (none; the CTO's reader gate).
lane: SERVED write by the box applier; the issuer signs the COO half on CB-ah-2's build.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 9 @cf58046f35 (msg 3180); row D2-S50.
