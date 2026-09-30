# NFRA_MCPINDEX task order -- `MX-t-12` -- a catalog row and a purpose-built read-only tool for platinum/advi -- HELD on Andrew's widening word (G-W)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-t-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~20</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only tool in an existing integration.
comp-iam: DECLARED-NOT-APPLICABLE -- the gateway role already reads opal-data-portal-v2 platinum/*.
comp-adversary: DECLARED-NOT-APPLICABLE -- the mdpf tool pattern, ruled.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 reads).
</preflight>

## 1. THE CELL -- `MX-t-12` (round 5; `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/REINSTATE_RULINGS_20260930.md` @4e598ab7be, order item 5)

**HELD:** this cell holds on G-W, Andrew's word to widen the catalog to `platinum/advi` (DATA_CATALOG.yaml:32,
"WIDENING IS ANDREW-ONLY"). His last word is NOT YET: "stays in `refused_units` until its W4b certification window
closes" (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_212xZ_O_FABRIC_OPEN_CALLS_ANSWERED.md:71-72`).
1.0.0_SA_CTO~O ruled it HELD in this round (msg 27022). The cell is issued with the round so the issuance covers
every cell, but no worker is spawned on it until the gate stands. A worker who finds the gate NOT standing files a
BLOCKING row and stops; it never works around the gate.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-30 ~13:1xZ) -- G-W STANDS for `platinum/advi`; this cell is RELEASED.**
- Andrew's word, verbatim, relayed by 1.0.0_SA_CTO~O (msg 27162), record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_13xxZ_R20_ETFS_BDFEES_YES_SCHWAB_GRANT_YES_ADVI_LIFTED.md` @1eba868308: "whatever needs to be lifted should be
  lifted". That lifts his "platinum/advi NOT YET" hold.
- **The catalog version bump that adds the advi row carries his verbatim and cites @1eba868308**, as DATA_CATALOG.yaml:32
  requires. It goes in the emitter's header text, never as a hand edit of the catalog.
- **Scope limit, unchanged:** `platinum/advi/49financial/` only. The firm scope is the key segment (C7), and a firm
  principal resolves only its own scope.
- **If the naming limb refuses the served key** as it refused `platinum/etfs` (row Z-W15-S5), file a BLOCKING row and
  stop. Andrew's R20 acknowledgement covers etfs and BD fees only, not advi, so do not work around it.
- Graded by: no gate limb graded this modification (to-pipeline-gate LIMB 6 grades only a newly-added order; GATE (viii)
  finds `<placeholders>NONE</placeholders>`).

**The act, on the portal_index pattern** (`infra/aws/ec2/opal-gateway/app/integrations/portal_index/`; read its mdpf
tools and MX-t-10's ETF tool first):
1. The surface is the advisor-intelligence page's served objects. `portal-page-advisor-intelligence` sits in the
   catalog's `refused_units`. Certify and add its row first, through the emitter's source; the version bump carries
   Andrew's verbatim word.
2. One read-only tool. It reads ONE whole object whose key comes from its own catalog row, through `catalog_gate`, and
   answers with the object's own as-of date. It is a new `ROWS` entry whose `catalog_ref` names a `portal_datasets` row
   carrying `read_tool` + `accessor`, added through `catalog_entries/` and the emitter, never a hand edit. Classify it
   SAFE and add it to `app/data_entitlement.py` `INDEX_TOOLS`.
3. The answer carries the row's own caveats. It is firm-scoped as the row declares; a firm principal resolves only its own scope.
4. Prove the figure in-process against the served object and by VersionId; record both in `EQUALITY_MX-t-12.md`.
5. Tests in `tests/test_portal_index.py`. Run AC1 and AC2, and commit.

## 2. BOUNDS

1. Nothing is deployed; it rides the next release after the gate stands.
2. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/portal_index/
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/tests/test_portal_index.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/catalog_entries/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~20/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W20-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-t-12" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/t12.AC1.sh; echo "exit=$?"</invocation><expect>placed and naming their reader N of N with N>=6 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-t-12" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/t12.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; passed>7; failed/error 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~20/NFRA_MCPINDEX.TO-MX-t-12.portal-tool-advi.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-5 order item 5, carried from MX-t-11 (superseded @a120fec68b). HELD on G-W
per 1.0.0_SA_CTO~O msg 27022; lifting it is Andrew's act alone (the MX-t-11 widening word on his list). Not spawned.
Dry-run at base: t12.AC1 FAIL (rows < 6).

<status>pending</status>
<round>5</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
