# NFRA_MCPINDEX task order -- `MX-t-10` -- a catalog row and a purpose-built read-only tool for platinum/etfs -- HELD on Andrew's widening word

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-t-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~15</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only tool in an existing integration.
comp-iam: DECLARED-NOT-APPLICABLE -- the gateway role already reads opal-data-portal-v2 json/* and platinum/*.
comp-adversary: DECLARED-NOT-APPLICABLE -- the mdpf tool pattern, ruled.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 reads).
</preflight>

## 1. THE CELL -- `MX-t-10` (round 4; `org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round3.md` @f354170b42)

**HELD:** this cell holds on G-W, Andrew's word to widen the catalog to `platinum/etfs` (DATA_CATALOG.yaml:32, "WIDENING IS ANDREW-ONLY"). It is issued with the round, so the issuance covers every cell, but no worker is spawned on it until the gate stands. A worker who finds the gate NOT standing files a BLOCKING row and stops; it never works around the gate.

**Why.** FWD-2 is "portal figures equal the portal's". Round 3 proved `platinum/mdpf` end to end. `platinum/etfs`
has no purpose-built tool, so its question went unanswered in the close run.

**The act, on the portal_index pattern** (`infra/aws/ec2/opal-gateway/app/integrations/portal_index/`; read its three
mdpf tools first):
1. The surface is `platinum/etfs/**`. The catalog holds NO row for it, so first add the catalog row with its verdict, keywords and caveats, through the emitter's source. That widens the served surface, which is why this cell is HELD.
2. One read-only tool. It reads ONE whole object whose key comes from its own catalog row, through `catalog_gate`, and
   answers with the object's own as-of date. It is a new `ROWS` entry whose `catalog_ref` names a `portal_datasets`
   row carrying `read_tool` + `accessor`, added through `catalog_entries/` and the emitter, never a hand edit.
   Classify it SAFE, like the others.
3. The answer carries the row's own caveats. It is firm-scoped as the catalog row declares, and a firm principal resolves only its own scope.
4. **Prove the figure.** Call the tool in-process, read-only, against the served object. Read the same key by
   VersionId with `aws s3api get-object`. Record in `EQUALITY_MX-t-10.md`: the headline figure and as-of on both
   sides, and the VersionId. It is graded live at MX-r-5's r5.J1.
5. Tests in `tests/test_portal_index.py`. Run AC1 and AC2, and commit.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-29 ~05:2xZ) -- G-W STANDS for `platinum/etfs`; this cell is RELEASED.**
- Andrew's word, relayed by 1.0.0_SA_CTO~O (msg 26446): "self-drive says adjudicate all open calls. Go with your
  recs." The record is `org/tier1_exec/1.0.0_SA_CTO/deliverables/` @dc75ddbe32: platinum/etfs YES; platinum/advi NOT
  YET.
- **The catalog version bump that adds the ETF row carries his verbatim and cites @dc75ddbe32**, as DATA_CATALOG.yaml:32
  requires ("Version bumps carry his verbatim"). Put it in the emitter's header text, never a hand edit of the
  catalog.
- Per-firm visibility is unchanged: the row's firm_scope is declared, and a firm principal resolves only its own
  scope.
- **Start after MX-t-9 is complete and drained.** The issuer continues you with this order. Both cells write
  portal_index and the catalog.
- Once this row lands, MX-d-5's AC2 grades the ETF ask as ROUTED to a platinum/etfs row first. The check already
  covers both states.

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-09-29 ~06:4xZ), on row Z-W15-S2 (ARMED, issuer-owned) -- the new tools must be ENTITLED.**
- `infra/aws/ec2/opal-gateway/app/data_entitlement.py` `INDEX_TOOLS` names only the 3 original mdpf tools, so
  `classify` returns None for any new portal_index tool, and it is DENIED to every principal once enabled.
- **Granted:** add `mdpf_get_model_benchmarks` (MX-t-9's) and this cell's ETF tool to `INDEX_TOOLS`, exactly those two
  names and no other change.
- Prove it: a test in `tests/test_portal_index.py` (or the entitlement test) asserts both new names classify like the
  existing three, and the 4th tool's relaxed assertion from MX-t-9 is restored to the strict form.
- The pre-existing failures `test_ogz1_ac05` and `test_ogz1_ac08` (test_data_entitlement_guard.py): baseline them on
  CLOUD and report whether they also fail there. Do not fix them unless your change caused them.

## 2. BOUNDS

1. Nothing is deployed; the release is MX-r-5 or a later round.
2. The widening happens only with Andrew's recorded word.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/portal_index/
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/tests/test_portal_index.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/catalog_entries/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~15/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W15-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-t-10" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/t10.AC1.sh; echo "exit=$?"</invocation><expect>placed and naming their reader N of N with N>=5 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-t-10" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/t10.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; passed>7; failed/error 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~15/NFRA_MCPINDEX.TO-MX-t-10.portal-tool-etfs.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-3 analysis s.5 item 3b. RESERVED: DATA_CATALOG.yaml:32 "WIDENING IS ANDREW-ONLY, unchanged. Version bumps carry his verbatim." The card went to 1.0.0_SA_CTO~O at ~04:36Z (MSTR~Z has no live session). HELD until Andrew's word is recorded.

<status>pending</status>
<round>4</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
