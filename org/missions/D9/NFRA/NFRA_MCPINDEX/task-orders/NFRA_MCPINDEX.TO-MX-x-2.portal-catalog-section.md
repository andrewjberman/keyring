# NFRA_MCPINDEX task order -- `MX-x-2` -- the portal_* catalog rows get their own emitter section, carrying the exact S3 key each describes (row Z-W3-S4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-x-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~13</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a catalog emitter + reader change; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- a measured schema defect (row Z-W3-S4).
EGRESS CLASS, declared: NONE. Offline code and tests only.
</preflight>

## 1. THE CELL -- `MX-x-2` (round 3, enrichment item 6, part 2)

**The defect (row Z-W3-S4).** `workflows/atom_decomposition/emit_catalog_v02.py` (:813-831) emits every
`workflows/atom_decomposition/catalog_entries/<entity>.yaml` under `silver_datasets:`. Its header says "no S3 key, no
precomputed artifact; each row is resolved live". The C1 schema has exactly 8 fields and no key field. Three of those
entries are `portal_*` rows: portal datasets that ARE precomputed served objects. So they sit under a header that
describes them wrongly, and the exact key each describes lives only in prose (`producer`) and in the integration's
FENCES, not in a field a consumer can reject on.

**The fix:**
1. The emitter writes `portal_*` entities to their own top-level section `portal_datasets:`. Its header states what
   they are: precomputed objects the portal serves, each resolved by its exact key. Each row carries every C1 field
   plus `s3_key`, the exact key the entry describes, taken from the source entry file. Add `s3_key` to each `portal_*`
   source file under `catalog_entries/`. The value is the key the `portal_index` integration already fences for that
   entity; read it there, never guess it.
2. `silver_datasets:` keeps its header and holds only non-portal entities.
3. The reader moves with the data: `infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py:166` reads
   `portal_datasets`. Its tests in `tests/test_portal_index.py` pass.
4. REGENERATE `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` by running the emitter
   (`cd workflows/atom_decomposition && python emit_catalog_v02.py`). The emitter takes no arguments and writes the
   catalog IN PLACE, so run it only in your worktree. Never hand-edit the catalog.
5. Check that `catalog_gate` and `validate_catalog_v02.py` still accept the catalog; find both with `comp-which`. If
   either refuses the new key, STOP and file a BLOCKING row. Do not widen them. If `validate_catalog_v02.py` rewrites
   `catalog_v02/validation_report.json`, restore that file before you commit.
6. Run AC1-AC3. Commit under your serial.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-28 ~22:0xZ), on the CTO ruling of row Z-W13-S3 (`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/RULING_Z-W13-S3_Z-W9-S1_20260928.md` @8ed938b2d7):**
- **NO `s3_key` field anywhere.** A catalog line stating a served address is a second hand-kept copy of the key
  (Rule 30), and the naming gate's legacy-read waiver cannot admit a YAML line.
- **Instead, each `portal_*` row names WHERE it is read,** in two fields:
  - `read_tool`: the portal_index tool;
  - `accessor`: the portal accessor whose channel row carries the key.
  Both must equal that entity's entry in `portal_index/integration.py`'s `ROWS` (tool name, then `ToolRow`'s
  accessor), e.g. `read_tool: mdpf_get_aum_metrics`, `accessor: getAUMMetricsByFirm`.
- Put them in the three `catalog_entries/portal_mdpf_*.yaml` source files, and have the emitter carry them into
  `portal_datasets:` in place of `s3_key`. The section header says the key is resolved by that tool through that
  accessor's channel row.
- Everything else in section 1 stands: the section, the reader move, the regeneration, the gates.
- If a consumer genuinely needs the raw key from the catalog, do not add it. File a row naming that consumer and its
  line.
- AC1 is re-issued (section 4) to grade exactly this. Your uncommitted `s3_key` work in the worktree is the thing to
  change.

## 2. BOUNDS

1. Nothing is deployed. The catalog changes only through the emitter.
2. The `channels:` rows and every other integration are unchanged.
3. No AWS, no push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/catalog_entries/
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/ec2/opal-gateway/app/integrations/portal_index/
infra/aws/ec2/opal-gateway/tests/test_portal_index.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~13/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W13-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-x-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/x2.AC1.sh; echo "exit=$?"</invocation><expect>placed and naming their reader N of N with N>=3 (no s3_key) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-x-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/x2.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; passed>=1; failed/error 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-x-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/x2.AC3.sh; echo "exit=$?"</invocation><expect>emitter rc=0; differing lines outside the build stamp: 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~13/NFRA_MCPINDEX.TO-MX-x-2.portal-catalog-section.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-2 analysis s.5 item 6 @e4445020f5 (Z-W3-S4). See MX-x-1's notes for the split.
- Dry-run at base: x2.AC1 FAIL (3 portal rows, all under silver_datasets, 0 keyed); x2.AC2 PASS (7 passed; a guard);
  x2.AC3 PASS (the emitter reproduces the committed catalog outside the build stamp).
- x2.AC3 backs up and restores the catalog bytes itself. The issuer measured the hazard it guards: a bare
  `emit_catalog_v02.py --help` rewrote the tracked catalog's stamp at 20:5xZ. It was restored the same minute with
  `git checkout`, and the diff was 2 stamp lines.
- Release: this changes gateway files, so they ship only through a narrow release. MX-r-4 carries them if this drains
  before its cut.

<status>complete -- issuer-graded on CLOUD after the drain @ac96f4ae3e by 2.0.0_SA_COO~MI, 2026-09-28 ~22:1xZ, as amended A1: x2.AC1 PASS (3 of 3 portal rows in portal_datasets naming read_tool + accessor equal to portal_index ROWS, no s3_key), x2.AC2 PASS (7 passed), x2.AC3 PASS (the emitter reproduces the catalog outside the stamp), instance VALID; the naming gate reads PASS. Rows Z-W13-S1/S2 are INERT observations; Z-W13-S3 is ruled @8ed938b2d7. Was: pending.</status>
<round>3</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
