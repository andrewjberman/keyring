# TO ADVI_COTBKF.TO-CB-aa-4.fwd3-serve-apply -- round 27 CB-aa-4: the SERVED write of the FWD-3 tables, under a pair, read back

<to_id>ADVI_COTBKF.TO-CB-aa-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.7.0_AE_CloudOps~CB2</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-aa-4` (`decompositions/ADVI_COTBKF_DECOMP.round27.md`) |
**outcome_ref:** FWD-3 | **depends_on:** `CB-aa-3`

---

## WORKER FACE

### THE CELL

ADVI_COTBKF builds Cottonwood's daily returns (FWD-3). CB-aa-3 delivers `data/assets/scripts/silver/commonwealth_fwd3_serve.py`, whose
`--build` writes three local parquet tables (`daily_returns`, `account_day_value`, `month_grades`), `--dry-run` prints their target
addresses from `lib/opal_naming.address` with row counts and content hashes, `--apply` writes them, and `--verify` reads them back and
compares. The targets are three NEW keys under `s3://opal-data-assets/commonwealth/cottonwood/silver/` (`daily_returns/`,
`account_day_value/`, `month_grades/`, each `date=2026-06-23/`); nothing exists at them today, so the write mints, it does not move
served output.

**Your item.** Apply it, the customary way for a dell2 deploy (Andrew ~22:0xZ, MSTR msg 1751), as the fresh lane `0.7.0_AE_CloudOps~CB2` (MSTR msg 2264; one project per Tier-2 seat instance):
1. **Before any write:** the never-widen pair is signed -- the COO half by `2.0.0_SA_COO~C2` and the CTO half by `1.0.0_SA_CTO~DELL2`,
   each naming the blast radius (exactly the three keys above; rollback = delete those three keys). The pair files are cited in this
   order's amendment when signed; do not write before both exist.
2. Open the change-management ledger entry in `org/critical_paths/change_management/` (and `.open_deploys/`), per CLAUDE.md NEVER-2.
3. From the drained trunk: run `--build` then `--dry-run`; the dry run's three addresses must equal the pair's three keys, else stop.
4. Run `--apply`, then `--verify`. Close the ledger with the read-back.

### ACCEPTANCE

<criterion id="CB27aa4-AC1" cell_refs="CB-aa-4"><invocation>python data/assets/scripts/silver/commonwealth_fwd3_serve.py --verify --data-dir .scratch/advi_cotbkf/r27 --out .scratch/advi_cotbkf/fwd3_serve</invocation><expect>match=True</expect></criterion>
`CB27aa4-AC1` -- the three served tables read back equal to the local build.

<expected_criteria>CB27aa4-AC1</expected_criteria>

## BOUNDS

- **Grant.** Exactly the three S3 keys above, the ledger files for this deploy, and this order's file. No other write.
- **Pair first.** No write before both halves of the never-widen pair exist; the dry run's addresses must equal the pair's keys.
- **Refusal clause.** If a criterion cannot be met as written, stop, roll back what was written (delete the keys this act minted), write
  the reason in the ledger and a NEW surprise row (id `ADVI_COTBKF-D2-W53-S<k>`, `"fabric": "dell2"`), and do not weaken the test.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your repo WRITE grant; the S3 grant is the three keys above.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round27.md</decomp_doc> (round 27), cell `CB-aa-4`.
<owned_cells>CB-aa-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB27aa4-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-aa-4.fwd3-serve-apply.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB27aa4-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the pair files, the ledger entry, the dry-run and verify lines, the three keys with their ETags.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time mint of three keys; no schedule (a scheduled refresh is a later item).
comp-iam: RUN at apply time -- the dell2 identity's write on the three keys under opal-data-assets; BLIND: none beyond the three keys.
comp-adversary: RUN -- pair before write; addresses from the builder and equal to the pair's keys; read-back equality; BLIND: a downstream reader (none yet).
lane: SERVED write by the box applier (Andrew ~22:0xZ); the issuer signs the COO half.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 2 (msgs 2213, 2257), E3; MSTR msg 1751 (dell2 applier).
