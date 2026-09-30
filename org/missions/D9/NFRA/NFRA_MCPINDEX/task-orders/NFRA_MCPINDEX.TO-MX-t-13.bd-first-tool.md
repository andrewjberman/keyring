# NFRA_MCPINDEX task order -- `MX-t-13` -- Black Diamond's first catalog row and read-only tool, behind one fenced read role, cut from MX-a-8's record

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-t-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~21</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: RUN -- 2026-09-30 ~08:4xZ by the issuer: `comp-iam role opal-gateway-role` shows sts:AssumeRole under the schwab ExternalId condition; `comp-iam role gateway-schwab-read-role` returns no match (its TF index does not resolve the reader role by name), so the APPLIED plane was read directly: simulate-principal-policy on gateway-schwab-read-role -> dim_position allowed, dim_transaction explicitDeny. This cell writes a NEW Black Diamond reader role, exact-prefix Allow from MX-a-8's read fence, deny else (C7); NOT applied here -- the apply is MX-r-7.
comp-adversary: DECLARED-NOT-APPLICABLE -- the Schwab reader-role and portal_index tool patterns.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (STS assume + S3 reads).
</preflight>

## 1. THE CELL -- `MX-t-13` (round 5; `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/REINSTATE_RULINGS_20260930.md` @4e598ab7be, ruling B5)

**Start after MX-a-8 is complete and drained.** The issuer continues you with this order. You build exactly the ONE
tool the record's `Question to tool` section names, over exactly its `Read fence`.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-30 ~09:3xZ) -- on row Z-W21-S1 (ARMED, issuer-owned), ruled by row Z-S62.**
- `bd` is refused in every naming slot (`infra/logic/registry/scopes.json`); the systems key is `blackdiamond`. So the
  integration id is `blackdiamond` (`app/integrations/blackdiamond/`), the tool prefix is `blackdiamond_`, and the test
  file is `tests/test_blackdiamond.py`. The `<paths>` block and t13.AC1/AC2 are amended to match.
- The tool is MX-a-8's `blackdiamond_list_fees` (record @4be9c0bb0a,
  `deliverables/0.9.0_WK_NFRA_MCPINDEX~21/analysis-blackdiamond.r5.result.md`). Its read fence is
  `s3://opal-data-bd/silver/fees/` only. Its scope argument is `49financial`. It refuses the whole answer if any returned
  `account_id` does not start with `z08`, and `test_mx_t13_scope_fenced` proves that refusal.
- Graded by: no gate limb graded this modification (to-pipeline-gate LIMB 6 grades only a newly-added order; GATE (viii)
  finds `<placeholders>NONE</placeholders>`).

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-09-30 ~11:0xZ) -- on row Z-W21-S9 (BLOCKING), ruled by row Z-S64.**
- The naming limb refuses the literals `opal-data-bd`, `silver/fees/` and `49financial` in the integration and
  `blackdiamond_reader_iam.tf`. `lookup('49financial')` resolves to a bucket that holds no fees, so the builder cannot
  name this legacy surface. The surface is under the live ADVI_FIRMBKTS remediation (`infra/logic/registry/remediations.json`).
- The lawful route is the LEGACY-READ waiver (`.tools/naming-gate.py:99-110,942-1180`, carrier
  `org/standards/NAMING_LEGACY_READS.json`). Its authority is a ruling record at a full pin, asked of 1.0.0_SA_CTO~O.
- **This continuation, before that ruling:**
  - Restructure so each literal is legal under the waiver's syntax. In Python, every occurrence of each literal is a
    DIRECT argument of calls to ONE named read helper; no module constant, f-string or variable carries it. In
    Terraform, each literal is the value of exactly ONE `locals` entry, referenced N times.
  - Keep t13.AC1/AC2 passing. Draft the carrier entries (fields exactly `id, file, literal, remediation, purpose,
    authority, as_of_cutoff, owner, read_context`; a helper site's `helper_body_sha256`; a tf site's kind `tf_local`)
    in `deliverables/0.9.0_WK_NFRA_MCPINDEX~21/LEGACY_READS_DRAFT_MX-t-13.json`, with `authority` left for the ruling.
  - Report and stop.
- The issuer writes the carrier entries once the CTO's record is at HEAD, and continues you to commit.
- Graded by: no gate limb graded this modification (to-pipeline-gate LIMB 6 grades only a newly-added order; GATE (viii)
  finds `<placeholders>NONE</placeholders>`).

**AMENDED A3 (2.0.0_SA_COO~MI, 2026-09-30 ~11:2xZ) -- HELD on R20, on 1.0.0_SA_CTO~O's ruling msg 27114.** The naming gate marks a literal NEW when it is absent from the file's HEAD pre-image (`.tools/naming-gate.py:1413`) and refuses a NEW OUT-OF-PATTERN/ALIAS literal before the LEGACY-READ lookup (:1444-1449, "a NEW or CHANGED literal can never reach it"). So no waiver entry can admit this cell's literals. The cell joins B3: both go to Andrew as ONE R20 acknowledgement (CLAUDE.md rule 30). The built cell stays UNCOMMITTED and frozen in `wk-mcpindex-r5-21` (branch wk-nfra_mcpindex-5-21 @4a9462b79a; AC1/AC2 PASS on the uncommitted tree; draft carrier LEGACY_READS_DRAFT_MX-t-13.json no longer needed). The A2 restructure stops. On Andrew's word the issuer continues ~21 to commit it as-is and MX-r-7 follows. Graded by: no gate limb graded this modification.

**The act:**
1. A new integration `blackdiamond` at `infra/aws/ec2/opal-gateway/app/integrations/blackdiamond/`, registered in
   `app/integrations/registry.py` like the dormant schwab factory (:51-55). It stays DORMANT: it is not added to
   `ENABLED_INTEGRATIONS`; MX-r-7 enables it.
2. **One fenced read role (PRD C7).** `infra/aws/terraform/opal-gateway/blackdiamond_reader_iam.tf`, on the pattern of
   `schwab_reader_iam.tf`: a role the gateway role may assume under its own ExternalId, an Allow on exactly the record's
   read-fence prefixes, and an explicit Deny on every other prefix of the bucket. The tool reads only through that role.
   Nothing is applied; `terraform validate` at most.
3. **The tool.** Read-only, C3-valid name starting `blackdiamond_`, typed arguments, scope as an argument. A principal resolves
   only its own firm by the record's `Scope rule`, and the tool never reads across firms. Every answer carries the
   source's own as-of date and the record's caveats and never-sum rules.
4. **C2, in full.** A catalog row whose `read_tool` names the tool, added through `workflows/atom_decomposition/catalog_entries/`
   and the emitter `workflows/atom_decomposition/emit_catalog_v02.py`, never a hand edit of `DATA_CATALOG.yaml`. Tag it
   SAFE, enter it in `app/destructive_ops.py` and `app/data_entitlement.py`, and move the pinned tool-count tests only
   if your change moves them.
5. Tests in `tests/test_blackdiamond.py` with exactly these names: `test_mx_t13_tool_registered_safe`,
   `test_mx_t13_catalog_gated`, `test_mx_t13_scope_fenced` (another firm's key is refused), and
   `test_mx_t13_answer_carries_as_of`.
6. **Prove the figure.** Call the tool in-process against one live object under your own read credentials, read the
   same key by VersionId with `aws s3api get-object`, and record both in `EQUALITY_MX-t-13.md`. Run AC1 and AC2, and commit.

## 2. BOUNDS

1. Nothing is deployed or applied; the release is MX-r-7.
2. No identity, grant or sign-in change. A new data role is not an identity path; per-principal grants stay as they are.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/blackdiamond/
infra/aws/ec2/opal-gateway/app/integrations/registry.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/ec2/opal-gateway/tests/test_blackdiamond.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
infra/aws/terraform/opal-gateway/blackdiamond_reader_iam.tf
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/catalog_entries/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~21/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W21-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-t-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/t13.AC1.sh; echo "exit=$?"</invocation><expect>registry names blackdiamond=True; catalog rows naming a blackdiamond_* blackdiamond function 1 or more -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-t-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/t13.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 4 of 4; failed/error tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~21/NFRA_MCPINDEX.TO-MX-t-13.bd-first-tool.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Reinstatement ruling B5 and round-5 order item 4. Orion, Eclipse and SmartX follow
this pattern in later rounds. Dry-run at base: t13.AC1 FAIL (no black_diamond integration), t13.AC2 FAIL (file absent).

<status>complete -- issuer-graded on CLOUD after the drain @d3b0efe5c6 by 2.0.0_SA_COO~MI, 2026-09-30 ~23:5xZ: t13.AC1 PASS (1 of 1 blackdiamond_* catalog row), t13.AC2 PASS (4 of 4), instance VALID. blackdiamond_list_fees (dormant), reader role blackdiamond_reader_iam.tf (not applied); the 5 literals admitted under R20 X12 (entries R20-04..08 @0d71a22887, Andrew's word @1eba868308); equality re-proved on silver/fees/2026-09-29. Released by MX-r-7. Was: pending.</status>
<round>5</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
