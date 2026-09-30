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

**The act:**
1. A new integration `black_diamond` at `infra/aws/ec2/opal-gateway/app/integrations/black_diamond/`, registered in
   `app/integrations/registry.py` like the dormant schwab factory (:51-55). It stays DORMANT: it is not added to
   `ENABLED_INTEGRATIONS`; MX-r-7 enables it.
2. **One fenced read role (PRD C7).** `infra/aws/terraform/opal-gateway/bd_reader_iam.tf`, on the pattern of
   `schwab_reader_iam.tf`: a role the gateway role may assume under its own ExternalId, an Allow on exactly the record's
   read-fence prefixes, and an explicit Deny on every other prefix of the bucket. The tool reads only through that role.
   Nothing is applied; `terraform validate` at most.
3. **The tool.** Read-only, C3-valid name starting `bd_`, typed arguments, scope as an argument. A principal resolves
   only its own firm by the record's `Scope rule`, and the tool never reads across firms. Every answer carries the
   source's own as-of date and the record's caveats and never-sum rules.
4. **C2, in full.** A catalog row whose `read_tool` names the tool, added through `workflows/atom_decomposition/catalog_entries/`
   and the emitter `workflows/atom_decomposition/emit_catalog_v02.py`, never a hand edit of `DATA_CATALOG.yaml`. Tag it
   SAFE, enter it in `app/destructive_ops.py` and `app/data_entitlement.py`, and move the pinned tool-count tests only
   if your change moves them.
5. Tests in `tests/test_black_diamond.py` with exactly these names: `test_mx_t13_tool_registered_safe`,
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
infra/aws/ec2/opal-gateway/app/integrations/black_diamond/
infra/aws/ec2/opal-gateway/app/integrations/registry.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/ec2/opal-gateway/tests/test_black_diamond.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
infra/aws/terraform/opal-gateway/bd_reader_iam.tf
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
  <criterion id="AC1" cell_refs="MX-t-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/t13.AC1.sh; echo "exit=$?"</invocation><expect>registry names black_diamond=True; catalog rows naming a bd_* black_diamond function 1 or more -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-t-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/t13.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 4 of 4; failed/error tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~21/NFRA_MCPINDEX.TO-MX-t-13.bd-first-tool.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Reinstatement ruling B5 and round-5 order item 4. Orion, Eclipse and SmartX follow
this pattern in later rounds. Dry-run at base: t13.AC1 FAIL (no black_diamond integration), t13.AC2 FAIL (file absent).

<status>pending</status>
<round>5</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
