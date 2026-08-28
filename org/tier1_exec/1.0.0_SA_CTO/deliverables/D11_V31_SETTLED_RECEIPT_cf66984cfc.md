# D11 / NFRA_SUBSTRATECARDING -- THE SETTLED v3.1 REVALIDATION RECEIPT (KEYFILL boundary step 2, issuer ruling 79178)

**Issued by** 1.0.0_SA_CTO~X (schema owner) at 2026-08-28T23:59:00Z -- REPORT-ONLY, no byte written to any card.
**SETTLED PIN** = cf66984cfc39e7f45c0799c75be43c4ec1fb7934 (0.4.0_DT_ClientPlatform~X, 2026-08-28T23:55:26Z) -- the LAST of the three re-stamp commits: f58b008944 (CTO~X, CloudComp 43) -> d3b3461318 (AE~X, CloudOps 11) -> cf66984cfc (DT~X, 18). Preceded by the cut @baae9a766a (tool + derived schema).
**Tree read** at HEAD 95775d3e8bb0d5c4be9092c9c8365821b21174b8; is-ancestor of HEAD: cf66984cfc YES, d3b3461318 YES, f58b008944 YES, baae9a766a YES; `git diff --stat cf66984cfc HEAD` over the three card roots + the v3.1 schema = 0 lines (0 = the tree read IS the settled pin for every input).
**Instrument** org/standards/migrate_substrate_card_v3_to_v3_1.py sha256(LF) 53e12a5104ebd735 -- with the settled-mode fix (an already-3.1 card is validated AS v3.1 and runs the three findings; never re-stamped); schema org/standards/SUBSTRATE_CARD.v3.1.schema.json sha256(LF) 19a3547047b750c8. Self-test (CRO incomplete-map falsifier) PASS at the head of the run.

## Receipt (stdout, verbatim)

```
self-test: PASS -- incomplete-map falsifier discriminates (confirmed=inferred vs declared-only=measured); complete map agrees under both
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-bcin__org_tier2_senior_0.4.0_DS_ClientPlatform_deliverables_motif_c2c3_mater.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-coth__kuzu_nessie_db.json
PASS           prose=disch floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-hffm__org_tier1_exec_3.0.0_SA_CVO_deliverables_kimi_subdivision_harness_c2_i.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-jgzc__data_firm_registry.json.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-lqzx__.comp-graph_graph.json.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-nthk__org_tier1_exec_3.0.0_SA_CVO_deliverables_kimi_subdivision_harness.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-pcac__org_modules_graph_keep-dormant.yaml.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-qvzv__org_tier2_senior_0.4.0_DS_ClientPlatform_deliverables_motif_c2c3_mater.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-rpcx__comp-heat.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-ukdh__org_modules_graph_nerves-edges.json.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-uvcz__org_modules_graph_nerves-risk-edges.json.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-vlov__opal-313476888478-globgrph_warehouse_globgrph_graph_edges_6629328d-a58.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-xnwo__opal-313476888478-globgrph_warehouse_globgrph_graph_nodes_4c6c23bd-fff.json
PASS           prose=disch floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-xzjx__org_tier1_exec_3.0.0_SA_CVO_deliverables_kimi_subdivision_harness_c3_s.json
PASS           prose=n/a   floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-yjky__opal-estate-report_kuzu_nessie_db.json
PASS           prose=clean floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W2\W2-znom__infra_system_ontology_SYSTEM_DEFINITIONS.yaml.json
PASS           prose=disch floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W3\W3-gkih__infra_aws_globgrph_kuzu_load_py.json
PASS           prose=disch floor=ok      0.4.0_DT_ClientPlatform~X    org\tier2_senior\0.4.0_DT_ClientPlatform\deliverables\D11_CARDS_W3\W3-mdiu__infra_aws_globgrph_kuzu_stitch_load_py.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-dmua_mdpf_delivery_cadence_contract.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-dxxm_c0_c1_rung_boundary.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-fwhj_c1_frontend_adapter.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-hzfk_relations.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-idsf_node_bindings.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-igwg_native_cloudedge_direction.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-iivv_pstmrt_completeness_and_trigger_layer.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-kwjy_live_graph_edge_types.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-mqju_c2_motif_families.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-pzkj_non_relation_edges.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-qgtd_graph_contracts.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-uyan_roles.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W2\W2-yoyi_relation_composites.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W3\W3-bsft_derive_runner_PATH_A_graph_nodes_edges.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W3\W3-bzgw_cse_emit_frontend_coevolution_PATH_B_s3_watermark.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W3\W3-csnj_derive_runner_PATH_B_graph_contracts.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W3\W3-dljc_cse_emit_frontend_coevolution_PATH_A_local_jsonl.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W3\W3-ggoq_comp_aws_cli_iceberg_commit.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W3\W3-thav_incremental_updater_PATH_A_iceberg_nessie.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W3\W3-uuxp_incremental_updater_PATH_B_s3_branch_head_marker.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-_comp-graph_baseline_json.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-_comp-graph_managed_policy_actions_cache_json.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-_comp-graph_pathrooting-census_json.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-_comp-graph_pydeps_json.card.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-axes_history_jsonl.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-c2_instances_json.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-c3_structures_json.card.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-dncq_build_manifest_json_SET.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-estate-coverage-resolver_json.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-kuzu_ac7_db.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-kuzu_ac7_dir.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-kuzu_db.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-kuzu_nessie_db_fallback_jsonl.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-kuzu_nessie_db_local.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-kuzu_stitch_db.card.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~Y         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-lgbr_platinum_CACHE_SET.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-motif_c2c3_materialize_ab_json.card.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-motif_c2c3_materialize_json.card.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-nerves-edges_json.card.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-nerves-risk-edges_json.card.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-nerves_resolve.card.json
PASS           prose=disch floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-snap_store_WRITER.card.json
PASS           prose=clean floor=ok      0.8.0_AE_CloudComp~X         org\tier2_senior\0.8.0_AE_CloudComp\deliverables\D11_CARDS_W4\W4-stitch_graph_json.card.json
PASS           prose=clean floor=ok      0.7.0_AE_CloudOps~X          org\tier2_senior\0.7.0_AE_CloudOps\deliverables\D11_CARDS_W2\anchor_catalog.json
PASS           prose=disch floor=ok      0.7.0_AE_CloudOps~X          org\tier2_senior\0.7.0_AE_CloudOps\deliverables\D11_CARDS_W2\baked_static_spec_layers.json
PASS           prose=clean floor=ok      0.7.0_AE_CloudOps~X          org\tier2_senior\0.7.0_AE_CloudOps\deliverables\D11_CARDS_W2\comp_debris.json
PASS           prose=disch floor=ok      0.7.0_AE_CloudOps~X          org\tier2_senior\0.7.0_AE_CloudOps\deliverables\D11_CARDS_W2\comp_ladder.json
PASS           prose=disch floor=ok      0.7.0_AE_CloudOps~X          org\tier2_senior\0.7.0_AE_CloudOps\deliverables\D11_CARDS_W2\dup_scan.json
PASS           prose=clean floor=ok      0.7.0_AE_CloudOps~X          org\tier2_senior\0.7.0_AE_CloudOps\deliverables\D11_CARDS_W2\resource_summaries.json
PASS           prose=disch floor=ok      0.7.0_AE_CloudOps~X          org\tier2_senior\0.7.0_AE_CloudOps\deliverables\D11_CARDS_W2\summary_corpus.json
PASS           prose=disch floor=ok      0.7.0_AE_CloudOps~X          org\tier2_senior\0.7.0_AE_CloudOps\deliverables\D11_CARDS_W3\cse_store__PATH_A_append.json
PASS           prose=disch floor=ok      0.7.0_AE_CloudOps~X          org\tier2_senior\0.7.0_AE_CloudOps\deliverables\D11_CARDS_W3\cse_store__PATH_B_drop.json
PASS           prose=disch floor=ok      0.7.0_AE_CloudOps~X          org\tier2_senior\0.7.0_AE_CloudOps\deliverables\D11_CARDS_W3\resource_summaries_store.json
PASS           prose=disch floor=ok      0.7.0_AE_CloudOps~X          org\tier2_senior\0.7.0_AE_CloudOps\deliverables\D11_CARDS_W3\snap_store.json

RECEIPT: seen 80 | v3 0 | already v3.1 72 | not v3 8 | PASS 72 | REFUSED-enum 0 | REFUSED-other 0 | delta prose present 30 (discharged in place 30, LIVE false claim 0) | scalar UNDERSTATES true-MIN floor 0 | unbased valued sub-claim 0 | report only (no byte written)
  owner 0.4.0_DT_ClientPlatform~X: {'already': 18, 'PASS': 18, 'prose_present': 4, 'prose_discharged': 4}
  owner 0.7.0_AE_CloudOps~X: {'not_v3': 2, 'already': 11, 'PASS': 11, 'prose_present': 8, 'prose_discharged': 8}
  owner 0.8.0_AE_CloudComp~X: {'not_v3': 3, 'already': 30, 'PASS': 30, 'prose_present': 10, 'prose_discharged': 10}
  owner 0.8.0_AE_CloudComp~Y: {'not_v3': 3, 'already': 13, 'PASS': 13, 'prose_present': 8, 'prose_discharged': 8}
```
