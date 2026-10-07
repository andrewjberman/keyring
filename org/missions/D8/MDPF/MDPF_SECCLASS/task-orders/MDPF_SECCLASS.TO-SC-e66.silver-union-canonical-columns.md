# TO MDPF_SECCLASS.TO-SC-e66 -- round 11 SC-e-66: W41-S4: the BD silver assets dim's scheduled union path writes the canonical class columns

<to_id>MDPF_SECCLASS.TO-SC-e66</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~55</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-66` (`decompositions/MDPF_SECCLASS_DECOMP_R11.md`) |
**outcome_ref:** FWD-1, FWD-2 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-66`. CTO round-10 analysis ruling 2.4: "The silver_dim FAIL (W41-S4) is a round-11 cell: off the page chain, but a served defect."

**Row W41-S4, measured:**
- The live `silver/bd_assets_dim.parquet` in opal-data-bd (nightly 22:11Z) has no `asset_class_canonical`, `sub_asset_class_canonical`
  or `class_source` column, and reads PHYS equity, GLD and VXX alternatives.
- The deployed `code/silver/build_bd_assets_dim.py` equals the repo file, and that file adds the columns on the full-rebuild path.
- The scheduled path is `--union-bronze` (SSM `infra/aws/ssm/opal-bd-asset-dim-download.json:114`). It runs `build_union_dim()` in
  `data/black_diamond/scripts/silver/build_bd_assets_dim.py` (~:340-372), which blends only ADDED rows and ends with
  `assert len(out.columns) == len(dim.columns), 'the union changed the column set'`, so the columns can never land.
- No gold or platinum class read uses these columns (B_01 reads `cusip` only).

**Build:**
1. In `build_union_dim()`, compute the three canonical columns for EVERY row of the union output. Use the same code the full-rebuild
   path uses to add them (read it in the same file and reuse its function; do not write a second classifier).
2. Replace the frozen column-set assert with one that admits exactly the three columns as the only additions.
3. Every other column's values must stay byte-for-byte what the union produced before. The existing rule "blend ONLY the added rows"
   is unchanged.
4. Write `data/black_diamond/scripts/silver/tests/test_assets_dim_union_canonical.py` on a small fixture (a current dim without the
   columns, plus a pull). It asserts:
   - the three columns are present on every row, with GLD and PHYS commodities/Metals and VXX structured/Hedge from a fixture
     canonical lookup;
   - every pre-existing column is unchanged for the kept rows;
   - the difference control: a row the canonical lookup lacks reads absent (no value invented).
5. Write the half request `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SILVER_UNION_CANONICAL_20261007.md`.
   Shape it like `NEVER_WIDEN_HALF_REQUEST_SECCLASS_D04_UNCLASSIFIED_20261007.md` in the same folder. It names:
   - the one served key (`silver/bd_assets_dim.parquet`) and its readers;
   - both branches of the delta: the columns added, and every other column unchanged;
   - the rollback (the key's prior VersionId, read at the act);
   - the 22:11Z nightly as the timing input.
   Read-only reads of opal-data-bd are allowed (row W41-S1).

### AMENDMENT 1 (issuer, 2.0.0_SA_COO~M1, 2026-10-07 ~17:2xZ; release mode, CTO round-11 analysis @fc96f7c48c section 2 item 2)

**The release port.** e66 (build 9f533072d4, proof 0859b56dbf, ~48) is VALID on `secclass-r11-held-silver`, whose base still carries
the old S55. Its three files are re-staged onto the round head bba789b60b (S58-S61, origin-merged). Each is blob-equal to 0859b56dbf's,
and the round head left the builder and its tests unchanged since e66's base. BD silver passes 36.

Slot ~55 on branch `secclass-r12-rel-e66` commits that port. The issuer's lane refuses these paths.

**Your work:** the three files are ALREADY STAGED. Do not rebuild.
1. Confirm each blob equals 0859b56dbf's.
2. Commit them.
3. Run AC1, AC2 and AC3.
4. Write and validate the proof instance (slot ~55), flip status to complete, and commit.

### ACCEPTANCE

<criterion id="SC11-e66-AC1" cell_refs="SC-e-66"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/silver/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC11-e66-AC1` -- the BD silver suite, the new union test included, passes. The control at the base is 30 passed; your test makes it
the build check.

<criterion id="SC11-e66-AC2" cell_refs="SC-e-66"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/sc_e66_union_canonical.py</invocation><expect>SC-E66 ok=True</expect></criterion>
`SC11-e66-AC2` -- `build_union_dim()` names the three canonical columns and no longer freezes the column set. The check reads the tree
it is run from.

<criterion id="SC11-e66-AC3" cell_refs="SC-e-66"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SILVER_UNION_CANONICAL_20261007.md</invocation><expect>HALF-READY</expect></criterion>
`SC11-e66-AC3` -- the half request for the served file is ready to sign. A served key needs its pair; that is the third criterion's
reason.

<expected_criteria>SC11-e66-AC1,SC11-e66-AC2,SC11-e66-AC3</expected_criteria>

Dry-run at the base (cecc5f9013, 2026-10-07): SC11-e66-AC1 PASS as expected (control, 30 passed); SC11-e66-AC2 FAIL as expected (`canonical_cols_named=1/3 column_set_frozen_assert=True`); SC11-e66-AC3 FAIL as expected (NOT-READY: absent).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment;
  rows S49, S54).
- No upload, no S3 write, no SSM change, no deploy, no run of the builder without `--dry-run`. This is a shipped BD silver file, held
  off CLOUD until its half signs. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W55-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
data/black_diamond/scripts/silver/build_bd_assets_dim.py
data/black_diamond/scripts/silver/tests/test_assets_dim_union_canonical.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SILVER_UNION_CANONICAL_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R11.md</decomp_doc> (round 11), cell `SC-e-66`.
<owned_cells>SC-e-66</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC11-e66-AC1, SC11-e66-AC2, SC11-e66-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~55/MDPF_SECCLASS.TO-SC-e66.silver-union-canonical-columns.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC11-e66-AC1,SC11-e66-AC2,SC11-e66-AC3` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the union path before and after (file:line), the column set before and after, the fixture outcome, AC1-AC3 outputs, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the 22:11Z nightly (SSM opal-bd-asset-dim-download --union-bronze) is the release's timing input, named in the half request.
comp-iam: DECLARED-NOT-APPLICABLE no role or grant changes; the BD host already reads etf-classifications (TO-DEPLOY-e42 preflight).
comp-adversary: RUN -- W41-S4; a union that rewrites already-served derived values (step 3, and the test's kept-row arm); a second classifier (step 1 reuses the full-rebuild path's); BLIND: the next nightly's file (its pair's real run).
lane: the <paths> block IS the grant.
</preflight>

Source: round-10 analysis @a856d1525f section 2.4, section 3 item 7; row W41-S4; PRD v0.15 (ADMITTED); DECOMP_R11.
