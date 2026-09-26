# NFRA_MCPINDEX task order -- `MX-t-8` -- ROUND 2, E2: the portal purpose-built tools, reading the SAME precomputed objects the portal reads

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-t-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a build cell; no cron, alarm, monitor or cadence.
comp-iam: RUN at the cut (round-1 preflight carried): opal-gateway-role already reads opal-data-portal-v2 platinum/* and json/*; no firm-bucket grant; nothing new is granted here.
comp-adversary: DECLARED-NOT-APPLICABLE -- enrichment round of a thread.
EGRESS CLASS, declared: NONE. Tests use fixtures; no network.
</preflight>

## 1. THE CELL -- `MX-t-8` (round 2, decomposition section R2.1)

The round-1 portal analysis, `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~3/analysis-portal.result.md`
(READ AC5-AC8, AC11, AC12), measured the portal's precomputed objects in `opal-data-portal-v2`. It proposed 10
purpose-built tools (AC7): `mdpf_get_aum_metrics`, `mdpf_get_account_distribution`, `mdpf_get_aggregate_aua`,
`mdpf_get_category_views`, `mdpf_get_non_model_assets`, `etfs_get_positioning`, `advi_get_leaderboard`,
`advi_get_mix_summary`, `advi_get_partner_analytics`, `advi_get_growth_chart`. The advisor tools read ONLY
`platinum/advi/49financial/` in `opal-data-portal-v2`. The Inflection/Cottonwood firm buckets need a grant that does
not exist and are OUT of this cell.

Build **a new integration `portal_index`** (`app/integrations/portal_index/`) registering those tools:
1. Each reads ONE whole precomputed object, by its EXACT key prefix (the analysis's AC8 fence, exclusions kept), and
   never by bucket.
2. **A read aimed at a sibling property's prefix is refused.** This is the negative control (R-6, W4-S1).
3. **An absent or empty object answers "no data for that date",** never 0.
4. Every answer carries the object's own as-of date.
5. **Each tool declares its class** through MX-c-4's declaration, and **its catalog-entry reference** resolves to an
   entry in `app/refs/DATA_CATALOG.yaml`. Add the entries as emitter inputs under
   `workflows/atom_decomposition/catalog_entries/portal_*`, then regenerate the catalog with `emit_catalog_v02.py`.
   Never hand-edit it.
6. **Dormant by default**, the integrations standard's s.6: with `ENABLED_INTEGRATIONS` empty it adds zero tools; with
   its id set it adds exactly its pinned list. `validate_integration_spec` returns `[]`.
7. **R-7:** "model composition and weights" (which holdings, at what weights, make up a model) is either answered by one
   of these tools from a precomputed object, or named UNANSWERABLE from the portal's objects, with the reason, in your
   result.
8. **`tests/test_portal_index.py`** (new), with fixtures built from the analysis's measured shapes (no client name, full
   account number or balance), naming exactly:
   - `test_portal_tools_register_dormant_with_class`
   - `test_portal_tools_catalog_refs_resolve`
   - `test_portal_tool_reads_its_exact_prefix_only`
   - `test_sibling_prefix_is_refused`
   - `test_empty_partition_is_not_zero`
   - `test_parity_with_served_object` (for mdpf, etfs and 49financial advi: the tool's figure and as-of date equal the
     served object's own for one fixture, and a one-day date shift reports the mismatch)

**AMENDED after the first run (rows NFRA_MCPINDEX-Z-W3-S1, -S2, -S3, -S6):**
9. **The keys come ONLY from the catalog** (AMENDED AGAIN to the CTO's ruling D-5 = (c),
   `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/ROUND1_RULINGS.md` R-4 @3805559000, READ IT; the D-4
   waiver route is withdrawn, because `.tools/naming-gate.py` refuses a NEW literal before any waiver).
   - Each tool resolves its object key from its OWN existing catalog row, through `app/graphql_plumbing/catalog_gate.py`.
   - The module carries NO key literal, fragment or prefix: not `platinum/...`, and not the bucket-relative pieces.
   - Name the test `test_module_holds_no_key_literal`. It walks the module's AST for string constants and fails on any
     that is, or is part of, an `opal-data-portal-v2` key. It carries its own MUTANT arm: one planted key literal is
     caught.
   - The exact-prefix fence (item 1) and the sibling-prefix refusal (item 2) now hold over the keys the catalog
     yields.
10. **Enable-readiness, for this family AND the discover family:**
    - add the tool classes to `app/data_entitlement.py`, so neither the portal tools nor `opal_discover`/`opal_describe`
      are denied to everyone;
    - wire both factories in `app/integrations/registry.py`, so `ENABLED_INTEGRATIONS` can name them.
    Both stay dormant.
11. **The catalog regeneration** runs in this worktree with `portal/` checked out (the issuer provisions it).
12. **The pinned tool count moves with the tools** (row S10): update
    `tests/test_entitlement_admin.py::test_ogz2_ac08`'s pinned integration and tool counts to the new registry, as C2
    moves a pinned count with each tool. No other assertion in that file changes. ONE phase: commit the module and run
    the proof.

**AMENDED by the issuer after the second run (row NFRA_MCPINDEX-Z-W3-S11, no CTO ruling needed):**
13. **This cell registers ONLY the tools whose key `catalog_gate` resolves today:** `mdpf_get_aum_metrics`,
    `mdpf_get_account_distribution` and `mdpf_get_aggregate_aua`. These are the 3 of 10 you measured, all SAFE, prefix
    `platinum/mdpf/{scope}/`.
    - The other 7 leave this cell and go to the round-3 enrichment list as a catalog-row cell: category-views,
      etfs positioning, the four advi tools, and non-model-assets, whose catalog verdict `deny` stands. Do not add
      catalog rows for them.
    - Every item above now reads over the 3. `test_parity_with_served_object` covers the mdpf family only.
    - The pinned counts in item 12 move with the 3 tools plus the discover family.
    - Keep R-7's answer (UNANSWERABLE from the portal's objects, with your reason) in your result.
    - Keep the no-key-literal test and its mutant arm unchanged.

**Standing rules (R-6):**
- the interpreter is `python`;
- the prefix fence is item 1 and its control is item 2;
- the served file this cell writes is the catalog, and it is in your `<paths>`;
- if you run `validate_catalog_v02.py`, restore `catalog_v02/validation_report.json` before committing.

## 2. BOUNDS

1. Nothing is deployed and no served key is written. `integrations/schwab/` is never edited.
2. No private data in the repository: masked references and aggregate counts only.
3. Standing: no push, no install, no vendor call. A live READ of `opal-data-portal-v2` to confirm a key's shape is
   allowed through the `.tools/aws` shim. REFUSE a criterion you cannot meet as written, and report the refusal with
   its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/portal_index/
infra/aws/ec2/opal-gateway/tests/test_portal_index.py
workflows/atom_decomposition/catalog_entries/
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/integrations/registry.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~3/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Read (never write): `workflows/atom_decomposition/emit_catalog_v02.py`, `app/integrations/base.py`,
`app/integrations/registry.py`, `infra/logic/registry/systems.json`, `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md`.

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_MCPINDEX-Z-W3-S<k>`, fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-t-8"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/t8.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 2 of 2; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-t-8"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/t8.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 4 of 4; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-t-8"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/t8.AC3.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 1 of 1; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~3/NFRA_MCPINDEX.TO-MX-t-8.portal-tools.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once:
- the tools with their prefixes and classes;
- R-7's answer;
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E2 (S3, FWD-2, R-7). SPAWN ONLY after MX-c-5 is complete ON the held branch. Cut the worktree from
`wk-nfra_mcpindex-1-1d`'s head; the issuer merges this branch back INTO the held branch. The catalog regeneration can
conflict with MX-d-2's; resolve by re-running the emitter at the merge (the round-1 bound).

<status>pending</status>
<round>2</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
